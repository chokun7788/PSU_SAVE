# ผล Implement Flow แก้ Intent Trap ไทย/อังกฤษ

วันที่: 2026-09-24  
เอกสารต้นทาง: `docs/97_intent_trap_bilingual_remediation_flow_20260924.md`  
สถานะ: แก้และตรวจเฉพาะ P0/P1 ที่ระบุด้านล่าง; **ยังไม่ผ่านเกณฑ์ production-ready ทั้ง Flow**

## 1. หลักฐานและวิธีอ่านตัวเลข

- Corpus: `data/eval/intent_trap_bilingual_1000_v2.jsonl` (SHA-256 `acc001627588b3562b7874e011a0e626a4867ed99da89dc3d2902ec7a3d810e9`)
- ผลดิบรอบสุดท้าย: `reports/master_ground_truth_eval/master_gt_eval_20260924_195543.json` (SHA-256 `cf403ab80a9927289b50e2fb3443542930f330b5e484fcddae2d603d4d30e237`)
- ผลแยกสถานะ: `reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_rescored_v2.json`
- คิวอ่านคำตอบด้วยคน: `reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl`
- ชุดหลักแบบสุ่ม 5 ข้อ/หมวด/ภาษา: `reports/master_ground_truth_eval/master_gt_eval_20260924_191717.json` (checkpoint ก่อนแก้ route เพิ่ม)

| รอบ | ผ่านอัตโนมัติ | ไม่ผ่านที่ตรวจยืนยันได้ | ต้องอ่านคำตอบ | ติด Dashboard สด |
|---|---:|---:|---:|---:|
| Baseline ที่บันทึกในเอกสาร 97 | 167 | 477 | 261 | 95 |
| รอบสุดท้าย 1,000 ข้อ | 500 | 0 | 400 | 100 |

ตัวรันดิบรายงาน 900/1,000 เพราะนับกรณี route-only เป็นผ่านด้วย ตัวเลขนั้น **ไม่ใช่ accuracy 90%**; 400 ข้อมีสถานะ manual review และ 100 ข้อไม่มีข้อมูลจองสดให้ตัดสิน การเพิ่ม blocked จาก 95 เป็น 100 เกิดจากคำถาม VR วันศุกร์ 5 สำนวนที่เคยไปตอบตารางคงที่ ตอนนี้เข้าทาง live lookup ที่ถูกต้อง แต่ปลายทางยังไม่พร้อม

เวลาในรอบสุดท้ายวัดที่ pipeline แบบเรียงคำถาม: P50 `0.042s`, P95 `0.625s`, P99 `2.143s`, Max `2.200s`; ไม่มีข้อเกิน 10 หรือ 20 วินาที **ยังไม่ใช่การยืนยัน HTTP ceiling ภายใต้ concurrent load**

## 2. สิ่งที่แก้และตรวจแล้ว

