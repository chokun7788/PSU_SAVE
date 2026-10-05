from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
from unittest.mock import patch

from app.booking.live_status import get_live_booking_status, is_live_booking_question, render_live_booking_answer, reset_live_booking_cache
from app.booking.wordpress_status import BookingFetchError, _csv_rows, fetch_wordpress_status
from app.pipeline.engine import answer_question_pipeline_debug
from booking_dashboard import server as dashboard
from tests.smoke_test_live_booking_status import LIVE_PAYLOAD


SERVICES = "id,name,duration\n1,PC #01,60\n2,PC #02,60\n8,VR Station (Morning),30\n"
APPOINTMENTS = (
    "id,name,service_id,day,time,duration,status,email,token\n"
    "a,SENSITIVE_CUSTOMER,1,2026-10-01,10:00,60,approved,SENSITIVE_EMAIL,SENSITIVE_TOKEN\n"
    "b,SENSITIVE_CUSTOMER,2,2026-10-01,10:00,60,cancelled,SENSITIVE_EMAIL,SENSITIVE_TOKEN\n"
    "c,SENSITIVE_CUSTOMER,2,2026-10-01,11:00,60,no-show,SENSITIVE_EMAIL,SENSITIVE_TOKEN\n"
    "d,SENSITIVE_CUSTOMER,8,2026-10-01,10:00,30,approved,SENSITIVE_EMAIL,SENSITIVE_TOKEN\n"
)


