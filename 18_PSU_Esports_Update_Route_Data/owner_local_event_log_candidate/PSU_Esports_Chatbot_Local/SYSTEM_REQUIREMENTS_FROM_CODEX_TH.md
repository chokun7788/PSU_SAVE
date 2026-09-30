# ข้อกำหนดระบบที่สรุปจากการทำงานร่วมกัน

เอกสารนี้บันทึกเจตนาของระบบที่ตกลงกันระหว่างการพัฒนา เพื่อให้ผู้ดูแลหรือผู้พัฒนารอบถัดไปใช้เป็นขอบเขตเดียวกัน ไม่ใช่คู่มือใช้งานรายวัน

## เป้าหมายหลักปัจจุบัน

1. Chatbot ต้องตอบ FAQ ของ PSU Esports Studio เป็นความสามารถหลัก พร้อมแหล่งอ้างอิงที่ตรวจสอบได้
2. รองรับภาษาไทยและอังกฤษด้วย Auto / ไทย / English โดยข้อมูลจริงชุดเดียวกัน และไม่แปลข้อเท็จจริงสดด้วย LLM
3. ทำงานด้วย Local Model ขนาดไม่เกินประมาณ 10B เป็นหลัก ไม่พึ่ง Cloud Chatbot API ระหว่างตอบ
4. ใช้ Fast/Structured สำหรับข้อเท็จจริงชัดเจน, Semantic RAG สำหรับเอกสารและข้อมูลใหม่, Local LLM สำหรับช่วยเข้าใจเจตนา/บริบทและเรียบเรียงจากหลักฐานที่ยืนยันแล้ว
5. ให้ตอบได้กับการพิมพ์ไม่เป็นทางการ การพิมพ์สลับภาษา และ typo ในระดับที่ปลอดภัย โดยขอให้พิมพ์ใหม่เมื่อคุณภาพ input ไม่พอ แทนการเดาคำตอบ

## ข้อมูลและการเพิ่มความรู้

- แหล่งข้อมูลตั้งต้นคือเว็บไซต์ PSU Esports Studio, PDF และ Facebook/ประกาศที่ผ่านการคัดเลือก
- ข้อมูลใหม่ต้องเข้าสู่ format กลาง, ตรวจ schema, review/approve แล้วจึงสร้าง Structured Projection และ RAG Index ใน release เดียวกัน
- ข้อมูลที่ต้องตอบแบบ exact เช่น ราคา, เวลาเปิด, โซน, อุปกรณ์ และรายชื่อเกม ต้องมาจาก verified record ไม่ใช่ข้อเท็จจริงที่ LLM คิดขึ้น
- English localization เป็น overlay ที่ต้องอนุมัติ หากไม่พร้อมให้ตอบ no-answer ภาษาอังกฤษพร้อมแหล่งต้นฉบับ

## การตอบและประสบการณ์ผู้ใช้

- ผู้ใช้เริ่มจาก Text เป็นหลัก; Image/PDF เป็น Phase ถัดไป
- คำตอบควรมี format ที่สม่ำเสมอระหว่างไทยและอังกฤษ โดยเฉพาะรายการเกม, ตารางเปิดบริการ, ราคา และกฎ
- บอทเก็บบริบทเฉพาะใน Session เดียวกัน เพื่อรองรับคำถามต่อเนื่อง แต่ไม่ควรนำ context ของคนหนึ่งไปปนกับอีกคน
- หากหลักฐานไม่พอ, target กำกวม, หรืออยู่นอกขอบเขต PSU Esports ให้ถามกลับหรือ no-answer อย่างชัดเจน

## Local Operation และ Audit

- ชุดนี้ใช้ `127.0.0.1` เท่านั้นสำหรับเจ้าของเครื่อง จึงไม่มี Login และไม่ใช่เว็บไซต์สาธารณะ
- ทุกการสนทนาถูกบันทึกเป็น Session Number/Session ID, Message ID, Request/Exchange ID, ข้อความ, คำตอบ, route, mode, latency, language และแหล่งอ้างอิง ใน SQLite/JSONL ภายในเครื่อง
- Refresh หน้าเว็บต้องเริ่ม Session ใหม่และล้างเฉพาะหน้าจอ แต่ audit log ของทุก Session ต้องอยู่ต่อเนื่องเพื่อให้ผู้ดูแลดูย้อนหลังได้
- Log เป็นข้อมูลลับ ผู้ดูแลต้องกำหนด retention, backup และผู้มีสิทธิ์เข้าถึงก่อนนำไปใช้กับผู้ใช้จริง

## Core Functions อื่นที่ยังเป็น Phase ถัดไป

### Check Slot

ต้องใช้ WordPress/Booking API จริงผ่าน Adapter เพื่อแสดงสถานะ read-only ของ zone/equipment/game, ช่วงจอง, ช่วงว่าง, maintenance และวันปิด โดยห้ามแสดงข้อมูลผู้จอง

### Admin Content Input / Dual Publish

ต้องมีหน้า Admin สำหรับเพิ่มเกม, กฎ, อุปกรณ์, FAQ, ข่าว และวันเปิดปิด; LLM ช่วยได้เพียง Draft แต่ผู้อนุมัติเป็นผู้ Publish หลัง validation และต้องมี rollback

### Booking และ Payment Verification

ต้องเป็น Booking State Machine ที่ deterministic ไม่ให้ LLM ยืนยันธุรกรรมเอง ชุด production ต้องมี Slot Hold, idempotency, secure form, payment provider และ manual review fallback; การอ่าน QR/OCR จากสลิปเพียงอย่างเดียวไม่ถือว่ายืนยันเงินเข้า

## ข้อกำหนดก่อนเปิดเป็นเว็บไซต์สาธารณะ

ต้องย้ายจาก Local-only เป็น production architecture ที่มี HTTPS, Login/role, signed server-side session, PostgreSQL, separate log access, retention policy, rate limit, multi-user worker/queue, monitoring และ load test ก่อนเปิดใช้งานจริง
