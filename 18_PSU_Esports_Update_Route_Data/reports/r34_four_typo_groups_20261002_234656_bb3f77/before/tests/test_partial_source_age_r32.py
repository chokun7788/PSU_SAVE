import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.competition_request_contract import validate_requested_clauses

class PartialSourceAgeTests(unittest.TestCase):
    def test_supported_eligibility_kept_when_age_is_missing(self):
        for q,l,known,note in [('กติกา CS2 คุณสมบัติและอายุขั้นต่ำคืออะไร','th','เปิดรับเฉพาะ','อายุขั้นต่ำ'),('What are CS2 tournament eligibility and minimum age requirements?','en','General eligibility','minimum-age')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'partial');self.assertIn(known,x.answer);self.assertIn(note,x.answer)
                self.assertTrue(any(r['id'].endswith('s17_c01') for r in x.rows))
                errors=validate_requested_clauses(q,'Missing age only',[{'id':r['id']} for r in x.rows],l,'pipeline:competition_rule_detail_partial_source')
                self.assertTrue(errors,'Must reject an age-gap-only response even with the correct eligibility source')
    def test_age_only_does_not_imply_general_eligibility(self):
        for q,l in [('กติกา CS2 อายุขั้นต่ำเท่าไร','th'),('What is the CS2 tournament minimum age?','en')]:
            x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'no_answer');self.assertFalse(x.rows)

    def test_typo_recovery_preserves_thai_conjunction(self):
        from app.pipeline.competition_facet_recovery import recover_facet_cue
        for q in ['กติกา CS2 คุณสมบัตและอายุขั้นต่ำคืออะไร','กติกา CS2 คุณสมบัตกับอายุขั้นต่ำคืออะไร']:
            with self.subTest(q=q):
                x=recover_facet_cue(q);self.assertIsNotNone(x)
                recovered=x[0];self.assertIn('คุณสมบัติ',recovered)
                self.assertIn('และ' if 'และ' in q else 'กับ',recovered)
                self.assertEqual(lookup_competition_reply(recovered,'th').outcome,'partial')
