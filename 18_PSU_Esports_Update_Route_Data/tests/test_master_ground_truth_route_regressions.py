from __future__ import annotations

import os
import unittest
from datetime import date

os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"
os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW"] = "0"

from app.pipeline.competition_targets import looks_like_competition_rule_query
from app.pipeline.bilingual_english import _english_holiday_context
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.query_signals import looks_like_clear_general_request
from tools.run_master_ground_truth_eval import actual_status


class MasterGroundTruthRouteRegressionTests(unittest.TestCase):
    @staticmethod
    def answer(question: str):
        return answer_question_pipeline_debug(
            question,
            experimental_allow_llm=False,
            experimental_rag_fallback=False,
            locale="en",
            global_timeout_sec=10.0,
        )

    def test_booking_policy_words_do_not_imply_competition_rules(self) -> None:
        for question in (
            "What is the studio policy for late check in?",
            "What is the studio policy for payment timeout?",
            "What is the studio policy for account number?",
        ):
            with self.subTest(question=question):
                self.assertFalse(looks_like_competition_rule_query(question))

    def test_explicit_competition_context_still_routes_to_rulebook(self) -> None:
        self.assertTrue(looks_like_competition_rule_query("What is the CS2 tournament timeout rule?"))
        self.assertTrue(looks_like_competition_rule_query("Which competition rules cover check-in?"))

    def test_route_category_controls_safe_outcome_status(self) -> None:
        answer = "No information about this service was found in the available knowledge base."
        self.assertEqual("no_answer", actual_status("pipeline:rule_en", answer, "no_answer"))
        self.assertEqual("clarification", actual_status("pipeline:rule_en", "Please specify a game.", "clarification"))
        self.assertEqual(
            "no_answer",
            actual_status(
                "pipeline:games_unknown_target_en",
                "I could not find Hades II in the verified PSU game records.",
                "games",
            ),
        )
        self.assertEqual(
            "no_answer",
            actual_status(
                "pipeline:live_booking_status_unavailable",
                "I cannot confirm the live booking status because the dashboard is unavailable.",
                "schedule",
            ),
        )

    def test_booking_facets_are_not_flattened_to_generic_steps(self) -> None:
        cases = (
            ("What is the studio policy for late check in?", "reservation", "no refund"),
            ("How do I pay for my booking?", "reservation", "795-276244-1"),
            ("How many sessions can one booking include?", "reservation", "3 sessions"),
            ("What information do I need to book?", "reservation", "phone number"),
        )
        for question, category, expected_text in cases:
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertEqual(category, result.route.category)
                self.assertIn(expected_text.casefold(), result.answer.casefold())

    def test_static_game_catalog_and_duration_do_not_use_live_booking(self) -> None:
        catalog = self.answer("Which game is available in the Cockpit Zone?")
        self.assertEqual("games", catalog.route.category)
        self.assertIn("Gran Turismo 7", catalog.answer)

        duration = self.answer("How long is one PC Zone booking slot?")
        self.assertEqual("reservation", duration.route.category)
        self.assertIn("60 minutes", duration.answer)

    def test_explicit_negative_rule_beats_broad_member_or_equipment_signal(self) -> None:
        membership = self.answer("What is the studio policy for annual membership?")
        self.assertEqual("no_answer", membership.route.category)
        self.assertIn("annual membership", membership.answer.casefold())

        keyboard = self.answer("What is the studio policy for selling keyboard?")
        self.assertEqual("no_answer", keyboard.route.category)
        self.assertIn("selling gaming keyboards", keyboard.answer.casefold())

    def test_english_booking_wrappers_do_not_block_verified_intent(self) -> None:
        booking = self.answer("Could you check this using verified information: How do I book a machine")
        self.assertEqual("reservation", booking.route.category)
        self.assertIn("booking steps", booking.answer.casefold())

        checkin = self.answer("Do I need to check in when I arrive")
        self.assertEqual("reservation", checkin.route.category)
        self.assertIn("30 minutes", checkin.answer.casefold())

    def test_ambiguous_english_references_request_clarification(self) -> None:
        for question in ("How much does it cost", "Where can I play it", "Can I book this"):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertEqual("clarification", result.route.category)

    def test_game_location_and_capacity_use_static_records(self) -> None:
        location = self.answer("Which machine can you play Resident Evil 4 on")
        self.assertEqual("games", location.route.category)
        self.assertIn("available on", location.answer.casefold())

        capacity = self.answer("How many players can join PC #03 to #10")
        self.assertEqual("reservation", capacity.route.category)
        self.assertIn("1 person", capacity.answer.casefold())

    def test_unknown_game_variants_do_not_expand_to_catalog(self) -> None:
        for question in ("Is there Minecraft", "Can Roblox be played", "Is Valorant Mobile available"):
            with self.subTest(question=question):
                result = self.answer(question)
                self.assertIn(result.route.category, {"games", "no_answer"})
                self.assertIn("could not find", result.answer.casefold())

    def test_game_family_result_is_narrow_and_ranking_uses_catalog(self) -> None:
        family = self.answer("Is there a game with overcook")
        self.assertEqual("games", family.route.category)
        self.assertIn("Overcooked! 2", family.answer)
        self.assertNotIn("Mario Kart", family.answer)

        ranking = self.answer("Which equipment has the most games")
        self.assertEqual("games", ranking.route.category)
        self.assertIn("17 titles each", ranking.answer)
        self.assertNotIn("The Last of Us", ranking.answer)

    def test_compound_keeps_verified_target_and_booking_step(self) -> None:
        controls = self.answer("How do you play Gran Turismo 7 and what button is the gas pedal")
        self.assertEqual("multi_question", controls.route.category)
        self.assertIn("R2: Accelerate", controls.answer)

        booking = self.answer("How is VR for 30 minutes different from VR for 1 hour, and how do I book it")
        self.assertEqual("multi_question", booking.route.category)
        self.assertIn("Booking steps:", booking.answer)

    def test_general_comparison_is_not_equipment_inventory(self) -> None:
        self.assertTrue(looks_like_clear_general_request("How do frame rate and resolution differ?"))
        self.assertFalse(looks_like_clear_general_request("What is the frame rate of the PSU studio PC?"))

    def test_official_thai_member_identifiers_in_english_questions(self) -> None:
        by_name = self.answer("What is ผศ.ดร.นิวัติ แก้วประดับ's role")
        self.assertEqual("overview", by_name.route.category)
        self.assertIn("อธิการบดี", by_name.answer)
        self.assertNotIn("รองอธิการบดี", by_name.answer)

        by_role = self.answer("Who holds the role of รองอธิการบดี")
        self.assertEqual("overview", by_role.route.category)
        self.assertIn("รศ.ดร.พันธ์ ทองชุมนุม", by_role.answer)
        self.assertNotIn("ผศ.ดร.นิวัติ แก้วประดับ", by_role.answer)

    def test_equipment_facets_do_not_expand_to_game_or_inventory_list(self) -> None:
        gpu = self.answer("What GPU model is inside the PCs")
        self.assertEqual("equipment", gpu.route.category)
        self.assertIn("does not verify the GPU model", gpu.answer)
        self.assertNotIn("Gaming Monitor", gpu.answer)

        controller = self.answer("What controller is used for PS5")
        self.assertEqual("equipment", controller.route.category)
        self.assertIn("does not specify the PS5 controller model", controller.answer)
        self.assertNotIn("verified games", controller.answer.casefold())

        headsets = self.answer("Do you provide headsets")
        self.assertEqual("equipment", headsets.route.category)
        self.assertIn("Gaming Headset", headsets.answer)

    def test_missing_english_game_detail_names_target(self) -> None:
        result = self.answer("How do you play Animal Crossing: New Horizons")
        self.assertEqual("games", result.route.category)
        self.assertIn("Animal Crossing: New Horizons", result.answer)
        self.assertIn("approved English localization", result.answer)

        zone = self.answer("Which studio zone has Animal Crossing: New Horizons")
        self.assertEqual("games", zone.route.category)
        self.assertIn("Nintendo Switch Zone", zone.answer)

    def test_pc_game_question_uses_machine_catalog_not_game_translation(self) -> None:
        absent = self.answer("Does PC #01 have Call of Duty: Warzone")
        self.assertEqual("games", absent.route.category)
        self.assertIn("not listed for PC #01", absent.answer)
        self.assertIn("last verified", absent.answer.casefold())

        present = self.answer("Does PC #03 have Call of Duty: Warzone")
        self.assertEqual("games", present.route.category)
        self.assertIn("listed for PC #03", present.answer)
        self.assertNotIn("not listed", present.answer)

        different_game = self.answer("Does PC #10 have TEKKEN 8")
        self.assertIn("not listed for PC #10", different_game.answer)

    def test_english_calendar_keeps_schedule_when_holiday_name_is_thai(self) -> None:
        holiday = _english_holiday_context(date(2026, 9, 24))
        self.assertIn("calendar", holiday)
        self.assertNotIn("วันมหิดล", holiday)

        tomorrow = self.answer("Will the studio be open tomorrow")
        self.assertEqual("schedule", tomorrow.route.category)
        self.assertIn("System reference date", tomorrow.answer)

        closures = self.answer("Are there any special closures this week")
        self.assertEqual("schedule", closures.route.category)
        self.assertIn("local service calendar", closures.answer.casefold())

        undated_holiday = self.answer("Is the studio open on public holidays")
        self.assertEqual("clarification", undated_holiday.route.category)
        self.assertIn("Which public holiday or date", undated_holiday.answer)

        weather = self.answer("Will it rain tomorrow")
        self.assertEqual("no_answer", weather.route.category)
        self.assertNotIn("open for play", weather.answer)

    def test_unverified_thai_studio_claim_is_a_no_answer_outcome(self) -> None:
        result = answer_question_pipeline_debug(
            "อัดวิดีโอในศูนย์ได้ไหม",
            experimental_allow_llm=True,
            experimental_rag_fallback=True,
            locale="th",
            global_timeout_sec=20.0,
        )
        self.assertEqual("no_answer", result.route.category)
        self.assertIn("ยังไม่พบข้อมูลที่ยืนยันได้", result.answer)

    def test_verified_equipment_availability_does_not_enter_game_retrieval(self) -> None:
        result = answer_question_pipeline_debug(
            "ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกมมิ่งให้ไหม",
            experimental_allow_llm=True,
            experimental_rag_fallback=True,
            locale="th",
            global_timeout_sec=20.0,
        )
        self.assertEqual("equipment", result.route.category)
        self.assertIn("Gaming Mouse", result.answer)
        self.assertEqual("pipeline:equipment_availability_fast_path", result.mode)
        self.assertLess(result.elapsed, 5.0)

        broken = answer_question_pipeline_debug(
            "เมาส์พังต้องจ่ายค่าปรับไหม",
            experimental_allow_llm=False,
            experimental_rag_fallback=False,
            locale="th",
            global_timeout_sec=10.0,
        )
        self.assertNotEqual("pipeline:equipment_availability_fast_path", broken.mode)


if __name__ == "__main__":
    unittest.main()
