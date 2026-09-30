import importlib.util
import sys
import unittest
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("regression_runner_tested", ROOT / "tools/run_current_flow_regression.py")
runner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)


class FakeConnection:
    def __init__(self, events):
        self.events = events

    def poll(self, timeout):
        return bool(self.events)

    def recv(self):
        return self.events.pop(0)


class RunnerTests(unittest.TestCase):
    def test_plain_preserves_nested_values(self):
        @dataclass
        class Result:
            trace: list
        self.assertEqual(runner.plain(Result([SimpleNamespace(stage="test", ok=False)])),
                         {"trace": [{"stage": "test", "ok": False}]})

    def test_watchdog_preserves_guard_but_never_fabricates_answer(self):
        conn = FakeConnection([{"event": "phase", "guard": {"flags": []}, "pipeline_executed": True}])
        result = runner.receive_case(conn, 30)
        self.assertEqual(result["status"], "harness_timeout")
        self.assertEqual(result["answer"], "")
        self.assertTrue(result["right_censored"])
        self.assertTrue(result["pipeline_executed"])
        self.assertFalse(result["strict_passed"])

    def test_completed_response(self):
        result = runner.receive_case(FakeConnection([{"event": "result", "status": "completed", "answer": "ok"}]), 30)
        self.assertEqual(result, {"status": "completed", "answer": "ok"})

    def test_strict_latency_is_not_legacy_pass(self):
        result = SimpleNamespace(validation=SimpleNamespace(ok=True))
        judge = lambda *args: {"passed": True, "errors": []}
        check = runner.outcome_checks({}, result, 10.5, "faq", judge, judge)
        self.assertTrue(check["legacy_judge"]["passed"])
        self.assertFalse(check["strict_passed"])

    def test_strict_validation(self):
        result = SimpleNamespace(validation=SimpleNamespace(ok=False))
        judge = lambda *args: {"passed": True, "errors": []}
        self.assertFalse(runner.outcome_checks({}, result, 1, "faq", judge, judge)["strict_passed"])

    def test_mode_mismatch_is_separate_from_text(self):
        result = SimpleNamespace(validation=SimpleNamespace(ok=True))
        judge = lambda *args: {"passed": False, "errors": ["mode_mismatch:canonical_answer"]}
        check = runner.outcome_checks({}, result, 1, "faq", judge, judge)
        self.assertTrue(check["text_contract_passed"])
        self.assertFalse(check["strict_passed"])

    def test_percentile_nearest_rank(self):
        self.assertEqual(runner.percentile(list(range(1, 21)), .95), 19)


if __name__ == "__main__":
    unittest.main()
