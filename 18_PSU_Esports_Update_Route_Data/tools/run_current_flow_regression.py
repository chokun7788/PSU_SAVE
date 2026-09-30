"""Serial model-enabled regression with real input guard and a process watchdog.

This is an in-process backend evaluation, not an HTTP/load benchmark. The watchdog
protects the evaluation runner; it does not implement a production deadline.
"""
from __future__ import annotations

import argparse
import dataclasses
import faulthandler
import hashlib
import importlib.util
import json
import math
import multiprocessing as mp
import os
import shutil
import statistics
import subprocess
import sys
import time
import traceback
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODEL = "scb10x/typhoon2.5-qwen3-4b"
FAQ = ROOT / "data/eval/model_benchmark_1500.jsonl"
KEYBOARD = ROOT / "data/eval/keyboard_input_anomaly_ground_truth_500_20260830.jsonl"


def plain(value):
    if dataclasses.is_dataclass(value):
        return plain(dataclasses.asdict(value))
    if isinstance(value, (dict, SimpleNamespace)):
        return {str(k): plain(v) for k, v in (vars(value) if isinstance(value, SimpleNamespace) else value).items()}
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def write_json(path, value):
    path.write_text(json.dumps(plain(value), ensure_ascii=False, indent=2), encoding="utf-8")


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def configure(db):
    env = {
        "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1",
        "PSU_LLM_PREFLIGHT": "0", "PSU_OLLAMA_THINK": "false",
        "PSU_CHATBOT_OLLAMA_MODEL": MODEL, "PSU_INTENT_LLM_MODEL": MODEL,
        "PSU_TOOL_ROUTER_MODEL": MODEL, "PSU_FACTS_LLM_MODEL": MODEL,
        "PSU_KNOWLEDGE_LLM_MODEL": MODEL, "PSU_LLM_MAX_CALLS": "2",
        # Keep evaluation behavior aligned with the production 10-second SLA:
        # 9 seconds for useful pipeline work and 1 second for final response.
        "PSU_GENERAL_LLM_TIMEOUT_SEC": "4", "PSU_PIPELINE_GLOBAL_TIMEOUT_SEC": "9",
        "PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC": "4", "PSU_FACTS_LLM_TIMEOUT_SEC": "4",
        "PSU_INTENT_LLM_TIMEOUT_SEC": "1.2", "PSU_QUERY_PLANNER_TIMEOUT_SEC": "1.2",
        "PSU_TOOL_ROUTER_TIMEOUT_SEC": "1.2",
        "PSU_GENERAL_LLM_NUM_PREDICT": "128", "PSU_RAG_LLM_NUM_PREDICT": "128",
        "PSU_FACTS_LLM_NUM_PREDICT": "192", "PSU_INTENT_LLM_NUM_PREDICT": "128",
        "PSU_TOOL_ROUTER_NUM_PREDICT": "128", "PSU_GENERAL_LLM_NUM_CTX": "2048",
        "PSU_FACTS_LLM_NUM_CTX": "3072", "PSU_INTENT_LLM_NUM_CTX": "2048",
        "PSU_TOOL_ROUTER_NUM_CTX": "2048", "PSU_QUERY_PLANNER_NUM_CTX": "2048",
        "PSU_LLM_TOOL_ROUTER": "0", "PSU_FACTS_LLM_COMPOSER": "1",
        "PSU_RAG_LLM_COMPOSER": "1", "PSU_MODEL_FIRST_FLOW": "1",
        "PSU_MODEL_FIRST_MIN_REMAINING_SEC": "6.0", "PSU_SEMANTIC_RETRIEVAL": "1",
        "PSU_EMBEDDING_MODEL": "psu-bge-m3:q8_0", "PSU_EMBEDDING_NUM_CTX": "1024",
        "OLLAMA_URL": "http://127.0.0.1:11434", "PSU_CANONICAL_KNOWLEDGE": "1",
        "PSU_KNOWLEDGE_DB": str(db), "PSU_KNOWLEDGE_ALLOW_DEMO": "1",
        "PSU_INPUT_QUALITY_GUARD_MODE": "enforce", "PSU_INPUT_QUALITY_REPEAT_POLICY": "ask_retype",
        "PSU_INPUT_QUALITY_LAYOUT_THRESHOLD": "0.39", "PSU_INPUT_QUALITY_REPEAT_THRESHOLD": "0.55",
    }
    os.environ.update(env)
    return env


