# Copy Paste Prompt สำหรับเปิดแชทใหม่

ให้ copy ข้อความด้านล่างไปใส่แชทใหม่ได้เลย

```text
ผมกำลังทำโปรเจกต์ PSU Esports Chatbot อยู่ในเครื่อง Windows

โปรเจกต์อยู่ที่:
C:\Users\Chokhun\Downloads\Learn-LLM

ขอให้คุณอ่าน handoff summary ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705

ไฟล์ที่ควรอ่านก่อน:
1. 00_README_START_HERE.md
2. 01_HANDOFF_CONTEXT_FOR_NEXT_CHAT.md
3. 03_FILE_AND_FOLDER_MAP.md
4. 05_PIPELINE_RULE_RAG_LLM_DESIGN.md
5. 08_KNOWN_ISSUES_NEXT_STEPS.md
6. 11_AGENT_STATE_TRANSFER_FULL.md
7. 17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md

โฟลเดอร์หลักของระบบล่าสุด:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

โฟลเดอร์ deploy Vercel:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Production URL:
https://psu-esports-chatbot.vercel.app

เป้าหมายโปรเจกต์:
ทำ Chatbot สำหรับ PSU Esports Studio - Phuket เพื่อตอบ FAQ/กฎ/ราคา/เวลา/การจอง/เกม/อุปกรณ์/กติกาแข่งขัน โดยเน้นฟรี local เป็นหลัก และ deploy demo ได้

สถานะล่าสุด:
- ระบบ production ไม่ได้ใช้ LLM เป็นหลัก แต่ใช้ rulebase, deterministic calculator, competition fact cards, curated RAG-lite
- GT360 ผ่าน 360/360
- Competition challenger v2 ผ่าน 369/369
- Production Vercel deploy แล้ว
- local web/API ใช้ http://127.0.0.1:8018/
- notebook test หลักคือ:
  C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb

ปัญหาล่าสุดที่แก้แล้ว:
คำถามแนว “อุปกรณ์เล่นเกมอะไรได้บ้าง / Cockpit มีเกมอะไรบ้าง / VR มีเกมอะไรบ้าง” เคยตอบผิดเป็น “ยังไม่พบ เกมนี้...” ตอนนี้เพิ่ม route equipment_game_catalog แล้ว และ production API ตอบถูกแล้ว

สิ่งที่อยากให้ช่วยต่อ:
ให้ดูจาก handoff summary แล้วช่วยทำงานต่อโดยรักษาแนวทางเดิม:
- ตอบเป็นภาษาไทย
- แก้จากโค้ดจริงในโฟลเดอร์
- ทุกครั้งที่แก้ให้รันทดสอบและบันทึก report/log
- อย่าให้ AI เดาข้อมูลที่ไม่มี
- ถ้าแก้ deploy ต้อง sync จากโฟลเดอร์ 18 ไป 20 แล้ว deploy Vercel
- ถ้าเพิ่มข้อมูลใหม่ควรเพิ่ม Ground Truth หรือ ad-hoc test ด้วย
- รักษา answer-first style: ตอบประเด็นก่อน แล้วค่อยรายละเอียด/แหล่งข้อมูล
- ถ้าคำตอบผิด ให้ดู route/mode/source ก่อน แล้วค่อยแก้เฉพาะจุด
- อย่าแก้ตัวตรวจให้ผ่อนลงเพื่อให้ PASS ง่าย ๆ
```

## Prompt แบบสั้นมาก

```text
อ่านโฟลเดอร์นี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705

แล้วช่วยทำโปรเจกต์ PSU Esports Chatbot ต่อจากสถานะล่าสุด โดยโฟลเดอร์หลักคือ:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

deploy folder:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Production:
https://psu-esports-chatbot.vercel.app

ให้อ่าน 00_README_START_HERE.md และ 01_HANDOFF_CONTEXT_FOR_NEXT_CHAT.md ก่อนตอบ
ถ้ามีเวลาอ่านน้อย ให้เปิด 17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md ก่อน
```

## Prompt สำหรับให้ AI ตรวจปัญหาคำตอบ

```text
ผมมี Chatbot PSU Esports ที่ตอบผ่าน pipeline rulebase/RAG-lite ไม่ใช่ LLM เป็นหลัก
ช่วยตรวจปัญหาคำตอบจากคำถามนี้ให้หน่อย:

คำถาม:
<ใส่คำถาม>

คำตอบที่ได้:
<ใส่คำตอบ>

สิ่งที่อยากได้:
- วิเคราะห์ว่า route น่าจะผิดไหม
- ควรเข้า category ไหน
- data มีหรือไม่มี
- ถ้าต้องแก้ ควรแก้ไฟล์ไหน
- ควรเพิ่ม ground truth/ad-hoc test อะไร

บริบทโปรเจกต์อยู่ที่:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

## Prompt สำหรับให้ AI เพิ่มข้อมูลใหม่

```text
ช่วยเพิ่มข้อมูลใหม่เข้า PSU Esports Chatbot โดยอ่าน handoff ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705

ข้อมูลใหม่คือ:
<แปะข้อมูล>

ต้องการให้:
- จัดเข้าหมวด data/rules/curated ตามเหมาะสม
- ปรับ route/fast path ถ้าจำเป็น
- เพิ่ม ad-hoc test หรือ ground truth
- รันทดสอบ
- สรุปไฟล์ที่แก้และผล test
```
