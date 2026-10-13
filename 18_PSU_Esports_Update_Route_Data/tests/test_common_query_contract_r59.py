"""Behavior guards for schema interpretation; no models or owner DB writes."""
import unittest
from app.knowledge.common.query_contract import resolve_fields,broad_request,live_request
from app.knowledge.common.answer import named,title,CommonAnswerer
from app.knowledge.common.planner import checked_plan,plan_rejection,semantic_guard

class SchemaQueryTests(unittest.TestCase):
    def test_quantity_scope(self):
        for kind,key in [('zone','room_seats'),('resource','capacity_persons'),('service','capacity_max'),('game_mode','players_max')]:
            with self.subTest(kind=kind):self.assertIn(key,resolve_fields('How many people can use it?',{kind})[0])
        self.assertEqual(set(resolve_fields('เล่นขั้นต่ำกี่คนและสูงสุดกี่คน',{'game_mode'})[0]),{'players_min','players_max'})
    def test_duration_scopes(self):
        fields=resolve_fields('เวลาเล่นกับเวลาที่กันช่องจองกี่นาที',{'service'})[0]
        self.assertEqual(set(fields),{'session_minutes','occupancy_minutes'})
        self.assertEqual(resolve_fields('ราคาและได้กี่นาที',{'rate'})[0],['amount_minor','duration_minutes'])
    def test_broad_count_and_negation(self):
        for q in ['football','small','install','ข้อมูลครบไหม','all seats','ไม่ต้องตอบทั้งหมด','not all information']:
            with self.subTest(q=q):self.assertFalse(broad_request(q))
        self.assertTrue(broad_request('Show all information'))
        self.assertTrue(broad_request('ข้อมูลทั้งหมด'))
    def test_zero_price_is_not_live(self):
        self.assertFalse(live_request('free to play'))
        self.assertFalse(live_request('เล่นฟรี'))
        self.assertTrue(live_request('PC available now'))
        self.assertFalse(live_request('ระหว่างเล่นกดปุ่มอะไร'))
        self.assertTrue(live_request('ระหว่าง 15:00-16:00 เครื่องว่างไหม'))
    def test_repeat_long_name_and_numbers(self):
        names={'short':['Cloud Garden'],'long':['Cloud Garden Plus']}
        self.assertEqual(named('Cloud Ggarden Plus controls',names)[0],['long'])
        self.assertEqual(named('Cloud Ggarden controls',names)[0],['short'])
        self.assertEqual(named('Game 88',{'a':['Game 8']})[0],[])
        self.assertEqual(named('Game 88',{'a':['Game 8'],'b':['Game 88']})[0],['b'])
    def test_shape_and_semantic_guard(self):
        records={'a':{'kind':'audience','fields':{}}};ids=['a']
        for fields in [[[]],[2],['fake']]:
            self.assertEqual(plan_rejection({'requested_fields':fields,'all_fields':False,'platform':None},ids,records),'invalid_fields')
        self.assertIsNone(checked_plan({'requested_fields':['required_proofs'],'all_fields':False,'platform':'a'},ids,records))
        proposal=checked_plan({'requested_fields':['name','eligibility','required_proofs'],'all_fields':False,'platform':None},ids,records)
        clean,why=semantic_guard('What proof is required?',proposal,ids,records)
        self.assertEqual(clean['requested_fields'],['required_proofs'])
        self.assertEqual(why['removed_unrequested_fields'],['name','eligibility'])
    def test_opening_status_not_periods(self):
        self.assertEqual(set(resolve_fields('What is the opening status on that date and why?',{'closure'})[0]),{'state','reason'})
        self.assertEqual(set(resolve_fields('Opening hours and maintenance periods',{'schedule'})[0]),{'open_periods','maintenance_periods'})
    def test_reference_label_and_runtime_coverage(self):
        self.assertEqual(title({'record_id':'internal','fields':{'value':{'status':'known','value':'https://example.invalid/help'}}},'en'),'https://example.invalid/help')
        self.assertEqual(title({'record_id':'internal','fields':{},'aliases':{'en':['Public label']}},'en'),'Public label')
        class Store:
            def still_current(self,snap):return True
        result=CommonAnswerer(Store()).finish({'active':'test'},0,'partial',[],{'requested_fields':['capacity_persons']},[])
        self.assertFalse(result.validation.ok)
        self.assertEqual(result.decision_artifact['response_type'],'partial_answer')
if __name__=='__main__':unittest.main()