def fingerprints():
    paths = list((ROOT / "app").rglob("*.py"))
    for pattern in ("*.json", "*.jsonl"):
        paths.extend((ROOT / "data").rglob(pattern))
    paths.extend([Path(__file__), ROOT / "tools/run_model_benchmark_eval.py",
                  ROOT / "tools/run_keyboard_input_pipeline_eval.py", ROOT / "tests/test_canonical_knowledge.py"])
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))}


def pilot_cases():
    specs = [
        ("Nebula Fields แนวไหน", "canonical_answer", ["Sandbox"], []),
        ("เนบิวลาฟิลด์ เป็นเกมแนวอะไร", "canonical_answer", ["Sandbox"], []),
        ("What genre is Nebula Fields?", "canonical_answer", ["Sandbox"], []),
        ("Nebula Fields เล่นยังไง", "canonical_answer", ["เลือกโหมดสำรวจ", "ข้อมูลสมมติ"], []),
        ("How to play Nebula Fields?", "canonical_answer", ["เลือกโหมดสำรวจ"], []),
        ("Nebula Fields มีให้เล่นไหม", "canonical_no_answer", [], ["ไม่มีให้บริการ"]),
        ("Nebula Fields อยู่โซนไหน", "canonical_no_answer", [], []),
        ("Nebula Fields เล่นยังไง และมีให้เล่นไหม", "canonical_partial", ["เลือกโหมด", "ยังไม่มีข้อมูลยืนยัน"], []),
        ("กฎอาหารทดลอง คืออะไร", "canonical_answer", ["ยกเว้น", "ไม่ครอบคลุมบริเวณเครื่องเล่น"], []),
        ("สรุปกฎ กฎอาหารทดลอง", "canonical_answer", ["ยกเว้น", "ไม่ครอบคลุมบริเวณเครื่องเล่น"], []),
        ("Nebula Fields บน PS5 เล่นยังไง", "canonical_clarification", [], []),
        ("Nebula Fields ราคาเท่าไร", "canonical_clarification", [], []),
        ("มีเกมทั้งหมดกี่เกม", "canonical_clarification", [], []),
        ("จอง Nebula Fields", "canonical_clarification", [], []),
        ("Nebula Fields มีให้เล่นพรุ่งนี้ไหม", "canonical_clarification", [], []),
        ("Nebula Fields ดีไหม", "canonical_clarification", [], []),
    ]
    return [{"id": f"CP-{i:02d}", "question": q, "expected_mode_prefix": mode,
             "must_contain": required, "must_not_contain": forbidden, "group": "synthetic_canonical"}
            for i, (q, mode, required, forbidden) in enumerate(specs, 1)]


def setup_pilot(db, out):
    from app.knowledge.store import KnowledgeStore
    from app.knowledge.local_models import embed_documents
    fixture = load_module("regression_fixture", ROOT / "tests/test_canonical_knowledge.py")
    store = KnowledgeStore(db)
    store.initialize(allow_demo=True)
    for record in (fixture.game_record(), fixture.rule_record()):
        row = store.save(record, actor="evaluation_fixture", expected_version=0)
        store.approve(row["record_id"], row["version"], row["hash"], actor="evaluation_reviewer")
        write_json(out / (row["record_id"] + ".json"), record)
    release = store.publish(actor="evaluation_reviewer", request_key="regression_initial",
                            expected_active=store.snapshot()["active"], embed=embed_documents)
    return {"release": release, "snapshot": store.snapshot()}


def outcome_checks(case, result, elapsed, suite, faq_judge, keyboard_judge):
    if suite == "keyboard":
        legacy = keyboard_judge(case.get("source_case"), result, elapsed, 9)
    else:
        legacy = faq_judge(case, result, elapsed, 9, "llm")
    validation = bool(result.validation.ok)
    errors = legacy.get("errors", [])
    text_errors = [e for e in errors if e.startswith(("missing", "forbidden", "llm_unavailable", "llm_response_too_short"))]
    return {"legacy_judge": legacy, "text_contract_passed": not text_errors,
            "text_contract_errors": text_errors,
            "strict_passed": bool(legacy.get("passed")) and validation and elapsed <= 10,
            "within_10s": elapsed <= 10}


