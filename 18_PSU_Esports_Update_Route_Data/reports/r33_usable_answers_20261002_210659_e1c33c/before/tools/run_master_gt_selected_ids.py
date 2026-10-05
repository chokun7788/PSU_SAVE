#!/usr/bin/env python3
"""Run a reviewable, non-overwriting subset of the master GT corpus."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.run_master_ground_truth_eval import DEFAULT_CORPUS, evaluate, read_jsonl  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ids", required=True, help="Comma-separated master GT case IDs")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output exists: {args.output}")
    ids = {value.strip() for value in args.ids.split(",") if value.strip()}
    rows = [row for row in read_jsonl(DEFAULT_CORPUS) if row["id"] in ids]
    missing = ids - {row["id"] for row in rows}
    if missing:
        parser.error(f"Unknown case IDs: {', '.join(sorted(missing))}")
    results = []
    for row in rows:
        result = evaluate(row, allow_llm=False, rag_fallback=False)
        results.append(result)
        print(f"{row['id']} {'PASS' if result['passed'] else 'FAIL'} {result['elapsed_sec']}s", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in results), encoding="utf-8")
    summary = {"selected": len(results), "passed": sum(row["passed"] for row in results), "output": str(args.output)}
    args.output.with_suffix(".summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
