# Cost Calculation Template

ใช้ไฟล์นี้เป็น template คิดค่าใช้จ่าย API vs Local

---

## 1. Estimate Traffic

กรอก:

```text
คำถามต่อวัน = ...
คำถามต่อเดือน = ...
ผู้ใช้พร้อมกันสูงสุด = ...
คำตอบเฉลี่ยยาวกี่ tokens = ...
context เฉลี่ยกี่ tokens = ...
```

---

## 2. API Cost

กรอก:

```text
input_tokens_per_question = ...
output_tokens_per_question = ...
questions_per_month = ...
input_price_per_1m_tokens = ...
output_price_per_1m_tokens = ...
embedding_cost_per_month = ...
rerank_cost_per_month = ...
```

สูตร:

```text
monthly_input_cost =
questions_per_month * input_tokens_per_question / 1,000,000 * input_price_per_1m_tokens

monthly_output_cost =
questions_per_month * output_tokens_per_question / 1,000,000 * output_price_per_1m_tokens

monthly_api_cost =
monthly_input_cost + monthly_output_cost + embedding_cost_per_month + rerank_cost_per_month
```

---

## 3. Local Cost

กรอก:

```text
gpu_server_cost_per_month = ...
electricity_cost_per_month = ...
storage_cost_per_month = ...
monitoring_cost_per_month = ...
maintenance_hours_per_month = ...
hourly_value = ...
```

สูตร:

```text
maintenance_cost =
maintenance_hours_per_month * hourly_value

monthly_local_cost =
gpu_server_cost_per_month
+ electricity_cost_per_month
+ storage_cost_per_month
+ monitoring_cost_per_month
+ maintenance_cost
```

---

## 4. Break-even

```text
ถ้า monthly_api_cost < monthly_local_cost:
ใช้ API ก่อน

ถ้า monthly_api_cost > monthly_local_cost มากพอ:
พิจารณา Local หรือ Hybrid
```

---

## 5. Hybrid Cost

กรอก:

```text
percent_answered_by_cache = ...
percent_answered_by_local = ...
percent_answered_by_api = ...
```

สูตร:

```text
api_questions =
questions_per_month * percent_answered_by_api

local_questions =
questions_per_month * percent_answered_by_local

cache_questions =
questions_per_month * percent_answered_by_cache
```

เป้าหมาย:

```text
ให้ cache/local รับคำถามง่าย
ให้ API รับคำถามยาก
```

---

## 6. ตัวอย่างเป้าหมาย Hybrid

```text
cache/curated facts: 30%
local model: 40%
API fallback: 30%
```

ถ้าทำได้:

- API cost ลดลง
- คุณภาพยังดี
- local ไม่ต้องรับทุกงาน

---

## 7. สิ่งที่ต้องไม่ลืม

API cost ต้องคิด:

- input/output tokens
- embedding
- reranking
- retries
- failed requests

Local cost ต้องคิด:

- GPU server
- ค่าไฟ
- maintenance
- downtime
- monitoring
- backup
- engineering time

ดังนั้น Local ไม่ได้ฟรี และ API ไม่ได้แพงเสมอไป ต้องวัดจาก traffic จริง

