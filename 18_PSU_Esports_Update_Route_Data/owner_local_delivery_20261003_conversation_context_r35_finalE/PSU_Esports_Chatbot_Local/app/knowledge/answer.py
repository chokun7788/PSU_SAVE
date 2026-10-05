from __future__ import annotations

import os
import re
import sqlite3
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from app.knowledge.local_models import embed_question, order_evidence
from app.knowledge.records import FACTS, REGISTRY_VERSION, digest, timestamp
from app.knowledge.store import KnowledgeStore
from app.pipeline.request_deadline import remaining_sec
from app.pipeline.schemas import EntityBundle, PipelineAnswer, PipelineRoute, PipelineTrace, ValidationResult
from app.pipeline.vector_retrieval import embed_text, _cosine_sparse


ROOT = Path(__file__).resolve().parents[2]
SIGNALS = {
    "genre": ("แนวไหน", "แนวอะไร", "ประเภทไหน", "genre", "what kind"),
    "service_availability": ("มีให้เล่น", "มีเกมนี้", "มีเกม", "มีไหม", "มีมั้ย", "available", "do you have"),
    "available_at": ("โซนไหน", "อยู่ไหน", "อยู่ที่ไหน", "which zone", "where"),
    "how_to_play": ("เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "สอนเล่น", "เริ่มเล่น", "how to play"),
    "controls": ("ปุ่ม", "ควบคุม", "บังคับ", "controls", "buttons"),
    "overview": ("คืออะไร", "เกี่ยวกับอะไร", "แนะนำ", "what is", "describe"),
    "policy": ("กฎอะไร", "กฎมีอะไร", "สรุปกฎ", "กฎว่า", "กฎเป็น", "กติกาอะไร", "summarize the rule", "what are the rules"),
}
LABELS = {"genre": "แนวเกม", "service_availability": "การให้บริการ", "available_at": "โซนที่ให้บริการ",
          "how_to_play": "วิธีเล่น", "controls": "การควบคุม", "overview": "รายละเอียด", "policy": "กฎและข้อยกเว้น"}
SAFE = {
    "clarification": "กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ",
    "no_answer": "ยังไม่มีข้อมูลที่อนุมัติและยืนยันคำตอบนี้ได้ครับ กรุณาตรวจสอบกับเจ้าหน้าที่",
    "timeout": "ขณะนี้ตรวจสอบข้อมูลไม่ทันเวลาที่กำหนด กรุณาลองใหม่อีกครั้งครับ",
    "busy": "ขณะนี้ระบบตรวจสอบข้อมูลไม่พร้อม กรุณาลองใหม่อีกครั้งครับ",
}
UNSUPPORTED = re.compile(r"ราคา|กี่บาท|ถูกที่สุด|ทั้งหมด|กี่เกม|เปรียบเทียบ|เทียบกับ|จอง|ยกเลิก|ชำระ|"
                         r"พรุ่งนี้|วันนี้|เมื่อวาน|นักศึกษา|บุคคลภายนอก|ศิษย์เก่า|\d|ps5|\bpc\b|switch|"
                         r"price|cheapest|compare|total|book|cancel|tomorrow", re.I)


def _normal(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).casefold().split())


def alias_matches(question: str, alias: str) -> bool:
    pattern = re.escape(_normal(alias))
    if re.search(r"[a-z0-9]", alias, re.I):
        pattern = r"(?<![a-z0-9])" + pattern + r"(?![a-z0-9])"
    return bool(re.search(pattern, _normal(question)))


def _trace(stage: str, decision: str, started: float, **metadata) -> PipelineTrace:
    return PipelineTrace(stage, decision, 0.0, "", {"elapsed_ms": round((time.perf_counter() - started) * 1000, 2), **metadata})


