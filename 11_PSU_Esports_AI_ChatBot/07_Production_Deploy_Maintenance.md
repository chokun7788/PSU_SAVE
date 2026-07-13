# 07 — Production, Deploy และ Maintenance

เมื่อ MVP ตอบได้แล้ว ค่อยทำให้เป็นระบบใช้งานจริง

---

## 1. โครง production ที่แนะนำ

```text
Frontend chat
  -> Backend API
  -> RAG service
  -> Vector DB
  -> LLM provider
```

Frontend:

- Streamlit สำหรับ demo
- React/Next.js สำหรับเว็บจริง

Backend:

- FastAPI

Vector DB:

- Chroma สำหรับเริ่ม
- Qdrant/pgvector สำหรับ production

---

## 2. Logging ที่ควรเก็บ

ต่อคำถามควรเก็บ:

- question
- retrieved chunk ids
- categories ที่ถูกค้น
- answer
- source URLs
- latency
- user feedback

อย่าเก็บข้อมูลส่วนบุคคลเกินจำเป็น

---

## 3. อัปเดตข้อมูลเว็บ

ข้อมูลเว็บเปลี่ยนได้ ควรวางแผน:

```text
weekly/monthly scrape
-> regenerate jsonl
-> rebuild vector index
-> run eval
-> deploy index ใหม่
```

ถ้าเป็นระบบจอง/games/rules แนะนำอัปเดตถี่กว่าข่าวทั่วไป

---

## 4. เรื่องความปลอดภัย

ต้องระวัง:

- prompt injection
- ข้อมูลส่วนบุคคล
- ผู้ใช้ถามข้อมูลการจองของคนอื่น
- บอทตอบเกินข้อมูลในเว็บ
- บอทให้คำแนะนำผิดเรื่องกฎ

---

## 5. Versioning

ควรเก็บ version ของ:

- dataset
- prompt
- embedding model
- vector index
- evaluation result

ตัวอย่าง:

```text
dataset_2026-06-28
prompt_v1
embedding_multilingual_e5
index_v1
```

---

## 6. ก่อนปล่อยให้คนใช้

Checklist:

- [ ] มี testset
- [ ] ตอบจาก context เท่านั้น
- [ ] มี citation
- [ ] ถามนอกขอบเขตแล้วไม่เดา
- [ ] ไม่เปิดเผยข้อมูลส่วนตัว
- [ ] มี link ไปเว็บหลัก/ระบบจอง
- [ ] มี logging สำหรับ debug
- [ ] มีแผนอัปเดตข้อมูล

