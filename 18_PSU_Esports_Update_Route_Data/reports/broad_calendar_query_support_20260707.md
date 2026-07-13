# Broad Calendar Query Support - 2026-07-07

## เป้าหมาย

เพิ่มความสามารถตอบคำถามเกี่ยวกับวันที่/เดือน/ปี/วันหยุดให้ครอบคลุมขึ้น โดยไม่ใช้ paid API และยังตอบเร็วจาก local data

ตัวอย่างคำถามที่ต้องรองรับ:

- วันนี้วันที่เท่าไหร่
- อีก 10 วันคือวันอะไร
- อีก 3 สัปดาห์คือวันอะไร
- เดือนที่แล้วมีวันหยุดอะไรบ้าง
- ปี 2569 มีวันหยุดกี่วัน
- ปี 2569 มีวันหยุดอะไรบ้าง

## สิ่งที่เพิ่ม

ไฟล์หลัก:

- `app/calendar/service_calendar.py`
- `app/runtime/fast_answer.py`
- `app/pipeline/router.py`

เพิ่ม resolver:

- `resolve_date_from_text()`
  - วันนี้
  - พรุ่งนี้
  - มะรืน
  - อีก N วัน
  - N วันข้างหน้า
  - N วันก่อน
  - อีก N สัปดาห์
  - วันที่แบบตัวเลข
  - วันที่ + เดือนภาษาไทย
- `resolve_month_from_text()`
  - เดือนนี้
  - เดือนหน้า
  - เดือนที่แล้ว / เดือนก่อน
  - ชื่อเดือนเต็มและภาษาพูด เช่น `ธันวา`, `ตุลา`, `กันยา`
  - ปี พ.ศ. เช่น `2569`
- `resolve_year_from_text()`
  - ปีนี้
  - ปีหน้า
  - ปีที่แล้ว / ปีก่อน
  - ปี พ.ศ. / ค.ศ. เช่น `2569`, `2026`

เพิ่ม query answer:

- date context
- month holiday context
- year holiday context
- year holiday count

## แหล่งข้อมูล

ระบบไม่ได้เรียก API สดตอนตอบ

ข้อมูลวันหยุดอ่านจาก local file:

- `data/calendar/thai_holidays_2026.jsonl`

ไฟล์นี้มี `source_url` อ้างอิง เช่น:

- Time and Date Thailand holidays 2026
- Bank of Thailand Financial Institutions Holidays 2026 สำหรับบางรายการ

ข้อมูลวันปิดบริการของศูนย์อ่านจาก:

- `data/calendar/service_closures.jsonl`

## ผลทดสอบ Smoke ในโฟลเดอร์ 20

- `วันนี้วันที่เท่าไหร่`
  - `schedule/schedule_query`
  - `pipeline:calendar_date_context_fast_path`
- `อีก10วันคือวันอะไร`
  - `schedule/schedule_query`
  - `pipeline:calendar_date_context_fast_path`
  - ตอบ `อีก 10 วันคือ 17/07/2026 (วันศุกร์)`
- `อีก 3 สัปดาห์คือวันอะไร`
  - ตอบ `28/07/2026 (วันอังคาร)`
- `เดือนที่แล้วมีวันหยุดอะไรบ้าง`
  - `pipeline:calendar_month_context_fast_path`
  - ตอบเดือนมิถุนายน 2026 / พ.ศ. 2569 มี 2 รายการ
- `ปี2569มีวันหยุดกี่วัน`
  - `pipeline:calendar_year_context_fast_path`
  - ตอบวันหยุด/วันหยุดราชการ 23 รายการ และรายการปฏิทินไทยรวม 34 รายการ
- `ปี 2569 มีวันหยุดอะไรบ้าง`
  - `pipeline:calendar_year_context_fast_path`
  - ตอบรายการปฏิทินไทยทั้งปี
- `ดือนธันวา 2569 มีวันหยุดอะไรบ้าง`
  - `pipeline:calendar_month_context_fast_path`
  - ตอบเดือนธันวาคม 2026 / พ.ศ. 2569 ได้ถูกต้อง

Compile:

- `python -m compileall app` ผ่านทั้งโฟลเดอร์ 18 และ 20

ไม่ได้ run Ground Truth ตามคำสั่งผู้ใช้

## ข้อจำกัด

- ตอนนี้ข้อมูลวันหยุด local มีปี 2026 / พ.ศ. 2569 เป็นหลัก
- ถ้าถามปีที่ไม่มีข้อมูล ระบบควรตอบ no-answer/ยังไม่มีข้อมูล ไม่ควรเดา
- วันหยุดไทย/เทศกาลไม่ได้แปลว่าศูนย์ปิดอัตโนมัติ การปิดบริการจริงต้องดู `service_closures.jsonl`
- ยังไม่ได้เชื่อม API สด เพราะผู้ใช้ต้องการไม่ใช้ API เสียเงินและต้องตอบเร็ว
