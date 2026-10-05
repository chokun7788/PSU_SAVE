from __future__ import annotations

import copy
import json
import os
import sqlite3
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from app.knowledge.answer import KnowledgeAnswerer, alias_matches, try_canonical_answer
from app.knowledge.records import digest, text_hash, validate_record
from app.knowledge.store import Conflict, KnowledgeStore
from app.pipeline.request_deadline import request_deadline


def game_record(title="Nebula Fields", record_id="demo_nebula") -> dict:
    overview = "เกมทดสอบจำลองการสำรวจดาวและสร้างฐาน เป็นข้อมูลสมมติสำหรับทดสอบระบบเท่านั้น"
    how_to = "เลือกโหมดสำรวจ เก็บทรัพยากร แล้วสร้างฐานบนดาวจำลอง"
    snapshot = f"แนวเกม: Sandbox\n{overview}\n{how_to}"
    ref = lambda quote: [{"source_id": "demo_guide", "quote": quote}]
    return {
        "schema_version": "2.1-pilot", "record_id": record_id, "type": "game", "title": title,
        "aliases": [title, "เนบิวลาฟิลด์"], "entity_id": "game:" + record_id,
        "scope": {"branch": "psu_phuket", "access": "public"},
        "effective_from": "2026-01-01T00:00:00+07:00", "valid_until": None,
        "facts": [
            {"fact_id": "genre", "predicate": "genre", "value": "Sandbox", "claim_status": "verified", "source_refs": ref("แนวเกม: Sandbox")},
            {"fact_id": "availability", "predicate": "service_availability", "value": None, "claim_status": "unknown", "source_refs": []},
        ],
        "sections": [
            {"section_id": "overview", "facet": "overview", "heading": "ลักษณะเกม", "text": overview,
             "depends_on": [], "source_refs": ref(overview)},
            {"section_id": "how", "facet": "how_to_play", "heading": "วิธีเริ่มเล่น", "text": how_to,
             "depends_on": ["overview"], "source_refs": ref(how_to)},
        ],
        "sources": [{"source_id": "demo_guide", "title": "คู่มือสมมติ", "url": "demo://nebula-guide",
                     "snapshot_text": snapshot, "snapshot_sha256": text_hash(snapshot),
                     "authority": ["genre", "overview", "how_to_play"]}],
    }


def rule_record() -> dict:
    record = game_record("กฎอาหารทดลอง", "demo_food_rule")
    record.update(type="rule", aliases=["กฎอาหารทดลอง", "Demo food rule"], entity_id="rule:demo_food")
    policy = "ห้ามนำอาหารเข้าโซน DEMO-A ยกเว้นพื้นที่รับประทานอาหารที่กำหนด"
    exception = "ข้อยกเว้นนี้ใช้เฉพาะพื้นที่รับประทานอาหาร ไม่ครอบคลุมบริเวณเครื่องเล่น"
    snapshot = policy + "\n" + exception
    record["facts"] = []
    record["sections"] = [
        {"section_id": "policy", "facet": "policy", "heading": "ข้อกำหนด", "text": policy,
         "depends_on": ["exceptions"], "source_refs": [{"source_id": "demo_guide", "quote": policy}]},
        {"section_id": "exceptions", "facet": "exceptions", "heading": "ขอบเขตข้อยกเว้น", "text": exception,
         "depends_on": [], "source_refs": [{"source_id": "demo_guide", "quote": exception}]},
    ]
    record["sources"][0].update(snapshot_text=snapshot, snapshot_sha256=text_hash(snapshot), authority=["policy", "exceptions"])
    return record


