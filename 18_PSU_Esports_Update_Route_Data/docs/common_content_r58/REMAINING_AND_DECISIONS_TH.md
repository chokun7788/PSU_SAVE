# งานที่ยังเหลือและข้อมูลที่ต้องตัดสินใจ

## P0 — ข้อเท็จจริงก่อนเผยแพร่

1. ร่าง 41 รายการยังไม่อนุมัติจริง ต้องตรวจการ map, English, relations และ validity ไม่ให้เครื่องลงนามแทนคน ตารางเดิมยังทำงานผ่าน legacy adapter
2. ข้อมูลเดิม canonical 270 รายการ มี mapping games 36 รายการ และเพิ่มร่างอ้างหลักฐาน 5 รายการ คิว canonical อีก 234 รายการยังรอ typed migration (270−36) ไม่มีการเติมคำตอบจากการเดา ดู migration_queue.json ส่วน draft 41 ไม่ใช่ 41 จาก 270 ทั้งหมด
3. ราคา/เหมาไม่มีวันมีผลยืนยันในบาง source: ถามเจ้าของเจาะจงว่า “ราคาใน workbook รุ่นนี้เริ่มใช้วันที่เท่าไร มีวันสิ้นสุดหรือไม่ และใช้กับกลุ่มใด?” ห้ามใช้วันที่ไฟล์แก้ไขแทนวันมีผล
4. กฎ Tekken/ข้อมูล RoV ที่ขัดกันหรือไม่ครบ: ระบุไฟล์ รุ่นงานแข่งขัน และข้อความข้อที่ขัดกันในคิว review อย่า merge ต่างเกมเป็นชุดเดียว
5. นโยบายที่ยัง unknown ต้องถามเป็นรายข้อ เช่น เวลาที่หายเพราะเกมอัปเดตมีชดเชยหรือไม่/ขั้นตอนอย่างไร ไม่ใช้ schema เติมคำตอบ

## P1 — งานที่ระบบทำต่อเองได้

- Typed migration ที่เหลือพร้อม lineage จากไฟล์เดิม เขียน mapper ตามหมวดและตรวจ unknown/semantics แบบไม่ publish อัตโนมัติ
- ต่อ calculator กับ rate/calculation_rule/rental แบบ amount_minor รวม rounding, eligibility, duration, minimums ตอนนี้ V3 ตอบข้อมูลเรทที่ประกาศได้ แต่ยังไม่ได้แทนสูตรคิดค่าใช้บริการทุกแบบของ legacy
- ต่อ calendar engine ให้ใช้ schedule+closure precedence เดียว ตรวจวันพิเศษ/maintenance/all zones และช่วงขอบเวลา ตอนนี้ typed validator ตรวจข้อมูลได้ แต่ runtime calendar เดิมยังเป็น operational adapter
- ต่อ live_binding กับ WordPress physical pool/version/freshness adapter โดยไม่ใช้ static records เป็น occupancy; ความถูกต้องสดที่ผู้ใช้ยืนยันก่อนหน้าแยกจาก schema tests รอบนี้
- เพิ่ม semantic record retrieval เมื่อคำถามไม่กล่าวชื่อ/หมวดชัดเจน ตอนนี้ V3 เน้นชื่อจากข้อมูล, schema fields, generic location/contact/schedule selectors และ bounded planner ไม่อ้างว่า arbitrary wording ทุกแบบผ่านแล้ว
- เพิ่ม batch publish UI / migration comparison UI / conflict evidence editor ตอนนี้ API รองรับ batch แต่ปุ่มหน้าเว็บ publish รายการที่เลือกทีละตัว
- English labels ของ fields แสดง canonical key ที่อ่านได้ และ fallback Thai source เมื่อไม่มี EN; ยังควรทำ glossary และ review เฉพาะ policy semantics ก่อนเปลี่ยนข้อเท็จจริง
- ทดสอบ optional LLM field planner เพิ่มด้วย paraphrases ที่ held out; model format valid ไม่เท่ากับเลือก field ถูก ให้ดู method/obligations ใน log
- ทดสอบจำนวนคนใช้งานพร้อมกันและ isolation ของ admin ถ้าจะขยายเกิน local operator รอบนี้ไม่ได้รัน load/full GT test 2 หมื่นเคส

## ข้อจำกัดที่ไม่ควรถูกตีความว่าผ่านแล้ว

24 types validate/publish ได้ใน fixtures ไม่ได้หมายความว่าทุกหมวด migrate ข้อมูลจริงและมี operational adapter ครบ รายการ “ทั้งหมด” ใน V3 มีขอบเขต published common catalog และไม่รวม legacy ที่ยังรอย้าย ความพร้อมของ owner editor แยกจาก correctness ของข้อมูลจริง, การแปลเชิงนโยบาย, live occupancy และ concurrency

ชุดทดสอบใหม่ใช้ข้อมูลสมมุติที่ผลแน่นอน ฐานใช้งานไม่ได้เผยแพร่ชื่อ Starfish Quest/Coral Trail ไม่มีการทับข้อมูล owner JSON หรือ log เดิม
