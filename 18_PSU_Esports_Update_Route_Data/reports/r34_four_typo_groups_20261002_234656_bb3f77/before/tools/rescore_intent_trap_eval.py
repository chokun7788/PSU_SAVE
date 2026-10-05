#!/usr/bin/env python3
"""Offline rescore of saved answers after correcting candidate-Gold mistakes."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from run_master_ground_truth_eval import contains_contract, expected_status_ok, read_jsonl


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data/eval/intent_trap_bilingual_1000_v2.jsonl"


def rescore(corpus: Path, detail: Path) -> dict:
    cases = {row["id"]: row for row in read_jsonl(corpus)}
    prior = json.loads(detail.read_text(encoding="utf-8"))
    if len(cases) != len(prior) or {row["id"] for row in prior} != set(cases):
        raise ValueError("Saved result IDs do not match corrected corpus")
    rows = []
    for original in prior:
        case = cases[original["id"]]
        if case["question"] != original["question"]:
            raise ValueError(f"Question changed after live run: {case['id']}")
        blocked = (
            case["domain"] == "weekday_live_slots"
            and original["mode"] == "pipeline:live_booking_status_unavailable"
        )
        route_ok = original["actual_route"] in case["expected_route_categories"]
        status_ok = expected_status_ok(case["expected_answer_status"], original["actual_status"], original["mode"])
        content_ok, content_failures = contains_contract(original["answer"], case["answer_contract"])
        latency_ok = original["elapsed_sec"] <= case["latency_ceiling_sec"]
        failures = list(content_failures)
        if not route_ok:
            failures.append(f"route expected {case['expected_route_categories']}, got {original['actual_route']}")
        if not status_ok:
            failures.append(f"status expected {case['expected_answer_status']}, got {original['actual_status']}")
        if not latency_ok:
            failures.append(f"latency {original['elapsed_sec']:.3f}s exceeded ceiling")
        state = (
            "blocked_external_dependency" if blocked
            else "fail" if case["expected_answer_status"] == "route_only" and failures
            else "manual_review_required" if case["expected_answer_status"] == "route_only"
            else "pass" if not failures else "fail"
        )
        rows.append({
            **original,
            "passed": state == "pass",
            "evaluation_state": state,
            "failures": failures,
            "route_ok": route_ok,
            "status_ok": status_ok,
            "content_ok": content_ok,
            "latency_ok": latency_ok,
        })
    by_group = defaultdict(lambda: {"pass": 0, "fail": 0, "blocked_external_dependency": 0, "manual_review_required": 0})
    for row in rows:
        by_group[f"{row['locale']}/{row['domain']}"][row["evaluation_state"]] += 1
    summary = {
        "raw_detail": str(detail), "corrected_corpus": str(corpus),
        "total": len(rows),
        "passed": sum(row["evaluation_state"] == "pass" for row in rows),
        "failed": sum(row["evaluation_state"] == "fail" for row in rows),
        "blocked_external_dependency": sum(row["evaluation_state"] == "blocked_external_dependency" for row in rows),
        "manual_review_required": sum(row["evaluation_state"] == "manual_review_required" for row in rows),
        "by_group": dict(sorted(by_group.items())),
        "note": "Offline rescore only; no second pipeline execution. Live-dashboard-unavailable cases are unscorable for target-date and slot correctness. Route-only cases require human semantic review and are not counted as passes.",
    }
    return {"summary": summary, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("detail", type=Path)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    args = parser.parse_args()
    report = rescore(args.corpus, args.detail)
    output = args.detail.with_name(args.detail.stem + "_intent_trap_rescored_v2.json")
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    review_queue = args.detail.with_name(args.detail.stem + "_intent_trap_manual_review_v2.jsonl")
    review_queue.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in report["rows"] if row["evaluation_state"] == "manual_review_required"),
        encoding="utf-8",
    )
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print(f"OFFLINE RESCORE: {output}")
    print(f"MANUAL REVIEW QUEUE: {review_queue}")


if __name__ == "__main__":
    main()
