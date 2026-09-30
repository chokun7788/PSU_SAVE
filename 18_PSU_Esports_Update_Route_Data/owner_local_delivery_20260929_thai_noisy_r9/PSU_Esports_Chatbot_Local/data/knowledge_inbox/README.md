# Dynamic RAG Knowledge Inbox

โฟลเดอร์นี้ใช้เตรียมเอกสารใหม่ก่อนนำเข้า Semantic RAG โดยไม่ต้องแก้ rule, fast path หรือ structured tool

## ขั้นตอน

1. คัดลอก `document.example.json` แล้วเปลี่ยนชื่อไฟล์และข้อมูลจริง
2. ใช้ `status: "draft"` ระหว่างตรวจเนื้อหา แหล่งข้อมูล และวันหมดอายุ
3. ตรวจ schema โดยไม่เขียนฐานข้อมูล:

```powershell
python tools\ingest_rag_documents.py --input data\knowledge_inbox --validate-only
```

ผลลัพธ์จะแสดง `ready_document_ids` สำหรับเอกสารที่พร้อม Publish และ
`pending_document_ids` แยกตามสถานะ `draft`, `in_review`, `approved` หรือ `archived`
เพื่อให้ผู้ดูแลเห็นว่าเอกสารใดยังไม่เข้าสู่ RAG ก่อนสั่ง build index

4. ส่ง `status: "in_review"` ให้ผู้ตรวจตรวจ Draft แล้วบันทึก `approved_by` และ `approved_at`
5. เมื่อผ่านการอนุมัติ เปลี่ยนเป็น `status: "published"` และนำเข้าพร้อมสร้าง semantic index:

```powershell
python tools\ingest_rag_documents.py --input data\knowledge_inbox --build-index
```

ไฟล์ published จะถูก chunk ลง `data/curated/dynamic_knowledge.jsonl` และ vector จะถูกสร้างใหม่ที่ `data/vector/psu_semantic_vector_index.json`

## กฎข้อมูลสำคัญ

- `id`, `title`, `text`, `category`, `source_url`, `trust_level`, `updated_at` ต้องมีเสมอ
- เอกสารที่ `published` ต้องมี `approved_by`, `approved_at`, `source_snapshot_text` และ `source_snapshot_sha256` ที่ตรงกับข้อความต้นทาง
- `text` ที่เผยแพร่ต้องเป็นข้อความตัดตอนที่พบใน `source_snapshot_text`; ห้ามให้ LLM สร้างข้อเท็จจริงใหม่แล้ว Publish
- ระบุ `content_type`, `entity_ids`, `facets`, `language` และ `version` เพื่อให้ retrieval filter สิ่งที่ถามก่อนจัดอันดับเอกสาร
- category ที่รองรับ: `knowledge`, `events_news`, `about_us`, `games`, `equipment`
- trust level ที่รองรับ: `official`, `internal_verified`, `user_confirmed`, `secondary`
- ข่าวหรือข้อมูลที่เปลี่ยนตามเวลาต้องตั้ง `time_sensitive: true` และมี `valid_until`
- การตั้ง `freshness_verified: true` ต้องมี `retrieved_at`, `valid_until` และห้ามใช้แหล่ง `secondary`
- ระบบไม่เผยแพร่เอกสาร `draft`, `in_review`, `approved` หรือ `archived`; เผยแพร่ได้เฉพาะ `published`
- การใช้ `id` เดิมจะอัปเดตเอกสารเดิม ไม่สร้างข้อมูลซ้ำ
