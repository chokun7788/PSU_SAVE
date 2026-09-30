from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.semantic_vector_retrieval import retrieve_semantic_guarded  # noqa: E402


def _doc(identifier: str, game: str) -> dict:
    row = {
        "id": identifier,
        "category": "games",
        "game": game,
        "text": f"Verified information about {game}",
        "status": "published",
        "source_url": "https://esports.phuket.psu.ac.th/Services/our-games",
    }
    return {"id": identifier, "category": "games", "row": row, "vector": [1.0]}


def main() -> int:
    index = {"model": "test", "dimensions": 1, "doc_count": 2, "docs": [
        _doc("game_valorant", "VALORANT"),
        _doc("game_cs2", "Counter-Strike 2"),
    ]}
    route = PipelineRoute("games", "game_detail_lookup", 0.95, "fact", "low", "test")
    hits, trace = retrieve_semantic_guarded(
        "Tell me about VALORANT",
        route,
        required_entity_ids=("valorant",),
        query_vector=(1.0,),
        index=index,
    )
    assert [hit["id"] for hit in hits] == ["game_valorant"]
    assert trace.metadata["blocked"].get("legacy_target_mismatch") == 1
    assert trace.metadata["second_score"] is None
    assert trace.metadata["margin"] is None
    print("OK semantic retrieval rejects legacy evidence that explicitly names a different game target")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
