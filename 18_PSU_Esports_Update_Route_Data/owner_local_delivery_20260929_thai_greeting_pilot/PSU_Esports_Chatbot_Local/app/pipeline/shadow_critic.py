from __future__ import annotations

import json
import os
import re
import time
import urllib.request
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from typing import Any

from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success
from app.pipeline.schemas import PipelineAnswer


CRITIC_KIND = "shadow_critic"
DEFAULT_MODEL = os.getenv("PSU_SHADOW_CRITIC_MODEL", os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b"))
DEFAULT_TIMEOUT_SEC = float(os.getenv("PSU_SHADOW_CRITIC_TIMEOUT_SEC", "8"))
DEFAULT_NUM_PREDICT = int(os.getenv("PSU_SHADOW_CRITIC_NUM_PREDICT", "260"))

ALLOWED_LABELS = {
    "wrong_route",
    "wrong_intent",
    "wrong_target",
    "wrong_answer_type",
    "missing_subanswer",
    "unsupported_claim",
    "source_mismatch",
    "missing_evidence",
    "should_clarify",
    "should_no_answer",
    "unnecessary_llm_call",
    "timeout",
    "empty_answer",
    "format_issue",
}

SEVERITY_ORDER = {"none": 0, "low": 1, "medium": 2, "high": 3}


@dataclass(frozen=True)
class ShadowCriticResult:
    case_id: str
    question: str
    verdict: str
    score: float
    severity: str
    labels: tuple[str, ...]
    reason: str
    suggested_fix: str
    deterministic_labels: tuple[str, ...]
    llm_labels: tuple[str, ...]
    critic_used_llm: bool
    critic_model: str
    critic_elapsed_sec: float
    critic_status: str
    pipeline_mode: str
    pipeline_route: str
    pipeline_intent: str
    pipeline_elapsed_sec: float
    pipeline_validation_ok: bool
    llm_call_count: int

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _plain(value: Any) -> Any:
    if hasattr(value, "as_dict"):
        return value.as_dict()
    if hasattr(value, "__dataclass_fields__"):
        return asdict(value)
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(v) for v in value]
    return value


def _compact(text: str, limit: int) -> str:
    value = str(text or "")
    return value if len(value) <= limit else value[:limit].rstrip() + "..."


def _norm(text: Any) -> str:
    return str(text or "").strip().lower()


def _category_matches(expected: str, result: PipelineAnswer) -> bool:
    expected = _norm(expected)
    category = _norm(result.route.category)
    intent = _norm(result.route.intent)
    if not expected:
        return True
    aliases = {
        "members": {"members", "overview"},
        "game_controls": {"game_controls", "games"},
        "games": {"games"},
        "service_fee": {"service_fee"},
        "reservation": {"reservation"},
        "schedule": {"schedule"},
        "equipment": {"equipment"},
        "rules": {"rules"},
        "competition_rules": {"competition_rules"},
        "general": {"general", "knowledge", "no_answer", "clarification"},
    }
    if category in aliases.get(expected, {expected}):
        if expected == "game_controls":
            return "control" in intent or "control" in _norm(result.universal_intent.operation if result.universal_intent else "")
        return True
    return False


def _answer_has_any(answer: str, values: list[Any]) -> bool:
    clean = _norm(answer)
    return any(_norm(value) and _norm(value) in clean for value in values)


def _expected_is_safe_abstention(case: dict[str, Any]) -> bool:
    expected = " ".join(
        _norm(case.get(key))
        for key in ("expected_support", "expected_behavior", "quality_bucket")
    )
    return any(term in expected for term in ("no_answer", "clarif", "out_of_scope", "unsupported"))


