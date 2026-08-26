from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True)
class WarmupResult:
    ok: bool
    elapsed_sec: float
    warmed: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    timings: dict[str, float] = field(default_factory=dict)


def _truthy(value: str | None, *, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def pipeline_warmup_enabled() -> bool:
    return _truthy(os.getenv("PSU_PIPELINE_WARMUP"), default=True)


def pipeline_reranker_warmup_enabled() -> bool:
    """Load the expensive document reranker before accepting user work."""
    return _truthy(os.getenv("PSU_PIPELINE_WARMUP_RERANKER"), default=False)


def pipeline_embedding_warmup_enabled() -> bool:
    explicit = os.getenv("PSU_PIPELINE_WARMUP_EMBEDDING")
    if explicit is not None:
        return _truthy(explicit, default=False)
    return _truthy(os.getenv("PSU_SEMANTIC_RETRIEVAL"), default=False)


def warm_pipeline_caches(*, include_probe_queries: bool = True) -> WarmupResult:
    """Warm deterministic caches and optionally the document reranker."""
    started = time.perf_counter()
    warmed: list[str] = []
    errors: list[str] = []
    timings: dict[str, float] = {}

    def run_step(name: str, fn: Callable[[], object]) -> None:
        step_started = time.perf_counter()
        try:
            fn()
            warmed.append(name)
        except Exception as exc:  # pragma: no cover - warmup must not block startup.
            errors.append(f"{name}: {exc!r}")
        finally:
            timings[name] = round(time.perf_counter() - step_started, 4)

    def warm_game_title_aliases() -> None:
        from app.pipeline import game_title_correction as titles

        titles.game_alias_entries()
        titles._broad_compacts()
        titles._specific_alias_needles()
        titles._delete_index()
        titles._thai_alias_prefixes()
        titles._compact("TEKKEN 8")
        titles._compact("Mario Kart 8 Deluxe")
        titles._compact("อุปกรณ์ไหนเกมเยอะสุด")

    def warm_structured_tools() -> None:
        from app.pipeline import structured_tools as tools

        tools._equipment_rows()
        tools._member_rows()
        tools._game_rows()
        tools._game_alias_entries()
        tools._control_rows()
        tools._games_by_zone()

    def warm_routing_data() -> None:
        from app.pipeline.routing_policy import _load_matrix
        from app.pipeline.semantic_intent import _load_catalog

        _load_matrix()
        _load_catalog()

    def warm_retrieval_data() -> None:
        from app.pipeline.retrieval import load_competition_fact_cards, load_curated_rows
        from app.pipeline.vector_retrieval import _game_alias_index, load_vector_index

        load_curated_rows()
        load_competition_fact_cards()
        load_vector_index()
        _game_alias_index()

    def warm_probe_queries() -> None:
        from app.pipeline.engine import get_pipeline

        pipeline = get_pipeline()
        for question in (
            "Tekken 8",
            "TEKKEN 8 มีปุ่มอะไรบ้าง",
            "อุปกรณ์ไหนเกมเยอะสุด",
            "สมาชิกทีมมีใครบ้าง",
            "วันจันทร์เปิดให้เล่นกี่โมง ปิดกี่โมง",
            "PC Zone มีอุปกรณ์อะไรบ้าง",
            "ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท",
            "ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่",
            "ถ้าเล่น Tekken 8 กับ Mario มีปุ่มอะไรบ้าง",
            "อาชีพที่เกี่ยวข้องกับกีฬาอีสปอร์ตมีอะไรบ้าง",
            "ประวัติอีสปอร์ตเริ่มต้นอย่างไร",
            "ข่าวกิจกรรมล่าสุดของ PSU Esports Studio มีอะไรบ้าง",
        ):
            pipeline.answer(
                question,
                experimental_rag_fallback=False,
                experimental_allow_llm=False,
            )

    def warm_document_reranker() -> None:
        from app.pipeline.document_reranker import _load_model, document_reranker_enabled

        if not document_reranker_enabled():
            return
        _load_model()

    def warm_semantic_embedding() -> None:
        from app.pipeline.semantic_embeddings import warm_semantic_embedding_model

        warm_semantic_embedding_model()

    run_step("game_title_aliases", warm_game_title_aliases)
    run_step("structured_tools", warm_structured_tools)
    run_step("routing_data", warm_routing_data)
    run_step("retrieval_data", warm_retrieval_data)
    if include_probe_queries:
        run_step("probe_queries", warm_probe_queries)
    if pipeline_embedding_warmup_enabled():
        run_step("semantic_embedding", warm_semantic_embedding)
    if pipeline_reranker_warmup_enabled():
        run_step("document_reranker", warm_document_reranker)

    return WarmupResult(
        ok=not errors,
        elapsed_sec=round(time.perf_counter() - started, 4),
        warmed=tuple(warmed),
        errors=tuple(errors),
        timings=timings,
    )
