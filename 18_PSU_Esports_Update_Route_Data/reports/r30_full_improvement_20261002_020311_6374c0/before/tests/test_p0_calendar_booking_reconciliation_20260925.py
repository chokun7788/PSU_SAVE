from __future__ import annotations

import os
import time
import unittest
from datetime import date, datetime
from unittest.mock import patch

from app.booking.live_status import (
    LiveBookingSnapshot,
    LiveResource,
    LiveSlot,
    _snapshot_from_payload,
    is_live_booking_question,
    live_booking_calendar_conflict,
    render_live_booking_answer,
    requested_time_window,
)
from app.calendar.service_calendar import resolve_date_from_text
from app.pipeline.bilingual_english import _answer_schedule
from app.pipeline.schemas import EntityBundle
from app.runtime.fast_answer import answer_schedule
from booking_dashboard import server as dashboard


def snapshot(day: str, at: str) -> LiveBookingSnapshot:
    slot_start = at[:2] + ":00"
    slot_end = f"{int(at[:2]) + 1:02d}:00"
    return LiveBookingSnapshot(
        ok=True,
        date=day,
        now=f"{day}T{at}:00+07:00",
        generated_at=f"{day}T09:00:00+07:00",
        source="remote_csv_live",
        center_open=True,
        center_reason="",
        open_periods=(("09:00", "16:00"),),
        resources=(
            LiveResource(
                resource_id="1",
                resource_name="PC #01",
                capacity=1,
                status="available",
                available_now=1,
                slots=(LiveSlot(slot_start, slot_end, "available", 0, 0, 1),),
            ),
        ),
    )


