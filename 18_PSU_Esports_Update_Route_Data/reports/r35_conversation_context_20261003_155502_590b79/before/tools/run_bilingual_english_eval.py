from __future__ import annotations

import argparse
import json
import math
import os
import statistics
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("PSU_BILINGUAL_EN_ENABLED", "1")

from app.core.locale import contains_thai_prose
from app.pipeline.engine import AnswerQualityPipeline


DEFAULT_CORPUS = ROOT / "data" / "eval" / "english_gold_400_20260902.jsonl"
REPORT_ROOT = ROOT / "reports" / "bilingual_english"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil((percentile / 100) * len(ordered)) - 1))
    return ordered[index]


def _question(row: dict[str, Any], *, allow_machine_translations: bool = False) -> str:
    if row.get("suite") == "english_shadow":
        allowed_statuses = {"approved"}
        if allow_machine_translations:
            allowed_statuses.add("machine_translated_unreviewed")
        if row.get("translation_status") not in allowed_statuses or not str(row.get("question_en") or "").strip():
            return ""
        return str(row["question_en"]).strip()
    return str(row.get("question") or "").strip()


def _expected_categories(row: dict[str, Any]) -> list[str]:
    """Normalize one allowed category or a list of allowed categories."""
    values = row.get("expected_categories")
    if values is None:
        values = row.get("expected_category")
    if isinstance(values, list):
        return [str(value) for value in values if value]
    return [str(values)] if values else []


def _evaluate(row: dict[str, Any], result) -> tuple[list[str], list[str]]:
    answer = result.answer or ""
    answer_lower = answer.casefold()
    failures: list[str] = []
    blockers: list[str] = []
    expected_categories = _expected_categories(row)
    if expected_categories and result.route.category not in expected_categories:
        failures.append(f"category:{result.route.category} not in {expected_categories}")
    if result.language is None or result.language.effective != "en":
        failures.append("effective_language_not_en")
    if contains_thai_prose(answer):
        failures.append("thai_prose_leak")
    if result.elapsed >= float(row.get("latency_ceiling_sec") or 10.0):
        failures.append(f"latency:{result.elapsed:.4f}")
    if result.mode == "pipeline:request_timeout_no_answer":
        failures.append("pipeline_timeout")
    if not result.validation.ok:
        failures.append("answer_validation_failed")
    for required in row.get("must_contain") or []:
        if str(required).casefold() not in answer_lower:
            failures.append(f"missing:{required}")
    alternatives = [str(value) for value in row.get("must_contain_any") or [] if value]
    if alternatives and not any(value.casefold() in answer_lower for value in alternatives):
        failures.append("missing_any:" + "|".join(alternatives))
    for forbidden in row.get("must_not_contain") or []:
        if str(forbidden).casefold() in answer_lower:
            failures.append(f"forbidden:{forbidden}")
    expected_status = str(row.get("expected_answer_status") or "answer_available")
    if expected_status == "localization_pending":
        blockers.append("approved_english_localization_required")
    return failures, blockers


