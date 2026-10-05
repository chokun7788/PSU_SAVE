# Flow r29 — ตรวจ input guard จากบริบทและหลักฐานราย span

## เป้าหมายและข้อจำกัด

แก้ false rejection 31 ข้อ โดยรักษา true-layout controls 5 ข้อ ไม่ปิด guard ไม่เพิ่ม alias ทั้งประโยค ไม่แก้ Gold/ต้นฉบับ/นโยบาย. การผ่าน guard ไม่ใช่คำตอบถูก ต้องตรวจ route/คำตอบแยกหลังปลดการหยุด. เว็บใช้อยู่ r28 บน8090จนกว่ารุ่นใหม่จะผ่าน actual HTTP

## ขั้นตอน

1. Freeze 36 cases จากชุดเก่า พร้อม clean/noisy/metadata/expected outcome และ features/span/raw mapping/score ทั้งหมด. แยก keyboard_layout tags ก่อนถือว่าเป็น false rejection
2. วิเคราะห์ทุก source span: normalization ลบเลข/เครื่องหมายจาก mapped candidate จนเหลือ 1–2 ตัวอักษรหรือไม่, target_quality ดีกว่า source จริงหรือไม่, มี lexical neighbor ของคำอังกฤษในบริบทประโยคหรือไม่
3. ลดหลักฐาน layout ที่อ่อน: mapped English ต้องมีรูปแบบภาษาอังกฤษพอ, source ที่แข็งแรงกว่า mapping ไม่ใช่หลักฐานการแก้, Thai span ที่อ่านได้และ mapped target ไม่ใช่คำอังกฤษต้องไม่ตัดสินทั้งประโยคจาก ngram อย่างเดียว
4. ให้ alphabetic English typo ที่มี lexical neighbor 1 edit (รวม transpose) และมี English context หลายคำผ่านได้. ไม่แก้ input ที่ส่งเข้าระบบ; ไม่ให้ short fragments/ตัวเลข/ชื่อ/negation เปลี่ยนค่า. Diagnostic ต้องแสดงเหตุผล lexical context
5. ประกาศ controls เพิ่มจากข้อความใหม่และ projection แป้นสองทิศทาง, clean sentences, names, codes, dates/numbers. แยก development หลังดู failuresออกจาก untouched regressions; ไม่สร้าง expectationsจากผล runtime
6. รัน guard 36 + regression4,280 + controls; บันทึก false reject และ layout detection แยก. ตรวจ end-to-end กลุ่ม31กับ source/clean answersและ fixture booking; ข้อผิดที่ยังเหลือแยกguard/recovery/route/retrieval/contract
7. Unit/competition regression/APIจริง: pipeline direct ไม่ผ่านเว็บ guard. สร้าง package ใหม่หลัง freezecode, รันชุดทีละชุด, เปลี่ยน8090เมื่อผ่านและเก็บแพ็กเกจ/logsเดิม. ตรวจ Gold/source hashesสุดท้าย
8. รายงานอะไรแก้ได้ อะไรไม่แก้ สิ่งที่รอเจ้าของยังอ้างแบบเดิม; ไม่เอา guard-pass ไปนับเป็น booked/free ถูกต้องหรือ owner policy approval

## การรับผล

31 ordinary noisy inputs ไม่ถูก block, 5 deliberate layouts ยังตรวจพบ. ไม่มี newly blocked ใน competition regressionsและ valid heldout controls. ยอมรับว่า short/mixed ambiguous fragmentsอาจให้ downstreamถามกลับ; ไม่เพิ่มความมั่นใจจาก scorengramโดยเดา. การตัดสิน thresholdต้องรายงาน tradeoffกับ controls

## การปรับ Flow หลังทดลองจริง

