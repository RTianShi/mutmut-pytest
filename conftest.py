# conftest.py

import os
import json
import re
from pathlib import Path
import pytest

LOG_DIR = Path("pytest_mutant_logs")
LOG_DIR.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 这个 hook 在 setup/call/teardown 三个阶段都会被调用，用 call 阶段来关注测试执行失败
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mutant_id = os.environ.get("MUTANT_ID", "unknown")
        nodeid = item.nodeid  # 测试函数名 + 参数
        # longrepr 或 longreprtext 包含失败 traceback & expression
        longrepr = getattr(rep, "longreprtext", None) or str(getattr(rep, "longrepr", ""))
        # 尝试提取断言表达式行号与文件
        m = re.search(r'File \"([^\"]+)\", line (\d+)', longrepr)
        file = m.group(1) if m else None
        line = int(m.group(2)) if m else None

        # 额外，尝试从 longrepr 找出断言表达式本身
        # 断言输出通常形如 "E       assert something == something_else"
        expr_match = None
        for l in longrepr.splitlines():
            l = l.strip()
            if l.startswith("assert "):
                expr_match = l
                break

        record = {
            "mutant_id": mutant_id,
            "nodeid": nodeid,
            "file": file,
            "line": line,
            "assert_expr": expr_match,
            "longrepr": longrepr.replace("\n", "\\n")
        }
        # 日志文件名里可以带 nodeid 安全化
        safe_node = nodeid.replace("/", "__").replace("::", "__").replace(":", "_")
        out_path = LOG_DIR / f"{mutant_id}__{safe_node}.json"
        try:
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=2)
        except Exception:
            pass
