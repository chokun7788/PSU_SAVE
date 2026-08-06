# VR Game Controls Source Research - 2026-07-29

เอกสารนี้สรุปการหาแหล่งอ้างอิงสำหรับข้อมูลปุ่ม/วิธีควบคุมเกม VR ที่ยังไม่มีข้อมูลครบใน PSU Esports Chatbot

สำคัญ:

- ข้อมูลนี้เป็น "ข้อมูลการควบคุมของตัวเกม/แพลตฟอร์ม" จากแหล่งอ้างอิงภายนอก
- ยังไม่ใช่การยืนยันว่า PSU Esports Studio - Phuket ตั้งค่า controller เหมือนกันทุกเครื่อง
- ถ้าจะเอาเข้า chatbot ให้ใส่ `coverage_status: partial` ก่อน จนกว่าจะตรวจจากเครื่องจริงหรือภาพ in-game control settings
- ห้ามแต่งปุ่มละเอียดเองถ้าแหล่งทางการไม่ได้บอก

## VR games ที่พบใน catalog ตอนนี้

จากไฟล์:

- `data/curated/game_item_details.jsonl`
- `data/curated/our_games_scraped_details.jsonl`

พบเกม VR ชัด ๆ:

1. Beat Saber
2. Horizon Call of the Mountain

## สรุปสั้น

| เกม | หา source ทางการได้ไหม | ได้ข้อมูลระดับไหน | ควรใส่ chatbot ตอนนี้ไหม |
|---|---|---|---|
| Beat Saber | ได้ | motion/control concept, platform support, tracked controller support | ใส่ได้แบบ high-level controls / motion controls แต่ยังไม่ควรใส่ปุ่มละเอียดแบบฟันธง |
| Horizon Call of the Mountain | ได้ | PS VR2 required, Sense controllers required, Gesture/Analogue movement schemes, motion interaction | ใส่ได้แบบ high-level controls + movement schemes แต่ exact button mapping ต้องตรวจในเกมเพิ่ม |

## 1. Beat Saber

### แหล่งอ้างอิงที่เจอ

1. PlayStation official game page
   - URL: `https://www.playstation.com/en-us/games/beat-saber/`
   - ข้อมูลสำคัญ: เกมเป็น PS VR/PS VR2 และอธิบายว่าใช้ saber หนึ่งอันในแต่ละมือเพื่อฟัน beat ตามสีและทิศทาง

2. Beat Saber official FAQ
   - URL: `https://beatsaber.com/faq.html`
   - ข้อมูลสำคัญ: พูดถึงปัญหา tracking, Quest controller tracking, floor/player height, PlayStation support status

3. Steam official store page
   - URL: `https://store.steampowered.com/app/620980/Beat_Saber/`
   - ข้อมูลสำคัญ: ระบุว่าเป็น VR Only และมี Tracked Controller Support

### ข้อมูลที่ยืนยันได้จาก source

Beat Saber ไม่ใช่เกมที่ใช้ปุ่มแบบ gamepad เป็นหลัก แต่ใช้ motion controller เป็นหลัก:

- มือซ้าย = saber ซ้าย
- มือขวา = saber ขวา
- ฟัน block/beat ที่ลอยเข้ามา
- ต้องฟันให้ตรงสีและทิศทาง
- ใช้การขยับตัวเพื่อหลบสิ่งกีดขวาง
- ต้องใช้ tracked controllers / VR controllers

### ข้อมูลที่ยังไม่ควรฟันธง

ยังไม่เจอ source ทางการที่บอก exact mapping เช่น:

- ปุ่มไหน pause ใน PS VR2
- ปุ่มไหน confirm/back ในเมนูเกม
- ปุ่มไหน reset view เฉพาะในเกม

ถ้าจะเก็บลง chatbot ตอนนี้ ควรตอบแบบนี้:

```text
Beat Saber ควบคุมหลักด้วยการขยับคอนโทรลเลอร์ครับ
- มือซ้ายถือ saber ซ้าย
- มือขวาถือ saber ขวา
- ฟันบล็อกให้ตรงสีและทิศทางที่บล็อกบอก
- ขยับตัว/ย่อตัวเพื่อหลบสิ่งกีดขวาง

ตอนนี้ยังไม่มีข้อมูลปุ่มเมนู/ปุ่มเฉพาะในเกมที่ยืนยันจากแหล่งทางการของ PSU Esports Studio - Phuket ครับ
```

### Draft data ที่แนะนำ

ถ้าจะเพิ่มเข้า `game_control_facts.jsonl` ควรเพิ่มแบบ motion controls ไม่ใช่ button mapping:

