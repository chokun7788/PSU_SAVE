# PSU Esports Chatbot - Next Issue Resolution Plan

วันที่: 2026-07-06

## ภาพรวม

ระบบตอนนี้ใช้งาน demo ได้แล้ว และ regression หลักล่าสุดผ่าน:

- GT360: 360/360 PASS
- Competition challenger v2: 369/369 PASS

ปัญหาที่เหลือไม่ใช่ระบบตอบมั่วทั้งระบบ แต่เป็น edge cases และ workflow รอบนอก เช่นคำถามพิมพ์ผิด, หลายคำถามในประโยคเดียว, memory, booking action, data freshness และ source metadata บางจุด

## ปัญหาและแนวทางแก้

### 1. คำถามพิมพ์ผิดหรือ wording แปลกแล้ว route หลุด

ตัวอย่างล่าสุด:

```text
ตอนนี้รายการแข่งมเกมอะไรบ้าง
```

เคยหลุดไป `events_news/news_lookup` แล้วตอบข่าว Tekken แทนรายการเกมแข่ง 4 เกม

แนวทางแก้:

- เพิ่ม typo/paraphrase patterns เฉพาะจุดใน router
- เพิ่ม ad-hoc test ทุกครั้งที่เจอคำถามจริงที่หลุด
- ถ้า pattern เริ่มเยอะ ให้ทำ normalization layer ก่อน router เช่นแก้คำติดกัน/สะกดผิดที่พบบ่อย
- ห้ามแก้แบบกว้างจนคำถามข่าวจริงหลุดไป competition list

Quality gate:

- reproduce คำถามจริง
- ตรวจ `route/mode/source`
- run ad-hoc เทียบกับคำถามใกล้เคียง
- ถ้าแก้ router ให้ run GT360 และ competition challenger v2

### 2. หลายคำถามในข้อความเดียว

ตัวอย่าง:

```text
วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่
```

ความเสี่ยง:

- router เลือกได้แค่ intent เดียว
- คำตอบอาจตอบแค่ครึ่งเดียว หรือดึงหมวดผิด

แนวทางแก้:

- ทำ multi-question splitter ก่อน pipeline หลัก
- แยกคำถามด้วยคำเชื่อม เช่น `แล้ว`, `กับ`, `และ`, `ส่วน`, `?`
- ส่งแต่ละคำถามเข้า pipeline เดิม
- รวมคำตอบแบบ answer-first เป็นข้อ ๆ
- จำกัดจำนวนคำถามต่อครั้ง เช่นไม่เกิน 3 ข้อ เพื่อคุม latency และความชัดเจน

Quality gate:

- test คำถามผสม schedule + price
- test คำถามผสม equipment + game catalog
- test คำถามผสม competition list + competition rule

### 3. ยังไม่มี conversation memory จริง

ตัวอย่าง:

```text
ผู้ใช้: VR ราคาเท่าไหร่
ผู้ใช้: แล้ว 1 ชั่วโมงล่ะ
```

ความเสี่ยง:

- คำถามที่สองไม่มี context ว่าหมายถึง VR

แนวทางแก้:

- เพิ่ม session state ฝั่ง web/API แบบ lightweight
- เก็บ intent/service/user_group ล่าสุด เช่น `service=vr`, `user_group=general_student`
- ใช้ memory เฉพาะกรณีคำถาม follow-up ชัด เช่น `แล้ว 1 ชั่วโมงล่ะ`, `ต่างกันเท่าไหร่`
- ถ้าไม่มั่นใจ ให้ถามกลับ ไม่เดา

Quality gate:

- memory ต้องไม่ทำให้ผู้ใช้คนละ session ปนกัน
- ต้องยังตอบ no-answer เมื่อ context ไม่พอ
- ไม่ใช้ memory ข้ามเรื่องมั่ว เช่นจาก VR ไป competition rule

### 4. Booking ยังเป็น Q&A ไม่ใช่ action จริง

ความจริงปัจจุบัน:

- ระบบตอบวิธีจองได้
- ระบบยังจอง/ยกเลิก/เช็ก slot จริงไม่ได้

แนวทางแก้:

- ระยะสั้น: คงคำตอบแบบให้คำแนะนำเท่านั้น
- เพิ่ม guard ห้ามตอบว่า `จองให้แล้ว` หรือ `ยกเลิกให้แล้ว`
- ระยะถัดไป: ถ้าจะทำ action จริง ต้องมี booking API หรือ admin workflow ที่ยืนยันจากศูนย์

Quality gate:

- คำถามเช่น `จองให้หน่อย` ต้องไม่ตอบว่าทำสำเร็จ
- คำถาม `ยกเลิกให้หน่อย` ต้องแนะนำขั้นตอนหรือบอกว่ายังทำ action ไม่ได้

### 5. ข้อมูลจริงอาจเก่าเมื่อเว็บ/ศูนย์เปลี่ยน

หมวดเสี่ยง:

- ราคา
- วันหยุดพิเศษ
- กติกา
- รายการเกม
- สถานะเปิดรับสมัครแข่งขัน

แนวทางแก้:

- เพิ่ม manual update checklist
- ทำ unanswered/stale-data log review รายสัปดาห์
- เพิ่ม field วันที่อัปเดตใน data สำคัญ
- ถ้าข้อมูลไม่มีหรือไม่แน่ใจ ให้ no-answer สุภาพ

Quality gate:

- validate data ทุกครั้งหลังแก้
- sample test หมวดที่แก้
- ถ้าเป็นราคา/schedule/competition ต้อง run regression ที่เกี่ยวข้อง

### 6. Source metadata บาง fast path ยังไม่สวย

ตัวอย่าง:

- ข้อความคำตอบบอก `แหล่งข้อมูล: data/competition_rules`
- แต่ `sources` object อาจยังมี fallback source อื่นปน

แนวทางแก้:

- เพิ่ม source id เฉพาะสำหรับ competition rules list
- ปรับ `HITS` หรือ `_answer()` ให้ส่ง source ที่ตรงกับคำตอบมากขึ้น
- ตรวจ source expectation ไม่ให้กระทบ ground truth เดิม

Quality gate:

- ad-hoc ตรวจ answer text และ sources object
- source ต้องไม่หลุดไป News เมื่อเป็น competition game list
- run GT360 หลังแก้ source metadata

## ลำดับแนะนำ

1. ทำ multi-question splitter เพราะช่วย UX ชัดที่สุด
2. ทำ typo/paraphrase normalization สำหรับคำถามที่เจอบ่อย
3. ปรับ source metadata ให้สะอาดขึ้น
4. ทำ unanswered/stale-data review workflow
5. ทำ lightweight session memory
6. ค่อยพิจารณา booking action เมื่อมี API หรือ policy จริงจากศูนย์

## Workflow ทุกครั้งที่แก้คำตอบผิด

```text
reproduce -> ดู route/mode/source -> หาสาเหตุ -> แก้เฉพาะจุด -> ad-hoc test -> regression ที่เกี่ยวข้อง -> ถ้าจะ deploy ให้ผู้ใช้กดเอง
```

หมายเหตุ: ตามคำสั่งล่าสุด ไม่ deploy อัตโนมัติ ให้หยุดที่พร้อม deploy และแจ้งผู้ใช้

