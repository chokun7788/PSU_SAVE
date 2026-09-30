#!/usr/bin/env python3
"""Validate and publish owner-approved competition-rule V2.1 claims.

Draft review rows and runtime rows intentionally use separate schemas.  This
tool is the only supported conversion boundary; it never promotes a pending
row and never treats a draft English translation as approved evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.pipeline.chatbot_role import CHATBOT_PROMPT_VERSION
from app.pipeline.competition_claim_contract import numeric_tokens
from app.pipeline.competition_taxonomy import COMPETITION_TAXONOMY_VERSION


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data" / "competition_rules" / "review"
DEFAULT_QUEUE = REVIEW_DIR / "competition_rule_claim_v2_review_queue.jsonl"
REVIEW_SCHEMA = REVIEW_DIR / "competition_rule_claim_v2_review.schema.json"
RUNTIME_SCHEMA = REVIEW_DIR / "competition_rule_claim_v2_1_runtime.schema.json"


@dataclass(frozen=True)
class ClaimValidationReport:
    records: int
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    status_counts: dict[str, int]

    @property
    def ok(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict[str, Any]:
        return {
            "records": self.records,
            "ok": self.ok,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "status_counts": dict(self.status_counts),
        }


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON object required: {path}")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"Object required at {path}:{line_number}")
        rows.append(row)
    return rows


def _json_path(parts: Iterable[Any]) -> str:
    value = ".".join(str(part) for part in parts)
    return value or "$"


def _source_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_review_rows(rows: list[dict[str, Any]]) -> ClaimValidationReport:
    validator = Draft202012Validator(read_json(REVIEW_SCHEMA), format_checker=FormatChecker())
    errors: list[str] = []
    warnings: list[str] = []
    status_counts: Counter[str] = Counter()
    claim_ids: set[str] = set()
    source_ids: set[str] = set()

    for index, row in enumerate(rows, 1):
        marker = str(row.get("claim_id") or f"row:{index}")
        for error in sorted(validator.iter_errors(row), key=lambda item: tuple(item.absolute_path)):
            errors.append(f"{marker}:{_json_path(error.absolute_path)}: {error.message}")

        claim_id = str(row.get("claim_id") or "")
        if claim_id in claim_ids:
            errors.append(f"{marker}: duplicate claim_id")
        claim_ids.add(claim_id)

        source = row.get("source") if isinstance(row.get("source"), dict) else {}
        source_id = str(source.get("source_chunk_id") or "")
        if source_id in source_ids:
            warnings.append(f"{marker}: duplicate source_chunk_id {source_id}; split claims must use unique claim IDs")
        source_ids.add(source_id)
        clause = str(source.get("clause_th") or "")
        expected_hash = _source_hash(clause) if clause else ""
        if expected_hash and str(source.get("clause_sha256") or "") != expected_hash:
            errors.append(f"{marker}: source.clause_sha256 does not match clause_th")

        evidence = row.get("evidence") if isinstance(row.get("evidence"), dict) else {}
        refs = evidence.get("source_refs") if isinstance(evidence.get("source_refs"), list) else []
        if source_id and source_id not in refs:
            errors.append(f"{marker}: evidence.source_refs does not include source_chunk_id")

        approval = row.get("approval") if isinstance(row.get("approval"), dict) else {}
        quality = row.get("quality") if isinstance(row.get("quality"), dict) else {}
        claim = row.get("claim") if isinstance(row.get("claim"), dict) else {}
        review_status = str(approval.get("review_status") or "unknown")
        status_counts[review_status] += 1
        if review_status == "approved":
            if row.get("status") != "approved":
                errors.append(f"{marker}: owner-approved row must have status=approved")
            if quality.get("atomicity") != "verified":
                errors.append(f"{marker}: owner-approved row must have atomicity=verified")
            if quality.get("heading_clause_relation") != "separated":
                errors.append(f"{marker}: owner-approved row must separate heading and clause")
            if not str(claim.get("answer_th") or "").strip():
                errors.append(f"{marker}: owner-approved row requires answer_th")
            if not str(approval.get("approved_by") or "").strip() or not str(approval.get("approved_at") or "").strip():
                errors.append(f"{marker}: owner-approved row requires reviewer and timestamp")

        if claim.get("answer_en_status") == "approved":
            if approval.get("english_review_status") != "approved":
                errors.append(f"{marker}: approved English requires english_review_status=approved")
            if not str(approval.get("english_approved_by") or "").strip() or not str(approval.get("english_approved_at") or "").strip():
                errors.append(f"{marker}: approved English requires reviewer and timestamp")

    return ClaimValidationReport(
        records=len(rows),
        errors=tuple(errors),
        warnings=tuple(warnings),
        status_counts=dict(status_counts),
    )


def _nullable(value: Any) -> str | None:
    text = str(value or "").strip()
    return text or None


def _runtime_claim_id(review_claim_id: str) -> str:
    value = review_claim_id.removeprefix("review::")
    return "rule::" + value


def is_publishable(row: dict[str, Any]) -> tuple[bool, tuple[str, ...]]:
    reasons: list[str] = []
    approval = row.get("approval") if isinstance(row.get("approval"), dict) else {}
    quality = row.get("quality") if isinstance(row.get("quality"), dict) else {}
    claim = row.get("claim") if isinstance(row.get("claim"), dict) else {}
    if row.get("status") != "approved":
        reasons.append("record_not_approved")
    if approval.get("review_status") != "approved":
        reasons.append("owner_review_pending")
    if quality.get("atomicity") != "verified":
        reasons.append("atomicity_not_verified")
    if quality.get("heading_clause_relation") != "separated":
        reasons.append("heading_clause_not_separated")
    if not str(claim.get("answer_th") or "").strip():
        reasons.append("thai_answer_missing")
    if not str(approval.get("approved_by") or "").strip() or not str(approval.get("approved_at") or "").strip():
        reasons.append("owner_approval_identity_missing")
    return not reasons, tuple(reasons)


def convert_review_row(row: dict[str, Any], *, release_id: str) -> dict[str, Any]:
    publishable, reasons = is_publishable(row)
    if not publishable:
        raise ValueError(f"{row.get('claim_id')}: not publishable: {', '.join(reasons)}")

    source = row["source"]
    claim = row["claim"]
    retrieval = row["retrieval"]
    evidence = row["evidence"]
    quality = row["quality"]
    approval = row["approval"]
    english_approved = (
        claim.get("answer_en_status") == "approved"
        and approval.get("english_review_status") == "approved"
        and bool(str(approval.get("english_approved_by") or "").strip())
        and bool(str(approval.get("english_approved_at") or "").strip())
    )
    claim_id = _runtime_claim_id(str(row["claim_id"]))
    return {
        "schema_version": "competition_rule_claim_v2_1",
        "claim_id": claim_id,
        "release_id": release_id,
        "status": "approved",
        "answerable": True,
        "source": {
            "document_id": source["document_id"],
            "source_chunk_id": source["source_chunk_id"],
            "source_url": source["source_url"],
            "source_file": source["source_file"],
            "source_version": source["document_id"],
            "source_priority": approval.get("source_priority") or "imported_legacy_document",
            "heading_th": source["heading_th"],
            "clause_th": source["clause_th"],
            "clause_sha256": source["clause_sha256"],
        },
        "claim": {
            "proposition_id": claim_id,
            "statement_th": claim["statement_th"],
            "answer_th": claim["answer_th"],
            "answer_en": claim["answer_en"] if english_approved else None,
            "english_status": "approved" if english_approved else "missing",
            "structured_values": claim.get("structured_values") or [],
        },
        "retrieval": {
            "game_id": retrieval["game_id"],
            "canonical_section": retrieval["canonical_section_proposed"],
            "facet": retrieval["facet_proposed"],
            "aliases_th": retrieval["aliases_th"],
            "aliases_en": retrieval["aliases_en"],
            "question_patterns_th": retrieval["question_patterns_th"],
            "question_patterns_en": retrieval["question_patterns_en"],
        },
        "evidence": {
            "mode": "exact_source_clause",
            "source_refs": evidence["source_refs"],
            "source_span_sha256": source["clause_sha256"],
            "evidence_links": evidence["evidence_links"],
        },
        "lifecycle": {
            "effective_from": _nullable(approval.get("effective_from")),
            "effective_to": _nullable(approval.get("effective_to")),
            "supersedes_claim_id": approval.get("supersedes_claim_id"),
            "conflicts_with": approval.get("conflicts_with") or [],
        },
        "quality": {
            "atomicity": "verified",
            "heading_clause_relation": "separated",
            "completeness": approval.get("completeness") or "direct",
        },
        "approval": {
            "thai_status": "approved",
            "approved_by": approval["approved_by"],
            "approved_at": approval["approved_at"],
            "english_status": "approved" if english_approved else "missing",
            "english_approved_by": approval.get("english_approved_by") if english_approved else None,
            "english_approved_at": approval.get("english_approved_at") if english_approved else None,
        },
    }


def validate_runtime_rows(rows: list[dict[str, Any]]) -> ClaimValidationReport:
    validator = Draft202012Validator(read_json(RUNTIME_SCHEMA), format_checker=FormatChecker())
    errors: list[str] = []
    claim_ids: set[str] = set()
    propositions: set[str] = set()
    all_claim_ids = {str(row.get("claim_id") or "") for row in rows}
    status_counts: Counter[str] = Counter()
    for index, row in enumerate(rows, 1):
        marker = str(row.get("claim_id") or f"row:{index}")
        for error in sorted(validator.iter_errors(row), key=lambda item: tuple(item.absolute_path)):
            errors.append(f"{marker}:{_json_path(error.absolute_path)}: {error.message}")
        claim_id = str(row.get("claim_id") or "")
        proposition = str((row.get("claim") or {}).get("proposition_id") or "")
        if claim_id in claim_ids:
            errors.append(f"{marker}: duplicate claim_id")
        if proposition in propositions:
            errors.append(f"{marker}: duplicate proposition_id")
        claim_ids.add(claim_id)
        propositions.add(proposition)
        status_counts[str(row.get("status") or "unknown")] += 1
        source = row.get("source") if isinstance(row.get("source"), dict) else {}
        clause = str(source.get("clause_th") or "")
        if clause and str(source.get("clause_sha256") or "") != _source_hash(clause):
            errors.append(f"{marker}: runtime source hash does not match clause_th")
        evidence = row.get("evidence") if isinstance(row.get("evidence"), dict) else {}
        if source.get("clause_sha256") and evidence.get("source_span_sha256") != source.get("clause_sha256"):
            errors.append(f"{marker}: evidence source_span_sha256 does not match source hash")
        claim = row.get("claim") if isinstance(row.get("claim"), dict) else {}
        if claim.get("english_status") == "approved":
            thai_numbers = numeric_tokens(str(claim.get("answer_th") or ""))
            english_numbers = numeric_tokens(str(claim.get("answer_en") or ""))
            if thai_numbers != english_numbers:
                errors.append(f"{marker}: approved English numeric values differ from Thai")
        quality = row.get("quality") if isinstance(row.get("quality"), dict) else {}
        if quality.get("completeness") == "complete_list" and not claim.get("structured_values"):
            errors.append(f"{marker}: complete_list requires structured_values")
        lifecycle = row.get("lifecycle") if isinstance(row.get("lifecycle"), dict) else {}
        supersedes = str(lifecycle.get("supersedes_claim_id") or "")
        if supersedes and supersedes not in all_claim_ids:
            errors.append(f"{marker}: supersedes unknown claim {supersedes}")
        for conflict in lifecycle.get("conflicts_with") or []:
            if str(conflict) not in all_claim_ids:
                errors.append(f"{marker}: conflicts_with unknown claim {conflict}")
    return ClaimValidationReport(len(rows), tuple(errors), (), dict(status_counts))


def build_runtime(rows: list[dict[str, Any]], *, release_id: str) -> tuple[list[dict[str, Any]], Counter[str]]:
    runtime_rows: list[dict[str, Any]] = []
    blocked: Counter[str] = Counter()
    for row in rows:
        publishable, reasons = is_publishable(row)
        if not publishable:
            blocked.update(reasons)
            continue
        runtime_rows.append(convert_review_row(row, release_id=release_id))
    return runtime_rows, blocked


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows)
    path.write_text(content + ("\n" if content else ""), encoding="utf-8")


def command_validate_review(args: argparse.Namespace) -> int:
    rows = read_jsonl(Path(args.input))
    report = validate_review_rows(rows)
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    return 0 if report.ok else 1


def command_validate_runtime(args: argparse.Namespace) -> int:
    rows = read_jsonl(Path(args.input))
    report = validate_runtime_rows(rows)
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    return 0 if report.ok else 1


def command_build_runtime(args: argparse.Namespace) -> int:
    review_rows = read_jsonl(Path(args.input))
    review_report = validate_review_rows(review_rows)
    if not review_report.ok:
        print(json.dumps(review_report.as_dict(), ensure_ascii=False, indent=2))
        return 1
    runtime_rows, blocked = build_runtime(review_rows, release_id=args.release_id)
    runtime_report = validate_runtime_rows(runtime_rows)
    manifest = {
        "schema_version": "competition_rule_release_manifest_v1",
        "release_id": args.release_id,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "review_records": len(review_rows),
        "runtime_records": len(runtime_rows),
        "prompt_version": CHATBOT_PROMPT_VERSION,
        "taxonomy_version": COMPETITION_TAXONOMY_VERSION,
        "review_schema_sha256": _file_hash(REVIEW_SCHEMA),
        "runtime_schema_sha256": _file_hash(RUNTIME_SCHEMA),
        "review_queue_sha256": _file_hash(Path(args.input)),
        "blocked_reasons": dict(blocked),
        "runtime_validation": runtime_report.as_dict(),
    }
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if not runtime_report.ok:
        return 1
    Path(args.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(args.manifest).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not runtime_rows and not args.allow_empty:
        print("No owner-approved records are publishable; audit manifest written, runtime file not written.", file=sys.stderr)
        return 2
    write_jsonl(Path(args.output), runtime_rows)
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    validate_review = subparsers.add_parser("validate-review")
    validate_review.add_argument("--input", default=str(DEFAULT_QUEUE))
    validate_review.set_defaults(func=command_validate_review)

    validate_runtime = subparsers.add_parser("validate-runtime")
    validate_runtime.add_argument("--input", required=True)
    validate_runtime.set_defaults(func=command_validate_runtime)

    build = subparsers.add_parser("build-runtime")
    build.add_argument("--input", default=str(DEFAULT_QUEUE))
    build.add_argument("--release-id", required=True)
    build.add_argument("--output", required=True)
    build.add_argument("--manifest", required=True)
    build.add_argument("--allow-empty", action="store_true")
    build.set_defaults(func=command_build_runtime)
    return result


def main() -> int:
    args = parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
