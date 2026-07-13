# 02 - Architecture ร่วมกันของทั้งแบบ API และ Local

ไม่ว่าจะเลือก API หรือ Local โครงหลักของ AI Chatbot ควรเหมือนกันเกือบทั้งหมด

ความแตกต่างอยู่ที่ชั้น LLM:

```text
API path:
Backend -> OpenAI/Gemini/Claude/Typhoon API

Local path:
Backend -> Ollama/vLLM/llama.cpp/TGI -> Local model
```

---

## Architecture กลาง

```text
User
-> Chat UI
-> Backend API
-> Query preprocessing
-> Retriever
-> Vector database
-> Reranker/filter
-> Prompt builder
-> LLM
-> Answer post-processing
-> Citation
-> Logs
```

---

## ส่วนประกอบหลัก

### 1. Chat UI

หน้าที่:

- รับคำถาม
- แสดงคำตอบ
- แสดงแหล่งอ้างอิง
- แสดงสถานะ loading
- เก็บ feedback เช่น ถูก/ผิด

ตัวเลือก:

- Next.js
- React + Vite
- Streamlit สำหรับ demo เร็ว
- Gradio สำหรับ prototype

แนะนำ:

```text
Demo เร็ว: Streamlit
Production: Next.js + FastAPI
```

---

### 2. Backend API

หน้าที่:

- รับ request จาก frontend
- จัดการ session
- เรียก retriever
- สร้าง prompt
- เรียก LLM
- คืนคำตอบ
- เก็บ log

ตัวเลือก:

- FastAPI
- Flask
- Node.js/Express
- NestJS

แนะนำ:

```text
FastAPI
```

เพราะเหมาะกับ Python ecosystem ของ RAG, embeddings, vector database และ evaluation tools

---

### 3. Data Pipeline

หน้าที่:

- scrape เว็บ
- clean HTML
- แยกหมวดหมู่
- chunk ข้อมูล
- สร้าง metadata
- ทำ curated facts

ไฟล์ที่ควรมี:

```text
all_pages.jsonl
all_chunks.jsonl
faq_facts.jsonl
dataset_manifest.json
```

---

### 4. Embedding Layer

หน้าที่:

- แปลงข้อความเป็น vector
- ใช้ค้นหา chunk ที่มีความหมายใกล้กับคำถาม

ตัวเลือกแบบ API:

- OpenAI embeddings
- Gemini embeddings
- Cohere embeddings

ตัวเลือกแบบ local:

- bge-m3
- multilingual-e5
- sentence-transformers

---

### 5. Vector Database

หน้าที่:

- เก็บ embeddings
- ค้นหา top-k chunks
- filter ด้วย metadata เช่น category/page/source

ตัวเลือก:

- Chroma
- Qdrant
- pgvector/PostgreSQL
- Weaviate

แนะนำ:

```text
MVP: Chroma
Production: Qdrant หรือ pgvector
```

---

### 6. Reranker

หน้าที่:

- จัดอันดับ chunk ใหม่หลัง retrieval
- ลดโอกาสดึงข้อมูลผิดหมวด

ตัวเลือก:

- Cohere Rerank
- bge-reranker
- cross-encoder reranker

MVP อาจยังไม่ต้องมี แต่ถ้าบอทตอบผิดเพราะ context ผิด ควรเพิ่ม

---

### 7. Prompt Builder

หน้าที่:

- รวม system prompt
- รวมคำถามผู้ใช้
- รวม context
- ใส่กฎห้ามเดา
- บังคับรูปแบบคำตอบ

ควรมี rule:

```text
ถ้า context ไม่มีข้อมูล ให้ตอบว่าไม่พบข้อมูลในฐานข้อมูล
ห้ามเดา
ตอบภาษาไทย
อ้างอิงหมวดหรือ source เสมอ
```

---

### 8. LLM Layer

แบบ API:

- ส่ง prompt ไป API
- รับคำตอบกลับมา

แบบ Local:

- ส่ง prompt ไป local inference server
- server generate คำตอบจากโมเดลที่โหลดไว้

---

### 9. Logging และ Evaluation

ควรเก็บ:

- user question
- retrieved chunks
- model answer
- model name
- latency
- token usage
- source/category
- feedback
- error

เหตุผล:

- หา bug ง่าย
- ปรับ chunk/prompt ได้
- คำนวณ cost ได้
- รู้ว่าควรใช้ local หรือ API ต่อ

---

## Data Flow ตอนผู้ใช้ถาม

```text
1. ผู้ใช้ถาม
2. backend clean คำถาม
3. route category เบื้องต้น เช่น reservation/game/competition
4. embed คำถาม
5. vector database ค้น top-k chunks
6. filter/rerank
7. สร้าง context
8. ส่ง context + question ให้ LLM
9. LLM ตอบ
10. backend ตรวจรูปแบบคำตอบ
11. ส่งคำตอบ + citation กลับ frontend
12. บันทึก log
```

---

## หลักสำคัญ

อย่าผูกระบบกับโมเดลตัวเดียว

ควรเขียน backend ให้เปลี่ยน LLM provider ได้ง่าย เช่น:

```text
LLM_PROVIDER=openai
LLM_PROVIDER=gemini
LLM_PROVIDER=anthropic
LLM_PROVIDER=ollama
LLM_PROVIDER=vllm
```

แบบนี้ถ้าอยากสลับ API เป็น Local หรือ Local เป็น API จะไม่ต้องเขียนระบบใหม่ทั้งหมด

