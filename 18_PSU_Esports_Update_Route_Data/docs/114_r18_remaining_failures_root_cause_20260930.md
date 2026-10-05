# วิเคราะห์ว่าทำไม r18 ยังพลาด

วันที่ 30 กันยายน 2026 · อ่านผล `reports/typo_r16_20260930/paired_{th,en}_r18.jsonl` ทั้ง 2,000 คู่ เทียบผล r15, ตรวจโค้ด และรัน trace ซ้ำกรณีตัวแทนโดยปิด LLM/RAG เช่นเดียวกับ benchmark · **เป็นการวิเคราะห์ ไม่ได้แก้โค้ดหรือข้อมูลศูนย์ในรอบนี้**

## 1. ขนาดปัญหาและความหมายของตัวเลข

r18 ทำให้ regression จาก typo ลดจาก 239 เหลือ **181 คู่** (ไทย 80, อังกฤษ 101); คือกรณีที่ข้อความสะอาดผ่านเกณฑ์ แต่ข้อความที่ถูกทำให้พิมพ์ผิดไม่ผ่าน เกณฑ์นี้ไม่เท่ากับจำนวนข้อเท็จจริงที่ตอบผิดจริง เพราะตรวจ route, สถานะ, เนื้อหา และเวลาแบบรวมผ่าน/ตก และ gold ทั้งหมดเป็น candidate หรือ pending review

| จุดแรกที่เกณฑ์พบว่าตก (ไม่ซ้อนกัน) | ไทย | อังกฤษ | รวม | ตัวอย่างผลต่อผู้ใช้ |
|---|---:|---:|---:|---|
| Route ผิด | 60 | 71 | **131** | เกม/อุปกรณ์กลายเป็นถามช่องจองสด หรือเรื่องเฉพาะกลายเป็น general |
| Route ถูก แต่สถานะผิด | 16 | 17 | **33** | ควรตอบแต่ปฏิเสธ/ถามกลับ หรือควรถามกลับแต่ตอบ |
| Route และสถานะถูก แต่เนื้อหาตก | 4 | 13 | **17** | ถาม Sofa แต่ตอบทีวี; ถามข้อมูลจองแต่ตอบเพียงขั้นตอนทั่วไป |

หากนับทุกเงื่อนไขที่ตกแบบซ้อนกัน route 131, status 135, content 72, latency 0. ฉะนั้นห้ามบวกเลขชุดหลังเป็น 338 ปัญหาอิสระ เวลาของ 4,000 pipeline calls ในชุด r18 เกิน 10 วินาที 3 calls แต่ไม่เกินเพดาน benchmark 20 วินาที; 181 คู่ที่นี่ไม่ได้ตกเพราะเวลา

โดเมนที่เหลือมากสุด: compound 32, studio rules 26, games catalog 23, reservation policy 22, members/contact 21, service fee 16, schedule 12, equipment 10, game detail 9, live booking 5, competition rules 5. ชนิดการทำ typo ที่ตก: mixed 64, neighbor 37, delete 31, transpose 27, repeat 22

## 2. รากปัญหาของระบบที่ตรวจยืนยันได้

### A. ตัวซ่อม r18 ตั้งใจรองรับคำบอกงานเพียงชุดจำกัด

`app/core/intent_cue_recovery.py` แก้คำที่ชี้งานบางกลุ่ม เช่น ราคา/ว่าง/ปุ่ม/available/controls/temporary เมื่ออยู่ในบริบทที่ระบุ และคืน candidate แรกหนึ่งรายการต่อการเรียก ไม่ใช่เครื่องพิสูจน์ว่าข้อความทุกคำสะกดถูก ร่วมกับตัวแก้เดิมแล้วยังเหลือ typo ทั่วไปและหลายจุด เช่น `Are drins allowwd`, `ตำแหน่ง` → `ทำำแหน่ง`, `วันปิด` → `วันปิิด`, `แพงกว่า` → `แพงกว่่า` โดยเฉพาะ mixed 64 ข้อ

