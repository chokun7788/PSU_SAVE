#!/usr/bin/env python3
"""Summarize a RAG robustness evaluation detail JSON into a reviewable report."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "rag_robustness_eval"


def latest_detail_file() -> Path:
    files = sorted(
        (
            path for path in REPORT_DIR.glob("rag_robustness_eval_*.json")
            if not path.name.endswith("_summary.json")
        ),
        key=lambda path: path.stat().st_mtime,
    )
    if not files:
        raise FileNotFoundError(f"No robustness detail report exists in {REPORT_DIR}")
    return files[-1]


def load_rows(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return [row for row in data if isinstance(row, dict)]


def failure_kind(failure: str) -> str:
    if failure.startswith("route expected"):
        return "route_mismatch"
    if failure.startswith("outcome expected"):
        return "safe_outcome_mismatch"
    if failure.startswith("validation errors"):
        return "answer_validation_failed"
    if failure.startswith("latency "):
        return "latency_exceeded"
    return "other"


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, int((len(ordered) * fraction + 0.999999)) - 1))
    return ordered[index]


def markdown(rows: list[dict[str, Any]], source: Path) -> str:
    total = len(rows)
    passed = sum(bool(row.get("passed")) for row in rows)
    failed = total - passed
    locale_rows = {locale: [row for row in rows if row.get("locale") == locale] for locale in ("th", "en")}
    failure_counts = Counter(
        failure_kind(str(failure))
        for row in rows for failure in (row.get("failures") or [])
    )
    group_counts: dict[str, dict[str, int]] = {}
    category_pairs = Counter()
    for row in rows:
        group = str(row.get("group") or "unknown")
        counts = group_counts.setdefault(group, {"passed": 0, "failed": 0})
        counts["passed" if row.get("passed") else "failed"] += 1
        if not row.get("route_ok"):
            category_pairs[(str(row.get("actual_category")), " | ".join(row.get("expected_route_categories") or []))] += 1

    lines = [
        "# RAG Robustness Evaluation Analysis",
        "",
        f"- Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"- Detail input: `{source}`",
        f"- Evaluated: {total}",
        f"- Passed: {passed} ({(passed / total * 100) if total else 0:.2f}%)",
        f"- Failed: {failed} ({(failed / total * 100) if total else 0:.2f}%)",
        "",
        "## Locale Comparison",
        "",
        "| Locale | Cases | Passed | Failed | Pass rate |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for locale, locale_data in locale_rows.items():
        locale_passed = sum(bool(row.get("passed")) for row in locale_data)
        lines.append(
            f"| {locale} | {len(locale_data)} | {locale_passed} | {len(locale_data) - locale_passed} | "
            f"{(locale_passed / len(locale_data) * 100) if locale_data else 0:.2f}% |"
        )

    lines.extend([
        "", "## Latency", "",
        "| Locale | P50 | P95 | P99 | Max | >10s | >20s |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ])
    for locale, locale_data in {"all": rows, **locale_rows}.items():
        values = [float(row.get("elapsed_sec") or 0) for row in locale_data]
        lines.append(
            f"| {locale} | {percentile(values, .50):.3f}s | {percentile(values, .95):.3f}s | "
            f"{percentile(values, .99):.3f}s | {max(values, default=0):.3f}s | "
            f"{sum(value > 10 for value in values)} | {sum(value > 20 for value in values)} |"
        )

    lines.extend(["", "## Failure Taxonomy", ""])
    for kind, count in failure_counts.most_common():
        lines.append(f"- `{kind}`: {count}")

    lines.extend(["", "## Results by Group", "", "| Group | Passed | Failed | Pass rate |", "| --- | ---: | ---: | ---: |"])
    for group, counts in sorted(group_counts.items()):
        group_total = counts["passed"] + counts["failed"]
        lines.append(
            f"| {group} | {counts['passed']} | {counts['failed']} | {counts['passed'] / group_total * 100:.2f}% |"
        )

    lines.extend(["", "## Most Frequent Route Mismatches", ""])
    if category_pairs:
        for (actual, expected), count in category_pairs.most_common(12):
            lines.append(f"- `{actual}` instead of `{expected}`: {count}")
    else:
        lines.append("- No route mismatch observed.")

    lines.extend(["", "## Slowest Cases", "", "| Case | Locale | Group | Elapsed | Route | Status | Question |", "| --- | --- | --- | ---: | --- | --- | --- |"])
    for row in sorted(rows, key=lambda item: float(item.get("elapsed_sec") or 0), reverse=True)[:15]:
        question = " ".join(str(row.get("question") or "").split()).replace("|", "\\|")
        lines.append(
            f"| {row.get('id')} | {row.get('locale')} | {row.get('group')} | {float(row.get('elapsed_sec') or 0):.3f}s | "
            f"{row.get('actual_category')} | {row.get('actual_status')} | {question} |"
        )

    lines.extend(["", "## Representative Failures", ""])
    failures = [row for row in rows if not row.get("passed")]
    for row in failures[:20]:
        expectation = ", ".join(row.get("expected_route_categories") or [])
        answer = " ".join(str(row.get("answer") or "").split())
        if len(answer) > 360:
            answer = f"{answer[:357]}..."
        lines.extend([
            f"### {row.get('id')} ({row.get('locale')}, {row.get('group')})",
            f"- Question: {row.get('question')}",
            f"- Expected: route `{expectation}`; outcome `{row.get('expected_answer_status')}`",
            f"- Actual: route `{row.get('actual_category')}`; outcome `{row.get('actual_status')}`; mode `{row.get('mode')}`; {float(row.get('elapsed_sec') or 0):.3f}s",
            f"- Failure: {'; '.join(str(item) for item in row.get('failures', []))}",
            f"- Answer excerpt: {answer or '[empty]'}",
            "",
        ])
    if not failures:
        lines.append("No failed cases were recorded.")

    lines.extend([
        "## Interpretation",
        "",
        "- This report scores routing, safe outcome, validation and latency. It does not claim that passing prose is fully owner-approved factual content.",
        "- `live_lookup_required` verifies that the pipeline provides a safe non-stale response path; availability accuracy additionally requires a reachable live booking source.",
        "- Use failures with their trace in the detail JSON to prioritize fixes. Do not weaken expected routes merely to raise the score unless the runtime route contract has deliberately changed.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a RAG robustness detail JSON report.")
    parser.add_argument("--input", type=Path, default=None)
    args = parser.parse_args()
    input_path = args.input or latest_detail_file()
    rows = load_rows(input_path)
    output_path = input_path.with_name(f"{input_path.stem}_analysis.md")
    output_path.write_text(markdown(rows, input_path), encoding="utf-8")
    print(f"Analysis: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
