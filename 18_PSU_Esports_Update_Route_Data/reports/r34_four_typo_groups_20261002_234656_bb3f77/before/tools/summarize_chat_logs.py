from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_DIR = ROOT / "data" / "logs"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"WARN invalid jsonl {path}:{line_no}")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize PSU Esports chatbot JSONL logs.")
    parser.add_argument("--date", help="YYYY-MM-DD. Defaults to latest web_chat_*.jsonl")
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    log_dir = Path(args.log_dir)
    if args.date:
        path = log_dir / f"web_chat_{args.date}.jsonl"
    else:
        files = sorted(log_dir.glob("web_chat_*.jsonl"))
        if not files:
            print(f"No log files found in {log_dir}")
            return 0
        path = files[-1]

    rows = read_jsonl(path)
    answered = [row for row in rows if row.get("answer")]
    errors = [row for row in rows if row.get("error")]
    route_counts = Counter(f"{row.get('route_category')}/{row.get('route_intent')}" for row in answered)
    mode_counts = Counter(str(row.get("mode") or "") for row in answered)
    question_counts = Counter(str(row.get("question") or "").strip() for row in answered)
    no_answer_rows = [
        row for row in answered
        if row.get("route_category") == "no_answer" or "ไม่พบข้อมูล" in str(row.get("answer") or "")
    ]
    variant_changed_rows = [
        row for row in answered
        if ((row.get("query_debug") or {}).get("active_query_changed"))
    ]

    print(f"CHAT LOG SUMMARY: {path}")
    print(f"- records: {len(rows)}")
    print(f"- answered: {len(answered)}")
    print(f"- errors: {len(errors)}")
    print(f"- no-answer-ish: {len(no_answer_rows)}")
    print(f"- query-variant changed: {len(variant_changed_rows)}")

    print("\nTop routes:")
    for route, count in route_counts.most_common(args.top):
        print(f"- {route}: {count}")

    print("\nTop modes:")
    for mode, count in mode_counts.most_common(args.top):
        print(f"- {mode}: {count}")

    print("\nRepeated questions:")
    for question, count in question_counts.most_common(args.top):
        if count <= 1:
            continue
        print(f"- {count}x {question}")

    if no_answer_rows:
        print("\nRecent no-answer candidates:")
        for row in no_answer_rows[-args.top:]:
            print(f"- {row.get('question')} | {row.get('mode')} | {row.get('route_category')}/{row.get('route_intent')}")

    if variant_changed_rows:
        print("\nRecent query variant selections:")
        for row in variant_changed_rows[-args.top:]:
            debug = row.get("query_debug") or {}
            print(
                f"- {debug.get('original_question') or row.get('question')} "
                f"=> {debug.get('active_query')} | {row.get('route_category')}/{row.get('route_intent')}"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
