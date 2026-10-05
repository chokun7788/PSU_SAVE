#!/usr/bin/env python3
"""Evaluate all or a stratified slice of the bilingual master GT corpus."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


DEFAULT_CORPUS = ROOT / "data" / "eval" / "master_ground_truth_bilingual_10000_v2.jsonl"
REPORT_DIR = ROOT / "reports" / "master_ground_truth_eval"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def actual_status(mode: str, answer: str, route_category: str = "") -> str:
    value = f"{mode} {answer}".casefold()
    if "general_rag_miss_llm_unavailable" in mode.casefold():
        return "no_answer"
    if any(token in mode.casefold() for token in ("live_booking_status_unavailable", "equipment_spec_unverified")):
        return "no_answer"
    if "localization_pending" in value or "missing_english_localization" in value or "does not yet have an approved english localization" in value:
        return "localization_pending"
    if route_category == "clarification":
        return "clarification"
    if route_category == "no_answer":
        return "no_answer"
    if "clarification" in value or "which game" in value or "เกมไหน" in value:
        return "clarification"
    if (
        "no_answer" in value
        or "ไม่พบข้อมูล" in value
        or "could not find" in value
        or "no information" in value and "found" in value
        or "unavailable" in mode.casefold() and "cannot confirm" in answer.casefold()
        or "unknown_target" in mode.casefold()
    ):
        return "no_answer"
    return "answer"


def expected_status_ok(expected: str, actual: str, mode: str) -> bool:
    if expected == "answer_available":
        return actual == "answer"
    if expected in {"clarification_required", "safe_clarification"}:
        return actual == "clarification"
    if expected in {"no_answer_expected", "safe_no_answer"}:
        return actual == "no_answer"
    if expected == "localization_pending":
        return actual in {"localization_pending", "answer"}
    if expected == "live_lookup_required":
        return any(token in mode for token in ("live", "booking", "schedule", "calendar", "opening"))
    return True


def contains_contract(answer: str, contract: dict[str, Any]) -> tuple[bool, list[str]]:
    normalized = answer.casefold()
    failures: list[str] = []
    required = [str(item) for item in contract.get("must_contain", []) if str(item)]
    required_any = [str(item) for item in contract.get("must_contain_any", []) if str(item)]
    forbidden = [str(item) for item in contract.get("must_not_contain", []) if str(item)]
    missing = [item for item in required if item.casefold() not in normalized]
    if missing:
        failures.append(f"missing required text: {missing[:4]}")
    if required_any and not any(item.casefold() in normalized for item in required_any):
        failures.append(f"none of required alternatives found: {required_any[:6]}")
    present_forbidden = [item for item in forbidden if item.casefold() in normalized]
    if present_forbidden:
        failures.append(f"forbidden text present: {present_forbidden[:4]}")
    return not failures, failures


def choose_cases(
    rows: list[dict[str, Any]], *, locale: str, domains: set[str],
    sample_per_domain: int, offset: int, limit: int,
) -> list[dict[str, Any]]:
    selected = [
        row for row in rows
        if (not locale or row.get("locale") == locale)
        and (not domains or row.get("domain") in domains)
    ]
    if sample_per_domain:
        grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in selected:
            grouped[(str(row["locale"]), str(row["domain"]))].append(row)
        sampled: list[dict[str, Any]] = []
        for key in sorted(grouped):
            candidates = grouped[key]
            if len(candidates) <= sample_per_domain:
                sampled.extend(candidates)
                continue
            step = max(1, len(candidates) // sample_per_domain)
            sampled.extend(candidates[index] for index in range(0, len(candidates), step)[:sample_per_domain])
        selected = sampled
    if offset:
        selected = selected[offset:]
    if limit:
        selected = selected[:limit]
    return selected


def evaluate(case: dict[str, Any], *, allow_llm: bool, rag_fallback: bool) -> dict[str, Any]:
    reference_date = ""
    if case.get("domain") == "weekday_live_slots":
        reference_date = str((case.get("metadata") or {}).get("reference_date") or "")
    if reference_date:
        with patch("app.booking.live_status.today_bangkok", return_value=date.fromisoformat(reference_date)):
            result = answer_question_pipeline_debug(
                str(case["question"]),
                experimental_allow_llm=allow_llm,
                experimental_rag_fallback=rag_fallback,
                locale=str(case["locale"]),
                global_timeout_sec=float(case.get("latency_ceiling_sec", 20.0)),
            )
    else:
        result = answer_question_pipeline_debug(
            str(case["question"]),
            experimental_allow_llm=allow_llm,
            experimental_rag_fallback=rag_fallback,
            locale=str(case["locale"]),
            global_timeout_sec=float(case.get("latency_ceiling_sec", 20.0)),
        )
    answer = result.answer or ""
    status = actual_status(result.mode, answer, result.route.category)
    expected_routes = set(case.get("expected_route_categories") or [])
    route_ok = result.route.category in expected_routes
    status_ok = expected_status_ok(str(case.get("expected_answer_status") or ""), status, result.mode)
    content_ok, failures = contains_contract(answer, case.get("answer_contract") or {})
    latency_ok = result.elapsed <= float(case.get("latency_ceiling_sec", 20.0))
    if not route_ok:
        failures.append(f"route expected {sorted(expected_routes)}, got {result.route.category}")
    if not status_ok:
        failures.append(f"status expected {case.get('expected_answer_status')}, got {status}")
    if not latency_ok:
        failures.append(f"latency {result.elapsed:.3f}s exceeded ceiling")
    return {
        "id": case["id"], "locale": case["locale"], "domain": case["domain"],
        "question": case["question"], "review_status": case["review_status"],
        "reference_date": reference_date,
        "expected_routes": sorted(expected_routes), "actual_route": result.route.category,
        "expected_status": case["expected_answer_status"], "actual_status": status,
        "mode": result.mode, "elapsed_sec": round(result.elapsed, 4),
        "route_ok": route_ok, "status_ok": status_ok, "content_ok": content_ok,
        "latency_ok": latency_ok, "passed": not failures, "failures": failures,
        "answer": answer,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the bilingual master ground-truth evaluator.")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--locale", choices=("th", "en"), default="")
    parser.add_argument("--domains", default="", help="Comma-separated domain names")
    parser.add_argument("--sample-per-domain", type=int, default=0)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--failed-ids-from", type=Path, help="Run only failed cases from a previous raw or rescore report")
    args = parser.parse_args()
    domains = {item.strip() for item in args.domains.split(",") if item.strip()}
    corpus_rows = read_jsonl(args.corpus)
    if args.failed_ids_from:
        previous = json.loads(args.failed_ids_from.read_text(encoding="utf-8"))
        previous_rows = previous.get("rows", []) if isinstance(previous, dict) else previous
        failed_ids = {
            str(row["id"]) for row in previous_rows
            if row.get("evaluation_state") == "fail"
            or ("evaluation_state" not in row and row.get("passed") is False)
        }
        missing_ids = failed_ids - {str(row["id"]) for row in corpus_rows}
        if missing_ids:
            raise ValueError(f"Previous report contains IDs missing from corpus: {sorted(missing_ids)[:5]}")
        corpus_rows = [row for row in corpus_rows if row["id"] in failed_ids]
    cases = choose_cases(
        corpus_rows, locale=args.locale, domains=domains,
        sample_per_domain=args.sample_per_domain, offset=args.offset, limit=args.limit,
    )
    results = []
    for index, case in enumerate(cases, start=1):
        row = evaluate(case, allow_llm=args.allow_llm, rag_fallback=args.rag_fallback)
        results.append(row)
        print(f"[{index}/{len(cases)}] {'PASS' if row['passed'] else 'FAIL'} {row['id']} {row['domain']} {row['elapsed_sec']:.3f}s")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    detail = REPORT_DIR / f"master_gt_eval_{stamp}.json"
    summary = REPORT_DIR / f"master_gt_eval_{stamp}_summary.json"
    detail.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    by_domain: dict[str, dict[str, int]] = {}
    for row in results:
        counts = by_domain.setdefault(row["domain"], {"passed": 0, "failed": 0})
        counts["passed" if row["passed"] else "failed"] += 1
    summary.write_text(json.dumps({
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(results), "passed": sum(row["passed"] for row in results),
        "failed": sum(not row["passed"] for row in results), "by_domain": by_domain,
        "detail_file": str(detail),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"MASTER GT EVAL: {sum(row['passed'] for row in results)}/{len(results)} passed")
    print(f"DETAIL: {detail}")
    print(f"SUMMARY: {summary}")
    return 0 if all(row["passed"] for row in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
