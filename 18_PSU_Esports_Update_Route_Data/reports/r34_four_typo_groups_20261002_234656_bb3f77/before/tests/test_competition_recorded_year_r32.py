import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply, _recorded_year_guard

class RecordedEditionGuardTests(unittest.TestCase):
    def test_mismatch_both_languages(self):
        for q,l in [('CS2 tournament 2027 eligibility and roster','en'),('กติกา RoV ปี 2026 จำนวนผู้เล่นต่อทีม','th'),('VALORANT tournament 2025 rules','en'),('กติกา CS2 ปี 2025 และ 2026 คุณสมบัติ','th')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l)
                self.assertEqual(x.outcome,'no_answer');self.assertFalse(x.rows)
                self.assertIn('requested_rulebook_year_not_in_source',x.reasons)
    def test_matching_editions_keep_verified_clauses(self):
        for q,l in [('CS2 tournament 2026 eligibility and roster','en'),('กติกา RoV ปี 2025 จำนวนผู้เล่นต่อทีม','th')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'answer');self.assertTrue(x.rows)
    def test_numbers_and_undated_source_not_guessed(self):
        for q in ['CS2 rules 16000 money 1.2027', 'CS2 rule section 2027.1', 'CS2 rules for 2026']:
            self.assertIsNone(_recorded_year_guard(q,'en','competition_rules_cs2_psu_phuket_2026'))
        self.assertIsNone(_recorded_year_guard('Tekken 8 rules 2027','en','competition_rules_tekken8_psu_esports'))

    def test_year_abstention_survives_answer_contract(self):
        from app.pipeline.answer_contracts import validate_answer_contract
        from app.pipeline.schemas import PipelineRoute
        for q,l in [('CS2 tournament 2027 eligibility and roster','en'),('กติกา RoV ปี 2026 จำนวนผู้เล่นต่อทีม','th')]:
            with self.subTest(q=q):
                a=lookup_competition_reply(q,l)
                route=PipelineRoute('competition_rules','competition_rules_lookup',0.97,'fact','medium','test')
                from app.pipeline.question_frame import build_question_frame
                x=validate_answer_contract(q,a.answer,route,frame=build_question_frame(q,route),hits=[],mode='pipeline:competition_rule_detail_no_answer')
                self.assertTrue(x.ok,x.errors);self.assertIn('no_answer',x.answer_types)

    def test_birth_year_and_four_digit_fee_are_not_editions(self):
        for q in ['CS2 tournament entry fee 2027 baht', 'CS2 born in 2007 eligibility', 'กติกา CS2 เกิดปี 2007 สมัครได้ไหม', 'กติกา CS2 ค่าสมัคร 2027 บาท']:
            with self.subTest(q=q):
                self.assertIsNone(_recorded_year_guard(q,'en','competition_rules_cs2_psu_phuket_2026'))
        self.assertIsNotNone(_recorded_year_guard('CS2 rules 2027: born in 2007 eligible?','en','competition_rules_cs2_psu_phuket_2026'))
