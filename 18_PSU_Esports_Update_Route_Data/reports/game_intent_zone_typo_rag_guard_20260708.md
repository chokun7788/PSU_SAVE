# Game Intent, Zone Typo, and RAG Guard Fix - 2026-07-08

## ปัญหา

ผู้ใช้แจ้งเคสที่ยังตอบผิด:

- `อยากเล่น VR`
  - เคยตอบว่า `ยังไม่พบ เกมนี้...`
  - ทั้งที่ VR เป็นโซน/อุปกรณ์ ไม่ใช่ชื่อเกมที่ไม่พบ
- `วิธฟเล่น super smash`
  - typo คำว่า `วิธี`
  - เคยตอบแค่ catalog Nintendo Switch
- `วิธีเล่น SSMU`
  - `SSMU` เป็นตัวย่อ Super Smash Bros Ultimate
  - เคยหลุดไป experimental RAG และดึง VALORANT มาตอบ
- `วิธีเล่นโอเวอคุก`
  - พิมพ์ Overcooked เป็นไทยแบบไม่ตรง alias
  - เคยหลุดไป experimental RAG และดึง League of Legends มาตอบ
- คำถามแนว `วิธีเล่น เกมมั่ว ๆ`
  - ไม่ควรให้ RAG สุ่มเกมอื่นมาตอบ

## สาเหตุ

- `_looks_like_game_availability()` จับ `อยากเล่น` กว้างเกินไป แล้วมอง `VR` เป็นเกมที่ไม่พบ
- normalization ยังไม่มี `วิธฟ`, `SSMU`, `โอเวอคุก`
- ถ้าเป็น game-detail intent แต่จับชื่อเกมไม่ได้ ระบบยังปล่อยไป curated/experimental RAG ได้
- RAG จึงดึงเกมใกล้เคียงผิดบริบท เช่น VALORANT หรือ League of Legends

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/core/normalization.py`
- `app/runtime/fast_answer.py`

### Normalization

เพิ่ม:

- `วิธฟ` -> `วิธี`
- `วีธฟ` -> `วิธี`
- `ssmu` -> `super smash`
- `โอเวอคุก` -> `overcooked`
- `โอเวอคุ๊ก` -> `overcooked`
- `โอเวอร์คุค` -> `overcooked`

### Zone Play Request

เพิ่ม `_zone_play_request_answer()`:

- ถ้าผู้ใช้ถามแนว `อยากเล่น VR`, `อยากเล่น PS5`, `อยากเล่น Cockpit`
- ระบบจะตอบโซน/เกมในโซนนั้น แทนการตอบว่าไม่พบเกม

### Game Detail Unknown No-answer

เพิ่ม `_game_detail_unknown_no_answer()`:

- ถ้าคำถามเป็นแนว `วิธีเล่น...` / `สอนเล่น...`
- แต่ระบบจับชื่อเกมไม่ได้
- ให้ตอบว่าไม่แน่ใจว่าหมายถึงเกมไหน และไม่ดึงเกมอื่นมาตอบแทน

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20 โดยเปิด `experimental_rag_fallback=True`:

- `อยากเล่น VR`
  - normalized: `อยากเล่น vr`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:zone_play_request_fast_path`
  - ไม่หลุดไป `games_unknown_fast_path`
- `วิธฟเล่น super smash`
  - normalized: `วิธีเล่น super smash`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วิธีเล่น SSMU`
  - normalized: `วิธีเล่น super smash`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วิธีเล่นโอเวอคุก`
  - normalized: `วิธีเล่นovercooked`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `วิธีเล่น เกมมั่ว ๆ`
  - route: `games/games_lookup`
  - mode: `pipeline:games_detail_unknown_no_answer_fast_path`
  - ไม่หลุดไป RAG
- `วิธีเล่น Valorant`
  - ยังตอบ game detail ปกติ

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
