# Partial Game Name Support

วันที่: 2026-07-06

## สรุปสั้น

เพิ่มการรองรับชื่อเกมแบบพิมพ์ไม่ครบ/ชื่อกว้าง เช่น:

```text
อยากเล่น Mario
อยากเล่นมาริโอ
อยากเล่น Resident Evil
อยากเล่น Call of Duty
```

ระบบจะไม่ no-answer ทันทีถ้ามีเกมที่เกี่ยวข้องใน catalog แต่จะตอบเป็นรายการเกมที่เกี่ยวข้องและยืนยันได้

ยังไม่ deploy แต่ sync ไปโฟลเดอร์ deploy `20_PSU_Esports_Vercel_Deploy` แล้ว และ compile ฝั่ง `20` ผ่านแล้ว

## ไฟล์ที่แก้

```text
app/runtime/fast_answer.py
app/pipeline/router.py
```

## สิ่งที่เพิ่ม

### 1. Game family matcher

เพิ่ม family mapping:

```text
Mario
- Mario Kart 8 Deluxe
- Mario Party Superstars
- New Super Mario Bros. U Deluxe
- Super Mario Odyssey

Resident Evil
- Resident Evil 4
- Resident Evil Village

Call of Duty
- Call of Duty: Warzone
- Call of Duty: Modern Warfare III
```

### 2. คำตอบแบบไม่เดา

ถ้าผู้ใช้ถามชื่อกว้าง:

```text
อยากเล่น Mario
```

ระบบตอบ:

```text
พบเกมที่เกี่ยวข้องกับ Mario ในรายการที่ยืนยันได้ครับ
- Mario Kart 8 Deluxe: เล่นได้ที่ Nintendo Switch Zone
- Mario Party Superstars: เล่นได้ที่ Nintendo Switch Zone
- New Super Mario Bros. U Deluxe: เล่นได้ที่ Nintendo Switch Zone
- Super Mario Odyssey: เล่นได้ที่ Nintendo Switch Zone
ถ้าหมายถึงเกมไหนเป็นพิเศษ สามารถพิมพ์ชื่อเกมเต็มเพื่อให้ผมตอบเฉพาะเกมนั้นได้ครับ
```

ถ้าผู้ใช้ถามชื่อชัด:

```text
อยากเล่น Mario Kart
```

ระบบตอบเฉพาะเกม:

```text
เล่น Mario Kart 8 Deluxe ได้ครับ
มีให้เล่นที่: Nintendo Switch Zone
```

ถ้าเกมไม่มีในฐาน:

```text
อยากเล่น Pokemon
```

ระบบยัง no-answer เพราะไม่มีข้อมูลยืนยัน

## Ad-hoc test

Questions:

```text
reports/ad_hoc_questions_partial_game_name_20260706.txt
```

Report:

```text
reports/ad_hoc_pipeline_results_partial_game_name_20260706.md
reports/ad_hoc_pipeline_results_partial_game_name_20260706.jsonl
```

ผล:

```text
questions=12
routes:
- games/game_availability_lookup: 12
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

Competition challenger v2:

```text
Total: 369
PASS: 369
FAIL: 0
Pass rate: 100.00%
```

## Deploy folder

sync จาก `18` ไป `20` แล้ว:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

compile deploy folder ผ่าน:

```text
py_compile app/runtime/fast_answer.py app/pipeline/router.py app/pipeline/engine.py api/chat.py api/health.py
```

ทดสอบจากโฟลเดอร์ `20` แล้ว:

```text
อยากเล่น Mario -> games_family_availability_fast_path
อยากเล่นมาริโอ -> games_family_availability_fast_path
อยากเล่น Mario Kart -> games_availability_fast_path
อยากเล่น Pokemon -> games_unknown_fast_path
```

