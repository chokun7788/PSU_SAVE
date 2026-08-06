# Game Title Fuzzy Correction - 2026-07-21

## ปัญหาที่เจอ

- ผู้ใช้พิมพ์ชื่อเกมผิดเล็กน้อย เช่น `tekkrn8` แต่ระบบตอบว่าไม่พบข้อมูล ทั้งที่ควรโยงไปหา `TEKKEN 8`
- ระบบเดิมแก้ได้เฉพาะ alias ที่เขียนไว้ตรง ๆ ทำให้ต้องเพิ่มคำผิดทีละคำ ซึ่งขยายต่อยากและไม่ครอบคลุมทุกเกม
- เคสตระกูลเกม เช่น `Mario` มี fast path family answer แย่งตอบก่อนชื่อเกมเต็ม ทำให้ typo ที่ถูกแก้เป็น `Mario Kart 8 Deluxe` ยังตอบเป็นกลุ่ม Mario ได้

## สิ่งที่แก้

- เพิ่ม `app/pipeline/game_title_correction.py`
  - อ่านชื่อเกมและ aliases จากข้อมูล curated หลายแหล่ง:
    - `game_title_aliases.jsonl`
    - `game_item_details.jsonl`
    - `our_games_scraped_details.jsonl`
    - `game_control_facts.jsonl`
  - ใช้ fuzzy matching ระดับ token/window เพื่อสร้าง correction จากชื่อเกมที่มีจริงในฐาน
  - ไม่ต้องเพิ่ม alias ทีละเคส เช่น `tekkrn8`, `valornat`, `fortnte`, `overcookd 2`
- ปรับ `app/pipeline/preprocess.py`
  - ถ้า fuzzy correction มั่นใจสูง จะใช้คำถามที่แก้ชื่อเกมแล้วเป็น active query ทันที
  - ยังเก็บ query เดิมไว้ใน `query_variants` เพื่อ debug/trace
- ปรับ `app/runtime/fast_answer.py`
  - ถ้าคำถามมีชื่อเกมเต็มที่ยืนยันได้แล้ว เช่น `Mario Kart 8 Deluxe` จะไม่ให้ family answer ของ `Mario` แย่งตอบ
- เพิ่ม `tests/smoke_test_game_title_typo_correction.py`
  - ล็อก regression สำหรับ typo หลายเกมและเคส family-vs-specific game

## อัปเดตเพิ่มเติม: Broad / Family Title Typo

- เพิ่ม canonical broad title สำหรับ franchise/family ที่มีหลายเกม เช่น `Mario`, `Resident Evil`, `Call of Duty`
- จุดประสงค์คือไม่ให้ typo คำกว้าง เช่น `msrio` หรือ `mqrio` ถูกเดาเป็นเกมภาคใดภาคหนึ่งทันที
- Flow ใหม่:
  - `msrio มีข้อมูลไหม` -> normalize เป็น `Mario มีข้อมูลไหม` -> family answer แสดงเกมกลุ่ม Mario ทั้งหมด
  - `mqrio มีข้อมูลไหม` -> normalize เป็น `Mario มีข้อมูลไหม` -> family answer
  - `mqrio kart มีข้อมูลไหม` -> normalize เป็น `Mario Kart 8 Deluxe มีข้อมูลไหม` -> specific game answer
- ปรับ threshold สำหรับ alias สั้นประมาณ 5-6 ตัวให้ยืดหยุ่นขึ้น แต่เพิ่ม shape guard ว่าต้องมีรูปคำใกล้จริง เช่นตัวแรกตรงกัน และท้ายคำ/ prefix / digit shape ต้องพอสัมพันธ์กัน
- เพิ่ม negative guard เช่น `music มีข้อมูลไหม` ต้องไม่ถูกแก้เป็นชื่อเกม

## อัปเดตเพิ่มเติม: Typo Candidate Layer จาก `typo.md`

- อ่านแนวทางจาก `C:\Users\Chokhun\Downloads\Learn-LLM\typo.md` แล้วเลือกหยิบส่วนที่เหมาะกับระบบตอนนี้ที่สุดก่อน คือชั้น candidate resolver ก่อนเข้า fast/rule/RAG
- เพิ่ม scoring แบบผสมใน `app/pipeline/game_title_correction.py`
  - `SequenceMatcher` เดิมสำหรับคำที่ใกล้กันตรง ๆ
  - character n-gram score สำหรับคำที่สลับตัวอักษร/ติดกัน/ตกบางตัว เช่น `mariokrt 8`
  - delete lookup คล้าย SymSpell สำหรับคำที่มีตัวอักษรขาด/เกิน เช่น `valrant`, `overcookd2`
- ยังไม่ใช้ LLM query rewriting เป็นตัวหลักในขั้นนี้ เพราะถ้าให้ LLM แก้ชื่อเกมก่อนตรวจฐานข้อมูล มีโอกาส hallucinate ชื่อเกมที่ไม่มีในระบบได้
- เพิ่มตัวกรอง alias จาก `game_control_facts.jsonl` เพราะไฟล์ control มี alias ของปุ่ม/คำสั่งปนอยู่ เช่น `Accelerate`, `Steer`; ถ้าเอาไป fuzzy ทั้งหมดจะเสี่ยงจับคำทั่วไปเป็นเกมผิด
- เพิ่มการแยก broad vs specific title:
  - `resdent evil มีข้อมูลไหม` -> `Resident Evil`
  - `resdent evil 4 มีข้อมูลไหม` -> `Resident Evil 4`
  - `call of dutty มีข้อมูลไหม` -> `Call of Duty`
  - `call of dutty warzone มีข้อมูลไหม` -> `Call of Duty: Warzone`

