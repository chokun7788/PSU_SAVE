from __future__ import annotations

"""Project approved canonical content into Structured and RAG-ready JSONL.

The English projection contains only approved English records. Drafts and
legacy unreviewed text are deliberately excluded.
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_content import (
    CONTENT_ROOT,
    PUBLISHABLE_LIFECYCLE_STATUS,
    load_records,
    source_sha256,
    validate_records,
)


RUNTIME_CATEGORY = {
    "booking": "reservation",
    "competition": "competition_rules",
    "competition_rules": "competition_rules",
    "game_controls": "game_controls",
    "games": "games",
    "knowledge": "knowledge",
    "members": "members",
    "resources": "games",
    "rules": "rules",
    "schedule": "schedule",
    "services": "service_fee",
}


def flatten(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return "\n".join(part for item in value if (part := flatten(item)))
    if isinstance(value, dict):
        return "\n".join(f"{key}: {part}" for key, item in value.items() if (part := flatten(item)))
    return str(value or "").strip()


def _write_jsonl_atomic(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")
    for _ in range(20):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            time.sleep(0.15)
    raise RuntimeError(f"Unable to replace {path}")


def _runtime_category(record: dict[str, Any]) -> str:
    facts = record.get("facts") if isinstance(record.get("facts"), dict) else {}
    return str(facts.get("route_category") or RUNTIME_CATEGORY.get(str(record.get("category") or ""), record.get("category") or "knowledge"))


def _field_facets(record: dict[str, Any], field: str) -> list[str]:
    key = field.removesuffix("_th").removesuffix("_en")
    category = str(record.get("category") or "")
    if key in {"summary", "text", "title", "sections"}:
        key = "overview"
    if key == "answer":
        key = "competition_rule" if category == "competition_rules" else "policy"
    if category == "game_controls" and key in {"action", "description"}:
        key = "controls"
    return list(dict.fromkeys([key, "overview"]))


def _tags(record: dict[str, Any], field: str = "") -> list[str]:
    facts = record.get("facts") if isinstance(record.get("facts"), dict) else {}
    aliases = record.get("aliases") if isinstance(record.get("aliases"), dict) else {}
    values = [str(record.get("category") or ""), str(record.get("kind") or ""), field]
    values.extend(str(value) for value in facts.get("tags") or [] if value)
    values.extend(str(value) for value in aliases.get("th") or [] if value)
    values.extend(str(value) for value in aliases.get("en") or [] if value)
    if facts.get("game"):
        values.append(str(facts["game"]))
    return list(dict.fromkeys(value for value in values if value))


def _target_entity_id(value: Any) -> str:
    """Match the stable compact ID produced by the existing target resolver."""
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").casefold()
    return re.sub(r"[^0-9a-z]+", "", text)


def _projection_rows(
    record: dict[str, Any], *, locale: str, fields: dict[str, Any], base: dict[str, Any]
) -> list[dict[str, Any]]:
    """Split each field/section into a bounded, independently retrievable unit."""
    rows: list[dict[str, Any]] = []
    for field, value in fields.items():
        if field == "title" or value in (None, "", [], {}):
            continue
        if field == "sections" and isinstance(value, list):
            for section in value:
                if not isinstance(section, dict):
                    continue
                text = flatten(section.get("text"))
                if not text:
                    continue
                section_index = int(section.get("section_index") or len(rows) + 1)
                heading = flatten(section.get("section_title")) or base["title"]
                rows.append({
                    **base,
                    "projection_id": f"{base['content_id']}::{locale}::section:{section_index}",
                    "title": heading,
                    "text": text,
                    "field": f"section:{section_index}",
                    "facets": ["competition_rule", "overview"],
                    "tags": list(dict.fromkeys([*base["tags"], heading])),
                })
            continue
        text = flatten(value)
        if not text:
            continue
        rows.append({
            **base,
            "projection_id": f"{base['content_id']}::{locale}::{field}",
            "title": flatten(fields.get("title")) or base["content_id"],
            "text": text,
            "field": field,
            "facets": _field_facets(record, field),
            "tags": _tags(record, field),
        })
    return rows


def project(records: tuple[dict[str, Any], ...]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    structured: list[dict[str, Any]] = []
    rag_th: list[dict[str, Any]] = []
    rag_en: list[dict[str, Any]] = []
    for record in records:
        lifecycle = record["lifecycle"]
        # Draft, review, approved, and withdrawn records are repository data only.
        # They must never become runtime Structured/RAG evidence until explicitly published.
        if lifecycle["status"] != PUBLISHABLE_LIFECYCLE_STATUS:
            continue
        content_id = str(record["content_id"])
        source = record["source"]
        facts = record.get("facts") if isinstance(record.get("facts"), dict) else {}
        source_ids = list(source.get("source_ids") or [content_id])
        base = {
            "content_id": content_id,
            "category": _runtime_category(record),
            "canonical_category": record["category"],
            "kind": record["kind"],
            "aliases": list(dict.fromkeys([*(record["aliases"].get("th") or []), *(record["aliases"].get("en") or [])])),
            "facts": facts,
            "tags": _tags(record),
            "game": str(facts.get("game") or ""),
            "entity_ids": [_target_entity_id(facts["game"])] if facts.get("game") else [],
            "source_ids": source_ids,
            "source_url": source.get("url") or "",
            "source_path": source.get("path"),
            "version": lifecycle["version"],
            "trust_level": "internal_verified",
            "status": "published",
        }
        structured.append(base)
        thai_fields = record["locales"]["th"]["fields"]
        for row in _projection_rows(record, locale="th", fields=thai_fields, base=base):
            rag_th.append({**row, "locale": "th", "source_text_sha256": source_sha256(thai_fields)})
        english = record["locales"]["en"]
        if english.get("status") != "approved":
            continue
        english_fields = english.get("fields") or {}
        if not english_fields or english.get("source_sha256") != source_sha256(thai_fields):
            continue
        for row in _projection_rows(record, locale="en", fields=english_fields, base=base):
            rag_en.append({
                **row,
                "locale": "en",
                "source_text_sha256": english["source_sha256"],
                "approved_by": english.get("approved_by"),
                "approved_at": english.get("approved_at"),
            })
    return structured, rag_th, rag_en


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Structured and RAG projections from canonical content.")
    parser.add_argument("--content-root", type=Path, default=CONTENT_ROOT)
    parser.add_argument("--output", type=Path, default=CONTENT_ROOT / "projections")
    args = parser.parse_args()
    records = load_records(args.content_root)
    validation = validate_records(records)
    if not validation.ok:
        raise SystemExit("\n".join(validation.errors))
    structured, rag_th, rag_en = project(records)
    _write_jsonl_atomic(args.output / "structured_projection.jsonl", structured)
    _write_jsonl_atomic(args.output / "rag_th_projection.jsonl", rag_th)
    _write_jsonl_atomic(args.output / "rag_en_approved_projection.jsonl", rag_en)
    manifest = {
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "content_records": len(records),
        "structured_records": len(structured),
        "rag_th_records": len(rag_th),
        "rag_en_approved_records": len(rag_en),
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, **manifest, "output": str(args.output)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
