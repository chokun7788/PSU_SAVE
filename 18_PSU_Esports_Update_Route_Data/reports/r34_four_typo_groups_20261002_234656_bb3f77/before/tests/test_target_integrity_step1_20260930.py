from __future__ import annotations

import unittest

from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.structured_tools import _resolve_member_role_span


class TargetIntegrityStepOneTests(unittest.TestCase):
    @staticmethod
    def answer(question: str, locale: str = "th"):
        return answer_question_pipeline_debug(
            question, locale=locale, experimental_allow_llm=False,
            experimental_rag_fallback=False, global_timeout_sec=20.0,
        )

    def test_explicit_sofa_target_survives_incidental_display_in_preamble(self):
        for question in (
            "ขอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร",
            "จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร",
            "จอสอบถาม Sofa 2 seats อยู่โซนไหน",
            "Sofa 2 seats คืออะไร",
        ):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertEqual("equipment", result.route.category)
                self.assertIn("Sofa 2 seats", result.answer)
                self.assertNotIn("TV 86 นิ้ว:", result.answer)

    def test_real_display_and_gpu_questions_still_select_the_requested_component(self):
        for question, required, forbidden in (
            ("จอ PC เป็นรุ่นอะไร", "Gaming Monitor", "Gaming PC:"),
            ("เครื่อง PC ใช้การ์ดจอรุ่นอะไร", "Gaming PC", "Gaming Monitor:"),
            ("Nintendo Switch ใช้ทีวีกี่นิ้ว", "TV 86", "Sofa 2 seats:"),
        ):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertIn(required, result.answer)
                self.assertNotIn(forbidden, result.answer)

    def test_typo_in_long_role_does_not_collapse_to_its_shorter_suffix(self):
        for question in (
            "ตำแหน่ง รองประธาน คือใคร",
            "ตำแหน่ง รอวประธาน คือใร",
            "ตำแหน่งรอวประธานคือใคร",
            "ใครเป็นรอวประธาน",
            "ตำแหน่ง รองประธาาน คือใคร",
            "ตำแหน่ง รองประาน คือใคร",
            "ตำแหน่ง รองประธนา คือใคร",
        ):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertIn("ตำแหน่ง รองประธาน", result.answer)
                self.assertIn("นายนพัทธ์ ฝอยทอง", result.answer)
                self.assertNotIn("นายษุภากรณ์", result.answer)

    def test_exact_role_and_longer_existing_role_remain_distinct(self):
        for question, required, forbidden in (
            ("ตำแหน่งประธานคือใคร", "นายษุภากรณ์", "นายนพัทธ์"),
            ("ตำแหน่ง ประธาน ึือใคร", "นายษุภากรณ์", "นายนพัทธ์"),
            ("กรรมการมีใครบ้าง", "ตำแหน่ง กรรมการ", "ตำแหน่ง ประธาน"),
            ("ตำแหน่ง รอวอธิการบดี คือใคร", "ตำแหน่ง รองอธิการบดี", "ตำแหน่ง อธิการบดี มี"),
        ):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertIn(required, result.answer)
                self.assertNotIn(forbidden, result.answer)

    def test_unsupported_modifier_requests_clarification_without_assigning_a_person(self):
        for question in (
            "ตำแหน่ง ผู้ช่วยประธาน คือใคร",
            "ตำแหน่ง อดีตประธาน คือใคร",
            "ตำแหน่ง รองประธานฝ่ายกิจการ คือใคร",
        ):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertEqual("clarification", result.route.category)
                self.assertIn("ยังยืนยันตำแหน่ง", result.answer)
                self.assertNotIn("นายษุภากรณ์", result.answer)
                self.assertNotIn("นายนพัทธ์", result.answer)

    def test_equal_distance_role_candidates_are_not_guessed(self):
        resolution = _resolve_member_role_span(
            "ตำแหน่ง รอวประธาน คือใคร",
            [{"role": "รองประธาน"}, {"role": "รอบประธาน"}],
        )
        self.assertIsNotNone(resolution)
        self.assertEqual("ambiguous", resolution.status)
        self.assertEqual("", resolution.role)

    def test_english_named_equipment_retains_its_target(self):
        result = self.answer("What is Sofa 2 seats", locale="en")
        self.assertIn("Sofa 2 seats", result.answer)
        self.assertNotIn("TV 86", result.answer)

    def test_creator_lookup_is_not_answered_as_bot_self_description(self):
        for question in ("คนทำแชทบอทคือใคร", "ใครทำแชทบอท", "ผู้พัฒนาแชทบอทคือใคร"):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertIn("นายภาสวุฒิ ชูติประชากิจ", result.answer)
                self.assertIn("AI Chat Bot Developer", result.answer)
                self.assertNotIn("ผมคือ PSU Esports Assistant", result.answer)


if __name__ == "__main__":
    unittest.main()