| หัวข้อใน Flow 97 | สิ่งที่ทำ | หลักฐาน |
|---|---|---|
| A1 segmentation | ไม่ตัด `กับ` กลางคำ `เกี่ยวกับ`; ตัดเฉพาะ preface/suffix ที่เป็นคำกำกับรูปแบบและไม่ถือ target/date | `app/pipeline/engine.py`, `app/pipeline/protected_intents.py`; tests |
| A2-D3 protected facets | แยกค่าบริการที่ไม่ระบุโซน, ราคาที่ระบุ PS5, สิทธิ์คนนอก, กฎความเสียหาย, อาหารนำเข้า vs รับประทาน, ตารางจองรายสัปดาห์, คำขอแต่งข้อมูล/แนะนำหุ้น ก่อน catalog handler | `app/pipeline/protected_intents.py`, `app/core/customer_group.py`; focused 1,000 |
| B1-B2 live date/target | ชื่อวันเปล่าหมายถึงครั้งถัดไป; วันเดียวกับวันนี้ไม่ถูกชี้เป็นวันนี้โดยเงียบ ๆ; ปฏิเสธ JSON Dashboard ที่ตอบคนละวัน; คำตอบสั้นแสดงวันที่/เวลาอัปเดต/แหล่งข้อมูล; ไม่ขยาย Nintendo หมายเลข 2 เป็นทั้งโซน | `app/booking/live_status.py`; Dashboard จำลอง 100/100 ตรวจวันที่ request/response |
| E3 fallback safety บางส่วน | Direct RAG ที่ไม่ยืนยันหลักฐานจบเป็น no-answer ไม่คัดลอกข้อความใกล้เคียงหรือแสดงชื่อรหัสเอกสารภายใน | `app/pipeline/experimental_fallback.py`, `app/pipeline/engine.py`; regression tests |
| F identity/greeting | สำนวนตัวตนอังกฤษที่หลากหลายยังตอบได้โดยไม่แย่งคำถาม `What equipment ... Could you...`; คำทักทายไทยลากอักษรจบด้วย fixed greeting; `hello what games do you have` ไม่ถูกตัดเหลือแค่ทักทาย | `app/pipeline/chatbot_identity.py`, `app/pipeline/router.py`, `app/pipeline/bilingual_english.py`, `app/runtime/fast_answer.py` |
| G1 targeted rerun | Runner เลือก failed IDs จาก raw/rescore โดยไม่เขียนทับไฟล์เก่า | `tools/run_master_ground_truth_eval.py`; 37 ข้อผิดเดิมและ 20 ข้อ regression ที่พบระหว่างแก้ผ่านการ rerun เฉพาะข้อ |

ชุด regression ที่เกี่ยวข้องผ่าน 52 tests. Dashboard จำลองตรวจ **วันที่ที่เรียกและวันที่ที่แสดง** ครบ 100 สำนวน ไม่ใช่การรับรองว่าสถานะว่าง/จองของแต่ละเครื่องถูกต้องจาก WordPress จริง. ชุด `unclear_or_outside_scope` 100 ข้อหลังตัดคำกำกับรูปแบบผ่านตัวตรวจดิบทั้งหมด, สูงสุด `2.816s` เทียบกับก่อนแก้ที่มีเคส `17.931s`.

## 3. สิ่งที่ยังไม่ผ่านหรือยังพิสูจน์ไม่ได้

1. **400 manual-review**: สิทธิ์คนนอก 100, สิทธิ์ใช้อุปกรณ์ 100, การนำอาหารเข้า 100, คำถามกำกวม/นอกขอบเขต 100. ตัวอย่างที่ตรวจด้วยตาไม่เห็นการฟันธงสิทธิ์หรืออนุญาตนำเข้าจากหลักฐานคนละ facet แต่ยังไม่มี human adjudication ของทุกคำตอบ/ทุกสำนวน จึงห้ามเปลี่ยนเป็น pass อัตโนมัติ.
2. **100 live-dashboard blocked**: adapter ไม่ได้ข้อมูลจริงในรอบนี้. Fake Dashboard ยืนยันวันครบ 100 ข้อ แต่ยังต้องตรวจ resource, slot start/end, booked/free, maintenance, stale snapshot และ privacy สำหรับทั้ง 100 ข้อด้วย fixture ที่ล็อก expected facts; หลังจากนั้นต้องทดสอบ WordPress จริง.
3. **ชุดหลัก 10,000 ยังไม่รันเต็มหลังแก้**: sample checkpoint 105/120 โดยตัวตรวจดิบ. รันซ้ำ 15 ข้อที่ผิดหลังแก้ route ได้ 6/15 ผ่าน; อีก 9 ข้อยังไม่ผ่านอัตโนมัติ. ห้ามอนุมาน sample เป็นผล 10,000.
4. **English content ที่รออนุมัติจริง**: 5 ตัวอย่างกฎการแข่งขันอังกฤษและ 1 คำถามอุปกรณ์ Logitech G923 จบ `localization_pending` เพราะ `data/locales/en/approved_localizations.jsonl` ยังว่าง. ห้ามเปิดคำแปลร่างโดยเปลี่ยนสถานะเป็น approved เอง.
5. **Gold/source conflict 3 ข้อใน sample**: `EN-04651` ถามตำแหน่ง referee แต่ไม่พบ record ที่ยืนยัน, `TH-03931` คำถามนำอาหารเข้าแต่ Gold คาด answer ทั้งที่ source ยืนยันเพียงพื้นที่รับประทาน, `TH-04851` มีเพียงคำว่า `เกม` แต่ Gold คาด clarification แทนรายชื่อเกม. ให้ reviewer ตัดสิน source และ expected status ก่อนแก้ตัวตอบหรือเปลี่ยน Gold.
6. **สถาปัตยกรรม Flow 97 ยังไม่ครบ**: ยังไม่ได้ย้ายทุก handler ไป `RequestPlan`/typed `AnswerDraft`, ยังไม่ได้ทำ facet/source-version validator ครอบทุก route, ยังไม่ได้ LLM intent-review JSON ที่บังคับ schema และ evidence-span ครบ, และยังไม่ได้ parent-owned stage trace/HTTP concurrent load test.
7. **การนำขึ้นใช้จริงยังไม่ยืนยัน**: ไม่ได้ rebuild owner delivery folder หรือทดสอบเครื่องเจ้าของในรอบนี้; แก้ใน source repository ปัจจุบันเท่านั้น. `0 >20s` เป็นผล serial pipeline ไม่ใช่ guarantee ของ Web API, worker restart หรือ 30 users.

