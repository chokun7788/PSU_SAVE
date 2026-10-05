from __future__ import annotations

import re
from typing import Any

from app.core.normalization import normalize_text


def _source_id(hit: dict[str, Any]) -> str:
    metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
    return str(
        hit.get("source_id")
        or hit.get("id")
        or metadata.get("source_id")
        or metadata.get("title")
        or "unknown_source"
    ).strip()


def _text(hit: dict[str, Any]) -> str:
    metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
    return str(hit.get("text") or metadata.get("text") or hit.get("description_th") or "").strip()


def pack_evidence(
    query: str,
    hits: list[dict[str, Any]] | None,
    *,
    max_items: int = 5,
    max_chars: int = 6000,
) -> dict[str, Any]:
    """Create a compact, source-labelled evidence object for the LLM."""
    items: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    used_chars = 0
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        source_id = _source_id(hit)
        text = _text(hit)
        if not text:
            continue
        key = (source_id, normalize_text(text))
        if key in seen:
            continue
        seen.add(key)
        remaining = max_chars - used_chars
        if remaining <= 80:
            break
        clipped = text[:remaining]
        metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
        item = {
            "source_id": source_id,
            "title": str(hit.get("title") or metadata.get("title") or "").strip(),
            "text": clipped,
            "category": str(hit.get("category") or metadata.get("category") or "").strip(),
            "source_url": str(hit.get("source_url") or metadata.get("source_url") or "").strip(),
            "trust_level": str(hit.get("trust_level") or metadata.get("trust_level") or "").strip(),
            "updated_at": str(hit.get("updated_at") or metadata.get("updated_at") or "").strip(),
            "score": float(hit.get("_document_rerank_score", hit.get("_hybrid_score", hit.get("_score", 0.0))) or 0.0),
        }
        items.append(item)
        used_chars += len(clipped)
        if len(items) >= max_items:
            break

    scores = [float(item["score"]) for item in items]
    margin = scores[0] - scores[1] if len(scores) > 1 else scores[0] if scores else 0.0
    return {
        "query": query,
        "items": items,
        "source_ids": [item["source_id"] for item in items],
        "top_score": round(scores[0], 4) if scores else 0.0,
        "score_margin": round(margin, 4),
        "item_count": len(items),
        "max_chars": max_chars,
        "packing": "source_labelled_compact_v1",
    }
