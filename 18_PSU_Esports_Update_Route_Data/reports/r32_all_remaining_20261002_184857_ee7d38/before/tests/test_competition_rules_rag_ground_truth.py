from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "build_competition_rules_rag_ground_truth.py"
OUTPUT = ROOT / "data" / "eval" / "competition_rules_rag_ground_truth_v1.jsonl"


def load_builder():
    spec = importlib.util.spec_from_file_location("competition_rules_rag_builder", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CompetitionRulesRagGroundTruthTests(unittest.TestCase):
    def test_corpus_is_valid_and_bilingual(self) -> None:
        builder = load_builder()
        rows = builder.build_rows()
        self.assertEqual([], builder.validate(rows))
        self.assertGreaterEqual(len(rows), 500)
        self.assertGreaterEqual(sum(row["locale"] == "th" for row in rows), 250)
        self.assertGreaterEqual(sum(row["locale"] == "en" for row in rows), 250)

    def test_positive_cases_lock_rulebook_and_evidence(self) -> None:
        builder = load_builder()
        for row in builder.build_rows():
            if row["case_type"] == "facet_targeted_retrieval":
                self.assertTrue(row["target_locked"])
                self.assertTrue(row["expected_rulebook_ids"])
                if row["expected_answer_status"] == "answer_available":
                    self.assertTrue(row["rag_required"])
                    self.assertTrue(row["allowed_evidence_rule_ids"])
                else:
                    self.assertFalse(row["rag_required"])
                    self.assertFalse(row["allowed_evidence_rule_ids"])

    def test_checked_in_corpus_matches_builder(self) -> None:
        builder = load_builder()
        stored = [json.loads(line) for line in OUTPUT.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(builder.build_rows(), stored)

    def test_human_written_source_gaps_are_safe_negative_gold(self) -> None:
        builder = load_builder()
        rows = [row for row in builder.build_rows() if row["case_type"] == "source_gap_safe_no_answer"]
        self.assertEqual(20, len(rows))
        self.assertEqual(10, sum(row["locale"] == "th" for row in rows))
        self.assertEqual(10, sum(row["locale"] == "en" for row in rows))
        for row in rows:
            self.assertEqual("no_answer_expected", row["expected_answer_status"])
            self.assertFalse(row["rag_required"])
            self.assertTrue(row["target_locked"])
            self.assertTrue(row["expected_rulebook_ids"])
            self.assertFalse(row["allowed_evidence_rule_ids"])
            self.assertFalse(row["allowed_evidence_fact_ids"])
            self.assertTrue(row["source_gap_manifest_key"])
            self.assertTrue(row["source_gap_reason"])


if __name__ == "__main__":
    unittest.main()
