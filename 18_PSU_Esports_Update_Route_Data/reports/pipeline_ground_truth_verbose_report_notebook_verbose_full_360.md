# Ground Truth Verbose Result

- Total: 360
- PASS: 356
- FAIL: 4
- ERROR: 0
- Pass rate: 98.89%
- Average latency: 0.0108s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_notebook_verbose_full_360.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_notebook_verbose_full_360.md`

## Mode Summary
- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 46
- `pipeline:guard_no_answer`: 25
- `pipeline:games_fast_path`: 21
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:checkin_fast_path`: 12
- `pipeline:penalty_fast_path`: 11
- `pipeline:payment_fast_path`: 10
- `pipeline:equipment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:knowledge_fast_path`: 7
- `pipeline:overview_fast_path`: 5
- `pipeline:news_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:mixed_reservation_fast`: 4
- `pipeline:competition_fact_card`: 2
- `pipeline:mixed_rules_fast`: 2
- `pipeline:rag_direct_curated`: 2
- `pipeline:calendar_schedule_fast_path`: 2
- `pipeline:category_rule_fast_path`: 1

## Route Summary
- `service_fee`: 139
- `schedule`: 48
- `reservation`: 47
- `no_answer`: 25
- `games`: 22
- `rules`: 22
- `penalty`: 11
- `contact`: 10
- `equipment`: 9
- `knowledge`: 9
- `overview`: 9
- `events_news`: 5
- `competition_rules`: 4
## 1. [PASS] ถูก

**คำถาม:** วันจันทร์เปิดให้เล่นกีโมง ปิดกี่โมง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.008` sec

## 2. [PASS] ถูก

**คำถาม:** วันจันทร์เปิดให้เล่นกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0052` sec

## 3. [PASS] ถูก

**คำถาม:** จันทร์เปิดปิดยังไง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0029` sec

## 4. [PASS] ถูก

**คำถาม:** วันจันทร์เล่นได้ตั้งแต่กี่โมง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0038` sec

## 5. [PASS] ถูก

**คำถาม:** วันจันทร์มีรอบเล่นช่วงไหนบ้าง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0038` sec

## 6. [PASS] ถูก

**คำถาม:** Monday open close time?

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0076` sec

## 7. [PASS] ถูก

**คำถาม:** monday hours for play

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0063` sec

## 8. [PASS] ถูก

**คำถาม:** ถ้าไปวันจันทร์เช้าเล่นได้ไหม แล้วเปิดจริงกี่โมง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.008` sec

## 9. [PASS] ถูก

**คำถาม:** วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม

**คำตอบ(จาก AI):**

วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0121` sec

## 10. [PASS] ถูก

**คำถาม:** จันทร์เช้า maintenance แล้วบ่ายเปิดกี่โมง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_day_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0099` sec

## 11. [PASS] ถูก

**คำถาม:** วันจันทร์ช่วงเช้าเปิดไหม

**คำตอบ(จาก AI):**

วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0032` sec

## 12. [PASS] ถูก

**คำถาม:** จันทร์ 9 โมงเล่นได้ไหม

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0071` sec

## 13. [PASS] ถูก

**คำถาม:** Monday morning available?

**คำตอบ(จาก AI):**

วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0048` sec

## 14. [PASS] ถูก

**คำถาม:** วันจันทร์ 09:00-12:00 เป็นอะไร

**คำตอบ(จาก AI):**

วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0117` sec

## 15. [PASS] ถูก

**คำถาม:** เช้าวันจันทร์เป็น maintenance ใช่ไหม

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0076` sec

## 16. [PASS] ถูก

**คำถาม:** ศูนย์เปิดกีโมงปิดกี่โมง

**คำตอบ(จาก AI):**

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0037` sec

## 17. [PASS] ถูก

**คำถาม:** เปิดปิดกี่โมงนะ

**คำตอบ(จาก AI):**

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0029` sec

## 18. [PASS] ถูก

**คำถาม:** เวลาเปิดให้บริการคืออะไร

**คำตอบ(จาก AI):**

เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0036` sec

## 19. [PASS] ถูก

**คำถาม:** service hours คืออะไร

**คำตอบ(จาก AI):**

เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0053` sec

## 20. [PASS] ถูก

**คำถาม:** เปิดถึง 16:00 ใช่ไหม

**คำตอบ(จาก AI):**

เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0067` sec

## 21. [PASS] ถูก

**คำถาม:** เปิด 24 ชม ไหม

**คำตอบ(จาก AI):**

ไม่เปิด 24 ชั่วโมง ตามข้อมูลที่มี ศูนย์ใช้ช่วงเวลา Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยต้องดูวัน Maintenance ประกอบ

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_general

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0062` sec

## 22. [PASS] ถูก

**คำถาม:** ช่วงเช้าของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0053` sec

## 23. [PASS] ถูก

**คำถาม:** Morning คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0058` sec

## 24. [PASS] ถูก

**คำถาม:** รอบเช้า 09 ถึง 12 ใช่ไหม

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0099` sec

## 25. [PASS] ถูก

**คำถาม:** ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0043` sec

## 26. [PASS] ถูก

**คำถาม:** ตอนเช้าเปิดกี่โมง

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0035` sec

## 27. [PASS] ถูก

**คำถาม:** รอบเช้าเริ่มตอนไหน

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0032` sec

## 28. [PASS] ถูก

**คำถาม:** morning session time?

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0055` sec

## 29. [PASS] ถูก

**คำถาม:** morning slot time

**คำตอบ(จาก AI):**

รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_morning

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0048` sec

## 30. [PASS] ถูก

**คำถาม:** ช่วงบ่ายของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0044` sec

## 31. [PASS] ถูก

**คำถาม:** Afternoon คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0051` sec

## 32. [PASS] ถูก

**คำถาม:** รอบบ่าย 13 ถึง 16 ใช่ไหม

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0099` sec

## 33. [PASS] ถูก

**คำถาม:** ช่วงบ่ายเปิดกี่โมงปิดกี่โมง

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0033` sec

## 34. [PASS] ถูก

**คำถาม:** รอบบ่ายปิดกี่โมง

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0035` sec

## 35. [PASS] ถูก

**คำถาม:** afternoon session time?

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0047` sec

## 36. [PASS] ถูก

**คำถาม:** afternoon slot time

**คำตอบ(จาก AI):**

รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_afternoon

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0059` sec

## 37. [PASS] ถูก

**คำถาม:** วันศุกร์ maintenance คืออะไร

**คำตอบ(จาก AI):**

วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0067` sec

## 38. [PASS] ถูก

**คำถาม:** Friday maintenance ทำอะไร

**คำตอบ(จาก AI):**

วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0065` sec

## 39. [PASS] ถูก

**คำถาม:** maintenance weekly hardware inspection คืออะไร

**คำตอบ(จาก AI):**

เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0109` sec

## 40. [PASS] ถูก

**คำถาม:** วันศุกร์มีตรวจอุปกรณ์ไหม

**คำตอบ(จาก AI):**

วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0039` sec

## 41. [PASS] ถูก

**คำถาม:** ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม

**คำตอบ(จาก AI):**

วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_maintenance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0043` sec

## 42. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0087` sec

## 43. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0092` sec

## 44. [PASS] ถูก

**คำถาม:** PS5 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0077` sec

## 45. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0115` sec

## 46. [PASS] ถูก

**คำถาม:** PS5 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.009` sec

## 47. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0113` sec

## 48. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0086` sec

## 49. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0089` sec

## 50. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0092` sec

## 51. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0101` sec

## 52. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0091` sec

## 53. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0103` sec

## 54. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0221` sec

## 55. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0239` sec

## 56. [PASS] ถูก

**คำถาม:** คนนอก เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.021` sec

## 57. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0258` sec

## 58. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0251` sec

## 59. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0248` sec

## 60. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0123` sec

## 61. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0091` sec

## 62. [PASS] ถูก

**คำถาม:** Nintendo 1-2 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0096` sec

## 63. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0108` sec

## 64. [PASS] ถูก

**คำถาม:** Nintendo 1-2 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0123` sec

## 65. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0109` sec

## 66. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0122` sec

## 67. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0098` sec

## 68. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0125` sec

## 69. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.01` sec

## 70. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0142` sec

## 71. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0098` sec

## 72. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0295` sec

## 73. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0261` sec

## 74. [PASS] ถูก

**คำถาม:** คนนอก เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0284` sec

## 75. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0262` sec

## 76. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0357` sec

## 77. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0261` sec

## 78. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0119` sec

## 79. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0087` sec

## 80. [PASS] ถูก

**คำถาม:** Nintendo 3-4 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0108` sec

## 81. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0153` sec

## 82. [PASS] ถูก

**คำถาม:** Nintendo 3-4 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.011` sec

## 83. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0118` sec

## 84. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0122` sec

## 85. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0081` sec

## 86. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0128` sec

## 87. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.011` sec

## 88. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0131` sec

## 89. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0115` sec

## 90. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0428` sec

## 91. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0296` sec

## 92. [PASS] ถูก

**คำถาม:** คนนอก เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0312` sec

## 93. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0255` sec

## 94. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0347` sec

## 95. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.03` sec

## 96. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0154` sec

## 97. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0132` sec

## 98. [PASS] ถูก

**คำถาม:** Cockpit สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.008` sec

## 99. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0117` sec

## 100. [PASS] ถูก

**คำถาม:** Cockpit สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0136` sec

## 101. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0173` sec

## 102. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0127` sec

## 103. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0154` sec

## 104. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0165` sec

## 105. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0096` sec

## 106. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.013` sec

## 107. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0128` sec

## 108. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.029` sec

## 109. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0275` sec

## 110. [PASS] ถูก

**คำถาม:** คนนอก เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0254` sec

## 111. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0262` sec

## 112. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.029` sec

## 113. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0293` sec

## 114. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.012` sec

## 115. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0116` sec

## 116. [PASS] ถูก

**คำถาม:** VR 30 นาที สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0153` sec

## 117. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0164` sec

## 118. [PASS] ถูก

**คำถาม:** VR 30 นาที สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0188` sec

## 119. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.016` sec

## 120. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0172` sec

## 121. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0149` sec

## 122. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0215` sec

## 123. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0167` sec

## 124. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0261` sec

## 125. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0202` sec

## 126. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0515` sec

## 127. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0489` sec

## 128. [PASS] ถูก

**คำถาม:** คนนอก เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0434` sec

## 129. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0314` sec

## 130. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0454` sec

## 131. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0315` sec

## 132. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0112` sec

## 133. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0096` sec

## 134. [PASS] ถูก

**คำถาม:** VR 1 ชั่วโมง สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0106` sec

## 135. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0112` sec

## 136. [PASS] ถูก

**คำถาม:** VR 1 ชั่วโมง สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0124` sec

## 137. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0128` sec

## 138. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0116` sec

## 139. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0107` sec

## 140. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0176` sec

## 141. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0178` sec

## 142. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.014` sec

## 143. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0143` sec

## 144. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0416` sec

## 145. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0275` sec

## 146. [PASS] ถูก

**คำถาม:** คนนอก เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0276` sec

## 147. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0295` sec

## 148. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0362` sec

## 149. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: medium | variant: price_synonym

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0275` sec

## 150. [PASS] ถูก

**คำถาม:** ราคา PC ต่อชั่วโมงเท่าไหร่

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.022` sec

## 151. [PASS] ถูก

**คำถาม:** นักเรียน มอ เล่น PC ฟรีไหม

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0074` sec

## 152. [PASS] ถูก

**คำถาม:** คนนอกเล่นคอมต้องจ่ายเท่าไหร่

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0127` sec

## 153. [PASS] ถูก

**คำถาม:** PC มีราคาใน service fee ไหม

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0308` sec

## 154. [PASS] ถูก

**คำถาม:** ทำไมคำนวณ PC ไม่ได้

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0181` sec

## 155. [PASS] ถูก

**คำถาม:** จอง PC 9 ถึง 11 ต้องเสียกี่บาท

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0363` sec

## 156. [PASS] ถูก

**คำถาม:** ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0311` sec

## 157. [PASS] ถูก

**คำถาม:** PC price for general student?

**คำตอบ(จาก AI):**

ราคา PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น
ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: price_missing_data

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0096` sec

## 158. [PASS] ถูก

**คำถาม:** ราคาค่าบริการทั้งหมดมีอะไรบ้าง

**คำตอบ(จาก AI):**

ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0113` sec

## 159. [PASS] ถูก

**คำถาม:** สรุป service fee ให้หน่อย

**คำตอบ(จาก AI):**

ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0192` sec

## 160. [PASS] ถูก

**คำถาม:** ตารางราคา 2026 มีอะไร

**คำตอบ(จาก AI):**

ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0176` sec

## 161. [PASS] ถูก

**คำถาม:** ค่าเล่นแต่ละเครื่องเท่าไหร่

**คำตอบ(จาก AI):**

ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.009` sec

## 162. [PASS] ถูก

**คำถาม:** service fee table includes what

**คำตอบ(จาก AI):**

ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0221` sec

