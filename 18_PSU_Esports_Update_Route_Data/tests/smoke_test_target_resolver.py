from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.target_resolver import resolve_target_candidate  # noqa: E402


def main() -> int:
    previous = os.environ.get("PSU_TARGET_RERANKER")
    os.environ["PSU_TARGET_RERANKER"] = "0"
    try:
        nintendo_price = resolve_target_candidate(
            "Nintendo Switch ราคาเท่าไหร่",
            operation="price",
            preferred_domains=("service_fee",),
        )
        assert nintendo_price.top_candidate is not None, nintendo_price.as_dict()
        assert nintendo_price.top_candidate.domain == "service_fee", nintendo_price.as_dict()

        nintendo_game = resolve_target_candidate(
            "Nintendo Switch Sports ปุ่มอะไร",
            operation="controls",
            preferred_domains=("games",),
        )
        assert nintendo_game.status == "exact", nintendo_game.as_dict()
        assert nintendo_game.top_candidate is not None, nintendo_game.as_dict()
        assert nintendo_game.top_candidate.domain == "games", nintendo_game.as_dict()
        assert nintendo_game.top_candidate.label == "Nintendo Switch Sports", nintendo_game.as_dict()

        modern_warfare = resolve_target_candidate(
            "Modern Warfare III ราคาเท่าไหร่",
            operation="price",
            preferred_domains=("service_fee",),
        )
        assert modern_warfare.status == "exact", modern_warfare.as_dict()
        assert modern_warfare.top_candidate is not None, modern_warfare.as_dict()
        assert modern_warfare.top_candidate.domain == "games", modern_warfare.as_dict()
        assert modern_warfare.top_candidate.label == "Call of Duty: Modern Warfare III", modern_warfare.as_dict()

        pc_price = resolve_target_candidate(
            "PC ราคาเท่าไหร่",
            operation="price",
            preferred_domains=("service_fee",),
        )
        assert pc_price.top_candidate is not None, pc_price.as_dict()
        assert pc_price.top_candidate.domain == "service_fee", pc_price.as_dict()
    finally:
        if previous is None:
            os.environ.pop("PSU_TARGET_RERANKER", None)
        else:
            os.environ["PSU_TARGET_RERANKER"] = previous

    print("OK target resolver smoke tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
