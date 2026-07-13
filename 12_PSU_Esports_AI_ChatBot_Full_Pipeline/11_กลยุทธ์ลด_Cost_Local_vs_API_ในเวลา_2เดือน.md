# 11 - กลยุทธ์ลด Cost: Local AI vs API ในเวลา 2 เดือน

ไฟล์นี้ตอบคำถามว่า ถ้ามีเวลาทำ 2 เดือน และอยากทำ AI Chatbot ของเว็บ PSU Esports Studio - Phuket ให้ใช้งานจริงพร้อม Deploy ควรใช้ API หรือทำโมเดลรันเองดี

---

## 1. สรุปก่อน

ถ้าเป้าหมายคือ deploy ให้ทันใน 2 เดือน:

```text
ทางที่แนะนำที่สุด:
RAG + API ก่อน
แล้วทำ Local Model เป็นแผนลด cost ระยะยาว
```

ไม่แนะนำให้เริ่มจาก:

```text
โหลดโมเดลใหญ่
-> เทรนให้จำข้อมูลเว็บ
-> deploy โมเดลเองทั้งหมด
```

เหตุผล:

- ใช้เวลานานกว่า
- ต้องมี GPU หรือ server ที่เหมาะ
- debug ยากกว่า
- คุมคุณภาพภาษาไทยยากกว่า
- ข้อมูลเว็บเปลี่ยนแล้วต้อง update ยุ่งกว่า
- ถ้าใช้ผิดวิธี cost อาจแพงกว่า API

สำหรับโปรเจกต์นี้ คำว่า "ทำ AI ของเราเอง" ควรหมายถึง:

```text
เรามีระบบ RAG ของเราเอง
เรามีฐานข้อมูลความรู้ของเราเอง
เรามี backend/chatbot ของเราเอง
และเลือกได้ว่าจะใช้ API หรือ local model เป็นสมองตอบคำถาม
```

---

## 2. Cost ไม่ได้มีแค่ค่าโมเดล

เวลาเทียบ API กับ Local ต้องคิด cost ทั้งหมด:

### API Cost

มีค่าใช้จ่ายหลัก:

- ค่า input tokens
- ค่า output tokens
- ค่า embedding ตอนสร้างฐานข้อมูล
- ค่า embedding ตอนผู้ใช้ถาม
- ค่า reranker ถ้าใช้

ข้อดี:

- เริ่มเร็ว
- ไม่ต้องดูแล GPU
- คุณภาพสูงกว่าในช่วงแรก
- deploy ง่าย
- scale ง่าย

ข้อเสีย:

- จ่ายตามจำนวนการใช้งาน
- ถ้าคนถามเยอะมาก cost จะเพิ่มตาม
- ต้องพึ่งผู้ให้บริการ

### Local Model Cost

มีค่าใช้จ่ายหลัก:

- เครื่องหรือ server GPU
- ค่าไฟ
- ค่า cloud GPU ถ้าเช่า
- เวลาดูแลระบบ
- latency และ throughput
- monitoring
- fallback ตอน model ตอบพลาด

ข้อดี:

- คุมระบบได้มากกว่า
- ถ้ามีผู้ใช้เยอะมาก อาจถูกกว่า
- ข้อมูลไม่ต้องส่งไป API ภายนอกสำหรับขั้นตอบ
- เหมาะกับการทดลอง open-weight model

ข้อเสีย:

- setup ยากกว่า
- ใช้เวลา optimize
- ต้องมีคนดูแล
- ถ้า traffic น้อย อาจแพงกว่า API
- คุณภาพอาจสู้ API รุ่นดี ๆ ไม่ได้

---

## 3. จุดคุ้มทุนคิดยังไง

ให้คิดแบบนี้:

```text
API cost ต่อเดือน =
จำนวนคำถามต่อเดือน
* token cost ต่อคำถาม
```

```text
Local cost ต่อเดือน =
ค่า server/GPU ต่อเดือน
+ ค่าไฟ
+ เวลาดูแล
+ ค่า downtime/maintenance
```

ถ้า:

```text
API cost ต่อเดือน < Local cost ต่อเดือน
```

ให้ใช้ API ก่อน

ถ้า:

```text
API cost ต่อเดือน > Local cost ต่อเดือนมากพอ
```

ค่อยย้ายบางส่วนไป local

---

## 4. ตัวอย่างคำนวณคร่าว ๆ