## 163. [PASS] ถูก

**คำถาม:** ขอเรทราคา PS5 Switch Cockpit VR

**คำตอบ(จาก AI):**

PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: list | ระดับ: medium | variant: price_summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0285` sec

## 164. [PASS] ถูก

**คำถาม:** จองต้องล่วงหน้ากี่ชั่วโมง

**คำตอบ(จาก AI):**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0046` sec

## 165. [PASS] ถูก

**คำถาม:** ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง

**คำตอบ(จาก AI):**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0047` sec

## 166. [PASS] ถูก

**คำถาม:** ต้อง book ล่วงหน้ากี่ hr

**คำตอบ(จาก AI):**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0072` sec

## 167. [PASS] ถูก

**คำถาม:** จองก่อน 1 ชั่วโมงใช่ไหม

**คำตอบ(จาก AI):**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0076` sec

## 168. [PASS] ถูก

**คำถาม:** walk in ได้ไหมหรือต้องจองก่อน

**คำตอบ(จาก AI):**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0064` sec

## 169. [PASS] ถูก

**คำถาม:** จองได้สูงสุดกี่ session

**คำตอบ(จาก AI):**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_max_session

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0043` sec

## 170. [PASS] ถูก

**คำถาม:** ครั้งนึงจองได้กี่รอบ

**คำตอบ(จาก AI):**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_max_session

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0046` sec

## 171. [PASS] ถูก

**คำถาม:** one booking max sessions?

**คำตอบ(จาก AI):**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_max_session

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.006` sec

## 172. [PASS] ถูก

**คำถาม:** จองทีเดียว 4 sessions ได้ไหม

**คำตอบ(จาก AI):**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_max_session

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0096` sec

## 173. [PASS] ถูก

**คำถาม:** จองสามรอบได้ไหม

**คำตอบ(จาก AI):**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_max_session

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0031` sec

## 174. [PASS] ถูก

**คำถาม:** หลังจองต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_timeout

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0036` sec

## 175. [PASS] ถูก

**คำถาม:** ไม่จ่ายใน 10 นาทีจะเกิดอะไร

**คำตอบ(จาก AI):**

หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_timeout

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0076` sec

## 176. [PASS] ถูก

**คำถาม:** payment timeout กี่นาที

**คำตอบ(จาก AI):**

หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_timeout

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0057` sec

## 177. [PASS] ถูก

**คำถาม:** จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม

**คำตอบ(จาก AI):**

หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_timeout

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0068` sec

## 178. [PASS] ถูก

**คำถาม:** ชำระเงินหลัง booking ต้องเร็วแค่ไหน

**คำตอบ(จาก AI):**

หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_timeout

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0082` sec

## 179. [PASS] ถูก

**คำถาม:** กดจองแล้วแก้ไขได้ไหม

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_edit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0029` sec

## 180. [PASS] ถูก

**คำถาม:** ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_edit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0045` sec

## 181. [PASS] ถูก

**คำถาม:** แก้เวลา booking ได้ไหม

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_edit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0068` sec

## 182. [PASS] ถูก

**คำถาม:** ต้องยกเลิกแล้วจองใหม่ใช่ไหม

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_edit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0037` sec

## 183. [PASS] ถูก

**คำถาม:** แนบสลิปเดิมตอนจองใหม่ได้ไหม

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_edit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0034` sec

## 184. [PASS] ถูก

**คำถาม:** สิทธิ์การจองโอนให้เพื่อนได้ไหม

**คำตอบ(จาก AI):**

ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_transfer

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.004` sec

## 185. [PASS] ถูก

**คำถาม:** ให้คนอื่นมาใช้ booking แทนได้ไหม

**คำตอบ(จาก AI):**

ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_transfer

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0082` sec

## 186. [PASS] ถูก

**คำถาม:** transfer booking ได้ไหม

**คำตอบ(จาก AI):**

ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_transfer

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.006` sec

## 187. [PASS] ถูก

**คำถาม:** จองแทนกันได้ไหม

**คำตอบ(จาก AI):**

ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์ | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: booking_transfer

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0026` sec

## 188. [PASS] ถูก

**คำถาม:** เช็คอินล่วงหน้าได้กี่นาที

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0053` sec

## 189. [PASS] ถูก

**คำถาม:** check in ได้เร็วสุดกี่นาที

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0047` sec

## 190. [PASS] ถูก

**คำถาม:** เช็คอินก่อนเวลาได้ 1800 วินาทีไหม

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0098` sec

## 191. [PASS] ถูก

**คำถาม:** ต้องเช็คอินก่อนเริ่มรอบใช่ไหม

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_advance

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0045` sec

## 192. [PASS] ถูก

**คำถาม:** ถ้า check-in ไม่ทันจะโดนอะไร

**คำตอบ(จาก AI):**

ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/](https://esports.computing.psu.ac.th/) (`rule_checkin_late / reservation / rule_checkin_late`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, ไม่มีการคืนเงิน | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_late

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:category_rule_fast_path` | elapsed: `0.0064` sec

## 193. [PASS] ถูก

**คำถาม:** เช็คอินต้องใช้บัตรอะไร

**คำตอบ(จาก AI):**

ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บัตรประชาชน | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_id

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0046` sec

## 194. [PASS] ถูก

**คำถาม:** แสดงบัตรประชาชนได้ไหมตอนเช็คอิน

**คำตอบ(จาก AI):**

ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บัตรประชาชน | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin_id

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0038` sec

## 195. [PASS] ถูก

**คำถาม:** ชำระเงินผ่านอะไร

**คำตอบ(จาก AI):**

ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1 | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_method

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0035` sec

## 196. [PASS] ถูก

**คำถาม:** โอนเงินไปบัญชีไหน

**คำตอบ(จาก AI):**

ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1 | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_method

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0028` sec

## 197. [PASS] ถูก

**คำถาม:** ชื่อบัญชีจ่ายค่าจองคืออะไร

**คำตอบ(จาก AI):**

ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1 | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_method

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0047` sec

## 198. [PASS] ถูก

**คำถาม:** เลขบัญชีธนาคารสำหรับจองคืออะไร

**คำตอบ(จาก AI):**

ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1 | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_method

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0046` sec

## 199. [PASS] ถูก

**คำถาม:** ธนาคารที่ใช้รับเงินคืออะไร

**คำตอบ(จาก AI):**

ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1 | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: medium | variant: payment_method

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:payment_fast_path` | elapsed: `0.0037` sec

## 200. [PASS] ถูก

**คำถาม:** PS5 มี Spider-Man 2 ไหม

**คำตอบ(จาก AI):**

PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Spider-Man 2 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_ps5_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0089` sec

