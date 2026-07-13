from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import asdict
from typing import Any, Iterable

from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.formatter import format_no_answer
from app.pipeline.preprocess import extract_entities, preprocess_input
from app.pipeline.retrieval import (
    answer_from_competition_fact_hits,
    answer_from_curated_hits,
    retrieve_competition_fact_cards,
    retrieve_curated,
)
from app.pipeline.router import route_intent


DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "qwen2.5:3b")
DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
DEFAULT_LLM_TIMEOUT_SEC = float(os.getenv("PSU_CHATBOT_LLM_TIMEOUT_SEC", "8.0"))

EXACT_FAST_CATEGORIES = {"service_fee", "schedule", "penalty", "contact"}
SYNTHESIS_TERMS = (
    "สรุป",
    "สอน",
    "ขั้นตอน",
    "ทำยังไง",
    "ยังไง",
    "อธิบาย",
    "รายละเอียด",
    "ทั้งหมด",
    "ครบ",
    "เปรียบเทียบ",
    "ต่างกัน",
    "แนะนำ",
    "ต้องทำอะไร",
    "how",
    "explain",
    "summary",
    "compare",
)


def _source_from_hit(hit: dict[str, Any]) -> dict[str, str]:
    metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
    return {
        "id": str(hit.get("id", metadata.get("title", ""))),
        "title": str(metadata.get("title", hit.get("id", ""))),
        "category": str(metadata.get("category", "")),
        "source_url": str(metadata.get("source_url", "")),
    }