```json
{"game":"Beat Saber","platform":"VR / PS VR2","control_type":"motion","button":"Left controller motion","action_th":"ควบคุม saber ซ้าย / ฟันบล็อกสีซ้ายตามทิศทาง","coverage_status":"partial","source_ids":["beat_saber_playstation_official","beat_saber_steam_store"]}
{"game":"Beat Saber","platform":"VR / PS VR2","control_type":"motion","button":"Right controller motion","action_th":"ควบคุม saber ขวา / ฟันบล็อกสีขวาตามทิศทาง","coverage_status":"partial","source_ids":["beat_saber_playstation_official","beat_saber_steam_store"]}
{"game":"Beat Saber","platform":"VR / PS VR2","control_type":"body_movement","button":"Body movement","action_th":"ขยับตัวหรือย่อตัวเพื่อหลบสิ่งกีดขวาง","coverage_status":"partial","source_ids":["beat_saber_playstation_official"]}
```

ต้องตรวจเพิ่มจากเครื่องจริงก่อนเพิ่ม:

- Pause/Menu button
- Confirm/Back button
- Reset position/view button เฉพาะในเกม

## 2. Horizon Call of the Mountain

### แหล่งอ้างอิงที่เจอ

1. PlayStation official game page
   - URL: `https://www.playstation.com/en-us/games/horizon-call-of-the-mountain/`
   - ข้อมูลสำคัญ: PlayStation VR2 required, PS VR2 Sense controllers required, รองรับ sitting/standing/roomscale, ใช้ Sense controllers สองข้างเพื่อ interact, climb, shoot bow, craft

2. PlayStation official support page
   - URL: `https://www.playstation.com/en-us/support/games/horizon-call-of-the-mountain/`
   - ข้อมูลสำคัญ: เลือก control scheme ได้ 2 แบบ คือ Gesture และ Analogue
   - Gesture = เคลื่อนที่ด้วย physical movements
   - Analogue = ใช้ sticks บน PS VR2 Sense controllers เพื่อเคลื่อนที่
   - เปลี่ยน control scheme ได้ใน Options menu

3. PlayStation VR2 official FAQ
   - URL: `https://blog.playstation.com/2023/02/06/playstation-vr2-the-ultimate-faq/`
   - ข้อมูลสำคัญ: layout ของ PS VR2 Sense controller
   - Left controller: analog stick, Triangle, Square, grip L1, trigger L2, Create
   - Right controller: analog stick, Cross, Circle, grip R1, trigger R2, Options

4. PlayStation PS VR2 Sense controller setup page
   - URL: `https://www.playstation.com/en-us/support/hardware/ps-vr-2-sense-controller/`
   - ข้อมูลสำคัญ: การ pair, charge, custom button assignments

### ข้อมูลที่ยืนยันได้จาก source

Horizon Call of the Mountain ใช้ PS VR2 Sense controllers เป็นหลัก:

- ต้องใช้ PS VR2
- ต้องใช้ PS VR2 Sense controllers
- เลือก movement ได้ 2 แบบ:
  - Gesture: เคลื่อนที่ด้วยการขยับร่างกาย/ท่าทาง
  - Analogue: ใช้ analog sticks บน Sense controllers เพื่อเดิน
- ใช้การขยับมือ/คอนโทรลเลอร์ในการ:
  - ปีน
  - ยิงธนู
  - craft items
  - interact กับสิ่งแวดล้อม

### ข้อมูลที่ยังไม่ควรฟันธง

ยังไม่เจอ source ทางการที่แจก exact button mapping แบบครบ เช่น:

- L1/R1 ใช้จับ/ปีนใน Horizon แน่ไหม
- L2/R2 ใช้ยิง/ปล่อยธนูแน่ไหม
- Square/Cross/Circle/Triangle ใช้กับ action อะไรในเกมแน่

ถึง PS VR2 FAQ บอกว่า L1/R1 คือ grip button และ R2/L2 คือ trigger button แต่ไม่ควรเอาไปผูกกับ action ของ Horizon แบบฟันธงถ้าไม่มี source ของ Horizon เองหรือภาพจาก in-game settings

ถ้าจะเก็บลง chatbot ตอนนี้ ควรตอบแบบนี้:

```text
Horizon Call of the Mountain ใช้ PS VR2 Sense controllers ครับ
- เลือกการเดินได้ 2 แบบ: Gesture หรือ Analogue
- Gesture คือเดิน/เคลื่อนที่ด้วยท่าทางร่างกาย
- Analogue คือใช้ analog sticks บน Sense controllers เพื่อเคลื่อนที่
- การปีน ยิงธนู craft และโต้ตอบ ใช้การขยับมือ/คอนโทรลเลอร์เป็นหลัก

ตอนนี้ยังไม่มีข้อมูลปุ่มละเอียดรายปุ่มจากแหล่งทางการของ PSU Esports Studio - Phuket ครับ
```

### Draft data ที่แนะนำ

```json
{"game":"Horizon Call of the Mountain","platform":"PS VR2","control_type":"movement_scheme","button":"Gesture mode","action_th":"เคลื่อนที่ด้วยการขยับร่างกาย/ท่าทาง","coverage_status":"partial","source_ids":["horizon_cotm_playstation_support"]}
{"game":"Horizon Call of the Mountain","platform":"PS VR2","control_type":"movement_scheme","button":"Analogue sticks","action_th":"ใช้ analog sticks บน PS VR2 Sense controllers เพื่อเคลื่อนที่","coverage_status":"partial","source_ids":["horizon_cotm_playstation_support"]}
{"game":"Horizon Call of the Mountain","platform":"PS VR2","control_type":"motion","button":"Sense controller motion","action_th":"ใช้การขยับมือ/คอนโทรลเลอร์เพื่อปีน ยิงธนู craft และโต้ตอบกับสิ่งแวดล้อม","coverage_status":"partial","source_ids":["horizon_cotm_playstation_game_page"]}
```

