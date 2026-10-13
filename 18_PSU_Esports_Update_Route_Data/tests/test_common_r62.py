import unittest,os,copy,json,threading,urllib.request
from unittest.mock import patch
from http.server import ThreadingHTTPServer
from .test_common_content_r58 import CommonTests,record
from app.knowledge.common.answer import CommonAnswerer,try_common_answer
from app.knowledge.common.authority import filter_legacy_hits,scoped_names
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.owner_server import preview_answer,make_handler
from app.knowledge.common.budget import budget_request
from app.knowledge.common.name_candidates import recover,distance
from app.knowledge.common.query_contract import resolve_fields

class LogicTests(unittest.TestCase):
 def test_equipment_and_price_remain_separate_requested_topics(self):
  fields,_=resolve_fields('What kit is covered by the rental price?',{'rental_package'})
  self.assertIn('equipment_included',fields);self.assertIn('amount_minor',fields)
  fields,_=resolve_fields('which equipment is included?',{'rental_package'})
  self.assertIn('equipment_included',fields);self.assertNotIn('amount_minor',fields)
 def test_duration_does_not_become_price_duration(self):
  fields,_=resolve_fields('how long can I play?',{'service'})
  self.assertIn('session_minutes',fields);self.assertNotIn('duration_minutes',fields)
 def test_group_budget_does_not_claim_individual_arithmetic(self):
  r=record('rate','r');r['fields']['currency']['value']='THB';r['fields']['calculation_rule']['value']='linear';r['fields']['duration_minutes'].update(status='known',value=30)
  for q in ['มีเงิน100บาท มา4คนเล่นอะไรได้บ้าง','I have 100 baht for 4 people']:
   b=budget_request(q,{'r':r},[]);self.assertEqual(b['party_count'],4);self.assertTrue(b['unresolved_qualifiers']);self.assertIsNone(b['rows'][0]['max_minutes'])
 def test_keyboard_distance_and_numeric_protection(self):
  self.assertLess(distance('สวัาดี','สวัสดี'),2)
  self.assertIsNone(recover('PC 2 controls',{'one':['PC 1']}))
  r=recover('cockpik controls',{'one':['Cockpit']});self.assertIsNotNone(r);self.assertEqual(r['record_ids'],['one'])
  self.assertIsNone(recover('what game can I play?',{'one':['White game']}))
 def test_field_authority_does_not_suppress_unmanaged_fields(self):
  r=record('game','a');s={'release':{'records':{'a':r},'names':{'a':['New Game']}},'withdrawn':[],'historical_names':{'a':['Old Game']}}
  hits=[{'title':'Old Game','common_field':'how_to_play','id':'old'},{'title':'Old Game','common_field':'competition_rule','id':'rule'},{'title':'Other Game','common_field':'how_to_play','id':'other'}]
  kept,blocked=filter_legacy_hits(s,hits);self.assertEqual([x['id'] for x in kept],['rule','other']);self.assertEqual(len(blocked),1)
  s['withdrawn']=['a'];kept,_=filter_legacy_hits(s,hits);self.assertEqual([x['id'] for x in kept],['other'])
 def test_current_alias_wins_historical_alias(self):
  s={'release':{'names':{'new':['Shared Name']}},'historical_names':{'old':['Shared Name']}}
  self.assertNotIn('Shared Name',scoped_names(s).get('old',[]))
 def test_budget_fixed_free_unknown_do_not_extrapolate(self):
  r=record('rate','r');r['fields']['currency'].update(status='known',value='THB');r['fields']['duration_minutes'].update(status='known',value=30);records={'r':r}
  for rule in ['fixed','no_extrapolation']:
   r['fields']['calculation_rule']['value']=rule
   x=budget_request('I have 100 baht',records,[]);self.assertIsNone(x['rows'][0]['max_minutes'])
  r['fields']['calculation_rule']['value']='linear'
  self.assertEqual(budget_request('มีเงิน 100 บาทเล่นอะไรได้',records,[])['rows'][0]['max_minutes'],60)
  r['fields']['amount_minor']['value']=0;self.assertIsNone(budget_request('budget 100 THB',records,[])['rows'][0]['max_minutes'])
  r['fields']['amount_minor'].update(status='unknown',value=None);self.assertEqual(budget_request('budget 100 THB',records,[])['unknown_rate_ids'],['r'])
 def test_budget_rental_does_not_select_regular_hourly_rates(self):
  hourly=record('rate','hourly');package=record('rental_package','package')
  package['fields']['amount_minor']['value']=5000;package['fields']['currency']['value']='THB';package['fields']['period_label']['value']='full_day'
  result=budget_request('มีงบ100บาทเหมาเต็มวัน',{'hourly':hourly,'package':package},[])
  self.assertEqual(result['kind_scope'],'rental_package');self.assertEqual([r['rate_id'] for r in result['rows']],['package']);self.assertIsNone(result['rows'][0]['max_minutes'])