def _sources_from_hits(hits: Iterable[dict[str, Any]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    sources: list[dict[str, str]] = []
    for hit in hits:
        source = _source_from_hit(hit)
        key = (source["id"], source["source_url"])
        if key in seen:
            continue
        seen.add(key)
        sources.append(source)
    return sources


def _source_from_row(row: dict[str, Any]) -> dict[str, str]:
    return {
        "id": str(row.get("id", "")),
        "title": str(row.get("title", row.get("id", ""))),
        "category": str(row.get("category", "competition_rules" if row.get("game") else "")),
        "source_url": str(row.get("source_url", "")),
    }


def _compact_trace(trace: Iterable[Any], limit: int = 12) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    for item in list(trace)[-limit:]:
        compact.append(
            {
                "stage": getattr(item, "stage", ""),
                "decision": getattr(item, "decision", ""),
                "confidence": getattr(item, "confidence", 0.0),
                "detail": getattr(item, "detail", ""),
                "metadata": getattr(item, "metadata", {}),
            }
        )
    return compact


def _is_no_answer(text: str) -> bool:
    lowered = (text or "").lower()
    return "ยังไม่พบข้อมูล" in lowered or "ไม่พบข้อมูล" in lowered or "no verified" in lowered


def _should_use_llm(question: str, route_category: str, pipeline_mode: str, pipeline_confidence: float) -> bool:
    q = (question or "").lower()
    if route_category in EXACT_FAST_CATEGORIES:
        return False
    if pipeline_confidence < 0.72 or "no_answer" in pipeline_mode:
        return True
    return any(term in q for term in SYNTHESIS_TERMS)


def _normalize_mode(mode: str) -> str:
    value = (mode or "auto").strip().lower()
    aliases = {
        "rule": "rulebase",
        "rules": "rulebase",
        "fast": "rulebase",
        "pipeline": "rulebase",
        "deterministic": "rulebase",
        "retrieval": "rag",
        "rag_direct": "rag",
        "llm": "rag_llm",
        "rag+llm": "rag_llm",
        "rag_llm": "rag_llm",
        "hybrid": "auto",
        "mixed": "auto",
    }
    return aliases.get(value, value)


def route_preview(question: str) -> dict[str, Any]:
    pre = preprocess_input(question)
    entities = extract_entities(pre)
    route, route_trace = route_intent(pre, entities)
    return {
        "question": question,
        "normalized_query": pre.normalized_query,
        "language_hint": pre.language_hint,
        "entities": asdict(entities),
        "route": asdict(route),
        "route_trace": asdict(route_trace),
    }


def retrieve_context(question: str, *, limit: int = 5) -> dict[str, Any]:
    pre = preprocess_input(question)
    entities = extract_entities(pre)
    route, route_trace = route_intent(pre, entities)

    rows: list[dict[str, Any]] = []
    traces: list[dict[str, Any]] = [asdict(route_trace)]

    if route.category == "competition_rules":
        fact_hits, fact_trace = retrieve_competition_fact_cards(pre.clean_query, limit=limit)
        traces.append(asdict(fact_trace))
        for row in fact_hits:
            rows.append(
                {
                    "kind": "competition_fact_card",
                    "id": row.get("id", ""),
                    "score": row.get("_score", 0),
                    "title": row.get("id", ""),
                    "category": "competition_rules",
                    "source_url": row.get("source_url", ""),
                    "text": _fact_card_text(row),
                    "raw": row,
                }
            )

    category = None if route.category in {"general", "unknown"} else route.category
    curated_hits, curated_trace = retrieve_curated(pre.clean_query, category, limit=limit)
    traces.append(asdict(curated_trace))
    for row in curated_hits:
        rows.append(
            {
                "kind": "curated",
                "id": row.get("id", ""),
                "score": row.get("_score", 0),
                "title": row.get("title", row.get("id", "")),
                "category": row.get("category", ""),
                "source_url": row.get("source_url", ""),
                "text": str(row.get("text", "")).strip(),
                "raw": row,
            }
        )

    rows.sort(key=lambda item: float(item.get("score", 0)), reverse=True)
    return {
        "question": question,
        "route": asdict(route),
        "entities": asdict(entities),
        "context_rows": rows[:limit],
        "traces": traces,
    }


def _fact_card_text(row: dict[str, Any]) -> str:
    parts = [
        f"คำตอบ: {str(row.get('answer', '')).strip()}",
        f"หลักฐาน: {str(row.get('evidence', '')).strip()}",
        f"เกม/รายการ: {str(row.get('game', '')).strip()} / {str(row.get('tournament', '')).strip()}",
    ]
    return "\n".join(part for part in parts if part and not part.endswith(": "))


def _context_to_prompt_block(context_rows: list[dict[str, Any]], *, max_chars: int = 2500) -> str:
    blocks: list[str] = []
    used = 0
    for index, row in enumerate(context_rows, start=1):
        text = str(row.get("text", "")).strip()
        if not text:
            continue
        block = (
            f"[{index}] id={row.get('id', '')}\n"
            f"category={row.get('category', '')}\n"
            f"source={row.get('source_url', '')}\n"
            f"{text}"
        )
        if used + len(block) > max_chars:
            remaining = max_chars - used
            if remaining <= 300:
                break
            block = block[:remaining] + "\n...(context truncated)"
        blocks.append(block)
        used += len(block)
    return "\n\n---\n\n".join(blocks)


def _call_ollama(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    num_predict: int = 96,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.85,
            "repeat_penalty": 1.08,
            "num_predict": num_predict,
            "num_ctx": 3072,
            "stop": ["\n\nQUESTION:", "\n\nCONTEXT:", "\n\nคำถาม:"],
        },
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{ollama_url.rstrip('/')}/api/generate",
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


def _build_grounded_prompt(question: str, context_rows: list[dict[str, Any]]) -> str:
    context_block = _context_to_prompt_block(context_rows[:3])
    return f"""ตอบเป็นภาษาไทยสั้นและตรงคำถามของ PSU Esports Studio - Phuket
ใช้เฉพาะ CONTEXT เท่านั้น ห้ามเดา ถ้าไม่มีข้อมูลให้บอกว่า "ยังไม่พบข้อมูลที่ยืนยันได้จากข้อมูลที่มี"
บรรทัดแรกต้องตอบใจความหลักก่อน ถ้ามีตัวเลข/ราคา/เวลาให้ขึ้นต้นด้วยตัวเลขนั้น
ตอบไม่เกิน 5 บรรทัด ไม่ต้องคัดลอก context ยาว

QUESTION: {question}

CONTEXT:
{context_block}

ANSWER:"""


def ask_rulebase(question: str) -> dict[str, Any]:
    started = time.perf_counter()
    result = answer_question_pipeline_debug(question)
    return {
        "requested_mode": "rulebase",
        "selected_mode": "rulebase",
        "method": "pipeline_fast_verified",
        "question": question,
        "answer": result.answer,
        "elapsed_sec": round(time.perf_counter() - started, 4),
        "pipeline_elapsed_sec": result.elapsed,
        "pipeline_mode": result.mode,
        "model": None,
        "confidence": result.confidence,
        "route": asdict(result.route),
        "entities": asdict(result.entities),
        "sources": _sources_from_hits(result.hits),
        "trace": _compact_trace(result.trace),
        "ok": True,
        "error": "",
    }


def ask_rag(question: str, *, limit: int = 5) -> dict[str, Any]:
    started = time.perf_counter()
    ctx = retrieve_context(question, limit=limit)
    route_category = ctx["route"]["category"]
    rows = ctx["context_rows"]

    answer = ""
    confidence = 0.0
    raw_hits: list[dict[str, Any]] = []

    if route_category == "competition_rules":
        fact_rows = [row["raw"] for row in rows if row.get("kind") == "competition_fact_card"]
        answer, raw_hits, confidence = answer_from_competition_fact_hits(fact_rows, question)

    if not answer:
        curated_rows = [row["raw"] for row in rows if row.get("kind") == "curated"]
        answer, raw_hits, confidence = answer_from_curated_hits(curated_rows, question)

    if not answer:
        if rows:
            preview_lines = []
            for index, row in enumerate(rows[:3], start=1):
                snippet = " ".join(str(row.get("text", "")).split())[:240]
                preview_lines.append(f"{index}. {row.get('id', '')}: {snippet}")
            answer = (
                "พบข้อมูลใกล้เคียงจาก RAG แต่ยังสรุปเป็นคำตอบฟันธงโดยไม่ใช้ LLM ไม่ได้ครับ\n\n"
                "Context ที่เจอ:\n" + "\n".join(preview_lines)
            )
            confidence = 0.58
        else:
            answer = format_no_answer(route_category)
            confidence = 0.40

    sources = _sources_from_hits(raw_hits) if raw_hits else [_source_from_row(row) for row in rows[:3]]
    return {
        "requested_mode": "rag",
        "selected_mode": "rag",
        "method": "retrieval_direct_no_llm",
        "question": question,
        "answer": answer,
        "elapsed_sec": round(time.perf_counter() - started, 4),
        "pipeline_elapsed_sec": None,
        "pipeline_mode": None,
        "model": None,
        "confidence": confidence,
        "route": ctx["route"],
        "entities": ctx["entities"],
        "sources": sources,
        "trace": ctx["traces"],
        "context_rows": _public_context_rows(rows),
        "ok": True,
        "error": "",
    }


def ask_rag_llm(
    question: str,
    *,
    model: str = DEFAULT_MODEL,
    limit: int = 5,
    llm_timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    num_predict: int = 96,
) -> dict[str, Any]:
    started = time.perf_counter()
    ctx = retrieve_context(question, limit=limit)
    rows = ctx["context_rows"]

    if not rows:
        return {
            "requested_mode": "rag_llm",
            "selected_mode": "rag_llm",
            "method": "rag_llm_no_context",
            "question": question,
            "answer": format_no_answer(ctx["route"]["category"]),
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "pipeline_elapsed_sec": None,
            "pipeline_mode": None,
            "model": model,
            "confidence": 0.35,
            "route": ctx["route"],
            "entities": ctx["entities"],
            "sources": [],
            "trace": ctx["traces"],
            "context_rows": [],
            "ok": False,
            "error": "no_retrieved_context",
        }

    prompt = _build_grounded_prompt(question, rows)
    try:
        response = _call_ollama(
            prompt,
            model=model,
            timeout_sec=llm_timeout_sec,
            ollama_url=ollama_url,
            num_predict=num_predict,
        )
        answer = str(response.get("response", "")).strip()
        if not answer:
            answer = "ยังไม่พบข้อมูลที่ยืนยันได้จากข้อมูลที่มีครับ"
        answer = _append_sources_if_missing(answer, rows)
        ok = not _is_no_answer(answer)
        error = ""
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        answer = (
            f"เรียก LLM ไม่สำเร็จภายใน {llm_timeout_sec:.1f} วินาทีครับ "
            "ลองใช้ mode='rag' หรือเพิ่ม llm_timeout_sec หากต้องการให้ LLM เรียบเรียงจาก context"
        )
        response = {}
        ok = False
        error = f"{type(exc).__name__}: {exc}"

    return {
        "requested_mode": "rag_llm",
        "selected_mode": "rag_llm",
        "method": "retrieval_plus_grounded_ollama",
        "question": question,
        "answer": answer,
        "elapsed_sec": round(time.perf_counter() - started, 4),
        "pipeline_elapsed_sec": None,
        "pipeline_mode": None,
        "model": model,
        "confidence": 0.78 if ok else 0.45,
        "route": ctx["route"],
        "entities": ctx["entities"],
        "sources": [_source_from_row(row) for row in rows[:3]],
        "trace": ctx["traces"] + [{"stage": "llm", "decision": "ollama_generate", "confidence": 0.78 if ok else 0.45, "detail": error}],
        "context_rows": _public_context_rows(rows),
        "llm_raw": {
            "model": response.get("model", model),
            "eval_count": response.get("eval_count"),
            "eval_duration": response.get("eval_duration"),
            "prompt_eval_count": response.get("prompt_eval_count"),
        },
        "ok": ok,
        "error": error,
    }


def ask_auto(
    question: str,
    *,
    model: str = DEFAULT_MODEL,
    limit: int = 5,
    llm_timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
    allow_llm: bool = True,
) -> dict[str, Any]:
    started = time.perf_counter()
    fast = ask_rulebase(question)
    route_category = fast["route"]["category"]
    pipeline_mode = str(fast.get("pipeline_mode", ""))

    # Keep exact, validated facts on the deterministic path. It is faster and safer.
    if not _should_use_llm(question, route_category, pipeline_mode, float(fast["confidence"])):
        fast["requested_mode"] = "auto"
        fast["selected_mode"] = "auto_fast_verified"
        fast["method"] = "auto chose rulebase/deterministic because this is an exact fact or calculation"
        fast["elapsed_sec"] = round(time.perf_counter() - started, 4)
        return fast

    if allow_llm:
        llm = ask_rag_llm(question, model=model, limit=limit, llm_timeout_sec=llm_timeout_sec)
        llm["requested_mode"] = "auto"
        llm["selected_mode"] = "auto_rag_llm" if llm["ok"] else "auto_rag_llm_failed"
        llm["method"] = "auto chose RAG+LLM because the question needs synthesis or the fast answer was weak"
        llm["elapsed_sec"] = round(time.perf_counter() - started, 4)
        if llm["ok"]:
            return llm

    rag = ask_rag(question, limit=limit)
    rag["requested_mode"] = "auto"
    rag["selected_mode"] = "auto_rag_fallback"
    rag["method"] = "auto used direct RAG fallback because LLM was disabled/failed"
    rag["elapsed_sec"] = round(time.perf_counter() - started, 4)

    if rag["confidence"] >= fast["confidence"] or _is_no_answer(fast["answer"]):
        return rag

    fast["requested_mode"] = "auto"
    fast["selected_mode"] = "auto_fast_fallback"
    fast["method"] = "auto kept the original fast answer because fallback was not stronger"
    fast["elapsed_sec"] = round(time.perf_counter() - started, 4)
    return fast


def _append_sources_if_missing(answer: str, context_rows: list[dict[str, Any]]) -> str:
    if "แหล่งข้อมูล" in answer:
        return answer
    source_bits: list[str] = []
    for row in context_rows[:2]:
        source = str(row.get("source_url", "")).strip()
        row_id = str(row.get("id", "")).strip()
        label = row_id
        if source:
            label = f"{row_id} ({source})" if row_id else source
        if label and label not in source_bits:
            source_bits.append(label)
    if not source_bits:
        return answer
    return answer.rstrip() + "\nแหล่งข้อมูล: " + "; ".join(source_bits)


def ask_mode(
    question: str,
    *,
    mode: str = "auto",
    model: str = DEFAULT_MODEL,
    limit: int = 5,
    llm_timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
    allow_llm: bool = True,
) -> dict[str, Any]:
    selected = _normalize_mode(mode)
    if selected == "auto":
        return ask_auto(question, model=model, limit=limit, llm_timeout_sec=llm_timeout_sec, allow_llm=allow_llm)
    if selected == "rulebase":
        return ask_rulebase(question)
    if selected == "rag":
        return ask_rag(question, limit=limit)
    if selected == "rag_llm":
        return ask_rag_llm(question, model=model, limit=limit, llm_timeout_sec=llm_timeout_sec)
    raise ValueError("mode must be one of: auto, rulebase, rag, rag_llm")


def compare_modes(
    question: str,
    *,
    modes: tuple[str, ...] = ("rulebase", "rag", "rag_llm", "auto"),
    model: str = DEFAULT_MODEL,
    limit: int = 5,
    llm_timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for mode in modes:
        results.append(ask_mode(question, mode=mode, model=model, limit=limit, llm_timeout_sec=llm_timeout_sec))
    return results


def _public_context_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    public_rows: list[dict[str, Any]] = []
    for row in rows:
        public_rows.append(
            {
                "kind": row.get("kind", ""),
                "id": row.get("id", ""),
                "score": row.get("score", 0),
                "title": row.get("title", ""),
                "category": row.get("category", ""),
                "source_url": row.get("source_url", ""),
                "text_preview": " ".join(str(row.get("text", "")).split())[:320],
            }
        )
    return public_rows


def print_mode_result(result: dict[str, Any], *, show_context: bool = False, show_trace: bool = True) -> None:
    route = result.get("route", {})
    print("=" * 92)
    print(f"คำถาม: {result.get('question', '')}")
    print("-" * 92)
    print(f"selected_mode: {result.get('selected_mode')} | method: {result.get('method')}")
    if result.get("pipeline_mode"):
        print(f"pipeline_mode: {result.get('pipeline_mode')}")
    print(f"route: {route.get('category')} / {route.get('intent')} | confidence: {result.get('confidence')}")
    print(f"model: {result.get('model') or '-'} | elapsed: {result.get('elapsed_sec')} sec")
    if result.get("error"):
        print(f"error: {result.get('error')}")
    print("-" * 92)
    print("คำตอบจาก AI:")
    print(result.get("answer", ""))

    sources = result.get("sources") or []
    if sources:
        print("-" * 92)
        print("แหล่งข้อมูล:")
        for source in sources:
            print(f"- {source.get('id')} | {source.get('source_url')}")

    if show_context and result.get("context_rows"):
        print("-" * 92)
        print("Retrieved Context:")
        for row in result.get("context_rows", []):
            print(f"- [{row.get('kind')}] {row.get('id')} score={row.get('score')}")
            print(f"  {row.get('text_preview')}")

    if show_trace and result.get("trace"):
        print("-" * 92)
        print("Trace:")
        for item in result.get("trace", [])[-8:]:
            print(f"- {item.get('stage')} -> {item.get('decision')} ({item.get('confidence')}) {item.get('detail', '')}")


def interactive_ask(
    *,
    default_mode: str = "auto",
    model: str = DEFAULT_MODEL,
    limit: int = 5,
    llm_timeout_sec: float = DEFAULT_LLM_TIMEOUT_SEC,
) -> None:
    print("พิมพ์คำถามได้เลย | เปลี่ยนโหมดด้วย /mode auto, /mode rulebase, /mode rag, /mode rag_llm | ออกด้วย exit")
    mode = default_mode
    while True:
        question = input(f"[{mode}] > ").strip()
        if not question:
            continue
        if question.lower() in {"exit", "quit", "q"}:
            break
        if question.startswith("/mode"):
            parts = question.split(maxsplit=1)
            if len(parts) == 2:
                mode = _normalize_mode(parts[1])
                print(f"เปลี่ยนโหมดเป็น {mode}")
            else:
                print(f"โหมดปัจจุบัน: {mode}")
            continue
        result = ask_mode(question, mode=mode, model=model, limit=limit, llm_timeout_sec=llm_timeout_sec)
        print_mode_result(result, show_context=False, show_trace=True)
