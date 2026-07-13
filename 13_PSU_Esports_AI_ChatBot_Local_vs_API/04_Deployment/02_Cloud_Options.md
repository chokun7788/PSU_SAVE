# 02 - Cloud Options

ไฟล์นี้สรุปตัวเลือก cloud/deploy สำหรับแบบ API และ Local

---

## แบบ API

### 1. Render / Railway / Fly.io

เหมาะกับ:

- MVP
- deploy ง่าย
- backend container
- budget เริ่มต้นไม่สูง

ใช้กับ:

```text
FastAPI backend
Streamlit app
small database
```

ข้อควรระวัง:

- persistent disk ต้องตรวจให้ดี
- free/low tier อาจ sleep
- ต้องดู limit ของแต่ละ platform

---

### 2. Vercel + Managed Backend

เหมาะกับ:

- Next.js frontend
- frontend production
- backend แยกไป Cloud Run/Fly/Render

โครง:

```text
Vercel -> frontend
Cloud Run/Render -> FastAPI backend
Qdrant Cloud/Supabase -> database/vector
LLM API -> provider
```

---

### 3. Google Cloud Run

เหมาะกับ:

- containerized backend
- autoscaling
- ไม่อยากดูแล VM

ใช้คู่กับ:

- Cloud SQL
- managed vector DB
- Secret Manager

---

### 4. VPS ธรรมดา

เหมาะกับ:

- budget คงที่
- deploy ด้วย Docker Compose
- traffic ไม่หนักมาก

ต้องดูแล:

- SSL
- firewall
- backup
- monitoring
- OS updates

---

## แบบ Local

### 1. Local Machine / On-premise

เหมาะกับ:

- demo ภายใน
- ข้อมูลไม่อยากออกนอกเครื่อง
- มี GPU อยู่แล้ว

ไม่เหมาะถ้า:

- ต้อง uptime สูง
- เครื่องอยู่หลังเน็ตไม่เสถียร
- ไม่มีคนดูแล

---

### 2. GPU VPS / Dedicated GPU Server

เหมาะกับ:

- production local
- ต้องรันโมเดลตลอดเวลา
- traffic สม่ำเสมอ

ต้องมี:

- NVIDIA driver
- Docker + NVIDIA runtime
- monitoring GPU
- backup
- security

---

### 3. RunPod / Modal / Replicate / Hugging Face Endpoints

เหมาะกับ:

- ทดลอง GPU
- serverless/on-demand
- benchmark
- ไม่อยากถือ server ตลอดเดือน

ข้อควรระวัง:

- cold start
- model load time
- pricing ตาม usage
- endpoint security

---

### 4. Kubernetes GPU

เหมาะกับ:

- workload ใหญ่
- มีทีม infra
- หลายโมเดล
- ต้อง autoscale จริงจัง

ไม่แนะนำเป็น baseline สำหรับงาน 2 เดือนถ้าเริ่มจากศูนย์

---

## ตัวเลือกที่แนะนำตามเป้าหมาย

### Demo เร็ว

```text
Streamlit + API model + Chroma
Deploy บน Render/Railway/Streamlit Cloud
```

### Production MVP

```text
Next.js + FastAPI
Qdrant/pgvector
LLM API
Deploy บน Vercel + Cloud Run หรือ VPS
```

### Local Demo

```text
FastAPI + Ollama + Chroma
Deploy บนเครื่อง GPU หรือ GPU VPS
```

### Local Production

```text
Next.js + FastAPI
vLLM/TGI
Qdrant/Postgres
GPU server + Docker Compose
```

### Hybrid

```text
API production
+ local model service
+ routing layer
+ fallback
```

---

## คำแนะนำสำหรับโปรเจกต์นี้

ถ้าต้องส่งใน 2 เดือน:

```text
Deploy API version ก่อน
```

แล้วทำ:

```text
Local GPU deployment เป็น experiment/optional path
```

ถ้า local benchmark ผ่าน:

```text
ค่อยเปิด route บางคำถามไป local
```

