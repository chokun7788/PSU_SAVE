from __future__ import annotations

import unittest

from app.core.normalization import normalize_text
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input
from app.pipeline.social_dialogue import social_dialogue_reply
from app.pipeline.target_lock import resolve_game_entity


def _run(question: str):
    return answer_question_pipeline_debug(
        question,
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
    )


class ThaiNoisyInputFlowTests(unittest.TestCase):
    def test_social_reply_does_not_consume_a_following_task(self) -> None:
        self.assertEqual(social_dialogue_reply("ขอบคุนคับบบ")[0], "social_thanks")
        self.assertIsNone(social_dialogue_reply("ขอบคุนคับบบ PS5 ราคาเท่าไหร่"))
        self.assertNotEqual(_run("ขอบคุนคับบบ PS5 ราคาเท่าไหร่").route.intent, "social_thanks")

    def test_racing_catalog_and_tournament_question_stay_separate(self) -> None:
        catalog = _run("มีเกมแข่งรดไหม")
        self.assertEqual(catalog.route.category, "games")
        self.assertIn("Gran Turismo 7", catalog.answer)
        rules = _run("เกมแข่งรถมีกติกาการแข่งขันอย่างไร")
        self.assertEqual(rules.route.category, "competition_rules")

    def test_colloquial_price_uses_verified_fee_answer(self) -> None:
        result = _run("เพลย์ห้าคิดตังเท่าไหรอะ")
        self.assertEqual(result.route.intent, "service_fee_query")
        self.assertIn("60 นาที", result.answer)

    def test_recovery_keeps_booking_slot_literals(self) -> None:
        normalized = normalize_text("วันนี้ 10:00 PC1 ว่างมั้ยย")
        self.assertIn("10:00", normalized)
        self.assertIn("pc1", normalized)
        self.assertEqual(_run("วันนี้ 10:00 PC1 ว่างมั้ยย").route.intent, "live_booking_status")

    def test_number_in_verified_game_title_is_not_a_catalog_count(self) -> None:
        known = _run("มี Counter-Strike 2 ไหม")
        self.assertEqual(known.route.category, "games")
        self.assertIn("Counter-Strike 2 เล่นได้ที่", known.answer)
        unknown = _run("Hades II มีให้เล่นไหม")
        self.assertNotIn("Hades II เล่นได้ที่", unknown.answer)

    def test_round_duration_comes_from_verified_service_rows(self) -> None:
        for question, expected in (
            ("PC Zone รอบละกี่นาที", "60 นาที"),
            ("VR Zone รอบละกี่นาที", "30 และ 60 นาที"),
        ):
            with self.subTest(question=question):
                result = _run(question)
                self.assertEqual(result.route.category, "reservation")
                self.assertIn(expected, result.answer)

    def test_explicit_remastered_title_is_not_part_one(self) -> None:
        question = "มี The Last of Us Part II (Remastered) ไหม"
        resolved = resolve_game_entity(question, operation="availability")
        self.assertEqual(resolved.status, "exact")
        self.assertEqual(resolved.top_candidate.title, "The Last of Us Part II (Remastered)")
        answer = _run(question)
        self.assertIn("PlayStation 5", answer.answer)

    def test_demonstrative_game_needs_a_target_without_context(self) -> None:
        missing = _run("เกมนี้เล่นที่ไหน")
        self.assertEqual(missing.route.category, "clarification")
        self.assertIn("เกมไหน", missing.answer)
        named = _run("เกมนี้ Counter-Strike 2 เล่นที่ไหน")
        self.assertEqual(named.route.category, "games")

    def test_nintendo_service_capacity_survives_game_title_correction(self) -> None:
        for label, capacity in (("1-2", "1-2 คน"), ("1-4", "1-4 คน")):
            question = f"Nintendo Switch ({label} Persons) เล่นได้กี่คน"
            with self.subTest(label=label):
                self.assertEqual(preprocess_input(question).clean_query, question)
                result = _run(question)
                self.assertIn(capacity, result.answer)
        sports = _run("Nintendo Switch Sports เล่นที่ไหน")
        self.assertEqual(sports.route.category, "games")

    def test_zone_catalog_and_genre_are_not_single_game_requests(self) -> None:
        for question in (
            "PC Zone มีเกมอะไรให้เล่น",
            "Cockpit Zone มีเกมอะไรให้เล่นบ้าง",
            "มีเกม shooting บน PC ไหม",
        ):
            with self.subTest(question=question):
                result = _run(question)
                self.assertEqual(result.route.category, "games")
                self.assertNotIn("กรุณาระบุชื่อเกม", result.answer)
                self.assertIn("เกม", result.answer)
                if "shooting" in question:
                    self.assertIn("เกมแนว", result.answer)
                    self.assertNotIn("TEKKEN 8", result.answer)


if __name__ == "__main__":
    unittest.main()
