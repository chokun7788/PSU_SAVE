# Game Popularity No-answer Guard - 2026-07-07

## ปัญหา

คำถาม:

```text
เกมไหนคนเล่ยมากที่สุด
```

ถูก normalize เป็น:

```text
เกมไหนคนเล่นมากที่สุด
```

แต่ระบบเคยดึง RAG game detail ของ PUBG มาตอบ ทั้งที่ฐานข้อมูลไม่มีสถิติยืนยันว่าเกมไหนมีคนเล่นมากที่สุด

## สาเหตุ

- route เข้า games/games_lookup
- deterministic เดิมไม่มีคำตอบเฉพาะสำหรับคำถามเชิงสถิติ/อันดับความนิยม
- curated RAG จึงเลือก game detail ที่ใกล้เคียงมาแทน
- หลังเพิ่ม no-answer fast path แล้ว ยังมีปัญหาเมื่อเปิด `experimental_rag_fallback=True` เพราะ engine ข้าม deterministic no-answer ไปลอง RAG ต่อ

## สิ่งที่แก้

ไฟล์ที่แก้:

- `app/runtime/fast_answer.py`
- `app/pipeline/engine.py`

เพิ่ม:

- `_game_popularity_no_answer()`
  - จับคำถามแนว `คนเล่นมากที่สุด`, `คนเล่นเยอะที่สุด`, `เกมยอดนิยม`, `ฮิตที่สุด`, `most played`, `most popular`
  - ตอบว่าไม่มีสถิติยืนยัน ไม่เดาอันดับความนิยม
  - แสดงเฉพาะรายการเกมที่ยืนยันได้แทน

ปรับ engine:

- ถ้า deterministic no-answer มี confidence >= 0.90 จะไม่ให้ `experimental_rag_fallback` ข้ามไป RAG ต่อ
- ป้องกันคำตอบ policy/no-answer ที่มั่นใจสูงถูก RAG ทับด้วยข้อมูลใกล้เคียงผิดบริบท

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20 โดยเปิด `experimental_rag_fallback=True`:

- `เกมไหนคนเล่ยมากที่สุด`
  - normalized: `เกมไหนคนเล่นมากที่สุด`
  - mode: `pipeline:games_popularity_no_answer_fast_path`
- `เกมไหนคนเล่นเยอะที่สุด`
  - mode: `pipeline:games_popularity_no_answer_fast_path`
- `เกมยอดนิยมคือเกมอะไร`
  - mode: `pipeline:games_popularity_no_answer_fast_path`
- `มีเกมอะไรให้เล่นบ้าง`
  - ยังตอบ catalog ปกติด้วย `pipeline:games_catalog_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง
