from __future__ import annotations

import sys
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute
from app.pipeline.semantic_vector_retrieval import has_semantic_domain_anchor, refine_route_with_semantic_evidence


def main() -> int:
    os.environ["PSU_SEMANTIC_RETRIEVAL"] = "1"
    assert not has_semantic_domain_anchor("what is a mechanical keyboard?")
    assert has_semantic_domain_anchor("What are PSU Esports Studio opening hours?")
    route = PipelineRoute("general", "detail", 0.4, "fact", "low", "general question")
    refined, trace = refine_route_with_semantic_evidence("what is a mechanical keyboard?", route)
    assert refined == route
    assert trace.decision == "skipped_unanchored_general"
    print("OK unanchored general questions bypass semantic retrieval")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
