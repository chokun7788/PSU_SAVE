from __future__ import annotations

import json
import unittest
from pathlib import Path

from app.pipeline.competition_taxonomy import (
    CANONICAL_FACETS,
    COMPETITION_GAME_IDS,
    REVIEW_MODULES,
)


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data" / "competition_rules" / "review"


class CompetitionTaxonomyContractTests(unittest.TestCase):
    def test_schema_enums_match_runtime_taxonomy(self) -> None:
        review = json.loads((REVIEW_DIR / "competition_rule_claim_v2_review.schema.json").read_text(encoding="utf-8"))
        runtime = json.loads((REVIEW_DIR / "competition_rule_claim_v2_1_runtime.schema.json").read_text(encoding="utf-8"))

        self.assertEqual(set(CANONICAL_FACETS), set(review["$defs"]["canonicalFacet"]["enum"]))
        self.assertEqual(set(CANONICAL_FACETS), set(runtime["$defs"]["canonicalFacet"]["enum"]))
        self.assertEqual(
            set(COMPETITION_GAME_IDS),
            set(review["properties"]["retrieval"]["properties"]["game_id"]["enum"]),
        )
        self.assertEqual(
            set(COMPETITION_GAME_IDS),
            set(runtime["properties"]["retrieval"]["properties"]["game_id"]["enum"]),
        )
        self.assertEqual(
            set(REVIEW_MODULES),
            set(review["properties"]["retrieval"]["properties"]["module_proposed"]["enum"]),
        )

    def test_review_queue_uses_only_shared_taxonomy_values(self) -> None:
        rows = [
            json.loads(line)
            for line in (REVIEW_DIR / "competition_rule_claim_v2_review_queue.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        self.assertFalse({row["retrieval"]["game_id"] for row in rows} - set(COMPETITION_GAME_IDS))
        self.assertFalse({row["retrieval"]["facet_proposed"] for row in rows} - set(CANONICAL_FACETS))
        self.assertFalse({row["retrieval"]["module_proposed"] for row in rows} - set(REVIEW_MODULES))


if __name__ == "__main__":
    unittest.main()
