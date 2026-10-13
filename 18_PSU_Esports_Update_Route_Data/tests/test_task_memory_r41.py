"""Cross-topic request memory and per-task execution coverage contracts."""
import os
import sys
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0')
from app.session.conversation_store import ConversationStore,TurnConflict
from app.session.task_memory import task_from_response,resolve_memory
from app.pipeline.task_contract import compound_contract,single_contract
from app.pipeline.schemas import PipelineRoute,PipelineTrace,EntityBundle,ValidationResult
from app.pipeline.engine import AnswerQualityPipeline,answer_question_pipeline_debug as answer

def response(question,category='games',mode='pipeline:structured_game_controls',intent='game_control_lookup',rid='reply'):
    return dict(ok=True,request_id=rid,answer='Recorded source response',resolved_question=question,
                route_category=category,route_intent=intent,mode=mode)

def commit(store,q,**kwargs):
    turn=str(store.snapshot('s')['revision']+1)
    prepared=store.begin('s',turn,q,locale='en',history=store.history('s'))
    body=response(q,rid=turn,**kwargs)
    store.complete('s',turn,prepared['revision'],body,plan=prepared['plan'])
    store.acknowledge('s',turn)
    return prepared

def child(mode='pipeline:structured_game_controls',typ='fact',ok=True,trace=()):
    return SimpleNamespace(mode=mode,route=PipelineRoute('games','game_control_lookup',1,typ,'low','fixture'),
        validation=ValidationResult(ok),hits=[{}],trace=trace)

