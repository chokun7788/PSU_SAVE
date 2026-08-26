# Action Plan จาก Per-Case Audit 162 เคส

วันที่: 2026-08-23

## ข้อสรุป

การตรวจรายข้อไม่ได้หมายความว่าควรเขียน exception 162 ชุด แต่ใช้แต่ละข้อเป็นหลักฐานเพื่อหา implementation unit ที่เป็นต้นเหตุร่วม ถ้าแก้รายคำถาม ระบบจะผ่าน test ชุดนี้แต่พังกับคำใหม่ที่ใช้รูปภาษาใกล้เคียงกัน

จาก 162 เคส พบ implementation units ที่ควรแก้จริง 9 ส่วน:

1. Request-local state initialization
2. Boundary/context-aware lexical matcher
3. General-vs-PSU equipment scope arbitration
4. Deterministic/LLM route arbitration
5. General one-call operation path และ latency budget
6. Freshness/source precondition
7. Compound semantic split และ subanswer coverage
8. General output-shape contract
9. Semantic evaluator แทน exact keyword อย่างเดียว

## วิธีหาว่าแต่ละข้อพลาดตรงไหน

ใช้ Fault Localization ตามลำดับนี้:

1. อ่าน intent ของคำถามและ expected contract จาก case bank
2. อ่านคำตอบจริงเพื่อดูว่าตอบคนละเรื่อง, ขาดคำตอบ, ไม่มี source หรือผิดรูปแบบหรือไม่
3. เทียบ No-LLM กับ LLM ด้วย ID เดียวกันเพื่อหา first divergence
4. ไล่ `route -> universal intent -> ambiguity -> question frame -> candidate -> execution -> validation`
5. จุดแรกที่ state เปลี่ยนจากสิ่งที่คำถามต้องการคือ first wrong stage
6. ถ้า route ถูกแต่คำตอบผิด ให้ตรวจ target/source/answer contract และ model output
7. ถ้าคำตอบถูกแต่ช้า ให้แยก wall time, visible LLM time, queue/hidden overhead และ fallback work
8. สร้าง counterfactual path ว่าถ้าตัดสินถูกควรใช้ structured, fast, retrieval, clarification หรือ LLM แบบใด
9. เขียน regression assertion ที่ตรวจ behavior ไม่ใช่แก้ expected text ให้ตรง output เดิม

## Wave 1: P0

### 1. แก้ Request State Exception

- กระทบโดยตรง: 2 เคส
- เคสหลัก: `MB-0607-CR-071`, `MB-0636-ANA-010`
- จุดเสีย: `_answer_single()` ใช้ `rag_llm_attempted`/`rag_source_conflict` ก่อน initialize
- วิธีแก้: สร้าง `RequestExecutionState` หรือ initializer กลางก่อนแยก single/compound
- ห้ามแก้ด้วยการดัก `UnboundLocalError` เพราะจะซ่อน state bug
- Test: single RAG fallback, bare booking clarification, no-context, source conflict และ compound path

### 2. สร้าง Lexical Matcher กลาง

- กระทบ confirmed wrong answers โดยตรงอย่างน้อย 10 เคส และลด validation false warnings เพิ่มเติม
- ตัวอย่าง collision: `ข้อเสีย/เสีย`, `Crossing/cross`, `กากบาท/บาท`
- วิธีแก้:
  - English ใช้ token boundary หรือ alias tokenization
  - Thai ใช้ phrase/context rules และ negative phrase
  - แยก `contains_phrase`, `contains_token`, `contains_price_signal`, `contains_control_signal`
  - คืน matched span/reason เพื่อ trace ได้
- Test matrix ต้องมีทั้ง positive และ negative pair ไม่ใช่ทดสอบแต่คำที่เคยพัง

### 3. Freshness Guard

- กระทบตรง: `MB-0649-ANA-023`
- วิธีแก้: `ตอนนี้/ล่าสุด/วันนี้/ข่าว/ชาร์ต/สถานะปัจจุบัน` สร้าง source requirement
- มี live Web/API: ตอบพร้อม URL และ retrieval timestamp
- ไม่มี live source: safe no-answer หรือถาม platform/region
- Test ต้องห้าม model-generated current name โดยไม่มี source

