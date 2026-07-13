# Domain-context Fuzzy Normalization - 2026-07-07

## ปัญหา

ผู้ใช้กังวลว่าการเพิ่ม alias/typo ทีละคำ เช่น `เล่ง -> เล่น` จะไม่ scalable เพราะผู้ใช้อาจพิมพ์ผิดได้หลายแบบ

ตัวอย่างปัญหา:

```text
วิธีเล่น Beat Saver
วิธีเ่น Valorant
เล่ง Beat Saber
วิทีเล่น Valorant
วีธีเล่ง Tekken
```

ถ้าแก้ด้วย replacement list อย่างเดียว จะต้องไล่เพิ่มคำผิดไปเรื่อย ๆ

## แนวทางที่เลือก

เพิ่ม fuzzy normalization เฉพาะคำ intent ที่สำคัญ และเปิดใช้เฉพาะเมื่อ query มี context ของระบบ เช่น เกม, VR, PS5, PC, ชื่อเกม, ราคา, เวลา, บริการ

ไม่ทำ spell correction ภาษาไทยทั้งระบบ เพราะเสี่ยงเปลี่ยนคำที่ผู้ใช้ตั้งใจพิมพ์ และอาจทำให้ route ผิดกว่าเดิม

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/core/normalization.py`

เพิ่ม:

- `DOMAIN_CONTEXT_FUZZY_KEYWORDS`
  - `เล่น`
  - `วิธี`
  - `เปิด`
- `DOMAIN_CONTEXT_TERMS`
  - context ของระบบ เช่น `เกม`, `vr`, `ps5`, `pc`, `valorant`, `beat`, `saber`, `ราคา`, `บริการ`, `เวลา`
- `_has_domain_context()`
- ปรับ `_fuzzy_replace_keyword()` ให้รองรับคำที่ขาด/เกิน 1 ตัวอักษรสำหรับคำสั้น
- เพิ่ม guard `candidate in canonical` เพื่อกันไม่ให้คำที่ถูกอยู่แล้วโดนแก้ซ้ำ เช่น `เล่น -> เล่นน`, `วิธี -> วิธีี`

คำที่ตั้งใจไม่ใส่ fuzzy กว้างในรอบนี้:

- `จอง`
- `ปิด`

เหตุผล:

- คำสั้นเกินไปและมีโอกาส false positive เช่น `ผิด` อาจโดนลากไป `ปิด`
- ถ้าต้องรองรับ booking typo ควรเพิ่มพร้อม test case แยก

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

Normalization:

- `เล่ง Beat Saber` -> `เล่น beat saber`
- `วิธีเล่ง Beat Saver` -> `วิธีเล่น beat saber`
- `วิทีเล่น Valorant` -> `วิธีเล่น valorant`
- `วีธีเล่ง Tekken` -> `วิธีเล่น tekken`
- `อยากเล่ง Mario` -> `อยากเล่น mario`
- `เล่น Beat Saber` -> `เล่น beat saber`
- `วิธีเล่น Valorant` -> `วิธีเล่น valorant`
- `กติกาเกมผิดไหม` ไม่ถูกแก้เป็นคำอื่น
- `จอคอมมีไหม` ไม่ถูกแก้เป็น `จอง...`

Pipeline:

- `วิธีเล่ง Beat Saver`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วิทีเล่น Valorant`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วีธีเล่ง Tekken`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `อยากเล่ง Mario`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_family_availability_fast_path`
- `ตอนนี้เปิดไหม`
  - route: `schedule/schedule_query`
  - mode: `pipeline:current_service_slot_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง

## ข้อจำกัด

- วิธีนี้ไม่ได้ทำให้ภาษาไทยทุกคำถูก 100%
- เหมาะกับคำ intent สำคัญในโดเมน chatbot
- ถ้าจะขยายต่อ ควรเพิ่มทีละกลุ่มพร้อม guard และ smoke test เพื่อไม่ให้ false positive เพิ่มขึ้น
