from __future__ import annotations

import unittest

from app.core.multi_error_phrase_recovery import detect_multi_error_phrase_recovery
from app.core.typo_similarity import osa_distance
from app.pipeline.chatbot_identity import is_chatbot_identity_query, is_multi_error_chatbot_identity_query
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input
from app.pipeline.social_dialogue import social_dialogue_reply


def _answer(question: str):
    return answer_question_pipeline_debug(
        question,
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
    )


class MultiErrorTypoRecoveryTests(unittest.TestCase):
    def test_adjacent_transposition_counts_as_one_edit(self) -> None:
        self.assertEqual(osa_distance("ดไ้", "ได้"), 1)
        self.assertEqual(osa_distance("เปิกี่โมว", "เปิดกี่โมง"), 2)

    def test_multiple_errors_in_two_clause_identity_question(self) -> None:
        for question in (
            "นานเปนไคแเสทำอะไรไดเทั่ง",
            "นยเปนใคแล้วทำอาไรไดบ้าง",
            "คุนเปนไคแระช่วยอารายไดบ้าง",
            "บอทนีเปนไคแระทำอาไรไดบ้าง",
            "นายเปนคัยแล้วทำไรไดบ้าง",
            "นานเปนไคแเสทำอะไรไดเทั่งครับ",
        ):
            with self.subTest(question=question):
                self.assertTrue(is_multi_error_chatbot_identity_query(question))
                self.assertEqual(_answer(question).route.intent, "chatbot_identity")

    def test_short_social_and_identity_recovery(self) -> None:
        self.assertEqual(_answer("สวัวาดี").route.intent, "chatbot_greeting")
        self.assertEqual(_answer("ตุณคือใครรร").route.intent, "chatbot_identity")
        self.assertEqual(social_dialogue_reply("ขอโทดดดับ")[0], "social_apology")
        self.assertEqual(social_dialogue_reply("ขอบุนคับ")[0], "social_thanks")

    def test_phrase_recovery_keeps_resource_and_duration(self) -> None:
        cases = (
            ("PS5 ราาคาเท่าไหน่", "PS5 ราคาเท่าไหร่", "service_fee_query"),
            ("VR 30 นาที คิดตัวเท่าไหรอ่า", "VR 30 นาที คิดตังเท่าไหรอะ", "service_fee_query"),
            ("วันเสาร์เปดกี่โมว", "วันเสาร์เปิดกี่โมง", "schedule_query"),
            ("มีเมออะไรบ้าง", "มีเกมอะไรบ้าง", "list"),
            ("มีหูฟไหม", "มีหูฟังไหม", "list"),
            ("ติดต่าทาไงหน", "ติดต่อทางไหน", "detail"),
        )
        for question, corrected, intent in cases:
            with self.subTest(question=question):
                self.assertEqual(preprocess_input(question).clean_query, corrected)
                self.assertEqual(preprocess_input(question).raw_query, question)
                self.assertEqual(_answer(question).route.intent, intent)

    def test_valid_questions_and_other_targets_are_not_redirected(self) -> None:
        for question in (
            "ปิดกี่โมง",
            "เปิดกี่โมง",
            "มีเมนูอะไรบ้าง",
            "PS5 ราคาเท่าไหร่",
            "วันนี้ 10:00 PC1 ว่างไหม",
        ):
            with self.subTest(question=question):
                self.assertIsNone(detect_multi_error_phrase_recovery(question))
        for question in (
            "ผู้จัดการเป็นใครแล้วทำอะไรได้บ้าง",
            "นายชนะชัยทำอะไรได้บ้าง",
            "PC1 เป็นอะไรแล้วทำอะไรได้บ้าง",
            "กติกา CS2 เรื่องคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน ว่าอย่างไร",
            "ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ",
        ):
            with self.subTest(question=question):
                self.assertFalse(is_chatbot_identity_query(question))
                self.assertNotEqual(_answer(question).route.intent, "chatbot_identity")
        self.assertIsNone(social_dialogue_reply("ขอโทษครับ PC1 ราคาเท่าไหร่"))


if __name__ == "__main__":
    unittest.main()
