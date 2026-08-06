# Local-Only LLM Pipeline Plan - 2026-07-21

## เป้าหมายใหม่

ตัดแนวคิด deploy บน Vercel ออก และใช้ระบบแบบ local-first/local-only เป็นหลัก ดังนั้น pipeline สามารถใช้ Local LLM มากขึ้นได้ เพราะไม่ต้องติดข้อจำกัด serverless runtime และไม่ต้องกลัวว่า Vercel ไม่มีโมเดลบนเครื่อง

## LLM จะทำหน้าที่อะไร

LLM ไม่ควรเป็นตัวตอบทุกอย่างเอง แต่ควรเป็นผู้ช่วยในจุดที่ deterministic logic อ่อนกว่า:

1. Intent Helper  
   ใช้ช่วย classify คำถามเมื่อ heuristic ไม่มั่นใจ เช่น แยก booking/equipment/game/rule/general

2. Tool Router Helper  
   ใช้ช่วยเลือกเส้นทางว่าจะไป structured, fast path, rulebase, retrieval, vector, general LLM หรือ clarification

3. Facts-only Composer  
   ใช้เรียบเรียงคำตอบจาก structured facts ให้เป็นภาษาไทยที่อ่านง่ายขึ้น โดยห้ามเพิ่มข้อมูลนอก facts

4. General Fallback  
   ใช้ตอบคำถามนอกฐานข้อมูล PSU เช่น เมืองหลวง คำศัพท์ทั่วไป หรือคำถามทั่วไปที่ไม่ต้องใช้ข้อมูลล่าสุด

5. RAG Summarizer ในอนาคต  
   ใช้สรุปจาก retrieved facts/chunks เมื่อคำถามต้องรวมหลายแหล่ง แต่ต้องมี evidence validator กัน hallucination

## สิ่งที่ทำในรอบนี้

### 1. ทำ Validator ให้เป็น safety net กลาง

แก้ `app/pipeline/validator.py`

เพิ่ม hard-reject สำหรับเคสผิดชนิด:

•    คำถามจอง แต่ตอบเป็นอุปกรณ์หรือ catalog เกม  
•    คำถามเกมเฉพาะ เช่น `ROV คือเกมอะไร` แต่ตอบ catalog ทั้งหมด  
•    คำถามกติกา/รอบชิง แต่ตอบ catalog เกม  

หมายเหตุสำคัญ: ถ้า route label ผิดแต่เนื้อหาคำตอบถูก จะให้ warning ไม่ใช่ reject เช่น route ยังเป็น `equipment/count` แต่คำตอบเป็น booking selection ที่ถูกต้อง

### 2. ไม่ให้ structured confidence สูง override validation error

แก้ `app/pipeline/engine.py`

ก่อนหน้า structured tool confidence สูงสามารถตอบออกได้แม้ validation fail  
ตอนนี้ถ้า validator มี error จะ reject แล้ว fallback ไปขั้นถัดไป

### 3. เปิด LLM helper เป็น default สำหรับ local terminal chat

แก้:

•    `start_local_ai_chat.ps1`  
•    `tools/local_ai_chat.py`  
•    `docs/31_local_ai_terminal_chat.md`

เมื่อเปิด local chat แบบปกติ:

```powershell
.\start_local_ai_chat.ps1
```

จะเปิด:

•    `PSU_UNIVERSAL_INTENT_LLM=1`  
•    `PSU_LLM_TOOL_ROUTER=1`  
•    `PSU_FACTS_LLM_COMPOSER=1`  

ถ้าต้องการเทียบกับแบบ deterministic:

```powershell
.\start_local_ai_chat.ps1 -NoToolRouter -NoComposer
```

หรือปิด LLM ทั้งหมด:

```powershell
.\start_local_ai_chat.ps1 -NoLlm
```

### 4. เพิ่มคำสั่งใน terminal chat

เพิ่ม:

•    `/router on` / `/router off`  
•    `/composer on` / `/composer off`

## ผลทดสอบ

ผ่าน:

•    `python -m py_compile app\pipeline\validator.py app\pipeline\engine.py tools\local_ai_chat.py`  
•    `python tests\smoke_test_answer_validator.py`  
•    `python tests\smoke_test_audit_regressions.py`  
•    `python tests\smoke_test_structured_tools.py`  
•    `python tests\smoke_test_game_catalog.py`

ทดสอบ local CLI:

•    `จอง Nintendo Switch ต้องเลือกอะไรบ้าง` ตอบ booking selection ถูกต้องในประมาณ 0.56 วินาทีเมื่อปิด LLM  
•    `เมืองหลวงของประเทศไทยคืออะไร` ใช้ `general_llm_fallback` ตอบได้จริงด้วย `qwen2.5:3b` ประมาณ 10 วินาที  
•    `สมาชิก PSU Esport มีกี่หมวด` ใช้ structured facts พร้อม local helper ได้ประมาณ 4 วินาที

Ollama model ที่พบในเครื่อง:

•    `qwen2.5:3b`  
•    `qwen3:4b`

แนะนำใช้ `qwen2.5:3b` เป็น default เพราะ qwen3 เป็น thinking model และเคยเจอ response ว่างเมื่อ `num_predict` ไม่พอ

## Workflow ที่ควรเป็นต่อไป

```text
User Input
-> Session Context Resolver
-> Normalize / Alias
-> Heuristic Intent
-> Local LLM Intent Helper เฉพาะเมื่อไม่มั่นใจ
-> Candidate Generation
-> Tool Preconditions
-> LLM Tool Router เฉพาะเคสคลุมเครือ
-> Execute Tool
-> Answer Validator
-> ถ้า validator fail ให้ fallback candidate ถัดไป
-> Facts-only Composer หรือ General LLM
-> Final Answer + Decision Log
```

## ปัญหาที่ยังเหลือ

•    Candidate execution mismatch ยังมีอยู่ ต้องทำให้ Decision Artifact บันทึกตัวที่ execute จริงชัดขึ้น  
•    ข้อมูลกติกาแข่งบางเรื่องยังไม่ครบ เช่น ตัวสำรอง, no-show, voice chat, account policy  
•    ข้อมูลปุ่มบางเกมยังไม่มี เช่น Overcooked 2, Nintendo Switch Sports  
•    LLM helper อาจเพิ่ม latency เป็น 4-10 วินาทีต่อคำถาม แต่ถ้าใช้ local-only ถือว่ารับได้  
•    LLM ยังต้องถูกจำกัดให้ใช้ facts เป็นหลัก ไม่ควรให้ตอบ PSU-specific เองโดยไม่มี evidence

## สิ่งที่ควรทำถัดไป

1. ทำ Tool Preconditions เป็น module กลาง แทนการกระจาย guard ในหลายไฟล์
2. ปรับ Decision Artifact ให้เก็บ rejected-by-validator และ executed candidate จริง
3. เพิ่ม RAG answer validator สำหรับคำถามหลายแหล่ง
4. เติม fact card กติกา/ปุ่มที่ audit บอกว่ายังขาด
5. รัน eval 400 ข้อแบบ local LLM enabled เป็นรอบทดลองแยก แต่ควรคาดว่าจะใช้เวลานานขึ้นมาก
