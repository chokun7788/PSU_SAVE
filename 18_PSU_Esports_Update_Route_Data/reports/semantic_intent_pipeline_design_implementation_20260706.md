# Semantic Intent Pipeline Design / Implementation - 2026-07-06

## เป้าหมาย

แก้ปัญหาระบบต้องเพิ่ม alias หรือคำผิดทีละคำ เช่น `รายกาา`, `รายกาน`, `แข่งมเกม` ซึ่งไม่เหมาะกับการใช้งานจริง เพราะผู้ใช้สามารถพิมพ์คำเพี้ยนหรือใช้สำนวนใหม่ได้ตลอด

แนวทางใหม่คือเพิ่มชั้น `semantic intent matching` เพื่อจับว่า "คำถามนี้หมายถึง intent อะไร" ก่อนค่อยเลือก rulebase/RAG/source ที่ถูกต้อง

## Pipeline ที่ต้องการ

```text
User question
-> Preprocess / light normalization
-> High-confidence exact rules
-> Semantic intent matching
-> Route + source scope
-> Deterministic fast answer หรือ scoped RAG
-> Answer formatter
-> Validator / guard
-> Answer-first response หรือ no-answer
```

## Stage 1: Preprocess / Light Normalization

ไฟล์หลัก:

- `app/core/normalization.py`
- `app/pipeline/preprocess.py`

หน้าที่:

- lower-case ภาษาอังกฤษ
- normalize คำย่อและคำผิดที่พบบ่อย
- normalize เลขไทยเป็นเลขอารบิก
- normalize domain term สำคัญ เช่น `นศ.` -> `นักศึกษา`
- ไม่พยายามแก้ภาษาไทยทุกคำ เพราะเสี่ยงแก้ชื่อเกมหรือศัพท์เฉพาะผิด

หลักสำคัญ:

- normalization เป็นแค่ชั้นช่วย ไม่ใช่แกนหลัก
- ไม่ควรเพิ่ม alias ไม่รู้จบ
- คำ domain เช่น `RoV`, `CS2`, `TEKKEN`, `PS5`, `VR`, `PC` ต้องไม่ถูกแก้มั่ว

## Stage 2: High-confidence Exact Rules

ไฟล์หลัก:

- `app/pipeline/router.py`
- `app/runtime/fast_answer.py`
- `data/rules/*.jsonl`

หน้าที่:

- ให้ rulebase เดิมที่มั่นใจสูงทำงานก่อน
- ใช้กับคำตอบที่ต้องแม่น เช่น ราคา, เวลาเปิด, วิธีจอง, รายการเกม, รายการแข่ง, กฎพื้นที่

เหตุผล:

- Rulebase เร็วและคุมคำตอบได้
- ข้อมูลสำคัญต้องไม่ให้ LLM หรือ RAG เดาเอง
- ถ้า exact rule จับได้ชัด ให้ตอบทันที

## Stage 3: Semantic Intent Matching

ไฟล์ที่เพิ่ม:

- `app/pipeline/semantic_intent.py`
- `data/intent/semantic_intents.jsonl`

หลักการ:

- ไม่จับคำเป๊ะ
- ไม่ list คำผิดทุกคำ
- เก็บ "ตัวอย่างคำถามหลายสไตล์" ต่อ intent
- เทียบคำถามผู้ใช้กับตัวอย่างใน catalog
- ถ้าคะแนนถึง threshold และห่างจากอันดับสองพอ จึงเลือก intent

ตัวอย่าง intent:

- `competition_game_list`
- `competition_rules_lookup`
- `competition_prize_unknown`
- `game_availability_lookup`
- `equipment_game_catalog`
- `equipment_lookup`
- `service_fee_query`
- `schedule_query`
- `booking_policy`
- `studio_rules`
- `contact_lookup`
- `related_guidance`

ตัวอย่างการจับ:

```text
รายกานแข่งขันมีอะไรบ้าง
-> competition_game_list

ตอนนี้มีทัวร์เกมไรบ้าง
-> competition_game_list

อยากเล่น Tekken 8
-> game_availability_lookup

ไม่มีบัตรนักศึกษาทำยังไงตอนจอง
-> booking_policy
```

## วิธี match ตอนนี้

