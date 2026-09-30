#!/usr/bin/env python3
"""Classify competition-rule evaluation failures without altering raw results."""

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
DEFAULT_REPORT_DIR = ROOT / "reports" / "competition_rules_rag_eval"


def _classification(row: dict[str, Any]) -> tuple[str, str]:
    """Return a durable triage class and its evidence-based explanation."""
    mode = str(row.get("mode") or "")
    failures = " ".join(str(item) for item in row.get("failures") or ())
    expected_status = str(row.get("expected_answer_status") or "")
    actual_status = str(row.get("actual_status") or "")
    expected_runtime_status = {
        "answer_available": "answer",
        "clarification_required": "clarification",
        "no_answer_expected": "no_answer",
    }.get(expected_status, expected_status)

    if "localization_pending" in mode or "missing_english_localization" in mode:
        return (
            "english_localization_gap",
            "The Thai target source was found, but no approved English overlay was available.",
        )
    if "facet_not_covered" in mode:
        return (
            "source_coverage_gap",
            "The selected rulebook has no retrieved section that directly proves the requested facet.",
        )
    if not bool(row.get("route_ok")) or not bool(row.get("target_ok")):
        return (
            "routing_or_target_failure",
            "The request did not retain the expected competition route or rulebook target.",
        )
    if expected_runtime_status != actual_status:
        return (
            "safe_outcome_contract_gap",
            "The runtime safe outcome differs from the Gold-required answer, clarification, or no-answer status.",
        )
    if "retrieval evidence did not match" in failures:
        return (
            "gold_or_section_contract_gap",
            "The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.",
        )
    if not bool(row.get("validation_ok")):
        return (
            "answer_contract_failure",
            "The validator rejected the generated answer despite the selected route/evidence.",
        )
    return (
        "needs_manual_trace_review",
        "The report does not contain enough structured evidence to classify the failure automatically.",
    )


def _read_rows(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        content = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(content, list):
            raise ValueError(f"Expected a JSON array: {path}")
        for row in content:
            if isinstance(row, dict):
                rows.append({**row, "_report_file": path.name})
    return rows


def _markdown(rows: list[dict[str, Any]], source_paths: list[Path]) -> str:
    by_locale: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_locale[str(row.get("locale") or "unknown")].append(row)

    lines = [
        "# Competition Rules RAG: Automated Failure Triage",
        "",
        "## Input Reports",
        "",
        *[f"- `{path.name}`" for path in source_paths],
        "",
        "## Summary",
        "",
        "| Locale | Passed | Total | Failed |",
        "| --- | ---: | ---: | ---: |",
    ]
    for locale in sorted(by_locale):
        locale_rows = by_locale[locale]
        failed = sum(not bool(row.get("passed")) for row in locale_rows)
        lines.append(f"| {locale} | {len(locale_rows) - failed} | {len(locale_rows)} | {failed} |")

    failed_rows = [row for row in rows if not bool(row.get("passed"))]
    class_counts = Counter(row["triage_class"] for row in failed_rows)
    lines.extend([
        "",
        "## Failure Taxonomy",
        "",
        "| Classification | Count | Meaning |",
        "| --- | ---: | --- |",
    ])
    for category, count in class_counts.most_common():
        exemplar = next(row for row in failed_rows if row["triage_class"] == category)
        lines.append(f"| `{category}` | {count} | {exemplar['triage_reason']} |")

    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in failed_rows:
        grouped[(str(row.get("locale")), row["triage_class"], str(row.get("expected_facet") or "safe_outcome"))].append(row)

    lines.extend(["", "## Review Queue", ""])
    for (locale, category, facet), items in sorted(grouped.items()):
        lines.append(f"### {locale} / {category} / {facet} ({len(items)} cases)")
        lines.append("")
        for row in items:
            answer = " ".join(str(row.get("answer") or "").splitlines())
            if len(answer) > 260:
                answer = answer[:257] + "..."
            lines.extend([
                f"- `{row.get('id')}` — {row.get('question')}",
                f"  - Expected: `{row.get('expected_answer_status')}`; actual: `{row.get('actual_status')}` via `{row.get('mode')}`",
                f"  - Reason: {row['triage_reason']}",
                f"  - Output: {answer or '(empty)'}",
            ])
        lines.append("")

    lines.extend([
        "## Next Action by Class",
        "",
        "- `routing_or_target_failure`: inspect Question Frame and target lock before touching retrieval.",
        "- `source_coverage_gap`: add or approve a source section; keep the safe no-answer until then.",
        "- `gold_or_section_contract_gap`: review section bundles and create reviewed Gold, without widening current Gold silently.",
        "- `english_localization_gap`: approve an English overlay tied to the current Thai source hash.",
        "- `safe_outcome_contract_gap`: decide whether the corpus expects clarification or no-answer, then make that distinction explicit.",
        "- `answer_contract_failure`: inspect the validator error and evidence metadata before changing wording.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify existing competition RAG JSON reports.")
    parser.add_argument("--report", type=Path, action="append", required=True, help="Detail JSON report; may be repeated.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_REPORT_DIR)
    args = parser.parse_args()

    report_paths = [path.resolve() for path in args.report]
    rows = _read_rows(report_paths)
    for row in rows:
        category, reason = _classification(row)
        row["triage_class"] = category
        row["triage_reason"] = reason

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = args.output_dir / f"competition_rules_rag_triage_{stamp}.json"
    markdown_path = args.output_dir / f"competition_rules_rag_triage_{stamp}.md"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown_path.write_text(_markdown(rows, report_paths), encoding="utf-8")

    counts = Counter(row["triage_class"] for row in rows if not bool(row.get("passed")))
    print(f"TRIAGED: {len(rows)} rows; failed={sum(counts.values())}; classes={dict(counts)}")
    print(f"JSON: {json_path}")
    print(f"MARKDOWN: {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
