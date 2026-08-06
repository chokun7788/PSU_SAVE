# Copy Paste Prompt For New Chat

ใช้ข้อความนี้เปิดแชทใหม่:

```text
คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจากแชทเดิม

โปรดอ่านไฟล์แรกนี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\00_NEXT_CHAT_READ_THIS_FIRST.md

จากนั้นอ่านไฟล์ที่ไฟล์แรกแนะนำ โดยถ้ามีเวลาน้อยให้อ่าน:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\08_ALL_IN_ONE_HANDOFF.md

บริบทสำคัญ:
- ตอนนี้โฟกัส local chatbot/local LLM เป็นหลัก
- ไม่ต้องยุ่ง git
- ไม่ต้องยุ่ง Vercel/deploy folder ถ้าฉันไม่ได้สั่งใหม่
- source หลักอยู่ที่:
  C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
- daily log อยู่ที่:
  C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs

Requirement สำคัญ:
- ตอบภาษาไทย
- answer-first
- ไม่เวิ่นเว้อ
- ถ้าไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา
- ถ้าคำตอบมาจาก rule/fast/structured/RAG ห้ามบอกว่าเป็น LLM
- ต้องเขียน daily log เมื่อทำงานที่มีสาระ
- ไม่ต้องบอกทุกครั้งว่าเขียน daily log หรือรัน test อะไร ถ้าฉันไม่ได้ถาม
- แก้ logic ให้ถูกจริง อย่าแก้ test ให้ผ่านง่าย

งานนี้คือ chatbot สำหรับ PSU Esports Studio - Phuket ที่ใช้ pipeline หลายชั้น:
normalization/alias/typo correction -> heuristic router -> adaptive Intent LLM -> structured tools -> fast/rule -> RAG/vector -> optional facts composer -> general Local LLM fallback -> validate/format/log

ช่วยรับช่วงต่อเหมือนเป็นแชทเดิม และถ้าจะทำอะไรให้ดูไฟล์ handoff ก่อนเสมอ
```

