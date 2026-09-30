from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from app.pipeline.engine import answer_question_pipeline_debug


class VerifiedAnswerPathTests(unittest.TestCase):
    def answer(self, question: str, locale: str = "th"):
        with patch.dict(os.environ, {"PSU_LIVE_BOOKING_ENABLED": "0", "PSU_CANONICAL_KNOWLEDGE": "0"}):
            return answer_question_pipeline_debug(
                question,
                locale=locale,
                experimental_allow_llm=False,
                global_timeout_sec=9,
            )

    def test_contact_email_with_thai_spelling(self) -> None:
        result = self.answer("ขออีเมลติดต่อศูนย์")
        self.assertEqual(result.route.category, "contact")
        self.assertIn("psuesportspkt@gmail.com", result.answer)

    def test_booking_email_does_not_turn_into_studio_contact(self) -> None:
        result = self.answer("จองแล้วต้องตรวจสอบอีเมลไหม")
        self.assertNotEqual(result.route.category, "contact")
        self.assertNotIn("psuesportspkt@gmail.com", result.answer)

    def test_undated_holiday_opening_request_asks_for_date(self) -> None:
        result = self.answer("วันหยุดราชการเปิดไหม")
        self.assertIn("วันที่เท่าไร", result.answer)
        self.assertNotIn("วันหยุดไทย/เทศกาลถัดไป", result.answer)

    def test_same_day_policy_is_not_live_station_status(self) -> None:
        for question, locale, expected in (
            ("วันนี้จองได้ไหม", "th", "ล่วงหน้า 1 ชั่วโมง"),
            ("Can I book today?", "en", "one-hour advance rule"),
        ):
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "reservation")
                self.assertIn(expected, result.answer)
                self.assertNotIn("ว่างอยู่ตอนนี้", result.answer)

    def test_station_slot_question_remains_live_lookup(self) -> None:
        result = self.answer("วันนี้ตอน10โมง PC1 ว่างไหม")
        self.assertEqual(result.route.intent, "live_booking_status")
        self.assertIn("ยังยืนยัน", result.answer)

    def test_named_headset_definition_is_item_detail(self) -> None:
        result = self.answer("Gaming Headset คืออุปกรณ์อะไร")
        self.assertEqual(result.route.category, "equipment")
        self.assertIn("หูฟังเกมมิ่งสำหรับฟังเสียงเกม", result.answer)
        self.assertNotIn("อุปกรณ์บนหน้า Home:", result.answer)

    def test_verified_tekken_price_question_is_service_fee(self) -> None:
        result = self.answer("ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 ราคาเท่าไหร่")
        self.assertEqual(result.route.category, "service_fee")
        self.assertIn("TEKKEN 8 ไม่มีราคาแยกตามชื่อเกม", result.answer)
        self.assertNotIn("กติกา", result.answer)

    def test_competition_rule_with_price_word_remains_competition(self) -> None:
        result = self.answer("Tekken 8 แข่งค่าสมัครราคาเท่าไหร่")
        self.assertEqual(result.route.category, "competition_rules")

    def test_zone_equipment_request_remains_catalog(self) -> None:
        result = self.answer("PC Zone มีอุปกรณ์อะไรบ้าง")
        self.assertEqual(result.route.category, "equipment")
        self.assertIn("Gaming Headset", result.answer)


if __name__ == "__main__":
    unittest.main()
