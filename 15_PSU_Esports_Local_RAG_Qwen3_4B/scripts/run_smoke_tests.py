from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


PROJECT_DIR = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_DIR.parent / "16_PSU_Esports_RAG_Experiment_Timeline"
REPORT_PATH = REPORT_DIR / "04_smoke_test_results_2026-06-29.md"
LOG_PATH = REPORT_DIR / "smoke_test_log_2026-06-29.jsonl"
NOTEBOOK_PATH = PROJECT_DIR / "notebooks" / "01_local_rag_qwen3_4b.ipynb"


@dataclass
class TestCase:
    group: str
    name: str
    question: str
    use_rules: bool = True
    use_direct: bool = True
    expected_mode: str | None = None
    expected_keywords: tuple[str, ...] = ()
    forbidden_keywords: tuple[str, ...] = ()


TEST_CASES = [
    TestCase("rule", "checkin_minutes", "เช็คอินล่วงหน้าได้กี่นาที", True, True, "rule_fast_path", ("30 นาที",)),
    TestCase("rule", "checkin_seconds", "เช็คอินล่วงหน้าได้กี่วินาที", True, True, "rule_fast_path", ("1,800", "วินาที")),
    TestCase("rule", "checkin_hours", "เช็คอินล่วงหน้าได้กี่ชั่วโมง", True, True, "rule_fast_path", ("0.5", "ชั่วโมง")),
    TestCase("rule", "ps5_games", "PS5 มีเกมอะไรบ้าง", True, True, "rule_fast_path", ("TEKKEN 8",)),
    TestCase("rule", "overview_about", "ศูนย์นี้เกี่ยวกับอะไร", True, True, "rule_fast_path", ("ศูนย์พัฒนาการเรียนรู้", "อีสปอร์ต")),
    TestCase("rule", "refund", "ยกเลิกจองได้เงินคืนไหม", True, True, "rule_fast_path", ("ไม่มีการคืนเงิน",)),
    TestCase("rule", "smoking", "สูบบุหรี่ได้ไหม", True, True, "rule_fast_path", ("ห้าม",)),
    TestCase("rule", "service_schedule", "ศูนย์เปิดถึงกี่โมง", True, True, "rule_fast_path", ("เปิด 09:00", "ปิด 16:00")),
    TestCase("rag_direct", "overview_about", "ศูนย์นี้เกี่ยวกับอะไร", False, True, "rag_direct_curated", ("ศูนย์พัฒนาการเรียนรู้", "อีสปอร์ต")),
    TestCase("rag_direct", "contact", "ติดต่อศูนย์ได้ทางไหน", False, True, "rag_direct_curated", ("Facebook", "psuesportspkt")),
    TestCase("rag_direct", "ps5_games", "PS5 มีเกมอะไรบ้าง", False, True, "rag_direct_curated", ("TEKKEN 8",), ("Nintendo Switch", "PC ได้แก่")),
    TestCase("rag_direct", "checkin_seconds_no_rule", "เช็คอินล่วงหน้าได้กี่วินาที", False, True, "rag_direct_curated", ("30 นาที",), ("เปลี่ยนแปลงเวลา", "จองล่วงหน้าผ่านระบบ")),
    TestCase("rag_direct", "service_schedule_no_rule", "ศูนย์เปิดถึงกี่โมง", False, True, "rag_direct_curated", ("เปิด 09:00", "ปิด 16:00")),
    TestCase("rag_llm", "overview_about", "ศูนย์นี้เกี่ยวกับอะไร", False, False, "rag_llm", ("อีสปอร์ต",), ("ไม่พบข้อมูล",)),
    TestCase("rag_llm", "contact", "ติดต่อศูนย์ได้ทางไหน", False, False, "rag_llm", ("Facebook",)),
    TestCase("rag_llm", "rules_summary", "กฎการใช้บริการมีอะไรบ้าง", False, False, "rag_llm", ("ห้าม",)),
    TestCase("rag_llm", "service_schedule_llm", "ศูนย์เปิดถึงกี่โมง", False, False, "rag_llm", ("09:00", "16:00"), ("根据",)),
]


def load_notebook_namespace() -> dict[str, Any]:
    os.chdir(PROJECT_DIR)
    nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    ns: dict[str, Any] = {}
    # Config, load records, Chroma, retriever, and answer functions.
    for idx in [4, 7, 11, 12, 14, 16]:
        exec("".join(nb["cells"][idx]["source"]), ns)
    ns["LOG_PATH"] = LOG_PATH
    return ns


def warm_model(ns: dict[str, Any]) -> float:
    payload = {
        "model": ns["LLM_MODEL"],
        "messages": [
            {"role": "system", "content": "Answer briefly."},
            {"role": "user", "content": "OK"},
        ],
        "stream": False,
        "keep_alive": ns["LLM_KEEP_ALIVE"],
        "options": {
            "temperature": 0.0,
            "num_ctx": 512,
            "num_predict": 8,
        },
    }
    start = time.time()
    r = requests.post(f"{ns['OLLAMA_BASE_URL']}/api/chat", json=payload, timeout=120)
    r.raise_for_status()
    return round(time.time() - start, 3)


