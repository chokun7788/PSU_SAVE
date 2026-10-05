from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_retrieval import load_canonical_rag_rows  # noqa: E402
from app.pipeline.retrieval import retrieve_curated  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.semantic_vector_retrieval import retrieve_semantic_guarded  # noqa: E402


def main() -> int:
    rows = load_canonical_rag_rows()
    assert len(rows) >= 500
    assert all(row["language"] == "th" for row in rows)
    assert all(row["dynamic_knowledge"] for row in rows)

    competition = [row for row in rows if row["category"] == "competition_rules"]
    assert len(competition) >= 100
    assert any("section:" in row["id"] for row in competition)

    game_hits, _ = retrieve_curated("VALORANT เล่นยังไง", "games", limit=3)
    assert any(hit.get("_canonical_projection") and hit.get("game") == "VALORANT" for hit in game_hits)

    rule_hits, _ = retrieve_curated("CS2 ใช้ภาษาอะไรในการแข่งขัน", "competition_rules", limit=3)
    assert any(hit.get("_canonical_projection") and hit.get("game") == "Counter-Strike 2" for hit in rule_hits)

    valorant = next(
        row for row in rows
        if row["category"] == "games"
        and row.get("game") == "VALORANT"
        and "how_to_play" in row.get("facets", [])
    )
    other_game = next(row for row in rows if row["category"] == "games" and row.get("game") not in {"", "VALORANT"})
    index = {
        "model": "test-model",
        "dimensions": 1,
        "backend": "test",
        "docs": [
            {"id": valorant["id"], "category": "games", "vector": [1.0], "row": valorant},
            {"id": other_game["id"], "category": "games", "vector": [1.0], "row": other_game},
        ],
    }
    route = PipelineRoute("games", "game_detail", 0.95, "fact", "medium", "test")
    strict_hits, trace = retrieve_semantic_guarded(
        "VALORANT เล่นยังไง",
        route,
        query_vector=(1.0,),
        index=index,
        required_entity_ids=("valorant",),
        required_facets=("how_to_play",),
        locale="th",
    )
    assert strict_hits and all(hit.get("game") == "VALORANT" for hit in strict_hits), trace.metadata
    assert trace.metadata["blocked"].get("entity_mismatch", 0) >= 1
    print(f"OK canonical RAG rows={len(rows)} competition_chunks={len(competition)} strict_target={strict_hits[0]['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
