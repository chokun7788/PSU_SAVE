# 01 - เลือกโมเดลสำหรับแบบ Local

การเลือก local model ต้องดูมากกว่า "โมเดลเก่งไหม" ต้องดูด้วยว่าเครื่องรันไหวหรือไม่, ภาษาไทยดีพอไหม, latency รับได้ไหม, และ license ใช้กับงานจริงได้หรือไม่

---

## ปัจจัยเลือกโมเดล

1. คุณภาพภาษาไทย
2. ความสามารถทำ RAG
3. ขนาดโมเดล
4. VRAM ที่ต้องใช้
5. context length
6. speed/token per second
7. license
8. tool/API compatibility
9. community support

---

## Model Family ที่น่าลอง

### Qwen

เหมาะกับ:

- multilingual
- reasoning ดี
- รุ่นขนาดกลางค่อนข้างคุ้ม
- ใช้ผ่าน Ollama/vLLM ได้ง่าย

ควรลอง:

```text
7B-9B:
เริ่มต้น/เครื่องเล็ก

14B:
คุณภาพดีขึ้น แต่ต้องใช้ VRAM มากขึ้น

32B:
ดีขึ้นมาก แต่ต้องใช้ GPU ใหญ่หรือ quantization
```

---

### Llama

เหมาะกับ:

- community ใหญ่
- tooling เยอะ
- serving รองรับดี
- มีหลายขนาด

ควรลอง:

```text
8B:
เริ่มต้นง่าย

70B:
คุณภาพสูงขึ้นมาก แต่ hardware สูงมาก
```

---

### Typhoon / Thai-focused Models

เหมาะกับ:

- ภาษาไทย
- บริบทไทย
- งานที่อยาก benchmark โมเดลไทย

ควรลองถ้ามีรุ่นที่รองรับ:

```text
instruct/chat model
context length เหมาะกับ RAG
license ใช้ได้กับงานที่ต้องการ
```

---

### Mistral / Mixtral

เหมาะกับ:

- latency/quality balance
- inference ecosystem ดี
- บางรุ่นมีความเร็วดี

ควร benchmark ภาษาไทยก่อนใช้จริง

---

## ขนาดโมเดลที่ควรเริ่ม

สำหรับเวลา 2 เดือน:

```text
เริ่มที่ 7B-14B ก่อน
```

เหตุผล:

- setup ง่ายกว่า
- benchmark เร็วกว่า
- ใช้ GPU ขนาดกลางได้
- ถ้าคำถามเป็น RAG ไม่จำเป็นต้องใช้โมเดลใหญ่มาก

ถ้า 7B/14B ตอบไม่ดีพอ:

```text
ลอง 32B
หรือใช้ API fallback สำหรับคำถามยาก
```

---

## Embedding แบบ Local

Embedding local สำคัญพอ ๆ กับ LLM

ตัวเลือก:

### bge-m3

เหมาะกับ:

- multilingual
- retrieval
- dense/sparse/multi-vector use case
- ใช้กับเอกสารไทยได้ดีในหลายงาน

### multilingual-e5

เหมาะกับ:

- multilingual search
- ใช้ง่ายผ่าน sentence-transformers

### sentence-transformers รุ่น multilingual

เหมาะกับ:

- ใช้งานง่าย
- run CPU/GPU ได้

---

## Reranker แบบ Local

ตัวเลือก:

- bge-reranker
- cross-encoder multilingual
- reranker ที่รองรับภาษาไทย/หลายภาษา

ควรใช้ถ้า:

- retrieval ดึงข้อมูลผิดหมวดบ่อย
- คำถามคล้ายกันหลายหน้า
- ต้องการคุณภาพสูงขึ้น

---

## Quantization

Quantization คือการลดความละเอียดน้ำหนักโมเดล เช่น:

```text
FP16 -> 16-bit
INT8 -> 8-bit
INT4/Q4 -> 4-bit
```

ข้อดี:

- ใช้ VRAM น้อยลง
- รันบนเครื่องเล็กลง
- cost ถูกลง

ข้อเสีย:

- คุณภาพอาจลดลง
- บางคำตอบอาจเพี้ยน
- ต้อง benchmark

แนะนำ:

```text
ทดลอง Q4 หรือ Q5 สำหรับ Ollama/llama.cpp
ใช้ FP16/BF16 ถ้ามี GPU เพียงพอและต้องการคุณภาพสูง
```

---

## Context Length

สำหรับ RAG ไม่ควรยัด context เยอะเกิน

เป้าหมาย:

```text
4K-8K tokens เพียงพอสำหรับคำถามทั่วไป
16K+ มีประโยชน์ถ้าคำถามต้องอ่านหลายหน้า
```

Local model context ยาวขึ้นจะกิน VRAM มากขึ้น เพราะ KV cache เพิ่ม

---

## Recommendation สำหรับโปรเจกต์นี้

### Local MVP

```text
LLM:
Qwen/Llama/Typhoon 7B-14B ผ่าน Ollama

Embedding:
bge-m3 หรือ multilingual-e5

Vector DB:
Chroma

Serving:
Ollama
```

### Local Production

```text
LLM:
Qwen/Llama/Typhoon 14B-32B ถ้า GPU ไหว

Serving:
vLLM หรือ TGI

Embedding:
bge-m3 service

Vector DB:
Qdrant/pgvector

Fallback:
API model สำหรับคำถามยาก
```

---

## วิธีเลือกจริง

ใช้ testset เดียวกันทุกโมเดล:

```text
คำถามจอง 20 ข้อ
คำถามกฎ 20 ข้อ
คำถามเกม 20 ข้อ
คำถามแข่งขัน 20 ข้อ
คำถามที่ไม่มีข้อมูล 20 ข้อ
```

วัด:

- correctness
- hallucination
- citation correctness
- latency
- tokens/sec
- memory usage
- crash rate
- user preference

โมเดลที่ควรเลือกไม่ใช่โมเดลที่ใหญ่ที่สุด แต่คือโมเดลที่:

```text
ตอบถูกพอ
เร็วพอ
รันนิ่งพอ
cost คุ้ม
ดูแลได้จริง
```

