# 10 — เลือกโมเดล LLM / Embedding สำหรับโปรเจกต์นี้

ไฟล์นี้ตอบคำถามว่า ถ้าจะทำ AI Chatbot ของเว็บ PSU Esports Studio - Phuket ควรใช้โมเดลอะไร และต้องโหลดโมเดลมาฝึกเองไหม

---

## 1. เข้าใจผิดที่เจอบ่อย

หลายคนคิดว่า:

```text
โหลดโมเดลมาไว้ในเครื่อง
-> เอาข้อมูลเว็บไปสอนโมเดล
-> ได้ AI ที่รู้ข้อมูลเว็บ
```

แต่สำหรับงานนี้ ไม่แนะนำเริ่มแบบนั้น

วิธีที่เหมาะกว่าคือ:

```text
เก็บข้อมูลเว็บไว้ในฐานข้อมูลค้นหา
-> เวลาผู้ใช้ถาม ค้นข้อมูลที่เกี่ยวข้อง
-> ส่งข้อมูลนั้นให้ LLM อ่าน
-> LLM ตอบจากข้อมูลที่ให้
```

วิธีนี้เรียกว่า RAG

---

## 2. ต้องมีโมเดลกี่ตัว

โดยทั่วไปต้องมี 2 ส่วน:

### 1. LLM สำหรับตอบ

หน้าที่:

- อ่าน context
- สรุปคำตอบ
- ตอบภาษาไทย
- จัดรูปแบบคำตอบ
- บอกว่าไม่พบข้อมูลถ้า context ไม่มี

ตัวอย่าง:

- OpenAI GPT mini / flagship model
- Gemini Flash / Pro
- Claude Haiku / Sonnet
- Typhoon API
- Local model ผ่าน Ollama เช่น Qwen / Llama / Typhoon

### 2. Embedding model สำหรับค้นข้อมูล

หน้าที่:

- แปลงข้อความเว็บเป็น vector
- แปลงคำถามเป็น vector
- ใช้ค้นว่า chunk ไหนใกล้คำถาม

ตัวอย่าง:

- OpenAI `text-embedding-3-small`
- OpenAI `text-embedding-3-large`
- Cohere multilingual embedding
- BGE-M3
- multilingual-e5

---

## 3. คำแนะนำสำหรับโปรเจกต์นี้

ถ้าคุณยังไม่ค่อยมีพื้นฐาน ให้ใช้แบบนี้ก่อน:

```text
LLM: ใช้ API cloud
Embedding: ใช้ API หรือ local multilingual embedding
Vector DB: Chroma local
```

อย่าเพิ่ง train / fine-tune โมเดลเอง

---

## 4. ชุดแนะนำตามระดับ

### ชุด A: ง่ายสุด เหมาะกับเริ่มทำให้สำเร็จ

ใช้เมื่อ:

- อยากทำให้เสร็จเร็ว
- ไม่อยากยุ่งกับ GPU
- ยังไม่อยากโหลดโมเดลเอง

แนะนำ:

```text
LLM: OpenAI mini model หรือ Gemini Flash
Embedding: OpenAI text-embedding-3-small
Vector DB: Chroma
```

ข้อดี:

- ทำง่าย
- คุณภาพดี
- ไม่ต้องมีคอมแรง
- เหมาะกับ MVP

ข้อเสีย:

- มีค่าใช้จ่ายตามการใช้งาน
- ข้อมูลถูกส่งไป API ภายนอก

เหมาะกับคุณตอนนี้ที่สุด

---

### ชุด B: ภาษาไทยเน้น ๆ

ใช้เมื่อ:

- อยากให้ตอบไทยดี
- ข้อมูลเป็นภาษาไทยเยอะ
- อยากลองโมเดลไทย

แนะนำ:

```text
LLM: Typhoon API หรือ OpenAI/Gemini/Claude ที่รองรับไทยดี
Embedding: multilingual embedding เช่น BGE-M3, multilingual-e5, OpenAI embedding
Vector DB: Chroma หรือ Qdrant
```

ข้อดี:

- เหมาะกับข้อมูลไทย
- Typhoon เป็นแนว Thai-first

ข้อเสีย:

- ต้องเช็กเอกสาร API และเงื่อนไขการใช้งาน
- ecosystem อาจไม่กว้างเท่า OpenAI/Gemini

---

### ชุด C: Local ในเครื่อง

ใช้เมื่อ:

- ไม่อยากส่งข้อมูลออกนอกเครื่อง
- อยากทดลองฟรี
- เครื่องมี RAM/VRAM พอ

แนะนำ:

```text
LLM: Ollama + Qwen/Llama/Typhoon local
Embedding: BGE-M3 หรือ multilingual-e5 local
Vector DB: Chroma local
```

ข้อดี:

- ข้อมูลอยู่ในเครื่อง
- ไม่เสียค่า API ต่อคำถาม
- เหมาะกับทดลอง offline

ข้อเสีย:

- ช้ากว่า cloud มากถ้าเครื่องไม่แรง
- คุณภาพอาจสู้ cloud model ไม่ได้
- setup ยุ่งกว่า
- ถ้าใช้โมเดลเล็ก อาจตอบไทยไม่ดีเท่า API

---

### ชุด D: Production จริง

ใช้เมื่อ:

- มีคนใช้จริง
- ต้องการความเร็วและเสถียร
- ต้องการ monitor / scaling

แนะนำ:

```text
LLM: OpenAI / Gemini / Claude / Typhoon API ตามคุณภาพและงบ
Embedding: OpenAI text-embedding-3-small/large หรือ Cohere multilingual
Vector DB: Qdrant หรือ pgvector
Reranker: Cohere Rerank หรือ BGE/Jina reranker
Backend: FastAPI
Frontend: Streamlit ช่วงแรก, React/Next.js ตอนจริง
```

---

## 5. สำหรับเว็บ PSU Esports ควรเลือกอะไร

คำแนะนำจริง:

### เริ่มต้น

```text
LLM: Gemini Flash หรือ OpenAI mini model
Embedding: OpenAI text-embedding-3-small หรือ BGE-M3
Vector DB: Chroma
```

### ถ้าตอบไทยยังไม่ถูกใจ

ลอง:

```text
LLM: Typhoon API
หรือ Claude/Gemini/OpenAI รุ่นที่เก่งภาษาไทยขึ้น
```

### ถ้าต้อง offline/local

ลอง:

```text
Ollama + Qwen 7B/14B หรือ Llama 8B/13B
Embedding local: BGE-M3 หรือ multilingual-e5
```

แต่ local ควรเป็นทางเลือกหลังจากทำ MVP สำเร็จแล้ว

---

## 6. ต้อง train โมเดลเองไหม

คำตอบ: ยังไม่ต้อง

สำหรับงานนี้ ให้ใช้ RAG ก่อน เพราะ:

- ข้อมูลอยู่ในเว็บ
- กฎการจองเปลี่ยนได้
- รายชื่อเกมเปลี่ยนได้
- ข้อมูลต้องอ้างอิง source
- train เองยาก แพง และต้องมี dataset

ถ้าจะ "สอนข้อมูลเว็บ" ให้ระบบ ให้ทำแบบนี้:

```text
เอาข้อมูลเว็บไปทำ chunks
-> embedding
-> vector database
-> retrieve ตอนถาม
```

ไม่ใช่เอาไป fine-tune โมเดล

---

## 7. Fine-tuning ใช้เมื่อไร

ใช้เมื่อ:

- อยากให้ตอบตาม style เฉพาะมาก ๆ
- prompt แล้วก็ยังไม่ทำตามรูปแบบ
- มี dataset คำถาม-คำตอบคุณภาพสูงจำนวนมาก
- ระบบ RAG ดีแล้วแต่ยังต้องปรับพฤติกรรม

ไม่ใช้เพื่อ:

- เพิ่มความรู้ใหม่จากเว็บ
- จำกฎการจอง
- จำรายชื่อเกม

ความรู้ใหม่ควรใช้ RAG

---

## 8. เปรียบเทียบง่าย ๆ

| วิธี | เหมาะไหม | เหตุผล |
|---|---|---|
| โหลดโมเดลมา train เอง | ยังไม่เหมาะ | ยาก ใช้เครื่องแรง ต้องมี dataset |
| โหลดโมเดล local ผ่าน Ollama | พอได้สำหรับทดลอง | ไม่ต้อง train แต่เครื่องต้องพอ |
| ใช้ API + RAG | เหมาะที่สุดตอนเริ่ม | ทำง่าย คุณภาพดี |
| Fine-tune | ยังไม่จำเป็น | ใช้ทีหลังเมื่อ RAG นิ่งแล้ว |

---

## 9. Stack ที่แนะนำให้ทำจริงตอนนี้

เริ่มแบบนี้:

```text
Data:
  data/curated/faq_facts.jsonl
  data/processed/all_chunks.jsonl

Embedding:
  text-embedding-3-small หรือ BGE-M3

Vector DB:
  Chroma local

LLM:
  OpenAI mini model / Gemini Flash / Typhoon API

Prompt:
  prompts/system_prompt_th.md

UI:
  Streamlit
```

---

## 10. Roadmap การเลือกโมเดล

### รอบที่ 1: ทำให้ใช้ได้ก่อน

ใช้ cloud API + Chroma

### รอบที่ 2: วัดคุณภาพ

ทดสอบคำถามใน `eval/testset.jsonl`

### รอบที่ 3: เทียบโมเดล

ลอง LLM 2-3 ตัว:

- OpenAI mini
- Gemini Flash
- Typhoon API

ดูว่า:

- ตอบไทยดีไหม
- ตอบตาม context ไหม
- ราคา/latency รับได้ไหม

### รอบที่ 4: ค่อยคิด local

ถ้าต้องการประหยัดหรือ privacy ค่อยลอง Ollama

---

## 11. สรุปสั้นที่สุด

คุณไม่ต้องเริ่มจากโหลดโมเดลมาฝึกเอง

ให้เริ่มแบบนี้:

```text
ใช้ LLM API เป็นสมองภาษา
ใช้ embedding model เป็นตัวค้น
ใช้ vector DB เป็นหน่วยความจำ
ใช้ข้อมูลเว็บเป็น context
ใช้ RAG ให้บอทตอบจาก context
```

ถ้าทำตามนี้จะเร็วกว่า ถูกกว่า และแก้ง่ายกว่าการ train โมเดลเองมาก

