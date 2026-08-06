# Current State And Recent Work

สรุปสถานะล่าสุดจนถึง 2026-07-23

## ทิศทางล่าสุด

ผู้ใช้ตัดสินใจว่า:

- ไม่ deploy ลง Vercel ตอนนี้
- ไม่ต้องยุ่ง git
- ใช้ local chatbot/local LLM เป็นหลัก
- ต้องพัฒนาให้ใกล้ chatbot จริงขึ้น:
  - จำบริบทใน session
  - เข้าใจคำถามต่อเนื่อง
  - รองรับ typo/ภาษาวิบัติ/ทับศัพท์
  - ใช้ LLM ให้เป็นประโยชน์มากขึ้น โดยไม่ให้ hallucinate

## Local Chat / Notebook

มี local terminal chat:

```text
start_local_ai_chat.ps1
tools\local_ai_chat.py
```

มี notebook สำหรับถามลอง:

```text
notebooks\04_local_hybrid_chat_debug.ipynb
```

ความสามารถ:

- มี `SESSION_ID`
- เก็บ history ใน session
- มี log ต่อ session
- มี trace/mode/source_type
- เปิด/ปิด LLM, tool router, composer, RAG fallback ได้

## Model ปัจจุบัน

default local model:

```text
qwen2.5:3b
```

เหตุผล:

- เร็วกว่า qwen3:4b ในงาน intent/general สั้น ๆ
- qwen3:4b เคยมีปัญหา thinking ยาวแล้ว final response ว่างเมื่อ `num_predict` ไม่พอ

Typhoon:

- ผู้ใช้สนใจ `supachai/llama-3-typhoon-v1.5:8b-instruct`
- ยังไม่ได้ย้ายระบบไปใช้เป็น default
- น่าทดลองในอนาคตเพื่อเทียบคุณภาพภาษาไทยกับ Qwen2.5

## Adaptive Intent LLM

ทำแล้ว:

- เปิด adaptive intent review เป็น default เมื่อ allow LLM
- exact/strong route ข้าม LLM
- broad/ambiguous route ให้ Intent LLM review
- เพิ่ม trace `intent_candidates`
- ใช้ candidate/policy filtering ก่อนเลือกเส้นทาง

ผล eval ล่าสุด:

```text
Adaptive intent eval: 8/8 ผ่าน
```

รายงาน:

```text
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.json
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.csv
```

## Real Usage Eval

สร้างชุดคำถามใช้งานจริงแล้ว:

```text
tools\generate_real_usage_eval_cases.py
```

ผลล่าสุด:

```text
Routing real usage: 115/115 ผ่าน
Answer quality: 26/26 ผ่าน
```

รายงาน:

```text
reports\routing_eval\routing_eval_20260723_000249.json
reports\routing_eval\routing_eval_20260723_000249.csv
reports\answer_quality_eval\answer_quality_eval_20260722_235928.json
reports\answer_quality_eval\answer_quality_eval_20260722_235928.csv
```

## Game Title Typo / ภาษาวิบัติ

งานล่าสุด:

- แก้ `เกม คอลออฟดูตี้` ไม่เจอข้อมูล
- ทำให้ `คอลออฟดูตี้` เข้า broad family `Call of Duty`
- ตอบรวม:
  - `Call of Duty: Modern Warfare III`
  - `Call of Duty: Warzone`
- เพิ่ม fuzzy ภาษาไทยใน `game_title_correction.py`
- เพิ่ม family `Overcooked`
- ลด false positive ของ `คอลออฟ` ที่เคยชน `Horizon Call of the Mountain`
- normalize typo ของเลขโรมัน เช่น `Part OI`, `Part ll`, `Part 2` -> `Part II`
- กันไม่ให้ alias จาก control facts ที่เป็นประโยคปุ่มยาว ๆ เข้า title correction index

ผลล่าสุด:

```text
Game title fuzzy eval: 44/44 ผ่าน
```

รายงาน:

```text
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.json
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.csv
```

## Members

มีข้อมูล members จากหน้าเว็บ:

```text
data\curated\member_profiles.jsonl
```

หมวดหลัก:

- Members
- cooperative education and Internship student
- PSU Phuket Esports Club - PSU Phuket

ระบบควรตอบได้:

- สมาชิกทั้งหมดมีกี่คน
- มีกี่หมวด
- แต่ละหมวดมีใครบ้าง
- ใครเป็นตำแหน่งอะไร
- ตำแหน่งนี้ใครทำ

ข้อควรระวัง:

- คำถาม `ตอนนี้สตาฟมีใครบ้าง` เคยไปตอบจำนวนเกม ต้องกัน routing ผิดหมวด
- คำตอบที่ยาวต้องไม่ตัดด้วย `...` ถ้าผู้ใช้ต้องการครบ

## Games

ข้อมูลเกมอยู่หลายไฟล์:

```text
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\game_title_aliases.jsonl
data\curated\game_control_facts.jsonl
```

ระบบ structured ล่าสุดอ่านได้ประมาณ 44 game rows/entries รวมรายการที่เป็นภาค/กลุ่ม/รีมาสเตอร์บางรายการ

มี legacy บางจุดที่ยังพูดว่า 36 เกมจาก fast path เก่า ต้องระวังและควร align ในอนาคต

สิ่งที่ควรตอบได้:

- เกมทั้งหมดมีอะไรบ้าง
- PS5 มีเกมอะไรบ้าง
- Nintendo มีเกมอะไรบ้าง
- PC มีเกมอะไรบ้าง
- VR มีเกมอะไรบ้าง
- เกมนี้คืออะไร
- เกมนี้เล่นยังไง
- เกมนี้มีปุ่มอะไรบ้าง
- เกมตระกูล Mario / Resident Evil / Call of Duty / Overcooked มีอะไรบ้าง

## Game Controls

ข้อมูลปุ่มควบคุมมาจาก:

```text
data\control_game
data\control_game_split\ps5
data\control_game_split\nintendo
data\curated\game_control_facts.jsonl
```

สิ่งที่ผู้ใช้ต้องการ:

- ถ้าถามปุ่มของเกม ให้ตอบทุกปุ่มที่มีในข้อมูล
- ไม่ตอบแค่ 3-5 ปุ่มถ้าไฟล์มีครบ
- แยก platform ถ้ามีหลาย platform
- ถ้าไม่มีข้อมูลปุ่ม ให้บอกว่าไม่พบข้อมูลปุ่มที่ยืนยันได้

## Formatting

งานก่อนหน้าแก้เรื่อง format ไปแล้ว:

- bullet เป็น `•`
- แยกหัวข้อชัดเจน
- อุปกรณ์ตอบเป็นหมวด zone
- เกมควรตอบเป็นหมวด/zone/family ตามคำถาม
- ราคา/ข้อมูลแถวควรปรับเป็น bullet ให้อ่านง่าย

ยังต้องระวัง:

- บางคำตอบจาก fast path อาจยังเป็นแถวหรือ paragraph ยาว
- ถ้าพบให้ปรับ formatter/answer function ให้เป็นรูปแบบเดียวกัน