## อัปเดตเพิ่มเติม: Stress Test ไทย/อังกฤษ

- ทดสอบคำถาม typo ทั้งอังกฤษและไทยแบบแปลก ๆ แล้วแก้เพิ่ม 3 จุด:
  - `mariokrt 8` เดิมแก้เป็น `Mario Kart 8 Deluxe 8` เพราะเลือก token window สั้นเกินไป ตอนนี้แก้ให้เลือก window ที่ครอบคลุมกว่าเมื่อเป็นเกมเดียวกัน
  - `มาริโอคาท 8` และ `มาริโอคาส` เดิมหล่นไปตอบ family `Mario` ตอนนี้ให้ alias เฉพาะของ `Mario Kart 8 Deluxe` ชนะ family answer
  - `Resident Evil` ที่สะกดถูกอยู่แล้วเดิมอาจถูกดันเป็น `Resident Evil 4` ตอนนี้ล็อก exact broad title ให้ยังตอบเป็น family
- เพิ่ม known game alias signal ใน `app/pipeline/universal_intent.py`
  - ถ้าคำถามมี alias เกมจาก curated data เช่น `แกรนทัวลิสโม่ 7 เล่นยังไง` จะถือว่าเป็น domain `games` แม้ไม่มีคำว่า `เกม` อยู่ในประโยค
  - ช่วยให้คำถาม “ชื่อเกม + เล่นยังไง/คืออะไร/ปุ่มอะไร” เข้า structured game tool ได้ตรงขึ้น
- เคสที่ยืนยันหลังแก้:
  - `mariokrt 8 มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
  - `มาริโอคาท 8 มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
  - `มาริโอคาส มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
  - `แกรนทัวลิสโม่ 7 เล่นยังไง` -> `Gran Turismo 7`
  - `Resident Evil มีข้อมูลไหม` -> family list ของ Resident Evil
  - `resdent evil 4 มีข้อมูลไหม` -> `Resident Evil 4`
  - `music`, `accelerate`, `ms paint` ไม่ถูกโยงเป็นเกม

## Guard ที่ใส่ไว้

- ไม่ fuzzy-match alias ที่สั้นมากหรือ ambiguous เช่น `vr`, `pc`, `lol`, `gt7`, `tk8`
- เน้น typo ภาษาอังกฤษ/romanized ก่อน เพราะ fuzzy ภาษาไทยทั้งประโยคเสี่ยงจับผิดเกม
- ถ้าคะแนนสูสีกับคนละเกมและไม่ชัดพอ จะไม่แก้เพื่อกันตอบมั่ว
- ถ้าคำถามกว้างจริง เช่น `Mario มีข้อมูลไหม` ยังให้ตอบเป็นกลุ่ม Mario ได้ตามเดิม

## ตัวอย่างที่ผ่านแล้ว

- `อยากเล่น tekkrn8 ต้องทำยังไง` -> `TEKKEN 8`
- `tekkrn8 มีปุ่มอะไรบ้าง` -> ปุ่มของ `TEKKEN 8`
- `valornat คือเกมอะไร` -> `VALORANT`
- `fortnte มีข้อมูลไหม` -> `Fortnite`
- `mario krta 8 มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
- `mariokrt 8 มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
- `msrio มีข้อมูลไหม` -> `Mario` family
- `mqrio มีข้อมูลไหม` -> `Mario` family
- `mqrio kart มีข้อมูลไหม` -> `Mario Kart 8 Deluxe`
- `valrant คือเกมอะไร` -> `VALORANT`
- `overcookd2 มีปุ่มอะไรบ้าง` -> `Overcooked 2`
- `resdent evil มีข้อมูลไหม` -> `Resident Evil` family
- `resdent evil 4 มีข้อมูลไหม` -> `Resident Evil 4`
- `call of dutty warzone มีข้อมูลไหม` -> `Call of Duty: Warzone`
- `zeldq มีข้อมูลไหม` -> `The Legend of Zelda: Breath of the Wild`
- `overcookd 2 มีปุ่มอะไรบ้าง` -> รู้ว่าเป็น `Overcooked 2` และตอบว่าไม่มีข้อมูลปุ่มที่ยืนยันได้

## ข้อจำกัดที่ยังเหลือ

- ระบบยังไม่ได้แก้ typo ภาษาไทยแบบ general เต็มรูปแบบ เพราะเสี่ยง false positive สูงกว่าอังกฤษ
- เกมชื่อสั้น/ตัวย่อสั้นมากยังต้องพึ่ง exact alias หรือ alias ที่ตั้งไว้เดิม
- fuzzy correction ช่วยเรื่องชื่อเกมก่อนเข้า pipeline แต่คำถามซับซ้อนยังต้องพึ่ง router/retrieval/composer ชั้นถัดไป
- ยังไม่ได้ทำ wrong-keyboard-layout correction และ LLM structured extraction ตาม `typo.md`; สองอย่างนี้เหมาะทำเป็นเฟสถัดไปหลังเก็บ log คำถามจริงเพิ่ม
- ตัวอย่าง wrong keyboard layout เช่น `l;ylfu` ยังไม่ถูกแปลงเป็นภาษาไทย เพราะยังไม่ได้เปิดชั้น keyboard-layout correction

## Validation

- `python -m py_compile app\pipeline\game_title_correction.py app\pipeline\preprocess.py app\runtime\fast_answer.py app\pipeline\universal_intent.py tests\smoke_test_game_title_typo_correction.py`
- `python tests\smoke_test_game_title_typo_correction.py`
- `python tests\smoke_test_game_catalog.py`
- `python tests\smoke_test_game_controls.py`
- `python tests\smoke_test_answer_validator.py`
