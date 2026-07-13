# Human Review Checker - PSU Esports Chatbot

สร้างเมื่อ: 2026-07-02T00:10:24

ไฟล์นี้ใช้สำหรับตรวจคุณภาพคำตอบด้วยคน หลังจากระบบ Ground Truth อัตโนมัติเช็ค keyword/source แล้ว

## วิธีให้คะแนน

- `ตรงเจตนาคำถาม`: ประโยคแรกตอบสิ่งที่ผู้ใช้ถามจริงไหม เช่น ถ้าถาม “ต่างกันเท่าไหร่” ควรขึ้นต้นด้วย “ต่างกัน ... บาท”
- `ความถูกต้อง`: ราคา เวลา กฎ และกลุ่มผู้ใช้ถูกไหม
- `ความครบถ้วน`: มีรายละเอียดที่จำเป็นครบไหม ถ้าถามเวลาโดยไม่ระบุวันควรบอกภาพรวม Monday-Friday และ Maintenance
- `น้ำเสียง/อ่านง่าย`: สุภาพ กระชับ ไม่วกวน ไม่ทำให้ลูกค้าสับสน
- `Route เหมาะไหม`: ควรใช้ rule/calculator/RAG/no-answer ถูกทางไหม

## Decision ที่แนะนำ

- `pass`: ใช้งานได้แล้ว
- `minor_fix`: ข้อเท็จจริงถูก แต่เรียงคำตอบแปลก/ขาดรายละเอียดเล็กน้อย
- `major_fix`: ตอบคนละประเด็น ราคาผิด เวลา/กฎผิด หรือทำให้เข้าใจผิด
- `needs_data`: ข้อมูลไม่มีจริง ต้องขอไฟล์/กฎ/นโยบายเพิ่ม
- `needs_policy`: ต้องให้ผู้ดูแลยืนยัน เพราะกระทบกฎหรือการดำเนินงานจริง

## Auto Summary

- Source eval: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round6_finalaudit_20260701.jsonl`
- Total: 360
- Auto PASS: 360
- Auto FAIL: 0

> หมายเหตุ: Auto PASS แปลว่า keyword/source ผ่านเท่านั้น ยังต้องดู Human Review เพื่อเช็คว่าตอบตรงเจตนาและอ่านเป็นธรรมชาติไหม

---

## 1. [PASS] v2_001

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์เปิดให้เล่นกีโมง ปิดกี่โมง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 2. [PASS] v2_002

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์เปิดให้เล่นกี่โมงถึงกี่โมง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 3. [PASS] v2_003

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** จันทร์เปิดปิดยังไง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 4. [PASS] v2_004

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์เล่นได้ตั้งแต่กี่โมง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 5. [PASS] v2_005

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์มีรอบเล่นช่วงไหนบ้าง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 6. [PASS] v2_006

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** Monday open close time?

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 7. [PASS] v2_007

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** monday hours for play

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 8. [PASS] v2_008

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ถ้าไปวันจันทร์เช้าเล่นได้ไหม แล้วเปิดจริงกี่โมง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 9. [PASS] v2_009

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม

**คำตอบจาก AI:**

```text
วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 10. [PASS] v2_010

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** จันทร์เช้า maintenance แล้วบ่ายเปิดกี่โมง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 11. [PASS] v2_011

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์ช่วงเช้าเปิดไหม

**คำตอบจาก AI:**

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 12. [PASS] v2_012

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** จันทร์ 9 โมงเล่นได้ไหม

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 13. [PASS] v2_013

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** Monday morning available?

**คำตอบจาก AI:**

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 14. [PASS] v2_014

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันจันทร์ 09:00-12:00 เป็นอะไร

**คำตอบจาก AI:**

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 15. [PASS] v2_015

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เช้าวันจันทร์เป็น maintenance ใช่ไหม

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 16. [PASS] v2_016

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ศูนย์เปิดกีโมงปิดกี่โมง

**คำตอบจาก AI:**

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 17. [PASS] v2_017

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิดกี่โมงนะ

**คำตอบจาก AI:**

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 18. [PASS] v2_018

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เวลาเปิดให้บริการคืออะไร

**คำตอบจาก AI:**

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 19. [PASS] v2_019

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** service hours คืออะไร

**คำตอบจาก AI:**

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 20. [PASS] v2_020

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดถึง 16:00 ใช่ไหม

**คำตอบจาก AI:**

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 21. [PASS] v2_021

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิด 24 ชม ไหม

**คำตอบจาก AI:**

