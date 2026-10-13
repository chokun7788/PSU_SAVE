"""Request replay, content distinctions and state invariants with bounded fixtures."""
import os,sys,copy,json,time,threading,unittest
from pathlib import Path
from unittest.mock import patch
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0')
from app.session.conversation_store import ConversationStore
from app.session.context_resolver import ResolvedQuestion
from app.session.task_memory import task_from_response,resolve_memory
from app.pipeline.engine import answer_question_pipeline_debug as answer
from app.pipeline.task_contract import compound_contract
from app.pipeline.schemas import PipelineRoute,PipelineTrace,ValidationResult
from app.core.normalization import normalize_text
from app.pipeline.protected_intents import is_weekly_booking_window_query,is_maximum_booking_lead_query

def body(query,category='schedule',intent='schedule_query',mode='pipeline:structured_schedule',rid='r'):
    return dict(ok=True,request_id=rid,answer='source body',resolved_question=query,route_category=category,route_intent=intent,mode=mode)
def execute(s,q,lang='en',sid='s'):
    from dataclasses import asdict
    n=str(s.snapshot(sid)['revision']+1);h=s.history(sid);p=s.begin(sid,n,q,locale=lang,history=h)
    r=ResolvedQuestion(**p['context_resolution']) if p.get('context_resolution') else ResolvedQuestion(q,q,False)
    result=answer(r.resolved_question,locale=lang,request_plan=p['plan'],recent_history=h,experimental_allow_llm=False)
    b=body(r.resolved_question,result.route.category,result.route.intent,result.mode,n);b['answer']=result.answer
    b['trace']=[asdict(t) for t in result.trace];b['task_contract']=next(t.metadata for t in result.trace if t.stage=='task_answer_contract')
    s.complete(sid,n,p['revision'],b,plan=p['plan']);s.acknowledge(sid,n)
    return result,p
def mock_commit(s,q,category,intent,mode):
    n=str(s.snapshot('s')['revision']+1);p=s.begin('s',n,q,locale='en');b=body(q,category,intent,mode,n)
    s.complete('s',n,p['revision'],b);s.acknowledge('s',n)

