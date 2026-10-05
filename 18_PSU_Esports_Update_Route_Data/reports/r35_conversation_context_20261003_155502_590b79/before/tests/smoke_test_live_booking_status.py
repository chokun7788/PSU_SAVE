from __future__ import annotations

import os
import unittest
from datetime import date
from unittest.mock import patch

from app.booking.live_status import (
    get_live_booking_status,
    is_live_booking_question,
    _resource_scopes,
    render_live_booking_answer,
    reset_live_booking_cache,
    resolve_live_target_date,
)
from app.runtime.fast_answer import answer_live_booking_status


LIVE_PAYLOAD = {
    "ok": True,
    "date": "2026-09-17",
    "now": "2026-09-17 14:30:00",
    "generated_at": "2026-09-17 14:30:01",
    "source": "remote_csv_live",
    "center": {"open": True, "reason": "", "open_periods": [["09:00", "16:00"]]},
    "resources": [
        {
            "resource_id": "pc-01",
            "resource_name": "PC #01",
            "capacity": 1,
            "status": "busy",
            "available_now": 0,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "busy", "booked_count": 1, "no_show_count": 0, "available_count": 0},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
            "customer": "must not be read",
        },
        {
            "resource_id": "pc-02",
            "resource_name": "PC #02",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
        {
            "resource_id": "pc-03",
            "resource_name": "PC #03",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "13:00", "end": "14:00", "status": "past", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
        {
            "resource_id": "ps5-01",
            "resource_name": "PlayStation 5 #1",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "busy", "booked_count": 1, "no_show_count": 0, "available_count": 0},
            ],
        },
        {
            "resource_id": "cockpit-01",
            "resource_name": "Cockpit #1",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
        {
            "resource_id": "vr-morning",
            "resource_name": "VR Station (Morning)",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
        {
            "resource_id": "vr-afternoon",
            "resource_name": "VR Station (Afternoon)",
            "capacity": 1,
            "status": "busy",
            "available_now": 0,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "busy", "booked_count": 1, "no_show_count": 0, "available_count": 0},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
        {
            "resource_id": "switch-morning",
            "resource_name": "Nintendo Switch (Morning)",
            "capacity": 1,
            "status": "available",
            "available_now": 1,
            "slots": [
                {"start": "14:00", "end": "15:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
                {"start": "15:00", "end": "16:00", "status": "available", "booked_count": 0, "no_show_count": 0, "available_count": 1},
            ],
        },
    ],
}


class _Response:
    def __init__(self, body: bytes) -> None:
        self.body = body

    def read(self, _: int) -> bytes:
        return self.body

    def __enter__(self) -> "_Response":
        return self

    def __exit__(self, *_: object) -> None:
        return None


class LiveBookingStatusSmokeTest(unittest.TestCase):
    def assert_targeted_answer(self, actual: str, expected_body: str) -> None:
        lines = actual.splitlines()
        self.assertIn("2026-09-17", lines[0])
        self.assertEqual("\n".join(lines[1:-2]), expected_body)
        self.assertIn("2026-09-17 14:30:01", lines[-2])
        self.assertIn("https://esports.computing.psu.ac.th/reservation", lines[-1])

    def setUp(self) -> None:
        reset_live_booking_cache()
        self.previous = dict(os.environ)
        os.environ["PSU_LIVE_BOOKING_ENABLED"] = "1"
        os.environ["PSU_LIVE_BOOKING_CACHE_SEC"] = "0"

    def tearDown(self) -> None:
        os.environ.clear()
        os.environ.update(self.previous)
        reset_live_booking_cache()

    @patch("app.booking.live_status.urlopen")
    def test_only_aggregate_fields_are_exposed(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        public = snapshot.as_public_dict()

        self.assertTrue(snapshot.ok)
        self.assertEqual(public["resources"][0]["resource_name"], "PC #01")
        self.assertNotIn("customer", public["resources"][0])
        self.assertNotIn("appointment_id", public["resources"][0])
        self.assertNotIn("must not be read", str(public).lower())

    @patch("app.booking.live_status.urlopen")
    def test_renders_current_slot_in_thai_and_english(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        thai = render_live_booking_answer("ตอนนี้ slot ไหนว่าง", snapshot, "th")
        english = render_live_booking_answer("which slots are available now", snapshot, "en")
        self.assertIn("PC #01: ถูกจองแล้ว", thai)
        self.assertIn("PC #02: ว่าง", thai)
        self.assertIn("PC #01: booked", english)
        self.assertIn("PC #02: available", english)

    @patch("app.booking.live_status.urlopen")
    def test_compact_station_question_defaults_to_now_and_stays_concise(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        thai = render_live_booking_answer("pc2 ว่างไหม", snapshot, "th")
        self.assert_targeted_answer(thai, "PC #02 ว่างอยู่ตอนนี้ ณ 14:30 น. (เวลาไทย) ครับ")
        self.assertNotIn("PC #01", thai)
        self.assertNotIn("สถานะ Slot", thai)

        english = render_live_booking_answer("Is PC2 free?", snapshot, "en")
        self.assert_targeted_answer(english, "PC #02 is available right now (14:30, Asia/Bangkok).")
        self.assertNotIn("PC #01", english)

    @patch("app.booking.live_status.urlopen")
    def test_conversational_thai_time_uses_the_slot_and_reports_past_booking_history(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        answer = render_live_booking_answer("pc3 ตอนบ่ายโมงว่างไหม", snapshot, "th")
        self.assert_targeted_answer(answer, "PC #03 ไม่มีรายการจองในช่วง 13:00-14:00 น. (เวลาไทย) ครับ")
        self.assertNotIn("14:30", answer.splitlines()[1])

        explicit_range = render_live_booking_answer("PC3 บ่ายโมงถึงบ่ายสองโมง เคยถูกจองไหม", snapshot, "th")
        self.assert_targeted_answer(explicit_range, "PC #03 ไม่มีรายการจองในช่วง 13:00-14:00 น. (เวลาไทย) ครับ")

        english = render_live_booking_answer("Was PC3 booked at 1pm?", snapshot, "en")
        self.assert_targeted_answer(english, "PC #03 had no booking during 13:00-14:00 (Asia/Bangkok).")

    @patch("app.runtime.fast_answer.get_live_booking_status")
    def test_fast_path_keeps_thai_station_number_and_does_not_expand_to_zone(self, mocked_status) -> None:
        import json

        with patch("app.booking.live_status.urlopen") as mocked_urlopen:
            mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
            snapshot = get_live_booking_status("2026-09-17")
        mocked_status.return_value = snapshot

        result = answer_live_booking_status("pc เครื่อง 2 ว่างไหม", 0.0)
        self.assertIsNotNone(result)
        assert result is not None
        self.assert_targeted_answer(result.answer, "PC #02 ว่างอยู่ตอนนี้ ณ 14:30 น. (เวลาไทย) ครับ")
        self.assertNotIn("โซน PC", result.answer)

    @patch("app.runtime.fast_answer.get_live_booking_status")
    def test_fast_path_recovers_misspelled_zone_and_lists_resources(self, mocked_status) -> None:
        import json

        with patch("app.booking.live_status.urlopen") as mocked_urlopen:
            mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
            snapshot = get_live_booking_status("2026-09-17")
        mocked_status.return_value = snapshot
        result = answer_live_booking_status("cockpik ว่างไหม", 0.0)
        self.assertIsNotNone(result)
        assert result is not None
        self.assertIn("โซน Cockpit: ว่าง 1/1", result.answer)
        self.assertIn("Cockpit #1: ว่าง", result.answer)

    @patch("app.booking.live_status.urlopen")
    def test_zone_question_lists_every_station_without_an_explicit_list_request(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        summary = render_live_booking_answer("PC Zone ว่างไหม", snapshot, "th")
        self.assert_targeted_answer(
            summary,
            "โซน PC: ว่าง 2/3 รายการ ณ 14:30 น. (เวลาไทย)\n"
            "•    PC #01: ถูกจองแล้ว\n"
            "•    PC #02: ว่าง\n"
            "•    PC #03: ว่าง",
        )

        listing = render_live_booking_answer("PC Zone มีอะไรว่างบ้าง", snapshot, "th")
        self.assertIn("•    PC #01: ถูกจองแล้ว", listing)
        self.assertIn("•    PC #02: ว่าง", listing)

    @patch("app.booking.live_status.urlopen")
    def test_all_equipment_groups_and_multiple_targets_are_scoped(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        self.assertEqual(_resource_scopes("PC กับ VR ว่างไหม"), ("pc", "vr"))
        self.assertEqual(_resource_scopes("Cockpit, PlayStation and Nintendo available?"), ("cockpit", "ps5", "switch"))

        cockpit = render_live_booking_answer("cockpit ว่างให้เล่นไหม", snapshot, "th")
        self.assert_targeted_answer(cockpit, "โซน Cockpit: ว่าง 1/1 รายการ ณ 14:30 น. (เวลาไทย)\n•    Cockpit #1: ว่าง")

        playstation = render_live_booking_answer("PlayStation ว่างไหม", snapshot, "th")
        self.assert_targeted_answer(playstation, "โซน PlayStation 5: ว่าง 1/1 รายการ ณ 14:30 น. (เวลาไทย)\n•    PlayStation 5 #1: ว่าง")

        nintendo = render_live_booking_answer("Nintendo Switch ว่างไหม", snapshot, "en")
        self.assert_targeted_answer(nintendo, "Nintendo Switch Zone: 1/1 resources are available right now (14:30, Asia/Bangkok).\n•    Nintendo Switch (Morning): available")

        vr_afternoon = render_live_booking_answer("VR ช่วงบ่ายว่างไหม", snapshot, "th")
        self.assert_targeted_answer(vr_afternoon, "โซน VR: ไม่ว่าง ณ 14:30 น. (ว่าง 0/1 รายการ, เวลาไทย)\n•    VR Station (Afternoon): ถูกจองแล้ว")

        multiple = render_live_booking_answer("PC กับ VR ว่างไหม", snapshot, "th")
        self.assert_targeted_answer(
            multiple,
            "โซน PC: ว่าง 2/3 รายการ ณ 14:30 น. (เวลาไทย)\n"
            "•    PC #01: ถูกจองแล้ว\n•    PC #02: ว่าง\n•    PC #03: ว่าง\n"
            "โซน VR: ว่าง 1/2 รายการ ณ 14:30 น. (เวลาไทย)\n"
            "•    VR Station (Morning): ว่าง\n•    VR Station (Afternoon): ถูกจองแล้ว",
        )

        english_multiple = render_live_booking_answer("Are PC and VR free?", snapshot, "en")
        self.assert_targeted_answer(
            english_multiple,
            "PC Zone: 2/3 resources are available right now (14:30, Asia/Bangkok).\n"
            "•    PC #01: booked\n•    PC #02: available\n•    PC #03: available\n"
            "VR Zone: 1/2 resources are available right now (14:30, Asia/Bangkok).\n"
            "•    VR Station (Morning): available\n•    VR Station (Afternoon): booked",
        )

    @patch("app.booking.live_status.urlopen")
    def test_one_edit_zone_typos_use_the_live_status_path(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        for query, family, expected in (
            ("cockpik ว่างไหม", "cockpit", "Cockpit #1: ว่าง"),
            ("cokcpit ว่างไหม", "cockpit", "Cockpit #1: ว่าง"),
            ("nintndo ว่างไหม", "switch", "Nintendo Switch (Morning): ว่าง"),
            ("playstaton ว่างไหม", "ps5", "PlayStation 5 #1: ว่าง"),
        ):
            with self.subTest(query=query):
                self.assertEqual(_resource_scopes(query), (family,))
                self.assertTrue(is_live_booking_question(query))
                self.assertIn(expected, render_live_booking_answer(query, snapshot, "th"))
        station = render_live_booking_answer("cockpik #1 ว่างไหม", snapshot, "th")
        self.assertIn("Cockpit #1 ว่างอยู่ตอนนี้", station)
        self.assertNotIn("โซน Cockpit:", station)
        english = render_live_booking_answer("Is cockpik available now?", snapshot, "en")
        self.assertIn("Cockpit Zone: 1/1 resources are available", english)
        self.assertIn("Cockpit #1: available", english)
        for query in ("cocktail ว่างไหม", "Is Minecraft available?", "Which game is available in the Cockpit Zone?"):
            with self.subTest(query=query):
                self.assertFalse(is_live_booking_question(query))

    @patch("app.booking.live_status.urlopen")
    def test_english_plural_zone_questions_stay_scoped_and_list_all_resources(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        cases = (
            ("Are PCs available now?", ("pc",), "PC Zone: 2/3 resources", 3),
            ("Are VRs free?", ("vr",), "VR Zone: 1/2 resources", 2),
            ("Are PS5s available?", ("ps5",), "PlayStation 5 Zone: 1/1 resources", 1),
            ("Are switches available?", ("switch",), "Nintendo Switch Zone: 1/1 resources", 1),
            ("How many cockpits are available?", ("cockpit",), "Cockpit Zone: 1/1 resources", 1),
            ("Are cockpiks available?", ("cockpit",), "Cockpit Zone: 1/1 resources", 1),
            ("Are nintndos available?", ("switch",), "Nintendo Switch Zone: 1/1 resources", 1),
            ("Are PCs and VRs available?", ("pc", "vr"), "PC Zone: 2/3 resources", 5),
        )
        for query, scopes, summary, expected_rows in cases:
            with self.subTest(query=query):
                self.assertEqual(_resource_scopes(query), scopes)
                self.assertTrue(is_live_booking_question(query))
                answer = render_live_booking_answer(query, snapshot, "en")
                self.assertIn(summary, answer)
                self.assertEqual(answer.count("•    "), expected_rows)
        self.assertEqual(_resource_scopes("Are spaces available?"), ())

    @patch("app.booking.live_status.urlopen")
    def test_broad_zone_reports_each_resource_for_range_past_and_closed(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        future = render_live_booking_answer("PC ว่างไหม 14:00-16:00", snapshot, "th")
        self.assertIn("โซน PC: ว่างตลอดช่วง 14:00-16:00 น. 2/3", future)
        self.assertIn("PC #01: ถูกจองหรือไม่ว่างบางส่วนของช่วงเวลา", future)
        self.assertIn("PC #02: ว่างตลอดช่วง", future)
        future_en = render_live_booking_answer("Are PCs free from 14:00 to 16:00?", snapshot, "en")
        self.assertIn("PC Zone: 2/3 resources are available for the full period", future_en)
        self.assertIn("PC #01: booked or unavailable during part of the period", future_en)
        self.assertIn("PC #02: available for the full period", future_en)

        past = render_live_booking_answer("PC ว่างไหม 13:00", snapshot, "th")
        self.assertIn("PC #03: ไม่มีรายการจอง", past)
        self.assertIn("PC #01: ยังยืนยันไม่ได้", past)
        past_en = render_live_booking_answer("Were PCs booked at 13:00?", snapshot, "en")
        self.assertIn("PC #03: no booking", past_en)
        self.assertIn("PC #01: cannot confirm", past_en)

        closed_payload = json.loads(json.dumps(LIVE_PAYLOAD))
        closed_payload["center"]["open"] = False
        closed_payload["center"]["open_periods"] = []
        mocked_urlopen.return_value = _Response(json.dumps(closed_payload).encode("utf-8"))
        reset_live_booking_cache()
        closed = get_live_booking_status("2026-09-17")
        answer = render_live_booking_answer("PC ว่างไหม", closed, "th")
        self.assertIn("ว่าง 0/3 รายการ", answer)
        self.assertEqual(answer.count(": ปิดให้บริการ"), 3)
        closed_en = render_live_booking_answer("Are PCs available?", closed, "en")
        self.assertIn("the studio is not open", closed_en)
        self.assertEqual(closed_en.count(": studio closed"), 3)

        no_slots_payload = json.loads(json.dumps(LIVE_PAYLOAD))
        for resource in no_slots_payload["resources"]:
            if resource["resource_id"].startswith("pc-"):
                resource["slots"] = []
        mocked_urlopen.return_value = _Response(json.dumps(no_slots_payload).encode("utf-8"))
        reset_live_booking_cache()
        no_slots = get_live_booking_status("2026-09-17")
        unknown = render_live_booking_answer("PC ว่างไหม", no_slots, "th")
        self.assertIn("ยืนยันความว่างไม่ได้", unknown)
        self.assertEqual(unknown.count(": ยังยืนยันไม่ได้"), 3)

    @patch("app.booking.live_status.urlopen")
    def test_unknown_station_does_not_fall_back_to_the_whole_zone(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        answer = render_live_booking_answer("PC 99 ว่างไหม", snapshot, "th")
        self.assert_targeted_answer(answer, "ไม่พบ โซน PC เครื่อง #99 ใน Booking Dashboard ครับ")
        self.assertNotIn("1/2", answer)

    @patch("app.booking.live_status.urlopen")
    def test_filters_zone_station_and_checks_the_whole_time_range(self, mocked_urlopen) -> None:
        import json

        mocked_urlopen.return_value = _Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")

        thai = render_live_booking_answer("PC Zone ว่างอะไรบ้างช่วง 14:00-16:00", snapshot, "th")
        self.assertIn("โซน PC: ว่างตลอดช่วงเวลาที่ถาม 2/3", thai)
        self.assertIn("PC #01: ถูกจองหรือไม่ว่างบางส่วนของช่วงเวลา", thai)
        self.assertIn("PC #02: ว่างตลอดช่วง", thai)
        self.assertNotIn("PlayStation 5 #1", thai)

        english = render_live_booking_answer("Which PS5 stations are free from 14:00 to 16:00?", snapshot, "en")
        self.assertIn("PlayStation 5 Zone: 0/1 resources are available for the full requested period.", english)
        self.assertIn("PlayStation 5 #1: booked or unavailable during part of the period", english)
        self.assertNotIn("PC #01", english)

        station = render_live_booking_answer("Is PC #02 free from 14:00 to 16:00?", snapshot, "en")
        self.assert_targeted_answer(station, "PC #02 is available for the full period 14:00-16:00 (Asia/Bangkok).")
        self.assertNotIn("PC #01", station)


    def test_detects_live_questions_but_not_booking_howto(self) -> None:
        self.assertTrue(is_live_booking_question("ตอนนี้เปิดไหม"))
        self.assertTrue(is_live_booking_question("Which slots are available now?"))
        self.assertTrue(is_live_booking_question("PC Zone ว่างอะไรบ้างพรุ่งนี้ 13:00-14:00"))
        self.assertTrue(is_live_booking_question("Which PS5 stations are free tomorrow from 13:00 to 14:00?"))
        self.assertTrue(is_live_booking_question("pc2 ว่างไหม"))
        self.assertTrue(is_live_booking_question("Is PC2 free?"))
        self.assertFalse(is_live_booking_question("How do I book a slot?"))
        self.assertFalse(is_live_booking_question("Which game is available in the Cockpit Zone?"))
        self.assertFalse(is_live_booking_question("How long is one PC Zone booking slot?"))
        self.assertFalse(is_live_booking_question("I am planning a visit and need to know: Is Minecraft available at the studio?"))

    @patch("app.booking.live_status.today_bangkok", return_value=date(2026, 9, 17))
    def test_resolves_thai_and_english_target_dates(self, _) -> None:
        self.assertEqual(resolve_live_target_date("PC ว่างเมื่อวาน 13:00-14:00"), "2026-09-16")
        self.assertEqual(resolve_live_target_date("PC ว่างพรุ่งนี้ 13:00-14:00"), "2026-09-18")
        self.assertEqual(resolve_live_target_date("Which PC stations are free tomorrow?"), "2026-09-18")
        self.assertEqual(resolve_live_target_date("Slot on 2026-09-20 at 14:00"), "2026-09-20")

    @patch("app.booking.live_status.urlopen")
    def test_english_hides_unapproved_thai_closure_note(self, mocked_urlopen) -> None:
        import json

        payload = {**LIVE_PAYLOAD, "center": {"open": False, "reason": "Maintenance ช่วงบ่าย", "open_periods": [["09:00", "16:00"]]}}
        mocked_urlopen.return_value = _Response(json.dumps(payload).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        english = render_live_booking_answer("Is PC free from 14:00 to 15:00?", snapshot, "en")
        self.assertIn("studio is not open", english)
        self.assertNotIn("ช่วงบ่าย", english)

    @patch("app.booking.live_status.urlopen")
    def test_rejects_non_live_sample_payload(self, mocked_urlopen) -> None:
        import json

        payload = {**LIVE_PAYLOAD, "source": "sample_fallback"}
        mocked_urlopen.return_value = _Response(json.dumps(payload).encode("utf-8"))
        snapshot = get_live_booking_status("2026-09-17")
        self.assertFalse(snapshot.ok)
        self.assertIn("not live", snapshot.error)


if __name__ == "__main__":
    unittest.main()
