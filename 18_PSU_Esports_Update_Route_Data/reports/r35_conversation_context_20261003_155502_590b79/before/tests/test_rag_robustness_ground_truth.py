from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "build_rag_robustness_ground_truth.py"
DATA_PATH = ROOT / "data" / "eval" / "rag_robustness_ground_truth_v1.jsonl"


def load_builder_module():
    spec = importlib.util.spec_from_file_location("rag_robustness_builder", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RagRobustnessGroundTruthTests(unittest.TestCase):
    def test_generated_matrix_is_valid_and_bilingual(self) -> None:
        builder = load_builder_module()
        rows = builder.build_rows()
        self.assertEqual([], builder.validate(rows))
        self.assertEqual(600, len(rows))
        self.assertEqual(300, sum(row["locale"] == "th" for row in rows))
        self.assertEqual(300, sum(row["locale"] == "en" for row in rows))

    def test_checked_in_jsonl_matches_the_builder(self) -> None:
        builder = load_builder_module()
        stored = [json.loads(line) for line in DATA_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(builder.build_rows(), stored)

    def test_short_and_noisy_variants_remain_distinct_after_normalization(self) -> None:
        builder = load_builder_module()
        rows = builder.build_rows()
        for locale in ("th", "en"):
            keys = [builder._question_key(row["question"]) for row in rows if row["locale"] == locale]
            self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
