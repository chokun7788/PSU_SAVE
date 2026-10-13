import re,unittest
from dataclasses import asdict
from app.pipeline.service_fact_query import recover_service_fact_query
from app.pipeline.user_service_facts import answer_user_service_facts
from app.session.service_fact_dialogue import service_fact_state,resolve_service_fact_followup
from app.session.conversation_store import ConversationStore
from app.session.context_resolver import resolve_question_with_context

def response(q,locale='th',rid='first'):
    r=answer_user_service_facts(q,locale)
    return dict(ok=True,request_id=rid,answer=r['answer'],mode=r['mode'],route_category=r['route'].category,
                route_intent=r['route'].intent,trace=[asdict(t) for t in r['trace']])

class ServiceFactDialogueTests(unittest.TestCase):
    def test_bounded_lexical_recovery_and_negation_numeric_preservation(self):
        for q,target in [('Do I need a membrship?','membership'),
                         ('Can I walkk in?','walk'),
                         ('เอาคีย์บอดส่วนตัวมาได้ไหม','คีย์บอร์ด'),
                         ('จอง 3 เครื่องโอนครังเดียว ไม่จ่ายสองครั้ง วันที่ 2026-10-09 PC01','ครั้งเดียว')]:
            with self.subTest(question=q):
                fixed,changes=recover_service_fact_query(q)
                self.assertIn(target,fixed);self.assertTrue(changes)
                self.assertEqual(re.findall(r'\d+',q),re.findall(r'\d+',fixed))
                self.assertEqual('ไม่' in q,'ไม่' in fixed)
                self.assertEqual(q.casefold().count('not'),fixed.count('not'))

    def test_real_short_words_and_known_game_controls_are_not_rewritten(self):
        for q in ['Can I check in while my group arrives?',
                  'Is this the best rest area?', 'What maps are there in VALORANT?',
                  'Which mouse button fires in CS2?']:
            fixed,changes=recover_service_fact_query(q)
            self.assertFalse(changes,(q,changes))

    def test_short_followup_requires_acknowledged_same_session_history(self):
        store=ConversationStore();q='มีที่จอดรถไหม'
        prepared=store.begin('one','first',q)
        store.complete('one','first',prepared['revision'],response(q))
        self.assertIsNone(resolve_service_fact_followup('ฟรีไหม',store.history('one')))
        store.acknowledge('one','first')
        resolved=resolve_question_with_context('ฟรีไหม',store.history('one'))
        self.assertTrue(resolved.used_context);self.assertIn('ค่าจอด',resolved.resolved_question)
        self.assertFalse(resolve_question_with_context('ฟรีไหม',store.history('two')).used_context)

    def test_unknown_controller_and_note_format_are_not_invented(self):
        for q,missing in [('เอาจอยตัวเองมาใช้ได้ไหม','personal_controller_permission'),
                          ('จองหลายเครื่องโอนครั้งเดียวได้ไหม ต้องเขียนอะไรใน note','combined_transfer_note_format')]:
            r=answer_user_service_facts(q)
            self.assertIn(missing,r['trace'][0].metadata['missing_fields'])
        self.assertNotIn('ไม่อนุญาตให้นำจอย',answer_user_service_facts('เอาจอยตัวเองมาใช้ได้ไหม')['answer'])

    def test_history_state_is_harvested_from_trace_not_answer_words(self):
        self.assertEqual(['parking'],service_fact_state(response('มีที่จอดรถไหม'))['claim_ids'])
        self.assertIsNone(service_fact_state(dict(mode='pipeline:no_answer',answer='parking')))

    def test_explicit_topic_shift_and_untrusted_client_history_do_not_inherit(self):
        previous=dict(role='assistant',mode='pipeline:user_service_facts',service_fact_state={'claim_ids':['parking']},delivery_status='client_acknowledged')
        self.assertIsNone(resolve_service_fact_followup('ราคา PC ของบุคคลภายนอก',[previous]))
        self.assertIsNone(resolve_service_fact_followup('ฟรีไหม',[{**previous,'delivery_status':'uncertain'}]))
        self.assertIsNone(resolve_service_fact_followup('แล้วมอเตอร์ไซค์ล่ะ',[previous,{**previous,'mode':'pipeline:structured_games_catalog','service_fact_state':None}]))

    def test_membership_scope_does_not_leak_to_steam_or_teams(self):
        for q in ['Steam ต้องเป็นสมาชิกก่อนหรือเปล่า','สมาชิกทีม VALORANT ต้องมีกี่คน']:
            r=answer_user_service_facts(q)
            if 'สมาชิกทีม' in q:
                self.assertIsNone(r)  # Bound roster questions delegate to rulebook coverage.
                continue
            self.assertEqual('pipeline:service_fact_scope_clarification',r['mode'])
            self.assertEqual([],r['hits'])

    def test_debug_off_response_can_keep_internal_state(self):
        store=ConversationStore();q='มีที่จอดรถไหม';full=response(q)
        internal=service_fact_state(full)
        public={k:v for k,v in full.items() if k!='trace'}
        prepared=store.begin('one','first',q)
        store.complete('one','first',prepared['revision'],public,fact_state=internal)
        store.acknowledge('one','first')
        self.assertTrue(resolve_question_with_context('ฟรีไหม',store.history('one')).used_context)

    def test_dataclass_trace_is_accepted(self):
        r=answer_user_service_facts('มีที่จอดรถไหม')
        self.assertEqual(['parking'],service_fact_state({'mode':r['mode'],'trace':r['trace']})['claim_ids'])

    def test_fee_after_compound_is_clarified_then_selected(self):
        full=response('มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม')
        previous=dict(role='assistant',delivery_status='client_acknowledged',service_fact_state=service_fact_state(full))
        resolved=resolve_question_with_context('ฟรีไหม',[previous])
        self.assertTrue(resolved.used_context)
        r=answer_user_service_facts('ฟรีไหม',recent_history=[previous])
        self.assertEqual('clarification',r['route'].category)
        self.assertIn('ที่จอดรถ',r['answer']);self.assertIn('ดูเพื่อน',r['answer'])
        pending=service_fact_state(dict(mode=r['mode'],trace=r['trace']))
        selected=resolve_question_with_context('ที่จอดรถ',[{**previous,'service_fact_state':pending}])
        self.assertIn('ฟรี',selected.resolved_question)
