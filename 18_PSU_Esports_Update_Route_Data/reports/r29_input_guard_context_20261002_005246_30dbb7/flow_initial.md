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
