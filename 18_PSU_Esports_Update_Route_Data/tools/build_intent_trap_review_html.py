from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl"
DEFAULT_OUTPUT = ROOT / "reports/master_ground_truth_eval/intent_trap_400_review_20260924.html"
TEMPLATE = ROOT / "review_ui/intent_trap_400_template.html"


def build_html(source: Path, output: Path) -> int:
    raw = source.read_bytes()
    rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    ids = [str(row["id"]) for row in rows]
    if len(rows) != 400 or len(ids) != len(set(ids)):
        raise ValueError(f"Expected 400 unique review items, got {len(rows)} rows and {len(set(ids))} IDs")
    if any(row.get("evaluation_state") != "manual_review_required" for row in rows):
        raise ValueError("Input contains an item that is not pending manual review")

    items = [
        {key: row[key] for key in ("id", "locale", "domain", "question", "answer", "actual_route", "actual_status")}
        for row in rows
    ]
    payload = {
        "source_file": source.name,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "items": items,
    }
    embedded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count("__REVIEW_DATA__") != 1:
        raise ValueError("HTML template must contain exactly one data placeholder")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.replace("__REVIEW_DATA__", embedded), encoding="utf-8", newline="\n")
    print(f"Created {output} with {len(items)} review items")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a self-contained HTML review file for the 400 intent-trap cases.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    return build_html(args.source, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
