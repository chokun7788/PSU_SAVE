# Intent-trap bilingual 1,000: คำถามแบบที่เคยตอบผิดในหน้าเว็บ

## ขอบเขต

- สร้าง 100 สถานการณ์ต่อภาษา x 5 รูปแบบการถาม = ไทย 500 + อังกฤษ 500 ข้อ แยก 10 หมวด หมวดละ 50 ข้อต่อภาษา
- ชุดนี้เป็น `scenario_curated_paraphrase_pending_review` ไม่ใช่ 1,000 เจตนาอิสระหรือ Gold ที่มนุษย์อนุมัติครบ
- รัน Flow จริงด้วย `--allow-llm --rag-fallback` วันที่ 24 ก.ย. 2026 โดยไม่เขียนทับผลเดิม
- Corpus v1 ที่ใช้รัน: `data/eval/intent_trap_bilingual_1000_v1.jsonl`; corpus v2 แก้ *เฉพาะเกณฑ์ประเมิน* ที่ route ตัวตน/คำทักทาย ไม่เปลี่ยนข้อความคำถามหรือคำตอบที่บันทึก
- Raw: `reports/master_ground_truth_eval/master_gt_eval_20260924_134028.json`
- Offline rescore: `reports/master_ground_truth_eval/master_gt_eval_20260924_134028_intent_trap_rescored_v2.json`; ไม่ได้รัน Pipeline ครั้งที่สอง

## ผลที่อ่านได้อย่างถูกต้อง

| กลุ่ม | ไทย | อังกฤษ | รวม |
|---|---:|---:|---:|
| ผ่านเกณฑ์อัตโนมัติ | 112 | 55 | 167 |
| ไม่ผ่านเกณฑ์อัตโนมัติ | 211 | 266 | 477 |
| ต้องตรวจความหมายโดยคน | 127 | 134 | 261 |
| ตัดสินสถานะสดไม่ได้ เพราะ Dashboard ไม่พร้อม | 50 | 45 | 95 |

คะแนนดิบของ evaluator ก่อนแก้ Gold คือ 406/1,000 แต่มี false fail เช่น `who r u` ตอบตัวตนถูกแล้วแต่ route `knowledge` ไม่อยู่ในรายการที่คาด และมี false pass เช่น `INTENT-TRAP-TH-0201` ถามว่า *นำอาหารเข้าได้ไหม* แต่ตอบเพียง *รับประทานได้เฉพาะพื้นที่กำหนด* จึง **ห้ามตีความ 406 หรือ 167 ว่าเป็นอัตราคำตอบถูกจริง** กลุ่มที่ต้องตรวจด้วยคนอยู่ใน `reports/master_ground_truth_eval/master_gt_eval_20260924_134028_intent_trap_manual_review_v2.jsonl`.

## ผลแยกหมวดที่ต้องจัดการก่อน

| หมวด | ไทยผ่าน/50 | อังกฤษผ่าน/50 | สิ่งที่พบ |
|---|---:|---:|---|
| วัน/เวลาที่จองได้ | 10 | 0 | ตอบขั้นตอนจองแทนตาราง, บางข้อไป Live Dashboard ทั้งที่ถามตารางปกติ |
| ความรับผิดชอบเมื่ออุปกรณ์เสียหาย | 29 | 5 | อังกฤษจับ `PS5`, `game`, `controller` ไป Games/Equipment ก่อนกฎค่าปรับ |
| ราคาที่ยังไม่ระบุบริการ | 34 | 15 | อังกฤษไป Equipment Catalog หรือ Member Lookup แทนการถามบริการ/ระยะเวลา |
| รับประทานอาหารในพื้นที่ | 19 | 20 | มีข้อมูลเรื่องพื้นที่ที่กำหนด แต่ route หลุดหรือไม่เจอกฎ |
| ตัวตนบอท/คำผิดเล็กน้อย | 20 | 15 | บางรูปแบบตอบได้ บางรูปแบบ no-answer; `who r u` เป็นตัวอย่างที่ *ตอบถูก* หลังแก้ Gold |
| Slot ตามชื่อวัน | 0 | 0 | 95 ข้อ Dashboard ไม่พร้อมจึงตัดสิน slot ไม่ได้; อีก 5 ข้ออังกฤษตอบตารางศุกร์แทน VR slot |

กลุ่มบุคคลภายนอก สิทธิ์ใช้อุปกรณ์ การนำอาหารเข้า และข้อความกำกวม มีรวม 400 ข้อ เกณฑ์ปัจจุบันตรวจได้เพียง route/คำต้องห้าม: 139 ข้อเห็นข้อผิดพลาดได้อัตโนมัติ อีก 261 ข้อต้องอ่านความหมายและหลักฐานด้วยคน

## ตัวอย่างหลักฐานรายข้อ