สมมติหนึ่งคำถามใช้ประมาณ:

```text
input context: 3,000-5,000 tokens
output answer: 300-800 tokens
```

ถ้าใช้โมเดล API ขนาดเล็กหรือกลาง ค่าใช้จ่ายต่อคำถามมักยังไม่สูงมากสำหรับบอท FAQ/RAG

ตัวอย่างระดับ traffic:

```text
1,000 คำถาม/เดือน
-> API มักคุ้มกว่า local ชัดเจน

10,000 คำถาม/เดือน
-> API ยังมักคุ้มกว่า ถ้าคุม prompt/context ดี

100,000 คำถาม/เดือน
-> เริ่มควร benchmark local model จริงจัง

500,000+ คำถาม/เดือน
-> local หรือ hybrid มีโอกาสคุ้มกว่า
```

ตัวเลขนี้เป็นกรอบคิด ไม่ใช่ราคาตายตัว เพราะราคาจริงขึ้นกับ:

- โมเดลที่เลือก
- จำนวน context ที่ส่งให้ LLM
- จำนวนคำตอบที่ generate
- cache ได้มากแค่ไหน
- มีผู้ใช้พร้อมกันกี่คน
- ต้องการ latency เท่าไร

---

## 5. กลยุทธ์ที่เหมาะกับโปรเจกต์นี้

แนะนำทำแบบ Hybrid ตั้งแต่แรก:

```text
Phase 1:
ใช้ API เพื่อให้บอทตอบดีและ deploy ทัน

Phase 2:
ทำ local model path ไว้ทดลอง

Phase 3:
ถ้า local ตอบดีพอ ให้ route คำถามง่ายไป local
และให้ API ตอบคำถามยากหรือกรณีไม่มั่นใจ
```

โครงแบบ production:

```text
User
-> Chat UI
-> Backend API
-> Query router
   -> answer from curated facts/cache ถ้าตอบได้ตรง
   -> local model ถ้าเป็นคำถามง่าย
   -> API model ถ้าเป็นคำถามยากหรือ local confidence ต่ำ
-> show answer + citation
```

---

## 6. วิธีลด Cost โดยไม่ลดคุณภาพมาก

### 1. ใช้ curated facts ก่อน LLM

ข้อมูลที่เป็นกฎแน่นอน เช่น:

- เช็คอินล่วงหน้าได้กี่นาที
- ยกเลิกได้ไหม
- จองได้กี่ชั่วโมง
- เล่น PS5 มีเกมอะไรบ้าง
- กฎการใช้ห้อง

ให้เก็บเป็น structured facts แล้วตอบจากข้อมูลนี้ก่อน

ถ้าตอบได้ ไม่ต้องเรียก LLM หรือเรียก LLM แบบสั้นมาก

### 2. จำกัด context ที่ส่งเข้า LLM

อย่าส่งข้อมูลเว็บทั้งหน้าเข้าโมเดลทุกครั้ง

ใช้:

- top-k retrieval
- reranking
- category filter
- chunk ที่ดี
- max context tokens

### 3. Cache คำถามยอดฮิต

คำถามที่เจอบ่อย:

- จองยังไง
- เช็คอินยังไง
- เปิดกี่โมง
- มีเกมอะไรบ้าง
- กฎการจองคืออะไร

ให้ cache คำตอบไว้

### 4. ใช้โมเดลเล็กก่อน

เริ่มด้วยโมเดลเล็กหรือกลาง เช่น:

- gpt-5.4-mini
- Gemini Flash
- Claude Haiku
- local Qwen/Typhoon/Llama ขนาดกลาง

ค่อยขยับเป็นโมเดลใหญ่เฉพาะคำถามที่ยาก

### 5. ทำ fallback

ถ้า local model ไม่มั่นใจ:

```text
local answer confidence ต่ำ
-> ส่งต่อให้ API model
```

แบบนี้ช่วยประหยัด แต่ยังรักษาคุณภาพ

---

## 7. Local Model ควรทำไหม

ควรทำ แต่ควรทำเป็นแผนคู่ขนาน ไม่ใช่เส้นทางหลักตั้งแต่วันแรก

เหมาะกับ:

- ทดลองลด cost
- งาน demo
- งานที่ไม่อยากส่งข้อมูลออกนอกระบบ
- กรณีมีเครื่อง GPU อยู่แล้ว
- กรณี traffic สูง

