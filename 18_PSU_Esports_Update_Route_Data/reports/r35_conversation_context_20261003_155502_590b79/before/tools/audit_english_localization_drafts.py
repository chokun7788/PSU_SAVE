from __future__ import annotations

"""Audit English localization drafts without treating them as approved content.

The Local LLM can accelerate translation work, but dates, prices, names, and
conditions remain facts.  This tool catches mechanical high-risk mistakes and
creates an immutable audit artifact for a human reviewer.
"""

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260909_verified.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "reports" / "bilingual_english"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _buddhist_years(value: str) -> set[int]:
    return {int(year) for year in re.findall(r"(?<!\d)(25\d{2})(?!\d)", value or "")}


def _gregorian_years(value: str) -> set[int]:
    return {int(year) for year in re.findall(r"(?<!\d)(20\d{2})(?!\d)", value or "")}


def audit(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], Counter[str]]:
    findings: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for line_no, row in enumerate(rows, 1):
        text = str(row.get("text") or "").strip()
        source = str(row.get("source_text") or "")
        base = {
            "line": line_no,
            "content_id": str(row.get("content_id") or ""),
            "field": str(row.get("field") or ""),
            "category": str(row.get("category") or ""),
        }
        if not text:
            findings.append({**base, "severity": "error", "code": "empty_draft", "detail": "Draft has no English text."})
            counts["empty_draft"] += 1
            continue
        thai_years = _buddhist_years(source)
        expected_years = {year - 543 for year in thai_years}
        actual_years = _gregorian_years(text)
        if expected_years and actual_years and not (expected_years & actual_years):
            findings.append({
                **base,
                "severity": "error",
                "code": "buddhist_year_conversion",
                "detail": f"Thai source year(s) {sorted(thai_years)} require Gregorian {sorted(expected_years)}, but draft has {sorted(actual_years)}.",
            })
            counts["buddhist_year_conversion"] += 1
        if re.search(r"[\u0E00-\u0E7F]", text):
            findings.append({**base, "severity": "warning", "code": "thai_prose_in_english_draft", "detail": "Draft still contains Thai characters; review whether this is an allowed proper noun."})
            counts["thai_prose_in_english_draft"] += 1
        if str(row.get("status") or "draft") != "draft":
            findings.append({**base, "severity": "warning", "code": "unexpected_status", "detail": "Machine draft file contains a non-draft status."})
            counts["unexpected_status"] += 1
    return findings, counts


def repair_buddhist_year_conversions(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    """Repair only an objectively wrong B.E. to Gregorian year conversion.

    This does not approve wording, translate missing content, or modify a
    source record. It writes a new draft registry so the original model output
    remains available for audit.
    """
    repaired: list[dict[str, Any]] = []
    repair_count = 0
    for original in rows:
        row = dict(original)
        source_years = _buddhist_years(str(row.get("source_text") or ""))
        expected_years = {year - 543 for year in source_years}
        actual_years = _gregorian_years(str(row.get("text") or ""))
        if len(expected_years) == 1 and actual_years and not (expected_years & actual_years):
            expected = str(next(iter(expected_years)))
            row["text"] = re.sub(r"(?<!\d)20\d{2}(?!\d)", expected, str(row.get("text") or ""))
            row["translation_audit"] = "mechanical_buddhist_year_repair_pending_human_review"
            repair_count += 1
        repaired.append(row)
    return repaired, repair_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--repaired-output", type=Path, help="Optional new draft registry with only deterministic Buddhist-year repairs.")
    args = parser.parse_args()
    rows = _read_jsonl(args.input)
    audited_input = args.input
    repair_count = 0
    if args.repaired_output:
        repaired, repair_count = repair_buddhist_year_conversions(rows)
        args.repaired_output.parent.mkdir(parents=True, exist_ok=True)
        args.repaired_output.write_text(
            "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in repaired),
            encoding="utf-8",
        )
        rows = repaired
        audited_input = args.repaired_output
    findings, counts = audit(rows)
    output_dir = args.output_dir or DEFAULT_OUTPUT_DIR / f"localization_draft_audit_{datetime.now().strftime('%Y%m%dT%H%M%S')}"
    output_dir.mkdir(parents=True, exist_ok=False)
    (output_dir / "findings.json").write_text(json.dumps(findings, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# English Draft Localization Audit",
        "",
        "> These are machine-generated drafts. Passing this audit does not approve or publish any localization.",
        "",
        f"- Audited registry: `{audited_input}`",
        f"- Draft rows: **{len(rows)}**",
        f"- Errors: **{sum(item['severity'] == 'error' for item in findings)}**",
        f"- Warnings: **{sum(item['severity'] == 'warning' for item in findings)}**",
        "",
        "## Findings",
        "",
    ]
    if findings:
        for item in findings:
            lines.append(f"- **{item['severity'].upper()}** `{item['code']}` - `{item['content_id']}/{item['field']}`: {item['detail']}")
    else:
        lines.append("- No mechanical date/status issue found. Human factual review is still required.")
    lines.extend(["", "## Counts", "", *[f"- `{key}`: {value}" for key, value in sorted(counts.items())]])
    (output_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "findings": len(findings), "repairs": repair_count, "counts": dict(counts), "output_dir": str(output_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