def worker(conn, db, log_path):
    configure(db)
    sys.dont_write_bytecode = True
    with open(log_path, "a", encoding="utf-8", buffering=1) as log:
        sys.stdout = sys.stderr = log
        faulthandler.enable(file=log)
        try:
            from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
            from app.session.context_resolver import resolve_question_with_context
            from app.pipeline.engine import answer_question_pipeline_debug
            from app.pipeline.request_deadline import request_deadline, deadline_metadata
            from app.pipeline.warmup import warm_pipeline_caches
            from app.knowledge.local_models import warm_knowledge_models
            faq_eval = load_module("regression_faq_eval", ROOT / "tools/run_model_benchmark_eval.py")
            kb_eval = load_module("regression_keyboard_eval", ROOT / "tools/run_keyboard_input_pipeline_eval.py")
            startup = time.perf_counter()
            guard = RuntimeInputQualityGuard.from_environment()
            caches = warm_pipeline_caches()
            models = warm_knowledge_models()
            conn.send({"event": "ready", "elapsed_sec": time.perf_counter() - startup,
                       "guard": guard.startup_status(), "caches": plain(caches), "models": plain(models)})
            while True:
                task = conn.recv()
                if task is None:
                    break
                case, suite = task["case"], task["suite"]
                print(f"CASE {case['id']} {datetime.now().astimezone().isoformat()}", flush=True)
                faulthandler.dump_traceback_later(25, file=log)
                started = time.perf_counter()
                prefix = {}
                try:
                    with request_deadline(9):
                        question = case.get("observed_input", case.get("question", ""))
                        decision = guard.inspect(question)
                        prefix = {"guard": decision.to_log_dict(), "guard_message": decision.message,
                                  "pipeline_executed": not decision.should_short_circuit}
                        conn.send({"event": "phase", **prefix})
                        if decision.should_short_circuit:
                            result = SimpleNamespace(answer=decision.message, mode=decision.mode,
                                route=SimpleNamespace(category="input_quality"), validation=SimpleNamespace(ok=True),
                                trace=[], decision_artifact=None)
                            resolved = {"resolved_question": question, "skipped": "input_guard"}
                            context_sec = 0.0
                        else:
                            step = time.perf_counter()
                            resolved = resolve_question_with_context(question, [])
                            context_sec = time.perf_counter() - step
                            result = answer_question_pipeline_debug(resolved.resolved_question,
                                experimental_allow_llm=True, experimental_rag_fallback=True)
                        elapsed = time.perf_counter() - started
                        deadline = deadline_metadata()
                    checks = outcome_checks(case, result, elapsed, suite, faq_eval._judge, kb_eval._judge_against_source)
                    data = plain(result)
                    calls = faq_eval._full_llm_call_rows(result)
                    canonical = [t for t in data["trace"] if t.get("stage") == "knowledge_llm_order"]
                    stages = faq_eval._stage_timing_rows(result.trace)
                    conn.send({"event": "result", "status": "completed", "wall_sec": elapsed,
                        "right_censored": False, **prefix, **data, **checks,
                        "context": plain(resolved), "context_sec": context_sec, "deadline": plain(deadline),
                        "stage_timings": stages, "llm_calls": plain(calls), "canonical_llm_events": canonical})
                except Exception:
                    conn.send({"event": "result", "status": "exception", "wall_sec": time.perf_counter() - started,
                               **prefix, "answer": "", "exception": traceback.format_exc(), "strict_passed": False})
                finally:
                    faulthandler.cancel_dump_traceback_later()
        except Exception:
            conn.send({"event": "startup_error", "exception": traceback.format_exc()})


def stop_worker(process, conn):
    if process.is_alive():
        try:
            conn.send(None)
        except (BrokenPipeError, EOFError, OSError):
            pass
        process.join(2)
    if process.is_alive():
        process.terminate()
        process.join(10)
    if process.is_alive():
        process.kill()
        process.join(10)
    conn.close()


def start_worker(db, out, number):
    parent, child = mp.get_context("spawn").Pipe()
    process = mp.get_context("spawn").Process(target=worker, args=(child, db, str(out / f"worker_{number:03d}.log")))
    process.start()
    child.close()
    if not parent.poll(180):
        stop_worker(process, parent)
        raise RuntimeError("Worker startup exceeded 180 seconds")
    event = parent.recv()
    write_json(out / f"startup_{number:03d}.json", event)
    if event.get("event") != "ready":
        stop_worker(process, parent)
        raise RuntimeError(str(event))
    print(f"Worker {number} ready in {event['elapsed_sec']:.2f}s", flush=True)
    return process, parent


def receive_case(conn, watchdog):
    started = time.perf_counter()
    partial = {}
    while True:
        remaining = watchdog - (time.perf_counter() - started)
        if remaining <= 0 or not conn.poll(max(0, remaining)):
            return {**partial, "status": "harness_timeout", "wall_sec": time.perf_counter() - started,
                    "right_censored": True, "answer": "", "strict_passed": False,
                    "error": "No chatbot output received before the evaluation watchdog; not a product response."}
        try:
            event = conn.recv()
        except (EOFError, OSError):
            return {**partial, "status": "worker_crash", "wall_sec": time.perf_counter() - started,
                    "answer": "", "strict_passed": False}
        if event.get("event") == "phase":
            partial.update({k: v for k, v in event.items() if k != "event"})
        elif event.get("event") == "result":
            return {k: v for k, v in event.items() if k != "event"}
        else:
            return {**event, "status": "worker_error", "answer": "", "strict_passed": False}


