import unittest
from unittest.mock import patch
from tools.competition_content_grader_r27 import atomic_clauses, literal_source_matches, rescore
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.competition_detail import lookup_competition_detail

class AtomicGraderTests(unittest.TestCase):
    def test_short_flattened_equipment_is_substantive(self):
        source={'s':'Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format'}
        self.assertEqual(len(literal_source_matches('Answer: PlayStation 5 console used',source)),1)

    def test_penalty_without_modal_is_substantive(self):
        source={'s':'Warning for the first offense with minimal impact'}
        self.assertTrue(literal_source_matches('Answer: Warning for the first offense with minimal impact',source))

    def test_heading_citation_partial_clause_do_not_pass(self):
        source={'s':'Competition Rules and Format for CS2\nPlayers must not communicate unless authorized.'}
        for answer in ('Competition Rules and Format for CS2 Source: s','Players must not communicate','Players must communicate unless authorized.'):
            with self.subTest(answer=answer):self.assertFalse(literal_source_matches(answer,source))

    def test_wrong_time_unit_does_not_pass(self):
        source={'s':'Protests must be filed within 15 minutes after the match.'}
        self.assertFalse(literal_source_matches('Protests must be filed within 15 seconds after the match.',source))

    def test_cardinal_number_at_start_is_not_an_outline_label(self):
        source={'s':'5 players must attend the match.'}
        self.assertFalse(literal_source_matches('6 players must attend the match.',source))

    def test_score_is_a_real_word_not_scope_typo(self):
        q='What score is recorded for a forfeited map in the VALORANT tournament?'
        self.assertEqual(recover_intent_cues(q),q)
        result=answer_question_pipeline_debug(q,locale='en',experimental_allow_llm=False)
        self.assertIn('13-0',result.answer.splitlines()[0])

    def test_thai_duplicated_task_vowel_is_consumed_once(self):
        q='กติกกา CS2 เวลาต่อรอบ 1:55 คืออะไร'
        recovered= recover_intent_cues(q)
        self.assertEqual(recovered,'กติกา CS2 เวลาต่อรอบ 1:55 คืออะไร')
        self.assertNotIn('กติกาา',recovered)

    def test_settings_include_stage_and_advantage(self):
        for locale,q in [('th','กติกา Tekken 8 การตั้งค่าเกมเป็นอย่างไร'),('en','What are the Tekken 8 tournament in-game settings?')]:
            result=answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=False)
            self.assertIn('Stage: Random',result.answer)
            self.assertIn('Advantage: No advantage',result.answer)

    def test_detail_lookup_does_not_invent_missing_clause(self):
        from app.pipeline.retrieval import load_curated_rows
        rows=[r for r in load_curated_rows() if not str(r.get('id','')).endswith('_s58_c01')]
        with patch('app.pipeline.retrieval.load_curated_rows',return_value=rows):
            self.assertIsNone(lookup_competition_detail('กติกา CS2 ยื่นประท้วงภายในกี่นาที','th'))

    def test_detail_lookup_rejects_unknown_game_and_catalog(self):
        for q in ('กติกา Free Fire รายงานตัวเมื่อไร','มีเกม CS2 ไหม','กติกา CS2 กับ VALORANT ใช้คีย์บอร์ดอะไร'):
            self.assertIsNone(lookup_competition_detail(q,'th'))
        self.assertIsNone(lookup_competition_detail('What rules apply to the CS2 competition?','en'))

    def test_recovery_preserves_real_scope_numbers_names_and_negation(self):
        for q in ('What scope does the CS2 rulebook cover?','Under CS2 tournament rules, do not bring notes?','กติกา CS2 ไม่ใช่ 15 วินาที ใช่ไหม'):
            self.assertEqual(recover_intent_cues(q),q)

    def test_anchored_two_part_typo_preserves_name_and_numbers(self):
        q='Under CS2 tournamment ruls, can a coach file a proest within 15 minutes?'
        from app.core.intent_cue_recovery import recover_intent_cue_sequence
        corrected,changes=recover_intent_cue_sequence(q)
        self.assertIn('CS2',corrected);self.assertIn('15 minutes',corrected)
        self.assertIn('protest',corrected);self.assertIn('tournament rules',corrected)
        self.assertLessEqual(len(changes),3)

    def test_combined_eligibility_roster_registration_preserves_each_topic(self):
        result=answer_question_pipeline_debug('What do the CS2 tournament rules say about eligibility, roster, and registration?',locale='en',experimental_allow_llm=False)
        for clause in ('Open only to students','5 players','not permitted after'):
            self.assertIn(clause,result.answer)

    def test_eligibility_cannot_replace_age_threshold(self):
        self.assertIsNone(lookup_competition_detail('What are CS2 tournament eligibility and minimum age requirements?','en'))

    def test_source_grader_does_not_erase_route_or_timeout_failure(self):
        row={'id':'x','locale':'th','source_ids':['s'],'answer':'ผู้เล่นต้องใช้ภาษาไทยเท่านั้น','passed':False,'failures':['answer_without_substantive_source_content','route_mismatch','latency_failure']}
        records,summary=rescore([row],{'s':{'text':row['answer']}},lambda *_:None)
        self.assertEqual(records[0]['remaining_failures'],['route_mismatch','latency_failure'])
        self.assertEqual(summary['source_grade_passed'],0)

    def test_missing_game_clarifies_without_models(self):
        for locale,q in [('th','กติกาแข่งขันมีอะไรบ้าง'),('en','What are the tournament rules?')]:
            with self.subTest(locale=locale):
                with patch('app.pipeline.engine.refine_route_with_semantic_evidence',side_effect=AssertionError('unneeded semantic model')),patch('app.pipeline.engine.resolve_universal_intent',side_effect=AssertionError('unneeded intent model')):
                    result=answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=True,experimental_rag_fallback=True)
                self.assertIn('clarification',result.mode)
                self.assertEqual(result.route.category,'competition_rules')
                self.assertFalse(result.hits)

    def test_entry_timing_measures_before_split(self):
        result=answer_question_pipeline_debug('กติกา CS2 ทีมละกี่คน',experimental_allow_llm=False,experimental_rag_fallback=True)
        timing={t.decision:t.metadata for t in result.trace if t.stage=='timing'}
        for stage in ('locale_resolution','intent_cue_preflight','canonical_preflight'):
            self.assertIn(stage,timing)
            self.assertGreaterEqual(timing[stage]['elapsed_ms'],0)
        self.assertIn('entry_to_split_ms',timing['split_multi_question'])
