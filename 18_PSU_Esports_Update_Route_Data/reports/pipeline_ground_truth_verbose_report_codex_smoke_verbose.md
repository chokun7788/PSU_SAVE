# Ground Truth Verbose Result

- Total: 2
- PASS: 2
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0077s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_codex_smoke_verbose.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_codex_smoke_verbose.md`

## Mode Summary
- `pipeline:schedule_fast_path`: 2

## Route Summary
- `schedule`: 2
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
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0101` sec

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
- mode: `pipeline:schedule_fast_path` | elapsed: `0.0053` sec
