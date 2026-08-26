# Dynamic RAG Knowledge Inbox

โฟลเดอร์นี้ใช้เตรียมเอกสารใหม่ก่อนนำเข้า Semantic RAG โดยไม่ต้องแก้ rule, fast path หรือ structured tool

## ขั้นตอน

1. คัดลอก `document.example.json` แล้วเปลี่ยนชื่อไฟล์และข้อมูลจริง
2. ใช้ `status: "draft"` ระหว่างตรวจเนื้อหา แหล่งข้อมูล และวันหมดอายุ
3. ตรวจ schema โดยไม่เขียนฐานข้อมูล:

```powershell
python tools\ingest_rag_documents.py --input data\knowledge_inbox --validate-only
```

4. เมื่อเจ้าของข้อมูลตรวจแล้ว เปลี่ยนเป็น `status: "published"` และนำเข้าพร้อมสร้าง semantic index:

```powershell
python tools\ingest_rag_documents.py --input data\knowledge_inbox --build-index
```

ไฟล์ published จะถูก chunk ลง `data/curated/dynamic_knowledge.jsonl` และ vector จะถูกสร้างใหม่ที่ `data/vector/psu_semantic_vector_index.json`

## กฎข้อมูลสำคัญ

- `id`, `title`, `text`, `category`, `source_url`, `trust_level`, `updated_at` ต้องมีเสมอ
- category ที่รองรับ: `knowledge`, `events_news`, `about_us`, `games`, `equipment`
- trust level ที่รองรับ: `official`, `internal_verified`, `user_confirmed`, `secondary`
- ข่าวหรือข้อมูลที่เปลี่ยนตามเวลาต้องตั้ง `time_sensitive: true` และมี `valid_until`
- การตั้ง `freshness_verified: true` ต้องมี `retrieved_at`, `valid_until` และห้ามใช้แหล่ง `secondary`
- ระบบไม่เผยแพร่เอกสาร `draft` หรือ `archived`
- การใช้ `id` เดิมจะอัปเดตเอกสารเดิม ไม่สร้างข้อมูลซ้ำ

