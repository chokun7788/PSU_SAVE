from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.chatbot_role import CHATBOT_ROLE_TH
from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success
from app.pipeline.request_deadline import deadline_metadata, timeout_for_call
from app.pipeline.schemas import PipelineTrace, UniversalIntent


PLANNER_DOMAINS = {
    "members",
    "games",
    "game_controls",
    "equipment",
    "reservation",
    "service_fee",
    "schedule",
    "rules",
    "penalty",
    "competition_rules",
    "contact",
    "knowledge",
    "general",
}

PLANNER_OPERATIONS = {
    "count",
    "list",
    "group_count",
    "group_list",
    "role_lookup",
    "detail",
    "how_to",
    "control",
    "price_calculate",
    "schedule_lookup",
    "rule_lookup",
    "compare",
    "source_lookup",
    "availability",
    "recommendation",
    "general_answer",
    "unknown",
}


@dataclass(frozen=True)
class QueryPlanTask:
    task_id: str
    question: str
    domain: str
    operation: str
    target: str = ""
    target_type: str = ""
    filters: dict[str, Any] = field(default_factory=dict)
    needs_clarification: bool = False
    confidence: float = 0.0
    reason: str = ""

    def to_universal_intent(self) -> UniversalIntent:
        return UniversalIntent(
            domain=self.domain,
            operation=self.operation,
            target=self.target,
            filters=dict(self.filters),
            confidence=self.confidence,
            method="query_planner",
            reason=self.reason or "validated task from constrained query planner",
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "question": self.question,
            "domain": self.domain,
            "operation": self.operation,
            "target": self.target,
            "target_type": self.target_type,
            "filters": dict(self.filters),
            "needs_clarification": self.needs_clarification,
            "confidence": self.confidence,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class QueryPlan:
    tasks: tuple[QueryPlanTask, ...]
    is_compound: bool
    confidence: float
    reason: str = ""
    clarification: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "tasks": [task.as_dict() for task in self.tasks],
            "is_compound": self.is_compound,
            "confidence": self.confidence,
            "reason": self.reason,
            "clarification": self.clarification,
        }


def _truthy(value: str | None, *, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def query_planner_enabled() -> bool:
    return _truthy(os.getenv("PSU_QUERY_PLANNER"), default=True)


def _extract_json_object(text: str) -> dict[str, Any] | None:
    """Extract planner JSON from common local-model wrappers.

    Small local models sometimes return a fenced object, a think block, or a
    top-level task array even when the prompt requests a JSON object. These
    transformations only normalize transport formatting; schema validation
    remains in ``parse_query_plan``.
    """
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"```(?:json)?", "", text, flags=re.IGNORECASE).replace("```", "").strip()
    if not text:
        return None
    try:
        value = json.loads(text)
        if isinstance(value, dict):
            return value
        if isinstance(value, list):
            return {"tasks": value, "is_compound": len(value) > 1}
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        try:
            value = json.loads(text[start : end + 1])
            return value if isinstance(value, dict) else None
        except json.JSONDecodeError:
            pass
    array_start = text.find("[")
    array_end = text.rfind("]")
    if array_start >= 0 and array_end > array_start:
        try:
            value = json.loads(text[array_start : array_end + 1])
            return {"tasks": value, "is_compound": isinstance(value, list) and len(value) > 1} if isinstance(value, list) else None
        except json.JSONDecodeError:
            return None
    return None


