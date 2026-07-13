# Known Issues และ Next Steps

ไฟล์นี้สรุปปัญหาที่ยังเหลือและแผนต่อจากสถานะล่าสุด

## สถานะโดยรวม

ตอนนี้ระบบเป็น MVP ที่ใช้งาน demo ได้แล้ว:

- มีเว็บ local
- มีเว็บ production บน Vercel
- มี API `/api/chat`
- ตอบ FAQ หลักได้เร็ว
- Ground Truth หลักผ่าน
- Competition challenger ผ่าน
- มี daily log และ report

แต่ยังไม่ใช่ระบบ production สมบูรณ์สำหรับศูนย์จริง เพราะยังมีส่วนที่ต้องเติม data และ integration

## Issue 1: หลายคำถามในข้อความเดียว

ตอนนี้ระบบยังเน้นตอบหนึ่งคำถามต่อหนึ่ง input

ตัวอย่างที่ยังอาจไม่ดี:

```text
วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่ แล้ว Cockpit เล่นเกมอะไร
```

ระบบอาจตอบแค่ intent แรกหรือ intent ที่ router เลือก

แนวทางแก้:

1. เพิ่ม question splitter
2. แยกคำถามด้วยคำเชื่อม เช่น แล้ว, และ, อีกอย่าง, รวมถึง, ?
3. route ทีละ sub-question
4. รวมคำตอบเป็นหลายหัวข้อ

ตัวอย่าง output:

```text
1. วันนี้เปิดไหม
...

2. VR ราคาเท่าไหร่
...

3. Cockpit เล่นเกมอะไร
...
```

## Issue 2: Conversation Memory

หน้าเว็บตอนนี้เก็บประวัติบน frontend memory

ผล:

- ถ้าถามต่อในหน้าเดียว ยังมี history ที่ frontend ส่งได้บางส่วน
- ถ้า refresh/ปิดหน้าเว็บ ประวัติหาย
- backend log มีแต่ไม่ได้ใช้เป็น memory เพื่อเข้าใจ context ถัดไป

ตัวอย่างที่ยังควรพัฒนา:

```text
User: วันนี้เปิดไหม
Bot: วันนี้...
User: แล้วราคา VR ล่ะ
```

คำว่า `แล้ว` อาจต้องใช้ context เดิม

แนวทางแก้:

1. สร้าง session_id
2. เก็บ conversation history ใน localStorage หรือ backend DB
3. ทำ context summarizer แบบสั้น
4. ให้ router ใช้ last intent/entity เมื่อคำถามขาดบริบท

สำหรับ production จริง:

- ถ้าไม่อยากเก็บถาวร ให้เก็บใน browser session/localStorage
- ถ้าต้องการ log analytics ให้เก็บใน DB
- ต้องแจ้ง privacy/log policy

## Issue 3: Facebook Messenger Integration

เป้าหมายผู้ใช้คือเน้น ChatBot ทาง Facebook

ยังไม่ได้ทำจริง

ต้องทำ:

1. สร้าง Facebook App
2. ทำ Page Access Token
3. ทำ webhook endpoint
4. verify webhook
5. รับ message event
6. ส่งคำถามเข้า `answer_question_pipeline_debug`
7. ส่งคำตอบกลับ Messenger
8. เก็บ log

ข้อควรระวัง:

- Vercel ทำ webhook ได้ แต่ต้องดู timeout และ cold start
- ถ้าใช้ LLM local ต้องแยก backend ไม่ใช่ Vercel
- Messenger มีข้อจำกัด message format และ policy

## Issue 4: Booking Action ยังไม่มี

ตอนนี้ระบบตอบ FAQ เท่านั้น

ยังไม่ทำ:

- จองจริง
- ยกเลิกจอง
- เช็คสถานะ booking
- login
- payment
- ดึง slot ว่างจริง

เพราะยังไม่มี API booking ที่ยืนยันจากศูนย์

แนวทาง phase 2:

1. ขอ API spec จากศูนย์
2. ทำ auth/login flow
3. ทำ tool/action layer แยกจาก Q&A
4. ให้ AI แนะนำขั้นตอน แต่ action จริงต้อง confirm ก่อน
5. ทำ audit log

## Issue 5: ข้อมูลจริงจากเจ้าหน้าที่ยังไม่ครบ

ข้อมูลที่ยังต้องขอ:

- กฎค่าปรับอุปกรณ์เสียหาย เช่น เมาส์พัง คิดยังไง
- รายละเอียด booking policy ล่าสุด
- รายการเกมล่าสุดที่มีจริง
- รายการอุปกรณ์ล่าสุดและจำนวนจริง
- วันหยุด/วันปิดพิเศษจริงทั้งปี
- เงื่อนไขสมาชิก/บุคคลภายนอก
- ข้อมูลการแข่งขันที่กำลังเปิดรับสมัครจริง
- policy การใช้ภาพ/เสียง/ข้อมูลส่วนตัว

ถ้าไม่มีข้อมูล:

```text
ต้องให้บอทตอบว่าไม่พบข้อมูลที่ยืนยันได้
```

ไม่ควรให้ LLM เดา

## Issue 6: RAG/LLM ยังไม่ใช่ production หลัก

ตอนนี้ production ตอบด้วย fast path/rule/RAG-lite

ข้อดี:

