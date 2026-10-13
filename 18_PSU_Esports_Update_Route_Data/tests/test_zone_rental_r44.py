"""Workbook-bound tariff and acknowledged dialogue oracles, separate from play fees."""
import copy,json,unittest,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
from app.pipeline.zone_rental import resolve_zone_rental_plan as resolve, build_zone_rental_answer as build, valid_zone_rental_plan as valid, load_zone_rental_data, TARGETS
from app.session.conversation_store import ConversationStore

ROOT=Path(__file__).resolve().parents[1]

class ZoneRentalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        with zipfile.ZipFile(ROOT/'data/sources/zone_rental_fees_20261006.xlsx') as z:
            shared=[''.join(t.text or '' for t in s.findall('.//m:t',ns)) for s in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
            cls.cells={}
            for c in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//m:sheetData/m:row/m:c',ns):
                v=c.findtext('m:v',default='',namespaces=ns)
                if v:cls.cells[c.attrib['r']]=shared[int(v)] if c.attrib.get('t')=='s' else v

    def test_all_24_rates_bound_to_original_cells(self):
        result=build(resolve('Show all rental rates'),'en')
        rows=result['metadata']['returned_rates']
        self.assertEqual(len(rows),24)
        columns={('external','full_day'):'B',('external','half_day'):'C',('internal','full_day'):'D',('internal','half_day'):'E'}
        for rate in rows:
            target,group,period=rate['id'].split(':')
            cell=f'{columns[group,period]}{TARGETS.index(target)+3}'
            self.assertEqual(rate['cell'],cell)
            self.assertEqual(rate['value'],int(self.cells[cell]))

    def test_capacity_and_equipment_from_original(self):
        data=load_zone_rental_data()
        for row in data['rows']:
            self.assertEqual(row['seats'],int(self.cells[f"F{row['source_row']}"]))
            self.assertEqual(row['equipment_th'],self.cells[f"G{row['source_row']}"].strip())
        pc=build(resolve('เหมา PC รองรับกี่คน มีอุปกรณ์อะไร'))
        self.assertIn('43 ที่นั่ง',pc['answer']);self.assertIn('PC 10 เครื่อง',pc['answer'])

    def test_package_is_not_sum_of_individual_zones(self):
        rates=build(resolve('ราคาเหมาทั้งศูนย์หน่วยงานภายนอกเต็มวัน'))['metadata']['returned_rates']
        self.assertEqual([(r['id'],r['value']) for r in rates],[('all_zones:external:full_day',12000)])

    def test_missing_hours_effective_dates_not_invented(self):
        d=load_zone_rental_data()
        self.assertIsNone(d['effective_from']);self.assertIsNone(d['effective_until'])
        self.assertEqual(d['period_hours'],{'half_day':None,'full_day':None})
        for q,field in [('เหมา PC กี่ชั่วโมง','duration_definition'),('ราคาเหมาเริ่มใช้เมื่อไร','effective_date')]:
            r=build(resolve(q));self.assertIn(field,r['metadata']['missing_fields'])
            self.assertEqual(r['metadata']['returned_rates'],[])

    def test_staff_amount_is_not_invented(self):
        r=build(resolve('เช่าโซน PC มีค่าเจ้าหน้าที่นอกเวลาเท่าไหร่'))
        self.assertIn('overtime',r['metadata']['missing_fields'])
        self.assertIn('All Zones',r['answer']);self.assertIn('ไม่ได้ระบุจำนวนเงิน',r['answer'])

    def test_english_contains_no_thai(self):
        r=build(resolve('Show all rental fees'),'en')
        self.assertFalse(any('\u0e00'<=ch<='\u0e7f' for ch in r['answer']))

    def test_unknown_target_is_not_all_zones(self):
        for q in ('ราคาเหมา Xbox เต็มวัน','Xbox rental price for a full day','Rental price for Xbox full day','Rental price for external organizations for Xbox'):
            p=resolve(q);self.assertEqual(p['targets'],[])
            self.assertTrue(p['unresolved_targets']);self.assertEqual(build(p)['metadata']['returned_rates'],[])

    def test_partial_unknown_keeps_known_and_missing(self):
        r=build(resolve('ราคาเหมา PC และ Xbox เต็มวัน'))
        self.assertEqual(len(r['metadata']['returned_rates']),2)
        self.assertEqual(r['metadata']['missing_fields'],['unresolved_targets'])
        self.assertEqual(r['metadata']['outcome'],'answered_partial')

    def test_fuzzy_target_without_alias_does_not_add_unknown(self):
        p=resolve('ราคาเหมา cockpik ครึ่งวัน')
        self.assertEqual(p['targets'],['cockpit']);self.assertEqual(p['unresolved_targets'],[])

    def test_individual_is_not_an_internal_organization(self):
        p=resolve('นักศึกษา PSU ราคาเหมา PC')
        self.assertEqual(p['groups'],['external','internal'])
        self.assertIn('eligibility',build(p)['metadata']['missing_fields'])

    def test_per_machine_is_not_zone_rate(self):
        p=resolve('ราคาเหมา PC1 เต็มวัน')
        self.assertEqual(p['targets'],['pc'])
        self.assertEqual(build(p)['metadata']['missing_fields'],['per_unit'])

    def test_half_full_hourly_are_separate(self):
        self.assertIsNone(resolve('PC hourly price for external users'))
        p=resolve('ราคาเหมา PC รายชั่วโมง')
        self.assertIn('hourly_rental',build(p)['metadata']['missing_fields'])

    def test_target_exclusions(self):
        self.assertNotIn('pc',resolve('Show all rental rates except PC')['targets'])
        self.assertEqual(resolve('เช่า PC เต็มวัน')['targets'],['pc'])

    def test_invalid_duplicate_or_missing_plan_rejected(self):
        p=resolve('ราคาเหมา PC')
        for key in ('targets','groups','periods','asks'):
            changed=copy.deepcopy(p);changed[key]+=changed[key][:1];self.assertFalse(valid(changed))
        p['targets']=[];self.assertFalse(valid(p));self.assertIsNone(build(p))

    def _completed(self,ack=True):
        store=ConversationStore();q='ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน'
        turn=store.begin('one','first',q,history=[]);r=build(turn['plan'])
        store.complete('one','first',turn['revision'],dict(ok=True,request_id='first',answer=r['answer'],route_category='service_fee',route_intent='zone_rental_fee',mode=r['mode']),plan=turn['plan'])
        if ack:store.acknowledge('one','first')
        return store

    def test_acknowledged_followup_retains_scope(self):
        s=self._completed();t=s.begin('one','next','VR',history=s.history('one'))
        self.assertEqual(t['plan']['targets'],['vr']);self.assertEqual(t['plan']['groups'],['external'])
        self.assertEqual(t['plan']['periods'],['half_day']);self.assertTrue(t['plan']['context_used'])

    def test_unacknowledged_and_other_session_cannot_inherit(self):
        s=self._completed(False)
        self.assertIsNone(resolve('VR',s.history('one')))
        self.assertIsNone(resolve('VR',s.history('two')))

    def test_rental_and_play_tasks_have_distinct_memory_keys(self):
        s=self._completed();keys=s.snapshot('one')['current_task_keys']
        self.assertEqual(keys,['zone_rental/zone_rental_fee'])
        t=s.begin('one','resume','กลับไปเรื่องราคาเหมาเมื่อกี้',history=s.history('one'))
        self.assertEqual(t['plan']['schema_type'],'zone_rental_v1');self.assertEqual(t['plan']['groups'],['external'])

    def test_topic_shifts_do_not_keep_rental(self):
        s=self._completed()
        for q in ('PC มีเกมอะไรบ้าง','PC รายชั่วโมงราคาเท่าไหร่','PC ว่างไหม','กฎการแข่งขัน CS2'):
            self.assertIsNone(resolve(q,s.history('one')))

    def test_venue_word_alone_is_not_a_rental_request(self):
        for q in ('Where is the venue?','What are the venue opening hours?'):
            self.assertIsNone(resolve(q))

if __name__=='__main__':unittest.main()
