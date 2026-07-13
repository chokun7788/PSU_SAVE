# 07 — Production Pipeline: ทำให้ใช้งานจริง

เมื่อ prototype ตอบได้แล้ว ต้องทำให้เป็นระบบที่คนอื่นใช้ได้จริง

---

## 1. Architecture

```text
User
  -> Chat UI
  -> Backend API
  -> RAG Service
  -> Vector DB
  -> LLM
```

---

## 2. Backend

ใช้ FastAPI

Endpoint แนะนำ:

```text
POST /chat
POST /feedback
GET /health
POST /admin/reindex
```

Response:

```json
{
  "answer": "...",
  "sources": [
    {
      "title": "เกมบน PlayStation 5",
      "url": "https://esports.computing.psu.ac.th/",
      "category": "services"
    }
  ],
  "retrieved_chunk_ids": ["fact_ps5_games"]
}
```

---

## 3. Frontend

เริ่มง่าย:

- Streamlit

ใช้งานจริง:

- React / Next.js

UI ควรมี:

- ช่องถาม
- คำตอบ
- แหล่งอ้างอิง
- ปุ่ม copy
- ปุ่มถูก/ผิด
- ข้อความเตือนว่าไม่ใช่ระบบจอง real-time

---

## 4. Vector DB

MVP:

- Chroma local

Production:

- Qdrant
- pgvector
- Weaviate

ต้อง backup:

- dataset version
- index version
- embedding model name

---

## 5. Logging

ต้อง log:

- question
- answer
- retrieved ids
- categories
- source URLs
- latency
- token usage
- feedback

ไม่ควร log:

- ข้อมูลส่วนตัวเกินจำเป็น
- เลขบัตรประชาชน
- เบอร์ผู้ใช้ ถ้าไม่จำเป็น

---

## 6. Monitoring

ดู metric:

- จำนวนคำถามต่อวัน
- latency p95
- error rate
- no-answer rate
- thumbs down rate
- cost ต่อวัน
- top failed questions

---

## 7. Data Update

ควรมี scheduled job:

```text
scrape website
-> regenerate jsonl
-> update curated facts
-> rebuild index
-> run eval
-> deploy if pass
```

ถ้า eval fail ห้าม deploy index ใหม่

---

## 8. Security

ต้องระวัง:

- prompt injection
- user พยายามขอ system prompt
- user ถามข้อมูลส่วนตัว
- user ให้บอทรับจองแทน
- user ถามข้อมูล real-time

บอทต้องตอบในขอบเขตเท่านั้น

---

## 9. Deployment Checklist

- [ ] API รันได้
- [ ] UI ใช้งานได้
- [ ] Vector DB persistent
- [ ] มี `.env`
- [ ] ไม่ hardcode API key
- [ ] มี health check
- [ ] มี logging
- [ ] มี eval ก่อน deploy
- [ ] มี backup dataset/index
- [ ] มีคู่มือ update data

