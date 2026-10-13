import copy,json,os,tempfile,threading,unittest,urllib.request,urllib.error
from pathlib import Path
from unittest.mock import patch
from http.server import ThreadingHTTPServer
from app.knowledge.common.registry import CATALOG,template,schema_errors,value,content_hash
from app.knowledge.common.store import CommonStore,Conflict
from app.knowledge.common.owner_server import save_owner_record,make_handler
from app.knowledge.common.answer import CommonAnswerer,try_common_answer

ORDER=['center','zone','equipment_model','resource','service','game','audience','contact','procedure','policy','facility','game_service','game_mode','control_set','rate','rental_package','schedule','closure','competition','competition_rule','news','person','faq','live_binding']
TEST_TMP=Path(__file__).resolve().parents[1]/'data/common_test_tmp'
TEST_TMP.mkdir(parents=True,exist_ok=True)
def default(s):
    t=s.get('type');t=next((x for x in t if x!='null'),None) if isinstance(t,list) else t
    if s.get('enum'):return s['enum'][0]
    if t=='object':return {k:default(v) for k,v in s['properties'].items()}
    if t=='array':return [default(s['items'])]
    if t=='integer':return max(1,s.get('minimum',0))
    if t=='boolean':return True
    if s.get('format')=='date-time':return '2026-10-01T00:00:00+07:00'
    if s.get('format')=='date':return '2026-10-12'
    if s.get('pattern') and '[0-5]' in s['pattern']:return '09:00'
    return 'confirmed fixture'
def record(kind,rid=None):
    r=template(kind);r['record_id']=rid or 'fixture_'+kind;r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'};r['localization']['en_status']='reviewed'
    for f in CATALOG[kind]['fields']:
        if not f['publish_core']:continue
        v=default(f['value_schema'])
        if f['reference_kind']:v=['fixture_'+f['reference_kind']] if f['value_schema']['type']=='array' else 'fixture_'+f['reference_kind']
        if f['key'] in ('conditions_all','preconditions','open_periods','bookable_periods'):v=[]
        if f['key']=='steps':v=[{'order':1,'instruction':{'th':'แสดงบัตร','en':'Show ID'},'contact_id':None}]
        if f['key']=='bindings':v=[{'buttons':['Space'],'gesture':'press','action':{'th':'กระโดด','en':'Jump'},'context':{'th':'ระหว่างเล่น','en':'During play'}}]
        if f['key']=='supported_platforms':v=['PC']
        if f['key']=='platform':v='PC'
        if f['key']=='name' or f['key']=='title':v={'th':'ทดสอบ '+kind,'en':'Fixture '+kind}
        r['fields'][f['key']].update(status='known',value=v,evidence_refs=[],note=None)
    if kind=='game':
        for k,v in {'title':{'th':'ดาวทะเลผจญภัย','en':'Starfish Quest'},'summary':{'th':'เกมสำรวจใต้ทะเล','en':'Explore under the sea'},'how_to_play':{'th':'เก็บไข่มุกและหาทางออก','en':'Collect pearls and find the exit'},'supported_platforms':['PC']}.items():r['fields'][k].update(status='known',value=v,evidence_refs=[],note=None)
    if kind=='game_service':r['fields']['offered']['value']=True
    if kind=='rate':r['fields']['amount_minor']['value']=3500
    return r

class CommonTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=TEST_TMP);self.path=Path(self.tmp.name)/'approved.sqlite';self.store=CommonStore(self.path);self.store.initialize(allow_demo=True);self.saved={}
    def tearDown(self):self.tmp.cleanup()
    def save(self,r,version=0,review=True):
        x=save_owner_record(self.store,copy.deepcopy(r),version,'fixture',translation_reviewed=review);self.saved[x['record_id']]=x;return x
    def approve(self,x):self.store.approve(x['record_id'],x['version'],x['hash'],actor='fixture')
    def publish(self,ids=None):
        return self.store.publish(ids or list(self.saved),actor='fixture',expected_active=self.store.snapshot()['active'],request_key=os.urandom(8).hex())
    def fixture(self):
        for k in ORDER:self.approve(self.save(record(k)))
        self.publish()
    def answer(self,q,**kw):return CommonAnswerer(self.store).answer(q,**kw)
    def test_all_24_templates_and_missing_field(self):
        for kind in CATALOG:
            with self.subTest(kind=kind):
                r=template(kind);self.assertEqual(schema_errors(r),[]);r['fields'].pop(next(iter(r['fields'])));self.assertTrue(schema_errors(r))
    def test_all_24_types_publish_read_and_old_pilot_tables(self):
        self.fixture();s=self.store.snapshot();self.assertEqual(len(s['release']['records']),24)
        with self.store.connect() as c:self.assertEqual(c.execute('SELECT count(*) FROM records').fetchone()[0],0)
        for rid in s['release']['records']:
            with self.subTest(rid=rid):self.assertEqual(self.store.get(rid)['hash'],self.saved[rid]['hash'])
    def test_unapproved_and_stale_approval(self):
        x=self.save(record('game'))
        with self.assertRaises(Conflict):self.publish()
        self.approve(x);self.save(record('game'),version=1)
        with self.assertRaises(Conflict):self.approve(x)
        with self.assertRaises(Conflict):self.publish()
    def test_draft_isolation_update_and_restart(self):
        r=record('game');self.approve(self.save(r));release=self.publish();r['fields']['how_to_play']['value']['th']='สะสมกุญแจ'
        x=self.save(r,1);self.assertIn('เก็บไข่มุก',self.answer('ดาวทะเลผจญภัยเล่นยังไง').answer)
        self.approve(x);new=self.publish();self.assertNotEqual(release,new);self.assertIn('สะสมกุญแจ',self.answer('ดาวทะเลผจญภัยเล่นยังไง').answer)
        self.assertEqual(CommonStore(self.path).snapshot()['active'],new)
    def test_new_title_paraphrase_en_typo_compound_and_followup(self):
        self.fixture()
        cases=[('ดาวทะเลผจญภัยเล่นยังไงและปุ่มอะไร','th',['เก็บไข่มุก','Space']),('How to play Starfish Quest and what are the controls?','en',['Collect pearls','Space']),('Starfish Quesst controls','en',['Space'])]
        for q,lang,want in cases:
            with self.subTest(q=q):
                a=self.answer(q,locale=lang);self.assertIsNotNone(a)
                for text in want:self.assertIn(text,a.answer)
        a=self.answer('แล้วปุ่มทั้งหมดล่ะ',history=[{'role':'user','content':'ดาวทะเลผจญภัยเล่นยังไง'}]);self.assertIn('Space',a.answer)
        a=self.answer('แล้วปุ่มล่ะ',history=[{'role':'user','text':'ดาวทะเลผจญภัยเล่นยังไง'}]);self.assertIn('Space',a.answer)
    def test_wrong_platform_and_unknown_field(self):
        self.fixture();r=record('control_set','fixture_control_ps5');r['fields']['platform']['value']='PS5';g=self.store.get('fixture_game')['record'];g['fields']['supported_platforms']['value']=['PC','PS5'];gx=self.save(g,1);self.approve(gx);self.approve(self.save(r));self.publish(['fixture_game','fixture_control_ps5'])
        a=self.answer('Starfish Quest controls',locale='en');self.assertIn('Choose a platform',a.answer)
        a=self.answer('Starfish Quest PC controls',locale='en');self.assertIn('Space',a.answer);self.assertNotIn('Choose a platform',a.answer)
        a=self.answer('Starfish Quest genre',locale='en');self.assertIn('Not yet confirmed',a.answer)
    def test_list_all_no_top_k(self):
        for n in range(105):
            r=record('game',f'new_game_{n:03}');r['fields']['title']['value']={'th':f'เกมทดสอบ {n}','en':f'Synthetic title {n}'};self.approve(self.save(r))
        self.publish();a=self.answer('all games',locale='en');self.assertIn(': 105',a.answer);self.assertIn('Synthetic title 104',a.answer)
    def test_expired_and_future(self):
        from datetime import datetime
        r=record('game');r['validity']['effective_until']='2026-10-01T00:00:00+07:00';self.approve(self.save(r));self.publish()
        a=self.answer('Starfish Quest how to play',locale='en',at=datetime.fromisoformat('2026-10-10T12:00:00+07:00'));self.assertIn('not effective',a.answer);self.assertNotIn('Collect pearls',a.answer)
    def test_exact_price_and_validity_gate(self):
        self.fixture();r=self.store.get('fixture_rate')['record'];r['aliases']['en']=['Special PC rate'];x=self.save(r,1);self.approve(x);self.publish(['fixture_rate']);a=self.answer('Special PC rate price',locale='en');self.assertIn('35.00 THB',a.answer)
        r['validity']={'state':'unknown','effective_from':None,'effective_until':None};x=self.save(r,2)
        with self.assertRaises(ValueError):self.approve(x)
    def test_money_type_missing_source_negative_and_extra(self):
        self.fixture()
        for change in ('string','negative','unknown_zero','extra'):
            with self.subTest(change=change):
                r=self.store.get('fixture_rate')['record']
                if change=='string':r['fields']['amount_minor']['value']='35'
                elif change=='negative':r['fields']['amount_minor']['value']=-1
                elif change=='unknown_zero':r['fields']['amount_minor'].update(status='unknown',value=0,evidence_refs=[])
                else:r['fields']['invented']={'status':'known','value':'wrong'}
                with self.assertRaises(ValueError):self.save(r,1)
    def test_fk_scope_and_withdraw_dependency(self):
        self.fixture();r=self.store.get('fixture_game_service')['record'];r['fields']['service_id']['value']='fixture_zone'
        with self.assertRaises(ValueError):self.save(r,1)
        with self.assertRaises(Conflict):self.store.withdraw('fixture_game',actor='fixture')
        self.store.withdraw('fixture_game_service',actor='fixture');self.store.withdraw('fixture_game_mode',actor='fixture');self.store.withdraw('fixture_control_set',actor='fixture');self.store.withdraw('fixture_competition_rule',actor='fixture');self.store.withdraw('fixture_competition',actor='fixture');self.store.withdraw('fixture_game',actor='fixture')
        self.assertIn('withdrawn',self.answer('Starfish Quest how to play',locale='en').answer)
    def test_stale_translation_and_source_tamper(self):
        r=record('game');x=self.save(r);self.approve(x);r['fields']['summary']['value']['th']='เปลี่ยนความหมาย';x=self.save(r,1,review=False)
        self.assertEqual(x['record']['localization']['en_status'],'stale')
        with self.assertRaises(ValueError):self.approve(x)
        clean=self.save(record('zone'))
        with self.store.connect(write=True) as c:
            refs=clean['record']['fields']['name']['evidence_refs']
            c.execute("UPDATE cc_sources SET snapshot='{}' WHERE source_id=?",(refs[0]['source_id'],))
        with self.assertRaisesRegex(ValueError,'hash mismatch'):self.approve(clean)
    def test_atomic_publish_and_idempotence(self):
        self.fixture();active=self.store.snapshot()['active'];ids=['fixture_game'];key='same-request'
        a=self.store.publish(ids,actor='fixture',expected_active=active,request_key=key);self.assertEqual(a,self.store.publish(ids,actor='fixture',expected_active=active,request_key=key))
        with self.assertRaises(Conflict):self.store.publish(['fixture_zone'],actor='fixture',expected_active=active,request_key=key)
        with self.assertRaises(Conflict):self.store.publish(ids,actor='fixture',expected_active=active,request_key='other')
        self.assertEqual(self.store.snapshot()['active'],a)
    def test_rollback_without_resurrecting_withdrawn(self):
        r=record('game');self.approve(self.save(r));first=self.publish();self.approve(self.save(r,1));second=self.publish();self.store.rollback(first,actor='fixture',expected_active=second);self.assertEqual(self.store.snapshot()['active'],first)
        self.store.withdraw('fixture_game',actor='fixture')
        with self.assertRaises(Conflict):self.store.rollback(second,actor='fixture',expected_active=first)
    def test_demo_guard_and_unrelated_scope(self):
        self.fixture()
        with patch.dict(os.environ,{'PSU_KNOWLEDGE_DB':str(self.path),'PSU_COMMON_ALLOW_DEMO':'0'}):self.assertIsNone(try_common_answer('Starfish Quest controls'))
        self.assertIsNone(self.answer('What should I eat tonight?'));self.assertIsNone(self.answer('Starfish Quest available now?'))
    def test_new_numbered_edition_not_fuzzed(self):
        r=record('game');r['fields']['title']['value']={'th':'เกมทดสอบ 8','en':'Novel game 8'};self.approve(self.save(r));self.publish();self.assertIsNone(self.answer('Novel game 9 controls'))
    def test_unknown_platform_never_inherits_controls(self):
        self.fixture()
        for q in ('Starfish Quest PS4 controls','ดาวทะเลผจญภัย PlayStation 4 ปุ่มอะไร'):
            a=self.answer(q,locale='en');self.assertNotIn('Space',a.answer);self.assertIn('No confirmed',a.answer)
    def test_withdraw_name_survives_next_release(self):
        self.approve(self.save(record('game')));self.publish();self.store.withdraw('fixture_game',actor='fixture')
        r=record('game','another_game');r['fields']['title']['value']={'th':'อีกเกมหนึ่ง','en':'Another title'};self.approve(self.save(r));self.publish(['another_game'])
        self.assertIn('withdrawn',self.answer('Starfish Quest how to play',locale='en').answer)
        self.assertIn('withdrawn',CommonAnswerer(CommonStore(self.path)).answer('Starfish Quest how to play',locale='en').answer)
    def test_nested_english_translation_requires_status(self):
        self.fixture();r=self.store.get('fixture_control_set')['record'];r['localization']['en_status']='missing';r['localization']['source_revision_hash']=None
        x=self.save(r,1,review=False)
        with self.assertRaisesRegex(ValueError,'English translation'):self.approve(x)
    def test_rate_overlap_compares_actual_instants(self):
        self.fixture();r=record('rate','second_rate');r['validity']={'state':'known','effective_from':'2026-12-31T17:00:00Z','effective_until':'2027-02-01T00:00:00Z'}
        self.approve(self.save(r));self.publish(['second_rate']) # Exact adjacent boundary, not an overlap.
        r['validity']['effective_from']='2026-12-31T16:59:59Z';self.approve(self.save(r,1))
        with self.assertRaisesRegex(ValueError,'Overlapping rates'):self.publish(['second_rate'])
    def test_competition_cycle_rejected_atomically(self):
        self.fixture();old=self.store.snapshot()['active'];r=record('competition_rule','second_rule');r['fields']['depends_on_ids'].update(status='known',value=['fixture_competition_rule']);self.approve(self.save(r))
        first=self.store.get('fixture_competition_rule')['record'];first['fields']['depends_on_ids'].update(status='known',value=['second_rule']);self.approve(self.save(first,1))
        with self.assertRaisesRegex(ValueError,'Cyclic'):self.publish(['fixture_competition_rule','second_rule'])
        self.assertEqual(old,self.store.snapshot()['active'])
    def test_generic_location_and_game_listing_and_rule_scope(self):
        self.fixture();r=self.store.get('fixture_center')['record'];r['fields']['address'].update(status='known',value={'th':'อาคารทดสอบ','en':'Fixture building'});self.approve(self.save(r,1));self.publish(['fixture_center'])
        self.assertIn('อาคารทดสอบ',self.answer('ศูนย์อยู่ที่ไหน').answer)
        self.assertIn('Starfish Quest',self.answer('Which games are there?',locale='en').answer)
        a=self.answer('Starfish Quest rules',locale='en');self.assertIn('competition',json.dumps(a.decision_artifact));self.assertNotIn('Collect pearls',a.answer)
    def test_planner_accepts_only_relevant_schema_fields(self):
        from app.knowledge.common.planner import checked_plan
        self.fixture();records=self.store.snapshot()['release']['records'];ids=['fixture_game']
        self.assertIsNotNone(checked_plan({'requested_fields':['bindings'],'all_fields':False,'platform':'PC'},ids,records))
        for p in ({'requested_fields':['amount_minor'],'all_fields':False,'platform':None},{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}):self.assertIsNone(checked_plan(p,ids,records))
    def test_expired_parent_does_not_leak_controls(self):
        from datetime import datetime
        self.fixture();r=self.store.get('fixture_game')['record'];r['validity']['effective_until']='2026-10-01T00:00:00+07:00';self.approve(self.save(r,1));self.publish(['fixture_game'])
        a=self.answer('Starfish Quest controls',locale='en',at=datetime.fromisoformat('2026-10-10T00:00:00+07:00'));self.assertIn('not effective',a.answer);self.assertNotIn('Space',a.answer)
    def test_unknown_wording_clarifies_and_schema_planner_can_resolve(self):
        self.fixture();a=self.answer('Starfish Quest บังคับตัวละครด้วยอะไร');self.assertEqual(a.decision_artifact['response_type'],'clarification');self.assertNotIn('เก็บไข่มุก',a.answer)
        a=self.answer('Starfish Quest บังคับตัวละครด้วยอะไร',planner=lambda *args:{'requested_fields':['bindings'],'all_fields':False,'platform':None,'method':'bounded_llm_schema_fields'});self.assertIn('Space',a.answer)
        a=self.answer('Starfish Quest ขอรายละเอียด');self.assertIn('เก็บไข่มุก',a.answer);self.assertNotIn('body:',a.answer)
    def test_empty_early_v3_database_does_not_block_legacy(self):
        with self.store.connect(write=True) as c:c.execute('DROP TABLE cc_names')
        self.assertIsNone(CommonAnswerer(self.store).answer('PC ราคาเท่าไหร่'))
        with patch.dict(os.environ,{'PSU_KNOWLEDGE_DB':str(self.path),'PSU_COMMON_ALLOW_DEMO':'1'}):self.assertIsNone(try_common_answer('PC ราคาเท่าไหร่'))

