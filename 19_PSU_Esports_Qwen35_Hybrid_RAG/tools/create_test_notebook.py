from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "02_test_qwen35_hybrid_rag.ipynb"


def md(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def main() -> None:
    cells = [
        md(
            """# PSU Esports Qwen3.5 Hybrid RAG Test

Notebook นี้ใช้ทดสอบ pipeline ใหม่ในโฟลเดอร์ 19:

- unified corpus
- lexical retrieval
- optional vector retrieval
- RAG + Qwen3.5
- model comparison"""
        ),
        md("## 1. Load Project"),
        code(
            """from pathlib import Path
import sys

PROJECT_ROOT = Path(r"C:\\Users\\Chokhun\\Downloads\\Learn-LLM\\19_PSU_Esports_Qwen35_Hybrid_RAG")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.hybrid_engine import HybridRagEngine
from app.rag.ollama_client import ollama_embed

print(PROJECT_ROOT)
"""
        ),
        md("## 2. Build Unified Corpus + Lexical Index"),
        code(
            """import subprocess, sys

subprocess.run([sys.executable, str(PROJECT_ROOT / "tools" / "01_build_unified_corpus.py")], check=True)
subprocess.run([sys.executable, str(PROJECT_ROOT / "tools" / "02_build_lexical_index.py")], check=True)
"""
        ),
        md("## 3. Ask 1 Question"),
        code(
            """MODEL = "qwen3:4b"  # เปลี่ยนเป็น "qwen3.5:4b" หลังจาก ollama pull qwen3.5:4b
QUESTION = "สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย"

engine = HybridRagEngine()
result = engine.answer(
    QUESTION,
    model=MODEL,
    top_k=5,
    use_llm=True,
    timeout_sec=10,
)

print("mode:", result["mode"])
print("model:", result.get("model"))
print("elapsed:", result["elapsed_sec"])
if result.get("error"):
    print("error:", result["error"])
print("-" * 80)
print(result["answer"])
print("-" * 80)
for hit in result["hits"]:
    print(hit["id"], hit["score"], hit["category"], hit["source_kind"])
    print(hit["text_preview"])
    print()
"""
        ),
        md("## 4. Retrieval Only: ดูว่า RAG ดึงอะไรมา"),
        code(
            """QUESTION = input("พิมพ์คำถามสำหรับเช็ค retrieval: ").strip()

engine = HybridRagEngine()
result = engine.answer(QUESTION, use_llm=False, top_k=8)

print(result["answer"])
print("-" * 80)
for hit in result["hits"]:
    print(hit["id"], "score=", hit["score"], "lexical=", hit["lexical_score"], "vector=", hit["vector_score"])
    print(hit["category"], "/", hit["source_kind"], "/", hit["source_url"])
    print(hit["text_preview"])
    print()
"""
        ),
        md("## 5. Compare Models"),
        code(
            """QUESTIONS = [
    "CS2 แข่งทีมละกี่คน",
    "สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย",
    "ต่างมหาลัยเล่น VR 30 นาทีเท่าไหร่",
    "วันไหนหยุดบ้างในเดือนนี้",
    "ทำเมาส์พังต้องเสียค่าปรับไหม",
]

MODELS = ["qwen2.5:3b", "qwen3:4b"]  # เพิ่ม "qwen3.5:4b" หลังโหลดโมเดลแล้ว

engine = HybridRagEngine()
for question in QUESTIONS:
    print("=" * 100)
    print("QUESTION:", question)
    for model in MODELS:
        result = engine.answer(question, model=model, top_k=5, use_llm=True, timeout_sec=10)
        print("-" * 80)
        print("MODEL:", model, "| mode:", result["mode"], "| elapsed:", result["elapsed_sec"])
        if result.get("error"):
            print("error:", result["error"])
        print(result["answer"][:900])
"""
        ),
        md("## 6. Optional Vector Search"),
        code(
            """# ต้องรันก่อนใน PowerShell:
# ollama pull qwen3-embedding:0.6b
# py -3 tools\\03_build_vector_index_ollama.py --model qwen3-embedding:0.6b

QUESTION = "RoV ถ้ามาสายและหลุดเกมมีกฎยังไง"
EMBEDDING_MODEL = "qwen3-embedding:0.6b"
MODEL = "qwen3:4b"  # เปลี่ยนเป็น qwen3.5:4b ได้

query_embedding = ollama_embed([QUESTION], model=EMBEDDING_MODEL, timeout_sec=30)[0]
engine = HybridRagEngine()
result = engine.answer(
    QUESTION,
    model=MODEL,
    top_k=5,
    query_embedding=query_embedding,
    use_llm=True,
    timeout_sec=10,
)
print(result["answer"])
print("-" * 80)
for hit in result["hits"]:
    print(hit["id"], "score=", hit["score"], "lexical=", hit["lexical_score"], "vector=", hit["vector_score"])
"""
        ),
        md("## 7. Interactive Ask"),
        code(
            """MODEL = "qwen3:4b"  # เปลี่ยนเป็น qwen3.5:4b ได้
engine = HybridRagEngine()

while True:
    q = input("ถามอะไรดี? (exit เพื่อออก): ").strip()
    if q.lower() in {"exit", "quit", "q"}:
        break
    result = engine.answer(q, model=MODEL, top_k=5, use_llm=True, timeout_sec=10)
    print("=" * 80)
    print("mode:", result["mode"], "| elapsed:", result["elapsed_sec"])
    if result.get("error"):
        print("error:", result["error"])
    print(result["answer"])
"""
        ),
    ]

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    NOTEBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
    NOTEBOOK_PATH.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {NOTEBOOK_PATH}")


if __name__ == "__main__":
    main()