- เร็ว
- ฟรี
- deploy Vercel ได้
- คุมคำตอบได้

ข้อจำกัด:

- ไม่ flexible เท่า LLM
- ต้องเพิ่ม rule/alias เมื่อเจอคำถามใหม่
- คำถามยาวหรือคลุมเครืออาจ route ผิด

Next step สำหรับ RAG/LLM:

1. ใช้โฟลเดอร์ `19_PSU_Esports_Qwen35_Hybrid_RAG`
2. รวม corpus จาก `18`
3. ทำ lexical + vector index
4. ใช้ Qwen 3B-4B quantized ผ่าน Ollama
5. ให้ LLM ตอบเฉพาะเมื่อมี retrieved context ดีพอ
6. ถ้า context ไม่ดี ให้ no-answer
7. ทำ timeout ไม่เกิน 10 วินาที

## Issue 7: Data Update Flow ยังไม่เป็น admin-friendly

ตอนนี้การเพิ่มข้อมูลต้องแก้ JSONL/code

คนทั่วไปหรือเจ้าหน้าที่อาจไม่สะดวก

Next step:

- ทำ admin page ง่าย ๆ
- เพิ่ม/แก้/ปิด rule
- upload PDF/txt กติกา
- preview answer
- run mini regression
- export JSONL

## Issue 8: Evaluation ยังควรมี Human Review

ถึง GT จะผ่าน แต่ user เคยพบว่า:

- บางคำตอบถูก keyword แต่สื่อสารผิด
- บางคำตอบตอบรายละเอียดก่อนคำตอบหลัก
- บางคำตอบใช้ route ถูกแต่ภาษาไม่ตรงใจ

Human review criteria ที่เคยคุย:

คะแนน 0-4:

```text
4 = ดีแล้ว ใช้จริงได้ ตอบตรง อ่านง่าย
3 = ถูก แต่ยังเรียงคำตอบ/เติมรายละเอียดได้อีกนิด
2 = มีส่วนถูก แต่ทำให้ลูกค้าเข้าใจผิดได้
1 = ตอบผิดเป็นหลัก แต่ยังเกี่ยวข้องนิดหน่อย
0 = ผิด/มั่ว/ไม่มีข้อมูลแต่ตอบเหมือนมี
```

Decision:

```text
pass = ผ่าน ใช้ได้เลย
minor_fix = ถูก แต่ควรปรับคำพูด/เรียงคำตอบ
major_fix = ผิดประเด็น ผิดราคา ผิดกฎ หรือเสี่ยงเข้าใจผิด
needs_data = ไม่มีข้อมูลจริง ต้องขอข้อมูลเพิ่ม
needs_policy = ต้องถามศูนย์/ผู้ดูแล เพราะเป็นเรื่องกฎหรือนโยบาย
```

ผู้ใช้บอกภายหลังว่า human review ไม่ต้องทำต่อก็ได้ แต่แนวคิดนี้ยังควรเก็บไว้ใช้เมื่อเข้าสู่ production

## Issue 9: Holiday API ยัง manual

ตอนนี้วันปิด 28-30 ก.ค. 2026 config เอง

ถ้าจะใช้งานจริง:

- ใช้ Thai public holiday API
- หรือ maintain `service_closures.jsonl` โดยเจ้าหน้าที่
- ควรแยก holiday public กับ closure ของศูนย์

คำถามที่ควร test:

- วันนี้เปิดไหม
- เดือนนี้หยุดวันไหน
- 28 ก.ค. เปิดไหม
- วันหยุดราชการเปิดไหม

## Issue 10: Deploy package อาจมีไฟล์เกิน

ตอน sync data ไป deploy folder มีบางไฟล์ ground_truth/human_review/log ถูก copy เข้า local deploy folder แต่ `vercel.json` exclude ไว้

ควรทำต่อ:

- ทำ script sync ที่ copy เฉพาะไฟล์จำเป็น
- หรือจัด deploy folder สะอาดกว่าเดิม
- ตรวจขนาดก่อน deploy

## Priority Next Steps

แนะนำลำดับทำต่อ:

1. เก็บคำถามจริงจาก user log แล้วทำ ad-hoc/GT ใหม่
2. เพิ่ม multi-question splitter
3. เพิ่ม session memory เบื้องต้นในเว็บ
4. เพิ่ม admin data update flow แบบง่าย
5. เพิ่มข้อมูลจริงจากศูนย์ เช่น penalty, booking API, latest games
6. ทำ Facebook Messenger webhook
7. ทดลอง RAG/LLM fallback จากโฟลเดอร์ `19`
8. ทำ Dockerfile สำหรับ local backend
9. ทำ GitHub repo และ Vercel auto deploy
10. ทำ dashboard ดู logs และ unanswered questions

## Checklist ก่อนส่ง demo

ก่อน demo ควรเช็ค:

- เว็บ production เปิดได้
- `/api/health` OK
- `/api/chat` ตอบคำถามหลักได้
- local server ยังรันได้
- ราคา Service Fee ตอบถูก
- วันนี้/วันหยุดตอบถูก
- คำถาม unknown game ไม่มั่ว
- คำถามกติกาแข่งไม่หลุดเกม
- route/mode/source แสดงในเว็บ
- มี daily log ล่าสุด
- มี report GT ล่าสุด

