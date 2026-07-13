# API Approach - ทำ Chatbot โดยใช้ LLM ผ่าน API

แนวทางนี้คือให้ระบบของเราเป็นเจ้าของข้อมูล, RAG pipeline, backend, frontend และ evaluation แต่ใช้โมเดลจากผู้ให้บริการภายนอกสำหรับการตอบ เช่น OpenAI, Google Gemini, Anthropic Claude หรือ Typhoon API

---

## เหมาะกับใคร

เหมาะมากถ้า:

- มีเวลา 2 เดือนและต้อง deploy จริง
- ยังไม่มี GPU
- ต้องการคุณภาพภาษาไทยดีตั้งแต่ต้น
- ต้องการลดงาน infra
- ต้องการระบบที่ปรับปรุงได้เร็ว
- ต้องการ benchmark ก่อนตัดสินใจลงทุน local model

---

## Architecture แบบ API

```text
User
-> Web Chat UI
-> FastAPI Backend
-> Retriever
-> Vector DB
-> Prompt Builder
-> LLM API
-> Answer + Citation
-> Logs/Evaluation
```

---

## Stack ที่แนะนำสำหรับ MVP

```text
Frontend:
Next.js หรือ Streamlit

Backend:
FastAPI

Data processing:
Python + BeautifulSoup/Playwright

Embedding:
OpenAI embeddings หรือ Gemini/Cohere embeddings

Vector DB:
Chroma สำหรับ MVP
Qdrant หรือ pgvector สำหรับ production

LLM:
โมเดล API tier เล็ก/กลางก่อน เช่น OpenAI mini, Gemini Flash, Claude Haiku, Typhoon

Evaluation:
promptfoo, Ragas, DeepEval หรือ testset แบบ custom

Deploy:
Docker + Render/Railway/Fly.io/VPS/Cloud Run
```

---

## ข้อดี

- เร็วสุดสำหรับการทำให้ใช้งานได้จริง
- คุณภาพคำตอบดีตั้งแต่แรก
- ไม่ต้องดูแล GPU
- scale ง่ายกว่า
- มี fallback หลาย provider ได้
- เหมาะกับ deadline 2 เดือน

---

## ข้อเสีย

- มีค่าใช้จ่ายตามการใช้งาน
- ต้องบริหาร token/context ให้ดี
- ต้องจัดการ API key และ privacy
- ถ้า traffic สูงมาก อาจแพงกว่า local

---

## สิ่งที่ต้องมี

อย่างน้อย:

- API key ของผู้ให้บริการโมเดล
- backend ที่ซ่อน API key
- vector database
- logging
- rate limit
- evaluation set
- prompt policy
- fallback เมื่อ API ล่มหรือ quota เต็ม

---

## แนวทางที่แนะนำในโปรเจกต์นี้

เริ่มด้วย:

```text
API-based RAG
```

แล้วเพิ่ม:

```text
cache + curated facts + cost logging
```

จากนั้นค่อยทดลอง:

```text
local model path
```

เพื่อดูว่าคุ้มย้ายบางส่วนไป local หรือไม่

