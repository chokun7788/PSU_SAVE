# 04 — ขั้นตอนทำจริงแบบ MVP

MVP คือ chatbot เวอร์ชันแรกที่ตอบคำถามได้จริง โดยยังไม่ต้องทำระบบใหญ่

---

## Step 0: เตรียม environment

```bash
cd C:\Users\Chokhun\Downloads\Learn-LLM\11_PSU_Esports_AI_ChatBot
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

ถ้าเครื่องยังไม่มี Python ใน PATH ให้ใช้ Python ที่ติดตั้งไว้หรือใช้ Conda/Miniconda แทน

---

## Step 1: ตรวจข้อมูลก่อน

ลองเปิด:

```text
data/raw/psu_esports_ai_extracted/README_TH.md
data/raw/psu_esports_ai_extracted/reservation/summary.md
data/raw/psu_esports_ai_extracted/services/summary.md
```

แล้วลองค้นแบบง่ายด้วย:

```bash
python src/simple_retriever_demo.py "จองได้สูงสุดกี่ session"
python src/simple_retriever_demo.py "PS5 มีเกมอะไร"
python src/simple_retriever_demo.py "เช็คอินล่วงหน้าได้กี่นาที"
```

เป้าหมาย: เช็กก่อนว่าไฟล์ข้อมูลมีเนื้อหาที่ต้องการจริง

---

## Step 2: เลือกหมวดสำหรับ index

เริ่มจากหมวด:

```text
reservation
services
competition
knowledge
contact
```

ยังไม่ต้องใส่ `news` ถ้าระบบยังค้นไม่แม่น

---

## Step 3: สร้าง Vector Index

แนวคิด:

```python
for chunk in chunks:
    vector = embedding_model.embed(chunk["text"])
    vector_db.add(
        id=chunk["id"],
        vector=vector,
        document=chunk["text"],
        metadata={
            "category": chunk["category"],
            "title": chunk["title"],
            "url": chunk["url"]
        }
    )
```

เริ่มง่ายด้วย Chroma หรือ FAISS ได้

---

## Step 4: เขียน retriever

เมื่อผู้ใช้ถาม:

```python
question_vector = embed(question)
hits = vector_db.search(question_vector, top_k=5)
```

สิ่งที่ควร print debug:

- chunk id
- category
- score
- title
- text preview

ถ้า retrieved chunk ไม่ตรง อย่าเพิ่งแก้ prompt ให้แก้ retrieval ก่อน

---

## Step 5: สร้าง prompt

ใช้ prompt จาก:

```text
prompts/system_prompt_th.md
prompts/answer_format.md
```

หลักการ:

- ตอบจาก context เท่านั้น
- ถ้าไม่มีข้อมูล ให้บอกว่าไม่พบ
- อ้างอิงแหล่งที่มา
- ตอบภาษาไทย

---

## Step 6: ต่อ LLM

ตัวเลือก:

- Cloud LLM เช่น GPT, Claude, Gemini
- Local LLM เช่น Ollama ถ้าต้องการให้ข้อมูลไม่ออกนอกเครื่อง

สำหรับเริ่มต้นใช้ cloud ง่ายกว่า แต่ถ้าข้อมูลมีความอ่อนไหว ให้พิจารณา local หรือ policy ขององค์กร

---

## Step 7: ทำ UI

เริ่มง่ายด้วย Streamlit:

```text
ช่องพิมพ์คำถาม
-> เรียก backend RAG
-> แสดงคำตอบ
-> แสดงแหล่งอ้างอิง
```

ถ้าจะทำเว็บจริงค่อยใช้ FastAPI + React/Next.js

---

## Step 8: ทดสอบด้วยชุดคำถาม

ใช้:

```text
eval/testset.jsonl
```

ทดสอบว่าบอท:

- ตอบถูกไหม
- อ้างอิงไหม
- ไม่ hallucinate ไหม
- ถามนอกขอบเขตแล้วบอกว่าไม่พบไหม

---

## MVP Definition of Done

ถือว่า MVP สำเร็จเมื่อ:

- ถามเรื่องกฎจองแล้วตอบถูก
- ถามเรื่องเกม/อุปกรณ์แล้วตอบถูก
- ถามเรื่องการแข่งขันที่อยู่ในเว็บแล้วตอบได้
- ถามเรื่องนอกเว็บแล้วไม่เดา
- คำตอบมี source/citation
- มี testset อย่างน้อย 20 ข้อ

