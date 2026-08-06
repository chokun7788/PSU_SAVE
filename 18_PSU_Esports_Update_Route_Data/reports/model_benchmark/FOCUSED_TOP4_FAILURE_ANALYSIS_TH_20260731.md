# วิเคราะห์คำตอบที่ผิดจาก Focused Top 4 Eval ณ วันที่ 31 กรกฎาคม 2026

ไฟล์นี้วิเคราะห์จากผลรันจริงใน `reports/model_benchmark/20260731_focused_top4_sample25/*/results.jsonl`

รอบทดสอบนี้มี 5 runs:

- No-LLM
- `scb10x/typhoon2.5-qwen3-4b`
- `scb10x/llama3.2-typhoon2-3b-instruct`
- `qwen3:4b`
- `qwen2.5:7b`

รวมทั้งหมด 1,680 คำตอบ จาก 336 คำถามต่อ run

## สรุปก่อน

ภาพรวมที่ผิดไม่ได้มาจาก LLM อย่างเดียว ส่วนใหญ่ผิดเพราะ routing / precondition / ambiguity gate เลือกทางผิดก่อนถึงขั้นตอบ เช่นคำถามถามเครื่องย่อย `PC #01` แต่ระบบตอบจากข้อมูลระดับ `PC Zone` หรือคำถามถามจำนวนคน แต่ระบบเข้า schedule/equipment แทน availability/capacity

ตัวเลขจากผลรัน:

- Fail rows รวม: 147
- Unique fail cases: 47
- กลุ่มที่ผิดมากสุด:
  - `availability_service`: 63 failures
  - `general_llm`: 41 failures
  - `availability_machine_split`: 20 failures
  - `policy_schedule_rules`: 10 failures
  - `ambiguity_no_answer`: 8 failures
  - `availability_game`: 5 failures

## 1. ถามเกมเฉพาะเครื่อง แต่ระบบตอบระดับโซน

### เคสที่ผิด

- `PC #01 มี Call of Duty: Warzone ไหม`
- `PC #02 มี Call of Duty: Warzone ไหม`
- `PC #03 มี TEKKEN 8 ไหม`
- `PC #10 มี TEKKEN 8 ไหม`

ทุกโมเดลและ No-LLM ผิดเหมือนกัน แปลว่าไม่ใช่ปัญหาของ LLM แต่เป็นปัญหา deterministic routing

### ระบบตอบอะไร

ระบบเข้า:

- mode: `pipeline:structured_game_detail`
- route: `games/game_availability_lookup`
- capability: `structured.games`

ตัวอย่างคำตอบที่ผิด:

- `Call of Duty: Warzone ... เล่นได้ที่: PC Zone`
- `TEKKEN 8 ... เล่นได้ที่: PC Zone และ PlayStation 5 Zone`

### ทำไมถึงผิด

ข้อมูลใน `game_item_details.jsonl` บอกแค่ระดับโซน เช่น `PC Zone` แต่คำถามถามระดับเครื่องย่อย `PC #01`, `PC #03`

ข้อมูลเครื่องย่อยที่ถูกต้องมีอยู่แล้วใน `data/curated/service_game_availability.jsonl`:

- `PC #01-#02` มี `TEKKEN 8` แต่ไม่มี `Call of Duty: Warzone`
- `PC #03-#10` มี `Call of Duty: Warzone` แต่ไม่มี `TEKKEN 8`

แต่ระบบเลือก `structured.games` ก่อน ทำให้ไม่ได้ใช้ตาราง availability รายเครื่อง

### จริง ๆ ควรตอบอะไร

`PC #01 มี Call of Duty: Warzone ไหม`

ควรตอบ:

```text
PC #01 ไม่มี Call of Duty: Warzone ครับ
Call of Duty: Warzone เล่นได้ที่ PC #03-#10

PC #01-#02 มีเกม: TEKKEN 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT
```

`PC #03 มี TEKKEN 8 ไหม`

ควรตอบ:

```text
PC #03 ไม่มี TEKKEN 8 ครับ
TEKKEN 8 เล่นได้ที่ PC #01-#02 และ PlayStation 5 #01-#02

PC #03-#10 มีเกม: Call of Duty: Warzone, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT
```

