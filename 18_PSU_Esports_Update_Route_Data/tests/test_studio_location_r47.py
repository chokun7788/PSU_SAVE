"""Address evidence must answer the requested subject, not just pass transport."""
import json,os,unittest
from pathlib import Path
from app.pipeline.bilingual_english import _answer_studio_location,requires_english_intent_review
from app.pipeline.question_frame import build_question_frame
from app.pipeline.schemas import PipelineRoute,UniversalIntent
from app.rules.matcher import RuleMatcher

class StudioLocationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matcher=RuleMatcher.default()
        path=Path(__file__).resolve().parents[1]/'data/rules/contact_rules.jsonl'
        cls.fact=next(json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if json.loads(line)['id']=='rule_contact_location')
    def test_paraphrases_use_exact_existing_address_and_source(self):
        for q in ('Where is the venue?','Where can I find the studio?','Where is the centre?','What is the venue address?'):
            r=_answer_studio_location(q,self.matcher)
            self.assertIn(self.fact['answer_en'],r.answer);self.assertIn(self.fact['source_url'],r.answer)
            self.assertEqual(r.route.category,'contact')
            self.assertEqual({i for h in r.hits for i in h['metadata']['source_ids']},set(self.fact['source_ids']))
    def test_unknown_studio_cannot_get_psu_address(self):
        r=_answer_studio_location('Where is the Xbox studio in Bangkok?',self.matcher)
        self.assertEqual(r.route.answer_type,'clarification');self.assertNotIn('80 Moo 1',r.answer)
    def test_other_location_subjects_are_not_studio_addresses(self):
        for q in ('Where is the RoV competition venue?','Where is the studio manager?','Where is the TV in the studio?','Where can I play Beat Saber in the studio?','What are the studio opening hours?'):
            self.assertIsNone(_answer_studio_location(q,self.matcher),q)
    def test_address_is_not_invented_travel_directions(self):
        r=_answer_studio_location('How do I get to the venue?',self.matcher)
        self.assertIn(self.fact['answer_en'],r.answer);self.assertIn('travel directions are not provided',r.answer)
    def test_verified_location_does_not_require_llm_review(self):
        self.assertFalse(requires_english_intent_review(_answer_studio_location('Where is the venue?',self.matcher)))
    def test_contact_frame_not_overwritten_by_generic_equipment_location(self):
        route=PipelineRoute('contact','detail',.9,'fact','low','contact source')
        intent=UniversalIntent(domain='contact',operation='detail',confidence=.9)
        frame=build_question_frame('ศูนย์อยู่ที่ไหน',route,intent)
        self.assertEqual(frame.domain,'contact');self.assertEqual(frame.operation,'contact_lookup')
        self.assertIn('fact',frame.expected_answer_types);self.assertNotIn('equipment',frame.expected_answer_types)
    def test_equipment_location_keeps_equipment_frame(self):
        route=PipelineRoute('equipment','equipment_item_lookup',.95,'fact','low','equipment source')
        frame=build_question_frame('จอทีวีอยู่ที่ไหน',route)
        self.assertEqual(frame.domain,'equipment');self.assertEqual(frame.operation,'equipment_lookup')
    def test_thai_paraphrases_use_same_curated_fact(self):
        from app.pipeline.closed_query_improvements import _studio_location_th
        for q in ('ศูนย์อยู่ที่ไหน','ขอที่อยู่ศูนย์','ที่ตั้ง PSU Esports Studio อยู่ที่ไหน'):
            r=_studio_location_th(q,'th');self.assertIsNotNone(r,q)
            self.assertIn(self.fact['answer_th'],r.answer)
            self.assertEqual(r.evidence['source_ids'],self.fact['source_ids'])
    def test_thai_other_location_not_assigned_psu_address(self):
        from app.pipeline.closed_query_improvements import _studio_location_th
        r=_studio_location_th('ศูนย์ Xbox กรุงเทพอยู่ที่ไหน','th')
        self.assertIn('clarification',r.mode);self.assertNotIn('80 หมู่ 1',r.answer)
        self.assertIsNone(_studio_location_th('จอทีวีของศูนย์อยู่ที่ไหน','th'))

if __name__=='__main__':unittest.main()