def _clamp_confidence(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = default
    return round(max(0.0, min(0.98, number)), 3)


def _planner_confidence(value: Any, default: float = 0.58) -> float:
    """Treat the prompt's copied 0.0 placeholder as unspecified, not as trust."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if number <= 0:
        return default
    return _clamp_confidence(number, default)


def _bounded_text(value: Any, limit: int) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()[:limit]


def _coerce_task(raw: Any, index: int) -> QueryPlanTask | None:
    if not isinstance(raw, dict):
        return None
    question = _bounded_text(raw.get("question") or raw.get("query") or raw.get("subquery") or raw.get("text"), 260)
    domain = _bounded_text(raw.get("domain") or raw.get("category"), 40).lower()
    operation = _bounded_text(raw.get("operation") or raw.get("intent") or raw.get("action"), 50).lower()
    if len(question) < 2 or domain not in PLANNER_DOMAINS or operation not in PLANNER_OPERATIONS:
        return None
    filters = raw.get("filters") if isinstance(raw.get("filters"), dict) else {}
    safe_filters = {str(key)[:60]: value for key, value in list(filters.items())[:8]}
    return QueryPlanTask(
        task_id=_bounded_text(raw.get("task_id") or raw.get("id") or f"task_{index}", 40),
        question=question,
        domain=domain,
        operation=operation,
        target=_bounded_text(raw.get("target"), 120),
        target_type=_bounded_text(raw.get("target_type"), 40),
        filters=safe_filters,
        needs_clarification=str(raw.get("needs_clarification", False)).strip().lower() in {"1", "true", "yes", "y"},
        confidence=_planner_confidence(raw.get("confidence")),
        reason=_bounded_text(raw.get("reason"), 180),
    )


def parse_query_plan(response_text: str, original_query: str = "") -> QueryPlan | None:
    data = _extract_json_object(response_text)
    if data is None:
        return None
    raw_tasks = data.get("tasks")
    if not isinstance(raw_tasks, list):
        raw_tasks = data.get("subqueries")
    if not isinstance(raw_tasks, list):
        raw_tasks = data.get("sub_questions") or data.get("queries")
    if isinstance(raw_tasks, dict):
        raw_tasks = [raw_tasks]
    if not isinstance(raw_tasks, list):
        raw_tasks = [data] if data.get("question") or data.get("query") else []
    if not raw_tasks or len(raw_tasks) > 4:
        return None
    tasks: list[QueryPlanTask] = []
    seen_questions: set[str] = set()
    for index, raw_task in enumerate(raw_tasks, 1):
        task = _coerce_task(raw_task, index)
        if task is None:
            return None
        key = normalize_text(task.question)
        if key in seen_questions:
            return None
        seen_questions.add(key)
        tasks.append(task)
    is_compound = bool(data.get("is_compound", len(tasks) > 1))
    if is_compound and len(tasks) < 2:
        return None
    if len(tasks) > 1 and not is_compound:
        return None
    confidence = _planner_confidence(data.get("confidence"), min(task.confidence for task in tasks))
    if confidence < 0.45:
        return None
    clarification = _bounded_text(data.get("clarification"), 240)
    return QueryPlan(
        tasks=tuple(tasks),
        is_compound=is_compound,
        confidence=confidence,
        reason=_bounded_text(data.get("reason"), 220),
        clarification=clarification,
    )


def should_use_query_planner(
    question: str,
    parts: list[str] | None = None,
    *,
    route_category: str = "",
    route_confidence: float = 0.0,
    force_complex: bool = False,
) -> tuple[bool, str]:
    if not query_planner_enabled():
        return False, "PSU_QUERY_PLANNER is disabled"
    if len(parts or []) > 1:
        if force_complex:
            return True, "compound complexity gate requires constrained planner"
        if _truthy(os.getenv("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"), default=False):
            return True, "planner explicitly enabled for deterministic split"
        return False, "deterministic splitter produced standalone parts; planner skipped"

    query = normalize_text(question or "")
    if not query:
        return False, "empty query"
    operation_groups = (
        ("price", "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร"),
        ("controls", "ปุ่ม", "คอนโทรล", "จอย", "กดอะไร"),
        ("games", "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม"),
        ("equipment", "อุปกรณ์", "เครื่องอะไร", "มีอะไรบ้าง"),
        ("booking", "จอง", "เช็คอิน", "booking"),
        ("schedule", "เปิด", "ปิด", "กี่โมง", "เวลา"),
        ("members", "สมาชิก", "ทีมงาน", "ใครเป็น", "ตำแหน่ง"),
    )
    matched_groups = sum(1 for _name, *terms in operation_groups if any(term in query for term in terms))
    bridge = any(term in query for term in ("และ", "แล้ว", "พร้อม", "รวมถึง", "อีกเรื่อง", "ทั้ง", "กับ"))
    if matched_groups >= 2 and bridge:
        return True, f"multiple operation groups detected ({matched_groups})"
    if route_category in {"general", "unknown", "no_answer"} and route_confidence < 0.62 and len(query) >= 14:
        return True, "weak route needs constrained query planning"
    return False, "single clear operation does not need planner"


def _build_prompt(query: str, parts: list[str]) -> str:
    domains = ", ".join(sorted(PLANNER_DOMAINS))
    operations = ", ".join(sorted(PLANNER_OPERATIONS))
    parts_json = json.dumps(parts[:4], ensure_ascii=False)
    return f"""{CHATBOT_ROLE_TH}

คุณทำหน้าที่เป็น Constrained Query Planner เท่านั้น ไม่ใช่ผู้ตอบคำถาม
หน้าที่คือแตกคำถามเป็น task ย่อยที่เป็นคำถามเดี่ยวแบบ standalone เพื่อส่งต่อให้ pipeline ของระบบ
ห้ามตอบข้อเท็จจริง ห้ามแต่งราคา เกม ปุ่ม เวลา รายชื่อ หรือข้อมูล PSU

ข้อบังคับ:
- คืน JSON เท่านั้น ห้ามมี markdown หรือข้อความนอก JSON
- แต่ละ task ต้องเป็นคำถามภาษาไทยที่ครบความหมายและมี target เดิมของผู้ใช้
- ใช้ได้ไม่เกิน 4 tasks และห้ามสร้าง task ที่ไม่มีอยู่ในคำถาม
- domain ต้องเลือกจาก: {domains}
- operation ต้องเลือกจาก: {operations}
- ถ้าเป็นคำถามเดียวให้คืน 1 task และ is_compound=false
- ถ้าเป็นหลายคำถามให้แยกทุกเจตนาออกจากกัน และ is_compound=true
- ถ้า target ไม่ชัด ให้ใส่ needs_clarification=true แทนการเดาเกม/อุปกรณ์

คำถามเดิม: {query}
ส่วนที่ splitter เดิมมองเห็น: {parts_json}

รูปแบบ JSON:
{{
  "is_compound": true,
  "confidence": 0.0,
  "reason": "สั้น ๆ",
  "tasks": [
    {{
      "task_id": "task_1",
      "question": "คำถามเดี่ยวแบบ standalone",
      "domain": "games",
      "operation": "list",
      "target": "",
      "target_type": "",
      "filters": {{}},
      "needs_clarification": false,
      "confidence": 0.0,
      "reason": "สั้น ๆ"
    }}
  ]
}}"""


def planner_skip_trace(reason: str, *, allow_llm: bool) -> PipelineTrace:
    detail = reason if allow_llm else f"experimental_allow_llm is false; {reason}"
    return PipelineTrace(
        "query_planner",
        "skipped",
        0.0,
        detail,
        {"method": "gated", "llm_attempted": False, "allow_llm": allow_llm},
    )


def plan_query(
    query: str,
    parts: list[str],
    *,
    allow_llm: bool,
    gate_reason: str,
    timeout_cap_sec: float | None = None,
) -> tuple[QueryPlan | None, PipelineTrace]:
    model = os.getenv("PSU_QUERY_PLANNER_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
    configured_timeout = max(0.05, float(os.getenv("PSU_QUERY_PLANNER_TIMEOUT_SEC", "8")))
    if timeout_cap_sec is not None:
        configured_timeout = min(configured_timeout, max(0.05, float(timeout_cap_sec)))
    timeout = timeout_for_call(configured_timeout)
    num_predict = max(64, int(os.getenv("PSU_QUERY_PLANNER_NUM_PREDICT", "128")))
    call_metadata: dict[str, Any] = {
        "llm_kind": "query_planner",
        "llm_model": model,
        "llm_configured_timeout_sec": configured_timeout,
        "llm_timeout_sec": timeout,
        "llm_num_predict": num_predict,
        "gate_reason": gate_reason,
        **deadline_metadata(),
    }
    if not allow_llm:
        return None, planner_skip_trace("experimental_allow_llm is false", allow_llm=False)
    if not query_planner_enabled():
        return None, planner_skip_trace("PSU_QUERY_PLANNER is disabled", allow_llm=True)
    if timeout <= 0:
        return None, PipelineTrace("query_planner", "skipped_deadline", 0.0, "global request deadline exhausted before planner", {"llm_attempted": False, "llm_call": {**call_metadata, "llm_skipped_by_deadline": True}})
    allowed, health = llm_call_allowed("query_planner", model)
    call_metadata.update(health)
    if not allowed:
        return None, PipelineTrace("query_planner", "skipped_health", 0.0, "LLM circuit breaker cooldown active", {"llm_attempted": False, "llm_call": {**call_metadata, "llm_skipped_by_health": True, **health}})

    prompt = _build_prompt(query, parts)
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0, "num_predict": num_predict, "num_ctx": 4096},
    }
    request = urllib.request.Request(
        f"{os.getenv('OLLAMA_URL', 'http://127.0.0.1:11434').rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        response_text = str(data.get("response") or "")
        plan = parse_query_plan(response_text, query)
    except (OSError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        elapsed_ms = (time.perf_counter() - started) * 1000
        health = record_llm_failure("query_planner", model, error_type=type(exc).__name__, error=str(exc), elapsed_ms=elapsed_ms)
        return None, PipelineTrace("query_planner", "llm_error", 0.0, str(exc), {"llm_attempted": True, "llm_call": {**call_metadata, "llm_prompt_chars": len(prompt), "llm_elapsed_ms": round(elapsed_ms, 2), "llm_parsed": False, **health}})

    elapsed_ms = (time.perf_counter() - started) * 1000
    if plan is None:
        health = record_llm_failure("query_planner", model, error_type="InvalidPlannerJSON", error="planner response failed schema validation", elapsed_ms=elapsed_ms)
        return None, PipelineTrace("query_planner", "invalid_plan", 0.0, "planner response failed allowlist/schema validation", {"llm_attempted": True, "llm_call": {**call_metadata, "llm_prompt_chars": len(prompt), "llm_elapsed_ms": round(elapsed_ms, 2), "llm_response_chars": len(response_text), "llm_parsed": False, **health}})

    health = record_llm_success("query_planner", model, elapsed_ms=elapsed_ms, detail="validated_plan")
    metadata = {
        "llm_attempted": True,
        "plan": plan.as_dict(),
        "llm_call": {**call_metadata, "llm_prompt_chars": len(prompt), "llm_elapsed_ms": round(elapsed_ms, 2), "llm_response_chars": len(response_text), "llm_parsed": True, **health},
    }
    return plan, PipelineTrace("query_planner", "plan_accepted", plan.confidence, plan.reason or "validated constrained query plan", metadata)