### วิธีแก้ที่ควรทำ

เพิ่ม `machine-specific availability resolver` ให้ทำงานก่อน `structured.games`

เงื่อนไข:

- ถ้ามี service/zone + เลขเครื่อง เช่น `PC #01`, `PC 3`, `#10`
- และมีชื่อเกม
- ให้ไปเช็ค `service_game_availability.jsonl` ก่อนเสมอ

ถ้า match แล้ว ให้ตอบ yes/no จากเครื่องจริง ไม่ใช้คำตอบระดับ zone

## 2. ถามว่าเล่นได้กี่คน แต่ระบบไปตอบเวลาเปิด-ปิดหรืออุปกรณ์

### เคสที่ผิด

- `PC #01-#02 เล่นได้กี่คน`
- `PC #03-#10 เล่นได้กี่คน`
- `PlayStation 5 #01-#02 เล่นได้กี่คน`
- `Nintendo Switch (1-2 Persons) เล่นได้กี่คน`
- `Nintendo Switch (1-4 Persons) เล่นได้กี่คน`
- `Cockpit #01-#02 เล่นได้กี่คน`
- `VR Station 30 นาที เล่นได้กี่คน`
- `VR Station 1 ชั่วโมง เล่นได้กี่คน`

### ระบบตอบอะไร

หลายเคสเข้า:

- `pipeline:schedule_fast_path`
- route: `schedule/count`

แล้วตอบเวลารอบบริการ เช่น Morning 09:00-12:00 / Afternoon 13:00-16:00

บางเคส PC เข้า:

- `pipeline:structured_equipment_item`
- route: `equipment/equipment_item_lookup`

แล้วตอบรายละเอียด Gaming PC แทนจำนวนคน

### ทำไมถึงผิด

คำว่า `กี่คน` ถูกตีเป็น count กว้าง ๆ แล้วไปชนกับ schedule/equipment

ระบบยังไม่มี operation ชัดเจนสำหรับ:

- service capacity
- จำนวนผู้เล่นต่อรอบ
- จำนวนคนที่บริการนั้นรองรับ

ทั้งที่ข้อมูล `capacity_persons` มีอยู่ใน `service_game_availability.jsonl`

### จริง ๆ ควรตอบอะไร

ควรตอบจาก `capacity_persons`:

```text
PC #01-#02 รองรับ 1 คนต่อรอบ 60 นาทีครับ
PC #03-#10 รองรับ 1 คนต่อรอบ 60 นาทีครับ
PlayStation 5 #01-#02 รองรับ 1-2 คนต่อรอบ 60 นาทีครับ
Nintendo Switch (1-2 Persons) รองรับ 1-2 คนต่อรอบ 60 นาทีครับ
Nintendo Switch (1-4 Persons) รองรับ 1-4 คนต่อรอบ 60 นาทีครับ
Cockpit #01-#02 รองรับ 1 คนต่อรอบ 60 นาทีครับ
VR Station 30 นาที รองรับ 1-5 คนต่อรอบ 30 นาทีครับ
VR Station 1 ชั่วโมง รองรับ 1-5 คนต่อรอบ 60 นาทีครับ
```

### วิธีแก้ที่ควรทำ

เพิ่ม operation ใหม่ เช่น `service_capacity_lookup`

เงื่อนไข:

- มีคำว่า `กี่คน`, `กี่ player`, `รองรับกี่คน`, `เล่นได้กี่คน`, `กี่ persons`
- และมี service/zone/machine target
- ให้ route ไป structured availability/capacity ก่อน schedule/equipment

## 3. ถามรายการเกมของโซน แต่ Ambiguity Gate ถามกลับ

### เคสที่ผิด

- `PC Zone รายการเกมมีอะไรบ้าง`
- `PlayStation 5 Zone รายการเกมมีอะไรบ้าง`
- `Nintendo Switch Zone รายการเกมมีอะไรบ้าง`
- `Cockpit Zone รายการเกมมีอะไรบ้าง`
- `VR Zone รายการเกมมีอะไรบ้าง`

### ระบบตอบอะไร

ระบบเข้า:

- mode: `pipeline:ambiguity_clarification`
- route: `clarification/ambiguity_gate_clarification`

แล้วถามกลับว่า “หมายถึงเรื่องไหนของ Zone นี้?” พร้อม preview เกม/อุปกรณ์/ราคา/จอง

### ทำไมถึงผิด

Ambiguity Gate เห็นว่า `PC Zone` หรือ `VR Zone` เป็น target กว้าง แล้ว flag เป็น `service_target_broad_missing_operation`

แต่จริง ๆ คำว่า `รายการเกม` ชัดแล้วว่า operation คือ list games

ปัญหาคือ gate ยังให้ broad-zone rule ชนะ explicit game-list keyword

### จริง ๆ ควรตอบอะไร

ควร list เกมทันที ไม่ต้องถามกลับ

ตัวอย่าง `PC Zone รายการเกมมีอะไรบ้าง`

```text
PC Zone มีเกมตามเครื่องดังนี้ครับ

PC #01-#02:
• TEKKEN 8
• Counter-Strike 2
• League of Legends
• PUBG: BATTLEGROUNDS
• VALORANT

PC #03-#10:
• Call of Duty: Warzone
• Counter-Strike 2
• League of Legends
• PUBG: BATTLEGROUNDS
• VALORANT
```

ตัวอย่าง `VR Zone รายการเกมมีอะไรบ้าง`

```text
VR Zone มีเกม:
• Beat Saber
• Horizon Call of the Mountain
• Resident Evil 4
• Resident Evil Village

ทั้ง VR 30 นาที และ VR 1 ชั่วโมง ใช้รายการเกมเดียวกันครับ
```

### วิธีแก้ที่ควรทำ

เพิ่ม explicit game-list override ก่อน Ambiguity Gate clarify

คำที่ควรถือว่าชัด:

- `รายการเกม`
- `รายชื่อเกม`
- `มีเกมอะไรบ้าง`
- `เกมในโซน`
- `เกมของโซน`
- `เล่นเกมอะไรได้บ้าง`

ถ้ามีคำเหล่านี้ ให้ตอบ list games เลย

## 4. ถามว่าจะเล่น Call of Duty ต้องจองอะไร แต่ตอบขั้นตอนจองทั่วไป

### เคสที่ผิด

- `ถ้าจะเล่น Call of Duty ต้องจองอะไร`

### ระบบตอบอะไร

ระบบเข้า:

- mode: `pipeline:structured_booking_selection`
- route: `reservation/booking_policy`

แล้วตอบขั้นตอนจองทั่วไป เช่น เลือกบริการ เลือกวันเวลา กรอกข้อมูล ชำระเงิน

### ทำไมถึงผิด

คำว่า `Call of Duty` เป็นชื่อ family ไม่ใช่เกมเดียวในข้อมูลจริง:

- `Call of Duty: Warzone`
- `Call of Duty: Modern Warfare III`

ระบบเห็นคำว่า `จอง` แล้วเลือก booking policy แต่ไม่ได้ resolve ว่าเกมนี้อยู่ service ไหน

### จริง ๆ ควรตอบอะไร

ควรตอบแบบมี preview และถามให้ชัด เพราะ `Call of Duty` มีมากกว่า 1 รายการ:

```text
Call of Duty ในข้อมูลตอนนี้มี 2 เกมครับ

• ถ้าหมายถึง Call of Duty: Warzone ให้จอง PC #03-#10
• ถ้าหมายถึง Call of Duty: Modern Warfare III ให้จอง PlayStation 5 #01-#02

พิมพ์ต่อได้เลยว่า Warzone หรือ Modern Warfare III
```

ถ้าผู้ใช้พิมพ์ `warzone` ต่อ ควรตอบ:

```text
ถ้าจะเล่น Call of Duty: Warzone ให้จอง PC #03-#10 ครับ
```

### วิธีแก้ที่ควรทำ

เพิ่ม `game-to-booking resolver`

เงื่อนไข:

- มีคำว่า `จอง`, `ต้องจองอะไร`, `เล่น ... ต้องจอง`
- และมีชื่อเกมหรือชื่อ family

ให้ resolve แบบนี้:

