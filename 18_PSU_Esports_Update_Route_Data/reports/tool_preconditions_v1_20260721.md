# Tool Preconditions v1 - 2026-07-21

## ทำไปเพื่อแก้อะไร

ก่อนหน้านี้ระบบยังแก้แบบ patch/case-based เยอะเกินไป เช่นเจอคำถามจองแล้ว equipment แย่งตอบ ก็เพิ่ม guard เฉพาะจุดหนึ่ง พอเจอคำถามใหม่ก็ต้องเพิ่ม guard อีก

รอบนี้จึงเริ่มทำ precondition layer กลาง เพื่อให้ทุก tool มีเงื่อนไขชัดเจนว่า:

•    ใช้ได้เมื่อไหร่  
•    ห้ามใช้เมื่อไหร่  
•    ถ้าถูก reject ต้องบันทึกเหตุผลไว้ใน trace/artifact  

## ไฟล์ที่เพิ่ม/แก้

เพิ่ม:

•    `app/pipeline/tool_preconditions.py`  
•    `tests/smoke_test_tool_preconditions.py`

แก้:

•    `app/pipeline/capability_registry.py`  
•    `app/pipeline/engine.py`  
•    `app/pipeline/decision_artifact.py`  
•    `tests/smoke_test_decision_artifact.py`  
•    `tests/smoke_test_structured_tools.py`

## กติกา precondition ที่เพิ่ม

### Structured Games

•    ห้ามตอบคำถามจอง  
•    ห้ามตอบคำถามราคา  
•    ห้ามตอบคำถามกติกา/รอบชิงด้วย catalog  
•    อนุญาตเมื่อเป็น game detail หรือ game catalog จริง

### Structured Equipment

•    ห้ามตอบคำถามจอง  
•    ห้ามตอบคำถามราคา  
•    ห้ามตอบคำถามกติกา  
•    อนุญาตเมื่อเป็นอุปกรณ์/จำนวน/รุ่น/โซนจริง

### Structured Reservation

•    อนุญาตคำถามจอง/เลือกบริการ/จำนวนผู้เล่น  
•    ห้ามตอบคำถามราคา เพราะต้องให้ calculator หรือ service fee จัดการ

### Price Calculator

•    อนุญาตเมื่อมีคำถามราคา/กี่บาท/คำนวณ  
•    ทำให้คำถาม `9โมงถึง11โมงเสียกี่บาท` เข้า calculator ก่อน structured service fee

### Competition

•    คำถามกติกา/รอบชิง/BO3 ใช้ fast domain handler หรือ competition retrieval  
•    ห้าม schedule หรือ game catalog แย่งจากคำว่า `รอบ`

## Decision Artifact v2 ที่เพิ่ม

เพิ่มใน artifact:

•    `tool_preconditions`  
•    `final.executed_capability`  
•    `final.selected_matches_execution`  
•    `candidate_execution` สำหรับกรณี structured ผ่าน precondition แต่ไม่มีคำตอบ หรือถูก validator reject

สิ่งนี้ช่วยแยกได้ว่า:

•    candidate ถูก reject ตั้งแต่ precondition  
•    candidate ถูก execute แล้วไม่เจอคำตอบ  
•    candidate ถูก validator reject  
•    final answer มาจาก capability ไหนจริง

## ผลทดสอบ

ผ่าน:

•    `python -m py_compile app\pipeline\tool_preconditions.py app\pipeline\capability_registry.py app\pipeline\decision_artifact.py app\pipeline\engine.py`  
•    `python tests\smoke_test_tool_preconditions.py`  
•    `python tests\smoke_test_decision_artifact.py`  
•    `python tests\smoke_test_audit_regressions.py`  
•    `python tests\smoke_test_structured_tools.py`  
•    `python tests\smoke_test_game_catalog.py`  
•    `python tests\smoke_test_answer_validator.py`

รัน 400 ข้อ:

•    Eval: `data/eval/question_bank_runs/20260721_012559_20260721_tool_preconditions_v1_400`  
•    Audit: `data/eval/audits/20260721_tool_preconditions_v1_400_audit`

ผลรวมยังเท่ารอบก่อน:

•    Average score: 8.716 / 10  
•    Bad cases: 3  
•    game_rules: 8.848  
•    play_booking_controls: 9.502  
•    equipment_game_inside: 9.626  
•    out_of_scope: 6.889

เหตุผลที่คะแนนยังไม่เพิ่มคือรอบนี้แก้ architecture/trace/precondition เป็นหลัก ไม่ได้เติมข้อมูลใหม่ที่ขาด

## สิ่งที่ดีขึ้นจริง

•    คำถามจอง Nintendo ถูก map ไป structured reservation แม้ intent เดิมจะหลงเป็น equipment  
•    คำถามราคา PS5 9-11 เข้า fast price calculator และ selected/executed capability ตรงกัน  
•    คำถาม ROV รอบชิงไม่ให้ schedule/game catalog แย่งจากคำว่า `รอบ`  
•    Artifact อธิบายได้มากขึ้นว่าทำไม tool ถูกปฏิเสธหรือ fallback  

## สิ่งที่ยังไม่ดี

•    selected/executed ยังไม่ตรงทุกข้อ เพราะบาง candidate ที่ rank ชนะผ่าน precondition แต่ execute แล้วไม่มีคำตอบจริง จึง fallback ไป tool ถัดไป  
•    audit ยังนับ `candidate_execution_mismatch` แบบเดิมอยู่ เพราะ audit script ยังไม่ได้อ่าน artifact v2 ละเอียดพอ  
•    คะแนนไม่เพิ่มจนกว่าจะเติมข้อมูลที่ขาด เช่น กติกาแข่งบางหัวข้อและปุ่มบางเกม  
•    precondition ยังเป็น heuristic-based ไม่ใช่ semantic classifier เต็มตัว  

## งานถัดไปที่ควรทำ

1. ปรับ audit script ให้อ่าน artifact v2 และแยก mismatch จริงออกจาก fallback ปกติ
2. เพิ่ม execution planner ให้เลือก candidate ตาม precondition/ranking จริง แทนลำดับ hard-coded ใน engine
3. เติม fact card กติกาแข่งที่ยังขาด
4. เติมข้อมูลปุ่มเกมที่ยังไม่มี
5. รัน eval แบบเปิด Local LLM helper เฉพาะ 50-100 ข้อ เพื่อดู latency/คุณภาพก่อนรัน 400 เต็ม