```text
ไม่เปิด 24 ชั่วโมง ตามข้อมูลที่มี ศูนย์ใช้ช่วงเวลา Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยต้องดูวัน Maintenance ประกอบ

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 22. [PASS] v2_022

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ช่วงเช้าของตารางคือเวลาไหน

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 23. [PASS] v2_023

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** Morning คือกี่โมงถึงกี่โมง

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 24. [PASS] v2_024

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** รอบเช้า 09 ถึง 12 ใช่ไหม

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 25. [PASS] v2_025

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 26. [PASS] v2_026

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ตอนเช้าเปิดกี่โมง

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 27. [PASS] v2_027

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** รอบเช้าเริ่มตอนไหน

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 28. [PASS] v2_028

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** morning session time?

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 29. [PASS] v2_029

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** morning slot time

**คำตอบจาก AI:**

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `09:00, 12:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 30. [PASS] v2_030

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ช่วงบ่ายของตารางคือเวลาไหน

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 31. [PASS] v2_031

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** Afternoon คือกี่โมงถึงกี่โมง

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 32. [PASS] v2_032

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** รอบบ่าย 13 ถึง 16 ใช่ไหม

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 33. [PASS] v2_033

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ช่วงบ่ายเปิดกี่โมงปิดกี่โมง

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 34. [PASS] v2_034

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** รอบบ่ายปิดกี่โมง

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 35. [PASS] v2_035

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** afternoon session time?

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 36. [PASS] v2_036

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** afternoon slot time

**คำตอบจาก AI:**

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Monday, Friday, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 37. [PASS] v2_037

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันศุกร์ maintenance คืออะไร

**คำตอบจาก AI:**

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 38. [PASS] v2_038

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** Friday maintenance ทำอะไร

**คำตอบจาก AI:**

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 39. [PASS] v2_039

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** maintenance weekly hardware inspection คืออะไร

**คำตอบจาก AI:**

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 40. [PASS] v2_040

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** วันศุกร์มีตรวจอุปกรณ์ไหม

**คำตอบจาก AI:**

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 41. [PASS] v2_041

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:schedule_fast_path`

**คำถาม:** ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม

**คำตอบจาก AI:**

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 42. [PASS] v2_042

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 43. [PASS] v2_043

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 44. [PASS] v2_044

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PS5 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 45. [PASS] v2_045

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 46. [PASS] v2_046

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PS5 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 47. [PASS] v2_047

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 48. [PASS] v2_048

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 49. [PASS] v2_049

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 50. [PASS] v2_050

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 51. [PASS] v2_051

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 52. [PASS] v2_052

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 53. [PASS] v2_053

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 54. [PASS] v2_054

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 55. [PASS] v2_055

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 56. [PASS] v2_056

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 57. [PASS] v2_057

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 58. [PASS] v2_058

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง PS5 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 59. [PASS] v2_059

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PlayStation 5 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, 60, 150` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 60. [PASS] v2_060

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 61. [PASS] v2_061

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 62. [PASS] v2_062

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Nintendo 1-2 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 63. [PASS] v2_063

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 64. [PASS] v2_064

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Nintendo 1-2 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 65. [PASS] v2_065

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 66. [PASS] v2_066

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 67. [PASS] v2_067

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 68. [PASS] v2_068

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 69. [PASS] v2_069

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 70. [PASS] v2_070

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 71. [PASS] v2_071

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 50` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 72. [PASS] v2_072

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 73. [PASS] v2_073

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 74. [PASS] v2_074

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 75. [PASS] v2_075

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 76. [PASS] v2_076

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 77. [PASS] v2_077

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 1-2 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 1-2, 140` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 78. [PASS] v2_078

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 79. [PASS] v2_079

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 80. [PASS] v2_080

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Nintendo 3-4 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 81. [PASS] v2_081

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 82. [PASS] v2_082

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Nintendo 3-4 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 83. [PASS] v2_083

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 84. [PASS] v2_084

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 85. [PASS] v2_085

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 86. [PASS] v2_086

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 87. [PASS] v2_087

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 88. [PASS] v2_088

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 89. [PASS] v2_089

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 100` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 90. [PASS] v2_090

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 91. [PASS] v2_091

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 92. [PASS] v2_092

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 93. [PASS] v2_093

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 94. [PASS] v2_094

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 95. [PASS] v2_095

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Switch 3-4 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, 3-4, 280` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 96. [PASS] v2_096

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 97. [PASS] v2_097

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 98. [PASS] v2_098

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Cockpit สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 99. [PASS] v2_099

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 100. [PASS] v2_100

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** Cockpit สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 101. [PASS] v2_101

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 102. [PASS] v2_102

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 103. [PASS] v2_103

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 104. [PASS] v2_104

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 105. [PASS] v2_105

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 106. [PASS] v2_106

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 107. [PASS] v2_107

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 65` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 108. [PASS] v2_108

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 109. [PASS] v2_109

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 110. [PASS] v2_110

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 111. [PASS] v2_111

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 112. [PASS] v2_112

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง Cockpit ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 113. [PASS] v2_113

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** พวงมาลัยขับรถ สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท

รายละเอียดจากตาราง:
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, 60, 200` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 114. [PASS] v2_114

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 115. [PASS] v2_115

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 116. [PASS] v2_116

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 30 นาที สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 117. [PASS] v2_117

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 118. [PASS] v2_118

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 30 นาที สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 119. [PASS] v2_119

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 120. [PASS] v2_120

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 121. [PASS] v2_121

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 122. [PASS] v2_122

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 123. [PASS] v2_123

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 124. [PASS] v2_124

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 125. [PASS] v2_125

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 190` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 126. [PASS] v2_126

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 127. [PASS] v2_127

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 128. [PASS] v2_128

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 129. [PASS] v2_129

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 130. [PASS] v2_130

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 131. [PASS] v2_131

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR ครึ่งชั่วโมง สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 30, 525` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 132. [PASS] v2_132

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 133. [PASS] v2_133

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 134. [PASS] v2_134

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 1 ชั่วโมง สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 135. [PASS] v2_135

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน ม.อ. เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 136. [PASS] v2_136

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 1 ชั่วโมง สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 137. [PASS] v2_137

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก PSU เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 0, 0, บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 138. [PASS] v2_138

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 139. [PASS] v2_139

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 140. [PASS] v2_140

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 141. [PASS] v2_141

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 142. [PASS] v2_142

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 143. [PASS] v2_143

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 375` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 144. [PASS] v2_144

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 145. [PASS] v2_145

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 146. [PASS] v2_146

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอก เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 147. [PASS] v2_147

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นคนนอก จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 148. [PASS] v2_148

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 149. [PASS] v2_149

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** VR 60 นาที สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, 1 ชั่วโมง, 1050` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 150. [PASS] v2_150

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ราคา PC ต่อชั่วโมงเท่าไหร่

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 151. [PASS] v2_151

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน มอ เล่น PC ฟรีไหม

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 152. [PASS] v2_152

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอกเล่นคอมต้องจ่ายเท่าไหร่

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 153. [PASS] v2_153

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PC มีราคาใน service fee ไหม

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 154. [PASS] v2_154

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ทำไมคำนวณ PC ไม่ได้

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 155. [PASS] v2_155

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** จอง PC 9 ถึง 11 ต้องเสียกี่บาท

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 156. [PASS] v2_156

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 157. [PASS] v2_157

