"""Regression checks for the canonical competition-rule migration."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "competition_rule_canonical", ROOT / "tools" / "build_competition_rule_canonical.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CompetitionRuleCanonicalTests(unittest.TestCase):
    def test_current_migration_is_complete_and_valid(self) -> None:
        model = MODULE.build()

        self.assertEqual([], MODULE.validate(model))
        self.assertEqual([], MODULE.check_existing(model))
        self.assertEqual(model["source_counts"]["chunks"], len(model["records"]))
        self.assertEqual(model["source_counts"]["facts"], len(model["facts_projection"]))
        self.assertEqual(len(model["records"]), len(model["rag_projections"]))
        self.assertEqual(4, len(model["releases"]))
        self.assertFalse(any(release["runtime_eligible"] for release in model["releases"]))
        self.assertFalse(
            [row for row in model["records"] if row["canonical_section"] == "other_or_unclassified"]
        )
        self.assertFalse(
            [row for row in model["facts_projection"] if row["canonical_section"] == "other_or_unclassified"]
        )
        self.assertTrue(all("เกม:" in row["text_th"] and "รายการแข่งขัน:" in row["text_th"] for row in model["rag_projections"]))
        self.assertEqual(
            sum(row["evidence_status"] != "verified_direct" for row in model["facts_projection"]),
            len(model["fact_evidence_review_queue"]),
        )


if __name__ == "__main__":
    unittest.main()
