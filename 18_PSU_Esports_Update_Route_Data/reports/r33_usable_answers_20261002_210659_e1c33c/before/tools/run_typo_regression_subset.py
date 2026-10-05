"""Rerun a selected frozen r15 regression subset without overwriting old output."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from tools.run_bilingual_2000_typo_eval_20260929 import read_rows, run_case


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--paired-baseline", type=Path, nargs="+", required=True)
    parser.add_argument("--domain", default="")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"output exists: {args.output}")
    selected = {
        row["id"] for path in args.paired_baseline for row in read_rows(path)
        if row.get("regression") and (not args.domain or row.get("domain") == args.domain)
    }
    rows = [row for row in read_rows(args.fixture) if row["id"] in selected]
    if len(rows) != len(selected):
        parser.error("some baseline IDs are missing from the fixture")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        for index, row in enumerate(rows, 1):
            clean = run_case(row, "clean_question")
            noisy = run_case(row, "noisy_question")
            result = {
                "id": row["id"], "locale": row["locale"], "domain": row["domain"],
                "clean": clean, "noisy": noisy,
                "regression": bool(clean["passed"] and not noisy["passed"]),
            }
            stream.write(json.dumps(result, ensure_ascii=False) + "\n")
            stream.flush()
            if index % 25 == 0 or index == len(rows):
                print(f"{index}/{len(rows)} clean={sum(1 for x in read_rows(args.output) if x['clean']['passed'])}"
                      f" noisy={sum(1 for x in read_rows(args.output) if x['noisy']['passed'])}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
