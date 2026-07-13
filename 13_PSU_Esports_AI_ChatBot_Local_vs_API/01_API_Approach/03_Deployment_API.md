# 03 - วิธี Deploy แบบ API

การ deploy แบบ API ง่ายกว่า Local เพราะไม่ต้องรันโมเดลเอง สิ่งที่ต้อง deploy คือ frontend, backend, vector database และ storage/logs

---

## Architecture ตอน Deploy

```text
Browser
-> Frontend
-> Backend API
-> Vector DB
-> LLM API Provider
-> Logs DB
```

---

## Option 1: Deploy ง่ายสุด

เหมาะกับ demo/MVP

```text
Frontend + Backend:
Streamlit app

Vector DB:
Chroma persistent folder

LLM:
API provider

Deploy:
Streamlit Community Cloud / Render / Railway / VPS
```

ข้อดี:

- ทำเร็ว
- เหมาะกับงานนำเสนอ
- code น้อย

ข้อเสีย:

- production scale จำกัด
- auth/logging อาจต้องทำเพิ่ม

---

## Option 2: Deploy แบบแยก Frontend/Backend

เหมาะกับงานจริงมากกว่า

```text
Frontend:
Next.js

Backend:
FastAPI

Vector DB:
Qdrant Cloud / pgvector / Chroma on persistent disk

Logs DB:
PostgreSQL

Deploy:
Vercel + Cloud Run
หรือ VPS + Docker Compose
```

ข้อดี:

- ขยายต่อได้ดี
- UI ยืดหยุ่น
- backend แยกชัดเจน
- เพิ่ม auth/admin ได้ง่าย

ข้อเสีย:

- setup มากกว่า

---

## Option 3: VPS + Docker Compose

เหมาะกับ:

- อยากคุมระบบเอง
- budget ไม่สูง
- traffic ไม่หนักมาก
- ต้องการ deploy ง่ายและเข้าใจได้

ส่วนประกอบ:

```text
nginx
frontend
backend
vector-db
postgres
```

ข้อดี:

- ราคาคงที่
- deploy เข้าใจง่าย
- backup ได้เอง

ข้อเสีย:

- ต้องดูแล server
- ต้อง setup SSL/security
- ต้อง monitor เอง

---

## Option 4: Cloud Run / Serverless Container

เหมาะกับ:

- ไม่อยากดูแล server
- traffic ขึ้นลง
- ต้องการ autoscale

ส่วนประกอบ:

```text
Frontend:
Vercel หรือ Cloud Run

Backend:
Cloud Run

Vector DB:
Qdrant Cloud / managed Postgres + pgvector

Logs:
Cloud SQL / Supabase / managed Postgres
```

ข้อดี:

- scale อัตโนมัติ
- ไม่ต้องดูแล VM
- เหมาะกับ API workload

ข้อเสีย:

- cold start
- config เยอะขึ้น
- ต้องระวัง persistent storage

---

## Environment Variables ที่ต้องมี

```env
APP_ENV=production
LLM_PROVIDER=openai
LLM_MODEL=latest-mini-model
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=latest-small-embedding-model
OPENAI_API_KEY=...
VECTOR_DB=chroma
CHROMA_PATH=/data/chroma
DATABASE_URL=postgresql://...
LOG_LEVEL=info
MAX_CONTEXT_TOKENS=6000
TOP_K=8
RATE_LIMIT_PER_MINUTE=20
```

---

## ขั้นตอน Deploy แบบ API

### Step 1: เตรียมข้อมูล

```text
scrape website
clean text
chunk
classify category
create curated facts
```

### Step 2: สร้าง Vector Index

```text
load chunks
call embedding API
save vectors to Chroma/Qdrant/pgvector
```

### Step 3: ทำ Backend

endpoint หลัก:

```text
POST /chat
GET /health
POST /feedback
GET /sources/{id}
```

### Step 4: ทำ Frontend

หน้าที่:

- กล่องถามตอบ
- แสดง answer
- แสดง sources
- ปุ่ม feedback

### Step 5: ใส่ Security

ต้องมี:

- rate limit
- CORS config
- API key ไม่ออก frontend
- input length limit
- logging แบบไม่เก็บข้อมูลอ่อนไหวเกินจำเป็น

### Step 6: Deploy

เลือก platform:

```text
ง่าย:
Render/Railway/Fly.io

คุมเอง:
VPS + Docker Compose

Cloud จริง:
Cloud Run + managed DB
```

### Step 7: Monitor

ดู:

- latency
- error rate
- token usage
- cost per day
- top questions
- no-answer rate
- bad feedback rate

---

## เทคนิค Deploy ให้ไม่พังง่าย

### 1. Health Check

ทำ endpoint:

```text
GET /health
```

ควรเช็ก:

- backend ยังทำงาน
- vector db connect ได้
- config ครบ

### 2. Timeout

ตั้ง timeout สำหรับ LLM API:

```text
10-30 วินาที
```

ถ้าเกิน ให้ตอบข้อความสุภาพ:

```text
ระบบใช้เวลานานเกินไป กรุณาลองใหม่อีกครั้ง
```

### 3. Retry

retry เฉพาะ error ชั่วคราว เช่น:

- timeout
- rate limit
- 5xx

ไม่ retry ถ้า:

- API key ผิด
- request invalid

### 4. Fallback Provider

ตัวอย่าง:

```text
primary: OpenAI mini-tier
fallback: Gemini Flash
```

### 5. Cache

cache:

- embedding ของคำถามยอดฮิต
- คำตอบ FAQ
- retrieved context บางคำถาม

---

## Checklist ก่อนเปิดใช้งานจริง

- [ ] ไม่มี API key อยู่ใน frontend
- [ ] มี rate limit
- [ ] มี health check
- [ ] มี logs
- [ ] มี backup vector data
- [ ] มี eval set
- [ ] มี fallback response เมื่อไม่พบข้อมูล
- [ ] มี prompt ห้าม hallucination
- [ ] มี cost monitor
- [ ] มีวิธี update ข้อมูลเว็บ

