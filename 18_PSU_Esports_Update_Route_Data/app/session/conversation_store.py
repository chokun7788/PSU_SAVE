"""Bounded parent-process state; worker replacement does not replace dialogue."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import threading
import time
from collections import OrderedDict
from dataclasses import asdict, is_dataclass

from app.session.conversation_plan import resolve_request_plan, valid_price_task


class TurnConflict(ValueError):
    pass


class ConversationStore:
    def __init__(self, *, ttl=1800.0, max_sessions=512, clock=time.monotonic, persistence_path=None, wall_clock=time.time):
        self.ttl, self.max_sessions, self.clock = ttl, max_sessions, clock
        self._sessions = OrderedDict()
        self._guard = threading.RLock()
        from app.session.state_persistence import StatePersistence
        self._persistence=StatePersistence(persistence_path,max_sessions=max_sessions,wall_clock=wall_clock) if persistence_path else None

    def _save(self,session_id):
        if self._persistence:self._persistence.save(session_id,self._sessions[session_id],now=self.clock())

    def _record(self, session_id):
        now=self.clock()
        for key in list(self._sessions):
            if self._sessions[key]['expires'] <= now:
                del self._sessions[key]
        if session_id not in self._sessions:
            while len(self._sessions) >= self.max_sessions:
                self._sessions.popitem(last=False)
            restored=self._persistence.load(session_id,now=now,ttl=self.ttl) if self._persistence else None
            self._sessions[session_id]=restored or {'revision':0,'active':None,'history':[],'turns':OrderedDict(),'expires':now+self.ttl,
                                       'task_memory':OrderedDict(),'current_task_keys':[]}
        r=self._sessions[session_id]
        r['expires']=now+self.ttl
        self._sessions.move_to_end(session_id)
        return r

    def history(self, session_id, fallback=None):
        with self._guard:
            own=self._record(session_id)['history']
            if own:
                result = copy.deepcopy(own[-16:])
                deliveries = {t['response'].get('request_id'):t['delivery'] for t in self._sessions[session_id]['turns'].values() if t['response']}
                for item in result:
                    if item.get('role') == 'assistant':
                        item['delivery_status'] = deliveries.get(item.get('request_id'),'uncertain')
                return result
            if not isinstance(fallback,list):
                return []
            result = copy.deepcopy([r for r in fallback[-10:] if isinstance(r,dict) and r.get('role') in {'user','assistant'} and isinstance(r.get('text'),str) and len(r['text']) <= 16000])
            for item in result:
                item['delivery_status'] = 'uncertain'  # Client metadata cannot prove delivery.
            return result

    def begin(self, session_id, turn_id, question, *, locale='th', history=None, fingerprint_locale=None):
        fingerprint=hashlib.sha256(json.dumps([question,locale if fingerprint_locale is None else fingerprint_locale],ensure_ascii=False).encode()).hexdigest()
        with self._guard:
            r=self._record(session_id)
            old=r['turns'].get(turn_id)
            if old:
                if old['fingerprint'] != fingerprint:
                    raise TurnConflict('client_turn_id was reused for a different question or language')
                if old['response'] is None and old['revision'] != r['revision']:
                    raise TurnConflict('pending turn is older than the active state revision')
                return copy.deepcopy(old)
            from app.session.task_memory import resolve_memory
            context_resolution, memory_plan = resolve_memory(question,r,locale=locale)
            plan=memory_plan if context_resolution is not None else resolve_request_plan(question,history,active_task=r['active'],locale=locale)
            r['revision']+=1
            if plan and plan.get('tasks') and valid_price_task(plan['tasks'][0]):
                r['active']=copy.deepcopy(plan['tasks'][0])
            else:
                # An explicit topic shift is committed even when its tool fails.
                r['active']=None
            turn={'fingerprint':fingerprint,'revision':r['revision'],'question':question,'plan':plan,'response':None,'delivery':'prepared',
                  'context_resolution':context_resolution}
            r['turns'][turn_id]=turn
            while len(r['turns'])>8:
                r['turns'].popitem(last=False)
            self._save(session_id)
            return copy.deepcopy(turn)

    def complete(self, session_id, turn_id, revision, response, *, plan=None, fact_state=None):
        with self._guard:
            r=self._record(session_id)
            turn=r['turns'].get(turn_id)
            if not turn or r['revision'] != revision:
                return False
            if turn['response'] is not None:
                # The first completed response is authoritative for this turn.
                # Duplicate callbacks must not rewrite memory or add history.
                return False
            if plan and plan.get('tasks') and valid_price_task(plan['tasks'][0]):
                r['active']=copy.deepcopy(plan['tasks'][0])
                turn['plan']=copy.deepcopy(plan)
            if response.get('ok'):
                turn['response']=copy.deepcopy(response)
                from app.session.task_memory import harvest_tasks, MAX_TASKS
                tasks=harvest_tasks(turn['question'],response,plan or turn['plan'])
                if tasks:
                    r['current_task_keys']=[]
                    for task in tasks:
                        task['acknowledged']=False
                        r['task_memory'][task['key']]=task;r['task_memory'].move_to_end(task['key'])
                        if task['key'] not in r['current_task_keys']:r['current_task_keys'].append(task['key'])
                    while len(r['task_memory'])>MAX_TASKS:r['task_memory'].popitem(last=False)
                elif response.get('mode')!='pipeline:dialogue_state_clarification':
                    r['current_task_keys']=[]
                intent=response.get('universal_intent')
                if is_dataclass(intent):
                    intent=asdict(intent)
                from app.session.service_fact_dialogue import service_fact_state
                r['history'].extend([
                    {'role':'user','text':turn['question']},
                    {'role':'assistant','text':response.get('answer',''),'route_category':response.get('route_category',''),
                     'mode':response.get('mode',''),
                     'route_intent':response.get('route_intent',''),'resolved_text':(turn['plan'] or {}).get('resolved_query',response.get('resolved_question',turn['question'])),
                     'universal_intent':intent,'request_plan':turn['plan'],'request_id':response.get('request_id',''),
                     'rule_coverage':copy.deepcopy(response.get('rule_coverage')),
                     'service_fact_state':copy.deepcopy(fact_state) if fact_state is not None else service_fact_state(response),
                     'common_read_state':copy.deepcopy(response.get('common_read_state'))},
                ])
                r['history']=r['history'][-16:]
                self._save(session_id)
            return True

    def delivery(self, session_id, turn_id, status):
        if status not in {'server_written','uncertain'}:
            raise ValueError('invalid delivery status')
        with self._guard:
            turn=self._record(session_id)['turns'].get(turn_id)
            if turn and turn['delivery'] != 'client_acknowledged':
                turn['delivery']=status
                self._save(session_id)

    def acknowledge(self, session_id, response_id):
        with self._guard:
            for turn in self._record(session_id)['turns'].values():
                if turn['response'] and turn['response'].get('request_id')==response_id:
                    turn['delivery']='client_acknowledged'
                    for task in self._record(session_id)['task_memory'].values():
                        if task.get('response_id')==response_id:task['acknowledged']=True
                    self._save(session_id)
                    return True
        return False

    def snapshot(self, session_id):
        with self._guard:
            r=self._record(session_id)
            return {'schema_version':1,'revision':r['revision'],'active_task':copy.deepcopy(r['active']),
                    'task_memory_schema_version':1,'requested_tasks':copy.deepcopy(list(r['task_memory'].values())),
                    'current_task_keys':list(r['current_task_keys']),
                    'delivery':{k:t['delivery'] for k,t in r['turns'].items()},'storage':'sqlite_parent_state' if self._persistence and not self._persistence.last_error else 'parent_memory',
                    'survives_server_restart':bool(self._persistence and self._persistence.ready and not self._persistence.last_error),
                    'persistence':self._persistence.health() if self._persistence else {'enabled':False}}


from pathlib import Path
def _state_path():
    if os.getenv('PSU_CONVERSATION_PERSISTENCE','1').lower() in {'0','false','off'}:return None
    return os.getenv('PSU_CONVERSATION_STATE_PATH') or str(Path(os.getenv('PSU_CHAT_LOG_DIR') or Path(__file__).resolve().parents[2]/'data/state')/'dialogue_state_v1.sqlite3')
STORE = ConversationStore(ttl=max(60,float(os.getenv('PSU_CONVERSATION_TTL_SEC','1800'))), max_sessions=max(1,int(os.getenv('PSU_CONVERSATION_MAX_SESSIONS','512'))),persistence_path=_state_path())
