from __future__ import annotations

import unittest
from copy import deepcopy
from datetime import datetime, timezone

from app.pipeline.competition_claim_contract import (
    numeric_tokens,
    validate_completeness,
    select_eligible_claims,
    validate_sentence_attributions,
)


def runtime_claim(*, claim_id: str = "rule::cs2-team-size", game_id: str = "cs2", facet: str = "team_size") -> dict:
    source_hash = "a" * 64
    return {
        "schema_version": "competition_rule_claim_v2_1",
        "claim_id": claim_id,
        "release_id": "release-1",
        "status": "approved",
        "answerable": True,
        "source": {"clause_th": "ทีมละ 5 คน", "clause_sha256": source_hash},
        "claim": {"answer_th": "ทีมละ 5 คน", "answer_en": "Five players per team.", "english_status": "approved"},
        "retrieval": {"game_id": game_id, "facet": facet},
        "evidence": {"source_refs": ["source-1"], "source_span_sha256": source_hash},
        "lifecycle": {"effective_from": None, "effective_to": None, "conflicts_with": []},
        "quality": {"atomicity": "verified", "heading_clause_relation": "separated"},
    }


class CompetitionClaimContractTests(unittest.TestCase):
    def test_exact_target_and_facet_are_accepted(self) -> None:
        row = runtime_claim()

        result = select_eligible_claims(
            [row], release_id="release-1", game_id="cs2", facet="team_size", locale="en"
        )

        self.assertEqual((row,), result.accepted)
        self.assertEqual((), result.rejected)

    def test_cross_game_claim_is_rejected_before_ranking(self) -> None:
        result = select_eligible_claims(
            [runtime_claim(game_id="valorant")],
            release_id="release-1",
            game_id="cs2",
            facet="team_size",
            locale="th",
        )

        self.assertEqual((), result.accepted)
        self.assertIn("cross_game", result.rejected[0].codes)

    def test_missing_english_localization_is_rejected(self) -> None:
        row = runtime_claim()
        row["claim"]["english_status"] = "missing"
        row["claim"]["answer_en"] = None

        result = select_eligible_claims(
            [row], release_id="release-1", game_id="cs2", facet="team_size", locale="en"
        )

        self.assertIn("missing_localization", result.rejected[0].codes)

    def test_expired_and_conflicting_claim_is_rejected(self) -> None:
        row = runtime_claim()
        row["lifecycle"]["effective_to"] = "2026-01-01T00:00:00+00:00"
        row["lifecycle"]["conflicts_with"] = ["rule::other"]

        result = select_eligible_claims(
            [row],
            release_id="release-1",
            game_id="cs2",
            facet="team_size",
            locale="th",
            effective_at=datetime(2026, 9, 22, tzinfo=timezone.utc),
        )

        self.assertIn("expired", result.rejected[0].codes)
        self.assertIn("unresolved_conflict", result.rejected[0].codes)

    def test_sentence_attribution_rejects_unknown_claim(self) -> None:
        payload = {
            "sentences": [
                {"text": "ทีมละ 5 คน", "claim_ids": ["rule::other"], "factual_values": {"team_size": 5}}
            ],
            "used_claim_ids": ["rule::other"],
        }

        result = validate_sentence_attributions(payload, allowed_claim_ids=["rule::cs2-team-size"])

        self.assertFalse(result.ok)
        self.assertTrue(any("claim_not_allowed" in error for error in result.errors))

    def test_sentence_attribution_accepts_selected_claim(self) -> None:
        payload = {
            "sentences": [
                {
                    "text": "ทีมละ 5 คน",
                    "claim_ids": ["rule::cs2-team-size"],
                    "factual_values": {"team_size": 5},
                }
            ],
            "used_claim_ids": ["rule::cs2-team-size"],
        }

        result = validate_sentence_attributions(payload, allowed_claim_ids=["rule::cs2-team-size"])

        self.assertTrue(result.ok, result.errors)

    def test_complete_list_requires_verified_structured_rows(self) -> None:
        row = runtime_claim()
        row["quality"]["completeness"] = "direct"

        result = validate_completeness("ขอบทลงโทษทั้งหมด", [row])

        self.assertFalse(result.ok)
        self.assertTrue(result.required)

    def test_numeric_tokens_support_bilingual_parity_check(self) -> None:
        self.assertEqual(("5", "30"), numeric_tokens("ทีมละ 5 คน ภายใน 30 นาที"))


if __name__ == "__main__":
    unittest.main()