def deterministic_review(case: dict[str, Any], result: PipelineAnswer) -> tuple[list[str], list[str]]:
    """Return deterministic labels and human-readable reasons.

    These checks are the primary signal. The LLM is only a second opinion and
    cannot turn a deterministic contract failure into a pass.
    """
    labels: list[str] = []
    reasons: list[str] = []
    answer = result.answer or ""
    expected_category = str(case.get("expected_category") or "").strip()
    if expected_category and not _category_matches(expected_category, result):
        labels.append("wrong_route")
        reasons.append(f"expected category {expected_category}, got {result.route.category}")

    expected_mode = str(case.get("expected_mode_prefix") or "").strip()
    if expected_mode and not result.mode.startswith(expected_mode):
        labels.append("wrong_route")
        reasons.append(f"expected mode prefix {expected_mode}, got {result.mode}")

    expected_intent = str(case.get("expected_intent") or "").strip()
    actual_intent = result.universal_intent.operation if result.universal_intent is not None else result.route.intent
    if expected_intent and expected_intent not in {result.route.intent, actual_intent}:
        if expected_intent not in _norm(result.route.intent) and expected_intent not in _norm(actual_intent):
            labels.append("wrong_intent")
            reasons.append(f"expected intent {expected_intent}, got {actual_intent}")

    missing = [value for value in case.get("must_contain", []) if _norm(value) not in _norm(answer)]
    if missing:
        labels.append("missing_subanswer")
        reasons.append("missing expected content: " + ", ".join(map(str, missing[:5])))
    if case.get("must_contain_any") and not _answer_has_any(answer, list(case["must_contain_any"])):
        labels.append("missing_subanswer")
        reasons.append("none of the expected answer alternatives were found")
    forbidden = [value for value in case.get("must_not_contain", []) if _norm(value) in _norm(answer)]
    if forbidden:
        labels.append("unsupported_claim")
        reasons.append("answer contains forbidden content: " + ", ".join(map(str, forbidden[:5])))

    if not result.validation.ok:
        labels.append("wrong_answer_type")
        reasons.append("pipeline validation failed: " + "; ".join(result.validation.errors[:3]))
    if not answer.strip():
        labels.append("empty_answer")
        reasons.append("answer is empty")
    if "timeout" in _norm(result.mode):
        labels.append("timeout")
        reasons.append("pipeline timed out")

    if _expected_is_safe_abstention(case):
        safe_answer = any(term in _norm(answer) for term in ("ไม่พบข้อมูล", "ขอรายละเอียด", "ตอบได้เฉพาะ", "แจ้งเจ้าหน้าที่"))
        if not safe_answer:
            labels.append("should_no_answer")
            reasons.append("case expects clarification/no-answer but answer is not a safe abstention")

    return list(dict.fromkeys(label for label in labels if label in ALLOWED_LABELS)), reasons


def _critic_prompt(case: dict[str, Any], result: PipelineAnswer) -> str:
    trace = [_plain(item) for item in result.trace[-14:]]
    sources = []
    for hit in result.hits[:8]:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        sources.append({
            "id": hit.get("id") if isinstance(hit, dict) else "",
            "category": metadata.get("category", "") if isinstance(metadata, dict) else "",
            "source_url": metadata.get("source_url", "") if isinstance(metadata, dict) else "",
        })
    contract = {
        "expected_category": case.get("expected_category"),
        "expected_intent": case.get("expected_intent"),
        "expected_mode_prefix": case.get("expected_mode_prefix"),
        "must_contain": case.get("must_contain", []),
        "must_contain_any": case.get("must_contain_any", []),
        "must_not_contain": case.get("must_not_contain", []),
        "expected_behavior": case.get("expected_behavior", ""),
    }
    return f"""คุณเป็น Shadow Critic สำหรับตรวจคำตอบของ PSU Esports Studio - Phuket Chatbot
คุณไม่ได้ตอบผู้ใช้ และห้ามสร้างข้อเท็จจริงใหม่ ให้ตรวจเฉพาะคำตอบที่ได้รับ

เกณฑ์:
- ตรวจว่าคำตอบตรงคำถามและ expected contract หรือไม่
- ตรวจว่าคำตอบมี source รองรับหรือไม่จาก SOURCES/TRACE
- ถ้าเป็นคำถามกำกวม ต้องถามกลับ
- ถ้าไม่มีข้อมูลจริง ต้อง no-answer ไม่เดา
- ห้ามตัดสินว่าถูกเพียงเพราะคำตอบฟังดูดี
- ใช้ label ได้เฉพาะ: {', '.join(sorted(ALLOWED_LABELS))}

ตอบ JSON เท่านั้น:
{{"verdict":"pass|fail|needs_review","score":0.0,"severity":"none|low|medium|high","labels":[],"reason":"สั้น ๆ","suggested_fix":"สั้น ๆ"}}

QUESTION:
{_compact(case.get('question', ''), 1400)}

EXPECTED_CONTRACT:
{json.dumps(contract, ensure_ascii=False)}

ANSWER:
{_compact(result.answer, 5000)}

PIPELINE:
{json.dumps({'mode': result.mode, 'route': f'{result.route.category}/{result.route.intent}', 'intent': _plain(result.universal_intent), 'validation': _plain(result.validation)}, ensure_ascii=False)}

SOURCES:
{json.dumps(sources, ensure_ascii=False)}

TRACE_TAIL:
{json.dumps(trace, ensure_ascii=False)[:8000]}
"""