ต้องตรวจเพิ่มจากเครื่องจริงก่อนเพิ่ม:

- ปุ่มจับ/ปล่อยตอนปีน
- ปุ่มยิงธนู/ดึงสาย/เลือกอาวุธ
- ปุ่มเมนู/เปลี่ยนเครื่องมือ
- ปุ่ม reset view เฉพาะในเกม

## 3. Source IDs ที่ควรเพิ่มใน Source Registry v2

ถ้าจะทำ source registry กลาง แนะนำเพิ่ม source เหล่านี้:

```json
{"source_id":"beat_saber_playstation_official","category":"game_controls","title":"Beat Saber PlayStation Official Page","source_url":"https://www.playstation.com/en-us/games/beat-saber/","source_type":"official_game_page","trust_level":"official","updated_at":"2026-07-29","origin":"PlayStation official game page","description":"Official PlayStation page describing Beat Saber gameplay and PS VR/PS VR2 support."}
{"source_id":"beat_saber_official_faq","category":"game_controls","title":"Beat Saber Official FAQ","source_url":"https://beatsaber.com/faq.html","source_type":"official_faq","trust_level":"official","updated_at":"2026-07-29","origin":"Beat Saber official website","description":"Official FAQ for Beat Saber tracking, platform, and support notes."}
{"source_id":"beat_saber_steam_store","category":"game_controls","title":"Beat Saber Steam Store Page","source_url":"https://store.steampowered.com/app/620980/Beat_Saber/","source_type":"official_store_page","trust_level":"official","updated_at":"2026-07-29","origin":"Steam store page by Beat Games","description":"Store page indicating Beat Saber is VR only and supports tracked controllers."}
{"source_id":"horizon_cotm_playstation_game_page","category":"game_controls","title":"Horizon Call of the Mountain PlayStation Official Page","source_url":"https://www.playstation.com/en-us/games/horizon-call-of-the-mountain/","source_type":"official_game_page","trust_level":"official","updated_at":"2026-07-29","origin":"PlayStation official game page","description":"Official page describing PS VR2 requirement, Sense controller requirement, and motion interaction."}
{"source_id":"horizon_cotm_playstation_support","category":"game_controls","title":"Horizon Call of the Mountain PlayStation Support Page","source_url":"https://www.playstation.com/en-us/support/games/horizon-call-of-the-mountain/","source_type":"official_support_page","trust_level":"official","updated_at":"2026-07-29","origin":"PlayStation official support","description":"Official support page describing Gesture and Analogue control schemes."}
{"source_id":"psvr2_controller_official_faq","category":"controller_reference","title":"PlayStation VR2 Ultimate FAQ","source_url":"https://blog.playstation.com/2023/02/06/playstation-vr2-the-ultimate-faq/","source_type":"official_platform_faq","trust_level":"official","updated_at":"2026-07-29","origin":"PlayStation Blog official FAQ","description":"Official PS VR2 Sense controller layout and platform controller reference."}
```

## 4. คำตอบที่ chatbot ควรใช้เมื่อถามปุ่ม VR แล้วข้อมูลยัง partial

ควรตอบแบบไม่เดา:

```text
เกมนี้เป็น VR เลยควบคุมหลักด้วยการขยับคอนโทรลเลอร์/ร่างกายมากกว่าปุ่มแบบจอยทั่วไปครับ

ข้อมูลที่ยืนยันได้ตอนนี้:
- ...

ส่วนปุ่มละเอียดรายปุ่ม เช่น pause/menu/reset view ยังไม่มีข้อมูลที่ยืนยันจาก PSU Esports Studio - Phuket หรือหน้าคู่มือ official แบบละเอียดครับ
```

ห้ามตอบแบบนี้:

```text
กด R2 เพื่อยิงธนู / L1 เพื่อปีน / X เพื่อกระโดด
```

ถ้ายังไม่มีแหล่งเฉพาะของเกมหรือ screenshot จาก settings ในเกม เพราะเสี่ยงเดา

## 5. สิ่งที่ควรทำต่อ

1. เพิ่ม source registry entries ด้านบน
2. เพิ่ม VR control facts แบบ `coverage_status: partial`
3. ทำ field ใหม่ `control_type` เพื่อรองรับ motion/gesture ไม่ใช่แค่ button
4. เพิ่ม no-answer policy สำหรับ exact VR button mapping ที่ยังไม่ยืนยัน
5. ถ่ายรูป/จดจากหน้า in-game control settings ของ Beat Saber และ Horizon Call of the Mountain บนเครื่องจริง แล้วค่อยเพิ่ม exact button mapping
