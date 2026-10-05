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
