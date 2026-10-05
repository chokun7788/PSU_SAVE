"""Build a non-runtime review queue for atomic competition-rule claims.

The existing imported chunks remain the immutable Thai source.  This tool
creates a v2 review queue that separates source provenance, claim text,
retrieval metadata, and English draft wording.  It never enables a release.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl"
CANONICAL = ROOT / "data" / "competition_rules" / "canonical" / "competition_rule_rag_projections.jsonl"
LOCALIZATIONS = ROOT / "data" / "locales" / "en" / "localization_review_drafts_competition_20260921_repaired.jsonl"
OUTPUT = ROOT / "data" / "competition_rules" / "review" / "competition_rule_claim_v2_review_queue.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    sources = read_jsonl(SOURCE)
    canonical_by_source = {
        str((row.get("source_locator") or {}).get("source_chunk_id") or ""): row
        for row in read_jsonl(CANONICAL)
    }
    english_by_source = {
        str(row.get("content_id") or ""): str(row.get("text") or "")
        for row in read_jsonl(LOCALIZATIONS)
        if row.get("field") == "text" and str(row.get("content_id") or "").startswith("competition_rules_")
    }

    queue: list[dict[str, Any]] = []
    for source in sources:
        source_id = str(source.get("id") or "")
        clause_th = str(source.get("text") or "").strip()
        heading_th = str(source.get("section_title") or "").strip()
        canonical = canonical_by_source.get(source_id, {})
        queue.append({
            "schema_version": "competition_rule_claim_v2",
            "claim_id": f"review::{source_id}",
            "status": "needs_owner_review",
            "source": {
                "source_chunk_id": source_id,
                "document_id": str(source.get("document_id") or ""),
                "source_url": str(source.get("source_url") or ""),
                "source_file": str(source.get("source_file") or ""),
                "section_index": source.get("section_index"),
                "chunk_index": source.get("chunk_index"),
                "heading_th": heading_th,
                "clause_th": clause_th,
                "clause_sha256": sha256(clause_th),
            },
            "claim": {
                "statement_th": clause_th,
                "answer_th": "",
                "answer_en": english_by_source.get(source_id, ""),
                "answer_en_status": "draft" if english_by_source.get(source_id) else "missing",
            },
            "retrieval": {
                "game": str(source.get("game") or ""),
                "game_id": str(canonical.get("game_id") or ""),
                "canonical_section_proposed": str(canonical.get("canonical_section") or ""),
                "module_proposed": str(canonical.get("module") or ""),
                "facet_proposed": str(canonical.get("facet") or ""),
                "aliases_th": [],
                "aliases_en": [],
                "question_patterns_th": [],
                "question_patterns_en": [],
            },
            "evidence": {
                "support_mode": "exact_source_clause_required",
                "source_span_th": clause_th,
                "source_refs": [source_id],
                "evidence_links": [],
            },
            "quality": {
                "atomicity": "review_required",
                "heading_clause_relation": "same_field_ambiguous" if heading_th == clause_th else "distinct",
                "provenance": "source_hash_verified",
                "review_notes": [],
            },
            "approval": {
                "review_status": "pending_owner_review",
                "approved_by": "",
                "approved_at": "",
                "effective_from": "",
                "effective_to": "",
            },
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in queue) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"output": str(OUTPUT), "claims": len(queue)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
