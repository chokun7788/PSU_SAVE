# 02 - Tools Stack สำหรับแบบ API

ไฟล์นี้สรุปเครื่องมือที่ควรใช้ถ้าทำ AI Chatbot แบบ API-based RAG

---

## Stack แนะนำแบบ MVP

```text
Frontend:
Streamlit หรือ Next.js

Backend:
FastAPI

LLM:
OpenAI/Gemini/Claude/Typhoon API

Embedding:
OpenAI/Gemini/Cohere embeddings

Vector DB:
Chroma

Data processing:
Python + BeautifulSoup + Playwright

Storage:
JSONL + SQLite/PostgreSQL

Evaluation:
custom testset + promptfoo/Ragas

Deploy:
Docker + Render/Railway/Fly.io/VPS/Cloud Run
```

---

## Frontend Tools

### Streamlit

เหมาะกับ:

- demo เร็ว
- ใช้ในงานนำเสนอ
- ไม่ต้องทำ frontend ซับซ้อน

ข้อดี:

- เขียน Python ล้วนได้
- ทำ chat UI ได้เร็ว
- deploy ง่าย

ข้อเสีย:

- UI production อาจไม่ยืดหยุ่นเท่า Next.js

### Next.js

เหมาะกับ:

- production
- UI สวยและปรับแต่งได้
- แยก frontend/backend ชัดเจน

ข้อดี:

- ทำหน้าเว็บจริงได้ดี
- รองรับ auth/session ได้
- deploy ง่ายบน Vercel หรือ container

ข้อเสีย:

- ต้องรู้ JavaScript/TypeScript

แนะนำ:

```text
ถ้า deadline แคบ:
Streamlit ก่อน

ถ้าต้องทำเว็บจริง:
Next.js + FastAPI
```

---

## Backend Tools

### FastAPI

ใช้ทำ endpoint เช่น:

```text
POST /chat
GET /health
GET /sources
POST /feedback
GET /admin/logs
```

เหตุผลที่เหมาะ:

- async ได้
- เข้ากับ Python RAG ecosystem
- docs อัตโนมัติ
- deploy ด้วย Docker ง่าย

---

## Data Processing Tools

### Requests / httpx

ใช้ดึง HTML/API ธรรมดา

### BeautifulSoup

ใช้ parse HTML

### Playwright

ใช้กรณีเว็บ render ด้วย JavaScript หรือมีข้อมูลต้องรอโหลด

### Pandas

ใช้จัดข้อมูล JSONL/CSV

### tiktoken หรือ tokenizer ที่ตรงกับ provider

ใช้ประมาณจำนวน tokens เพื่อคุม cost

---

## RAG Framework

เลือกได้ 2 แบบ:

### แบบไม่ใช้ framework ใหญ่

เขียนเองด้วย:

- Python
- vector db client
- provider SDK

ข้อดี:

- เข้าใจระบบชัด
- debug ง่าย
- เหมาะกับโปรเจกต์เรียนรู้

ข้อเสีย:

- ต้องเขียน boilerplate เอง

### ใช้ framework

ตัวเลือก:

- LangChain
- LlamaIndex

ข้อดี:

- มี loader/retriever/evaluator เยอะ
- ต่อ provider ได้เร็ว

ข้อเสีย:

- abstraction เยอะ
- debug ยากขึ้นสำหรับมือใหม่

แนะนำสำหรับโปรเจกต์นี้:

```text
เริ่มแบบเขียนเองก่อน
ถ้าซับซ้อนขึ้นค่อยใช้ LlamaIndex/LangChain เฉพาะส่วนที่จำเป็น
```

---

## Vector Database

### Chroma

เหมาะกับ:

- MVP
- local development
- ใช้ง่าย
- dataset ไม่ใหญ่มาก

### Qdrant

เหมาะกับ:

- production
- filter metadata ดี
- scale ได้
- มี cloud option

### pgvector

เหมาะกับ:

- อยากใช้ PostgreSQL ตัวเดียว
- มีระบบ backend ที่ใช้ Postgres อยู่แล้ว
- query/log/metadata อยู่ฐานเดียวกัน

แนะนำ:

```text
Week 1-4:
Chroma

Week 5-8:
ถ้า deploy production จริง ให้พิจารณา Qdrant หรือ pgvector
```

---

## Logging Tools

MVP:

- SQLite
- JSONL logs

Production:

- PostgreSQL
- Supabase
- Grafana/Loki
- LangSmith หรือ OpenTelemetry

ควร log:

```text
timestamp
session_id
question
retrieved_chunk_ids
answer
model
latency_ms
tokens_input
tokens_output
cost_estimate
feedback
```

---

## Evaluation Tools

### Custom Testset

ต้องมีแน่นอน

ไฟล์ตัวอย่าง:

```text
eval/testset.jsonl
```

ควรมี fields:

```json
{
  "id": "booking_001",
  "question": "เช็คอินล่วงหน้าได้กี่นาที",
  "expected_answer_keywords": ["30 นาที"],
  "category": "reservation"
}
```

### promptfoo

เหมาะกับ:

- test prompt หลายเวอร์ชัน
- compare provider
- regression test

### Ragas / DeepEval

เหมาะกับ:

- วัด faithfulness
- วัด context relevance
- วัด answer correctness

---

## Secrets และ Environment

ห้ามใส่ API key ใน code

ใช้:

```text
.env
environment variables
secret manager ของ cloud
```

ตัวอย่าง:

```env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...
TYPHOON_API_KEY=...
```

---

## Tool Stack แบบแนะนำสุดท้าย

ถ้าอยากเร็วและ deploy ได้:

```text
Frontend: Streamlit
Backend: FastAPI
LLM: OpenAI mini-tier หรือ Gemini Flash
Embedding: OpenAI embeddings
Vector DB: Chroma
Logs: SQLite
Deploy: Docker on VPS/Render/Railway
Eval: custom testset + promptfoo
```

ถ้าจะ production ขึ้น:

```text
Frontend: Next.js
Backend: FastAPI
LLM: OpenAI/Gemini/Claude with fallback
Embedding: OpenAI/Cohere
Vector DB: Qdrant หรือ pgvector
Logs: PostgreSQL
Monitoring: Grafana/LangSmith/OpenTelemetry
Deploy: Cloud Run/Fly.io/VPS/Kubernetes
```

