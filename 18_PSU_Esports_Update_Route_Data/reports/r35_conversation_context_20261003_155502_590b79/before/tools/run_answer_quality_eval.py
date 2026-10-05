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


CASES_PATH = ROOT / "data" / "eval" / "answer_quality_cases.jsonl"
REPORT_DIR = ROOT / "reports" / "answer_quality_eval"


def _load_cases(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def _contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def _source_text(hits: list[dict[str, Any]]) -> str:
    chunks: list[str] = []
    for hit in hits:
        chunks.extend(str(hit.get(key, "")) for key in ("id", "category", "source_url", "title", "url"))
    return " ".join(chunks)


def _format_ok(answer: str, rules: list[str]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    for rule in rules:
        if rule == "bullet" and "•" not in answer:
            missing.append("bullet")
        elif rule == "answer_first" and answer.lstrip().startswith(("รายละเอียด", "แหล่งข้อมูล")):
            missing.append("answer_first")
        elif rule == "source_last" and "แหล่งข้อมูล:" in answer and not answer.rstrip().splitlines()[-1].startswith("แหล่งข้อมูล:"):
            missing.append("source_last")
    return not missing, missing


def _trace_summary(trace: list[Any]) -> list[dict[str, Any]]:
    return [
        {
            "stage": item.stage,
            "decision": item.decision,
            "confidence": item.confidence,
            "detail": item.detail,
            "metadata": item.metadata,
        }
        for item in trace
    ]


def _evaluate_case(case: dict[str, Any], *, allow_llm: bool) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_rag_fallback=True,
        experimental_allow_llm=allow_llm,
    )
    answer = result.answer
    source_blob = _source_text(result.hits)
    must_contain = [str(item) for item in case.get("must_contain", [])]
    must_not_contain = [str(item) for item in case.get("must_not_contain", [])]
    source_keywords = [str(item) for item in case.get("source_keywords", [])]
    format_rules = [str(item) for item in case.get("format_rules", [])]
    expected_category = str(case.get("expected_category") or "")

    missing = [item for item in must_contain if not _contains(answer, item)]
    forbidden = [item for item in must_not_contain if _contains(answer, item)]
    missing_sources = [item for item in source_keywords if not _contains(source_blob, item) and not _contains(answer, item)]
    format_passed, missing_format = _format_ok(answer, format_rules)
    route_ok = not expected_category or result.route.category == expected_category
    validation_ok = result.validation.ok

    route_score = 1.5 if route_ok else 0.0
    required_score = 3.0 if not missing else max(0.0, 3.0 * (1 - (len(missing) / max(1, len(must_contain)))))
    forbidden_score = 2.0 if not forbidden else 0.0
    source_score = 1.5 if not missing_sources else max(0.0, 1.5 * (1 - (len(missing_sources) / max(1, len(source_keywords)))))
    format_score = 1.0 if format_passed else 0.0
    validation_score = 1.0 if validation_ok else 0.0
    score = round(route_score + required_score + forbidden_score + source_score + format_score + validation_score, 2)
    min_score = float(case.get("min_score", 8.0))
    passed = score >= min_score and not missing and not forbidden and route_ok and validation_ok

    intent = result.universal_intent
    return {
        "id": case.get("id"),
        "question": case.get("question"),
        "passed": passed,
        "score": score,
        "min_score": min_score,
        "route_ok": route_ok,
        "validation_ok": validation_ok,
        "missing": missing,
        "forbidden": forbidden,
        "missing_sources": missing_sources,
        "missing_format": missing_format,
        "expected_category": expected_category,
        "actual_category": result.route.category,
        "actual_intent": result.route.intent,
        "actual_domain": intent.domain if intent else "",
        "actual_operation": intent.operation if intent else "",
        "mode": result.mode,
        "confidence": result.confidence,
        "elapsed": result.elapsed,
        "answer": answer,
        "sources": result.hits,
        "notes": case.get("notes", ""),
        "trace": _trace_summary(result.trace),
    }


def _write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"answer_quality_eval_{stamp}.json"
    csv_path = REPORT_DIR / f"answer_quality_eval_{stamp}.csv"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    fields = [
        "id", "passed", "score", "min_score", "question", "expected_category",
        "actual_category", "actual_intent", "actual_domain", "actual_operation",
        "mode", "confidence", "elapsed", "missing", "forbidden",
        "missing_sources", "missing_format", "notes", "answer",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            csv_row = {field: row.get(field, "") for field in fields}
            for field in ("missing", "forbidden", "missing_sources", "missing_format"):
                csv_row[field] = json.dumps(csv_row[field], ensure_ascii=False)
            writer.writerow(csv_row)
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run answer quality evaluation.")
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
            f"[{index}/{len(cases)}] {status} {row['id']} score={row['score']}/{row['min_score']} "
            f"route={row['actual_category']}/{row['actual_intent']} mode={row['mode']} elapsed={row['elapsed']}"
        )

    json_path, csv_path = _write_reports(rows)
    passed_count = sum(1 for row in rows if row["passed"])
    failed_count = len(rows) - passed_count
    avg_score = round(sum(float(row["score"]) for row in rows) / max(1, len(rows)), 2)
    print(f"ANSWER QUALITY EVAL: {passed_count}/{len(rows)} passed, {failed_count} failed, avg_score={avg_score}")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    return 1 if failed_count and args.fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
