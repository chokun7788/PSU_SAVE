# Accuracy-First Hybrid Retrieval Pipeline

เอกสารนี้เป็นแผน pipeline สำหรับ PSU Esports Chatbot เวอร์ชันที่เน้นความถูกต้องก่อนความเร็ว โดยยังรักษาลักษณะคำตอบเดิมไว้ให้มากที่สุด

## เป้าหมาย

- ตอบแบบ answer-first: ตอบประเด็นก่อน แล้วค่อยรายละเอียดและแหล่งข้อมูล
- ลดการตอบมั่วจาก RAG/vector โดยเฉพาะการดึงเอกสารผิดหมวดหรือผิดเกม
- รองรับคำสะกดผิด ชื่อไทยทับศัพท์ ตัวย่อ และคำถามที่ถามแบบกว้าง
- ให้ Vercel deploy ได้ง่าย ไม่โหลด embedding model ใหญ่ตอน runtime
- เพิ่ม neural embedding แบบ offline ได้ภายหลังโดยไม่ต้องเปลี่ยน API คำตอบ

## ขอบเขตข้อมูลปัจจุบัน

ข้อมูลที่เข้า vector index ตอนนี้คือข้อมูล curated หลักจาก `data/curated/*.jsonl` ยกเว้น `rule_patterns.jsonl`

- `curated_competition_rules.jsonl`
- `curated_facts.jsonl`
- `curated_facts_data_fix_2026-06-29.jsonl`
- `curated_facts_service_fee_2026_aliases.jsonl`
- `equipment_item_details.jsonl`
- `game_item_details.jsonl`
- `our_games_scraped_details.jsonl`

ข้อมูลที่ยังไม่ได้เข้า vector โดยตรง:

- calendar/holiday JSONL
- rule patterns
- raw source files
- ground truth/test files
- logic fast path ที่อยู่ในโค้ด

## Pipeline หลัก

```text
User question
  -> preprocess / normalization
  -> entity extraction
  -> route intent
  -> deterministic fast path
  -> hybrid candidate retrieval
  -> rerank
  -> evidence guard
  -> answer formatter
  -> Thai response style post-processor
```

## ลำดับการตัดสินใจ

### 1. Deterministic Fast Path

ใช้ก่อนเสมอเมื่อมั่นใจสูง เช่น:

- ราคา / service fee
- เวลาเปิดปิดและ calendar ที่ resolve ได้
- รายชื่อเกม catalog
- game detail ที่ entity ชัดเจน
- equipment usage guide
- competition fact card ที่ match กติกาชัดเจน

เหตุผล: ข้อมูลกลุ่มนี้ควบคุมคำตอบได้ดีที่สุด และ style คำตอบนิ่งที่สุด

### 2. Hybrid Candidate Retrieval

ใช้เมื่อ fast path ไม่พอ โดยรวม candidate จากหลายแหล่ง:

- lexical curated retrieval
- guarded vector retrieval
- metadata จาก category, source file, title, aliases, tags

ตอน runtime ปัจจุบันใช้ local vector backend:

```text
local_hash_char_ngram_v1
```

ยังไม่โหลด neural embedding model บน Vercel เพื่อลด cold start และ bundle size

### 3. Rerank

ให้คะแนนใหม่หลังรวม candidate:

- category ตรง route
- entity ตรงคำถาม เช่นชื่อเกม/ชื่ออุปกรณ์
- source file เหมาะกับ intent
- lexical overlap
- vector score
- priority จาก curated data
- penalty ถ้า competition rules โผล่มาในคำถามที่ไม่ได้ถามการแข่งขัน

ตัวอย่าง guard:

- ถามเกม ต้องไม่ดึงกติกาแข่ง เว้นแต่ถามแข่ง/กติกาโดยตรง
- ถามชื่อเกมที่ไม่รู้จักและ entity score ต่ำ ต้อง no-answer
- ถามวันหยุด ต้องใช้ calendar logic ไม่ดึง schedule กว้าง
- ถาม genre เช่น Action ต้องใช้ game detail/catalog ไม่ดึงข่าวหรือกติกา

### 4. Evidence Guard

ก่อนตอบต้องผ่านเงื่อนไข:

- candidate มี source ที่ระบุได้
- category ไม่ข้าม intent สำคัญ
- score ถึง threshold ของหมวดนั้น
- ถ้าเป็น game detail ต้อง match entity หรือเป็น family/genre query ที่ยืนยันได้
- ถ้าคำถามต้องการข้อมูลสถิติ แต่ไม่มี source สถิติ ให้ตอบ no-answer

### 5. Answer Formatter

ยังใช้ formatter เดิมเพื่อรักษา style:

- answer-first
- ระบุแหล่งข้อมูลท้ายคำตอบ
- ไม่บอกว่าใช้ LLM ถ้าคำตอบมาจาก rulebase/fast path/RAG deterministic
- ถ้าไม่มีข้อมูลจริง ให้ no-answer สุภาพ

## แผน embedding ที่เหมาะกับ Vercel

### ระยะสั้น

- ใช้ local vector เดิม
- เพิ่ม hybrid rerank/guard
- ไม่เพิ่ม dependency หนัก
- ไม่เปลี่ยน API

### ระยะกลาง

- สร้าง offline neural embedding จากเครื่อง dev
- เก็บ vector เป็นไฟล์ใน `data/vector`
- runtime ค้นจากไฟล์ ไม่โหลด model
- ใช้ rerank/guard ชุดเดิม

### ระยะยาว

- ถ้า dataset ใหญ่ขึ้นมาก ให้แยก vector store ไปนอก Vercel เช่น Qdrant/Supabase pgvector
- Vercel API ทำหน้าที่ route, retrieve, guard, format

## เกณฑ์ no-answer

ระบบควร no-answer เมื่อ:

- ไม่มี candidate ที่ผ่าน guard
- candidate คะแนนใกล้กันหลายตัวและ entity ไม่ชัด
- source ไม่รองรับคำตอบที่ผู้ใช้ถาม
- คำถามเป็นสถิติ/อันดับ/ความนิยม แต่ไม่มีข้อมูลสถิติจริง
- คำถามถามเกมที่ไม่มีในรายการและ fuzzy/entity ไม่มั่นใจ

## วิธีทดสอบแบบประหยัด

ไม่จำเป็นต้อง run Ground Truth ทุกครั้ง ให้ใช้ smoke ชุดเล็กหลังแก้ logic:

- คำถามที่เคยตอบผิด
- no-answer guard เช่น `เกม abcxyz คืออะไร`
- เกมสะกดเพี้ยน เช่น `พั้บจี`, `เรสิเด้นอีวิล`
- genre เช่น `เกม Action มีอะไรบ้าง`
- calendar เช่น `อาทิตย์หน้าเล่นได้ไหม`, `ปี 2027 มีวันหยุดอะไรบ้าง`

Ground Truth ชุดใหญ่ให้ run เฉพาะก่อน deploy สำคัญหรือเมื่อผู้ใช้ขอ
