"""Second-generation scoring for frozen paired typo results.

This module never rewrites r15 outputs or the source fixture. It can rescore
existing records and makes the distinction between a live lookup and verified
availability explicit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def answer_outcome(mode: str, answer: str, category: str) -> str:
    mode = mode.casefold()
    answer = answer.casefold()
    if "live_booking_status_unavailable" in mode:
        return "live_unavailable"
    if "missing_english_localization" in mode or "localization_pending" in mode:
        return "localization_pending"
    if category == "clarification" or any(
        term in mode for term in ("clarification", "ambiguous", "requires_target")
    ):
        return "clarification"
    if category == "no_answer" or any(
        term in mode for term in ("no_answer", "unknown_target", "rag_miss")
    ):
        return "no_answer"
    if any(term in answer for term in ("ไม่พบ roblox", "not found in the verified", "could not find")):
        return "no_answer"
    return "answer"


def status_matches(expected: str, actual: str, mode: str, route: str) -> bool:
    if expected == "answer_available":
        return actual == "answer"
    if expected in {"clarification_required", "safe_clarification"}:
        return actual == "clarification"
    if expected in {"no_answer_expected", "safe_no_answer"}:
        return actual in {"no_answer", "live_unavailable"}
    if expected == "localization_pending":
        return actual == "localization_pending"
    if expected == "live_lookup_required":
        # Routing to an opening-hours or calendar answer alone is insufficient.
        return route in {"schedule", "reservation"} and "live_booking" in mode
    return False


def contract_matches(answer: str, contract: dict[str, Any]) -> tuple[bool, list[str]]:
    haystack = answer.casefold()
    failures: list[str] = []
    for term in contract.get("must_contain", []):
        if str(term).casefold() not in haystack:
            failures.append(f"missing required: {term}")
    alternatives = [str(term) for term in contract.get("must_contain_any", []) if str(term)]
    if alternatives and not any(term.casefold() in haystack for term in alternatives):
        failures.append(f"missing all alternatives: {alternatives}")
    for index, group in enumerate(contract.get("must_contain_all_groups", []), 1):
        terms = [str(term) for term in group if str(term)]
        if not terms or not any(term.casefold() in haystack for term in terms):
            failures.append(f"required group {index} missing: {terms}")
    for term in contract.get("must_not_contain", []):
        if str(term).casefold() in haystack:
            failures.append(f"forbidden term present: {term}")
    return not failures, failures


def rescore_result(result: dict[str, Any], expected_routes: list[str],
                   expected_status: str, contract: dict[str, Any]) -> dict[str, Any]:
    route = str(result.get("actual_route") or "")
    mode = str(result.get("mode") or "")
    answer = str(result.get("answer") or "")
    outcome = answer_outcome(mode, answer, route)
    route_ok = route in expected_routes
    status_ok = status_matches(expected_status, outcome, mode, route)
    content_ok, failures = contract_matches(answer, contract)
    latency_ok = bool(result.get("latency_ok"))
    if not route_ok:
        failures.append(f"route {route} outside expected {expected_routes}")
    if not status_ok:
        failures.append(f"outcome {outcome} differs from expected {expected_status}")
    if not latency_ok:
        failures.append("latency failed legacy ceiling")
    return {
        "route_ok": route_ok, "status_ok": status_ok, "content_ok": content_ok,
        "latency_ok": latency_ok, "passed": not failures, "outcome": outcome,
        "failures": failures,
    }


def rescore_pair(row: dict[str, Any], overlay: dict[str, Any] | None = None) -> dict[str, Any]:
    overlay = overlay or {}
    routes = list(overlay.get("expected_route_categories", row["expected_route_categories"]))
    expected = str(overlay.get("expected_answer_status", row["expected_answer_status"]))
    contract = dict(row.get("answer_contract") or {})
    contract.update(overlay.get("answer_contract") or {})
    clean = rescore_result(row["clean"], routes, expected, contract)
    noisy = rescore_result(row["noisy"], routes, expected, contract)
    return {
        "id": row["id"], "locale": row["locale"], "domain": row["domain"],
        "review_status": row.get("review_status", ""),
        "legacy": {
            "clean_passed": bool(row["clean"]["passed"]),
            "noisy_passed": bool(row["noisy"]["passed"]),
            "regression": bool(row["regression"]),
        },
        "v2": {
            "clean": clean, "noisy": noisy,
            "regression": clean["passed"] and not noisy["passed"],
        },
        "overlay_applied": bool(overlay),
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Rescore a frozen paired typo run.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overlay", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"output already exists: {args.output}")
    overlays = {
        row["id"]: row for row in _read_jsonl(args.overlay)
    } if args.overlay else {}
    rows = _read_jsonl(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(rescore_pair(row, overlays.get(row["id"])), ensure_ascii=False) + "\n")
    print(json.dumps({
        "input": str(args.input), "output": str(args.output), "count": len(rows),
        "legacy_regressions": sum(bool(row["regression"]) for row in rows),
        "v2_regressions": sum(
            rescore_pair(row, overlays.get(row["id"]))["v2"]["regression"] for row in rows
        ),
        "overlay_count": sum(row["id"] in overlays for row in rows),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
