"""Durable admission and polling for the existing idempotent chat endpoint.

Queued jobs recover after restart. In-flight work fails explicitly on restart:
an ambiguous network/worker failure is never replayed automatically.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path
from contextlib import contextmanager


class JobError(ValueError):
    def __init__(self, reason, status=400):
        self.reason, self.status = reason, status
        super().__init__(reason)


class ChatJobQueue:
    def __init__(self, path, endpoint, *, capacity=32, workers=2, ttl=90, call_timeout=25, model_busy=None):
        self.path, self.endpoint = str(path), endpoint
        self.capacity, self.workers, self.ttl = capacity, workers, ttl
        self.call_timeout = call_timeout
        self.model_busy = model_busy
        self._stop = threading.Event()
        self._threads = []
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self._db() as db:
            db.execute('PRAGMA journal_mode=WAL')
            db.execute('''CREATE TABLE IF NOT EXISTS chat_jobs (
                id TEXT PRIMARY KEY, session TEXT NOT NULL, turn TEXT NOT NULL,
                fingerprint TEXT NOT NULL, payload TEXT NOT NULL, status TEXT NOT NULL,
                created REAL NOT NULL, deadline REAL NOT NULL, started REAL,
                finished REAL, response TEXT, error TEXT, UNIQUE(session,turn))''')
            columns = {row['name'] for row in db.execute('PRAGMA table_info(chat_jobs)')}
            for name, definition in [('attempts','INTEGER NOT NULL DEFAULT 0'),('next_attempt','REAL NOT NULL DEFAULT 0'),('last_admission_error','TEXT')]:
                if name not in columns:
                    db.execute(f'ALTER TABLE chat_jobs ADD COLUMN {name} {definition}')
            db.execute("UPDATE chat_jobs SET status='failed',error='worker_lost',finished=? WHERE status='running'", (time.time(),))

    @contextmanager
    def _db(self):
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def submit(self, payload):
        body = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        fingerprint = hashlib.sha256(body.encode()).hexdigest()
        session, turn = payload['client_session_id'], payload['client_turn_id']
        now, job_id = time.time(), uuid.uuid4().hex
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT * FROM chat_jobs WHERE session=? AND turn=?',(session,turn)).fetchone()
            if old:
                if old['fingerprint'] != fingerprint:
                    raise JobError('client_turn_conflict',409)
                return self._public(old)
            count = db.execute("SELECT COUNT(*) FROM chat_jobs WHERE status IN ('queued','running')").fetchone()[0]
            if count >= self.capacity:
                raise JobError('admission_full',503)
            db.execute('INSERT INTO chat_jobs (id,session,turn,fingerprint,payload,status,created,deadline) VALUES (?,?,?,?,?,?,?,?)',
                       (job_id,session,turn,fingerprint,body,'queued',now,now+self.ttl))
        # Return only after the SQLite transaction has committed.
        return self.get(job_id,session)

    def get(self, job_id, session):
        with self._db() as db:
            row = db.execute('SELECT * FROM chat_jobs WHERE id=? AND session=?',(job_id,session)).fetchone()
        if row is None:
            raise JobError('not_found',404)
        return self._public(row)

    def cancel(self, job_id, session):
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT * FROM chat_jobs WHERE id=? AND session=?',(job_id,session)).fetchone()
            if row is None:
                raise JobError('not_found',404)
            if row['status'] == 'running':
                raise JobError('cancellation_requires_queued_job',409)
            if row['status'] == 'queued':
                db.execute("UPDATE chat_jobs SET status='cancelled',error='cancelled',finished=? WHERE id=?",(time.time(),job_id))
        return self.get(job_id,session)

    def _public(self, row):
        now = row['finished'] if row['finished'] is not None else time.time()
        # Last dispatch start: earlier rejected attempts belong to admission
        # delay, not completed inference. These are wall times, not GPU times.
        started = row['started'] if row['status'] != 'queued' else None
        timing = dict(elapsed_sec=round(max(0,now-row['created']),3),
                      admission_wait_sec=round(max(0,(started or now)-row['created']),3),
                      active_dispatch_sec=round(max(0,now-started),3) if started is not None else 0.0,
                      remaining_sec=round(max(0,row['deadline']-now),3) if row['status'] in ('queued','running') else 0.0,
                      meaning='wall_time_last_dispatch_not_model_inference')
        return dict(ok=True, job_id=row['id'], session_id=row['session'], turn_id=row['turn'],
                    status=row['status'], created_at=row['created'], deadline_at=row['deadline'],
                    started_at=row['started'], finished_at=row['finished'], error=row['error'],
                    result=json.loads(row['response']) if row['response'] else None,
                    dispatch_attempts=row['attempts'], last_admission_error=row['last_admission_error'],
                    timing=timing, poll_after_ms=400, storage='local_sqlite')

    def _claim(self):
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            now = time.time()
            db.execute("UPDATE chat_jobs SET status='failed',error='queue_expired',finished=? WHERE status='queued' AND deadline<=?",(now,now))
            rows = db.execute("""SELECT j.* FROM chat_jobs j WHERE j.status='queued' AND j.next_attempt<=?
                AND NOT EXISTS (SELECT 1 FROM chat_jobs p WHERE p.session=j.session
                  AND p.status IN ('queued','running') AND (p.created<j.created OR (p.created=j.created AND p.rowid<j.rowid)))
                ORDER BY CASE WHEN j.attempts>0 AND j.created<? THEN 0 ELSE 1 END,
                         j.attempts,j.created,j.rowid""",(now,now-15)).fetchall()
            busy = bool(self.model_busy and self.model_busy())
            row = None
            for candidate in rows:
                if busy:
                    from app.pipeline.query_signals import looks_like_clear_general_request
                    if looks_like_clear_general_request(json.loads(candidate['payload'])['question']):
                        continue  # Scheduling hint only; normal pipeline still interprets every dispatched job.
                row = candidate
                break
            if row:
                db.execute("UPDATE chat_jobs SET status='running',started=?,attempts=attempts+1 WHERE id=?",(now,row['id']))
        return row

    def _finish(self, job_id, status, *, result=None, error=None):
        with self._db() as db:
            db.execute('UPDATE chat_jobs SET status=?,response=?,error=?,finished=? WHERE id=? AND status=\'running\'',
                       (status,json.dumps(result,ensure_ascii=False) if result is not None else None,error,time.time(),job_id))

    def _defer(self, job_id, reason):
        # Release the dispatcher on rejected model admission so a fast facts
        # job from another conversation can proceed while the GPU is occupied.
        # _claim favours first attempts over retries; retries aged 15 seconds
        # regain priority so a stream of new arrivals cannot always bypass them.
        with self._db() as db:
            db.execute("UPDATE chat_jobs SET status='queued',next_attempt=?,last_admission_error=? WHERE id=? AND status='running'",
                       (time.time()+.25,reason,job_id))

    def _execute(self, row):
        while not self._stop.is_set():
            remaining = row['deadline']-time.time()
            if remaining <= 0:
                self._finish(row['id'],'failed',error='queue_expired')
                return
            request = urllib.request.Request(self.endpoint,data=row['payload'].encode(),headers={'Content-Type':'application/json'},method='POST')
            try:
                with urllib.request.urlopen(request,timeout=min(self.call_timeout,remaining)) as response:
                    result = json.load(response)
                self._finish(row['id'],'completed',result=result)
                return
            except urllib.error.HTTPError as exc:
                try:
                    result = json.load(exc)
                except (ValueError, OSError):
                    result = {}
                finally:
                    exc.close()
                # Only explicit non-execution admission rejections are replayable.
                if exc.code in (409,503) and result.get('error') in ('server_busy','session_busy','pipeline_worker_restarting'):
                    self._defer(row['id'],result.get('reason') or result['error'])
                    return
                self._finish(row['id'],'failed',result=result,error=result.get('error') or 'backend_error')
                return
            except (OSError, ValueError) as exc:
                self._finish(row['id'],'failed',error='provider_unavailable' if isinstance(exc,urllib.error.URLError) else 'worker_lost')
                return

    def _run(self):
        while not self._stop.is_set():
            row = self._claim()
            if row:
                self._execute(row)
            else:
                self._stop.wait(.05)

    def start(self):
        for i in range(self.workers):
            thread = threading.Thread(target=self._run,daemon=True,name=f'psu-chat-job-{i}')
            thread.start()
            self._threads.append(thread)

    def stop(self):
        self._stop.set()
        for thread in self._threads:
            thread.join(timeout=.5)

    def snapshot(self):
        with self._db() as db:
            counts = dict(db.execute('SELECT status,COUNT(*) FROM chat_jobs GROUP BY status').fetchall())
        return dict(enabled=True,capacity=self.capacity,dispatch_workers=self.workers,ttl_sec=self.ttl,counts=counts,durable=True)