class CalendarBookingReconciliationTests(unittest.TestCase):
    def test_iso_date_resolver_and_thai_special_closure(self) -> None:
        resolved = resolve_date_from_text("2026-07-28 เปิดไหม", today=date(2026, 9, 25))
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved.target_date, date(2026, 7, 28))
        result = answer_schedule("2026-07-28 เปิดไหม", time.perf_counter())
        self.assertIsNotNone(result)
        self.assertIn("ศูนย์ปิดให้บริการ", result.answer)

    def test_english_explicit_dates_use_recorded_closure(self) -> None:
        for question in (
            "Is the studio open on 28/07/2026?",
            "Is the studio open on 2026-07-28?",
        ):
            with self.subTest(question=question):
                result = _answer_schedule(question, EntityBundle())
                self.assertIsNotNone(result)
                self.assertIn("closed due to a registered special closure", result.answer)
                self.assertIn("28", result.answer)

    def test_holiday_alone_does_not_claim_studio_closure(self) -> None:
        with patch.dict(os.environ, {"PSU_ESPORTS_TODAY": "2026-10-12"}):
            th = answer_schedule("พรุ่งนี้เปิดไหม", time.perf_counter())
            en = _answer_schedule("Is the studio open tomorrow?", EntityBundle())
        self.assertIsNotNone(th)
        self.assertIsNotNone(en)
        self.assertIn("วันหยุดไทยอย่างเดียวไม่ได้ทำให้ปิดอัตโนมัติ", th.answer)
        self.assertIn("a Thai public holiday alone does not automatically close", en.answer)

    def test_disagreement_never_claims_lunch_or_special_date_available(self) -> None:
        for day, at in (("2026-09-28", "12:30"), ("2026-09-29", "12:30"), ("2026-07-28", "13:00")):
            status = snapshot(day, at)
            for query, locale in (
                (f"PC #01 ว่างไหม {day} {at}", "th"),
                (f"Is PC #01 available on {day} at {at}?", "en"),
            ):
                with self.subTest(day=day, at=at, locale=locale):
                    self.assertIsNotNone(live_booking_calendar_conflict(query, status))
                    answer = render_live_booking_answer(query, status, locale)
                    self.assertIn("ขัดกับ" if locale == "th" else "disagree", answer)
                    self.assertNotIn("ว่างอยู่ตอนนี้", answer)
                    self.assertNotIn("is available right now", answer)

    def test_compact_thai_station_time_reads_requested_hour(self) -> None:
        status = snapshot("2026-09-29", "08:00")
        for query, expected in (
            ("วันนี้ตอน10โมง PC1 ว่างไหม", "10:00"),
            ("วันนี้ตอน10:00 PC1 ว่างไหม", "10:00"),
            ("วันนี้ตอน10โมงครึ่ง PC1 ว่างไหม", "10:30"),
            ("Is PC1 free today at 10am?", "10:00"),
        ):
            with self.subTest(query=query):
                window = requested_time_window(query, status)
                self.assertIsNotNone(window)
                self.assertEqual(window.start, expected)
                self.assertTrue(window.explicit)
        self.assertEqual(requested_time_window("PC1 ว่างไหม", status).start, "08:00")

    def test_regular_open_window_can_report_booking_fact(self) -> None:
        status = snapshot("2026-09-28", "13:00")
        query = "PC #01 ว่างไหม 2026-09-28 13:00"
        self.assertIsNone(live_booking_calendar_conflict(query, status))
        self.assertIn("ว่าง", render_live_booking_answer(query, status, "th"))

    def test_empty_service_export_is_unavailable_even_if_fetch_succeeded(self) -> None:
        payload = {
            "ok": True,
            "source": "remote_csv_live",
            "date": "2026-09-29",
            "center": {"open": True, "open_periods": [["09:00", "16:00"]]},
            "resources": [],
        }
        with self.assertRaisesRegex(ValueError, "no valid resources"):
            _snapshot_from_payload(payload)

    def test_now_opening_question_uses_live_path_in_both_languages(self) -> None:
        self.assertTrue(is_live_booking_question("Is the studio open now?"))
        self.assertTrue(is_live_booking_question("ตอนนี้เล่นได้ไหม"))


    def test_dashboard_weekly_lunch_is_not_bookable(self) -> None:
        for day, open_at_13 in (("2026-09-28", True), ("2026-09-29", True), ("2026-10-02", False)):
            with self.subTest(day=day), patch.object(dashboard, "now_bangkok", return_value=datetime(2026, 9, 25, 8, 0)):
                status = dashboard.build_status(
                    [], [{"id": "1", "name": "PC #01", "duration": "60"}], day,
                    {"mode": "remote_csv_live", "appointments_meta": {"hash": "fixture"}, "services_meta": {"hash": "fixture"}},
                )
                lunch = next(s for s in status["services"][0]["slots"] if s["start"] == "12:00")
                self.assertEqual((lunch["status"], lunch["available_count"]), ("closed", 0))
                self.assertFalse(any(start <= "12:30" < end for start, end in status["center"]["open_periods"]))
                at_13 = next(s for s in status["services"][0]["slots"] if s["start"] == "13:00")
                self.assertEqual(at_13["status"] == "available", open_at_13)

    def test_vr_half_hour_reservation_blocks_the_full_hour(self) -> None:
        schedule = dashboard.default_center_schedule()
        with patch.object(dashboard, "load_center_schedule", return_value=schedule), patch.object(
            dashboard, "now_bangkok", return_value=datetime(2026, 9, 29, 8, 0)
        ):
            status = dashboard.build_status(
                dashboard.parse_csv(
                    "id,service_id,day,time,duration,status\n"
                    "1,8,2026-09-29,09:00,30,approved\n"
                ),
                dashboard.parse_csv("id,name,duration\n8,VR Station (Morning),30\n"),
                "2026-09-29",
                {"mode": "remote_csv_live", "appointments_meta": {"hash": "fixture"}, "services_meta": {"hash": "fixture"}},
            )
        slot = next(s for s in status["services"][0]["slots"] if s["start"] == "09:00")
        self.assertEqual((slot["end"], slot["status"], slot["available_count"]), ("10:00", "busy", 0))
        live = _snapshot_from_payload(dashboard.chatbot_status_payload(status))
        self.assertIn("0/1", render_live_booking_answer("Is VR free from 09:30 to 10:00?", live, "en"))
        thai = render_live_booking_answer("VR 9โมงครึ่งว่างไหม", live, "th")
        self.assertIn("ไม่ว่างตลอดช่วง 09:00-10:00", thai)
        self.assertIn("0/1", thai)

    def test_dashboard_date_override_cannot_open_lunch(self) -> None:
        schedule = dashboard.default_center_schedule()
        schedule["dates"]["2026-09-29"] = {"open": True, "open_periods": [["11:00", "14:00"]]}
        with patch.object(dashboard, "load_center_schedule", return_value=schedule):
            center = dashboard.center_status_for_date("2026-09-29")
        self.assertEqual(center["source"], "date_override")
        self.assertEqual(center["open_periods"], [["11:00", "12:00"], ["13:00", "14:00"]])


if __name__ == "__main__":
    unittest.main()
