"""Parent-owned model leases shared by spawned pipeline workers.

The parent can revoke a dead worker's lease without relying on that worker
to release a multiprocessing semaphore. This controls calls, not GPU batching.
"""
from __future__ import annotations

import queue
import threading
import time
import uuid
from collections import deque


class RemoteModelGate:
    def __init__(self, messages, replies, owner):
        self.messages, self.replies, self.owner = messages, replies, owner
        self._local = threading.Lock()
        self._token = None

    def acquire(self, *, timeout=0):
        deadline = time.monotonic() + max(0, timeout)
        if not self._local.acquire(timeout=max(0, timeout)):
            return False
        token = uuid.uuid4().hex
        acquired = False
        try:
            self.messages.put(('acquire', self.owner, token, deadline), timeout=.05)
            while True:
                wait = deadline - time.monotonic()
                if wait <= 0:
                    return False
                reply_token, granted = self.replies.get(timeout=wait)
                if reply_token == token:
                    acquired = bool(granted)
                    if acquired:
                        self._token = token
                    return acquired
        except queue.Empty:
            return False
        finally:
            if not acquired:
                self.messages.put(('release', self.owner, token, 0))
                self._local.release()

    def release(self):
        token, self._token = self._token, None
        if token is not None:
            try:
                self.messages.put(('release', self.owner, token, 0))
            finally:
                self._local.release()


class ModelAdmissionBroker:
    def __init__(self, context, *, limit=1):
        self.context, self.limit = context, max(1, limit)
        self.messages = context.Queue(maxsize=1024)
        self.replies = {}
        self.active = {}
        self.pending = deque()
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = None
        self.peak_active = 0

    def register(self):
        owner = uuid.uuid4().hex
        replies = self.context.Queue(maxsize=16)
        with self._lock:
            self.replies[owner] = replies
        return self.messages, replies, owner

    def start(self):
        if self._thread is None:
            self._thread = threading.Thread(target=self._run, daemon=True, name='psu-model-admission')
            self._thread.start()

    def revoke(self, owner):
        with self._lock:
            self.replies.pop(owner, None)
            self.active.pop(owner, None)
            self.pending = deque(item for item in self.pending if item[0] != owner)

    def snapshot(self):
        with self._lock:
            return dict(limit=self.limit, active=len(self.active), waiting=len(self.pending),
                        peak_active=self.peak_active, scope='all_pipeline_workers', durable=False)

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1)

    def _reply(self, owner, token, granted):
        replies = self.replies.get(owner)
        if replies is None:
            return False
        try:
            replies.put_nowait((token, granted))
            return True
        except queue.Full:
            return False

    def _run(self):
        while not self._stop.is_set():
            try:
                action, owner, token, deadline = self.messages.get(timeout=.02)
            except queue.Empty:
                action = None
            with self._lock:
                if action == 'acquire' and owner in self.replies:
                    self.pending.append((owner, token, deadline))
                elif action == 'release':
                    if self.active.get(owner) == token:
                        self.active.pop(owner, None)
                    self.pending = deque(item for item in self.pending if item[:2] != (owner, token))
                waiting = deque()
                for owner, token, deadline in self.pending:
                    if owner not in self.replies:
                        continue
                    if time.monotonic() >= deadline:
                        self._reply(owner, token, False)
                    elif len(self.active) < self.limit and owner not in self.active:
                        if self._reply(owner, token, True):
                            self.active[owner] = token
                            self.peak_active = max(self.peak_active, len(self.active))
                    else:
                        waiting.append((owner, token, deadline))
                self.pending = waiting
