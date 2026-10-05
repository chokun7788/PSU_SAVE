from __future__ import annotations

"""Rebuild all runtime RAG artifacts from published Canonical Content.

Run this after an approved content change.  English drafts are intentionally
ignored until their canonical record is explicitly approved.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_content import CONTENT_ROOT, load_records, validate_records
from app.knowledge.canonical_retrieval import clear_canonical_rag_cache
from app.pipeline.semantic_vector_retrieval import build_semantic_index
from app.pipeline.vector_retrieval import write_vector_index
from tools.build_canonical_projections import _write_jsonl_atomic, project


def _write_projection(records: tuple[dict, ...], output: Path) -> dict[str, int]:
    structured, rag_th, rag_en = project(records)
    _write_jsonl_atomic(output / "structured_projection.jsonl", structured)
    _write_jsonl_atomic(output / "rag_th_projection.jsonl", rag_th)
    _write_jsonl_atomic(output / "rag_en_approved_projection.jsonl", rag_en)
    manifest = {
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "content_records": len(records),
        "structured_records": len(structured),
        "rag_th_records": len(rag_th),
        "rag_en_approved_records": len(rag_en),
    }
    temporary = output / "manifest.json.tmp"
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output / "manifest.json")
    clear_canonical_rag_cache()
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild runtime RAG artifacts from published Canonical Content.")
    parser.add_argument("--skip-semantic", action="store_true", help="Rebuild projection and lexical index only.")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--embedding-timeout-sec", type=float, default=120.0)
    args = parser.parse_args()

    records = load_records(CONTENT_ROOT)
    validation = validate_records(records)
    if not validation.ok:
        raise SystemExit("\n".join(validation.errors))

    projection = _write_projection(records, CONTENT_ROOT / "projections")
    vector = write_vector_index()
    semantic: dict[str, object] | None = None
    if not args.skip_semantic:
        semantic = build_semantic_index(
            batch_size=max(1, args.batch_size),
            timeout_sec=max(1.0, args.embedding_timeout_sec),
        ).as_dict()

    print(json.dumps({
        "ok": True,
        "projection": projection,
        "vector_docs": vector.get("doc_count"),
        "semantic": semantic,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