เพื่อไม่ให้ production พึ่งโมเดลใหญ่หรือ API ภายนอกทันที ตอนนี้ใช้ `local_char_ngram_semantic_intent`

วิธีนี้:

- ตัดช่องว่าง/สัญลักษณ์ออก
- สร้าง character n-gram ขนาด 2-4
- คำนวณ cosine similarity ระหว่างคำถามกับตัวอย่าง intent
- ใช้ `min_confidence` และ `min_margin` กันการเดาสุ่ม

ข้อดี:

- เร็ว
- ไม่มีค่า API
- ไม่ต้องโหลดโมเดลหนักบน Vercel
- เหมาะกับภาษาไทยที่มักไม่มีเว้นวรรค
- ทน typo ระดับหนึ่ง เช่น `รายกานแข่งขัน`

ข้อจำกัด:

- ยังไม่ใช่ semantic embedding model จริง
- ถ้าสำนวนต่างมากเกินไป ต้องเพิ่มตัวอย่าง intent เพิ่ม
- ไม่ควรใช้แทน RAG หรือ validator

## ตำแหน่งใน Router

ใน `app/pipeline/router.py` semantic intent ถูกวางหลัง rule เฉพาะที่มั่นใจสูง เช่น:

- equipment item
- equipment game catalog
- student fee
- PC availability
- schedule
- competition game list
- game availability
- competition rule/prize
- game detail

แล้วจึงใช้ semantic ก่อน route กว้าง ๆ เช่น news/general/games lookup

เหตุผล:

- ไม่ให้ semantic ไปทับ exact rule ที่ถูกอยู่แล้ว
- ลดปัญหาคำถามหลุดไป `events_news/news_lookup`
- ลดปัญหา RAG หยิบ context คนละหมวด

## Stage 4: Route + Source Scope

หลังรู้ intent แล้ว route ต้องกำหนด source ที่ค้นได้:

```text
competition_game_list -> data/competition_rules
competition_rules_lookup -> competition_rules
game_availability_lookup -> our-games
equipment_game_catalog -> our-games/equipment
service_fee_query -> service fee data
schedule_query -> calendar/service hours
booking_policy -> reservation rules
studio_rules -> studio rules
```

หลักสำคัญ:

- RAG ต้องถูกจำกัด source ตาม intent
- ไม่ควรค้นทั้งฐานข้อมูลแบบกว้าง ๆ โดยไม่มี scope
- ถ้า context ไม่ตรง intent ให้ no-answer หรือถามเพิ่ม

## Stage 5: Deterministic Fast Answer

ไฟล์ที่แก้:

- `app/pipeline/engine.py`

ปรับเพิ่ม:

- ถ้า route เป็น `games/competition_game_list` จาก semantic intent ให้ตอบด้วย `COMPETITION_GAME_SUMMARY` โดยตรง
- ไม่ปล่อยให้ตกไป curated RAG กว้าง ๆ

เหตุผล:

- เคส `ตอนนี้มีทัวร์เกมไรบ้าง` semantic จับ intent ถูกแล้ว
- แต่ fast answer เดิมยังดู keyword ใน query เดิม
- จึงต้องให้ engine เชื่อ route.intent ด้วย

## Stage 6: Scoped RAG

ถ้า fast answer ไม่มีคำตอบ:

- ใช้ route.category เพื่อเลือกฐานข้อมูล
- retrieve เฉพาะข้อมูลในหมวดนั้น
- ต้องมี confidence gate
- ถ้าข้อมูลไม่ชัด ไม่ควรตอบเดา

ตัวอย่างปัญหาเดิม:

```text
ถาม: มีคอมให้เล่นไหม
ผิด: ไปดึงกติกา VALORANT
```

แนวใหม่:

```text
semantic intent -> equipment / pc_availability
source scope -> equipment/service data
ไม่ค้น competition_rules
```

## Stage 7: Answer Formatting

นโยบายคำตอบ:

- answer-first
- ตอบประเด็นก่อน
- ตามด้วยรายละเอียดเท่าที่จำเป็น
- ใส่แหล่งข้อมูล
- ถ้าเป็น rulebase/fast path ห้ามบอกว่าใช้ LLM
- ถ้าไม่มีข้อมูลจริง ให้ no-answer สุภาพ

## Stage 8: Validation / Guard

