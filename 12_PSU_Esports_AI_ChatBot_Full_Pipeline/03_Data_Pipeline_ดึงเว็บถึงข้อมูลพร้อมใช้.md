# 03 — Data Pipeline: ดึงเว็บถึงข้อมูลพร้อมใช้

Data pipeline คือขั้นตอนที่เปลี่ยนเว็บไซต์ให้กลายเป็นข้อมูลที่ AI ใช้ตอบได้

---

## 1. แหล่งข้อมูล

ใช้ข้อมูลจาก:

```text
https://esports.phuket.psu.ac.th/
https://esports.phuket.psu.ac.th/home
https://esports.computing.psu.ac.th/
```

หมวดหลัก:

- home/main
- reservation
- services
- competition
- training
- news
- knowledge
- about_us
- contact
- policies

---

## 2. Scrape

สิ่งที่ต้องดึง:

- URL
- title
- visible text
- headings
- links
- images
- fetched time

ผลลัพธ์:

```text
pages.json
```

---

## 3. Clean

ต้องลบ:

- navigation ซ้ำ
- footer ซ้ำ
- skip links
- report abuse
- page details
- whitespace ซ้ำ

ต้องคงไว้:

- เนื้อหาหลัก
- กฎ
- รายชื่อเกม
- ตารางเวลา
- URL
- heading

---

## 4. Classify Category

ใช้ URL path แบ่งหมวด เช่น:

| path | category |
|---|---|
| `esports.computing.psu.ac.th` | reservation |
| `/Services` | services |
| `/events-news/Activities` | competition |
| `/events-news/news` | news |
| `/Knowledge` | knowledge |
| `/Contact-Us` | contact |

---

## 5. Chunking

แบ่งข้อความเป็น chunk เพื่อทำ retrieval

ขนาดเริ่มต้น:

- 800-1500 ตัวอักษร
- overlap 100-200 ตัวอักษร

แต่สำหรับข้อมูล fact เช่นกฎจอง/รายชื่อเกม ควรทำ curated facts แยก ไม่พึ่ง chunk อัตโนมัติอย่างเดียว

---

## 6. Curated Facts

สำหรับเว็บนี้ curated facts สำคัญมาก

ควรทำเองในหัวข้อ:

- ตารางเวลาให้บริการ
- กฎการจอง
- เช็คอิน
- ยกเลิก/คืนเงิน
- ค่าปรับ
- รายชื่อเกม PC
- รายชื่อเกม PS5
- รายชื่อเกม Nintendo Switch
- รายชื่อเกม VR
- Cockpit
- ติดต่อ

ไฟล์:

```text
data/curated/faq_facts.jsonl
```

---

## 7. JSONL Schema

ควรมี field:

```json
{
  "id": "fact_ps5_games",
  "record_type": "curated_fact",
  "category": "services",
  "subcategory": "ps5_games",
  "tags": ["services", "games", "ps5"],
  "title": "เกมบน PlayStation 5",
  "url": "https://esports.computing.psu.ac.th/",
  "text": "PlayStation 5 มีเกม ..."
}
```

---

## 8. Data Quality Checklist

- [ ] ข้อมูลจองมีครบ
- [ ] รายชื่อเกมครบ
- [ ] มี URL อ้างอิง
- [ ] ไม่มีเมนูเว็บซ้ำปนเยอะ
- [ ] category ถูก
- [ ] chunk ไม่ยาวเกิน
- [ ] curated facts อ่านรู้เรื่อง
- [ ] มีข้อมูล contact
- [ ] มี policy ถ้าจะถาม privacy/security

---

## 9. Update Data

ควร scrape ใหม่เป็นรอบ:

- ทุกสัปดาห์ ถ้าเว็บอัปเดตบ่อย
- ทุกเดือน ถ้าข้อมูลนิ่ง
- ทันที เมื่อกฎจองหรือรายชื่อเกมเปลี่ยน

หลัง scrape ใหม่ต้อง:

1. regenerate jsonl
2. update curated facts ถ้ามีข้อมูลสำคัญเปลี่ยน
3. rebuild vector index
4. run eval

