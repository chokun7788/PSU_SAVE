from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.localization import LOCALE_ROOT, LocalizationRecord, source_text_sha256


SOURCE_SPECS = (
    (ROOT / "data" / "curated" / "game_item_details.jsonl", ("summary_th", "how_to_play_th", "genre")),
    (ROOT / "data" / "curated" / "equipment_item_details.jsonl", ("what_th", "how_to_use_th", "use_cases_th", "note_th")),
    (ROOT / "data" / "curated" / "member_profiles.jsonl", ("name", "role", "affiliation")),
    (ROOT / "data" / "curated" / "curated_facts.jsonl", ("title", "text")),
    (ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl", ("title", "section_title", "text")),
)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    text = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def _member_id(row: dict[str, Any]) -> str:
    value = "|".join(str(row.get(key) or "") for key in ("name", "role", "affiliation"))
    return "member_" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def source_records() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path, _fields in SOURCE_SPECS:
        for row in _read_jsonl(path):
            copied = dict(row)
            content_id = str(copied.get("id") or "").strip()
            if not content_id and path.name == "member_profiles.jsonl":
                content_id = _member_id(copied)
                copied["id"] = content_id
            if content_id:
                copied["_source_path"] = str(path.relative_to(ROOT))
                records[content_id] = copied
    return records


def source_fields() -> dict[tuple[str, str], dict[str, Any]]:
    records = source_records()
    fields: dict[tuple[str, str], dict[str, Any]] = {}
    for path, configured_fields in SOURCE_SPECS:
        path_key = str(path.relative_to(ROOT))
        for content_id, row in records.items():
            if row.get("_source_path") != path_key:
                continue
            for field in configured_fields:
                value = row.get(field)
                if value not in (None, "", []):
                    fields[(content_id, field)] = row
    return fields


def export_drafts(output: Path) -> int:
    rows = []
    for (content_id, field), source in sorted(source_fields().items()):
        rows.append({
            "content_id": content_id,
            "field": field,
            "locale": "en",
            "text": "",
            "source_text": source.get(field),
            "source_text_sha256": source_text_sha256(source.get(field)),
            "status": "draft",
            "version": 1,
            "approved_by": "",
            "approved_at": "",
            "source_path": source.get("_source_path"),
            "category": source.get("category"),
            "title": source.get("title") or source.get("item") or source.get("name") or content_id,
        })
    _write_jsonl(output, rows)
    return len(rows)


def validate_candidate(path: Path, *, require_approved: bool = False) -> tuple[list[dict[str, Any]], list[str]]:
    rows = _read_jsonl(path)
    fields = source_fields()
    errors: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    validated: list[dict[str, Any]] = []
    for index, row in enumerate(rows, 1):
        try:
            record = LocalizationRecord.from_dict(row)
        except (TypeError, ValueError) as exc:
            errors.append(f"row {index}: {exc}")
            continue
        key = (record.content_id, record.field, record.locale)
        if key in seen:
            errors.append(f"row {index}: duplicate key {key}")
            continue
        seen.add(key)
        source = fields.get((record.content_id, record.field))
        if source is None:
            errors.append(f"row {index}: unknown source field {record.content_id}/{record.field}")
            continue
        expected_hash = source_text_sha256(source.get(record.field))
        if record.source_text_sha256 != expected_hash:
            errors.append(f"row {index}: stale source hash {record.content_id}/{record.field}")
        if record.status == "approved":
            if not record.usable:
                errors.append(f"row {index}: approved row is missing text/reviewer/timestamp")
            if re.search(r"[\u0E00-\u0E7F]", record.text):
                errors.append(f"row {index}: approved English text contains Thai prose")
        elif require_approved:
            continue
        validated.append({
            "content_id": record.content_id,
            "field": record.field,
            "locale": record.locale,
            "text": record.text,
            "source_text_sha256": record.source_text_sha256,
            "status": record.status,
            "version": record.version,
            "approved_by": record.approved_by,
            "approved_at": record.approved_at,
        })
    return validated, errors


def _selection_key(value: str) -> tuple[str, str]:
    """Parse the explicit ``content_id:field`` selector used by reviewers."""
    content_id, separator, field = str(value or "").rpartition(":")
    if not separator or not content_id.strip() or not field.strip():
        raise ValueError("selection must use content_id:field")
    return content_id.strip(), field.strip()


def _draft_rows(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    """Load only current, non-empty English drafts that still match their Thai source."""
    known_fields = source_fields()
    rows: dict[tuple[str, str], dict[str, Any]] = {}
    for index, row in enumerate(_read_jsonl(path), 1):
        record = LocalizationRecord.from_dict(row)
        key = (record.content_id, record.field)
        if key in rows:
            raise ValueError(f"duplicate draft at row {index}: {record.content_id}/{record.field}")
        source = known_fields.get(key)
        if source is None:
            raise ValueError(f"unknown source field at row {index}: {record.content_id}/{record.field}")
        if record.locale != "en" or record.status != "draft" or not record.text:
            continue
        if record.source_text_sha256 != source_text_sha256(source.get(record.field)):
            raise ValueError(f"stale source hash at row {index}: {record.content_id}/{record.field}")
        rows[key] = dict(row)
    return rows


def write_review_queue(draft_path: Path, output: Path, *, category: str = "") -> int:
    """Write a human-readable queue. This never changes a runtime registry."""
    requested_category = category.strip().casefold()
    sources = source_records()
    rows = _draft_rows(draft_path)
    selected = []
    for (content_id, field), row in sorted(rows.items()):
        source = sources[content_id]
        source_category = str(source.get("category") or "knowledge")
        if requested_category and source_category.casefold() != requested_category:
            continue
        selected.append((content_id, field, row, source, source_category))

    lines = [
        "# English Localization Review Queue",
        "",
        "> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.",
        "",
        f"- Draft input: `{draft_path}`",
        f"- Filter: `{category or 'all categories'}`",
        f"- Review items: **{len(selected)}**",
        "",
        "## Review procedure",
        "",
        "1. Compare every English draft with its Thai source, especially prices, time limits, exceptions, and prohibitions.",
        "2. Select only accurate records using the selector shown under each item.",
        "3. Create an approval candidate with `approve`, then run `validate`, then `publish`.",
        "4. Do not approve a wording that changes scope, certainty, names, prices, or conditions.",
        "",
        "## Commands after review",
        "",
        "Create a candidate from explicit, reviewed selectors (replace the reviewer and selectors):",
        "",
        "```powershell",
        f"py tools/manage_english_localizations.py approve {draft_path} --output data/locales/en/reviewed_candidate.jsonl --reviewer <reviewer-id> --select <content_id:field>",
        "```",
        "",
        "Then validate it before publishing. Publishing builds one atomic English release; it never publishes an individual draft directly.",
        "",
        "```powershell",
        "py tools/manage_english_localizations.py validate data/locales/en/reviewed_candidate.jsonl",
        "py tools/manage_english_localizations.py publish data/locales/en/reviewed_candidate.jsonl --build-vector",
        "```",
        "",
    ]
    for number, (content_id, field, row, source, source_category) in enumerate(selected, 1):
        lines.extend([
            f"## {number}. {content_id} / {field}",
            "",
            f"- Selector: `{content_id}:{field}`",
            f"- Category: `{source_category}`",
            f"- Title: {source.get('title') or source.get('item') or source.get('name') or content_id}",
            f"- Source hash: `{row['source_text_sha256']}`",
            "",
            "**Thai source**",
            "",
            str(row.get("source_text") or source.get(field) or ""),
            "",
            "**English draft**",
            "",
            str(row.get("text") or ""),
            "",
        ])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return len(selected)


def approve_selected_drafts(
    draft_path: Path,
    output: Path,
    *,
    selections: Iterable[str],
    reviewer: str,
    approved_at: str = "",
    existing_candidate: Path | None = None,
) -> int:
    """Create a publish candidate from explicitly selected, reviewable draft rows."""
    reviewer = reviewer.strip()
    if not reviewer:
        raise ValueError("reviewer is required")
    chosen = [_selection_key(value) for value in selections]
    if not chosen:
        raise ValueError("at least one --select content_id:field is required")
    if len(set(chosen)) != len(chosen):
        raise ValueError("duplicate --select value")

    drafts = _draft_rows(draft_path)
    candidate_rows = _read_jsonl(existing_candidate) if existing_candidate and existing_candidate.exists() else []
    by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in candidate_rows:
        record = LocalizationRecord.from_dict(row)
        by_key[(record.content_id, record.field, record.locale)] = dict(row)

    timestamp = approved_at.strip() or datetime.now().astimezone().isoformat(timespec="seconds")
    for content_id, field in chosen:
        draft = drafts.get((content_id, field))
        if draft is None:
            raise ValueError(f"selected current non-empty draft not found: {content_id}/{field}")
        approved = dict(draft)
        approved["status"] = "approved"
        approved["approved_by"] = reviewer
        approved["approved_at"] = timestamp
        by_key[(content_id, field, "en")] = approved

    _write_jsonl(output, [by_key[key] for key in sorted(by_key)])
    return len(chosen)


def _projection_rows(approved: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records = source_records()
    structured: list[dict[str, Any]] = []
    rag: list[dict[str, Any]] = []
    for localization in approved:
        source = records[localization["content_id"]]
        projection = {
            "projection_id": f"{localization['content_id']}::{localization['field']}::en",
            "content_id": localization["content_id"],
            "field": localization["field"],
            "locale": "en",
            "text": localization["text"],
            "category": source.get("category") or "knowledge",
            "title": source.get("title") or source.get("item") or source.get("name") or localization["content_id"],
            "game": source.get("game") or "",
            "target": source.get("game") or source.get("item") or source.get("name") or "",
            "source_url": source.get("source_url") or "",
            "source_text_sha256": localization["source_text_sha256"],
            "version": localization["version"],
            "status": "published",
            "trust_level": source.get("trust_level") or ("official" if "psu.ac.th" in str(source.get("source_url") or "") else "internal_verified"),
        }
        rag.append(projection)
        if localization["field"] in {"summary_th", "how_to_play_th", "genre", "what_th", "how_to_use_th", "use_cases_th", "note_th", "name", "role", "affiliation"}:
            structured.append(projection)
    return structured, rag


def publish(candidate: Path, *, build_vector: bool = False) -> Path:
    rows, errors = validate_candidate(candidate)
    if errors:
        raise SystemExit("\n".join(errors))
    approved = [row for row in rows if row["status"] == "approved"]
    timestamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    release_id = f"en-{timestamp}"
    releases = LOCALE_ROOT / "releases"
    staging = releases / f".{release_id}.staging"
    release = releases / release_id
    if staging.exists():
        resolved_releases = releases.resolve()
        resolved_staging = staging.resolve()
        if resolved_staging.parent != resolved_releases or not resolved_staging.name.endswith(".staging"):
            raise RuntimeError(f"Refusing to remove unsafe staging path: {resolved_staging}")
        shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=False)
    structured, rag = _projection_rows(approved)
    _write_jsonl(staging / "approved_localizations.jsonl", approved)
    _write_jsonl(staging / "structured_projection.jsonl", structured)
    _write_jsonl(staging / "rag_projection.jsonl", rag)
    manifest = {
        "release_id": release_id,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "approved_localizations": len(approved),
        "structured_records": len(structured),
        "rag_records": len(rag),
        "candidate_sha256": hashlib.sha256(candidate.read_bytes()).hexdigest(),
    }
    (staging / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    if build_vector and rag:
        from app.pipeline.semantic_vector_retrieval import build_semantic_index

        build_semantic_index(path=staging / "semantic_index.json", rows=rag)
    os.replace(staging, release)
    current_tmp = LOCALE_ROOT / "CURRENT.tmp"
    current_tmp.write_text(release_id + "\n", encoding="utf-8")
    os.replace(current_tmp, LOCALE_ROOT / "CURRENT")
    # Keep the requested registry path as a human-readable mirror. Runtime uses
    # CURRENT, so a mirror failure cannot expose half a release.
    _write_jsonl(LOCALE_ROOT / "approved_localizations.jsonl", approved)
    return release


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage reviewed English localization overlays.")
    sub = parser.add_subparsers(dest="command", required=True)
    export = sub.add_parser("export-drafts")
    export.add_argument("--output", type=Path, default=LOCALE_ROOT / "localization_review_drafts.jsonl")
    validate = sub.add_parser("validate")
    validate.add_argument("candidate", type=Path)
    review = sub.add_parser("review-queue")
    review.add_argument("draft", type=Path)
    review.add_argument("--output", type=Path, required=True)
    review.add_argument("--category", default="", help="Optional source category, for example knowledge or competition_rules.")
    approve = sub.add_parser("approve")
    approve.add_argument("draft", type=Path)
    approve.add_argument("--output", type=Path, required=True)
    approve.add_argument("--select", action="append", required=True, help="Explicit content_id:field selected after human review. Repeat for each item.")
    approve.add_argument("--reviewer", required=True, help="Authorized reviewer identifier.")
    approve.add_argument("--approved-at", default="", help="Optional ISO-8601 approval timestamp.")
    approve.add_argument("--existing-candidate", type=Path, help="Optional candidate file to extend without discarding prior approvals.")
    publish_parser = sub.add_parser("publish")
    publish_parser.add_argument("candidate", type=Path)
    publish_parser.add_argument("--build-vector", action="store_true")
    args = parser.parse_args()
    if args.command == "export-drafts":
        count = export_drafts(args.output)
        print(json.dumps({"ok": True, "draft_count": count, "output": str(args.output)}, ensure_ascii=False))
        return 0
    if args.command == "validate":
        rows, errors = validate_candidate(args.candidate)
        print(json.dumps({"ok": not errors, "row_count": len(rows), "errors": errors}, ensure_ascii=False, indent=2))
        return 0 if not errors else 1
    if args.command == "review-queue":
        count = write_review_queue(args.draft, args.output, category=args.category)
        print(json.dumps({"ok": True, "review_count": count, "output": str(args.output)}, ensure_ascii=False))
        return 0
    if args.command == "approve":
        count = approve_selected_drafts(
            args.draft,
            args.output,
            selections=args.select,
            reviewer=args.reviewer,
            approved_at=args.approved_at,
            existing_candidate=args.existing_candidate,
        )
        rows, errors = validate_candidate(args.output)
        print(json.dumps({"ok": not errors, "approved_count": count, "candidate": str(args.output), "errors": errors}, ensure_ascii=False, indent=2))
        return 0 if not errors else 1
    release = publish(args.candidate, build_vector=args.build_vector)
    print(json.dumps({"ok": True, "release": str(release)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
