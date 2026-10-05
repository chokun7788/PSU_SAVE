"""Paired clean/noisy pipeline evaluation for the bilingual 2,000-case typo set.

Each completed pair is appended and flushed so interrupted runs can resume.
This evaluates deterministic paths only; source labels remain subject to review.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_master_ground_truth_eval import evaluate  # noqa: E402

FIXTURE = ROOT / "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl"
REPORT_DIR = ROOT / "reports/bilingual_typo_2000_20260929"


def read_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def run_case(row: dict, question_key: str) -> dict:
    case = {**row, "question": row[question_key]}
    try:
        return evaluate(case, allow_llm=False, rag_fallback=False)
    except Exception as exc:  # An error is a failure, never silently skipped.
        return {
            "id": row["id"], "question": row[question_key], "passed": False,
            "route_ok": False, "status_ok": False, "content_ok": False,
            "latency_ok": False, "actual_route": "pipeline_exception",
            "actual_status": "exception", "mode": "pipeline_exception",
            "elapsed_sec": None, "answer": "", "failures": [f"{type(exc).__name__}: {exc}"],
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    parser.add_argument("--locale", choices=("th", "en"), required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    rows = [row for row in read_rows(args.fixture) if row["locale"] == args.locale]
    if args.offset:
        rows = rows[args.offset:]
    if args.limit:
        rows = rows[:args.limit]
    output = args.output or REPORT_DIR / f"paired_{args.locale}_r15.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and not args.resume:
        parser.error(f"Output exists; pass --resume to append missing cases: {output}")
    completed = read_rows(output) if output.exists() else []
    expected_ids = [row["id"] for row in rows]
    completed_ids = [row["id"] for row in completed]
    if len(completed_ids) != len(set(completed_ids)) or completed_ids != expected_ids[:len(completed_ids)]:
        parser.error("Existing output does not match the beginning of this fixture")

    started = datetime.now().isoformat(timespec="seconds")
    with output.open("a", encoding="utf-8") as stream:
        for index, row in enumerate(rows[len(completed):], start=len(completed) + 1):
            clean = run_case(row, "clean_question")
            noisy = run_case(row, "noisy_question")
            result = {
                "id": row["id"], "locale": row["locale"], "domain": row["domain"],
                "review_status": row.get("review_status", ""),
                "edit_recipe": row["edit_recipe"], "edit_actions": row["edit_actions"],
                "protected_literals": row["protected_literals"],
                "clean_question": row["clean_question"], "noisy_question": row["noisy_question"],
                "expected_route_categories": row["expected_route_categories"],
                "expected_answer_status": row["expected_answer_status"],
                "answer_contract": row.get("answer_contract", {}),
                "clean": clean, "noisy": noisy,
                "route_changed": clean["actual_route"] != noisy["actual_route"],
                "status_changed": clean["actual_status"] != noisy["actual_status"],
                "mode_changed": clean["mode"] != noisy["mode"],
                "regression": bool(clean["passed"] and not noisy["passed"]),
                "recovery": bool(not clean["passed"] and noisy["passed"]),
            }
            stream.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
            stream.flush()
            completed.append(result)
            if index % 25 == 0 or index == len(rows):
                print(
                    f"{args.locale} {index}/{len(rows)} "
                    f"clean={sum(item['clean']['passed'] for item in completed)} "
                    f"noisy={sum(item['noisy']['passed'] for item in completed)} "
                    f"regressions={sum(item['regression'] for item in completed)}",
                    flush=True,
                )
    summary = {
        "fixture": str(args.fixture), "output": str(output), "locale": args.locale,
        "started_at": started, "finished_at": datetime.now().isoformat(timespec="seconds"),
        "count": len(completed), "clean_pass": sum(row["clean"]["passed"] for row in completed),
        "noisy_pass": sum(row["noisy"]["passed"] for row in completed),
        "regressions": sum(row["regression"] for row in completed),
        "recoveries": sum(row["recovery"] for row in completed),
        "route_changed": sum(row["route_changed"] for row in completed),
        "status_changed": sum(row["status_changed"] for row in completed),
        "review_status": dict(Counter(row["review_status"] for row in completed)),
        "deterministic_only": True,
    }
    summary_path = output.with_suffix(".summary.json")
    if summary_path.exists() and not args.resume:
        parser.error(f"Summary exists: {summary_path}")
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
