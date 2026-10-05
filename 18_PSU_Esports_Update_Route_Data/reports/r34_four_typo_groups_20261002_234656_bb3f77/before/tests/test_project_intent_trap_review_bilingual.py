from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.project_intent_trap_review_bilingual import CORPUS, project


class BilingualReviewProjectionTests(unittest.TestCase):
    def _review_file(self, directory: Path) -> Path:
        rows = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines() if line.strip()]
        decisions = [
            {"id": row["id"], "decision": "incorrect", "note": "แค่จองกับโอนเงินก็สามารถใช้ได้เลย" if row["id"] == "INTENT-TRAP-TH-0201" else ""}
            for row in rows
            if row["locale"] == "th" and row["id"] != "INTENT-TRAP-TH-0121"
        ]
        decisions.append({"id": "INTENT-TRAP-EN-0101", "decision": "incorrect", "note": ""})
        path = directory / "review.json"
        path.write_text(json.dumps({
            "source_sha256": hashlib.sha256(CORPUS.read_bytes()).hexdigest(),
            "decisions": decisions,
        }, ensure_ascii=False), encoding="utf-8")
        return path

    def test_projects_pairs_without_claiming_human_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = project(self._review_file(Path(directory)))
        entries = {entry["id"]: entry for entry in result["decisions"]}
        self.assertEqual(result["total"], 400)
        self.assertEqual(result["reviewed"], 400)
        self.assertEqual(result["manual_reviewed"], 200)
        self.assertEqual(result["assistant_projected"], 200)
        self.assertEqual(entries["INTENT-TRAP-TH-0121"]["origin"], "assistant_projected")
        self.assertEqual(entries["INTENT-TRAP-EN-0101"]["origin"], "user_manual")
        self.assertEqual(entries["INTENT-TRAP-EN-0102"]["origin"], "assistant_projected")
        food = entries["INTENT-TRAP-EN-0201"]
        self.assertIn("note_about_booking_on_food_question", food["warnings"])
        self.assertIn("Booking and making", food["translated_source_note_en"])
        self.assertNotEqual(food["note"], food["translated_source_note_en"])
        self.assertEqual(entries["INTENT-TRAP-EN-0451"]["decision"], "partial")

    def test_rejects_review_from_another_corpus(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            review_path = self._review_file(Path(directory))
            review = json.loads(review_path.read_text(encoding="utf-8"))
            review["source_sha256"] = "wrong"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "does not match"):
                project(review_path)


if __name__ == "__main__":
    unittest.main()
