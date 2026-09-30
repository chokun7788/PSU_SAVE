from __future__ import annotations

import json
import math
import sqlite3
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Any

from app.knowledge.records import MAX_RECORDS, REGISTRY_VERSION, canonical_json, digest, validate_record


class Conflict(ValueError):
    pass


class KnowledgeStore:
    """Trusted local operator API; this is not a public admin authentication layer."""

    def __init__(self, path: Path | str):
        self.path = Path(path).resolve()

    @contextmanager
    def connect(self, *, write: bool = False):
        conn = sqlite3.connect(self.path.as_uri() + "?mode=rw", uri=True, timeout=0.25)
        conn.row_factory = sqlite3.Row
        try:
            if write:
                conn.execute("BEGIN IMMEDIATE")
            else:
                conn.execute("BEGIN")
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def initialize(self, *, allow_demo: bool = False) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.path)
        try:
            conn.executescript("""
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS records (
                    record_id TEXT PRIMARY KEY, head INTEGER NOT NULL, withdrawn INTEGER NOT NULL DEFAULT 0);
                CREATE TABLE IF NOT EXISTS revisions (
                    record_id TEXT NOT NULL, version INTEGER NOT NULL, payload TEXT NOT NULL,
                    hash TEXT NOT NULL, created_by TEXT NOT NULL, PRIMARY KEY(record_id,version));
                CREATE TABLE IF NOT EXISTS approvals (
                    record_id TEXT NOT NULL, version INTEGER NOT NULL, hash TEXT NOT NULL,
                    approved_by TEXT NOT NULL, approved_at TEXT NOT NULL, PRIMARY KEY(record_id,version));
                CREATE TABLE IF NOT EXISTS releases (
                    release_id TEXT PRIMARY KEY, created_at TEXT NOT NULL, payload TEXT NOT NULL,
                    hash TEXT NOT NULL, request_key TEXT UNIQUE NOT NULL);
                CREATE TABLE IF NOT EXISTS ownership (
                    alias TEXT NOT NULL, record_id TEXT NOT NULL, PRIMARY KEY(alias,record_id));
                CREATE TABLE IF NOT EXISTS audit (
                    id INTEGER PRIMARY KEY, at TEXT NOT NULL, event TEXT NOT NULL, actor TEXT NOT NULL, detail TEXT NOT NULL);
            """)
            for key, value in (("active", ""), ("epoch", "0"), ("allow_demo", "1" if allow_demo else "0")):
                conn.execute("INSERT OR IGNORE INTO meta VALUES (?,?)", (key, value))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def _audit(conn, event: str, actor: str, detail: dict) -> None:
        if not isinstance(actor, str) or not actor.strip() or len(actor) > 100:
            raise ValueError("local operator identity required")
        conn.execute("INSERT INTO audit(at,event,actor,detail) VALUES (?,?,?,?)",
                     (datetime.now(timezone.utc).isoformat(), event, actor, canonical_json(detail)))

    def save(self, record: dict, *, actor: str, expected_version: int) -> dict:
        with self.connect(write=True) as conn:
            demo = conn.execute("SELECT value FROM meta WHERE key='allow_demo'").fetchone()[0] == "1"
            clean = validate_record(record, allow_demo=demo)
            key = clean["record_id"]
            current = conn.execute("SELECT * FROM records WHERE record_id=?", (key,)).fetchone()
            version = current["head"] if current else 0
            if version != expected_version or (current and current["withdrawn"]):
                raise Conflict("stale revision or withdrawn identity; create a new identity after withdrawal")
            if current is None and conn.execute("SELECT count(*) FROM records").fetchone()[0] >= MAX_RECORDS:
                raise ValueError("pilot record limit reached")
            payload = canonical_json(clean)
            revision_hash = digest(clean)
            conn.execute("INSERT INTO revisions VALUES (?,?,?,?,?)", (key, version + 1, payload, revision_hash, actor))
            conn.execute("INSERT INTO records VALUES (?,?,0) ON CONFLICT(record_id) DO UPDATE SET head=excluded.head",
                         (key, version + 1))
            self._audit(conn, "save", actor, {"record_id": key, "version": version + 1, "hash": revision_hash})
            return {"record_id": key, "version": version + 1, "hash": revision_hash}

    def approve(self, record_id: str, version: int, expected_hash: str, *, actor: str) -> None:
        with self.connect(write=True) as conn:
            row = conn.execute("SELECT r.* FROM revisions r JOIN records h USING(record_id) "
                               "WHERE r.record_id=? AND r.version=? AND h.head=r.version AND h.withdrawn=0",
                               (record_id, version)).fetchone()
            if row is None or row["hash"] != expected_hash or digest(json.loads(row["payload"])) != expected_hash:
                raise Conflict("approval must match current immutable revision")
            existing = conn.execute("SELECT * FROM approvals WHERE record_id=? AND version=?", (record_id, version)).fetchone()
            if existing:
                if existing["hash"] != expected_hash:
                    raise Conflict("approval hash mismatch")
                return
            conn.execute("INSERT INTO approvals VALUES (?,?,?,?,?)",
                         (record_id, version, expected_hash, actor, datetime.now(timezone.utc).isoformat()))
            self._audit(conn, "approve", actor, {"record_id": record_id, "version": version, "hash": expected_hash})

    def snapshot(self) -> dict[str, Any]:
        with self.connect() as conn:
            meta = dict(conn.execute("SELECT key,value FROM meta").fetchall())
            active = conn.execute("SELECT * FROM releases WHERE release_id=?", (meta["active"],)).fetchone()
            release = json.loads(active["payload"]) if active else None
            if active and digest(release) != active["hash"]:
                raise ValueError("release integrity check failed")
            return {"active": meta["active"], "epoch": int(meta["epoch"]), "release": release,
                    "allow_demo": meta["allow_demo"] == "1",
                    "ownership": [dict(r) for r in conn.execute("SELECT * FROM ownership")],
                    "withdrawn": [r[0] for r in conn.execute("SELECT record_id FROM records WHERE withdrawn=1")]}

    def publish(self, *, actor: str, request_key: str, expected_active: str,
                embed: Callable[[list[str]], tuple[list, dict]]) -> str:
        if not request_key or len(request_key) > 100:
            raise ValueError("bounded idempotency key required")
        with self.connect() as conn:
            prior = conn.execute("SELECT release_id,payload FROM releases WHERE request_key=?", (request_key,)).fetchone()
            if prior:
                if json.loads(prior["payload"])["base_release"] != expected_active:
                    raise Conflict("idempotency key reused with a different base release")
                return prior[0]
            meta = dict(conn.execute("SELECT key,value FROM meta").fetchall())
            if meta["active"] != expected_active:
                raise Conflict("active release changed before build")
            heads = [tuple(r) for r in conn.execute("SELECT * FROM records ORDER BY record_id")]
            rows = conn.execute("SELECT r.*, a.hash AS approval_hash FROM records h "
                                "JOIN revisions r ON r.record_id=h.record_id AND r.version=h.head "
                                "LEFT JOIN approvals a ON a.record_id=r.record_id AND a.version=r.version "
                                "WHERE h.withdrawn=0 ORDER BY r.record_id").fetchall()
            if any(r["approval_hash"] != r["hash"] for r in rows):
                raise Conflict("all current revisions must be approved before publication")
            records = []
            for row in rows:
                record = validate_record(json.loads(row["payload"]), allow_demo=meta["allow_demo"] == "1")
                if digest(record) != row["hash"]:
                    raise ValueError("revision integrity check failed")
                records.append({"record": record, "version": row["version"], "hash": row["hash"]})
        # Build both projections before the short activation transaction.
        units = []
        aliases: dict[str, str] = {}
        for item in records:
            r = item["record"]
            for alias in [r["title"], *r["aliases"]]:
                key = alias.casefold().strip()
                if key in aliases and aliases[key] != r["record_id"]:
                    raise ValueError("alias shared by different records; resolve before publishing")
                aliases[key] = r["record_id"]
            for section in r["sections"]:
                units.append({"unit_id": f"{r['record_id']}:{section['section_id']}", "record_id": r["record_id"],
                              "section_id": section["section_id"], "facet": section["facet"], "text": section["text"],
                              "search_text": f"{r['title']} {section['facet']} {section['heading']} {section['text']}"})
        vectors, embedding = embed([u["search_text"] for u in units]) if units else ([], {"model": "none", "dimensions": 0})
        if len(vectors) != len(units) or (units and not embedding.get("model")):
            raise ValueError("incomplete embedding projection")
        dimension = embedding.get("dimensions", 0)
        for unit, vector in zip(units, vectors):
            if len(vector) != dimension or dimension < 1 or not all(math.isfinite(float(v)) for v in vector):
                raise ValueError("invalid embedding dimensions or values")
            norm = math.sqrt(sum(float(v) ** 2 for v in vector))
            if norm <= 0:
                raise ValueError("zero embedding vector")
            unit["vector"] = [float(v) / norm for v in vector]
        payload = {"registry_version": REGISTRY_VERSION, "base_release": expected_active, "records": records,
                   "structured": {i["record"]["record_id"]: i["record"]["facts"] for i in records},
                   "rag": units, "embedding": embedding}
        release_id = uuid.uuid4().hex
        with self.connect(write=True) as conn:
            prior = conn.execute("SELECT release_id,payload FROM releases WHERE request_key=?", (request_key,)).fetchone()
            if prior:
                if json.loads(prior["payload"])["base_release"] != expected_active:
                    raise Conflict("idempotency key reused with a different base release")
                return prior[0]
            now_meta = dict(conn.execute("SELECT key,value FROM meta").fetchall())
            now_heads = [tuple(r) for r in conn.execute("SELECT * FROM records ORDER BY record_id")]
            if now_meta["active"] != expected_active or now_meta["epoch"] != meta["epoch"] or now_heads != heads:
                raise Conflict("content/release changed during build; rebuild against the latest snapshot")
            conn.execute("INSERT INTO releases VALUES (?,?,?,?,?)",
                         (release_id, datetime.now(timezone.utc).isoformat(), canonical_json(payload), digest(payload), request_key))
            for alias, record_id in aliases.items():
                previous = conn.execute("SELECT record_id FROM ownership WHERE alias=?", (alias,)).fetchall()
                if any(r[0] != record_id for r in previous):
                    raise Conflict("alias belongs to an older identity; explicit migration required")
                conn.execute("INSERT OR IGNORE INTO ownership VALUES (?,?)", (alias, record_id))
            conn.execute("UPDATE meta SET value=? WHERE key='active'", (release_id,))
            conn.execute("UPDATE meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self._audit(conn, "activate", actor, {"release_id": release_id, "hash": digest(payload)})
        return release_id

    def withdraw(self, record_id: str, *, actor: str) -> None:
        with self.connect(write=True) as conn:
            row = conn.execute("SELECT * FROM records WHERE record_id=?", (record_id,)).fetchone()
            if row is None:
                raise ValueError("unknown record")
            if row["withdrawn"]:
                return
            conn.execute("UPDATE records SET withdrawn=1 WHERE record_id=?", (record_id,))
            conn.execute("UPDATE meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self._audit(conn, "withdraw", actor, {"record_id": record_id})

    def rollback(self, release_id: str, *, actor: str, expected_active: str) -> None:
        with self.connect(write=True) as conn:
            row = conn.execute("SELECT * FROM releases WHERE release_id=?", (release_id,)).fetchone()
            active = conn.execute("SELECT value FROM meta WHERE key='active'").fetchone()[0]
            if active != expected_active or row is None:
                raise Conflict("stale activation or unknown release")
            payload = json.loads(row["payload"])
            if digest(payload) != row["hash"] or payload["registry_version"] != REGISTRY_VERSION:
                raise ValueError("incompatible rollback release")
            revoked = {r[0] for r in conn.execute("SELECT record_id FROM records WHERE withdrawn=1")}
            if any(item["record"]["record_id"] in revoked for item in payload["records"]):
                raise Conflict("rollback cannot resurrect withdrawn records")
            conn.execute("UPDATE meta SET value=? WHERE key='active'", (release_id,))
            conn.execute("UPDATE meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self._audit(conn, "rollback", actor, {"release_id": release_id})

    def still_current(self, snapshot: dict) -> bool:
        with self.connect() as conn:
            meta = dict(conn.execute("SELECT key,value FROM meta").fetchall())
            return meta["active"] == snapshot["active"] and int(meta["epoch"]) == snapshot["epoch"]