1. ต้องแยก intentional keyboard layout จาก noisy questions ก่อนนับ false rejection: 36 เดิม = ordinary31 + layout5.
2. Guard-pass → ตรวจ clean/noisy pair → ตรวจเนื้อหาที่ต่าง → เทียบ source clauses/price group/duration/operation/review status. Legacy route-passอย่างเดียวไม่พอ.
3. English guard ใช้ lexical one-edit neighborsเฉพาะ sentence context. Recover task wordใน syntax frameแยกต่างหาก; raw input/ชื่อ/เลขยังอยู่ในlog. Price much/costฟื้นได้หลายspan; eligibility labelsต้องมี independent price/resource/institution context.
4. Full-name mismatchใช้ directory-only suggestionใน explicit role frame: budget≤2, ratio≤.16, runner-up margin≥2. แสดง “หากหมายถึง…” +ชื่อจริง ไม่แทนชื่อผู้ใช้และไม่เลือกเมื่อใกล้หลายคน.
5. Secondary control source noteต้องติดไปกับsource rowsก่อนลดmetadata. ทั้ง structured/vector pathต้องบอกว่าคนยังไม่ได้ตรวจเทียบเครื่องจริง.
6. Live HTTPเปิดLLM/semanticต่างจากdirect regressionที่ปิด; หากคำตอบต่างให้ทดสอบ cleanคู่ใน environmentเดียวกัน. ห้ามผ่อน expectedเพียงให้ผ่าน. Video-policy clean/noisy safe unknownยังมี explanation defectแยกไว้.
7. Package freeze/hash → actualHTTPชุดเดิม+ใหม่แบบ sequential → ตรวจowned process/port → เปลี่ยน8090 → smoke72 → ปิด8091เฉพาะตัวที่สร้าง. เก็บ package/logs/snapshotsเดิม.

## ผลสุดท้าย r29

| การทดสอบ | ผล | สิ่งที่ยืนยันได้ |
|---|---:|---|
| Ordinary noiseเดิม | 31/31ไม่ถูกblock | input guardเปิดทางให้pipeline |
| Intentional layoutsเดิม | 5/5ยังblock | ข้อความขอพิมพ์ใหม่ TH/EN |
| Guard controlsรวม | 100/100 | 36เดิม+64 controls; ไม่ใช่ human traffic |
| Guard regression | 4,283, newly blocked0 | ตัดfalse reject31; เป็นguard-only |
| Unit/regression modules | 168/168 | recovered cues, conditional names, notes, booking fixture,competition/worker |
| Direct clean/noisy | 31/31legacy; เหมือน29คู่ | 62responses; 2คู่ต่างแบบอธิบายได้; clean semanticsยังมีงานต่อ |
| Actual HTTP test port8091 | 684/684ตามcontracts | 280+320+12+36เดิม+36noise/layout; 2liveเคสpath-only |
| หลังเปลี่ยนเว็บ8090 | 72/72 | รุ่นr29บนพอร์ตใช้งาน |
| Preservation | ผ่าน | 9protectedfiles unchanged; snapshotsverified; appตรงpackage; ไม่มีevalในpackage |

684/684 ไม่ใช่การรับรองว่าแชทบอทตอบถูกทุกคำถาม หรือว่าเจ้าของอนุมัติทุกข้อ. 4,283ไม่ได้รันคำตอบทั้งหมด. สถานะจองจริงยังไม่มีoracleตามที่ผู้ใช้พักไว้.

## ลำดับงานต่อจากผลที่พบ

1. P1 ราคาแบบ “1 hour or 2 hours”: รองรับทุกduration alternativeพร้อมผลคำนวณที่ตรวจแยกกัน.
2. P1 คำถามปุ่มเฉพาะ: explicit button matchingต้องชนะgeneric description; ไทยOptionsมีCircleปน/อังกฤษD-Padคืนรายการกว้าง.
3. P1 “need to book to play [game]”: เพิ่มคำตอบว่าต้องเลือกบริการใดจากgame→serviceข้อมูลเดิม หรือclarifyถ้าต้องการขั้นตอน/อุปกรณ์ต่างกัน.
4. P2 ภาษาอังกฤษ safe unknown: แยกข้อมูลต้นฉบับไม่มีจากไม่มีคำแปล; photo/video policyยังรอเจ้าของ.
5. Owner decisions: Tekken pause, RoV6.1.5.1, rulebook/version, English names,controllers,photo/video/public/food policyและfee/ageที่ไม่มีข้อมูล. ใช้แบบฟอร์มเดิม ไม่เดานโยบาย.

หลักฐานรายกรณี: reports/r29_input_guard_context_20261002_005246_30dbb7/DETAILED_CAUSE_ANALYSIS_TH.md และ JSONLก่อน/หลังทุกครั้ง. Runtime: 2026.10.02-input-context-r29-verified. เว็บ: http://127.0.0.1:8090/
