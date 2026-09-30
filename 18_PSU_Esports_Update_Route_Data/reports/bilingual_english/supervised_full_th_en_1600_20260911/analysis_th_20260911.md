# รายงานทดสอบ Thai + English 1,600 ข้อ

> วันที่รัน: 11 กันยายน 2026 | Profile: Local LLM + Semantic RAG + English draft-preview
>
> ขอบเขต: รันแบบ serial worker เดียวกับ `Typhoon2.5-Qwen3-4B` ไม่มี browser, HTTP queue หรือ concurrent users ผลนี้จึงเป็นพฤติกรรมของ pipeline ไม่ใช่ผล load test หน้าเว็บ

## ผลที่ยืนยันได้จาก Raw Log

| ชุดทดสอบ | Content/contract pass | P50 | P95 | เกิน 10 วินาที | Worker crash | Harness timeout |
|---|---:|---:|---:|---:|---:|---:|
| Thai 1,600 | 1,388 / 1,600 (86.75%) | 0.767s | 10.390s | 89 | 0 | 0 |
| English Shadow 1,600 | 1,061 / 1,600 (66.31%) | 0.030s | 2.927s | 4 | 0 | 0 |

ค่า P50/P95 ข้างต้นตัด `watchdog_escape_observed` ออกแล้ว แต่ **ไม่ถือว่า SLA ผ่าน**: มีการคืนผลหลังเวลาควบคุมของ evaluator 25 วินาที 2 เคส ได้แก่ `MB-1099-SF-130` (887.269s) และ `EN-SHADOW-0608` (7,902.739s) ทั้งคู่ลงท้ายด้วย `pipeline:request_timeout_no_answer` ซึ่งยืนยันว่า deadline ภายใน pipeline ยังหยุดงานจริงไม่ได้ในทุกเส้นทาง

## ผลเทียบภาษา

- จับคู่ได้ครบ 1,600 คู่ด้วย `English source_case_id -> Thai benchmark id`
- Route category ต่างกัน 595 คู่
- รูปแบบ bullet ต่างกันอย่างมีนัย 480 คู่
- หนึ่งภาษาผ่าน แต่อีกภาษาหนึ่งไม่ผ่าน 387 คู่

ดังนั้น ภาษาอังกฤษยังไม่ใช่เพียง “คำตอบภาษาไทยที่เปลี่ยนคำ” แต่ยังใช้ route และ template คนละชุดในหลายกรณี

## ปัญหาหลักที่พบ

### P0: Timeout ถูกตรวจพบ แต่ยังหยุดงานไม่ได้จริง

**หลักฐาน:** 2 เคสข้างต้นตอบกลับเป็น timeout หลัง 887 และ 7,902 วินาที แทนที่จะคืน safe outcome ภายใน 20 วินาที

**สาเหตุที่เป็นไปได้:** timeout ภายในเป็นเพียง cooperative check หรืออยู่หลัง native/LLM/RAG call ที่ block อยู่; worker/evaluator ไม่สามารถตัดงานได้ทันทีในเส้นทางนั้น

**ผลกระทบ:** ค่า latency รายงานหลอกได้ และผู้ใช้จริงอาจรอค้างนานมาก แม้ข้อความสุดท้ายจะบอกว่าหมดเวลาแล้ว

**การแก้ที่ต้องทำก่อนเปิดใช้จริง:** แยก pipeline request ไป child process ที่ parent terminate ได้, ส่งผลผ่าน bounded IPC, คืน `request_timeout_no_answer` ภายใน 20 วินาที, recycle worker แล้วรัน 2 เคสนี้แบบ isolated ก่อน regression เต็มชุด

### P1: Thai general fallback ใช้เวลาจนเกือบ 20 วินาที แต่จบด้วย no-answer

**หลักฐาน:** Thai มี 156 failures ใน `general_llm`; slow cases ส่วนใหญ่เป็นคำถามนอกขอบเขต PSU เช่น API, JSON, GPU และ latency ซึ่งรอราว 19 วินาทีแล้วตอบว่าไม่มีข้อมูล

**ข้อสังเกต:** หากนโยบายบอตคือคุยเฉพาะ PSU Esports การตอบ no-answer นั้นปลอดภัยกว่า แต่ชุด benchmark บางข้อยังคาดหวังคำตอบทั่วไป จึงเป็นทั้ง contract drift และ latency waste

**การแก้:** Boundary guard ต้องตัดสิน no-answer ก่อนเรียก LLM เมื่อไม่มี PSU entity/source signal; แก้ gold contract ให้ไม่ถือ no-answer เป็น failure สำหรับโจทย์นอก scope ที่ตั้งใจห้ามตอบ

### P1: English routing ยังเสีย hierarchy ของ intent

**หลักฐาน:** English failure 518 ข้อเป็น `category`; ตัวอย่าง route ที่ผิดซ้ำคือ `general/knowledge -> no_answer` 266, `competition_rules -> games` 55, `multi_question -> service_fee` 50 และ `members/overview -> no_answer` 34