## Wave 2: P1 Correctness

### 4. แยก General Concept จาก PSU Inventory

- กระทบ: mechanical keyboard 26 เคส
- จุดเสีย: `looks_like_equipment_query()` ใช้คำนามอุปกรณ์เพียงคำเดียว
- วิธีแก้:
  - definition cues: `คืออะไร`, `หมายถึง`, `ต่างกัน`, `ข้อดีข้อเสีย` ให้ general ได้
  - inventory cues: `ศูนย์มี`, `มีกี่`, `รุ่นอะไร`, `อยู่โซนไหน`, `อุปกรณ์ของ PSU` ให้ structured
  - ถ้าไม่มี PSU/inventory context ห้าม structured equipment precondition ผ่าน
- Existing gap: test ปัจจุบันมี technical general route แต่ยังไม่มี mechanical-vs-inventory contrast matrix

### 5. Route Arbitration ระหว่าง Deterministic กับ LLM

- กระทบตรง: `MB-0240-G-152`
- Existing test `tests/smoke_test_correctness_control_flow_v1.py` พิสูจน์ ranking ถูกเฉพาะ `experimental_allow_llm=False`
- วิธีแก้:
  - exact/high-confidence operation frame ซ่อม incompatible route ได้ แม้ route ปัจจุบันไม่ใช่ general
  - deterministic exact target/operation เป็น hard evidence
  - LLM review เปลี่ยน route ได้เมื่อมีเหตุผลและ confidence margin สูงกว่าเท่านั้น
  - trace ต้องเก็บ old/new route และ evidence ที่ชนะ
- เพิ่ม LLM-on test โดย stub Intent ให้จงใจตอบ equipment แล้ว assert ว่า structured game ranking ยังชนะ

### 6. Compound Semantic Coverage

- กระทบตรงที่พบ: `MB-1320-C-084`
- จุดเสีย: comparison pair ถูก splitter แยกผิดและ booking ซ้ำใน child
- วิธีแก้:
  - parse operations ก่อน split: `compare(VR30, VR60)` และ `booking_howto(VR)`
  - planner task ต้องรักษา compared entities ทั้งคู่
  - composer มี coverage slots เช่น `comparison`, `price_30`, `price_60`, `booking_steps`
  - Final Hard Veto ไม่ให้ผ่านเมื่อ child ใด no-answer ทั้งที่มี structured source
- เพิ่มใน `smoke_test_compound_question_planner.py` และ `smoke_test_query_planner.py`

### 7. Product Scope และ Missing-Input Clarification

- กระทบตรง: `MB-0650-ANA-024`
- วิธีแก้: แยกสามสถานะ `safe_general_allowed`, `missing_required_input`, `out_of_scope_or_unsafe`
- ข้อความ `ช่วยทำการบ้านคณิตให้หน่อย` ไม่มีโจทย์ จึงควรอยู่ missing input ไม่ใช่ PSU-only refusal
- หลังผู้ใช้ส่งโจทย์จริงจึงค่อยเรียก General LLM ภายใต้ safety/latency policy

## Wave 3: P1 Latency

### 8. Clear-General One-Call Path

- กระทบตรง: translation/promo 40 เคสเกิน 10 วินาที
- หลักฐาน: focused full trace แสดง Intent LLM + General LLM และ full-run overhead signature เหมือนกันทั้งกลุ่ม
- วิธีแก้:
  - deterministic operation detector สำหรับ `translate`, `define`, `rewrite`, `generate_one_sentence`
  - route ชัดแล้วข้าม Intent LLM
  - max actual LLM calls = 1
  - token budget ตาม shape: คำแปล 32-64, หนึ่งประโยค 64-96, อธิบายสั้น 96-128
  - model work budget 5-7 วินาที และ backend deadline 8.5-9 วินาที
  - deadline ใกล้หมดให้ deterministic bounded fallback ไม่รอจน 20 วินาที
- Existing gap: `smoke_test_llm_timing_and_general_guard.py` ตรวจ metadata/route แต่ยังไม่ assert actual call count และ output shape

