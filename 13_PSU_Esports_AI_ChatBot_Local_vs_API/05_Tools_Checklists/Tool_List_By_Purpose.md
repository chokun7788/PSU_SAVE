# Tool List By Purpose

ไฟล์นี้รวมเครื่องมือที่ใช้ทำ AI Chatbot แยกตามหน้าที่ พร้อมบอกว่าเหมาะกับ API, Local หรือทั้งคู่

---

## 1. Scraping / Data Collection

| Tool | ใช้กับ | เหมาะเมื่อ |
|---|---|---|
| requests/httpx | ทั้งคู่ | เว็บเป็น HTML/API ปกติ |
| BeautifulSoup | ทั้งคู่ | parse HTML |
| Playwright | ทั้งคู่ | เว็บมี JavaScript/render client-side |
| Scrapy | ทั้งคู่ | crawl เว็บขนาดใหญ่ |

แนะนำ:

```text
เริ่มด้วย requests + BeautifulSoup
ใช้ Playwright เฉพาะหน้าที่ต้อง render JS
```

---

## 2. Data Storage

| Tool | ใช้กับ | เหมาะเมื่อ |
|---|---|---|
| JSONL | ทั้งคู่ | เก็บ raw/processed chunks |
| SQLite | ทั้งคู่ | MVP logs |
| PostgreSQL | ทั้งคู่ | production logs/users |
| Supabase | ทั้งคู่ | managed PostgreSQL ใช้ง่าย |

แนะนำ:

```text
MVP:
JSONL + SQLite

Production:
JSONL backup + PostgreSQL
```

---

## 3. Chunking / Processing

| Tool | ใช้กับ | เหมาะเมื่อ |
|---|---|---|
| Python custom chunker | ทั้งคู่ | ต้องคุม logic เอง |
| LangChain text splitters | ทั้งคู่ | ใช้ framework |
| LlamaIndex node parser | ทั้งคู่ | ใช้ LlamaIndex |
| spaCy / regex / custom rules | ทั้งคู่ | chunk ตามหัวข้อ/ประโยค |

เทคนิคที่ควรใช้:

- chunk ตามหัวข้อ
- chunk ตามหน้า/หมวด
- semantic chunking
- preserve source URL
- metadata category
- overlap เล็กน้อย

---

## 4. Embedding

### API

| Provider | เหมาะเมื่อ |
|---|---|
| OpenAI Embeddings | ใช้ง่าย คุณภาพดี |
| Gemini Embeddings | ใช้ Google stack |
| Cohere Embed | multilingual + ใช้คู่ rerank |

### Local

| Model/Tool | เหมาะเมื่อ |
|---|---|
| bge-m3 | multilingual retrieval |
| multilingual-e5 | multilingual search |
| sentence-transformers | โหลดโมเดลง่าย |
| Text Embeddings Inference | production embedding service |

---

## 5. Vector Database

| Tool | ใช้กับ | เหมาะเมื่อ |
|---|---|---|
| Chroma | ทั้งคู่ | MVP/local dev |
| Qdrant | ทั้งคู่ | production vector search |
| pgvector | ทั้งคู่ | ใช้ PostgreSQL เป็นหลัก |
| Weaviate | ทั้งคู่ | ต้องการ vector DB feature ครบ |

แนะนำ:

```text
เริ่ม:
Chroma

Production:
Qdrant หรือ pgvector
```

---

## 6. LLM Provider / Serving

### API

| Provider | เหมาะเมื่อ |
|---|---|
| OpenAI | production, quality, tooling |
| Google Gemini | cost/context/Google ecosystem |
| Anthropic Claude | response quality/reasoning |
| Typhoon | Thai-focused experiments |

### Local

| Tool | เหมาะเมื่อ |
|---|---|
| Ollama | เริ่มง่าย |
| vLLM | production throughput |
| llama.cpp | quantized/edge/CPU-friendly |
| Hugging Face TGI | production Hugging Face model serving |

---

## 7. Reranking

| Tool | ใช้กับ | เหมาะเมื่อ |
|---|---|---|
| Cohere Rerank | API | ใช้ง่าย คุณภาพดี |
| bge-reranker | Local | ลด cost และรันเอง |
| cross-encoder reranker | Local | rerank แม่นขึ้น |

ใช้เมื่อ:

- retriever ดึง chunk ผิด
- คำถามคลุมเครือ
- หลายหมวดมีคำใกล้กัน

---

## 8. Backend

| Tool | เหมาะเมื่อ |
|---|---|
| FastAPI | Python RAG production |
| Flask | app เล็ก |
| Node.js/Express | ทีมถนัด JS |
| NestJS | backend TypeScript structured |

แนะนำ:

```text
FastAPI
```

---

## 9. Frontend

| Tool | เหมาะเมื่อ |
|---|---|
| Streamlit | demo เร็ว |
| Gradio | prototype AI |
| Next.js | production web |
| React/Vite | frontend custom |

แนะนำ:

```text
MVP demo:
Streamlit

Production:
Next.js
```

---

## 10. Evaluation

| Tool | เหมาะเมื่อ |
|---|---|
| custom testset JSONL | ต้องมีทุกโปรเจกต์ |
| promptfoo | compare prompt/model/provider |
| Ragas | RAG metrics |
| DeepEval | LLM/RAG evaluation |
| LangSmith | tracing/eval ถ้าใช้ LangChain |

---

## 11. Monitoring

| Tool | เหมาะเมื่อ |
|---|---|
| JSON logs | MVP |
| PostgreSQL logs | production |
| Prometheus | metrics |
| Grafana | dashboard |
| OpenTelemetry | tracing |
| LangSmith | LLM tracing |

Local เพิ่ม:

- GPU utilization
- VRAM usage
- model load time
- tokens/sec

API เพิ่ม:

- token usage
- estimated cost
- provider error rate

---

## 12. Deployment

### API

| Platform | เหมาะเมื่อ |
|---|---|
| Render/Railway/Fly.io | MVP container |
| Vercel | Next.js frontend |
| Cloud Run | managed container |
| VPS + Docker Compose | คุม cost/ระบบเอง |

### Local

| Platform | เหมาะเมื่อ |
|---|---|
| Local GPU machine | demo/internal |
| GPU VPS | production local |
| RunPod/Modal/Replicate | on-demand GPU |
| Kubernetes GPU | workload ใหญ่ |

---

## Stack ที่แนะนำจริง

### API MVP

```text
Streamlit
FastAPI
OpenAI/Gemini API
OpenAI/Gemini embeddings
Chroma
SQLite logs
Docker
```

### API Production

```text
Next.js
FastAPI
OpenAI/Gemini/Claude with fallback
Qdrant/pgvector
PostgreSQL
Docker
Cloud Run/VPS
```

### Local MVP

```text
Streamlit
FastAPI
Ollama
Qwen/Llama/Typhoon
bge-m3
Chroma
```

### Local Production

```text
Next.js
FastAPI
vLLM/TGI
Qwen/Llama/Typhoon
bge-m3 service
Qdrant
PostgreSQL
GPU server
Prometheus/Grafana
```

