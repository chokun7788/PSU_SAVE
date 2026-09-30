from __future__ import annotations

import unittest

from app.core.thai_transposition_recovery import (
    detect_thai_transposition_recovery,
    recover_thai_transposition_query,
)
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input


def _answer(question: str):
    return answer_question_pipeline_debug(
        question,
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
    )


class ThaiTranspositionRecoveryTests(unittest.TestCase):
    def test_adjacent_order_error_in_capability_question(self) -> None:
        cases = {
            "สามารถถามอะไรดไ้บ้าง": "สามารถถามอะไรได้บ้าง",
            "ถามอะไรดไ้บ้าง": "ถามอะไรได้บ้าง",
            "ทำอะไรดไ้บ้าง": "ทำอะไรได้บ้าง",
            "ช่วยอะไรดไ้บ้างครับ": "ช่วยอะไรได้บ้างครับ",
        }
        for original, expected in cases.items():
            with self.subTest(original=original):
                recovery = detect_thai_transposition_recovery(original)
                self.assertIsNotNone(recovery)
                self.assertEqual(recovery.observed, "ดไ้")
                self.assertEqual(recovery.candidate, expected)
                self.assertEqual(preprocess_input(original).clean_query, expected)
                self.assertEqual(preprocess_input(original).raw_query, original)
                result = _answer(original)
                self.assertEqual(result.route.intent, "chatbot_identity")
                self.assertIn("ช่วยตอบคำถามเกี่ยวกับ", result.answer)

    def test_other_subjects_and_unrelated_messages_are_not_rewritten(self) -> None:
        for question in (
            "สามารถถามอะไรได้บ้าง",
            "ดไ้",
            "PC1 ทำอะไรดไ้บ้าง",
            "PS5 ทำอะไรดไ้บ้าง",
            "ในเกมทำอะไรดไ้บ้าง",
            "ผู้จัดการทำอะไรดไ้บ้าง",
            "ถามอะไรดไ้บ้างบน PC",
            "วันนี้ 10:00 PC1 ว่างไหม",
        ):
            with self.subTest(question=question):
                self.assertIsNone(detect_thai_transposition_recovery(question))
                self.assertEqual(recover_thai_transposition_query(question), question)


if __name__ == "__main__":
    unittest.main()
