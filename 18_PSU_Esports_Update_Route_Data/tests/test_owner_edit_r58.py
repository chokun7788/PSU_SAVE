import copy,json,os,threading,unittest,urllib.request,urllib.error
from http.server import ThreadingHTTPServer
from unittest.mock import patch
from tests.test_common_content_r58 import CommonTests,record
from app.knowledge.common.owner_server import save_owner_record,make_handler
from app.knowledge.common.store import Conflict
from app.knowledge.common.registry import value

class OwnerEditTests(unittest.TestCase):
    def setUp(self):
        self.fx=CommonTests();self.fx.setUp();self.fx.fixture();self.store=self.fx.store
    def tearDown(self):self.fx.tearDown()
    def edit(self,rid,key,val,note='แก้ข้อมูลตามเอกสารทดสอบ',review=True):
        old=self.store.get(rid);r=copy.deepcopy(old['record']);r['fields'][key].update(status='known',value=val)
        return save_owner_record(self.store,r,old['version'],'editor-fixture',translation_reviewed=review,change_note=note)
    def publish(self,x):
        self.store.approve(x['record_id'],x['version'],x['hash'],actor='editor-fixture')
        return self.store.publish([x['record_id']],actor='editor-fixture',expected_active=self.store.snapshot()['active'],request_key=os.urandom(8).hex())
    def test_price_edit_keeps_old_until_publish_and_keeps_history(self):
        rid='fixture_rate';original=self.store.revision(rid,1);x=self.edit(rid,'amount_minor',7000)
        self.assertEqual(value(self.store.snapshot()['release']['records'][rid],'amount_minor'),3500)
        ctx=self.store.edit_context(rid);self.assertEqual(ctx['published']['revision'],1);self.assertEqual(ctx['latest']['version'],2);self.assertEqual(ctx['history'][0]['change_note'],'แก้ข้อมูลตามเอกสารทดสอบ')
        self.publish(x);ctx=self.store.edit_context(rid);self.assertEqual(value(ctx['published'],'amount_minor'),7000);self.assertEqual(ctx['published']['revision'],2);self.assertEqual(self.store.revision(rid,1)['record'],original['record'])
        self.assertIn('70.00 THB',self.fx.answer('Fixture audience price',locale='en').answer)
    def test_game_details_edit_only_changes_selected_field(self):
        rid='fixture_game';original=self.store.get(rid)['record'];x=self.edit(rid,'how_to_play',{'th':'สะสมกุญแจทดสอบ','en':'Collect fixture keys'})
        self.assertIn('เก็บไข่มุก',self.fx.answer('ดาวทะเลผจญภัยเล่นยังไง').answer);self.publish(x)
        updated=self.store.get(rid)['record'];self.assertEqual(updated['record_id'],rid)
        for key in original['fields']:
            if key!='how_to_play':self.assertEqual(value(original,key),value(updated,key))
        self.assertIn('สะสมกุญแจทดสอบ',self.fx.answer('ดาวทะเลผจญภัยเล่นยังไง').answer)
    def test_policy_and_competition_rule_edits_are_separate(self):
        for rid,key in [('fixture_policy','details'),('fixture_competition_rule','text')]:
            before=copy.deepcopy(self.store.snapshot()['release']['records'][rid]);x=self.edit(rid,key,{'th':'ข้อความกฎใหม่สมมุติ','en':'Updated fixture rule'})
            self.assertEqual(self.store.snapshot()['release']['records'][rid],before);self.publish(x)
            self.assertEqual(value(self.store.snapshot()['release']['records'][rid],key)['th'],'ข้อความกฎใหม่สมมุติ');self.assertEqual(value(self.store.revision(rid,1)['record'],key),value(before,key))
    def test_future_replacement_does_not_remove_current_price(self):
        rid='fixture_rate';old=self.store.get(rid);r=copy.deepcopy(old['record']);r['validity']={'state':'known','effective_from':'2090-01-01T00:00:00+07:00','effective_until':None};r['fields']['amount_minor']['value']=9000
        x=save_owner_record(self.store,r,old['version'],'editor-fixture',translation_reviewed=True);active=self.store.snapshot()['active']
        with self.assertRaisesRegex(ValueError,'Future replacement'):self.publish(x)
        self.assertEqual(self.store.snapshot()['active'],active);self.assertEqual(value(self.store.edit_context(rid)['published'],'amount_minor'),3500)
        with patch('app.knowledge.common.store.now',return_value='2090-01-01T00:00:00+07:00'):self.publish(x)
        self.assertEqual(value(self.store.edit_context(rid)['published'],'amount_minor'),9000)
    def test_future_policy_replacement_uses_same_guard(self):
        rid='fixture_policy';old=self.store.get(rid);r=copy.deepcopy(old['record']);r['validity']={'state':'known','effective_from':'2090-01-01T00:00:00+07:00','effective_until':None}
        x=save_owner_record(self.store,r,old['version'],'editor-fixture',translation_reviewed=True)
        with self.assertRaisesRegex(ValueError,'Future replacement'):self.publish(x)
        self.assertEqual(self.store.edit_context(rid)['published']['revision'],1)
    def test_stale_edit_and_stale_approval_do_not_overwrite(self):
        rid='fixture_game';old=self.store.get(rid);self.edit(rid,'edition','fixture edition')
        with self.assertRaises(Conflict):save_owner_record(self.store,copy.deepcopy(old['record']),old['version'],'other-fixture')
        with self.assertRaises(Conflict):self.store.approve(rid,old['version'],old['hash'],actor='other-fixture')
        self.assertEqual(self.store.edit_context(rid)['total_revisions'],2)
    def test_translation_review_invalidated_when_content_changed(self):
        x=self.edit('fixture_game','edition','changed',review=False);self.assertEqual(x['record']['localization']['en_status'],'stale')
        with self.assertRaises(ValueError):self.store.approve(x['record_id'],x['version'],x['hash'],actor='editor-fixture')
    def test_history_limit_and_invalid_revision(self):
        ctx=self.store.edit_context('fixture_rate',limit=1);self.assertEqual(len(ctx['history']),1);self.assertEqual(ctx['total_revisions'],1)
        for version in [0,-1,True,'1',999]:
            with self.subTest(version=version),self.assertRaises(ValueError):self.store.revision('fixture_rate',version)
        with self.assertRaises(ValueError):self.store.edit_context('missing')
        with self.assertRaises(ValueError):self.store.edit_context('fixture_rate',limit=101)
    def test_bad_reason_does_not_create_revision_or_source(self):
        with self.store.connect() as c:before=c.execute('select count(*) from cc_sources').fetchone()[0]
        r=self.store.get('fixture_game')['record']
        for reason in ['x'*1001,{'not':'text'}]:
            with self.assertRaises(ValueError):save_owner_record(self.store,copy.deepcopy(r),1,'editor-fixture',change_note=reason)
        with self.store.connect() as c:self.assertEqual(c.execute('select count(*) from cc_sources').fetchone()[0],before)
        self.assertEqual(self.store.get('fixture_game')['version'],1)
    def test_history_api_is_authenticated_and_read_only(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(self.store,'test-cap','editor-fixture',0));port=server.server_port;server.RequestHandlerClass=make_handler(self.store,'test-cap','editor-fixture',port)
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        def call(path,token='test-cap'):
            req=urllib.request.Request(f'http://127.0.0.1:{port}'+path,headers={'Authorization':'Bearer '+token})
            with urllib.request.urlopen(req,timeout=5) as r:return json.load(r)
        try:
            before=self.store.snapshot()['epoch'];ctx=call('/api/edit-context?id=fixture_game');self.assertEqual(ctx['latest']['version'],1)
            self.assertEqual(call('/api/revision?id=fixture_game&version=1')['record'],ctx['latest']['record']);self.assertEqual(self.store.snapshot()['epoch'],before)
            for path in ['/api/edit-context?id=fixture_game','/api/revision?id=fixture_game&version=1']:
                with self.assertRaises(urllib.error.HTTPError) as e:call(path,token='wrong')
                self.assertEqual(e.exception.code,401)
            with self.assertRaises(urllib.error.HTTPError) as e:call('/api/revision?id=fixture_game&version=0')
            self.assertEqual(e.exception.code,400)
        finally:server.shutdown();server.server_close();thread.join(timeout=2)

if __name__=='__main__':unittest.main()
