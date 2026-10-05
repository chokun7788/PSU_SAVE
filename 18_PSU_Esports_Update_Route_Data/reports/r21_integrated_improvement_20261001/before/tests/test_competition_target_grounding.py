from __future__ import annotations

import unittest

from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.competition_coverage import assess_competition_evidence
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.question_frame import build_question_frame
from app.pipeline.retrieval import _competition_row_intents, retrieve_curated
from app.pipeline.schemas import PipelineRoute
from app.pipeline.execution_context import request_execution_context


class CompetitionTargetGroundingTests(unittest.TestCase):
    def test_competition_resolution_is_computed_once_per_request(self) -> None:
        with request_execution_context() as context:
            first = resolve_competition_targets("กติกา RoV เรื่อง disconnect")
            second = resolve_competition_targets("กติกา RoV เรื่อง disconnect")

        self.assertIs(first, second)
        self.assertEqual(1, context.counters["competition_resolution_computed"])
        self.assertEqual(1, context.counters["competition_resolution_reused"])

    def test_safe_thai_tekken_variant_resolves_without_rewriting_query(self) -> None:
        question = "กติกา เทคเล่น 8 เรื่องการตั้งค่าในเกม"

        resolved = resolve_competition_targets(question)

        self.assertEqual("exact", resolved.status)
        self.assertEqual(["tekken8"], [target.game_id for target in resolved.targets])
        self.assertIn("เทคเล่น 8", question)

    def test_source_facet_does_not_inherit_an_unrelated_import_tag(self) -> None:
        row = {
            "title": "Counter-Strike 2: เวลาการแข่งขัน",
            "text": "สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์",
            # This models a legacy import error found in the current corpus.
            "tags": ["competition_rules", "penalty_matrix"],
        }

        intents = _competition_row_intents(row)

        self.assertIn("schedule", intents)
        self.assertNotIn("penalty_matrix", intents)

    def test_thai_rov_disconnect_locks_the_rov_rulebook(self) -> None:
        question = "ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง"
        frame = build_question_frame(
            question,
            PipelineRoute("competition_rules", "competition_rules_lookup", 0.99, "competition_rule", "medium", "test"),
        )

        self.assertEqual(frame.domain, "competition_rules")
        self.assertEqual(frame.metadata["competition_game_ids"], ["rov"])
        self.assertEqual(frame.metadata["competition_rulebook_ids"], ["competition_rules_rov_blueket_2025_men"])

    def test_explicit_unknown_competition_game_is_not_mapped_to_a_known_game(self) -> None:
        resolved = resolve_competition_targets("กติกา Free Fire เรื่อง pause คืออะไร")

        self.assertEqual(resolved.status, "unknown_explicit")
        self.assertEqual(resolved.targets, ())

    def test_conduct_query_ranks_conduct_sections_first(self) -> None:
        hits, _ = retrieve_curated(
            "What do the CS2 tournament rules say about player conduct and sportsmanship?",
            "competition_rules",
            exclude_canonical_projection=True,
        )

        hit_ids = [hit["id"] for hit in hits]
        self.assertIn("competition_rules_cs2_psu_phuket_2026_s36_c01", hit_ids)
        self.assertIn("competition_rules_cs2_psu_phuket_2026_s35_c01", hit_ids)

    def test_team_composition_ranks_the_team_size_section_first(self) -> None:
        hits, _ = retrieve_curated(
            "What do the CS2 tournament rules say about team size and roster composition?",
            "competition_rules",
            exclude_canonical_projection=True,
        )

        self.assertEqual(hits[0]["id"], "competition_rules_cs2_psu_phuket_2026_s18_c01")

    def test_named_game_plus_rule_facet_enters_competition_rag(self) -> None:
        question = "Counter-Strike 2 มีข้อกำหนดเรื่องจำนวนผู้เล่นและองค์ประกอบทีม ไหม"
        frame = build_question_frame(
            question,
            PipelineRoute("games", "game_detail", 0.90, "game_detail", "low", "test"),
        )

        self.assertEqual(frame.domain, "competition_rules")
        self.assertEqual(frame.metadata["competition_game_ids"], ["cs2"])

    def test_multi_game_query_retains_both_explicit_targets(self) -> None:
        resolved = resolve_competition_targets("CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง")

        self.assertEqual(resolved.status, "multiple")
        self.assertEqual([target.game_id for target in resolved.targets], ["cs2", "valorant"])

    def test_untargeted_rule_question_clarifies_instead_of_defaulting_to_cs2(self) -> None:
        result = answer_question_pipeline_debug(
            "กติกา timeout เป็นยังไง",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
        )

        self.assertEqual(result.route.category, "competition_rules")
        self.assertEqual(result.mode, "pipeline:competition_target_clarification")
        self.assertEqual(result.hits, [])

    def test_generic_settings_query_renders_settings_not_timeout(self) -> None:
        result = answer_question_pipeline_debug(
            "ห้องแข่ง CS2 ต้องใช้การกำหนดค่าอะไร",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_source_rag")
        self.assertIn("Competitive (5v5)", result.answer)
        self.assertIn("Freeze time: 15 วินาที", result.answer)
        self.assertNotIn("การขอเวลานอก", result.answer)

    def test_missing_target_facet_does_not_substitute_another_rule(self) -> None:
        result = answer_question_pipeline_debug(
            "ผู้เล่น VALORANT มีข้อควรระวังเรื่องการวางตัวอะไร",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
        self.assertEqual(result.hits, [])
        self.assertIn("จะไม่ใช้หัวข้ออื่นมาตอบแทน", result.answer)

    def test_known_source_gap_has_a_machine_readable_reason(self) -> None:
        hits, _ = retrieve_curated(
            "ผู้เล่น VALORANT มีข้อควรระวังเรื่องการวางตัวอะไร",
            "competition_rules",
            exclude_canonical_projection=True,
        )

        coverage = assess_competition_evidence("ผู้เล่น VALORANT มีข้อควรระวังเรื่องการวางตัวอะไร", hits)

        self.assertFalse(coverage.covered)
        self.assertEqual(coverage.facet, "conduct")
        self.assertTrue(coverage.reason.startswith("known_source_gap:"), coverage.reason)

    def test_in_match_contact_requires_a_contact_instruction(self) -> None:
        result = answer_question_pipeline_debug(
            "ถ้าเกิดเรื่องระหว่างแข่ง VALORANT ต้องแจ้งใคร",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
        self.assertNotIn("FPS", result.answer)

    def test_roster_question_requires_starter_and_substitute_evidence(self) -> None:
        result = answer_question_pipeline_debug(
            "จำนวนตัวจริงและตัวสำรองของ VALORANT กำหนดไว้อย่างไร",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
        self.assertNotIn("Player Emergency Pause", result.answer)

    def test_checkin_question_does_not_use_an_unrelated_note_rule(self) -> None:
        result = answer_question_pipeline_debug(
            "วันแข่ง CS2 ต้องไปรายงานตัวอย่างไร",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
        self.assertNotIn("นำโน้ตหรือเอกสาร", result.answer)

    def test_checkin_renderer_does_not_append_adjacent_match_prep_rules(self) -> None:
        result = answer_question_pipeline_debug(
            "VALORANT กำหนดเวลา check-in ยังไง",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_source_rag")
        self.assertIn("30 นาที", result.answer)
        self.assertNotIn("นำโน้ตหรือเอกสาร", result.answer)
        self.assertNotIn("ผู้เล่นต้อง ปิด", result.answer)

    def test_generic_in_match_process_does_not_use_a_graph_setting(self) -> None:
        result = answer_question_pipeline_debug(
            "ขั้นตอนทำงานระหว่างการแข่งขัน VALORANT เป็นแบบไหน",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="th",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
        self.assertNotIn("FPS", result.answer)

    def test_english_untargeted_rule_question_requests_a_game(self) -> None:
        result = answer_question_pipeline_debug(
            "Please tell me the timeout rules.",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_target_clarification_en")
        self.assertIn("Which game's competition rules", result.answer)

    def test_english_protest_question_without_target_requests_a_game(self) -> None:
        result = answer_question_pipeline_debug(
            "Can you show me the protest rules?",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_target_clarification_en")

    def test_english_missing_valorant_conduct_does_not_become_translation_pending(self) -> None:
        result = answer_question_pipeline_debug(
            "What fair-play rules apply to VALORANT?",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
        self.assertNotIn("approved English wording is not available", result.answer)

    def test_english_starting_player_question_does_not_use_match_prep_capacity(self) -> None:
        result = answer_question_pipeline_debug(
            "How many starting players must a VALORANT team field?",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
        self.assertEqual([], result.hits)
        self.assertNotIn("No more than 6 players", result.answer)

    def test_english_general_match_issue_does_not_use_bug_or_post_match_text(self) -> None:
        result = answer_question_pipeline_debug(
            "Who should a player contact for a general issue during a VALORANT match?",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
        self.assertEqual([], result.hits)
        self.assertNotIn("Play-Through Bug", result.answer)

    def test_english_comparison_keeps_both_targets_before_localization_check(self) -> None:
        result = answer_question_pipeline_debug(
            "How do CS2 and VALORANT technical pause rules differ?",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_source_localization_pending_en")
        self.assertIn("Counter-Strike 2 and VALORANT", result.answer)
        self.assertTrue(any("valorant" in str(hit).casefold() for hit in result.hits))

    def test_unsupported_english_rulebook_skips_live_booking(self) -> None:
        result = answer_question_pipeline_debug(
            "Please check whether this knowledge base has Free Fire competition rules.",
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=5,
            locale="en",
        )

        self.assertEqual(result.mode, "pipeline:competition_unknown_target_no_answer")
        self.assertNotEqual(result.route.intent, "live_booking_status")


if __name__ == "__main__":
    unittest.main()
