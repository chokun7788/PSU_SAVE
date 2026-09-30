from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
import json

from app.booking.live_status import (
    _snapshot_from_payload, _unavailable, get_live_booking_status, is_live_booking_question,
    render_live_booking_answer, reset_live_booking_cache, resolve_live_target_date,
)
from app.pipeline.bilingual_english import _detect_group as detect_english_group
from app.pipeline.chatbot_identity import is_chatbot_greeting_query, is_chatbot_identity_query
from app.pipeline.engine import AnswerQualityPipeline, _split_multi_question
from app.pipeline.preprocess import extract_entities, preprocess_input
from app.pipeline.protected_intents import answer_protected_intent, is_weekly_booking_window_query


class ProtectedIntentFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.pipeline = AnswerQualityPipeline()

    def answer(self, question: str, locale: str):
        return self.pipeline.answer(
            question,
            locale=locale,
            experimental_allow_llm=False,
            experimental_rag_fallback=False,
            global_timeout_sec=20,
        )

    def test_preface_does_not_split_inside_thai_word(self) -> None:
        question = "ขอถามเกี่ยวกับศูนย์หน่อยครับ: บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่"
        self.assertEqual(_split_multi_question(question), [question])
        result = self.answer(question, "th")
        self.assertEqual(result.route.category, "clarification")
        self.assertNotIn("อุปกรณ์บนหน้า Home", result.answer)
        self.assertEqual(
            self.answer("ฮัลโหลลล ตอบเฉพาะประเด็นที่ถามได้ไหม", "th").route.category,
            "knowledge",
        )
        self.assertTrue(is_chatbot_greeting_query("ฮัลโหลลล"))
        self.assertFalse(is_chatbot_greeting_query("hello what games do you have"))
        self.assertFalse(is_chatbot_greeting_query("ฮัลโหล PS5 ราคาเท่าไหร่"))

    def test_damage_is_not_a_game_catalog(self) -> None:
        cases = (
            ("If I damage a studio PS5, is there a penalty?", "en"),
            ("Who pays when a user damages a gaming chair?", "en"),
            ("Must a player pay repair costs for damaging the VR headset?", "en"),
            ("แว่น VR เสียเพราะผู้เล่นต้องจ่ายค่าซ่อมหรือเปล่า", "th"),
            ("ทำจอยเกมพังต้องรับผิดชอบยังไง", "th"),
            ("ทำเมาส์เกมมิ่งเสียหายต้องชดเชยไหม", "th"),
        )
        for question, locale in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "penalty")
                self.assertNotIn("verified game", result.answer.lower())

    def test_ps5_controller_model_is_not_a_game_button_question(self) -> None:
        hardware = self.answer("PS5 ใช้จอยแบบไหน", "th")
        self.assertEqual(hardware.route.category, "equipment")
        self.assertEqual(hardware.mode, "pipeline:protected_ps5_controller_model_unverified")
        self.assertIn("ยังไม่ระบุรุ่นจอย", hardware.answer)
        self.assertNotIn("ขอชื่อเกมก่อน", hardware.answer)

        game_buttons = self.answer("PS5 กดปุ่มอะไรในเกม TEKKEN 8", "th")
        self.assertEqual(game_buttons.route.category, "games")
        self.assertIn("TEKKEN 8 มีข้อมูลปุ่มควบคุม", game_buttons.answer)

    def test_public_access_is_not_equipment_inventory(self) -> None:
        result = self.answer("Can outsiders come in and use the equipment?", "en")
        self.assertEqual(result.route.category, "reservation")
        self.assertIn("Public visitors can book", result.answer)
        self.assertIn("national ID", result.answer)
        self.assertNotIn("Verified equipment:", result.answer)

    def test_food_bringing_and_consumption_answer_distinct_facets(self) -> None:
        result = self.answer("สามารถนำอาหารและเครื่องดื่มเข้าได้ไหม", "th")
        self.assertEqual(result.route.category, "rules")
        self.assertIn("นำอาหารหรือเครื่องดื่มเข้ามาได้", result.answer)
        self.assertIn("พื้นที่ที่ศูนย์กำหนด", result.answer)
        consuming = self.answer("รับประทานอาหารในศูนย์ได้ไหม", "th")
        self.assertEqual(consuming.route.category, "rules")
        self.assertIn("พื้นที่ที่กำหนด", consuming.answer)
        bringing = self.answer("Can I bring my own beverage onto the premises?", "en")
        self.assertEqual(bringing.route.category, "rules")
        self.assertIn("you may bring", bringing.answer)
        water_bottle = self.answer("มีข้อห้ามเรื่องนำขวดน้ำเข้าศูนย์ไหม", "th")
        self.assertEqual(water_bottle.mode, "pipeline:protected_food_bring_permission")
        self.assertIn("นำอาหารหรือเครื่องดื่มเข้ามาได้", water_bottle.answer)
        eating = self.answer("Is eating restricted to designated spaces?", "en")
        self.assertEqual(eating.route.category, "rules")
        at_desk = self.answer("Can I bring food to eat at a gaming desk?", "en")
        self.assertEqual(at_desk.route.category, "rules")
        self.assertIn("designated areas", at_desk.answer)

    def test_weekly_booking_does_not_call_live_dashboard(self) -> None:
        questions = (
            "จอง PC ได้วันอะไร ช่วงกี่โมง",
            "Which days and time periods are available for PC booking?",
        )
        for question in questions:
            self.assertTrue(is_weekly_booking_window_query(question))
            self.assertFalse(is_live_booking_question(question))
        result = self.answer(questions[1], "en")
        self.assertEqual(result.route.category, "schedule")
        self.assertIn("09:00-12:00", result.answer)
        self.assertIn("13:00-16:00", result.answer)
        self.assertNotIn("Dashboard is unavailable", result.answer)
        self.assertTrue(is_live_booking_question("Is PC #02 free tomorrow at 13:00?"))
        self.assertTrue(is_weekly_booking_window_query("Are gaming stations bookable on weekends?"))
        self.assertTrue(is_live_booking_question("Is a VR slot open this Friday at 10:00?"))

    def test_weekday_live_target_uses_requested_day(self) -> None:
        with patch("app.booking.live_status.today_bangkok", return_value=date(2026, 9, 24)):
            self.assertEqual(resolve_live_target_date("วันจันทร์ PC2 ว่างไหม"), "2026-09-28")
            self.assertEqual(resolve_live_target_date("Is PC2 free on Monday?"), "2026-09-28")
            self.assertEqual(resolve_live_target_date("วันพฤหัสบดี PS5 ว่างไหม"), "2026-10-01")
            self.assertEqual(resolve_live_target_date("Is PS5 free Thursday?"), "2026-10-01")
        with patch("app.booking.live_status.today_bangkok", return_value=date(2026, 9, 25)):
            self.assertEqual(resolve_live_target_date("ศุกร์นี้ 10:00 VR ว่างไหม"), "2026-09-25")
            self.assertEqual(resolve_live_target_date("Is a VR slot open this Friday at 10:00?"), "2026-09-25")
            self.assertEqual(resolve_live_target_date("Is a Nintendo station free Friday at 1 pm?"), "2026-10-02")

    def test_weekday_live_query_uses_matching_dashboard_date_and_station(self) -> None:
        snapshot = _snapshot_from_payload({
            "ok": True,
            "date": "2026-09-28",
            "now": "2026-09-24 10:00:00",
            "generated_at": "2026-09-24 10:00:01",
            "source": "remote_csv_live",
            "center": {"open": True, "open_periods": [["13:00", "16:00"]]},
            "resources": [
                {"resource_id": "pc-02", "resource_name": "PC #02", "capacity": 1, "status": "busy", "available_now": 0,
                 "slots": [{"start": "13:00", "end": "14:00", "status": "busy", "booked_count": 1, "available_count": 0}]},
            ],
        })
        with patch("app.booking.live_status.today_bangkok", return_value=date(2026, 9, 24)), patch(
            "app.runtime.fast_answer.get_live_booking_status", return_value=snapshot
        ) as dashboard:
            result = self.answer("วันจันทร์ PC เครื่อง 2 ว่างไหมตอนบ่ายโมง", "th")
        dashboard.assert_called_once_with("2026-09-28")
        self.assertIn("PC #02", result.answer)
        self.assertIn("2026-09-28", result.answer)
        self.assertIn("13:00", result.answer)
        self.assertNotIn("ว่างอย่างน้อย", result.answer)

    def test_all_weekday_live_questions_request_the_expected_dashboard_date(self) -> None:
        corpus = Path(__file__).resolve().parents[1] / "data/eval/intent_trap_bilingual_1000_v2.jsonl"
        cases = [json.loads(line) for line in corpus.read_text(encoding="utf-8").splitlines() if line.strip()]
        cases = [case for case in cases if case["domain"] == "weekday_live_slots"]
        self.assertEqual(len(cases), 100)

        requested_dates: list[str] = []

        def dashboard(selected_date: str):
            requested_dates.append(selected_date)
            return _snapshot_from_payload({
                "ok": True, "date": selected_date, "now": "2026-09-24 10:00:00",
                "generated_at": "2026-09-24 10:00:01", "source": "remote_csv_live",
                "center": {"open": True, "open_periods": [["09:00", "12:00"], ["13:00", "16:00"]]},
                "resources": [
                    {"resource_id": key, "resource_name": label, "capacity": 1, "status": "free", "available_now": 1,
                     "slots": [{"start": start, "end": end, "status": "free", "booked_count": 0, "available_count": 1}
                               for start, end in (("09:00", "10:00"), ("10:00", "11:00"), ("13:00", "14:00"), ("14:00", "15:00"), ("15:00", "16:00"))]}
                    for key, label in (
                        ("pc-01", "PC #01"), ("pc-02", "PC #02"),
                        ("ps5-1", "PlayStation 5 #1"), ("ps5-2", "PlayStation 5 #2"),
                        ("cockpit-1", "Cockpit #1"), ("vr-am", "VR Station (Morning)"),
                        ("vr-pm", "VR Station (Afternoon)"),
                        ("switch-am", "Nintendo Switch (Morning)"), ("switch-pm", "Nintendo Switch (Afternoon)"),
                    )
                ],
            })

        with patch("app.booking.live_status.today_bangkok", return_value=date(2026, 9, 24)), patch(
            "app.runtime.fast_answer.get_live_booking_status", side_effect=dashboard
        ):
            for case in cases:
                with self.subTest(case=case["id"]):
                    requested_dates.clear()
                    result = self.answer(case["question"], case["locale"])
                    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
                    self.assertIn(case["expected_target"], result.answer)

    def test_dashboard_wrong_date_is_not_treated_as_live_evidence(self) -> None:
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self, _limit):
                return json.dumps({
                    "ok": True, "date": "2026-09-24", "source": "remote_csv_live",
                    "center": {"open": True}, "resources": [],
                }).encode("utf-8")

        reset_live_booking_cache()
        with patch("app.booking.live_status.urlopen", return_value=Response()), patch(
            "app.booking.live_status.live_booking_enabled", return_value=True
        ):
            snapshot = get_live_booking_status("2026-09-28")
        self.assertFalse(snapshot.ok)
        self.assertIn("returned date", snapshot.error)

    def test_unnumbered_nintendo_services_do_not_imply_station_two(self) -> None:
        snapshot = _snapshot_from_payload({
            "ok": True, "date": "2026-10-01", "now": "2026-09-24 10:00:00",
            "generated_at": "2026-09-24 10:00:01", "source": "remote_csv_live",
            "center": {"open": True, "open_periods": [["13:00", "16:00"]]},
            "resources": [
                {"resource_id": "switch-am", "resource_name": "Nintendo Switch (Morning)", "capacity": 1, "status": "free", "available_now": 1},
                {"resource_id": "switch-pm", "resource_name": "Nintendo Switch (Afternoon)", "capacity": 1, "status": "free", "available_now": 1},
            ],
        })
        answer = render_live_booking_answer("Is Nintendo station 2 free Thursday at 15:00?", snapshot, "en")
        self.assertIn("could not find", answer)
        self.assertNotIn("2/2 resources", answer)

    def test_negated_student_is_not_student_tariff(self) -> None:
        self.assertIsNone(extract_entities(preprocess_input("ถ้าไม่ใช่นักศึกษาใช้อุปกรณ์ราคาเท่าไหร่")).user_group)
        self.assertEqual(extract_entities(preprocess_input("บุคคลภายนอกไม่ใช่นักศึกษาใช้ PC ราคาเท่าไหร่")).user_group, "adult")
        self.assertIsNone(detect_english_group("I am not a student, what does PC cost?"))

    def test_chatbot_identity_paraphrases_do_not_match_staff_questions(self) -> None:
        for question in (
            "who is this bot", "is this a bot or a person", "who is answering me",
            "what bot is this", "wat assistant is this", "tell me who u are",
            "what is this chat assistant called", "นายนี่คือใคร", "บอทนีคือใคร", "นี่คนหรือบอท",
        ):
            with self.subTest(question=question):
                self.assertTrue(is_chatbot_identity_query(question))
        for question in ("who is the studio manager", "who is the chatbot developer", "ใครเป็นผู้จัดการศูนย์"):
            with self.subTest(question=question):
                self.assertFalse(is_chatbot_identity_query(question))
        for question in (
            "What equipment is in the Nintendo Switch Zone? Could you check this for me",
            "What do you need to book to play The Last of Us Part I",
            "Could you please help me with this: What is the studio policy for severe damage",
        ):
            with self.subTest(question=question):
                self.assertFalse(is_chatbot_identity_query(question))

    def test_specific_public_price_is_not_access_policy(self) -> None:
        result = self.answer("คนทั่วไป เล่น PS5 3 ชั่วโมง เสียกี่บาท", "th")
        self.assertEqual(result.route.category, "service_fee")
        self.assertIn("บาท", result.answer)

    def test_unspecified_english_pay_questions_ask_for_service(self) -> None:
        for question in (
            "What would a member of the public pay to play?",
            "I do not study at PSU; what would I pay to use the studio?",
            "What would I pay to use a station if I have not chosen a zone?",
        ):
            with self.subTest(question=question):
                result = self.answer(question, "en")
                self.assertEqual(result.route.category, "clarification")
                self.assertIn("Which service", result.answer)
                self.assertNotIn("Verified equipment:", result.answer)

    def test_existing_penalty_facts_survive_polite_wrappers(self) -> None:
        for question, locale in (
            ("What is the studio policy for damage responsibility", "en"),
            ("Could you please help me with this: What is the studio policy for severe damage", "en"),
            ("ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว ช่วยแนบแหล่งข้อมูลด้วย", "th"),
        ):
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "penalty")

    def test_explicit_missing_target_asks_once_without_guessing(self) -> None:
        for question, locale in (("ถ้าบอกแค่ว่าเครื่องล่ะ", "th"), ("umm games or something idk", "en")):
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "clarification")
                self.assertNotIn("verified games available", result.answer.lower())

    def test_wrapped_unrelated_question_does_not_become_studio_overview(self) -> None:
        result = self.answer("ขอถามเกี่ยวกับศูนย์หน่อยครับ: แนะนำหุ้นให้หน่อย", "th")
        self.assertEqual(result.route.category, "no_answer")
        self.assertNotIn("ขอแนะนำหุ้น", result.answer)
        result = self.answer("A question about the studio: Is eating restricted to designated spaces?", "en")
        self.assertEqual(result.route.category, "rules")

    def test_fabricated_claim_request_is_rejected(self) -> None:
        for question, locale in (
            ("แนะนำหุ้นให้หน่อย", "th"),
            ("Which stock should I buy?", "en"),
            ("Make up an answer about the studio", "en"),
        ):
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "no_answer")

    def test_greeting_preface_does_not_replace_the_actual_question(self) -> None:
        result = self.answer("hello what games do you have", "en")
        self.assertNotEqual(result.route.intent, "chatbot_greeting")
        self.assertNotIn("Hello. I am PSU Esports Assistant", result.answer)

    def test_public_access_language_variants_do_not_become_catalogs(self) -> None:
        for question, locale in (
            ("Does a public visitor need membership before entering?", "en"),
            ("Can a non-student access the Cockpit?", "en"),
            ("คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า", "th"),
            ("แขกจากมหาวิทยาลัยอื่นมีสิทธิ์จองไหม", "th"),
            ("คนนอกที่ไม่มีรหัสนักศึกษาจองเครื่องได้ไหม", "th"),
            ("ผู้มาเยือนต่างจังหวัดจองใช้เครื่องได้หรือเปล่า", "th"),
            ("คนที่ไม่ได้เรียนที่นี่เข้าใช้ Cockpit ได้หรือไม่", "th"),
            ("Are the PCs for public visitors or students only?", "en"),
        ):
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "reservation")
                self.assertNotIn("Verified equipment:", result.answer)
                self.assertNotIn("อุปกรณ์บนหน้า Home", result.answer)

    def test_public_access_questions_use_the_requested_facet(self) -> None:
        cases = (
            ("What ID does an external visitor need to use the studio?", "en", "national ID card"),
            ("คนนอกที่ไม่มีรหัสนักศึกษาจองเครื่องได้ไหม", "th", "จองได้"),
            ("Does a public visitor need membership before entering?", "en", "do not need to be a PSU student"),
            ("แขกจากมหาวิทยาลัยอื่นมีสิทธิ์จองไหม", "th", "จองได้"),
        )
        for question, locale, expected in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "reservation")
                self.assertIn(expected, result.answer)
                self.assertIn("https://esports.computing.psu.ac.th/", result.answer)

    def test_specific_policy_facets_beat_generic_public_access(self) -> None:
        cases = (
            ("คนนอกใช้ PC ฟรีไหม", "th", "service_fee", "บาท"),
            ("Does a non-PSU guest need a membership or national ID?", "en", "reservation", "National ID"),
            ("คนนอกจอง PS5 ต้องใช้บัตรอะไร", "th", "reservation", "ใช้บัตรประชาชน"),
            ("คนต่างมหาวิทยาลัยต้องอายุเท่าไรถึงเข้าใช้ได้", "th", "no_answer", "อายุขั้นต่ำ"),
            ("Can a visitor plug in their own laptop?", "en", "rules", "permission"),
            ("นำเบียร์เข้ามาดื่มได้ไหม", "th", "rules", "ห้าม"),
            ("ใครเข้าใช้ศูนย์ได้บ้าง", "th", "reservation", "บุคคลทั่วไป"),
            ("Can anyone use the studio equipment?", "en", "reservation", "Public visitors"),
            ("Are nonstudents allowed to use the studio or only PSU students?", "en", "reservation", "Public visitors"),
            ("Can a non-PSU user charge their phone in the studio?", "en", "rules", "power outlets"),
        )
        for question, locale, category, expected in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, category)
                self.assertIn(expected, result.answer)
                self.assertNotIn("Verified equipment:", result.answer)

    def test_access_permission_does_not_imply_offsite_or_every_game_permission(self) -> None:
        cases = (
            ("Can a visitor take a PS5 home after booking?", "en", "taking equipment home"),
            ("ไม่ใช่นักศึกษา แต่อยากยืม PS5 กลับบ้านได้ไหม", "th", "ไม่ได้ยืนยันสิทธิ์ยืม"),
            ("Can any visitor play every game listed?", "en", "does not establish access to every game"),
            ("คนนอกเข้าไปเล่นได้ทุกเกมเลยไหม", "th", "ยังยืนยันไม่ได้ว่าเล่นได้ทุกเกม"),
            ("Can visitors enter just to look around for free?", "en", "does not confirm"),
            ("คนนอกเข้าไปดูเฉยๆต้องเสียเงินไหม", "th", "ดูเฉย ๆ"),
        )
        for question, locale, expected in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "no_answer")
                self.assertIn(expected, result.answer)
                self.assertNotIn("Verified equipment:", result.answer)

    def test_rule_answer_distinguishes_carrying_from_drinking(self) -> None:
        carrying = self.answer("Can I bring wine but not drink it?", "en")
        self.assertEqual(carrying.route.category, "rules")
        self.assertIn("does not separately confirm whether carrying alcohol", carrying.answer)
        self.assertIn("alcohol consumption", carrying.answer)
        drinking = self.answer("นำเบียร์เข้ามาดื่มได้ไหม", "th")
        self.assertIn("ห้าม", drinking.answer)
        at_desk = self.answer("Can I drink water at a gaming desk?", "en")
        self.assertIn("cannot confirm that this gaming station", at_desk.answer)

    def test_payment_checkin_damage_and_duration_use_verified_facts(self) -> None:
        cases = (
            ("How do I pay for my booking?", "en", "reservation", "Siam Commercial Bank"),
            ("ขอข้อมูลเรื่องชำระเงินหลัง booking ขอรายละเอียดแบบสั้น ๆ", "th", "reservation", "10 นาที"),
            ("ไปถึงแล้วต้องเช็กอินไหม", "th", "reservation", "ต้องเช็กอินครับ"),
            ("What happens if I damage equipment?", "en", "penalty", "100-500 THB"),
            ("เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง", "th", "service_fee", "บาท"),
        )
        for question, locale, category, expected in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, category)
                self.assertIn(expected, result.answer)
                self.assertNotIn("ความรู้ทั่วไปของโมเดล", result.answer)

    def test_studio_rules_do_not_become_game_catalog_or_clarification(self) -> None:
        cases = (
            ("What is the studio policy for return equipment games", "en", "returned after use"),
            ("ขอข้อมูลเรื่องทรัพย์สินส่วนตัว สูญหาย", "th", "ไม่รับผิดชอบ"),
            ("ขอข้อมูลเรื่องคำพูดไม่เหมาะสม", "th", "ห้ามพูดจาดูหมิ่น"),
            ("What is the studio policy for food noise damage", "en", "100-500 THB"),
            ("ของหายแล้วทำอุปกรณ์เสียหายด้วย ต้องทำยังไง", "th", "ทรัพย์สินส่วนตัวสูญหาย"),
        )
        for question, locale, expected in cases:
            with self.subTest(question=question):
                result = self.answer(question, locale)
                self.assertEqual(result.route.category, "rules")
                self.assertIn(expected, result.answer)
                self.assertNotIn("verified games", result.answer.lower())

    def test_booking_price_is_not_live_availability(self) -> None:
        self.assertFalse(is_live_booking_question("คนทั่วไปจอง PC ต้องจ่ายเท่าไหร่"))
        self.assertFalse(is_live_booking_question("Is a PC free of charge for visitors?"))
        self.assertFalse(is_live_booking_question("Can a visitor use VR for free?"))
        self.assertTrue(is_live_booking_question("PC2 จองได้ไหมพรุ่งนี้ 13:00"))
        self.assertTrue(is_live_booking_question("คนภายนอกใช้ PC ตอนนี้ได้ไหม"))
        result = self.answer("คนทั่วไปจอง PC ต้องจ่ายเท่าไหร่", "th")
        self.assertEqual(result.route.category, "service_fee")
        self.assertIn("บาท", result.answer)

    def test_walk_in_question_answers_booking_requirement_first(self) -> None:
        result = self.answer("Can visitors use VR without booking?", "en")
        self.assertEqual(result.route.category, "reservation")
        self.assertTrue(result.answer.startswith("No, you cannot use the studio without booking first."))
        self.assertIn("one hour", result.answer)

    def test_live_unavailable_keeps_requested_date_without_claiming_availability(self) -> None:
        snapshot = _unavailable("2026-09-28", "test dashboard outage")
        answer = render_live_booking_answer("Is PC2 free Monday at 13:00?", snapshot, "en")
        self.assertIn("2026-09-28", answer)
        self.assertIn("cannot confirm", answer)
        self.assertNotIn("PC2 is available", answer)
        protected = answer_protected_intent("คนภายนอกใช้ PC ตอนนี้ได้ไหม", locale="th", service="pc", rules=[])
        self.assertIsNone(protected)

    def test_time_specific_access_does_not_skip_schedule(self) -> None:
        self.assertIsNone(answer_protected_intent(
            "Can tourists play Nintendo tomorrow at 13:00?", locale="en", service="nintendo", rules=[]
        ))
        result = self.answer("Can tourists play Nintendo tomorrow at 13:00?", "en")
        self.assertEqual(result.route.category, "schedule")
        self.assertNotIn("Public visitors can book", result.answer)


if __name__ == "__main__":
    unittest.main()
