# Ground Truth

Ground Truth คือชุดคำถาม-คำตอบที่ใช้วัดว่า RAG Chatbot ตอบถูกจริงไหม

ควรมีตั้งแต่ MVP เพราะจะช่วยตอบคำถามสำคัญ:

- retrieval ดึงข้อมูลถูกไหม
- Qwen3 4B ตอบจาก context จริงไหม
- คำตอบภาษาไทย/อังกฤษดีพอไหม
- ถ้าไม่มีข้อมูล บอทยอมตอบว่าไม่พบไหม

---

## จำนวนที่แนะนำ

```text
MVP: 30-50 ข้อ
หลัง demo: 100 ข้อ
production: 200+ ข้อ
```

ตอนนี้มีไฟล์:

```text
ground_truth_seed.jsonl
```

ใช้เป็นตัวอย่างสั้น ๆ สำหรับดู format

```text
ground_truth_full.jsonl
```

ใช้เป็นชุดหลักสำหรับประเมิน MVP โดยอิงจากข้อมูล Webscraping ปัจจุบัน ครอบคลุมหมวด overview, equipment, games, services, reservation, rules, penalty, contact, knowledge, news, about_us, english และ no_answer

---

## Format

ใช้ JSONL หนึ่งบรรทัดต่อหนึ่งคำถาม:

```json
{"id":"reservation_001","category":"reservation","question":"เช็คอินล่วงหน้าได้กี่นาที","expected_keywords":["30 นาที"],"expected_source_keywords":["Reservation"],"answer_type":"fact"}
```

---

## หมวดที่ควรมี

- reservation
- rules
- penalty
- games
- equipment
- contact
- competition
- knowledge
- events_news
- about_us
- no_answer
- english

---

## วิธีใช้ใน Notebook

Notebook หลักจะใช้ `ground_truth_full.jsonl` เป็นค่าเริ่มต้น

ถ้าต้องการทดสอบเร็ว ให้เปลี่ยน path กลับไปใช้ `ground_truth_seed.jsonl`

---

## หมายเหตุ

Ground Truth ชุดนี้อิงจากข้อมูล Webscraping ที่มีตอนนี้เท่านั้น ถ้าได้รับไฟล์กฎ official เพิ่ม ควรเพิ่มคำถามหมวด rules/reservation/penalty ใหม่อีกชุด และอาจต้องปรับ expected keywords ให้ตรงกับเอกสาร official
