# PSU Esports Qwen3.5 Hybrid RAG

โฟลเดอร์นี้เป็นชุดทดลอง pipeline ใหม่สำหรับทำ RAG/LLM ของ PSU Esports Studio - Phuket โดยแยกจากโฟลเดอร์ `18_PSU_Esports_Update_Route_Data`

เป้าหมายคือทำให้ RAG ถามตอบดีขึ้น โดยไม่เอาข้อมูลหลายชนิดไปปนกันแบบไม่มีหมวด:

1. copy data เดิมเข้ามาไว้ที่ `data/source_18`
2. normalize ทุก schema เป็น `data/unified/unified_knowledge.jsonl`
3. สร้าง lexical index สำหรับ keyword/BM25-like retrieval
4. optionally สร้าง vector index ด้วย Ollama embedding
5. ใช้ hybrid retrieval เพื่อดึง context
6. ให้ Qwen3.5-4B เรียบเรียงคำตอบจาก context เท่านั้น

## คำตอบสั้น: นี่คือการสอนโมเดลไหม

ยังไม่ใช่ fine-tune และไม่ได้ทำให้ Qwen3.5 จำข้อมูลถาวร

สิ่งที่ทำคือ RAG:

- เก็บข้อมูลจริงไว้ใน JSONL/index
- ตอน user ถาม ค่อยดึงข้อมูลที่เกี่ยวข้องขึ้นมา
- ส่ง context นั้นให้ Qwen3.5 เรียบเรียง

ข้อดีคือแก้ข้อมูลได้ง่ายกว่า fine-tune และลดโอกาส model จำข้อมูลเก่าผิดๆ

## โครงสร้าง

```text
19_PSU_Esports_Qwen35_Hybrid_RAG
├─ app/rag/
│  ├─ hybrid_engine.py
│  ├─ ollama_client.py
│  └─ text.py
├─ data/
│  ├─ source_18/
│  ├─ unified/
│  └─ index/
├─ docs/
│  ├─ 01_pipeline_design.md
│  └─ 02_model_usage_policy.md
├─ notebooks/
│  └─ 02_test_qwen35_hybrid_rag.ipynb
├─ tools/
│  ├─ 01_build_unified_corpus.py
│  ├─ 02_build_lexical_index.py
│  ├─ 03_build_vector_index_ollama.py
│  ├─ 04_ask_qwen35_hybrid.py
│  └─ 05_compare_models.py
└─ reports/
```

## วิธีรันพื้นฐาน

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\19_PSU_Esports_Qwen35_Hybrid_RAG"
py -3 tools\01_build_unified_corpus.py
py -3 tools\02_build_lexical_index.py
py -3 tools\04_ask_qwen35_hybrid.py "CS2 แข่งทีมละกี่คน" --model qwen3:4b
```

ถ้าโหลด Qwen3.5 แล้ว:

```powershell
ollama pull qwen3.5:4b
py -3 tools\04_ask_qwen35_hybrid.py "สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย" --model qwen3.5:4b
```

## Vector RAG

ถ้าต้องการ vector search ให้โหลด embedding model ก่อน:

```powershell
ollama pull qwen3-embedding:0.6b
py -3 tools\03_build_vector_index_ollama.py --model qwen3-embedding:0.6b
py -3 tools\04_ask_qwen35_hybrid.py "RoV ถ้ามาสายและหลุดเกมมีกฎยังไง" --model qwen3.5:4b --use-vector
```

ถ้ายังไม่ทำ vector index ระบบยังใช้ lexical retrieval ได้

## ใช้กี่โมเดล

ตอนใช้งานจริงขั้นต่ำใช้ 1 LLM:

- `qwen3.5:4b` เป็นตัวเรียบเรียงคำตอบ

ถ้าใช้ Vector RAG จะมีอีก 1 embedding model:

- `qwen3-embedding:0.6b` ใช้แปลงข้อความเป็นเวกเตอร์

ดังนั้น production ที่ดีมักมี 2 โมเดลคนละหน้าที่:

- LLM สำหรับตอบ
- Embedding model สำหรับค้นข้อมูล

ส่วน `qwen2.5:3b`, `qwen3:4b`, `qwen3.5:4b` ที่มีหลายตัวตอนนี้ ใช้เพื่อเทียบคุณภาพ/ความเร็วก่อน ยังไม่จำเป็นต้องลบ
