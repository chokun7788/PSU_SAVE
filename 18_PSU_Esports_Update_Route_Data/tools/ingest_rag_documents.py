from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DEFAULT_OUTPUT = ROOT / "data" / "curated" / "dynamic_knowledge.jsonl"
DEFAULT_INDEX = ROOT / "data" / "vector" / "psu_semantic_vector_index.json"
ALLOWED_CATEGORIES = {"knowledge", "events_news", "about_us", "games", "equipment"}
ALLOWED_TRUST_LEVELS = {"official", "user_confirmed", "internal_verified", "secondary"}


@dataclass
class IngestionReport:
    input_documents: int = 0
    published_documents: int = 0
    output_chunks: int = 0
    replaced_documents: int = 0
    skipped_drafts: int = 0
    errors: list[str] = field(default_factory=list)
    output_path: str = ""
    semantic_index: dict[str, Any] | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "input_documents": self.input_documents,
            "published_documents": self.published_documents,
            "output_chunks": self.output_chunks,
            "replaced_documents": self.replaced_documents,
            "skipped_drafts": self.skipped_drafts,
            "errors": self.errors,
            "output_path": self.output_path,
            "semantic_index": self.semantic_index,
        }


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} must be a JSON object")
        rows.append(value)
    return rows


def _markdown_document(path: Path) -> dict[str, Any]:
    sidecar = path.with_suffix(path.suffix + ".meta.json")
    if not sidecar.exists():
        sidecar = path.with_suffix(".meta.json")
    if not sidecar.exists():
        raise ValueError(f"{path} requires metadata sidecar {path.stem}.meta.json")
    metadata = _read_json(sidecar)
    if not isinstance(metadata, dict):
        raise ValueError(f"{sidecar} must contain one JSON object")
    return {**metadata, "text": path.read_text(encoding="utf-8-sig"), "_input_file": str(path)}


def read_documents(path: Path) -> list[dict[str, Any]]:
    if path.is_dir():
        documents: list[dict[str, Any]] = []
        for child in sorted(path.iterdir()):
            name = child.name.lower()
            if (
                name == "readme.md"
                or name.endswith(".schema.json")
                or child.name.endswith(".meta.json")
                or child.suffix.lower() not in {".json", ".jsonl", ".md", ".txt"}
            ):
                continue
            documents.extend(read_documents(child))
        return documents
    if not path.exists():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    if suffix == ".jsonl":
        return [{**row, "_input_file": str(path)} for row in _read_jsonl(path)]
    if suffix == ".json":
        value = _read_json(path)
        values = value if isinstance(value, list) else [value]
        if any(not isinstance(item, dict) for item in values):
            raise ValueError(f"{path} must contain an object or an array of objects")
        return [{**item, "_input_file": str(path)} for item in values]
    if suffix in {".md", ".txt"}:
        return [_markdown_document(path)]
    raise ValueError(f"unsupported input type: {path}")


def _iso_date(value: Any, field_name: str, *, required: bool = False) -> str:
    text = str(value or "").strip()
    if not text:
        if required:
            raise ValueError(f"missing required field: {field_name}")
        return ""
    try:
        date.fromisoformat(text[:10])
    except ValueError as exc:
        raise ValueError(f"{field_name} must be ISO date YYYY-MM-DD: {text}") from exc
    return text


def validate_document(document: dict[str, Any]) -> dict[str, Any]:
    row = dict(document)
    for field_name in ("id", "title", "text", "category", "source_url", "trust_level", "updated_at"):
        if not str(row.get(field_name) or "").strip():
            raise ValueError(f"missing required field: {field_name}")
    row["id"] = re.sub(r"[^0-9A-Za-z_.-]+", "_", str(row["id"]).strip()).strip("_")
    if not row["id"]:
        raise ValueError("id contains no usable characters")
    row["category"] = str(row["category"]).strip()
    if row["category"] not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"unsupported category {row['category']!r}; allowed={sorted(ALLOWED_CATEGORIES)}"
        )
    row["trust_level"] = str(row["trust_level"]).strip()
    if row["trust_level"] not in ALLOWED_TRUST_LEVELS:
        raise ValueError(
            f"unsupported trust_level {row['trust_level']!r}; allowed={sorted(ALLOWED_TRUST_LEVELS)}"
        )
    row["updated_at"] = _iso_date(row.get("updated_at"), "updated_at", required=True)
    row["valid_from"] = _iso_date(row.get("valid_from"), "valid_from")
    row["valid_until"] = _iso_date(
        row.get("valid_until") or row.get("expires_at"),
        "valid_until",
    )
    row["status"] = str(row.get("status") or "draft").strip().lower()
    if row["status"] not in {"draft", "published", "archived"}:
        raise ValueError("status must be draft, published, or archived")
    row["time_sensitive"] = bool(row.get("time_sensitive"))
    row["freshness_verified"] = bool(row.get("freshness_verified"))
    row["retrieved_at"] = str(row.get("retrieved_at") or "").strip()
    if row["time_sensitive"] and not row["valid_until"]:
        raise ValueError("time_sensitive documents require valid_until")
    if row["freshness_verified"]:
        if not row["retrieved_at"] or not row["valid_until"]:
            raise ValueError("freshness_verified documents require retrieved_at and valid_until")
        if row["trust_level"] == "secondary":
            raise ValueError("secondary sources cannot be marked freshness_verified")
    row["tags"] = [str(value).strip() for value in row.get("tags", []) if str(value).strip()]
    row["aliases"] = [str(value).strip() for value in row.get("aliases", []) if str(value).strip()]
    row["priority"] = max(0, min(100, int(row.get("priority") or 50)))
    row["text"] = str(row["text"]).strip()
    row["title"] = str(row["title"]).strip()
    row["source_url"] = str(row["source_url"]).strip()
    row["dynamic_knowledge"] = True
    return row


