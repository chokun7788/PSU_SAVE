#!/usr/bin/env python3
"""
RAG app skeleton for PSU Esports ChatBot.

This file is intentionally a skeleton. Replace the TODO sections with your
chosen embedding model, vector database, and LLM provider.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHUNKS_PATH = ROOT / "data" / "processed" / "all_chunks.jsonl"
SYSTEM_PROMPT_PATH = ROOT / "prompts" / "system_prompt_th.md"


def load_records(categories: set[str] | None = None) -> list[dict]:
    records = []
    with CHUNKS_PATH.open(encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if categories is None or item["category"] in categories:
                records.append(item)
    return records


def build_context(hits: list[dict]) -> str:
    blocks = []
    for i, hit in enumerate(hits, 1):
        blocks.append(
            f"[{i}] title={hit['title']}\n"
            f"category={hit['category']}\n"
            f"url={hit['url']}\n"
            f"text={hit['text']}"
        )
    return "\n\n".join(blocks)


def build_prompt(question: str, hits: list[dict]) -> list[dict]:
    system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    context = build_context(hits)
    user_prompt = f"<context>\n{context}\n</context>\n\nคำถาม: {question}"
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def retrieve(question: str, top_k: int = 5) -> list[dict]:
    # TODO:
    # 1. embed question
    # 2. query vector database
    # 3. return top_k records with text/title/url/category
    #
    # For now this function is a placeholder.
    raise NotImplementedError("Implement vector retrieval here.")


def call_llm(messages: list[dict]) -> str:
    # TODO:
    # Call your chosen LLM provider here.
    # Keep temperature low for RAG, e.g. 0 or 0.2.
    raise NotImplementedError("Implement LLM call here.")


def answer(question: str) -> str:
    hits = retrieve(question, top_k=5)
    messages = build_prompt(question, hits)
    return call_llm(messages)


if __name__ == "__main__":
    print("This is a skeleton. Start with simple_retriever_demo.py, then implement retrieval and LLM calls here.")