- ถ้าเกมเดียว match service เดียว: ตอบ service ที่ต้องจอง
- ถ้าเกมเดียวอยู่หลาย service: แสดง options
- ถ้า family มีหลายเกม: ถาม clarify พร้อม preview จากข้อมูลจริง

## 5. คำว่า “ประชาสัมพันธ์” ทำให้ระบบเข้า member role ผิด

### เคสที่ผิด

- `เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค`
- `เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบสั้น ๆ`

### ระบบตอบอะไร

ระบบเข้า:

- mode: `pipeline:structured_members_role_lookup`
- route: `overview/members_lookup`

แล้วตอบว่า:

```text
ตำแหน่ง ประชาสัมพันธ์ มี 1 คนครับ
...
```

### ทำไมถึงผิด

คำว่า `ประชาสัมพันธ์` มีสองความหมาย:

- เป็น role ของสมาชิกทีม
- เป็น action/verb เช่น “เขียนข้อความประชาสัมพันธ์”

ระบบตอนนี้จับ role keyword แรงเกินไป แล้วไม่ได้ดูคำกริยานำหน้า เช่น `เขียน`, `แต่ง`, `ช่วยเขียน`, `ประโยค`, `ข้อความ`

### จริง ๆ ควรตอบอะไร

ควรเป็น general generation โดยไม่แต่งข้อมูลกิจกรรมที่ไม่มี:

```text
ขอเชิญชวนทุกคนเข้าร่วมกิจกรรมของ PSU Esports Studio - Phuket เพื่อเปิดประสบการณ์ความสนุกและการเรียนรู้ร่วมกันครับ
```

ถ้าอยากเข้มเรื่อง no-guess ควรตอบ:

```text
ได้ครับ หากยังไม่ระบุชื่อกิจกรรม วันเวลา หรือสถานที่ ผมจะเขียนเป็นประโยคกลาง ๆ ให้:
ขอเชิญชวนทุกคนเข้าร่วมกิจกรรมของ PSU Esports Studio - Phuket เพื่อร่วมสนุกและเรียนรู้ด้านอีสปอร์ตไปด้วยกันครับ
```

### วิธีแก้ที่ควรทำ

เพิ่ม negative guard ให้ member role lookup:

ถ้ามีคำเหล่านี้:

- `เขียน`
- `แต่ง`
- `ช่วยเขียน`
- `ประโยค`
- `ข้อความ`
- `แคปชัน`
- `caption`
- `ประกาศ`

และไม่มีคำถามแบบ:

- `ใคร`
- `ใครทำ`
- `ใครเป็น`
- `ตำแหน่ง`
- `คนไหน`
- `สมาชิก`

ห้ามเข้า `structured.members`

## 6. ถามค่าปรับจอยพัง แต่ระบบถามกลับเรื่องราคาโซน

### เคสที่ผิด

- `ทำจอยพังโดนปรับเท่าไหร่`

### ระบบตอบอะไร

ระบบเข้า:

- mode: `pipeline:ambiguity_clarification`
- route: `clarification/ambiguity_gate_clarification`

แล้วถามกลับว่า:

```text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
```

### ทำไมถึงผิด

คำว่า `เท่าไหร่` ทำให้ระบบมองเป็น price/service fee

แต่คำว่า `จอยพัง`, `พัง`, `โดนปรับ` ควรชนะ price route เพราะนี่คือ penalty/damage ไม่ใช่ค่าบริการ

ข้อมูลมีอยู่แล้วใน `data/curated/curated_facts.jsonl`:

- ความเสียหายเล็กน้อย เช่นปุ่มหลวม มีค่าปรับ 100-500 บาท
- ความเสียหายปานกลาง เช่นคอนโทรลเลอร์ปุ่มค้าง ต้องชำระค่าซ่อมตามราคาจริง หรือ 500-2,000 บาท
- ความเสียหายร้ายแรง เช่นอุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

### จริง ๆ ควรตอบอะไร

