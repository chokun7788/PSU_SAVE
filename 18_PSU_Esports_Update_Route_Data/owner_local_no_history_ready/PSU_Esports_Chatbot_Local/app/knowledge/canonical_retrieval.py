"""Runtime adapter for published Canonical Content RAG projections.

The adapter exposes Thai source projections and approved English projections
only.  It keeps the current retrieval row contract so the existing pipeline
can migrate without a second RAG path.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROJECTION_ROOT = ROOT / "data" / "content" / "projections"


def canonical_rag_enabled() -> bool:
    """One-flag rollback path during the canonical-data migration."""
    return os.getenv("PSU_CANONICAL_RAG_ENABLED", "1").strip().lower() in {
        "1", "true", "yes", "on",
    }


def _row_from_projection(row: dict[str, Any]) -> dict[str, Any] | None:
    if str(row.get("status") or "").lower() != "published":
        return None
    text = str(row.get("text") or "").strip()
    content_id = str(row.get("content_id") or "").strip()
    if not text or not content_id:
        return None
    return {
        "id": str(row.get("projection_id") or content_id),
        "content_id": content_id,
        "category": str(row.get("category") or "knowledge"),
        "canonical_category": str(row.get("canonical_category") or row.get("category") or "knowledge"),
        "title": str(row.get("title") or content_id),
        "text": text,
        "aliases": list(row.get("aliases") or []),
        "tags": list(row.get("tags") or []),
        "game": str(row.get("game") or ""),
        "source_url": str(row.get("source_url") or ""),
        "source_ids": list(row.get("source_ids") or [content_id]),
        "priority": float(row.get("priority") or 0.0),
        "entity_ids": list(row.get("entity_ids") or []),
        "facets": list(row.get("facets") or []),
        "language": str(row.get("locale") or "th"),
        "trust_level": str(row.get("trust_level") or "internal_verified"),
        "status": "published",
        "dynamic_knowledge": True,
        "ingestion_source": "canonical_content",
        "content_version": row.get("version"),
        "_source_file": "canonical_rag_projection.jsonl",
        "_canonical_projection": True,
    }


@lru_cache(maxsize=4)
def _load_projection(path_text: str) -> tuple[dict[str, Any], ...]:
    path = Path(path_text)
    if not path.exists():
        return ()
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        candidate = _row_from_projection(json.loads(line))
        if candidate is not None:
            rows.append(candidate)
    return tuple(rows)


def load_canonical_rag_rows(*, locale: str = "th") -> tuple[dict[str, Any], ...]:
    """Return release-safe projection rows for one locale only."""
    if not canonical_rag_enabled():
        return ()
    filename = "rag_en_approved_projection.jsonl" if locale.strip().lower() == "en" else "rag_th_projection.jsonl"
    return _load_projection(str(PROJECTION_ROOT / filename))


def clear_canonical_rag_cache() -> None:
    _load_projection.cache_clear()
