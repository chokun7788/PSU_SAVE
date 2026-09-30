"""Ensure active Canonical releases cannot race legacy fact cards."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from app.pipeline.retrieval import retrieve_competition_fact_cards


class CanonicalCompetitionFactGuardTests(unittest.TestCase):
    def test_active_rulebook_skips_legacy_short_fact_cards(self) -> None:
        cards = (
            {
                "id": "cs2_map_pool",
                "game": "Counter-Strike 2",
                "intent": "map_pool",
                "answer": "Legacy short answer",
                "evidence": "Legacy evidence",
                "source_ids": ["competition_rules_cs2_psu_phuket_2026"],
                "question_patterns": ["CS2 ใช้ map อะไร"],
                "tags": ["cs2", "map_pool"],
            },
            {
                "id": "rov_format",
                "game": "Arena of Valor (RoV)",
                "intent": "format",
                "answer": "RoV answer",
                "evidence": "RoV evidence",
                "source_ids": ["competition_rules_rov_blueket_2025_men"],
                "question_patterns": ["RoV แข่งแบบไหน"],
                "tags": ["rov", "format"],
            },
        )
        with (
            patch("app.pipeline.retrieval.load_competition_fact_cards", return_value=cards),
            patch(
                "app.pipeline.retrieval.active_canonical_competition_release_ids",
                return_value=frozenset({"competition_rules_cs2_psu_phuket_2026"}),
            ),
        ):
            hits, trace = retrieve_competition_fact_cards("CS2 ใช้ map อะไร")

        self.assertEqual([], hits)
        self.assertEqual(1, trace.metadata["skipped_for_active_canonical"])
        self.assertEqual(["competition_rules_cs2_psu_phuket_2026"], trace.metadata["active_release_ids"])


if __name__ == "__main__":
    unittest.main()
