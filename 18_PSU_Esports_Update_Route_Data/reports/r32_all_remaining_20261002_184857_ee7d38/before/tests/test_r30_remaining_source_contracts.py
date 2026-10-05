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

    def test_enumerated_roster_topic_keeps_the_count_without_action_collision(self):
        a=lookup_competition_reply('What do the CS2 tournament rules say about eligibility, roster, and registration?','en').answer
        for term in ['Open only to students','5 players','not permitted after']:self.assertIn(term,a)
    def test_available_general_periods_is_schedule_not_device_occupancy(self):
        for q in ['Which days and time periods are available for PC booking?','Which time periods are available for PC booking?']:
            with self.subTest(q=q):self.assertTrue(is_weekly_booking_window_query(q))
        for q in ['Which PC1 booking slots are available on Friday afternoon?','Which time periods is PC1 available today?']:
            with self.subTest(q=q):self.assertFalse(is_weekly_booking_window_query(q))
    def test_event_version_and_protest_language_are_rule_propositions(self):
        self.assertTrue(looks_like_competition_rule_query('รายการ CS2 ใช้เวอร์ชันเกมแบบไหน'))
        for q,l,term in [('CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย','th','ภาษาไทย'),('May CS2 protests be submitted in English or must they use Thai?','en','Thai')]:
            with self.subTest(q=q):self.assertIn(term,lookup_competition_reply(q,l).answer)
    def test_catalog_name_repeat_layout_review_requests_retype_without_mutation(self):
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce'
        for q in [',u Call of Duty: Modern Warfare III wss,',',u Delta Force wss,']:
            with self.subTest(q=q):
                d=guard.inspect(q);self.assertTrue(d.should_short_circuit)
                self.assertEqual(d.features.input_text,q)
                self.assertIn('keyboard_layout_mismatch',d.flags)
                self.assertFalse(d.composition_evidence['raw_input_mutated'])
    def test_catalog_name_layout_review_does_not_block_ordinary_prose(self):
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce'
        for q in ['Is Delta Force available?','Can u play Delta Force?','I like Delta Force, u?','มี Call of Duty: Modern Warfare III ไหม','Is Call of Duty: Modern Warfare III available?','Can I play Delta Force?','Can I pllay Delta Force?']:
            with self.subTest(q=q):self.assertNotIn('keyboard_layout_mismatch',guard.inspect(q).flags)

    def test_event_duration_and_venue_preserve_one_literal_source_clause(self):
        for q,l,terms in [('CS2 แข่งกี่วันและแข่งที่ไหน','th',['1 วัน','PSU Esports Studio']),('How many days does the CS2 tournament last and where is it held?','en',['one day','PSU Esports Studio'])]:
            with self.subTest(q=q):
                a=lookup_competition_reply(q,l)
                for term in terms:self.assertIn(term,a.answer)
                self.assertIn('event_duration_venue',a.concepts)
                self.assertTrue(any(row['id'].endswith('s08_c01') for row in a.rows))
        from app.pipeline.competition_detail import CONCEPTS
        import re
        concept=next(x for x in CONCEPTS if x.name=='event_duration_venue')
        for q in ['Under CS2 tournament rules, may players leave in the last round?','CS2 แข่งแล้วตั้งค่าปุ่มยิงอยู่ที่ไหน','How many days can a CS2 player pause a tournament?']:
            with self.subTest(q=q):self.assertIsNone(re.search(concept.question,q,re.I))
