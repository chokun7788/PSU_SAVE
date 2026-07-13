# 03 - วิธี Deploy แบบ Local

การ deploy แบบ Local ต่างจาก API เพราะต้อง deploy ตัวโมเดลด้วย ไม่ใช่แค่ backend

---

## Architecture ตอน Deploy

```text
Browser
-> Frontend
-> Backend API
-> Vector DB
-> Local LLM Server
-> GPU
-> Logs DB
```

---

## Option 1: เครื่อง Local ในองค์กร

เหมาะกับ:

- demo ภายใน
- ใช้ในศูนย์/หน่วยงาน
- มีเครื่อง GPU อยู่แล้ว
- ไม่ต้องการส่งข้อมูลออกนอกระบบ

ข้อดี:

- คุมข้อมูลได้
- ค่า API เป็นศูนย์สำหรับ inference
- เหมาะกับ offline/internal

ข้อเสีย:

- uptime ขึ้นกับเครื่อง
- ต้องดูแลไฟ/เน็ต/backup
- ถ้าเครื่องดับ ระบบดับ
- scale ยาก

---

## Option 2: VPS GPU / Dedicated GPU Server

เหมาะกับ:

- deploy จริง
- traffic ปานกลาง
- ต้องการ cost คงที่
- ดูแล server ได้

ส่วนประกอบ:

```text
GPU server
Docker Compose
Nginx/Caddy
FastAPI backend
LLM server
Vector DB
PostgreSQL
Monitoring
```

ข้อดี:

- คุมระบบได้ดี
- cost คาดเดาได้
- เหมาะกับ local model production

ข้อเสีย:

- ต้องดูแล server
- ต้องทำ security
- GPU server แพงกว่า VPS ธรรมดา

---

## Option 3: Cloud GPU แบบ Serverless/On-demand

เหมาะกับ:

- traffic ไม่คงที่
- ต้องการทดลอง
- ไม่อยากผูกกับ server ตลอดเดือน

ตัวเลือกแนวนี้:

- RunPod
- Modal
- Replicate
- Hugging Face Inference Endpoints
- cloud GPU provider อื่น

ข้อดี:

- ไม่ต้องถือ GPU server ตลอดเวลา
- scale ได้
- เหมาะกับทดลอง/benchmark

ข้อเสีย:

- cold start
- config อาจซับซ้อน
- cost อาจไม่คงที่
- latency อาจสูงกว่า server ที่เปิดตลอด

---

## Option 4: Kubernetes GPU

เหมาะกับ:

- ทีม infra พร้อม
- workload ใหญ่
- หลายโมเดล
- ต้องการ autoscaling จริงจัง

ไม่แนะนำสำหรับโปรเจกต์ 2 เดือนถ้ายังไม่มีทีม infra

---

## Deploy ด้วย Ollama

เหมาะกับ MVP

flow:

```text
1. ติดตั้ง Ollama
2. pull model
3. เปิด Ollama server
4. backend เรียก http://ollama:11434
5. ใช้ Docker Compose รวมกับ backend/vector db
```

ข้อควรระวัง:

- ต้องตั้ง model keep-alive
- ต้องดู memory
- ต้องจำกัด concurrent requests
- ต้อง log latency

---

## Deploy ด้วย vLLM

เหมาะกับ production local

flow:

```text
1. เตรียม GPU server
2. ติดตั้ง NVIDIA driver/CUDA/Docker
3. run vLLM OpenAI-compatible server
4. backend เรียก endpoint เหมือน OpenAI-compatible API
5. monitor GPU memory/tokens/sec
```

ข้อดี:

- backend เปลี่ยนจาก API เป็น local ได้ง่าย
- OpenAI-compatible endpoint
- batching ดีกว่า

ข้อควรระวัง:

- ต้องเลือก dtype/quantization ให้เหมาะ
- context ยาวกิน VRAM
- concurrent users มากขึ้นต้อง tune

---

## Deploy ด้วย llama.cpp

เหมาะกับ:

- เครื่องเล็ก
- quantized GGUF
- ประหยัด resource

flow:

```text
1. ดาวน์โหลด GGUF model
2. run llama.cpp server
3. backend เรียก local endpoint
4. วัด latency และคุณภาพ
```

ข้อควรระวัง:

- quantization อาจลดคุณภาพ
- CPU-only อาจช้า
- ควร benchmark กับคำถามจริง

---

## Security สำหรับ Local Deploy

ถึงจะ local ก็ต้อง secure:

- ห้าม expose LLM server ตรงออก internet
- ให้ frontend เรียก backend เท่านั้น
- backend เป็นตัวคุม request
- ใส่ rate limit
- จำกัด input length
- ใส่ auth สำหรับ admin
- เปิด firewall เฉพาะ port ที่จำเป็น
- ทำ HTTPS

---

## Backup

ต้อง backup:

- source code
- config
- vector database
- raw/processed data
- logs สำคัญ
- curated facts
- eval set

ไม่จำเป็นต้อง backup:

- model weights ถ้าดาวน์โหลดใหม่ได้
- cache ชั่วคราว

---

## Update Model

ขั้นตอนที่ควรทำ:

```text
1. โหลดโมเดลใหม่ใน staging
2. รัน eval testset
3. เทียบกับโมเดลเก่า
4. ตรวจ hallucination
5. ทดสอบ latency
6. ถ้าผ่าน ค่อยเปลี่ยน production
7. เก็บโมเดลเก่าไว้ rollback
```

---

## Checklist ก่อนเปิด Local Production

- [ ] GPU memory เพียงพอ
- [ ] model โหลดสำเร็จหลัง reboot
- [ ] backend ต่อ LLM server ได้
- [ ] vector db persistent
- [ ] มี health check
- [ ] มี rate limit
- [ ] มี monitoring GPU
- [ ] มี API fallback หรือ fallback answer
- [ ] eval set ผ่าน
- [ ] backup ได้
- [ ] restart แล้วระบบกลับมาเอง

