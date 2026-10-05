from __future__ import annotations

import unittest

from app.knowledge.competition_claim_store import retrieve_runtime_claims
from tests.test_competition_claim_contract import runtime_claim


class CompetitionClaimStoreTests(unittest.TestCase):
    def test_prefilter_prevents_cross_game_semantic_score_from_winning(self) -> None:
        cs2 = runtime_claim(claim_id="rule::cs2-team-size", game_id="cs2", facet="team_size")
        valorant = runtime_claim(claim_id="rule::valorant-team-size", game_id="valorant", facet="team_size")

        result = retrieve_runtime_claims(
            "CS2 team size",
            [cs2, valorant],
            release_id="release-1",
            game_id="cs2",
            facet="team_size",
            locale="en",
            semantic_scores={"rule::cs2-team-size": 0.1, "rule::valorant-team-size": 1.0},
        )

        self.assertEqual(["rule::cs2-team-size"], [item.claim["claim_id"] for item in result.ranked])
        self.assertIn("cross_game", result.selection.rejected[0].codes)

    def test_wrong_facet_is_removed_before_ranking(self) -> None:
        team = runtime_claim(claim_id="rule::team", facet="team_size")
        pause = runtime_claim(claim_id="rule::pause", facet="pause_timeout")

        result = retrieve_runtime_claims(
            "CS2 team size",
            [team, pause],
            release_id="release-1",
            game_id="cs2",
            facet="team_size",
            locale="th",
            semantic_scores={"rule::pause": 1.0},
        )

        self.assertEqual(["rule::team"], [item.claim["claim_id"] for item in result.ranked])
        self.assertIn("wrong_facet", result.selection.rejected[0].codes)

    def test_result_is_bounded_to_eight_claims(self) -> None:
        rows = [runtime_claim(claim_id=f"rule::row-{index}") for index in range(12)]

        result = retrieve_runtime_claims(
            "CS2 team size",
            rows,
            release_id="release-1",
            game_id="cs2",
            facet="team_size",
            locale="th",
            limit=100,
        )

        self.assertEqual(8, len(result.ranked))


if __name__ == "__main__":
    unittest.main()
