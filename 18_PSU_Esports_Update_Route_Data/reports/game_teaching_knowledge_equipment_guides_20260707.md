# Game Teaching, Knowledge, and Equipment Guides - 2026-07-07

## เป้าหมาย

แก้กลุ่มคำถามที่ยังตอบไม่ดี:

- `สอนเล่นเกม PubG หน่อย`
- คำถาม Knowledge เช่น `เกม Multiplayer Online Battle Arena (MOBA) ยอดนิยม`
- คำถาม `ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต`
- คำถามวิธีใช้อุปกรณ์ เช่น PS5, Cockpit, VR, Nintendo Switch
- คำตอบจาก curated RAG บางครั้งมี `????`

## แหล่งข้อมูลที่ใช้

- `https://esports.phuket.psu.ac.th/Knowledge/เกมที่นิยมในปัจจุบัน`
- `https://esports.phuket.psu.ac.th/Knowledge/ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต`
- `https://esports.phuket.psu.ac.th/Services/how-to-use-equipment-in-studio`
- `https://esports.phuket.psu.ac.th/Services/our-games`

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/runtime/fast_answer.py`
- `app/pipeline/router.py`
- `data/curated/game_item_details.jsonl`

### 1. สอนเล่นเกม

เพิ่ม intent phrase:

- `สอนเล่น`
- `สอนเล่นเกม`
- `สอนหน่อย`
- `เล่นยังไงดี`
- `เล่นเกมยังไง`

ผล:

- `สอนเล่นเกม PubG หน่อย`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
  - ตอบวิธีเล่น PUBG ไม่หลุดไป catalog/RAG

### 2. Knowledge: MOBA / ประเภทเกมยอดนิยม

เพิ่ม fast path:

- `knowledge_moba_popular_games_fast_path`
- `knowledge_moba_definition_fast_path`
- `knowledge_esports_game_types_fast_path`
- `knowledge_popular_games_by_genre_fast_path`

ตัวอย่างคำตอบ:

- MOBA ยอดนิยม: League of Legends, Dota 2, Mobile Legends: Bang Bang, Honor of Kings, Wild Rift, Arena of Valor
- ประเภทเกมอีสปอร์ต: MOBA, FPS, Battle Royale, Fighting Games, Sports Games

### 3. คู่มือใช้อุปกรณ์ ไทย/อังกฤษ

เพิ่ม fast path จากภาพในหน้า `How to Use Equipment in Studio`:

- `equipment_usage_cockpit_fast_path`
- `equipment_usage_ps5_fast_path`
- `equipment_usage_vr_fast_path`
- `equipment_usage_nintendo_fast_path`

รองรับคำถามเช่น:

- `วิธีใช้ PS5`
- `สอนใช้ VR`
- `ใช้ Cockpit ยังไง`
- `วิธีใช้งาน Nintendo Switch`

คำตอบมีทั้ง:

- ภาษาไทย
- English
- แหล่งข้อมูลหน้า how-to-use-equipment

### 4. แก้ `????` ใน curated game data

ไฟล์ `data/curated/game_item_details.jsonl` มี field `text` บางส่วนเป็น `??????` จาก label ที่เสีย encoding

แก้โดย rewrite `text` ของ 36 แถวจาก field structured ที่ถูกต้อง:

- `game`
- `summary_th`
- `genre`
- `how_to_play_th`
- `zones`

รูปแบบใหม่:

```text
ชื่อเกม: summary
แนวเกม: genre
วิธีเล่นโดยสรุป: how_to_play
เล่นได้ที่: zones
```

### 5. Route cleanup

แก้ router ไม่ให้คำถาม:

```text
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ตมีอะไรบ้าง
```

หลุดไป `events_news/news_lookup` หรือ `competition_game_list`

ผลหลังแก้:

- route: `knowledge/knowledge_lookup`
- mode: `pipeline:knowledge_esports_game_types_fast_path`

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

- `สอนเล่นเกม PubG หน่อย`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
  - ไม่มี `????`
- `กม Multiplayer Online Battle Arena (MOBA) ยอดนิยม`
  - route: `knowledge/knowledge_lookup`
  - mode: `pipeline:knowledge_moba_popular_games_fast_path`
- `ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ตมีอะไรบ้าง`
  - route: `knowledge/knowledge_lookup`
  - mode: `pipeline:knowledge_esports_game_types_fast_path`
- `วิธีใช้ PS5`
  - route: `equipment/zone_equipment_lookup`
  - mode: `pipeline:equipment_usage_ps5_fast_path`
- `สอนใช้ VR`
  - route: `equipment/zone_equipment_lookup`
  - mode: `pipeline:equipment_usage_vr_fast_path`
- `ใช้ Cockpit ยังไง`
  - route: `equipment/zone_equipment_lookup`
  - mode: `pipeline:equipment_usage_cockpit_fast_path`
- `วิธีใช้งาน Nintendo Switch`
  - route: `equipment/zone_equipment_lookup`
  - mode: `pipeline:equipment_usage_nintendo_fast_path`
- `วิธีเล่น เซลด้า`
  - route: `games/game_detail_lookup`
  - mode: `pipeline:game_detail_fast_path`
  - ไม่มี `????`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
