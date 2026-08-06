# Pretest Answer Quality Review - 2026-08-01

## ขอบเขตที่เช็ค

- ยังไม่ได้รัน Full Eval ทุกโมเดลใหม่
- เช็คจาก case bank 1,600 cases, report No-LLM ล่าสุด, partial benchmark หลังแก้ regression, และ spot-check คำถามเสี่ยง
- case bank 1,600 cases อยู่ที่:
  - `data/eval/model_benchmark_1500.jsonl`
  - ชื่อไฟล์ยังเป็น `1500` แต่มีจริง 1,600 cases

## โครงสร้าง case 1,600

- PSU/domain cases ที่ไม่จำเป็นต้องใช้ LLM: 1,321 cases
- general LLM cases: 279 cases
- กลุ่มใหญ่:
  - `game_controls`: 343
  - `general_llm`: 279
  - `service_fee`: 258
  - `availability_game`: 166
  - `games`: 158
  - `compound`: 89
  - `competition_rules`: 75
  - `members`: 63
  - `equipment`: 58

## สรุปจาก report ล่าสุด

### Full No-LLM report ก่อนแก้รอบท้าย

- Path: `reports/model_benchmark/20260801_143921/REPORT.md`
- Total: 1,600 cases
- Pass rate: 81.81%
- Avg score: 96.87
- Avg sec: 0.631
- P95 sec: 3.1724
- Fail หลัก:
  - `general_llm`: 279 cases
  - `availability_service`: 8 cases
  - `ambiguity_no_answer`: 2 cases
  - `game_controls`: 2 cases

### Partial No-LLM หลังแก้บางส่วน

- Path: `reports/model_benchmark/20260801_145943/no_llm/partial_summary.json`
- Completed: 1,250 / 1,600 cases
- Pass rate partial: 99.68%
- Fail ที่เห็นใน partial:
  - `ambiguity_no_answer`: 2 cases
  - `game_controls`: 2 cases
- หลังจาก partial นี้ มีการแก้เพิ่มแล้ว:
  - capacity route เป็น `reservation/count`
  - Call of Duty action scoring
  - no-answer/general wording current spot-check ไม่ขึ้น `Local LLM` แล้ว

## ปัญหาที่ควรระวังก่อน Full Test ใหม่

### 1. Broad / incomplete game family ยังเสี่ยงเลือกเกมเอง

ตัวอย่าง spot-check ปัจจุบัน:

- `Call of เล่นยังไง`
  - mode: `pipeline:hybrid_guarded_rerank`
  - elapsed ประมาณ 27 วินาที
  - ตอบเป็น `Call of Duty: Modern Warfare III` ทันที
  - ปัญหา: คำว่า `Call of` ยังไม่ครบและมีหลายเกมใน family จึงไม่ควรฟันธง

- `Mario เล่นยังไง`
  - mode: `pipeline:structured_game_controls`
  - ตอบเป็น `Mario Party Superstars`
  - ปัญหา: Mario มีหลายเกมใน current catalog เช่น Mario Kart 8 Deluxe, Mario Party Superstars, New Super Mario Bros. U Deluxe, Super Mario Odyssey จึงควรถามกลับ/แสดงตัวเลือกก่อน

ข้อเสนอ:

- เพิ่ม family ambiguity guard สำหรับ `Call of`, `Mario`, `Resident`, `Overcooked`, `The Last of Us`
- ถ้าผู้ใช้ถาม `เล่นยังไง/ปุ่ม/จองอะไร` แต่ระบุ family ไม่ครบ ให้ตอบแบบตัวเลือก ไม่เลือกเกมเอง
- สำหรับ `Call of` ที่ incomplete มาก ควรถามกลับก่อนเข้า hybrid/RAG

### 2. Hybrid/RAG path อาจช้าในคำถามที่ควรถามกลับ

ตัวอย่าง:

- `Call of เล่นยังไง` ใช้เวลาประมาณ 27 วินาที
- ก่อนหน้านี้ partial benchmark มี `Call of เล่นยังไง` p95/slow case ประมาณ 15 วินาที+

ปัญหา:

- route มั่นใจว่าเป็น `games/game_detail_lookup`
- hybrid retrieval ทำงานทั้งที่ target ยังไม่ชัด
- คำตอบออกมาเป็น fact ของเกมหนึ่งแทน clarification

ข้อเสนอ:

- ก่อน hybrid/RAG ต้องมี target confidence gate
- ถ้า target เป็น family/incomplete alias ให้หยุดที่ clarification
- ตั้ง latency guard สำหรับ hybrid retrieval ในคำถาม ambiguity เช่น skip hybrid เมื่อมี family ambiguity

### 3. คำตอบยาวเกินในบางหมวด

จาก partial result:

