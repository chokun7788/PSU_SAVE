from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "02_test_final_pipeline.ipynb"
MARKER = "mixed_rag_llm_modes_v1"


def markdown_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {"codex_marker": MARKER},
        "source": source.splitlines(keepends=True),
    }


def code_cell(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"codex_marker": MARKER},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def main() -> None:
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    notebook["cells"] = [
        cell
        for cell in notebook.get("cells", [])
        if cell.get("metadata", {}).get("codex_marker") != MARKER
    ]

    new_cells = [
        markdown_cell(
            """## 12. Manual Test แบบเลือกโหมด: Rulebase / RAG / RAG+LLM / Auto

ส่วนนี้เอาไว้พิมพ์คำถามเองและเลือกวิธีตอบได้โดยตรง:

- `mode="rulebase"` ใช้ pipeline เดิมที่เร็วและคุมคำตอบได้ดี เหมาะกับราคา เวลา กฎตรงๆ และ fact card
- `mode="rag"` ดึงข้อมูลจาก JSONL/curated/competition fact cards แล้วตอบแบบไม่เรียก LLM
- `mode="rag_llm"` ดึงข้อมูลก่อน แล้วให้ Ollama เรียบเรียงจาก context เท่านั้น เหมาะกับคำถามที่ต้องสรุป/อธิบายหลายส่วน
- `mode="auto"` ให้ระบบเลือกเอง โดย exact fact จะตอบด้วย rulebase/fact card ก่อน ส่วนคำถามที่ต้องสรุปจะลอง RAG+LLM

ค่า default ใช้ `qwen2.5:3b` เพื่อให้พยายามจบในเวลาประมาณไม่เกิน 10 วินาที ถ้าอยากลองคุณภาพที่อาจดีขึ้นให้เปลี่ยน `MODEL = "qwen3:4b"`"""
        ),
        code_cell(
            """from pathlib import Path
import sys

PROJECT_ROOT = Path(r"C:\\Users\\Chokhun\\Downloads\\Learn-LLM\\18_PSU_Esports_Update_Route_Data")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.runtime.mixed_mode_tester import (
    ask_mode,
    compare_modes,
    interactive_ask,
    print_mode_result,
    retrieve_context,
    route_preview,
)

MODEL = "qwen2.5:3b"   # เปลี่ยนเป็น "qwen3:4b" ได้ ถ้าอยากลองโมเดลที่ใหญ่ขึ้น
LLM_TIMEOUT_SEC = 8.0  # รวมกับ retrieval แล้วควรอยู่แถวๆ ไม่เกิน 10 วิ ถ้าเครื่องหน่วงให้เพิ่มเป็น 10-12
TOP_K = 5

print("Loaded mixed mode tester")
print("MODEL =", MODEL)
print("LLM_TIMEOUT_SEC =", LLM_TIMEOUT_SEC)
"""
        ),
        markdown_cell(
            """### 12.1 ถาม 1 คำถามแบบกำหนดโหมดเอง

แก้ `QUESTION` และ `MODE` ได้เลย:

- `MODE = "auto"`
- `MODE = "rulebase"`
- `MODE = "rag"`
- `MODE = "rag_llm"`"""
        ),
        code_cell(
            """QUESTION = "สมาชิกในทีม ROV ต้องมีกี่คน"
MODE = "auto"

result = ask_mode(
    QUESTION,
    mode=MODE,
    model=MODEL,
    limit=TOP_K,
    llm_timeout_sec=LLM_TIMEOUT_SEC,
)

print_mode_result(result, show_context=True, show_trace=True)
"""
        ),
        markdown_cell(
            """### 12.2 พิมพ์คำถามเอง แล้วเทียบทุกโหมด

Cell นี้จะถามคำถามเดียวกัน 4 แบบ เพื่อดูว่า rulebase, RAG, RAG+LLM และ auto ต่างกันยังไง"""
        ),
        code_cell(
            """QUESTION = input("พิมพ์คำถามที่อยากทดสอบ: ").strip()

results = compare_modes(
    QUESTION,
    modes=("rulebase", "rag", "rag_llm", "auto"),
    model=MODEL,
    limit=TOP_K,
    llm_timeout_sec=LLM_TIMEOUT_SEC,
)

for item in results:
    print_mode_result(item, show_context=False, show_trace=True)
"""
        ),
        markdown_cell(
            """### 12.3 ดูแค่ Route + Context ที่ RAG ดึงมา

ใช้ cell นี้เวลาอยากเช็คว่า “ตอบไม่ได้เพราะไม่มี data” หรือ “มี data แต่ retriever ดึงไม่ตรง”"""
        ),
        code_cell(
            """QUESTION = input("พิมพ์คำถามสำหรับดู route/context: ").strip()

print("Route Preview")
display(route_preview(QUESTION))

print("Retrieved Context")
ctx = retrieve_context(QUESTION, limit=TOP_K)
display(ctx)
"""
        ),
        markdown_cell(
            """### 12.4 Interactive Loop สำหรับถามเรื่อยๆ

คำสั่งในช่อง input:

- `/mode auto`
- `/mode rulebase`
- `/mode rag`
- `/mode rag_llm`
- `exit` เพื่อออก"""
        ),
        code_cell(
            """interactive_ask(
    default_mode="auto",
    model=MODEL,
    limit=TOP_K,
    llm_timeout_sec=LLM_TIMEOUT_SEC,
)
"""
        ),
    ]

    notebook["cells"].extend(new_cells)
    NOTEBOOK_PATH.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Updated {NOTEBOOK_PATH}")
    print(f"Added {len(new_cells)} cells with marker {MARKER}")


if __name__ == "__main__":
    main()
