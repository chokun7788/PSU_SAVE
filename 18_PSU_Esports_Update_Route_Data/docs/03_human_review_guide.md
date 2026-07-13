# Human Review Guide

Human Review คือขั้นตอนให้คนเช็คคำตอบของ AI เพื่อหาว่าผิดเพราะอะไร แล้วนำกลับไปแก้ Data, Rule, Router หรือ Prompt

## คะแนนที่แนะนำ

ให้คะแนน 0-4 ในแต่ละหัวข้อ

| คะแนน | ความหมาย |
|---:|---|
| 4 | ถูกครบ ใช้งานจริงได้ |
| 3 | ถูกเป็นหลัก แต่ขาดรายละเอียดเล็กน้อย |
| 2 | มีส่วนถูก แต่ยังเสี่ยงทำให้เข้าใจผิด |
| 1 | ผิดเป็นหลัก แต่มีบางคำเกี่ยวข้อง |
| 0 | ผิด/ไม่มีข้อมูล/ตอบมั่ว |

## มิติที่ควรให้คะแนน

- `correctness_score` คำตอบถูกไหม
- `grounding_score` อ้างอิงข้อมูลจริงไหม
- `completeness_score` ตอบครบตามคำถามไหม
- `tone_score` สุภาพ อ่านง่าย เหมาะกับลูกค้าทั่วไปไหม
- `route_score` route ที่ใช้เหมาะไหม เช่น ควรเป็น calculator แต่ไปเข้า LLM หรือไม่
- `actionability_score` ผู้ใช้เอาคำตอบไปทำต่อได้ไหม

## Decision

- `pass` ใช้งานได้
- `minor_fix` แก้เล็กน้อย เช่น เพิ่มรายละเอียดวันศุกร์
- `major_fix` ผิดสำคัญ เช่น ราคาผิด กลุ่มผู้ใช้ผิด
- `needs_data` ข้อมูลไม่มี ต้องขอข้อมูลเพิ่ม
- `needs_policy` ต้องถามผู้ดูแล เพราะข้อมูลมีผลทางกฎ/เงื่อนไข

## สาเหตุผิดที่ควร tag

- `missing_data` ข้อมูลไม่มีจริง
- `retrieval_miss` มีข้อมูลแต่ค้นไม่เจอ
- `wrong_route` ใช้ route ผิด
- `ambiguous_question` คำถามกำกวม
- `alias_missing` คำเหมือน/คำสะกดไม่ถูก map
- `calculator_bug` คำนวณผิด
- `llm_truncation` LLM ตอบไม่ครบหรือตัดจบ
- `prompt_issue` prompt ไม่บังคับให้ตอบครบพอ
- `ground_truth_issue` เฉลยผิดหรือแคบเกินไป

## วิธีใช้จริง

1. รัน Ground Truth หรือเก็บ chat log จากการทดสอบ
2. สร้าง batch review ด้วย `tools/create_human_review_batch.py`
3. เปิดไฟล์ JSONL แล้วให้คนกรอกคะแนน/notes
4. สรุปปัญหาเป็นกลุ่ม
5. แก้ data/rules/router/prompt ตามสาเหตุ
6. รัน Ground Truth ซ้ำ

จุดสำคัญคืออย่าแก้ทุกอย่างด้วย rulebase อย่างเดียว ถ้าปัญหาเกิดจาก data หรือคำถามกำกวม ควรแก้ที่ data/clarify route แทน