```text
ถ้าทำจอยหรือคอนโทรลเลอร์เสีย ค่าปรับขึ้นอยู่กับระดับความเสียหายครับ

• เสียหายเล็กน้อย เช่นปุ่มหลวม: 100-500 บาท
• เสียหายปานกลาง เช่นคอนโทรลเลอร์ปุ่มค้าง: ค่าซ่อมตามราคาจริง หรือ 500-2,000 บาท
• ถ้าเสียหายร้ายแรงจนใช้งานไม่ได้: ชดเชยเต็มจำนวนตามราคากลาง

แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### วิธีแก้ที่ควรทำ

เพิ่ม penalty guard ให้ชนะ price ambiguity:

คำ trigger:

- `จอยพัง`
- `จอยเสีย`
- `คอนโทรลเลอร์พัง`
- `ปุ่มค้าง`
- `ปุ่มหลวม`
- `ทำพัง`
- `เสียหาย`
- `โดนปรับ`
- `ปรับเท่าไหร่`
- `ค่าซ่อม`
- `ชดเชย`

ถ้ามีคำเหล่านี้ ให้ route ไป `penalty/penalty_policy` ก่อน service fee เสมอ

## 7. ถามกติกาในศูนย์ แต่ระบบไป competition/no-answer

### เคสที่ผิด

- `กติกาในศูนย์มีอะไรบ้าง`

### ระบบตอบอะไร

บาง run เข้า:

- `pipeline:general_psu_scope_no_answer`
- route: `general/competition_rules_lookup`

บาง run เข้า competition rules หรือ no-answer

### ทำไมถึงผิด

คำว่า `กติกา` ถูกโยงไป `competition_rules` แรงเกินไป

แต่คำว่า `ในศูนย์` หมายถึง studio rules / reservation rules ไม่ใช่กติกาการแข่งขัน

ข้อมูลกติกาศูนย์มีอยู่แล้วใน `data/curated/curated_facts.jsonl` เช่น:

- ฝากสัมภาระก่อนเข้าใช้บริการ
- รับประทานอาหารและเครื่องดื่มเฉพาะพื้นที่ที่กำหนด
- คืนอุปกรณ์และแผ่นเกมหลังใช้งาน
- งดส่งเสียงดังและห้ามพูดจาดูหมิ่น/เสียดสี
- ห้ามเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
- ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
- ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มแอลกอฮอล์ภายในศูนย์
- ห้ามพกอาวุธ ทะเลาะวิวาท หรือเล่นการพนัน

### จริง ๆ ควรตอบอะไร

```text
กติกาในศูนย์ที่ยืนยันได้มีหลัก ๆ ดังนี้ครับ

• ฝากสัมภาระก่อนเข้าใช้บริการ
• รับประทานอาหารและเครื่องดื่มเฉพาะพื้นที่ที่กำหนด
• คืนอุปกรณ์และแผ่นเกมหลังใช้งาน
• งดส่งเสียงดัง และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
• ห้ามเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
• ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
• ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มแอลกอฮอล์ภายในศูนย์
• ห้ามพกอาวุธ ทะเลาะวิวาท หรือเล่นการพนัน

แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### วิธีแก้ที่ควรทำ

แยก rule intent เป็น 2 กลุ่ม:

- `studio_rules`: กติกาในศูนย์, กฎการใช้บริการ, ข้อห้ามในศูนย์
- `competition_rules`: กติกาแข่ง, tournament, match, bracket, map, team, pause, penalty แข่งขัน

ถ้ามีคำว่า `ในศูนย์`, `ใช้บริการ`, `ห้อง`, `studio`, `ข้างใน`, `เข้าใช้` ให้ prefer `studio_rules`

## 8. General LLM บางตัวตอบปนภาษาอื่นหรือมี reasoning หลุด

### เคสที่ผิด

- `ช่วยทำการบ้านคณิตให้หน่อย`
- `อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ`
- `เฟรมเรตกับความละเอียดต่างกันยังไง`

### ระบบตอบอะไร

บางโมเดลตอบปนภาษาจีน เช่น:

```text
ขออภัยครับ 但我需要您提供具体的问题内容...
```

บางคำตอบมี reasoning ภาษาอังกฤษหลุด เช่น:

```text
Okay, let's tackle this question...
```

### ทำไมถึงผิด

เป็นปัญหา model behavior / output formatting ไม่ใช่ structured data

สาเหตุที่เป็นไปได้:

