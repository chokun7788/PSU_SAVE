import unittest,copy,os,tempfile,subprocess,sys
from unittest.mock import patch
from .test_common_content_r58 import CommonTests,record
from app.knowledge.common.registry import CATALOG,value
from app.knowledge.common.semantics import meaning,project
from app.knowledge.common.read_contract import build_needs
from app.knowledge.common.authority import classify
from app.knowledge.common.answer import try_common_answer,CommonAnswerer
from app.knowledge.common.discovery import discover_games

class PureTests(unittest.TestCase):
 def test_kind_meanings_and_full_coverage(self):
  for kind,c in CATALOG.items():
   for f in c['fields']:
    self.assertTrue(meaning(kind,f['key'],'en'));self.assertTrue(meaning(kind,f['key'],'th'))
  self.assertIn('installed',meaning('game_service','game_version','en').lower())
  self.assertIn('verified',meaning('control_set','game_version','en').lower())
 def test_projection_not_whole_rate_or_policy(self):
  keys,basis=project(record('rate'),['amount_minor','unit'])
  self.assertIn('audience_id',keys);self.assertIn('currency',keys);self.assertNotIn('persons_max',keys)
  keys,basis=project(record('policy'),['decision'])
  self.assertIn('conditions_all',keys);self.assertNotIn('consequence',keys)
  keys,_=project(record('policy'),['decision'],full=True)
  self.assertEqual(set(keys),set(record('policy')['fields']))
 def test_discovery_uses_mode_not_room_seats(self):
  m=record('game_mode');m['fields']['players_min'].update(status='known',value=2);m['fields']['players_max'].update(status='known',value=4)
  m['fields']['studio_supported'].update(status='known',value=True)
  records={'fixture_game_mode':m,'fixture_zone':record('zone')}
  for q in ['เกมไหนเล่น4คนได้','Which games can four people play?']:
   self.assertEqual(discover_games(q,records)['record_ids'],['fixture_game_mode'])
  self.assertEqual(discover_games('games for 5 people',records)['record_ids'],[])
  self.assertIsNone(discover_games('games for 4 people price',records))
 def test_read_contract_does_not_claim_semantic_proof(self):
  x=build_needs('what version?',{'game'},['game_version'],model=True)
  self.assertFalse(x['semantic_correctness_verified']);self.assertTrue(x['needs'][0]['ambiguous_kind'])
  self.assertEqual(x['needs'][0]['resolution'],'model_proposed')
 def test_no_release_and_live_defer(self):
  s={'release':None,'withdrawn':[]}
  self.assertEqual(classify('price',s,[])['decision'],'defer')
  self.assertEqual(classify('PC1 ว่างไหม',s,[])['reason'],'live_adapter_authority')
 def test_transposition_candidate_preserves_numbers(self):
  from app.knowledge.common.schema_language import recover_schema_language
  q,edits=recover_schema_language('versoin 2026 not now',{'competition'})
  self.assertIn('version 2026 not now',q);self.assertTrue(edits)
 def test_identity_field_not_added_to_answer_request(self):
  from app.knowledge.common.planner import semantic_guard
  records={'a':{'kind':'faq','fields':{}}}
  plan={'requested_fields':['answer','question','scope_note'],'all_fields':False,'platform':None}
  clean,audit=semantic_guard('Explain the response and the situations it applies to',plan,['a'],records)
  self.assertNotIn('question',clean['requested_fields']);self.assertIn('answer',clean['requested_fields'])
  clean,audit=semantic_guard('Give the question text and its response',plan,['a'],records)
  self.assertIn('question',clean['requested_fields'])
 def test_long_query_two_bounded_batches(self):
  from app.knowledge.common import planner
  q=' and '.join(['unfamiliar feature '+str(n) for n in range(7)])
  p=planner.FieldPlan({'requested_fields':['how_to_play'],'all_fields':False,'platform':None},{'unclear_clauses':[]})
  with patch.dict(os.environ,{'PSU_COMMON_PLAN_MAX_BATCHES':'2'}),patch.object(planner,'_plan_fields_batch',return_value=p) as fetch:
   result=planner.plan_fields(q,{'a':{'kind':'game','fields':{}}},['a'])
   self.assertIsNotNone(result);self.assertEqual(fetch.call_count,2)
   self.assertEqual(fetch.call_args.kwargs['whole_question'],q)
 def test_model_gate_excludes_other_process_and_releases(self):
  from pathlib import Path
  from app.knowledge.model_gate import SharedModelGate
  with tempfile.TemporaryDirectory() as tmp:
   path=Path(tmp)/'gate.lock';gate=SharedModelGate(path);self.assertTrue(gate.acquire(timeout=.1))
   code="from app.knowledge.model_gate import SharedModelGate; import sys; g=SharedModelGate(sys.argv[1]); acquired=g.acquire(timeout=.1); print(acquired); g.release() if acquired else None"
   try:
    child=subprocess.check_output([sys.executable,'-c',code,str(path)],text=True,timeout=10)
    self.assertEqual(child.strip(),'False')
   finally:gate.release()
   child=subprocess.check_output([sys.executable,'-c',code,str(path)],text=True,timeout=10)
   self.assertEqual(child.strip(),'True')

