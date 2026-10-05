from __future__ import annotations

from typing import Any

__all__ = [
    "AnswerQualityPipeline",
    "answer_question_pipeline",
    "answer_question_pipeline_debug",
]


def __getattr__(name: str) -> Any:
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from app.pipeline.engine import (
        AnswerQualityPipeline,
        answer_question_pipeline,
        answer_question_pipeline_debug,
    )

    values = {
        "AnswerQualityPipeline": AnswerQualityPipeline,
        "answer_question_pipeline": answer_question_pipeline,
        "answer_question_pipeline_debug": answer_question_pipeline_debug,
    }
    return values[name]
