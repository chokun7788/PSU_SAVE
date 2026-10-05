from __future__ import annotations

import copy
import os
import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import patch

from app.booking.live_status import _snapshot_from_payload, _unavailable, is_live_booking_question, render_live_booking_answer
from app.pipeline.engine import answer_question_pipeline_debug
from tests.smoke_test_live_booking_status import LIVE_PAYLOAD


def fixture():
    payload = copy.deepcopy(LIVE_PAYLOAD)
    payload.update(date="2026-10-01", now="2026-10-01 14:30:00", generated_at="2026-10-01 14:30:01")
    payload["center"]["open_periods"] = [["09:00", "12:00"], ["13:00", "16:00"]]
    # This new fixture deliberately books Nintendo for the requested 15:00
    # slot; the unchanged legacy fixture has that slot available.
    switch = next(r for r in payload["resources"] if r["resource_name"] == "Nintendo Switch (Morning)")
    switch["slots"][-1].update(status="busy", available_count=0, booked_count=1)
    return payload


class AvailableEquipmentOnlyTests(unittest.TestCase):
    def setUp(self):
        # This fixture describes 1 October, independently of the host clock.
        clock = patch('app.calendar.service_calendar.now_bangkok', return_value=datetime(2026, 10, 1, 14, 30, tzinfo=ZoneInfo('Asia/Bangkok')))
        clock.start()
        self.addCleanup(clock.stop)

    def test_broad_vacancy_is_live_but_inventory_is_static(self):
        for query in (
            "ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง",
            "ตอนบ่ายสามมีอุปกรณ์อะไรว่างให้เล่นบ้าง",
            "มีอุปกรณ์อะไรว่างให้เล่นบ้างตอนนี้",
            "ตอน15:00มีอะไรว่างบ้าง",
            "What equipment is available to play at 3pm?",
            "Which devices are free at 15:00?",
            "Which stations are available now?",
        ):
            with self.subTest(query=query):
                self.assertTrue(is_live_booking_question(query))
        for query in ("มีอุปกรณ์อะไรบ้าง", "What equipment is available?", "What equipment is available in VR Zone?", "What games are available at 3pm?", "How much does PC cost at 3pm?"):
            with self.subTest(query=query):
                self.assertFalse(is_live_booking_question(query))

    def test_exact_user_question_lists_only_free_devices_for_15_slot(self):
        status = _snapshot_from_payload(fixture())
        answer = render_live_booking_answer("ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง", status, "th")
        self.assertIn("15:00-16:00", answer)
        self.assertIn("6 รายการ", answer)
        for name in ("PC #01", "PC #02", "PC #03", "Cockpit #1", "VR Station (Morning)", "VR Station (Afternoon)"):
            self.assertIn("•    " + name, answer)
        for name in ("PlayStation 5 #1", "Nintendo Switch (Morning)"):
            self.assertNotIn(name, answer)
        self.assertNotIn("ถูกจอง", answer)
        self.assertNotIn("Gaming Monitor", answer)

    def test_english_uses_same_free_set_and_time(self):
        answer = render_live_booking_answer("What equipment is available to play at 3pm?", _snapshot_from_payload(fixture()), "en")
        self.assertIn("15:00-16:00", answer)
        self.assertIn("6 resources", answer)
        self.assertIn("PC #01", answer)  # busy now, but free at requested 15:00
        self.assertNotIn("PlayStation 5 #1", answer)
        self.assertNotIn("Nintendo Switch (Morning)", answer)
        self.assertNotIn(": booked", answer)

    def test_whole_range_filters_partial_booking_and_no_show(self):
        payload = fixture()
        payload["resources"][2]["slots"][-1].update(status="no_show", available_count=0, no_show_count=1)
        answer = render_live_booking_answer("14:00-16:00 มีอุปกรณ์อะไรว่างบ้าง", _snapshot_from_payload(payload), "th")
        for absent in ("PC #01", "PC #03", "PlayStation 5 #1", "VR Station (Afternoon)", "Nintendo Switch (Morning)"):
            self.assertNotIn(absent, answer)
        self.assertIn("PC #02", answer)
        self.assertIn("Cockpit #1", answer)
        self.assertIn("VR Station (Morning)", answer)

    def test_closed_period_lists_no_devices(self):
        payload = fixture()
        payload["center"].update(open=False, reason="owner fixture closure")
        for locale, query in (("th", "ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง"), ("en", "What equipment is available at 3pm?")):
            answer = render_live_booking_answer(query, _snapshot_from_payload(payload), locale)
            self.assertIn("ศูนย์ไม่เปิด" if locale == "th" else "studio is closed", answer)
            self.assertNotIn("•    PC", answer)

    def test_all_booked_returns_empty_list_not_inventory(self):
        payload = fixture()
        for resource in payload["resources"]:
            for slot in resource["slots"]:
                slot.update(status="busy", available_count=0, booked_count=1)
        answer = render_live_booking_answer("ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง", _snapshot_from_payload(payload), "th")
        self.assertIn("0 รายการ", answer)
        self.assertIn("ไม่พบอุปกรณ์ที่ยืนยันได้ว่าว่าง", answer)
        self.assertNotIn("•    PC", answer)

    def test_missing_slot_is_not_assumed_free(self):
        payload = fixture()
        payload["resources"][1]["slots"] = []
        answer = render_live_booking_answer("ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง", _snapshot_from_payload(payload), "th")
        self.assertNotIn("PC #02", answer)
        self.assertIn("ข้อมูล Slot ไม่ครบ", answer)

    def test_past_time_is_booking_history_not_bookable_now(self):
        payload = fixture()
        payload["now"] = "2026-10-01 16:30:00"
        answer = render_live_booking_answer("ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง", _snapshot_from_payload(payload), "th")
        self.assertIn("ประวัติการจอง", answer)
        self.assertIn("ไม่มีรายการจอง", answer)
        self.assertNotIn("อุปกรณ์ที่ว่างใน", answer)

    def test_zone_status_still_lists_both_free_and_booked(self):
        answer = render_live_booking_answer("PC ว่างไหม", _snapshot_from_payload(fixture()), "th")
        self.assertIn("PC #01: ถูกจองแล้ว", answer)
        self.assertIn("PC #02: ว่าง", answer)

    def test_pipeline_routes_actual_question_to_wordpress_and_filters_answer(self):
        for locale, query in (("th", "ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง"), ("en", "What equipment is available to play at 3pm?")):
            with self.subTest(locale=locale), patch.dict(os.environ, {"PSU_LIVE_BOOKING_FETCH_MODE": "wordpress", "PSU_LIVE_BOOKING_ENABLED": "1", "PSU_LIVE_BOOKING_CACHE_SEC": "0"}), patch("app.booking.wordpress_status.fetch_wordpress_status", return_value=fixture()) as fetch:
                result = answer_question_pipeline_debug(query, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=False)
            self.assertEqual(result.mode, "pipeline:live_booking_status_fast_path")
            self.assertIn("15:00-16:00", result.answer)
            self.assertIn("PC #01", result.answer)
            self.assertNotIn("PlayStation 5 #1", result.answer)
            fetch.assert_called_once_with("2026-10-01", 5.0)

    def test_upstream_failure_never_falls_back_to_static_equipment(self):
        with patch("app.runtime.fast_answer.get_live_booking_status", return_value=_unavailable("2026-10-01", "fixture unavailable")):
            result = answer_question_pipeline_debug("ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง", locale="th", experimental_allow_llm=False, experimental_rag_fallback=False)
        self.assertEqual(result.mode, "pipeline:live_booking_status_unavailable")
        self.assertIn("ยังยืนยันสถานะ", result.answer)
        self.assertNotIn("Gaming PC", result.answer)


if __name__ == "__main__":
    unittest.main()