def main() -> int:
    parser = argparse.ArgumentParser(description="Run English Gold or approved English Shadow cases through the bilingual pipeline.")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--allow-machine-translations", action="store_true", help="Evaluate unreviewed local-model translations; never treats them as approved knowledge.")
    args = parser.parse_args()

    rows = _read_jsonl(args.corpus)
    runnable = [(row, _question(row, allow_machine_translations=args.allow_machine_translations)) for row in rows]
    pending = [row for row, question in runnable if not question]
    runnable = [(row, question) for row, question in runnable if question]
    if args.limit > 0:
        runnable = runnable[: args.limit]
    run_id = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    output_dir = args.output_dir or REPORT_ROOT / run_id
    output_dir.mkdir(parents=True, exist_ok=False)
    if not runnable:
        summary = {
            "run_id": run_id,
            "status": "blocked_pending_human_review",
            "corpus": str(args.corpus),
            "total_source_rows": len(rows),
            "runnable_cases": 0,
            "pending_human_review": len(pending),
            "strict_pass": 0,
            "strict_pass_rate": None,
            "llm_enabled": args.allow_llm,
            "machine_translations_allowed": args.allow_machine_translations,
            "results": None,
        }
        (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 2

    results_path = output_dir / "results.jsonl"
    pipeline = AnswerQualityPipeline()
    latencies: list[float] = []
    strict_pass_count = 0
    critical_total = 0
    critical_pass = 0
    blocker_count = 0
    failure_types: Counter[str] = Counter()
    mode_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    started = time.perf_counter()

    with results_path.open("w", encoding="utf-8") as handle:
        for index, (row, question) in enumerate(runnable, 1):
            case_started = time.perf_counter()
            try:
                result = pipeline.answer(
                    question,
                    locale="en",
                    experimental_allow_llm=args.allow_llm,
                    experimental_rag_fallback=False,
                    global_timeout_sec=10.0,
                )
                failures, blockers = _evaluate(row, result)
                elapsed = float(result.elapsed)
                record = {
                    "id": row.get("id"),
                    "group": row.get("group"),
                    "question": question,
                    "answer": result.answer,
                    "route_category": result.route.category,
                    "route_intent": result.route.intent,
                    "mode": result.mode,
                    "language": result.language.to_dict() if result.language else None,
                    "latency_sec": elapsed,
                    "wall_sec": round(time.perf_counter() - case_started, 4),
                    "validation_ok": result.validation.ok,
                    "validation_errors": list(result.validation.errors),
                    "strict_pass": not failures,
                    "failures": failures,
                    "blockers": blockers,
                    "expected_answer_status": row.get("expected_answer_status"),
                    "critical_fact": bool(row.get("critical_fact")),
                    "translation_status": row.get("translation_status"),
                }
            except Exception as exc:
                elapsed = time.perf_counter() - case_started
                failures = [f"exception:{type(exc).__name__}"]
                blockers = []
                record = {
                    "id": row.get("id"),
                    "group": row.get("group"),
                    "question": question,
                    "answer": "",
                    "route_category": "",
                    "route_intent": "",
                    "mode": "exception",
                    "language": None,
                    "latency_sec": round(elapsed, 4),
                    "wall_sec": round(elapsed, 4),
                    "validation_ok": False,
                    "strict_pass": False,
                    "failures": failures,
                    "blockers": blockers,
                    "error": repr(exc),
                    "expected_answer_status": row.get("expected_answer_status"),
                    "critical_fact": bool(row.get("critical_fact")),
                    "translation_status": row.get("translation_status"),
                }
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            handle.flush()
            latencies.append(elapsed)
            strict_pass_count += int(not failures)
            blocker_count += int(bool(blockers))
            critical = bool(row.get("critical_fact"))
            critical_total += int(critical)
            critical_pass += int(critical and not failures)
            mode_counts[record["mode"]] += 1
            category_counts[record["route_category"]] += 1
            for failure in failures:
                failure_types[failure.split(":", 1)[0]] += 1
            if index % 25 == 0 or index == len(runnable):
                print(f"progress {index}/{len(runnable)} strict_pass={strict_pass_count} p95={_percentile(latencies, 95):.3f}s", flush=True)

    total = len(runnable)
    summary = {
        "run_id": run_id,
        "corpus": str(args.corpus),
        "total_source_rows": len(rows),
        "runnable_cases": total,
        "pending_human_review": len(pending),
        "strict_pass": strict_pass_count,
        "strict_pass_rate": round(strict_pass_count / total, 6),
        "critical_total": critical_total,
        "critical_pass": critical_pass,
        "critical_pass_rate": round(critical_pass / critical_total, 6) if critical_total else None,
        "localization_blocked_cases": blocker_count,
        "latency_sec": {
            "mean": round(statistics.fmean(latencies), 4),
            "p50": round(_percentile(latencies, 50), 4),
            "p95": round(_percentile(latencies, 95), 4),
            "p99": round(_percentile(latencies, 99), 4),
            "max": round(max(latencies), 4),
            "over_10s": sum(value >= 10.0 for value in latencies),
        },
        "failure_types": dict(failure_types),
        "mode_counts": dict(mode_counts),
        "category_counts": dict(category_counts),
        "llm_enabled": args.allow_llm,
        "machine_translations_allowed": args.allow_machine_translations,
        "machine_translated_cases": sum(
            str(row.get("translation_status") or "") == "machine_translated_unreviewed"
            for row, _question_text in runnable
        ),
        "wall_sec": round(time.perf_counter() - started, 3),
        "results": str(results_path),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