class BookingOnDemandTests(unittest.TestCase):
    def setUp(self) -> None:
        # Relative "today" questions must use the date of the frozen CSV.
        clock = patch('app.calendar.service_calendar.now_bangkok', return_value=datetime(2026, 10, 1, 10, 15, tzinfo=ZoneInfo('Asia/Bangkok')))
        clock.start()
        self.addCleanup(clock.stop)
        self.env = patch.dict(os.environ, {"PSU_LIVE_BOOKING_ENABLED": "1", "PSU_LIVE_BOOKING_FETCH_MODE": "wordpress", "PSU_LIVE_BOOKING_CACHE_SEC": "0"})
        self.env.start()
        reset_live_booking_cache()

    def tearDown(self) -> None:
        reset_live_booking_cache()
        self.env.stop()

    def fixture_payload(self, day="2026-10-01"):
        def read(url, timeout):
            return (APPOINTMENTS if url == dashboard.APPOINTMENTS_CSV_URL else SERVICES), {"hash": "known-fixture"}

        with patch.object(dashboard, "read_url", side_effect=read), patch.object(dashboard, "now_bangkok", return_value=datetime(2026, 10, 1, 10, 15)):
            return fetch_wordpress_status(day, 5.0)

    def test_known_booking_oracle_and_privacy_without_http_dashboard(self):
        payload = self.fixture_payload()
        resources = {r["resource_id"]: r for r in payload["resources"]}
        self.assertEqual(payload["source"], "remote_csv_live")
        self.assertEqual(payload["privacy"], "aggregate_only")
        self.assertEqual(resources["1"]["available_now"], 0)
        self.assertEqual(resources["2"]["available_now"], 1)  # cancelled is not booked
        for resource, start, expected in (("1", "10:00", 0), ("2", "10:00", 1), ("2", "11:00", 0), ("8", "10:00", 0), ("8", "12:00", 0)):
            slot = next(s for s in resources[resource]["slots"] if s["start"] == start)
            self.assertEqual(slot["available_count"], expected)
        self.assertNotIn("SENSITIVE", json.dumps(payload))
        self.assertNotIn("today_bookings", json.dumps(payload))

    def test_csv_personal_fields_removed_before_calculation(self):
        rows = _csv_rows(APPOINTMENTS, "appointments")
        self.assertNotIn("SENSITIVE", json.dumps(rows))
        self.assertNotIn("id", rows[0])
        self.assertEqual(rows[0]["service_id"], "1")

    def test_header_only_appointments_are_a_valid_empty_export(self):
        self.assertEqual(_csv_rows(APPOINTMENTS.splitlines()[0] + "\n", "appointments"), [])

    def test_html_empty_missing_fields_and_truncated_rows_are_rejected(self):
        for text, kind in (("<html>please log in</html>", "appointments"), ("", "appointments"), ("id,name\n1,PC\n", "services"), ("id,name,duration\n1,PC\n", "services"), ("id,name,duration\n", "services")):
            with self.subTest(kind=kind, text=text):
                with self.assertRaises(BookingFetchError):
                    _csv_rows(text, kind)

    def test_missing_calendar_never_created_or_replaced(self):
        with tempfile.TemporaryDirectory() as temp:
            missing = Path(temp) / "owner_schedule.json"
            with patch.object(dashboard, "CENTER_SCHEDULE_FILE", missing), patch.object(dashboard, "read_url") as read:
                with self.assertRaises(BookingFetchError) as exc:
                    fetch_wordpress_status("2026-10-01", 5)
            self.assertEqual(exc.exception.code, "calendar_unavailable")
            self.assertFalse(missing.exists())
            read.assert_not_called()

    def test_owner_special_closure_is_honored_without_rewriting(self):
        with tempfile.TemporaryDirectory() as temp:
            schedule = Path(temp) / "owner_schedule.json"
            saved = {"weekly": {}, "dates": {"2026-10-01": {"open": False, "reason": "Owner fixture closure"}}}
            schedule.write_text(json.dumps(saved), encoding="utf-8")
            before = schedule.read_bytes()
            with patch.object(dashboard, "CENTER_SCHEDULE_FILE", schedule):
                payload = self.fixture_payload()
            self.assertFalse(payload["center"]["open"])
            self.assertEqual(schedule.read_bytes(), before)
            self.assertTrue(all(s["available_count"] == 0 for r in payload["resources"] for s in r["slots"]))

    def test_shared_timeout_budget_does_not_start_second_fetch_after_expiry(self):
        with patch("app.booking.wordpress_status.time.monotonic", side_effect=[0, 0, 6]), patch.object(dashboard, "read_url", return_value=(APPOINTMENTS, {"hash": "fixture"})) as read:
            with self.assertRaises(BookingFetchError) as exc:
                fetch_wordpress_status("2026-10-01", 5)
        self.assertEqual(exc.exception.code, "timeout")
        self.assertEqual(read.call_count, 1)

    def test_each_question_gets_fresh_export_when_cache_zero(self):
        first = copy.deepcopy(LIVE_PAYLOAD)
        second = copy.deepcopy(first)
        second["resources"][0]["slots"][0].update(status="available", booked_count=0, available_count=1)
        with patch("app.booking.wordpress_status.fetch_wordpress_status", side_effect=[first, second]) as read, patch("app.booking.live_status.urlopen") as http:
            a = get_live_booking_status(first["date"])
            b = get_live_booking_status(first["date"])
        self.assertEqual(a.resources[0].slots[0].available_count, 0)
        self.assertEqual(b.resources[0].slots[0].available_count, 1)
        self.assertEqual(read.call_count, 2)
        self.assertFalse(b.cached)
        http.assert_not_called()

    def test_next_question_recovers_from_upstream_failure_even_with_cache_enabled(self):
        with patch.dict(os.environ, {"PSU_LIVE_BOOKING_CACHE_SEC": "10"}), patch("app.booking.wordpress_status.fetch_wordpress_status", side_effect=[BookingFetchError("upstream_unavailable", "fixture offline"), LIVE_PAYLOAD]) as read:
            failed = get_live_booking_status(LIVE_PAYLOAD["date"])
            recovered = get_live_booking_status(LIVE_PAYLOAD["date"])
        self.assertFalse(failed.ok)
        self.assertEqual(failed.error_code, "upstream_unavailable")
        self.assertTrue(recovered.ok)
        self.assertEqual(read.call_count, 2)
        for locale, phrase in (("th", "ดึงข้อมูลจองสดจาก WordPress ไม่สำเร็จ"), ("en", "could not be fetched from WordPress")):
            answer = render_live_booking_answer("PC available now", failed, locale)
            self.assertIn(phrase, answer)
            self.assertNotIn("2/", answer)

    def test_wrong_date_sample_and_empty_resources_never_confirm_vacancy(self):
        for payload in ({**LIVE_PAYLOAD, "date": "2026-10-02"}, {**LIVE_PAYLOAD, "source": "sample_fallback"}, {**LIVE_PAYLOAD, "resources": []}):
            reset_live_booking_cache()
            with patch("app.booking.wordpress_status.fetch_wordpress_status", return_value=payload):
                self.assertFalse(get_live_booking_status(LIVE_PAYLOAD["date"]).ok)

    def test_selected_owner_dashboard_not_replaced_by_bundled_calendar(self):
        with patch.dict(os.environ, {"PSU_LIVE_BOOKING_FETCH_MODE": "dashboard", "PSU_LIVE_BOOKING_STATUS_URL": "http://127.0.0.1:8080/api/chatbot-status"}), patch("app.booking.live_status.urlopen", side_effect=ConnectionRefusedError()), patch("app.booking.wordpress_status.fetch_wordpress_status") as direct:
            failed = get_live_booking_status("2026-10-01")
        self.assertFalse(failed.ok)
        self.assertEqual(failed.transport, "dashboard")
        direct.assert_not_called()

    def test_read_disabled_does_not_call_any_source(self):
        with patch.dict(os.environ, {"PSU_LIVE_BOOKING_ENABLED": "0"}), patch("app.booking.wordpress_status.fetch_wordpress_status") as direct:
            failed = get_live_booking_status("2026-10-01")
        self.assertEqual(failed.error_code, "disabled")
        direct.assert_not_called()

    def test_thai_and_english_booking_slot_questions_reach_live_source(self):
        queries = ["วันนี้มีช่วงไหนให้จองบ้าง", "วันนี้จอง PC ช่วงไหนได้บ้าง", "เช็คตารางจองวันนี้", "จอง PC1 ได้ไหม", "What slots can I book today?", "Can I reserve PC1 at 14:00 today?", "Show booking availability today", "cockpik ว่างไหม", "ตนนี้ pc ว่างให้เล่นไหม"]
        for query in queries:
            with self.subTest(query=query):
                self.assertTrue(is_live_booking_question(query))

    def test_procedure_price_inventory_and_personal_tracking_not_live_aggregate(self):
        for query in ["จอง PC ยังไง", "ราคาจอง PC เท่าไหร่", "มีเกมอะไรบ้าง", "เปิดวันไหนบ้าง", "How do I book PC?", "How much does PC cost?", "What equipment is available?", "Check my booking", "รายการจองของฉันวันนี้", "Is my reservation available now?"]:
            with self.subTest(query=query):
                self.assertFalse(is_live_booking_question(query))

    def test_pipeline_uses_live_fixture_and_records_transport_not_customer(self):
        payload = self.fixture_payload()
        for locale, question, words in (("th", "จอง PC1 ได้ไหมวันนี้ตอน10โมง", "ไม่ว่าง"), ("en", "Can I book PC1 today at 10am?", "not available")):
            with self.subTest(locale=locale), patch("app.booking.wordpress_status.fetch_wordpress_status", return_value=payload):
                result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=False)
            self.assertEqual(result.mode, "pipeline:live_booking_status_fast_path")
            self.assertIn(words, result.answer)
            stage = next(t for t in result.trace if t.stage == "live_booking_status")
            self.assertEqual(stage.metadata["transport"], "wordpress")
            self.assertFalse(stage.metadata["cached"])
            self.assertNotIn("SENSITIVE", str(result))

    def test_day_wide_slot_question_lists_multiple_slots_in_both_languages(self):
        with patch("app.booking.wordpress_status.fetch_wordpress_status", return_value=self.fixture_payload()):
            status = get_live_booking_status("2026-10-01")
        for locale, query, expected in (("th", "วันนี้จอง PC ช่วงไหนได้บ้าง", "10:00-11:00: ว่าง 1/2"), ("en", "What PC slots can I book today?", "10:00-11:00: 1/2 available")):
            with self.subTest(locale=locale):
                answer = render_live_booking_answer(query, status, locale)
                self.assertIn(expected, answer)
                self.assertIn("11:00-12:00", answer)
                self.assertIn("12:00-13:00: " + ("ปิด" if locale == "th" else "closed"), answer)
                self.assertIn("PC #02", answer)
                self.assertNotIn("VR Station", answer)

    def test_new_slot_listing_question_runs_through_pipeline_not_weekly_template(self):
        payload = self.fixture_payload()
        with patch("app.booking.wordpress_status.fetch_wordpress_status", return_value=payload) as direct:
            result = answer_question_pipeline_debug("วันนี้มีช่วงไหนให้จองบ้าง", locale="th", experimental_allow_llm=False, experimental_rag_fallback=False)
        self.assertEqual(result.mode, "pipeline:live_booking_status_fast_path")
        self.assertIn("10:00-11:00", result.answer)
        self.assertIn("13:00-14:00", result.answer)
        direct.assert_called_once()


if __name__ == "__main__":
    unittest.main()
