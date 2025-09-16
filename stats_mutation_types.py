#!/usr/bin/env python3
import subprocess
import re
import os
from pathlib import Path
from collections import defaultdict

ROOT = Path('.').resolve()
DIFFS_DIR = ROOT / 'mutant_diffs'
STATS_CSV = ROOT / 'mutation_type_stats.csv'
FAILURE_LOG = ROOT / 'mutant_diff_failures.log'

def run(cmd):
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out_combined = (p.stdout or '') + (p.stderr or '')
    return p.returncode, out_combined

def parse_results(txt):
    res = {}
    for line in txt.splitlines():
        line = line.strip()
        m = re.match(r'([A-Za-z0-9_.]+__mutmut_(\d+))\s*:\s*(\w+)', line)
        if m:
            full_key = m.group(1)
            status = m.group(3).lower()
            res[full_key] = status
    return res

def classify_diff(diff_text: str) -> str:
    lowered = diff_text.lower()
    # check if diff contains diff markers
    if not diff_text or '@@' not in diff_text:
        return 'unknown'
    # comparison operator change
    if re.search(r'(>=|<=|>|<)=?', diff_text) and not re.search(r'(?<!\w)(\+|\-|\*|/)(?!\w)', diff_text):
        return 'comparison_operator'
    # arithmetic op
    if re.search(r'(?<!\w)(\+|\-|\*|/)(?!\w)', diff_text):
        return 'arithmetic_operator'
    # boolean literal
    if re.search(r'\btrue\b|\bfalse\b', lowered):
        return 'boolean_literal'
    # constant number
    if re.search(r'\b(\d+)\b', diff_text):
        return 'constant_mutation'
    # string literal
    if re.search(r'\".*?\"|\'.*?\'', diff_text):
        return 'string_literal'
    # logical operator
    if ' and ' in lowered or ' or ' in lowered:
        return 'logical_operator'
    return 'other'

def ensure_diffs(full_keys):
    DIFFS_DIR.mkdir(exist_ok=True)
    with open(FAILURE_LOG, 'w', encoding='utf-8') as flog:
        for fk in full_keys:
            diff_file = DIFFS_DIR / f"{fk}.diff"
            if diff_file.exists():
                continue
            # try full key
            print(f"尝试获取 diff：{fk}")
            rc, out = run(f"mutmut show {fk}")
            if rc == 0 and out.strip():
                diff_file.write_text(out, encoding='utf-8')
                continue
            else:
                flog.write(f"[FAIL] full_key {fk} show failed (rc {rc}):\n{out}\n")
            # no fallback to numeric id in this version or optionally include
            # optional fallback
            m_id = re.search(r'__mutmut_(\d+)$', fk)
            if m_id:
                num = m_id.group(1)
                print(f"full key {fk} show 失败，尝试数字 id {num}")
                rc2, out2 = run(f"mutmut show {num}")
                if rc2 == 0 and out2.strip():
                    diff_file.write_text(out2, encoding='utf-8')
                    continue
                else:
                    flog.write(f"[FAIL] id {num} show failed (rc {rc2}):\n{out2}\n")
            flog.write(f"[ERROR] both show full_key & id failed for {fk}\n")

def main():
    code, results_text = run("mutmut results")
    if code != 0:
        print("mutmut results 执行失败，请先运行 mutmut run")
        return

    fk_status = parse_results(results_text)
    if not fk_status:
        print("解析 mutmut results 没有突变体")
        return

    full_keys = list(fk_status.keys())

    ensure_diffs(full_keys)

    type_total = defaultdict(int)
    type_killed = defaultdict(int)

    for fk, status in fk_status.items():
        diff_path = DIFFS_DIR / f"{fk}.diff"
        if diff_path.exists():
            diff_text = diff_path.read_text(encoding='utf-8')
        else:
            diff_text = ''
        mutation_type = classify_diff(diff_text)
        type_total[mutation_type] += 1
        if status != 'survived':
            type_killed[mutation_type] += 1

    # 输出统计
    print("mutation_type, total, killed, kill_rate (%)")
    for mtype in sorted(type_total.keys()):
        total = type_total[mtype]
        killed = type_killed.get(mtype, 0)
        rate = (killed / total * 100) if total > 0 else 0.0
        print(f"{mtype}, {total}, {killed}, {rate:.2f}")

    # 写 CSV
    import csv
    with open(STATS_CSV, 'w', encoding='utf-8', newline='') as wf:
        w = csv.writer(wf)
        w.writerow(['mutation_type','total','killed','kill_rate_percent'])
        for mtype in sorted(type_total.keys()):
            total = type_total[mtype]
            killed = type_killed.get(mtype, 0)
            rate = (killed / total * 100) if total > 0 else 0.0
            w.writerow([mtype, total, killed, f"{rate:.2f}"])

    print("统计写入:", STATS_CSV)
    print("失败日志:", FAILURE_LOG)

if __name__ == "__main__":
    main()
