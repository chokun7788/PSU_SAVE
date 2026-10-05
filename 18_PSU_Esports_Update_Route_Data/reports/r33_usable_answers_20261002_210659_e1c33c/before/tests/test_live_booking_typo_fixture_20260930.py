from __future__ import annotations

import unittest
from unittest.mock import patch

from app.booking.live_status import _snapshot_from_payload, _unavailable
from app.pipeline.engine import answer_question_pipeline_debug


def snapshot():
    def slot(status: str, available: int, booked: int) -> list[dict]:
        return [{
            "start": "14:00", "end": "15:00", "status": status,
            "booked_count": booked, "no_show_count": 0,
            "available_count": available,
        }]
    return _snapshot_from_payload({
        "ok": True, "date": "2026-09-30",
        "now": "2026-09-30 13:00:00",
        "generated_at": "2026-09-30 13:00:01",
        "source": "remote_csv_live",
        "center": {
            "open": True, "reason": "",
            "open_periods": [["09:00", "12:00"], ["13:00", "16:00"]],
        },
        "resources": [
            {
                "resource_id": "cockpit-01", "resource_name": "Cockpit #1",
                "capacity": 1, "status": "available", "available_now": 1,
                "slots": slot("available", 1, 0),
            },
            {
                "resource_id": "cockpit-02", "resource_name": "Cockpit #2",
                "capacity": 1, "status": "busy", "available_now": 0,
                "slots": slot("busy", 0, 1),
            },
        ],
    })


def answer(question: str, locale: str):
    return answer_question_pipeline_debug(
        question, locale=locale,
        experimental_allow_llm=False, experimental_rag_fallback=False,
    )


class LiveBookingTypoFixtureTests(unittest.TestCase):
    def test_thai_typo_uses_known_slot_truth(self) -> None:
        with patch("app.runtime.fast_answer.get_live_booking_status", return_value=snapshot()):
            result = answer("ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่าบง้าง", "th")
        self.assertEqual("schedule", result.route.category)
        self.assertIn("ว่างตลอดช่วงเวลาที่ถาม 1/2", result.answer)
        self.assertIn("Cockpit #1: ว่าง", result.answer)
        self.assertIn("Cockpit #2: ถูกจอง", result.answer)

    def test_english_answer_uses_same_snapshot(self) -> None:
        with patch("app.runtime.fast_answer.get_live_booking_status", return_value=snapshot()):
            result = answer("Which Cockpit Zone slots are availble at 14:00-15:00?", "en")
        self.assertEqual("schedule", result.route.category)
        self.assertIn("1/2", result.answer)
        self.assertIn("Cockpit #1: available", result.answer)
        self.assertIn("Cockpit #2: booked", result.answer)

    def test_api_unavailable_never_claims_vacancy(self) -> None:
        with patch("app.runtime.fast_answer.get_live_booking_status",
                   side_effect=lambda selected_date: _unavailable(selected_date, "fixture unavailable")):
            result = answer("ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่าบง้าง", "th")
        self.assertIn("ยังยืนยันสถานะ", result.answer)
        self.assertNotIn("ว่างตลอดช่วงเวลาที่ถาม 1/2", result.answer)


if __name__ == "__main__":
    unittest.main()