## 4. ลำดับทำต่อโดยไม่ลดเกณฑ์

1. ให้ reviewer อ่าน 400 รายการใน manual queue แบบจับคู่คำตอบกับแหล่งข้อมูล: facet, target, ข้ออ้างที่ยืนยันได้, locale และสถานะ safe abstention. เก็บ decision/reviewer/reason แยกจาก raw run; อย่าแก้ label เพื่อดันคะแนน.
2. สร้าง fixture Dashboard 100 กรณีที่มี expected `date + zone/station + exact slot + booking state + snapshot timestamp`; ตรวจ answer contract รายข้อ. เพิ่มเคส Nintendo/VR ที่เป็นชื่อรอบแทนเลขเครื่อง. จากนั้นทดสอบกับปลายทาง WordPress จริงและกรณีข้อมูลเก่า/คนละวัน.
3. ส่งคำแปลอังกฤษ 5 กฎการแข่งขันและคำอธิบายอุปกรณ์ให้ reviewer อนุมัติพร้อม `source_text_sha256`; เมื่อ approved จึง publish overlay แล้ว rerun failed IDs. ตรวจ Gold 3 ข้อที่ source ยังไม่ยืนยันแยกก่อน.
4. ทำ `RequestPlan`/`AnswerDraft` และ source-version contract แบบค่อย ๆ migrate handler: เริ่ม fee, eligibility, food, competition แล้วทดสอบ positive/negative controls; LLM ใช้จำแนก intent เฉพาะเมื่อ route สูสี และห้ามโมเดลสร้าง facts.
5. รันเต็ม 5,000 ไทย + 5,000 อังกฤษ, HTTP 5/10/20/30 users, P95/Max และ hard 20s ที่ client; ตรวจ source-grounded accuracy, worker crash, privacy log และ owner package หลังทุกขั้น.

## 5. คำสั่งทวนผล

```powershell
python -m unittest tests.test_intent_trap_protected_flow tests.smoke_test_live_booking_status tests.test_master_ground_truth_route_regressions -q
python -u -X utf8 tools/run_master_ground_truth_eval.py --corpus data/eval/intent_trap_bilingual_1000_v2.jsonl --allow-llm --rag-fallback
python -X utf8 tools/rescore_intent_trap_eval.py reports/master_ground_truth_eval/<raw-run>.json --corpus data/eval/intent_trap_bilingual_1000_v2.jsonl
python -u -X utf8 tools/run_master_ground_truth_eval.py --corpus data/eval/master_ground_truth_bilingual_10000_v2.jsonl --failed-ids-from reports/master_ground_truth_eval/master_gt_eval_20260924_191717.json --allow-llm --rag-fallback
```

ทุกรอบสร้างไฟล์ผลใหม่ ห้ามเขียนทับผลก่อนหน้า. การเปรียบเทียบ score ต้องระบุว่าเป็น raw evaluator, offline rescore, human reviewed หรือ external blocked เสมอ.
