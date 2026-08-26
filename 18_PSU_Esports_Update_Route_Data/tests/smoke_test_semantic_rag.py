from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.answer_contracts import validate_answer_contract  # noqa: E402
from app.pipeline.query_signals import has_live_evidence  # noqa: E402
from app.pipeline.question_frame import build_question_frame  # noqa: E402
from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.semantic_vector_retrieval import (  # noqa: E402
    answer_from_semantic_hits,
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
        "tags": ["semantic", "test"],
        "time_sensitive": False,
        "freshness_verified": False,
        "valid_until": future,
    }
    document.update(overrides)
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
        assert first.output_chunks >= 1

        updated = _published_document(text="ข้อมูลฉบับปรับปรุงที่ต้องแทนเอกสารเดิม")
        source.write_text(json.dumps([updated], ensure_ascii=False), encoding="utf-8")
        second = ingest(source, output_path=output, max_chars=300, overlap_chars=40)
        rows = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()]
        assert second.replaced_documents == 1
        assert all(row["document_id"] == "test_dynamic_document" for row in rows)
        assert any("ฉบับปรับปรุง" in row["text"] for row in rows)


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
        test_secondary_source_cannot_claim_current_verified_state,
        test_semantic_evidence_route_overrides_ambiguous_competition_wording,
        test_semantic_general_route_requires_dynamic_trusted_document,
        test_current_question_requires_time_bounded_verified_evidence,
        test_source_guard_marks_expired_time_sensitive_source,
    ]
    for test in tests:
        test()
        print(f"OK {test.__name__}")
    print("SEMANTIC RAG SMOKE TEST OK")
