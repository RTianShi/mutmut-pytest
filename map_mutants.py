#!/usr/bin/env python3
"""
map_mutants.py

用法示例：
  python3 map_mutants.py            # 默认模式（收集所有失败）
  python3 map_mutants.py --first   # 每个 mutant 只取第一个失败（更快）
  python3 map_mutants.py --full    # 收集所有失败（默认）

功能：
- 解析 `mutmut show` 得到 killed 突变体 id
- 依次对每个 id：
    - 确认 git 工作区干净
    - mutmut apply <id>
    - 运行 pytest（带 MUTANT_ID 环境变量）
    - 收集 pytest_mutant_logs 下的 JSON
    - git restore . 恢复源码
- 最终导出 mutant_killers.csv
"""

import subprocess
import sys
import os
import re
import csv
import json
from pathlib import Path
from shutil import which

ROOT = Path('.').resolve()
LOG_DIR = ROOT / 'pytest_mutant_logs'
REPORTS_DIR = ROOT / 'mutant_reports'
CSV_PATH = ROOT / 'mutant_killers.csv'


def run(cmd, capture=True, env=None):
    p = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT,
        text=True,
        env=env
    )
    return p.returncode, p.stdout if capture else ''


def ensure_tool(name):
    if which(name) is None:
        print(f"需要命令未找到：{name}，请先安装并确保在 PATH 中。", file=sys.stderr)
        sys.exit(1)


def parse_killed_ids(mutmut_show_text):
    m = re.search(r'(?mi)^killed\\b.*$', mutmut_show_text)
    block = mutmut_show_text
    if m:
        start = m.start()
        rest = mutmut_show_text[start:]
        end = re.search(r'(?mi)^\\s*(survived|suspicious|timeout|skipped)\\b', rest)
        block = rest if not end else rest[:end.start()]

    ids = set()
    for token in re.findall(r'(\\d+(?:-\\d+)?)', block):
        if '-' in token:
            a, b = token.split('-', 1)
            ids.update(range(int(a), int(b) + 1))
        else:
            ids.add(int(token))
    return sorted(ids)


def git_clean_check():
    rc, out = run('git status --porcelain')
    if out.strip():
        print("工作区不干净：请先 commit 或 stash 更改，然后重试。")
        print(out)
        sys.exit(1)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--first', action='store_true', help='每个 mutant 只取第一个失败')
    parser.add_argument('--full', action='store_true', help='收集所有失败（默认）')
    parser.add_argument('--pytest-args', default='-q', help='传递给 pytest 的额外参数')
    args = parser.parse_args()

    ensure_tool('mutmut')
    ensure_tool('pytest')

    rc, txt = run('mutmut show')
    if rc != 0 and not txt:
        print('运行 mutmut show 失败，请先运行 mutmut run。')
        sys.exit(1)

    killed_ids = parse_killed_ids(txt)
    if not killed_ids:
        print('未找到任何 killed 突变体。')
        sys.exit(0)

    print(f'解析到 {len(killed_ids)} 个 killed 突变体，前 20 个: {killed_ids[:20]}')

    LOG_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)

    rows = []

    for mid in killed_ids:
        print(f'处理 mutant {mid} ...')
        git_clean_check()

        for p in LOG_DIR.glob(f'{mid}__*.json'):
            try:
                p.unlink()
            except Exception:
                pass

        rc, out = run(f'mutmut apply {mid}')
        if rc != 0:
            print(f'mutmut apply {mid} 失败，跳过。')
            run('git restore .', capture=False)
            continue

        env = os.environ.copy()
        env['MUTANT_ID'] = str(mid)
        pytest_args = args.pytest_args
        cmd = f'pytest {pytest_args}'
        if args.first:
            cmd = f'pytest {pytest_args} -x --maxfail=1'

        print('运行:', cmd)
        rc, out = run(cmd, capture=True, env=env)

        found = list(LOG_DIR.glob(f'{mid}__*.json'))
        if not found:
            (REPORTS_DIR / f'mutant-{mid}-pytest-output.txt').write_text(out, encoding='utf-8')
            rows.append([mid, '', '', '', 'no json logs; pytest output saved'])
        else:
            if args.first:
                found = sorted(found)[:1]
            for jf in found:
                try:
                    info = json.loads(jf.read_text(encoding='utf-8'))
                except Exception as e:
                    rows.append([mid, '', '', '', f'json parse error: {e}'])
                    continue
                nodeid = info.get('nodeid', '')
                file = info.get('file', '')
                line = info.get('line', '')
                longrepr = info.get('longrepr', '').replace('\n', '\\n')
                rows.append([mid, nodeid, file, line, longrepr])

        run('git restore .', capture=False)

    with CSV_PATH.open('w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['mutant_id', 'test_nodeid', 'file', 'line', 'failure_message'])
        w.writerows(rows)

    print('完成，输出:')
    print(' - CSV:', CSV_PATH)
    print(' - JSON 日志目录:', LOG_DIR)
    print(' - pytest 输出目录:', REPORTS_DIR)


if __name__ == '__main__':
    main()