- prompt ยังบังคับภาษาไทยไม่แน่นพอใน general fallback
- ไม่มี output language validator
- ไม่มี sanitizer ตัด reasoning prefix
- บางโมเดล multilingual drift ง่ายกว่า

### จริง ๆ ควรตอบอะไร

`ช่วยทำการบ้านคณิตให้หน่อย`

```text
ส่งโจทย์คณิตมาได้เลยครับ เดี๋ยวช่วยอธิบายวิธีทำทีละขั้นตอน
```

`อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ`

```text
Latency คือความหน่วงหรือเวลาที่ข้อมูลใช้เดินทางจากจุดหนึ่งไปอีกจุดหนึ่ง ยิ่ง latency ต่ำ ระบบก็ยิ่งตอบสนองเร็วครับ
```

`เฟรมเรตกับความละเอียดต่างกันยังไง`

```text
เฟรมเรตคือจำนวนภาพต่อวินาที ยิ่งสูงภาพยิ่งลื่น ส่วนความละเอียดคือจำนวนพิกเซลของภาพ ยิ่งสูงภาพยิ่งคมชัดครับ
```

### วิธีแก้ที่ควรทำ

เพิ่ม `General LLM Output Validator`:

- ถ้าพบตัวอักษรจีน/ญี่ปุ่น/เกาหลีเกิน threshold ให้ retry 1 ครั้งด้วย prompt “ตอบภาษาไทยเท่านั้น”
- ถ้าขึ้นต้นด้วย reasoning เช่น `Okay`, `Let's`, `We need`, `I need to` ให้ตัดหรือ retry
- ถ้าเป็น Qwen3 แล้วมี `<think>` หรือ reasoning หลุด ให้ strip ก่อนส่งออก
- ตั้ง system prompt ให้ชัดว่า “ตอบไทยเท่านั้น ยกเว้นชื่อเฉพาะ/ศัพท์เทคนิค”

## 9. No-LLM fail ในกลุ่ม general_llm ไม่ใช่ bug หลัก

### เคสที่ผิด

เช่น:

- `API คืออะไร`
- `JSON คืออะไร`
- `GPU คืออะไรแบบเข้าใจง่าย`
- `ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค`

### ระบบตอบอะไร

No-LLM run ตอบว่า:

```text
ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิด...
```

### ทำไมถึงผิด

นี่เป็นผลที่คาดได้ เพราะคำถามพวกนี้ต้องใช้ general knowledge generation แต่ run นั้นปิด LLM

ดังนั้นไม่ควรเอาเคสนี้ไปตัดสินว่า rule path แย่ แต่ควรใช้แยกให้เห็นว่า:

- ถ้าไม่เปิด LLM ระบบตอบ general question ไม่ได้
- ถ้าเปิด LLM ระบบตอบได้ แต่ต้องมี output validator กันภาษา/format หลุด

### จริง ๆ ควรตอบอะไรเมื่อเปิด LLM

ตัวอย่าง:

```text
API คือช่องทางให้โปรแกรมสองตัวคุยกัน เช่น แอปเรียกข้อมูลจาก server ผ่าน API เพื่อเอาข้อมูลมาแสดงผล
```

## 10. บาง fail อาจเป็น eval strictness ไม่ใช่คำตอบผิดจริงทั้งหมด

### ตัวอย่าง

`เพลงฮิตตอนนี้คืออะไร`

ระบบตอบประมาณว่าเพลงฮิตเปลี่ยนตลอด ควรตรวจชาร์ตล่าสุด

ถ้าวัดตาม policy ของ chatbot:

- ถ้าเปิด general LLM: คำตอบแบบนี้พอรับได้ เพราะไม่ได้แต่งชื่อเพลง
- ถ้าต้องการ strict PSU-only: ควร no-answer

### ข้อสรุป

ต้องแยก eval expectation เป็น 2 policy:

- `general_allowed`: คำถามทั่วไปตอบได้ แต่ต้องไม่อ้างว่าเป็นข้อมูล PSU
- `psu_only`: คำถามนอก PSU ให้ no-answer