def read_last_log() -> dict[str, Any]:
    lines = [line for line in LOG_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    return json.loads(lines[-1])


def evaluate_result(case: TestCase, answer: str, mode: str) -> tuple[str, list[str]]:
    issues: list[str] = []
    if case.expected_mode and mode != case.expected_mode:
        issues.append(f"mode expected {case.expected_mode}, got {mode}")
    for keyword in case.expected_keywords:
        if keyword not in answer:
            issues.append(f"missing keyword: {keyword}")
    for keyword in case.forbidden_keywords:
        if keyword in answer:
            issues.append(f"forbidden keyword found: {keyword}")
    return ("PASS" if not issues else "CHECK"), issues


def short_answer(answer: str, limit: int = 180) -> str:
    one_line = " ".join(answer.split())
    if len(one_line) <= limit:
        return one_line
    return one_line[:limit].rstrip() + "..."


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    if LOG_PATH.exists():
        LOG_PATH.unlink()

    ns = load_notebook_namespace()
    warmup_sec = warm_model(ns)
    answer_question = ns["answer_question"]

    rows = []
    for case in TEST_CASES:
        print(f"running {case.group}/{case.name}: {case.question}", flush=True)
        start = time.time()
        answer, hits, elapsed = answer_question(
            case.question,
            use_rules=case.use_rules,
            use_direct=case.use_direct,
        )
        wall_sec = round(time.time() - start, 3)
        log_row = read_last_log()
        mode = log_row.get("mode", "unknown")
        verdict, issues = evaluate_result(case, answer, mode)
        print(f"done {case.group}/{case.name}: {verdict} mode={mode} elapsed={elapsed}s", flush=True)
        rows.append(
            {
                "group": case.group,
                "name": case.name,
                "question": case.question,
                "mode": mode,
                "expected_mode": case.expected_mode or "-",
                "latency_sec": elapsed,
                "wall_sec": wall_sec,
                "verdict": verdict,
                "issues": "; ".join(issues),
                "retrieved_ids": [h["id"] for h in hits],
                "answer": answer,
                "answer_short": short_answer(answer),
            }
        )

    report = build_markdown_report(rows, warmup_sec, ns)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(REPORT_PATH)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


def build_markdown_report(rows: list[dict[str, Any]], warmup_sec: float, ns: dict[str, Any]) -> str:
    pass_count = sum(1 for r in rows if r["verdict"] == "PASS")
    check_count = len(rows) - pass_count
    avg_latency = sum(float(r["latency_sec"]) for r in rows) / len(rows)

    lines = [
        "# Smoke Test Results - PSU Esports Local RAG",
        "",
        "วันที่ทดสอบ: 2026-06-29",
        "",
        "ทดสอบ pipeline ล่าสุดหลังปรับ rule-based fast path, RAG direct curated fallback, และ fast model",
        "",
        "## Environment",
        "",
        f"- Project: `{PROJECT_DIR}`",
        f"- LLM model: `{ns['LLM_MODEL']}`",
        f"- Embedding model: `{ns['EMBEDDING_MODEL']}`",
        f"- TOP_K: `{ns['TOP_K']}`",
        f"- MAX_CONTEXT_CHARS: `{ns['MAX_CONTEXT_CHARS']}`",
        f"- LLM_NUM_CTX: `{ns['LLM_NUM_CTX']}`",
        f"- LLM_NUM_PREDICT: `{ns['LLM_NUM_PREDICT']}`",
        f"- Warmup latency: `{warmup_sec}` sec",
        "",
        "## Summary",
        "",
        f"- Total tests: `{len(rows)}`",
        f"- PASS: `{pass_count}`",
        f"- CHECK: `{check_count}`",
        f"- Average recorded latency: `{avg_latency:.3f}` sec",
        "",
        "## Result Table",
        "",
        "| Group | Question | Mode | Expected | Latency | Verdict | Retrieved IDs | Short Answer |",
        "|---|---|---|---|---:|---|---|---|",
    ]

    for r in rows:
        ids = ", ".join(r["retrieved_ids"])
        answer_short = r["answer_short"].replace("|", "\\|")
        lines.append(
            f"| {r['group']} | {r['question']} | `{r['mode']}` | `{r['expected_mode']}` | "
            f"{float(r['latency_sec']):.3f}s | {r['verdict']} | {ids} | {answer_short} |"
        )

    check_rows = [r for r in rows if r["verdict"] != "PASS"]
    lines += [
        "",
        "## Cases To Check",
        "",
    ]
    if not check_rows:
        lines.append("ไม่มี case ที่ต้องเช็กเพิ่มจากเกณฑ์เบื้องต้น")
    else:
        for r in check_rows:
            lines += [
                f"### {r['name']}",
                "",
                f"- Question: `{r['question']}`",
                f"- Mode: `{r['mode']}`",
                f"- Issues: {r['issues']}",
                f"- Retrieved IDs: `{', '.join(r['retrieved_ids'])}`",
                "",
                "Answer:",
                "",
                "```text",
                r["answer"],
                "```",
                "",
            ]

    lines += [
        "",
        "## Notes",
        "",
        "- `rule_fast_path` เร็วที่สุดและเหมาะกับ FAQ ซ้ำ ๆ",
        "- `rag_direct_curated` ใช้เมื่อ retrieval เจอ curated fact ชัดเจน จึงไม่ต้องเรียก LLM",
        "- `rag_llm` ใช้เมื่อคำถามต้องสรุปจาก context หรือไม่มี rule/direct answer",
        "- ถ้า retrieved IDs ถูกแต่คำตอบผิด ให้ปรับ prompt หรือเพิ่ม direct/curated rule",
        "- ถ้า retrieved IDs ผิด ให้ปรับ route category, chunk, tags, หรือ curated facts",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
