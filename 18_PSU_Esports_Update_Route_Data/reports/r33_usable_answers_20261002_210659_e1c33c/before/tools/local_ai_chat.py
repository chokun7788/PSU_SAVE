from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def _plain(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _source_list(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_id = str(hit.get("id") or metadata.get("title") or metadata.get("source_id") or "")
        url = str(metadata.get("source_url") or metadata.get("url") or "")
        key = (source_id, url)
        if key in seen:
            continue
        seen.add(key)
        sources.append({"id": source_id, "url": url})
    return sources


def _trace_query_debug(result: Any, question: str, resolved_question: str) -> dict[str, Any]:
    traces: list[dict[str, Any]] = []
    for item in getattr(result, "trace", []) or []:
        stage = getattr(item, "stage", "")
        decision = getattr(item, "decision", "")
        if stage == "preprocess" or decision in {"selected_query_variant", "kept_original_query"}:
            traces.append({
                "stage": stage,
                "decision": decision,
                "confidence": getattr(item, "confidence", 0.0),
                "detail": getattr(item, "detail", ""),
                "metadata": getattr(item, "metadata", {}),
            })

    selected_trace = next((item for item in traces if item["decision"] == "selected_query_variant"), None)
    normalized_trace = next((item for item in traces if item["decision"] == "normalized"), None)
    query_variants = []
    if normalized_trace:
        query_variants = list((normalized_trace.get("metadata") or {}).get("query_variants") or [])

    return {
        "original_question": question,
        "resolved_question": resolved_question,
        "normalized_query": normalized_trace["detail"] if normalized_trace else "",
        "query_variants": query_variants,
        "active_query": selected_trace["detail"] if selected_trace else resolved_question,
        "active_query_changed": selected_trace is not None,
        "trace": traces,
    }


def _set_runtime_model(model: str, timeout_sec: float, num_predict: int) -> None:
    os.environ["PSU_CHATBOT_OLLAMA_MODEL"] = model
    os.environ["PSU_GENERAL_LLM_TIMEOUT_SEC"] = str(timeout_sec)
    os.environ["PSU_GENERAL_LLM_NUM_PREDICT"] = str(num_predict)
    try:
        import app.pipeline.experimental_fallback as experimental_fallback

        experimental_fallback.DEFAULT_MODEL = model
        experimental_fallback.DEFAULT_TIMEOUT_SEC = timeout_sec
        experimental_fallback.DEFAULT_GENERAL_NUM_PREDICT = num_predict
    except Exception:
        pass


def _set_global_timeout(global_timeout_sec: float) -> None:
    os.environ["PSU_PIPELINE_GLOBAL_TIMEOUT_SEC"] = str(max(0.0, float(global_timeout_sec)))


def _set_local_llm_features(*, allow_llm: bool, tool_router: bool, composer: bool) -> None:
    os.environ["PSU_UNIVERSAL_INTENT_LLM"] = "1" if allow_llm else "0"
    os.environ["PSU_QUERY_PLANNER"] = "1" if allow_llm else "0"
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1" if allow_llm and tool_router else "0"
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1" if allow_llm and composer else "0"


def _set_intent_runtime(*, intent_first: bool, intent_model: str, intent_timeout: float, intent_predict: int) -> None:
    os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = "1" if intent_first else "0"
    os.environ.setdefault("PSU_INTENT_LLM_FIRST_ONLY_WEAK", "1")
    os.environ["PSU_INTENT_LLM_TIMEOUT_SEC"] = str(intent_timeout)
    os.environ["PSU_INTENT_LLM_NUM_PREDICT"] = str(intent_predict)
    if intent_model:
        os.environ["PSU_INTENT_LLM_MODEL"] = intent_model


def _set_entity_reranker(*, enabled: bool, model: str, cache_dir: str) -> None:
    os.environ["PSU_ENTITY_RERANKER"] = "1" if enabled else "0"
    if model:
        os.environ["PSU_ENTITY_RERANKER_MODEL"] = model
    if cache_dir:
        os.environ["PSU_ENTITY_RERANKER_CACHE_DIR"] = cache_dir


def _env_truthy(name: str, default: str = "0") -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "y", "on"}


def _check_ollama(model: str, timeout_sec: float, num_predict: int) -> tuple[bool, str, float]:
    started = time.perf_counter()
    payload = {
        "model": model,
        "prompt": "ตอบสั้นๆ ภาษาไทย: สวัสดี",
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": num_predict},
    }
    request = urllib.request.Request(
        f"{os.getenv('OLLAMA_URL', 'http://127.0.0.1:11434').rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_sec) as response:
            data = json.loads(response.read().decode("utf-8"))
        answer = str(data.get("response", "")).strip()
        thinking = str(data.get("thinking", "")).strip()
        done_reason = str(data.get("done_reason") or "")
        if answer:
            return True, answer, round(time.perf_counter() - started, 3)
        if thinking:
            return (
                False,
                f"empty response; thinking_len={len(thinking)}; done_reason={done_reason}; num_predict={num_predict}",
                round(time.perf_counter() - started, 3),
            )
        return False, f"empty response; done_reason={done_reason}; num_predict={num_predict}", round(time.perf_counter() - started, 3)
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return False, f"{type(exc).__name__}: {exc}", round(time.perf_counter() - started, 3)


def _print_help() -> None:
    print(
        """
คำสั่งในแชท:
  /help              แสดงคำสั่งทั้งหมด
  /exit, /quit       ออกจากแชท
  /clear             ล้าง history ใน session นี้
  /debug on|off      เปิด/ปิด trace debug
  /llm on|off        เปิด/ปิด Local LLM fallback
  /router on|off     เปิด/ปิด LLM tool router
  /composer on|off   เปิด/ปิด facts-only LLM composer
  /rag on|off        เปิด/ปิด experimental RAG fallback
  /reranker on|off   เปิด/ปิด gated entity reranker
  /model NAME        เปลี่ยน Ollama model เช่น /model qwen2.5:1.5b
  /global-timeout SEC เปลี่ยน timeout รวมต่อ 1 คำถาม (0 = ปิด)
  /timeout SEC       เปลี่ยน timeout ของ general LLM
  /predict N         เปลี่ยน num_predict ของ general LLM
  /check             ทดสอบเรียก Ollama model ปัจจุบันแบบสั้น
  /llm-health        ดูสถานะ LLM health / circuit breaker
  /history           ดูจำนวนข้อความใน memory
  /session           ดู session id ปัจจุบัน
""".strip()
    )
    print(
        """
Intent experiment:
  /intent first       enable adaptive LLM intent review
  /intent normal      return to heuristic-first intent
  /intent-model NAME  use a separate Ollama model for intent
  /intent-timeout SEC set intent model timeout
  /intent-predict N   set intent model num_predict
""".strip()
    )


class LocalChat:
    def __init__(
        self,
        *,
        model: str,
        timeout_sec: float,
        global_timeout_sec: float,
        num_predict: int,
        allow_llm: bool,
        tool_router: bool,
        composer: bool,
        intent_first: bool,
        intent_model: str,
        intent_timeout: float,
        intent_predict: int,
        entity_reranker: bool,
        entity_reranker_model: str,
        entity_reranker_cache_dir: str,
        rag_fallback: bool,
        debug: bool,
        log: bool,
    ) -> None:
        _set_runtime_model(model, timeout_sec, num_predict)
        _set_global_timeout(global_timeout_sec)
        _set_local_llm_features(allow_llm=allow_llm, tool_router=tool_router, composer=composer)
        _set_intent_runtime(
            intent_first=intent_first and allow_llm,
            intent_model=intent_model,
            intent_timeout=intent_timeout,
            intent_predict=intent_predict,
        )
        _set_entity_reranker(
            enabled=entity_reranker,
            model=entity_reranker_model,
            cache_dir=entity_reranker_cache_dir,
        )
        from app.pipeline.warmup import pipeline_warmup_enabled, warm_pipeline_caches
        from app.pipeline.llm_health import llm_health_snapshot, llm_preflight_enabled, preflight_ollama
        from app.runtime.pipeline_answer import answer_question_pipeline_debug
        from app.session.chat_logger import write_chat_log
        from app.session.context_resolver import resolve_question_with_context

        if pipeline_warmup_enabled():
            print("Warming PSU Esports chatbot caches...")
            warmup = warm_pipeline_caches()
            status = "ok" if warmup.ok else "partial"
            print(f"Warmup {status} in {warmup.elapsed_sec:.4f}s")
            for error in warmup.errors:
                print(f"Warmup warning: {error}")

        if allow_llm and llm_preflight_enabled():
            print("Checking Local LLM health...")
            preflight = preflight_ollama(
                model=model,
                kind="preflight",
                timeout_sec=float(os.getenv("PSU_LLM_PREFLIGHT_TIMEOUT_SEC", "90")),
                num_predict=int(os.getenv("PSU_LLM_PREFLIGHT_NUM_PREDICT", "1")),
                num_ctx=int(os.getenv("PSU_LLM_PREFLIGHT_NUM_CTX", os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072"))),
            )
            status = "ok" if preflight.get("ok") else "unhealthy"
            print(f"LLM preflight {status} in {float(preflight.get('elapsed_ms', 0.0)) / 1000:.3f}s")
            if not preflight.get("ok"):
                print(f"LLM warning: {preflight.get('error_type')}: {preflight.get('error')}")

        self.answer_question_pipeline_debug = answer_question_pipeline_debug
        self.write_chat_log = write_chat_log
        self.resolve_question_with_context = resolve_question_with_context
        self.llm_health_snapshot = llm_health_snapshot
        self.model = model
        self.timeout_sec = timeout_sec
        self.global_timeout_sec = global_timeout_sec
        self.num_predict = num_predict
        self.allow_llm = allow_llm
        self.tool_router = tool_router
        self.composer = composer
        self.intent_first = intent_first
        self.intent_model = intent_model
        self.intent_timeout = intent_timeout
        self.intent_predict = intent_predict
        self.entity_reranker = entity_reranker
        self.entity_reranker_model = entity_reranker_model
        self.entity_reranker_cache_dir = entity_reranker_cache_dir
        self.rag_fallback = rag_fallback
        self.debug = debug
        self.log = log
        self.session_id = f"local-cli-{uuid4()}"
        self.history: list[dict[str, Any]] = []

    def handle_command(self, line: str) -> bool:
        parts = line.strip().split(maxsplit=1)
        command = parts[0].lower()
        value = parts[1].strip() if len(parts) > 1 else ""

        if command in {"/exit", "/quit"}:
            return False
        if command == "/help":
            _print_help()
        elif command == "/clear":
            self.history.clear()
            print("ล้าง memory ของ session นี้แล้ว")
        elif command == "/history":
            print(f"history: {len(self.history)} messages | session_id={self.session_id}")
        elif command == "/session":
            print(f"session_id={self.session_id}")
        elif command == "/debug":
            self.debug = value.lower() in {"1", "true", "on", "yes", "y"}
            print(f"debug={self.debug}")
        elif command == "/llm":
            self.allow_llm = value.lower() in {"1", "true", "on", "yes", "y"}
            _set_local_llm_features(allow_llm=self.allow_llm, tool_router=self.tool_router, composer=self.composer)
            _set_intent_runtime(
                intent_first=self.intent_first and self.allow_llm,
                intent_model=self.intent_model,
                intent_timeout=self.intent_timeout,
                intent_predict=self.intent_predict,
            )
            print(f"allow_llm={self.allow_llm}")
        elif command == "/intent":
            if value.lower() in {"first", "on", "1", "true", "yes", "y"}:
                self.intent_first = True
            elif value.lower() in {"normal", "off", "0", "false", "no", "n"}:
                self.intent_first = False
            _set_intent_runtime(
                intent_first=self.intent_first and self.allow_llm,
                intent_model=self.intent_model,
                intent_timeout=self.intent_timeout,
                intent_predict=self.intent_predict,
            )
            print(
                f"intent_first={self.intent_first} | intent_model={self.intent_model or self.model} "
                f"| timeout={self.intent_timeout}s | num_predict={self.intent_predict}"
            )
        elif command == "/intent-model":
            if not value:
                print(f"intent_model={self.intent_model or self.model}")
            else:
                self.intent_model = value
                _set_intent_runtime(
                    intent_first=self.intent_first and self.allow_llm,
                    intent_model=self.intent_model,
                    intent_timeout=self.intent_timeout,
                    intent_predict=self.intent_predict,
                )
                print(f"intent_model={self.intent_model}")
        elif command == "/intent-timeout":
            try:
                self.intent_timeout = float(value)
            except ValueError:
                print(f"intent_timeout={self.intent_timeout}")
            else:
                _set_intent_runtime(
                    intent_first=self.intent_first and self.allow_llm,
                    intent_model=self.intent_model,
                    intent_timeout=self.intent_timeout,
                    intent_predict=self.intent_predict,
                )
                print(f"intent_timeout={self.intent_timeout}")
        elif command == "/intent-predict":
            try:
                self.intent_predict = int(value)
            except ValueError:
                print(f"intent_predict={self.intent_predict}")
            else:
                _set_intent_runtime(
                    intent_first=self.intent_first and self.allow_llm,
                    intent_model=self.intent_model,
                    intent_timeout=self.intent_timeout,
                    intent_predict=self.intent_predict,
                )
                print(f"intent_predict={self.intent_predict}")
        elif command == "/router":
            self.tool_router = value.lower() in {"1", "true", "on", "yes", "y"}
            _set_local_llm_features(allow_llm=self.allow_llm, tool_router=self.tool_router, composer=self.composer)
            print(f"tool_router={self.tool_router} | PSU_LLM_TOOL_ROUTER={os.environ.get('PSU_LLM_TOOL_ROUTER')}")
        elif command == "/composer":
            self.composer = value.lower() in {"1", "true", "on", "yes", "y"}
            _set_local_llm_features(allow_llm=self.allow_llm, tool_router=self.tool_router, composer=self.composer)
            print(f"composer={self.composer} | PSU_FACTS_LLM_COMPOSER={os.environ.get('PSU_FACTS_LLM_COMPOSER')}")
        elif command == "/rag":
            self.rag_fallback = value.lower() in {"1", "true", "on", "yes", "y"}
            print(f"rag_fallback={self.rag_fallback}")
        elif command == "/reranker":
            self.entity_reranker = value.lower() in {"1", "true", "on", "yes", "y"}
            _set_entity_reranker(
                enabled=self.entity_reranker,
                model=self.entity_reranker_model,
                cache_dir=self.entity_reranker_cache_dir,
            )
            print(f"entity_reranker={self.entity_reranker} | model={self.entity_reranker_model}")
        elif command == "/model":
            if not value:
                print(f"model={self.model}")
            else:
                self.model = value
                _set_runtime_model(self.model, self.timeout_sec, self.num_predict)
                print(f"model={self.model}")
        elif command == "/global-timeout":
            try:
                self.global_timeout_sec = float(value)
            except ValueError:
                print(f"global_timeout={self.global_timeout_sec}")
            else:
                _set_global_timeout(self.global_timeout_sec)
                print(f"global_timeout={self.global_timeout_sec}")
        elif command == "/timeout":
            try:
                self.timeout_sec = float(value)
            except ValueError:
                print(f"timeout={self.timeout_sec}")
            else:
                _set_runtime_model(self.model, self.timeout_sec, self.num_predict)
                print(f"timeout={self.timeout_sec}")
        elif command == "/predict":
            try:
                self.num_predict = int(value)
            except ValueError:
                print(f"num_predict={self.num_predict}")
            else:
                _set_runtime_model(self.model, self.timeout_sec, self.num_predict)
                print(f"num_predict={self.num_predict}")
        elif command == "/check":
            ok, text, elapsed = _check_ollama(self.model, self.timeout_sec, self.num_predict)
            status = "OK" if ok else "FAILED"
            print(f"Ollama {status} | model={self.model} | num_predict={self.num_predict} | elapsed={elapsed}s")
            print(text or "(empty response)")
        elif command == "/llm-health":
            print(json.dumps(self.llm_health_snapshot(), ensure_ascii=False, indent=2))
        else:
            print("ไม่รู้จักคำสั่งนี้ พิมพ์ /help เพื่อดูคำสั่งทั้งหมด")
        return True

    def ask(self, question: str) -> None:
        resolved = self.resolve_question_with_context(question, self.history[-12:])
        started = time.perf_counter()
        result = self.answer_question_pipeline_debug(
            resolved.resolved_question,
            experimental_rag_fallback=self.rag_fallback,
            experimental_allow_llm=self.allow_llm,
        )
        wall_sec = round(time.perf_counter() - started, 4)
        sources = _source_list(result.hits)
        query_debug = _trace_query_debug(result, question, resolved.resolved_question)

        print()
        print(result.answer)
        print()
        print(
            f"[mode={result.mode} | route={result.route.category}/{result.route.intent} "
            f"| confidence={result.confidence:.2f} | latency={result.elapsed:.3f}s | wall={wall_sec:.3f}s]"
        )
        if result.universal_intent is not None:
            print(
                f"[intent={result.universal_intent.domain}/{result.universal_intent.operation} "
                f"| method={result.universal_intent.method} | confidence={result.universal_intent.confidence:.2f}]"
            )
        if sources:
            print("sources:")
            for source in sources[:5]:
                label = source["id"] or "source"
                url = source["url"]
                print(f"- {label}: {url}" if url else f"- {label}")

        if self.debug:
            print("debug:")
            print(json.dumps({
                "context_resolution": resolved.to_dict(),
                "query_debug": query_debug,
                "trace": _plain(result.trace),
                "validation": _plain(result.validation),
            }, ensure_ascii=False, indent=2))

        self.history.append({"role": "user", "text": question})
        self.history.append({
            "role": "assistant",
            "text": result.answer,
            "universal_intent": _plain(result.universal_intent),
            "route_category": result.route.category,
            "route_intent": result.route.intent,
            "resolved_text": resolved.resolved_question,
        })
        self.history = self.history[-20:]

        if self.log:
            sinks = self.write_chat_log({
                "channel": "local_cli",
                "client_session_id": self.session_id,
                "question": question,
                "resolved_question": resolved.resolved_question,
                "context_resolution": resolved.to_dict(),
                "query_debug": query_debug,
                "recent_history_count": len(self.history),
                    "experimental": {
                    "rag_fallback": self.rag_fallback,
                    "allow_llm": self.allow_llm,
                    "tool_router": self.tool_router,
                    "composer": self.composer,
                    "intent_first": self.intent_first,
                    "intent_model": self.intent_model or os.environ.get("PSU_INTENT_LLM_MODEL") or self.model,
                    "intent_timeout": self.intent_timeout,
                    "intent_predict": self.intent_predict,
                    "entity_reranker": self.entity_reranker,
                    "entity_reranker_model": self.entity_reranker_model,
                    "model": self.model,
                    "global_timeout": self.global_timeout_sec,
                    "num_predict": self.num_predict,
                },
                "answer": result.answer,
                "mode": result.mode,
                "route_category": result.route.category,
                "route_intent": result.route.intent,
                "universal_intent": _plain(result.universal_intent),
                "confidence": result.confidence,
                "latency_sec": result.elapsed,
                "wall_sec": wall_sec,
                "sources": sources,
                "validation_ok": result.validation.ok,
            })
            if self.debug:
                print(f"log_sinks={sinks}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local terminal chat for PSU Esports RAG chatbot")
    parser.add_argument("--model", default=os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b"))
    parser.add_argument("--timeout", type=float, default=float(os.getenv("PSU_GENERAL_LLM_TIMEOUT_SEC", "20")))
    parser.add_argument("--global-timeout", type=float, default=float(os.getenv("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC", "20")))
    parser.add_argument("--num-predict", type=int, default=int(os.getenv("PSU_GENERAL_LLM_NUM_PREDICT", "128")))
    parser.add_argument("--no-llm", action="store_true", help="disable Local LLM fallback")
    parser.add_argument("--no-tool-router", action="store_true", help="disable LLM tool router")
    parser.add_argument("--no-composer", action="store_true", help="disable facts-only LLM composer")
    parser.add_argument("--composer", action="store_true", help="enable facts-only LLM composer for nicer but slower structured answers")
    parser.set_defaults(intent_first=_env_truthy("PSU_UNIVERSAL_INTENT_LLM_FIRST", "1"))
    parser.add_argument("--intent-first", dest="intent_first", action="store_true", help="enable adaptive Local LLM intent review after normalization")
    parser.add_argument("--no-intent-first", dest="intent_first", action="store_false", help="disable adaptive Local LLM intent review")
    parser.add_argument("--intent-model", default=os.getenv("PSU_INTENT_LLM_MODEL", ""), help="optional separate Ollama model for intent classification")
    parser.add_argument("--intent-timeout", type=float, default=float(os.getenv("PSU_INTENT_LLM_TIMEOUT_SEC", "8")))
    parser.add_argument("--intent-predict", type=int, default=int(os.getenv("PSU_INTENT_LLM_NUM_PREDICT", "50")))
    parser.set_defaults(entity_reranker=_env_truthy("PSU_ENTITY_RERANKER", "0"))
    parser.add_argument("--entity-reranker", action="store_true", help="enable gated BGE entity reranker for ambiguous game names")
    parser.add_argument("--entity-reranker-model", default=os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3"))
    parser.add_argument("--entity-reranker-cache-dir", default=os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", "D:/AIModels/huggingface"))
    parser.add_argument("--no-rag-fallback", action="store_true", help="disable experimental RAG fallback")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--no-log", action="store_true")
    parser.add_argument("--once", default="", help="ask one question and exit")
    return parser.parse_args()


def main() -> int:
    _configure_stdout()
    args = parse_args()
    chat = LocalChat(
        model=args.model,
        timeout_sec=args.timeout,
        global_timeout_sec=args.global_timeout,
        num_predict=args.num_predict,
        allow_llm=not args.no_llm,
        tool_router=not args.no_tool_router,
        composer=args.composer and not args.no_composer,
        intent_first=args.intent_first,
        intent_model=args.intent_model,
        intent_timeout=args.intent_timeout,
        intent_predict=args.intent_predict,
        entity_reranker=args.entity_reranker,
        entity_reranker_model=args.entity_reranker_model,
        entity_reranker_cache_dir=args.entity_reranker_cache_dir,
        rag_fallback=not args.no_rag_fallback,
        debug=args.debug,
        log=not args.no_log,
    )

    if args.once:
        chat.ask(args.once)
        return 0

    print("PSU Esports Local AI Chat")
    print(
        f"model={chat.model} | timeout={chat.timeout_sec}s | num_predict={chat.num_predict} "
        f"| global_timeout={chat.global_timeout_sec}s "
        f"| allow_llm={chat.allow_llm} | tool_router={chat.tool_router} | composer={chat.composer} "
        f"| intent_first={chat.intent_first} | intent_model={chat.intent_model or chat.model} "
        f"| entity_reranker={chat.entity_reranker} | rag_fallback={chat.rag_fallback}"
    )
    print("พิมพ์ /help เพื่อดูคำสั่ง หรือ /exit เพื่อออก")

    while True:
        try:
            line = input("\nคุณ> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nออกจากแชทแล้ว")
            return 0
        if not line:
            continue
        if line.startswith("/"):
            if not chat.handle_command(line):
                print("ออกจากแชทแล้ว")
                return 0
            continue
        chat.ask(line)


if __name__ == "__main__":
    raise SystemExit(main())
