"""Confirmed facts and boundaries of the 2026-10-08 user answers."""
import hashlib,json,unittest
from pathlib import Path
from app.pipeline.user_service_facts import answer_user_service_facts,load_facts,PATH

class UserServiceFactsTests(unittest.TestCase):
    def test_original_source_binding(self):
        raw=PATH.parents[1]/'sources/user_service_answers_20261008.json'
        facts=load_facts()
        self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(),facts['raw_sha256'])
        items={i['number']:i for i in json.loads(raw.read_text(encoding='utf-8'))['items']}
        self.assertEqual(50,len(items));self.assertEqual(18,len(facts['claims']))
        for claim in facts['claims'].values():
            for number in claim['source_items']:
                self.assertEqual('user_confirmed',items[number]['status'])
        self.assertEqual([45,46],facts['pending_boundary']['items'])

    def test_separate_tournament_rental_and_unknown_policies(self):
        for q in ['กฎการแข่งขัน VALORANT เอาคีย์บอร์ดตัวเองมาได้ไหม',
                  'Can I bring my own keyboard to the CS2 tournament?',
                  'Where is the RoV competition venue?',
                  'Nintendo Switch rental for four people',
                  'ขอเหมาอุปกรณ์พร้อมที่นั่งพัก',
                  'What maps are there in VALORANT?',
                  'Where is the 65-inch TV located?',
                  'Where is the Xbox studio in Bangkok?']:
            with self.subTest(question=q):self.assertIsNone(answer_user_service_facts(q,'en'))

    def test_no_implication_of_refund(self):
        r=answer_user_service_facts('เปลี่ยนเวลาจองแล้วได้เงินคืนไหม')
        metadata=r['trace'][0].metadata
        self.assertIn('refund_conditions',metadata['missing_fields'])
        self.assertEqual('answered_partial',metadata['outcome'])

    def test_unanswered_conditions_do_not_become_permission(self):
        for q,field in [('ติดตั้งเกมเองได้ไหม','game_installation_permission'),
                        ('มีบัญชี Steam ให้ยืมไหม','game_account_policy'),
                        ('โอนเกินทำยังไง','overpayment_resolution'),
                        ('โอนขาดต้องจ่ายเพิ่มไหม','underpayment_resolution'),
                        ('เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองไหม','minor_guardian_policy'),
                        ('เอาจอยตัวเองมาได้ไหม','personal_controller_permission'),
                        ('ที่นั่งคือจำนวนคนเล่นพร้อมกันหรือในห้อง','seat_capacity_definition')]:
            with self.subTest(question=q):
                r=answer_user_service_facts(q)
                meta=r['trace'][0].metadata
                self.assertIn(field,meta['missing_fields'])
                self.assertEqual([],meta['claim_ids'])
                self.assertEqual('no_answer',meta['outcome'])

    def test_no_claim_of_immediate_walk_in_or_free_parking(self):
        for q,field in [('walk in เล่นได้ทันทีไหม','immediate_walk_in_slot'),
                        ('Is parking free?','parking_fee')]:
            r=answer_user_service_facts(q,'en')
            self.assertIn(field,r['trace'][0].metadata['missing_fields'])

    def test_claims_have_both_languages_and_preserved_conditions(self):
        facts=load_facts()
        for key,c in facts['claims'].items():
            with self.subTest(claim=key):
                self.assertTrue(c['answers']['th']);self.assertTrue(c['answers']['en'])
        self.assertIn('note',facts['claims']['combined_transfer']['answers']['en'])
        self.assertIn('named',facts['claims']['player_identity']['answers']['en'])
        self.assertIn('or passport',facts['claims']['checkin_documents']['answers']['en'])
        self.assertEqual('agent_translation_from_user_confirmed_thai',facts['english_status'])

    def test_late_arrival_uses_recorded_rule_and_marks_exception_missing(self):
        r=answer_user_service_facts('ไปสายสิบห้านาทียังเล่นได้ไหม')
        self.assertEqual(['rule_checkin_late'],r['trace'][0].metadata['recorded_rule_ids'])
        self.assertIn('late_grace_exception',r['trace'][0].metadata['missing_fields'])
        self.assertEqual('answered_partial',r['trace'][0].metadata['outcome'])
        self.assertIn('ยกเลิก',r['answer'])
        self.assertEqual('recorded_booking_rule',r['hits'][1]['metadata']['source_type'])

    def test_english_inflections_preserve_fault_and_update_intents(self):
        for q,field in [('How is lost time compensated if a machine crashes while playing?','technical_fault_compensation'),
                        ('Does my service time start counting while the game updates?','update_time_charging')]:
            with self.subTest(question=q):
                r=answer_user_service_facts(q,'en')
                self.assertIn(field,r['trace'][0].metadata['missing_fields'])

    def test_fault_and_closure_keep_known_refund_exception(self):
        for locale,q in [('th','เครื่องค้างระหว่างเล่น เวลาที่เสียไปคิดยังไง'),
                         ('en','How is lost time compensated if a machine crashes?'),
                         ('th','ศูนย์ปิดพิเศษหลังจองแล้วทำยังไง'),
                         ('en','How is my booking handled if the studio closes unexpectedly?')]:
            with self.subTest(question=q):
                r=answer_user_service_facts(q,locale)
                self.assertEqual(['rule_refund_policy'],r['trace'][0].metadata['recorded_rule_ids'])
                self.assertEqual('answered_partial',r['trace'][0].metadata['outcome'])
                self.assertIn('refund' if locale=='en' else 'คืนเงิน',r['answer'])
