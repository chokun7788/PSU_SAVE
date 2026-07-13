# Personal Requirements And Work Style

ไฟล์นี้สรุป requirement ประจำตัวของผู้ใช้และวิธีทำงานที่ต้องรักษาไว้ทุกครั้งเมื่อรับช่วงโปรเจกต์นี้

## ภาษาและสไตล์คำตอบ

- ตอบผู้ใช้เป็นภาษาไทย
- ใช้ answer-first style: ตอบประเด็นก่อน แล้วค่อยให้รายละเอียดหรือแหล่งข้อมูล
- คำตอบ chatbot ที่ออกสู่ user ควรสุภาพ กระชับ ตรงประเด็น
- ถ้ามีแหล่งข้อมูล ให้ใส่แหล่งข้อมูลท้ายคำตอบ
- ถ้าคำตอบมาจาก rulebase/fast path/curated data ห้ามบอกว่าใช้ LLM
- ถ้าไม่มีข้อมูลจริงในฐานข้อมูล ห้ามเดา ให้ตอบ no-answer แบบสุภาพ
- ระวังภาษาไทย เช่น การเว้นวรรคคำซ้ำด้วย `ๆ` ควรเป็น `หลาย ๆ อย่าง` ไม่ใช่ `หลายๆอย่าง`

## การทำงานกับโค้ด

- ถ้าจะแก้โค้ด ให้แก้ไฟล์จริงใน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

- เมื่อพร้อม deploy หรือผู้ใช้ขอให้ทำฝั่ง deploy ให้ sync ไป:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

- ถ้าแก้คำตอบผิด ให้ตรวจ route/mode/source ก่อนแก้
- อย่าแก้ด้วยการเพิ่มข้อความมั่ว ๆ ถ้ายังไม่รู้ว่าคำตอบมาจาก handler ไหน
- อย่าแก้ตัวตรวจหรือ test ให้ผ่อนลงเพื่อให้ PASS ง่ายขึ้น
- อย่า revert งานเก่าของผู้ใช้หรือไฟล์ที่ไม่เกี่ยวข้อง

## Testing Policy

- ทุกครั้งที่แก้ logic สำคัญ ให้ run อย่างน้อย:
  - `python -m py_compile ...`
  - smoke test เฉพาะเคสที่เกี่ยวข้อง
- ไม่ต้อง run Ground Truth ชุดใหญ่ทุกครั้ง เพราะผู้ใช้ต้องการประหยัด token
- ถ้าผู้ใช้สั่งให้ run Ground Truth ค่อย run ตามไฟล์/command ที่มีอยู่
- ถ้า deploy ต้อง test production API หลัง deploy

## Daily Log

ต้องเขียน daily log เมื่อทำงานที่มีสาระ เช่น แก้ logic, เพิ่ม data, เปลี่ยน retrieval, sync deploy, เพิ่ม handoff

Daily log อยู่ที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ชื่อไฟล์ใช้วันที่ เช่น:

```text
2026-07-11.md
```

สิ่งที่ควรลง daily log:

- เป้าหมายของงาน
- ปัญหาที่พบ
- ไฟล์ที่แก้
- logic/data ที่เพิ่ม
- test ที่ run
- ผลลัพธ์
- ยังไม่ได้ทำอะไร เช่น ยังไม่ได้ deploy หรือยังไม่ได้ run Ground Truth

## Deploy Policy

- ผู้ใช้มักบอกว่าไม่ต้อง deploy ให้ เพราะจะกดเอง
- ถ้าผู้ใช้ไม่ได้สั่ง deploy ห้าม deploy production เอง
- ถ้าต้อง deploy:
  1. sync จาก 18 ไป 20
  2. compile/test ใน 20
  3. ผู้ใช้หรือ agent ค่อย run `vercel --prod`
  4. test production API หลัง deploy

## Token Budget Preference

ผู้ใช้ต้องการประหยัด token:

- อย่าอ่านไฟล์ใหญ่โดยไม่จำเป็น
- อย่า run test ใหญ่ทุกครั้ง
- ถ้าจะทดสอบ ให้ทำ smoke test แบบพอดี
- ถ้ามีไฟล์ summary/handoff ให้ใช้ก่อนอ่านโค้ดจำนวนมาก

## สิ่งที่ผู้ใช้ให้ความสำคัญ

- คำตอบต้องถูกต้องมากกว่าตอบเร็ว
- ยอมให้ตอบช้าประมาณ 5 ถึง 7 วินาทีได้ถ้าคำตอบดีขึ้น
- ต้องรองรับคำพิมพ์ผิด สะกดเพี้ยน ภาษาไทยทับศัพท์ ชื่อย่อ และคำถามหลากหลาย
- ต้องลด hallucination
- ข้อมูลที่เพิ่มใหม่ควรนำไปใช้ได้จริง ไม่ใช่เพิ่มแล้วระบบยังไม่ route ไปหา

