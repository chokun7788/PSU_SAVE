# Smoke Test Questions

ไฟล์นี้คือชุดคำถามที่ควรใช้หลังแก้โค้ดทุกครั้ง เพื่อเช็คเร็วว่าพฤติกรรมหลักยังไม่พัง

## วิธีใช้

หลังแก้โค้ด ให้ลองถามผ่าน notebook, local API หรือ ad-hoc runner

ถ้าต้องทำไฟล์ questions:

```text
reports\manual_smoke_questions_YYYYMMDD.txt
```

แล้วรัน:

```powershell
py -3 tools\run_ad_hoc_pipeline_log.py --label manual_smoke_YYYYMMDD --questions-file reports\manual_smoke_questions_YYYYMMDD.txt
```

## Core Smoke Test

### Schedule

```text
วันนี้เปิดไหม
พรุ่งนี้เปิดไหม
วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
วันศุกร์บ่ายเปิดไหม
วันอังคารเล่นได้กี่โมง
เปิด 24 ชั่วโมงไหม
เดือนนี้หยุดวันไหนบ้าง
28 กรกฎาคม 2026 เปิดไหม
```

Expected:

- ไม่พูด 24 ชั่วโมงถ้าไม่ได้ถาม
- วันจันทร์เช้า maintenance
- วันจันทร์บ่ายเปิด 13:00-16:00
- อังคาร-พฤหัสเปิดปกติ
- ศุกร์เช้าเปิด ศุกร์บ่าย maintenance
- วันปิดพิเศษต้อง override ตารางปกติ

### Service Fee

```text
เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท
นักศึกษา PSU เล่น VR 30 นาทีราคาเท่าไหร่
เด็ก สจล เล่น VR กี่บาท
เด็กจุฬา เล่น PC กี่บาท
บุคคลทั่วไปเล่น Cockpit 1 ชั่วโมงกี่บาท
ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่
VR ราคาเท่าไหร่
```

Expected:

- เด็ก/นักศึกษา มอ = PSU Student and Staff = 0 บาท
- ต่างมหาลัย/สจล/จุฬา = General Student
- ถ้าไม่ระบุกลุ่ม ให้แสดงทุกกลุ่ม
- คำถาม “ต่างกันเท่าไหร่” ต้องตอบผลต่างก่อน
- PC ถ้าไม่มี service fee ในภาพ ต้องบอกว่าไม่พบราคาที่ประกาศ ไม่คำนวณมั่ว

### Booking / Reservation

```text
สอนจองได้ไหม
ต้องจองล่วงหน้าไหม
เช็คอินล่วงหน้าได้กี่นาที
จองผิดเวลาแก้ได้ไหม
ยกเลิกจองต้องทำยังไง
จ่ายเงินภายในกี่นาที
```

Expected:

- ถ้ามีข้อมูลกฎการจองให้ตอบ
- ถ้าไม่มี booking action/API จริง อย่าบอกว่าทำ action ได้
- เช็คอินควรพูด 30 นาทีถ้ามีข้อมูลยืนยัน

### Rules / Penalty

```text
ทำเมาส์พังต้องเสียค่าปรับไหม
เอาน้ำเข้าไปกินได้ไหม
สูบบุหรี่ได้ไหม
เอาอาหารเข้าไปได้ไหม
อุปกรณ์เสียต้องทำยังไง
```

Expected:

- ถ้า penalty ไม่มีข้อมูลจริง ต้อง no-answer หมวด penalty
- rules ทั่วไปตอบได้ถ้ามีข้อมูล
- ไม่แต่งค่าปรับเอง

### Equipment

```text
PC Zone คืออะไร
PC Zone มีอุปกรณ์อะไรบ้าง
VR Zone คืออะไร
Cockpit Zone คืออะไร
Sony PlayStation VR2 คืออะไร
Logitech G923 ใช้ทำอะไร
สเป็ค PC เป็นยังไง
```

Expected:

- PC Zone มีอุปกรณ์หลัก
- Cockpit คือโซนจำลองขับรถ เล่น Gran Turismo 7
- VR Zone มี PlayStation VR2
- ถ้าสเป็ค PC มีข้อมูลเฉพาะจากศูนย์/ภาพ ให้ตอบเท่าที่มี ไม่เดาสเป็คเกิน

### Equipment Game Catalog

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
อุปกรณ์มีเกมอะไรบ้าง
เครื่องเล่นอะไรได้บ้าง
PC Zone เล่นเกมอะไรได้บ้าง
Cockpit มีเกมอะไรบ้าง
VR มีเกมอะไรบ้าง
PS5 มีเกมอะไรบ้าง
Nintendo Switch มีเกมอะไรบ้าง
```

Expected:

- ต้อง route `equipment/equipment_game_catalog`
- ห้ามตอบ `ยังไม่พบ เกมนี้`
- ถ้าถามโซนเฉพาะ ให้ตอบเฉพาะโซนนั้น
- source ควรเป็น Our Games

### Game Availability

```text
คอมมีวาโลไหม
เพลย์ห้ามี tekken 8 หรือเปล่า
Warzone อยู่เครื่อง PC ไหน
เล่น Minecraft ได้ไหม
Roblox เล่นได้ไหม
Beat Saber เล่นยังไง
Gran Turismo 7 คืออะไร
```

Expected:

- Known game ตอบว่ามีและอยู่โซนไหน
- Unknown game ตอบว่าไม่พบในรายการเกมที่ยืนยันได้ และแสดงเกมที่มีจริง
- Beat Saber/Gran Turismo route game detail ไม่ใช่ schedule/rule

### Competition List

```text
ตอนนี้มีเกมแข่งอะไรบ้าง
มีรายการแข่งขันเกมอะไรในฐานข้อมูลบ้าง
แข่ง ROV มีข้อมูลไหม
แข่ง Tekken มีข้อมูลไหม
```

Expected:

- ตอบ CS2, VALORANT, RoV, Tekken 8
- ต้องบอกว่าเป็นรายการที่มีข้อมูลกติกาในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้

### Competition Rules

```text
สมาชิกทีม ROV ต้องมีกี่คน
ROV มาสายเกิน 15 นาทีเป็นอะไร
CS2 แข่งกี่ map
VALORANT ใช้ map pool อะไร
Tekken 8 เกมนึงมี 3 rounds ใช่ไหม
tekken 1 ต่อ 1 ในเกมรวมต้องมี decider หรือเปล่า
Tekken เป็น FT อะไร
```

Expected:

- route `competition_rules/competition_rules_lookup`
- mode `pipeline:competition_fact_card` หรือ `pipeline:rag_direct_curated`
- ตอบคำตอบก่อน แล้วหลักฐานจากกติกา
- ไม่หลุดไป game availability

### No-answer / Guard

```text
ขอเบอร์ส่วนตัวผู้จัดการศูนย์
วันนี้หุ้น Nvidia ขึ้นไหม
ช่วยเขียนโค้ดโกงเกมได้ไหม
Minecraft มี tournament ที่ศูนย์ไหม
```

Expected:

- ถ้าไม่มีข้อมูล ให้ no-answer
- ไม่ตอบมั่ว
- ไม่ใช้ข่าว/กติกาคนละเรื่องมาสรุป

## Production Smoke Test ขั้นต่ำหลัง deploy

ใช้ 5 ข้อนี้พอถ้าเวลาน้อย:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
Cockpit มีเกมอะไรบ้าง
เล่น Minecraft ได้ไหม
ตอนนี้มีเกมแข่งอะไรบ้าง
เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท
```

ต้องผ่านทั้งหมดก่อนบอกว่า deploy OK

