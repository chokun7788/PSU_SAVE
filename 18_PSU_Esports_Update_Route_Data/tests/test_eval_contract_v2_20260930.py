from __future__ import annotations

import unittest

from tools.eval_contract_v2 import answer_outcome, contract_matches, rescore_pair, status_matches


class EvalContractV2Tests(unittest.TestCase):
    def test_ambiguous_and_not_found_are_not_available_answers(self) -> None:
        self.assertEqual(
            "clarification",
            answer_outcome("pipeline:game_target_ambiguous", "กรุณาระบุชื่อเกม", "games"),
        )
        self.assertEqual(
            "no_answer",
            answer_outcome("pipeline:game_lookup", "ไม่พบ Roblox ในรายการเกมที่ยืนยันได้", "games"),
        )
        self.assertEqual(
            "live_unavailable",
            answer_outcome("pipeline:live_booking_status_unavailable", "dashboard unavailable", "schedule"),
        )

    def test_live_lookup_needs_live_handler_not_calendar(self) -> None:
        self.assertFalse(status_matches("live_lookup_required", "answer", "pipeline:calendar_opening", "schedule"))
        self.assertTrue(status_matches("live_lookup_required", "live_unavailable", "pipeline:live_booking_status_unavailable", "schedule"))

    def test_compound_contract_requires_each_group(self) -> None:
        contract = {"must_contain_all_groups": [["PS5", "PlayStation 5"], ["บาท"], ["เกมที่ยืนยันได้", "verified games"]]}
        self.assertFalse(contract_matches("PS5 ราคา 50 บาท", contract)[0])
        self.assertTrue(contract_matches("PS5 ราคา 50 บาท; เกมที่ยืนยันได้: Fortnite", contract)[0])

    def test_rescore_retains_legacy_fields(self) -> None:
        row = {
            "id": "x", "locale": "th", "domain": "compound",
            "expected_route_categories": ["multi_question"],
            "expected_answer_status": "answer_available",
            "answer_contract": {"must_contain_any": ["PS5", "บาท", "เกม"]},
            "clean": {
                "actual_route": "multi_question", "mode": "pipeline:multi_question_splitter",
                "answer": "PS5 ราคา 50 บาท และเกมที่ยืนยันได้: Fortnite",
                "passed": True, "latency_ok": True,
            },
            "noisy": {
                "actual_route": "service_fee", "mode": "pipeline:deterministic_calculator_fast",
                "answer": "PS5 ราคา 50 บาท", "passed": False, "latency_ok": True,
            },
            "regression": True,
        }
        overlay = {"answer_contract": {"must_contain_all_groups": [["PS5"], ["บาท"], ["เกมที่ยืนยันได้"]]}}
        result = rescore_pair(row, overlay)
        self.assertTrue(result["legacy"]["regression"])
        self.assertTrue(result["v2"]["regression"])
        self.assertFalse(result["v2"]["noisy"]["content_ok"])


if __name__ == "__main__":
    unittest.main()
