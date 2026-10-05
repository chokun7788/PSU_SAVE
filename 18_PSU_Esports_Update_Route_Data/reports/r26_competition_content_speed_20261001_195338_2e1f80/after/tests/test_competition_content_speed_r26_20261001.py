"""Content completeness and bounded route optimization, source-backed."""
import os
import unittest
from unittest.mock import patch

from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.competition_fast_route import exact_competition_intent
from app.pipeline.competition_presentation import build_penalty_types
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.retrieval import load_curated_rows, competition_hits_cover_intent


class CompetitionContentSpeed(unittest.TestCase):
    def setUp(self):
        env=patch.dict(os.environ,{'PSU_BILINGUAL_EN_ENABLED':'1','PSU_SEMANTIC_RETRIEVAL':'0'})
        env.start();self.addCleanup(env.stop)

    def answer(self,q,locale='th',llm=False):
        return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)

    def test_registered_game_and_facet_determine_intent(self):
        for q in ('สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ','สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ'):
            with self.subTest(q=q):
                with patch('app.pipeline.engine.refine_route_with_semantic_evidence',side_effect=AssertionError('unnecessary semantic route call')),patch('app.pipeline.engine.resolve_universal_intent',side_effect=AssertionError('unnecessary intent review')):
                    result=self.answer(q,llm=True)
                self.assertTrue(result.validation.ok)
                self.assertEqual(result.route.category,'competition_rules')
                self.assertTrue(any(t.decision=='skipped_exact_competition_facet' for t in result.trace))
                self.assertTrue(any(t.stage=='competition_source_grounding' for t in result.trace))

    def test_ambiguous_and_nonrule_questions_do_not_take_fast_route(self):
        for q in ('CS2','มีเกม CS2 ไหม','CS2 กดปุ่มอะไร','RoV จองยังไง','กติกาใช้ผู้เล่นกี่คน','กติกา CS2 และ VALORANT มีผู้เล่นกี่คน','กติกา Minecraft มีผู้เล่นกี่คน','กติกา CS2 มีอะไรบ้าง'):
            with self.subTest(q=q):self.assertIsNone(exact_competition_intent(q))

    def test_routing_does_not_grant_source_coverage(self):
        for locale,q in (('th','กติกา Tekken 8 อายุขั้นต่ำเท่าไร'),('en','What is the Tekken 8 tournament minimum age requirement?')):
            with self.subTest(locale=locale):
                result=self.answer(q,locale)
                self.assertIn('no_answer',result.mode)
                self.assertNotIn('18 ปี',result.answer)

    def test_all_thai_penalty_types_and_conditions(self):
        result=self.answer('กติกา VALORANT มีบทลงโทษประเภทไหนบ้าง')
        for term in ('Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit'):
            self.assertEqual(result.answer.count(term),1)
        for term in ('ระบุเจตนาไม่ได้','เจตนาใช้ช่องโหว่','ความผิดครั้งแรก','ความผิดซ้ำ','ล็อกผล'):
            self.assertIn(term,result.answer)
        self.assertEqual({h['id'].rsplit('_s',1)[-1] for h in result.hits},{f'{i:02d}_c01' for i in range(11,16)})
        self.assertNotIn('ประเภทบทลงโทษในเกม',result.answer.splitlines()[0])

    def test_age_requires_an_age_value_and_unit_not_rule_number_or_update_date(self):
        row={'id':'source_fixture','category':'competition_rules','section_title':'คุณสมบัติผู้สมัคร','text':''}
        for text in ('1. อายุขั้นต่ำ','อายุขั้นต่ำ Update 2026','ผู้เล่นต้องยอมรับกติกา'):
            self.assertFalse(competition_hits_cover_intent('กติกา Tekken 8 อายุขั้นต่ำเท่าไร',[dict(row,text=text)]))
        self.assertTrue(competition_hits_cover_intent('กติกา Tekken 8 อายุขั้นต่ำเท่าไร',[dict(row,text='ผู้สมัครต้องมีอายุอย่างน้อย 18 ปี')]))

    def test_incomplete_penalty_type_series_cannot_be_completed_by_guess(self):
        rows=[r for r in load_curated_rows() if 'valorant_psu_phuket_2026' in str(r.get('id','')) and not r.get('_canonical_projection')]
        with patch('app.pipeline.retrieval.load_curated_rows',return_value=[r for r in rows if not r['id'].endswith('_s15_c01')]):
            self.assertIsNone(build_penalty_types('VALORANT บทลงโทษมีประเภทไหนบ้าง',rows))

    def test_specific_violation_does_not_get_generic_penalty_types(self):
        rows=[r for r in load_curated_rows() if 'valorant_psu_phuket_2026' in str(r.get('id',''))]
        for q in ('VALORANT ใช้ช่องโหว่มีบทลงโทษอะไรบ้าง','VALORANT โกงมีบทลงโทษประเภทไหนบ้าง'):
            self.assertIsNone(build_penalty_types(q,rows))

    def test_missing_pause_proposition_has_no_answer_mode(self):
        for locale,q in (('th','VALORANT technical pause ได้กี่นาที'),('en','How long is a VALORANT technical pause?')):
            with self.subTest(locale=locale):
                result=self.answer(q,locale)
                self.assertIn('no_answer',result.mode)
                self.assertTrue(result.validation.ok)
                self.assertNotIn('60',result.answer)
                self.assertTrue(result.hits)

    def test_tournament_typo_uses_edit_distance_only_with_registered_target(self):
        for variant in ('tournamment','tournment','touranment'):
            q=f'What is the Tekken 8 {variant} format?'
            self.assertIn('tournament',recover_intent_cues(q))
            result=self.answer(q,'en')
            self.assertEqual(result.route.category,'competition_rules')
            self.assertIn('FT2',result.answer)
        for q in ('What is the tournamment format?','Tekken 8 equipment information','Minecraft tournamment format','CS2 tournament format'):
            self.assertEqual(recover_intent_cues(q),q)


if __name__=='__main__':unittest.main()
