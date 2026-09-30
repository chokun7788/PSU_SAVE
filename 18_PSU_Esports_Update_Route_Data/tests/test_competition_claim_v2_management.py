from __future__ import annotations

import importlib.util
import sys
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "manage_competition_claim_v2", ROOT / "tools" / "manage_competition_claim_v2.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CompetitionClaimV2ManagementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = MODULE.read_jsonl(MODULE.DEFAULT_QUEUE)

    def test_current_review_queue_passes_draft_contract(self) -> None:
        report = MODULE.validate_review_rows(self.rows)

        self.assertTrue(report.ok, report.errors[:5])
        self.assertEqual(104, report.records)
        self.assertEqual(104, report.status_counts["pending_owner_review"])

    def test_pending_rows_cannot_publish(self) -> None:
        runtime_rows, blocked = MODULE.build_runtime(self.rows, release_id="test-release")

        self.assertEqual([], runtime_rows)
        self.assertEqual(104, blocked["owner_review_pending"])

    def test_approved_thai_row_converts_without_draft_english(self) -> None:
        row = deepcopy(self.rows[0])
        row["status"] = "approved"
        row["claim"]["answer_th"] = row["source"]["clause_th"]
        row["quality"]["atomicity"] = "verified"
        row["quality"]["heading_clause_relation"] = "separated"
        row["approval"]["review_status"] = "approved"
        row["approval"]["approved_by"] = "test-reviewer"
        row["approval"]["approved_at"] = "2026-09-22T10:00:00+07:00"

        runtime = MODULE.convert_review_row(row, release_id="test-release")
        report = MODULE.validate_runtime_rows([runtime])

        self.assertTrue(report.ok, report.errors)
        self.assertEqual("missing", runtime["claim"]["english_status"])
        self.assertIsNone(runtime["claim"]["answer_en"])

    def test_hash_mismatch_is_rejected(self) -> None:
        row = deepcopy(self.rows[0])
        row["source"]["clause_th"] += " changed"

        report = MODULE.validate_review_rows([row])

        self.assertFalse(report.ok)
        self.assertTrue(any("clause_sha256" in error for error in report.errors))


if __name__ == "__main__":
    unittest.main()