หลังสร้างคำตอบ:

- ตรวจ source
- ตรวจ no-answer policy
- ตรวจว่า route กับคำตอบสอดคล้องกัน
- ตรวจว่าไม่ได้อ้างข้อมูลที่ไม่มีจริง

ห้าม:

- แก้ validator ให้ผ่านง่าย
- ให้ LLM เดาข้อมูลราคา/เวลา/กติกา
- ตอบข่าวเมื่อผู้ใช้ถามรายการแข่งปัจจุบัน

## Stage 9: Feedback Loop

เมื่อเจอคำถามผิด:

1. ดู `route/mode/source`
2. ถ้า route ผิด ให้เพิ่มตัวอย่างใน `data/intent/semantic_intents.jsonl`
3. ถ้า route ถูกแต่ตอบผิด ให้แก้ fast answer/RAG/source scope
4. ถ้าไม่มีข้อมูลจริง ให้เพิ่ม fact card หรือ no-answer rule
5. run compile + smoke เฉพาะจุด
6. ไม่ต้อง run Ground Truth ทุกครั้ง เว้นแต่ผู้ใช้สั่ง

## ผลทดสอบ Smoke

ทดสอบจากไฟล์ UTF-8 ชุดเล็กในโฟลเดอร์ 20:

```text
รายกานแข่งขันมีอะไรบ้าง -> games/competition_game_list -> competition_game_list_fast_path
ตอนนี้มีทัวร์เกมไรบ้าง -> games/competition_game_list -> competition_game_list_fast_path
อยากเล่น Tekken 8 -> games/game_availability_lookup -> games_availability_fast_path
เล่น Mario ได้ไหม -> games/game_availability_lookup -> games_family_availability_fast_path
ใช้บัตรนักศึกษาเล่นฟรีไหม -> service_fee/service_fee_query -> deterministic_calculator_fast
ไม่มีบัตรนักศึกษาทำยังไงตอนจอง -> reservation/booking_policy -> booking_identity_fast_path
เอาของกินเข้าไปได้ไหม -> rules/studio_rules -> rules_fast_path
วันนี้เปิดไหม -> schedule/schedule_query -> calendar_schedule_fast_path
RoV แข่งชนะได้เงินเท่าไหร่ -> no_answer/competition_prize_unknown -> category_rule_fast_path
```

Compile:

```text
python -m compileall app
```

ผ่านทั้งโฟลเดอร์ 18 และ 20

ไม่ได้ run Ground Truth ตามคำสั่งผู้ใช้

## ไฟล์ที่เพิ่ม/แก้

เพิ่ม:

- `app/pipeline/semantic_intent.py`
- `data/intent/semantic_intents.jsonl`

แก้:

- `app/pipeline/router.py`
- `app/pipeline/engine.py`

sync ไปโฟลเดอร์ deploy 20 แล้ว:

- `20_PSU_Esports_Vercel_Deploy/app/pipeline/semantic_intent.py`
- `20_PSU_Esports_Vercel_Deploy/data/intent/semantic_intents.jsonl`
- `20_PSU_Esports_Vercel_Deploy/app/pipeline/router.py`
- `20_PSU_Esports_Vercel_Deploy/app/pipeline/engine.py`

## ขั้นต่อไปถ้าจะใช้ Embedding จริง

โครงนี้พร้อมต่อ embedding model จริงได้ โดยเปลี่ยนเฉพาะ implementation ใน `semantic_intent.py`

แนวทาง:

- สร้าง embedding ให้ตัวอย่างใน `semantic_intents.jsonl`
- cache embedding ไว้ ไม่ embed ใหม่ทุก request
- embed query ผู้ใช้
- cosine similarity กับ intent examples
- ใช้ threshold/margin แบบเดิม
- fallback เป็น local char n-gram ถ้า API/model ใช้ไม่ได้

ยังไม่เปิด embedding API ตอนนี้ เพราะต้องตัดสินใจเรื่อง:

- provider/model
- API key
- latency
- cost
- cache strategy
- Vercel cold start

## สถานะ

- semantic intent pipeline รุ่นแรก implement แล้ว
- ทำงานใน 18 และ sync ไป 20 แล้ว
- 20 พร้อมให้ผู้ใช้ deploy เอง
- ยังไม่ได้ deploy production
