# ทบทวนและปรับแผนแก้คำถามพิมพ์ผิด/คำตอบผิด ฉบับที่ 2

วันที่ 30 กันยายน 2026 · อ้างอิง r15 และ docs/109–111 · สถานะ: แผนปรับปรุง ยังไม่ได้แก้โค้ดหรือข้อมูลศูนย์

เอกสารนี้เป็นฉบับดำเนินงานที่ปรับจาก docs/111_full_typo_and_answer_reliability_remediation_plan_20260930.md โดยเก็บไฟล์เดิมไว้เพื่อเทียบเหตุผลและไม่เขียนทับหลักฐาน r15

## 1. ข้อที่แผนเดิมถูกต้อง และข้อที่ต้องแก้

แผนเดิมแยกการรับข้อความ การแยกงาน route ข้อมูลจริง และการวัดผลได้ถูกทิศ; คุ้มครองตัวเลข/วัน/เวลา/รหัสเครื่อง; ไม่เดาสถานะจองและนโยบาย; รู้ว่าคำจริงชนกันอย่าง play/pay ควรถามกลับ จุดเหล่านี้ต้องคงไว้

| ช่องว่างในแผนเดิม | หลักฐานจากระบบปัจจุบัน | แก้ในฉบับนี้ |
|---|---|---|
| วางตัวสร้าง candidate แบบกว้างเร็วเกินไป | preprocess_input มี keyboard, transposition, multi-error phrase, game-title variants และ query_variants อยู่แล้ว; สร้างอีกชั้นอาจแก้ซ้ำ | ทำ audit ว่าคำใดหลุดที่ขั้นใดก่อน แล้วเพิ่ม candidate เฉพาะ intent/คำเชื่อมที่พิสูจน์ว่าขาด พร้อมเพดานและ provenance |
| เขียนว่า “ย้าย preprocess ก่อน splitter” แบบกว้าง | engine.py มีการแยกคำถามก่อน preprocess จริง แต่มีทางลัด canonical knowledge ก่อน split และมีข้อยกเว้น competition/damage policy | เพิ่ม preflight แบบอ่านอย่างเดียวสำหรับ split/intent ก่อนการแก้ข้อความเต็ม; ทดสอบทุก entry path และรักษาข้อยกเว้นเดิม |
| “ตรวจ live หนึ่งครั้งต่อคำถาม” ไม่ตรงกับโค้ด | live_status.py cache ตามวันที่ 0–30 วินาที, shared fetch lock, ตรวจ source=remote_csv_live และวันที่ตอบ | reuse snapshot ต่อวันที่ที่ถาม; ตรวจความสดของ generated_at/เวลา/slot ที่ขอ; แยก API ติดต่อได้จากค่าจองถูกต้อง; ไม่เรียกซ้ำเพราะ clause เดียวกัน |
| เกณฑ์เวลา 20 วินาทีปนกับเป้าการใช้งาน | master GT ใช้ ceiling 20 วินาที แต่ docs/77 ระบุเป้าผู้ใช้ 10 วินาที; direct call เคย 119.188 วินาที | รายงาน 3 ชั้นแยกกัน: latency ของ pipeline, HTTP ที่ผู้ใช้รอ, และ dashboard fetch; 20 วินาทีเป็นเกณฑ์ benchmark เดิม ส่วน 10 วินาทีเป็น production target ที่ต้องทดสอบบนเครื่องเป้าหมาย |
| เสนอ structured status ทั้งระบบในก้าวเดียว | PipelineAnswer ปัจจุบันมี mode/route/answer ไม่มี status field; หลายตัวตอบสร้าง object นี้ | ทำ adapter เฉพาะ evaluator ก่อน แล้วค่อยเพิ่ม optional outcome/status แบบไม่ทำลาย API/constructor เก่า; ย้าย handler ทีละกลุ่ม |
| “239 regressions” ยังไม่มีขั้นวินิจฉัยป้ายกำกับ | 1,107/2,000 ไม่มี positive contract; 72/84 English competition clean expected ขัดกับสถานะคำแปล; play/pay เปลี่ยนความหมาย | แยกข้อผิดระบบ ข้อกำกวม ข้อ source/owner pending และ evaluator defect ก่อนใช้เป็น gate; frozen r15 คงเดิม |
| ไม่มีตัวชี้วัด false correction/ค่าใช้จ่ายที่ชัด | การแก้สะกดอาจทำ clean หรือ OOD กลายเป็นคำถามราคา/จองที่ระบบตอบได้ แต่ผู้ใช้ไม่ได้ถาม | gate แบบสองด้าน: การกู้คำถามที่ยืนยันแล้ว และการไม่เปลี่ยนคำถามที่เดิมถูก/กำกวม; เพิ่ม clarification rate, wrong-topic rate และเวลาต่อขั้น |
| ขอบเขตแพ็กเกจ r16 กว้างเกิน | ปัญหาข้อมูลราคา/คำแปล/สถานะจริงต้องเจ้าของยืนยัน ขณะที่ typo logic ทำเองได้ | ออกเป็นหลายชิ้นเล็ก เปิดด้วย flag ในแพ็กเกจทดลอง; ให้ข้อมูล owner pending เป็น gate เฉพาะคำตอบที่พึ่งข้อมูลนั้น |

