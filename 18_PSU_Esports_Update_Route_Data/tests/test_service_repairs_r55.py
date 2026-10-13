import unittest
from unittest.mock import patch
from app.booking.live_status import _requested_resource_number,_snapshot_from_payload,render_live_booking_answer,_slot_window_for_resources,TimeWindow
from app.calculator.service_fee import _detect_minutes
from app.pipeline.user_service_facts import answer_user_service_facts
from app.pipeline.service_query_completion import split_service_operations,answer_explicit_source_operation,answer_budget
from app.session.conversation_plan import resolve_request_plan,customer_filter
from app.session.context_resolver import resolve_question_with_context
from app.pipeline.competition_conversation_signals import is_more_rule_request
from app.pipeline.conversation_rules import build_full_rule_answer,rulebook_manifest
from app.pipeline.competition_targets import resolve_competition_targets
from app.rules.matcher import RuleMatcher

class ServiceRepairsR55(unittest.TestCase):
    def test_station_numbers_do_not_consume_quantity_or_clocks(self):
        for q in ('VR9:00','VR 09:30','VR 30นาที','VR 9 pm','VR 2 hours','VR 100บาท','VR 4คน'):
            with self.subTest(q=q):self.assertIsNone(_requested_resource_number(q,'vr'))
        for q,n in (('PC1',1),('PC10',10),('VR#1 เวลา09:00',1),('Cockpit #2 10:00',2)):
            with self.subTest(q=q):self.assertEqual(_requested_resource_number(q, 'pc' if q.startswith('PC') else 'vr' if q.startswith('VR') else 'cockpit'),n)
    def test_duration_words_and_eligibility(self):
        for q,n in (('two hours',120),('สองชั่วโมง',120),('three hours',180),('one hour',60),('30 minutes',30)):
            with self.subTest(q=q):self.assertEqual(_detect_minutes(q),n)
        self.assertEqual(customer_filter('General adult PC')[1],['general_adult'])
        self.assertEqual(customer_filter('I am not a student')[0],'non_student_unspecified')
    def test_policy_subjects_and_nearby_unknowns(self):
        cases=[('อัพสลิปผืด ส่งใหม่ทางไหน','wrong_slip'),('เพื่อนยังมาไม่ถึง เช็คอินให้ทั้งแก๊งได้ไหม','group_checkin'),('จองชื่อเราแต่ให้เพื่อนที่ไม่มีชื่อเล่นแทนได้ไหม','player_identity'),('ไปถึงต้องเอาบัตรไรไปมั่ง','checkin_documents'),('มา4คน เล่นอันไหนดี','four_people'),('we are 4 ppl what can we play','four_people'),('which documnts do i bring for checkin','checkin_documents'),('Is there seating where I can rest while waiting for friends?','rest_seating')]
        for q,key in cases:
            with self.subTest(q=q):
                result=answer_user_service_facts(q,'en' if q.isascii() else 'th');self.assertIsNotNone(result)
                self.assertIn(key,result['trace'][0].metadata['claim_ids'])
        self.assertIn('spectator_fee',answer_user_service_facts('นั่งดูเพื่อนต้องเสียเงินไหม')['validation'].warnings)
        self.assertIn('personal_controller_permission',answer_user_service_facts('เอาจอยตัวเองมาได้ไหม')['validation'].warnings)
    def test_price_two_hours(self):
        plan=resolve_request_plan('General adult PC for two hours, how much?',[],locale='en')
        self.assertEqual(plan['tasks'][0]['filters']['duration_minutes'],120)
        self.assertEqual(plan['tasks'][0]['filters']['customer_group_ids'],['general_adult'])
    def test_affordability_known_zero_and_missing_groups(self):
        for q,l in [('บุคคลทั่วไปมี100บาทเล่นPCได้กี่รอบ','th'),('I have 100 THB and want to play PC as a general adult. How many sessions can I afford?','en')]:
            with self.subTest(q=q):
                result=answer_budget(q,l);row=result['trace'][0].metadata['packages'][0]
                self.assertEqual((row['sessions'],row['remainder']),(1,30))
        self.assertEqual(answer_budget('I have 100 THB for PC','en')['route'].category,'clarification')
        result=answer_budget('PSU staff have 100 THB for PC','en');self.assertIsNone(result['trace'][0].metadata['packages'][0]['sessions'])
        self.assertIsNone(answer_budget('โอน100บาทแล้วผิดสลิป','th'))
    def test_clause_subjects_operations_and_time(self):
        cases=[('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่',2),('What games are on PC, and how much does two hours cost for a general adult?',2),('วันนี้ PC1 เวลา10โมง และ PC2 เวลา11โมงว่างไหม',2),('ชำระเงินยังไง จ่ายเงินสดได้ไหม',2),('Where is the studio and when does it open?',2)]
        for q,n in cases:
            with self.subTest(q=q):self.assertEqual(len(split_service_operations(q)),n)
        parts=split_service_operations('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่');self.assertTrue(parts[1].startswith('PC '))
        self.assertEqual(len(split_service_operations('How do I shoot and reload in CS2?')),1)
    def test_server_plan_preserves_compound(self):
        self.assertIsNone(resolve_request_plan('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่',[]))
        self.assertIsNone(resolve_request_plan('What games are on PC, and how much does two hours cost for a general adult?',[],locale='en'))
    def test_catalog_and_policy_negative_scopes(self):
        for q in ('มีเกม Minecraft ไหม','Can I install games myself?','ขอลงเกมอะไรเพิ่มได้บ้าง','ไม่เอารายการเกมอะไรแล้ว'):
            with self.subTest(q=q):self.assertIsNone(answer_explicit_source_operation(q,'en' if q.isascii() else 'th',RuleMatcher.default()))
        self.assertIn('change_time',answer_user_service_facts('อยากเปลี่ยนรอบที่จอง ต้องทำไง')['trace'][0].metadata['claim_ids'])
        self.assertIn('game_account_policy',answer_user_service_facts('เอา Steam ตัวเองล็อกอินได้ไหม')['validation'].warnings)
    def test_new_phrasings_and_capacity(self):
        p=resolve_request_plan('ขอราคาบุคคลทั่วไป',[])
        self.assertIn('service',p['tasks'][0]['pending_slots'])
        self.assertIsNone(resolve_request_plan('คอมมีเกมไรบ้าง แล้วบุคคลทั่วไปเล่นสามชั่วโมงกี่บาท',[]))
        self.assertIn('game_installation_permission',answer_user_service_facts('Can I install Minecraft myself?','en')['validation'].warnings)
        result=answer_budget('General adult budget 200 THB Nintendo Switch four people','en')
        rows=result['trace'][0].metadata['packages']
        self.assertEqual([(r['package'],r['sessions']) for r in rows],[('nintendo_switch_3_4',0)])
    def test_game_scope_task_memory(self):
        from app.session.task_memory import task_from_response,resolve_memory
        task=task_from_response('PC มีเกมอะไรบ้าง',dict(route_category='games',route_intent='game_list',mode='pipeline:source_operation_game_list',request_id='r1'))
        self.assertIsNotNone(task);self.assertEqual(task['operation'],'list')
    def test_budget_group_followup(self):
        history=[dict(role='user',text='I have 100 THB for PC'),dict(role='assistant',text='Which group?',route_category='clarification',route_intent='budget_group')]
        resolved=resolve_question_with_context('general adult',history,locale='en')
        self.assertTrue(resolved.used_context);self.assertIn('100',resolved.resolved_question)
        self.assertEqual(answer_budget(resolved.resolved_question,'en')['trace'][0].metadata['packages'][0]['sessions'],1)
    def test_catalog_totals_and_scopes(self):
        for q,l,key,count in [('Nintendo มีเกมไรมั่ง','th','Nintendo Switch',17),('Cockpit เล่นเกมอะไร','th','Cockpit',1),('What games are on PC?','en','PC',6),('ศูนย์มีเกมทั้งหมดกี่เกม','th','',42),('ที่ศูนย์มีเกมให้เล่นทั้งหมดกี่เกม','th','',42)]:
            with self.subTest(q=q):
                result=answer_explicit_source_operation(q,l,RuleMatcher.default())
                self.assertIsNotNone(result);self.assertIn(key,result['answer']);self.assertEqual(result['trace'][0].metadata['game_count'],count)
    def test_controls_actions_and_source_limit(self):
        result=answer_explicit_source_operation('How do I shoot and reload in CS2?','en',RuleMatcher.default())
        self.assertIn('Left Mouse Button',result['answer']);self.assertIn('R: Reload',result['answer']);self.assertIn('secondary',result['answer'])
    def test_control_preflight_reuses_existing_catalog_aliases(self):
        for q,game in [('ปุ่มยิงกับรีโหลดใน CS2 คืออะไร','Counter-Strike 2'),('ขอปุ่ม Tekken 8 ทั้งหมด','TEKKEN 8')]:
            with self.subTest(q=q):
                result=answer_explicit_source_operation(q,'th',RuleMatcher.default())
                self.assertEqual(result['mode'],'pipeline:source_operation_control_lookup')
                self.assertIn(game,result['answer'])
                self.assertIn('ยังไม่ได้ตรวจยืนยัน',result['answer'])
        self.assertIsNone(answer_explicit_source_operation('ขอปุ่ม CS2 กับ Tekken 8','th',RuleMatcher.default()))
    def test_explicit_booking_scope(self):
        self.assertIsNone(resolve_request_plan('จองเครื่องยังไง ขอขั้นตอนทั้งหมด',[],locale='th'))
        self.assertIn('จอง',answer_explicit_source_operation('จองเครื่องยังไง ขอขั้นตอนทั้งหมด','th',RuleMatcher.default())['answer'])
    def test_availability_followup_keeps_filters(self):
        history=[dict(role='user',text='วันที่2026-10-13 PC1 เวลา10โมงว่างไหม'),dict(role='assistant',text='answer',route_intent='live_booking_status',route_category='schedule',resolved_text='วันที่2026-10-13 PC1 เวลา10โมงว่างไหม')]
        result=resolve_question_with_context('แล้ว PC2 ล่ะ',history)
        self.assertTrue(result.used_context);self.assertIn('#2',result.resolved_question);self.assertIn('10โมง',result.resolved_question);self.assertIn('2026-10-13',result.resolved_question)
        history[-1]['context_eligible']=False
        self.assertFalse(resolve_question_with_context('แล้ว PC2 ล่ะ',history).used_context)
    def test_full_rule_coverage_does_not_skip_acknowledged_pages(self):
        self.assertTrue(is_more_rule_request('ต่อ เอากฎที่เหลือ'))
        self.assertTrue(is_more_rule_request('Continue with the remaining rules.'))
        history=[];seen=set();expected=None
        for i in range(20):
            q='กติกา CS2 ทั้งหมด' if i==0 else 'ต่อ เอากฎที่เหลือ'
            resolved=resolve_question_with_context(q,history)
            result=build_full_rule_answer(resolved.resolved_question,'th',recent_history=history)
            self.assertIsNotNone(result)
            metadata=next(t.metadata for t in result['trace'] if t.stage=='competition_full_coverage')
            returned=set(metadata['returned_ids']);self.assertFalse(seen & returned);seen |= returned
            expected=set(metadata['expected_ids'])
            history += [dict(role='user',text=q),dict(role='assistant',text=result['answer'],route_category='competition_rules',resolved_text=resolved.resolved_question,delivery_status='client_acknowledged',rule_coverage=metadata)]
            if seen==expected:break
        self.assertEqual(seen,expected);self.assertEqual(len(seen),56)
    def test_explicit_rule_overview_with_discourse_particle(self):
        from app.pipeline.competition_conversation_signals import is_broad_rule_request
        for q in ('กฎแข่ง ROV ล่ะ','กฎแข่ง CS2 ล่ะ','What about the rules for RoV?'):
            with self.subTest(q=q):
                self.assertTrue(is_broad_rule_request(q))
                r=resolve_question_with_context(q,[])
                self.assertEqual(r.reason,'canonicalized_explicit_generic_competition_rules')
                self.assertFalse(r.used_context)
        self.assertFalse(is_broad_rule_request('กฎแข่ง ROV ปี 2030 ล่ะ'))
        self.assertFalse(is_broad_rule_request('กฎแข่ง ROV เรื่องการพักเกมล่ะ'))
    def test_timeout_partial_progress_is_scoped_and_not_a_claimed_cause(self):
        import tempfile,queue,time,os
        from pathlib import Path
        from app.pipeline.performance_trace import ParentPerformanceLogger
        from app.web_api.server import _supervisor_timeout_response
        from app.core.locale import resolve_locale
        with tempfile.TemporaryDirectory(dir=os.getenv('PSU_TEST_TMP_DIR')) as folder:
            events=queue.Queue();logger=ParentPerformanceLogger(events,path=Path(folder)/'progress.jsonl');logger.start()
            events.put(dict(event='stage_finished',request_id='one',stage='retrieval',status='accepted',sequence=1,elapsed_ms=30,remaining_ms=100))
            deadline=time.monotonic()+1
            while logger.snapshot()['events_written']<1 and time.monotonic()<deadline:time.sleep(.02)
            partial=logger.request_snapshot('one');other=logger.request_snapshot('two');logger.stop()
            self.assertEqual(partial['last_reported_stage'],'retrieval');self.assertFalse(partial['cause_confirmed']);self.assertEqual(other['events'],[])
            response=_supervisor_timeout_response(request_id='one',started=time.perf_counter(),worker_id=0,locale=resolve_locale('hello',requested='en'),diagnostics={'partial_progress':partial})
            self.assertEqual(response['processing_diagnostics']['partial_progress']['last_reported_stage'],'retrieval')
    def test_vr_hour_occupancy_fixture(self):
        snapshot=_snapshot_from_payload(dict(ok=True,date='2026-10-13',now='2026-10-13 08:00:00',generated_at='2026-10-13 08:00:00',source='remote_csv_live',center=dict(open=False,reason='',open_periods=[['09:00','12:00'],['13:00','16:00']]),resources=[dict(resource_id='vr1',resource_name='VR Station #1 Morning',capacity=1,status='available',available_now=1,slots=[dict(start='09:00',end='09:30',status='available',available_count=1,booked_count=0,no_show_count=0),dict(start='09:30',end='10:00',status='busy',available_count=0,booked_count=1,no_show_count=0)])]))
        self.assertEqual(_slot_window_for_resources(snapshot.resources,TimeWindow('09:00','09:30',True)).label,'09:00-10:00')
        for q,l in [('วันที่2026-10-13 VR9:00-9:30 ว่างไหม','th'),('Is VR available on 2026-10-13 from 09:00 to 09:30?','en')]:
            with self.subTest(q=q):
                answer=render_live_booking_answer(q,snapshot,l);self.assertNotIn('#9',answer);self.assertIn('09:00-10:00',answer);self.assertIn('0/1',answer)
if __name__=='__main__':unittest.main()
