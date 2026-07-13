# Requirements and Acceptance Criteria

ไฟล์นี้สรุป requirement แบบชัดเจนสำหรับ agent ใหม่ ว่า “ระบบที่ดี” ในมุมผู้ใช้ต้องเป็นอย่างไร

## Functional Requirements

### FR1: ตอบ FAQ ของศูนย์ได้

ต้องตอบ:

- ศูนย์คืออะไร
- ตั้งอยู่ที่ไหน
- ติดต่อยังไง
- เปิดปิดกี่โมง
- จองยังไง
- เช็คอินยังไง
- กฎทั่วไปคืออะไร

Acceptance:

- คำตอบมีข้อมูลจริง
- มีแหล่งข้อมูล
- ไม่ยาวเกินจำเป็น

### FR2: ตอบราคาได้ถูกต้อง

ต้องตอบราคาตาม Service Fee 2026

Acceptance:

- ถ้ารู้กลุ่มผู้ใช้ ตอบราคากลุ่มนั้นก่อน
- ถ้าไม่รู้กลุ่ม แสดงทุกกลุ่ม
- ถ้าข้อมูลราคา service นั้นไม่มี ต้องไม่คำนวณมั่ว
- ต้องมีหน่วยเวลา/session

### FR3: ตอบเวลาเปิดปิดและวันหยุดได้

Acceptance:

- แยกวันจันทร์/อังคาร-พฤหัส/ศุกร์
- แยก morning/afternoon
- วันหยุดพิเศษ override ตารางปกติ
- คำว่า “วันนี้” ใช้ Asia/Bangkok

### FR4: ตอบเกมและอุปกรณ์ได้

Acceptance:

- ถามโซน -> ตอบโซน
- ถามอุปกรณ์ -> ตอบอุปกรณ์
- ถามเกมในโซน -> ตอบเกมในโซน
- ถามเกมที่ไม่มี -> no-answer แบบมีรายการเกมที่ยืนยันได้

### FR5: ตอบกติกาการแข่งขันได้

Acceptance:

- แยกเกมถูก
- อ้างกติกาถูก
- ตอบคำตอบก่อน
- ถ้าไม่มีในกติกา ไม่เดา

### FR6: มี route/mode/source ให้ debug

Acceptance:

- API response มี `mode`
- มี `route_category`
- มี `route_intent`
- มี `sources`
- latency

### FR7: Deploy demo ได้

Acceptance:

- Vercel production เปิดได้
- `/api/health` ok
- `/api/chat` ตอบได้
- หน้าเว็บถามตอบได้

## Non-functional Requirements

### NFR1: เร็ว

เป้าหมาย:

- Rulebase/fast path: ต่ำกว่า 1 วินาที
- RAG/LLM fallback ถ้ามีในอนาคต: ไม่เกิน 10 วินาที

### NFR2: ฟรีหรือประหยัด

ต้องเน้น:

- Local
- Rulebase
- RAG-lite
- Vercel free/demo

หลีกเลี่ยง:

- API LLM เสียเงินสำหรับ production MVP

### NFR3: ไม่ hallucinate

ห้าม:

- แต่งค่าปรับเอง
- แต่ง booking API เอง
- แต่งสถานะเปิดรับสมัครแข่งขันเอง
- ตอบเกมที่ไม่มีว่าเล่นได้

### NFR4: Maintainable

ควร:

- แยก data เป็น JSONL
- แยก route
- มี test
- มี daily log
- มี handoff summary

### NFR5: Deployable

ต้อง:

- copy/sync ไป deploy folder ได้
- compile ผ่าน
- deploy Vercel ได้

## Definition of Done สำหรับการแก้หนึ่งปัญหา

ถือว่าเสร็จเมื่อ:

1. reproduce ปัญหาได้
2. รู้สาเหตุ
3. แก้โค้ด/data เฉพาะจุด
4. เพิ่ม ad-hoc test หรือ ground truth
5. compile ผ่าน
6. validate ผ่าน
7. run regression ที่เกี่ยวข้อง
8. อ่านคำตอบจริงอย่างน้อย sample สำคัญ
9. update report/log ถ้าเป็นงานใหญ่
10. ถ้า deploy ต้อง test production

## Quality Gates

ก่อนตอบว่าพร้อม:

```text
py_compile OK
validate_update OK
ad-hoc OK
GT360 OK ถ้าแก้ core route/price/schedule/game
competition challenger OK ถ้าแก้ competition/game route
production API OK ถ้า deploy
```

## Failure Severity

### Critical

- ตอบราคาผิด
- ตอบกฎผิดจนลูกค้าเข้าใจผิด
- บอกเล่นได้ทั้งที่ไม่มีข้อมูล
- ดึงกติกาคนละเกมมาตอบ
- เว็บ production ใช้งานไม่ได้

### Major

- route ผิดแต่คำตอบพอเกี่ยว
- ตอบไม่ครบจนสับสน
- source ผิด
- no-answer ทั้งที่มีข้อมูล

### Minor

- คำตอบยาวไป
- เรียงประโยคไม่สวย
- source ซ้ำ
- รายละเอียดน้อยไปเล็กน้อย

## Review Rubric ที่เคยคุย

คะแนน:

```text
4 = ดีแล้ว ใช้จริงได้ ตอบตรง อ่านง่าย
3 = ถูก แต่ยังเรียงคำตอบ/เติมรายละเอียดได้อีกนิด
2 = มีส่วนถูก แต่ทำให้ลูกค้าเข้าใจผิดได้
1 = ตอบผิดเป็นหลัก แต่ยังเกี่ยวข้องนิดหน่อย
0 = ผิด/มั่ว/ไม่มีข้อมูลแต่ตอบเหมือนมี
```

Decision:

```text
pass = ผ่าน ใช้ได้เลย
minor_fix = ถูก แต่ควรปรับคำพูด/เรียงคำตอบ
major_fix = ผิดประเด็น ผิดราคา ผิดกฎ หรือเสี่ยงเข้าใจผิด
needs_data = ไม่มีข้อมูลจริง ต้องขอข้อมูลเพิ่ม
needs_policy = ต้องถามศูนย์/ผู้ดูแล เพราะเป็นเรื่องกฎหรือนโยบาย
```