## 2. นิยามผลลัพธ์ที่ต้องแยกก่อนดูเปอร์เซ็นต์

หนึ่ง test case ต้องบันทึกอย่างน้อย: raw question, locale, protected spans, candidate ที่พิจารณา, split tasks, target/resource/time, route ต่อ task, answer outcome, source/version, คำตอบ, latency pipeline และ latency HTTP (ถ้ามี) รวมทั้ง expected label และระดับการตรวจของ label

แยกผลเป็น 4 กลุ่ม:
1. **Confirmed defect**: หลักฐานชัดว่าระบบตอบผิดงาน ตอบไม่ครบ หรือกล่าวข้อเท็จจริงเท็จ เช่น PUBG ราคาไปเรื่องย่อเกม และ PS5 ตอบเรื่องเดียว
2. **Safe but misrouted**: route ผิด แต่คำตอบยังปฏิเสธ/ถามอย่างปลอดภัย ต้องซ่อมเส้นทางและไม่อ้างว่าเป็น factual failure
3. **Ambiguous or label defect**: play/pay, expected English answer ที่ยังไม่มีคำแปลอนุมัติ, status heuristic ตี “ไม่พบ Roblox” ผิด; ต้องแก้ label/ถามกลับ ไม่บังคับระบบให้ทำตาม gold ที่ไม่น่าเชื่อถือ
4. **Evidence unavailable**: live status จริง ราคาเวอร์ชันล่าสุด ปุ่มบนเครื่องจริง; ทดสอบ logic กับ fixture ได้ แต่ห้ามบอกว่าความจริงปลายทางได้รับการยืนยัน

คะแนนรายงานต้องแยก route accuracy, task completeness, answer outcome, supported fact, false positive correction, harmful claim, latency และ live data correctness ไม่ยุบเป็น pass rate เดียว

## 3. Flow ที่แก้แล้ว: แทรกในระบบเดิมอย่างปลอดภัย

A. รับ raw input และ locale ตามเดิม → รู้จักและล็อกช่วงข้อมูลที่ห้ามแก้: รหัสช่อง/เครื่อง, ชื่อเกมที่มั่นใจ, ตัวเลข/เวลา/วัน, กลุ่มผู้ใช้, negation

B. ทำ **preflight ราคาถูก** บน raw: ตรวจคำบอกงาน/คำเชื่อมที่ชัด และระบุ span ที่ “อาจ” เป็น typo; ยังไม่เปลี่ยนข้อความ ผู้ใช้ถามสองเรื่องหรือมีหลาย target หรือไม่ให้บันทึกเป็นข้อสันนิษฐาน ไม่ตัดสินจากคำเชื่อมคำเดียว

C. ใช้ความสามารถ preprocess เดิมสร้าง variant; เพิ่ม candidate เฉพาะ span intent/คำเชื่อมที่ล้มเหลวจาก r15 (ไทยและอังกฤษ) และไม่ซ่อมทั้งประโยคด้วย nearest text ตัวเดียว จำกัดจำนวน variant, edit budget และเวลา; เก็บ raw กับ offset เพื่อ audit

D. ทำ **joint interpretation**: ให้คะแนนคู่ (split tasks, intent/operation, target, time, candidate) โดยพิจารณาคำถามต้นฉบับเป็น candidate หนึ่งเสมอ ตรวจ hard veto และความต่างคะแนนกับตัวเลือกถัดไป คะแนนว่าพิมพ์ผิด คะแนนเจตนา และหลักฐานตอบต้องแยกกัน ห้ามเลือก route เพราะเนื้อหาหมวดนั้นมีพร้อมกว่า

