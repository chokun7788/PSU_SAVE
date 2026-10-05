from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["PSU_SEMANTIC_RETRIEVAL"] = "1"
os.environ["PSU_EMBEDDING_TIMEOUT_SEC"] = "8"

from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.request_deadline import request_deadline  # noqa: E402
from app.pipeline.semantic_vector_retrieval import retrieve_semantic_guarded  # noqa: E402


def main() -> int:
    route = PipelineRoute("games", "game_detail", 0.95, "fact", "medium", "live canonical probe")
    with request_deadline(20.0):
        hits, trace = retrieve_semantic_guarded(
            "VALORANT เล่นยังไง",
            route,
            required_entity_ids=("valorant",),
            required_facets=("how_to_play",),
            locale="th",
        )
    assert hits, trace.detail
    assert any(hit.get("_canonical_projection") for hit in hits), [hit.get("id") for hit in hits]
    assert all(hit.get("game") == "VALORANT" for hit in hits), [hit.get("game") for hit in hits]
    assert trace.metadata["doc_count"] >= 250
    print(f"OK live canonical semantic RAG hits={len(hits)} top={hits[0]['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
