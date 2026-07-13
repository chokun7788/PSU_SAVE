# Game Intent Answer-first Implementation

วันที่: 2026-07-06

## สรุปสั้น

แก้คำถามแนว `อยากเล่น <ชื่อเกม>` ให้ตอบตรงเกมที่ผู้ใช้ถามก่อน ไม่ตอบเป็น list กว้างของทั้งโซน

แก้แบบ pattern กลาง ไม่ได้ hardcode เฉพาะ Tekken 8

ยังไม่ได้ deploy และยังไม่ได้ sync ไปโฟลเดอร์ deploy

## ปัญหาเดิม

ตัวอย่าง:

```text
อยากเล่น Tekken 8
```

คำตอบเดิม:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```

ปัญหา:

- ไม่ answer-first
- ตอบเป็น list กว้าง ทั้งที่ผู้ใช้ถามเกมเดียว
- ถามเกมอื่นในทรงเดียวกันอาจไม่ได้คำตอบที่ตรงเจตนา

## สิ่งที่แก้

### 1. Router

ไฟล์:

```text
app/pipeline/router.py
```

เพิ่ม pattern ใน game availability:

```text
อยากเล่น
อยากลองเล่น
จะเล่น
ขอเล่น
```

ผล:

```text
อยากเล่น Tekken 8
อยากเล่นเกม Tekken 8
อยากเล่น Beat Saber
อยากเล่น Gran Turismo 7
```

เข้า route:

```text
games / game_availability_lookup
```

### 2. Fast answer template

ไฟล์:

```text
app/runtime/fast_answer.py
```

เปลี่ยน known-game availability answer เป็น:

```text
เล่น <ชื่อเกม> ได้ครับ
มีให้เล่นที่: <โซน>
แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

### 3. ปรับลำดับ answer_games

ปรับให้ specific game availability มาก่อน related guidance เพื่อกันเคส:

```text
อยากเล่นเกม Tekken 8
อยากเล่นเกม Beat Saber
```

ไม่หลุดไปคำตอบแนว genre/related guidance

## ตัวอย่างผลลัพธ์

```text
Q: อยากเล่น Tekken 8
route: games / game_availability_lookup
mode: pipeline:games_availability_fast_path

เล่น TEKKEN 8 ได้ครับ
มีให้เล่นที่: PC Zone และ PlayStation 5 Zone
แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

```text
Q: อยากเล่น Beat Saber
route: games / game_availability_lookup
mode: pipeline:games_availability_fast_path

เล่น Beat Saber ได้ครับ
มีให้เล่นที่: VR Zone
...
```

```text
Q: อยากเล่น Minecraft
route: games / game_availability_lookup
mode: pipeline:games_unknown_fast_path

ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้...
```

## Ad-hoc test

Questions:

```text
reports/ad_hoc_questions_game_intent_answer_first_20260706.txt
```

Latest report:

```text
reports/ad_hoc_pipeline_results_game_intent_answer_first_fix2_20260706.md
reports/ad_hoc_pipeline_results_game_intent_answer_first_fix2_20260706.jsonl
```

ผล:

```text
questions=12
routes:
- competition_rules/competition_rules_lookup: 1
- equipment/related_guidance: 1
- games/game_availability_lookup: 10
```

ตัวอย่างที่ทดสอบ:

```text
อยากเล่น Tekken 8
อยากเล่นเกม Tekken 8
อยากเล่น Beat Saber
อยากเล่นเกม Beat Saber
อยากเล่น Gran Turismo 7
อยากเล่น Mario Kart
อยากเล่น Valorant
อยากเล่น Fortnite
อยากเล่น Minecraft
Beat Saber คือเกมอะไรแล้วเล่นยังไง
Tekken 8 เกมนึงมี 3 rounds ใช่ไหม
อยากเล่นเกมขยับตัวควรเล่นโซนไหน
```

## Regression

Compile:

```text
py_compile OK
```

Validate:

```text
VALIDATION OK
- rule files: 8
- rules: 77
- curated rows: 324
- service fee sanity: OK
```

GT360:

```text
Total: 360
PASS: 360
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_game_intent_answer_first_fix2_gt360_20260706.md
reports/pipeline_ground_truth_results_game_intent_answer_first_fix2_gt360_20260706.jsonl
```

Competition challenger v2:

```text
Total: 369
PASS: 369
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_game_intent_answer_first_fix2_comp_v2_20260706.md
reports/pipeline_ground_truth_results_game_intent_answer_first_fix2_comp_v2_20260706.jsonl
```

## ข้อจำกัด

- ยังตอบจาก catalog ที่ยืนยันได้เท่านั้น
- ถ้าเกมไม่อยู่ในรายการ เช่น Minecraft ต้อง no-answer
- ยังไม่ใช่ LLM rewrite อิสระ แต่เป็น template ที่นุ่มขึ้นและตรงเจตนามากขึ้น