ตอนนี้ eval บางข้อคาด no-answer แต่ระบบเปิด general fallback อยู่ จึงนับ fail ทั้งที่พฤติกรรมอาจถูกตาม mode ที่เปิด

## Root Cause Ranking

### P0: ต้องแก้ก่อน

1. Machine-specific availability ถูกข้าม
   - กระทบข้อมูลจริงสูง
   - ทำให้ตอบผิดแบบมั่นใจ
   - ตัวอย่าง: `PC #01 มี Warzone ไหม`

2. Service capacity ไม่มี route ชัด
   - กระทบคำถามใช้งานจริง
   - คำถามง่ายมากแต่ตอบผิดหมวด
   - ตัวอย่าง: `VR 30 นาที เล่นได้กี่คน`

3. Penalty damage โดน price ambiguity กลืน
   - เสี่ยงตอบผิดเรื่องเงิน/ค่าปรับ
   - ตัวอย่าง: `ทำจอยพังโดนปรับเท่าไหร่`

### P1: ควรแก้ถัดไป

4. Explicit game-list ยังโดน Ambiguity Gate
   - ผู้ใช้ถามชัดแล้ว แต่ระบบถามกลับ
   - ทำให้ UX แย่

5. Booking by game/family ยังตอบ generic
   - ควร map เกมไป service ที่ต้องจอง
   - ถ้าชื่อ family มีหลายเกมให้ถามกลับพร้อม preview

6. Studio rules vs competition rules ยังปนกัน
   - คำว่า `กติกา` กว้างเกินไป
   - ต้องแยก `กติกาในศูนย์` กับ `กติกาแข่งขัน`

### P2: เสริมคุณภาพ

7. Member role false positive จากคำว่า `ประชาสัมพันธ์`
   - ต้องเพิ่ม negative guard สำหรับคำสั่งให้เขียนข้อความ

8. General LLM output language drift
   - เพิ่ม language/output validator

9. Eval policy ของ general/no-answer ต้องแยก mode
   - ลด false fail ใน report

## Fix Plan ที่แนะนำ

ทำตามลำดับนี้จะคุ้มที่สุด:

1. เพิ่ม `service_game_availability` เป็น structured tool จริง
   - รองรับ list games by zone
   - รองรับ machine-specific yes/no
   - รองรับ capacity/duration
   - รองรับ game-to-booking mapping

2. เพิ่ม route priority ใหม่ก่อน `structured.games`, `equipment`, `schedule`
   - `machine_availability_lookup`
   - `service_capacity_lookup`
   - `zone_game_list_lookup`
   - `game_booking_target_lookup`

3. แก้ Ambiguity Gate
   - ถ้ามี explicit operation เช่น `รายการเกม`, `เล่นได้กี่คน`, `โดนปรับ`
   - ห้ามถามกลับแบบ broad-zone

4. เพิ่ม penalty/rules guard
   - damage/penalty ต้องชนะ price
   - studio rules ต้องชนะ competition rules เมื่อมีคำว่า `ในศูนย์/ใช้บริการ`

5. เพิ่ม General LLM Output Validator
   - กันภาษาปน
   - กัน reasoning หลุด
   - retry 1 ครั้ง หรือ fallback เป็นคำตอบสั้นที่ปลอดภัย

6. ปรับ eval expectation
   - แยก `No-LLM expected no-answer`
   - แยก `LLM-enabled expected answer`
   - แยก policy `general_allowed` กับ `psu_only`

## สรุปสั้นที่สุด

คำตอบที่ผิดรอบนี้มี 2 แบบใหญ่ ๆ:

1. ผิดตั้งแต่เลือกทาง
   - เครื่องย่อยถูกตอบเป็นโซน
   - จำนวนคนถูกตอบเป็นเวลาเปิดปิด
   - ค่าปรับถูกเข้าใจเป็นราคา service
   - กติกาในศูนย์ถูกมองเป็นกติกาแข่ง

2. ผิดจาก LLM output
   - ภาษาปน
   - reasoning หลุด
   - general/no-answer policy ยังวัดปนกัน

จุดที่ควรแก้ก่อนสุดคือ availability/capacity/penalty เพราะเป็นข้อมูลจริงของศูนย์และมีผลกับผู้ใช้โดยตรง
