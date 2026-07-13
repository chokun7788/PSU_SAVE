# 05 - เทคนิค Optimization สำหรับ Local AI

Local model จะคุ้มหรือไม่ ขึ้นกับการ optimize มาก ถ้าไม่ optimize อาจช้า แพง และตอบแย่กว่า API

---

## 1. Quantization

ลดขนาดโมเดลเพื่อลด VRAM

ตัวเลือกทั่วไป:

```text
FP16/BF16:
คุณภาพดี แต่กิน VRAM

INT8:
ประหยัดขึ้น คุณภาพมักยังดี

Q4/Q5:
ประหยัดมาก เหมาะกับเครื่องเล็ก แต่ต้องทดสอบคุณภาพ
```

แนะนำ:

```text
เริ่ม Q4/Q5 สำหรับ demo
ถ้า GPU ไหว ค่อยลอง FP16/BF16 เพื่อเทียบคุณภาพ
```

---

## 2. Context Budget

อย่าส่ง context ยาวเกินไป

ควรตั้ง:

```text
MAX_CONTEXT_TOKENS=4000-8000
TOP_K=4-8
```

ถ้าส่ง context ยาว:

- VRAM เพิ่ม
- latency เพิ่ม
- KV cache ใหญ่
- concurrent users ลด

---

## 3. Streaming

เปิด streaming response

ข้อดี:

- ผู้ใช้เห็นคำตอบทันที
- รู้สึกเร็วขึ้น
- ไม่ต้องรอจบทั้งคำตอบ

---

## 4. Batching

ถ้ามีผู้ใช้หลายคนพร้อมกัน:

- ใช้ vLLM/TGI
- เปิด continuous batching
- จำกัด max concurrent requests

Ollama เหมาะกับเริ่มต้น แต่ production traffic สูงควร benchmark กับ vLLM/TGI

---

## 5. Prompt สั้นและชัด

Local model มักไวต่อ prompt มากกว่า API รุ่นใหญ่

ควร:

- เขียน system prompt สั้น
- บอกกฎชัดเจน
- ใส่ context เป็น block ชัด
- ไม่ใช้ instruction ซับซ้อนเกิน
- บังคับตอบภาษาไทย

---

## 6. Reranking

ถ้า local LLM ไม่เก่งเท่า API การให้ context ที่แม่นขึ้นสำคัญมาก

เพิ่ม:

```text
retrieval top_k=12
reranker เลือกเหลือ top_k=5
```

ช่วยให้ local model อ่านข้อมูลที่ตรงกว่า

---

## 7. Answer Template

ให้ local model ตอบตาม format คงที่:

```text
คำตอบ:
...

รายละเอียด:
...

แหล่งข้อมูล:
...

หมายเหตุ:
ถ้าไม่พบข้อมูล ให้บอกไม่พบ
```

ช่วยลดการตอบฟุ้งและลด hallucination

---

## 8. Guardrails หลังคำตอบ

หลัง model ตอบ ควรตรวจ:

- มีคำว่าไม่พบข้อมูลเมื่อไม่มี context หรือไม่
- มี citation หรือไม่
- ตอบยาวเกินหรือไม่
- มีข้อมูลที่ไม่มีใน context หรือไม่

ถ้าผิด:

```text
retry ด้วย prompt ที่เข้มขึ้น
หรือส่งต่อ API fallback
```

---

## 9. Cache

Local ก็ต้อง cache เพราะช่วยลด latency และ GPU load

cache:

- FAQ answer
- retrieved chunks
- embeddings
- normalized question

---

## 10. Model Warmup

หลัง start server:

```text
ส่งคำถามสั้น ๆ เพื่อ warm model
```

ช่วยลด first request latency

---

## 11. Queue

ถ้ามีคนถามพร้อมกันมาก:

```text
รับ request
จัด queue
จำกัด concurrent
แจ้งผู้ใช้ว่ากำลังประมวลผล
```

ดีกว่าปล่อยให้ GPU memory เต็มแล้ว crash

---

## 12. Hybrid Fallback

Local path ควรมี fallback:

```text
ถ้า local timeout
-> API fallback

ถ้า local confidence ต่ำ
-> API fallback

ถ้า context เป็นเรื่องกฎสำคัญ
-> ใช้ curated facts หรือ API
```

---

## 13. Evaluation สำคัญมาก

ทุกครั้งที่เปลี่ยน:

- model
- quantization
- prompt
- chunking
- reranker
- context length

ต้องรัน eval เดิม

ห้ามตัดสินจากคำถาม 2-3 ข้อ

---

## Optimization Path ที่แนะนำ

```text
1. Ollama + 7B/14B
2. ทำ RAG ให้ตอบได้
3. วัด latency/accuracy
4. เพิ่ม reranker ถ้าค้นผิด
5. ปรับ prompt ให้สั้น
6. ปรับ quantization
7. ถ้า traffic สูง ย้ายไป vLLM/TGI
8. ทำ hybrid fallback
```

