"""Validation and loading helpers for the canonical content repository.

Canonical records keep Thai facts, English review state, sources, and aliases
in one place. Runtime projections are built from these records; this module
does not make unapproved English text available to the chatbot.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONTENT_ROOT = ROOT / "data" / "content"
SCHEMA_VERSION = 1
_RESERVED_DIRS = frozenset({"schema", "review", "projections", "releases"})
PUBLISHABLE_LIFECYCLE_STATUS = "published"
_LIFECYCLE_STATUSES = frozenset({"draft", "review", "approved", "published", "withdrawn"})


def source_sha256(value: Any) -> str:
    serialized = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CanonicalValidation:
    records: int
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def iter_record_paths(root: Path = CONTENT_ROOT) -> tuple[Path, ...]:
    if not root.exists():
        return ()
    return tuple(
        path for path in sorted(root.rglob("*.json"))
        if path.parent.name not in _RESERVED_DIRS and path.name != "manifest.json"
    )


def load_records(root: Path = CONTENT_ROOT) -> tuple[dict[str, Any], ...]:
    records: list[dict[str, Any]] = []
    for path in iter_record_paths(root):
        row = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(row, dict):
            raise RuntimeError(f"Canonical record must be an object: {path}")
        copied = dict(row)
        copied["_content_path"] = str(path.relative_to(root))
        records.append(copied)
    return tuple(records)


def validate_records(records: tuple[dict[str, Any], ...] | list[dict[str, Any]]) -> CanonicalValidation:
    errors: list[str] = []
    seen: set[str] = set()
    for index, row in enumerate(records, 1):
        marker = str(row.get("_content_path") or f"record {index}")
        content_id = str(row.get("content_id") or "").strip()
        if not content_id:
            errors.append(f"{marker}: missing content_id")
        elif content_id in seen:
            errors.append(f"{marker}: duplicate content_id {content_id}")
        seen.add(content_id)
        if row.get("schema_version") != SCHEMA_VERSION:
            errors.append(f"{marker}: unsupported schema_version")
        if not str(row.get("category") or "").strip() or not str(row.get("kind") or "").strip():
            errors.append(f"{marker}: missing category or kind")
        lifecycle = row.get("lifecycle")
        if not isinstance(lifecycle, dict):
            errors.append(f"{marker}: lifecycle is required")
        else:
            lifecycle_status = str(lifecycle.get("status") or "").strip()
            if lifecycle_status not in _LIFECYCLE_STATUSES:
                errors.append(f"{marker}: unsupported lifecycle.status {lifecycle_status!r}")
            version = lifecycle.get("version")
            if not isinstance(version, int) or version < 1:
                errors.append(f"{marker}: lifecycle.version must be a positive integer")
        aliases = row.get("aliases")
        if not isinstance(aliases, dict) or not isinstance(aliases.get("th"), list) or not isinstance(aliases.get("en"), list):
            errors.append(f"{marker}: aliases must contain th/en lists")
        source = row.get("source")
        if not isinstance(source, dict) or not str(source.get("path") or "").strip():
            errors.append(f"{marker}: source.path is required")
        locales = row.get("locales")
        if not isinstance(locales, dict) or not isinstance(locales.get("th"), dict) or not isinstance(locales.get("en"), dict):
            errors.append(f"{marker}: locales.th and locales.en are required")
            continue
        thai = locales["th"]
        english = locales["en"]
        thai_fields = thai.get("fields")
        if not isinstance(thai_fields, dict) or not thai_fields:
            errors.append(f"{marker}: locales.th.fields must not be empty")
            continue
        expected_hash = source_sha256(thai_fields)
        if str(english.get("source_sha256") or "") != expected_hash:
            errors.append(f"{marker}: locales.en.source_sha256 is stale")
        en_status = str(english.get("status") or "missing")
        if en_status == "approved":
            if not english.get("approved_by") or not english.get("approved_at"):
                errors.append(f"{marker}: approved English requires reviewer and timestamp")
            if not isinstance(english.get("fields"), dict) or not english["fields"]:
                errors.append(f"{marker}: approved English fields must not be empty")
    return CanonicalValidation(records=len(records), errors=tuple(errors))
