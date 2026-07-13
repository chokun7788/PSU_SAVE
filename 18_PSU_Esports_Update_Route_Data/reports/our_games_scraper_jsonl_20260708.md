# Our Games Scraper JSONL 2026-07-08

## เป้าหมาย

ดึงข้อมูลเกมทั้งหมดจากหน้า `https://esports.phuket.psu.ac.th/Services/our-games` ด้วยโค้ด แทนการให้ AI อ่านและพิมพ์ข้อมูลเอง เพื่อลด token และลดความเสี่ยงตกหล่น

## สิ่งที่เพิ่ม

- เพิ่ม `tools/scrape_our_games.py`
  - fetch หน้า Our Games
  - ตัด navigation ซ้ำของ Google Sites ออก
  - parse เฉพาะ block `Our Games`
  - แยก section `Nintendo Switch` และ `PlayStation 5`
  - ใช้ `bs4` ถ้ามี และ fallback เป็น `html.parser` ของ standard library ถ้าไม่มี
- สร้าง `data/sources/our_games_raw.jsonl`
  - เก็บข้อมูลดิบจากเว็บแบบเต็ม
  - field สำคัญ: `game`, `source_section`, `listed_under`, `description`, `aliases`, `source_url`
- สร้าง `data/curated/our_games_scraped_details.jsonl`
  - เวอร์ชันพร้อมใช้กับ retrieval/vector
  - ใช้ข้อความสั้นกว่า raw เพื่อไม่ให้ chatbot ตอบยาวเกินไป
- rebuild `data/vector/psu_hybrid_vector_index.json`
  - index เพิ่มจาก 247 เป็น 278 documents

## ผล scrape

- รวม 31 เกม
- Nintendo Switch: 16 เกม
- PlayStation 5: 15 เกม

หมายเหตุ: field `source_section` คือ section ในหน้าเว็บ ไม่ได้แปลว่าเป็นโซนจองโดยตรงเสมอ จึงไม่ฟันธง `เล่นได้ที่ PlayStation 5 Zone` จาก scraper สำหรับทุกเกม

## Logic ที่แก้เพิ่ม

- ปรับ `app/pipeline/retrieval.py`
  - game detail จาก curated ทุกไฟล์ต้องผ่าน entity match
  - กันเคส `เกม abcxyz คืออะไร` ไม่ให้ดึง Zelda/Super Smash มั่ว
- ปรับ `app/runtime/fast_answer.py`
  - เพิ่ม `Mario Kart Live: Home Circuit`
  - ปรับ matcher ให้ alias ที่ยาวและเฉพาะกว่าชนะก่อน เช่น `mario kart live` ชนะ `mario kart`

## Smoke

- `Mario Kart Live คือเกมอะไร`
  - mode: `pipeline:game_detail_fast_path`
  - ตอบ Mario Kart Live ถูก
- `Mario Kart 8 คือเกมอะไร`
  - mode: `pipeline:game_detail_fast_path`
  - ยังตอบ Mario Kart 8 Deluxe ถูก
- `อยากเล่น Mario Kart Live`
  - mode: `pipeline:games_availability_fast_path`
- `เกม abcxyz คืออะไร`
  - mode: `pipeline:no_answer`
  - ไม่ดึงเกมอื่นมาตอบ

## ตรวจแล้ว

- `py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\retrieval.py tools\scrape_our_games.py`
- `py -3 tools\validate_update.py`
- ไม่ได้ run Ground Truth ชุดใหญ่
- ยังไม่ได้ deploy production
