from __future__ import annotations

import unittest

from app.booking.live_status import is_live_booking_question
from app.core.keyboard_neighbor_recovery import (
    adjacent_key_substitution,
    detect_keyboard_neighbor_recovery,
    recover_keyboard_neighbor_query,
)
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input


def _answer(question: str):
    return answer_question_pipeline_debug(
        question,
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
    )


class KeyboardNeighborRecoveryTests(unittest.TestCase):
    def test_substitution_uses_physical_neighbors_and_character_type(self) -> None:
        for observed, intended in (("า", "ส"), ("แ", "อ"), ("ส", "ว"), ("ด", "ก")):
            with self.subTest(observed=observed, intended=intended):
                self.assertTrue(adjacent_key_substitution(observed, intended))
        for observed, intended in (("า", "อ"), ("า", "ี"), ("ส", "ส")):
            with self.subTest(observed=observed, intended=intended):
                self.assertFalse(adjacent_key_substitution(observed, intended))

    def test_correction_requires_both_neighbor_and_intent_context(self) -> None:
        cases = {
            "สวัาดี": "สวัสดี",
            "จแงยังไง": "จองยังไง",
            "PC1 ส่างไหม": "PC1 ว่างไหม",
            "มีเดมอะไรบ้าง": "มีเกมอะไรบ้าง",
            "วันนี้ 10:00 PC1 ส่างไหม": "วันนี้ 10:00 PC1 ว่างไหม",
        }
        for original, expected in cases.items():
            with self.subTest(original=original):
                recovery = detect_keyboard_neighbor_recovery(original)
                self.assertIsNotNone(recovery)
                self.assertEqual(recovery.candidate, expected)
                self.assertEqual(preprocess_input(original).clean_query, expected)
                self.assertEqual(preprocess_input(original).raw_query, original)

    def test_preserves_ambiguous_or_other_intents(self) -> None:
        unchanged = (
            "PS5 นาคา",
            "สวัาดี PC1 ว่างไหม",
            "มีเดมเกมอะไรบ้าง",
            "ขอเดมเกม",
            "Beat Saber ใช้จอยยังไง",
            "สวัสดี",
            "จองยังไง",
            "PC1 ว่างไหม",
            "มีเกมอะไรบ้าง",
            "Nintendo Switch Sports เล่นที่ไหน",
        )
        for question in unchanged:
            with self.subTest(question=question):
                self.assertIsNone(detect_keyboard_neighbor_recovery(question))
                self.assertEqual(recover_keyboard_neighbor_query(question), question)

    def test_failing_examples_reach_the_expected_answer_paths(self) -> None:
        booking = _answer("จแงยังไง")
        self.assertEqual(booking.route.intent, "booking_policy")
        self.assertIn("ขั้นตอนจอง", booking.answer)
        games = _answer("มีเดมอะไรบ้าง")
        self.assertEqual(games.route.category, "games")
        self.assertIn("42 เกม", games.answer)
        self.assertEqual(_answer("สวัาดี").route.intent, "chatbot_greeting")
        self.assertTrue(is_live_booking_question(preprocess_input("PC1 ส่างไหม").clean_query))


if __name__ == "__main__":
    unittest.main()
