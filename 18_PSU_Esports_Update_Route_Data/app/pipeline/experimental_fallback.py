from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from app.pipeline.chatbot_role import CHATBOT_ROLE_TH
from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success, release_llm_slot
from app.pipeline.request_deadline import deadline_metadata, timeout_for_call
from app.pipeline.query_signals import has_any_signal
from app.pipeline.retrieval import (
    answer_from_competition_fact_hits,
    answer_from_curated_hits,
    hit_from_curated,
    retrieve_competition_fact_cards,
    retrieve_curated,
)
from app.pipeline.schemas import PipelineRoute, PipelineTrace
from app.core.normalization import normalize_text
from app.pipeline.vector_retrieval import retrieve_vector_guarded


DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
DEFAULT_TIMEOUT_SEC = float(os.getenv("PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC", "1.5"))
DEFAULT_GENERAL_NUM_PREDICT = int(os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", "128"))
DEFAULT_RAG_NUM_PREDICT = int(os.getenv("PSU_RAG_LLM_NUM_PREDICT", "96"))


class OllamaEmptyResponseError(RuntimeError):
    """Raised when Ollama returns only thinking/internal text and no final answer."""


@dataclass(frozen=True)
class ExperimentalFallback:
    answer: str
    hits: list[dict[str, Any]]
    mode: str
    confidence: float
    trace: PipelineTrace


@dataclass(frozen=True)
class GeneralGenerationProfile:
    name: str
    num_predict: int
    instruction: str
    configured_num_predict: int
    expected_items: int = 0


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def select_general_generation_profile(question: str) -> GeneralGenerationProfile:
    configured = max(16, int(os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", str(DEFAULT_GENERAL_NUM_PREDICT))))
    if not _truthy(os.getenv("PSU_GENERAL_LLM_ADAPTIVE_NUM_PREDICT", "1")):
        return GeneralGenerationProfile(
            "configured",
            configured,
            "ตอบตามรูปแบบและความยาวที่ผู้ใช้ขอ",
            configured,
        )

    q = normalize_text(question)
    expected_items = 0
    if has_any_signal(q, "ช่วยเขียน", "เขียนประโยค", "ช่วยแต่ง", "ช่วยร่าง", "แคปชั่น", "caption", "คำโปรย"):
        cap = 96
        name = "short_creation"
        instruction = (
            "สร้างข้อความทั่วไปตามที่ขอหนึ่งประโยค ไม่เกิน 25 คำ โดยไม่ต้องถามรายละเอียดเพิ่ม "
            "ห้ามแต่งวัน เวลา สถานที่ หรือข้อเท็จจริงเฉพาะที่ผู้ใช้ไม่ได้ให้มา "
            "หากคำสั่งอธิบายเพิ่มเติมขัดกับรูปแบบหนึ่งประโยค ให้ยึดข้อความที่ขอสร้างเป็นหลัก "
            "และต้องคงคำนามหลักจากคำสั่งตามตัวสะกดเดิม เช่น หากถามถึงกิจกรรมต้องมีคำว่า 'กิจกรรม'"
        )
        expected_items = 1
    elif has_any_signal(q, "ข้อดีข้อเสีย", "ข้อดีและข้อเสีย", "เปรียบเทียบ", "ต่างกันยังไง", "ต่างกันอย่างไร"):
        cap = 112
        name = "definition_with_tradeoffs"
        instruction = (
            "ตอบให้ครบ 3 บรรทัดเท่านั้น: บรรทัดแรกขึ้นต้น 'คำตอบ:' ไม่เกิน 20 คำ, "
            "บรรทัดสองขึ้นต้น 'ข้อดี:' ไม่เกิน 15 คำ, บรรทัดสามขึ้นต้น 'ข้อเสีย:' ไม่เกิน 15 คำ"
        )
        expected_items = 3
    elif has_any_signal(q, "แปลคำว่า", "ช่วยแปล", "แปลเป็นภาษา", "translate"):
        cap = 48
        name = "translation"
        instruction = "ตอบเฉพาะคำแปลภาษาไทยหนึ่งวลี ไม่เกิน 8 คำ ห้ามอธิบายเพิ่ม"
        expected_items = 1
    elif has_any_signal(q, "ประโยคเดียว", "หนึ่งประโยค", "1 ประโยค"):
        cap = 64
        name = "single_sentence"
        instruction = "ตอบเพียงหนึ่งประโยค ไม่เกิน 25 คำ ห้ามเติมย่อหน้าหรือคำอธิบายต่อท้าย"
        expected_items = 1
    elif has_any_signal(q, "2 ข้อ", "สองข้อ", "bullet", "หัวข้อ"):
        cap = 96
        name = "short_bullets"
        instruction = "ตอบ 2 bullet เท่านั้น แต่ละข้อไม่เกิน 18 คำ ไม่เพิ่มหัวข้อหรือคำถามต่อท้าย"
        expected_items = 2
    elif has_any_signal(q, "2 ประโยค", "สองประโยค"):
        cap = 96
        name = "two_sentences"
        instruction = (
            "ตอบให้ครบสองประโยคเท่านั้น แต่ละประโยคไม่เกิน 25 คำ "
            "หากคำถามเกี่ยวกับการขอบคุณ ต้องมีคำว่า 'ขอบคุณ' ตามตัวสะกดนี้อย่างน้อยหนึ่งครั้ง"
        )
        expected_items = 2
    elif has_any_signal(q, "ไม่เกิน 3 บรรทัด", "ตอบสั้น", "แบบสั้น", "สั้น ๆ", "สั้นๆ", "คำจำกัดความ"):
        cap = 96
        name = "concise_definition"
        instruction = "ตอบไม่เกิน 2 ประโยค รวมไม่เกิน 45 คำ ใช้คำง่ายและตอบเฉพาะสาระที่ถาม"
    else:
        cap = 128
        name = "general_concise"
        instruction = (
            "ตอบคำตอบหลักก่อนเพียง 1-2 ประโยค รวมไม่เกิน 35 คำ ใช้คำง่าย "
            "และไม่เพิ่มรายละเอียดที่ผู้ใช้ไม่ได้ถาม"
        )

    return GeneralGenerationProfile(name, min(configured, cap), instruction, configured, expected_items)


def _ollama_think_value() -> bool | str:
    raw = os.getenv("PSU_OLLAMA_THINK", "false").strip().lower()
    if raw in {"1", "true", "yes", "y", "on"}:
        return True
    if raw in {"low", "medium", "high", "max"}:
        return raw
    return False


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
        fact_answer, _, _ = answer_from_competition_fact_hits(fact_rows, query)
        if fact_answer:
            for row in fact_rows[:1]:
                rows.append({
                    **row,
                    "_experimental_kind": "competition_fact_card",
                    "text": _fact_card_text(row),
                    "category": "competition_rules",
                    "title": row.get("id", "competition_fact_card"),
                })
        elif fact_rows:
            details.append("fact_card_answer_guard:rejected_intent_or_detail_mismatch")

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
            scoped_answer, _, _ = answer_from_curated_hits(scoped_rows, query)
            if route.category != "competition_rules" or scoped_answer:
                rows.extend({**row, "_experimental_kind": "curated"} for row in scoped_rows)
            elif scoped_rows:
                details.append("scoped_answer_guard:rejected_intent_or_score_mismatch")
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
    return f"""{CHATBOT_ROLE_TH}

ตอบเป็นภาษาไทยแบบสั้น ตรงคำถาม และสุภาพ
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
    response_metadata: dict[str, Any] | None = None,
) -> str:
    timeout_sec = timeout_for_call(timeout_sec)
    if timeout_sec <= 0:
        raise TimeoutError("global request deadline exhausted before experimental fallback LLM call")
    payload = {
        "model": DEFAULT_MODEL,
        "prompt": prompt,
        "stream": True,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "think": _ollama_think_value(),
        "options": {
            "temperature": 0.15,
            "top_p": 0.8,
            "num_predict": num_predict,
            "num_ctx": int(os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072")),
        },
    }
    request = urllib.request.Request(
        f"{DEFAULT_OLLAMA_URL.rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    response = None
    chunks: list[str] = []
    last_data: dict[str, Any] = {}
    try:
        response = urllib.request.urlopen(request, timeout=timeout_sec)
        for raw_line in response:
            line = raw_line.decode("utf-8", errors="replace").strip()
            if not line:
                continue
            last_data = json.loads(line)
            chunks.append(str(last_data.get("response") or ""))
            if last_data.get("done"):
                break
    finally:
        if response is not None:
            response.close()
    if response_metadata is not None:
        for key in (
            "done",
            "done_reason",
            "total_duration",
            "load_duration",
            "prompt_eval_count",
            "prompt_eval_duration",
            "eval_count",
            "eval_duration",
        ):
            if key in last_data:
                response_metadata[f"ollama_{key}"] = last_data.get(key)
    answer = "".join(chunks).strip()
    if answer:
        return answer
    thinking = str(last_data.get("thinking", "")).strip()
    if thinking:
        raise OllamaEmptyResponseError(
            "Ollama returned thinking but no final response "
            f"(thinking_len={len(thinking)}, done_reason={last_data.get('done_reason') or 'unknown'}, "
            f"num_predict={num_predict}, model={DEFAULT_MODEL})."
        )
    return ""


def _ollama_call_metadata(
    *,
    kind: str,
    prompt: str,
    timeout_sec: float,
    num_predict: int,
    elapsed_ms: float,
    answer: str = "",
    error: BaseException | None = None,
) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "llm_kind": kind,
        "llm_model": DEFAULT_MODEL,
        "llm_timeout_sec": timeout_sec,
        "llm_num_predict": num_predict,
        "llm_num_ctx": int(os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072")),
        "llm_keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "llm_prompt_chars": len(prompt),
        "llm_elapsed_ms": round(elapsed_ms, 2),
        "llm_response_chars": len(answer),
        **deadline_metadata(),
    }
    if error is not None:
        metadata["llm_error_type"] = type(error).__name__
        metadata["llm_error"] = str(error)
    return metadata


def _build_general_prompt(question: str, profile: GeneralGenerationProfile | None = None) -> str:
    profile = profile or select_general_generation_profile(question)
    return f"""ตอบภาษาไทยให้สั้น ตรงคำถาม และสุภาพ
ตอบคำตอบสุดท้ายทันที ไม่ต้องแสดงขั้นตอนคิด
{profile.instruction}
ใช้คำลงท้ายแบบสุภาพเป็น "ครับ" เมื่อจำเป็น และห้ามใช้ emoji
ต้องคงคำสำคัญหลักจากคำถามตามตัวสะกดเดิมอย่างน้อยหนึ่งคำในคำตอบ เว้นแต่เป็นงานแปลที่ให้ตอบเฉพาะคำแปล
ห้ามโยงคำถามทั่วไปเข้ากับ PSU Esports Studio - Phuket หากผู้ใช้ไม่ได้ถามถึงศูนย์
ถ้าเป็นคำถามข้อเท็จจริงที่ยังขาดข้อมูลจำเป็น ให้ถามกลับหนึ่งคำถามและห้ามเดา แต่งานสร้างข้อความทั่วไปให้ทำตามรูปแบบด้านบนโดยไม่ต้องขอวัน เวลา หรือสถานที่

QUESTION: {question}
ANSWER:"""


def _line_looks_complete(line: str) -> bool:
    clean = line.strip().rstrip("*_` ")
    if len(clean) < 8:
        return False
    dangling = (" และ", " หรือ", " ที่", " การ", " กับ", " ของ", " เพื่อ", " โดย", " ใน", " เป็น", " คือ", ":")
    terminal = ("ครับ", "ค่ะ", "คะ", "ครับ.", "ค่ะ.", ".", "!", "?", "。", "！", "？")
    return not clean.endswith(dangling) and clean.endswith(terminal)


def _shape_general_output(
    answer: str,
    profile: GeneralGenerationProfile,
    provider: dict[str, Any],
) -> str:
    lines = [line.strip() for line in answer.splitlines() if line.strip()]
    if profile.name not in {"single_sentence", "short_creation", "two_sentences", "short_bullets"} or not profile.expected_items:
        return answer.strip()
    selected = lines[: profile.expected_items]
    if len(lines) > len(selected):
        provider["llm_output_extra_items_removed"] = len(lines) - len(selected)
    if (
        str(provider.get("ollama_done_reason") or "").lower() == "length"
        and len(selected) == profile.expected_items
        and all(_line_looks_complete(line) for line in selected)
    ):
        provider["llm_output_bounded_prefix_complete"] = True
    return "\n".join(selected).strip()


def _general_output_contract(answer: str, profile: GeneralGenerationProfile, provider: dict[str, Any]) -> tuple[bool, str]:
    if not answer.strip():
        return False, "empty_output"
    if (
        str(provider.get("ollama_done_reason") or "").lower() == "length"
        and not provider.get("llm_output_bounded_prefix_complete")
    ):
        return False, "token_limit_truncation"
    clean = answer.strip()
    if profile.name == "translation" and (len(clean) > 100 or len(clean.splitlines()) > 2):
        return False, "translation_shape_mismatch"
    if profile.name in {"single_sentence", "short_creation"} and len([line for line in clean.splitlines() if line.strip()]) > 1:
        return False, "single_sentence_shape_mismatch"
    if profile.name == "two_sentences" and len([line for line in clean.splitlines() if line.strip()]) > 2:
        return False, "two_sentence_shape_mismatch"
    if profile.name == "definition_with_tradeoffs":
        normalized = normalize_text(clean)
        if "ข้อดี" not in normalized or "ข้อเสีย" not in normalized:
            return False, "tradeoff_coverage_missing"
    return True, "ok"


def _general_llm_answer(question: str) -> str:
    answer, _metadata = _general_llm_answer_with_metadata(question)
    return answer


def _general_llm_answer_with_metadata(question: str) -> tuple[str, dict[str, Any]]:
    configured_timeout_sec = float(os.getenv("PSU_GENERAL_LLM_TIMEOUT_SEC", "12"))
    timeout_sec = timeout_for_call(configured_timeout_sec)
    profile = select_general_generation_profile(question)
    num_predict = profile.num_predict
    prompt = _build_general_prompt(question, profile)
    allowed, budget_health = llm_call_allowed("general_llm", DEFAULT_MODEL)
    if not allowed:
        return "", {
            **_ollama_call_metadata(
                kind="general_llm",
                prompt=prompt,
                timeout_sec=timeout_sec,
                num_predict=num_predict,
                elapsed_ms=0.0,
                error=RuntimeError("LLM circuit breaker cooldown active"),
            ),
            **budget_health,
            "llm_generation_profile": profile.name,
            "llm_configured_num_predict": profile.configured_num_predict,
            "llm_skipped_by_health": True,
        }
    if timeout_sec <= 0:
        release_llm_slot()
        return "", {
            **_ollama_call_metadata(
                kind="general_llm",
                prompt=prompt,
                timeout_sec=timeout_sec,
                num_predict=num_predict,
                elapsed_ms=0.0,
                error=TimeoutError("global request deadline exhausted before general LLM"),
            ),
            "llm_configured_timeout_sec": configured_timeout_sec,
            **budget_health,
            "llm_generation_profile": profile.name,
            "llm_configured_num_predict": profile.configured_num_predict,
            "llm_skipped_by_deadline": True,
        }
    call_started = time.perf_counter()
    provider_metadata: dict[str, Any] = {}
    try:
        answer = _call_ollama(
            prompt,
            timeout_sec=timeout_sec,
            num_predict=num_predict,
            response_metadata=provider_metadata,
        )
        provider_metadata["llm_raw_response_chars"] = len(answer)
        answer = _shape_general_output(answer, profile, provider_metadata)
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, OllamaEmptyResponseError) as exc:
        elapsed_ms = (time.perf_counter() - call_started) * 1000
        health = record_llm_failure(
            "general_llm",
            DEFAULT_MODEL,
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_ms=elapsed_ms,
        )
        metadata = _ollama_call_metadata(
            kind="general_llm",
            prompt=prompt,
            timeout_sec=timeout_sec,
            num_predict=num_predict,
            elapsed_ms=elapsed_ms,
            error=exc,
        )
        metadata.update(budget_health)
        metadata.update({
            "llm_generation_profile": profile.name,
            "llm_configured_num_predict": profile.configured_num_predict,
        })
        metadata.update(provider_metadata)
        metadata.update(health)
        raise
    elapsed_ms = (time.perf_counter() - call_started) * 1000
    output_ok, output_reason = _general_output_contract(answer, profile, provider_metadata)
    if answer and not output_ok:
        health = record_llm_success("general_llm", DEFAULT_MODEL, elapsed_ms=elapsed_ms)
        metadata = _ollama_call_metadata(
            kind="general_llm",
            prompt=prompt,
            timeout_sec=timeout_sec,
            num_predict=num_predict,
            elapsed_ms=elapsed_ms,
            answer=answer,
        )
        metadata.update(budget_health)
        metadata.update(provider_metadata)
        metadata.update(health)
        metadata.update({
            "llm_generation_profile": profile.name,
            "llm_configured_num_predict": profile.configured_num_predict,
            "llm_output_contract_ok": False,
            "llm_output_rejected_reason": output_reason,
        })
        return "", metadata
    if answer:
        health = record_llm_success("general_llm", DEFAULT_MODEL, elapsed_ms=elapsed_ms)
    else:
        health = record_llm_failure(
            "general_llm",
            DEFAULT_MODEL,
            error_type="EmptyResponse",
            error="empty response",
            elapsed_ms=elapsed_ms,
        )
    if not answer:
        metadata = _ollama_call_metadata(
            kind="general_llm",
            prompt=prompt,
            timeout_sec=timeout_sec,
            num_predict=num_predict,
            elapsed_ms=elapsed_ms,
            answer=answer,
        )
        metadata.update(budget_health)
        metadata.update({
            "llm_generation_profile": profile.name,
            "llm_configured_num_predict": profile.configured_num_predict,
        })
        metadata.update(provider_metadata)
        metadata.update(health)
        return "", metadata
    note = "หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket"
    if "หมายเหตุ" not in answer:
        answer = answer.rstrip() + f"\n{note}"
    metadata = _ollama_call_metadata(
        kind="general_llm",
        prompt=prompt,
        timeout_sec=timeout_sec,
        num_predict=num_predict,
        elapsed_ms=elapsed_ms,
        answer=answer,
    )
    metadata["llm_configured_timeout_sec"] = configured_timeout_sec
    metadata["llm_generation_profile"] = profile.name
    metadata["llm_configured_num_predict"] = profile.configured_num_predict
    metadata["llm_output_contract_ok"] = True
    metadata.update(provider_metadata)
    metadata.update(budget_health)
    metadata.update(health)
    return answer, metadata


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
    return (
        "ตอนนี้ยังตอบคำถามความรู้ทั่วไปไม่ได้ชั่วคราวครับ กรุณาลองใหม่อีกครั้ง\n"
        "สำหรับข้อมูลของ PSU Esports Studio - Phuket ยังถามเรื่องเกม ปุ่ม อุปกรณ์ ราคา การจอง เวลาเปิด และกติกาได้ตามปกติครับ"
    )


def _general_disabled_answer() -> str:
    return (
        "คำถามนี้ไม่ได้อยู่ในข้อมูลของ PSU Esports Studio - Phuket จึงยังตอบจากข้อมูลที่ยืนยันได้ไม่ได้ครับ\n"
        "ลองถามเรื่องเกม ปุ่ม อุปกรณ์ ราคา การจอง เวลาเปิด หรือกติกาของศูนย์ได้ครับ"
    )


def _looks_like_psu_specific_question(question: str) -> bool:
    q = normalize_text(question)
    strong_signals = (
        "psu", "สงขลานครินทร์", "psu phuket", "esports", "อีสปอร์ต", "studio",
        "ภูเก็ต", "ps5", "playstation", "เพลย์", "nintendo", "switch", "vr",
        "วีอาร์", "pc zone", "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย",
        "คอนโทรลเลอร์", "สมาชิกทีม", "สตาฟ",
    )
    service_or_studio_signals = (
        "ศูนย์", "จอง", "เช็คอิน", "เชคอิน", "ค่าบริการ", "บริการ", "เวลาเปิด",
        "เปิดกี่โมง", "ปิดกี่โมง", "เปิดไหม", "อุปกรณ์", "โซน", "ปุ่ม",
        "กติกา", "การแข่งขัน", "แข่ง", "ทัวร์",
    )
    return any(signal in q for signal in strong_signals) or (
        any(signal in q for signal in service_or_studio_signals)
        and any(signal in q for signal in ("psu", "esports", "studio", "ศูนย์", "ps5", "playstation", "nintendo", "switch", "vr", "pc zone", "cockpit", "โซน"))
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
        if _looks_like_psu_specific_question(question):
            trace = PipelineTrace(
                "experimental_rag_fallback",
                "blocked_general_llm_for_psu_signal",
                0.52,
                "general route contains PSU/service signal; skip model-only answer",
                {
                    "allow_llm": allow_llm,
                    "model": DEFAULT_MODEL,
                    "llm_attempted": False,
                    "guard": "psu_specific_general_llm_block",
                },
            )
            return ExperimentalFallback(
                _no_context_answer(PipelineRoute("no_answer", "psu_specific_general_block", 0.52, "no_answer", "medium", "PSU signal blocked general LLM")),
                [],
                "general_psu_scope_no_answer",
                0.52,
                trace,
            )
        llm_error = ""
        llm_call: dict[str, Any] = {}
        try:
            answer, llm_call = _general_llm_answer_with_metadata(question)
            if answer:
                trace = PipelineTrace(
                    "experimental_rag_fallback",
                    "general_llm",
                    0.58,
                    "general route uses local LLM without document retrieval",
                    {"allow_llm": True, "model": DEFAULT_MODEL, "llm_attempted": True, "llm_call": llm_call},
                )
                return ExperimentalFallback(
                    answer,
                    [],
                    "general_llm_fallback",
                    0.58,
                    trace,
                )
            if llm_call.get("llm_skipped_by_health"):
                llm_error = "LLM circuit breaker cooldown active"
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, OllamaEmptyResponseError) as exc:
            llm_error = f"{type(exc).__name__}: {exc}"
            timeout_sec = timeout_for_call(float(os.getenv("PSU_GENERAL_LLM_TIMEOUT_SEC", "12")))
            profile = select_general_generation_profile(question)
            num_predict = profile.num_predict
            llm_call = _ollama_call_metadata(
                kind="general_llm",
                prompt=_build_general_prompt(question, profile),
                timeout_sec=timeout_sec,
                num_predict=num_predict,
                elapsed_ms=timeout_sec * 1000 if isinstance(exc, TimeoutError) else 0.0,
                error=exc,
            )
            llm_call["llm_generation_profile"] = profile.name
            llm_call["llm_configured_num_predict"] = profile.configured_num_predict
        trace = PipelineTrace(
            "experimental_rag_fallback",
            "general_llm_unavailable",
            0.42,
            "general route skips document retrieval to avoid PSU context noise",
            {"allow_llm": True, "model": DEFAULT_MODEL, "llm_attempted": True, "llm_error": llm_error, "llm_call": llm_call},
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
        timeout_sec = timeout_for_call(DEFAULT_TIMEOUT_SEC)
        num_predict = int(os.getenv("PSU_RAG_LLM_NUM_PREDICT", str(DEFAULT_RAG_NUM_PREDICT)))
        prompt = _build_prompt(question, rows)
        allowed, health = llm_call_allowed("rag_llm", DEFAULT_MODEL)
        if not allowed:
            llm_error = "LLM circuit breaker cooldown active"
            llm_call = {
                **_ollama_call_metadata(
                    kind="rag_llm",
                    prompt=prompt,
                    timeout_sec=timeout_sec,
                    num_predict=num_predict,
                    elapsed_ms=0.0,
                    error=RuntimeError(llm_error),
                ),
                **health,
                "llm_skipped_by_health": True,
            }
        elif timeout_sec <= 0:
            release_llm_slot()
            allowed = False
            llm_error = "global request deadline exhausted before RAG LLM"
            llm_call = {
                **_ollama_call_metadata(
                    kind="rag_llm",
                    prompt=prompt,
                    timeout_sec=timeout_sec,
                    num_predict=num_predict,
                    elapsed_ms=0.0,
                    error=TimeoutError(llm_error),
                ),
                "llm_skipped_by_deadline": True,
            }
        else:
            llm_call = {}
        call_started = time.perf_counter()
        if allowed:
            try:
                answer = _call_ollama(
                    prompt,
                    num_predict=num_predict,
                )
                elapsed_ms = (time.perf_counter() - call_started) * 1000
                if answer:
                    health = record_llm_success("rag_llm", DEFAULT_MODEL, elapsed_ms=elapsed_ms)
                else:
                    health = record_llm_failure("rag_llm", DEFAULT_MODEL, error_type="EmptyResponse", error="empty response", elapsed_ms=elapsed_ms)
                llm_call = _ollama_call_metadata(
                    kind="rag_llm",
                    prompt=prompt,
                    timeout_sec=timeout_sec,
                    num_predict=num_predict,
                    elapsed_ms=elapsed_ms,
                    answer=answer,
                )
                llm_call.update(health)
                if answer:
                    source_line = _source_line(rows)
                    if source_line and "แหล่งข้อมูล" not in answer:
                        answer = answer.rstrip() + f"\nแหล่งข้อมูล: {source_line}"
                    trace = PipelineTrace(
                        "experimental_rag_fallback",
                        "rag_llm",
                        0.70,
                        "; ".join(details),
                        {"allow_llm": True, "model": DEFAULT_MODEL, "llm_attempted": True, "llm_call": llm_call},
                    )
                    return ExperimentalFallback(
                        answer,
                        [_hit_from_row(row) for row in rows[:3]],
                        "experimental_rag_llm_fallback",
                        0.70,
                        trace,
                    )
            except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, OllamaEmptyResponseError) as exc:
                elapsed_ms = (time.perf_counter() - call_started) * 1000
                llm_error = f"{type(exc).__name__}: {exc}"
                health = record_llm_failure(
                    "rag_llm",
                    DEFAULT_MODEL,
                    error_type=type(exc).__name__,
                    error=str(exc),
                    elapsed_ms=elapsed_ms,
                )
                llm_call = _ollama_call_metadata(
                    kind="rag_llm",
                    prompt=prompt,
                    timeout_sec=timeout_sec,
                    num_predict=num_predict,
                    elapsed_ms=elapsed_ms,
                    error=exc,
                )
                llm_call.update(health)
    else:
        llm_call = {}

    answer = _direct_rag_answer(question, rows)
    source_line = _source_line(rows)
    if source_line:
        answer += f"\nแหล่งข้อมูล: {source_line}"
    trace = PipelineTrace(
        "experimental_rag_fallback",
        "rag_direct",
        0.62,
        "; ".join(details),
        {
            "allow_llm": allow_llm,
            "llm_attempted": bool(allow_llm),
            "llm_error": llm_error,
            "llm_call": llm_call,
            "elapsed": round(time.perf_counter() - started, 4),
        },
    )
    return ExperimentalFallback(
        answer,
        [_hit_from_row(row) for row in rows[:3]],
        "experimental_rag_direct_fallback",
        0.62,
        trace,
    )
