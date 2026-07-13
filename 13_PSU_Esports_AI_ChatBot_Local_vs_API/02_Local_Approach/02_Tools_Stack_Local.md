# 02 - Tools Stack สำหรับแบบ Local

Local stack มีชั้นเครื่องมือมากกว่า API เพราะต้องดูแลทั้ง model serving, GPU, memory, container และ monitoring

---

## Stack แบบง่ายที่สุด

เหมาะกับการทดลองในเครื่อง:

```text
LLM Serving:
Ollama

LLM:
Qwen/Llama/Typhoon

Embedding:
sentence-transformers + bge-m3/multilingual-e5

Vector DB:
Chroma

Backend:
FastAPI

Frontend:
Streamlit
```

---

## Stack แบบ production local

```text
LLM Serving:
vLLM หรือ Hugging Face TGI

Model:
Qwen/Llama/Typhoon instruct model

Embedding Service:
sentence-transformers service หรือ TEI

Vector DB:
Qdrant หรือ pgvector

Backend:
FastAPI

Frontend:
Next.js

Reverse Proxy:
Nginx/Caddy

Logs:
PostgreSQL + structured logs

Monitoring:
Prometheus + Grafana

Deploy:
Docker Compose บน GPU server
```

---

## LLM Serving Tools

### Ollama

เหมาะกับ:

- เริ่มต้น
- ทดลอง local model
- setup ง่าย
- ใช้งานผ่าน local API

ข้อดี:

- ติดตั้งง่าย
- pull model ง่าย
- เหมาะกับ demo

ข้อเสีย:

- production throughput อาจไม่ดีที่สุด
- control บางอย่างน้อยกว่า vLLM

### vLLM

เหมาะกับ:

- production
- throughput สูง
- batching ดี
- OpenAI-compatible API
- GPU server จริง

ข้อดี:

- เหมาะกับ serving หลาย request
- ใช้ memory ดี
- รองรับ OpenAI-compatible endpoint

ข้อเสีย:

- setup ยากกว่า Ollama
- ต้องเข้าใจ GPU และ model config

### llama.cpp

เหมาะกับ:

- CPU/GPU แบบประหยัด
- quantized GGUF models
- เครื่องเล็ก
- edge deployment

ข้อดี:

- ใช้โมเดล quantized ได้ดี
- รันได้หลาย platform
- ไม่ต้องใช้ GPU ใหญ่มาก

ข้อเสีย:

- throughput จำกัดกว่า GPU serving
- คุณภาพขึ้นกับ quantization

### Hugging Face TGI

เหมาะกับ:

- production inference
- Hugging Face model ecosystem
- GPU deployment

ข้อดี:

- production-ready
- รองรับ metrics
- ใช้กับ Hugging Face models ได้ดี

ข้อเสีย:

- setup infra มากกว่า Ollama

---

## Embedding Tools

### sentence-transformers

เหมาะกับ:

- โหลด embedding model มารันง่าย
- ใช้ Python
- เหมาะกับ bge/e5 models

### Text Embeddings Inference

เหมาะกับ:

- ทำ embedding service แยก
- production
- batch requests

### Ollama embeddings

เหมาะกับ:

- prototype
- ไม่อยากตั้ง embedding service แยก

---

## Vector DB Tools

### Chroma

ใช้ตอนเริ่ม:

- ง่าย
- local persistent ได้
- dataset เล็ก-กลาง

### Qdrant

ใช้ตอน production:

- ทำ metadata filter ดี
- scale ได้
- มี Docker/Cloud

### pgvector

ใช้ถ้าต้องการ:

- PostgreSQL ตัวเดียว
- รวม logs/metadata/vector
- backup/restore ง่าย

---

## GPU/Infrastructure Tools

ควรใช้:

- NVIDIA driver
- CUDA runtime
- Docker with NVIDIA Container Toolkit
- nvidia-smi
- Prometheus node exporter
- GPU exporter

คำสั่งที่ต้องรู้:

```bash
nvidia-smi
docker ps
docker logs
docker compose up -d
docker compose down
```

---

## Monitoring Tools

ต้องดู:

- GPU memory
- GPU utilization
- CPU/RAM
- latency
- tokens/sec
- requests/min
- error rate
- queue length
- model reload/crash

ตัวเลือก:

- Prometheus
- Grafana
- Loki
- OpenTelemetry
- custom JSON logs

---

## Development Tools

แนะนำ:

- Python 3.11+
- uv หรือ pip
- Docker
- Git
- Makefile หรือ task runner
- pytest
- ruff

---

## Tool Stack แนะนำตามช่วงเวลา

### Week 1-4

```text
ใช้ stack เดียวกับ API:
FastAPI + Chroma + API model
```

### Week 5

```text
เพิ่ม Ollama
ทดสอบ local LLM
ทดสอบ local embeddings
```

### Week 6

```text
benchmark:
Ollama vs API
local embedding vs API embedding
```

### Week 7-8

ถ้า local ดีพอ:

```text
ย้ายเป็น vLLM/TGI
หรือคง Ollama ถ้า traffic ต่ำ
```

ถ้า local ยังไม่ดี:

```text
ใช้ API main
เก็บ local เป็น optional route
```

