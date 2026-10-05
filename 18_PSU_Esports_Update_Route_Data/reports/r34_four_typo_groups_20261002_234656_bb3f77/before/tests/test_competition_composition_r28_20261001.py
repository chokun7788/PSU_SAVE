import unittest
from unittest.mock import patch
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.core.intent_cue_recovery import recover_intent_cues

def answer(q,locale='th'):
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=False,experimental_rag_fallback=True)

class CompositionR28Tests(unittest.TestCase):
    def test_two_equipment_prohibitions_are_both_answered(self):
        result=answer('Under CS2 tournament rules, are macros allowed and may I install software?','en')
        self.assertIn('No scripts or macros',result.answer)
        self.assertIn('install',result.answer);self.assertIn('Do not install',result.answer)
        self.assertTrue(result.validation.ok)

    def test_regular_money_and_overtime_are_not_mutually_excluded(self):
        result=answer('กติกา CS2 เงินเริ่มต้นและเวลาระเบิดรอบปกติเท่าไร แล้วต่อเวลามีกี่รอบและเงินเริ่มต้นเท่าไร')
        for word in ('$800','$10,000','40 วินาที','6'):self.assertIn(word,result.answer)

    def test_only_overtime_cannot_borrow_regulation_money(self):
        result=answer('What is CS2 tournament overtime starting money?','en')
        self.assertIn('$10,000',result.answer);self.assertNotIn('$800',result.answer)

    def test_protest_language_and_procedure_preserve_both(self):
        result=answer('Under CS2 tournament rules, which language must protests use, who may file a protest and within how many minutes?','en')
        for term in ('Thai','15 minutes','captain','coach'):self.assertIn(term,result.answer)

    def test_fee_is_not_late_registration(self):
        for locale,q in [('th','กติกา CS2 ค่าสมัครกี่บาท'),('en','What is the CS2 tournament registration fee?')]:
            result=answer(q,locale)
            self.assertIn('no_answer',result.mode)
            self.assertNotIn('after the registration period',result.answer)
            self.assertFalse(result.hits)

    def test_supported_clause_is_kept_with_unknown_fee(self):
        result=answer('Under CS2 tournament rules, are scripts allowed and what is the registration fee?','en')
        self.assertIn('No scripts or macros',result.answer)
        self.assertIn('could not find verified registration-fee information',result.answer)
        self.assertIn('partial',result.mode)
        self.assertLess(result.answer.index('could not find'),result.answer.index('Source:'))

    def test_truncated_numbered_clause_does_not_borrow_other_penalties(self):
        for locale,q in [('th','กติกา RoV ข้อ 6.1.5.1 บทลงโทษเต็มว่าอะไร'),('en','What is the complete RoV tournament penalty clause 6.1.5.1?')]:
            result=answer(q,locale)
            self.assertIn('no_answer',result.mode);self.assertFalse(result.hits)
            self.assertIn('6.1.5.1',result.answer)
            self.assertNotIn('6.2.4.1',result.answer);self.assertNotIn('6.1.2.1',result.answer)

    def test_numbered_reference_must_be_exact(self):
        reply=lookup_competition_reply('กติกา RoV ข้อ 6.1.5.10 ว่าอะไร','th')
        self.assertEqual(reply.outcome,'no_answer')
        self.assertIn('explicit_clause_not_covered',reply.reasons)

    def test_complete_numbered_clause_keeps_resume_condition(self):
        reply=lookup_competition_reply('กติกา RoV ข้อ 4.3.1 ว่าอะไร','th')
        self.assertEqual(reply.outcome,'answer')
        for word in ('5 ครั้ง','1 นาที','Resume'):self.assertIn(word,reply.answer)

    def test_pause_conflict_is_visible_before_permission(self):
        for locale,q in [('th','กติกา Tekken 8 หยุดเกมได้ไหม'),('en','May I pause under Tekken 8 tournament rules?')]:
            result=answer(q,locale)
            self.assertIn('conflict',result.mode)
            self.assertIn('ขัดกัน' if locale=='th' else 'conflict',result.answer.splitlines()[0])
            self.assertGreaterEqual(len(result.hits),2)

    def test_future_explicit_age_source_is_not_treated_as_missing(self):
        row={'id':'competition_rules_cs2_psu_phuket_2026_s99_c01','text':'ผู้เข้าแข่งขันต้องมีอายุขั้นต่ำ 20 ปี','game':'Counter-Strike 2','tournament':'PSU Phuket CS2 2026 Tournament','source_url':'local://fixture'}
        with patch('app.pipeline.competition_source_gaps._rows',return_value=[row]):
            reply=lookup_competition_reply('กติกา CS2 อายุขั้นต่ำกี่ปี','th')
        self.assertEqual(reply.outcome,'answer');self.assertIn('20 ปี',reply.answer)

    def test_future_explicit_fee_source_is_read_without_guessing(self):
        row={'id':'competition_rules_cs2_psu_phuket_2026_s99_c01','text':'ค่าสมัครการแข่งขัน 250 บาทต่อทีม','game':'Counter-Strike 2','tournament':'PSU Phuket CS2 2026 Tournament','source_url':'local://fixture'}
        with patch('app.pipeline.competition_source_gaps._rows',return_value=[row]):
            reply=lookup_competition_reply('กติกา CS2 ค่าสมัครกี่บาท','th')
        self.assertEqual(reply.outcome,'answer');self.assertIn('250 บาทต่อทีม',reply.answer)

    def test_arrival_minutes_are_not_a_minimum_age(self):
        row={'id':'competition_rules_cs2_psu_phuket_2026_s99_c01','text':'Players must arrive at least 30 minutes early.','game':'Counter-Strike 2','source_url':'local://fixture'}
        with patch('app.pipeline.competition_source_gaps._rows',return_value=[row]), patch('app.pipeline.competition_source_gaps._text',return_value='Players must be at least 30 minutes early.'):
            reply=lookup_competition_reply('What is the CS2 tournament minimum age?','en')
        self.assertEqual(reply.outcome,'no_answer');self.assertNotIn('30',reply.answer)

    def test_recovery_preserves_meaning_and_protected_values(self):
        q='Under CS2 tournament rules, no macros, 1:55 round time and $800 in regulation?'
        self.assertEqual(recover_intent_cues(q),q)

    def test_final_decision_is_not_the_final_match(self):
        result=answer('Under CS2 tournament rules, whose decisions are final?','en')
        self.assertIn('Judgment authority',result.answer.splitlines()[0])
        self.assertNotIn('Semifinals',result.answer)

    def test_partial_reply_does_not_bypass_foreign_game_evidence(self):
        from app.pipeline.validator import validate_answer
        from app.pipeline.retrieval import load_curated_rows,hit_from_curated
        q='Under CS2 tournament rules, are scripts allowed and what is the registration fee?'
        result=answer(q,'en')
        foreign=next(r for r in load_curated_rows() if str(r.get('id','')).startswith('competition_rules_valorant_psu_phuket_2026_s01'))
        validation=validate_answer(q,result.answer,result.route,result.entities,hits=[hit_from_curated(foreign)],mode=result.mode)
        self.assertFalse(validation.ok)

    def test_dispute_resolution_is_not_display_resolution(self):
        result=answer('What do the CS2 tournament rules say about dispute resolution?','en')
        self.assertNotIn('brightness',result.answer.casefold())
        self.assertNotIn('crosshair',result.answer.casefold())
        self.assertTrue(result.validation.ok)
        self.assertTrue(any('_s58_' in str(h.get('id','')) for h in result.hits))
        for word in ('15 minutes','captain','coach'):self.assertIn(word,result.answer)

    def test_local_dispute_mask_preserves_separate_display_request(self):
        from app.pipeline.competition_detail import requested_detail_concepts
        names=[c.name for c in requested_detail_concepts('Under CS2 tournament rules, explain dispute resolution and how to change screen resolution.','cs2')]
        self.assertIn('custom_display',names)

    def test_english_pronouns_do_not_trigger_wrong_keyboard_rejection(self):
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce';guard.repeat_policy='warn_and_continue'
        for q in ('Under CS2 tournament rules, what personal equipment may I bring and who is responsible for its quality and readiness?', 'Could you help me? Under CS2 tournament rules, what personal equipment may I bring and who is responsible for its quality and readiness?', 'Under CS2 tournamment ruls, what personal equipment may I bring and who is responsible for its quality and readiness?'):
            self.assertFalse(guard.inspect(q).should_short_circuit,q)
        for q in ('g]jo','อยากถามว่า g]jo ได้ไหม'):
            self.assertTrue(guard.inspect(q).should_short_circuit,q)
