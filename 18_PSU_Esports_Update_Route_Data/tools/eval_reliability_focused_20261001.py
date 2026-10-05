"""Trace-bearing source-supported pilot, isolated from frozen GT."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tests.test_reliability_flow_20261001 import CASES, run_focused_case


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite evidence")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results = []
    with args.output.open("x", encoding="utf-8") as stream:
        for case in CASES:
            row = run_focused_case(case)
            results.append(row)
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            print(row["id"], row["passed"], row["failures"], flush=True)
    print(json.dumps({"count": len(results), "passed": sum(r["passed"] for r in results)}, ensure_ascii=False))
    return 0 if all(r["passed"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