class DomainResumeR42Tests(unittest.TestCase):
    def test_completed_turn_is_immutable_and_history_not_duplicated(self):
        s=ConversationStore();p=s.begin('s','t','opening hours',locale='en');b=body('opening hours')
        self.assertTrue(s.complete('s','t',p['revision'],b));s.acknowledge('s','r')
        before=s.snapshot('s');changed={**b,'request_id':'second','answer':'second body'}
        self.assertFalse(s.complete('s','t',p['revision'],changed))
        self.assertEqual(len(s.history('s')),2);self.assertEqual(s.snapshot('s'),before)
        self.assertEqual(s.begin('s','t','opening hours',locale='en')['response']['request_id'],'r')

    def test_concurrent_callbacks_only_one_commit_wins(self):
        s=ConversationStore();p=s.begin('s','t','opening hours',locale='en');barrier=threading.Barrier(2)
        def commit(rid):barrier.wait();return s.complete('s','t',p['revision'],body('opening hours',rid=rid))
        with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(commit,['a','b']))
        self.assertEqual(sorted(results),[False,True]);self.assertEqual(len(s.history('s')),2)

    def test_members_and_contact_have_archives_without_aliasing_to_price(self):
        for q,cat,intent,mode,command,domain in [
            ('How many member groups are there?','overview','members_lookup','pipeline:structured_member_group_count_en','back to the member list','members'),
            ('How can I contact the studio?','contact','contact_methods','pipeline:rule_en','back to the contact details','contact')]:
            s=ConversationStore();mock_commit(s,q,cat,intent,mode);mock_commit(s,'VALORANT controls','games','game_control_lookup','pipeline:structured_game_controls')
            r=s.begin('s','return',command,locale='en');self.assertEqual(r['context_resolution']['context_domain'],domain)
            self.assertEqual(r['context_resolution']['resolved_question'],q)

    def test_booking_return_requires_scope_when_two_operations_exist(self):
        s=ConversationStore();mock_commit(s,'How to book PC?','reservation','booking_policy','pipeline:booking_fast_path')
        mock_commit(s,'PC1 free now?','schedule','live_booking_status','pipeline:live_booking_status_fast_path')
        p=s.begin('s','return','back to booking',locale='en');self.assertEqual(p['plan']['message_key'],'booking_scope')
        p=s.begin('s','return-policy','back to the booking process',locale='en');self.assertEqual(p['context_resolution']['resolved_question'],'How to book PC?')

    def test_unacknowledged_and_cross_session_new_domains_cannot_resume(self):
        s=ConversationStore();p=s.begin('s','a','How can I contact the studio?',locale='en')
        s.complete('s','a',p['revision'],body('How can I contact the studio?','contact','contact_methods','pipeline:rule_en'))
        for sid in ('s','other'):
            p=s.begin(sid,'r','back to the contact details',locale='en');self.assertEqual(p['plan']['message_key'],'no_previous_task')

    def test_new_conditions_do_not_disappear_on_resume(self):
        s=ConversationStore();mock_commit(s,'studio opening hours','schedule','schedule_query','pipeline:structured_schedule')
        record=s._sessions['s']
        for command in ('back to the opening hours tomorrow','กลับไปเรื่องเวลาเปิดปิดของพรุ่งนี้'):
            r,p=resolve_memory(command,record,locale='en');self.assertEqual(p['message_key'],'scope')
        for command in ('back to opening hours on 2026-10-08','back to booking for PC1 at 15:00'):
            self.assertEqual(resolve_memory(command,record,locale='en'),(None,None))

    def test_mixed_return_domains_clarify_instead_of_choosing_first(self):
        s=ConversationStore();mock_commit(s,'studio opening hours','schedule','schedule_query','pipeline:structured_schedule')
        p=s.begin('s','r','back to opening hours and contact details',locale='en')
        self.assertEqual(p['plan']['message_key'],'scope')

    def test_correct_thai_open_close_cues_are_not_corrupted_by_fuzzy_rewrite(self):
        for q in ('เวลาเปิดปิด','เวลาเปิดปิดศูนย์','เปิดปิดกี่โมง','วันนี้ศูนย์เปิดหรือปิด','เวลาเปิดและเวลาปิด'):
            self.assertEqual(normalize_text(q),q)
        s=ConversationStore();mock_commit(s,'เวลาเปิดปิดศูนย์','schedule','schedule_query','pipeline:structured_schedule')
        p=s.begin('s','r','กลับไปเรื่องเวลาเปิดปิด',locale='th');self.assertEqual(p['context_resolution']['resolved_question'],'เวลาเปิดปิดศูนย์')

    def test_maximum_days_and_minimum_hour_are_different_facets(self):
        for q,lang in [('How many days ahead can I book?','en'),('จองล่วงหน้าได้กี่วัน','th')]:
            self.assertTrue(is_maximum_booking_lead_query(q));self.assertFalse(is_weekly_booking_window_query(q))
            r=answer(q,locale=lang,experimental_allow_llm=False)
            self.assertIn('booking_maximum_lead_unconfirmed',r.mode)
            self.assertEqual(next(t.metadata['status'] for t in r.trace if t.stage=='task_answer_contract'),'missing')
            self.assertNotIn('Regular booking/service periods',r.answer)
        for q in ('What days can I book?','Which days and hours are bookable?'):
            self.assertTrue(is_weekly_booking_window_query(q));self.assertFalse(is_maximum_booking_lead_query(q))
        for q,lang in [('How far in advance must I book?','en'),('ต้องจองก่อนใช้งานกี่ชั่วโมง','th')]:
            self.assertFalse(is_maximum_booking_lead_query(q))
            r=answer(q,locale=lang,experimental_allow_llm=False);self.assertNotIn('maximum_lead_unconfirmed',r.mode)
        for q in ('How far ahead must I book?','How many days in advance can I cancel my booking?',
                  'จองได้สูงสุดกี่เครื่อง','ต้องจองล่วงหน้ากี่วัน'):
            self.assertFalse(is_maximum_booking_lead_query(q),q)
        for q in ('จองล่วงหน้าได้สูงสุดกี่วัน','What is the maximum advance booking limit?'):
            self.assertTrue(is_maximum_booking_lead_query(q),q)

    def test_member_group_count_is_not_person_count(self):
        for q in ('How many member groups are there?','How many groups of members are there?'):
            r=answer(q,locale='en',experimental_allow_llm=False);self.assertIn('structured_member_group_count',r.mode)
            self.assertIn('3 groups',r.answer);self.assertIn('25 member records',r.answer)
        r=answer('How many members are there?',locale='en',experimental_allow_llm=False)
        self.assertIn('structured_member_count',r.mode)

    def test_booking_policy_fields_answer_the_actual_requested_quantity(self):
        for q,lang in [('How far ahead must I book?','en'),('ต้องจองล่วงหน้ากี่วัน','th'),
                       ('How many days in advance can I cancel my booking?','en'),('ต้องยกเลิกจองล่วงหน้ากี่วัน','th')]:
            self.assertFalse(is_weekly_booking_window_query(q),q)
            r=answer(q,locale=lang,experimental_allow_llm=False)
            self.assertEqual(r.route.category,'reservation',q)
            self.assertIn('1 hour' if lang=='en' else '1 ชั่วโมง',r.answer,q)
            self.assertNotIn('booking_steps',r.route.intent,q)
        for q,lang in [('จองได้สูงสุดกี่เครื่อง','th'),('What is the maximum number of devices I can book?','en')]:
            r=answer(q,locale=lang,experimental_allow_llm=False)
            self.assertIn('booking_maximum_resources_unconfirmed',r.mode,q)
            self.assertEqual(next(t.metadata['status'] for t in r.trace if t.stage=='task_answer_contract'),'missing')

    def test_same_operation_compound_resume_reexecutes_every_child(self):
        s=ConversationStore();p=s.begin('s','a','two schedules',locale='en')
        questions=['What are the studio opening hours?','What are the Friday opening hours?']
        results=[answer(q,locale='en',experimental_allow_llm=False) for q in questions]
        b=body('; '.join(questions),'multi_question','multi_question_split','pipeline:multi_question_splitter','a');b['task_contract']=compound_contract(questions,results)
        s.complete('s','a',p['revision'],b);s.acknowledge('s','a')
        mock_commit(s,'VALORANT controls','games','game_control_lookup','pipeline:structured_game_controls')
        p=s.begin('s','r','back to the opening hours',locale='en');self.assertEqual(p['plan']['schema_type'],'dialogue_resume_v1')
        result=answer(p['context_resolution']['resolved_question'],locale='en',request_plan=p['plan'],experimental_allow_llm=False)
        c=next(t.metadata for t in result.trace if t.stage=='task_answer_contract')
        self.assertEqual(len(c['tasks']),2);self.assertEqual([t['category'] for t in c['tasks']],['schedule','schedule'])

    def test_raw_labels_with_comma_cannot_split_into_phantom_targets(self):
        from types import SimpleNamespace
        s=ConversationStore();p=s.begin('s','a','two requests',locale='en')
        child=SimpleNamespace(mode='pipeline:structured_schedule',route=PipelineRoute('schedule','schedule_query',1,'fact','low','fixture'),validation=ValidationResult(True),trace=[],hits=[])
        b=body('two requests','multi_question','multi_question_split','pipeline:multi_question_splitter','a')
        b['task_contract']=compound_contract(['Monday, regular hours','Friday, regular hours'],[child,child])
        s.complete('s','a',p['revision'],b);s.acknowledge('s','a')
        p=s.begin('s','r','back to the opening hours',locale='en')
        self.assertEqual(p['plan']['targets'],['Monday, regular hours','Friday, regular hours'])
        self.assertEqual(len(p['plan']['requests']),2)

    def test_invalid_or_excess_resume_plan_cannot_fall_through_to_unrelated_answer(self):
        for plan in (dict(schema_type='dialogue_resume_v1',schema_version=1,domain='general',operation='chat',requests=['hello']),
            dict(schema_type='dialogue_resume_v1',schema_version=1,domain='schedule',operation='schedule_lookup',requests=['hours']*5)):
            r=answer('back to opening hours',locale='en',request_plan=plan,experimental_allow_llm=False)
            self.assertEqual(r.mode,'pipeline:dialogue_state_clarification')

    def test_live_booking_resume_fetches_again_instead_of_replaying_old_status(self):
        from app.booking.live_status import _snapshot_from_payload
        from tests.smoke_test_live_booking_status import LIVE_PAYLOAD
        fixture=copy.deepcopy(LIVE_PAYLOAD)
        for resource in fixture['resources']:
            if resource['resource_id']=='pc-01':
                resource.update(status='available',available_now=1)
                for slot in resource['slots']:slot.update(status='available',available_count=1,booked_count=0)
        free=_snapshot_from_payload(fixture);busy=_snapshot_from_payload(copy.deepcopy(LIVE_PAYLOAD))
        s=ConversationStore()
        with patch('app.runtime.fast_answer.get_live_booking_status',side_effect=[free,busy]) as fetch:
            first,p=execute(s,'Is PC1 available on 2026-09-17 at 14:00?')
            execute(s,'VALORANT controls')
            last,p=execute(s,'back to the booking status')
        self.assertEqual(fetch.call_count,2)
        self.assertNotEqual(first.answer,last.answer)
        self.assertIn('PC #01 is available for the full period 14:00-15:00',first.answer)
        self.assertIn('PC #01 is not available for the full period 14:00-15:00',last.answer)
        self.assertEqual(p['context_resolution']['context_domain'],'reservation')
        self.assertEqual(p['context_resolution']['resolved_question'],'Is PC1 available on 2026-09-17 at 14:00?')

    def test_iso_dates_are_not_hour_ranges_in_either_language(self):
        from app.booking.live_status import requested_time_window,_snapshot_from_payload,resolve_live_target_date
        from tests.smoke_test_live_booking_status import LIVE_PAYLOAD
        snapshot=_snapshot_from_payload(copy.deepcopy(LIVE_PAYLOAD))
        for q in ('Is PC1 available on 2026-09-17 at 14:00?','วันที่ 2026-09-17 PC1 ว่างตอน 14:00 ไหม',
                  '2026-05-18 PC1 free at 14:00','PC1 ว่างไหม 2026-10-01 เวลา 14:00'):
            self.assertEqual(requested_time_window(q,snapshot).start,'14:00',q)
        for q in ('PC1 2026-09-17 14:00-15:00','PC1 2026-09-17 from 14 to 15'):
            w=requested_time_window(q,snapshot);self.assertEqual((w.start,w.end),('14:00','15:00'))
        implicit=requested_time_window('PC1 free on 2026-09-17?',snapshot)
        self.assertFalse(implicit.explicit)
        self.assertEqual(implicit.start,'14:30')
        self.assertEqual(resolve_live_target_date('PC1 on 2026-09-17 at 14:00'),'2026-09-17')

    def test_polite_resume_prefix_keeps_acknowledged_task(self):
        s=ConversationStore();mock_commit(s,'studio opening hours','schedule','schedule_query','pipeline:structured_schedule')
        for q in ('please go back to the earlier service hours','please return to the previous opening hours'):
            r,p=resolve_memory(q,s._sessions['s'],locale='en')
            self.assertTrue(r['used_context']);self.assertEqual(r['resolved_question'],'studio opening hours')

    def test_same_intent_repeated_questions_split_without_splitting_noun_lists(self):
        from app.pipeline.engine import _split_english_compound_question
        for q in ('What are the studio opening hours and what are the Friday opening hours?',
                  'What are the studio opening hours? What are the Friday opening hours?'):
            self.assertEqual(len(_split_english_compound_question(q)),2)
        for q in ('What are the opening and closing hours?',
                  'What are the board and mini games controls in Mario Party Superstars?'):
            self.assertEqual(len(_split_english_compound_question(q)),1)

if __name__=='__main__':unittest.main()
