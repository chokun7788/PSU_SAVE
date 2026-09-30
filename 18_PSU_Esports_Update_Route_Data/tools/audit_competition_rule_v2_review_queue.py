"""Validate the v2 competition-rule review queue and create a quality report."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "competition_rules" / "review" / "competition_rule_claim_v2_review_queue.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def issue_codes(row: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    source = row.get("source") if isinstance(row.get("source"), dict) else {}
    claim = row.get("claim") if isinstance(row.get("claim"), dict) else {}
    retrieval = row.get("retrieval") if isinstance(row.get("retrieval"), dict) else {}
    evidence = row.get("evidence") if isinstance(row.get("evidence"), dict) else {}
    quality = row.get("quality") if isinstance(row.get("quality"), dict) else {}
    if row.get("schema_version") != "competition_rule_claim_v2":
        issues.append("invalid_schema_version")
    if not row.get("claim_id") or not source.get("source_chunk_id"):
        issues.append("missing_stable_identifier")
    if not source.get("clause_th") or not source.get("clause_sha256"):
        issues.append("missing_source_clause_or_hash")
    if claim.get("statement_th") != source.get("clause_th"):
        issues.append("claim_not_equal_to_source_clause")
    if not retrieval.get("game") or not retrieval.get("game_id"):
        issues.append("missing_game_target")
    if not retrieval.get("canonical_section_proposed") or not retrieval.get("facet_proposed"):
        issues.append("missing_proposed_facet")
    if evidence.get("support_mode") != "exact_source_clause_required":
        issues.append("unsafe_evidence_mode")
    if source.get("source_chunk_id") not in set(evidence.get("source_refs") or []):
        issues.append("missing_self_source_reference")
    if quality.get("heading_clause_relation") == "same_field_ambiguous":
        issues.append("heading_and_clause_not_separated")
    if quality.get("atomicity") != "verified":
        issues.append("atomicity_review_required")
    if claim.get("answer_en") and claim.get("answer_en_status") != "approved":
        issues.append("english_not_approved")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the non-runtime competition-rule claim v2 review queue.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "reports" / "competition_rules_rag_eval" / "rule_v2_format_audit")
    args = parser.parse_args()

    rows = read_jsonl(args.input)
    seen: set[str] = set()
    report_rows: list[dict[str, Any]] = []
    for row in rows:
        issues = issue_codes(row)
        claim_id = str(row.get("claim_id") or "")
        if claim_id in seen:
            issues.append("duplicate_claim_id")
        seen.add(claim_id)
        report_rows.append({
            "claim_id": claim_id,
            "source_chunk_id": str((row.get("source") or {}).get("source_chunk_id") or ""),
            "game": str((row.get("retrieval") or {}).get("game") or ""),
            "issues": issues,
        })

    counts = Counter(issue for row in report_rows for issue in row["issues"])
    by_game = Counter(row["game"] for row in report_rows)
    by_facet = Counter(
        str((source_row.get("retrieval") or {}).get("facet_proposed") or "unknown")
        for source_row in rows
    )
    priority_facets = (
        "penalty",
        "penalty_matrix",
        "protest_dispute",
        "dispute",
        "disconnect",
        "team_size",
        "pause_timeout",
        "match_settings",
        "match_configuration",
        "in_match_operations",
    )
    prioritized = [
        row for row, source_row in zip(report_rows, rows)
        if str((source_row.get("retrieval") or {}).get("facet_proposed") or "") in priority_facets
    ]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "rule_v2_format_audit.json").write_text(json.dumps({
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "input": str(args.input),
        "claims": len(report_rows),
        "issue_counts": dict(counts),
        "counts_by_game": dict(by_game),
        "counts_by_facet": dict(by_facet),
        "priority_claim_ids": [row["claim_id"] for row in prioritized],
        "rows": report_rows,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = [
        "# Competition Rule V2 Format Audit",
        "",
        "> This report is a review backlog. It does not authorize runtime publication.",
        "",
        f"- Claims: **{len(report_rows)}**",
        f"- Issue counts: `{dict(counts)}`",
        f"- Counts by game: `{dict(by_game)}`",
        f"- High-priority claims: **{len(prioritized)}**",
        "",
        "## Review Order",
        "",
        "1. Penalty/penalty matrix and protest/dispute claims.",
        "2. Disconnect, pause and in-match operation claims.",
        "3. Team-size and match-setting/configuration claims.",
        "4. Remaining identity, registration, schedule, equipment and conduct claims.",
        "",
        "## Counts by Facet",
        "",
        *[f"- `{facet}`: {count}" for facet, count in sorted(by_facet.items())],
        "",
        "## Interpretation",
        "",
        "- `heading_and_clause_not_separated`: importer currently stores a heading and the answerable clause in one field.",
        "- `atomicity_review_required`: a reviewer must confirm whether one source chunk expresses exactly one answerable claim.",
        "- `english_not_approved`: an English draft exists but cannot be published until a named reviewer approves it.",
        "",
    ]
    (args.output_dir / "rule_v2_format_audit.md").write_text("\n".join(markdown), encoding="utf-8")
    print(json.dumps({"claims": len(report_rows), "issue_counts": dict(counts), "output_dir": str(args.output_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