class OwnerHTTPTests(unittest.TestCase):
    def test_auth_origin_draft_approve_publish_preview(self):
        with tempfile.TemporaryDirectory(dir=TEST_TMP) as tmp:
            store=CommonStore(Path(tmp)/'db.sqlite');store.initialize()
            server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(store,'test-capability','fixture',0));port=server.server_port;server.RequestHandlerClass=make_handler(store,'test-capability','fixture',port)
            thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
            def call(path,body=None,token='test-capability',origin=None):
                headers={'Authorization':'Bearer '+token}
                if origin:headers['Origin']=origin
                if body is not None:headers['Content-Type']='application/json'
                req=urllib.request.Request(f'http://127.0.0.1:{port}'+path,data=json.dumps(body).encode() if body is not None else None,headers=headers)
                with urllib.request.urlopen(req,timeout=5) as res:return json.load(res)
            try:
                with self.assertRaises(urllib.error.HTTPError) as e:call('/api/status',token='wrong')
                self.assertEqual(e.exception.code,401)
                with self.assertRaises(urllib.error.HTTPError) as e:call('/api/save',{'attest':True},origin='https://attacker.invalid')
                self.assertEqual(e.exception.code,403)
                self.assertEqual(call('/api/registry')['kinds'],24)
                x=call('/api/save',{'record':record('game'),'expected_version':0,'attest':True,'translation_reviewed':True})
                self.assertNotIn('Collect pearls',call('/api/preview',{'question':'Starfish Quest how to play','locale':'en'})['answer'])
                call('/api/approve',{'id':x['record_id'],'version':x['version'],'hash':x['hash'],'confirm':True})
                call('/api/publish',{'ids':[x['record_id']],'expected_active':'','request_key':'http-new'})
                self.assertIn('Collect pearls',call('/api/preview',{'question':'Starfish Quest how to play','locale':'en'})['answer'])
            finally:server.shutdown();server.server_close();thread.join()