## 201. [FAIL] ผิด

**คำถาม:** เพลย์ห้ามี tekken 8 หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_ps5_specific

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `True`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0256` sec
- missing_source_keywords: `['Reservation']`

## 202. [PASS] ถูก

**คำถาม:** เกมบน PlayStation มีอะไรบ้าง

**คำตอบ(จาก AI):**

PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_ps5_list

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0029` sec

## 203. [PASS] ถูก

**คำถาม:** PS5 เล่น Fortnite ได้ไหม

**คำตอบ(จาก AI):**

PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Fortnite | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_ps5_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0093` sec

## 204. [PASS] ถูก

**คำถาม:** มี God of War Ragnarok ไหม

**คำตอบ(จาก AI):**

PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, God of War Ragnarok | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_ps5_specific

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0101` sec

## 205. [PASS] ถูก

**คำถาม:** Switch มี Mario Kart ไหม

**คำตอบ(จาก AI):**

Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_switch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0092` sec

## 206. [PASS] ถูก

**คำถาม:** นินเทนโดมี Overcooked 2 ไหม

**คำตอบ(จาก AI):**

Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Overcooked 2 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_switch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0086` sec

## 207. [PASS] ถูก

**คำถาม:** เกม Nintendo มีอะไรบ้าง

**คำตอบ(จาก AI):**

Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_switch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0063` sec

## 208. [PASS] ถูก

**คำถาม:** เล่น Super Smash Bros ที่ศูนย์ได้ไหม

**คำตอบ(จาก AI):**

Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Super Smash | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_switch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0109` sec

## 209. [PASS] ถูก

**คำถาม:** Switch Sports มีไหม

**คำตอบ(จาก AI):**

Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Switch Sports | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_switch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0049` sec

## 210. [PASS] ถูก

**คำถาม:** PC มี valorant ไหม

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.007` sec

## 211. [FAIL] ผิด

**คำถาม:** คอมเล่น CS2 ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, Counter-Strike 2 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_pc

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0127` sec
- missing_keywords: `['PC']`
- missing_source_keywords: `['Reservation']`

## 212. [PASS] ถูก

**คำถาม:** PC games list

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0044` sec

## 213. [PASS] ถูก

**คำถาม:** มี PUBG บน PC ไหม

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, PUBG | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.008` sec

## 214. [PASS] ถูก

**คำถาม:** Warzone อยู่เครื่อง PC ไหน

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, Warzone | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0085` sec

## 215. [PASS] ถูก

**คำถาม:** VR เล่นเกมอะไร

**คำตอบ(จาก AI):**

VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: list | ระดับ: medium | variant: game_vr

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0046` sec

## 216. [PASS] ถูก

**คำถาม:** Beat Saber มีไหม

**คำตอบ(จาก AI):**

VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_vr

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0048` sec

## 217. [PASS] ถูก

**คำถาม:** แว่น VR มี Horizon ไหม

**คำตอบ(จาก AI):**

VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Horizon | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_vr

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0098` sec

## 218. [PASS] ถูก

**คำถาม:** Cockpit เล่นเกมอะไร

**คำตอบ(จาก AI):**

Cockpit ใช้เล่นเกม Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, Gran Turismo 7 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_cockpit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0045` sec

## 219. [PASS] ถูก

**คำถาม:** พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม

**คำตอบ(จาก AI):**

Cockpit ใช้เล่นเกม Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gran Turismo 7 | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_cockpit

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0035` sec

## 220. [PASS] ถูก

**คำถาม:** PC Zone มีอุปกรณ์อะไรบ้าง

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, Gaming Monitor, Gaming Chair | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: list | ระดับ: medium | variant: equipment_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0068` sec

## 221. [PASS] ถูก

**คำถาม:** คอมที่ศูนย์มีทั้งหมดกี่เครื่อง

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0035` sec

## 222. [PASS] ถูก

**คำถาม:** Gaming PC รุ่นอะไร

**คำตอบ(จาก AI):**

สเปก PC ที่บันทึกไว้ตอนนี้: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, CPU Intel Core i5-14400, RAM DDR5 32GB, GPU NVIDIA GeForce RTX 5060 8GB, Mainboard MSI PRO H610M-G และใน PC Zone มี Gaming PC ทั้งหมด 10 เครื่อง

หมายเหตุ: ข้อมูลนี้มาจากสเปกเครื่อง/ภาพ CPU-Z ที่บันทึกไว้ในโปรเจกต์ ส่วนหน้า Home ระบุรายการอุปกรณ์ PC Zone เช่น Gaming PC, Gaming Monitor, Gaming Chair, Gaming Keyboard, Gaming Mouse และ Gaming Headset
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: MSI MAG Infinite S3, 10 Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0052` sec

## 223. [PASS] ถูก

**คำถาม:** เก้าอี้เกมมิ่งมีไหมใน PC zone

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming Chair, 10 Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0066` sec

## 224. [PASS] ถูก

**คำถาม:** เมาส์กับหูฟังมีให้ไหม

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming Mouse, Gaming Headset | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_pc

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0039` sec

## 225. [PASS] ถูก

**คำถาม:** Cockpit zone มีทีวีขนาดกี่นิ้ว

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_zone

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0059` sec

## 226. [PASS] ถูก

**คำถาม:** พวงมาลัยใช้รุ่นอะไร

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_zone

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0045` sec

## 227. [PASS] ถูก

**คำถาม:** Nintendo zone มีทีวีกี่นิ้ว

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_zone

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0072` sec

## 228. [PASS] ถูก

**คำถาม:** PS5 zone มีเครื่องกี่เครื่อง

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_zone

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0058` sec

## 229. [PASS] ถูก

**คำถาม:** VR zone ใช้แว่นรุ่นอะไร

**คำตอบ(จาก AI):**

อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units | Expected source keywords: home | หมวด: equipment | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment_zone

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `equipment` | intent: `equipment_lookup`
- mode: `pipeline:equipment_fast_path` | elapsed: `0.0073` sec

## 230. [PASS] ถูก

**คำถาม:** เอาขนมเข้าไปกินตรงโต๊ะได้ไหม

**คำตอบ(จาก AI):**

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, พื้นที่ที่กำหนด | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: food_drink_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.004` sec

## 231. [PASS] ถูก

**คำถาม:** กินน้ำในพื้นที่เล่นได้ไหม

**คำตอบ(จาก AI):**

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, พื้นที่ที่กำหนด | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: food_drink_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0049` sec

