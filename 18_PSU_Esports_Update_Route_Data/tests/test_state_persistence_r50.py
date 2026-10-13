import unittest,sqlite3,json,os,uuid
from types import SimpleNamespace
from contextlib import closing
from pathlib import Path
from dataclasses import asdict
from app.session.conversation_store import ConversationStore,TurnConflict
from app.session.context_resolver import resolve_question_with_context
from app.pipeline.user_service_facts import answer_user_service_facts
from app.pipeline.competition_targets import looks_like_competition_rule_query
from app.pipeline.competition_taxonomy import detect_competition_facet

def complete(store,session='one',turn='first',q='มีที่จอดรถไหม',ack=True):
    prepared=store.begin(session,turn,q,history=store.history(session))
    result=answer_user_service_facts(q)
    response=dict(ok=True,request_id=turn,mode=result['mode'],answer=result['answer'],resolved_question=q,route_category=result['route'].category,route_intent=result['route'].intent,trace=[asdict(t) for t in result['trace']])
    store.complete(session,turn,prepared['revision'],response)
    if ack:store.acknowledge(session,turn)
    return response

class PersistentDialogueTests(unittest.TestCase):
    def setUp(self):
        fixture=Path(os.environ['PSU_TEST_STATE_DIR'])/uuid.uuid4().hex;fixture.mkdir(parents=True)
        self.temp=SimpleNamespace(name=str(fixture));self.path=fixture/'state.sqlite3'
    def store(self,**kw):return ConversationStore(persistence_path=self.path,**kw)
    def test_restart_restores_acknowledged_context_and_isolates_sessions(self):
        complete(self.store());second=self.store()
        self.assertTrue(resolve_question_with_context('ฟรีไหม',second.history('one')).used_context)
        self.assertFalse(resolve_question_with_context('ฟรีไหม',second.history('two')).used_context)
        self.assertTrue(second.snapshot('one')['survives_server_restart'])
    def test_restart_does_not_promote_unacknowledged_delivery(self):
        complete(self.store(),ack=False)
        self.assertFalse(resolve_question_with_context('ฟรีไหม',self.store().history('one')).used_context)
    def test_duplicate_turn_and_conflicting_payload_survive_restart(self):
        complete(self.store());second=self.store()
        self.assertEqual('first',second.begin('one','first','มีที่จอดรถไหม')['response']['request_id'])
        with self.assertRaises(TurnConflict):second.begin('one','first','เอาคีย์บอร์ดส่วนตัวมาได้ไหม')
    def test_pending_request_is_reexecuted_and_not_promoted(self):
        first=self.store();turn=first.begin('one','pending','มีที่จอดรถไหม')
        second=self.store();fresh=second.begin('one','pending','มีที่จอดรถไหม')
        self.assertIsNone(fresh['response']);self.assertGreater(fresh['revision'],turn['revision'])
        self.assertEqual([],second.history('one'))
    def test_wall_clock_ttl_expires_across_new_monotonic_clock(self):
        wall=[100.];first=self.store(ttl=60,clock=lambda:500.,wall_clock=lambda:wall[0]);complete(first)
        wall[0]=161.;second=self.store(ttl=60,clock=lambda:2.,wall_clock=lambda:wall[0])
        self.assertEqual([],second.history('one'))
    def test_corrupt_snapshot_is_not_trusted_and_file_is_preserved(self):
        complete(self.store())
        with closing(sqlite3.connect(self.path)) as db,db:db.execute("UPDATE dialogue_state_v1 SET state_json='invalid json'")
        second=self.store();self.assertEqual([],second.history('one'));self.assertTrue(second.snapshot('one')['persistence']['last_error']);self.assertTrue(self.path.exists())
    def test_failed_storage_does_not_break_memory_context(self):
        first=ConversationStore(persistence_path=Path(self.temp.name));complete(first)
        self.assertTrue(resolve_question_with_context('ฟรีไหม',first.history('one')).used_context)
        self.assertFalse(first.snapshot('one')['survives_server_restart'])
    def test_live_response_is_not_replayed_from_disk(self):
        first=self.store();p=first.begin('one','live','PC1 ว่างไหม')
        first.complete('one','live',p['revision'],dict(ok=True,request_id='live',answer='ว่าง',mode='pipeline:live_booking_status_fast_path',route_category='reservation',route_intent='live_booking_status'))
        first.acknowledge('one','live');second=self.store()
        self.assertIsNone(second.begin('one','live','PC1 ว่างไหม')['response'])
    def test_explicit_return_to_service_topic_after_shift(self):
        first=self.store();complete(first)
        p=first.begin('one','shift','PC มีเกมอะไรบ้าง')
        first.complete('one','shift',p['revision'],dict(ok=True,request_id='shift',answer='PC Zone',mode='pipeline:structured_games_catalog',route_category='games',route_intent='list',resolved_question='PC มีเกมอะไรบ้าง'))
        first.acknowledge('one','shift');second=self.store()
        turn=second.begin('one','resume','กลับไปเรื่องที่จอดรถ',history=second.history('one'))
        self.assertEqual('มีที่จอดรถไหม',turn['context_resolution']['resolved_question'])
        self.assertEqual([],self.store().history('other'))
    def test_ambiguous_compound_return_is_not_replayed_as_single_subject(self):
        first=self.store();complete(first,q='มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม')
        turn=first.begin('one','resume','กลับไปเรื่องที่จอดรถ',history=first.history('one'))
        self.assertEqual('dialogue_state_clarification_v1',turn['plan']['schema_type'])
    def test_team_member_count_is_a_bound_rulebook_facet(self):
        for q in ['สมาชิกทีม CS2 ต้องมีกี่คน','How many members are in a CS2 team?']:
            self.assertTrue(looks_like_competition_rule_query(q));self.assertEqual('team_size',detect_competition_facet(q))
        self.assertEqual('pause_timeout',detect_competition_facet('VALORANT team members request how many timeouts?'))
        self.assertFalse(looks_like_competition_rule_query('Steam สมาชิกต้องจ่ายไหม'))
    def test_two_independent_noun_typos_recover_without_number_changes(self):
        q='จอองหลายเครืองโอนครังเดียวได้ปะ 3 PC01 2026-10-09'
        r=answer_user_service_facts(q);meta=r['trace'][0].metadata
        self.assertIn('combined_transfer',meta['claim_ids']);self.assertGreaterEqual(len(meta['lexical_recoveries']),2)
        self.assertIn('PC01'.lower(),meta['normalized_service_question']);self.assertIn('2026-10-09',meta['normalized_service_question'])
