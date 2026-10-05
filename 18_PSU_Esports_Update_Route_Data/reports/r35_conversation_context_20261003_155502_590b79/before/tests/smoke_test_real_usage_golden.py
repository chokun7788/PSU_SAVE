from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_real_usage_golden_eval import CASES_PATH, evaluate_case, load_cases  # noqa: E402


def main() -> int:
    cases = load_cases(CASES_PATH)
    failures: list[dict] = []
    for index, case in enumerate(cases, start=1):
        row = evaluate_case(case, allow_llm=False, rag_fallback=False, include_trace=False)
        status = "OK" if row["passed"] else "FAIL"
        print(f"{status} [{index}/{len(cases)}] {row['id']} {row['mode']}")
        if not row["passed"]:
            failures.append(row)

    if failures:
        preview = []
        for row in failures[:8]:
            preview.append(f"{row['id']} {row['question']}: {row['failures']}\n{row['answer'][:600]}")
        raise AssertionError("REAL USAGE GOLDEN FAILURES:\n\n" + "\n\n".join(preview))

    print(f"REAL USAGE GOLDEN SMOKE TEST OK ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
