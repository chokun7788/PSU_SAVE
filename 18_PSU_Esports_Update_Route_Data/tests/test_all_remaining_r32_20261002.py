import unittest,re
from unittest.mock import patch
from datetime import date
from app.pipeline.competition_detail import lookup_competition_detail
from app.pipeline.competition_request_contract import validate_requested_clauses
from app.pipeline.retrieval import hit_from_curated
from app.core.intent_cue_recovery import recover_intent_cues
from app.booking.live_status import is_live_booking_question,_unavailable
from app.pipeline.engine import answer_question_pipeline_debug

class AllRemainingR32Tests(unittest.TestCase):
    def test_vacancy_typo_frames_use_live_handler_even_offline(self):
        for q in ['พรุ่งนี้ 13:00 Nintendo Switch วางหรือเปล่า','PC1 10:00 วางมั้ย','PC1 10:00 วางหรือไม่','PC1 10:00 วางรึเปล่า']:
            with self.subTest(q=q),patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'known fixture offline')):
                self.assertTrue(is_live_booking_question(q))
                r=answer_question_pipeline_debug(q,locale='th',experimental_allow_llm=False)
                self.assertTrue(r.mode.startswith('pipeline:live_booking_status_unavailable'))
                self.assertNotIn('calendar_schedule',r.mode)
    def test_non_vacancy_frames_preserve_word_and_numbers(self):
        for q in ['PC1 วางเครื่องตรงไหน','PC1 10:00 วางเครื่องบนโต๊ะ','PC1 10:00 ว่าต้องจ่ายเท่าไหร่','PC1 10:00 ไม่ว่างไหม']:
            with self.subTest(q=q):self.assertEqual(recover_intent_cues(q),q)
    def test_facet_recovery_preserves_target_and_quantities(self):
        q='กติกา RoV จำนวผู้เล่นต่อทีม และข้อ 4.2.1'
        recovered=recover_intent_cues(q)
        self.assertIn('จำนวนผู้เล่น',recovered);self.assertIn('RoV',recovered);self.assertIn('4.2.1',recovered)
        for negative in ['RoV จะเป็นผู้เล่นต่อทีม','กติกา CS3 จำนวนผู้เล่น','CS2 game settings ไม่ใช่กติกา','ค่าบริการจำนวนผู้เล่น RoV']:
            with self.subTest(q=negative):self.assertEqual(recover_intent_cues(negative),negative)
    def test_compound_content_rejects_every_individual_missing_clause(self):
        for q,ids in [('CS2 competition eligibility, roster and registration',{'s17','s18','s12'}),('CS2 competition in-game settings',{'s23','s24','s25','s26','s27'}),('CS2 competition equipment rules',{'s41','s42','s43'})]:
            for locale in ['th','en']:
                with self.subTest(q=q,locale=locale):
                    a=lookup_competition_detail(q,locale);self.assertEqual(a.outcome,'answer')
                    seen={re.search(r'_(s\d+)_',r['id'])[1] for r in a.rows};self.assertTrue(ids<=seen)
                    hits=[hit_from_curated(r) for r in a.rows]
                    self.assertFalse(validate_requested_clauses(q,a.answer,hits,locale,'pipeline:competition_rule_detail_source'))
                    for row in a.rows:
                        from app.knowledge.localization import approved_localization
                        from app.pipeline.competition_presentation import source_clause_lines
                        text=approved_localization(row,'text') if locale=='en' else row['text']
                        for clause in source_clause_lines(text):
                            bad=a.answer.replace(clause,'[omitted]')
                            self.assertTrue(validate_requested_clauses(q,bad,hits,locale,'pipeline:competition_rule_detail_source'),row['id'])
    def test_rov_team_size_distinguishes_match_from_registered_roster(self):
        for locale in ['th','en']:
            a=lookup_competition_detail('RoV competition rules: team size',locale)
            self.assertIn('5v5',a.answer);self.assertIn('s06_c01',a.rows[0]['id'])
            self.assertIn('registered roster' if locale=='en' else 'รายชื่อที่ลงทะเบียน',a.answer)
            self.assertFalse(validate_requested_clauses('RoV competition rules: team size',a.answer,[hit_from_curated(r) for r in a.rows],locale,'pipeline:competition_rule_detail_source'))
    def test_heading_alone_cannot_substantiate_settings(self):
        a=lookup_competition_detail('CS2 tournament in-game settings','th')
        errors=validate_requested_clauses('CS2 tournament in-game settings','2. การตั้งค่าในเกม',[hit_from_curated(r) for r in a.rows],'th','pipeline:competition_rule_detail_source')
        self.assertGreaterEqual(len(errors),5)
    def test_location_interrogative_and_real_word_ambiguity(self):
        r=answer_question_pipeline_debug('Wherw can you pay VALORANT',locale='en',experimental_allow_llm=False)
        self.assertIn('clarification',r.mode);self.assertNotIn('70 THB',r.answer)
        self.assertEqual(recover_intent_cues('Where can I pay for my booking?'),'Where can I pay for my booking?')
    def test_game_zone_location_typo(self):
        r=answer_question_pipeline_debug('Pokémon Champions อยู่โซซนไหน',locale='th',experimental_allow_llm=False)
        self.assertIn('Nintendo Switch',r.answer)

    def test_recovery_preserves_valid_threshold_identity_and_punctuation(self):
        for q in ['กติกา RoV หยุดเกิน 10 นาทีกรรมการทำอย่างไร','กติกา Tekken 8 ใช้กับการแข่งขันไหน','Please check: I am preparing for a Counter Strike 2 match. What is the policy for the competition format? please.']:
            with self.subTest(q=q):self.assertEqual(recover_intent_cues(q),q)
