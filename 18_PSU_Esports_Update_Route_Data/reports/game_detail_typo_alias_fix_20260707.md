# Game Detail Typo and Alias Fix - 2026-07-07

## ปัญหา

ผู้ใช้ทดสอบแล้วพบว่า typo เล็กน้อยทำให้คำถามเกมหลุด route:

```text
วิธีเล่น Beat Saver
```

เคยหลุดไป `general/unknown_domain_query` และ experimental RAG ดึงข้อมูล VALORANT กติกาแข่งมาตอบ

อีกเคส:

```text
วิธีเ่น Valorant
```

เคยเข้า games แต่ตอบ catalog PC แทน game detail เพราะคำว่า `เล่น` พิมพ์ตกตัว `ล`

## สาเหตุ

- route/detail matcher พึ่ง exact alias มากเกินไป
- `Beat Saver` ไม่อยู่ใน alias ของ `Beat Saber`
- `วิธีเ่น` ไม่ถูก normalize เป็น `วิธีเล่น`
- เมื่อ route ไม่แม่น experimental RAG อาจดึงข้อมูลใกล้เคียงผิดหมวด เช่น competition rules ของ VALORANT

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/core/normalization.py`
- `app/runtime/fast_answer.py`

รายละเอียด:

- เพิ่ม typo normalization:
  - `วิธีเ่น` -> `วิธีเล่น`
  - `beat saver` / `beatsaver` -> `beat saber`
- เพิ่ม fuzzy alias matching ให้ `_match_game_detail()` และ `_match_supported_game()`
  - ใช้ `contains_alias()` ที่มีอยู่แล้วใน `app/core/normalization.py`
  - จำกัดเฉพาะ alias ที่ยาวพอ เพื่อลด false positive จาก alias สั้น เช่น `lol`, `gt7`
  - threshold: `0.88`
- sync ไฟล์ที่แก้ไปโฟลเดอร์ deploy 20 แล้ว

## เหตุผลที่ไม่เอา PyThaiNLP กลับมา

ปัญหานี้เป็น domain typo / game alias มากกว่า spell correction ภาษาไทยทั่วไป

การใช้ normalization + fuzzy alias เหมาะกว่าเพราะ:

- เร็วกว่า
- ไม่เพิ่ม dependency หนักใน Vercel
- คุม source ได้ว่าแมตช์เฉพาะเกมที่มีข้อมูลยืนยัน
- ลดความเสี่ยง cold start และ timeout

PyThaiNLP ยังเก็บเป็น optional helper ได้ แต่ไม่ควรเป็นตัวหลักของ production ตอนนี้

## แนวทางทำงานกับโฟลเดอร์ 18 และ 20

ไม่แนะนำให้แก้เฉพาะโฟลเดอร์ 20 อย่างเดียว เพราะ 20 คือ deploy copy ถ้าแก้เฉพาะ 20 แล้วรอบถัดไป sync จาก 18 อาจทับงานหาย

แนวทางที่ใช้:

1. แก้ source จริงในโฟลเดอร์ 18
2. sync เฉพาะไฟล์ที่แตะไป 20
3. compile ทั้ง 18 และ 20
4. smoke test ใน 20 เพราะเป็นโฟลเดอร์ deploy จริง

วิธีนี้ลดงานซ้ำและยังไม่ทำให้ source/deploy drift

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

- `วิธีเล่น Beat Saver`
  - normalized: `วิธีเล่น beat saber`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
  - ตอบวิธีเล่น Beat Saber ถูกต้อง
- `วิธีเ่น Valorant`
  - normalized: `วิธีเล่น valorant`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
  - ตอบวิธีเล่น VALORANT ถูกต้อง
- `วิธีเล่น Beat Saber`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วิธีเล่น Valorant`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `มีเกมอะไรให้เล่นบ้าง`
  - route: `games/game_catalog_lookup`
  - mode: `pipeline:games_catalog_fast_path`
- `มีเกม Minecraft ไหม`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_unknown_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

แก้และ sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
