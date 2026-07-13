# Thai Response Style Post-processor - 2026-07-07

## เป้าหมาย

เพิ่มชั้นจัดรูปภาษาไทยก่อนส่งคำตอบให้ผู้ใช้ เพื่อให้คำตอบอ่านถูกหลักขึ้น โดยเฉพาะการเว้นวรรคหน้า/หลัง `ๆ`

ตัวอย่าง:

```text
หลายๆอย่าง -> หลาย ๆ อย่าง
ตอบสั้นๆ -> ตอบสั้น ๆ
ข้อ1 -> ข้อ 1
30นาที -> 30 นาที
5คน -> 5 คน
```

## วิธีที่ทำ

เพิ่มไฟล์:

- `app/core/thai_style.py`

แล้วเรียกใช้จาก:

- `app/pipeline/engine.py`

โดยใส่ที่ `_build_result()` ซึ่งเป็นจุดรวมก่อนคืนคำตอบออกจาก pipeline ดังนั้นคำตอบจากทุก mode จะผ่านตัวจัดรูปเดียวกัน เช่น:

- rulebase
- deterministic fast path
- curated RAG
- competition fact card
- no-answer
- multi-question answer

## สิ่งที่ formatter แก้ตอนนี้

- จัด `ๆ` ให้มีช่องว่างหน้า/หลังตามหลักการเขียนภาษาไทย
- จัดเลขติดคำไทย เช่น `ข้อ1`, `30นาที`, `5คน`
- ลดช่องว่างซ้ำ
- ลบช่องว่างก่อน punctuation เช่น `ครับ :` -> `ครับ:`
- เก็บบรรทัด bullet/list ให้ยังอ่านได้
- ไม่แก้ URL, `local://...`, และ inline code ใน backtick

## เหตุผลที่ทำเป็น post-processor

- ไม่ต้องไล่แก้คำตอบใน rulebase/JSONL ทีละจุด
- ไม่เปลี่ยน logic หรือข้อมูลจริง
- ครอบคลุมทุกคำตอบที่ออกจาก pipeline
- ลดความเสี่ยงจากการแก้ source data โดยตรง

## ผลทดสอบ

ทดสอบ style processor:

```text
หลายๆอย่าง ข้อ1 ใช้เวลา30นาที มีผู้เล่น5คน และ PS5
```

ได้:

```text
หลาย ๆ อย่าง ข้อ 1 ใช้เวลา 30 นาที มีผู้เล่น 5 คน และ PS5
```

ทดสอบคำถามจริงในโฟลเดอร์ 20:

- `รายกานแข่งขันมีอะไรบ้าง` -> `games/competition_game_list` / `pipeline:competition_game_list_fast_path`
- `RoV pause เล่นๆ โดนอะไร` -> `competition_rules/competition_rules_lookup` / `pipeline:competition_fact_card`
- `ตอบสั้นๆ ราคา VR เท่าไหร่` -> `service_fee/service_fee_query` / `pipeline:deterministic_calculator_fast`

Compile:

- `python -m compileall app` ผ่านทั้งโฟลเดอร์ 18 และ 20

ไม่ได้ run Ground Truth ตามคำสั่งผู้ใช้

## ไฟล์ที่เพิ่ม/แก้

เพิ่ม:

- `18_PSU_Esports_Update_Route_Data/app/core/thai_style.py`
- `20_PSU_Esports_Vercel_Deploy/app/core/thai_style.py`

แก้:

- `18_PSU_Esports_Update_Route_Data/app/pipeline/engine.py`
- `20_PSU_Esports_Vercel_Deploy/app/pipeline/engine.py`

## ข้อจำกัด

นี่เป็นตัวจัดรูปภาษาไทยระดับ presentation ไม่ใช่ grammar checker เต็มรูปแบบ จึงยังไม่ตรวจเรื่อง:

- การเลือกใช้คำราชาศัพท์
- ความกำกวมของประโยค
- ความสละสลวยแบบ human editor
- ความถูกต้องเชิงข้อมูล

ถ้าต้องการตรวจภาษาไทยละเอียดขึ้นในอนาคต ควรเพิ่ม `Thai style lint` เป็นอีกชั้นหนึ่ง โดยเริ่มจาก rule ที่วัดผลได้ก่อน เช่น `ๆ`, เลขติดคำไทย, เว้นวรรครอบวงเล็บ, และคำซ้ำที่พบบ่อย
