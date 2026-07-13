# 03 — RAG Architecture สำหรับเว็บนี้

ไฟล์นี้อธิบายสถาปัตยกรรมที่แนะนำสำหรับ AI Chatbot ของ PSU Esports Studio - Phuket

---

## 1. ภาพรวมระบบ

```text
Website data
  -> scrape / extract
  -> clean
  -> chunk
  -> embed
  -> vector database
  -> retrieve
  -> rerank/filter
  -> prompt
  -> LLM answer
```

---

## 2. Pipeline ฝั่งเตรียมข้อมูล

### Step 1: ดึงข้อมูลเว็บ

ใช้ crawler ดึง:

- เว็บไซต์หลัก
- ระบบจอง
- หน้า policy
- หน้า services
- หน้า competition
- หน้า knowledge

ในโปรเจกต์นี้เตรียมข้อมูลไว้แล้วใน:

```text
data/processed/all_chunks.jsonl
```

### Step 2: เลือกหมวด

เริ่มจาก:

```text
reservation
services
competition
knowledge
contact
```

### Step 3: Embed

ตัวเลือก embedding:

- ง่าย/สะดวก: API embedding
- Local/free: multilingual-e5 หรือ BGE-M3

เพราะข้อมูลมีภาษาไทยและอังกฤษปนกัน ควรเลือก embedding ที่รองรับ multilingual

### Step 4: เก็บลง Vector DB

ตัวเลือก:

- เริ่มง่าย: Chroma
- ใช้จริง: Qdrant, pgvector, Weaviate

ควรเก็บ `text` + `metadata`

---

## 3. Pipeline ฝั่งถามตอบ

```text
User question
  -> normalize Thai/English
  -> optional route category
  -> embed question
  -> retrieve top-k chunks
  -> optional rerank
  -> build context
  -> call LLM
  -> answer with citation
```

---

## 4. Retrieval Strategy ที่แนะนำ

### MVP

- vector search top-k = 5
- ใช้ข้อมูลหมวด reservation/services/competition/knowledge/contact
- ตอบจาก context เท่านั้น

### Version 2

- เพิ่ม hybrid search เพราะมีชื่อเกมภาษาอังกฤษปนไทย
- เพิ่ม reranker เพื่อคัด chunk ที่ตรงที่สุด
- เพิ่ม category routing

### Version 3

- เพิ่ม news
- เพิ่ม feedback จากผู้ใช้
- เพิ่ม evaluation อัตโนมัติ
- เพิ่มระบบ update ข้อมูลเว็บเป็นรอบ ๆ

---

## 5. Hybrid Search สำคัญกับเว็บนี้

เว็บนี้มีคำแบบ:

- RoV
- VALORANT
- Counter-Strike 2
- TEKKEN 8
- Nintendo Switch
- PlayStation 5
- session
- check-in
- ชื่อกิจกรรมไทย/อังกฤษปนกัน

semantic search อย่างเดียวอาจพลาดคำเฉพาะ ควรเพิ่ม BM25 หรือ keyword search ในเวอร์ชันถัดไป

---

## 6. Context ที่ส่งให้ LLM

ควรส่ง context แบบมี source:

```text
[1] category=reservation title=... url=...
เนื้อหา...

[2] category=services title=... url=...
เนื้อหา...
```

ให้ LLM อ้างอิง `[1]`, `[2]` หรือใส่ URL ในคำตอบ

---

## 7. คำตอบต้องมี guardrails

บอทต้อง:

- ไม่เดาข้อมูลนอก context
- ไม่บอกตารางว่างแบบ real-time ถ้าไม่ได้เชื่อมระบบจริง
- ไม่รับจองแทนผู้ใช้ ถ้ายังไม่ได้เชื่อม API
- ไม่เปิดเผยข้อมูลส่วนตัว
- ถ้าถามนอกเว็บ ให้ตอบว่าไม่พบข้อมูล

---

## 8. Architecture ที่แนะนำสำหรับทำจริง

```text
Frontend:
  Streamlit หรือ Web chat

Backend:
  FastAPI

RAG:
  Retriever + prompt builder + LLM client

Storage:
  Chroma/Qdrant/pgvector

Data:
  JSONL from website

Monitoring:
  log question, retrieved chunk ids, answer, feedback
```

