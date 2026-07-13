# Evaluation และ Monitoring Checklist

AI Chatbot จะน่าเชื่อถือได้ต้องมีการวัดผล ไม่ใช่แค่ลองถามเองไม่กี่ข้อ

---

## 1. Testset ที่ควรมี

ควรมีอย่างน้อย 50-100 คำถาม

หมวดที่ต้องครอบคลุม:

- reservation
- booking rules
- check-in/cancel
- games/devices
- competition
- training/activities
- contact
- no-answer

---

## 2. รูปแบบ testset

```json
{
  "id": "reservation_001",
  "category": "reservation",
  "question": "เช็คอินล่วงหน้าได้กี่นาที",
  "expected_keywords": ["30 นาที"],
  "must_not_include": ["เดา", "อาจจะ"],
  "expected_source_category": "reservation"
}
```

---

## 3. Metrics ที่ควรวัด

### Answer Correctness

คำตอบถูกไหม

### Context Relevance

chunk ที่ดึงมาเกี่ยวข้องไหม

### Faithfulness

คำตอบอิง context จริงไหม

### No-answer Accuracy

ถ้าไม่มีข้อมูล บอกว่าไม่พบไหม

### Citation Accuracy

แหล่งอ้างอิงตรงไหม

### Latency

ตอบเร็วไหม

### Cost

ค่าใช้จ่ายต่อคำถามเท่าไร

---

## 4. เกณฑ์ผ่าน MVP

ตัวอย่างเกณฑ์:

```text
คำถามกฎการจอง:
accuracy >= 90%

คำถามเกม/อุปกรณ์:
accuracy >= 85%

no-answer:
ไม่ควรเดา

latency:
ส่วนใหญ่ <= 10 วินาที
```

---

## 5. คำถามที่ต้องมีในชุดทดสอบ

ตัวอย่าง:

```text
เช็คอินล่วงหน้าได้กี่นาที
ถ้าไม่มาเช็คอินจะเกิดอะไรขึ้น
จอง PS5 ได้ไหม
PS5 มีเกมอะไรบ้าง
Nintendo Switch มีเกมอะไรบ้าง
VR ใช้ได้ไหม
กฎการจองมีอะไรบ้าง
มีการแข่งขันอะไรบ้าง
ติดต่อศูนย์ได้ทางไหน
เว็บมีข้อมูลค่าบริการไหม
```

คำถาม no-answer:

```text
ศูนย์มีบริการซ่อมคอมไหม
สมัครสมาชิกเสียเงินเท่าไร
มีที่จอดรถฟรีกี่คัน
เปิด 24 ชั่วโมงไหม
```

---

## 6. A/B Test โมเดล

ควรเทียบ:

```text
API model A
API model B
Local model A
Local model B
```

ใช้ testset เดียวกัน แล้วเก็บ:

- accuracy
- latency
- cost
- hallucination
- source correctness

---

## 7. Logs ที่ต้องเก็บ

```json
{
  "timestamp": "2026-06-28T10:00:00+07:00",
  "session_id": "abc",
  "question": "PS5 มีเกมอะไรบ้าง",
  "provider": "openai",
  "model": "mini-tier-model",
  "retrieved_chunk_ids": ["services_ps5_001"],
  "answer": "...",
  "latency_ms": 4200,
  "input_tokens": 3500,
  "output_tokens": 450,
  "estimated_cost": 0.0,
  "feedback": null
}
```

---

## 8. Dashboard ที่ควรมี

### Daily Usage

- จำนวนคำถาม
- จำนวนผู้ใช้
- จำนวน error
- latency เฉลี่ย

### Quality

- feedback ดี/ไม่ดี
- no-answer rate
- top failed questions
- hallucination reports

### Cost

- cost/day
- cost/provider
- cost/model
- tokens/day

### Local GPU

- VRAM usage
- GPU utilization
- tokens/sec
- queue length
- model crashes

---

## 9. Alert ที่ควรตั้ง

### API

- cost เกิน limit
- error rate สูง
- rate limit บ่อย
- latency สูง

### Local

- GPU memory ใกล้เต็ม
- model server down
- latency สูง
- queue ยาว
- crash/restart บ่อย

---

## 10. Regression Test

ทุกครั้งที่เปลี่ยน:

- prompt
- model
- embedding
- chunking
- reranker
- system prompt
- curated facts

ต้องรัน testset เดิม

เป้าหมาย:

```text
ห้ามแก้เรื่องหนึ่งแล้วทำอีกเรื่องพัง
```

---

## 11. Weekly Review

ทุกสัปดาห์ควรดู:

- คำถามที่เจอบ่อย
- คำถามที่ตอบไม่ได้
- คำถามที่ตอบผิด
- category ที่ retrieval ผิด
- cost trend
- local vs API quality

ผลลัพธ์ที่ควร update:

- curated facts
- chunks
- prompt
- testset
- routing rules