def _split_long_paragraph(paragraph: str, max_chars: int) -> list[str]:
    if len(paragraph) <= max_chars:
        return [paragraph]
    sentences = [part.strip() for part in re.split(r"(?<=[.!?。！？])\s+|(?<=ครับ)\s+|(?<=ค่ะ)\s+", paragraph) if part.strip()]
    if len(sentences) <= 1:
        return [paragraph[offset:offset + max_chars].strip() for offset in range(0, len(paragraph), max_chars)]
    pieces: list[str] = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip()
        if current and len(candidate) > max_chars:
            pieces.append(current)
            current = sentence
        else:
            current = candidate
    if current:
        pieces.append(current)
    return pieces


def chunk_text(text: str, *, max_chars: int = 900, overlap_chars: int = 120) -> list[str]:
    max_chars = max(300, max_chars)
    overlap_chars = max(0, min(overlap_chars, max_chars // 3))
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n+", text) if part.strip()]
    units: list[str] = []
    for paragraph in paragraphs:
        units.extend(_split_long_paragraph(paragraph, max_chars))

    chunks: list[str] = []
    current = ""
    for unit in units:
        candidate = f"{current}\n\n{unit}".strip()
        if current and len(candidate) > max_chars:
            chunks.append(current)
            prefix = current[-overlap_chars:].lstrip() if overlap_chars else ""
            current = f"{prefix}\n\n{unit}".strip()
            if len(current) > max_chars:
                chunks.extend(
                    current[offset:offset + max_chars].strip()
                    for offset in range(0, len(current) - max_chars, max_chars - overlap_chars or max_chars)
                )
                current = current[-max_chars:]
        else:
            current = candidate
    if current:
        chunks.append(current)
    return [chunk for chunk in chunks if chunk]


def document_to_chunks(
    document: dict[str, Any],
    *,
    max_chars: int = 900,
    overlap_chars: int = 120,
) -> list[dict[str, Any]]:
    row = validate_document(document)
    if row["status"] != "published":
        return []
    chunks = chunk_text(row["text"], max_chars=max_chars, overlap_chars=overlap_chars)
    output: list[dict[str, Any]] = []
    content_hash = hashlib.sha256(row["text"].encode("utf-8")).hexdigest()
    for index, chunk in enumerate(chunks, 1):
        chunk_id = f"{row['id']}__c{index:03d}"
        output.append({
            **{key: value for key, value in row.items() if key not in {"id", "text", "_input_file"}},
            "id": chunk_id,
            "document_id": row["id"],
            "chunk_index": index,
            "chunk_count": len(chunks),
            "content_hash": content_hash,
            "text": chunk,
            "ingestion_source": "dynamic_rag",
            "input_file": str(row.get("_input_file") or ""),
        })
    return output


def _read_existing(path: Path) -> list[dict[str, Any]]:
    return _read_jsonl(path) if path.exists() else []


def _write_jsonl_atomic(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    temporary.replace(path)


def ingest(
    input_path: Path,
    *,
    output_path: Path = DEFAULT_OUTPUT,
    max_chars: int = 900,
    overlap_chars: int = 120,
    replace_all: bool = False,
    validate_only: bool = False,
    build_index: bool = False,
    index_path: Path = DEFAULT_INDEX,
) -> IngestionReport:
    report = IngestionReport(output_path=str(output_path))
    documents = read_documents(input_path)
    report.input_documents = len(documents)
    new_chunks: list[dict[str, Any]] = []
    incoming_document_ids: set[str] = set()
    for position, document in enumerate(documents, 1):
        source = str(document.get("_input_file") or input_path)
        try:
            validated = validate_document(document)
            if validated["status"] != "published":
                report.skipped_drafts += 1
                continue
            incoming_document_ids.add(validated["id"])
            chunks = document_to_chunks(
                document,
                max_chars=max_chars,
                overlap_chars=overlap_chars,
            )
            report.published_documents += 1
            new_chunks.extend(chunks)
        except Exception as exc:  # noqa: BLE001 - collect all document errors for admin review.
            report.errors.append(f"document {position} ({source}): {exc}")

    if report.errors:
        return report
    existing = [] if replace_all else _read_existing(output_path)
    retained = [
        row for row in existing
        if str(row.get("document_id") or row.get("id") or "") not in incoming_document_ids
    ]
    report.replaced_documents = len({
        str(row.get("document_id") or row.get("id") or "")
        for row in existing
        if str(row.get("document_id") or row.get("id") or "") in incoming_document_ids
    })
    merged = sorted(
        [*retained, *new_chunks],
        key=lambda row: (str(row.get("document_id") or ""), int(row.get("chunk_index") or 0)),
    )
    report.output_chunks = len(merged)
    if validate_only:
        return report

    _write_jsonl_atomic(output_path, merged)
    from app.pipeline.retrieval import load_curated_rows

    load_curated_rows.cache_clear()
    if build_index:
        from app.pipeline.semantic_vector_retrieval import build_semantic_index

        result = build_semantic_index(path=index_path)
        report.semantic_index = result.as_dict()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate, chunk, publish, and optionally embed dynamic RAG documents."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-chars", type=int, default=900)
    parser.add_argument("--overlap-chars", type=int, default=120)
    parser.add_argument("--replace-all", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--build-index", action="store_true")
    parser.add_argument("--index-path", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args()

    report = ingest(
        args.input,
        output_path=args.output,
        max_chars=args.max_chars,
        overlap_chars=args.overlap_chars,
        replace_all=args.replace_all,
        validate_only=args.validate_only,
        build_index=args.build_index,
        index_path=args.index_path,
    )
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
