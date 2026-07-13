# PSU Esports RAG Experiment Timeline

โฟลเดอร์นี้ใช้บันทึกสิ่งที่ทดลองระหว่างทำ Local RAG Chatbot สำหรับ PSU Esports Studio - Phuket

จุดประสงค์:

- เก็บ timeline ว่าทดลองอะไรไปแล้ว
- บันทึกปัญหาที่เจอและวิธีแก้
- ใช้เป็นรายงานอัปเดตงานรายวัน/รายสัปดาห์
- ใช้อธิบายตอน demo ว่าระบบพัฒนามาถึงจุดนี้ได้อย่างไร
- ใช้ย้อนดู decision ว่าทำไมเลือก rule-based, RAG direct fallback, และ fast model

---

## ไฟล์ในโฟลเดอร์

```text
README.md
01_experiment_timeline.md
02_issue_fix_result_log.md
03_next_checklist.md
```

---

## โปรเจกต์ที่เกี่ยวข้อง

โฟลเดอร์ระบบ RAG หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
```

ไฟล์สำคัญของระบบ:

```text
notebooks/01_local_rag_qwen3_4b.ipynb
data/processed/optimized_chunks.jsonl
data/curated/curated_facts.jsonl
data/curated/rule_patterns.jsonl
scripts/rule_matcher.py
optimization/latency_optimization.md
optimization/rule_based_fast_path.md
logs/chat_log.jsonl
```

---

## สถานะล่าสุด

สถานะล่าสุด ณ วันที่ 2026-06-29:

- มี Local RAG pipeline ใน notebook แล้ว
- ใช้ `qwen2.5:3b` เป็น fast default
- ยังเก็บ `qwen3:4b` เป็น quality option
- มี rule-based fast path สำหรับ FAQ ซ้ำ ๆ
- มี RAG direct curated fallback เพื่อกัน LLM ตอบว่าไม่พบข้อมูลทั้งที่ retrieve ถูก
- มี optimized chunks และ curated facts
- มี ground truth เริ่มต้นสำหรับประเมินระบบ
- มี log คำถาม/คำตอบใน `logs/chat_log.jsonl`

---

## Pipeline ล่าสุด

```text
User Question
-> Rule-based FAQ Fast Path
   -> ถ้า match: ตอบทันที
-> RAG Retrieval
   -> ถ้าเจอ curated_fact ชัดเจน: ตอบจาก retrieved text โดยตรง
-> LLM Generation
   -> ใช้ qwen2.5:3b ตอบจาก context
-> Log
   -> เก็บ mode, latency, retrieved_ids, answer
```

mode ที่ควรดูใน log:

```text
rule_fast_path       = ตอบจาก rule
rag_direct_curated   = retrieve เจอ curated fact แล้วตอบตรงจากข้อมูล
rag_llm              = ใช้ RAG + LLM เต็ม
```

