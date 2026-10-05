# ผลรอบ r27 — กติกาการแข่งขัน ไทย/อังกฤษ

## พร้อมลองใช้

เว็บ: http://127.0.0.1:8090/  
รุ่น: `2026.10.01-competition-contract-r27-verified`  
แพ็กเกจ: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_contract_r27_verified\PSU_Esports_Chatbot_Local`

## สิ่งที่แก้จากหลักฐาน

1. แยกหัวข้อย่อยของกติกา: เลือก clause เต็มจากเกมที่ถาม เช่น อุปกรณ์ โน้ต ประท้วง จำนวนฮีโร่ เงื่อนไขเริ่มใหม่ การตั้งค่า และรายการบทลงโทษ ประโยคแรกต้องตอบเรื่องที่ถามก่อน
2. รักษาค่า หน่วย เงื่อนไขและข้อยกเว้น ใช้ต้นฉบับไทยและ English overlay ที่ hash ตรง ไม่สร้างข้อกฎที่ไม่มีในแหล่ง
3. กู้คำหัวข้อพิมพ์ผิดแบบมีบริบทและจำกัดระยะ เช่น protest/notes/heroes/settings และไทย พร้อมป้องกัน score ไม่ให้ถูกแก้เป็น scope ชื่อเกม ตัวเลข และคำปฏิเสธยังมี negative tests
4. คำถามกติกาไม่ระบุเกมถามกลับก่อนเรียกโมเดล เพิ่ม timing ของ locale/cue/canonical preflight เพื่อให้ตรวจเวลาได้ละเอียดขึ้น
5. แก้ตัวตรวจที่ปฏิเสธ clause อังกฤษสั้น ตรวจครบหนึ่ง clause จาก source ได้โดยยังรักษา gates เดิมและคะแนนดิบ แยก presence จาก completeness
6. แก้ช่วง worker เปลี่ยนทุก 250 คำถาม: เตรียมตัวใหม่พร้อมก่อนสลับ ตัวเดิมยังรับงาน ระหว่างทดสอบจับ TypeError ใน log ที่เพิ่มได้และแก้โดยส่ง request_id พร้อมเพิ่ม test ที่บังคับ signature จริง

## ผลอัตโนมัติ — ความหมายต่างกัน

| ชุดตรวจ | ผล | สิ่งที่ยืนยันได้ |
| --- | --- | --- |
| Gold เดิม 2,000 ข้อ — คะแนนดิบ | 1,953/2,000 | 47 ข้อถูกตัวตรวจ legacy ปฏิเสธ source content; เก็บผลเดิมไว้ |
| Gold เดิม — atomic-source grade | 2,000/2,000 | route/status/game/evidence ตาม gates เดิม และ complete-clause presence; ไม่ใช่ตรวจทุกความหมายในทุกคำตอบ |
| รายละเอียดกติกา 320 ข้อบนเว็บจริง | 320/320 | 52 ประเด็น ×2 ภาษา ×3 รูปคำถาม +8 controls; ทุก clause ที่ fixture กำหนดและประโยคแรก |
| คำถามใหม่และ typo 128 ข้อบนเว็บจริง | 128/128 | 16 ประเด็น ×2 ภาษา ×4 รูปแบบ; เป็น development/regression หลังวิเคราะห์แล้ว ไม่ใช่ blind user traffic |
| ตรวจเนื้อหาชุดก่อนหน้า | 80/80 | ค่า/หน่วย/ข้อห้าม/เงื่อนไข/ตาราง 16 anchors |
| เว็บ regression | 36/36 | คำถามผู้ใช้จริงในแชท ประวัติข้ามเกม overview, source gap, catalog, booking route |
| Unit/regression | 135/135 | grader negatives, recovery guards, routing และ worker recycle signature/races |
| โปรเซสแยก | ผ่าน | 24 คำถาม ข้าม planned recycle 2 ครั้งและกู้หลัง crash; timeout recovery เดิมผ่าน |
| HTTP ต่อเนื่องบนแพ็กเกจจริง | 573/573 ส่งกลับ 200 | 572 คำถามจากชุดข้างต้น +1 probe; promoted worker 2 ครั้ง ไม่มี 500/503 |
| หลังเปลี่ยนเว็บ 8090 | 36/36 +8/8 | runtime/health พร้อม และ regression/clarification ผ่าน |

### เวลา

ชุด clarification เดิม r26 จำนวน 8 ครั้ง median 1.53415s / max 12.7451s; r27 บนเว็บทดสอบ median 0.08515s / max 0.1115s; หลังขึ้น 8090 median 0.07035s / max 0.1094s.

เป็นเวลาจากเครื่องนี้และคำถามกลุ่มนี้ภายใต้ cache/load ณ ตอนรัน ไม่ใช่ benchmark ที่ควบคุมทุกปัจจัยหรือคำรับประกันทุกคำถาม รายละเอียด 320 max 5.8511s (Free Fire ที่ไม่มี rulebook), ชุดใหม่ 128 max 0.9575s.

## วิเคราะห์ความผิดที่พบระหว่างพัฒนา

- Baseline v1 165/320 มีทั้ง runtime failures และ literal oracle ที่คลาดเคลื่อน จึงเก็บ v1 ไว้และมี `oracle_revision_audit.json`; ห้ามใช้ตัวเลขนี้เป็น semantic accuracy
- รอบ B 233/320: mode ใหม่ไม่มี competition_rule ทำให้ contract ไม่รู้จัก แก้การระบุ mode
- รอบ C 311/320: Tekken settings เลือก chunk สั้นเสีย Stage/Advantage, score ถูกแก้เป็น scope และ EN literal oracle ต่างคำแปล แยกแก้สาเหตุ
- ชุดใหม่รอบ A 112/128: กู้ task word แต่ไม่กู้ facet word ที่พิมพ์ขาด เพิ่มบริบทและ unique edit candidate แบบจำกัด
- Gold run A 1,938/2,000: มี regression `apply to` จับ overview เป็น scope และ composite eligibility/roster/registration ตอบเพียงเรื่องเดียว แก้แล้ว run B มีเหลือ 47 legacy false failures
- HTTP candidate 503 เกิดจากปิด worker เดิมก่อน replacement ready แม้ถามทีละข้อ; ไม่ใช่ข้อมูลข้อกฎขาด
- HTTP final ครั้งแรก 318/320: TypeError จาก `ParentPerformanceLogger.emit_parent()` ขาด request_id ในส่วน log ที่เพิ่มไว้ การใช้ Mock ที่ไม่ตรวจ signature ปล่อยให้ unit pass; เปลี่ยนเป็น autospec และแก้ทั้ง 4 branches
- verified ผ่าน 320/128/36/80/8 ต่อเนื่องและอีก 1 probe; event/log/PID ยืนยันสลับหลัง ready 2 ครั้ง

รายประเด็นพร้อมคำตอบเดิม ข้อที่ควรปรากฏ source/hash และผลหลังแก้อยู่ใน `CAUSE_ANALYSIS_TH.md`.

## สิ่งที่ต้องให้ผู้จัดยืนยัน

1. Tekken s03 ระบุห้าม pause แต่ s07 อนุญาตบางกรณี: s07 เป็นข้อยกเว้นของ s03 หรือไม่? เหตุใดได้รับอนุญาต? ต้องขอกรรมการก่อนหรือไม่? โทษแต่ละกรณีเสีย Round, Game หรือ FT2 Match?
2. V2 review 104 รายการยังรอตรวจและยังไม่ publish การผ่าน source hash/translation checks เป็นการตรวจระบบ ไม่ใช่คำรับรองนโยบายหรือคำแปลจากผู้จัด

## ขอบเขตที่ยังควรพัฒนา

- การกู้ typo หลายตำแหน่งมี span/edit budget เพื่อป้องกันการเปลี่ยนความหมาย ยังไม่รองรับทุก slang/การพิมพ์ผิด และอาจต้องถามกลับ
- Detail selector ใช้แนวคิดทั่วไปของหัวข้อในขอบเขต rulebook ที่มีและ clause matching; ประโยคใหม่ที่ต่างโครงสร้างมากหรือถามหลายประเด็นอาจยังใช้ fallback เดิม ต้องทดสอบ unseen cases เพิ่มเมื่อมีข้อมูลจริง
- ชุด 2,000 ไม่ได้ตรวจ every required proposition จึงใช้ชุด 320/128/80 ประกอบ ยังไม่เท่ากับตรวจเนื้อหาทั้ง 104 chunks ในทุกความหมาย
- การทดสอบ availability กับข้อมูลจริงของเจ้าของยังเลื่อนตามคำขอ ผล booking regression นี้ยืนยันการเข้า route/วันปิดหรือ source-unavailable; ไม่ใช่หลักฐานว่าเวลาจองสดทุกช่วงถูกต้อง
- งานถัดไปที่ทำเองได้: ขยาย proposition contracts จาก source ที่ยังไม่ครอบคลุม, เพิ่ม unseen compound/negation/typo cases และวิเคราะห์ trace แยกจากผล legacy; การแก้นโยบายขัดกันต้องรอผู้จัด

## การรักษาไฟล์และหลักฐาน

protected 7 ไฟล์ hash ตรงก่อน/หลัง (source, Gold, review queue, English CURRENT, owner schedule, r26 Flow); initial snapshots อื่นที่ไม่ได้แก้ hash ตรง; Git paths ที่มีอยู่ก่อนยังครบ.

เก็บ `before`, `ready_code`, `final_code` และ `verified_code` แยก; เก็บผลทุก attempt รวม partial/500/503; สร้างแพ็กเกจ r27 verified ใหม่. ปิดเฉพาะ launcher เว็บที่สร้างไว้และตรวจ PID/port/parent ก่อน เว็บทดสอบ 8091 ปิดแล้ว เว็บ 8090 พร้อมใช้งาน.

## ตรวจซ้ำ

Fixtures อยู่ `data/eval/competition_content_contract_r27_320_20261001.json` และ `data/eval/competition_new_questions_r27_128_20261001.json` ไม่รวมใน owner package และ runtime ไม่อ่าน Gold.

ใช้ `tools/run_competition_contract_r27.py --fixture <fixture> --report <new-report-dir> --run <new-name> --url http://127.0.0.1:8090 --llm` เพื่อรัน contract ผ่านเว็บ; ผลใช้ exclusive creation จึงต้องเลือกชื่อใหม่. ใช้ `tools/competition_content_grader_r27.py` เพื่อ rescore ผลดิบโดยแยก source presence. อย่ากดสร้าง Gold ทับไฟล์เดิม.
