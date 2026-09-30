from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import json
import os
import statistics
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.local_models import embed_documents, warm_knowledge_models
from app.knowledge.records import text_hash
from app.knowledge.store import KnowledgeStore
from app.pipeline.engine import answer_question_pipeline_debug


def main() -> int:
    parser = argparse.ArgumentParser(description="Model-enabled, synthetic canonical lifecycle pilot. Never writes the live KB.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--skip-unit-tests", action="store_true")
    parser.add_argument("--warmup", action="store_true", help="Measure explicit model startup before user requests")
    parser.add_argument("--integration-smokes", action="store_true", help="Run focused existing safety/regression tests, not a no-LLM benchmark")
    args = parser.parse_args()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    db = out / "demo_knowledge.sqlite"
    if db.exists():
        raise SystemExit("Use a fresh output directory; existing experiment will not be overwritten")
    os.environ.update(PSU_CANONICAL_KNOWLEDGE="1", PSU_KNOWLEDGE_DB=str(db), PSU_KNOWLEDGE_ALLOW_DEMO="1",
                      PSU_LLM_MAX_CALLS="2", PSU_KNOWLEDGE_LLM_MODEL="scb10x/typhoon2.5-qwen3-4b")
    spec = importlib.util.spec_from_file_location("canonical_fixture", ROOT / "tests" / "test_canonical_knowledge.py")
    fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture)
    store = KnowledgeStore(db)
    store.initialize(allow_demo=True)
    lifecycle = []
    results = []
    try:
        hardware = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,memory.used,memory.free", "--format=csv"],
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10).stdout.decode("utf-8", errors="replace")
    except (OSError, subprocess.SubprocessError):
        hardware = "GPU inventory unavailable"
    unit_exit = None
    smoke_results = []
    if not args.skip_unit_tests:
        completed = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_canonical_knowledge.py", "-v"],
                                   cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
        (out / "unit_tests.txt").write_bytes(completed.stdout)
        unit_exit = completed.returncode
        if unit_exit:
            raise SystemExit("Focused unit tests failed; see unit_tests.txt")
    if args.integration_smokes:
        smoke_env = dict(os.environ, PSU_CANONICAL_KNOWLEDGE="0", PYTHONIOENCODING="utf-8")
        for name in ("smoke_test_runtime_input_quality_guard.py", "smoke_test_request_deadline.py", "smoke_test_answer_pipeline.py"):
            completed = subprocess.run([sys.executable, str(ROOT / "tests" / name)], cwd=ROOT, env=smoke_env,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            (out / (name + ".log")).write_bytes(completed.stdout)
            smoke_results.append({"test": name, "exit_code": completed.returncode})
        (out / "integration_smokes.json").write_text(json.dumps(smoke_results, indent=2), encoding="utf-8")
        if any(r["exit_code"] for r in smoke_results):
            raise SystemExit("Existing smoke test failed; see integration_smokes.json")

    def publish_record(record, version=0):
        row = store.save(record, actor="synthetic_editor", expected_version=version)
        store.approve(row["record_id"], row["version"], row["hash"], actor="synthetic_reviewer")
        (out / f"{row['record_id']}_v{row['version']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        lifecycle.append({"action": "save_approve", **row})

    def activate(key):
        started = time.perf_counter()
        release = store.publish(actor="synthetic_reviewer", request_key=key,
                                expected_active=store.snapshot()["active"], embed=embed_documents)
        lifecycle.append({"action": "publish", "release_id": release, "elapsed_sec": time.perf_counter() - started})
        print(f"Published {key} in {lifecycle[-1]['elapsed_sec']:.2f}s", flush=True)
        return release

    def ask(case_id, question, mode, required=(), forbidden=()):
        started = time.perf_counter()
        result = answer_question_pipeline_debug(question, experimental_allow_llm=True,
                                                 experimental_rag_fallback=True, global_timeout_sec=9)
        elapsed = time.perf_counter() - started
        checks = {"expected_mode": result.mode == mode, "required_text": all(t in result.answer for t in required),
                  "forbidden_text_absent": all(t not in result.answer for t in forbidden),
                  "validation": result.validation.ok, "under_10s": elapsed <= 10,
                  "shared_finalizer": any(t.stage == "knowledge_finalizer" for t in result.trace)}
        entry = {"case_id": case_id, "question": question, "expected_mode": mode, "checks": checks,
                 "passed": all(checks.values()), "wall_sec": elapsed, "model_enabled": True, **dataclasses.asdict(result)}
        results.append(entry)
        with (out / "cases.jsonl").open("a", encoding="utf-8") as log:
            log.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"{case_id} {result.mode} {elapsed:.2f}s {'PASS' if entry['passed'] else 'FAIL'}", flush=True)

    publish_record(fixture.game_record())
    publish_record(fixture.rule_record())
    first = activate("initial")
    warmup = warm_knowledge_models() if args.warmup else None
    (out / "startup.json").write_text(json.dumps({"warmup": warmup, "hardware": hardware}, ensure_ascii=False, indent=2), encoding="utf-8")
    if warmup:
        print(f"Model warmup: {warmup['elapsed_sec']:.2f}s; LLM ready={warmup['llm']['ok']}", flush=True)
    ask("P01", "Nebula Fields แนวไหน", "canonical_answer", ("Sandbox",))
    ask("P02", "เนบิวลาฟิลด์ เป็นเกมแนวอะไร", "canonical_answer", ("Sandbox",))
    ask("P03", "What genre is Nebula Fields?", "canonical_answer", ("Sandbox",))
    ask("P04", "Nebula Fields เล่นยังไง", "canonical_answer", ("เลือกโหมดสำรวจ", "ข้อมูลสมมติ"))
    ask("P05", "How to play Nebula Fields?", "canonical_answer", ("เลือกโหมดสำรวจ",))
    ask("P06", "Nebula Fields มีให้เล่นไหม", "canonical_no_answer", forbidden=("เลือกโหมด", "ไม่มีให้บริการ"))
    ask("P07", "Nebula Fields อยู่โซนไหน", "canonical_no_answer")
    ask("P08", "Nebula Fields เล่นยังไง และมีให้เล่นไหม", "canonical_partial", ("เลือกโหมด", "ยังไม่มีข้อมูลยืนยัน"))
    ask("P09", "กฎอาหารทดลอง คืออะไร", "canonical_answer", ("ยกเว้น", "ไม่ครอบคลุมบริเวณเครื่องเล่น"))
    ask("P10", "สรุปกฎ กฎอาหารทดลอง", "canonical_answer", ("ยกเว้น", "ไม่ครอบคลุมบริเวณเครื่องเล่น"))
    ask("P11", "Nebula Fields บน PS5 เล่นยังไง", "canonical_clarification")
    ask("P12", "Nebula Fields ราคาเท่าไร", "canonical_clarification")
    ask("P13", "มีเกมทั้งหมดกี่เกม", "canonical_clarification")
    ask("P14", "จอง Nebula Fields", "canonical_clarification")
    ask("P15", "Nebula Fields มีให้เล่นพรุ่งนี้ไหม", "canonical_clarification")
    ask("P16", "Nebula Fields ดีไหม", "canonical_clarification")
    updated = fixture.game_record()
    updated["facts"][0]["value"] = "Puzzle"
    updated["facts"][0]["source_refs"][0]["quote"] = "แนวเกม: Puzzle"
    updated["sources"][0]["snapshot_text"] = updated["sources"][0]["snapshot_text"].replace("Sandbox", "Puzzle")
    updated["sources"][0]["snapshot_sha256"] = text_hash(updated["sources"][0]["snapshot_text"])
    publish_record(updated, 1)
    second = activate("updated")
    ask("P17", "Nebula Fields แนวไหน", "canonical_answer", ("Puzzle",), ("Sandbox",))
    store.rollback(first, actor="synthetic_reviewer", expected_active=second)
    ask("P18", "Nebula Fields แนวไหน", "canonical_answer", ("Sandbox",), ("Puzzle",))
    store.rollback(second, actor="synthetic_reviewer", expected_active=first)
    store.withdraw("demo_nebula", actor="synthetic_reviewer")
    ask("P19", "Nebula Fields เล่นยังไง", "canonical_no_answer", forbidden=("เลือกโหมด",))
    activate("withdrawn")
    ask("P20", "Nebula Fields แนวไหน", "canonical_no_answer", forbidden=("Puzzle", "Sandbox"))

    times = sorted(r["wall_sec"] for r in results)
    calls = [t for r in results for t in r["trace"] if t["stage"] == "knowledge_llm_order"]
    summary = {"created_at": datetime.now().astimezone().isoformat(), "cases": len(results),
               "passed": sum(r["passed"] for r in results), "unit_test_exit_code": unit_exit, "integration_smokes": smoke_results,
               "average_sec": statistics.mean(times), "max_sec": max(times),
               "p95_sec_nearest_rank": times[max(0, __import__("math").ceil(len(times) * .95) - 1)],
               "llm_attempted": sum(bool(t["metadata"].get("model_info", {}).get("attempted")) for t in calls),
               "llm_order_accepted": sum(t["decision"] == "accepted" for t in calls),
               "models": store.snapshot()["release"]["embedding"], "lifecycle": lifecycle, "warmup": warmup, "hardware": hardware,
               "limitations": ["synthetic development cases, not independent accuracy benchmark",
                               "LLM orders approved extracts; no free paraphrasing", "not the 1600/500 regression suite",
                               "not a concurrent load test; no production rollout", "schema approval is not automatic fact verification"]}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    rows = ["# Canonical Knowledge Pilot: Model-enabled Results", "", "Synthetic test data only. Not PSU service facts.", "",
            f"Checks passed: {summary['passed']}/{summary['cases']}",
            f"Mean: {summary['average_sec']:.3f}s; max: {summary['max_sec']:.3f}s", "",
            "| Case | Expected | Actual | Time | Checks |", "|---|---|---|---:|---|"]
    for r in results:
        rows.append(f"| {r['case_id']} | {r['expected_mode']} | {r['mode']} | {r['wall_sec']:.3f}s | {'PASS' if r['passed'] else 'FAIL'} |")
    for r in results:
        rows.extend(["", f"## {r['case_id']}", "", "Question: " + r["question"], "", r["answer"], "",
                     "Checks: `" + json.dumps(r["checks"], ensure_ascii=False) + "`"])
    (out / "questions_answers.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "lifecycle"}, ensure_ascii=False, indent=2), flush=True)
    return 0 if summary["passed"] == summary["cases"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
