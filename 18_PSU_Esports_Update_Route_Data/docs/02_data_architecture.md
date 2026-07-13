# Data Architecture

ระบบนี้ควรแยกข้อมูลเป็น 4 ชั้น เพื่อให้ debug ง่ายและไม่ปนกันระหว่างข้อมูลจริง, rule, vector chunk, และผลประเมิน

## 1. Raw Data

ใช้เก็บข้อมูลต้นฉบับ เช่น:

- เว็บที่ scrape มา
- PDF
- รูปภาพ Service Fee
- ข้อความจาก Facebook หรือประกาศ

ไฟล์ raw ไม่ควรถูกแก้ด้วยมือบ่อย เพราะต้องใช้ย้อนกลับไปตรวจว่า AI อ้างจากอะไร

## 2. Curated Facts

ใช้เก็บข้อเท็จจริงที่มนุษย์ตรวจแล้ว เช่น:

```json
{
  "id": "curated_opening_hours",
  "category": "hours",
  "title": "เวลาเปิดให้บริการ",
  "text": "วันจันทร์-พฤหัสบดี เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 ...",
  "source_url": "https://esports.computing.psu.ac.th/",
  "tags": ["hours", "open", "close"],
  "priority": 10
}
```

Curated facts เหมาะกับ RAG เพราะลด noise จาก web scraping และทำให้ retrieval ตรงขึ้น

## 3. Rule Patterns

ใช้กับ FAQ ที่คำตอบแน่นอน เช่น:

- เช็คอินล่วงหน้าได้กี่นาที
- จองล่วงหน้ากี่ชั่วโมง
- ไม่ชำระเงินภายใน 10 นาทีเกิดอะไรขึ้น
- วันศุกร์มี maintenance ช่วงไหน

ตัวอย่าง:

```json
{
  "id": "rule_checkin_advance",
  "category": "reservation",
  "intent": "checkin_advance_time",
  "patterns": ["เช็คอินล่วงหน้า", "checkin.*advance"],
  "answer_th": "เช็คอินได้ล่วงหน้าสูงสุด 30 นาที...",
  "source_ids": ["curated_checkin_30_minutes"],
  "priority": 100
}
```

ใน Update folder นี้ rule ถูกแยกเป็นไฟล์ตามหมวดใน `data/rules/`

## 4. Human Review Data

ใช้เก็บผลตรวจจากคนจริง เช่น AI ตอบครบไหม อ้างอิงถูกไหม route เหมาะไหม

ผล review นี้ควรเอากลับไปสร้าง:

- กฎใหม่
- alias ใหม่
- ground truth เพิ่ม
- curated fact เพิ่ม
- prompt guardrail ใหม่

## Format ที่ควรยึด

ทุก JSONL ควรมี:

- `id` ไม่ซ้ำ
- `category`
- `text` หรือ `answer_th`
- `source_url` หรือ `source_ids`
- `tags` ถ้าเป็น curated fact
- `priority` ถ้ามีการชนกันของคำตอบ

## ข้อควรระวัง

- ข้อมูลราคาต้องมีวันเริ่ม-วันหมดอายุ เพราะ Service Fee อาจเปลี่ยนได้
- PC ยังไม่มีราคาในภาพ Service Fee 2026 จึงไม่ควรคำนวณราคา PC แบบเดา
- วันศุกร์ต้องแยกเช้า/บ่ายให้ชัด เพราะช่วงบ่ายเป็น maintenance หรือปิดให้บริการตาม policy ที่มีอยู่
- ถ้าคำถามไม่ระบุกลุ่มผู้ใช้ ให้แสดงราคาทุกกลุ่มหรือถามกลับแบบมีตัวอย่างราคา
