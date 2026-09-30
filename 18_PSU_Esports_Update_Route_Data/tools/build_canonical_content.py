from __future__ import annotations

"""Build the grouped canonical content repository from the current data files.

It creates a reviewable data foundation only. English fields generated or
carried from legacy files remain `draft`/`legacy_unreviewed`; no runtime
chatbot data is changed by this tool.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_content import SCHEMA_VERSION, source_sha256, validate_records


CONTENT_ROOT = ROOT / "data" / "content"
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_")
    return cleaned or hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _member_id(row: dict[str, Any]) -> str:
    value = "|".join(str(row.get(key) or "") for key in ("name", "role", "affiliation"))
    return "member_" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def _split_aliases(values: Iterable[Any]) -> dict[str, list[str]]:
    thai: list[str] = []
    english: list[str] = []
    for raw in values:
        value = str(raw or "").strip()
        if not value:
            continue
        destination = thai if THAI_RE.search(value) else english
        if value not in destination:
            destination.append(value)
    return {"th": thai, "en": english}


def _source(path: Path, row: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "url": str(row.get("source_url") or ""),
        "source_ids": list(row.get("source_ids") or []),
        "last_verified_at": str(row.get("last_verified_at") or ""),
    }


def _record(
    *,
    content_id: str,
    category: str,
    kind: str,
    source_path: Path,
    source_row: dict[str, Any],
    thai_fields: dict[str, Any],
    facts: dict[str, Any],
    aliases: Iterable[Any],
    legacy_english: dict[str, Any] | None = None,
) -> dict[str, Any]:
    english_fields = {key: value for key, value in (legacy_english or {}).items() if value not in (None, "", [])}
    english_status = "legacy_unreviewed" if english_fields else "missing"
    return {
        "schema_version": SCHEMA_VERSION,
        "content_id": content_id,
        "category": category,
        "kind": kind,
        "lifecycle": {"status": "published", "version": 1},
        "aliases": _split_aliases(aliases),
        "facts": facts,
        "locales": {
            "th": {"status": "source", "fields": thai_fields},
            "en": {
                "status": english_status,
                "fields": english_fields,
                "source_sha256": source_sha256(thai_fields),
                "approved_by": "",
                "approved_at": "",
            },
        },
        "source": _source(source_path, source_row),
    }


def _simple_records(path: Path, category: str, kind: str, thai_keys: tuple[str, ...], *, folder: str) -> list[tuple[str, dict[str, Any]]]:
    output: list[tuple[str, dict[str, Any]]] = []
    for row in _read_jsonl(path):
        content_id = str(row.get("id") or (_member_id(row) if kind == "member" else "")).strip()
        if not content_id:
            continue
        thai_fields = {key: row[key] for key in thai_keys if row.get(key) not in (None, "", [])}
        if not thai_fields:
            continue
        ignored = set(thai_keys) | {"id", "category", "aliases", "answer_en", "action_en"}
        facts = {key: value for key, value in row.items() if key not in ignored and value not in (None, "", [])}
        aliases = list(row.get("aliases") or []) + [row.get("title"), row.get("item"), row.get("name"), row.get("game")]
        legacy = {"answer": row.get("answer_en"), "action": row.get("action_en")}
        record = _record(
            content_id=content_id,
            category=category,
            kind=kind,
            source_path=path,
            source_row=row,
            thai_fields=thai_fields,
            facts=facts,
            aliases=aliases,
            legacy_english=legacy,
        )
        output.append((f"{folder}/{_slug(content_id)}.json", record))
    return output


def _availability_records(path: Path) -> list[tuple[str, dict[str, Any]]]:
    output: list[tuple[str, dict[str, Any]]] = []
    for row in _read_jsonl(path):
        content_id = str(row.get("id") or "").strip()
        thai_fields = {"notes": list(row.get("notes") or [])}
        facts = {key: value for key, value in row.items() if key not in {"notes", "id", "category"} and value not in (None, "", [])}
        record = _record(
            content_id=content_id,
            category="resources",
            kind="service_availability",
            source_path=path,
            source_row=row,
            thai_fields=thai_fields,
            facts=facts,
            aliases=[row.get("zone"), row.get("service_label"), row.get("machine_label"), *list(row.get("games") or [])],
        )
        output.append((f"resources/availability/{_slug(content_id)}.json", record))
    return output


def _control_records(path: Path) -> list[tuple[str, dict[str, Any]]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in _read_jsonl(path):
        grouped[(str(row.get("platform_key") or "unknown"), str(row.get("game") or "unknown"))].append(row)
    output: list[tuple[str, dict[str, Any]]] = []
    for (platform, game), rows in sorted(grouped.items()):
        summary = next((row for row in rows if "_summary_" in str(row.get("id") or "")), rows[0])
        controls = [{
            "button": row.get("button"),
            "buttons": row.get("buttons") or [],
            "action_th": row.get("action_th"),
            "description_th": row.get("description_th"),
            "section": row.get("section"),
        } for row in rows if row.get("button")]
        english_controls = [{
            "button": row.get("button"),
            "action": row.get("action_en"),
        } for row in rows if row.get("button") and row.get("action_en")]
        content_id = f"controls.{platform}.{_slug(game)}"
        record = _record(
            content_id=content_id,
            category="game_controls",
            kind="control_map",
            source_path=path,
            source_row=summary,
            thai_fields={"summary": summary.get("text"), "controls": controls},
            facts={
                "game": game,
                "platform": summary.get("platform"),
                "platform_key": platform,
                "coverage_status": summary.get("coverage_status"),
                "control_count": len(controls),
                "source_urls": summary.get("source_urls") or [],
            },
            aliases=[game, *list(summary.get("aliases") or [])],
            legacy_english={"controls": english_controls},
        )
        output.append((f"game_controls/{platform}/{_slug(game)}.json", record))
    return output


def _competition_records(path: Path) -> list[tuple[str, dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in _read_jsonl(path):
        grouped[str(row.get("document_id") or row.get("id") or "unknown")].append(row)
    output: list[tuple[str, dict[str, Any]]] = []
    for document_id, rows in sorted(grouped.items()):
        rows.sort(key=lambda row: (int(row.get("section_index") or 0), int(row.get("chunk_index") or 0)))
        first = rows[0]
        sections = [{
            "section_title": row.get("section_title"),
            "text": row.get("text"),
            "section_index": row.get("section_index"),
        } for row in rows]
        content_id = f"competition.{_slug(document_id)}"
        record = _record(
            content_id=content_id,
            category="competition_rules",
            kind="competition_document",
            source_path=path,
            source_row=first,
            thai_fields={"title": first.get("title"), "sections": sections},
            facts={"game": first.get("game"), "tournament": first.get("tournament"), "document_id": document_id},
            aliases=[first.get("game"), first.get("tournament"), first.get("title")],
        )
        output.append((f"competition/{_slug(document_id)}.json", record))
    return output


def _closure_records(path: Path) -> list[tuple[str, dict[str, Any]]]:
    output: list[tuple[str, dict[str, Any]]] = []
    for row in _read_jsonl(path):
        date_value = str(row.get("date") or "")
        content_id = f"schedule.closure.{date_value}"
        record = _record(
            content_id=content_id,
            category="schedule",
            kind="service_closure",
            source_path=path,
            source_row=row,
            thai_fields={"title": row.get("title"), "note": row.get("note")},
            facts={"date": date_value, "status": row.get("status")},
            aliases=[row.get("title"), date_value],
        )
        output.append((f"schedule/closures/{date_value}.json", record))
    return output


def _rule_records(rule_dir: Path) -> list[tuple[str, dict[str, Any]]]:
    output: list[tuple[str, dict[str, Any]]] = []
    for path in sorted(rule_dir.glob("*.jsonl")):
        for row in _read_jsonl(path):
            route_category = str(row.get("category") or "rules")
            category = "booking" if route_category == "reservation" else "rules"
            folder = category
            content_id = str(row.get("id") or "")
            record = _record(
                content_id=content_id,
                category=category,
                kind="policy_rule",
                source_path=path,
                source_row=row,
                thai_fields={"answer": row.get("answer_th")},
                facts={
                    "route_category": route_category,
                    "intent": row.get("intent"),
                    "patterns": row.get("patterns") or [],
                    "priority": row.get("priority"),
                },
                aliases=list(row.get("patterns") or []),
                legacy_english={"answer": row.get("answer_en")},
            )
            output.append((f"{folder}/{_slug(content_id)}.json", record))
    return output


def build_records() -> list[tuple[str, dict[str, Any]]]:
    curated = ROOT / "data" / "curated"
    records: list[tuple[str, dict[str, Any]]] = []
    records.extend(_simple_records(curated / "game_item_details.jsonl", "games", "game_profile", ("title", "summary_th", "how_to_play_th", "genre"), folder="games"))
    records.extend(_simple_records(curated / "equipment_item_details.jsonl", "resources", "equipment", ("item", "what_th", "how_to_use_th", "use_cases_th", "note_th"), folder="resources/equipment"))
    records.extend(_simple_records(curated / "member_profiles.jsonl", "members", "member", ("name", "role", "affiliation"), folder="members"))
    records.extend(_simple_records(curated / "curated_facts_service_fee_2026_aliases.jsonl", "services", "service_fee_policy", ("title", "text"), folder="services"))
    records.extend(_simple_records(curated / "curated_facts.jsonl", "knowledge", "knowledge_fact", ("title", "text"), folder="knowledge"))
    records.extend(_availability_records(curated / "service_game_availability.jsonl"))
    records.extend(_control_records(curated / "game_control_facts.jsonl"))
    records.extend(_competition_records(ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl"))
    records.extend(_closure_records(ROOT / "data" / "calendar" / "service_closures.jsonl"))
    records.extend(_rule_records(ROOT / "data" / "rules"))
    paths = [path for path, _record_value in records]
    if len(paths) != len(set(paths)):
        raise RuntimeError("Canonical output path collision")
    validation = validate_records([record for _path, record in records])
    if not validation.ok:
        raise RuntimeError("\n".join(validation.errors))
    return sorted(records, key=lambda item: item[0])


def _write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for _ in range(20):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            time.sleep(0.15)
    raise RuntimeError(f"Unable to replace {path}")


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


def write_repository(records: list[tuple[str, dict[str, Any]]], output: Path, *, replace_generated: bool = False) -> dict[str, Any]:
    if output.exists():
        existing = {path.name for path in output.iterdir()}
        allowed_seed_files = {"README.md", "schema"}
        generated_paths = {
            "booking", "competition", "contact", "game_controls", "games", "knowledge", "members",
            "no_answer", "overview", "penalty", "resources", "rules", "schedule", "services",
            "review", "projections", "manifest.json",
        }
        unmanaged = existing - allowed_seed_files - generated_paths
        if unmanaged:
            raise RuntimeError(f"Refusing to overwrite non-empty output directory: {output}")
        generated_existing = existing & generated_paths
        if generated_existing and not replace_generated:
            raise RuntimeError("Generated content already exists; use --replace-generated after reviewing the source migration.")
        if replace_generated:
            resolved_output = output.resolve()
            if resolved_output != CONTENT_ROOT.resolve():
                raise RuntimeError("--replace-generated is allowed only for the default data/content directory")
            for name in generated_existing:
                target = output / name
                if target.is_dir():
                    shutil.rmtree(target)
                else:
                    target.unlink()
    output.mkdir(parents=True, exist_ok=True)
    categories = Counter()
    drafts: list[dict[str, Any]] = []
    for relative, record in records:
        _write_json_atomic(output / relative, record)
        categories[record["category"]] += 1
        thai_fields = record["locales"]["th"]["fields"]
        english = record["locales"]["en"]
        for field, value in thai_fields.items():
            if value in (None, "", [], {}):
                continue
            drafts.append({
                "content_id": record["content_id"],
                "category": record["category"],
                "field": field,
                "locale": "en",
                "source_text": value,
                "source_text_sha256": source_sha256(value),
                "text": english["fields"].get(field, ""),
                "status": "draft" if english["status"] != "approved" else "approved",
                "approved_by": english.get("approved_by", ""),
                "approved_at": english.get("approved_at", ""),
                "source_content_path": relative,
            })
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "record_count": len(records),
        "category_counts": dict(sorted(categories.items())),
        "english_draft_count": len(drafts),
        "english_approved_count": 0,
    }
    _write_json_atomic(output / "manifest.json", manifest)
    _write_jsonl_atomic(output / "review" / "en_localization_drafts.jsonl", drafts)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Create the grouped canonical PSU Esports content repository.")
    parser.add_argument("--output", type=Path, default=CONTENT_ROOT)
    parser.add_argument("--check", action="store_true", help="Validate generated records without writing files.")
    parser.add_argument("--replace-generated", action="store_true", help="Replace only prior generated folders under the default data/content directory.")
    args = parser.parse_args()
    records = build_records()
    if args.check:
        print(json.dumps({"ok": True, "record_count": len(records), "output": str(args.output)}, ensure_ascii=False, indent=2))
        return 0
    manifest = write_repository(records, args.output, replace_generated=args.replace_generated)
    print(json.dumps({"ok": True, "output": str(args.output), "manifest": manifest}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
