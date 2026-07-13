# Do-not-do และ Risk Register

ไฟล์นี้บอกข้อห้ามและความเสี่ยงที่ agent ใหม่ต้องระวัง

## Do Not Do

### 1. อย่าให้ LLM เดาข้อมูลสำคัญ

ห้ามเดา:

- ราคา
- กฎ
- ค่าปรับ
- วันหยุด
- สถานะการเปิดรับสมัคร
- booking slot
- payment/account

ถ้าไม่มีข้อมูล ให้ no-answer

### 2. อย่าแก้ตัวตรวจให้ผ่านง่ายขึ้น

ผู้ใช้ต้องการตัวตรวจรัดกุม

ถ้าคำตอบผิดแต่ตัวตรวจ PASS:

- แก้ evaluator/quality check ให้จับได้
- แก้คำตอบจริง
- ไม่ใช่ผ่อนเกณฑ์

### 3. อย่า deploy โดยไม่ test

ก่อน deploy:

- compile
- validate
- smoke test
- regression ที่เกี่ยวข้อง

หลัง deploy:

- test production `/api/chat`

### 4. อย่า copy data/model ใหญ่ขึ้น Vercel

Vercel ไม่เหมาะกับ:

- Ollama model
- vector DB ใหญ่
- log ถาวร
- long-running LLM

### 5. อย่า revert งานเดิมของผู้ใช้

repo มีหลายโฟลเดอร์ untracked/modified

ห้าม:

- git reset --hard
- git checkout -- .
- ลบโฟลเดอร์ที่ไม่ได้สร้างเอง

### 6. อย่าเชื่อ keyword PASS อย่างเดียว

ต้องดู answer จริงด้วย โดยเฉพาะ:

- ราคา
- schedule
- competition rules
- unknown game

### 7. อย่าตอบเหมือน action ทำได้ถ้ายังไม่มี API

เช่น:

- จองให้แล้ว
- ยกเลิกให้แล้ว
- เช็คสถานะให้แล้ว

ตอนนี้ยังทำ Q&A เท่านั้น

## Risk Register

### Risk 1: Route overlap

อาการ:

- คำถามเกมหลุดไป schedule
- คำถามกติกาหลุดไป game availability
- คำถามอุปกรณ์หลุดไป game catalog

วิธีลด:

- route order
- guard terms
- ad-hoc tests
- regression

### Risk 2: Data incomplete

อาการ:

- no-answer บ่อย
- ผู้ใช้คิดว่าระบบไม่ฉลาด

วิธีลด:

- ขอข้อมูลจริงจากศูนย์
- เพิ่ม curated facts
- เพิ่ม unanswered log review

### Risk 3: False pass

อาการ:

- test PASS แต่ตอบผิดจริง

วิธีลด:

- quality expectations
- direct answer checks
- human review sample
- stronger source/entity checks

### Risk 4: Production data stale

อาการ:

- เว็บ/ราคา/วันหยุดเปลี่ยน แต่ data local เก่า

วิธีลด:

- manual update workflow
- scheduled scraping/check
- admin update UI
- version/date in data

### Risk 5: Thai ambiguity

อาการ:

- นักเรียน มอ vs นักศึกษา มอ
- เด็ก สจล vs บุคคลทั่วไป
- เพลย์ห้า vs PS5

วิธีลด:

- alias/entity normalization
- ask-back only when truly ambiguous
- show multiple options when not enough info

### Risk 6: Vercel timeout/cold start

อาการ:

- API ช้า/timeout ถ้าเพิ่ม LLM หรือ data ใหญ่

วิธีลด:

- keep production fast path
- exclude heavy files
- external backend for LLM

### Risk 7: Log/privacy

อาการ:

- เก็บคำถามผู้ใช้โดยไม่มี policy

วิธีลด:

- anonymize
- clear retention
- do not log secrets
- use DB/policy if production real

## Red Flags in Answers

ถ้าเจอคำเหล่านี้ในคำตอบ อาจต้องตรวจ:

- `ยังไม่พบ เกมนี้`
- `ไม่ได้เปิด 24 ชั่วโมง` ในคำถามที่ไม่ได้ถาม 24 ชั่วโมง
- `ยังไม่ทราบกลุ่มผู้ใช้` ทั้งที่คำถามบอกกลุ่มแล้ว
- ตอบราคาบุคคลทั่วไปเมื่อถามเด็ก มอ
- ตอบฟรีเมื่อถามศิษย์เก่า/นักศึกษาทั่วไป
- ดึง CS2 มาตอบ Minecraft
- ดึง schedule มาตอบ Roblox
- ดึงข่าว Tekken มาตอบ “มีเกมแข่งอะไรบ้าง”
- ตอบค่าปรับโดยไม่มีข้อมูล

## Safe Fix Pattern

เมื่อต้องแก้:

```text
small change
-> ad-hoc test
-> relevant regression
-> inspect answer
-> report/log
```

อย่าแก้ทีละหลายหมวดถ้าไม่จำเป็น

