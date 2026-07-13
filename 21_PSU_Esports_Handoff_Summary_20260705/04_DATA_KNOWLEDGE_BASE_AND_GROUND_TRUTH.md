# Data, Knowledge Base และ Ground Truth

ไฟล์นี้สรุปฐานข้อมูลที่ระบบใช้ตอบคำถาม และชุดทดสอบที่ใช้วัดคุณภาพ

## แนวคิดข้อมูลของระบบ

ระบบไม่ได้ให้ LLM เดาข้อมูลเอง แต่ใช้ data ที่จัดหมวดไว้ เช่น:

- Rulebase JSONL
- Curated facts JSONL
- Service fee table ใน code/calculator
- Calendar closures JSONL
- Competition rule chunks/fact cards
- Game details
- Equipment details
- Ground Truth สำหรับทดสอบ

คำตอบควรยึดหลัก:

```text
ถ้าไม่มีข้อมูลจริง -> ตอบว่าไม่พบข้อมูลที่ยืนยันได้
ถ้ามีข้อมูลจริง -> ตอบคำตอบก่อน แล้วค่อยรายละเอียด/แหล่งข้อมูล
ถ้าข้อมูลมีหลายกลุ่ม เช่น ราคา -> อย่าเดา ถามกลับหรือแสดงทุกกลุ่ม
```

## Curated Facts

ไฟล์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\curated\curated_facts.jsonl
```

จำนวน:

```text
42 rows
```

คีย์หลัก:

```text
id, category, title, text, source_url, tags, priority
```

ใช้สำหรับ:

- ข้อมูล overview
- contact
- rules
- booking
- payment
- schedule
- knowledge
- facts ที่ไม่อยากเขียน hardcode ทั้งหมด

## Rulebase

โฟลเดอร์:

```text
data\rules
```

ไฟล์หลัก:

```text
contact_rules.jsonl
equipment_rules.jsonl
games_rules.jsonl
misc_rules.jsonl
no_answer_rules.jsonl
overview_rules.jsonl
penalty_rules.jsonl
reservation_rules.jsonl
```

ตัวอย่างจำนวน:

- `reservation_rules.jsonl`: 26 rules
- `games_rules.jsonl`: 10 rules
- `equipment_rules.jsonl`: 1 rule

ใช้สำหรับ:

- คำถามที่ pattern ชัดและคำตอบแน่นอน
- คำถาม FAQ ซ้ำ ๆ
- คำถามที่ควรตอบเร็วและไม่ต้องให้ LLM เรียบเรียง

ข้อควรระวัง:

- ถ้าใส่ rule กว้างเกิน จะลากคำถามผิดหมวด
- ถ้าใส่ rule แคบเกิน จะตอบไม่ได้เมื่อผู้ใช้พิมพ์คนละรูปแบบ
- ควรมี synonym/alias เฉพาะ entity เช่น PSU, มอ, นักศึกษา, student

## Service Fee

ข้อมูลราคาอยู่ใน code/calculator และ fast runtime ไม่ได้เป็น JSONL เพียงอย่างเดียว

ไฟล์สำคัญ:

```text
app\calculator\service_fee.py
app\runtime\fast_answer.py
```

ข้อมูลราคาอ้างจากภาพ Service Fee 2026:

```text
https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

บริการ:

- PlayStation 5 - 1 HR, 1-2 persons
- Nintendo Switch - 1 HR, 1-2 persons
- Nintendo Switch - 1 HR, 3-4 persons
- Cockpit - 1 HR, 1 person
- VR - 30 MINS, 1-5 persons
- VR - 1 HR, 1-5 persons

กลุ่มราคา:

- PSU Student and Staff: ฟรี
- PSU Alumni and General Student: ราคากลาง
- General Adult: ราคาสูง

ข้อกำหนดการตอบราคา:

- ตอบราคาไว้บรรทัดแรก
- ถ้ารู้กลุ่มผู้ใช้ ให้ตอบกลุ่มนั้นก่อน
- ถ้าไม่รู้กลุ่มผู้ใช้ ให้แสดงทุกกลุ่ม
- ถ้าเป็นนักศึกษาต่างมหาวิทยาลัย ให้ใช้ General Student
- ถ้าเป็นนักศึกษา/เด็ก/นักเรียน มอ ให้ใช้ PSU Student and Staff
- ถ้าเป็นบุคคลทั่วไป ให้ใช้ General Adult

