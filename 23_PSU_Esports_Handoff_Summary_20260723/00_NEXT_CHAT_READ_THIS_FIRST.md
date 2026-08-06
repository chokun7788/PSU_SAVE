# PSU Esports Chatbot - Next Chat Read This First

## Latest Handoff Update - 06/08/2026

สถานะล่าสุดหลังจากพัฒนาต่อถึงวันที่ 06/08/2026 ให้เริ่มอ่านจาก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\10_CURRENT_PROJECT_ALL_IN_ONE_20260806.md
```

Prompt สำหรับ copy ไปเปิด session ใหม่อยู่ที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\11_COPY_PASTE_PROMPT_FOR_NEXT_SESSION_20260806.md
```

ลำดับงานที่ควรทำต่อและรูปแบบ Daily Log อยู่ที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\12_NEXT_WORK_AND_DAILY_LOG_GUIDE_20260806.md
```

ไฟล์ 00-09 ยังใช้ดูพื้นฐานและประวัติได้ แต่เมื่อข้อมูลขัดกันให้ยึดไฟล์ 10, daily logs ล่าสุด และ source code จริงเป็นหลัก

ไฟล์นี้คือ entrypoint สำหรับส่งต่อแชทใหม่ของโปรเจกต์ PSU Esports Chatbot หลังจากพัฒนา/แก้ระบบต่อเนื่องมาถึงวันที่ 2026-07-23

เป้าหมายคือให้แชทใหม่เข้าใจงานต่อจากแชทเดิมได้เร็ว ลด token และไม่ต้องไล่อ่านบทสนทนายาวทั้งหมด

## Prompt สำหรับเปิดแชทใหม่

ให้ copy ข้อความนี้ไปใส่แชทใหม่ก่อนเริ่มงาน:

```text
คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจากแชทเดิม

กรุณาตอบเป็นภาษาไทย และก่อนเริ่มทำงานให้อ่านไฟล์นี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\00_NEXT_CHAT_READ_THIS_FIRST.md

หลังอ่านไฟล์แรกแล้ว ให้ทำตามลำดับไฟล์ที่ระบุไว้ในไฟล์นั้นเอง

โฟลเดอร์ source หลัก:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

Daily logs:
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs

ข้อกำหนดสำคัญ:
- ตอนนี้ให้โฟกัส local chatbot เป็นหลัก ไม่ต้องยุ่ง git และไม่ต้องยุ่ง Vercel/deploy folder ถ้าผู้ใช้ไม่ได้สั่งใหม่
- ตอบผู้ใช้เป็นภาษาไทย
- รักษา answer-first style: ตอบคำตอบหลักก่อน แล้วค่อยรายละเอียด/แหล่งข้อมูล
- ถ้าไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา ให้ตอบ no-answer แบบสุภาพ
- ถ้าคำตอบมาจาก rulebase/fast path/structured/RAG ห้ามบอกว่าเป็น LLM
- ทุกงานที่มีสาระต้องเขียน daily log เป็น .md
- ไม่ต้องบอกผู้ใช้ทุกครั้งว่าเขียน daily log หรือรัน test อะไร ถ้าไม่ได้ถาม
- อย่าแก้ test/validator ให้ผ่านง่าย ต้องแก้ logic หรือ data ให้ถูกจริง
- อย่าใช้ git หรือ commit/push แทนผู้ใช้

ถ้าต้องการภาพรวมเร็ว ให้อ่าน:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\08_ALL_IN_ONE_HANDOFF.md
```

## อ่านไฟล์ไหนต่อ

ถ้าอ่านได้แค่ไฟล์เดียว:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\08_ALL_IN_ONE_HANDOFF.md
```

ถ้าจะทำงานต่อจริง ให้อ่านตามลำดับนี้:

1. `08_ALL_IN_ONE_HANDOFF.md`
   - สรุปทุกอย่างในไฟล์เดียว: project, requirements, current architecture, current state, tests, known issues

2. `01_PERSONAL_REQUIREMENTS_AND_WORK_STYLE.md`
   - requirement ประจำตัวของผู้ใช้และวิธีทำงานที่ต้องรักษาไว้ทุกครั้ง

3. `02_PROJECT_PATHS_AND_FILE_MAP.md`
   - path สำคัญของ repo, data, notebook, tools, reports และแต่ละส่วนทำหน้าที่อะไร

4. `03_CURRENT_SYSTEM_FLOW_LOCAL_FIRST.md`
   - flow ปัจจุบันของระบบ local-first ตั้งแต่ input ไป output รวม intent LLM, structured tools, RAG, fast path, session memory

5. `04_CURRENT_STATE_AND_RECENT_WORK.md`
   - สถานะล่าสุดและสิ่งที่ทำแล้วจนถึง 2026-07-23

6. `05_TEST_EVAL_AND_RUNBOOK.md`
   - command สำหรับทดลอง local chat, notebook, eval, smoke test และการ debug

7. `06_KNOWN_ISSUES_AND_NEXT_STEPS.md`
   - ปัญหาที่ยังต้องระวังและ roadmap ต่อไป

8. `09_DAILY_LOG_POLICY_AND_TEMPLATE.md`
   - วิธีเขียน daily log และ template ที่ควรใช้

9. `07_COPY_PASTE_PROMPT_FOR_NEW_CHAT.md`
   - prompt แบบ copy/paste แยกไฟล์ สำหรับเปิดแชทใหม่

## สิ่งสำคัญที่สุดที่ต้องจำ

- โปรเจกต์นี้คือ chatbot สำหรับ PSU Esports Studio - Phuket
- ตอนนี้ผู้ใช้ให้ตัดเรื่อง git/Vercel ออกไปก่อน และเน้น local LLM/local chatbot
- โฟลเดอร์ 18 คือ source หลักที่แก้และทดสอบจริง
- ระบบไม่ได้ใช้ LLM ตอบทุกอย่างโดยตรง แต่ใช้หลายชั้น:
  - normalization / alias / typo correction
  - heuristic router
  - adaptive Intent LLM สำหรับคำถามกว้างหรือกำกวม
  - structured tools สำหรับ facts ที่ชัด
  - fast/rule path สำหรับคำตอบ deterministic
  - RAG/vector retrieval สำหรับ curated data
  - general Local LLM fallback สำหรับคำถามนอกโดเมน
- ต้องมี session memory สำหรับ follow-up ใน local chat/notebook
- ต้องมี trace/mode/source_type เพื่อรู้ว่าคำตอบมาจากอะไร
- ถ้าแก้อะไรสำคัญ ให้เพิ่ม/รัน test เฉพาะจุด และเขียน daily log
