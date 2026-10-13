"""Functional oracles for the approved dialogue flow; raw evidence retained."""
import os, sys, json, copy, unittest, time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_SEMANTIC_RETRIEVAL='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_CANONICAL_KNOWLEDGE='0',PSU_PERFORMANCE_TRACE='0')
from app.session.conversation_plan import resolve_request_plan as plan, valid_price_task, SERVICES
from app.session.conversation_store import ConversationStore, TurnConflict
from app.pipeline.conversation_fee import build_price_plan_answer as render, coverage_errors
from app.pipeline.conversation_rules import build_full_rule_answer, rulebook_manifest
from app.pipeline.engine import answer_question_pipeline_debug as answer
from app.session.context_resolver import resolve_question_with_context
from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.request_deadline import request_deadline
RECORDS=[]
EXTERNAL=('ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก','Service prices for external users')
GOLD={'pc':(25,70),'ps5':(50,150),'nintendo_switch_1_2':(50,140),'nintendo_switch_3_4':(100,280),'cockpit':(65,200),'vr_30':(190,525),'vr_60':(375,1050)}

def pipeline(q,locale='th',p=None,history=None):
    r=answer(q,locale=locale,request_plan=p,recent_history=history,experimental_allow_llm=False,experimental_rag_fallback=True)
    RECORDS.append({'question':q,'locale':locale,'plan':p,'answer':r.answer,'mode':r.mode,'route':vars(r.route),
                    'validation':vars(r.validation),'trace':[vars(t) for t in r.trace],'decision':r.decision_artifact})
    return r