**สาเหตุ:** English token/keyword route เลือก category ต้นทางเร็วเกินไป; game mention ชนะคำว่า rules/match; multi-question ไม่ถูก split ก่อนคิดราคา; fallback English no-answer ถูกนับเป็น category mismatch

**การแก้:**

1. สร้าง `QuestionFrame` ภาษาอังกฤษก่อน lock route โดยมี `primary_intent`, `secondary_intents`, `target`, `facet` และ `is_multi_question`
2. หาก route deterministic ไม่มั่นใจ ให้ Intent LLM ตรวจ Frame แบบ JSON สั้น ๆ ก่อน no-answer
3. ให้ `competition_rules` veto game detail เมื่อมี `rule`, `format`, `match`, `penalty`, `bracket` หรือ `check-in` signal
4. split multi-question ก่อน service-fee calculator แล้วตอบเป็น response blocks หลายส่วน
5. แก้ evaluation contract ให้ `no_answer` ถือว่า pass เฉพาะโจทย์ที่ไม่มี verified PSU evidence จริง

### P1: English knowledge ยังไม่ครบและมี Thai prose leak

**หลักฐาน:** `pipeline:english_no_answer` เกิด 358 ข้อ, `missing_english_localization` 42 ข้อ และพบ `thai_prose_leak` 23 ข้อ โดยเฉพาะ member directory ที่ส่งชื่อ/ตำแหน่งภาษาไทยทั้งก้อนกลับไป

**การแก้:**

1. สร้าง approved localization overlay ตาม `content_id + field`; Thai record ยังคงเป็น source of truth
2. ชื่อบุคลากรไทยที่เป็นชื่อทางการสามารถแสดงได้ตามที่ผู้ดูแลอนุมัติ แต่ role/คำอธิบายต้องมี English field หรือแสดง English no-answer
3. ไม่ใช้ Local LLM แปลข้อมูลสด; ใช้ได้เพียงสร้าง draft offline แล้ว human approve ก่อน publish
4. English RAG index ต้อง index เฉพาะ localization ที่ approved และ hash ต้นฉบับยังตรง

### P2: Format parity ระหว่างสองภาษาไม่สม่ำเสมอ

**หลักฐาน:** 480 คู่มีจำนวน bullet ต่างกันตั้งแต่ 3 บรรทัดขึ้นไป แม้ข้อมูลชุดเดียวกัน เช่น catalog, rules และ schedule

**การแก้:** สร้าง canonical `AnswerPlan` และ `ResponseBlock` ก่อน render แล้วให้ Thai/English render จาก block เดียวกัน เช่น `title`, `summary`, `sections`, `items`, `source`; ต่างกันเฉพาะ localized strings ไม่ใช่ branching ของ business logic

## ลำดับดำเนินการที่แนะนำ

1. **P0:** แก้ hard cancellation และทดสอบ 2 watchdog-escape cases ซ้ำจนไม่มีผลเกิน 20 วินาที
2. **P1:** ทำ English QuestionFrame + LLM intent review เฉพาะตอน deterministic route อ่อนหรือขัดแย้ง
3. **P1:** ทำ English multi-question splitter และ competition-rule precedence
4. **P1:** ปิด general LLM สำหรับคำถามนอก PSU scope ที่ไม่มี evidence
5. **P2:** ย้าย Thai/English templates ไปใช้ canonical response blocks เดียวกัน
6. **P2:** เติม/approve English localization เป็นหมวด: members, booking/rules, competition, equipment, game detail
7. รัน focused regression ของกลุ่มที่พลาดก่อน แล้วค่อยรัน Thai + English 1,600 ซ้ำ

## ข้อสรุป

ระบบตอบข้อเท็จจริงที่เข้า structured โดยตรงได้ดีและภาษาอังกฤษเร็วในเส้นทางนั้น แต่ยังไม่พร้อมเปิดเป็น English production chatbot เพราะ routing, localization และ timeout cancellation ยังมีช่องว่างชัดเจน การเพิ่ม LLM ควรใช้เป็น **bounded semantic recovery หลัง deterministic route ไม่มั่นใจ** ไม่ใช่ปล่อยให้ทุกคำถามไหลเข้า LLM/RAG; วิธีนี้จะเพิ่มความเข้าใจของคำถามธรรมชาติ โดยยังรักษาความเร็วและข้อเท็จจริงที่ตรวจสอบได้

## ไฟล์ประกอบ

- Raw Thai: `th_results.jsonl`
- Raw English: `en_results.jsonl`
- Machine-readable analysis: `analysis.json`
- English technical summary: `analysis.md`
- Evaluator: `tools/run_supervised_bilingual_full_eval.py`
- Analyzer: `tools/analyze_supervised_bilingual_full_eval.py`
