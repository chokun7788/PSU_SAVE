from __future__ import annotations

import unittest

from app.pipeline.chatbot_identity import is_chatbot_greeting_query
from app.pipeline.engine import answer_question_pipeline_debug


class ThaiGreetingTypoRecoveryTests(unittest.TestCase):
    def test_short_greeting_edits_are_recognized(self) -> None:
        for question in (
            "สวัสดี",
            "สวัวสดี",
            "สวะสดี",
            "สวัดดี",
            "สวสดี",
            "สวัสสดี",
            "สวัสดีี",
            "สวัวสดีครับ",
            "สวะสดีค่ะ",
        ):
            with self.subTest(question=question):
                self.assertTrue(is_chatbot_greeting_query(question))

    def test_greeting_does_not_swallow_a_real_question(self) -> None:
        for question in (
            "สวัวสดี PS5 ราคาเท่าไหร่",
            "สวะสดี PC1 ว่างไหม 10:00",
            "สวัสดีจองยังไง",
            "PS5 ราคาเท่าไหร่",
            "PC1 ว่างไหม",
            "สวัวสดีวันนี้เปิดกี่โมง",
            "สวัสดิภาพ",
        ):
            with self.subTest(question=question):
                self.assertFalse(is_chatbot_greeting_query(question))

    def test_pipeline_returns_greeting_for_reported_typos(self) -> None:
        for question in ("สวัวสดี", "สวะสดี", "สวัดดี"):
            with self.subTest(question=question):
                result = answer_question_pipeline_debug(
                    question,
                    experimental_allow_llm=False,
                    experimental_rag_fallback=False,
                )
                self.assertEqual(result.route.intent, "chatbot_greeting")
                self.assertIn("PSU Esports Assistant", result.answer)


if __name__ == "__main__":
    unittest.main()