หมวด: `service_fee` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** PC price for general student?

**คำตอบจาก AI:**

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, ไม่พบ, Service Fee` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 158. [PASS] v2_158

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ราคาค่าบริการทั้งหมดมีอะไรบ้าง

**คำตอบจาก AI:**

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 159. [PASS] v2_159

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** สรุป service fee ให้หน่อย

**คำตอบจาก AI:**

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 160. [PASS] v2_160

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ตารางราคา 2026 มีอะไร

**คำตอบจาก AI:**

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 161. [PASS] v2_161

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ค่าเล่นแต่ละเครื่องเท่าไหร่

**คำตอบจาก AI:**

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 162. [PASS] v2_162

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** service fee table includes what

**คำตอบจาก AI:**

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 163. [PASS] v2_163

หมวด: `service_fee` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ขอเรทราคา PS5 Switch Cockpit VR

**คำตอบจาก AI:**

```text
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Nintendo Switch, Cockpit, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 164. [PASS] v2_164

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองต้องล่วงหน้ากี่ชั่วโมง

**คำตอบจาก AI:**

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 165. [PASS] v2_165

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง

**คำตอบจาก AI:**

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 166. [PASS] v2_166

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ต้อง book ล่วงหน้ากี่ hr

**คำตอบจาก AI:**

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 167. [PASS] v2_167

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองก่อน 1 ชั่วโมงใช่ไหม

**คำตอบจาก AI:**

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 168. [PASS] v2_168

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** walk in ได้ไหมหรือต้องจองก่อน

**คำตอบจาก AI:**

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 169. [PASS] v2_169

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองได้สูงสุดกี่ session

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 170. [PASS] v2_170

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ครั้งนึงจองได้กี่รอบ

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 171. [PASS] v2_171

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** one booking max sessions?

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 172. [PASS] v2_172

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองทีเดียว 4 sessions ได้ไหม

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 173. [PASS] v2_173

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองสามรอบได้ไหม

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 174. [PASS] v2_174

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** หลังจองต้องจ่ายภายในกี่นาที

**คำตอบจาก AI:**

```text
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, จองใหม่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 175. [PASS] v2_175

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** ไม่จ่ายใน 10 นาทีจะเกิดอะไร

**คำตอบจาก AI:**

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, จองใหม่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 176. [PASS] v2_176

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** payment timeout กี่นาที

**คำตอบจาก AI:**

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, จองใหม่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 177. [PASS] v2_177

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม

**คำตอบจาก AI:**

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, จองใหม่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 178. [PASS] v2_178

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** ชำระเงินหลัง booking ต้องเร็วแค่ไหน

**คำตอบจาก AI:**

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, จองใหม่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 179. [PASS] v2_179

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** กดจองแล้วแก้ไขได้ไหม

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 180. [PASS] v2_180

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 181. [PASS] v2_181

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** แก้เวลา booking ได้ไหม

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 182. [PASS] v2_182

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ต้องยกเลิกแล้วจองใหม่ใช่ไหม

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 183. [PASS] v2_183

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** แนบสลิปเดิมตอนจองใหม่ได้ไหม

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 184. [PASS] v2_184

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** สิทธิ์การจองโอนให้เพื่อนได้ไหม

**คำตอบจาก AI:**

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่สามารถโอนสิทธิ์` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 185. [PASS] v2_185

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** ให้คนอื่นมาใช้ booking แทนได้ไหม

