import unittest
from app.core.duration_alternatives import parse_duration_alternatives
from app.pipeline.closed_query_improvements import answer_closed_query_improvement
from app.pipeline.control_button_target import explicit_button_selection
class R30FinalTests(unittest.TestCase):
    def test_three_choices_and_shared_units(self):
        for q,v in [('PC 1 or 2 or 3 hours cost?',(60,120,180)),('PC 1 ชั่วโมงหรือ 2 หรือ 3 ชั่วโมงกี่บาท',(60,120,180)),('VR 30 minutes or 1 or 2 hours cost?',(30,60,120))]:
            with self.subTest(q=q):self.assertEqual(parse_duration_alternatives(q).minutes,v)
    def test_denied_affiliation_is_not_a_free_price(self):
        for q,l in [('ผมไม่ใช่นักศึกษา มอ PC 1 หรือ 2 ชั่วโมงกี่บาท','th'),('I am not a PSU student, PC for 1 or 2 hours cost?','en')]:
            with self.subTest(q=q):
                category,r=answer_closed_query_improvement(q,l)
                self.assertEqual(category,'clarification');self.assertNotIn('0 THB',r.answer);self.assertNotIn('0 บาท',r.answer)
    def test_broad_fee_table_uses_all_stored_packages(self):
        for q,l in [('ค่าเล่นแต่ละเครื่องมีอะไรบ้าง','th'),('อุปกรณ์แต่ละโซนราคาเท่าไหร่','th'),('How much does each service cost?','en')]:
            with self.subTest(q=q):
                category,r=answer_closed_query_improvement(q,l)
                self.assertEqual(category,'service_fee')
                for v in ['PC','PlayStation 5','Nintendo Switch','Cockpit','VR','2026-07-27']:self.assertIn(v,r.answer)
                self.assertNotIn('ยังไม่พบราคา',r.answer)
    def test_unknown_identifier_all_letter_prefixes(self):
        self.assertEqual(explicit_button_selection('What does the Z9 button do?',[]).rows,())
    def test_unknown_game_does_not_silently_drop_booking_target(self):
        category,r=answer_closed_query_improvement('What do I need to book to play Roblox?','en')
        self.assertEqual(category,'clarification');self.assertTrue(r.evidence['no_inferred_booking_service']);self.assertNotIn('Booking steps:',r.answer)
