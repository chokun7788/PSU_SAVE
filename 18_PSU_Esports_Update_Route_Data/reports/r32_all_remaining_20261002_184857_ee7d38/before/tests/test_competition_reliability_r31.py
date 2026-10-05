import unittest
from app.pipeline.competition_targets import resolve_competition_targets,recover_competition_game_names
from app.pipeline.preprocess import preprocess_input
from app.pipeline.competition_detail import requested_detail_concepts
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.competition_request_contract import validate_requested_clauses
from app.pipeline.retrieval import hit_from_curated

class CompetitionReliabilityR31Tests(unittest.TestCase):
    def test_source_name_recovery_retains_raw_spans_and_full_title(self):
        for name in ['เคานน์เตอร์สไตรก์ 2','เคาน์เเตอร์สไตรก์ 2','เคาน์เตอร์สไรก์ 2','Counter strkie 2','Counter-Strikee 2','Couter Strike 2']:
            q=f'กติกา {name} เรื่องอุปกรณ์';pre=preprocess_input(q)
            with self.subTest(name=name):
                self.assertEqual(pre.raw_query,q)
                self.assertIn('Counter-Strike 2',pre.clean_query)
                self.assertIn('counter-strike 2',pre.normalized_query)
                self.assertNotIn('counter-strikeส',pre.normalized_query)
                self.assertEqual(resolve_competition_targets(pre.clean_query).targets[0].game_id,'cs2')
                for item in pre.name_recoveries:self.assertEqual(item['original'],item['input_text'][item['start']:item['end']])

    def test_supported_long_names_recover_unique_deletion_repeat_and_transposition(self):
        for q,game in [('Valorantt tournament rules','valorant'),('valoratn tournament rules','valorant'),('Valrant tournament rules','valorant'),('Arena of Valro tournament rules','rov'),('Tekekn 8 tournament rules','tekken8'),('กฎ เทคเคนน 8 อุปกรณ์','tekken8')]:
            with self.subTest(q=q):self.assertEqual(resolve_competition_targets(q).targets[0].game_id,game)

    def test_recovery_preserves_editions_short_ids_and_non_rule_prose(self):
        for q in ['CS3 tournament rules','rv tournament rules','Tekken 7 tournament rules','Tekekn 7 tournament rules','Tekken VII tournament rules','Counter strkie 3 tournament rules','What is the VALIANT competition?']:
            with self.subTest(q=q):self.assertEqual(recover_competition_game_names(q)[0],q)
        for q in ['Can I play Valorantt?','PC1 ว่างตอน 10:00 ไหม','กติกา Free Fire เรื่อง pause','กติกา Dota 2 เรื่อง pause']:
            with self.subTest(q=q):self.assertEqual(recover_competition_game_names(q)[0],q)

    def test_exact_names_are_not_rewritten_and_comparisons_keep_both_games(self):
        for q in ['กฎ เคาน์เตอร์สไตรก์ 2 เรื่องอุปกรณ์','VALORANT tournament rules','Tekken 8 tournament rules']:
            with self.subTest(q=q):self.assertFalse(recover_competition_game_names(q)[1])
        r=resolve_competition_targets('Compare Counter strkie 2 and Valorantt tournament rules')
        self.assertEqual({t.game_id for t in r.targets},{'cs2','valorant'})

    def test_venue_clause_is_selected_without_a_rule_keyword(self):
        for q,l in [('สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน','th'),('What is the location of the CS2 tournament?','en')]:
            with self.subTest(q=q):
                a=lookup_competition_reply(q,l);self.assertIn('PSU Esports Studio',a.answer)
                self.assertTrue(any(r['id'].endswith('s08_c01') for r in a.rows))

    def test_requested_event_year_is_not_guessed_from_an_older_rulebook(self):
        a=lookup_competition_reply('Where is the CS2 2027 tournament held?','en')
        self.assertEqual(a.outcome,'no_answer');self.assertIn('event_year_not_covered',a.reasons)

    def test_timeout_context_does_not_select_round_time(self):
        q='CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง'
        self.assertEqual([c.name for c in requested_detail_concepts(q,'cs2')],['tactical_timeout'])
        a=lookup_competition_reply(q,'th')
        for term in ['4 ครั้ง','30 วินาที','Freeze time']:self.assertIn(term,a.answer)
        self.assertNotIn('1:55',a.answer)

    def test_independently_asked_round_time_and_technical_pause_remain(self):
        self.assertIn('round_time',[c.name for c in requested_detail_concepts('CS2 round time and timeout duration?','cs2')])
        self.assertEqual([c.name for c in requested_detail_concepts('CS2 technical timeout rules?','cs2')],['technical_pause'])
        self.assertNotIn('tactical_timeout',[c.name for c in requested_detail_concepts('VALORANT timeout rules?','valorant')])

    def test_contract_rejects_correct_source_with_missing_quantities_or_condition(self):
        q='CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง';a=lookup_competition_reply(q,'th');hits=[hit_from_curated(r) for r in a.rows]
        self.assertFalse(validate_requested_clauses(q,a.answer,hits,'th','pipeline:competition_rule_detail_source'))
        for bad in [a.answer.replace('4 ครั้ง',''),a.answer.replace('30 วินาที',''),a.answer.replace('ใช้ได้ในช่วง Freeze time','')]:
            with self.subTest(answer=bad):self.assertIn('competition_requested_clause_incomplete:tactical_timeout',validate_requested_clauses(q,bad,hits,'th','pipeline:competition_rule_detail_source'))

    def test_contract_rejects_a_round_time_answer_even_with_cs2_source(self):
        q='CS2 timeout during freeze time quota?';a=lookup_competition_reply('CS2 round time rules?','en')
        errors=validate_requested_clauses(q,a.answer,[hit_from_curated(r) for r in a.rows],'en','pipeline:competition_rule_detail_source')
        self.assertIn('competition_requested_clause_source_missing:tactical_timeout',errors)

    def test_contract_does_not_accept_an_unsupported_claim_without_hits(self):
        errors=validate_requested_clauses('CS2 timeout rules?','4 requests of 30 seconds',[],'en','pipeline:competition_rule_detail_source')
        self.assertIn('competition_requested_clause_source_missing:tactical_timeout',errors)

    def test_comparison_focus_removes_the_original_recovered_other_name(self):
        from app.pipeline.competition_targets import competition_query_for_target
        q='Compare Counter strkie 2 and Valorantt tournament rules'
        focused=competition_query_for_target(q,'cs2')
        self.assertEqual([t.game_id for t in resolve_competition_targets(focused).targets],['cs2'])

    def test_venue_is_not_a_control_location_or_pause_duration(self):
        for q in ['CS2 แข่งแล้วตั้งค่าปุ่มยิงอยู่ที่ไหน','What is the location of the fire button in the CS2 tournament?','How many days can a CS2 player pause a tournament?']:
            with self.subTest(q=q):self.assertNotIn('event_duration_venue',[c.name for c in requested_detail_concepts(q,'cs2')])

    def test_coordinated_pause_and_timeout_requires_both_complete_clauses(self):
        for q,l in [('กติกา CS2 เรื่อง pause และ timeout','th'),('CS2 tournament pauses and timeouts','en'),('CS2 timeout and pause rules','en')]:
            with self.subTest(q=q):
                concepts={c.name for c in requested_detail_concepts(q,'cs2')}
                self.assertEqual(concepts,{'technical_pause','tactical_timeout'})
                a=lookup_competition_reply(q,l);hits=[hit_from_curated(r) for r in a.rows]
                self.assertFalse(validate_requested_clauses(q,a.answer,hits,l,'pipeline:competition_rule_detail_source'))
                timeout_only=lookup_competition_reply('CS2 timeout rules?',l)
                errors=validate_requested_clauses(q,timeout_only.answer,[hit_from_curated(r) for r in timeout_only.rows],l,'pipeline:competition_rule_detail_source')
                self.assertTrue(any(e.endswith(':technical_pause') for e in errors))

    def test_detail_answer_mode_is_classified_without_bypassing_content_or_abstention(self):
        from tools.eval_contract_v2 import answer_outcome
        self.assertEqual(answer_outcome('pipeline:competition_rule_detail_source','Source clause','competition_rules'),'answer')
        self.assertEqual(answer_outcome('pipeline:competition_rule_detail_source','','competition_rules'),'unknown')
        self.assertEqual(answer_outcome('pipeline:competition_rule_detail_source','Missing clause','no_answer'),'no_answer')

    def test_thai_technical_timeout_is_not_a_tactical_timeout_without_a_rules_keyword(self):
        from app.pipeline.competition_targets import looks_like_competition_rule_query
        q='CS2 เวลานอกทางเทคนิคขอได้กี่ครั้ง'
        self.assertTrue(looks_like_competition_rule_query(q))
        self.assertEqual([c.name for c in requested_detail_concepts(q,'cs2')],['technical_pause'])
        a=lookup_competition_reply(q,'th')
        self.assertIn('2 ครั้ง',a.answer);self.assertIn('10 นาที',a.answer)
        self.assertNotIn('4 ครั้ง',a.answer);self.assertNotIn('30 วินาที',a.answer)