def percentile(values, p):
    return sorted(values)[max(0, math.ceil(len(values) * p) - 1)] if values else None


def summarize(rows):
    result = {}
    for suite in sorted({r["suite"] for r in rows}):
        subset = [r for r in rows if r["suite"] == suite]
        times = [r["wall_sec"] for r in subset]
        item = {"total": len(subset), "status": dict(Counter(r["status"] for r in subset)),
                "legacy_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in subset),
                "strict_passed": sum(bool(r.get("strict_passed")) for r in subset),
                "text_contract_passed": sum(bool(r.get("text_contract_passed")) for r in subset),
                "mean_sec": statistics.mean(times), "median_sec": statistics.median(times),
                "p95_sec_nearest_rank": percentile(times, .95), "max_observed_sec": max(times),
                "over_10s": sum(t > 10 for t in times),
                "guard_blocked": sum(r.get("guard", {}).get("should_retype", False) for r in subset),
                "canonical_cases": sum(str(r.get("mode", "")).startswith("canonical_") for r in subset),
                "modes": dict(Counter(r.get("mode", r["status"]) for r in subset)),
                "llm_logged_entries": sum(len(r.get("llm_calls", [])) for r in subset),
                "canonical_llm_events": sum(len(r.get("canonical_llm_events", [])) for r in subset)}
        if suite == "keyboard":
            for flag, truth in (("keyboard_layout_mismatch", "should_detect_keyboard_layout"),
                                ("repeated_character_typo", "should_detect_repeated_character")):
                counts = Counter()
                for r in subset:
                    expected = bool(r["case"].get(truth))
                    detected = flag in r.get("guard", {}).get("flags", [])
                    counts[("T" if expected == detected else "F") + ("P" if detected else "N")] += 1
                item[flag] = dict(counts)
            item["legacy_block_agreement"] = sum(bool(r.get("guard", {}).get("should_retype")) == bool(r["case"].get("should_block_answer")) for r in subset)
            item["legacy_action_agreement"] = sum(r.get("guard", {}).get("detected_action") == r["case"].get("expected_action") for r in subset)
            mapped = [r for r in subset if r.get("pipeline_executed") and r["case"].get("source_case")]
            item["mapped_allowed"] = len(mapped)
            item["mapped_allowed_legacy_passed"] = sum(bool(r.get("legacy_judge", {}).get("passed")) for r in mapped)
            item["normal_input_blocked"] = sum(not r["case"].get("expected_flags") and bool(r.get("guard", {}).get("should_retype")) for r in subset)
        result[suite] = item
    return result


