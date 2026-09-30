from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "build_master_ground_truth_10000.py"
TH_PATH = ROOT / "data" / "eval" / "master_ground_truth_th_5000_v2.jsonl"
EN_PATH = ROOT / "data" / "eval" / "master_ground_truth_en_5000_v2.jsonl"


def load_builder():
    spec = importlib.util.spec_from_file_location("master_gt_builder", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MasterGroundTruthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.builder = load_builder()
        cls.rows = cls.builder.build()

    def test_exact_bilingual_counts_and_distribution(self) -> None:
        self.assertEqual([], self.builder.validate(self.rows))
        self.assertEqual(10000, len(self.rows))
        for locale in ("th", "en"):
            locale_rows = [row for row in self.rows if row["locale"] == locale]
            self.assertEqual(5000, len(locale_rows))
            self.assertEqual(Counter(self.builder.DOMAIN_TARGETS), Counter(row["domain"] for row in locale_rows))

    def test_static_live_and_safe_outcomes_are_distinct(self) -> None:
        statuses = {row["expected_answer_status"] for row in self.rows}
        self.assertIn("answer_available", statuses)
        self.assertIn("live_lookup_required", statuses)
        self.assertTrue({"clarification_required", "safe_clarification"} & statuses)
        self.assertTrue({"no_answer_expected", "safe_no_answer"} & statuses)
        for row in self.rows:
            live = row["source_contract"]["live_dependency"]
            self.assertEqual(live, row["expected_answer_status"] == "live_lookup_required")

    def test_schedule_rules_are_not_mislabeled_as_booking_policy(self) -> None:
        schedule_intents = {"service_schedule", "schedule_not_24_hours", "schedule_friday_maintenance_general"}
        rows = [
            row for row in self.rows
            if row.get("origin") == "rule_patterns" and row.get("expected_intent") in schedule_intents
        ]
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual("schedule_calendar", row["domain"])
            self.assertIn("schedule", row["expected_route_categories"])

    def test_every_core_source_record_is_represented(self) -> None:
        origins = Counter((row["locale"], row["origin"]) for row in self.rows if row["question_style"] == "source_form")
        for locale in ("th", "en"):
            self.assertGreaterEqual(origins[(locale, "game_item_details")], 108)
            self.assertGreaterEqual(origins[(locale, "equipment_item_details")], 48)
            self.assertGreaterEqual(origins[(locale, "competition_rules_rag_ground_truth_v1")], 274)
            covered_control_ids = {
                source_id
                for row in self.rows
                if row["locale"] == locale
                for source_id in row["source_contract"]["source_ids"]
                if source_id.startswith("game_control_")
            }
            self.assertGreaterEqual(len(covered_control_ids), 491)
            covered_member_ids = {
                source_id
                for row in self.rows
                if row["locale"] == locale
                for source_id in row["source_contract"]["source_ids"]
                if source_id.startswith("member-")
            }
            self.assertEqual(25, len(covered_member_ids))

    def test_checked_in_locale_files_match_builder(self) -> None:
        expected = {locale: [row for row in self.rows if row["locale"] == locale] for locale in ("th", "en")}
        for locale, path in (("th", TH_PATH), ("en", EN_PATH)):
            stored = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertEqual(expected[locale], stored)


if __name__ == "__main__":
    unittest.main()