## Calendar และวันปิดพิเศษ

ไฟล์:

```text
data\calendar\service_closures.jsonl
app\calendar\service_calendar.py
```

ใช้ตอบคำถาม:

- วันนี้เปิดไหม
- พรุ่งนี้เปิดไหม
- วันไหนหยุดบ้างเดือนนี้
- 28 กรกฎาคมเปิดไหม
- 30/7/2026 ศูนย์เปิดไหม

timezone:

```text
Asia/Bangkok
```

วันปิดพิเศษที่เคยเพิ่ม:

```text
28-30 กรกฎาคม 2026
```

หมายเหตุ:

- ตอนนี้เป็น manual config ไม่ได้ดึง API วันหยุดราชการอัตโนมัติทุกครั้ง
- ถ้าจะ production จริง ควรเชื่อม API วันหยุดไทยหรือให้เจ้าหน้าที่แก้ไฟล์ closure ได้

## Competition Rules

ไฟล์ต้นทางมาจาก `.txt` กติกาการแข่งขัน 4 รายการ

เกม/รายการ:

- Counter-Strike 2: PSU Phuket CS2 2026 Tournament
- VALORANT: PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย
- Tekken 8: PSU Esports ปะทะมันส์ สนั่นจอ

Output JSONL:

```text
data\competition_rules\competition_rule_documents.jsonl
data\competition_rules\competition_rule_chunks.jsonl
data\curated\curated_competition_rules.jsonl
data\competition_rules\competition_rule_fact_cards.jsonl
```

จำนวนล่าสุด:

- documents: 4
- chunks: 104
- curated competition rules: 104
- fact cards หลัก: 19

ใช้ตอบคำถาม:

- สมาชิกทีมมีกี่คน
- มาสายกี่นาทีโดนอะไร
- pause ได้กี่ครั้ง
- แข่งกี่ map
- Tekken เป็น FT อะไร
- Valorant ใช้ map pool อะไร
- RoV ใช้กติกาอะไร
- CS2 ใช้ overtime ไหม

ข้อกำหนดการตอบ:

- ตอบคำตอบก่อน
- ใส่หลักฐานจากกติกา
- ใส่ชื่อเกม/รายการ
- ใส่ source เป็น local competition rules
- ถ้าไม่พบในกติกา ไม่ควรเดา

## Game Details

ไฟล์:

```text
data\curated\game_item_details.jsonl
```

จำนวน:

```text
36 rows
```

ข้อมูลใช้ตอบ:

- เกมนี้คืออะไร
- เล่นยังไง
- อยู่โซนไหน
- เป็นแนวเกมอะไร
- มีเกมนี้ในศูนย์ไหม

ตัวอย่างเกม:

- VALORANT
- Counter-Strike 2
- PUBG: BATTLEGROUNDS
- Call of Duty: Warzone
- League of Legends
- TEKKEN 8
- Beat Saber
- Horizon Call of the Mountain
- Gran Turismo 7
- Mario Kart 8 Deluxe
- Overcooked 2
- Super Smash Bros Ultimate
- Nintendo Switch Sports
- Marvel's Spider-Man 2
- God of War Ragnarok

หมายเหตุ:

- ถามเกมที่ไม่มี เช่น Minecraft/Roblox ให้ตอบว่าไม่พบในรายการเกมที่ยืนยันได้
- อย่าดึง schedule หรือ competition rule มาตอบแทน

## Equipment Details

ไฟล์:

```text
data\curated\equipment_item_details.jsonl
```

จำนวน:

```text
16 rows
```

ใช้ตอบ:

- Sony PlayStation VR2 คืออะไร
- Logitech G923 ใช้ทำอะไร
- Cockpit คืออะไร
- VR Zone เล่นยังไง
- PC Zone มีอุปกรณ์อะไรบ้าง
- Nintendo Switch มีเกมอะไรบ้าง

ข้อมูลที่เพิ่ม:

- Gaming PC MSI MAG Infinite S3 14th
- Gaming Monitor
- Gaming Chair
- Gaming Keyboard
- Gaming Mouse
- Gaming Headset
- PlayStation 5 Slim
- Sony PlayStation VR2
- Nintendo Switch OLED
- Logitech G923
- Driving Force Shifter
- Racezone Full Cockpit V3
- Pulse Elite Wireless Headset
- TV 65/86 นิ้ว
- Sofa 2 seats

## Equipment Game Catalog

เพิ่มหลังพบปัญหาคำถามอุปกรณ์มีเกมอะไรบ้าง

คำถามที่ควรรองรับ:

- อุปกรณ์เล่นเกมอะไรได้บ้าง
- อุปกรณ์มีเกมอะไรบ้าง
- เครื่องเล่นอะไรได้บ้าง
- PC Zone เล่นเกมอะไรได้บ้าง
- Cockpit มีเกมอะไรบ้าง
- VR มีเกมอะไรบ้าง
- PS5 มีเกมอะไรบ้าง
- Nintendo Switch มีเกมอะไรบ้าง

ข้อมูลตอบ:

- PC Zone: VALORANT, Counter-Strike 2, PUBG, Warzone, TEKKEN 8, League of Legends
- PlayStation 5 Zone: Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกม PS5 อื่น ๆ ในรายการ
- Nintendo Switch Zone: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Switch อื่น ๆ ในรายการ
- Cockpit Zone: Gran Turismo 7
- VR Zone: Beat Saber, Horizon Call of the Mountain

Source:

```text
https://esports.phuket.psu.ac.th/Services/our-games
```

## Ground Truth

### GT360

ไฟล์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl
```

จำนวน:

```text
360 questions
```

หมวด:

- service_fee
- schedule
- reservation
- rules
- games
- equipment
- penalty
- contact
- knowledge
- overview
- events_news
- no_answer

ผลล่าสุด:

```text
360/360 PASS
```

Report:

```text
reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
```

### Competition Ground Truth v1

ไฟล์:

```text
data\ground_truth\ground_truth_competition_rules_v1_228.jsonl
```

จำนวน:

```text
228 questions
```

ใช้ตอนแรกสำหรับคำถามกติกาการแข่งขัน

### Competition by Game v2

โฟลเดอร์:

```text
data\ground_truth\competition_by_game_v2
```

ไฟล์:

```text
ground_truth_competition_all_games_v2_diverse.jsonl
ground_truth_competition_cs2_v2_diverse.jsonl
ground_truth_competition_rov_v2_diverse.jsonl
ground_truth_competition_tekken8_v2_diverse.jsonl
ground_truth_competition_valorant_v2_diverse.jsonl
```

ทำไว้เพื่อแยกเกมและทำคำถามหลากหลายขึ้น

### Competition Challenger v2

ไฟล์:

```text
data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl
```

จำนวน:

```text
369 questions
```

จุดประสงค์:

- คำถามแบบคนแข่งจริง
- คำถามแปลกกว่า pattern เดิม
- ทดสอบว่า route ไม่หลุดไปเกม/อุปกรณ์/schedule

ผลล่าสุด:

```text
369/369 PASS
```

Report:

```text
reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
```

## หลักการเพิ่มข้อมูลใหม่

ถ้าเป็นข้อมูล FAQ ตายตัว:

1. เพิ่มใน `data/rules/*.jsonl` หรือ `app/runtime/fast_answer.py`
2. เพิ่ม synonym/alias ใน normalization/router ถ้าจำเป็น
3. เพิ่ม ground truth
4. รัน test

ถ้าเป็นข้อมูลอธิบายยาว:

1. เพิ่มใน `data/curated/*.jsonl`
2. ทำ retrieval ให้เข้าหมวดถูก
3. เพิ่ม expected source keyword
4. ทดสอบคำถามหลายรูปแบบ

ถ้าเป็นกติกาแข่ง:

1. เพิ่มไฟล์ต้นทาง
2. รัน `tools\convert_competition_rules.py`
3. สร้างหรือแก้ fact cards
4. เพิ่ม ground truth แยกเกม
5. รัน competition challenger

ถ้าเป็นวันหยุด:

1. เพิ่มใน `data/calendar/service_closures.jsonl`
2. ทดสอบวันนี้/วันนั้น/เดือนนี้