เหตุผลที่ขอบเขตแคบมีความสำคัญ: การแก้คำทั่วไปแบบ nearest match อาจเปลี่ยนคำจริงเป็นเจตนาอื่น เช่น `pay/play`, รหัส PC1/PC11, เวลา หรือชื่อเกม จึงต้องมี candidate หลายทางพร้อม guard และการวัด false correction ก่อนขยาย ไม่ควรเพิ่ม alias ของทุกประโยคเพื่อไล่คะแนน

### B. คำ “available” มีสองความหมาย แต่ตัวเรียก Dashboard มาก่อนตัวตอบเกม/อุปกรณ์

`app/pipeline/engine.py` เรียก `answer_live_booking_status` ก่อน English catalog handlers; `app/booking/live_status.py:is_live_booking_question` กันคำถาม `what games/equipment` ที่สะกดถูก แต่ถ้า `games` → `gmes` หรือ `equipment` → `equipmennt` ตัวกันไม่ตรง ขณะที่ `available` กับชื่อโซนยังตรง จึงเข้า live booking

ตัวอย่าง `MASTER-GT-EN-01756`: `What games are available in Cockpit` → `What gmes are available in Cockpit` กลายเป็น `schedule/live_booking_status_unavailable` ทั้งที่ข้อมูลรายการเกมอยู่ใน `data/curated/service_game_availability.jsonl` (Cockpit มี Gran Turismo 7) ใน 181 ข้อมี **8 ข้อ** ลงโหมด live-unavailable และทั้ง 8 เป็นคำถาม static catalog/equipment/compound ที่ถูกส่งผิดทาง ไม่ใช่หลักฐานว่าระบบจองจริงตอบผิด 8 ครั้ง

### C. พิมพ์ผิดแล้ว operation หาย ทำให้ abstain หรือ fallback

ตัวอย่าง `นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร` และ `สัปดาห์นี้มีวันปิิดพิเศษไหม`: preprocess ไม่แก้คำ; operation กลายเป็น unknown; ตัวเลือกสูงสุด `retrieval.hybrid_guarded` ได้ 0.433 ต่ำกว่าเกณฑ์ 0.45 จึงถามกลับกว้าง ๆ ใน `pipeline:candidate_margin_clarification` จากการรัน trace ซ้ำครบ **25/25 ข้อ** ในโหมดนี้เป็น `abstain_low_score` ไม่ใช่คะแนนอันดับหนึ่งกับสองใกล้กัน (ตัวอย่าง margin 0.111; เกณฑ์ low-margin ใน `capability_registry.py` คือ 0.035) ชื่อโหมดจึงทำให้วิเคราะห์ผิดได้

บางคำถามอังกฤษตกเป็น `pipeline:english_no_answer` **56 ข้อ** และไทย `pipeline:no_answer` **29 ข้อ** ตัวอย่าง `Are drins allowwd` ได้ no-answer ทั้งที่กฎภาษาอังกฤษใน `data/rules/english_support_rules.jsonl` มีข้อความว่าเครื่องดื่มอนุญาตเฉพาะพื้นที่กำหนด เพราะ rule pattern ของ `drinks/allowed` ไม่ตรงและ English handler จบด้วย no-answer แทนการส่งไปเส้นไทย

### D. เลือกหมวดถูก แต่เลือกเป้าหมายย่อย/รายละเอียดผิด

`MASTER-GT-TH-03455`: `ขอสอบถาม... Sofa 2 seats` ถูกเปลี่ยนคำเกริ่นเป็น `จอสอบถาม...` ตัวค้นหาอุปกรณ์ `_detect_equipment_item` ยังตรวจ Sofa ได้ถูก แต่ `_equipment_answer` เห็น `จอ` ที่คำเกริ่นและโซนของ Sofa แล้ว **override** เป็น TV 86 นิ้ว คำตอบจึงผิดวัตถุ ทั้งที่ route equipment และ status answer ผ่าน ตัวเลือก `structured.equipment` ได้คะแนน 0.99 เพราะเป็นคะแนนเลือก *capability* ไม่ใช่ความน่าจะเป็นว่าระบุอุปกรณ์ถูก 99%