**คำตอบจาก AI:**

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่สามารถโอนสิทธิ์` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 186. [PASS] v2_186

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** transfer booking ได้ไหม

**คำตอบจาก AI:**

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่สามารถโอนสิทธิ์` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 187. [PASS] v2_187

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:booking_fast_path`

**คำถาม:** จองแทนกันได้ไหม

**คำตอบจาก AI:**

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่สามารถโอนสิทธิ์` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 188. [PASS] v2_188

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เช็คอินล่วงหน้าได้กี่นาที

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 189. [PASS] v2_189

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** check in ได้เร็วสุดกี่นาที

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 190. [PASS] v2_190

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เช็คอินก่อนเวลาได้ 1800 วินาทีไหม

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 191. [PASS] v2_191

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** ต้องเช็คอินก่อนเริ่มรอบใช่ไหม

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 192. [PASS] v2_192

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** ถ้า check-in ไม่ทันจะโดนอะไร

**คำตอบจาก AI:**

```text
ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ยกเลิก, ไม่มีการคืนเงิน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 193. [PASS] v2_193

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เช็คอินต้องใช้บัตรอะไร

**คำตอบจาก AI:**

```text
ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บัตรประชาชน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 194. [PASS] v2_194

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:checkin_fast_path`

**คำถาม:** แสดงบัตรประชาชนได้ไหมตอนเช็คอิน

**คำตอบจาก AI:**

```text
ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บัตรประชาชน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 195. [PASS] v2_195

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** ชำระเงินผ่านอะไร

**คำตอบจาก AI:**

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ธนาคารไทยพาณิชย์, 795-276244-1` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 196. [PASS] v2_196

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** โอนเงินไปบัญชีไหน

**คำตอบจาก AI:**

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ธนาคารไทยพาณิชย์, 795-276244-1` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 197. [PASS] v2_197

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** ชื่อบัญชีจ่ายค่าจองคืออะไร

**คำตอบจาก AI:**

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ธนาคารไทยพาณิชย์, 795-276244-1` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 198. [PASS] v2_198

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** เลขบัญชีธนาคารสำหรับจองคืออะไร

**คำตอบจาก AI:**

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ธนาคารไทยพาณิชย์, 795-276244-1` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 199. [PASS] v2_199

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:payment_fast_path`

**คำถาม:** ธนาคารที่ใช้รับเงินคืออะไร

**คำตอบจาก AI:**

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ธนาคารไทยพาณิชย์, 795-276244-1` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 200. [PASS] v2_200

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** PS5 มี Spider-Man 2 ไหม

**คำตอบจาก AI:**

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Spider-Man 2` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 201. [PASS] v2_201

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** เพลย์ห้ามี tekken 8 หรือเปล่า

**คำตอบจาก AI:**

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, TEKKEN 8` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 202. [PASS] v2_202

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** เกมบน PlayStation มีอะไรบ้าง

**คำตอบจาก AI:**

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, TEKKEN 8` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 203. [PASS] v2_203

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** PS5 เล่น Fortnite ได้ไหม

**คำตอบจาก AI:**

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, Fortnite` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 204. [PASS] v2_204

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** มี God of War Ragnarok ไหม

**คำตอบจาก AI:**

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PlayStation 5, God of War Ragnarok` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 205. [PASS] v2_205

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** Switch มี Mario Kart ไหม

**คำตอบจาก AI:**

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, Mario Kart` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 206. [PASS] v2_206

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** นินเทนโดมี Overcooked 2 ไหม

**คำตอบจาก AI:**

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, Overcooked 2` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 207. [PASS] v2_207

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** เกม Nintendo มีอะไรบ้าง

**คำตอบจาก AI:**

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, Mario Kart` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 208. [PASS] v2_208

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** เล่น Super Smash Bros ที่ศูนย์ได้ไหม

**คำตอบจาก AI:**

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, Super Smash` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 209. [PASS] v2_209

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** Switch Sports มีไหม

**คำตอบจาก AI:**

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Nintendo Switch, Switch Sports` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 210. [PASS] v2_210

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** PC มี valorant ไหม

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 211. [PASS] v2_211

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมเล่น CS2 ได้ไหม

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, Counter-Strike 2` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 212. [PASS] v2_212

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** PC games list

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 213. [PASS] v2_213

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** มี PUBG บน PC ไหม

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, PUBG` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 214. [PASS] v2_214

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** Warzone อยู่เครื่อง PC ไหน

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PC, Warzone` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 215. [PASS] v2_215

หมวด: `games` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** VR เล่นเกมอะไร

**คำตอบจาก AI:**

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, Beat Saber` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 216. [PASS] v2_216

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** Beat Saber มีไหม

**คำตอบจาก AI:**

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, Beat Saber` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 217. [PASS] v2_217

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** แว่น VR มี Horizon ไหม

**คำตอบจาก AI:**

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VR, Horizon` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 218. [PASS] v2_218

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** Cockpit เล่นเกมอะไร

**คำตอบจาก AI:**