E. ตัดสิน 3 ทาง:
- ใช้การตีความที่ชนะชัดและไม่ละเมิด guard
- ถ้ามี 2 ความหมายสมเหตุสมผลหรือคำจริงชนกัน ถามเฉพาะตัวเลือก เช่น “วิธีเล่นหรือค่าบริการ”
- ถ้าไม่รู้เจตนาและไม่มีข้อเท็จจริงพอ ใช้ fallback ปลอดภัย ห้ามตอบเรื่องเกม/ราคา/จองเพียงเพราะ target ตรง

F. route แต่ละ task → เรียกแหล่งข้อมูลตามชนิดงาน → ตรวจ freshness/coverage → answer outcome ต่อ task → ตรวจว่าตอบทุก task และความสัมพันธ์ของข้อเท็จจริง → render ไทย/อังกฤษ

G. หาก flag ใหม่ปิด ให้กลับเส้นทาง r15 เดิมได้; trace ระบุ flag/version ที่ใช้ ผลทดลองกับผลหน้าเว็บจึงเปรียบเทียบได้

หมายเหตุการผสานโค้ด: engine.py มี canonical knowledge shortcut ก่อน splitter และข้อยกเว้น competition_rule_query/is_damage_policy_query ดังนั้นแทรก preflight ต้องไม่ทำให้คำถามกติกาแตกเป็นหลายงาน และต้องทดสอบว่าทางลัด canonical เปิด/ปิดให้ผลสอดคล้องกัน หลีกเลี่ยงการเพิ่ม branch ใหม่ที่ bypass guard เดิม

## 4. ลำดับการพัฒนาใหม่: ใช้ชิ้นเล็กและมีประตูก่อนชิ้นถัดไป

### ชิ้น 0 — ล็อกหลักฐานและทำ triage ที่ตรวจย้อนกลับได้

