#!/usr/bin/env python3
"""Run the bilingual RAG robustness corpus against the live pipeline.

This evaluator deliberately scores route and safe outcome before prose. It is
therefore useful for new/ambiguous wording even when an owner has not approved
one exact textual answer yet.
"""

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


CASES_PATH = ROOT / "data" / "eval" / "rag_robustness_ground_truth_v1.jsonl"
REPORT_DIR = ROOT / "reports" / "rag_robustness_eval"

NO_ANSWER_SIGNALS = (
    "ไม่มีข้อมูล", "ไม่พบข้อมูล", "ไม่สามารถยืนยัน", "ไม่มีรายละเอียด",
    "ยังไม่มี context", "ยังไม่พบชื่อเกม", "ยังไม่พบเกม", "ไม่พบชื่อเกม",
    "i do not have", "i don't have", "no verified information", "no information available",
    "no context", "could not find this game", "could not find this title",
)
CLARIFICATION_SIGNALS = (
    "กรุณาระบุ", "ช่วยระบุ", "โปรดระบุ", "ขอรายละเอียดเพิ่ม", "ขอข้อมูลเพิ่ม",
    "กรุณาแจ้ง", "which game", "please specify", "could you clarify", "what date", "which date",
)
NO_ANSWER_MODE_MARKERS = ("no_answer", "unknown_target", "known_unsupported", "no_context")
CLARIFICATION_MODE_MARKERS = ("clarif", "ambiguous", "missing_game_context")