class TaskMemoryR41Tests(unittest.TestCase):
    def test_resume_price_retains_external_groups_across_rules(self):
        s=ConversationStore();commit(s,'PC prices for external users',category='service_fee',mode='pipeline:structured_service_fee_conversation',intent='service_fee_query')
        commit(s,'Competition rules for CS2',category='competition_rules',mode='pipeline:competition_rule_overview_source',intent='competition_rule_lookup')
        p=s.begin('s','resume','back to the prices',locale='en')
        self.assertEqual(p['plan']['tasks'][0]['filters']['customer_group_ids'],['general_student','general_adult'])
        self.assertIn('PC',p['context_resolution']['resolved_question'])

    def test_no_context_or_unacknowledged_resume_clarifies(self):
        s=ConversationStore();p=s.begin('s','1','VALORANT controls',locale='en')
        s.complete('s','1',p['revision'],response('VALORANT controls'))
        s.delivery('s','1','server_written')
        for sid in ('s','other'):
            r=s.begin(sid,'resume','back to the controls',locale='en')
            self.assertEqual(r['plan']['message_key'],'no_previous_task')

    def test_acknowledged_resume_survives_turn_eviction(self):
        s=ConversationStore();commit(s,'VALORANT controls')
        for i in range(10):commit(s,'unrelated '+str(i),category='general',mode='pipeline:no_answer',intent='unknown')
        r=s.begin('s','resume','back to the controls',locale='en')
        self.assertEqual(r['context_resolution']['resolved_question'],'VALORANT controls')

    def test_ttl_expiry_cannot_resurrect_old_task(self):
        now=[0];s=ConversationStore(ttl=10,clock=lambda:now[0]);commit(s,'VALORANT controls')
        now[0]=11
        self.assertEqual(s.begin('s','resume','back to the controls',locale='en')['plan']['message_key'],'no_previous_task')

    def test_stale_completion_cannot_replace_memory(self):
        s=ConversationStore();p=s.begin('s','old','VALORANT controls',locale='en');commit(s,'Beat Saber controls')
        self.assertFalse(s.complete('s','old',p['revision'],response('VALORANT controls')))
        self.assertEqual(s.snapshot('s')['requested_tasks'][0]['targets'],['Beat Saber'])

    def test_duplicate_turn_has_no_new_revision_and_replay_is_identical(self):
        s=ConversationStore();commit(s,'VALORANT controls');before=s.snapshot('s')
        duplicate=s.begin('s','1','VALORANT controls',locale='en')
        self.assertEqual(s.snapshot('s'),before)
        self.assertEqual(duplicate['response']['request_id'],'1')
        with self.assertRaises(TurnConflict):s.begin('s','1','Beat Saber controls',locale='en')

    def test_client_fallback_history_cannot_create_archive(self):
        s=ConversationStore();h=s.history('s',[{'role':'assistant','text':'VALORANT controls','route_category':'games','mode':'pipeline:structured_game_controls','delivery_status':'client_acknowledged'}])
        self.assertEqual(h[0]['delivery_status'],'uncertain')
        self.assertEqual(s.begin('s','1','back to the controls',locale='en',history=h)['plan']['message_key'],'no_previous_task')

    def test_new_target_number_negation_are_not_replaced_with_old_query(self):
        s=ConversationStore();commit(s,'VALORANT controls');record=s._sessions['s']
        for q in ('back to controls for Beat Saber','back to prices for PC','back to rules 2027','back to controls not VALORANT'):
            self.assertEqual(resolve_memory(q,record,locale='en'),(None,None),q)
        r,p=resolve_memory('back to controls for tomorrow',record,locale='en')
        self.assertEqual(p['message_key'],'scope')

    def test_compound_memory_keeps_both_selected_games(self):
        s=ConversationStore();p=s.begin('s','1','VALORANT and Beat Saber controls',locale='en')
        b=response('VALORANT and Beat Saber controls',category='multi_question',mode='pipeline:multi_question_splitter',rid='1')
        b['task_contract']=compound_contract(['VALORANT controls','Beat Saber controls'],[child(),child()])
        s.complete('s','1',p['revision'],b);s.acknowledge('s','1')
        self.assertEqual(s.snapshot('s')['requested_tasks'][0]['targets'],['VALORANT','Beat Saber'])
        for q in ('all of them','back to the controls'):
            p=s.begin('s',q,q,locale='en')
            self.assertEqual(p['plan']['targets'],['VALORANT','Beat Saber'])
            self.assertEqual(len(p['plan']['requests']),2)

    def test_compound_different_operations_all_needs_scope(self):
        s=ConversationStore();p=s.begin('s','1','controls and prices',locale='en')
        c=compound_contract(['VALORANT controls','PC prices'],[child(),child()]);c['tasks'][1].update(category='service_fee',intent='service_fee_query',mode='pipeline:structured_service_fee_conversation')
        b=response('controls and prices',category='multi_question',mode='pipeline:multi_question_splitter',rid='1');b['task_contract']=c
        s.complete('s','1',p['revision'],b);s.acknowledge('s','1')
        self.assertEqual(s.begin('s','2','all of them',locale='en')['plan']['message_key'],'scope')

    def test_partial_compound_all_does_not_drop_the_unknown_child(self):
        s=ConversationStore();p=s.begin('s','1','VALORANT and Minecraft controls',locale='en')
        b=response('VALORANT and Minecraft controls',category='multi_question',mode='pipeline:multi_question_splitter',rid='1')
        b['task_contract']=compound_contract(['VALORANT controls','Minecraft controls'],[child(),child('pipeline:game_controls_target_unconfirmed',typ='no_answer')])
        s.complete('s','1',p['revision'],b);s.acknowledge('s','1')
        for q in ('all of them','back to the controls'):
            p=s.begin('s',q,q,locale='en')
            self.assertEqual(len(p['plan']['requests']),2)
            self.assertIn('Minecraft',p['plan']['requests'][1])

    def test_generic_game_examples_are_not_selected_targets(self):
        b=response('Show game controls',mode='pipeline:game_control_missing_game_context');b['answer']='For example VALORANT or Beat Saber'
        t=task_from_response('Show game controls',b)
        self.assertEqual(t['targets'],[]);self.assertEqual(t['offered_options'],[])

    def test_family_ordinals_follow_display_order_not_alias_order(self):
        b=response('Call of Duty controls',mode='pipeline:game_family_clarification_en');b['answer']='1. Call of Duty: Warzone\n2. Call of Duty: Modern Warfare III'
        t=task_from_response('Call of Duty controls',b);t['acknowledged']=True
        self.assertEqual(t['offered_options'],['Call of Duty: Warzone','Call of Duty: Modern Warfare III'])
        record={'task_memory':{t['key']:t},'current_task_keys':[t['key']]}
        for q in ('the first one','อันแรก'):
            r,p=resolve_memory(q,record,locale='en');self.assertIn('Warzone',r['resolved_question']);self.assertNotIn('Modern Warfare',r['resolved_question'])
        r,p=resolve_memory('the fourth one',record,locale='en');self.assertEqual(p['message_key'],'ordinal_axis')

    def test_actual_family_prompts_in_both_languages_offer_ordinals(self):
        for q,lang in [('Call of Duty controls','en'),('Call of Duty มีปุ่มอะไรบ้าง','th')]:
            result=answer(q,locale=lang,experimental_allow_llm=False)
            b=response(q,category=result.route.category,mode=result.mode,intent=result.route.intent);b['answer']=result.answer
            t=task_from_response(q,b);self.assertIsNotNone(t)
            self.assertEqual(t['targets'],[]);self.assertEqual(len(t['offered_options']),2)
            t['acknowledged']=True;record={'task_memory':{t['key']:t},'current_task_keys':[t['key']]}
            r,p=resolve_memory('the second one',record,locale=lang)
            self.assertIn(t['offered_options'][1],r['resolved_question'])
            r,p=resolve_memory('all of them',record,locale=lang)
            self.assertEqual(len(p['requests']),2)

    def test_unknown_title_after_known_controls_never_inherits_game(self):
        from app.session.context_resolver import resolve_question_with_context
        history=[{'role':'user','text':'VALORANT มีปุ่มอะไรบ้าง'}, {'role':'assistant','text':'VALORANT controls',
            'route_category':'games','route_intent':'game_control_lookup','mode':'pipeline:structured_game_controls','resolved_text':'VALORANT มีปุ่มอะไรบ้าง'}]
        for q in ('Minecraft มีปุ่มอะไรบ้าง','มายคราฟต์มีปุ่มอะไรบ้าง'):
            r=resolve_question_with_context(q,history,locale='th')
            self.assertEqual(r.resolved_question,q);self.assertFalse(r.used_context)

    def test_timeout_retains_executed_and_pending_child_evidence(self):
        pipeline=AnswerQualityPipeline();calls=[0]
        def exceeded(*args):
            calls[0]+=1
            return calls[0]==2
        sample=answer('VALORANT controls',locale='en',experimental_allow_llm=False)
        with patch.object(pipeline,'_compound_children_are_deterministic',return_value=False), patch.object(pipeline,'_deadline_is_exceeded',side_effect=exceeded), patch.object(pipeline,'_answer_single',return_value=sample):
            result=pipeline._answer_multi('two requests',['VALORANT controls','Beat Saber controls'],experimental_allow_llm=False,experimental_rag_fallback=False)
        c=next(t.metadata for t in result.trace if t.stage=='task_answer_contract')
        self.assertEqual(c['executed_task_ids'],['task-1']);self.assertEqual(c['pending_task_ids'],['task-2'])
        self.assertEqual(c['outcome'],'unavailable');self.assertTrue(c['output_withheld'])

    def test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit(self):
        s=ConversationStore();commit(s,'What games are available in PC?',mode='pipeline:structured_games_catalog_en',intent='games_lookup')
        for q in ('all of them','the first one'):
            p=s.begin('s',q,q,locale='en');self.assertIn(p['plan']['message_key'],('scope','ordinal_axis'))
        p=s.begin('s','zones','all zones',locale='en');self.assertEqual(p['context_resolution']['reason'],'explicit_all_catalog_zones')

    def test_all_over_four_targets_does_not_drop_remainder(self):
        t=task_from_response('VALORANT controls',response('VALORANT controls'));t.update(acknowledged=True,targets=['a','b','c','d','e'])
        r,p=resolve_memory('all of them',{'task_memory':{t['key']:t},'current_task_keys':[t['key']]},locale='en')
        self.assertEqual(p['message_key'],'scope')

    def test_task_memory_is_bounded_and_snapshot_has_no_cached_answer(self):
        s=ConversationStore(max_sessions=1);commit(s,'VALORANT controls')
        snap=s.snapshot('s');self.assertFalse(snap['survives_server_restart']);self.assertNotIn('answer',snap['requested_tasks'][0])
        s.begin('other','1','anything',locale='en');self.assertNotIn('s',s._sessions)

    def test_contract_distinguishes_answer_missing_clarification_and_backend_failure(self):
        results=[child(),child('pipeline:game_controls_target_unconfirmed',typ='no_answer'),child('pipeline:game_control_missing_game_context',typ='clarification'),child('pipeline:backend_timeout',typ='no_answer')]
        c=compound_contract(['one','two','three','four'],results)
        self.assertEqual([t['status'] for t in c['tasks']],['answered','missing','clarification','unavailable'])
        self.assertEqual(c['outcome'],'answered_partial');self.assertEqual(c['expected_task_ids'],c['executed_task_ids'])

    def test_unexecuted_children_are_pending_not_answered(self):
        c=compound_contract(['one','two'],[child()])
        self.assertEqual(c['pending_task_ids'],['task-2']);self.assertEqual(c['outcome'],'answered_partial')

    def test_full_rule_first_page_is_partial_when_clauses_remain(self):
        r=child(trace=[PipelineTrace('competition_full_coverage','page',1,metadata={'remaining_ids':['rule-9']})])
        c=single_contract(r.mode,r.route,r.validation,r.hits,r.trace)
        self.assertEqual(c['status'],'partial');self.assertEqual(c['outcome'],'answered_partial')

    def test_final_language_veto_cannot_claim_complete_coverage(self):
        answer('VALORANT controls',locale='en',experimental_allow_llm=False)
        trace=[PipelineTrace('task_answer_contract','answered_complete',1,metadata={'kind':'compound','outcome':'answered_complete'})]
        from app.core.locale import resolve_locale
        with patch('app.pipeline.engine.current_locale_decision',return_value=resolve_locale('',requested='en')):
            result=AnswerQualityPipeline._build_result('ภาษาไทยที่ผิดภาษา',[],time.perf_counter(),'pipeline:multi_question_splitter',1,
                PipelineRoute('multi_question','multi_question_split',1,'summary','low','fixture'),EntityBundle(),ValidationResult(True),trace)
        self.assertEqual(result.mode,'pipeline:answer_contract_no_answer')
        self.assertEqual(next(t.metadata for t in result.trace if t.stage=='task_answer_contract')['outcome'],'schema_rejected')

if __name__=='__main__':unittest.main()