ไฟล์: docs/109–111, reports/bilingual_typo_2000_20260929/*r15*, data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl; สร้าง manifest และผล triage ใหม่ชื่อ v2

- บันทึก Git state และ hash ของ fixture/results โดยไม่แก้ของเก่า; เลือก 239 IDs เป็นรายการตรวจพร้อม clean/noisy output และ cause ที่แยกกัน
- ตรวจ labels จากคำถามและแหล่งข้อมูลที่มีได้เอง โดยใช้สถานะ “source-supported candidate” ไม่ใช้คำว่า owner-confirmed; ข้อที่ต้องเจ้าของ/คำถามมีความหมายกำกวมไว้คิวต่างหาก
- ทำตัวอย่าง “negative controls” ก่อนแก้: play/pay, จอย/จอง, กฎที่มี/ไม่มีคำปฏิเสธ, PC1/PC11, 09:00/10:00, เกมชื่อคล้าย, ข้อความนอกขอบเขต

Gate: ทุก regression มีรหัสสาเหตุและระดับความมั่นใจของ label; ไม่ลบ/แก้ผล r15

### ชิ้น 1 — แก้ evaluator เพื่อวัดผลจริง

ไฟล์: tools/run_master_ground_truth_eval.py, tools/run_bilingual_2000_typo_eval_20260929.py หรือ evaluator v2 ใหม่; test evaluator แยกจาก test chatbot

- ทำ outcome adapter จาก mode/route/answer ปัจจุบันเป็น typed status โดยระบุ unknown เมื่อเดาไม่ได้ ทดสอบด้วยกรณี Roblox, game_target_ambiguous, live_unavailable, localization_pending; เมื่อพร้อมค่อยเพิ่ม optional outcome ใน PipelineAnswer และย้าย handler เฉพาะเรื่อง
- เพิ่ม all_required_groups และ relation contract ที่ตรวจส่วนประกอบ เช่น [ราคา PS5] AND [รายชื่อเกม PS5], [VALORANT + Tab + scoreboard] ไม่ใช้ OR เพื่อผ่านคำถามหลายงาน
- เพิ่ม fixture-backed claim check: live status ต้องตรง resource/date/time/snapshot ที่กำหนด; “API ติดต่อได้” ไม่พอ มี generated_at และ provenance ด้วย
- แสดงคะแนน r15 evaluator และ v2 evaluator คู่กันบน output เดียวกัน แยกการเปลี่ยนเกณฑ์ออกจากการเปลี่ยนระบบ

Gate: evaluator v2 ตัดสิน hand-checked exemplar ทุกข้อถูก, ไม่มีกรณี answer เทียมจาก status heuristic, และไม่แตะ GT frozen

### ชิ้น 2 — Quick fixes เส้นทางตอบที่ยืนยันแล้ว

ไฟล์: app/pipeline/engine.py, app/pipeline/router.py, app/pipeline/question_frame.py, app/booking/live_status.py และ test ที่เกี่ยวข้อง

- เพิ่ม preflight ตรวจ operation/หลายงานก่อน splitter เดิม โดยใช้ raw กับ variant เดิม; รักษาข้อยกเว้นกติกาแข่งขัน/นโยบาย; อย่า wholesale ย้าย preprocess_input เพราะมันอาจแก้ game target ก่อน split
- เพิ่ม guard เฉพาะ action ที่หลุดจริง: price, live availability, controls, suspension ก่อนเกม detail/general; ทุก guard ต้องมี positive evidence จากคำถามและ negative controls
- แก้ PS5 multi-question ให้สอง task; ตอบแยกสองส่วนอย่างครบ/บอกส่วนที่ยังไม่มีข้อมูล; PUBG price และ Tab controls ต้องไม่ตก game detail เมื่อ keyword พิมพ์ผิด
- ถ้าข้อมูลสดใช้ไม่ได้ ตอบ cannot confirm; ข้อถามเฉพาะเครื่องไม่ควรแปลงเป็นถามรายชื่อเกม

Gate: confirmed defects ตัวอย่าง 5 แบบได้ route/outcome ที่ถูก, คำถาม clean และ negative controls ไม่ถูกซ่อมผิด, ไม่มีข้อความจอง/ราคา/กฎที่ไม่รองรับ

### ชิ้น 3 — Candidate recovery ที่จำกัดและตรวจคะแนนได้

ไฟล์: app/pipeline/preprocess.py, app/pipeline/input_recovery.py, app/core/*recovery*.py, app/pipeline/ambiguity_gate.py; เพิ่ม module ใหม่เฉพาะเมื่อของเดิมต่อยอดไม่ได้

- เก็บตัวสะกดผิดที่ทำให้ route หลุดจริงจาก 239 IDs เป็นกลุ่ม intent span; เริ่มด้วยการลบ/เพิ่ม/สลับ/เบิ้ลและแป้นใกล้ในคำสำคัญ ไม่ท่องจำประโยคเต็ม
- สำหรับไทย ระวังสระนำ/วรรณยุกต์/อักษรผสมและข้อความไม่มีช่องว่าง ใช้หน่วยที่ทดสอบได้ (ตัวอักษรและกลุ่มอักขระตามบริบท) ไม่สมมติว่า Unicode grapheme cluster เท่ากับคำหรือพยางค์ไทย; อังกฤษระวัง token boundary/คำที่กลายเป็นคำจริง
- ขยายจากหนึ่ง typo ไปหลายจุดด้วย candidate budget คงที่ และเลือกแก้เฉพาะ span ที่มีหลักฐาน ไม่ปล่อยจำนวน variant โตแบบคูณ; ถ้าเกินงบให้ถาม/ใช้ raw ไม่ยืดเวลาจน timeout
- เปิด trace เปรียบเทียบ raw กับ top candidates, score component, veto, split/route ที่จะได้; ตรวจ false correction บน clean/OOD และ holdout ที่ไม่ได้ใช้จูน

Gate: เพิ่มการกู้บน reviewed typo subset โดยไม่มี harmful false correction ใน negative controls และ protected fields; หากชนความหมายจริงให้ถามกลับอย่างเจาะจง

### ชิ้น 4 — คำตอบและแหล่งข้อมูล

ไฟล์: app/pipeline/validator.py, app/pipeline/schemas.py, app/pipeline/bilingual_english.py, app/booking/live_status.py, app/calculator/service_fee.py (อ่านเพื่อตรวจ; เปลี่ยนเมื่อหลักฐานพอ)

- เพิ่ม optional per-task outcome/source coverage โดยไม่หัก API เก่า; renderer ต้องรู้ส่วนไหนตอบได้/ไม่ได้ เพื่อไม่ให้คำตอบครึ่งเดียวดูเหมือนครบ
- Booking: fixture ทดสอบ snapshot ที่ source, date, generated_at, resource/slot ครบ; cache เดิม reuse ตามวันที่; หาก timestamp เก่า/slot ขาด/ตารางขัดกัน ให้ unknown ไม่ใช่ available; คืนจำนวนว่าง/ทั้งหมดกับรายช่องเมื่อหลักฐานสดพอ
- ราคา: ตรวจภาพที่ app/calculator/service_fee.py อ้าง (Jan 2026) กับภาพที่หน้า booking ใช้ (Aug 2026), ถอดตารางและความต่างเป็นรายกลุ่ม/โซน; ต้องให้เจ้าของยืนยันฉบับมีผลก่อนเปลี่ยนตัวเลขหรือคำตอบราคา
- English: route คำถามอังกฤษให้ถูกก่อน แล้วแปล/ตอบเฉพาะ fact ที่มี coverage; 72/84 competition clean cases ต้องแก้ expected status ให้ตรงสถานะอนุมัติ หรืออนุมัติคำแปลก่อน; ไฟล์ปุ่ม VALORANT แหล่งรองต้องระบุข้อจำกัดว่าคีย์จริงบนเครื่องศูนย์ยังไม่ตรวจ

Gate: fixture booking ยืนยันคำตอบว่าง/ถูกจอง/unknown ได้จริงใน test; ไม่มีการอ้างราคา กติกา คีย์บอร์ด หรือภาษาอังกฤษเกิน source coverage; owner pending ไม่ถูกซ่อนด้วยคำตอบเดา

### ชิ้น 5 — ตรวจรวม, เวลา, และส่งแพ็กเกจทดลอง

- รัน 239 IDs แบบ paired, 2,000 คู่เดิมโดยไม่สร้าง typo ใหม่, reviewed holdout แยกจากชุดจูน, clean/OOD/negative controls, calendar ไทย/อังกฤษ, API เปิด LLM และ package ที่ใช้งานจริงตามขอบเขตทรัพยากร
- วัด deterministic pipeline, client→HTTP response, และ Dashboard fetch แยกกัน; 20 วินาทีของ GT เก่าเป็นตัวเทียบย้อนหลัง; production target 10 วินาทีจาก docs/77 ต้องวัดบนเครื่อง/ภาระงานที่กำหนด รวม concurrency และ fallback เมื่อ dependency ล่ม; 119.188 วินาทีต้อง trace ก่อนระบุสาเหตุ
- เปิด flag ใหม่ในแพ็กเกจแยกจาก r15; sanity check ข้อสำคัญ, บันทึก manifest/hash/config/runtime profile; เก็บ rollback ที่ใช้คืน r15 ได้โดยไม่เปลี่ยนข้อมูลเจ้าของหรือ log เก่า

Gate: ดู “เกณฑ์ปล่อย” ข้างล่าง; ถ้า source owner pending ให้ระบุฟีเจอร์ที่ยังไม่รับรอง แทนการสรุปว่าแพ็กเกจทั้งหมดถูกต้อง

## 5. ชุดทดสอบและเกณฑ์ปล่อยที่วัดได้

| ด้าน | ต้องทดสอบ | เกณฑ์รับ |
|---|---|---|
| Safety | ตัวเลข เวลา วันที่ PC1/PC11, negation, ชื่อเกม/กลุ่มผู้ใช้, OOD, play/pay | ไม่มีการเปลี่ยน protected value; คำกำกวมไม่กลายเป็นคำตอบมั่นใจสูงผิดเรื่อง; harmful claim = 0 ในชุดที่ตรวจความจริงได้ |
| Intent | 239 regressions + clean ของคู่เดียวกัน + holdout ใหม่ | รายงานจำนวนที่แก้/ยังผิด/ถามกลับ/label defect แยก; confirmed defects ที่ปล่อยต้องแก้หรือมี safe fallback และเหตุที่ตรวจได้; clean regression ใหม่ทุกข้อถูก triage |
| Completeness | สองงานในหนึ่งประโยค, หลาย target หนึ่งงาน | ทุก task มี answer/outcome; evaluator all-groups จับคำตอบขาดได้; การ split ไม่เพิ่มงานเทียมใน competition/damage policy |
| Booking | open/booked/partial overlap/close/boundary/no_show/slot missing/source invalid/stale/date mismatch/maintenance | ผลตรง fixture สำหรับ resource + ช่วงเวลา + snapshot; HTTP 200 หรือ source marker อย่างเดียวไม่ถือว่าถูก; ถ้าไม่แน่ให้ unknown |
| Language/source | ไทย/อังกฤษ, pending localization, ราคา/กฎ/ปุ่มรอง | คำตอบอยู่ภาษา/หัวข้อที่ถาม; fact มี source และ coverage; owner pending ไม่ถูกนับเป็น typo fail |
| Runtime | pipeline และ HTTP บน package, dependency up/down, หลายคำขอพร้อมกัน | ไม่ค้างไร้ขอบเขต; latency/report แยก 10s production target กับ 20s legacy GT; หากไม่ถึง production target ต้องรายงานและไม่อ้างว่าผ่าน SLA |

ห้ามประกาศว่า “แก้ครบ” จาก synthetic GT อย่างเดียว ตัวเลขผ่านต้องมีตัวหารแยก: confirmed gold, source-supported candidate, ambiguous, owner pending, evaluator defect และ live fixture ตัวเลขเป้าด้าน uplift ต้องกำหนดจาก reviewed subset ที่เสร็จก่อน ไม่ตั้ง threshold ย้อนหลังเพื่อให้รอบที่รันผ่าน

## 6. ลำดับตัดสินใจหากเวลาหรือข้อมูลจำกัด

ทำชิ้น 0–1 ก่อนเพื่อเลิกหลอกตัวเองด้วยคะแนน; ชิ้น 2 ให้ผลเร็วกับข้อผิดจริง 4–5 แบบ; ชิ้น 3 ขยายความทน typo เฉพาะเมื่อวัด false correction ได้; ชิ้น 4 ทำส่วนข้อมูลที่พิสูจน์ได้และทำเครื่องหมาย owner pending; ชิ้น 5 เทียบทั้งระบบก่อนให้ใช้จริง แต่ละชิ้นแก้โค้ดน้อยที่สุดและรัน regression ที่เกี่ยวก่อนชุดใหญ่

**ไม่ต้องรอเจ้าของเพื่อทำ:** evaluator v2, triage จากหลักฐาน, preflight/split/intent guards, bounded candidates, fixture จำลอง, API test, latency trace, และแพ็กเกจทดลองแยก

**ต้องการคำตอบจากเจ้าของก่อนรับรองข้อมูล:**
1. ตารางค่าบริการที่ใช้กับลูกค้าปัจจุบันคือฉบับใด ระหว่างภาพ Jan/Aug 2026 และมีวันที่เริ่มใช้เมื่อใด? หากตัวเลขต่างกัน ขอรายการโซน/กลุ่มผู้ใช้ที่เปลี่ยน
2. กติกาแข่งขันภาษาอังกฤษฉบับใดอนุมัติให้เผยแพร่? ถ้ายังไม่มี ให้คง localization_pending และปรับ GT ให้ตรงสถานะจริง
3. คู่มือปุ่มเกมบนเครื่องศูนย์ตรงกับแหล่งรองที่เก็บอยู่หรือไม่ โดยเฉพาะ VALORANT Tab? หากยังไม่ตรวจ ให้ตอบพร้อมข้อจำกัด
4. เมื่อพร้อมกลับมาทดสอบจองจริง ขอวัน/เวลา/ช่องและสถานะที่เจ้าของทราบแน่ พร้อมเวลาที่บันทึกผล ข้อนี้พักไว้ตามคำขอเดิมและไม่ขัดขวางงาน logic

## 7. สิ่งที่ตรวจยืนยันแล้วและสิ่งที่ยังต้องพิสูจน์

ยืนยันจากการอ่านโค้ด: splitter มาก่อน preprocess ในเส้นหลัก; มี canonical shortcut ก่อน split; preprocess มีตัวซ่อมและ variants อยู่แล้ว; PipelineAnswer ยังไม่มี typed status; live adapter มี cache ตามวันที่, source marker, date check และ timeout; GT ใช้ 20 วินาที; เอกสาร rollout เดิมเสนอ production target 10 วินาที

ยังต้องพิสูจน์ด้วยการลงมือ: preflight ใหม่เข้ากับ canonical/exception paths ทุกแบบ, generated_at ของ dashboard ที่ใช้งานจริงสะท้อนข้อมูลล่าสุดเพียงใด, false correction บนคำถามจริง, การตอบตาม booking truth, ราคาเวอร์ชันที่มีผล, และ latency บนแพ็กเกจ/เครื่องเป้าหมาย

รายงานรอบต่อไปต้องบอกอย่างตรงไปตรงมาว่าเปลี่ยนโค้ดอะไร ทดสอบชุดใดผ่านหรือไม่ผ่าน และอะไรยังรอเจ้าของ ห้ามใช้จำนวน HTTP 200 หรือคะแนนรวมอย่างเดียวแทนคำตอบว่า “ถูกต้อง”
