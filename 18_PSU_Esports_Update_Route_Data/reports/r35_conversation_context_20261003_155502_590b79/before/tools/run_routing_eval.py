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


CASES_PATH = ROOT / "data" / "routing" / "routing_eval_cases.jsonl"
REPORT_DIR = ROOT / "reports" / "routing_eval"


def _load_cases(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def _trace_summary(trace: list[Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for item in trace:
        items.append({
            "stage": item.stage,
            "decision": item.decision,
            "confidence": item.confidence,
            "detail": item.detail,
            "metadata": item.metadata,
        })
    return items


def _matches(actual: str, expected: str | None) -> bool:
    return not expected or actual == expected


def _evaluate_case(case: dict[str, Any], *, allow_llm: bool) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_rag_fallback=True,
        experimental_allow_llm=allow_llm,
    )
    intent = result.universal_intent

    actual_domain = intent.domain if intent else ""
    actual_operation = intent.operation if intent else ""
    expected_category = str(case.get("expected_category") or "")
    expected_intent = str(case.get("expected_intent") or "")
    expected_domain = str(case.get("expected_domain") or "")
    expected_operation = str(case.get("expected_operation") or "")
    must_not_category = {str(value) for value in case.get("must_not_category", [])}

    route_ok = _matches(result.route.category, expected_category) and _matches(result.route.intent, expected_intent)
    intent_ok = _matches(actual_domain, expected_domain) and _matches(actual_operation, expected_operation)
    not_forbidden = result.route.category not in must_not_category
    passed = route_ok and intent_ok and not_forbidden

    return {
        "id": case.get("id"),
        "question": case.get("question"),
        "passed": passed,
        "route_ok": route_ok,
        "intent_ok": intent_ok,
        "not_forbidden": not_forbidden,
        "expected_category": expected_category,
        "expected_intent": expected_intent,
        "expected_domain": expected_domain,
        "expected_operation": expected_operation,
        "actual_category": result.route.category,
        "actual_intent": result.route.intent,
        "actual_domain": actual_domain,
        "actual_operation": actual_operation,
        "mode": result.mode,
        "confidence": result.confidence,
        "route_confidence": result.route.confidence,
        "intent_confidence": intent.confidence if intent else None,
        "elapsed": result.elapsed,
        "answer": result.answer,
        "notes": case.get("notes", ""),
        "trace": _trace_summary(result.trace),
    }


def _write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"routing_eval_{stamp}.json"
    csv_path = REPORT_DIR / f"routing_eval_{stamp}.csv"

    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    fields = [
        "id", "passed", "route_ok", "intent_ok", "not_forbidden", "question",
        "expected_category", "expected_intent", "expected_domain", "expected_operation",
        "actual_category", "actual_intent", "actual_domain", "actual_operation",
        "mode", "confidence", "route_confidence", "intent_confidence", "elapsed", "notes", "answer",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})

    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run routing golden-set evaluation.")
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    cases = _load_cases(args.cases)
    if args.limit > 0:
        cases = cases[:args.limit]

    rows: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        row = _evaluate_case(case, allow_llm=args.allow_llm)
        rows.append(row)
        status = "PASS" if row["passed"] else "FAIL"
        print(
            f"[{index}/{len(cases)}] {status} {row['id']} "
            f"expected={row['expected_category']}/{row['expected_intent']} "
            f"actual={row['actual_category']}/{row['actual_intent']} "
            f"intent={row['actual_domain']}/{row['actual_operation']} "
            f"mode={row['mode']} elapsed={row['elapsed']}"
        )

    json_path, csv_path = _write_reports(rows)
    passed_count = sum(1 for row in rows if row["passed"])
    failed_count = len(rows) - passed_count
    print(f"ROUTING EVAL: {passed_count}/{len(rows)} passed, {failed_count} failed")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")

    if failed_count and args.fail_on_error:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
