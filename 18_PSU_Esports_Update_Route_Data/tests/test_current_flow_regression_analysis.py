import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("regression_analysis_tested", ROOT / "tools/analyze_current_flow_regression.py")
analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analysis)


class AnalysisTests(unittest.TestCase):
    def test_confusion_counts_false_positives_separately(self):
        rows = [{"guard": {"flags": flags}, "case": {"truth": truth}}
                for flags, truth in [(["layout"], True), (["layout"], False), ([], True), ([], False)]]
        counts = analysis.confusion(rows, "layout", "truth")
        self.assertEqual({k: counts[k] for k in ("TP", "FP", "FN", "TN")}, dict(TP=1, FP=1, FN=1, TN=1))
        self.assertEqual(counts["precision_pct"], 50)

    def test_censored_latency_is_explicit(self):
        stats = analysis.latency([{"wall_sec": 30, "right_censored": True}, {"wall_sec": 2}])
        self.assertEqual(stats["right_censored"], 1)
        self.assertEqual(stats["over_10s"], 1)

    def test_unobserved_guard_is_not_a_true_negative(self):
        result = analysis.confusion([{"case": {"truth": False}}], "layout", "truth")
        self.assertEqual(result["TN"], 0)
        self.assertEqual(result["unobserved"], 1)

    def test_retype_is_not_answer_accuracy(self):
        row = {"id": "test", "suite": "keyboard", "question": "sample", "answer": "Please retype",
               "mode": "input_guard_repeat_retype", "status": "completed", "wall_sec": .01,
               "guard": {"flags": ["repeated_character_typo"], "should_retype": True},
               "case": {"expected_flags": ["repeated_character_typo"], "should_block_answer": False}}
        result = analysis.diagnose(row, None)
        self.assertIn("expected_retype_outcome", result["tags"])
        self.assertIn("legacy_block_policy_disagreement", result["tags"])
        self.assertNotIn("automated_contract_pass", result["tags"])

    def test_baseline_is_labeled_not_gold(self):
        row = {"id": "test", "suite": "faq", "question": "sample", "answer": "answer", "mode": "fast",
               "status": "completed", "wall_sec": .1, "case": {}, "legacy_judge": {"passed": True}}
        result = analysis.diagnose(row, {"answer": "previous answer"})
        self.assertEqual(result["baseline_answer_not_gold"], "previous answer")
        self.assertEqual(result["tags"], ["automated_contract_pass"])


if __name__ == "__main__":
    unittest.main()
