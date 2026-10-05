# Flow r28 — ความครบของคำถามกติกาหลายประเด็น

## ขอบเขต

ใช้ source และคำแปลที่ hash ตรง เพิ่มคำถามและคำตอบที่คาดหวังจาก clause ต้นฉบับก่อนแก้ selector. เก็บ owner pending, Gold, นโยบายศูนย์ และ logs เดิม. การตรวจคำแปลทำเองต่อได้ ส่วนกฎที่ขัดหรือ source ขาดต้องรอผู้จัด

## ขั้นตอน

1. ตรึงชุดประเด็นที่ยังไม่ครอบคลุมใน r27 รวมคำถามหลายเรื่องเกมเดียวและ controls: ไม่ระบุเกม, เกมไม่รองรับ, อายุ/ราคาไม่พบ, pause ที่ขัดกัน
2. แต่ละ expected clause มาจาก source ID/hash + approved English overlay; runtime ไม่อ่าน fixture และผล runtime ไม่ใช้สร้าง Gold
3. รัน baseline แยก clean/polite/typo, single/composite/controls. วิเคราะห์ทุก failure ตาม trace พร้อมเนื้อหาที่ควรปรากฏ
4. แก้การตรวจคำถามและการเลือก clause แบบแยกความหมาย ใช้แนวคิดทั่วไป ไม่ใช้ whole-question aliases. ตรวจว่า concept ที่จับหลายเรื่องไม่ตัดเรื่องอื่นและไม่มี head-only answer
5. ตรวจ local scope: ข้อห้าม macro/การติดตั้ง/เงื่อนไขการปรับค่า กับหัวข้ออื่นต้องไม่ถูก exclude ด้วยคำจากคำถามทั้งประโยค
6. เพิ่ม tests เฉพาะ failure จริง รวมคำที่ถูก, negation, game/number preservation และความกำกวม
7. รันชุดใหม่ซ้ำ, ชุดเดิม 320/128/80 และ unit; เมื่อเลือกคำตอบเปลี่ยนให้รัน Gold 2,000 อีกครั้ง เก็บ raw กับ source presence grade แยก
8. สร้าง package รุ่นใหม่ ไม่ทับแพ็กเกจเดิม ตรวจเว็บจริงก่อนนำขึ้น 8090. ใช้ผล r27 worker recycle เป็นหลักฐานเดิม; repeat เฉพาะ gate ที่ implementation ใหม่มีผล
9. สรุปสิ่งที่แก้ได้ ผลจริง ขอบเขต synthetic cases และคำถามเจ้าของที่ยังขาด. อัปเดต Flow ตามความผิดที่พบ

## การรับผล

Positive: game/source ถูก, complete expected clauses ทุกข้อ, first line ตรงหนึ่งประเด็นที่ถาม, validation ผ่าน. Safe controls: clarification/no-answer/conflict ตามหลักฐาน ไม่มีการแต่งข้อมูลอายุ/ค่าธรรมเนียม/คำที่ source ขาด. ไม่ใช้ source-presence pass แทน completeness

## ยังรอข้อมูล

Tekken s03/s07, RoV 6.1.5–6.1.5.1 ฉบับเต็ม, ขอบเขต/ฉบับที่มีผลและ V2 104. รุ่นจอย/นโยบายภาพ/ชื่ออังกฤษทางการเติมได้เมื่อมีข้อมูล. Booking oracle ยังเก็บภายหลัง

## ทบทวนจากผลจริงและ Flow ฉบับเสร็จ

1. Baseline 63/280: เพิ่มตัวจับ clause จาก source และแก้ global excludes; Candidate A 257/280
2. ตรวจ Candidate A: final decision ไม่ใช่ final match, macro/customization English source wording, no-answer contract และ oracle ที่ overspec Cypher 3 ข้อ; แก้เป็น v3 โดยเก็บ audit. Candidate B/C 280/280
3. Regression 320/128/80 ผ่าน; unit C 151 ผ่าน. รัน Gold เต็ม 2,000 แล้วพบ dispute resolution 12 ข้อผิดจริง; source presence ตัวตรวจเดิม false failure 47
4. Mask dispute/conflict resolution เฉพาะ display matching. Retest 59 ข้อและ source-grade รวมผ่าน 2,000 ข้อ; ไม่เรียกว่า second full run. Unit D ยังเห็น fixture-clock หลังข้ามวันและเลข source assertion ที่สมมติผิด; snapshot/แก้เฉพาะ testsแล้ว unit E 153 ผ่าน
5. Actual HTTP จำเป็น: direct pipeline ไม่ผ่าน input guard ของเว็บ. รอบแรก 275/280 พบ its false layout 3 และ concurrent busy 2. เพิ่ม English function-word prior; guard scan 4,283 ไม่มี newly blocked. Unit G 154 ผ่าน; ไม่บังคับ l;ylfu ให้ block เพราะก่อน/หลังไม่ block อยู่แล้ว เก็บ diagnostic
6. สร้าง package ใหม่ทุกครั้งและตรวจ app hash ตรง source. รัน HTTP ทีละชุด 648 ผ่าน; worker promotion 2 ครั้ง ไม่มี error. หลังเปลี่ยน 8090 ผ่าน 36; test8091หยุดแล้ว

### จุดที่ต้องเพิ่มใน Flow เมื่อพัฒนารอบถัดไป

- ก่อนเริ่ม pipeline ต้องตรวจ input guard ในสภาพ enforce จริง พร้อม raw span scores และ wrong-layout controls. ตรวจประโยคอังกฤษที่มีคำหน้าที่และหลายประเด็น; อย่าใช้ direct pipeline เป็นหลักฐานของทั้งเว็บ
- ดึง expected clauses จาก source/version/hash ก่อนแก้; ตรวจแต่ละประเด็นไม่ใช่เพียง citation. Source presence 2,000 pass ไม่เท่ากับทุกเงื่อนไขครบหรือ owner approval
- ก่อนสรุป semantic failure ให้แยก transport, guard, target/facet, completeness, source conflict/gap และ evaluator error
- เทส fixture ที่ใช้ today/tomorrow ต้อง freeze test clock ให้ตรง fixture; ไม่แก้ runtime ให้รับข้อมูลวันที่ผิด
- ห้ามทดสอบหลายชุดพร้อมกันบน backendหนึ่งตัวเมื่อไม่ได้กำลังตรวจ concurrency. หากจะตรวจ concurrency ต้องมีชุดและเกณฑ์ retry/busy ที่ประกาศแยก
- ต่อไปอ่าน noisy inputs เก่า 36 ข้อ, composites มากกว่า 2 ประเด็น/หลายเลข/หลายเกม, missing age+eligibility และ latency ของ unsupported games. ยังไม่รวมเป็นงานที่ผ่านแล้ว
- Owner pending ระบุคำถามเฉพาะตามแบบ 01–05; ไม่ใช้ OK ของการพัฒนาเป็นการเซ็นรับรองข้อกฎ

### ผลและเอกสาร

ผลสุดท้ายและข้อจำกัด: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r28_competition_composition_20261001_231456_23d4ce\FINAL_RESULTS_TH.md`. Verification: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r28_competition_composition_20261001_231456_23d4ce\FINAL_VERIFICATION.json`. วิเคราะห์ทุก anchor ที่ผิด: CAUSE_ANALYSIS_TH.md; ชุดใหญ่: FULL_GROUND_TRUTH_ANALYSIS_TH.md; input guard: INPUT_GUARD_ANALYSIS_TH.md

เว็บใช้รุ่น `2026.10.02-competition-composition-r28-guard-verified` ที่ http://127.0.0.1:8090/
