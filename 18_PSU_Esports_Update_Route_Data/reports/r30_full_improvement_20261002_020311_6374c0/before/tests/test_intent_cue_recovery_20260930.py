from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from app.booking.live_status import _unavailable
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.engine import _split_multi_question, answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input


def answer(question: str, locale: str = "auto"):
    return answer_question_pipeline_debug(
        question, locale=locale,
        experimental_allow_llm=False, experimental_rag_fallback=False,
        global_timeout_sec=20.0,
    )


class IntentCueRecoveryTests(unittest.TestCase):
    def test_recovery_keeps_raw_and_protected_values(self) -> None:
        cases = (
            ("PUBG: BATTLEGROUNDS ราคเท่าไฟร่", "PUBG: BATTLEGROUNDS ราคาเท่าไหร่"),
            ("ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่าบง้าง",
             "ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่างบ้าง"),
            ("PS5 ราคาเท่าไหร่ แล้วมีเกมะไรบ้าง",
             "PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง"),
            ("What does the Tab buttno do in VALORANT on PC",
             "What does the Tab button do in VALORANT on PC"),
            ("What is the studio policy for teporary suspension",
             "What is the studio policy for temporary suspension"),
            ("Is Cockpit Zone availble at 14:00-15:00?",
             "Is Cockpit Zone available at 14:00-15:00?"),
            ("ตอนนี้ Nintendo Switch ว่งไหม", "ตอนนี้ Nintendo Switch ว่างไหม"),
        )
        for raw, corrected in cases:
            with self.subTest(raw=raw):
                pre = preprocess_input(raw)
                self.assertEqual(raw, pre.raw_query)
                self.assertEqual(corrected, pre.clean_query)

    def test_control_cues_use_contextual_edit_distance(self) -> None:
        cases = (
            ("What does the R3 vutton do in Gran Turismo 7 on PS5",
             "What does the R3 button do in Gran Turismo 7 on PS5"),
            ("What are the cobtrols for Moving Out 2 on Nintendo Switch",
             "What are the controls for Moving Out 2 on Nintendo Switch"),
            ("ในเกม TEKKEN 8 บน PS5 ปุม R1 ใช้ทำอะไร",
             "ในเกม TEKKEN 8 บน PS5 ปุ่ม R1 ใช้ทำอะไร"),
            ("ในเกม Animal Crossing บน Nintendo Switch ุ่ม D-Pad ใช้มำอะไร",
             "ในเกม Animal Crossing บน Nintendo Switch ปุ่ม D-Pad ใช้มำอะไร"),
        )
        for raw, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(expected, recover_intent_cues(raw))

    def test_compound_split_recovers_second_operation(self) -> None:
        self.assertEqual(
            ["PS5 ราคาเท่าไหร่", "PS5 มีเกมอะไรบ้าง"],
            _split_multi_question("PS5 ราคาเท่าไหร่ แล้วมีเกมะไรบ้าง"),
        )

    def test_routes_match_requested_operations(self) -> None:
        self.assertEqual("service_fee", answer("PUBG: BATTLEGROUNDS ราคเท่าไฟร่", "th").route.category)
        compound = answer("PS5 ราคาเท่าไหร่ แล้วมีเกมะไรบ้าง", "th")
        self.assertEqual("multi_question", compound.route.category)
        self.assertIn("เกมที่ยืนยันได้", compound.answer)
        controls = answer("What does the Tab buttno do in VALORANT on PC", "en")
        self.assertIn("Tab: Show Scoreboard", controls.answer)
        self.assertEqual("penalty", answer("What is the studio policy for teporary suspension", "en").route.category)
        with patch("app.runtime.fast_answer.get_live_booking_status", side_effect=lambda date: _unavailable(date, "test")):
            live = answer("ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่าบง้าง", "th")
        self.assertEqual("schedule", live.route.category)
        self.assertIn("ยังยืนยันสถานะ", live.answer)

    def test_real_word_collision_asks_instead_of_rewriting(self) -> None:
        self.assertEqual("How do you pay Moving Out 2", recover_intent_cues("How do you pay Moving Out 2"))
        result = answer("How do you pay Moving Out 2", "en")
        self.assertEqual("clarification", result.route.category)
        self.assertIn("how to play", result.answer)
        self.assertIn("service fee", result.answer)

    def test_recovery_can_be_disabled_for_rollback(self) -> None:
        raw = "What does the Tab buttno do in VALORANT on PC"
        with patch.dict(os.environ, {"PSU_INTENT_CUE_RECOVERY": "0"}):
            self.assertEqual(raw, recover_intent_cues(raw))
            self.assertEqual(raw, preprocess_input(raw).clean_query)

    def test_negative_controls(self) -> None:
        for question in (
            "PS5 ราคาเท่าไร", "มีเมนูอะไรบ้าง", "ใช้จอยยังไง",
            "How do you pay for a booking?", "PC11 ว่างไหม 10:00",
            "What games are available in Cockpit Zone?",
            "What does the bottom shelf hold?", "Are studio controls available?",
            "What does the Tab button do in VALORANT?",
            "What are all the buttons in Hogwarts Legacy?",
            "What does the Analogue control scheme button do in Horizon Call of the Mountain?",
            "ในเกมนี้กลุ่มผู้เล่นมีอะไรบ้าง",
        ):
            with self.subTest(question=question):
                self.assertEqual(question, recover_intent_cues(question))


if __name__ == "__main__":
    unittest.main()
