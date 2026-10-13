"""Local, bounded server dialogue state, separate from transcript logs."""
from __future__ import annotations
import copy,json,sqlite3,time
from pathlib import Path
from collections import OrderedDict
from dataclasses import asdict,is_dataclass
from contextlib import closing

def plain(value):
    if is_dataclass(value):return plain(asdict(value))
    if isinstance(value,dict):return {str(k):plain(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [plain(v) for v in value]
    if isinstance(value,Path):return str(value)
    return value

class StatePersistence:
    def __init__(self,path,*,max_sessions=512,wall_clock=time.time):
        self.path=Path(path);self.max_sessions=max_sessions;self.wall_clock=wall_clock
        self.last_error='';self.writes=0;self.restores=0;self.ready=False

    def _connect(self):
        self.path.parent.mkdir(parents=True,exist_ok=True)
        db=sqlite3.connect(str(self.path),timeout=.15)
        try:
            if not self.ready:
                db.execute('PRAGMA journal_mode=WAL')
                db.execute('CREATE TABLE IF NOT EXISTS dialogue_state_v1 (session_id TEXT PRIMARY KEY, expires_at REAL NOT NULL, updated_at REAL NOT NULL, state_json TEXT NOT NULL)')
                db.commit();self.ready=True
            return db
        except sqlite3.Error:
            db.close();raise

    def load(self,session_id,*,now,ttl):
        try:
            with closing(self._connect()) as db, db:
                row=db.execute('SELECT expires_at,state_json FROM dialogue_state_v1 WHERE session_id=?',(session_id,)).fetchone()
            if not row or row[0]<=self.wall_clock():return None
            r=json.loads(row[1])
            if r.get('schema_version')!=1 or not isinstance(r.get('revision'),int) or not isinstance(r.get('history'),list) or not isinstance(r.get('turns'),dict) or not isinstance(r.get('task_memory'),dict) or not isinstance(r.get('current_task_keys'),list):raise ValueError('invalid_dialogue_state_schema')
            pending=any(not v.get('response') for v in r['turns'].values() if isinstance(v,dict))
            r.pop('schema_version');r['turns']=OrderedDict((k,v) for k,v in r['turns'].items() if isinstance(v,dict) and isinstance(v.get('response'),dict))
            r['task_memory']=OrderedDict(r['task_memory']);r['history']=r['history'][-16:]
            # A request interrupted before completion must be re-executed.
            if pending:r['active']=None
            r['expires']=now+min(ttl,row[0]-self.wall_clock())
            self.restores+=1;self.last_error='';return r
        except (OSError,sqlite3.Error,ValueError,TypeError,KeyError) as exc:
            self.last_error=type(exc).__name__;return None

    def save(self,session_id,record,*,now):
        try:
            r=plain(copy.deepcopy(record));r.pop('expires');r['schema_version']=1
            # Never replay a persisted live availability response as fresh.
            live_ids=set()
            for key,turn in list(r['turns'].items()):
                response=turn.get('response') or {}
                if 'live_booking' in response.get('mode',''):
                    live_ids.add(response.get('request_id'));del r['turns'][key]
            for h in r['history']:
                if h.get('role')=='assistant' and h.get('request_id') in live_ids:h['text']=''
            payload=json.dumps(r,ensure_ascii=False,allow_nan=False)
            if len(payload.encode('utf-8'))>2_000_000:raise ValueError('dialogue_state_too_large')
            wall=self.wall_clock();expires=wall+max(0,record['expires']-now)
            with closing(self._connect()) as db, db:
                db.execute('INSERT INTO dialogue_state_v1 VALUES (?,?,?,?) ON CONFLICT(session_id) DO UPDATE SET expires_at=excluded.expires_at,updated_at=excluded.updated_at,state_json=excluded.state_json',(session_id,expires,wall,payload))
                db.execute('DELETE FROM dialogue_state_v1 WHERE expires_at<=?',(wall,))
                db.execute('DELETE FROM dialogue_state_v1 WHERE session_id NOT IN (SELECT session_id FROM dialogue_state_v1 ORDER BY updated_at DESC LIMIT ?)',(self.max_sessions,))
            self.writes+=1;self.last_error='';return True
        except (OSError,sqlite3.Error,ValueError,TypeError,KeyError) as exc:
            self.last_error=type(exc).__name__;return False

    def health(self):
        return dict(enabled=True,ready=self.ready,last_error=self.last_error,writes=self.writes,restores=self.restores)