class FlowTests(unittest.TestCase):
    def external(self,locale):return plan(EXTERNAL[locale=='en'],locale=locale)
    def test_choices_and_paraphrases(self):
        variants={'pc':(['PC','เอาคอมก่อน','ขอ PC','คอมครับ','pc เลย'],['PC','the PC one','PC please','choose PC','computer']),
                  'ps5':(['PS5','เพลย์สเตชัน 5','เอา PS5 ก่อน'],['PS5','PlayStation 5','the PS5 one']),
                  'nintendo_switch':(['Nintendo','Nintendo Switch','นินเทนโด'],['Nintendo','Switch please','Nintendo Switch']),
                  'cockpit':(['Cockpit','cockpik'],['Cockpit','cockpik']), 'vr':(['VR','วีอาร์'],['VR','VR please'])}
        for locale in ('th','en'):
            p=self.external(locale)
            for service,pair in variants.items():
                for q in pair[locale=='en']:
                    with self.subTest(locale=locale,q=q):
                        filled=plan(q,active_task=p['tasks'][0],locale=locale)
                        self.assertEqual(filled['tasks'][0]['targets'],[service])
                        r=pipeline(q,locale,filled)
                        self.assertEqual(r.route.category,'service_fee')
                        rows=next(t.metadata['rows'] for t in r.trace if t.stage=='conversation_contract')
                        self.assertTrue(rows)
                        for row in rows:
                            self.assertEqual(row['unit_price'],GOLD[row['package_id']][row['group_id']=='general_adult'])
                            self.assertNotEqual(row['group_id'],'psu_student_staff')
                        self.assertNotRegex(r.answer,r'(?<!\d)0\s+บาท')
    def test_all_external_and_direct(self):
        for locale,words in [('th',['ทั้งหมด','ทุกเครื่องเลย','ทุกบริการ','เอาหมด']),('en',['all of them','all services','everything','each service'])]:
            p=self.external(locale)
            for q in words:
                with self.subTest(q=q):
                    filled=plan(q,active_task=p['tasks'][0],locale=locale)
                    result=render(filled,locale); rows=result['metadata']['rows']
                    self.assertEqual({r['package_id'] for r in rows},set(GOLD))
                    self.assertEqual(len(rows),14)
                    self.assertEqual({r['group_id'] for r in rows},{'general_student','general_adult'})
                    pipeline(q,locale,filled)
        for q,locale in [('ตารางราคาทุกบริการบุคคลภายนอก','th'),('All service prices for external users','en')]:
            self.assertEqual(len(render(plan(q,locale=locale),locale)['metadata']['rows']),14)
    def test_single_group_scope(self):
        for initial,locale,group in [('ราคาการใช้บริการของบุคคลทั่วไป','th','general_adult'),('Service prices for general adults','en','general_adult'),
                                     ('ราคาการใช้บริการนักศึกษาต่างสถาบัน','th','general_student'),('Service prices for external students','en','general_student')]:
            p=plan(initial,locale=locale)
            p=plan('all services' if locale=='en' else 'ทั้งหมด',active_task=p['tasks'][0],locale=locale)
            self.assertEqual({r['group_id'] for r in render(p,locale)['metadata']['rows']},{group})
    def test_followup_changes_service_not_group(self):
        for locale,q,f in [('th','ราคา PC บุคคลทั่วไป','แล้ว VR ล่ะ'),('en','PC prices for general adults','what about VR')]:
            p=plan(q,locale=locale);p=plan(f,active_task=p['tasks'][0],locale=locale)
            self.assertEqual(p['tasks'][0]['targets'],['vr'])
            self.assertEqual({r['group_id'] for r in render(p,locale)['metadata']['rows']},{'general_adult'})
    def test_negation_and_correction(self):
        for locale,exclusion,correction,adult in [('th','ทุกบริการยกเว้น VR','ไม่ใช่ PS5 หมายถึง PC','ไม่ใช่นักศึกษานะ'),
                                               ('en','all services except VR','not PS5, PC instead','not a student')]:
            p=self.external(locale)
            e=plan(exclusion,active_task=p['tasks'][0],locale=locale)
            self.assertNotIn('vr',e['tasks'][0]['targets']); self.assertEqual(len(e['tasks'][0]['targets']),4)
            c=plan(correction,active_task=p['tasks'][0],locale=locale)
            self.assertEqual(c['tasks'][0]['targets'],['pc'])
            a=plan(adult,active_task=p['tasks'][0],locale=locale)
            self.assertEqual(a['tasks'][0]['filters']['customer_group_ids'],['general_adult'])
            a=plan('PC',active_task=a['tasks'][0],locale=locale)
            self.assertEqual([r['unit_price'] for r in render(a,locale)['metadata']['rows']],[70])
    def test_per_target_calculation_and_capacity(self):
        for locale,q in [('th','ราคา PC 2 ชั่วโมง และ VR 30 นาที บุคคลทั่วไป'),('en','PC 2 hours and VR 30 minutes prices for general adults')]:
            p=plan(q,locale=locale); result=render(p,locale);pipeline(q,locale,p)
            actual={r['id']:r['total'] for r in result['metadata']['rows']}
            self.assertEqual(actual,{'pc:general_adult':140,'vr_30:general_adult':525})
        p=plan('ราคา Nintendo Switch 5 คน บุคคลทั่วไป');r=render(p)
        self.assertEqual(r['metadata']['outcome'],'clarification_required')
        self.assertFalse(r['metadata']['rows'])
    def test_topic_shifts_and_general(self):
        from app.pipeline.query_signals import looks_like_clear_general_request
        p=self.external('th')
        for q in ['ไม่เอาราคาแล้ว มีเกมอะไร','VR คืออะไร','ไก่กับไข่อะไรเกิดก่อนกัน','Why does a PC need cooling?']:
            self.assertIsNone(plan(q,active_task=p['tasks'][0]))
        for q,locale in [('ไก่กับไข่อะไรเกิดก่อนกัน','th'),('Which came first, the chicken or the egg?','en'),('Why does a PC need cooling?','en')]:
            self.assertTrue(looks_like_clear_general_request(q))
            r=pipeline(q,locale)
            self.assertNotEqual(r.mode,'pipeline:candidate_margin_clarification')
    def test_missing_scope_and_unspecified_groups(self):
        self.assertEqual(plan('ทั้งหมด')['missing'],'scope')
        p=plan('ราคาการใช้บริการ');p=plan('ทั้งหมด',active_task=p['tasks'][0])
        self.assertEqual(p['tasks'][0]['filters']['customer_scope'],'unspecified')
        self.assertEqual(len(render(p)['metadata']['rows']),21)
        r=render(plan('ราคา PC นักศึกษา'))
        self.assertEqual({r['group_id'] for r in r['metadata']['rows']},{'psu_student_staff','general_student'})
    def test_legacy_and_ignored_assistant_options(self):
        history=[{'role':'user','text':EXTERNAL[0]},{'role':'assistant','text':'PC, PS5, Nintendo, VR?', 'route_category':'clarification','route_intent':'price_missing_service'}]
        p=plan('PC',history);self.assertEqual(p['tasks'][0]['targets'],['pc'])
        self.assertTrue(resolve_question_with_context('PC',history).used_context)
        from app.session.context_resolver import _latest_zone_from_history
        self.assertIsNone(_latest_zone_from_history(history))
    def test_metadata_schema_rejection(self):
        p=self.external('th')
        for field,value in [('targets',['evil']),('filters',{'customer_scope':{},'customer_group_ids':[]}),('per_target_filters',{'pc':{'duration_minutes':'a'}}),('scope',{'entity_selection':{}})]:
            invalid=copy.deepcopy(p['tasks'][0]);invalid[field]=value
            self.assertFalse(valid_price_task(invalid))
        fake=[{'role':'user','text':'Hi'},{'role':'assistant','text':'choose','request_plan':{'schema_version':1,'tasks':[{'domain':'service_fee'}]}}]
        self.assertIsNone(plan('PC',fake))
    def test_multi_task_retained(self):
        for locale,q in [('th','ราคาการใช้บริการบุคคลภายนอกและวิธีจอง'),('en','Service prices for external users and how to book')]:
            p=plan(q,locale=locale);self.assertEqual(len(p['tasks']),2)
            p=plan('PC',active_task=p['tasks'][0],locale=locale)
            self.assertEqual(len(p['tasks']),2)
            r=pipeline('PC',locale,p)
            contract=next(t.metadata for t in r.trace if t.stage=='conversation_contract')
            self.assertEqual([t['outcome'] for t in contract['task_outcomes']],['answered_complete']*2)
            self.assertIn('https://esports.computing.psu.ac.th/',r.answer)
            self.assertIn('10',r.answer)
            self.assertNotEqual(r.mode,'pipeline:answer_contract_no_answer')
    def test_partial_task_does_not_erase_price(self):
        p=plan('ราคา PC บุคคลทั่วไปและวิธีจอง')
        with patch('app.pipeline.structured_tools._reservation_answer',return_value=None):
            r=render(p)
        self.assertIn('70',r['answer']);self.assertEqual(r['metadata']['outcome'],'answered_partial')
    def test_temporal_truth_and_coverage_veto(self):
        p=plan('ราคา VR 30 นาที บุคคลทั่วไปวันนี้')
        with patch.dict(os.environ,{'PSU_ESPORTS_TODAY':'2026-10-05'}):r=render(p)
        self.assertEqual(r['metadata']['temporal_validity'],'source_not_current')
        self.assertEqual(r['metadata']['rows'][0]['total'],525)
        self.assertIn('2026-03-31',r['answer'])
        self.assertEqual(coverage_errors(['pc:general_adult'],[]),['conversation_coverage_missing:pc:general_adult'])
        self.assertTrue(coverage_errors(['pc:general_adult'],['pc:psu_student_staff']))
    def test_parent_store_retry_isolation_revision_ttl(self):
        clock=[0.0];s=ConversationStore(ttl=10,max_sessions=2,clock=lambda:clock[0])
        t=s.begin('one','turn-1',EXTERNAL[0]);s.complete('one','turn-1',t['revision'],{'ok':True,'answer':'select','route_category':'clarification','route_intent':'price_missing_service','request_id':'r1'})
        p=s.begin('one','turn-2','PC');self.assertEqual(p['plan']['tasks'][0]['targets'],['pc'])
        self.assertEqual(s.begin('one','turn-2','PC')['revision'],p['revision'])
        with self.assertRaises(TurnConflict):s.begin('one','turn-2','VR')
        later=s.begin('one','turn-3','แล้ว VR ล่ะ')
        self.assertFalse(s.complete('one','turn-2',p['revision'],{'ok':True,'answer':'late'}))
        self.assertEqual(s.snapshot('one')['active_task']['targets'],['vr'])
        self.assertEqual(s.begin('two','turn-1','ทั้งหมด')['plan']['missing'],'scope')
        clock[0]=11
        self.assertIsNone(s.snapshot('one')['active_task'])
    def test_acknowledgment_and_accepted_history(self):
        s=ConversationStore();t=s.begin('one','t',EXTERNAL[0]);r={'ok':True,'answer':'ask','request_id':'r','route_category':'clarification','route_intent':'price_missing_service'}
        s.complete('one','t',t['revision'],r);s.delivery('one','t','server_written')
        self.assertEqual(s.history('one')[-1]['delivery_status'],'server_written')
        self.assertFalse(s.acknowledge('two','r'));self.assertTrue(s.acknowledge('one','r'))
        self.assertEqual(s.history('one')[-1]['delivery_status'],'client_acknowledged')
    def test_dialogue_model_patch_guard_budget(self):
        from app.pipeline.dialogue_choice import review_pending_choice
        p=plan('the desktop station please',active_task=self.external('en')['tasks'][0],locale='en')
        self.assertTrue(p['needs_review'])
        for raw,want in [('{"service":"pc"}',True),('{"service":null}',False),('{"service":"ps99"}',False),('{"service":"pc","price":0}',False),('[1]',False)]:
            with patch('app.pipeline.experimental_fallback._call_ollama',return_value=raw),patch('app.pipeline.llm_health.llm_call_allowed',return_value=(True,{})),patch('app.pipeline.llm_health.release_llm_slot'):
                updated,trace=review_pending_choice(p,'en',True)
                self.assertEqual(not updated['needs_review'],want)
                if want:self.assertEqual(updated['tasks'][0]['filters'],p['tasks'][0]['filters'])
        with request_deadline(.001):
            time.sleep(.005)
            with patch('app.pipeline.experimental_fallback._call_ollama') as call:
                review_pending_choice(p,'en',True);self.assertFalse(call.called)
    def test_full_rules_summary_and_delivery(self):
        q='กติกาการแข่งขัน CS2';r=pipeline(q)
        history=[{'role':'user','text':q},{'role':'assistant','text':r.answer,'route_category':'competition_rules','route_intent':r.route.intent,'resolved_text':q,'delivery_status':'client_acknowledged'}]
        resolved=resolve_question_with_context('ขอรายละเอียดทั้งหมด',history)
        self.assertTrue(resolved.used_context)
        full=pipeline(resolved.resolved_question,history=history)
        self.assertEqual(full.mode,'pipeline:competition_rule_full_sections_source')
        cov=next(t.metadata for t in full.trace if t.stage=='competition_full_coverage')
        self.assertTrue(cov['remaining_ids'])
        self.assertEqual(len(cov['covered_ids']),len(cov['returned_ids']))
    def test_full_rule_pages_no_skips_and_translation_gaps(self):
        for locale in ('th','en'):
            for game in ('CS2','RoV','Tekken 8','VALORANT'):
                with self.subTest(locale=locale,game=game):
                    q=('All detailed competition rules for ' if locale=='en' else 'กติกาการแข่งขันทั้งหมด ')+game
                    history=[];seen=set();outputs=[]
                    for i in range(25):
                        r=build_full_rule_answer(q if not history else ('Additional competition rules for ' if locale=='en' else 'กติกาการแข่งขันเพิ่มเติม ')+game,locale,recent_history=history)
                        self.assertIsNotNone(r)
                        c=r['trace'][0].metadata
                        self.assertFalse(seen.intersection(c['returned_ids']))
                        seen.update(c['returned_ids']);outputs.append(r['answer'])
                        RECORDS.append({'question':q,'locale':locale,'mode':r['mode'],'answer':r['answer'],'coverage':c})
                        history.extend([{'role':'user','text':q},{'role':'assistant','text':r['answer'],'route_category':'competition_rules','resolved_text':q,'rule_coverage':c,'delivery_status':'client_acknowledged'}])
                        history=history[-16:]
                        if not c['remaining_ids']:break
                    self.assertEqual(seen|set(c['locale_gap_ids']),set(c['expected_ids']))
                    self.assertLess(i,24)
                    if locale=='th':self.assertFalse(c['locale_gap_ids'])
                    exhausted=build_full_rule_answer(('Additional competition rules for ' if locale=='en' else 'กติกาการแข่งขันเพิ่มเติม ')+game,locale,recent_history=history)
                    self.assertFalse(exhausted['trace'][0].metadata['returned_ids'])
                    self.assertTrue(exhausted['hits'])
                    # No summary subset may stand in for full section coverage.
                    if game=='CS2' and locale=='th':
                        text='\n'.join(outputs);self.assertIn('การหมิ่นศาสนา',text);self.assertIn('MIRAGE',text)
                        self.assertIn('แบนถาวร',text)
    def test_rule_release_change_and_uncertain_repeat(self):
        q='All detailed competition rules for CS2'
        first=build_full_rule_answer(q,'en');c=first['trace'][0].metadata
        h=[{'role':'user','text':q},{'role':'assistant','text':first['answer'],'route_category':'competition_rules','rule_coverage':c,'resolved_text':q,'delivery_status':'server_written'}]
        repeat=build_full_rule_answer('Additional competition rules for CS2','en',recent_history=h)
        self.assertEqual(repeat['trace'][0].metadata['returned_ids'],c['returned_ids'])
        h[-1]['rule_coverage']=dict(c,source_release='other-release');h[-1]['delivery_status']='client_acknowledged'
        restarted=build_full_rule_answer('Additional competition rules for CS2','en',recent_history=h)
        self.assertTrue(restarted['trace'][0].metadata['source_changed'])
    def test_rule_continuation_uses_rendered_metadata_not_raw_scope_word(self):
        for locale,allq,moreq in [('th','ขอรายละเอียดทั้งหมด','ต่อ'),('en','all details please','continue')]:
            prior='All detailed competition rules for CS2' if locale=='en' else 'กติกาการแข่งขันทั้งหมด CS2'
            r=build_full_rule_answer(prior,locale);c=r['trace'][0].metadata
            h=[{'role':'user','text':allq},{'role':'assistant','text':r['answer'],'route_category':'competition_rules','resolved_text':prior,'rule_coverage':c,'delivery_status':'client_acknowledged'}]
            resolved=resolve_question_with_context(moreq,h,locale=locale)
            self.assertEqual(resolved.context_domain,'competition_rules')
            self.assertTrue(resolved.used_context)
    def test_rephrased_price_preserves_eligibility(self):
        for locale,q in [('th','ขอราคา Cockpit แทน'),('th','ขอราคา VR'),('en',"I'd like the cockpit rate instead"),('en','PC fees please')]:
            p=plan(q,active_task=self.external(locale)['tasks'][0],locale=locale)
            self.assertEqual(p['tasks'][0]['filters']['customer_group_ids'],['general_student','general_adult'])
            r=pipeline(q,locale,p)
            metadata=next(t.metadata for t in r.trace if t.stage=='conversation_contract')
            self.assertFalse(any(k.endswith(':psu_student_staff') for k in metadata['returned_ids']))
        explicit=plan('PC prices for general adults',active_task=self.external('en')['tasks'][0],locale='en')
        self.assertEqual(explicit['tasks'][0]['filters']['customer_group_ids'],['general_adult'])
        reset=plan('New question: PC prices',active_task=self.external('en')['tasks'][0],locale='en')
        self.assertEqual(reset['tasks'][0]['filters']['customer_scope'],'unspecified')
        prior=plan('Service prices for external users and how to book',locale='en')
        follow=plan('PC fees please',active_task=prior['tasks'][0],locale='en')
        self.assertEqual(len(follow['tasks']),2)
    def test_each_every_rule_scope(self):
        from app.pipeline.conversation_rules import wants_full_rules
        for q in ['Please show every section of the CS2 tournament rulebook','Each documented clause of the CS2 rules','Every single rule in the CS2 tournament']:
            self.assertTrue(wants_full_rules(q))
            r=build_full_rule_answer(q,'en')
            self.assertTrue(r and r['trace'][0].metadata['returned_ids'])
            self.assertIsNone(plan(q,locale='en'))
            result=pipeline(q,'en')
            self.assertEqual(result.route.category,'competition_rules')
            self.assertTrue(any(t.stage=='competition_full_coverage' for t in result.trace))
        self.assertFalse(wants_full_rules('Every PC is available'))
    def test_general_token_limit_complete_prefix_only(self):
        from app.pipeline.experimental_fallback import GeneralGenerationProfile, _shape_general_output, _general_output_contract
        from app.pipeline.execution_context import set_current_locale_decision, request_execution_context
        from app.core.locale import resolve_locale
        context=request_execution_context();context.__enter__()
        self.addCleanup(context.__exit__,None,None,None)
        set_current_locale_decision(resolve_locale('test',requested='en'))
        p=GeneralGenerationProfile('general_concise',128,'two sentences',128)
        provider={'ollama_done_reason':'length'}
        prefix=_shape_general_output('Eggs existed before chickens. Earlier ancestors laid eggs. An unfinished final',p,provider)
        self.assertEqual(prefix,'Eggs existed before chickens. Earlier ancestors laid eggs.')
        self.assertTrue(_general_output_contract(prefix,p,provider)[0])
        bad={'ollama_done_reason':'length'}
        fragment=_shape_general_output('The answer is an unfinished',p,bad)
        self.assertFalse(_general_output_contract(fragment,p,bad)[0])

if __name__=='__main__':
    output=Path(os.getenv('PSU_CONVERSATION_TEST_OUTPUT',str(ROOT/'reports'/'conversation_r38')));output.mkdir(parents=True,exist_ok=True)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(FlowTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    stamp=time.strftime('%Y%m%d_%H%M%S')+'_'+str(time.time_ns())
    (output/f'flow_results_{stamp}.json').write_text(json.dumps(RECORDS,ensure_ascii=False,indent=2),encoding='utf-8')
    (output/f'flow_summary_{stamp}.json').write_text(json.dumps({'tests_run':result.testsRun,'failures':[(str(t),txt) for t,txt in result.failures],'errors':[(str(t),txt) for t,txt in result.errors]},ensure_ascii=False,indent=2),encoding='utf-8')
    sys.exit(0 if result.wasSuccessful() else 1)
