import json,unittest
from unittest.mock import patch,Mock
from app.knowledge.common.query_contract import resolve_fields,focus_request,bare_selector,overview_request,unresolved_clauses,resolution_uncertain
from app.knowledge.common.schema_language import recover_schema_language
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common import planner

class GeneralizationTests(unittest.TestCase):
    def test_overview_is_not_any_information_word(self):
        self.assertTrue(overview_request('ขอข้อมูลหน่อย'))
        self.assertTrue(overview_request('Tell me about it'))
        self.assertFalse(overview_request('ข้อมูลหมดอายุเมื่อไหร่'))
        self.assertFalse(overview_request('What information does this notice contain?'))
    def test_rejected_task_not_negative_fact(self):
        q,focus=focus_request('ไม่เอาราคา ขอเวลาเล่นอย่างเดียว',{'service'})
        self.assertIsNotNone(focus);self.assertEqual(resolve_fields(q,{'service'})[0],['session_minutes'])
        q,focus=focus_request('I do not want the price; just tell me the play duration',{'service'})
        self.assertIsNotNone(focus);self.assertNotIn('amount_minor',resolve_fields(q,{'service'})[0])
        for text in ['ไม่ได้เป็นนักศึกษา','I am not a student','It is not allowed']:
            self.assertIsNone(focus_request(text,{'audience'})[1])
    def test_new_question_is_not_bare_selector(self):
        self.assertTrue(bare_selector('ครับ'))
        self.assertFalse(bare_selector('แล้วต้องยื่นอะไร'))
        self.assertFalse(bare_selector('How long does it last?'))
    def test_partial_and_purpose_need_review(self):
        self.assertTrue(resolution_uncertain('What should I present to verify my eligibility?',{'audience'}))
        self.assertTrue(resolution_uncertain('Are opening hours different from reservation periods?',{'schedule'}))
    def test_modifiers_share_quantity_object(self):
        q='What are the minimum and maximum player counts?'
        self.assertEqual(set(resolve_fields(q,{'game_mode'})[0]),{'players_min','players_max'})
        self.assertEqual(unresolved_clauses(q,{'game_mode'}),[])
    def test_metadata_semantics_scoped(self):
        self.assertIn('office_hours',resolve_fields('ช่วงเวลาที่ติดต่อฝ่ายช่วยเหลือ',{'contact'})[0])
        self.assertNotIn('office_hours',resolve_fields('ช่วงเวลาที่ติดต่อฝ่ายช่วยเหลือ',{'game'})[0])
        self.assertIn('reason',resolve_fields('เพราะเหตุใด',{'closure'})[0])
        self.assertIn('answer',resolve_fields('What is the response?',{'faq'})[0])
    def test_schema_spelling_preserves_valid_words_and_digits(self):
        q,edits=recover_schema_language('whic rulebook 2026 applies?',{'competition'})
        self.assertIn('which',q);self.assertIn('2026',q);self.assertTrue(edits)
        for word in ['not','now','pay','play','score','host','hear']:
            self.assertEqual(recover_schema_language(word,{'competition'})[0],word)
    def test_partial_not_validated_complete(self):
        class Store:
            def still_current(self,s):return True
        ans=CommonAnswerer(Store()).finish({'active':'test'},0,'known portion',[],{'requested_fields':['value'],'unresolved_clauses':['unknown part']},[{'record_id':'a','field':'value','status':'known','evidence_refs':[{'source_id':'s','locator':'/v'}]}])
        self.assertFalse(ans.validation.ok);self.assertEqual(ans.decision_artifact['response_type'],'partial_answer')
    def _call(self,reply):
        class Response:
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self,n):return json.dumps({'response':json.dumps(reply),'prompt_eval_count':123}).encode()
        audits=[];gate=Mock();gate.acquire.return_value=True
        with patch.object(planner,'MODEL_WORK',gate),patch.object(planner,'llm_call_allowed',return_value=(True,{})),patch.object(planner,'record_llm_success') as success,patch.object(planner,'record_llm_failure') as failure,patch.object(planner.urllib.request,'urlopen',return_value=Response()) as fetch:
            result=planner.plan_fields('Is it closed, and why?',{'a':{'kind':'closure','fields':{}}},['a'],diagnostic=audits.append)
            payload=json.loads(fetch.call_args.args[0].data)
            return result,audits,payload,success.called,failure.called
    def test_clause_schema_and_typed_coverage_repair(self):
        result,audits,payload,success,failure=self._call({'clause_fields':[{'id':0,'requested_fields':['state','reason']},{'id':1,'requested_fields':[]}],'all_fields':False,'platform':None})
        self.assertIsNotNone(result);self.assertTrue(success);self.assertFalse(failure)
        self.assertEqual(payload['format']['properties']['all_fields']['enum'],[False])
        self.assertEqual(result.semantic_audit['unclear_clauses'],[])
        self.assertTrue(result.semantic_audit['clause_coverage_repairs'])
    def test_duplicate_clause_is_output_failure_not_network(self):
        result,audits,payload,success,failure=self._call({'clause_fields':[{'id':0,'requested_fields':['state']},{'id':0,'requested_fields':['reason']}],'all_fields':False,'platform':None})
        self.assertIsNone(result);self.assertTrue(success);self.assertFalse(failure)
        self.assertTrue(audits[-1]['transport_ok']);self.assertFalse(audits[-1]['schema_accepted'])
        self.assertEqual(audits[-1]['error_stage'],'clause_schema')
    def test_many_clauses_preserved_and_planner_declines(self):
        from app.knowledge.common.query_contract import semantic_clauses
        q=' and '.join(['unfamiliar need '+str(n) for n in range(7)])
        self.assertEqual(len(semantic_clauses(q)),7)
        audits=[];gate=Mock();gate.acquire.return_value=True
        with patch.dict('os.environ',{'PSU_COMMON_PLAN_MAX_BATCHES':'1'}),patch.object(planner,'MODEL_WORK',gate),patch.object(planner,'llm_call_allowed',return_value=(True,{})),patch.object(planner,'release_llm_slot'),patch.object(planner.urllib.request,'urlopen') as fetch:
            self.assertIsNone(planner.plan_fields(q,{'a':{'kind':'game','fields':{}}},['a'],diagnostic=audits.append))
            fetch.assert_not_called();self.assertEqual(audits[-1]['gate_reason'],'too_many_clauses')
    def test_owner_preview_respects_chat_feature_setting(self):
        from app.knowledge.common.owner_server import preview_answer
        from dataclasses import dataclass
        @dataclass
        class Answer:
            decision_artifact:dict
        for flag,wanted in [('1',True),('0',False)]:
            with patch.dict('os.environ',{'PSU_LOCAL_LLM_ASSIST_ENABLED':flag}),patch.object(CommonAnswerer,'answer',return_value=Answer({})) as read:
                result=preview_answer(Mock(),'what is required?',locale='en',history=[{'role':'user','content':'demo'}])
                self.assertEqual(read.call_args.kwargs['planner'] is not None,wanted)
                self.assertEqual(result.decision_artifact['preview_llm_enabled'],wanted)
    def test_pipeline_default_and_explicit_disable(self):
        from app.pipeline.engine import answer_question_pipeline_debug
        for flag,wanted in [(None,True),(False,False),(True,True)]:
            sentinel=object()
            with patch('app.pipeline.engine.env_experimental_llm_default',return_value=True),patch('app.knowledge.common.answer.try_common_answer',return_value=sentinel) as read:
                self.assertIs(answer_question_pipeline_debug('Starfish game how to play',locale='en',experimental_allow_llm=flag),sentinel)
                self.assertEqual(read.call_args.kwargs['allow_llm'],wanted)
if __name__=='__main__':unittest.main()
