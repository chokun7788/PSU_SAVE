from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
LOCALE_ROOT = ROOT / "data" / "locales" / "en"
DEFAULT_REGISTRY_PATH = LOCALE_ROOT / "approved_localizations.jsonl"
CURRENT_RELEASE_PATH = LOCALE_ROOT / "CURRENT"


def _draft_preview_registry_path() -> Path | None:
    """Return an explicit local-only preview registry when opted in by the operator."""
    if os.getenv("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW", "0").strip().lower() not in {"1", "true", "yes", "on"}:
        return None
    configured = os.getenv("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH", "").strip()
    if not configured:
        return None
    candidate = Path(configured).expanduser()
    return candidate if candidate.is_file() else None


def active_release_dir() -> Path | None:
    if not CURRENT_RELEASE_PATH.exists():
        return None
    release_id = CURRENT_RELEASE_PATH.read_text(encoding="utf-8").strip()
    if not release_id or Path(release_id).name != release_id:
        return None
    candidate = LOCALE_ROOT / "releases" / release_id
    return candidate if candidate.is_dir() else None


def active_registry_path() -> Path:
    preview = _draft_preview_registry_path()
    if preview is not None:
        return preview
    release = active_release_dir()
    candidate = release / "approved_localizations.jsonl" if release is not None else DEFAULT_REGISTRY_PATH
    return candidate if candidate.exists() else DEFAULT_REGISTRY_PATH


def _is_draft_preview_record(record: "LocalizationRecord", path: Path, source_record: dict[str, Any]) -> bool:
    preview = _draft_preview_registry_path()
    if preview is None:
        return False
    try:
        matches_preview = path.resolve() == preview.resolve()
    except OSError:
        matches_preview = False
    return bool(
        matches_preview
        and record.status == "draft"
        and str(source_record.get("category") or "").strip().casefold() != "members"
        and record.content_id
        and record.field
        and record.locale == "en"
        and record.text
        and record.source_text_sha256
    )


def source_text_sha256(value: Any) -> str:
    if isinstance(value, (dict, list, tuple)):
        serialized = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    else:
        serialized = str(value or "")
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def source_record_content_id(source_record: dict[str, Any]) -> str:
    """Resolve a stable content key, including legacy member rows without an id."""
    content_id = str(source_record.get("id") or source_record.get("content_id") or "").strip()
    if content_id:
        return content_id
    member_values = [str(source_record.get(field) or "") for field in ("name", "role", "affiliation")]
    if any(member_values):
        return "member_" + hashlib.sha256("|".join(member_values).encode("utf-8")).hexdigest()[:16]
    return ""


@dataclass(frozen=True)
class LocalizationRecord:
    content_id: str
    field: str
    locale: str
    text: str
    source_text_sha256: str
    status: str
    version: int
    approved_by: str
    approved_at: str

    @classmethod
    def from_dict(cls, row: dict[str, Any]) -> "LocalizationRecord":
        return cls(
            content_id=str(row.get("content_id") or "").strip(),
            field=str(row.get("field") or "").strip(),
            locale=str(row.get("locale") or "").strip().lower(),
            text=str(row.get("text") or "").strip(),
            source_text_sha256=str(row.get("source_text_sha256") or "").strip().lower(),
            status=str(row.get("status") or "draft").strip().lower(),
            version=max(1, int(row.get("version") or 1)),
            approved_by=str(row.get("approved_by") or "").strip(),
            approved_at=str(row.get("approved_at") or "").strip(),
        )

    @property
    def usable(self) -> bool:
        return bool(
            self.content_id
            and self.field
            and self.locale == "en"
            and self.text
            and self.source_text_sha256
            and self.status == "approved"
            and self.approved_by
            and self.approved_at
        )


@lru_cache(maxsize=4)
def load_localization_registry(path_text: str = "") -> dict[tuple[str, str, str], LocalizationRecord]:
    path = Path(path_text) if path_text else active_registry_path()
    if not path.exists():
        return {}
    records: dict[tuple[str, str, str], LocalizationRecord] = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = LocalizationRecord.from_dict(json.loads(line))
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            raise RuntimeError(f"Invalid localization registry {path}:{line_no}: {exc}") from exc
        key = (record.content_id, record.field, record.locale)
        previous = records.get(key)
        if previous is None or record.version > previous.version:
            records[key] = record
    return records


def approved_localization(
    source_record: dict[str, Any],
    field: str,
    *,
    locale: str = "en",
    registry_path: Path | None = None,
) -> str | None:
    content_id = source_record_content_id(source_record)
    if not content_id or field not in source_record:
        return None
    path_text = str(registry_path or active_registry_path())
    record = load_localization_registry(path_text).get((content_id, field, locale))
    if record is None or not (record.usable or _is_draft_preview_record(record, Path(path_text), source_record)):
        return None
    if record.source_text_sha256 != source_text_sha256(source_record.get(field)):
        return None
    return record.text


def localization_status(
    source_record: dict[str, Any],
    field: str,
    *,
    locale: str = "en",
    registry_path: Path | None = None,
) -> str:
    content_id = source_record_content_id(source_record)
    path_text = str(registry_path or active_registry_path())
    record = load_localization_registry(path_text).get((content_id, field, locale))
    if record is None:
        return "missing"
    if _is_draft_preview_record(record, Path(path_text), source_record):
        return "draft_preview"
    if not record.usable:
        return record.status or "draft"
    if record.source_text_sha256 != source_text_sha256(source_record.get(field)):
        return "stale"
    return "approved"
