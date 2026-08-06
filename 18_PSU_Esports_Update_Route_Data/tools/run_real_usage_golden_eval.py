from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


CASES_PATH = ROOT / "data" / "eval" / "real_usage_golden_v1.jsonl"
REPORT_DIR = ROOT / "reports" / "real_usage_golden_eval"


def load_cases(path: Path = CASES_PATH) -> list[dict[str, Any]]:
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


def _contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def _source_text(hits: list[dict[str, Any]]) -> str:
    chunks: list[str] = []
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata", {}) if isinstance(hit.get("metadata"), dict) else {}
        for key in ("id", "category", "source_type", "source_url", "title", "url"):
            chunks.append(str(hit.get(key, "")))
            chunks.append(str(metadata.get(key, "")))
        source_ids = metadata.get("source_ids")
        if isinstance(source_ids, list):
            chunks.extend(str(item) for item in source_ids)
    return " ".join(chunks)


def _trace_summary(trace: list[Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in trace:
        rows.append({
            "stage": getattr(item, "stage", ""),
            "decision": getattr(item, "decision", ""),
            "confidence": getattr(item, "confidence", ""),
            "detail": getattr(item, "detail", ""),
            "metadata": getattr(item, "metadata", {}),
        })
    return rows


def evaluate_case(
    case: dict[str, Any],
    *,
    allow_llm: bool = False,
    rag_fallback: bool = False,
    include_trace: bool = False,
) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_rag_fallback=rag_fallback,
        experimental_allow_llm=allow_llm,
    )
    answer = result.answer or ""
    source_blob = _source_text(result.hits)
    intent = result.universal_intent

    expected_category = str(case.get("expected_category") or "")
    expected_intent = str(case.get("expected_intent") or "")
    expected_mode_prefix = str(case.get("expected_mode_prefix") or "")
    must_contain = [str(item) for item in case.get("must_contain", [])]
    must_not_contain = [str(item) for item in case.get("must_not_contain", [])]
    source_keywords = [str(item) for item in case.get("source_keywords", [])]
    must_not_category = {str(item) for item in case.get("must_not_category", [])}

    missing = [item for item in must_contain if not _contains(answer, item)]
    forbidden = [item for item in must_not_contain if _contains(answer, item)]
    missing_sources = [item for item in source_keywords if not _contains(source_blob, item) and not _contains(answer, item)]
    category_ok = not expected_category or result.route.category == expected_category
    intent_ok = not expected_intent or result.route.intent == expected_intent
    mode_ok = not expected_mode_prefix or result.mode.startswith(expected_mode_prefix)
    not_forbidden_category = result.route.category not in must_not_category
    validation_ok = result.validation.ok

    failures: list[str] = []
    if not category_ok:
        failures.append(f"category expected {expected_category}, got {result.route.category}")
    if not intent_ok:
        failures.append(f"intent expected {expected_intent}, got {result.route.intent}")
    if not mode_ok:
        failures.append(f"mode expected prefix {expected_mode_prefix}, got {result.mode}")
    if not not_forbidden_category:
        failures.append(f"forbidden category {result.route.category}")
    if missing:
        failures.append(f"missing answer keywords: {missing}")
    if forbidden:
        failures.append(f"forbidden answer keywords: {forbidden}")
    if missing_sources:
        failures.append(f"missing source keywords: {missing_sources}")
    if not validation_ok:
        failures.append(f"validation errors: {result.validation.errors}")

    return {
        "id": case.get("id"),
        "group": case.get("group"),
        "question": case.get("question"),
        "passed": not failures,
        "failures": failures,
        "expected_category": expected_category,
        "expected_intent": expected_intent,
        "expected_mode_prefix": expected_mode_prefix,
        "actual_category": result.route.category,
        "actual_intent": result.route.intent,
        "actual_domain": intent.domain if intent else "",
        "actual_operation": intent.operation if intent else "",
        "mode": result.mode,
        "confidence": result.confidence,
        "elapsed": result.elapsed,
        "validation_ok": validation_ok,
        "missing": missing,
        "forbidden": forbidden,
        "missing_sources": missing_sources,
        "answer": answer,
        "notes": case.get("notes", ""),
        "trace": _trace_summary(result.trace) if include_trace else None,
    }


def run_cases(
    cases: list[dict[str, Any]],
    *,
    allow_llm: bool = False,
    rag_fallback: bool = False,
    include_trace: bool = False,
) -> list[dict[str, Any]]:
    return [
        evaluate_case(case, allow_llm=allow_llm, rag_fallback=rag_fallback, include_trace=include_trace)
        for case in cases
    ]


def _write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"real_usage_golden_eval_{stamp}.json"
    csv_path = REPORT_DIR / f"real_usage_golden_eval_{stamp}.csv"
    summary_path = REPORT_DIR / f"real_usage_golden_eval_{stamp}_summary.json"

    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = [
        "id", "group", "passed", "question", "expected_category", "expected_intent",
        "actual_category", "actual_intent", "actual_domain", "actual_operation",
        "mode", "confidence", "elapsed", "validation_ok", "failures", "missing",
        "forbidden", "missing_sources", "notes", "answer",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            csv_row = {field: row.get(field, "") for field in fields}
            for field in ("failures", "missing", "forbidden", "missing_sources"):
                csv_row[field] = json.dumps(csv_row[field], ensure_ascii=False)
            writer.writerow(csv_row)

    group_counts: dict[str, dict[str, int]] = {}
    for row in rows:
        group = str(row.get("group") or "unknown")
        item = group_counts.setdefault(group, {"passed": 0, "failed": 0})
        item["passed" if row["passed"] else "failed"] += 1
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(rows),
        "passed": sum(1 for row in rows if row["passed"]),
        "failed": sum(1 for row in rows if not row["passed"]),
        "group_counts": group_counts,
        "json": str(json_path),
        "csv": str(csv_path),
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return json_path, csv_path, summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run real-usage golden regression cases for PSU Esports chatbot.")
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--group", default="", help="run only one case group")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--include-trace", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    cases = load_cases(args.cases)
    if args.group:
        cases = [case for case in cases if str(case.get("group")) == args.group]
    if args.limit > 0:
        cases = cases[:args.limit]

    rows: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        row = evaluate_case(
            case,
            allow_llm=args.allow_llm,
            rag_fallback=args.rag_fallback,
            include_trace=args.include_trace,
        )
        rows.append(row)
        status = "PASS" if row["passed"] else "FAIL"
        print(
            f"[{index}/{len(cases)}] {status} {row['id']} "
            f"route={row['actual_category']}/{row['actual_intent']} "
            f"mode={row['mode']} elapsed={row['elapsed']}"
        )
        if row["failures"]:
            for failure in row["failures"]:
                print(f"  - {failure}")

    json_path, csv_path, summary_path = _write_reports(rows)
    passed = sum(1 for row in rows if row["passed"])
    failed = len(rows) - passed
    print(f"REAL USAGE GOLDEN EVAL: {passed}/{len(rows)} passed, {failed} failed")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    print(f"SUMMARY: {summary_path}")
    return 1 if failed and args.fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
