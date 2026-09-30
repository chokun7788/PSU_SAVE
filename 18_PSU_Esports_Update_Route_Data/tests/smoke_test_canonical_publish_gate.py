from __future__ import annotations

"""Regression guard: only explicitly published Canonical records reach RAG."""

import copy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_content import load_records, validate_records
from tools.build_canonical_projections import project


def main() -> int:
    records = list(load_records())
    assert validate_records(records).ok
    published = copy.deepcopy(records[0])
    published["content_id"] = "publish-gate-published"
    published["lifecycle"] = {"status": "published", "version": 1}
    draft = copy.deepcopy(records[1])
    draft["content_id"] = "publish-gate-draft"
    draft["lifecycle"] = {"status": "draft", "version": 1}

    structured, rag_th, rag_en = project((published, draft))
    assert [row["content_id"] for row in structured] == ["publish-gate-published"]
    assert {row["content_id"] for row in rag_th} == {"publish-gate-published"}
    assert not rag_en
    print("OK unpublished Canonical records are excluded from Structured and RAG projections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
