# Calendar / Time Context Implementation 2026-07-06

## Summary

เพิ่ม calendar/time context ให้ระบบตอบคำถามวันที่ เวลา วันหยุดไทย/เทศกาล และช่วงให้บริการปัจจุบันได้จากข้อมูลกลางชุดเดียวกัน

งานนี้ยังยึดหลักเดิม:

- วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ
- การปิดบริการจริงของ PSU Esports Studio - Phuket ยืนยันจาก `data/calendar/service_closures.jsonl` เท่านั้น
- ถ้าไม่มีวันปิดพิเศษในไฟล์ service closures จะไม่เดาเองว่าศูนย์ปิด

## Changed Files

- `app/calendar/service_calendar.py`
  - เพิ่ม `now_bangkok()`
  - เพิ่ม `calendar_context()`
  - เพิ่ม `current_service_slot()`
  - เพิ่ม loader สำหรับวันหยุด/เทศกาลไทย
  - เพิ่มรายการ slot ประจำวันตามตารางบริการ
- `data/calendar/thai_holidays_2026.jsonl`
  - เพิ่มรายการวันหยุด/เทศกาลไทยปี 2026
  - แยก `type` เช่น `national_holiday`, `observance`, `government_holiday`, `bank_holiday_bangkok`
- `app/runtime/fast_answer.py`
  - เพิ่มคำตอบสำหรับ:
    - `วันนี้วันที่เท่าไหร่`
    - `ตอนนี้กี่โมง`
    - `ตอนนี้เล่นช่วงไหนได้บ้าง`
    - `วันนี้เป็นวันหยุดไทยไหม`
    - `เดือนนี้มีวันหยุดไทยอะไรบ้าง`
    - `29 กรกฎาคม 2026 เป็นวันหยุดอะไร`
  - คำตอบยัง answer-first และบอกแหล่งข้อมูล
- `app/pipeline/router.py`
  - ปรับ route ให้คำถามวันที่/ปฏิทินไม่โดนตีเป็น service fee เพราะคำว่า `เท่าไหร่`
  - ปรับ route ให้คำถามวันที่ปี 2026 ไม่โดน broad news/event route
- `app/web_api/server.py`
  - เพิ่ม `GET /api/calendar`
  - เพิ่ม `calendar` และ `server_date` ที่มีเวลา, service slot, วันหยุดไทยใน response ของ `/api/chat`
- `web_chat/app.js`
  - date chip แสดงเวลาเพิ่มถ้า API ส่ง `server_date.time`
- Deploy folder `20_PSU_Esports_Vercel_Deploy`
  - ซิงก์ `app`, `data`, `web_chat`
  - เพิ่ม `api/calendar.py`
  - ปรับ `api/chat.py` ให้ส่ง calendar context เหมือน local API

## API Shape

`/api/chat` จะมี field เพิ่ม:

- `server_date.time`
- `server_date.datetime_iso`
- `server_date.service_slot`
- `server_date.thai_holidays`
- `server_date.upcoming_thai_holidays`
- `calendar`

เพิ่ม endpoint:

- `GET /api/calendar`

ตัวอย่าง `service_slot.status`:

- `open`
- `maintenance`
- `closed`
- `outside_hours`

## Important Behavior

ตัวอย่างวันที่ mock: `2026-07-06T14:30:00+07:00`

- `ตอนนี้เล่นช่วงไหนได้บ้าง`
  - ตอบว่าเล่นได้ อยู่ช่วง `Afternoon 13:00-16:00`
- `วันนี้วันที่เท่าไหร่`
  - ตอบวันที่ `06/07/2026 (วันจันทร์)` และเวลาระบบ
- `เดือนนี้มีวันหยุดไทยอะไรบ้าง`
  - ตอบรายการปฏิทินไทย 28/29/30 กรกฎาคม 2026
  - ยังบอกวันปิดบริการของศูนย์จาก `service_closures.jsonl`
- `ตอนนี้รายการแข่งมเกมอะไรบ้าง`
  - ยังเข้า route `games/competition_game_list`
- `ตอนนี้อยากเล่น Tekken 8`
  - ยังเข้า route `games/game_availability_lookup`

## Sources

- Bank of Thailand Financial Institutions Holiday 2026: https://www.bot.or.th/en/financial-institutions-holiday.html
- Time and Date Thailand holidays 2026: https://www.timeanddate.com/holidays/thailand/2026
- PSU Esports reservation schedule: https://esports.computing.psu.ac.th/reservation

## Validation

ผ่าน:

- `python -m py_compile app\calendar\service_calendar.py app\runtime\fast_answer.py app\pipeline\router.py app\web_api\server.py`
- `python tools\validate_update.py`
- `python tests\smoke_test_fast_runtime.py`
- `python tests\smoke_test_answer_pipeline.py`
- Ad hoc calendar/time context:
  - `reports/ad_hoc_pipeline_results_calendar_time_context_fix2_20260706.md`
- GT360:
  - PASS 360/360
  - `reports/pipeline_ground_truth_report_calendar_time_context_gt360_20260706.md`
- Competition challenger v2:
  - PASS 369/369
  - `reports/pipeline_ground_truth_report_calendar_time_context_comp_v2_20260706.md`
- Deploy folder compile:
  - `python -m py_compile app\calendar\service_calendar.py app\runtime\fast_answer.py app\pipeline\router.py api\chat.py api\health.py api\calendar.py`
- Deploy folder API smoke with temporary Flask dependency:
  - `/api/chat` returned `pipeline:current_service_slot_fast_path`
  - `/api/calendar` returned `date=2026-07-06`, `time=14:30`, `service_slot.status=open`

## Deploy Note

ซิงก์โค้ดไป `20_PSU_Esports_Vercel_Deploy` แล้ว แต่ไม่ได้ deploy production ตามคำสั่งผู้ใช้