```text
Cockpit ใช้เล่นเกม Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Cockpit, Gran Turismo 7` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 219. [PASS] v2_219

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:games_fast_path`

**คำถาม:** พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม

**คำตอบจาก AI:**

```text
Cockpit ใช้เล่นเกม Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Gran Turismo 7` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 220. [PASS] v2_220

หมวด: `equipment` | ชนิดคำตอบ: `list` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** PC Zone มีอุปกรณ์อะไรบ้าง

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Gaming PC, Gaming Monitor, Gaming Chair` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 221. [PASS] v2_221

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** คอมที่ศูนย์มีทั้งหมดกี่เครื่อง

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Gaming PC, 10 Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 222. [PASS] v2_222

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** Gaming PC รุ่นอะไร

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `MSI MAG Infinite S3, 10 Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 223. [PASS] v2_223

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** เก้าอี้เกมมิ่งมีไหมใน PC zone

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Gaming Chair, 10 Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 224. [PASS] v2_224

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** เมาส์กับหูฟังมีให้ไหม

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Gaming Mouse, Gaming Headset` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 225. [PASS] v2_225

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** Cockpit zone มีทีวีขนาดกี่นิ้ว

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 226. [PASS] v2_226

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** พวงมาลัยใช้รุ่นอะไร

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 227. [PASS] v2_227

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** Nintendo zone มีทีวีกี่นิ้ว

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 228. [PASS] v2_228

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** PS5 zone มีเครื่องกี่เครื่อง

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 229. [PASS] v2_229

หมวด: `equipment` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:equipment_fast_path`

**คำถาม:** VR zone ใช้แว่นรุ่นอะไร

**คำตอบจาก AI:**

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Units` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 230. [PASS] v2_230

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** เอาขนมเข้าไปกินตรงโต๊ะได้ไหม

**คำตอบจาก AI:**

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `เฉพาะ, พื้นที่ที่กำหนด` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 231. [PASS] v2_231

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** กินน้ำในพื้นที่เล่นได้ไหม

**คำตอบจาก AI:**

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `เฉพาะ, พื้นที่ที่กำหนด` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 232. [PASS] v2_232

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** ต้องฝากกระเป๋าก่อนไหม

**คำตอบจาก AI:**

```text
กรุณาฝากสัมภาระก่อนเข้าใช้บริการ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ฝากสัมภาระ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 233. [PASS] v2_233

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** ใช้เสียงดังได้ไหม

**คำตอบจาก AI:**

```text
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `งด, เสียงดัง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 234. [PASS] v2_234

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** พูดจาเสียดสีคนอื่นได้ไหม

**คำตอบจาก AI:**

```text
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม, เสียดสี` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 235. [PASS] v2_235

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** ทิ้งขยะไว้ในโซนเล่นได้ไหม

**คำตอบจาก AI:**

```text
ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม, ทิ้งขยะ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 236. [PASS] v2_236

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ในศูนย์ได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 237. [PASS] v2_237

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** เอาแอลกอฮอล์เข้าได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 238. [PASS] v2_238

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** พกมีดเข้าไปได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 239. [PASS] v2_239

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** เล่นพนันในห้องได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 240. [PASS] v2_240

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** เอาปลั๊กไฟส่วนตัวมาใช้ได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 241. [PASS] v2_241

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:rules_fast_path`

**คำถาม:** ย้ายอุปกรณ์เองได้ไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 242. [PASS] v2_242

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** ทำอุปกรณ์เสียหายต้องจ่ายไหม

**คำตอบจาก AI:**

```text
ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `รับผิดชอบ, ค่าปรับ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 243. [PASS] v2_243

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** รอยขีดข่วนเล็กน้อยโดนปรับเท่าไหร่

**คำตอบจาก AI:**

```text
ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100–500 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 244. [PASS] v2_244

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** เบาะขาดต้องจ่ายกี่บาท

**คำตอบจาก AI:**

```text
ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 245. [PASS] v2_245

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** หูฟังสายขาดค่าปรับเท่าไหร่

**คำตอบจาก AI:**

```text
ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 246. [PASS] v2_246

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** จอแตกต้องชดเชยยังไง

**คำตอบจาก AI:**

```text
กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ชดเชย, เต็มจำนวน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 247. [PASS] v2_247

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** คอมพังต้องจ่ายเต็มไหม

**คำตอบจาก AI:**

```text
กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ชดเชย, เต็มจำนวน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 248. [PASS] v2_248

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน

**คำตอบจาก AI:**

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ระงับสิทธิ์` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 249. [PASS] v2_249

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** โดนแบนชั่วคราวกี่วัน

**คำตอบจาก AI:**

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ระงับสิทธิ์, 1-7 วัน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 250. [PASS] v2_250

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** กรณีไหนแบนถาวร

**คำตอบจาก AI:**

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ระงับสิทธิ์, ถาวร` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 251. [PASS] v2_251

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** อุทธรณ์การลงโทษได้ภายในกี่วัน

**คำตอบจาก AI:**

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `7 วัน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 252. [PASS] v2_252

หมวด: `penalty` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:penalty_fast_path`

**คำถาม:** ศูนย์เก็บประวัติคนทำผิดไหม

**คำตอบจาก AI:**

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บันทึก, ประวัติ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 253. [PASS] v2_253

หมวด: `overview` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:overview_fast_path`

**คำถาม:** ศูนย์นี้คืออะไรแบบสั้นๆ

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 254. [PASS] v2_254

หมวด: `overview` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:overview_fast_path`

**คำถาม:** PSU Esports Studio Phuket คืออะไร

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 255. [PASS] v2_255

หมวด: `overview` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:overview_fast_path`

**คำถาม:** ใครเป็นคนก่อตั้งศูนย์นี้

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 256. [PASS] v2_256

หมวด: `overview` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:overview_fast_path`

