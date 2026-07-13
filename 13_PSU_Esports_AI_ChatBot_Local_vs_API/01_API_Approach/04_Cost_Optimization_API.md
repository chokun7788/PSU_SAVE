# 04 - เทคนิคคุม Cost สำหรับแบบ API

การใช้ API ไม่จำเป็นต้องแพง ถ้าคุม pipeline ดี จุดที่ทำให้แพงมักไม่ใช่แค่ราคาโมเดล แต่คือการส่ง context เยอะเกิน, ไม่ cache, และให้ LLM ตอบทุกอย่างแม้คำถามง่าย

---

## Cost มาจากอะไร

โดยทั่วไป:

```text
cost = input tokens + output tokens + embedding + reranking + infra
```

สำหรับ RAG:

```text
input tokens = system prompt + context chunks + user question
output tokens = คำตอบที่ LLM generate
```

---

## เป้าหมายการคุม Cost

1. ส่ง context เท่าที่จำเป็น
2. ลดคำตอบยาวเกิน
3. cache คำถามยอดฮิต
4. ตอบ FAQ จาก curated facts
5. ใช้โมเดลเล็กก่อน
6. ใช้โมเดลใหญ่เฉพาะกรณียาก
7. monitor cost ต่อวัน

---

## เทคนิคที่ควรทำ

### 1. Curated Facts First

ข้อมูลที่เป็นกฎแน่นอนควรตอบจาก structured facts ก่อน เช่น:

- เช็คอินล่วงหน้าได้กี่นาที
- ยกเลิกได้ไหม
- จองได้กี่ชั่วโมง
- มีเกม PS5 อะไรบ้าง
- ช่องทางติดต่อคืออะไร

ถ้าตอบจาก facts ได้:

```text
ไม่ต้องเรียก LLM
หรือเรียก LLM แบบ context สั้นมากเพื่อเรียบเรียงภาษา
```

---

### 2. Top-k ที่เหมาะสม

อย่าดึง context เยอะเกิน

เริ่ม:

```text
TOP_K=6 หรือ 8
```

ถ้าคำตอบพลาดเพราะ context ไม่พอ ค่อยเพิ่ม

---

### 3. Metadata Filter

ถ้ารู้หมวดคำถาม ให้ filter ก่อนค้น:

```text
คำถามมีคำว่า จอง/เช็คอิน/ยกเลิก -> category=reservation
คำถามมีคำว่า PS5/Switch/VR/เกม -> category=services
คำถามมีคำว่า แข่งขัน/ทัวร์นาเมนต์ -> category=competition
```

ช่วยลด context ผิดและลด token

---

### 4. Context Compression

ก่อนส่งให้ LLM:

- ลบ boilerplate
- ลบ menu/footer
- ใช้ chunk ที่เกี่ยวเท่านั้น
- จำกัดจำนวนตัวอักษรต่อ chunk
- รวม chunk ซ้ำ

---

### 5. Output Limit

ตั้งค่า max output tokens:

```text
คำตอบทั่วไป: 400-800 tokens
คำตอบละเอียด: 1200 tokens
```

ไม่ควรปล่อยให้โมเดลตอบยาวทุกครั้ง

---

### 6. Model Tiering

ใช้โมเดลหลายระดับ:

```text
FAQ/simple:
curated facts/cache

normal RAG:
mini/flash/haiku tier

hard question:
flagship/pro/sonnet tier
```

---

### 7. Cache

Cache ได้หลายระดับ:

```text
question -> answer
question -> retrieved chunks
text -> embedding
URL -> cleaned content
```

คำถามที่ควร cache:

- จองยังไง
- เช็คอินยังไง
- เปิดกี่โมง
- มีกฎอะไรบ้าง
- มีเกมอะไรบ้าง

---

### 8. Batch Embedding

ตอนสร้าง index:

- batch หลาย chunks ต่อ request
- ไม่ embed ข้อมูลซ้ำ
- เก็บ hash ของ chunk
- ถ้า chunk ไม่เปลี่ยน ไม่ต้อง embed ใหม่

---

### 9. Daily Budget Guard

ตั้ง budget ต่อวัน:

```text
MAX_DAILY_LLM_COST=...
MAX_DAILY_REQUESTS=...
```

ถ้าเกิน:

- ตอบจาก cache/facts
- ลด model tier
- ปิดคำตอบยาว
- แจ้ง admin

---

## ตัวอย่าง Cost Dashboard ที่ควรมี

แสดง:

```text
จำนวนคำถามวันนี้
จำนวน tokens input
จำนวน tokens output
ค่าใช้จ่ายประมาณการ
โมเดลที่ใช้บ่อย
คำถามที่แพงที่สุด
คำถามที่ไม่มีคำตอบ
คำถามที่ feedback ไม่ดี
```

---

## เป้าหมายเชิงตัวเลขสำหรับ MVP

ควรตั้งเป้า:

```text
คำถามทั่วไป:
retrieved context <= 5,000-8,000 tokens

latency:
<= 5-10 วินาที

no-answer ที่ถูกต้อง:
บอกไม่พบเมื่อไม่มีข้อมูล

hallucination:
ต่ำมาก โดยเฉพาะเรื่องกฎการจอง
```

---

## สูตรคิดคร่าว ๆ

```text
cost ต่อคำถาม =
(input_tokens / 1,000,000 * input_price)
+ (output_tokens / 1,000,000 * output_price)
+ embedding_cost
+ rerank_cost
```

ให้ทำ spreadsheet/CSV เก็บค่า:

```text
question_id
input_tokens
output_tokens
model
estimated_cost
latency
```

---

## Recommendation สำหรับโปรเจกต์นี้

เริ่มแบบนี้:

```text
1. curated facts first
2. RAG with top_k=6-8
3. mini/flash/haiku tier model
4. cache FAQ
5. log token usage
6. weekly evaluate cost
```

หลังจากมี traffic จริง:

```text
ถ้า API cost เริ่มสูง:
ทำ local model สำหรับคำถามง่าย/กลาง
เก็บ API ไว้ fallback
```

