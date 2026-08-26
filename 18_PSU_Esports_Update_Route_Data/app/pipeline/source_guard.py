from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import re
from typing import Any

from app.core.source_registry import SOURCE_REGISTRY


_TRUST_RANK = {"official": 4, "user_confirmed": 3, "internal_verified": 2, "secondary": 1, "": 0}


def _claim_key(hit: dict[str, Any], metadata: dict[str, Any]) -> str:
    explicit = hit.get("claim_key") or hit.get("fact_key") or metadata.get("claim_key") or metadata.get("fact_key")
    if explicit:
        return str(explicit).strip()
    # Separate independent documents by default. Dates/counts from different
    # news items are not a conflict unless a source explicitly shares a claim.
    return str(hit.get("id") or metadata.get("source_id") or metadata.get("title") or "unknown_source").strip()


@dataclass(frozen=True)
class SourceQuality:
    source_ids: tuple[str, ...]
    authority_rank: int
    conflict: bool
    stale: bool
    warnings: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "source_ids": list(self.source_ids),
            "authority_rank": self.authority_rank,
            "conflict": self.conflict,
            "stale": self.stale,
            "warnings": list(self.warnings),
        }


def assess_sources(hits: list[dict[str, Any]] | None) -> SourceQuality:
    source_ids: list[str] = []
    categories: set[str] = set()
    numeric_signatures: dict[tuple[str, str], set[str]] = {}
    authority = 0
    stale = False
    warnings: list[str] = []
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
        source_id = str(hit.get("id") or metadata.get("source_id") or "").strip()
        if source_id and source_id not in source_ids:
            source_ids.append(source_id)
        record = SOURCE_REGISTRY.get(source_id)
        trust = str(hit.get("trust_level") or metadata.get("trust_level") or (record.trust_level if record else "")).strip()
        authority = max(authority, _TRUST_RANK.get(trust, 0))
        category = str(hit.get("category") or metadata.get("category") or (record.category if record else "")).strip()
        if category:
            categories.add(category)
        text = str(hit.get("text") or metadata.get("text") or "")
        numbers = {value for value in re.findall(r"(?<![A-Za-z])\d+(?:[.,]\d+)?", text)}
        if category and numbers:
            numeric_signatures.setdefault((category, _claim_key(hit, metadata)), set()).update(numbers)
        time_sensitive = bool(hit.get("time_sensitive") or metadata.get("time_sensitive"))
        valid_until = str(hit.get("valid_until") or metadata.get("valid_until") or "").strip()
        if time_sensitive and valid_until:
            try:
                stale = stale or date.fromisoformat(valid_until[:10]) < date.today()
            except ValueError:
                warnings.append("invalid_valid_until_date")

    conflict = any(len(values) > 3 for values in numeric_signatures.values())
    if conflict:
        warnings.append("same_claim_has_multiple_numeric_values_need_source_review")
    if stale:
        warnings.append("time_sensitive_source_expired")
    if not source_ids:
        warnings.append("missing_source_id")
    return SourceQuality(tuple(source_ids), authority, conflict, stale, tuple(warnings))
