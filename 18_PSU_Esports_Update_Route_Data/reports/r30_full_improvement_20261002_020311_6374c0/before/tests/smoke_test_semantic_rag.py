from __future__ import annotations

import json
import os
import sys
import tempfile
import hashlib
from datetime import date, timedelta
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.answer_contracts import validate_answer_contract  # noqa: E402
from app.pipeline.query_signals import has_live_evidence  # noqa: E402
from app.pipeline.question_frame import FrameTarget, QuestionFrame, build_question_frame  # noqa: E402
from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.semantic_vector_retrieval import (  # noqa: E402
    answer_from_semantic_hits,
    refine_route_with_semantic_evidence,
    retrieve_semantic_guarded,
    semantic_hits_have_current_evidence,
)
from app.pipeline.source_guard import assess_sources  # noqa: E402
from tools.ingest_rag_documents import ingest, validate_document  # noqa: E402


def _published_document(**overrides):
    future = (date.today() + timedelta(days=30)).isoformat()
    document = {
        "id": "test_dynamic_document",
        "title": "ข้อมูลทดสอบ Semantic RAG",
        "text": "รายละเอียดทดสอบย่อหน้าแรก\n\nรายละเอียดทดสอบย่อหน้าที่สอง",
        "category": "knowledge",
        "source_url": "local://tests/semantic-rag",
        "trust_level": "internal_verified",
        "updated_at": date.today().isoformat(),
        "status": "published",
        "content_type": "document",
        "entity_ids": ["test_dynamic_document"],
        "facets": ["overview"],
        "language": "th",
        "source_language": "th",
        "version": 1,
        "approved_by": "test_reviewer",
        "approved_at": f"{date.today().isoformat()}T09:00:00+07:00",
        "tags": ["semantic", "test"],
        "time_sensitive": False,
        "freshness_verified": False,
        "valid_until": future,
    }
    document.update(overrides)
    document.setdefault("source_snapshot_text", document["text"])
    document.setdefault("source_snapshot_sha256", hashlib.sha256(document["source_snapshot_text"].encode("utf-8")).hexdigest())
    return document


def _index(rows):
    return {
        "version": 1,
        "backend": "test_dense",
        "model": "test-embedding",
        "dimensions": 2,
        "doc_count": len(rows),
        "docs": rows,
    }


def _doc(row, vector):
    return {
        "id": row["id"],
        "category": row["category"],
        "title": row["title"],
        "dynamic": True,
        "vector": vector,
        "row": row,
    }


def test_ingestion_requires_publish_metadata_and_replaces_document() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        source = root / "documents.json"
        output = root / "dynamic_knowledge.jsonl"
        source.write_text(
            json.dumps([_published_document()], ensure_ascii=False),
            encoding="utf-8",
        )
        first = ingest(source, output_path=output, max_chars=300, overlap_chars=40)
        assert not first.errors, first.errors
        assert first.published_documents == 1
        assert first.ready_document_ids == ["test_dynamic_document"]
        assert first.status_counts == {"published": 1}
        assert first.output_chunks >= 1
        rows = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()]
        assert rows[0]["search_text"].startswith("[Type: document]")
        assert rows[0]["entity_ids"] == ["test_dynamic_document"]

        updated = _published_document(text="ข้อมูลฉบับปรับปรุงที่ต้องแทนเอกสารเดิม")
        updated["source_snapshot_text"] = updated["text"]
        updated["source_snapshot_sha256"] = hashlib.sha256(updated["text"].encode("utf-8")).hexdigest()
        source.write_text(json.dumps([updated], ensure_ascii=False), encoding="utf-8")
        second = ingest(source, output_path=output, max_chars=300, overlap_chars=40)
        rows = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()]
        assert second.replaced_documents == 1
        assert all(row["document_id"] == "test_dynamic_document" for row in rows)
        assert any("ฉบับปรับปรุง" in row["text"] for row in rows)


def test_ingestion_preflight_lists_pending_documents_without_publishing() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        source = root / "documents.json"
        pending = _published_document(id="pending_rule", status="in_review")
        source.write_text(json.dumps([pending], ensure_ascii=False), encoding="utf-8")
        report = ingest(source, output_path=root / "dynamic_knowledge.jsonl", validate_only=True)
        assert not report.errors, report.errors
        assert report.published_documents == 0
        assert report.ready_document_ids == []
        assert report.pending_document_ids == {"in_review": ["pending_rule"]}


def test_secondary_source_cannot_claim_current_verified_state() -> None:
    document = _published_document(
        trust_level="secondary",
        freshness_verified=True,
        retrieved_at="2026-08-23T10:00:00+07:00",
        time_sensitive=True,
    )
    try:
        validate_document(document)
    except ValueError as exc:
        assert "secondary" in str(exc)
    else:
        raise AssertionError("secondary freshness verification must be rejected")


