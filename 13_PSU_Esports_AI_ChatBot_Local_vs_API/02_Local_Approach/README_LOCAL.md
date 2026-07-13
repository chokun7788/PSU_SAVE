# Local Approach - ทำ Chatbot โดยรัน LLM เอง

แนวทาง Local / Self-hosted คือเราดาวน์โหลด open-weight model มารันเองบนเครื่องหรือ server แล้วให้ backend เรียกผ่าน local API

ตัวอย่าง:

```text
FastAPI Backend
-> Ollama/vLLM/llama.cpp/TGI
-> Qwen/Llama/Typhoon model
```

---

## เหมาะกับใคร

เหมาะถ้า:

- มี GPU หรือเช่า GPU ได้
- ต้องการลดค่า API ระยะยาว
- ต้องการควบคุมข้อมูลมากขึ้น
- ต้องการทดลอง open-weight model
- traffic สูงพอให้คุ้มค่า server
- มีเวลาทำ benchmark และ optimize

---

## ไม่เหมาะถ้า

- ต้อง deploy ให้ทันแบบความเสี่ยงต่ำมาก
- ยังไม่เคยดูแล server/GPU
- ไม่มีเวลาวัดคุณภาพโมเดล
- ต้องการภาษาไทยดีมากทันที
- traffic ยังไม่รู้ว่าจะเยอะแค่ไหน

---

## Architecture แบบ Local

```text
User
-> Web Chat UI
-> FastAPI Backend
-> Retriever
-> Vector DB
-> Prompt Builder
-> Local LLM Server
-> Local/Open-weight Model
-> Answer + Citation
-> Logs/Evaluation
```

---

## Stack แบบเริ่มง่าย

```text
Frontend:
Streamlit หรือ Next.js

Backend:
FastAPI

LLM Serving:
Ollama

LLM:
Qwen / Llama / Typhoon

Embedding:
bge-m3 หรือ multilingual-e5

Vector DB:
Chroma

Deploy:
เครื่อง local / VPS GPU / cloud GPU
```

---

## Stack แบบ production local

```text
Frontend:
Next.js

Backend:
FastAPI

LLM Serving:
vLLM หรือ TGI

LLM:
Qwen/Llama/Typhoon ขนาด 7B-32B ตาม GPU

Embedding:
bge-m3 ผ่าน sentence-transformers หรือ embedding server

Vector DB:
Qdrant หรือ pgvector

Logs:
PostgreSQL

Monitoring:
Prometheus/Grafana + app logs

Deploy:
GPU server + Docker Compose
หรือ Kubernetes ถ้าระบบใหญ่
```

---

## ข้อดี

- ค่า inference ต่อ request อาจถูกกว่าเมื่อ traffic สูง
- คุมข้อมูลได้มากขึ้น
- ไม่ผูกกับ provider เดียว
- offline/ภายในองค์กรได้
- ทดลอง model/quantization ได้เอง

---

## ข้อเสีย

- setup ยากกว่า
- ต้องมี GPU/VRAM พอ
- latency อาจสูงถ้าเครื่องไม่แรง
- throughput จำกัดตาม hardware
- ต้องดูแล uptime, memory, disk, driver
- คุณภาพภาษาไทยต้อง benchmark จริง

---

## ความจริงสำคัญ

Local ไม่ได้แปลว่าฟรี

ยังมี cost:

- ค่า GPU server
- ค่าไฟ
- ค่า setup
- เวลาดูแล
- ค่า downtime
- ค่า monitoring
- ค่า backup

Local คุ้มเมื่อ:

```text
API cost สูงกว่า local infrastructure cost อย่างชัดเจน
และ local model ตอบได้ดีพอ
```

---

## Recommendation สำหรับ 2 เดือน

```text
Week 1-4:
ทำ RAG ระบบเดียวกับ API ให้เสร็จ

Week 5:
ต่อ local model ด้วย Ollama

Week 6:
benchmark local vs API ด้วย testset เดียวกัน

Week 7:
ทำ hybrid routing

Week 8:
deploy local ถ้าคุณภาพและ latency ผ่าน
ไม่ผ่านให้ใช้ API เป็น main แล้วเก็บ local เป็น experiment
```