**คำถาม:** หน่วยงานที่ดำเนินการคือใคร

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 257. [PASS] v2_257

หมวด: `overview` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:overview_fast_path`

**คำถาม:** mission ของศูนย์คืออะไร

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์` | source keyword: `home`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 258. [PASS] v2_258

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:contact_fast_path`

**คำถาม:** ศูนย์อยู่ตรงไหน

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 259. [PASS] v2_259

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:contact_fast_path`

**คำถาม:** ที่ตั้งของ studio คือที่ไหน

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 260. [PASS] v2_260

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอ email ติดต่อ

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 261. [PASS] v2_261

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:contact_fast_path`

**คำถาม:** Facebook ศูนย์ชื่ออะไร

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 262. [PASS] v2_262

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:contact_fast_path`

**คำถาม:** เบอร์โทรระบบจองมีเบอร์อะไร

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 263. [PASS] v2_263

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** อีสปอร์ตคืออะไรแบบเข้าใจง่าย

**คำตอบจาก AI:**

```text
อีสปอร์ตคือกีฬาอิเล็กทรอนิกส์ เป็นการแข่งขันวิดีโอเกมที่ใช้ทักษะและความสามารถ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `อีสปอร์ต` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 264. [PASS] v2_264

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** esports เริ่มครั้งแรกที่ไหน

**คำตอบจาก AI:**

```text
ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Stanford, 1972` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 265. [PASS] v2_265

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง

**คำตอบจาก AI:**

```text
ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `Spacewar, 1972` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 266. [PASS] v2_266

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** เกมประเภท MOBA คืออะไร

**คำตอบจาก AI:**

```text
MOBA คือ Multiplayer Online Battle Arena เป็นหนึ่งในประเภทเกมยอดนิยมของอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `MOBA` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 267. [PASS] v2_267

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** อาชีพในวงการ esports มีอะไรบ้าง

**คำตอบจาก AI:**

```text
อาชีพในวงการอีสปอร์ตมีนักกีฬาอีสปอร์ต โค้ช ผู้จัดการทีม นักพากย์ ผู้จัดการแข่งขัน นักวิเคราะห์ และสายสนับสนุนอื่น ๆ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `อีสปอร์ต` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 268. [PASS] v2_268

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** Overcooked 2 ฝึกทักษะอะไร

**คำตอบจาก AI:**

```text
Overcooked 2 ช่วยฝึกการทำงานเป็นทีม การสื่อสาร การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `การทำงานเป็นทีม, สื่อสาร` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 269. [PASS] v2_269

หมวด: `knowledge` | ชนิดคำตอบ: `summary` | ระดับ: `medium` | Route: `pipeline:knowledge_fast_path`

**คำถาม:** Mario Kart 8 Deluxe ฝึกอะไร

**คำตอบจาก AI:**

```text
Mario Kart 8 Deluxe ช่วยฝึกไหวพริบ การตัดสินใจ และการตอบสนองระหว่างเล่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/knowledge
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไหวพริบ, การตัดสินใจ` | source keyword: `Knowledge`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 270. [PASS] v2_270

หมวด: `events_news` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:news_fast_path`

**คำถาม:** วันที่ 25 เมษายน 2569 แข่งเกมอะไร

**คำตอบจาก AI:**

```text
วันที่ 25 เมษายน 2569 เป็นข่าว PSU Phuket CS 2 2026
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `News`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 271. [PASS] v2_271

หมวด: `events_news` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:news_fast_path`

**คำถาม:** VALORANT 2026 จัดวันไหน

**คำตอบจาก AI:**

```text
PSU Phuket VALORANT 2026 จัดวันที่ 21 กุมภาพันธ์ 2569
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `News`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 272. [PASS] v2_272

หมวด: `events_news` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:news_fast_path`

**คำถาม:** SURAT SMASH ส่งตัวแทนกี่คน

**คำตอบจาก AI:**

```text
SURAT SMASH ส่งตัวแทน 4 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `News`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 273. [PASS] v2_273

หมวด: `events_news` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:news_fast_path`

**คำถาม:** นักศึกษาชาวจีนมีกี่คน

**คำตอบจาก AI:**

```text
ข่าวระบุว่านักศึกษาชาวจีนมี 11 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `News`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 274. [PASS] v2_274

หมวด: `events_news` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:news_fast_path`

**คำถาม:** GAME ON เปิดโลกอีสปอร์ตจัดให้ใคร

**คำตอบจาก AI:**

```text
กิจกรรม GAME ON จัดให้นักเรียน ม.3 โรงเรียนท้ายเหมืองวิทยา
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `News`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 275. [PASS] v2_275

หมวด: `about_us` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:members_fast_path`

**คำถาม:** อธิการบดีในหน้าสมาชิกคือใคร

**คำตอบจาก AI:**

```text
ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ (PSU)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Members`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 276. [PASS] v2_276

หมวด: `about_us` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:members_fast_path`

**คำถาม:** คณบดีวิทยาลัยการคอมพิวเตอร์คือใคร

**คำตอบจาก AI:**

```text
รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์ PSU
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Members`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 277. [PASS] v2_277

หมวด: `about_us` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:members_fast_path`

