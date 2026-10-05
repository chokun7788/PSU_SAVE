import unittest
from unittest.mock import patch
from app.pipeline.closed_query_improvements import answer_closed_query_improvement, _recorded_catalog_gap
from app.pipeline.bilingual_english import _weekday_from_query, _answer_booking_intent
from app.pipeline.schemas import EntityBundle
from app.rules.matcher import RuleMatcher

class UsableTaskFrameTests(unittest.TestCase):
    def test_thai_compound_contact_retains_both_source_records(self):
        category, result=answer_closed_query_improvement('ขออีเมลและเบอร์โทรติดต่อศูนย์หน่อย','th')
        self.assertEqual(category,'contact')
        for value in ('psuesportspkt@gmail.com','7627 6004','7627 6045'):self.assertIn(value,result.answer)
        self.assertEqual({source for hit in result.hits for source in hit['metadata']['source_ids']},{'curated_contact_email','curated_contact_phone'})
    def test_thus_is_not_a_plural_weekday_abbreviation(self):
        self.assertIsNone(_weekday_from_query('Could you help with thus: What are the studio rules',EntityBundle()))
    def test_full_weekday_plurals_and_abbreviations(self):
        self.assertEqual(_weekday_from_query('Open on Sundays?',EntityBundle()),6)
        self.assertEqual(_weekday_from_query('Open Thu?',EntityBundle()),3)
    def test_booking_transfer_does_not_answer_bank_account(self):
        result=_answer_booking_intent('What is the studio policy for transfer booking',RuleMatcher.default())
        self.assertIn('cannot be transferred',result.answer)
        self.assertNotIn('795-',result.answer)
    def test_bank_transfer_still_uses_payment_source(self):
        result=_answer_booking_intent('How do I pay by bank transfer for a booking',RuleMatcher.default())
        self.assertIn('795-276244-1',result.answer)
    def test_catalog_gap_has_source_and_preserves_title(self):
        result=_recorded_catalog_gap('ที่ศูนย์มี Minecraft ไหม','th')
        self.assertIn('Minecraft',result.answer)
        self.assertTrue(result.hits)
        self.assertTrue(result.evidence['absence_only'])
    def test_catalog_update_disables_historical_absence_guard(self):
        with patch('app.runtime.fast_answer._verified_game_catalog',return_value=({'name':'Minecraft'},)):
            self.assertIsNone(_recorded_catalog_gap('ที่ศูนย์มี Minecraft ไหม','th'))
    def test_general_game_description_is_not_studio_absence(self):
        self.assertIsNone(_recorded_catalog_gap('Minecraft เป็นเกมแนวไหน','th'))
        self.assertIsNone(_recorded_catalog_gap('How do I play Minecraft at the studio?','en'))
