# Structured Tool Regression Fix - 2026-07-21

## ปัญหาที่เจอ

หลังเพิ่ม Decision Artifact / Structured Tool Routing มีบางคำถามที่เคยแก้แล้วกลับมาตอบผิดอีก เช่น:

•    `ROV คือเกมอะไร` ถูกตอบเป็นรายชื่อเกมทั้งหมด 44 เกม  
•    `ROV รอบชิงเล่นกี่เกม` ถูก structured games ดึงไปตอบ catalog แทนกติกาการแข่งขัน  
•    `จอง Nintendo Switch ต้องเลือกอะไรบ้าง` ถูกตอบเป็นรายละเอียดอุปกรณ์ Nintendo Switch OLED  
•    `จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม` ถูกตอบเป็นรายชื่อเกม Nintendo Switch  
•    `อยากเล่นพวงมาลัยต้องจองโซนอะไร` เสี่ยงถูกตอบเป็นรายการอุปกรณ์แทนคำตอบตรงว่า Cockpit Zone

## สาเหตุหลัก

ปัญหาไม่ได้เกิดจาก rule/fast answer เดิมหาย แต่เกิดจากลำดับ pipeline ใหม่:

1. `answer_with_structured_tool()` ถูกเรียกก่อน fast/rule บางชุด
2. `structured_tools._game_answer()` เห็นคำว่า `เกมอะไร` แล้วตีเป็นคำถาม catalog แม้ผู้ใช้ถามรายละเอียดเกมเฉพาะ
3. `structured_tools._equipment_answer()` เห็นคำว่า `Nintendo Switch`, `PS5`, `พวงมาลัย` แล้วตอบข้อมูลอุปกรณ์ทันที แม้ route จริงควรเป็นการจอง
4. route/intent บางครั้งขัดกัน เช่น route เป็น `reservation/booking_policy` แต่ universal intent เป็น `equipment/count` ทำให้ tool ที่ชนะไม่ตรงกับคำถามจริง

สรุปคือ fix เก่าใน fast/rule ยังอยู่ แต่ถูก structured tool ที่เพิ่มใหม่ “แย่งตอบก่อน”

## สิ่งที่แก้

แก้ไฟล์ `app/pipeline/structured_tools.py`

•    เพิ่ม guard `_looks_like_specific_game_detail_query()` เพื่อแยก `ROV คือเกมอะไร` ออกจาก `PS5 มีเกมอะไรบ้าง`  
•    เพิ่ม guard `_looks_like_competition_rule_query()` เพื่อไม่ให้คำถามกติกา/รอบชิง/BO3 ถูกตอบเป็น catalog เกม  
•    เพิ่ม guard `_looks_like_booking_selection_query()` เพื่อกันคำถามจอง/เลือกบริการ/จำนวนผู้เล่น ไม่ให้อุปกรณ์แย่งตอบ  
•    เพิ่ม `_booking_selection_answer()` สำหรับคำถามจองที่ควรตอบตรง เช่น Nintendo Switch 1-2 Persons / 3-4 Persons และ Cockpit Zone สำหรับพวงมาลัย  
•    กันคำถามราคา เช่น `จอง PS5 9โมงถึง11โมงเสียกี่บาท` ไม่ให้ booking selection แย่งจาก calculator  

เพิ่ม test:

•    `tests/smoke_test_audit_regressions.py`

ปรับ test เก่า:

•    `tests/smoke_test_game_catalog.py` ให้ตรงกับฐานข้อมูลปัจจุบันที่มี 44 เกม และ bullet format ปัจจุบัน

## ผลหลังแก้

รัน smoke test ผ่าน:

•    `tests/smoke_test_audit_regressions.py`  
•    `tests/smoke_test_structured_tools.py`  
•    `tests/smoke_test_game_catalog.py`

รัน 400 ข้อใหม่:

•    Eval output: `data/eval/question_bank_runs/20260721_003429_20260721_structured_guard_fix_400`  
•    Audit output: `data/eval/audits/20260721_structured_guard_fix_400_audit`

เทียบ baseline ก่อนแก้:

•    Average score: 8.577 → 8.716  
•    Bad cases: 14 → 3  
•    `game_rules`: 8.527 → 8.848  
•    `play_booking_controls`: 9.266 → 9.502  
•    `specific_question_answered_with_full_catalog`: 10 → 2  

## สิ่งที่ยังเหลือ

•    Out-of-scope ยังตอบแบบ `general_llm_disabled` เพราะรอบนี้ปิด Local LLM ไว้  
•    คำถามกติกาบางข้อยังตอบว่า “ยังไม่พบข้อมูล” เพราะข้อมูลต้นทางยังไม่ครบ เช่น ตัวสำรอง, บัญชีที่ใช้แข่ง, voice chat, no-show  
•    เกมบางเกมยังไม่มีข้อมูลปุ่ม เช่น Overcooked 2, Nintendo Switch Sports  
•    Decision Artifact ยังมี `candidate_execution_mismatch` บางส่วน ควรปรับ registry/ranking ให้สะท้อน execution จริงมากขึ้น  

## แนวทางถัดไป

1. เติม/แยก fact card กติกาแข่งให้ละเอียดขึ้นตามหัวข้อที่ผู้ใช้ถามจริง
2. เพิ่มข้อมูล controls ของเกมที่ยังตอบว่าไม่มีข้อมูล
3. เปิด Local LLM เฉพาะ out-of-scope หรือใช้เป็น answer composer หลัง retrieval เพื่อให้ตอบยืดหยุ่นขึ้น
4. ปรับ Decision Artifact ให้บันทึก candidate ที่ถูก execute จริง ไม่ใช่แค่ตัวที่ rank ชนะในแผน
