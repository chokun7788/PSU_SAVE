from __future__ import annotations

import unittest
from collections import Counter
from datetime import date

from tools.build_intent_trap_ground_truth_1000 import build


class IntentTrapGroundTruthTests(unittest.TestCase):
    def test_counts_uniqueness_and_contracts(self) -> None:
        rows = build(date(2026, 9, 24))
        self.assertEqual(len(rows), 1000)
        self.assertEqual(len({row["id"] for row in rows}), 1000)
        self.assertEqual(len({row["question"].casefold() for row in rows}), 1000)
        self.assertEqual(Counter(row["locale"] for row in rows), {"th": 500, "en": 500})
        for locale in ("th", "en"):
            groups = Counter(row["domain"] for row in rows if row["locale"] == locale)
            self.assertEqual(len(groups), 10)
            self.assertTrue(all(count == 50 for count in groups.values()))
            self.assertEqual(len({row["metadata"]["scenario_id"] for row in rows if row["locale"] == locale}), 100)
        self.assertTrue(all(row["review_status"].endswith("pending_review") for row in rows))

    def test_weekday_target_does_not_fall_back_to_today(self) -> None:
        rows = build(date(2026, 9, 24))
        monday = next(row for row in rows if row["id"] == "INTENT-TRAP-TH-0301")
        self.assertEqual(monday["expected_target"], "2026-09-28")
        self.assertIn("2026-09-28", monday["answer_contract"]["must_contain"])


if __name__ == "__main__":
    unittest.main()
