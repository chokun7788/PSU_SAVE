"""Scoped rental requests must not apply one child's conditions to another."""
import copy,unittest
from app.pipeline.zone_rental import resolve_zone_rental_plan as resolve,build_zone_rental_answer as build,valid_zone_rental_plan as valid

def history(q):
    p=resolve(q)
    return [{'role':'assistant','delivery_status':'client_acknowledged','request_plan':p}]

class RentalScopeTests(unittest.TestCase):
    def rates(self,p):return {r['id']:r['value'] for r in build(p)['metadata']['returned_rates']}

    def test_separate_children_different_periods_and_groups(self):
        p=resolve('ราคาเหมา PC เต็มวันหน่วยงานภายนอก และ VR ครึ่งวันหน่วยงานภายใน')
        self.assertEqual(self.rates(p),{'pc:external:full_day':4000,'vr:internal:half_day':1500})
        answer=build(p)['answer']
        pc=answer.split('**PC Zone**')[1]
        self.assertIn('หน่วยงานภายนอก: เต็มวัน 4,000',pc)
        self.assertNotIn('หน่วยงานภายใน:',pc)

    def test_shared_tail_group_and_different_periods(self):
        p=resolve('PC rental full day and VR rental half day for external organizations')
        self.assertEqual(self.rates(p),{'pc:external:full_day':4000,'vr:external:half_day':3000})

    def test_same_zone_can_have_two_scopes(self):
        p=resolve('PC rental full day external organizations and PC rental half day internal organizations')
        self.assertEqual(self.rates(p),{'pc:external:full_day':4000,'pc:internal:half_day':1000})

    def test_group_and_period_negations(self):
        self.assertEqual(resolve('PC rental price excluding internal organizations')['groups'],['external'])
        self.assertEqual(resolve('ราคาเหมา VR ไม่เอาครึ่งวัน เอาเต็มวัน')['periods'],['full_day'])

    def test_filtered_all_followup_retains_dimensions(self):
        p=resolve('ทั้งหมด ยกเว้น VR',history('ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน'))
        self.assertNotIn('vr',p['targets']);self.assertEqual(len(p['targets']),5)
        self.assertEqual(p['groups'],['external']);self.assertEqual(p['periods'],['half_day'])

    def test_select_child_keeps_its_own_dimensions(self):
        p=resolve('PC',history('ราคาเหมา PC เต็มวันหน่วยงานภายนอก และ VR ครึ่งวันหน่วยงานภายใน'))
        self.assertEqual(self.rates(p),{'pc:external:full_day':4000})

    def test_field_then_price_restores_price_intent(self):
        p=resolve('รวมอะไรบ้าง',history('ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน'))
        h=[{'role':'assistant','delivery_status':'client_acknowledged','request_plan':p}]
        r=resolve('ราคาเท่าไหร่',h)
        self.assertEqual(r['asks'],['rates']);self.assertEqual(self.rates(r),{'pc:external:half_day':2000})

    def test_unknown_menu_selection_and_numbered_product(self):
        for q,h in [('Xbox',history('ขอราคาเหมา')),('ราคาเหมา PS55 เต็มวัน',[])]:
            p=resolve(q,h);self.assertEqual(p['targets'],[])
            self.assertEqual(self.rates(p),{});self.assertIn('unresolved_targets',build(p)['metadata']['missing_fields'])

    def test_custom_all_zones_is_not_full_bundle_price(self):
        p=resolve('Whole studio rental price except PC')
        self.assertEqual(self.rates(p),{})
        self.assertEqual(build(p)['metadata']['missing_fields'],['custom_package'])

    def test_booking_followup_does_not_apply_play_booking_cap(self):
        p=resolve('จองยังไง',history('ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน'))
        r=build(p);self.assertEqual(r['metadata']['missing_fields'],['booking'])
        self.assertNotIn('3 sessions',r['answer']);self.assertNotIn('3 เซส',r['answer'])

    def test_unknown_dimensions_in_child_rejected(self):
        p=resolve('PC rental full day and VR rental half day external')
        p['scoped_requests'][0]['groups']=['student']
        self.assertFalse(valid(p));self.assertIsNone(build(p))

    def test_overlarge_or_malformed_child_list_rejected(self):
        p=resolve('PC rental full day and VR rental half day external')
        for children in ([None],[{'targets':[],'groups':['external'],'periods':['full_day']}],[{'targets':[['pc']],'groups':['external'],'periods':['full_day']}],p['scoped_requests']*4):
            other=copy.deepcopy(p);other['scoped_requests']=children;self.assertFalse(valid(other))

    def test_all_prices_expands_compound_to_catalog(self):
        p=resolve('all rental rates',history('PC rental full day external organizations and VR rental half day internal organizations'))
        self.assertEqual(len(self.rates(p)),24)
        self.assertNotIn('scoped_requests',p)

    def test_excluding_every_period_requests_clarification(self):
        p=resolve('PC rental price not half day and not full day')
        self.assertEqual(self.rates(p),{})
        self.assertIn('scope_clarification',build(p)['metadata']['missing_fields'])

    def test_cancelled_price_task_is_not_resent(self):
        self.assertIsNone(resolve('ไม่เอาราคาเหมาแล้ว',history('ราคาเหมา PC')))

    def test_both_groups_is_not_an_unknown_equipment_name(self):
        p=resolve('both groups',history('PC rental price external half day'))
        self.assertEqual(p['unresolved_targets'],[])
        self.assertEqual(self.rates(p),{'pc:external:half_day':2000,'pc:internal:half_day':1000})

    def test_noun_style_topic_shifts_are_not_menu_choices(self):
        h=history('PC rental full day external organizations and VR rental half day internal organizations')
        for q in ('Competition rules for CS2','VALORANT controls','PC opening hours','PC มีเกมอะไรบ้าง'):
            self.assertIsNone(resolve(q,h),q)

if __name__=='__main__':unittest.main()
