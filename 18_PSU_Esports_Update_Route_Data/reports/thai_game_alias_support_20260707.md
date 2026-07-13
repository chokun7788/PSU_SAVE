# Thai Game Alias Support - 2026-07-07

## ปัญหา

ผู้ใช้อาจพิมพ์ชื่อเกมเป็นภาษาไทยหรือสะกดหลายแบบ เช่น:

- `อาโอวี`
- `วาโล`
- `วาโลแรนท์`
- `เทคเคน8`
- `เทกเคน`

ถ้าระบบพึ่ง exact English alias มากเกินไป จะทำให้ route หลุดหรือ RAG ดึงข้อมูลผิดหมวด

## แนวทางที่ใช้

แก้แบบประหยัด token/data:

- ไม่ดึงข้อมูลเว็บเพิ่ม
- ไม่โหลดข้อมูลก้อนใหญ่
- เพิ่ม alias เฉพาะชื่อเกมที่เกี่ยวกับฐานข้อมูลปัจจุบัน
- แยกเกมที่มีให้เล่นจริงใน catalog ออกจากเกมที่มีเฉพาะข้อมูลกติกาการแข่งขัน

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/core/normalization.py`
- `app/runtime/fast_answer.py`
- `app/pipeline/router.py`

เพิ่ม normalization:

- `วาโลแรนท์` / `วาโลแรน` -> `valorant`
- `วาโร` -> `วาโล`
- `เทคเคน8` -> `เทคเคน 8`
- `เทกเคน` -> `เทคเคน`
- `อาโอวี` / `เอโอวี` / `อาร์โอวี` / `อาโอวี่` -> `rov`

เพิ่ม alias ใน supported games:

- VALORANT: `วาโล`, `วาโลแรนท์`, `วาโลแรน`
- TEKKEN 8: `เทคเคน`, `เทคเคน 8`, `เทคเคน8`, `เทกเคน`

เพิ่ม known unsupported game:

- RoV / Arena of Valor: `rov`, `aov`, `arena of valor`, `อาโอวี`, `เอโอวี`, `อาร์โอวี`, `เกมตีป้อม`

เหตุผล:

- RoV มีข้อมูลกติกาการแข่งขันในฐานข้อมูล
- แต่ยังไม่พบว่า RoV อยู่ในรายการเกมให้เล่นของ PSU Esports Studio - Phuket
- ดังนั้นถ้าถามว่าอยากเล่น/วิธีเล่น RoV ต้องไม่ดึงเกมอื่นมาตอบ และไม่บอกว่ามีให้เล่น

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

- `อยากเล่น อาโอวี`
  - normalized: `อยากเล่น rov`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_known_unsupported_fast_path`
- `วิธีเล่น อาโอวี`
  - normalized: `วิธีเล่น rov`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:games_known_unsupported_fast_path`
- `กติกา อาโอวี`
  - normalized: `กติกา rov`
  - route: `competition_rules/competition_rules_lookup`
  - mode: `pipeline:competition_fact_card`
- `อยากเล่น วาโลแรนท์`
  - normalized: `อยากเล่น valorant`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_availability_fast_path`
- `วิธีเล่น วาโลแรนท์`
  - normalized: `วิธีเล่น valorant`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
- `อยากเล่น เทคเคน8`
  - normalized: `อยากเล่น เทคเคน 8`
  - route: `games/game_availability_lookup`
  - mode: `pipeline:games_availability_fast_path`
- `วิธีเล่น เทคเคน8`
  - normalized: `วิธีเล่น เทคเคน 8`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
