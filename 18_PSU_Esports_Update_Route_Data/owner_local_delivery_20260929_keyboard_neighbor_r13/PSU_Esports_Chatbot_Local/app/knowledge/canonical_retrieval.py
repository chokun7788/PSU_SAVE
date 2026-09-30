"""Runtime adapter for published Canonical Content RAG projections.

The adapter exposes Thai source projections and approved English projections
only.  It keeps the current retrieval row contract so the existing pipeline
can migrate without a second RAG path.
"""

from __future__ import annotations

import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROJECTION_ROOT = ROOT / "data" / "content" / "projections"
COMPETITION_CANONICAL_ROOT = ROOT / "data" / "competition_rules" / "canonical"


def canonical_rag_enabled() -> bool:
    """One-flag rollback path during the canonical-data migration."""
    return os.getenv("PSU_CANONICAL_RAG_ENABLED", "1").strip().lower() in {
        "1", "true", "yes", "on",
    }


def canonical_competition_rag_enabled() -> bool:
    """Enable only owner-approved competition releases in the live RAG path."""
    return os.getenv("PSU_CANONICAL_COMPETITION_RAG_ENABLED", "1").strip().lower() in {
        "1", "true", "yes", "on",
    }


def canonical_competition_shadow_enabled() -> bool:
    """Keep an inactive candidate count in traces without changing answers."""
    return os.getenv("PSU_CANONICAL_COMPETITION_RAG_SHADOW", "1").strip().lower() in {
        "1", "true", "yes", "on",
    }


def _row_from_projection(row: dict[str, Any]) -> dict[str, Any] | None:
    if str(row.get("status") or "").lower() != "published":
        return None
    text = str(row.get("text") or "").strip()
    content_id = str(row.get("content_id") or "").strip()
    if not text or not content_id:
        return None
    facts = row.get("facts") if isinstance(row.get("facts"), dict) else {}
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
        "rulebook_id": str(facts.get("document_id") or ""),
        "_source_file": "canonical_rag_projection.jsonl",
        "_canonical_projection": True,
    }


def _competition_row_from_projection(row: dict[str, Any], *, active_release_ids: set[str]) -> dict[str, Any] | None:
    """Adapt a release-safe competition record to the existing RAG row contract."""
    if not bool(row.get("runtime_eligible")):
        return None
    release_id = str(row.get("release_id") or "")
    if not release_id or release_id not in active_release_ids:
        return None
    text = str(row.get("text_th") or "").strip()
    chunk_id = str(row.get("chunk_id") or "").strip()
    locator = row.get("source_locator") if isinstance(row.get("source_locator"), dict) else {}
    if not text or not chunk_id:
        return None
    section = str(row.get("canonical_section") or "competition_rules")
    module = str(row.get("module") or "common")
    facet = str(row.get("facet") or section)
    game = str(row.get("game") or "")
    return {
        "id": chunk_id,
        "content_id": str(row.get("rule_id") or chunk_id),
        "category": "competition_rules",
        "canonical_category": "competition_rules",
        "title": f"{game}: {section}/{facet}" if game else f"Competition rules: {section}/{facet}",
        "text": text,
        "aliases": [game] if game else [],
        "tags": ["competition_rules", section, module, facet],
        "game": game,
        "source_url": str(locator.get("source_url") or ""),
        "source_ids": [str(row.get("rule_id") or chunk_id)],
        "priority": 1.0,
        "entity_ids": [str(row.get("game_id") or "")] if row.get("game_id") else [],
        "facets": [section, module, facet],
        "language": "th",
        "trust_level": "owner_approved_release",
        "status": "published",
        "dynamic_knowledge": True,
        "ingestion_source": "canonical_competition_release",
        "content_version": release_id,
        "release_id": release_id,
        "canonical_section": section,
        "module": module,
        "facet": facet,
        "conditions": dict(row.get("conditions") or {}),
        "source_locator": locator,
        "_source_file": "competition_rule_rag_projections.jsonl",
        "_canonical_projection": True,
    }


@lru_cache(maxsize=4)
def _load_active_competition_projection(projection_path_text: str, manifest_path_text: str) -> tuple[dict[str, Any], ...]:
    projection_path = Path(projection_path_text)
    manifest_path = Path(manifest_path_text)
    if not projection_path.exists() or not manifest_path.exists():
        return ()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    active_release_ids = {str(value) for value in manifest.get("active_release_ids") or []}
    if not active_release_ids:
        return ()
    rows: list[dict[str, Any]] = []
    for line in projection_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        candidate = _competition_row_from_projection(json.loads(line), active_release_ids=active_release_ids)
        if candidate is not None:
            rows.append(candidate)
    return tuple(rows)