- long answers > 1,200 ตัวอักษร: 50 cases
- กลุ่มที่ยาวมาก:
  - `structured_game_controls`
  - `multi_question_splitter`
  - `structured_games_catalog`
  - `games_known_unsupported_fast_path`

ตัวอย่าง:

- `Tekken 8 กับ Mario Kart 8 Deluxe มีปุ่มอะไรบ้าง`
- `Tekken 8 ราคาเท่าไหร่ แล้วมีปุ่มอะไรบ้าง`
- `The Last of Us Part II ปุ่มทั้งหมดมีอะไรบ้าง`

ข้อเสนอ:

- สำหรับ compound ที่มี controls ยาว ให้ตอบ first-pass แบบสรุปก่อน และบอกว่าถ้าต้องการปุ่มทั้งหมดให้ถามชื่อเกมแยก
- หรือจำกัดคำตอบ controls ใน compound ไว้ 5-8 ปุ่มต่อเกม
- แต่ถ้าผู้ใช้ถาม `ปุ่มทั้งหมด` แบบเดี่ยว ยังตอบครบได้

### 4. Clarification preview บางเคสมี fact แต่ไม่มี source line

จาก partial result พบ PSU fact ที่ไม่มี `แหล่งข้อมูล:` 18 cases ส่วนใหญ่เป็น:

- `game_control_missing_game_context`
- `ambiguity_clarification`
- calendar/schedule fast path บางเคส
- `experimental_rag_no_context`

ปัญหา:

- บางคำตอบเป็นแค่ถามกลับ อาจไม่ต้องมี source
- แต่บางคำตอบมี preview facts เช่น `PC มีอะไรบ้าง` ที่แสดงเกม/อุปกรณ์/ราคา ควรมี source line

ข้อเสนอ:

- ถ้า clarification มี preview จาก fact จริง ให้ใส่ source รวมท้ายคำตอบ
- ถ้าเป็น pure clarification ไม่มี fact ไม่จำเป็นต้องใส่ source

### 5. Internal wording ยังมีโอกาสหลุดในบาง path

ใน report ก่อนหน้า/partial เคยเห็น:

- `ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM...`
- `โหมดทดลอง RAG: ยังไม่มี context...`

สถานะ current spot-check:

- `เพลงฮิตตอนนี้คืออะไร`
- `ช่วยทำการบ้านคณิตให้หน่อย`
- `อธิบายคำว่า latency...`

ตอนนี้ตอบเป็น safe no-answer ปกติแล้ว ไม่เห็น `Local LLM`

ข้อเสนอ:

- ยังควร audit ทุก path ที่มีคำว่า `Local LLM`, `โหมดทดลอง RAG`, `experimental`, `RAG`
- user-facing answer ไม่ควรพูดชื่อ internal pipeline ยกเว้น user ถาม technical/debug โดยตรง

### 6. Benchmark ยังมี stale expectation

ตัวอย่าง:

- `Mario Kart Live ถ้าจะเลี้ยวต้องกดอะไร`
- benchmark ยัง expect `Left Stick|เลี้ยว`
- แต่ current catalog ไม่มี Mario Kart Live: Home Circuit แล้ว
- logic ปัจจุบันตอบถูกกว่า: ไม่พบในรายการเกมปัจจุบัน และไม่ดึงปุ่มเกมอื่นมาตอบแทน

ข้อเสนอ:

- ก่อน Full Test ใหม่ควร update case bank:
  - Mario Kart Live current catalog -> expect no-current-game guard
  - หรือแยกเป็น legacy control reference ไม่เอาไปตัดสิน current chatbot

### 7. `general_llm` ต้องแยกวัดจาก PSU-domain

- 279 cases เป็น general LLM โดยตั้งใจ
- No-LLM จะ fail กลุ่มนี้ตามธรรมชาติ
- ถ้ารันรวมแล้วดู pass rate เดียว จะทำให้ core PSU-domain ดูต่ำเกินจริง

ข้อเสนอ:

- Report ควรแสดง 2 ตัวเลข:
  - Overall รวม general
  - PSU-domain only ไม่รวม `general_llm`
- เวลาเทียบ model ให้ดู:
  - general LLM quality
  - PSU-domain regression
  - latency แยกตาม path

## สิ่งที่ควรทำก่อน Full Test รอบถัดไป

1. แก้ family ambiguity guard สำหรับชื่อเกมกว้าง/พิมพ์ไม่ครบ
2. กัน hybrid/RAG ไม่ให้ทำงานเมื่อ target ยังเป็น family ambiguity
3. ปรับ answer length policy สำหรับ compound + controls
4. ใส่ source line ให้ clarification preview ที่มี fact จริง
5. audit internal wording ไม่ให้ `Local LLM` / `โหมดทดลอง RAG` หลุดใน user-facing answer
6. update stale benchmark cases โดยเฉพาะ Mario Kart Live
7. แล้วค่อยรัน Full Eval ใหม่ทุกโมเดล