def export_markdown(rows, out):
    qa = out / "questions_answers"
    qa.mkdir(exist_ok=True)
    index = ["# Model-enabled regression: question and answer logs", "",
             "Only synthetic/public test data. No booking PII. Test configuration: guard enforce + isolated canonical pilot.", "",
             "The process watchdog is a runner safeguard, not a working production timeout. Timed-out cases have no returned answer.", ""]
    for suite in sorted({r["suite"] for r in rows}):
        subset = [r for r in rows if r["suite"] == suite]
        for start in range(0, len(subset), 100):
            name = f"{suite}_{start + 1:04d}_{min(start + 100, len(subset)):04d}.md"
            index.append(f"- [{name}](questions_answers/{name})")
            lines = [f"# {suite}: {start + 1}-{min(start + 100, len(subset))}", ""]
            for r in subset[start:start + 100]:
                lines.extend([f"## {r['id']}", "", "### Question", r["question"], "", "### Chatbot answer",
                    r.get("answer") or "[No answer returned; see status below.]", "", "### Evaluation",
                    f"Status: {r['status']}; mode: {r.get('mode', '-')}; elapsed: {r.get('wall_sec', 0):.3f}s",
                    "Legacy judge: `" + json.dumps(r.get("legacy_judge", {}), ensure_ascii=False) + "`",
                    "Guard: `" + json.dumps(r.get("guard", {}), ensure_ascii=False) + "`", "",
                    "Expected contract: `" + json.dumps({k: v for k, v in r["case"].items() if k.startswith(("expected", "must_", "should_"))}, ensure_ascii=False) + "`", "",
                    "Stage timings: `" + json.dumps(r.get("stage_timings", []), ensure_ascii=False) + "`", "",
                    f"Full trace, evidence, decision artifact and model metadata: ../results.jsonl, id {r['id']}", ""])
            (qa / name).write_text("\n".join(lines), encoding="utf-8")
    (out / "questions_answers.md").write_text("\n".join(index), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--limit-per-suite", type=int, default=0, help="Smoke-only; zero runs all cases")
    parser.add_argument("--watchdog-sec", type=float, default=30)
    args = parser.parse_args()
    sys.dont_write_bytecode = True
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    out = args.output_dir.resolve()
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Use a fresh output directory; logs are never overwritten")
    out.mkdir(parents=True, exist_ok=True)
    db = out / "isolated_canonical.sqlite"
    env = configure(db)
    before = fingerprints()
    write_json(out / "fingerprints_before.json", before)
    for path in (FAQ, KEYBOARD):
        shutil.copy2(path, out / path.name)
    with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=10) as response:
        models = json.load(response)
    available = {m["name"] for m in models.get("models", [])}
    if MODEL + ":latest" not in available or "psu-bge-m3:q8_0" not in available:
        raise SystemExit("Required local models are absent; no automatic download will be attempted")
    hardware = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,memory.used,memory.free", "--format=csv"],
                              capture_output=True, text=True, timeout=10).stdout
    faqs, keyboard = read_jsonl(FAQ), read_jsonl(KEYBOARD)
    source = {r["id"]: r for r in faqs}
    for case in keyboard:
        case["source_case"] = source.get(case.get("source_case_id"))
    suites = [("faq", faqs), ("keyboard", keyboard), ("canonical", pilot_cases())]
    tasks = [{"suite": suite, "case": case} for suite, cases in suites
             for case in (cases[:args.limit_per_suite] if args.limit_per_suite else cases)]
    write_json(out / "cases_manifest.json", tasks)
    manifest = {"started_at": datetime.now().astimezone().isoformat(), "model_enabled": True, "no_llm_baseline": False,
                "environment": env, "models": models, "hardware": hardware, "watchdog_sec": args.watchdog_sec,
                "counts": dict(Counter(t["suite"] for t in tasks)), "guard": "current runtime implementation, enforce; not shipped default shadow",
                "scope": "serial backend, empty session history, isolated synthetic canonical DB; not HTTP/load/production",
                "baseline_caveats": ["old FAQ runner bypassed input guard", "old keyboard runner used a prototype fitted on FAQ test questions",
                                     "evaluation date and warm/cache state differ", "canonical pilot owns only two synthetic records",
                                     "30-second watchdog observations are right-censored", "no network/browser latency included"]}
    write_json(out / "manifest.json", manifest)
    print("Preparing isolated pilot database and model embeddings", flush=True)
    write_json(out / "pilot_setup.json", setup_pilot(db, out))
    rows, process, conn, number = [], None, None, 0
    try:
        with (out / "results.jsonl").open("a", encoding="utf-8") as log:
            for task in tasks:
                if process is None:
                    number += 1
                    process, conn = start_worker(db, out, number)
                conn.send(task)
                result = receive_case(conn, args.watchdog_sec)
                row = {"id": task["case"]["id"], "suite": task["suite"], "case": task["case"],
                       "question": task["case"].get("observed_input", task["case"].get("question", "")),
                       "recorded_at": datetime.now().astimezone().isoformat(), "worker": number, "model_enabled": True, **result}
                rows.append(row)
                log.write(json.dumps(row, ensure_ascii=False) + "\n")
                log.flush()
                if row["status"] in {"harness_timeout", "worker_crash", "worker_error"}:
                    print(f"{row['id']}: {row['status']} ({row.get('wall_sec', 0):.2f}s); restarting owned worker", flush=True)
                    stop_worker(process, conn)
                    process = conn = None
                if len(rows) % 25 == 0 or len(rows) == len(tasks):
                    progress = {"completed": len(rows), "total": len(tasks), "last_id": row["id"], "summary": summarize(rows)}
                    write_json(out / "progress.json", progress)
                    print(f"Progress {len(rows)}/{len(tasks)} {row['id']} | strict passes {sum(bool(r.get('strict_passed')) for r in rows)}", flush=True)
    finally:
        if process is not None:
            stop_worker(process, conn)
        after = fingerprints()
        write_json(out / "fingerprints_after.json", after)
        write_json(out / "summary.json", {"finished_at": datetime.now().astimezone().isoformat(), "completed": len(rows),
            "expected": len(tasks), "worker_starts": number, "source_unchanged": before == after, "suites": summarize(rows)})
        export_markdown(rows, out)
    print(json.dumps(summarize(rows), ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
