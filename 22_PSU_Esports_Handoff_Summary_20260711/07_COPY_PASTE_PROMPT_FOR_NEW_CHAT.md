# Copy Paste Prompt For New Chat

ใช้ prompt นี้เปิดแชทใหม่:

```text
คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจากแชทเดิม

ก่อนตอบหรือเริ่มทำงาน กรุณาอ่านไฟล์นี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711\00_NEXT_CHAT_READ_THIS_FIRST.md

ไฟล์นี้จะบอกว่าต้องอ่านไฟล์ไหนต่อ, path โปรเจกต์อยู่ที่ไหน, ระบบตอนนี้ทำงานยังไง, ต้อง test/deploy ยังไง, และข้อห้ามสำคัญมีอะไรบ้าง

โฟลเดอร์หลักของโปรเจกต์:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

โฟลเดอร์ Deploy:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Production URL:
https://psu-esports-chatbot.vercel.app

สิ่งที่ต้องยึดไว้:
- ตอบเป็นภาษาไทย
- อ่าน handoff ก่อนเริ่มทำงาน
- ถ้าจะแก้โค้ด ให้แก้จากไฟล์จริงในโฟลเดอร์ 18
- ถ้าแก้คำตอบผิด ให้ดู route/mode/source ก่อน
- ถ้าไม่มีข้อมูลจริง ห้ามเดา ให้ตอบ no-answer แบบสุภาพ
- ทุกครั้งที่แก้ logic สำคัญ ให้ run compile/validate/smoke test ตามความเหมาะสม
- ไม่ต้อง run Ground Truth ชุดใหญ่ทุกครั้ง ยกเว้นผมบอก
- ถ้า deploy ต้อง sync จากโฟลเดอร์ 18 ไป 20 แล้ว test production API
- รักษา answer-first style
- อย่าแก้ตัวตรวจให้ผ่อนลงเพื่อให้ PASS ง่าย
- อย่าบอกว่าใช้ LLM ถ้าคำตอบจริงมาจาก rulebase/fast path
- ต้องเขียน daily log ใน C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs เมื่อทำงานที่มีสาระ

หลังอ่านไฟล์แรกแล้ว ให้ทำตามลำดับไฟล์ที่ระบุในนั้นเอง และเริ่มช่วยทำงานต่อจากสถานะล่าสุด
```

