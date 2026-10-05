from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from typing import Any
from urllib.parse import urlparse


SCHEMA_VERSION = "2.1-pilot"
REGISTRY_VERSION = "1"
FACTS = {"genre": str, "service_availability": bool, "available_at": str}
FACETS = {"overview", "how_to_play", "controls", "policy", "exceptions"}
MAX_RECORDS = 100


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def timestamp(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a timezone-aware ISO string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timezone required")
    return parsed


def _keys(value: Any, required: set[str], optional: set[str] | None = None) -> None:
    if not isinstance(value, dict) or not required <= value.keys() or value.keys() - required - (optional or set()):
        raise ValueError(f"invalid fields; expected {sorted(required)}")


def _text(value: Any, limit: int = 3000) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > limit or "\x00" in value:
        raise ValueError("invalid text or length")
    # Public answers are rendered as Markdown. Do not let content create links/HTML.
    if any(token in value for token in ("<", ">", "[", "]", "```")):
        raise ValueError("use plain text, not HTML or Markdown links")


def _id(value: Any) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[a-zA-Z0-9_:-]{1,100}", value):
        raise ValueError("invalid identifier")


def _list(value: Any, maximum: int) -> None:
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError("invalid list or item limit")


def validate_record(record: dict[str, Any], *, allow_demo: bool = False) -> dict[str, Any]:
    """Strict pilot envelope. Unsupported scope/fields fail instead of being ignored."""
    _keys(record, {"schema_version", "record_id", "type", "title", "aliases", "entity_id",
                   "scope", "effective_from", "valid_until", "facts", "sections", "sources"})
    if record["schema_version"] != SCHEMA_VERSION or record["type"] not in {"game", "rule"}:
        raise ValueError("unsupported schema or content type")
    for name in ("record_id", "entity_id"):
        _id(record[name])
    _text(record["title"], 120)
    if len(record["title"].strip()) < 3:
        raise ValueError("title too short for explicit ownership")
    _list(record["aliases"], 12)
    for alias in record["aliases"]:
        _text(alias, 120)
        if len(alias.strip()) < 3:
            raise ValueError("alias too short for explicit ownership")
    _keys(record["scope"], {"branch", "access"})
    if record["scope"] != {"branch": "psu_phuket", "access": "public"}:
        raise ValueError("pilot supports public PSU Phuket records only")
    start = timestamp(record["effective_from"])
    if record["valid_until"] is not None and timestamp(record["valid_until"]) <= start:
        raise ValueError("valid_until must be after effective_from")
    _list(record["sources"], 8)
    sources = {}
    for source in record["sources"]:
        _keys(source, {"source_id", "title", "url", "snapshot_text", "snapshot_sha256", "authority"})
        _id(source["source_id"])
        _text(source["title"], 160)
        _text(source["snapshot_text"], 20000)
        if source["snapshot_sha256"] != text_hash(source["snapshot_text"]):
            raise ValueError("source snapshot hash mismatch")
        if source["source_id"] in sources:
            raise ValueError("duplicate source ID")
        _list(source["authority"], 8)
        if any(item not in FACTS.keys() | FACETS for item in source["authority"]):
            raise ValueError("unsupported source authority")
        url = source["url"]
        if not isinstance(url, str) or len(url) > 2000:
            raise ValueError("source URL required")
        parsed = urlparse(url)
        if parsed.scheme == "demo" and allow_demo:
            pass
        elif parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError("public source must use HTTPS; demo sources are test-only")
        if any(c in url for c in "\r\n<>[]() "):
            raise ValueError("unsafe source URL")
        sources[source["source_id"]] = source

    def check_refs(unit: dict[str, Any], facet: str, supported_text: str | None) -> None:
        _list(unit["source_refs"], 4)
        if not unit["source_refs"]:
            raise ValueError("verified unit requires evidence")
        for ref in unit["source_refs"]:
            _keys(ref, {"source_id", "quote"})
            source = sources.get(ref["source_id"])
            if source is None or facet not in source["authority"]:
                raise ValueError("missing source or authority")
            _text(ref["quote"], 4000)
            if ref["quote"] not in source["snapshot_text"]:
                raise ValueError("quote not found in immutable source")
        if supported_text is not None and not any(supported_text in ref["quote"] for ref in unit["source_refs"]):
            raise ValueError("unit text must be an exact source excerpt in pilot")

    _list(record["facts"], 12)
    predicates = set()
    for fact in record["facts"]:
        _keys(fact, {"fact_id", "predicate", "value", "claim_status", "source_refs"})
        _id(fact["fact_id"])
        predicate = fact["predicate"]
        if predicate not in FACTS or predicate in predicates:
            raise ValueError("unsupported or duplicate predicate")
        predicates.add(predicate)
        if fact["claim_status"] == "unknown":
            if fact["value"] is not None or fact["source_refs"] != []:
                raise ValueError("unknown must have null value and no support assertion")
        elif fact["claim_status"] == "verified":
            if type(fact["value"]) is not FACTS[predicate]:
                raise ValueError("fact value type mismatch")
            if isinstance(fact["value"], str):
                _text(fact["value"], 160)
            check_refs(fact, predicate, fact["value"] if isinstance(fact["value"], str) else None)
        else:
            raise ValueError("unsupported claim status")
    _list(record["sections"], 12)
    sections = {}
    for section in record["sections"]:
        _keys(section, {"section_id", "facet", "heading", "text", "depends_on", "source_refs"})
        _id(section["section_id"])
        _text(section["heading"], 120)
        _text(section["text"], 1800)
        if section["facet"] not in FACETS or section["section_id"] in sections:
            raise ValueError("invalid facet or duplicate section")
        _list(section["depends_on"], 4)
        for dependency in section["depends_on"]:
            _id(dependency)
        check_refs(section, section["facet"], section["text"])
        sections[section["section_id"]] = section

    def visit(key: str, stack: set[str]) -> None:
        if key not in sections or key in stack or len(stack) > 4:
            raise ValueError("missing, cyclic or deep section dependency")
        for child in sections[key]["depends_on"]:
            visit(child, stack | {key})

    for key in sections:
        visit(key, set())
    if not predicates and not sections:
        raise ValueError("record has no answerable content")
    return json.loads(canonical_json(record))
