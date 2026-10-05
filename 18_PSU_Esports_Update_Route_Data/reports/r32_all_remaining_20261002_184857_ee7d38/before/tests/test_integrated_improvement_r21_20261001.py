from __future__ import annotations
import unittest
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.structured_tools import _detect_zone
from tests.test_reliability_flow_20261001 import run_focused_case
from tools.manage_english_localizations import source_records
from app.knowledge.localization import approved_localization

# New semantic checks supplement the unchanged frozen GT. Each group is AND;
# alternatives inside one group are OR. Facts refer to the stored source.
CASES = (
    ("price-not-permission", "th", "บุคคลทั่วไป เล่น PC 30 นาที เสียกี่บบาท", "service_fee", (("70 บาท",), ("1 session",)), (), False),
    ("public-permission", "th", "บุคคลทั่วไปเล่น PC ได้ไหม", "reservation", (("บุคคลทั่วไป",),), ("70 บาท",), False),
    ("polite-not-ps5", "th", "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า Counter-Strike 2 เล่นได้ที่โซนไหน", "games", (("Counter-Strike 2",), ("PC Zone",)), ("ไม่พบเกม", "PlayStation"), False),
    ("spatial-duplicate", "th", "PUBG: BATTLEGROUNDS เล่นได้ทที่ไหน", "games", (("PUBG",), ("PC",)), ("09:00",), False),
    ("vr-duration", "th", "VR Zone รอบละกีน่าที", "reservation", (("30",), ("60",), ("นาที",)), (), False),
    ("game-detail", "th", "ช่วยตอบจาข้อมูลที่ยืนยันได้หน่อย: Counter-Strike 2 คือเกมอะไน", "games", (("Counter-Strike 2",), ("ฝ่ายบุก",), ("ระเบิด",)), ("ยังไม่พบข้อมูล",), False),
    ("detail-two-edits", "th", "EA Sports FC 24 คือเดมอะร", "games", (("EA Sports FC 24",), ("ฟุตบอล",), ("ทำประตู",)), (), False),
    ("booking-limit", "en", "How many sessioons can one booking include", "reservation", (("maximum",), ("3 sessions",)), ("Booking steps:",), False),
    ("tuesday-afternoon", "en", "What are the afteronon opening hours on Tuesday", "schedule", (("Tuesday",), ("13:00-16:00",)), ("09:00-12:00",), False),
    ("friday-maintenance", "en", "Is Friday afteronon open", "schedule", (("maintenance",), ("13:00-16:00",)), (), False),
    ("offer-ood", "en", "Do you offer vernight accommodation? Please use verified information", "no_answer", (("could not find verified",),), ("Verified equipment", "Gaming Monitor"), False),
    ("offer-hardware", "en", "Do you offer headsets", "equipment", (("headset",),), (), False),
    ("member-count", "en", "How many memberss are there", "overview", (("25",), ("Members: 7",), ("Club",), ("13",)), (), False),
    ("member-role-scope", "en", "Who is the president", "clarification", (("university",), ("club",)), (), False),
    ("member-two-tasks", "en", "How many memberss are there, and who is the president", "multi_question", (("25",), ("university",), ("club",)), (), False),
    ("person-operation", "th", "นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร", "overview", (("กมลวรรณ",), ("กรรมการ",)), (), False),
    ("unknown-person", "th", "นายทดสอบบุคคลสมมุติ ตำแหน่งอะไร", "overview", (("ยังไม่", "ไม่พบ"),), ("กมลวรรณ",), False),
    ("compound-price-unclear-action", "th", "PC 2 ชั่วโมง บุคคลทั่วไป ราคาเท่าไหร่ แล้วของยังไง", "multi_question", (("140 บาท",), ("จอง",), ("หมายถึง",)), (), False),
    ("unresolved-reference", "th", "อันนี้จอได้มั้ย", "clarification", (("อุปกรณ์", "บริการ"),), ("สามารถจองได้",), False),
    ("unknown-minimum-age", "en", "What is the minimum sge requrement to enter the VALORANT competition", "competition_rules", (("could not find a verified",),), ("18 years", "16 years"), False),
    ("team-size-two-typos", "en", "Counter-Strike 2 rule teaam size", "competition_rules", (("5",), ("players",)), (), False),
    ("ambiguous-procedure", "en", "What do the CS2 tornament rules say about in-march procedure", "competition_rules", (("Which competition procedure",), ("before",), ("during",), ("after",)), ("Step-by-step competition procedure",), False),
    ("pay-play-clarification", "en", "How to pay Ring Fit Adventure", "clarification", (("playing", "play"), ("service fee", "pay")), (), False),
    ("technical-pause-comparison", "en", "How do CS2 and VALORANT technical pause rules differ?", "competition_rules", (("Counter-Strike 2",), ("VALORANT",), ("two times",), ("10 minutes",), ("disconnection",), ("not communicate", "may not communicate")), ("Tactical Timeout", "60 seconds"), False),
    ("tactical-pause", "en", "VALORANT tactical timeout rules", "competition_rules", (("2",), ("60 seconds",), ("Overtime",)), ("hardware malfunction",), False),
    ("emergency-pause", "en", "VALORANT emergency pause rules", "competition_rules", (("1",), ("10 minutes",), ("substitute",)), ("60 seconds",), False),
)

class IntegratedImprovementTests(unittest.TestCase):
    def test_translation_conditions_and_hashes(self):
        sources=source_records()
        text=approved_localization(sources['competition_rules_valorant_psu_phuket_2026_s09_c01'],'text')
        self.assertIn('indestructible',text)
        self.assertNotIn('in destructible areas',text)
        self.assertIn('must not pass through',text)
        forfeiture=approved_localization(sources['competition_rules_tekken8_psu_esports_s05_c01'],'text')
        self.assertIn('forfeit',forfeiture)
        self.assertNotIn('disqualification',forfeiture)
        self.assertIn('5v5',approved_localization(sources['game_detail_league_of_legends'],'genre'))
        changed={**sources['game_detail_league_of_legends'],'genre':'changed source after release'}
        self.assertIsNone(approved_localization(changed,'genre'))
        self.assertIsNone(approved_localization(sources['competition_rules_rov_blueket_2025_men_s08_c01'],'text'))

    def test_semantic_cases(self):
        for case in CASES:
            with self.subTest(case=case[0]):
                row=run_focused_case(case)
                self.assertTrue(row['passed'], row)

    def test_zone_needs_service_token(self):
        for text in ("เลย", "เลยอยากทราบว่า", "ช่วยบอกหน่อย", "this is complex"):
            with self.subTest(text=text):
                self.assertIsNone(_detect_zone(text))
        self.assertEqual(_detect_zone("cockpik ว่างไหม"),"Cockpit Zone")
        self.assertEqual(_detect_zone("PS5 มีอะไรบ้าง"),"PlayStation 5 Zone")

    def test_valid_operations_and_literals_survive(self):
        for query in ("เกม FINAL FANTASY XVI คืออะไร", "CS2 คือเกมแนวไหน", "How do you pay Moving Out 2",
                      "book PC 2 at 13:00 on 2026-10-01", "VR ราคา 30 บาท", "https://example.com/sessionn"):
            with self.subTest(query=query):
                self.assertEqual(recover_intent_cues(query),query)
        for case in CASES:
            corrected=recover_intent_cues(case[2])
            self.assertEqual(corrected,recover_intent_cues(corrected))

if __name__=='__main__':
    unittest.main()
