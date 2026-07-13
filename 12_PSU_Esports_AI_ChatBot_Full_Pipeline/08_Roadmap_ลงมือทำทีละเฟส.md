# 08 — Roadmap ลงมือทำทีละเฟส

นี่คือแผนทำจริงแบบเป็นเฟส

---

## Phase 1: เข้าใจข้อมูล

เวลา: 0.5-1 วัน

ทำ:

- อ่าน `11_PSU_Esports_AI_ChatBot/README.md`
- อ่าน `data/curated/faq_facts.jsonl`
- เปิด `reservation/summary.md`
- เปิด `services/summary.md`
- รัน `simple_retriever_demo.py`

ผลลัพธ์:

- รู้ว่าข้อมูลอยู่ไหน
- รู้ว่าหมวดไหนตอบเรื่องอะไร
- ทดลองค้นข้อมูลได้

---

## Phase 2: Prototype Retriever

เวลา: 1-2 วัน

ทำ:

- เลือก embedding model
- สร้าง vector index
- ใส่ curated facts
- ใส่ chunks 4 หมวดแรก
- retrieve top-k
- print debug

ผลลัพธ์:

- ถามแล้วได้ chunk ที่เกี่ยวข้อง

---

## Phase 3: ต่อ LLM

เวลา: 1 วัน

ทำ:

- ใช้ system prompt
- build context
- call LLM
- ตอบพร้อม citation

ผลลัพธ์:

- chatbot CLI ตอบคำถามได้

---

## Phase 4: ทำ UI

เวลา: 1-2 วัน

ทำ:

- Streamlit chat
- แสดง answer
- แสดง sources
- เพิ่มปุ่ม feedback ง่าย ๆ

ผลลัพธ์:

- คนทั่วไปลองใช้ได้

---

## Phase 5: Evaluation

เวลา: 1-2 วัน

ทำ:

- ใช้ `eval/testset.jsonl`
- รันคำถามทั้งหมด
- บันทึกคำตอบ
- ตรวจ pass/fail
- แก้ retrieval/prompt

ผลลัพธ์:

- มีตัวเลขคุณภาพ

---

## Phase 6: เพิ่มหมวด News

เวลา: 1 วัน

ทำหลังระบบนิ่งแล้ว

เหตุผล:

- news มีเยอะ
- อาจทำให้ retrieval noisy

ให้เพิ่มพร้อม category routing

---

## Phase 7: Deploy

เวลา: 2-5 วัน

ทำ:

- FastAPI
- Docker
- deploy server
- logging
- update data script

ผลลัพธ์:

- ใช้งานจริงได้

---

## Phase 8: Maintain

ทำต่อเนื่อง

- เพิ่มคำถามจริงเข้า testset
- update ข้อมูลเว็บ
- แก้ curated facts
- monitor คำตอบผิด
- ปรับ prompt/retrieval

---

## แผน 7 วันแบบเร็ว

| วัน | งาน |
|---|---|
| 1 | อ่านข้อมูล + รัน simple retriever |
| 2 | ทำ vector index |
| 3 | ต่อ LLM + prompt |
| 4 | ทำ Streamlit UI |
| 5 | ทำ evaluation |
| 6 | แก้ retrieval/prompt |
| 7 | เตรียม deploy/demo |