def test_published_document_requires_human_approval_and_immutable_source() -> None:
    for field in ("approved_by", "approved_at", "source_snapshot_text", "source_snapshot_sha256"):
        document = _published_document()
        document[field] = ""
        try:
            validate_document(document)
        except ValueError:
            pass
        else:
            raise AssertionError(f"published document without {field} must be rejected")

    document = _published_document()
    document["source_snapshot_sha256"] = "invalid"
    try:
        validate_document(document)
    except ValueError as exc:
        assert "source_snapshot_sha256" in str(exc)
    else:
        raise AssertionError("source hash mismatch must be rejected")


def test_chunk_hash_changes_when_retrieval_scope_changes() -> None:
    from tools.ingest_rag_documents import document_to_chunks

    first = document_to_chunks(_published_document(entity_ids=["valorant"], facets=["overview"]))
    second = document_to_chunks(_published_document(entity_ids=["overcooked_2"], facets=["overview"]))
    assert first[0]["content_hash"] != second[0]["content_hash"]


def test_semantic_retrieval_rejects_wrong_target_even_when_score_is_higher() -> None:
    wrong = _published_document(
        id="overcooked_detail",
        category="games",
        entity_ids=["overcooked_2"],
        facets=["overview"],
        text="Overcooked 2 is a cooperative cooking game.",
        language="en",
        source_language="en",
    )
    right = _published_document(
        id="valorant_detail",
        category="games",
        entity_ids=["valorant"],
        facets=["overview"],
        text="VALORANT is a tactical team shooter.",
        language="en",
        source_language="en",
    )
    route = PipelineRoute("games", "game_detail", 0.95, "fact", "low", "test")
    hits, trace = retrieve_semantic_guarded(
        "What is VALORANT?",
        route,
        query_vector=(1.0, 0.0),
        index=_index([_doc(wrong, [1.0, 0.0]), _doc(right, [0.9, 0.43589])]),
        required_entity_ids=["valorant"],
        required_facets=["overview"],
        locale="en",
    )
    assert hits and hits[0]["id"] == "valorant_detail", (hits, trace)
    assert trace.metadata["blocked"]["entity_mismatch"] == 1


def test_semantic_retrieval_rejects_wrong_facet_and_language() -> None:
    wrong = _published_document(
        id="valorant_controls_th",
        category="games",
        entity_ids=["valorant"],
        facets=["controls"],
        text="ข้อมูลปุ่มควบคุม VALORANT",
        language="th",
    )
    route = PipelineRoute("games", "game_detail", 0.95, "fact", "low", "test")
    hits, trace = retrieve_semantic_guarded(
        "What is VALORANT?",
        route,
        query_vector=(1.0, 0.0),
        index=_index([_doc(wrong, [1.0, 0.0])]),
        required_entity_ids=["valorant"],
        required_facets=["overview"],
        locale="en",
    )
    assert not hits
    assert trace.metadata["blocked"]["facet_mismatch"] == 1


def test_answer_contract_rejects_dynamic_evidence_for_another_target() -> None:
    wrong = _published_document(
        id="overcooked_detail_contract",
        category="games",
        entity_ids=["overcooked_2"],
        facets=["overview"],
        text="Overcooked 2 is a cooperative cooking game.",
        language="en",
        source_language="en",
    )
    frame = QuestionFrame(
        operation="game_detail",
        domain="games",
        expected_answer_types=("game_detail",),
        targets=(FrameTarget("valorant", "game", "games", "VALORANT", 1.0),),
        target_status="exact",
        target_required=True,
        confidence=1.0,
    )
    result = validate_answer_contract(
        "What is VALORANT?",
        "VALORANT is a tactical shooter.",
        PipelineRoute("games", "game_detail", 0.95, "fact", "low", "test"),
        hits=[{"id": wrong["id"], "metadata": {**wrong, "dynamic_knowledge": True}}],
        mode="pipeline:semantic_rag_dynamic",
        frame=frame,
    )
    assert "answer_contract_dynamic_evidence_target_mismatch" in result.errors


def test_semantic_evidence_route_overrides_ambiguous_competition_wording() -> None:
    route = PipelineRoute("knowledge", "knowledge_lookup", 0.91, "summary", "low", "test")
    intent = UniversalIntent(
        domain="knowledge",
        operation="detail",
        target="",
        filters={"semantic_route_category": "knowledge"},
        needs=("verified_evidence",),
        answer_style="summary_bullets",
        confidence=0.91,
        method="semantic_evidence",
        reason="test semantic route lock",
    )
    question = "อีสปอร์ตเริ่มมีการแข่งขันครั้งแรกเมื่อไหร่"
    frame = build_question_frame(question, route, intent)
    assert frame.operation == "semantic_evidence_lookup", frame
    assert frame.domain == "knowledge", frame

    validation = validate_answer_contract(
        question,
        "การแข่งขันอีสปอร์ตครั้งแรกเกิดขึ้นตามหลักฐานในบทความที่ตรวจสอบแล้ว",
        route,
        hits=[{"category": "knowledge", "source_url": "local://tests/knowledge"}],
        mode="pipeline:semantic_rag_dynamic",
        intent=intent,
    )
    assert validation.ok, validation.errors


