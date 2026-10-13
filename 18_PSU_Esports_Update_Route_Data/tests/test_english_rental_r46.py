"""English paraphrases must preserve source fields and clause-local price scopes."""
import unittest
from app.pipeline.zone_rental import resolve_zone_rental_plan as resolve,build_zone_rental_answer as build

START='PC rental price for external organizations full day'
def history(status='client_acknowledged'):
    return [{'role':'assistant','delivery_status':status,'request_plan':resolve(START)}]

class EnglishRentalTests(unittest.TestCase):
    def rates(self,p):return {r['id']:r['value'] for r in build(p,locale='en')['metadata']['returned_rates']}
    def test_whole_day_selects_full_day(self):
        self.assertEqual(self.rates(resolve('PC whole-day rental price external')),{'pc:external:full_day':4000})
    def test_misspelled_service_in_long_sentence(self):
        self.assertEqual(self.rates(resolve('cockpitt full-day rental cost for external organizations')),{'cockpit:external:full_day':2000})
    def test_comparisons_preserve_each_clause(self):
        for separator,prefix in [('versus',''),('with','Compare ')]:
            p=resolve(prefix+'PC full-day rental external organizations '+separator+' VR half-day rental internal organizations')
            self.assertEqual(self.rates(p),{'pc:external:full_day':4000,'vr:internal:half_day':1500})
            self.assertEqual(p['unresolved_targets'],[])
    def test_followup_fields_do_not_repeat_prices(self):
        for q,field in [('How many people can it accommodate?','capacity'),('How long is a full day?','duration_definition'),('How can I reserve it?','booking'),('What is the booking procedure?','booking'),('When do these prices take effect?','effective_date')]:
            p=resolve(q,history());self.assertEqual(p['asks'],[field],q)
            self.assertEqual(self.rates(p),{},q)
            self.assertEqual(p['targets'],['pc']);self.assertEqual(p['groups'],['external'])
    def test_unacknowledged_context_not_used(self):
        self.assertIsNone(resolve('How can I reserve it?',history('prepared')))
    def test_generic_exclusion_applied_before_defaults(self):
        p=resolve('Rental prices except VR')
        self.assertNotIn('vr',p['targets']);self.assertEqual(len(self.rates(p)),20)
    def test_per_machine_is_field_not_unknown_product(self):
        p=resolve('PC full-day rental price per machine')
        self.assertEqual(p['unresolved_targets'],[])
        self.assertEqual(build(p)['metadata']['missing_fields'],['per_unit'])
    def test_unknown_numeric_product_not_fuzzy_repaired(self):
        p=resolve('PS55 full-day rental cost for external organizations')
        self.assertEqual(self.rates(p),{});self.assertEqual(p['unresolved_targets'],['ps55'])
    def test_topic_shift_not_inherited_as_rental(self):
        for q in ('Competition rules for CS2','What games are available on PC?','PC opening hours'):
            self.assertIsNone(resolve(q,history()),q)

if __name__=='__main__':unittest.main()