**คำถาม:** ผู้จัดการศูนย์คือใคร

**คำตอบจาก AI:**

```text
นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Members`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 278. [PASS] v2_278

หมวด: `about_us` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:members_fast_path`

**คำถาม:** ประธาน PSU Phuket Esports Club คือใคร

**คำตอบจาก AI:**

```text
นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Members`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 279. [PASS] v2_279

หมวด: `about_us` | ชนิดคำตอบ: `fact` | ระดับ: `medium` | Route: `pipeline:members_fast_path`

**คำถาม:** Gallery มีหมวดภาพอะไร

**คำตอบจาก AI:**

```text
หน้า Gallery ของ PSU Esports Studio - Phuket มีหมวดภาพ Nintendo Switch และ PlayStation 5
แหล่งข้อมูล: https://esports.computing.psu.ac.th/members
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `PSU` | source keyword: `Members`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 280. [PASS] v2_280

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีบริการซ่อมคอมส่วนตัวไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 281. [PASS] v2_281

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** ส่งอาหารถึงโต๊ะเกมได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 282. [PASS] v2_282

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:no_answer`

**คำถาม:** เอาแมวเข้าได้ไหม

**คำตอบจาก AI:**

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 283. [PASS] v2_283

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** สมัครสมาชิกรายปีราคาเท่าไหร่

**คำตอบจาก AI:**

```text
ยังไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี ข้อมูลราคาที่มีตอนนี้เป็นค่าบริการตามประเภทอุปกรณ์และกลุ่มผู้ใช้ เช่น PSU Student and Staff, PSU Alumni and General Student และ General Adult
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 284. [PASS] v2_284

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** เช่าโน้ตบุ๊กกลับบ้านได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 285. [PASS] v2_285

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีห้องนอนพักค้างคืนไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 286. [PASS] v2_286

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** ขายคีย์บอร์ดเกมมิ่งไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 287. [PASS] v2_287

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** รับซ่อมจอย PS5 ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 288. [PASS] v2_288

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีบริการส่งเครื่องเกมไปบ้านไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 289. [PASS] v2_289

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** ซื้อเกม Steam ผ่านศูนย์ได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 290. [PASS] v2_290

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีคอร์สสอนเล่น Valorant ส่วนตัวไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 291. [PASS] v2_291

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** จ่ายด้วยคริปโตได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 292. [PASS] v2_292

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** ผ่อนชำระค่าเล่นได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 293. [PASS] v2_293

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีส่วนลดวันเกิดไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 294. [PASS] v2_294

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** จองแบบเหมาทั้งวันได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 295. [PASS] v2_295

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** เอาเครื่อง PC ตัวเองมาตั้งได้ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 296. [PASS] v2_296

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:no_answer`

**คำถาม:** มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม

**คำตอบจาก AI:**

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 297. [PASS] v2_297

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีอาหารบุฟเฟต์ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 298. [PASS] v2_298

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** รับจัดงานแต่งในศูนย์ไหม

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 299. [PASS] v2_299

หมวด: `reservation` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:mixed_reservation_fast`

**คำถาม:** ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง

**คำตอบจาก AI:**

```text
ถ้าจองแล้วไม่ชำระภายใน 10 นาที ระบบจะยกเลิกและต้องจองใหม่ หากเช็คอินไม่ทันก่อนเริ่มรอบ การจองจะถูกยกเลิกและไม่มีการคืนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `10 นาที, ยกเลิก, ไม่มีการคืนเงิน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 300. [PASS] v2_300

หมวด: `reservation` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:mixed_reservation_fast`

**คำถาม:** ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ

**คำตอบจาก AI:**

```text
สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง, 30 นาที, ยกเลิก` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 301. [PASS] v2_301

หมวด: `reservation` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:category_rule_fast_path`

**คำถาม:** จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที

**คำตอบจาก AI:**

```text
การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และหลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `3 Sessions, 10 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 302. [PASS] v2_302

หมวด: `reservation` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:mixed_reservation_fast`

**คำถาม:** กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม

**คำตอบจาก AI:**

```text
ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `สลิป, โอนเงิน` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 303. [PASS] v2_303

หมวด: `reservation` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:booking_fast_path`

**คำถาม:** ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง

**คำตอบจาก AI:**

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `1 ชั่วโมง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 304. [PASS] v2_304

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง

**คำตอบจาก AI:**

```text
กลุ่ม PSU Student and Staff ให้ดูราคา 0 บาทในแถวบริการที่เกี่ยวข้อง
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 305. [PASS] v2_305

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า

**คำตอบจาก AI:**

```text
Nintendo Switch 3-4 คน แพงกว่า 80 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน ราคา 280 บาท
- Cockpit ราคา 200 บาท

รายละเอียดจากตาราง:
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 306. [PASS] v2_306

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม

**คำตอบจาก AI:**

```text
เท่ากัน สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 ราคา 50 บาท
- Nintendo Switch 1-2 คน ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 307. [PASS] v2_307

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม

**คำตอบจาก AI:**

```text
ไม่ต้องจ่าย ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท

รายละเอียดจากตาราง:
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 308. [PASS] v2_308

