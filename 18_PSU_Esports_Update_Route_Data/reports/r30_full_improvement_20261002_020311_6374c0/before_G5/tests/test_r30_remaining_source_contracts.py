import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.competition_targets import resolve_competition_targets,looks_like_competition_rule_query,competition_query_for_target
from app.pipeline.protected_intents import is_weekly_booking_window_query
class R30RemainingSourceTests(unittest.TestCase):
    def test_client_multi_proposition_binds_one_source_before_split(self):
        q='CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม'
        self.assertTrue(looks_like_competition_rule_query(q))
        a=lookup_competition_reply(q,'th').answer
        self.assertIn('Steam',a);self.assertIn('ห้ามใช้การดัดแปลง',a)
        self.assertNotIn('ส่งเสียงดัง',a)
    def test_closed_registration_does_not_answer_roster_count(self):
        for q,l,term in [('CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ','th','หลังจากปิดรับสมัคร'),('CS2 registration is closed; can we add a teammate to the roster?','en','not permitted after')]:
            with self.subTest(locale=l):
                a=lookup_competition_reply(q,l).answer
                self.assertIn(term,a);self.assertNotIn('5 players',a);self.assertNotIn('ผู้เล่น 5 คน',a)
    def test_implicit_skin_permission_is_not_a_catalog_request(self):
        a=lookup_competition_reply('RoV ใช้สกินพิเศษได้หรือเปล่า','th').answer
        self.assertIn('ห้ามใช้สกินนอกจากสกิน Default',a)
        self.assertFalse(looks_like_competition_rule_query('RoV มีสกินอะไรบ้าง'))
    def test_bare_franchise_respects_explicit_other_edition(self):
        self.assertEqual(resolve_competition_targets('เทคเคนแต่ละเกมแข่งกี่รอบ').targets[0].game_id,'tekken8')
        for q in ['Tekken 7 tournament rules','เทคเคนภาค 7 กฎแข่ง','Tekken VII tournament rules','Tekken v7 tournament rules','Tekken version VII tournament rules']:
            with self.subTest(q=q):self.assertNotEqual(resolve_competition_targets(q).status,'exact')
        a=lookup_competition_reply('เทคเคนแต่ละเกมแข่งกี่รอบ','th').answer
        self.assertIn('จำนวนรอบต่อเกม (Round): 3',a)
        self.assertIn('Tekken 8',a.splitlines()[0])
        compared='เปรียบเทียบกฎ CS2 กับเทคเคน'
        self.assertEqual(len(resolve_competition_targets(compared).targets),2)
        focused=competition_query_for_target(compared,'cs2')
        self.assertEqual(resolve_competition_targets(focused).targets[0].game_id,'cs2')
        self.assertEqual(len(resolve_competition_targets(focused).targets),1)
    def test_generic_maintenance_policy_does_not_need_live_station_data(self):
        self.assertTrue(is_weekly_booking_window_query('วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง'))
        for q in ['PC1 ว่างไหมวันศุกร์ช่วงบ่าย','วันนี้บ่าย3 PC1 ว่างไหม','Is PC1 free on Friday afternoon?','PC1 จองได้ช่วงไหนที่ว่างวันศุกร์ช่วงบ่าย','Which PC1 booking slots are available on Friday afternoon?']:
            with self.subTest(q=q):self.assertFalse(is_weekly_booking_window_query(q))