def _parse_critic_json(text: str) -> dict[str, Any] | None:
    raw = str(text or "").strip()
    if not raw:
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, flags=re.DOTALL)
        if not match:
            return None
        try:
            value = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    return value if isinstance(value, dict) else None


def _call_critic_llm(prompt: str, *, model: str, timeout_sec: float) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    allowed, health = llm_call_allowed(CRITIC_KIND, model)
    if not allowed:
        return None, {"llm_attempted": False, "llm_skipped_by_health": True, **health}
    started = time.perf_counter()
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0.0, "top_p": 0.7, "num_predict": DEFAULT_NUM_PREDICT, "num_ctx": 8192},
    }
    try:
        request = urllib.request.Request(
            f"{os.getenv('OLLAMA_URL', 'http://127.0.0.1:11434').rstrip('/')}/api/generate",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=max(0.1, timeout_sec)) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        text = str(data.get("response") or "").strip()
        parsed = _parse_critic_json(text)
        elapsed_ms = (time.perf_counter() - started) * 1000
        if parsed is None:
            health_update = record_llm_failure(CRITIC_KIND, model, error_type="InvalidJSON", error="critic response was not valid JSON", elapsed_ms=elapsed_ms)
            return None, {"llm_attempted": True, "llm_parsed": False, "llm_elapsed_ms": round(elapsed_ms, 2), **health_update}
        health_update = record_llm_success(CRITIC_KIND, model, elapsed_ms=elapsed_ms, detail="shadow critic")
        return parsed, {"llm_attempted": True, "llm_parsed": True, "llm_elapsed_ms": round(elapsed_ms, 2), "llm_response_chars": len(text), **health_update}
    except Exception as exc:  # noqa: BLE001 - critic must never break evaluation
        elapsed_ms = (time.perf_counter() - started) * 1000
        health_update = record_llm_failure(CRITIC_KIND, model, error_type=type(exc).__name__, error=str(exc), elapsed_ms=elapsed_ms)
        return None, {"llm_attempted": True, "llm_parsed": False, "llm_elapsed_ms": round(elapsed_ms, 2), "llm_error": str(exc), **health_update}