หมวด: `service_fee` | ชนิดคำตอบ: `calculation` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่

**คำตอบจาก AI:**

```text
ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที 185 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `บาท` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 309. [PASS] v2_309

หมวด: `rules` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:mixed_rules_fast`

**คำถาม:** ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง

**คำตอบจาก AI:**

```text
เกี่ยวกับกฎอาหารและเสียงดัง: อาหาร/เครื่องดื่มทำได้เฉพาะพื้นที่ที่กำหนด, กรุณางดส่งเสียงดัง และหากทำอุปกรณ์เสียหายต้องรับผิดชอบค่าปรับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `เฉพาะ, เสียงดัง` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 310. [PASS] v2_310

หมวด: `rules` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:mixed_rules_fast`

**คำถาม:** ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม

**คำตอบจาก AI:**

```text
ทรัพย์สินสูญหายศูนย์ไม่รับผิดชอบ แต่ถ้าผู้ใช้ทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้ต้องรับผิดชอบค่าปรับ/ค่าซ่อม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่รับผิดชอบ, รับผิดชอบ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 311. [PASS] v2_311

หมวด: `rules` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 312. [PASS] v2_312

หมวด: `rules` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง

**คำตอบจาก AI:**

```text
อุปกรณ์และแผ่นเกมที่เบิกไปใช้งานต้องคืนหลังจากใช้งานเสร็จ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `คืน, หลังจากใช้งานเสร็จ` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 313. [PASS] v2_313

หมวด: `rules` | ชนิดคำตอบ: `multi_fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร

**คำตอบจาก AI:**

```text
หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `แจ้งเจ้าหน้าที่` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 314. [PASS] v2_314

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ตอบสั้นๆ

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 315. [PASS] v2_315

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ตอบสั้นๆ

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 316. [PASS] v2_316

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ตอบสั้นๆ

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 317. [PASS] v2_317

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม ตอบสั้นๆ

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 318. [PASS] v2_318

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที ตอบสั้นๆ

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 319. [PASS] v2_319

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ ตอบสั้นๆ

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 320. [PASS] v2_320

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม ตอบสั้นๆ

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 321. [PASS] v2_321

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอเฟสศูนย์หน่อย ตอบสั้นๆ

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `facebook.com/psuesportsphuket` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 322. [PASS] v2_322

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 323. [PASS] v2_323

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 324. [PASS] v2_324

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 325. [PASS] v2_325

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 326. [PASS] v2_326

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 327. [PASS] v2_327

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 328. [PASS] v2_328

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 329. [PASS] v2_329

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอเฟสศูนย์หน่อย ในเว็บบอกว่าไง

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `facebook.com/psuesportsphuket` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 330. [PASS] v2_330

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 331. [PASS] v2_331

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 332. [PASS] v2_332

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 333. [PASS] v2_333

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 334. [PASS] v2_334

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 335. [PASS] v2_335

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 336. [PASS] v2_336

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 337. [PASS] v2_337

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอเฟสศูนย์หน่อย ถามแทนเพื่อน

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `facebook.com/psuesportsphuket` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 338. [PASS] v2_338

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 339. [PASS] v2_339

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 340. [PASS] v2_340

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 341. [PASS] v2_341

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 342. [PASS] v2_342

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 343. [PASS] v2_343

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 344. [PASS] v2_344

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 345. [PASS] v2_345

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอเฟสศูนย์หน่อย แบบภาษาคนทั่วไป

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `facebook.com/psuesportsphuket` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 346. [PASS] v2_346

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 347. [PASS] v2_347

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 348. [PASS] v2_348

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 349. [PASS] v2_349

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 350. [PASS] v2_350

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 351. [PASS] v2_351

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 352. [PASS] v2_352

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 353. [PASS] v2_353

หมวด: `contact` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:contact_fast_path`

**คำถาม:** ขอเฟสศูนย์หน่อย ขอสรุปเร็วๆ

**คำตอบจาก AI:**

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/contact-us
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `facebook.com/psuesportsphuket` | source keyword: `Contact`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 354. [PASS] v2_354

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:schedule_fast_path`

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `13:00, 16:00, Maintenance` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 355. [PASS] v2_355

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `0, PlayStation 5` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 356. [PASS] v2_356

หมวด: `service_fee` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:deterministic_calculator_fast`

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `190, VR` | source keyword: `service_fee`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 357. [PASS] v2_357

หมวด: `games` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:games_fast_path`

**คำถาม:** คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `VALORANT` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 358. [PASS] v2_358

หมวด: `reservation` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:checkin_fast_path`

**คำถาม:** เชคอินก่อนกี่นาที ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `30 นาที` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 359. [PASS] v2_359

หมวด: `rules` | ชนิดคำตอบ: `fact` | ระดับ: `hard` | Route: `pipeline:rules_fast_path`

**คำถาม:** สูบบุหรี่ได้ปะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ห้าม` | source keyword: `Reservation`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:

## 360. [PASS] v2_360

หมวด: `no_answer` | ชนิดคำตอบ: `no_answer` | ระดับ: `hard` | Route: `pipeline:guard_no_answer`

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบจาก AI:**

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `ไม่พบข้อมูล` | source keyword: ``

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:
