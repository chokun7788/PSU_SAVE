import unittest
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.core.locale import resolve_locale
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.router import _looks_like_competition_rule_query

class R30CompetitionIngressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guard = RuntimeInputQualityGuard.from_environment()
    def test_low_score_mapping_is_not_a_locale_decision(self):
        for q in ['ปุ่ม', 'วีอาราค่าเทาไหร', 'วันนี้เปืดั้ย', 'เพลย์ห้าคิกตังเท่าไหรอะ']:
            with self.subTest(q=q):
                quality=self.guard.inspect(q)
                self.assertNotIn('keyboard_layout_mismatch',quality.flags)
                self.assertIsNone(quality.locale_layout_direction)
                self.assertEqual(resolve_locale(q,keyboard_layout_direction=quality.locale_layout_direction).effective,'th')
    def test_true_mapping_still_has_a_direction(self):
        quality=self.guard.inspect('ฟสสนไำก')
        self.assertIn('keyboard_layout_mismatch',quality.flags)
        self.assertEqual(quality.locale_layout_direction,'english_intended_thai_active')
    def test_team_starting_players_bind_to_source_count(self):
        result=lookup_competition_reply('CS2 ต้องส่งผู้เล่นหลักกี่คน','th')
        self.assertIsNotNone(result)
        self.assertIn('ผู้เล่น 5 คน',result.answer)
    def test_roster_request_beats_generic_on_site(self):
        result=lookup_competition_reply('CS2 เลทแล้วเปลี่ยนตัวตอนหน้างานได้ไหม','th')
        self.assertIsNotNone(result)
        self.assertIn('ไม่มีการเปลี่ยนแปลงสมาชิก',result.answer)
        self.assertNotIn('โน้ต',result.answer)
    def test_display_settings_in_both_languages(self):
        for q,l,expected in [('วาโลต้องปิดเลือดกับศพไหม','th','ปิด'),('Do I need to turn off blood and bodies in VALORANT?','en','OFF')]:
            with self.subTest(locale=l):
                result=lookup_competition_reply(q,l)
                self.assertIsNotNone(result)
                self.assertIn(expected,result.answer)
    def test_arrival_does_not_invent_a_separate_deadline(self):
        result=lookup_competition_reply('What if a RoV team arrives late by over 15 minutes?','en')
        self.assertIsNotNone(result)
        self.assertIn('15 minutes',result.answer)
        self.assertIn('separate arrival deadline',result.answer)
    def test_game_character_changes_do_not_imply_roster_rules(self):
        for q in ['cs2 เปลี่ยนตัวละครยังไง','cs2 เปลี่ยนสกินได้ไหม']:
            with self.subTest(q=q):self.assertFalse(_looks_like_competition_rule_query(q))
        self.assertTrue(_looks_like_competition_rule_query('กฎแข่ง cs2 เปลี่ยนสกินได้ไหม'))
