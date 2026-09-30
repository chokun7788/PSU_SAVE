from __future__ import annotations

"""Rescore an existing bilingual evaluation without rerunning the pipeline.

Raw run output is immutable.  This is used when an evaluator defect is fixed
and lets us distinguish a scoring correction from a behavioral change.
"""

import argparse
import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.locale import contains_thai_prose
from tools.run_bilingual_english_eval import _expected_categories


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def percentile(values: list[float], percent: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    position = max(0, min(len(ordered) - 1, math.ceil(len(ordered) * percent / 100) - 1))
    return ordered[position]


def failures_for(row: dict[str, Any], result: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    answer = str(result.get("answer") or "")
    answer_lower = answer.casefold()
    allowed_categories = _expected_categories(row)
    actual_category = str(result.get("route_category") or "")
    if allowed_categories and actual_category not in allowed_categories:
        failures.append(f"category:{actual_category} not in {allowed_categories}")
    language = result.get("language") or {}
    if language.get("effective") != "en":
        failures.append("effective_language_not_en")
    if contains_thai_prose(answer):
        failures.append("thai_prose_leak")
    if float(result.get("latency_sec") or 0.0) >= float(row.get("latency_ceiling_sec") or 10.0):
        failures.append(f"latency:{float(result.get('latency_sec') or 0.0):.4f}")
    if result.get("mode") == "pipeline:request_timeout_no_answer":
        failures.append("pipeline_timeout")
    if not bool(result.get("validation_ok")):
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
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Rescore a bilingual run from raw outputs after an evaluator-only fix.")
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    source = {str(row.get("id") or ""): row for row in read_jsonl(args.corpus)}
    raw = read_jsonl(args.results)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    output_rows: list[dict[str, Any]] = []
    failures = Counter()
    latencies: list[float] = []
    old_pass = 0
    corrected_pass = 0
    changed_cases: list[str] = []

    for record in raw:
        case_id = str(record.get("id") or "")
        if case_id not in source:
            raise SystemExit(f"Result ID missing from corpus: {case_id}")
        corrected_failures = failures_for(source[case_id], record)
        corrected = not corrected_failures
        old = bool(record.get("strict_pass"))
        old_pass += int(old)
        corrected_pass += int(corrected)
        if old != corrected:
            changed_cases.append(case_id)
        for failure in corrected_failures:
            failures[failure.split(":", 1)[0]] += 1
        latencies.append(float(record.get("latency_sec") or 0.0))
        output_rows.append({
            **record,
            "raw_strict_pass": old,
            "rescored_strict_pass": corrected,
            "rescored_failures": corrected_failures,
            "allowed_categories": _expected_categories(source[case_id]),
        })

    rescored_path = args.output_dir / "rescored_results.jsonl"
    rescored_path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in output_rows),
        encoding="utf-8",
    )
    total = len(output_rows)
    summary = {
        "purpose": "Evaluator-only correction. Pipeline answers, modes, and latencies were not rerun or changed.",
        "corpus": str(args.corpus),
        "raw_results": str(args.results),
        "total_cases": total,
        "raw_strict_pass": old_pass,
        "raw_strict_pass_rate": round(old_pass / total, 6) if total else None,
        "rescored_strict_pass": corrected_pass,
        "rescored_strict_pass_rate": round(corrected_pass / total, 6) if total else None,
        "cases_changed_by_scoring_fix": len(changed_cases),
        "rescored_failure_types": dict(failures),
        "latency_sec": {
            "p50": round(percentile(latencies, 50), 4),
            "p95": round(percentile(latencies, 95), 4),
            "p99": round(percentile(latencies, 99), 4),
            "max": round(max(latencies), 4) if latencies else 0.0,
        },
        "rescored_results": str(rescored_path),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
