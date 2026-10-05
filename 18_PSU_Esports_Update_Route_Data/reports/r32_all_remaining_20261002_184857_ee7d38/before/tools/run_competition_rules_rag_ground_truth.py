#!/usr/bin/env python3
"""Run the four-rulebook RAG corpus and verify retrieval evidence alignment."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


CASES_PATH = ROOT / "data" / "eval" / "competition_rules_rag_ground_truth_v1.jsonl"
REPORT_DIR = ROOT / "reports" / "competition_rules_rag_eval"
NO_ANSWER_MODES = ("no_answer", "unknown_target", "known_unsupported", "no_context")
CLARIFICATION_MODES = ("clarif", "ambiguous", "missing_game_context")


def load_cases(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def choose_cases(cases: list[dict[str, Any]], sample_per_game: int) -> list[dict[str, Any]]:
    if sample_per_game <= 0:
        return cases
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for case in cases:
        grouped[str(case.get("expected_game_id") or "safe")].append(case)
    selected: list[dict[str, Any]] = []
    for game_id in sorted(grouped):
        by_locale: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for case in grouped[game_id]:
            by_locale[str(case["locale"])].append(case)
        for locale in ("th", "en"):
            by_facet: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for case in by_locale[locale]:
                by_facet[str(case.get("expected_facet") or "safe_outcome")].append(case)
            locale_selected: list[dict[str, Any]] = []
            while len(locale_selected) < sample_per_game and any(by_facet.values()):
                for facet in sorted(by_facet):
                    if by_facet[facet] and len(locale_selected) < sample_per_game:
                        locale_selected.append(by_facet[facet].pop(0))
            selected.extend(locale_selected)
    return selected


def actual_status(answer: str, mode: str) -> str:
    key = mode.casefold()
    if "localization_pending" in key or "missing_english_localization" in key:
        # Source evidence exists, but an English overlay has not been
        # published. Reporting it as an answer hides a release-readiness gap.
        return "localization_pending"
    if any(marker in key for marker in NO_ANSWER_MODES):
        return "no_answer"
    if any(marker in key for marker in CLARIFICATION_MODES):
        return "clarification"
    return "answer"


def hit_identifiers(hits: list[dict[str, Any]]) -> tuple[set[str], set[str]]:
    evidence_ids: set[str] = set()
    rulebooks: set[str] = set()
    for hit in hits:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata", {}) if isinstance(hit.get("metadata"), dict) else {}
        for key in ("id", "source_chunk_id", "rule_id", "fact_id"):
            value = hit.get(key) or metadata.get(key)
            if value:
                evidence_ids.add(str(value))
        source_ids = metadata.get("source_ids", [])
        if isinstance(source_ids, list):
            rulebooks.update(str(item) for item in source_ids)
        for value in (hit.get("source_url"), metadata.get("source_url")):
            if value:
                rulebooks.add(str(value))
    return evidence_ids, rulebooks


def evaluate_case(case: dict[str, Any], *, allow_llm: bool, rag_fallback: bool, include_trace: bool) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_allow_llm=allow_llm,
        experimental_rag_fallback=rag_fallback,
        locale=str(case["locale"]),
        global_timeout_sec=float(case.get("latency_ceiling_sec", 20.0)),
    )
    evidence_ids, rulebook_refs = hit_identifiers(result.hits)
    expected_rulebooks = {str(item) for item in case.get("expected_rulebook_ids", [])}
    allowed_facts = {str(item) for item in case.get("allowed_evidence_fact_ids", [])}
    allowed_rules = {str(item) for item in case.get("allowed_evidence_rule_ids", [])}
    fact_id_match = bool(evidence_ids & allowed_facts)
    canonical_rule_match = bool(evidence_ids & allowed_rules)
    has_evidence_gold = bool(allowed_facts or allowed_rules)
    rulebook_match = all(any(rulebook in reference for reference in rulebook_refs) for rulebook in expected_rulebooks)
    status = actual_status(result.answer or "", result.mode)
    expected_status = str(case["expected_answer_status"])
    outcome_ok = (
        status == "answer" if expected_status == "answer_available"
        else status == "clarification" if expected_status == "clarification_required"
        else status == "no_answer"
    )
    route_ok = result.route.category in set(case.get("expected_route_categories") or [])
    # A target-specific no-answer/clarification must not be forced to attach
    # unrelated evidence merely to satisfy a retrieval metric. Its correctness
    # is judged by route, safe outcome, and absence of a fabricated claim.
    evidence_ok = (
        True
        if expected_status != "answer_available"
        # A comparison can be answerable and target-grounded while its Gold
        # row intentionally has no single acceptable chunk. Do not label that
        # unobserved evidence requirement as a retrieval failure.
        else True
        if case.get("rag_required") and not has_evidence_gold
        else fact_id_match or canonical_rule_match if case.get("rag_required") else None
    )
    # A controlled no-answer or clarification intentionally carries no source
    # hit.  Its target safety is proved by the closed-world route/outcome,
    # while requiring a citation here incorrectly turns correct abstention
    # into a target failure.
    target_ok = (
        True
        if expected_status != "answer_available" and status in {"no_answer", "clarification"}
        else not expected_rulebooks or rulebook_match
    )
    source_gap_safe = (
        status == "no_answer" and not evidence_ids and not rulebook_refs
        if case.get("case_type") == "source_gap_safe_no_answer"
        else None
    )
    latency_ok = result.elapsed <= float(case.get("latency_ceiling_sec", 20.0))
    failures: list[str] = []
    if not route_ok:
        failures.append(f"route expected {case.get('expected_route_categories')}, got {result.route.category}")
    if not outcome_ok:
        failures.append(f"outcome expected {expected_status}, got {status}")
    if not target_ok:
        failures.append(f"missing rulebook target(s): {sorted(expected_rulebooks)}")
    if not evidence_ok:
        failures.append("retrieval evidence did not match the allowed canonical fact/rule IDs")
    if source_gap_safe is False:
        failures.append("source-gap no-answer attached evidence or did not abstain safely")
    if not result.validation.ok:
        failures.append(f"validation errors: {list(result.validation.errors)}")
    if not latency_ok:
        failures.append(f"latency {result.elapsed:.3f}s exceeds {case.get('latency_ceiling_sec')}s")
    return {
        "id": case["id"], "locale": case["locale"], "case_type": case["case_type"], "question": case["question"],
        "expected_game_id": case.get("expected_game_id"), "expected_rulebook_ids": sorted(expected_rulebooks),
        "expected_facet": case.get("expected_facet"), "expected_answer_status": expected_status,
        "actual_category": result.route.category, "actual_intent": result.route.intent, "actual_status": status,
        "mode": result.mode, "elapsed_sec": round(result.elapsed, 4), "validation_ok": result.validation.ok,
        "route_ok": route_ok, "outcome_ok": outcome_ok, "target_ok": target_ok, "evidence_ok": evidence_ok,
        "source_gap_safe": source_gap_safe,
        "evidence_alignment": "legacy_fact_id" if fact_id_match else "canonical_rule_id" if canonical_rule_match else "not_specified" if not has_evidence_gold else "none",
        "returned_evidence_ids": sorted(evidence_ids), "returned_rulebook_refs": sorted(rulebook_refs),
        "passed": not failures, "failures": failures, "answer": result.answer or "",
        "trace": [{"stage": item.stage, "decision": item.decision, "metadata": item.metadata} for item in result.trace] if include_trace else None,
    }


def write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    detail_path = REPORT_DIR / f"competition_rules_rag_eval_{stamp}.json"
    summary_path = REPORT_DIR / f"competition_rules_rag_eval_{stamp}_summary.json"
    detail_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    by_game: dict[str, dict[str, int]] = {}
    for row in rows:
        game = str(row.get("expected_game_id") or "safe_outcome")
        counts = by_game.setdefault(game, {"passed": 0, "failed": 0, "evidence_ok": 0})
        counts["passed" if row["passed"] else "failed"] += 1
        counts["evidence_ok"] += int(row["evidence_ok"] is True)
    summary_path.write_text(json.dumps({
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(rows), "passed": sum(row["passed"] for row in rows),
        "failed": sum(not row["passed"] for row in rows),
        "evidence_ok": sum(row["evidence_ok"] is True for row in rows),
        "by_game": by_game, "detail_file": str(detail_path),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return detail_path, summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run RAG evidence checks for four competition rulebooks.")
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--locale", choices=("th", "en"), default="")
    parser.add_argument("--sample-per-game", type=int, default=0)
    parser.add_argument("--offset", type=int, default=0, help="Skip this many selected cases before evaluation.")
    parser.add_argument("--limit", type=int, default=0, help="Evaluate at most this many selected cases (0 means all).")
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--include-trace", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()
    cases = load_cases(args.cases)
    if args.locale:
        cases = [case for case in cases if case["locale"] == args.locale]
    if args.sample_per_game:
        cases = choose_cases(cases, args.sample_per_game)
    if args.offset:
        cases = cases[max(0, args.offset):]
    if args.limit:
        cases = cases[:max(0, args.limit)]
    rows: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        row = evaluate_case(case, allow_llm=args.allow_llm, rag_fallback=args.rag_fallback, include_trace=args.include_trace)
        rows.append(row)
        print(f"[{index}/{len(cases)}] {'PASS' if row['passed'] else 'FAIL'} {row['id']} {row['actual_category']} evidence={row['evidence_alignment']} {row['elapsed_sec']:.3f}s")
    detail_path, summary_path = write_reports(rows)
    failed = sum(not row["passed"] for row in rows)
    print(
        f"COMPETITION RAG EVAL: {len(rows) - failed}/{len(rows)} passed; "
        f"evidence={sum(row['evidence_ok'] is True for row in rows)}/{len(rows)}"
    )
    print(f"DETAIL: {detail_path}\nSUMMARY: {summary_path}")
    return 1 if failed and args.fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
