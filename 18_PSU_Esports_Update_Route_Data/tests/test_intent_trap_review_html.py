from __future__ import annotations

import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path

from tools.build_intent_trap_review_html import DEFAULT_SOURCE, build_html


def _embedded_payload(html: str) -> dict:
    match = re.search(r'<script id="reviewData" type="application/json">(.*?)</script>', html, re.DOTALL)
    assert match is not None
    return json.loads(match.group(1))


class ReviewHtmlTests(unittest.TestCase):
    def test_review_html_contains_all_400_answers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "review.html"
            build_html(DEFAULT_SOURCE, output)
            html = output.read_text(encoding="utf-8")
            payload = _embedded_payload(html)

        self.assertEqual(len(payload["items"]), 400)
        self.assertEqual(len({item["id"] for item in payload["items"]}), 400)
        self.assertEqual({item["locale"] for item in payload["items"]}, {"th", "en"})
        self.assertTrue(all(item["question"].strip() and item["answer"].strip() for item in payload["items"]))
        self.assertEqual(payload["source_sha256"], hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest())
        self.assertTrue(all(f'data-decision="{decision}"' in html for decision in ("correct", "partial", "incorrect")))
        self.assertIn("localStorage.setItem", html)
        self.assertIn('id="exportButton"', html)
        self.assertIn('id="importButton"', html)

    def test_review_data_cannot_end_embedded_script(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.jsonl"
            row = {
                "locale": "en",
                "domain": "unclear_or_outside_scope",
                "question": "What about </script><script>alert(1)</script>?",
                "answer": "Please clarify.",
                "actual_route": "clarification",
                "actual_status": "completed",
                "evaluation_state": "manual_review_required",
            }
            source.write_text(
                "\n".join(json.dumps({"id": f"REVIEW-{index:04d}", **row}) for index in range(400)),
                encoding="utf-8",
            )
            output = Path(directory) / "review.html"
            build_html(source, output)
            html = output.read_text(encoding="utf-8")

        self.assertNotIn("</script><script>alert(1)", html)
        self.assertEqual(_embedded_payload(html)["items"][0]["question"], row["question"])

    def test_review_html_rejects_duplicate_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.jsonl"
            row = {
                "id": "same-id",
                "locale": "th",
                "domain": "food_bring_scope",
                "question": "คำถาม",
                "answer": "คำตอบ",
                "actual_route": "clarification",
                "actual_status": "completed",
                "evaluation_state": "manual_review_required",
            }
            source.write_text("\n".join(json.dumps(row, ensure_ascii=False) for _ in range(400)), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "400 unique"):
                build_html(source, Path(directory) / "review.html")


if __name__ == "__main__":
    unittest.main()