def active_canonical_competition_release_ids() -> frozenset[str]:
    """Read the current manifest for guards that must avoid legacy duplicates."""
    if not canonical_competition_rag_enabled():
        return frozenset()
    path = COMPETITION_CANONICAL_ROOT / "active_release_manifest.json"
    if not path.exists():
        return frozenset()
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return frozenset()
    return frozenset(str(value) for value in manifest.get("active_release_ids") or [])


@lru_cache(maxsize=2)
def _load_competition_shadow_metadata(projection_path_text: str) -> tuple[dict[str, Any], ...]:
    """Load metadata only for observability; these rows never enter live RAG."""
    path = Path(projection_path_text)
    if not path.exists():
        return ()
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rows.append({
            "release_id": str(row.get("release_id") or ""),
            "game": str(row.get("game") or ""),
            "canonical_section": str(row.get("canonical_section") or ""),
            "module": str(row.get("module") or ""),
            "facet": str(row.get("facet") or ""),
            "text_th": str(row.get("text_th") or ""),
        })
    return tuple(rows)


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
    rows = list(_load_projection(str(PROJECTION_ROOT / filename)))
    if locale.strip().lower() == "th" and canonical_competition_rag_enabled():
        active_competition_rows = _load_active_competition_projection(
            str(COMPETITION_CANONICAL_ROOT / "competition_rule_rag_projections.jsonl"),
            str(COMPETITION_CANONICAL_ROOT / "active_release_manifest.json"),
        )
        active_release_ids = {str(row.get("release_id") or "") for row in active_competition_rows}
        if active_release_ids:
            rows = [
                row for row in rows
                if not (
                    row.get("category") == "competition_rules"
                    and str(row.get("rulebook_id") or "") in active_release_ids
                )
            ]
        rows.extend(active_competition_rows)
    return tuple(rows)


def canonical_competition_shadow_summary(query: str) -> dict[str, Any]:
    """Return a bounded, non-answering summary of inactive canonical candidates."""
    if not canonical_competition_shadow_enabled():
        return {"enabled": False, "candidate_count": 0, "games": [], "sections": []}
    normalized_query = query.casefold()
    query_terms = {term for term in re.findall(r"[a-z0-9]{2,}", normalized_query) if len(term) >= 2}
    for signal in (
        "กติกา", "แข่ง", "แข่งขัน", "แผนที่", "เลือกฝั่ง", "ต่อเวลา", "พัก",
        "บทลงโทษ", "ผู้เล่น", "สมัคร", "อุปกรณ์", "ตัวละคร", "ฮีโร่",
    ):
        if signal in normalized_query:
            query_terms.add(signal)
    if "แมพ" in normalized_query or "map" in normalized_query:
        query_terms.update({"แผนที่", "map"})
    if "ต่อเวลา" in normalized_query or "overtime" in normalized_query:
        query_terms.update({"ต่อเวลา", "overtime"})
    ignored_terms = {
        "cs2", "valorant", "rov", "aov", "tekken", "game", "games",
        "กติกา", "แข่ง", "แข่งขัน",
    }
    content_terms = query_terms - ignored_terms
    explicit_game_markers = {
        "cs2": ("counter-strike", "counter strike", "cs2"),
        "valorant": ("valorant",),
        "rov": ("arena of valor", "rov"),
        "aov": ("arena of valor", "rov"),
        "tekken": ("tekken",),
    }
    game_filters = tuple(
        marker
        for trigger, markers in explicit_game_markers.items()
        if trigger in normalized_query
        for marker in markers
    )
    matches: list[dict[str, Any]] = []
    for row in _load_competition_shadow_metadata(str(COMPETITION_CANONICAL_ROOT / "competition_rule_rag_projections.jsonl")):
        haystack = " ".join(str(row.get(key) or "") for key in ("game", "canonical_section", "module", "facet", "text_th")).casefold()
        if game_filters and not any(marker in str(row.get("game") or "").casefold() for marker in game_filters):
            continue
        if not content_terms or any(term in haystack for term in content_terms):
            matches.append(row)
    return {
        "enabled": True,
        "candidate_count": len(matches),
        "games": sorted({row["game"] for row in matches if row["game"]})[:4],
        "sections": sorted({row["canonical_section"] for row in matches if row["canonical_section"]})[:6],
    }


def clear_canonical_rag_cache() -> None:
    _load_projection.cache_clear()
    _load_active_competition_projection.cache_clear()
    _load_competition_shadow_metadata.cache_clear()