## 232. [PASS] ถูก

**คำถาม:** ต้องฝากกระเป๋าก่อนไหม

**คำตอบ(จาก AI):**

กรุณาฝากสัมภาระก่อนเข้าใช้บริการ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ฝากสัมภาระ | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: belongings_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0036` sec

## 233. [PASS] ถูก

**คำถาม:** ใช้เสียงดังได้ไหม

**คำตอบ(จาก AI):**

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: งด, เสียงดัง | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: noise_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0059` sec

## 234. [PASS] ถูก

**คำถาม:** พูดจาเสียดสีคนอื่นได้ไหม

**คำตอบ(จาก AI):**

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, เสียดสี | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: noise_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0052` sec

## 235. [PASS] ถูก

**คำถาม:** ทิ้งขยะไว้ในโซนเล่นได้ไหม

**คำตอบ(จาก AI):**

ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ทิ้งขยะ | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: trash_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0044` sec

## 236. [PASS] ถูก

**คำถาม:** สูบบุหรี่ในศูนย์ได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0045` sec

## 237. [PASS] ถูก

**คำถาม:** เอาแอลกอฮอล์เข้าได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0035` sec

## 238. [PASS] ถูก

**คำถาม:** พกมีดเข้าไปได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.004` sec

## 239. [PASS] ถูก

**คำถาม:** เล่นพนันในห้องได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0033` sec

## 240. [PASS] ถูก

**คำถาม:** เอาปลั๊กไฟส่วนตัวมาใช้ได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0057` sec

## 241. [PASS] ถูก

**คำถาม:** ย้ายอุปกรณ์เองได้ไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: prohibited

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0029` sec

## 242. [PASS] ถูก

**คำถาม:** ทำอุปกรณ์เสียหายต้องจ่ายไหม

**คำตอบ(จาก AI):**

ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รับผิดชอบ, ค่าปรับ | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_responsibility

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0039` sec

## 243. [PASS] ถูก

**คำถาม:** รอยขีดข่วนเล็กน้อยโดนปรับเท่าไหร่

**คำตอบ(จาก AI):**

ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_fine

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0056` sec

## 244. [PASS] ถูก

**คำถาม:** เบาะขาดต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_fine

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0051` sec

## 245. [PASS] ถูก

**คำถาม:** หูฟังสายขาดค่าปรับเท่าไหร่

**คำตอบ(จาก AI):**

ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_fine

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0045` sec

## 246. [PASS] ถูก

**คำถาม:** จอแตกต้องชดเชยยังไง

**คำตอบ(จาก AI):**

กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ชดเชย, เต็มจำนวน | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_severe

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0032` sec

## 247. [PASS] ถูก

**คำถาม:** คอมพังต้องจ่ายเต็มไหม

**คำตอบ(จาก AI):**

กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ชดเชย, เต็มจำนวน | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: damage_severe

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0039` sec

## 248. [PASS] ถูก

**คำถาม:** ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน

**คำตอบ(จาก AI):**

หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์ | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0043` sec

## 249. [PASS] ถูก

**คำถาม:** โดนแบนชั่วคราวกี่วัน

**คำตอบ(จาก AI):**

หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์, 1-7 วัน | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty_temp

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0032` sec

## 250. [PASS] ถูก

**คำถาม:** กรณีไหนแบนถาวร

**คำตอบ(จาก AI):**

หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์, ถาวร | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty_permanent

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0036` sec

## 251. [PASS] ถูก

**คำถาม:** อุทธรณ์การลงโทษได้ภายในกี่วัน

**คำตอบ(จาก AI):**

หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 7 วัน | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty_appeal

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.0042` sec

## 252. [PASS] ถูก

**คำถาม:** ศูนย์เก็บประวัติคนทำผิดไหม

**คำตอบ(จาก AI):**

หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บันทึก, ประวัติ | Expected source keywords: Reservation | หมวด: penalty | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty_record

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:penalty_fast_path` | elapsed: `0.004` sec

## 253. [PASS] ถูก

**คำถาม:** ศูนย์นี้คืออะไรแบบสั้นๆ

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | Expected source keywords: home | หมวด: overview | ชนิดคำตอบ: summary | ระดับ: medium | variant: overview

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `overview_lookup`
- mode: `pipeline:overview_fast_path` | elapsed: `0.0032` sec

## 254. [PASS] ถูก

**คำถาม:** PSU Esports Studio Phuket คืออะไร

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | Expected source keywords: home | หมวด: overview | ชนิดคำตอบ: summary | ระดับ: medium | variant: overview

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:overview_fast_path` | elapsed: `0.0049` sec

## 255. [PASS] ถูก

**คำถาม:** ใครเป็นคนก่อตั้งศูนย์นี้

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | Expected source keywords: home | หมวด: overview | ชนิดคำตอบ: summary | ระดับ: medium | variant: overview

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `overview_lookup`
- mode: `pipeline:overview_fast_path` | elapsed: `0.0036` sec

## 256. [PASS] ถูก

**คำถาม:** หน่วยงานที่ดำเนินการคือใคร

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | Expected source keywords: home | หมวด: overview | ชนิดคำตอบ: summary | ระดับ: medium | variant: overview

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `overview_lookup`
- mode: `pipeline:overview_fast_path` | elapsed: `0.0042` sec

## 257. [PASS] ถูก