class MutationTests(CommonTests):
 def test_r61_price_update_unknown_withdraw_rollback(self):
  self.fixture();r=record('rate');r['aliases']={'th':['อัตราทดลอง'],'en':['Fixture Tariff']}
  x=self.save(r,1);self.approve(x);self.publish();old=self.store.snapshot()['active']
  r['fields']['amount_minor']['value']=9000
  x=self.save(r,2);self.approve(x);self.publish()
  with patch.dict(os.environ,{'PSU_KNOWLEDGE_DB':str(self.path),'PSU_COMMON_ALLOW_DEMO':'1'}):
   ans=try_common_answer('Fixture rate amount_minor',locale='en')
   # Fixture aliases are empty; use the stable title fallback names from the release.
   name=self.store.snapshot()['release']['names']['fixture_rate'][0]
   ans=try_common_answer(name+' amount_minor',locale='en')
   self.assertIn('90.00',ans.answer);self.assertNotIn('35.00',ans.answer)
   r['fields']['tax_note'].update(status='unknown',value=None,evidence_refs=[])
   x=self.save(r,3);self.approve(x);self.publish()
   ans=try_common_answer(name+' tax_note',locale='en');self.assertIn('Not yet confirmed',ans.answer)
   self.store.rollback(old,actor='fixture',expected_active=self.store.snapshot()['active'])
   self.assertIn('35.00',try_common_answer(name+' amount_minor',locale='en').answer)
   self.store.withdraw('fixture_rate',actor='fixture')
   ans=try_common_answer(name+' amount_minor',locale='en')
   self.assertIsNotNone(ans);self.assertNotIn('35.00',ans.answer);self.assertNotIn('90.00',ans.answer)
 def test_r61_all_choices_preserves_price_need(self):
  self.fixture();names=self.store.snapshot()['release']['names'];name=names['fixture_audience'][0]
  a=self.answer('ทั้งหมด',history=[{'role':'user','content':name+' ราคา'}])
  self.assertIn('35.00',a.answer);self.assertIn('amount_minor',a.decision_artifact['query_plan']['requested_fields'])
 def test_r61_all_zones_not_unknown_or_empty(self):
  self.fixture();r=record('schedule');r['aliases']={'th':['ตารางทดลอง'],'en':['Fixture Schedule']};r['fields']['zone_ids'].update(status='known',value=[],evidence_refs=[],note=None)
  x=self.save(r,1);self.approve(x);self.publish();name=self.store.snapshot()['release']['names']['fixture_schedule'][0]
  for lang,word in [('th','ทุกโซน'),('en','All zones')]:
   self.assertIn(word,self.answer(name+' zone_ids',locale=lang).answer)
 def test_r61_unmanaged_competition_defer_owned_miss_blocks(self):
  r=record('game');self.approve(self.save(r));self.publish()
  with patch.dict(os.environ,{'PSU_KNOWLEDGE_DB':str(self.path),'PSU_COMMON_ALLOW_DEMO':'1'}):
   self.assertIsNone(try_common_answer('Starfish Quest tournament rules',locale='en'))
   with patch.object(CommonAnswerer,'answer',return_value=None):
    a=try_common_answer('Starfish Quest how_to_play',locale='en')
    self.assertIsNotNone(a);self.assertEqual(a.decision_artifact['query_plan']['authority']['decision'],'common')
 def test_r61_linked_account_policy_expands_requested_facts(self):
  self.fixture()
  service=record('game_service');service['fields']['account_policy_id'].update(status='known',value='fixture_policy',evidence_refs=[],note=None)
  x=self.save(service,1);self.approve(x);self.publish()
  a=self.answer('Starfish Quest account decision',locale='en')
  obligations=a.decision_artifact['obligations']
  self.assertTrue(any(o['record_id']=='fixture_policy' and o['field']=='decision' for o in obligations))
  self.assertTrue(a.decision_artifact['query_plan']['relation_edges'])
  self.assertTrue(any(h['id'].startswith('fixture_policy:decision:') for h in a.hits))

def load_tests(loader,tests,pattern):
 suite=loader.loadTestsFromTestCase(PureTests)
 for name in sorted(MutationTests.__dict__):
  if name.startswith('test_r61_'):suite.addTest(MutationTests(name))
 return suite
