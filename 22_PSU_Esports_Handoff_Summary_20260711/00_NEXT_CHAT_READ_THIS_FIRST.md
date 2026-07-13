# PSU Esports Chatbot - Next Chat Read This First

ไฟล์นี้คือ entrypoint สำหรับส่งต่อแชทใหม่ หลังจากแชทเดิมพัฒนา PSU Esports Chatbot มาหลายรอบแล้ว จุดประสงค์คือให้แชทใหม่รับช่วงต่อได้เร็ว ลดการใช้ token และไม่ต้องอ่านทั้งโปรเจกต์ตั้งแต่ต้น

## Prompt สำหรับแชทใหม่

ให้ copy ข้อความนี้ไปใส่ในแชทใหม่ก่อนเริ่มงาน:

```text
คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจากแชทเดิม

กรุณาตอบเป็นภาษาไทย และก่อนเริ่มทำงานให้อ่านไฟล์นี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711\00_NEXT_CHAT_READ_THIS_FIRST.md

หลังจากอ่านไฟล์แรกแล้ว ให้ทำตามลำดับไฟล์ที่ระบุในนั้นเอง

โฟลเดอร์ source หลัก:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

โฟลเดอร์ deploy:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Production URL:
https://psu-esports-chatbot.vercel.app

ข้อกำหนดสำคัญ:
- ตอบเป็นภาษาไทย
- ถ้าจะแก้โค้ด ให้แก้จากไฟล์จริงในโฟลเดอร์ 18 แล้ว sync ไป 20 เมื่อพร้อม deploy
- ถ้าแก้ logic สำคัญ ให้ run compile/validate/smoke test ตามความเหมาะสม
- ไม่ต้อง run Ground Truth ชุดใหญ่ทุกครั้ง ยกเว้นผู้ใช้ขอ
- ถ้า deploy ต้อง sync 18 ไป 20 แล้ว test production API
- ต้องเขียน daily log ใน C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
- ถ้าไม่มีข้อมูลจริง ห้ามเดา ให้ตอบ no-answer แบบสุภาพ
- รักษา answer-first style
- อย่าบอกว่าใช้ LLM ถ้าคำตอบจริงมาจาก rulebase/fast path
- อย่าแก้ตัวตรวจให้ผ่อนลงเพื่อให้ PASS ง่าย

เริ่มจากอ่านไฟล์ 06_ALL_IN_ONE_HANDOFF.md ในโฟลเดอร์ 22 ถ้าต้องการภาพรวมเร็ว แล้วค่อยอ่านไฟล์ย่อยตามงานที่จะทำ
```

## อ่านไฟล์ไหนต่อ

ถ้าอ่านได้แค่ไฟล์เดียว:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711\06_ALL_IN_ONE_HANDOFF.md
```

ถ้าจะทำงานต่อจริง ให้อ่านตามลำดับนี้:

1. `06_ALL_IN_ONE_HANDOFF.md`
   - สรุปทั้งหมดแบบไฟล์เดียว
   - มี project overview, requirements, current state, recent changes, paths, workflow, testing, deploy, known risks

2. `01_PERSONAL_REQUIREMENTS_AND_WORK_STYLE.md`
   - requirement ประจำตัวของผู้ใช้
   - สิ่งที่ต้องทำทุกครั้ง เช่น daily log, answer-first, ห้ามเดา, ห้าม deploy เองถ้าไม่ได้สั่ง

3. `02_PROJECT_PATHS_AND_FILE_MAP.md`
   - path ทั้งหมดและแต่ละ folder ทำหน้าที่อะไร
   - ไฟล์โค้ดและ data ที่ต้องดูเวลาจะแก้ปัญหา

4. `03_CURRENT_SYSTEM_FLOW.md`
   - flow ของระบบตั้งแต่ user ถามจนตอบ
   - rulebase, fast path, RAG-lite, vector retrieval, guard/no-answer

5. `04_RECENT_WORK_AND_CURRENT_STATE.md`
   - งานล่าสุดที่เพิ่งทำ
   - game control split PS5/Nintendo, JSONL, vector index, booking fix, game catalog count

6. `05_TEST_DEPLOY_RUNBOOK.md`
   - command compile/test/smoke/deploy
   - วิธี sync 18 ไป 20
   - วิธี deploy Vercel ที่ผู้ใช้กดเอง

7. `07_COPY_PASTE_PROMPT_FOR_NEW_CHAT.md`
   - prompt แบบ copy/paste สำหรับเปิดแชทใหม่

## Path สำคัญ

Root รวม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

Source หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

Deploy folder:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

Daily logs:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

Handoff เดิม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

Handoff ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711
```

## สิ่งสำคัญที่สุดที่ต้องจำ

- โปรเจกต์นี้เป็น chatbot สำหรับ PSU Esports Studio - Phuket
- ระบบ production เน้น rulebase/fast path/RAG-lite ที่ควบคุม hallucination มากกว่า LLM อิสระ
- โฟลเดอร์ 18 คือที่พัฒนาและทดสอบหลัก
- โฟลเดอร์ 20 คือที่ใช้ deploy Vercel
- ผู้ใช้มัก deploy เองเพื่อประหยัด token
- ถ้าแก้ logic สำคัญ ให้ compile และ smoke test เท่าที่จำเป็น
- ไม่ต้อง run Ground Truth ชุดใหญ่ทุกครั้ง ยกเว้นผู้ใช้ขอ
- ทุกงานที่มีสาระควรลง daily log

