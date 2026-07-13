# 03 - Roadmap 2 เดือนสำหรับทำทั้ง API และ Local

เป้าหมายคือทำให้ได้ระบบที่ deploy ได้จริง โดยไม่เสี่ยงจนเกินไป

---

## กลยุทธ์หลัก

```text
เดือนที่ 1:
สร้างระบบ RAG ที่ใช้งานได้ด้วย API

เดือนที่ 2:
เพิ่ม local model benchmark และ hybrid routing
```

เหตุผล:

- ระบบ RAG/Data/UI ใช้ร่วมกันทั้ง API และ Local
- API ทำให้มี baseline คุณภาพสูง
- Local เอามาเทียบกับ baseline
- ถ้า Local ไม่ผ่าน ยังมีระบบ API ที่ deploy ได้

---

## Week 1 - Data Foundation

งาน:

- ตรวจข้อมูลจากเว็บ
- clean text
- chunk
- classify category
- ทำ curated facts
- เตรียม testset

ผลลัพธ์:

```text
all_pages.jsonl
all_chunks.jsonl
faq_facts.jsonl
eval/testset.jsonl
```

ต้องทำให้ได้:

- ข้อมูลกฎการจองชัด
- ข้อมูลเกมแยกตาม device
- ข้อมูลการแข่งขันแยกหมวด
- มี metadata/source/category

---

## Week 2 - API RAG MVP

งาน:

- embedding chunks
- สร้าง vector db
- ทำ retriever
- ทำ prompt
- เรียก LLM API
- ตอบพร้อม citation

ผลลัพธ์:

```text
ถามตอบผ่าน command line หรือ simple web UI ได้
```

---

## Week 3 - Backend + Chat UI

งาน:

- FastAPI backend
- Streamlit หรือ Next.js UI
- endpoint /chat
- feedback button
- source display
- error handling

ผลลัพธ์:

```text
มีหน้า chat ให้คนลองใช้
```

---

## Week 4 - Evaluation + API Deploy

งาน:

- รัน testset
- ปรับ chunking/prompt
- เพิ่ม curated facts
- deploy API version
- เก็บ logs

ผลลัพธ์:

```text
API-based chatbot MVP ที่ deploy ได้
```

Milestone:

```text
ระบบควร demo ได้แล้ว
```

---

## Week 5 - Local Model Prototype

งาน:

- ติดตั้ง Ollama
- ลอง Qwen/Llama/Typhoon
- ลอง local embedding เช่น bge-m3
- ต่อ backend ให้เปลี่ยน provider ได้

ผลลัพธ์:

```text
ใช้ RAG pipeline เดิม แต่ LLM เป็น local
```

---

## Week 6 - Benchmark Local vs API

งาน:

- รัน testset เดียวกัน
- เทียบ accuracy
- เทียบ hallucination
- เทียบ latency
- เทียบ memory
- เทียบ cost

ผลลัพธ์:

```text
รายงานว่า local model ใช้จริงได้แค่ไหน
```

เกณฑ์ผ่าน:

- ตอบคำถามกฎถูก
- ไม่เดาเมื่อไม่มีข้อมูล
- latency พอรับได้
- crash น้อย

---

## Week 7 - Hybrid Routing

งาน:

- route FAQ ไป curated facts/cache
- route คำถามง่ายไป local
- route คำถามยากไป API
- ทำ fallback
- เพิ่ม monitoring

ผลลัพธ์:

```text
ระบบ Hybrid ที่ลด cost ได้บางส่วน
```

---

## Week 8 - Production Hardening

งาน:

- Docker Compose
- environment variables
- SSL/reverse proxy
- rate limit
- backup
- monitoring
- final evaluation
- documentation

ผลลัพธ์:

```text
Deploy-ready chatbot
+ API path
+ Local path
+ comparison report
```

---

## Milestone ที่ควรมี

### สิ้น Week 2

```text
RAG ตอบได้ใน local dev
```

### สิ้น Week 4

```text
API chatbot deploy ได้
```

### สิ้น Week 6

```text
รู้แล้วว่า local model คุ้มไหม
```

### สิ้น Week 8

```text
ระบบพร้อมนำเสนอ/ใช้งานจริง
```

---

## ถ้าเวลาหลุด

ให้ตัดตามลำดับนี้:

1. ตัด Kubernetes
2. ตัด vLLM production
3. ใช้ Ollama เป็น local demo
4. ใช้ API เป็น production
5. เก็บ hybrid เป็น roadmap

ห้ามตัด:

- evaluation
- citation
- curated facts
- logging
- no-hallucination rule