class FlowTests(CommonTests):
 def test_r62_resource_model_specs_and_policy_procedure_follow_declared_links(self):
  self.fixture()
  rr=self.store.get('fixture_resource')['record']
  model_link=next(f['key'] for f in __import__('app.knowledge.common.registry',fromlist=['CATALOG']).CATALOG['resource']['fields'] if f['reference_kind']=='equipment_model')
  rr['fields'][model_link].update(status='known',value=['fixture_equipment_model'] if model_link.endswith('_ids') else 'fixture_equipment_model',evidence_refs=[])
  model=self.store.get('fixture_equipment_model')['record'];model['fields']['specifications'].update(status='known',value={'th':'DEMO GPU','en':'DEMO GPU'},evidence_refs=[])
  # Use the schema's actual specification representation.
  from .test_common_content_r58 import default
  spec=next(f['value_schema'] for f in __import__('app.knowledge.common.registry',fromlist=['CATALOG']).CATALOG['equipment_model']['fields'] if f['key']=='specifications')
  model['fields']['specifications']['value']=default(spec)
  policy=self.store.get('fixture_policy')['record'];policy['fields']['procedure_id'].update(status='known',value='fixture_procedure',evidence_refs=[])
  policy['aliases']['en']=['Fixture policy']
  for r in [rr,model,policy]:self.approve(self.save(r,1))
  self.publish([r['record_id'] for r in [rr,model,policy]])
  a=self.answer('Fixture resource specifications',locale='en')
  self.assertTrue(any(o['record_id']=='fixture_equipment_model' and o['field']=='specifications' for o in a.decision_artifact['obligations']))
  a=self.answer('Fixture policy steps',locale='en');self.assertIn('Show ID',a.answer)
 def test_r62_all_information_contains_linked_policy_fields(self):
  self.fixture();r=self.store.get('fixture_game_service')['record'];r['fields']['account_policy_id'].update(status='known',value='fixture_policy',evidence_refs=[])
  self.approve(self.save(r,1));self.publish(['fixture_game_service'])
  a=self.answer('Starfish Quest all information',locale='en')
  self.assertTrue(any(o['record_id']=='fixture_policy' and o['field']=='details' for o in a.decision_artifact['obligations']))
 def test_r62_owner_rate_menu_has_service_and_group(self):
  self.fixture();r=next(x for x in self.store.list_heads() if x['record_id']=='fixture_rate')
  self.assertIn('service',r['label']);self.assertIn('audience',r['label'])
 def test_r62_all_prices_keep_requested_fields_in_both_languages(self):
  self.fixture()
  for q,lang in [('มีราคาอะไรบ้าง','th'),('What are your prices?','en')]:
   a=self.answer(q,locale=lang);self.assertIn('35.00',a.answer)
   self.assertFalse(a.decision_artifact['query_plan']['all_fields'])
   self.assertNotIn('name',a.decision_artifact['query_plan']['requested_fields'])
 def test_r62_zone_regular_price_is_not_replaced_by_rental_price(self):
  self.fixture();a=self.answer('Fixture zone price',locale='en')
  self.assertIn('35.00',a.answer)
  self.assertTrue(any(o['record_id']=='fixture_rate' for o in a.decision_artifact['obligations']))
  self.assertFalse(any(o['record_id']=='fixture_rental_package' for o in a.decision_artifact['obligations']))
  self.store.withdraw('fixture_rate',actor='fixture')
  self.assertEqual(self.answer('Fixture zone price',locale='en').decision_artifact['response_type'],'withdrawn')
 def test_r62_inherited_database_without_name_table_reads_without_migration(self):
  self.fixture()
  with self.store.connect(write=True) as c:c.execute('DROP TABLE cc_names')
  a=self.answer('Starfish Quest how_to_play',locale='en')
  self.assertIn('Collect pearls',a.answer)
  with self.store.connect() as c:self.assertIsNone(c.execute("SELECT 1 FROM sqlite_master WHERE name='cc_names'").fetchone())
 def test_r62_resource_price_and_group_scope(self):
  self.fixture();resource=self.store.snapshot()['release']['names']['fixture_resource'][0]
  a=self.answer(resource+' amount_minor',locale='en')
  self.assertIn('35.00',a.answer);self.assertTrue(any(o['record_id']=='fixture_rate' for o in a.decision_artifact['obligations']))
 def test_r62_old_alias_reads_updated_facts_then_blocks_withdrawal(self):
  r=record('game');r['aliases']['en']=['Old Alias'];self.approve(self.save(r));self.publish()
  r['aliases']['en']=['New Alias'];r['fields']['how_to_play']['value']['en']='DEMO updated verified instruction'
  x=self.save(r,1);self.approve(x);self.publish()
  self.assertIn('DEMO updated',self.answer('Old Alias how_to_play',locale='en').answer)
  self.store.withdraw('fixture_game',actor='fixture');self.assertIn('withdrawn',self.answer('Old Alias how_to_play',locale='en').answer)
 def test_r62_draft_preview_does_not_publish(self):
  r=record('game');self.save(r)
  with patch.dict(os.environ,{'PSU_LOCAL_LLM_ASSIST_ENABLED':'0'}):
   self.assertIsNone(preview_answer(self.store,'Starfish Quest how_to_play',locale='en'))
   a=preview_answer(self.store,'Starfish Quest how_to_play',locale='en',draft=True)
   self.assertIn('DRAFT PREVIEW',a.answer);self.assertIn('Collect pearls',a.answer)
  self.assertFalse(self.store.snapshot()['active'])
 def test_r62_typed_context_all_and_explicit_audience(self):
  self.fixture();names=self.store.snapshot()['release']['names'];service=names['fixture_service'][0];audience=names['fixture_audience'][0]
  first=self.answer(service+' amount_minor',locale='en')
  history=[{'role':'user','content':service+' amount_minor'},{'role':'assistant','content':first.answer,'common_read_state':state_from_answer(first)}]
  second=self.answer(audience,locale='en',history=history)
  self.assertIn('35.00',second.answer);self.assertIn('fixture_service',second.decision_artifact['query_plan']['record_ids'])
  history.extend([{'role':'user','content':audience},{'role':'assistant','content':second.answer,'common_read_state':state_from_answer(second)}])
  third=self.answer('all',locale='en',history=history);self.assertIn('35.00',third.answer)
 def test_r62_new_topic_does_not_inherit_price_audience(self):
  self.fixture();name=self.store.snapshot()['release']['names']['fixture_audience'][0]
  a=self.answer('เกมไหนเล่น4คนได้',history=[{'role':'user','content':name+' ราคา'}])
  self.assertNotIn('fixture_audience',a.decision_artifact['query_plan'].get('record_ids',[]))
 def test_r62_budget_uses_published_rates_and_sources(self):
  self.fixture();a=self.answer('มีเงิน100บาทเล่นอะไรได้บ้าง')
  self.assertIn('35.00',a.answer);self.assertTrue(a.hits);self.assertEqual(a.decision_artifact['query_plan']['budget']['budget_minor'],10000)
 def test_r62_legacy_catalog_and_new_game_merge_without_duplicates(self):
  r=record('game');self.approve(self.save(r));self.publish();s=self.store.snapshot();s['allow_demo']=False
  class View:
   def snapshot(self):return s
   def still_current(self,s):return True
  with patch('app.runtime.fast_answer._verified_game_catalog',return_value=({'name':'Legacy Game','aliases':[]},{'name':'Starfish Quest','aliases':['Starfish Quest']})):
   a=CommonAnswerer(View()).answer('list all games',locale='en')
  self.assertIn('Legacy Game',a.answer);self.assertEqual(a.answer.count('Starfish Quest'),1)
 def test_r62_owner_template_ids_unique_and_draft_http(self):
  server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(self.store,'test-r62','fixture',0));port=server.server_port;server.RequestHandlerClass=make_handler(self.store,'test-r62','fixture',port)
  thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
  try:
   def get():
    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/template?kind=game',headers={'Authorization':'Bearer test-r62'})
    with urllib.request.urlopen(req,timeout=5) as response:return json.load(response)
   self.assertNotEqual(get()['record_id'],get()['record_id'])
  finally:server.shutdown();server.server_close();thread.join(timeout=2)
def load_tests(loader,tests,pattern):
 suite=loader.loadTestsFromTestCase(LogicTests)
 for name in sorted(FlowTests.__dict__):
  if name.startswith('test_r62_'):suite.addTest(FlowTests(name))
 return suite
