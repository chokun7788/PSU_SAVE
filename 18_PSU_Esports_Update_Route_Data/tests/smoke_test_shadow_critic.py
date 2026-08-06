from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.shadow_critic import analyze_failures, review_case  # noqa: E402


def main() -> int:
    cases = [
        {
            "id": "shadow_pass_price",
            "group": "service_fee",
            "question": "ราคา PC ต่อชั่วโมงเท่าไหร่",
            "expected_category": "service_fee",
            "expected_mode_prefix": "pipeline:",
            "must_contain": ["PC", "0 บาท", "25 บาท", "70 บาท"],
            "must_not_contain": ["Local LLM"],
        },
        {
            "id": "shadow_pass_identity",
            "group": "knowledge",
            "question": "คุณเป็น AI จริงหรือเปล่า",
            "expected_category": "knowledge",
            "expected_mode_prefix": "pipeline:chatbot_identity_fast_path",
            "must_contain": ["PSU Esports Assistant"],
        },
        {
            "id": "shadow_pass_boundary",
            "group": "out_of_scope",
            "question": "สอนเขียน Python หน่อย",
            "expected_category": "general",
            "expected_behavior": "no_answer",
            "must_contain": ["ตอบได้เฉพาะข้อมูลของ PSU Esports Studio - Phuket"],
        },
    ]
    rows = []
    for case in cases:
        result = answer_question_pipeline_debug(
            case["question"],
            experimental_allow_llm=False,
            experimental_rag_fallback=False,
            global_timeout_sec=20,
        )
        critic = review_case(case, result, use_llm=False)
        row = {**critic.as_dict(), "category": case["group"]}
        rows.append(row)

    if any(row["verdict"] != "pass" for row in rows):
        raise AssertionError(rows)
    wrong_case = {
        **cases[0],
        "id": "shadow_expected_failure",
        "must_contain": ["ข้อความนี้ไม่มีอยู่จริง"],
    }
    wrong_result = answer_question_pipeline_debug(
        wrong_case["question"],
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=20,
    )
    wrong_critic = review_case(wrong_case, wrong_result, use_llm=False)
    if wrong_critic.verdict != "fail" or "missing_subanswer" not in wrong_critic.labels:
        raise AssertionError(wrong_critic)
    summary = analyze_failures(rows)
    if summary["total_cases"] != 3 or summary["pass_rate"] != 1.0:
        raise AssertionError(summary)
    if summary["llm_call_count_total"] < 0:
        raise AssertionError(summary)
    print("SHADOW CRITIC SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
