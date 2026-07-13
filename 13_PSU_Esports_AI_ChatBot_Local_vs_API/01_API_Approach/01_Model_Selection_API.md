# 01 - เลือกโมเดลสำหรับแบบ API

การเลือกโมเดลแบบ API ควรคิดเป็น 4 ชั้น:

1. LLM สำหรับตอบคำถาม
2. Embedding model สำหรับค้นข้อมูล
3. Reranker สำหรับจัดอันดับ context
4. Moderation/safety model ถ้าต้องเปิดใช้งานสาธารณะ

---

## 1. LLM สำหรับตอบคำถาม

หน้าที่:

- อ่าน context จาก RAG
- สรุปคำตอบภาษาไทย
- ตอบตามกฎของระบบ
- ไม่เดาเมื่อไม่มีข้อมูล
- อธิบายขั้นตอน เช่น วิธีจอง/เช็คอิน

---

## Provider ที่ควรพิจารณา

### OpenAI

เหมาะกับ:

- งาน RAG ทั่วไป
- ภาษาไทยค่อนข้างดี
- ecosystem ดี
- tooling เยอะ
- production ใช้ง่าย

แนวทางเลือก:

```text
เริ่ม: รุ่น mini/low-cost ของตระกูล GPT ล่าสุด
เพิ่มคุณภาพ: รุ่น flagship ถ้าคำถามยากหรือคำตอบต้องละเอียดมาก
```

ใช้เมื่อ:

- ต้องการ balance ระหว่างคุณภาพและต้นทุน
- อยากใช้ embeddings ของ provider เดียวกัน
- ต้องการ function/tool calling ในอนาคต

---

### Google Gemini

เหมาะกับ:

- cost-sensitive workload
- latency เร็ว
- context ยาว
- งานสรุปข้อมูลจำนวนมาก

แนวทางเลือก:

```text
เริ่ม: Flash tier
เพิ่มคุณภาพ: Pro tier
```

ใช้เมื่อ:

- ต้องการราคาคุ้ม
- มีระบบอยู่บน Google Cloud
- อยากทดลอง context window ใหญ่

---

### Anthropic Claude

เหมาะกับ:

- คำตอบเป็นธรรมชาติ
- การอ่าน context ยาว
- งานที่ต้องการ reasoning และความระมัดระวัง

แนวทางเลือก:

```text
เริ่ม: Haiku tier
เพิ่มคุณภาพ: Sonnet tier
```

ใช้เมื่อ:

- อยากได้คำตอบเรียบร้อย อธิบายดี
- ต้องการความระมัดระวังเรื่องการไม่เดา
- มี budget สูงกว่าเล็กน้อย

---

### Typhoon / Thai-focused provider

เหมาะกับ:

- งานภาษาไทย
- ต้องการ local context ของไทย
- ต้องการทดลองโมเดลไทย

ใช้เมื่อ:

- ภาษาไทยเป็นหัวใจหลัก
- อยาก benchmark กับ provider ต่างประเทศ
- ต้องการทางเลือกที่เหมาะกับบริบทไทย

---

## Recommendation สำหรับโปรเจกต์ PSU Esports

### MVP ที่แนะนำ

```text
LLM:
OpenAI mini-tier หรือ Gemini Flash

Embedding:
OpenAI embeddings หรือ multilingual embedding

Vector DB:
Chroma

Fallback:
เปลี่ยน provider ได้ผ่าน environment variable
```

เหตุผล:

- deploy เร็ว
- คุณภาพดีพอสำหรับ RAG
- cost ไม่สูงถ้าคุม context
- debug ง่าย

---

## 2. Embedding Model

Embedding สำคัญมาก เพราะถ้าค้น context ผิด ต่อให้ LLM เก่งก็อาจตอบผิด

หน้าที่:

```text
ข้อความเว็บ -> vector
คำถามผู้ใช้ -> vector
ค้น chunk ที่ใกล้กันที่สุด
```

---

## ตัวเลือก Embedding แบบ API

### OpenAI Embeddings

เหมาะกับ:

- ใช้ง่าย
- คุณภาพดี
- document ภาษาไทย/อังกฤษปนกัน
- production

### Gemini Embeddings

เหมาะกับ:

- ใช้ ecosystem Google
- ต้องการคุม provider ให้อยู่ใน Google stack

### Cohere Embed

เหมาะกับ:

- multilingual retrieval
- ใช้คู่กับ Cohere Rerank

---

## 3. Reranker

Reranker ไม่จำเป็นสำหรับ MVP แต่ช่วยมากถ้าข้อมูลหลายหมวดคล้ายกัน

ตัวอย่างปัญหา:

```text
ผู้ใช้ถาม: "จอง PS5 ยังไง"
retriever อาจดึงทั้งหน้ากฎจอง, หน้ารายชื่อเกม, หน้าข่าวกิจกรรม
reranker จะช่วยจัดอันดับว่าชิ้นไหนเกี่ยวที่สุด
```

ตัวเลือก:

- Cohere Rerank
- bge-reranker แบบ local
- cross-encoder reranker

แนะนำ:

```text
MVP:
ยังไม่ต้องใช้ก่อน

หลัง MVP:
เพิ่ม reranker ถ้าคำตอบผิดเพราะค้น context ผิด
```

---

## 4. Model Routing

อย่าใช้โมเดลเดียวตอบทุกอย่างถ้าต้องการลด cost

ควร route แบบนี้:

```text
คำถาม FAQ ง่าย:
ตอบจาก curated facts/cache

คำถามทั่วไป:
ใช้โมเดล API ราคาประหยัด

คำถามยาก:
ใช้โมเดลคุณภาพสูงกว่า

ไม่มั่นใจ:
ตอบว่าไม่พบข้อมูล หรือส่งต่อโมเดลใหญ่
```

---

## 5. Prompt Rule สำคัญ

ควรบังคับโมเดล:

```text
ใช้เฉพาะข้อมูลใน context
ห้ามเดา
ตอบภาษาไทย
ถ้าไม่พบข้อมูลให้บอกว่าไม่พบ
แสดงแหล่งอ้างอิงหรือหมวดข้อมูล
แยกคำตอบเป็นข้อ ๆ ถ้ามีหลายขั้นตอน
```

---

## 6. วิธีเลือกแบบเป็นขั้นตอน

1. ทำ testset 50-100 คำถาม
2. ลอง 2-3 provider
3. วัด accuracy
4. วัด hallucination
5. วัด latency
6. วัด cost ต่อ 1,000 คำถาม
7. เลือกโมเดลหลัก
8. ตั้ง fallback

---

## 7. ตัวอย่าง config

```env
LLM_PROVIDER=openai
LLM_MODEL=latest-mini-model
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=latest-small-embedding-model
RERANKER_PROVIDER=none
VECTOR_DB=chroma
```

ถ้าอยากลอง Gemini:

```env
LLM_PROVIDER=gemini
LLM_MODEL=flash-tier-model
EMBEDDING_PROVIDER=gemini
VECTOR_DB=chroma
```

ถ้าอยากลอง Claude:

```env
LLM_PROVIDER=anthropic
LLM_MODEL=haiku-or-sonnet-tier-model
EMBEDDING_PROVIDER=openai
VECTOR_DB=chroma
```

หมายเหตุ: ชื่อโมเดลและราคาเปลี่ยนได้ ควรตรวจหน้า docs/pricing ล่าสุดก่อน deploy จริง