def fake_embed(texts):
    return [[1.0, 0.0] for _ in texts], {"model": "test-double", "dimensions": 2}


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = KnowledgeStore(Path(self.temp.name) / "knowledge.sqlite")
        self.store.initialize(allow_demo=True)
        self.answerer = KnowledgeAnswerer(self.store, embed=lambda q, m: ((1.0, 0.0), {"model": "test-double"}),
                                         order=lambda q, units: ([u["unit_id"] for u in units], {"attempted": True}))

    def approve(self, record=None, version=0):
        row = self.store.save(record or game_record(), actor="editor", expected_version=version)
        self.store.approve(row["record_id"], row["version"], row["hash"], actor="reviewer")
        return row

    def publish(self, key="p1", embed=fake_embed):
        return self.store.publish(actor="reviewer", request_key=key, expected_active=self.store.snapshot()["active"], embed=embed)

    def ready(self):
        self.approve()
        return self.publish()

    def ask(self, query, **kwargs):
        with request_deadline(9):
            return self.answerer.answer(query, allow_llm=True, **kwargs)

    def test_default_feature_off_does_not_open_database(self):
        with patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "0"}), patch.object(KnowledgeStore, "snapshot", side_effect=AssertionError):
            self.assertIsNone(try_canonical_answer("hello", allow_llm=True))

    def test_missing_enabled_db_fails_closed_without_creating_file(self):
        path = str(Path(self.temp.name) / "missing.sqlite")
        with patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "1", "PSU_KNOWLEDGE_DB": path}):
            self.assertEqual(try_canonical_answer("Nebula Fields แนวไหน", allow_llm=True).mode, "canonical_busy")
        self.assertFalse(Path(path).exists())

    def test_demo_records_rejected_in_normal_store(self):
        store = KnowledgeStore(Path(self.temp.name) / "real.sqlite")
        store.initialize()
        with self.assertRaises(ValueError):
            store.save(game_record(), actor="editor", expected_version=0)

    def test_demo_db_needs_separate_runtime_opt_in(self):
        self.ready()
        with patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "1", "PSU_KNOWLEDGE_DB": str(self.store.path), "PSU_KNOWLEDGE_ALLOW_DEMO": "0"}):
            self.assertEqual(try_canonical_answer("Nebula Fields แนวไหน", allow_llm=True).mode, "canonical_busy")

    def test_schema_rejects_unknown_fields(self):
        record = game_record()
        record["auto_publish"] = True
        with self.assertRaises(ValueError):
            validate_record(record, allow_demo=True)

    def test_schema_rejects_internal_scope(self):
        record = game_record()
        record["scope"]["access"] = "internal"
        with self.assertRaises(ValueError):
            validate_record(record, allow_demo=True)

    def test_schema_requires_timezone(self):
        record = game_record()
        record["effective_from"] = "2026-01-01T00:00:00"
        with self.assertRaises(ValueError):
            validate_record(record, allow_demo=True)

    def test_schema_rejects_unknown_as_false(self):
        record = game_record()
        record["facts"][1]["value"] = False
        with self.assertRaises(ValueError):
            validate_record(record, allow_demo=True)

    def test_schema_checks_boolean_exact_type(self):
        record = game_record()
        record["facts"][1].update(value=1, claim_status="verified")
        with self.assertRaises(ValueError):
            validate_record(record, allow_demo=True)

    def test_source_hash_and_quote_are_checked(self):
        for change in ("hash", "quote", "authority"):
            with self.subTest(change=change):
                record = game_record()
                if change == "hash":
                    record["sources"][0]["snapshot_sha256"] = "wrong"
                elif change == "quote":
                    record["sections"][0]["source_refs"][0]["quote"] = "not in source"
                else:
                    record["sources"][0]["authority"] = []
                with self.assertRaises(ValueError):
                    validate_record(record, allow_demo=True)

    def test_cycles_and_missing_dependencies_are_rejected(self):
        for dependency in ("how", "missing"):
            with self.subTest(dependency=dependency):
                record = game_record()
                record["sections"][0]["depends_on"] = [dependency]
                with self.assertRaises(ValueError):
                    validate_record(record, allow_demo=True)

    def test_unapproved_draft_not_published(self):
        self.store.save(game_record(), actor="editor", expected_version=0)
        with self.assertRaises(Conflict):
            self.publish()
        self.assertEqual(self.store.snapshot()["active"], "")

    def test_stale_save_does_not_lose_update(self):
        self.approve()
        with self.assertRaises(Conflict):
            self.store.save(game_record(), actor="editor2", expected_version=0)

    def test_approval_hash_and_head_are_bound(self):
        row = self.approve()
        with self.assertRaises(Conflict):
            self.store.approve(row["record_id"], 1, "wrong", actor="reviewer")
        self.store.save(game_record(), actor="editor", expected_version=1)
        with self.assertRaises(Conflict):
            self.store.approve(row["record_id"], 1, row["hash"], actor="reviewer")

    def test_publish_both_projections(self):
        self.ready()
        release = self.store.snapshot()["release"]
        self.assertEqual(release["structured"]["demo_nebula"][0]["value"], "Sandbox")
        self.assertEqual(len(release["rag"]), 2)

    def test_publish_retry_does_not_rebuild(self):
        first = self.ready()
        retried = self.store.publish(actor="reviewer", request_key="p1", expected_active="",
                                     embed=lambda _: self.fail("retry rebuilt index"))
        self.assertEqual(retried, first)

    def test_publish_key_cannot_be_reused_for_different_base(self):
        self.ready()
        with self.assertRaises(Conflict):
            self.publish()

    def test_embedding_failure_keeps_previous_release(self):
        first = self.ready()
        self.approve(version=1)
        def fail(_):
            raise TimeoutError("simulated")
        with self.assertRaises(TimeoutError):
            self.publish("p2", fail)
        self.assertEqual(self.store.snapshot()["active"], first)

    def test_invalid_vectors_never_activate(self):
        self.approve()
        for vectors in ([], [[float("nan"), 0]] * 2, [[0, 0]] * 2, [[1]] * 2):
            with self.subTest(vectors=vectors):
                with self.assertRaises(ValueError):
                    self.publish(embed=lambda _, v=vectors: (v, {"model": "fake", "dimensions": 2}))
        self.assertEqual(self.store.snapshot()["active"], "")

    def test_edit_during_build_rejects_activation(self):
        self.approve()
        def concurrent(texts):
            self.store.save(game_record(), actor="editor2", expected_version=1)
            return fake_embed(texts)
        with self.assertRaises(Conflict):
            self.publish(embed=concurrent)
        self.assertEqual(self.store.snapshot()["active"], "")

    def test_withdraw_during_build_rejects_activation(self):
        first = self.ready()
        def concurrent(texts):
            self.store.withdraw("demo_nebula", actor="reviewer")
            return fake_embed(texts)
        with self.assertRaises(Conflict):
            self.publish("p2", concurrent)
        self.assertEqual(self.store.snapshot()["active"], first)

    def test_alias_collisions_rejected(self):
        self.approve()
        self.approve(game_record("Other game", "other"))
        with self.assertRaises(ValueError):
            self.publish()

    def test_exact_fact_does_not_wait_for_models(self):
        self.ready()
        self.answerer.embed = lambda *_: self.fail("unnecessary embedding")
        self.answerer.order = lambda *_: self.fail("unnecessary LLM")
        result = self.ask("Nebula Fields แนวไหน")
        self.assertEqual(result.mode, "canonical_answer")
        self.assertIn("Sandbox", result.answer)
        self.assertTrue(result.hits)

    def test_rag_uses_correct_facet_and_dependencies(self):
        self.ready()
        result = self.ask("Nebula Fields เล่นยังไง")
        self.assertEqual(result.mode, "canonical_answer")
        self.assertIn("เลือกโหมดสำรวจ", result.answer)
        self.assertIn("ข้อมูลสมมติ", result.answer)
        self.assertTrue(any(t.stage == "knowledge_retrieval" for t in result.trace))
        self.assertEqual(len(result.hits), 1)
        self.assertNotIn("[S2]", result.answer)

    def test_concurrent_publish_has_one_winner(self):
        self.approve()
        barrier = threading.Barrier(2)
        def build(texts):
            barrier.wait(timeout=3)
            return fake_embed(texts)
        def publish(key):
            try:
                return self.store.publish(actor="reviewer", request_key=key, expected_active="", embed=build)
            except Conflict:
                return None
        with ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(publish, ["a", "b"]))
        self.assertEqual(sum(x is not None for x in outcomes), 1)
        self.assertIn(self.store.snapshot()["active"], outcomes)

    def test_thirty_exact_requests_do_not_invoke_models(self):
        self.ready()
        self.answerer.embed = lambda *_: self.fail("exact path used model")
        with ThreadPoolExecutor(max_workers=30) as pool:
            outcomes = list(pool.map(lambda _: self.ask("Nebula Fields แนวไหน"), range(30)))
        self.assertTrue(all(r.mode == "canonical_answer" for r in outcomes))

    def test_web_guard_still_runs_before_pipeline(self):
        import http.client
        from http.server import ThreadingHTTPServer
        from app.web_api import server as web
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        self.ready()
        guard = RuntimeInputQualityGuard.from_environment()
        guard.mode = "enforce"
        handler = ThreadingHTTPServer(("127.0.0.1", 0), web.ChatHandler)
        thread = threading.Thread(target=handler.serve_forever, daemon=True)
        thread.start()
        try:
            with patch.object(web, "INPUT_QUALITY_GUARD", guard), patch.object(web, "_write_chat_log_async"), \
                    patch.object(web, "answer_question_pipeline_debug", side_effect=AssertionError("guard bypassed")):
                conn = http.client.HTTPConnection("127.0.0.1", handler.server_port, timeout=5)
                conn.request("POST", "/api/chat", json.dumps({"question": "g]jo"}), {"Content-Type": "application/json"})
                response = conn.getresponse()
                body = json.loads(response.read())
                conn.close()
                self.assertEqual(response.status, 200)
                self.assertIn("answer", body)
        finally:
            handler.shutdown()
            handler.server_close()
            thread.join(timeout=3)

    def test_web_request_can_read_new_record_without_old_catalog_entry(self):
        import http.client
        from http.server import ThreadingHTTPServer
        from app.web_api import server as web
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        self.ready()
        guard = RuntimeInputQualityGuard.from_environment()
        guard.mode = "enforce"
        handler = ThreadingHTTPServer(("127.0.0.1", 0), web.ChatHandler)
        thread = threading.Thread(target=handler.serve_forever, daemon=True)
        thread.start()
        try:
            with patch.object(web, "INPUT_QUALITY_GUARD", guard), patch.object(web, "_write_chat_log_async"), \
                    patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "1", "PSU_KNOWLEDGE_DB": str(self.store.path), "PSU_KNOWLEDGE_ALLOW_DEMO": "1"}):
                conn = http.client.HTTPConnection("127.0.0.1", handler.server_port, timeout=5)
                conn.request("POST", "/api/chat", json.dumps({"question": "Nebula Fields แนวไหน", "experimental_allow_llm": True}),
                             {"Content-Type": "application/json"})
                response = conn.getresponse()
                body = json.loads(response.read())
                conn.close()
                self.assertEqual(response.status, 200)
                self.assertEqual(body["mode"], "canonical_answer")
                self.assertIn("Sandbox", body["answer"])
                self.assertTrue(body["sources"])
        finally:
            handler.shutdown()
            handler.server_close()
            thread.join(timeout=3)

    def test_expired_request_returns_no_claim_timeout(self):
        self.ready()
        with request_deadline(0.000001):
            result = self.answerer.answer("Nebula Fields แนวไหน", allow_llm=True)
        self.assertEqual(result.mode, "canonical_timeout")
        self.assertFalse(result.hits)
        self.assertNotIn("Sandbox", result.answer)

    def test_unknown_availability_is_not_false_or_howto(self):
        self.ready()
        result = self.ask("Nebula Fields มีให้เล่นไหม")
        self.assertEqual(result.mode, "canonical_no_answer")
        self.assertNotIn("เลือกโหมด", result.answer)
        self.assertNotIn("ไม่มีให้บริการ", result.answer)

    def test_partial_keeps_missing_obligation_explicit(self):
        self.ready()
        result = self.ask("Nebula Fields เล่นยังไง และมีให้เล่นไหม")
        self.assertEqual(result.mode, "canonical_partial")
        self.assertIn("การให้บริการ: ยังไม่มีข้อมูลยืนยัน", result.answer)

    def test_rule_keeps_exception(self):
        self.approve(rule_record())
        self.publish()
        result = self.ask("กฎอาหารทดลอง คืออะไร")
        self.assertEqual(result.mode, "canonical_answer")
        self.assertIn("ไม่ครอบคลุมบริเวณเครื่องเล่น", result.answer)

    def test_model_cannot_drop_exception_or_add_unknown_id(self):
        self.ready()
        for ids in (["invented"], ["demo_nebula:how"], ["demo_nebula:how"] * 2):
            with self.subTest(ids=ids):
                self.answerer.order = lambda *_: (ids, {"attempted": True})
                result = self.ask("Nebula Fields เล่นยังไง")
                self.assertIn("ข้อมูลสมมติ", result.answer)
                self.assertTrue(any(t.decision == "checked_draft_fallback" for t in result.trace))

    def test_embedding_timeout_does_not_fall_back_to_legacy(self):
        self.ready()
        def fail(*_):
            raise TimeoutError("simulated")
        self.answerer.embed = fail
        self.assertEqual(self.ask("Nebula Fields เล่นยังไง").mode, "canonical_busy")

    def test_update_visible_without_reader_code_change(self):
        self.ready()
        record = game_record()
        record["facts"][0]["value"] = "Puzzle"
        source = record["sources"][0]
        source["snapshot_text"] = source["snapshot_text"].replace("Sandbox", "Puzzle")
        source["snapshot_sha256"] = text_hash(source["snapshot_text"])
        record["facts"][0]["source_refs"][0]["quote"] = "แนวเกม: Puzzle"
        self.approve(record, version=1)
        self.publish("p2")
        result = self.ask("Nebula Fields แนวไหน")
        self.assertIn("Puzzle", result.answer)
        self.assertNotIn("Sandbox", result.answer)

    def test_withdraw_and_empty_publish_keep_tombstone(self):
        self.ready()
        self.store.withdraw("demo_nebula", actor="reviewer")
        self.publish("p2")
        self.assertEqual(self.ask("Nebula Fields แนวไหน").mode, "canonical_no_answer")

    def test_revision_change_during_answer_suppresses_old_output(self):
        self.ready()
        def change(question, units):
            self.store.withdraw("demo_nebula", actor="reviewer")
            return [u["unit_id"] for u in units], {}
        self.answerer.order = change
        result = self.ask("Nebula Fields เล่นยังไง")
        self.assertEqual(result.mode, "canonical_no_answer")
        self.assertFalse(result.hits)
        self.assertTrue(all(o["status"] == "suppressed" for o in result.decision_artifact["obligations"]))

    def test_expired_and_future_records_do_not_answer(self):
        record = game_record()
        record["valid_until"] = "2026-09-01T00:00:00+07:00"
        self.approve(record)
        self.publish()
        for moment in (datetime(2025, 1, 1, tzinfo=timezone.utc), datetime(2026, 9, 1, tzinfo=timezone.utc)):
            with self.subTest(moment=moment):
                self.assertEqual(self.ask("Nebula Fields แนวไหน", now=moment).mode, "canonical_no_answer")

    def test_valid_until_boundary_exclusive(self):
        record = game_record()
        record["valid_until"] = "2026-09-01T00:00:00+07:00"
        self.approve(record)
        self.publish()
        self.assertEqual(self.ask("Nebula Fields แนวไหน", now=datetime.fromisoformat(record["valid_until"])).mode, "canonical_no_answer")

    def test_rollback_rejects_withdrawn_record(self):
        first = self.ready()
        self.store.withdraw("demo_nebula", actor="reviewer")
        with self.assertRaises(Conflict):
            self.store.rollback(first, actor="reviewer", expected_active=first)

    def test_rollback_and_stale_rollback(self):
        first = self.ready()
        self.approve(version=1)
        second = self.publish("p2")
        with self.assertRaises(Conflict):
            self.store.rollback(first, actor="reviewer", expected_active=first)
        self.store.rollback(first, actor="reviewer", expected_active=second)
        self.assertEqual(self.store.snapshot()["active"], first)

    def test_unknown_question_preserves_legacy_dispatch(self):
        self.ready()
        self.assertIsNone(self.ask("ร้านเปิดกี่โมง"))

    def test_incomplete_catalog_does_not_count(self):
        self.ready()
        self.assertEqual(self.ask("มีเกมทั้งหมดกี่เกม").mode, "canonical_clarification")

    def test_unsupported_calculation_platform_and_mutation_clarify(self):
        self.ready()
        for q in ("Nebula Fields ราคาเท่าไร", "Nebula Fields บน PS5 เล่นยังไง", "จอง Nebula Fields", "Nebula Fields พรุ่งนี้มีให้เล่นไหม"):
            with self.subTest(question=q):
                self.assertEqual(self.ask(q).mode, "canonical_clarification")

    def test_multiple_owned_entities_clarify(self):
        self.approve()
        other = game_record("Copper Meadow", "demo_copper")
        other["aliases"] = ["Copper Meadow"]
        self.approve(other)
        self.publish()
        self.assertEqual(self.ask("Nebula Fields กับ Copper Meadow เล่นยังไง").mode, "canonical_clarification")

    def test_latin_alias_has_token_boundaries(self):
        self.assertFalse(alias_matches("XNebula FieldsZ", "Nebula Fields"))
        self.assertTrue(alias_matches("NEBULA FIELDS เล่นยังไง", "Nebula Fields"))

    def test_integrity_failure_never_reads_tampered_release(self):
        first = self.ready()
        with self.store.connect(write=True) as conn:
            conn.execute("UPDATE releases SET payload='{}' WHERE release_id=?", (first,))
        with self.assertRaises(ValueError):
            self.store.snapshot()

    def test_pipeline_entrypoint_handles_owned_before_legacy(self):
        self.ready()
        from app.pipeline.engine import AnswerQualityPipeline
        with patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "1", "PSU_KNOWLEDGE_DB": str(self.store.path), "PSU_KNOWLEDGE_ALLOW_DEMO": "1"}):
            result = AnswerQualityPipeline().answer("Nebula Fields แนวไหน", experimental_allow_llm=True, global_timeout_sec=9)
        self.assertEqual(result.mode, "canonical_answer")


if __name__ == "__main__":
    unittest.main(verbosity=2)