1. `INTENT-TRAP-EN-0001` ถามค่าบริการสำหรับคนนอก แต่ตอบรายการอุปกรณ์ (`structured_equipment_catalog_en`)
2. `INTENT-TRAP-EN-0051` ถามวันและเวลาที่จองได้ แต่ตอบขั้นตอนจอง (`rule_en`)
3. `INTENT-TRAP-EN-0151` ถามค่าปรับกรณี PS5 เสียหาย แต่ตอบไม่พบเกมชื่อ `penalty` (`games_unknown_target_en`)
4. `INTENT-TRAP-EN-0401` ถามว่าคนนอกใช้อุปกรณ์ได้ไหม แต่ตอบรายการอุปกรณ์ทั้งหมด (`structured_equipment_catalog_en`)
5. `INTENT-TRAP-EN-0346` ถามว่า VR slot วันศุกร์ 10:00 ว่างไหม แต่ตอบเพียงศูนย์เปิดเช้า (`structured_schedule_en`); เปิดศูนย์ไม่ได้แปลว่า slot ว่าง
6. `INTENT-TRAP-TH-0201` ถูกนับผ่านใน raw score ทั้งที่คำตอบเรื่อง *รับประทาน* ไม่ยืนยันเรื่อง *นำเข้า*; ต้อง human adjudication

ตัวแปลงวันที่ยังไม่รองรับชื่อวัน: เมื่อจำลองวันที่อ้างอิง 2026-09-24 คำถาม `วันจันทร์มี PC เครื่องไหนว่างบ้างตอนบ่ายโมง` ให้ `resolve_date_from_text() = None` และ `resolve_live_target_date() = 2026-09-24` แทนวันจันทร์ 2026-09-28 ข้อนี้ตรวจได้จาก unit-level function แม้ Dashboard ไม่พร้อม

## Latency และข้อจำกัด

- ไทย 500 ข้อ: P50 0.551s, P95 11.086s, P99 20.758s, Max 30.029s; 31 ข้อเกิน 10s และ 7 ข้อเกินเพดานทดสอบ 20s
- อังกฤษ 500 ข้อ: P50 0.062s, P95 0.472s, P99 0.846s, Max 2.152s; ไม่มีข้อเกิน 10s
- `global_timeout_sec=20` ยังไม่ใช่ hard deadline: `INTENT-TRAP-TH-0052` ใช้ 30.029s แล้วจบแบบ timeout no-answer
- Dashboard ไม่พร้อมเป็นเงื่อนไขภายนอกของรอบนี้; การตอบว่าเช็กสดไม่ได้ปลอดภัยกว่าการเดา แต่ยังไม่ทดสอบความถูกต้องของวัน/เครื่อง/slot ได้ ต้องใช้ fake snapshot ใน integration test แล้วทดสอบกับ Dashboard จริงอีกครั้ง
- String/route contract ไม่วัดว่าข้อเท็จจริงครบ ตรงประเด็น และอ้างแหล่งข้อมูลถูก ต้อง review คำตอบ 261 ข้อ และตรวจ Gold ที่เหลือก่อนอ้าง production accuracy

## ลำดับแก้ที่แนะนำจากผล

1. สร้าง Question Frame ที่ล็อก `requested_facet` ก่อนเรียก handler: fee, booking schedule, eligibility, damage responsibility, food bringing/consumption และ live slot ห้ามคำว่าอุปกรณ์/จอง/PS5 แย่งเจตนาหลัก
2. รองรับชื่อวันใน date resolver พร้อม `target_date`; ถ้าระบุวันแล้ว resolve ไม่ได้ ห้ามใช้วันนี้เป็นค่าเริ่มต้น ตรวจว่าคำตอบ live อ้างวัน/เวลา/เครื่องเดียวกับคำถาม
3. แยก `opening_hours` ออกจาก `slot_availability` และ `booking_howto`; ตอบสถานะ slot จาก Dashboard เท่านั้น ถ้าไม่พร้อมให้แจ้งว่าเช็กไม่ได้
4. Route ความเสียหาย/ค่าปรับเข้า verified penalty policy ก่อน Game Catalog ทั้งสองภาษา; English generic damage wording ต้องใช้หลักฐานที่มี ไม่ปล่อย RAG draft ที่ยังไม่ผ่านการอนุมัติ
5. ทำ Answer Contract เช็กว่าตอบ *สิ่งที่ถาม* โดยเฉพาะ `bring` vs `eat`, `allowed to use` vs `equipment list`, `studio open` vs `station free`; ซ่อน `โหมดทดลอง RAG` จากคำตอบผู้ใช้
6. ทดสอบ focused 10 หมวดซ้ำก่อน Full Run และเพิ่ม integration test ด้วย fake Dashboard เพื่อปลด blocked 95 ข้ออย่างวัดผลได้

## คำสั่งรันซ้ำ

```powershell
python -X utf8 tools/build_intent_trap_ground_truth_1000.py
python -u -X utf8 tools/run_master_ground_truth_eval.py --corpus data/eval/intent_trap_bilingual_1000_v2.jsonl --allow-llm --rag-fallback
python -X utf8 tools/analyze_intent_trap_eval.py <path-to-new-detail.json> --corpus data/eval/intent_trap_bilingual_1000_v2.jsonl
```

การรันข้ามวันต้องสร้าง corpus ใหม่ก่อน เพื่อให้ expected date ของคำถามตามชื่อวันสัมพันธ์กับวันอ้างอิง