def test_knowledge_answer_with_competition_word_is_still_a_fact() -> None:
    route = PipelineRoute("knowledge", "knowledge_lookup", 0.88, "summary", "low", "test")
    result = validate_answer_contract(
        "อีสปอร์ตเริ่มมีประวัติอย่างไร",
        "อีสปอร์ตเริ่มต้นจากการแข่งขันเกม Spacewar ในปี ค.ศ. 1972",
        route,
        hits=[{"category": "knowledge", "source_url": "local://tests/knowledge"}],
        mode="pipeline:experimental_rag_direct_fallback",
    )
    assert result.ok, result.errors


def test_semantic_route_refiner_keeps_explicit_game_target() -> None:
    import app.pipeline.semantic_vector_retrieval as semantic

    previous_enabled = semantic.semantic_retrieval_enabled
    previous_hint = semantic.has_explicit_game_hint
    semantic.semantic_retrieval_enabled = lambda: True
    semantic.has_explicit_game_hint = lambda _query: True
    try:
        route = PipelineRoute("games", "game_detail_lookup", 0.95, "fact", "low", "test")
        refined, trace = refine_route_with_semantic_evidence("TEKKEN 8 คืออะไร", route)
    finally:
        semantic.semantic_retrieval_enabled = previous_enabled
        semantic.has_explicit_game_hint = previous_hint
    assert refined == route
    assert trace.decision == "kept_explicit_game_target"


def test_semantic_general_route_requires_dynamic_trusted_document() -> None:
    top = _published_document(
        id="semantic_top",
        title="หัวข้อใหม่ของศูนย์",
        text="คำตอบจากเอกสารใหม่ที่ผ่านการตรวจสอบแล้ว",
    )
    second = _published_document(
        id="semantic_other",
        title="หัวข้ออื่น",
        text="ข้อมูลคนละเรื่อง",
    )
    route = PipelineRoute("general", "general_lookup", 0.55, "summary", "low", "test")
    hits, trace = retrieve_semantic_guarded(
        "หัวข้อใหม่ของศูนย์",
        route,
        query_vector=(1.0, 0.0),
        index=_index([_doc(top, [1.0, 0.0]), _doc(second, [0.4, 0.916515])]),
    )
    assert trace.decision == "ollama_dense_guarded", trace
    assert hits and hits[0]["id"] == "semantic_top", hits
    answer, raw_hits, confidence = answer_from_semantic_hits(hits)
    assert answer and "ผ่านการตรวจสอบ" in answer
    assert raw_hits[0]["metadata"]["trust_level"] == "internal_verified"
    assert confidence >= 0.78


def test_current_question_requires_time_bounded_verified_evidence() -> None:
    future = (date.today() + timedelta(days=7)).isoformat()
    current = _published_document(
        id="current_news",
        category="events_news",
        title="ข่าวล่าสุดที่ตรวจสอบแล้ว",
        time_sensitive=True,
        freshness_verified=True,
        retrieved_at=f"{date.today().isoformat()}T09:00:00+07:00",
        valid_until=future,
    )
    route = PipelineRoute("events_news", "news_lookup", 0.9, "fact", "medium", "test")
    hits, _ = retrieve_semantic_guarded(
        "ข่าวล่าสุด",
        route,
        require_current=True,
        query_vector=(1.0, 0.0),
        index=_index([_doc(current, [1.0, 0.0])]),
    )
    assert semantic_hits_have_current_evidence(hits)
    _, raw_hits, _ = answer_from_semantic_hits(hits)
    assert has_live_evidence(raw_hits)


def test_source_guard_marks_expired_time_sensitive_source() -> None:
    expired = (date.today() - timedelta(days=1)).isoformat()
    quality = assess_sources([{
        "id": "expired_source",
        "category": "events_news",
        "text": "ข้อมูลหมดอายุ",
        "trust_level": "official",
        "time_sensitive": True,
        "valid_until": expired,
    }])
    assert quality.stale
    assert "time_sensitive_source_expired" in quality.warnings


if __name__ == "__main__":
    tests = [
        test_ingestion_requires_publish_metadata_and_replaces_document,
        test_ingestion_preflight_lists_pending_documents_without_publishing,
        test_secondary_source_cannot_claim_current_verified_state,
        test_published_document_requires_human_approval_and_immutable_source,
        test_chunk_hash_changes_when_retrieval_scope_changes,
        test_semantic_retrieval_rejects_wrong_target_even_when_score_is_higher,
        test_semantic_retrieval_rejects_wrong_facet_and_language,
        test_answer_contract_rejects_dynamic_evidence_for_another_target,
        test_semantic_evidence_route_overrides_ambiguous_competition_wording,
        test_knowledge_answer_with_competition_word_is_still_a_fact,
        test_semantic_route_refiner_keeps_explicit_game_target,
        test_semantic_general_route_requires_dynamic_trusted_document,
        test_current_question_requires_time_bounded_verified_evidence,
        test_source_guard_marks_expired_time_sensitive_source,
    ]
    for test in tests:
        test()
        print(f"OK {test.__name__}")
    print("SEMANTIC RAG SMOKE TEST OK")
