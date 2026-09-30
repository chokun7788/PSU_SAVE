#!/usr/bin/env python3
"""Compare a streaming r9 master GT run to the prior deterministic r8 run."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = ROOT / "reports/master_ground_truth_eval/r8_full_20260928"
CURRENT = ROOT / "reports/master_ground_truth_eval"


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                # The last line may still be being written by a live run.
                break
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output exists: {args.output}")

    old_rows = []
    for offset in (0, 2500, 5000, 7500):
        old_rows.extend(read_rows(PREVIOUS / f"chunk_{offset:04d}" / "results.jsonl"))
    new_rows = []
    thai_chunks = [f"20260929_r9_th_chunk_{offset}" for offset in (0, 1250, 2500, 3750)]
    thai_sources = thai_chunks if (CURRENT / thai_chunks[0] / "results.jsonl").exists() else ["20260929_r9_full_th_5000"]
    for name in (*thai_sources, "20260929_r9_full_en_5000"):
        new_rows.extend(read_rows(CURRENT / name / "results.jsonl"))
    old_by_id = {row["id"]: row for row in old_rows}
    compared = []
    domains: dict[str, Counter] = defaultdict(Counter)
    causes: Counter = Counter()
    transitions: Counter = Counter()
    for row in new_rows:
        old = old_by_id.get(row["id"])
        if old is None:
            continue
        domain = f"{row['locale']}/{row['domain']}"
        domains[domain]["count"] += 1
        domains[domain]["r8_pass"] += bool(old.get("passed"))
        domains[domain]["r9_pass"] += bool(row.get("passed"))
        change = f"{'pass' if old.get('passed') else 'fail'} -> {'pass' if row.get('passed') else 'fail'}"
        transitions[change] += 1
        if not row.get("passed"):
            for failure in row.get("failures", []):
                causes[failure.split(" expected ")[0].split(": ")[0]] += 1
        if old.get("passed") != row.get("passed"):
            compared.append({
                "id": row["id"], "locale": row["locale"], "domain": row["domain"],
                "question": row["question"], "change": change,
                "r8_route": old.get("actual_route"), "r9_route": row.get("actual_route"),
                "r8_mode": old.get("mode"), "r9_mode": row.get("mode"),
                "r8_failures": old.get("failures"), "r9_failures": row.get("failures"),
                "r8_answer": str(old.get("answer", ""))[:350],
                "r9_answer": str(row.get("answer", ""))[:350],
            })
    result = {
        "new_rows": len(new_rows), "matched": sum(transitions.values()),
        "transitions": dict(transitions),
        "by_domain": {key: dict(value) for key, value in sorted(domains.items())},
        "failure_causes": dict(causes.most_common()),
        "changed_cases": compared,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "changed_cases"}, ensure_ascii=False, indent=2))
    print(f"changed cases: {len(compared)}")


if __name__ == "__main__":
    main()