def _normalize_llm_labels(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return list(dict.fromkeys(str(item).strip() for item in value if str(item).strip() in ALLOWED_LABELS))


def review_case(
    case: dict[str, Any],
    result: PipelineAnswer,
    *,
    use_llm: bool = False,
    model: str = DEFAULT_MODEL,
    timeout_sec: float = DEFAULT_TIMEOUT_SEC,
) -> ShadowCriticResult:
    started = time.perf_counter()
    deterministic_labels, reasons = deterministic_review(case, result)
    llm_labels: list[str] = []
    llm_reason = ""
    suggested_fix = ""
    critic_status = "deterministic_only"
    critic_used_llm = False
    if use_llm:
        parsed, metadata = _call_critic_llm(_critic_prompt(case, result), model=model, timeout_sec=timeout_sec)
        critic_used_llm = bool(metadata.get("llm_attempted") and metadata.get("llm_parsed"))
        if parsed is not None:
            critic_status = "llm_reviewed"
            llm_labels = _normalize_llm_labels(parsed.get("labels"))
            llm_reason = str(parsed.get("reason") or "").strip()
            suggested_fix = str(parsed.get("suggested_fix") or "").strip()
        else:
            critic_status = "llm_unavailable"

    labels = list(dict.fromkeys((*deterministic_labels, *llm_labels)))
    if not labels and not use_llm:
        verdict = "pass"
        severity = "none"
        score = 1.0
    elif not labels and use_llm and critic_status == "llm_unavailable":
        verdict = "needs_review"
        severity = "low"
        score = 0.5
        reasons.append("shadow critic LLM unavailable; deterministic checks did not find a failure")
    elif labels:
        verdict = "fail"
        severity = "high" if any(label in labels for label in ("wrong_route", "wrong_target", "unsupported_claim", "source_mismatch")) else "medium"
        score = 0.25 if severity == "high" else 0.55
    else:
        verdict = "pass"
        severity = "none"
        score = 1.0
    if llm_reason and not reasons:
        reasons.append(llm_reason)
    reason = "; ".join(dict.fromkeys(reasons + ([llm_reason] if llm_reason and llm_reason not in reasons else []))) or "no failure detected by available checks"
    labels = [label for label in labels if label in ALLOWED_LABELS]
    trace_json = json.dumps(_plain(result.trace), ensure_ascii=False)
    llm_call_count = len(re.findall(r'"llm_kind"|"llm_attempted": true', trace_json))
    return ShadowCriticResult(
        case_id=str(case.get("id") or ""),
        question=str(case.get("question") or ""),
        verdict=verdict,
        score=round(score, 3),
        severity=severity,
        labels=tuple(labels),
        reason=reason,
        suggested_fix=suggested_fix,
        deterministic_labels=tuple(deterministic_labels),
        llm_labels=tuple(llm_labels),
        critic_used_llm=critic_used_llm,
        critic_model=model if use_llm else "",
        critic_elapsed_sec=round(time.perf_counter() - started, 4),
        critic_status=critic_status,
        pipeline_mode=result.mode,
        pipeline_route=f"{result.route.category}/{result.route.intent}",
        pipeline_intent=(f"{result.universal_intent.domain}/{result.universal_intent.operation}" if result.universal_intent else ""),
        pipeline_elapsed_sec=round(result.elapsed, 4),
        pipeline_validation_ok=bool(result.validation.ok),
        llm_call_count=llm_call_count,
    )


def analyze_failures(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    verdicts = Counter(str(row.get("verdict") or "unknown") for row in rows)
    labels = Counter(label for row in rows for label in row.get("labels", []))
    categories = Counter(str(row.get("category") or "unknown") for row in rows)
    routes = Counter(str(row.get("pipeline_route") or "unknown") for row in rows)
    modes = Counter(str(row.get("pipeline_mode") or "unknown") for row in rows)
    failures_by_category: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        category = str(row.get("category") or "unknown")
        for label in row.get("labels", []):
            failures_by_category[category][label] += 1
    latencies = sorted(float(row.get("pipeline_elapsed_sec") or 0.0) for row in rows)
    p95_index = max(0, min(len(latencies) - 1, int(len(latencies) * 0.95) - 1)) if latencies else 0
    return {
        "total_cases": total,
        "verdicts": dict(verdicts),
        "pass_rate": round(verdicts.get("pass", 0) / total, 4) if total else 0.0,
        "failure_rate": round((total - verdicts.get("pass", 0)) / total, 4) if total else 0.0,
        "hard_failure_rate": round(verdicts.get("fail", 0) / total, 4) if total else 0.0,
        "review_rate": round(verdicts.get("needs_review", 0) / total, 4) if total else 0.0,
        "labels": dict(labels),
        "categories": dict(categories),
        "top_routes": routes.most_common(15),
        "top_modes": modes.most_common(15),
        "failures_by_category": {key: dict(value) for key, value in failures_by_category.items()},
        "latency": {
            "avg_sec": round(sum(latencies) / len(latencies), 4) if latencies else 0.0,
            "p95_sec": round(latencies[p95_index], 4) if latencies else 0.0,
            "max_sec": round(max(latencies), 4) if latencies else 0.0,
        },
        "llm_call_count_total": sum(int(row.get("llm_call_count") or 0) for row in rows),
        "critic_llm_cases": sum(1 for row in rows if row.get("critic_used_llm")),
    }