class KnowledgeAnswerer:
    def __init__(self, store: KnowledgeStore, *, embed: Callable = embed_question, order: Callable = order_evidence):
        self.store = store
        self.embed = embed
        self.order = order

    def _finish(self, *, snapshot: dict | None, started: float, trace: list, response_type: str,
                answer: str = "", hits: list | None = None, obligations: list | None = None) -> PipelineAnswer:
        check_started = time.perf_counter()
        hits = hits or []
        obligations = obligations or []
        if response_type not in {*SAFE, "answer", "partial"}:
            raise ValueError("invalid response type")
        if response_type in {"answer", "partial"}:
            supported = [o for o in obligations if o["status"] == "supported"]
            if not supported or not answer or not hits:
                response_type = "no_answer"
        if snapshot is not None and not self.store.still_current(snapshot):
            trace.append(_trace("knowledge_finalizer", "release_changed", check_started))
            response_type = "no_answer"
        if remaining_sec() is not None and remaining_sec() <= 0:
            response_type = "timeout"
        if response_type in SAFE:
            answer, hits = SAFE[response_type], []
            # Do not claim that suppressed evidence was sent to the user.
            obligations = [{**o, "status": "suppressed", "evidence_ids": []} for o in obligations]
        trace.append(_trace("knowledge_finalizer", "passed", check_started, response_type=response_type,
                            release_id=snapshot["active"] if snapshot else None))
        return PipelineAnswer(
            answer=answer, hits=hits, elapsed=time.perf_counter() - started,
            mode="canonical_" + response_type, confidence=0.0,
            route=PipelineRoute("knowledge", "canonical_read", 0.0, response_type, "medium", "approved knowledge pilot"),
            entities=EntityBundle(), validation=ValidationResult(True), trace=trace,
            decision_artifact={"response_type": response_type, "release_id": snapshot["active"] if snapshot else None,
                               "obligations": obligations, "validation_policy": "approved_extracts_v1"})

    def answer(self, question: str, *, allow_llm: bool, now: datetime | None = None) -> PipelineAnswer | None:
        started = time.perf_counter()
        trace = []
        snapshot = self.store.snapshot()
        owned = {r["record_id"] for r in snapshot["ownership"] if alias_matches(question, r["alias"])}
        # A legacy catalog cannot claim completeness after new catalog entries are added.
        broad_catalog = bool(snapshot["ownership"]) and bool(re.search(r"เกมทั้งหมด|กี่เกม|รายชื่อเกม|มีเกมอะไร|all games|how many games", question, re.I))
        if not owned and not broad_catalog:
            return None
        trace.append(_trace("knowledge_snapshot", "owned", started, record_ids=sorted(owned), release_id=snapshot["active"]))
        release = snapshot["release"]
        if release is None or release["registry_version"] != REGISTRY_VERSION:
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="no_answer")
        records = {i["record"]["record_id"]: i["record"] for i in release["records"]}
        if broad_catalog or len(owned) != 1:
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="clarification")
        record_id = next(iter(owned))
        if record_id not in records or record_id in snapshot["withdrawn"]:
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="no_answer")
        record = records[record_id]
        current_time = now or datetime.now(timezone.utc)
        if current_time.tzinfo is None:
            raise ValueError("timezone required")
        if current_time < timestamp(record["effective_from"]) or (record["valid_until"] and current_time >= timestamp(record["valid_until"])):
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="no_answer")
        if record["scope"] != {"branch": "psu_phuket", "access": "public"}:
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="no_answer")

        contract_started = time.perf_counter()
        normalized = _normal(question)
        without_name = normalized
        for alias in sorted([record["title"], *record["aliases"]], key=len, reverse=True):
            without_name = without_name.replace(_normal(alias), " ")
        if UNSUPPORTED.search(without_name):
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="clarification")
        facets = {}
        for facet, signals in SIGNALS.items():
            for signal in signals:
                if signal in without_name:
                    facets[facet] = signal
                    break
        if record["type"] == "rule" and "overview" in facets:
            facets["policy"] = facets.pop("overview")
        if not facets or len(facets) > 3:
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="clarification")
        # Only one explicit subject is supported; independent compound subjects are deferred.
        if re.search(r"แล้วเกม|กับเกม|และเกม|and (?:the )?game", without_name):
            return self._finish(snapshot=snapshot, started=started, trace=trace, response_type="clarification")
        obligations = [{"obligation_id": f"o{i}", "entity_id": record["entity_id"], "facet": facet,
                        "question_span": span, "status": "not_found", "evidence_ids": []}
                       for i, (facet, span) in enumerate(facets.items(), 1)]
        trace.append(_trace("knowledge_contract", "explicit_signals", contract_started, obligations=obligations))
        sources = {s["source_id"]: s for s in record["sources"]}
        sections = {s["section_id"]: s for s in record["sections"]}
        units_by_id = {u["section_id"]: u for u in release["rag"] if u["record_id"] == record_id}
        blocks = []
        selected_units = []
        hits = []
        needs_document = any(o["facet"] not in FACTS for o in obligations)
        query_vector = None
        retrieval_error = False
        if needs_document:
            embedding_started = time.perf_counter()
            try:
                query_vector, info = self.embed(question, release["embedding"])
                trace.append(_trace("knowledge_embedding", "embedded", embedding_started, **info))
            except (OSError, ValueError, TimeoutError) as exc:
                retrieval_error = True
                trace.append(_trace("knowledge_embedding", "unavailable", embedding_started, error_type=type(exc).__name__))

        def add_hit(ref: dict, unit_id: str) -> str:
            source = sources[ref["source_id"]]
            for hit in hits:
                if hit["source_id"] == source["source_id"] and hit["snapshot_sha256"] == source["snapshot_sha256"]:
                    if ref["quote"] not in hit["text"]:
                        hit["text"] += "\n" + ref["quote"]
                    if unit_id not in hit["unit_ids"]:
                        hit["unit_ids"].append(unit_id)
                    return hit["citation_label"]
            label = "S" + str(len(hits) + 1)
            hits.append({"id": unit_id + ":" + label, "title": source["title"], "source_url": source["url"],
                         "text": ref["quote"], "source_id": source["source_id"],
                         "snapshot_sha256": source["snapshot_sha256"], "citation_label": label, "unit_ids": [unit_id]})
            return label

        for obligation in obligations:
            facet = obligation["facet"]
            if facet in FACTS:
                fact = next((f for f in release["structured"][record_id] if f["predicate"] == facet), None)
                if fact is None or fact["claim_status"] == "unknown":
                    continue
                value = fact["value"]
                if type(value) is bool:
                    value = "มีให้บริการตามข้อมูลที่อนุมัติ" if value else "ไม่มีให้บริการตามข้อมูลที่อนุมัติ"
                evidence_id = f"{record_id}:fact:{fact['fact_id']}"
                label = add_hit(fact["source_refs"][0], evidence_id)
                blocks.append({"unit_id": evidence_id, "text": f"{LABELS[facet]}: {value}", "label": label,
                               "obligation_id": obligation["obligation_id"]})
                obligation.update(status="supported", evidence_ids=[evidence_id])
                continue
            if query_vector is None:
                obligation["status"] = "unavailable"
                continue
            candidates = [u for u in units_by_id.values() if u["facet"] == facet]
            if not candidates:
                continue
            if len(candidates) > 4:
                obligation["status"] = "insufficient_budget"
                continue
            ranking_started = time.perf_counter()
            lexical_query = embed_text(question)
            dense = sorted(candidates, key=lambda u: sum(a * b for a, b in zip(query_vector, u["vector"])), reverse=True)
            lexical = sorted(candidates, key=lambda u: _cosine_sparse(lexical_query, embed_text(u["search_text"])), reverse=True)
            scores = {u["unit_id"]: 0.0 for u in candidates}
            for ranking in (dense, lexical):
                for rank, unit in enumerate(ranking, 1):
                    scores[unit["unit_id"]] += 1.0 / (60 + rank)
            ranked = sorted(candidates, key=lambda u: scores[u["unit_id"]], reverse=True)
            chosen = []
            seen = set()

            def include(section_id: str) -> None:
                if section_id in seen:
                    return
                if len(seen) >= 6 or section_id not in units_by_id:
                    raise ValueError("dependency budget or projection mismatch")
                seen.add(section_id)
                chosen.append(units_by_id[section_id])
                for dependency in sections[section_id]["depends_on"]:
                    include(dependency)

            try:
                for unit in ranked:
                    include(unit["section_id"])
                if sum(len(u["text"]) for u in chosen) > 4000:
                    raise ValueError("evidence text budget exceeded")
            except ValueError:
                obligation["status"] = "insufficient_budget"
                continue
            for unit in chosen:
                label = add_hit(sections[unit["section_id"]]["source_refs"][0], unit["unit_id"])
                blocks.append({**unit, "label": label, "obligation_id": obligation["obligation_id"]})
            selected_units.extend(chosen)
            obligation.update(status="supported", evidence_ids=[u["unit_id"] for u in chosen])
            trace.append(_trace("knowledge_retrieval", "facet_filtered_rrf", ranking_started,
                                facet=facet, candidates=len(candidates), selected=obligation["evidence_ids"],
                                lexical_backend="existing_char_ngram", score_semantics="rank_not_probability"))

        # The model can reorder extracts, never change their text or drop required units.
        if selected_units and allow_llm and len(blocks) <= 6:
            order_started = time.perf_counter()
            try:
                ids, info = self.order(question, blocks)
            except (OSError, ValueError, TimeoutError) as exc:
                ids, info = [], {"decision": "model_error", "error_type": type(exc).__name__}
            expected = [b["unit_id"] for b in blocks]
            accepted = len(ids) == len(expected) and len(set(expected)) == len(expected) and sorted(ids) == sorted(expected)
            rejection = "" if accepted else "not_exact_permutation"
            if accepted:
                mapping = {b["unit_id"]: b for b in blocks}
                proposed = [mapping[i] for i in ids]
                # Keep obligations grouped in original question order.
                accepted = [b["obligation_id"] for b in proposed] == [b["obligation_id"] for b in blocks]
                if not accepted:
                    rejection = "cross_obligation_order"
                if accepted:
                    blocks = proposed
            trace.append(_trace("knowledge_llm_order", "accepted" if accepted else "checked_draft_fallback", order_started,
                                model_info=info, rejection_reason=rejection, required_ids=expected))
        elif selected_units:
            trace.append(_trace("knowledge_llm_order", "skipped", time.perf_counter(), reason="disabled_or_evidence_budget"))

        supported = sum(o["status"] == "supported" for o in obligations)
        response_type = "answer" if supported == len(obligations) else "partial" if supported else "busy" if retrieval_error else "no_answer"
        answer_lines = [f"{b['text']} [{b['label']}]" for b in blocks]
        for obligation in obligations:
            if obligation["status"] != "supported" and supported:
                answer_lines.append(f"{LABELS[obligation['facet']]}: ยังไม่มีข้อมูลยืนยันในคำตอบนี้ครับ")
        answer = "\n\n".join(answer_lines)
        trace.append(_trace("knowledge_draft", "approved_extracts", time.perf_counter(),
                            answer_hash=digest(answer), evidence_hash=digest(blocks)))
        return self._finish(snapshot=snapshot, started=started, trace=trace, response_type=response_type,
                            answer=answer, hits=hits, obligations=obligations)


def try_canonical_answer(question: str, *, allow_llm: bool) -> PipelineAnswer | None:
    if os.getenv("PSU_CANONICAL_KNOWLEDGE", "0").lower() not in {"1", "true", "on"}:
        return None
    path = os.getenv("PSU_KNOWLEDGE_DB")
    started = time.perf_counter()
    answerer = KnowledgeAnswerer(KnowledgeStore(path or ROOT / "data" / "knowledge" / "approved.sqlite"))
    try:
        snapshot = answerer.store.snapshot()
        if snapshot["allow_demo"] and os.getenv("PSU_KNOWLEDGE_ALLOW_DEMO", "0") != "1":
            raise ValueError("demo database cannot serve public traffic")
        return answerer.answer(question, allow_llm=allow_llm)
    except (OSError, sqlite3.Error, ValueError, KeyError, TypeError) as exc:
        # An enabled but unavailable canonical store must not resurrect legacy facts.
        return answerer._finish(snapshot=None, started=started,
                                trace=[_trace("knowledge_store", "unavailable", started, error_type=type(exc).__name__)],
                                response_type="busy")
