from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def main() -> int:
    # High-confidence scope decisions are safe outcomes. Experimental RAG/LLM
    # must not replace them with a loosely related generated answer.
    cases = (
        "เครื่องไหนดีที่สุด",
        "มีอะไรแนะนำไหม",
        "สรุปคือทำยังไง",
        "เกม Valorant Mobile มีไหม",
        "ขอเบอร์โทรส่วนตัวเจ้าหน้าที่",
    )
    for question in cases:
        result = answer_question_pipeline_debug(
            question,
            locale="th",
            experimental_allow_llm=True,
            experimental_rag_fallback=True,
            global_timeout_sec=20.0,
        )
        assert result.route.category == "no_answer", (question, result.route.category, result.mode)
        assert "experimental_rag" not in result.mode, (question, result.mode)
        assert result.elapsed < 4.0, (question, result.elapsed, result.mode)
    print("OK high-confidence scope guards bypass experimental RAG/LLM fallback")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