### 9. Single LLM Slow Generation

- กระทบตรง: `MB-1326-GL-001`
- visible General LLM ใช้ 12.831 วินาที
- วิธีแก้: output budget selector, stop condition, shorter prompt, timeout ที่สอดคล้อง SLA และ complete-sentence fallback
- สำหรับ common definitions อาจมี deterministic micro-answer cache แต่ไม่ควรแทน LLM ทุก general query

### 10. ตัด Repeated Fuzzy Work

- กระทบชัดใน ranking fallback แม้ root correctness ต้องแก้ route ก่อน
- วิธีแก้:
  - ตรวจ named-game signal ก่อน scan
  - resolve game match หนึ่งครั้งต่อ normalized query
  - เก็บใน request context ให้ handlers ใช้ร่วมกัน
  - ทำ exact alias index ก่อน SequenceMatcher
- Test: count `_match_supported_game()` invocation และ assert ไม่เกินหนึ่งครั้งต่อ request

## Wave 4: P2 Output และ Evaluator

### 11. General Answer-Shape Contract

- กระทบ: 66 quality-risk cases เป็น primary cluster และซ้อนในเคสช้า/failed เพิ่มเติม
- Signals ที่ตรวจ: body ยาว, mixed particles, emoji, awkward Thai, repetition, truncation และรูปแบบไม่ตรงคำสั่ง
- วิธีแก้:
  - parse `max_sentences`, `max_lines`, `bullet_count`, `tone`, `language`, `allow_emoji`
  - ส่ง contract เข้า prompt และ validator
  - deterministic cleanup ทำได้เฉพาะสิ่งไม่เปลี่ยนสาระ เช่นลบ emoji/เลือกคำลงท้าย
  - repetition/truncation ใช้ bounded repair 1 ครั้งภายใน deadline
  - ถ้า repair ไม่ทัน ให้ fallback สั้นที่จบประโยค
- Regression ต้องตรวจ shape จริง ไม่ใช่แค่ keyword

### 12. Semantic Evaluator

- กระทบ false negative: 13 เคส
- พบ false positive เพิ่ม เช่น GPU ซ้ำและ compound ขาด comparison
- วิธีแก้:
  - Thai normalization และ synonym groups
  - ตรวจ category/operation/target/source/subanswers
  - style score แยกจาก factual correctness
  - ใช้ semantic reviewer เฉพาะ failed/high-risk sample ไม่จำเป็นต้องเรียก modelทุกเคส
- ห้ามเปลี่ยน expected เพียงเพราะ model ใช้คำอื่น ต้องยืนยันความหมายก่อน

## ลำดับ Regression ที่ควรรัน

1. P0 focused tests: exception + lexical collision + freshness
2. General scope matrix: mechanical concept เทียบ PSU inventory
3. LLM-on route arbitration: game-zone ranking และ Animal Crossing
4. Compound coverage: VR comparison + booking
5. General one-call tests: 40 translation/promo variants
6. Output-shape tests: ตัวแทนแต่ละ modifier แล้วตามด้วย 66 flagged cases
7. Full 1,600 No-LLM และ Typhoon ด้วย product profile 10 วินาที
8. หลัง sequential ผ่านจึงทำ 5-session และ 20-session load test

## Acceptance Criteria รอบถัดไป

- Exception = 0
- Confirmed wrong-route casesใน audit set = 0
- Unsupported current claim without source = 0
- Missing compound subanswer = 0
- Clear-general actual LLM call count <= 1
- Sequential requests >10s = 0
- ไม่มี obvious repetition/truncation
- Keyword false negatives 13 เคสผ่าน semantic contract โดยไม่เปิดช่องให้คำตอบคนละเรื่องผ่าน
- Full call ledger เก็บ actual/skipped call, queue wait และทุก timing stageแยกจาก compact trace

รายละเอียดรายข้อทั้งหมดอยู่ใน `PER_CASE_AUDIT_LOG_162.md`, `PER_CASE_AUDIT_LOG_162.csv` และ `PER_CASE_AUDIT_LOG_162.jsonl`
