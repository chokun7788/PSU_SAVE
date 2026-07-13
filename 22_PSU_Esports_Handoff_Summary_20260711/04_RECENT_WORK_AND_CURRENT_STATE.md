# Recent Work And Current State

สรุปสถานะล่าสุดหลังงานในแชทเดิมจนถึงวันที่ 2026-07-11

## งานล่าสุดที่สุด: Game Control JSONL + Vector

ผู้ใช้ต้องการให้แยกข้อมูลวิธีควบคุมเกมจาก folder เดิม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\control_game\nintendo
```

แม้ชื่อ folder เป็น `nintendo` แต่จริง ๆ มีทั้ง Nintendo Switch และ PS5

สิ่งที่ทำแล้ว:

- สร้าง script:

```text
tools\build_game_control_facts.py
```

- สร้าง folder ใหม่:

```text
data\control_game_split\ps5
data\control_game_split\nintendo
```

- สร้าง curated JSONL:

```text
data\curated\game_control_facts.jsonl
```

- rebuild vector:

```text
data\vector\psu_hybrid_vector_index.json
```

ผลลัพธ์:

- control facts ทั้งหมด: 346 rows
- PS5: 18 games, 261 rows
- Nintendo Switch: 8 games, 85 rows
- game controls ใน vector: 346 docs
- vector docs รวม: 659 docs

เพิ่ม logic:

- `app/pipeline/vector_retrieval.py`
  - เพิ่ม `looks_like_game_control_query()`
  - เปิดให้ route `games` และ `equipment` ดึง category `game_controls`
  - guard ให้ใช้เฉพาะคำถามปุ่ม/จอย/ควบคุม
  - format คำตอบปุ่มเป็น bullet ที่อ่านง่าย

- `app/pipeline/engine.py`
  - เพิ่ม `pipeline:game_control_vector_first`
  - ให้คำถามปุ่มลอง vector control ก่อน fast path เกมทั่วไป
  - ถ้า route เป็น general แต่มีสัญญาณถามปุ่ม ให้ลอง synthetic route `games/game_control_lookup`

Smoke test ที่ผ่าน:

- `ปุ่มกระโดดใน Call of Duty กดอะไร`
  - ตอบ Call of Duty: Modern Warfare III controls
- `เทคเคน 8 ปุ่มเตะขวากดอะไร`
  - ตอบ `Circle`
- `ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร`
  - ตอบ `Square`
- `เกมเทคอิดเอ้าปุ่มกระโดดกดอะไร`
  - ตอบ It Takes Two ปุ่ม `Cross`

## งานก่อนหน้า: Booking Fix

ปัญหาเดิม:

- `อยากรู้ว่าจะจองคิวเล่นเกมต้องทำยังไง`
- `จองอุปกรณ์ต้องทำยังไง`
- `วิธีการจองอุปกรณ์`

บางคำถามตอบผิดเป็นนโยบายยกเลิก/คืนเงิน

แก้แล้วใน:

```text
app\runtime\fast_answer.py
```

ผล:

- คำถามวิธีจองเข้า `pipeline:booking_howto_fast_path`
- `สอนจอง VR` ตอบวิธีจอง ไม่ตอบรายชื่อเกม VR
- cancellation/refund ยังแยกอยู่ ไม่โดน booking how-to แย่ง

## งานก่อนหน้า: Full Game Catalog Count

ปัญหาเดิม:

- ถาม `มีเกมทั้งหมดกี่เกม` แล้วตอบแค่รายการสรุปเก่าบางส่วน

แก้แล้ว:

- ให้ตอบจำนวนเกมทั้งหมดจากรายการเกมที่ยืนยันได้
- แสดงรายการแยกตาม zone
- mode ที่เกี่ยวข้อง:

```text
pipeline:games_full_catalog_count_fast_path
```

## งานก่อนหน้า: Game Alias / Typo

เพิ่มและใช้:

```text
data\curated\game_title_aliases.jsonl
```

ใช้รองรับ:

- ชื่อเกมภาษาไทย
- ชื่อย่อ
- สะกดเพี้ยน
- ทับศัพท์ เช่น `พับจี`, `วาโล`, `เทคเคน`, `เรสซิเดนท์`, `โอเวอคุก`

ข้อควรจำ:

- Alias ยังจำเป็น แม้มี vector
- Vector ช่วยจับคำใกล้เคียง แต่ alias ช่วยล็อก entity ให้ไม่หลุดไปเกมอื่น

## Production State

โฟลเดอร์ 20 มีการ sync งานล่าสุดแล้ว และ build vector ผ่านแล้ว

แต่:

- ยังไม่ได้ deploy production จากงานล่าสุด ถ้าผู้ใช้ยังไม่ได้กดเอง
- ถ้าคำตอบบน Vercel ยังเหมือนเดิม ให้เช็กก่อนว่า deploy แล้วจริงหรือยัง

## Known Risks

- ถ้า route/fast path ตอบก่อน retrieval ข้อมูลใหม่อาจไม่ถูกใช้
- ถ้า vector guard เปิดกว้างเกินไป จะกลับไปตอบมั่วจากเอกสารใกล้เคียง
- ถ้าเพิ่ม data ใหม่ ต้องเช็กว่า:
  - data ถูกโหลดเข้า curated หรือ vector จริงไหม
  - route/category อนุญาตให้ดึงไหม
  - answer formatter รองรับไหม
  - validation ไม่ block ผิดไหม

