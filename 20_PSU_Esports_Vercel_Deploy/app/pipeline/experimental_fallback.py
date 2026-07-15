from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from app.pipeline.retrieval import (
    hit_from_curated,
    retrieve_competition_fact_cards,
    retrieve_curated,
)
from app.pipeline.schemas import PipelineRoute, PipelineTrace
from app.core.normalization import normalize_text
from app.pipeline.vector_retrieval import retrieve_vector_guarded


DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "qwen2.5:3b")
DEFAULT_TIMEOUT_SEC = float(os.getenv("PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC", "1.5"))
DEFAULT_GENERAL_NUM_PREDICT = int(os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", "256"))
DEFAULT_RAG_NUM_PREDICT = int(os.getenv("PSU_RAG_LLM_NUM_PREDICT", "180"))


class OllamaEmptyResponseError(RuntimeError):
    """Raised when Ollama returns only thinking/internal text and no final answer."""


@dataclass(frozen=True)
class ExperimentalFallback:
    answer: str
    hits: list[dict[str, Any]]
    mode: str
    confidence: float
    trace: PipelineTrace


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def env_experimental_rag_fallback_default() -> bool:
    return _truthy(os.getenv("PSU_EXPERIMENTAL_RAG_FALLBACK"))


def env_experimental_llm_default() -> bool:
    return _truthy(os.getenv("PSU_EXPERIMENTAL_ALLOW_LLM"))


def _dedupe_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in rows:
        key = str(row.get("id", ""))
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def _retrieve_experimental_rows(query: str, route: PipelineRoute, limit: int) -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    details: list[str] = []

    if route.category == "competition_rules":
        fact_rows, fact_trace = retrieve_competition_fact_cards(query, limit=limit)
        details.append(f"fact_cards:{fact_trace.detail}")
        for row in fact_rows:
            rows.append({
                **row,
                "_experimental_kind": "competition_fact_card",
                "text": _fact_card_text(row),
                "category": "competition_rules",
                "title": row.get("id", "competition_fact_card"),
            })

    vector_rows, vector_trace = retrieve_vector_guarded(query, route, limit=limit)
    details.append(f"vector:{vector_trace.detail}")
    rows.extend({**row, "_experimental_kind": "curated"} for row in vector_rows)

    category = None if route.category in {"general", "no_answer", "unknown"} else route.category
    strict_vector_only = route.category == "games" and route.intent in {
        "game_detail_lookup",
        "game_availability_lookup",
        "games_lookup",
    }
    if category is not None and not strict_vector_only:
        scoped_rows, scoped_trace = retrieve_curated(query, category, limit=limit)
        details.append(f"scoped:{scoped_trace.detail}")
        if not rows:
            rows.extend({**row, "_experimental_kind": "curated"} for row in scoped_rows)
    elif strict_vector_only:
        details.append("scoped:skipped_after_vector_guard_for_game_entity_route")
    else:
        details.append("scoped:skipped_for_general_or_no_answer_route")
    rows = _dedupe_rows(rows)
    rows.sort(key=lambda row: float(row.get("_score", 0.0)), reverse=True)
    return rows[:limit], details


def _fact_card_text(row: dict[str, Any]) -> str:
    parts = [
        str(row.get("answer", "")).strip(),
        str(row.get("evidence", "")).strip(),
        str(row.get("game", "")).strip(),
        str(row.get("tournament", "")).strip(),
    ]
    return "\n".join(part for part in parts if part)


def _hit_from_row(row: dict[str, Any]) -> dict[str, Any]:
    if row.get("_experimental_kind") == "competition_fact_card":
        source_url = str(row.get("source_url", ""))
        row_id = str(row.get("id", "competition_fact_card"))
        return {
            "id": row_id,
            "metadata": {
                "source_url": source_url,
                "category": "competition_rules",
                "title": row_id,
                "source_ids": [row_id],
            },
        }
    return hit_from_curated(row)


def _manual_hit(source_id: str, category: str, source_url: str) -> dict[str, Any]:
    return {
        "id": source_id,
        "metadata": {
            "source_url": source_url,
            "category": category,
            "title": source_id,
            "source_ids": [source_id],
        },
    }


def _soft_related_fallback(question: str) -> ExperimentalFallback | None:
    q = normalize_text(question)
    home_url = "https://esports.phuket.psu.ac.th/home"
    reservation_url = "https://esports.computing.psu.ac.th/reservation"

    if any(term in q for term in ("เช่าจอ", "เช่า monitor", "เช่ามอนิเตอร์", "จอไปบ้าน", "ยืมจอ")):
        answer = (
            "โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้ตอนนี้คือศูนย์มี Gaming Monitor 10 Units สำหรับใช้งานใน PC Zone ภายในศูนย์\n"
            "ยังไม่มีข้อมูลยืนยันเรื่องบริการเช่าจอ/ยืมจอออกไปใช้นอกสถานที่ในฐานข้อมูลที่มีครับ\n"
            f"แหล่งข้อมูล: {home_url}"
        )
        return ExperimentalFallback(
            answer,
            [_manual_hit("home_equipment_pc_zone", "equipment", home_url)],
            "experimental_soft_related_fallback",
            0.66,
            PipelineTrace("experimental_rag_fallback", "soft_related_equipment_rental", 0.66, "monitor rental related answer"),
        )

    if any(term in q for term in ("ซ่อมคอม", "ซ่อม pc", "ซ่อมพีซี", "รับซ่อม", "คอมส่วนตัว")):
        answer = (
            "โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มี Gaming PC สำหรับให้ใช้งานใน PC Zone และมีอุปกรณ์ของศูนย์เอง\n"
            "ยังไม่มีข้อมูลยืนยันว่าศูนย์รับซ่อมคอมพิวเตอร์ส่วนตัวหรืออุปกรณ์ส่วนตัวของผู้ใช้ครับ\n"
            f"แหล่งข้อมูล: {home_url}"
        )
        return ExperimentalFallback(
            answer,
            [_manual_hit("home_equipment_pc_zone", "equipment", home_url)],
            "experimental_soft_related_fallback",
            0.66,
            PipelineTrace("experimental_rag_fallback", "soft_related_repair", 0.66, "personal repair related answer"),
        )

    if any(term in q for term in ("คอร์ส", "สอนเล่น", "สอน valorant", "สอนวาโล")):
        if any(term in q for term in ("valorant", "วาโล", "valo")):
            answer = (
                "โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือ VALORANT มีให้เล่นใน PC Zone และเป็นเกม Tactical FPS แบบทีม 5v5\n"
                "แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์มีคอร์สสอนเล่น VALORANT หรือคอร์สฝึกเฉพาะเกมในฐานข้อมูลที่มีครับ\n"
                f"แหล่งข้อมูล: {reservation_url}"
            )
            return ExperimentalFallback(
                answer,
                [_manual_hit("game_detail_valorant", "games", reservation_url)],
                "experimental_soft_related_fallback",
                0.66,
                PipelineTrace("experimental_rag_fallback", "soft_related_course", 0.66, "course question related to Valorant"),
            )

    if any(term in q for term in ("วันเกิด", "birthday", "จัดงาน", "ปาร์ตี้", "party")):
        answer = (
            "โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มีระบบจองเพื่อเข้าใช้บริการเป็นรอบเวลา\n"
            "แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์รับจัดงานวันเกิด/ปาร์ตี้/อีเวนต์ส่วนตัวในฐานข้อมูลที่มีครับ\n"
            f"แหล่งข้อมูล: {reservation_url}"
        )
        return ExperimentalFallback(
            answer,
            [_manual_hit("reservation", "reservation", reservation_url)],
            "experimental_soft_related_fallback",
            0.64,
            PipelineTrace("experimental_rag_fallback", "soft_related_private_event", 0.64, "private event related answer"),
        )

    return None


def _source_line(rows: list[dict[str, Any]], limit: int = 2) -> str:
    labels: list[str] = []
    for row in rows[:limit]:
        source = str(row.get("source_url", "")).strip()
        row_id = str(row.get("id", "")).strip()
        if source and source.startswith("http"):
            label = source
        elif source:
            label = source
        else:
            label = row_id
        if label and label not in labels:
            labels.append(label)
    return ", ".join(labels)


def _context_block(rows: list[dict[str, Any]], max_chars: int = 2600) -> str:
    blocks: list[str] = []
    used = 0
    for index, row in enumerate(rows[:4], 1):
        text = " ".join(str(row.get("text", "")).split())
        if not text:
            continue
        block = (
            f"[{index}] {row.get('title') or row.get('id')}\n"
            f"category={row.get('category', '')}\n"
            f"source={row.get('source_url', '')}\n"
            f"{text}"
        )
        if used + len(block) > max_chars:
            remaining = max_chars - used
            if remaining <= 250:
                break
            block = block[:remaining] + "\n...(context truncated)"
        blocks.append(block)
        used += len(block)
    return "\n\n---\n\n".join(blocks)


def _build_prompt(question: str, rows: list[dict[str, Any]]) -> str:
    return f"""ตอบเป็นภาษาไทยแบบสั้น ตรงคำถาม และสุภาพ
ใช้เฉพาะ CONTEXT ของ PSU Esports Studio - Phuket เท่านั้น
ห้ามแต่งราคา เวลา กติกา เกม หรือบริการที่ไม่มีใน CONTEXT
ถ้า CONTEXT ไม่ตรงคำถาม ให้ตอบว่าโยงได้แค่ข้อมูลใกล้เคียงอะไร และอย่าฟันธง
เริ่มด้วยคำตอบหลักก่อน แล้วค่อยรายละเอียด

QUESTION:
{question}

CONTEXT:
{_context_block(rows)}

ANSWER:"""


def _call_ollama(
    prompt: str,
    *,
    timeout_sec: float = DEFAULT_TIMEOUT_SEC,
    num_predict: int = DEFAULT_RAG_NUM_PREDICT,
) -> str:
    payload = {
        "model": DEFAULT_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.15,
            "top_p": 0.8,
            "num_predict": num_predict,
            "num_ctx": 3072,
        },
    }
    request = urllib.request.Request(
        f"{DEFAULT_OLLAMA_URL.rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        data = json.loads(response.read().decode("utf-8"))
    answer = str(data.get("response", "")).strip()
    if answer:
        return answer
    thinking = str(data.get("thinking", "")).strip()
    if thinking:
        raise OllamaEmptyResponseError(
            "Ollama returned thinking but no final response "
            f"(thinking_len={len(thinking)}, done_reason={data.get('done_reason') or 'unknown'}, "
            f"num_predict={num_predict}, model={DEFAULT_MODEL})."
        )
    return ""


def _build_general_prompt(question: str) -> str:
    return f"""ตอบเป็นภาษาไทยแบบสั้น กระชับ และเป็นประโยชน์
คำถามนี้อยู่นอกฐานข้อมูล PSU Esports Studio - Phuket จึงให้ตอบจากความรู้ทั่วไปของโมเดล
ห้ามอ้างว่าเป็นข้อมูลของ PSU Esports Studio - Phuket
ห้ามแต่งราคา เวลา ขั้นตอนบริการ หรือกฎของศูนย์
ถ้าคำถามต้องใช้ข้อมูลล่าสุด/ข้อมูลเฉพาะสถานที่ ให้บอกว่าควรตรวจสอบแหล่งข้อมูลจริงเพิ่มเติม

QUESTION:
{question}

ANSWER:"""


def _general_llm_answer(question: str) -> str:
    answer = _call_ollama(
        _build_general_prompt(question),
        timeout_sec=float(os.getenv("PSU_GENERAL_LLM_TIMEOUT_SEC", "12")),
        num_predict=int(os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", str(DEFAULT_GENERAL_NUM_PREDICT))),
    )
    if not answer:
        return ""
    note = "หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket"
    if "หมายเหตุ" not in answer:
        answer = answer.rstrip() + f"\n{note}"
    return answer


def _direct_rag_answer(question: str, rows: list[dict[str, Any]]) -> str:
    best = rows[0]
    best_text = " ".join(str(best.get("text", "")).split())
    if len(best_text) > 650:
        best_text = best_text[:650].rstrip() + "..."
    title = str(best.get("title") or best.get("id") or "ข้อมูลใกล้เคียง").strip()
    return (
        f"โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ {title}\n"
        f"{best_text}\n\n"
        "หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน"
    )


def _no_context_answer(route: PipelineRoute) -> str:
    category = route.category if route.category != "general" else "ภาพรวม/ข้อมูลทั่วไป"
    return (
        f"โหมดทดลอง RAG: ยังไม่มี context ที่โยงกับคำถามนี้ได้ชัดในฐานข้อมูลหมวด {category}\n"
        "ถ้าต้องการให้ตอบได้ ควรเพิ่ม fact/card หรือข้อมูลจริงของเรื่องนั้นเข้า knowledge base ก่อน"
    )


def _general_unavailable_answer(llm_error: str = "") -> str:
    timeout_sec = os.getenv("PSU_GENERAL_LLM_TIMEOUT_SEC", str(DEFAULT_TIMEOUT_SEC))
    num_predict = os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", str(DEFAULT_GENERAL_NUM_PREDICT))
    hint = (
        f"\nรายละเอียด: {llm_error}"
        if llm_error and ("thinking but no final response" in llm_error or "OllamaEmptyResponseError" in llm_error)
        else ""
    )
    return (
        "คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ\n"
        f"แต่ Local LLM รุ่น `{DEFAULT_MODEL}` ยังไม่ส่งคำตอบสุดท้ายกลับมา จึงยังตอบจากความรู้ทั่วไปไม่ได้\n"
        f"ค่าปัจจุบัน: timeout={timeout_sec}s, num_predict={num_predict}\n"
        "ถ้าใช้ `qwen3:4b` แล้วเจออาการนี้ แนะนำให้ลอง `qwen2.5:3b` ก่อน เพราะ Qwen3 เป็น thinking model และอาจใช้ token ไปกับการคิดจน response ว่าง"
        f"{hint}"
    )


def _general_disabled_answer() -> str:
    return (
        "คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ\n"
        "ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว"
    )


def build_experimental_fallback(
    question: str,
    route: PipelineRoute,
    *,
    started: float,
    allow_llm: bool,
    limit: int = 5,
) -> ExperimentalFallback:
    if route.category == "general" and not allow_llm:
        trace = PipelineTrace(
            "experimental_rag_fallback",
            "general_llm_disabled",
            0.42,
            "general route skips document retrieval when general LLM is disabled",
            {"allow_llm": False, "model": DEFAULT_MODEL},
        )
        return ExperimentalFallback(
            _general_disabled_answer(),
            [],
            "general_llm_disabled",
            0.42,
            trace,
        )

    soft = _soft_related_fallback(question)
    if soft is not None:
        return soft

    if allow_llm and route.category == "general":
        llm_error = ""
        try:
            answer = _general_llm_answer(question)
            if answer:
                trace = PipelineTrace(
                    "experimental_rag_fallback",
                    "general_llm",
                    0.58,
                    "general route uses local LLM without document retrieval",
                    {"allow_llm": True, "model": DEFAULT_MODEL},
                )
                return ExperimentalFallback(
                    answer,
                    [],
                    "general_llm_fallback",
                    0.58,
                    trace,
                )
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, OllamaEmptyResponseError) as exc:
            llm_error = f"{type(exc).__name__}: {exc}"
        trace = PipelineTrace(
            "experimental_rag_fallback",
            "general_llm_unavailable",
            0.42,
            "general route skips document retrieval to avoid PSU context noise",
            {"allow_llm": True, "model": DEFAULT_MODEL, "llm_error": llm_error},
        )
        return ExperimentalFallback(
            _general_unavailable_answer(llm_error),
            [],
            "general_llm_unavailable",
            0.42,
            trace,
        )

    rows, details = _retrieve_experimental_rows(question, route, limit)
    if not rows:
        trace = PipelineTrace("experimental_rag_fallback", "no_context", 0.42, "; ".join(details), {"allow_llm": allow_llm})
        if allow_llm and route.category == "general" and llm_error:
            trace.metadata["llm_error"] = llm_error
        return ExperimentalFallback(
            _no_context_answer(route),
            [],
            "experimental_rag_no_context",
            0.42,
            trace,
        )

    llm_error = ""
    if allow_llm:
        try:
            answer = _call_ollama(
                _build_prompt(question, rows),
                num_predict=int(os.getenv("PSU_RAG_LLM_NUM_PREDICT", str(DEFAULT_RAG_NUM_PREDICT))),
            )
            if answer:
                source_line = _source_line(rows)
                if source_line and "แหล่งข้อมูล" not in answer:
                    answer = answer.rstrip() + f"\nแหล่งข้อมูล: {source_line}"
                trace = PipelineTrace(
                    "experimental_rag_fallback",
                    "rag_llm",
                    0.70,
                    "; ".join(details),
                    {"allow_llm": True, "model": DEFAULT_MODEL},
                )
                return ExperimentalFallback(
                    answer,
                    [_hit_from_row(row) for row in rows[:3]],
                    "experimental_rag_llm_fallback",
                    0.70,
                    trace,
                )
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, OllamaEmptyResponseError) as exc:
            llm_error = f"{type(exc).__name__}: {exc}"

    answer = _direct_rag_answer(question, rows)
    source_line = _source_line(rows)
    if source_line:
        answer += f"\nแหล่งข้อมูล: {source_line}"
    trace = PipelineTrace(
        "experimental_rag_fallback",
        "rag_direct",
        0.62,
        "; ".join(details),
        {"allow_llm": allow_llm, "llm_error": llm_error, "elapsed": round(time.perf_counter() - started, 4)},
    )
    return ExperimentalFallback(
        answer,
        [_hit_from_row(row) for row in rows[:3]],
        "experimental_rag_direct_fallback",
        0.62,
        trace,
    )