`MASTER-GT-TH-04631`: `รองประธาน` → `รอวประธาน` ระบบจับ substring `ประธาน` แล้วตอบชื่อประธาน ทั้งที่แถวข้อมูล `data/curated/member_profiles.jsonl` มีตำแหน่งรองประธานพร้อมชื่ออยู่ ชนิดนี้เสี่ยงกว่าการ no-answer เพราะตอบข้อเท็จจริงอีกเป้าหมายอย่างมั่นใจ

### E. คำถามหลายงานหลุดงานหนึ่ง และ generic answer แทนรายละเอียดเฉพาะ

`MASTER-GT-TH-04903`: ถามราคา PS5 30 นาที **แล้วจองยังไง** แต่ `แล้ว` → `อล้ว` ตัวแยกงานไม่เห็นคำเชื่อม ระบบจึงคำนวณราคาอย่างเดียว; เกณฑ์ตกเพราะไม่มีส่วนขั้นตอนจอง แม้คำตอบราคาดูสมเหตุสมผลตามตารางในโปรเจกต์ (ตารางราคาเวอร์ชันปัจจุบันยังรอเจ้าของยืนยัน)

`MASTER-GT-EN-00418`: `What information do I need to book` → `What iformation do I need to book` ยัง route reservation แต่ตอบขั้นตอนจองทั่วไป `rule_en_booking_steps_natural` ไม่ระบุ Student ID และเบอร์โทรศัพท์ตามเนื้อหาที่คำถามต้องการ กรณีใกล้กันถามเวลาชำระเงินแต่ตอบขั้นตอนทั่วไป ไม่ระบุ 10 นาที ปัญหาไม่ใช่แค่สะกดคำ แต่เป็นการเลือก sub-intent/คำตอบที่กว้างกว่าคำถาม

### F. English localization pending บางกรณีเป็นผลหลัง route หลุด

13 regression ลง `missing_english_localization` โดยคำถามเดิมหลายข้อเข้าตัวตอบ structured ที่มีอยู่ เช่น `Which studio zone has FINAL FANTASY XVI` → `Which studio zonw has...` เดิมตอบ PlayStation 5 Zone แต่หลัง typo กลับตอบว่าไม่มีคำแปลอนุมัติ สิ่งนี้เป็นความผิดของ routing/coverage gate สำหรับข้อดังกล่าว ไม่ใช่หลักฐานว่าข้อมูลโซนหาย อย่างไรก็ดี กติกาแข่งขันอังกฤษบางส่วน **ยังรอคำแปลอนุมัติจริง** และไม่ควรแปลเดาเพื่อดันคะแนน

## 3. ปัญหาของตัววัดที่ต้องแยกจากข้อผิดระบบ

- ใน fixture 2,000 คู่ มี **1,107 คู่ไม่มี positive content contract**; ใน 181 regression ยังมี **100 คู่** แบบนี้ การ route/status ผ่านจึงไม่พิสูจน์ว่าตอบครบหรือถูกข้อเท็จจริง ในทางกลับกัน route ต่างแต่ตอบปฏิเสธอย่างปลอดภัยก็ถูกนับตกได้
- ป้าย review ของ 181 คู่คือ generated paraphrase pending review 72, inherited gold candidate 91, source-grounded candidate 18; **ไม่มีข้อใดถูกระบุว่า owner-confirmed** ดังนั้น 181 ไม่ใช่จำนวนคำตอบผิดที่คนตรวจยืนยันแล้ว
- r18 legacy ให้ regression 181; rescore v2 ให้ 179 เพราะนิยาม status/route และ overlay ต่างกัน มี 10 IDs ที่ป้าย regression ระหว่างสองตัววัดไม่ตรงกัน รวมกรณี no-answer และ live lookup จึงต้อง audit รายข้อก่อนใช้ v2 เป็นเกณฑ์ปล่อย
- ตัวอย่าง `MASTER-GT-TH-04758` ถามการส่งเครื่องเกมไปบ้าน เดิมและ noisy ยังปฏิเสธว่าไม่พบข้อมูล แต่ route เปลี่ยนจึงตก เป็น **route defect ที่ยังไม่เห็นการกล่าวอ้างผิด** ต่างจาก Sofa/รองประธานที่ตอบอีกวัตถุหนึ่งจริง
- ตัวเลข clean r18 ผ่าน 1,790/2,000 หมายความว่า **210 ข้อข้อความสะอาดก็ยังไม่ผ่าน** เกณฑ์เดิมด้วย สาเหตุรวมทั้ง coverage, localization และ label; อย่านำทั้งหมดไปนับว่าเกิดจาก typo