def load_cases(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        text = line.strip()
        if not text:
            continue
        try:
            rows.append(json.loads(text))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at {path}:{line_no}: {exc}") from exc
    return rows


def choose_cases(cases: list[dict[str, Any]], sample_per_locale: int) -> list[dict[str, Any]]:
    if sample_per_locale <= 0:
        return cases
    selected: list[dict[str, Any]] = []
    for locale in ("th", "en"):
        pool = [case for case in cases if case.get("locale") == locale]
        by_group: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for case in pool:
            by_group[str(case.get("group", "unknown"))].append(case)
        locale_cases: list[dict[str, Any]] = []
        while len(locale_cases) < sample_per_locale and any(by_group.values()):
            for group in sorted(by_group):
                if by_group[group] and len(locale_cases) < sample_per_locale:
                    locale_cases.append(by_group[group].pop(0))
        selected.extend(locale_cases)
    return selected


def _contains_any(text: str, signals: tuple[str, ...]) -> bool:
    folded = text.casefold()
    return any(signal.casefold() in folded for signal in signals)


def classify_answer(answer: str, mode: str) -> str:
    mode_key = mode.casefold()
    if "chatbot_identity" in mode_key or "greeting" in mode_key:
        return "answer"
    if any(marker in mode_key for marker in NO_ANSWER_MODE_MARKERS):
        return "no_answer"
    if any(marker in mode_key for marker in CLARIFICATION_MODE_MARKERS) or _contains_any(answer, CLARIFICATION_SIGNALS):
        return "clarification"
    answer_key = answer.casefold().lstrip()
    if any(answer_key.startswith(signal.casefold()) for signal in NO_ANSWER_SIGNALS):
        return "no_answer"
    return "answer"


def rebuild_failures(row: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if not row.get("route_ok"):
        failures.append(
            f"route expected one of {row.get('expected_route_categories')}, got {row.get('actual_category')}"
        )
    if not row.get("outcome_ok"):
        failures.append(
            f"outcome expected {row.get('expected_answer_status')}, got {row.get('actual_status')}"
        )
    if not row.get("validation_ok"):
        validation_failure = next(
            (str(item) for item in row.get("failures", []) if str(item).startswith("validation errors")),
            "validation errors",
        )
        failures.append(validation_failure)
    if not row.get("latency_ok"):
        failures.append(
            f"latency {float(row.get('elapsed_sec') or 0):.3f}s exceeds the case ceiling"
        )
    return failures


def rescore_rows(rows: list[dict[str, Any]], cases_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rescored: list[dict[str, Any]] = []
    for original in rows:
        row = dict(original)
        current_case = cases_by_id.get(str(row.get("id")))
        if current_case:
            for field in ("expected_route_categories", "expected_answer_status", "expected_source_requirement"):
                row[field] = current_case.get(field)
        row["actual_status"] = classify_answer(str(row.get("answer") or ""), str(row.get("mode") or ""))
        expected_status = str(row.get("expected_answer_status") or "")
        row["route_ok"] = str(row.get("actual_category")) in set(row.get("expected_route_categories") or [])
        if expected_status == "clarification_required":
            row["outcome_ok"] = row["actual_status"] == "clarification"
        elif expected_status == "no_answer_expected":
            row["outcome_ok"] = row["actual_status"] == "no_answer"
        else:
            row["outcome_ok"] = row["actual_status"] == "answer" and bool(str(row.get("answer") or "").strip())
        row["passed"] = bool(row.get("route_ok")) and bool(row["outcome_ok"]) and bool(row.get("validation_ok")) and bool(row.get("latency_ok"))
        row["failures"] = rebuild_failures(row)
        rescored.append(row)
    return rescored


def evaluate_case(
    case: dict[str, Any], *, allow_llm: bool, rag_fallback: bool, include_trace: bool
) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_rag_fallback=rag_fallback,
        experimental_allow_llm=allow_llm,
        locale=str(case.get("locale", "auto")),
        global_timeout_sec=float(case.get("latency_ceiling_sec", 20.0)),
    )
    answer = result.answer or ""
    actual_status = classify_answer(answer, result.mode)
    expected_status = str(case.get("expected_answer_status", ""))
    route_ok = result.route.category in set(case.get("expected_route_categories") or [])
    if expected_status == "clarification_required":
        outcome_ok = actual_status == "clarification"
    elif expected_status == "no_answer_expected":
        outcome_ok = actual_status == "no_answer"
    else:
        outcome_ok = actual_status == "answer" and bool(answer.strip())
    latency_ok = result.elapsed <= float(case.get("latency_ceiling_sec", 20.0))
    failures: list[str] = []
    if not route_ok:
        failures.append(
            f"route expected one of {case.get('expected_route_categories')}, got {result.route.category}"
        )
    if not outcome_ok:
        failures.append(f"outcome expected {expected_status}, got {actual_status}")
    if not result.validation.ok:
        failures.append(f"validation errors: {list(result.validation.errors)}")
    if not latency_ok:
        failures.append(f"latency {result.elapsed:.3f}s exceeds {case.get('latency_ceiling_sec')}s")
    return {
        "id": case.get("id"),
        "locale": case.get("locale"),
        "group": case.get("group"),
        "scenario_id": case.get("scenario_id"),
        "question": case.get("question"),
        "expected_route_categories": case.get("expected_route_categories"),
        "expected_answer_status": expected_status,
        "expected_source_requirement": case.get("expected_source_requirement"),
        "actual_category": result.route.category,
        "actual_intent": result.route.intent,
        "actual_status": actual_status,
        "mode": result.mode,
        "elapsed_sec": round(result.elapsed, 4),
        "validation_ok": result.validation.ok,
        "route_ok": route_ok,
        "outcome_ok": outcome_ok,
        "latency_ok": latency_ok,
        "passed": not failures,
        "failures": failures,
        "answer": answer,
        "trace": [
            {
                "stage": item.stage,
                "decision": item.decision,
                "detail": item.detail,
                "metadata": item.metadata,
            }
            for item in result.trace
        ] if include_trace else None,
    }


def write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    detail_path = REPORT_DIR / f"rag_robustness_eval_{stamp}.json"
    summary_path = REPORT_DIR / f"rag_robustness_eval_{stamp}_summary.json"
    detail_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    by_locale = Counter(str(row["locale"]) for row in rows)
    by_group: dict[str, dict[str, int]] = {}
    for row in rows:
        group = str(row["group"])
        counts = by_group.setdefault(group, {"passed": 0, "failed": 0})
        counts["passed" if row["passed"] else "failed"] += 1
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(rows),
        "passed": sum(row["passed"] for row in rows),
        "failed": sum(not row["passed"] for row in rows),
        "by_locale": dict(by_locale),
        "by_group": by_group,
        "detail_file": str(detail_path),
        "scope": "Route, safe outcome, validation and latency only; prose is reviewed separately.",
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return detail_path, summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the bilingual RAG robustness ground truth corpus.")
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--locale", choices=("th", "en"), default="")
    parser.add_argument("--group", default="")
    parser.add_argument("--sample-per-locale", type=int, default=0)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--include-trace", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    parser.add_argument("--rescore-input", type=Path, default=None, help="re-score an existing detail JSON without rerunning the pipeline")
    args = parser.parse_args()

    if args.rescore_input:
        rows = json.loads(args.rescore_input.read_text(encoding="utf-8"))
        if not isinstance(rows, list):
            raise ValueError("--rescore-input must contain a JSON array.")
        cases_by_id = {str(case.get("id")): case for case in load_cases(args.cases)}
        rescored = rescore_rows([row for row in rows if isinstance(row, dict)], cases_by_id)
        detail_path, summary_path = write_reports(rescored)
        failed = sum(not row["passed"] for row in rescored)
        print(f"RAG ROBUSTNESS RESCORE: {len(rescored) - failed}/{len(rescored)} passed, {failed} failed")
        print(f"DETAIL: {detail_path}")
        print(f"SUMMARY: {summary_path}")
        return 1 if failed and args.fail_on_error else 0

    cases = load_cases(args.cases)
    if args.locale:
        cases = [case for case in cases if case.get("locale") == args.locale]
    if args.group:
        cases = [case for case in cases if case.get("group") == args.group]
    cases = choose_cases(cases, args.sample_per_locale) if not args.locale else cases[:args.sample_per_locale or None]
    if not cases:
        raise ValueError("No cases selected.")

    rows: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        row = evaluate_case(
            case, allow_llm=args.allow_llm, rag_fallback=args.rag_fallback, include_trace=args.include_trace
        )
        rows.append(row)
        print(
            f"[{index}/{len(cases)}] {'PASS' if row['passed'] else 'FAIL'} {row['id']} "
            f"route={row['actual_category']} status={row['actual_status']} "
            f"elapsed={row['elapsed_sec']:.3f}s"
        )
    detail_path, summary_path = write_reports(rows)
    failed = sum(not row["passed"] for row in rows)
    print(f"RAG ROBUSTNESS EVAL: {len(rows) - failed}/{len(rows)} passed, {failed} failed")
    print(f"DETAIL: {detail_path}")
    print(f"SUMMARY: {summary_path}")
    return 1 if failed and args.fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