ไม่เหมาะถ้า:

- ต้อง deploy เร็ว
- ยังไม่คุ้นกับ LLM serving
- ไม่มี GPU
- ยังไม่มีระบบ evaluation
- ยังไม่รู้ว่าผู้ใช้จริงถามเยอะเท่าไร

---

## 8. โมเดล Local ที่น่าลอง

ใช้ผ่าน Ollama ก่อน เพราะง่าย:

```text
Ollama
-> Qwen
-> Llama
-> Typhoon ถ้ามีรุ่นที่เหมาะกับภาษาไทย
```

สำหรับ embedding local:

```text
bge-m3
multilingual-e5
mxbai-embed-large
```

ข้อแนะนำ:

```text
อย่า fine-tune ตั้งแต่ต้น
ให้ทำ RAG + prompt + eval ก่อน
```

ถ้าผ่านไปแล้ว local model ตอบรูปแบบไม่ดีจริง ๆ ค่อยทำ fine-tune แบบเล็ก เช่น LoRA หรือ QLoRA จากชุดคำถาม-คำตอบที่เราสร้างเอง

---

## 9. แผน 2 เดือนแบบเหมาะกับ Cost

### Week 1: ทำข้อมูลให้พร้อม

- scrape เว็บ
- clean text
- แยกหมวด
- ทำ chunks
- ทำ curated facts
- ทำ test questions

ผลลัพธ์ที่ต้องมี:

```text
all_pages.jsonl
all_chunks.jsonl
faq_facts.jsonl
eval/testset.jsonl
```

### Week 2: ทำ RAG MVP ด้วย API

- สร้าง embedding
- เก็บใน Chroma
- ทำ retriever
- ทำ prompt
- ทำ backend API
- ทดลองถามตอบ

เป้าหมาย:

```text
ถามเรื่องจอง กฎ เกม การแข่งขัน แล้วตอบได้พร้อม citation
```

### Week 3: ทำ Chat UI และ Logging

- หน้า chat
- conversation history
- feedback button
- log คำถาม
- log chunk ที่ถูก retrieve
- log คำตอบ

### Week 4: Evaluation รอบแรก

- ทดสอบด้วย 50-100 คำถาม
- ดู hallucination
- ดูคำถามที่ค้น context ผิด
- ปรับ chunking / prompt / curated facts

จุดนี้ควรมีบอทที่ demo ได้แล้ว

### Week 5: ทดลอง Local Model

- ติดตั้ง Ollama
- ลอง Qwen/Llama/Typhoon
- ใช้ RAG pipeline เดิม
- เปลี่ยนแค่ LLM backend
- วัดคุณภาพกับ testset เดิม

เปรียบเทียบ:

```text
API model vs Local model
accuracy
latency
cost
ความลื่นของภาษาไทย
ความชอบมั่ว
```

### Week 6: ทำ Hybrid Routing

- คำถามง่ายตอบจาก curated facts/cache
- คำถามกลางส่ง local
- คำถามยากส่ง API
- ถ้าไม่พบข้อมูล ให้บอกว่าไม่พบ ไม่เดา

### Week 7: Production Hardening

- rate limit
- auth/admin
- Docker
- environment variables
- monitoring
- error handling
- fallback
- scheduled re-scrape

### Week 8: Deploy และเก็บผลจริง

- deploy backend
- deploy frontend
- เปิดให้ user ทดลอง
- เก็บ log
- ทำ dashboard cost
- สรุปว่า API/local/hybrid คุ้มสุด

---

## 10. Recommendation สุดท้าย

ถ้ามีเวลา 2 เดือน:

```text
เดือนที่ 1:
ทำ API-based RAG ให้เสร็จและใช้งานได้จริง

เดือนที่ 2:
ทำ local model benchmark + hybrid cost optimization
```

อย่าเริ่มจากการเทรนโมเดล เพราะจะเสี่ยงเสียเวลาเยอะ และอาจยังไม่ได้ระบบที่ deploy ได้

ระบบที่ควรส่งงานได้จริง:

```text
RAG chatbot
+ citation
+ curated facts
+ eval set
+ logging
+ cost dashboard
+ local model experiment
+ API fallback
```

นี่จะดูเป็นงาน AI จริงมากกว่าแค่โหลดโมเดลมารัน เพราะมีครบทั้ง data pipeline, retrieval, evaluation, deployment และ cost strategy