## 4. ลำดับแก้จากความเสี่ยงและหลักฐาน

1. **กันการตอบผิดเป้าหมายที่มั่นใจสูง**: ให้การจับ Sofa/จอและตำแหน่งประธาน/รองประธานยึด span เป้าหมายที่ถามจริง; ตรวจ target–answer relation ก่อนส่งคำตอบ ตัวอย่างเหล่านี้ควรเป็น regression test โดยไม่เปลี่ยนข้อมูลเจ้าของ
2. **แยก static catalog จาก live slot ก่อนเรียก Dashboard**: ใช้ operation + object + time จากทั้ง raw/candidate; เกม/อุปกรณ์ที่ “มี” ไม่ควรเข้าช่องจองสดแม้คำศัพท์หมวดหนึ่งมี typo; ถ้าถามเวลาหรือ `now` และเครื่องใดว่างจึงค่อยเรียก live
3. **กู้หลาย cue แบบมีงบและ provenance**: อนุญาต candidate หลาย span พร้อมคะแนนแยก spelling/intent/target; คุ้มครองชื่อเกม เวลา รหัสเครื่อง คำปฏิเสธ และคำจริงที่ชนกัน ถ้าไม่แน่ให้ถามเจาะจง ไม่ลด threshold รวมเพื่อให้ผ่านคะแนน
4. **ตรวจความครบของคำถามและ sub-intent**: split `ราคา + จอง`, answer contract แบบ all-groups, และตรวจข้อมูลจอง/ชำระเงินที่ถามเฉพาะ ไม่ให้ rule ขั้นตอนทั่วไปผ่านแทน
5. **แยกการตรวจเกณฑ์**: rescore r15/r18 ด้วย v2 ชุดเดียวกัน, ทำ holdout ที่คนตรวจ, แยก safe fallback/route defect/factual wrong/owner pending และทดสอบ false correction กับ clean/OOD ก่อนใช้ในแพ็กเกจหลัก

งานที่ต้องเจ้าของตัดสินใจยังเป็นตารางค่าบริการฉบับมีผล, การอนุมัติกติกาแข่งขันอังกฤษ, keybinding บนเครื่องจริง และ fixture จองสดที่ทราบผล ไม่มีข้อใดควรถูกเดาเพื่อแก้ benchmark

## หลักฐานหลัก

- ผลรายข้อ: `reports/typo_r16_20260930/paired_th_r18.jsonl`, `paired_en_r18.jsonl`; เทียบ r15: `analysis_r18.json`
- ตัวแก้ใหม่: `app/core/intent_cue_recovery.py`; ลำดับเรียก: `app/pipeline/engine.py`, `app/pipeline/preprocess.py`
- ตัวเลือกและ threshold: `app/pipeline/capability_registry.py` (`selected.score < 0.45`, `margin < 0.035`)
- ตัวแยก live/static: `app/booking/live_status.py:is_live_booking_question`
- อุปกรณ์และการ override จอ: `app/pipeline/structured_tools.py:_detect_equipment_item`, `_equipment_answer`
- English fallback/ลำดับตัวตอบ: `app/pipeline/bilingual_english.py:answer_english_supported`
- ตัววัด: `tools/run_master_ground_truth_eval.py`, `tools/eval_contract_v2.py`
