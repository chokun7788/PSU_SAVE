# Game Catalog Intent Fix - 2026-07-07

## ปัญหา

คำถาม:

```text
มีเกมอะไรให้เล่นบ้าง
```

เคยตอบขึ้นต้นผิดว่า:

```text
ยังไม่พบ เกมนี้ ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
```

แม้รายละเอียดด้านล่างจะเป็นรายการเกมที่ถูกต้อง แต่ประโยคเปิดผิดบริบท เพราะผู้ใช้ถามรายการเกมรวม ไม่ได้ถามหาเกมเฉพาะชื่อใดชื่อหนึ่ง

## สาเหตุ

ใน `app/runtime/fast_answer.py` เงื่อนไข `_looks_like_game_availability()` กว้างเกินไป เพราะคำว่า `มีเกม` / `เกมอะไร` ถูกตีความเป็นคำถาม availability ของเกมเฉพาะ ก่อนจะถึง fallback catalog answer

อีกจุดที่พบจาก smoke test:

```text
ตอนนี้รายการแข่งเกมอะไรบ้าง
```

เคยหลุดไป route schedule เพราะ `_looks_like_schedule_date_query()` เจอคำว่า `ตอนนี้` ก่อน intent รายการแข่ง

## สิ่งที่แก้

- เพิ่ม `_looks_like_game_catalog()` ใน `app/runtime/fast_answer.py`
- ให้ `answer_games()` ตอบ catalog รวมก่อนเข้า unknown-game availability
- เพิ่ม `_looks_like_game_catalog_query()` ใน `app/pipeline/router.py`
- เพิ่ม route:
  - `games/game_catalog_lookup`
  - mode ที่คาดหวัง: `pipeline:games_catalog_fast_path`
- ปรับลำดับ router ให้ `competition_game_list` มาก่อน schedule date query เพื่อกันคำว่า `ตอนนี้` ทำให้รายการแข่งหลุดไป schedule
- sync ไฟล์ที่แก้ไปโฟลเดอร์ deploy 20 แล้ว

ไฟล์ที่แก้:

- `app/runtime/fast_answer.py`
- `app/pipeline/router.py`

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

- `มีเกมอะไรให้เล่นบ้าง`
  - route: `games/game_catalog_lookup`
  - mode: `pipeline:games_catalog_fast_path`
  - ตอบรายการเกมรวมโดยไม่ขึ้น `ยังไม่พบ เกมนี้`
- `เกมอะไรบ้าง`
  - route: `games/game_catalog_lookup`
  - mode: `pipeline:games_catalog_fast_path`
- `มีเกม Minecraft ไหม`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_unknown_fast_path`
  - ยังตอบ no-answer เฉพาะเกมที่ไม่มีข้อมูลยืนยันได้ตามเดิม
- `อยากเล่น Mario`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_family_availability_fast_path`
- `VR มีเกมอะไรบ้าง`
  - route: `equipment/equipment_game_catalog`
  - mode: `pipeline:equipment_game_catalog_fast_path`
- `ตอนนี้รายการแข่งเกมอะไรบ้าง`
  - route: `games/competition_game_list`
  - mode: `pipeline:competition_game_list_fast_path`
- `ตอนนี้เปิดไหม`
  - route: `schedule/schedule_query`
  - mode: `pipeline:current_service_slot_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

แก้และ sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