**คำถาม:** mission ของศูนย์คืออะไร

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/home](https://esports.computing.psu.ac.th/home) (`home / home / home`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | Expected source keywords: home | หมวด: overview | ชนิดคำตอบ: summary | ระดับ: medium | variant: overview

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `overview_lookup`
- mode: `pipeline:overview_fast_path` | elapsed: `0.0053` sec

## 258. [PASS] ถูก

**คำถาม:** ศูนย์อยู่ตรงไหน

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: medium | variant: contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0029` sec

## 259. [PASS] ถูก

**คำถาม:** ที่ตั้งของ studio คือที่ไหน

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: medium | variant: contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.004` sec

## 260. [PASS] ถูก

**คำถาม:** ขอ email ติดต่อ

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: medium | variant: contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0061` sec

## 261. [PASS] ถูก

**คำถาม:** Facebook ศูนย์ชื่ออะไร

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: medium | variant: contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0053` sec

## 262. [PASS] ถูก

**คำถาม:** เบอร์โทรระบบจองมีเบอร์อะไร

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: medium | variant: contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0053` sec

## 263. [PASS] ถูก

**คำถาม:** อีสปอร์ตคืออะไรแบบเข้าใจง่าย

**คำตอบ(จาก AI):**

อีสปอร์ตคือกีฬาอิเล็กทรอนิกส์ เป็นการแข่งขันวิดีโอเกมที่ใช้ทักษะและความสามารถ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_definition

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0038` sec

## 264. [PASS] ถูก

**คำถาม:** esports เริ่มครั้งแรกที่ไหน

**คำตอบ(จาก AI):**

ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Stanford, 1972 | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_origin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0052` sec

## 265. [PASS] ถูก

**คำถาม:** Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง

**คำตอบ(จาก AI):**

ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Spacewar, 1972 | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_origin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0085` sec

## 266. [PASS] ถูก

**คำถาม:** เกมประเภท MOBA คืออะไร

**คำตอบ(จาก AI):**

MOBA คือ Multiplayer Online Battle Arena เป็นหนึ่งในประเภทเกมยอดนิยมของอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: MOBA | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_moba

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0072` sec

## 267. [PASS] ถูก

**คำถาม:** อาชีพในวงการ esports มีอะไรบ้าง

**คำตอบ(จาก AI):**

อาชีพในวงการอีสปอร์ตมีนักกีฬาอีสปอร์ต โค้ช ผู้จัดการทีม นักพากย์ ผู้จัดการแข่งขัน นักวิเคราะห์ และสายสนับสนุนอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_career

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0076` sec

## 268. [PASS] ถูก

**คำถาม:** Overcooked 2 ฝึกทักษะอะไร

**คำตอบ(จาก AI):**

Overcooked 2 ช่วยฝึกการทำงานเป็นทีม การสื่อสาร การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: การทำงานเป็นทีม, สื่อสาร | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_game_skill

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0055` sec

## 269. [PASS] ถูก

**คำถาม:** Mario Kart 8 Deluxe ฝึกอะไร

**คำตอบ(จาก AI):**

Mario Kart 8 Deluxe ช่วยฝึกไหวพริบ การตัดสินใจ และการตอบสนองระหว่างเล่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/knowledge](https://esports.computing.psu.ac.th/knowledge) (`Knowledge / knowledge / Knowledge`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไหวพริบ, การตัดสินใจ | Expected source keywords: Knowledge | หมวด: knowledge | ชนิดคำตอบ: summary | ระดับ: medium | variant: knowledge_game_skill

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- quality_ok: `True`
- validation_ok: `True`
- route: `knowledge` | intent: `knowledge_lookup`
- mode: `pipeline:knowledge_fast_path` | elapsed: `0.0084` sec

## 270. [PASS] ถูก

**คำถาม:** วันที่ 25 เมษายน 2569 แข่งเกมอะไร

**คำตอบ(จาก AI):**

วันที่ 25 เมษายน 2569 เป็นข่าว PSU Phuket CS 2 2026
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/events-news/news](https://esports.computing.psu.ac.th/events-news/news) (`News / events_news / News`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: News | หมวด: events_news | ชนิดคำตอบ: fact | ระดับ: medium | variant: news

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- quality_ok: `True`
- validation_ok: `True`
- route: `events_news` | intent: `news_lookup`
- mode: `pipeline:news_fast_path` | elapsed: `0.0091` sec

## 271. [PASS] ถูก

**คำถาม:** VALORANT 2026 จัดวันไหน

**คำตอบ(จาก AI):**

PSU Phuket VALORANT 2026 จัดวันที่ 21 กุมภาพันธ์ 2569
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/events-news/news](https://esports.computing.psu.ac.th/events-news/news) (`News / events_news / News`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: News | หมวด: events_news | ชนิดคำตอบ: fact | ระดับ: medium | variant: news

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- quality_ok: `True`
- validation_ok: `True`
- route: `events_news` | intent: `news_lookup`
- mode: `pipeline:news_fast_path` | elapsed: `0.0059` sec

## 272. [PASS] ถูก

**คำถาม:** SURAT SMASH ส่งตัวแทนกี่คน

**คำตอบ(จาก AI):**

SURAT SMASH ส่งตัวแทน 4 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/events-news/news](https://esports.computing.psu.ac.th/events-news/news) (`News / events_news / News`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: News | หมวด: events_news | ชนิดคำตอบ: fact | ระดับ: medium | variant: news

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- quality_ok: `True`
- validation_ok: `True`
- route: `events_news` | intent: `news_lookup`
- mode: `pipeline:news_fast_path` | elapsed: `0.0084` sec

## 273. [PASS] ถูก

**คำถาม:** นักศึกษาชาวจีนมีกี่คน

**คำตอบ(จาก AI):**

ข่าวระบุว่านักศึกษาชาวจีนมี 11 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/events-news/news](https://esports.computing.psu.ac.th/events-news/news) (`News / events_news / News`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: News | หมวด: events_news | ชนิดคำตอบ: fact | ระดับ: medium | variant: news

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- quality_ok: `True`
- validation_ok: `True`
- route: `events_news` | intent: `news_lookup`
- mode: `pipeline:news_fast_path` | elapsed: `0.0032` sec

## 274. [PASS] ถูก

**คำถาม:** GAME ON เปิดโลกอีสปอร์ตจัดให้ใคร

**คำตอบ(จาก AI):**

กิจกรรม GAME ON จัดให้นักเรียน ม.3 โรงเรียนท้ายเหมืองวิทยา
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/events-news/news](https://esports.computing.psu.ac.th/events-news/news) (`News / events_news / News`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: News | หมวด: events_news | ชนิดคำตอบ: fact | ระดับ: medium | variant: news

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- quality_ok: `True`
- validation_ok: `True`
- route: `events_news` | intent: `news_lookup`
- mode: `pipeline:news_fast_path` | elapsed: `0.0069` sec

## 275. [PASS] ถูก

**คำถาม:** อธิการบดีในหน้าสมาชิกคือใคร

**คำตอบ(จาก AI):**

ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ (PSU)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/members](https://esports.computing.psu.ac.th/members) (`Members / about_us / Members`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Members | หมวด: about_us | ชนิดคำตอบ: fact | ระดับ: medium | variant: about

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `members_lookup`
- mode: `pipeline:members_fast_path` | elapsed: `0.0048` sec

## 276. [PASS] ถูก

**คำถาม:** คณบดีวิทยาลัยการคอมพิวเตอร์คือใคร

**คำตอบ(จาก AI):**

รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์ PSU
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/members](https://esports.computing.psu.ac.th/members) (`Members / about_us / Members`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Members | หมวด: about_us | ชนิดคำตอบ: fact | ระดับ: medium | variant: about

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `members_lookup`
- mode: `pipeline:members_fast_path` | elapsed: `0.0036` sec

## 277. [PASS] ถูก

**คำถาม:** ผู้จัดการศูนย์คือใคร

**คำตอบ(จาก AI):**

นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/members](https://esports.computing.psu.ac.th/members) (`Members / about_us / Members`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Members | หมวด: about_us | ชนิดคำตอบ: fact | ระดับ: medium | variant: about

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `members_lookup`
- mode: `pipeline:members_fast_path` | elapsed: `0.0034` sec

## 278. [PASS] ถูก

**คำถาม:** ประธาน PSU Phuket Esports Club คือใคร

**คำตอบ(จาก AI):**

นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/members](https://esports.computing.psu.ac.th/members) (`Members / about_us / Members`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Members | หมวด: about_us | ชนิดคำตอบ: fact | ระดับ: medium | variant: about

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `members_lookup`
- mode: `pipeline:members_fast_path` | elapsed: `0.0099` sec

## 279. [PASS] ถูก

**คำถาม:** Gallery มีหมวดภาพอะไร

**คำตอบ(จาก AI):**

หน้า Gallery ของ PSU Esports Studio - Phuket มีหมวดภาพ Nintendo Switch และ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/members](https://esports.computing.psu.ac.th/members) (`Members / about_us / Members`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU | Expected source keywords: Members | หมวด: about_us | ชนิดคำตอบ: fact | ระดับ: medium | variant: about

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- quality_ok: `True`
- validation_ok: `True`
- route: `overview` | intent: `members_lookup`
- mode: `pipeline:members_fast_path` | elapsed: `0.0045` sec

## 280. [PASS] ถูก

**คำถาม:** มีบริการซ่อมคอมส่วนตัวไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0041` sec

## 281. [PASS] ถูก

**คำถาม:** ส่งอาหารถึงโต๊ะเกมได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0035` sec

## 282. [PASS] ถูก

**คำถาม:** เอาแมวเข้าได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.003` sec

## 283. [PASS] ถูก

**คำถาม:** สมัครสมาชิกรายปีราคาเท่าไหร่

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0048` sec

## 284. [PASS] ถูก

**คำถาม:** เช่าโน้ตบุ๊กกลับบ้านได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0034` sec

## 285. [PASS] ถูก

**คำถาม:** มีห้องนอนพักค้างคืนไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0037` sec

## 286. [PASS] ถูก

**คำถาม:** ขายคีย์บอร์ดเกมมิ่งไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0052` sec

## 287. [PASS] ถูก

**คำถาม:** รับซ่อมจอย PS5 ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0059` sec

## 288. [PASS] ถูก

**คำถาม:** มีบริการส่งเครื่องเกมไปบ้านไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0044` sec

## 289. [PASS] ถูก

**คำถาม:** ซื้อเกม Steam ผ่านศูนย์ได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.008` sec

## 290. [PASS] ถูก

**คำถาม:** มีคอร์สสอนเล่น Valorant ส่วนตัวไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0076` sec

## 291. [PASS] ถูก

**คำถาม:** จ่ายด้วยคริปโตได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0032` sec

## 292. [PASS] ถูก

**คำถาม:** ผ่อนชำระค่าเล่นได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0035` sec

## 293. [PASS] ถูก

**คำถาม:** มีส่วนลดวันเกิดไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0033` sec

## 294. [PASS] ถูก

**คำถาม:** จองแบบเหมาทั้งวันได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0035` sec

## 295. [PASS] ถูก

**คำถาม:** เอาเครื่อง PC ตัวเองมาตั้งได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0086` sec

## 296. [PASS] ถูก

**คำถาม:** มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.004` sec

## 297. [PASS] ถูก

**คำถาม:** มีอาหารบุฟเฟต์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0032` sec

## 298. [PASS] ถูก

**คำถาม:** รับจัดงานแต่งในศูนย์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0034` sec

## 299. [PASS] ถูก

**คำถาม:** ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง

**คำตอบ(จาก AI):**

ถ้าจองแล้วไม่ชำระภายใน 10 นาที ระบบจะยกเลิกและต้องจองใหม่ หากเช็คอินไม่ทันก่อนเริ่มรอบ การจองจะถูกยกเลิกและไม่มีการคืนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, ไม่มีการคืนเงิน | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_reservation

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:mixed_reservation_fast` | elapsed: `0.0125` sec

## 300. [PASS] ถูก

**คำถาม:** ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ

**คำตอบ(จาก AI):**

สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง, 30 นาที, ยกเลิก | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_reservation

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:mixed_reservation_fast` | elapsed: `0.0096` sec

## 301. [PASS] ถูก

**คำถาม:** จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และต้องชำระเงินภายใน 10 นาทีหลังจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions, 10 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_reservation

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:mixed_reservation_fast` | elapsed: `0.0114` sec

## 302. [PASS] ถูก

**คำถาม:** กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม

**คำตอบ(จาก AI):**

ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: สลิป, โอนเงิน | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_reservation

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `payment_policy`
- mode: `pipeline:mixed_reservation_fast` | elapsed: `0.0067` sec

## 303. [PASS] ถูก

**คำถาม:** ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง

**คำตอบ(จาก AI):**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_reservation

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `booking_policy`
- mode: `pipeline:booking_fast_path` | elapsed: `0.0078` sec

## 304. [PASS] ถูก

**คำถาม:** นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง

**คำตอบ(จาก AI):**

ราคาสำหรับกลุ่ม PSU Student and Staff:
- PlayStation 5 60 นาที ราคา 0 บาท
- VR 30 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: hard | variant: mixed_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0144` sec
- validation_warnings: `['price_question_should_start_with_price_or_number']`

## 305. [PASS] ถูก

**คำถาม:** คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า

**คำตอบ(จาก AI):**

Nintendo Switch 3-4 คน แพงกว่า 80 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน ราคา 280 บาท
- Cockpit ราคา 200 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: hard | variant: mixed_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0296` sec

## 306. [PASS] ถูก

**คำถาม:** General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม

**คำตอบ(จาก AI):**

เท่ากัน สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 ราคา 50 บาท
- Nintendo Switch 1-2 คน ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: hard | variant: mixed_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0166` sec
- validation_warnings: `['price_question_should_start_with_price_or_number']`

## 307. [PASS] ถูก

**คำถาม:** ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม

**คำตอบ(จาก AI):**

ไม่ต้องจ่าย ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: hard | variant: mixed_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0177` sec

## 308. [PASS] ถูก

**คำถาม:** ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่

**คำตอบ(จาก AI):**

ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที 185 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: calculation | ระดับ: hard | variant: mixed_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.019` sec

## 309. [PASS] ถูก

**คำถาม:** ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง

**คำตอบ(จาก AI):**

เกี่ยวกับกฎอาหารและเสียงดัง: อาหาร/เครื่องดื่มทำได้เฉพาะพื้นที่ที่กำหนด, กรุณางดส่งเสียงดัง และหากทำอุปกรณ์เสียหายต้องรับผิดชอบค่าปรับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, เสียงดัง | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `penalty` | intent: `penalty_policy`
- mode: `pipeline:mixed_rules_fast` | elapsed: `0.0102` sec

## 310. [PASS] ถูก

**คำถาม:** ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม

**คำตอบ(จาก AI):**

ทรัพย์สินสูญหายศูนย์ไม่รับผิดชอบ แต่ถ้าผู้ใช้ทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้ต้องรับผิดชอบค่าปรับ/ค่าซ่อม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่รับผิดชอบ, รับผิดชอบ | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:mixed_rules_fast` | elapsed: `0.0139` sec

## 311. [PASS] ถูก

**คำถาม:** ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0049` sec

## 312. [PASS] ถูก

**คำถาม:** ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง

**คำตอบ(จาก AI):**

อุปกรณ์และแผ่นเกมที่เบิกไปใช้งานต้องคืนหลังจากใช้งานเสร็จ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: คืน, หลังจากใช้งานเสร็จ | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0091` sec

## 313. [PASS] ถูก

**คำถาม:** ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร

**คำตอบ(จาก AI):**

หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: แจ้งเจ้าหน้าที่ | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: multi_fact | ระดับ: hard | variant: mixed_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0072` sec

## 314. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ตอบสั้นๆ

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0107` sec

## 315. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ตอบสั้นๆ

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0078` sec

## 316. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ตอบสั้นๆ

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0144` sec

## 317. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0055` sec

## 318. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ตอบสั้นๆ

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0077` sec

## 319. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ตอบสั้นๆ

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0049` sec

## 320. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0066` sec

## 321. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ตอบสั้นๆ

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0061` sec

## 322. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0104` sec

## 323. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0086` sec

## 324. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0155` sec

## 325. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0057` sec

## 326. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0077` sec

## 327. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0057` sec

## 328. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0095` sec

## 329. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0091` sec

## 330. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0135` sec

## 331. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0122` sec

## 332. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0156` sec

## 333. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ: * รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

รายละเอียดที่เกี่ยวข้อง:
- บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้
- Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
- การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `True`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0336` sec
- missing_source_keywords: `['Reservation']`

## 334. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ถามแทนเพื่อน

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0062` sec

## 335. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.007` sec

## 336. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0064` sec

## 337. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ถามแทนเพื่อน

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0071` sec

## 338. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0076` sec

## 339. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0061` sec

## 340. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0125` sec

## 341. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)

รายละเอียดที่เกี่ยวข้อง:
- กฎระเบียบและรูปแบบการแข่งขัน VALORANT
- ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
- อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `True`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0149` sec
- missing_source_keywords: `['Reservation']`

## 342. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0042` sec

## 343. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0031` sec

## 344. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0042` sec

## 345. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0034` sec

## 346. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0092` sec

## 347. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0085` sec

## 348. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0135` sec

## 349. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0064` sec

## 350. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0068` sec

## 351. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0053` sec

## 352. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.0072` sec

## 353. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/contact-us](https://esports.computing.psu.ac.th/contact-us) (`Contact / contact / Contact`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | Expected source keywords: Contact | หมวด: contact | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_contact

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- quality_ok: `True`
- validation_ok: `True`
- route: `contact` | intent: `contact_lookup`
- mode: `pipeline:contact_fast_path` | elapsed: `0.0077` sec

## 354. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

วันนี้ 04/07/2026 (วันเสาร์): วันเสาร์ยังไม่พบช่วงให้บริการในตารางประจำที่มีอยู่ จึงควรตรวจสอบกับศูนย์ก่อนเดินทาง
วันที่อ้างอิงของระบบ: วันนี้คือ 04/07/2026 (วันเสาร์) ตามเวลาไทย

รายละเอียดจากตาราง:
- วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance* และเปิดช่วงบ่าย 13:00-16:00
- วันอังคาร-พฤหัสบดีเปิด 09:00-12:00 และ 13:00-16:00
- วันศุกร์เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 เป็น Maintenance
- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:calendar_schedule_fast_path` | elapsed: `0.0148` sec

## 355. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5 | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0096` sec

## 356. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png](https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png) (`service_fee_image_2026 / service_fee / service_fee_image_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR | Expected source keywords: service_fee | หมวด: service_fee | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_price

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- quality_ok: `True`
- validation_ok: `True`
- route: `service_fee` | intent: `service_fee_query`
- mode: `pipeline:deterministic_calculator_fast` | elapsed: `0.0158` sec

## 357. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

ข้อมูลเกม: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends

วันนี้ 04/07/2026 (วันเสาร์): วันเสาร์ยังไม่พบช่วงให้บริการในตารางประจำที่มีอยู่ จึงควรตรวจสอบกับศูนย์ก่อนเดินทาง
วันที่อ้างอิงของระบบ: วันนี้คือ 04/07/2026 (วันเสาร์) ตามเวลาไทย

รายละเอียดจากตาราง:
- วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance* และเปิดช่วงบ่าย 13:00-16:00
- วันอังคาร-พฤหัสบดีเปิด 09:00-12:00 และ 13:00-16:00
- วันศุกร์เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 เป็น Maintenance
- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT | Expected source keywords: Reservation | หมวด: games | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_games

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `schedule` | intent: `schedule_query`
- mode: `pipeline:calendar_schedule_fast_path` | elapsed: `0.0068` sec

## 358. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: Reservation | หมวด: reservation | ชนิดคำตอบ: fact | ระดับ: hard | variant: typo_checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `reservation` | intent: `checkin_policy`
- mode: `pipeline:checkin_fast_path` | elapsed: `0.0074` sec

## 359. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม | Expected source keywords: Reservation | หมวด: rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: casual_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- quality_ok: `True`
- validation_ok: `True`
- route: `rules` | intent: `studio_rules`
- mode: `pipeline:rules_fast_path` | elapsed: `0.0071` sec

## 360. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล | Expected source keywords: - | หมวด: no_answer | ชนิดคำตอบ: no_answer | ระดับ: hard | variant: unknown_or_out_of_scope

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `no_answer` | intent: `guard_no_answer`
- mode: `pipeline:guard_no_answer` | elapsed: `0.007` sec
