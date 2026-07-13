# 04 - Final Recommendation สำหรับโปรเจกต์ PSU Esports

ไฟล์นี้สรุปคำแนะนำแบบตัดสินใจให้เลย โดยอิงจากเงื่อนไข:

- มีเวลา 2 เดือน
- ต้องทำ AI Chatbot ให้ deploy ได้
- ต้องการคิดเรื่อง cost ระยะยาว
- อยากเปรียบเทียบ API กับ Local
- ข้อมูลหลักมาจากเว็บไซต์และระบบจอง

---

## คำแนะนำสุดท้าย

```text
อย่าเลือก API หรือ Local แบบสุดโต่งตั้งแต่แรก
ให้ทำ API เป็น production baseline
และทำ Local เป็น cost-saving experiment
จากนั้นรวมเป็น Hybrid ถ้า local ผ่านคุณภาพ
```

---

## ทำไมไม่ควร Local-only ตั้งแต่แรก

เพราะใน 2 เดือน งานที่ต้องเสร็จมีเยอะ:

- data pipeline
- chunking
- vector db
- prompt
- backend
- frontend
- evaluation
- logging
- deploy
- security
- monitoring
- cost tracking

ถ้าเพิ่มการดูแล GPU/local model ตั้งแต่วันแรก ความเสี่ยงจะสูงมาก

---

## ทำไมไม่ควร API-only ถ้าคิดระยะยาว

เพราะถ้าคนใช้เยอะมาก:

- token cost จะโตตาม usage
- ต้องมี budget guard
- ต้องมี fallback
- ต้องมี strategy ลด context/cache

ดังนั้นควรออกแบบระบบให้เปลี่ยน LLM provider ได้ตั้งแต่แรก

---

## Architecture ที่ควรทำจริง

```text
Frontend
-> Backend
-> Query Router
-> Curated Facts / Cache
-> RAG Retriever
-> Model Router
   -> Local LLM
   -> API LLM
-> Citation + Safety Check
-> Logs + Evaluation
```

---

## AI ที่ควรใช้ในแต่ละแบบ

### API Main

เริ่มด้วย:

```text
OpenAI mini-tier หรือ Gemini Flash
```

สำรอง/benchmark:

```text
Claude Haiku/Sonnet
Typhoon API
```

ใช้โมเดลใหญ่ขึ้นเฉพาะ:

- คำถามซับซ้อน
- สรุปหลายหน้า
- local/API รุ่นเล็กตอบไม่ดี
- ต้องการ quality สูงสำหรับ demo สำคัญ

---

### API Embedding

เริ่มด้วย:

```text
OpenAI embeddings หรือ Gemini/Cohere embeddings
```

เหตุผล:

- setup ง่าย
- คุณภาพดี
- ไม่ต้องดูแล embedding server

---

### Local LLM

เริ่มด้วย:

```text
Ollama + Qwen/Llama/Typhoon 7B-14B quantized
```

ถ้า production:

```text
vLLM/TGI + 14B-32B ถ้า GPU ไหว
```

---

### Local Embedding

เริ่มด้วย:

```text
bge-m3 หรือ multilingual-e5
```

---

## สิ่งที่ต้องรองรับ

### ระบบต้องรองรับ Provider Switching

เช่น:

```text
LLM_PROVIDER=openai
LLM_PROVIDER=gemini
LLM_PROVIDER=anthropic
LLM_PROVIDER=ollama
LLM_PROVIDER=vllm
```

### ระบบต้องรองรับ Hybrid Routing

```text
FAQ -> curated facts/cache
ง่าย -> local
ยาก -> API
local timeout -> API fallback
ไม่พบข้อมูล -> no-answer
```

### ระบบต้องรองรับ Evaluation

เพราะต้องพิสูจน์ว่า local คุ้มจริง ไม่ใช่แค่รันได้

---

## Final Stack ที่แนะนำ

### Month 1 Production Baseline

```text
Frontend:
Streamlit หรือ Next.js

Backend:
FastAPI

LLM:
OpenAI/Gemini API

Embedding:
OpenAI/Gemini embeddings

Vector DB:
Chroma

Logs:
SQLite/PostgreSQL

Deploy:
Render/Railway/Cloud Run/VPS
```

### Month 2 Local/Hybrid

```text
Local LLM:
Ollama -> vLLM ถ้าพร้อม

Local model:
Qwen/Llama/Typhoon 7B-14B ก่อน

Local embedding:
bge-m3/multilingual-e5

Routing:
curated facts + local + API fallback

Monitoring:
latency + cost + GPU usage
```

---

## เกณฑ์ตัดสินหลังจบ 2 เดือน

ถ้า Local:

- accuracy ใกล้ API
- hallucination ต่ำ
- latency รับได้
- server stable
- cost ถูกกว่าจริง

ให้ใช้:

```text
Hybrid with local main for simple/normal questions
```

ถ้า Local ยังไม่ผ่าน:

ให้ใช้:

```text
API main
Local demo/experiment
```

นี่ก็ยังถือว่าเป็นงาน AI ที่ดี เพราะมี baseline, evaluation, deploy และแผนลด cost ชัดเจน

