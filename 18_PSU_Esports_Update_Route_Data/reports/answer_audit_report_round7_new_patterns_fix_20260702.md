# Answer Audit Report - PSU Esports Chatbot

สร้างเมื่อ: 2026-07-02T12:09:03
Source results: `reports\pipeline_ground_truth_results_quality_pipeline_round7_new_patterns_fix_20260702.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\answer_audit_results_round7_new_patterns_fix_20260702.jsonl`

## Summary

- Total: 360
- pass: 360
- minor_fix: 0
- major_fix: 0
- needs_data: 0
- needs_policy: 0

## By Category

| Category | pass | minor_fix | major_fix | needs_data | needs_policy |
|---|---:|---:|---:|---:|---:|
| about_us | 5 | 0 | 0 | 0 | 0 |
| contact | 10 | 0 | 0 | 0 | 0 |
| equipment | 10 | 0 | 0 | 0 | 0 |
| events_news | 5 | 0 | 0 | 0 | 0 |
| games | 26 | 0 | 0 | 0 | 0 |
| knowledge | 7 | 0 | 0 | 0 | 0 |
| no_answer | 25 | 0 | 0 | 0 | 0 |
| overview | 5 | 0 | 0 | 0 | 0 |
| penalty | 11 | 0 | 0 | 0 | 0 |
| reservation | 94 | 0 | 0 | 0 | 0 |
| rules | 23 | 0 | 0 | 0 | 0 |
| service_fee | 139 | 0 | 0 | 0 | 0 |

## Items To Review

ไม่พบข้อที่ audit heuristic มองว่าต้องแก้

## All Items

### 1. v2_001 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์เปิดให้เล่นกีโมง ปิดกี่โมง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 2. v2_002 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์เปิดให้เล่นกี่โมงถึงกี่โมง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 3. v2_003 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: จันทร์เปิดปิดยังไง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 4. v2_004 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์เล่นได้ตั้งแต่กี่โมง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 5. v2_005 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์มีรอบเล่นช่วงไหนบ้าง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 6. v2_006 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: Monday open close time?
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 7. v2_007 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: monday hours for play
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 8. v2_008 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ถ้าไปวันจันทร์เช้าเล่นได้ไหม แล้วเปิดจริงกี่โมง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 9. v2_009 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
- คำตอบหลัก:

```text
วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 10. v2_010 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: จันทร์เช้า maintenance แล้วบ่ายเปิดกี่โมง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 11. v2_011 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์ช่วงเช้าเปิดไหม
- คำตอบหลัก:

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 12. v2_012 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: จันทร์ 9 โมงเล่นได้ไหม
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 13. v2_013 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: Monday morning available?
- คำตอบหลัก:

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 14. v2_014 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันจันทร์ 09:00-12:00 เป็นอะไร
- คำตอบหลัก:

```text
วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 15. v2_015 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เช้าวันจันทร์เป็น maintenance ใช่ไหม
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 16. v2_016 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ศูนย์เปิดกีโมงปิดกี่โมง
- คำตอบหลัก:

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 17. v2_017 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิดกี่โมงนะ
- คำตอบหลัก:

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 18. v2_018 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เวลาเปิดให้บริการคืออะไร
- คำตอบหลัก:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 19. v2_019 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: service hours คืออะไร
- คำตอบหลัก:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 20. v2_020 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดถึง 16:00 ใช่ไหม
- คำตอบหลัก:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 21. v2_021 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิด 24 ชม ไหม
- คำตอบหลัก:

```text
ไม่เปิด 24 ชั่วโมง ตามข้อมูลที่มี ศูนย์ใช้ช่วงเวลา Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยต้องดูวัน Maintenance ประกอบ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 22. v2_022 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ช่วงเช้าของตารางคือเวลาไหน
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 23. v2_023 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: Morning คือกี่โมงถึงกี่โมง
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 24. v2_024 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: รอบเช้า 09 ถึง 12 ใช่ไหม
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 25. v2_025 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 26. v2_026 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ตอนเช้าเปิดกี่โมง
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 27. v2_027 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: รอบเช้าเริ่มตอนไหน
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 28. v2_028 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: morning session time?
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 29. v2_029 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: morning slot time
- คำตอบหลัก:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 30. v2_030 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ช่วงบ่ายของตารางคือเวลาไหน
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 31. v2_031 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: Afternoon คือกี่โมงถึงกี่โมง
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 32. v2_032 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: รอบบ่าย 13 ถึง 16 ใช่ไหม
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 33. v2_033 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ช่วงบ่ายเปิดกี่โมงปิดกี่โมง
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 34. v2_034 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: รอบบ่ายปิดกี่โมง
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 35. v2_035 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: afternoon session time?
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 36. v2_036 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: afternoon slot time
- คำตอบหลัก:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 37. v2_037 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันศุกร์ maintenance คืออะไร
- คำตอบหลัก:

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 38. v2_038 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: Friday maintenance ทำอะไร
- คำตอบหลัก:

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 39. v2_039 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: maintenance weekly hardware inspection คืออะไร
- คำตอบหลัก:

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 40. v2_040 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: วันศุกร์มีตรวจอุปกรณ์ไหม
- คำตอบหลัก:

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 41. v2_041 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม
- คำตอบหลัก:

```text
วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 42. v2_042 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 43. v2_043 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 44. v2_044 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PS5 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 45. v2_045 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น PlayStation 5 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 46. v2_046 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PS5 สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 47. v2_047 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น PlayStation 5 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 48. v2_048 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 49. v2_049 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 50. v2_050 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 51. v2_051 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 52. v2_052 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 53. v2_053 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 54. v2_054 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 55. v2_055 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 56. v2_056 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น PS5 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 57. v2_057 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง PlayStation 5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 58. v2_058 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง PS5 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 59. v2_059 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PlayStation 5 สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- PlayStation 5 60 นาที ราคา 150 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 60. v2_060 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 61. v2_061 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 62. v2_062 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Nintendo 1-2 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 63. v2_063 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น Switch 1-2 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 64. v2_064 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Nintendo 1-2 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 65. v2_065 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น Switch 1-2 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 1-2 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 66. v2_066 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 67. v2_067 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 68. v2_068 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 69. v2_069 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 70. v2_070 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 71. v2_071 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 1-2 คน 60 นาที ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 72. v2_072 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 73. v2_073 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 74. v2_074 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 75. v2_075 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง Switch 1-2 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 76. v2_076 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง Nintendo 1-2 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 77. v2_077 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 1-2 สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 1-2 คน 60 นาที ราคา 140 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 78. v2_078 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 79. v2_079 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 80. v2_080 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Nintendo 3-4 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 81. v2_081 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น Switch 3-4 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 82. v2_082 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Nintendo 3-4 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 83. v2_083 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น Switch 3-4 กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Nintendo Switch 3-4 คน 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 84. v2_084 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 85. v2_085 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 86. v2_086 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 87. v2_087 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 88. v2_088 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 89. v2_089 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 100 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Nintendo Switch 3-4 คน 60 นาที ราคา 100 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 90. v2_090 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 91. v2_091 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 92. v2_092 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 93. v2_093 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง Switch 3-4 ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 94. v2_094 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง Nintendo 3-4 คน ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 95. v2_095 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Switch 3-4 สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 280 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน 60 นาที ราคา 280 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 96. v2_096 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 97. v2_097 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 98. v2_098 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Cockpit สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 99. v2_099 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 100. v2_100 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: Cockpit สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 101. v2_101 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- Cockpit 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 102. v2_102 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 103. v2_103 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 104. v2_104 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 105. v2_105 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 106. v2_106 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 107. v2_107 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 65 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- Cockpit 60 นาที ราคา 65 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 108. v2_108 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 109. v2_109 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 110. v2_110 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น Cockpit กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 111. v2_111 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง พวงมาลัยขับรถ ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 112. v2_112 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง Cockpit ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 113. v2_113 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: พวงมาลัยขับรถ สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 200 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Cockpit 60 นาที ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 114. v2_114 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 115. v2_115 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 116. v2_116 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 30 นาที สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 117. v2_117 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 118. v2_118 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 30 นาที สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 119. v2_119 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 30 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 120. v2_120 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 121. v2_121 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 122. v2_122 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 123. v2_123 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 124. v2_124 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 125. v2_125 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 126. v2_126 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 127. v2_127 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 128. v2_128 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น VR 30 นาที กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 129. v2_129 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 130. v2_130 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง VR 30 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 131. v2_131 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR ครึ่งชั่วโมง สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 525 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 30 นาที ราคา 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 132. v2_132 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษา มอ จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 133. v2_133 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 134. v2_134 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 1 ชั่วโมง สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 135. v2_135 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน ม.อ. เล่น VR 60 นาที กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 136. v2_136 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 1 ชั่วโมง สำหรับเด็ก PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 137. v2_137 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก PSU เล่น VR 60 นาที กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 138. v2_138 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 139. v2_139 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 140. v2_140 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 141. v2_141 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 142. v2_142 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นศิษย์เก่า PSU จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 143. v2_143 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 1 ชั่วโมง ราคา 375 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 144. v2_144 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นบุคคลทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 145. v2_145 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 146. v2_146 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอก เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 147. v2_147 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นคนนอก จอง VR 60 นาที ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 148. v2_148 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็นGeneral Adult จอง VR 1 ชั่วโมง ราคาเท่าไหร่
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 149. v2_149 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: VR 60 นาที สำหรับGeneral Adult ต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ราคา 1050 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- VR 1 ชั่วโมง ราคา 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 150. v2_150 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ราคา PC ต่อชั่วโมงเท่าไหร่
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 151. v2_151 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน มอ เล่น PC ฟรีไหม
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 152. v2_152 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอกเล่นคอมต้องจ่ายเท่าไหร่
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 153. v2_153 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PC มีราคาใน service fee ไหม
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 154. v2_154 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ทำไมคำนวณ PC ไม่ได้
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 155. v2_155 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: จอง PC 9 ถึง 11 ต้องเสียกี่บาท
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 156. v2_156 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 157. v2_157 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: PC price for general student?
- คำตอบหลัก:

```text
PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 158. v2_158 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ราคาค่าบริการทั้งหมดมีอะไรบ้าง
- คำตอบหลัก:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 159. v2_159 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: สรุป service fee ให้หน่อย
- คำตอบหลัก:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 160. v2_160 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ตารางราคา 2026 มีอะไร
- คำตอบหลัก:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 161. v2_161 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ค่าเล่นแต่ละเครื่องเท่าไหร่
- คำตอบหลัก:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 162. v2_162 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: service fee table includes what
- คำตอบหลัก:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 163. v2_163 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ขอเรทราคา PS5 Switch Cockpit VR
- คำตอบหลัก:

```text
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 164. v2_164 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองต้องล่วงหน้ากี่ชั่วโมง
- คำตอบหลัก:

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 165. v2_165 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง
- คำตอบหลัก:

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 166. v2_166 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ต้อง book ล่วงหน้ากี่ hr
- คำตอบหลัก:

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 167. v2_167 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองก่อน 1 ชั่วโมงใช่ไหม
- คำตอบหลัก:

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 168. v2_168 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: walk in ได้ไหมหรือต้องจองก่อน
- คำตอบหลัก:

```text
ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 169. v2_169 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองได้สูงสุดกี่ session
- คำตอบหลัก:

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 170. v2_170 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ครั้งนึงจองได้กี่รอบ
- คำตอบหลัก:

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 171. v2_171 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: one booking max sessions?
- คำตอบหลัก:

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 172. v2_172 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองทีเดียว 4 sessions ได้ไหม
- คำตอบหลัก:

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 173. v2_173 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองสามรอบได้ไหม
- คำตอบหลัก:

```text
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 174. v2_174 [pass]

- หมวด: `reservation` | route: `service_fee` | score: `4/4`
- คำถาม: หลังจองต้องจ่ายภายในกี่นาที
- คำตอบหลัก:

```text
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 175. v2_175 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ไม่จ่ายใน 10 นาทีจะเกิดอะไร
- คำตอบหลัก:

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 176. v2_176 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: payment timeout กี่นาที
- คำตอบหลัก:

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 177. v2_177 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม
- คำตอบหลัก:

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 178. v2_178 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ชำระเงินหลัง booking ต้องเร็วแค่ไหน
- คำตอบหลัก:

```text
หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 179. v2_179 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: กดจองแล้วแก้ไขได้ไหม
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 180. v2_180 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 181. v2_181 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: แก้เวลา booking ได้ไหม
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 182. v2_182 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ต้องยกเลิกแล้วจองใหม่ใช่ไหม
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 183. v2_183 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: แนบสลิปเดิมตอนจองใหม่ได้ไหม
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 184. v2_184 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: สิทธิ์การจองโอนให้เพื่อนได้ไหม
- คำตอบหลัก:

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 185. v2_185 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ให้คนอื่นมาใช้ booking แทนได้ไหม
- คำตอบหลัก:

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 186. v2_186 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: transfer booking ได้ไหม
- คำตอบหลัก:

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 187. v2_187 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: จองแทนกันได้ไหม
- คำตอบหลัก:

```text
ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 188. v2_188 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เช็คอินล่วงหน้าได้กี่นาที
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 189. v2_189 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: check in ได้เร็วสุดกี่นาที
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 190. v2_190 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เช็คอินก่อนเวลาได้ 1800 วินาทีไหม
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 191. v2_191 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ต้องเช็คอินก่อนเริ่มรอบใช่ไหม
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 192. v2_192 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ถ้า check-in ไม่ทันจะโดนอะไร
- คำตอบหลัก:

```text
ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 193. v2_193 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เช็คอินต้องใช้บัตรอะไร
- คำตอบหลัก:

```text
ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 194. v2_194 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: แสดงบัตรประชาชนได้ไหมตอนเช็คอิน
- คำตอบหลัก:

```text
ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 195. v2_195 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ชำระเงินผ่านอะไร
- คำตอบหลัก:

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 196. v2_196 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: โอนเงินไปบัญชีไหน
- คำตอบหลัก:

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 197. v2_197 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ชื่อบัญชีจ่ายค่าจองคืออะไร
- คำตอบหลัก:

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 198. v2_198 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เลขบัญชีธนาคารสำหรับจองคืออะไร
- คำตอบหลัก:

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 199. v2_199 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ธนาคารที่ใช้รับเงินคืออะไร
- คำตอบหลัก:

```text
ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 200. v2_200 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: PS5 มี Spider-Man 2 ไหม
- คำตอบหลัก:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 201. v2_201 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: เพลย์ห้ามี tekken 8 หรือเปล่า
- คำตอบหลัก:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 202. v2_202 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: เกมบน PlayStation มีอะไรบ้าง
- คำตอบหลัก:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 203. v2_203 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: PS5 เล่น Fortnite ได้ไหม
- คำตอบหลัก:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 204. v2_204 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: มี God of War Ragnarok ไหม
- คำตอบหลัก:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 205. v2_205 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: Switch มี Mario Kart ไหม
- คำตอบหลัก:

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 206. v2_206 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: นินเทนโดมี Overcooked 2 ไหม
- คำตอบหลัก:

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 207. v2_207 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: เกม Nintendo มีอะไรบ้าง
- คำตอบหลัก:

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 208. v2_208 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: เล่น Super Smash Bros ที่ศูนย์ได้ไหม
- คำตอบหลัก:

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 209. v2_209 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: Switch Sports มีไหม
- คำตอบหลัก:

```text
Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 210. v2_210 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: PC มี valorant ไหม
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 211. v2_211 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมเล่น CS2 ได้ไหม
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 212. v2_212 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: PC games list
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 213. v2_213 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: มี PUBG บน PC ไหม
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 214. v2_214 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: Warzone อยู่เครื่อง PC ไหน
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 215. v2_215 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: VR เล่นเกมอะไร
- คำตอบหลัก:

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 216. v2_216 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: Beat Saber มีไหม
- คำตอบหลัก:

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 217. v2_217 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: แว่น VR มี Horizon ไหม
- คำตอบหลัก:

```text
VR มีเกม Beat Saber และ Horizon Call of the Mountain
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 218. v2_218 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: Cockpit เล่นเกมอะไร
- คำตอบหลัก:

```text
Cockpit ใช้เล่นเกม Gran Turismo 7
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 219. v2_219 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม
- คำตอบหลัก:

```text
Cockpit ใช้เล่นเกม Gran Turismo 7
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 220. v2_220 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: PC Zone มีอุปกรณ์อะไรบ้าง
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 221. v2_221 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: คอมที่ศูนย์มีทั้งหมดกี่เครื่อง
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 222. v2_222 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: Gaming PC รุ่นอะไร
- คำตอบหลัก:

```text
สเปก PC ที่บันทึกไว้ตอนนี้: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, CPU Intel Core i5-14400, RAM DDR5 32GB, GPU NVIDIA GeForce RTX 5060 8GB, Mainboard MSI PRO H610M-G และใน PC Zone มี Gaming PC ทั้งหมด 10 เครื่อง

หมายเหตุ: ข้อมูลนี้มาจากสเปกเครื่อง/ภาพ CPU-Z ที่บันทึกไว้ในโปรเจกต์ ส่วนหน้า Home ระบุรายการอุปกรณ์ PC Zone เช่น Gaming PC, Gaming Monitor, Gaming Chair, Gaming Keyboard, Gaming Mouse และ Gaming Headset
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 223. v2_223 [pass]

- หมวด: `equipment` | route: `games` | score: `4/4`
- คำถาม: เก้าอี้เกมมิ่งมีไหมใน PC zone
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 224. v2_224 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: เมาส์กับหูฟังมีให้ไหม
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 225. v2_225 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: Cockpit zone มีทีวีขนาดกี่นิ้ว
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 226. v2_226 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: พวงมาลัยใช้รุ่นอะไร
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 227. v2_227 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: Nintendo zone มีทีวีกี่นิ้ว
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 228. v2_228 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: PS5 zone มีเครื่องกี่เครื่อง
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 229. v2_229 [pass]

- หมวด: `equipment` | route: `equipment` | score: `4/4`
- คำถาม: VR zone ใช้แว่นรุ่นอะไร
- คำตอบหลัก:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 230. v2_230 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: เอาขนมเข้าไปกินตรงโต๊ะได้ไหม
- คำตอบหลัก:

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 231. v2_231 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: กินน้ำในพื้นที่เล่นได้ไหม
- คำตอบหลัก:

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 232. v2_232 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ต้องฝากกระเป๋าก่อนไหม
- คำตอบหลัก:

```text
กรุณาฝากสัมภาระก่อนเข้าใช้บริการ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 233. v2_233 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ใช้เสียงดังได้ไหม
- คำตอบหลัก:

```text
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 234. v2_234 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: พูดจาเสียดสีคนอื่นได้ไหม
- คำตอบหลัก:

```text
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 235. v2_235 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ทิ้งขยะไว้ในโซนเล่นได้ไหม
- คำตอบหลัก:

```text
ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 236. v2_236 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ในศูนย์ได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 237. v2_237 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: เอาแอลกอฮอล์เข้าได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 238. v2_238 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: พกมีดเข้าไปได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 239. v2_239 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: เล่นพนันในห้องได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 240. v2_240 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: เอาปลั๊กไฟส่วนตัวมาใช้ได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 241. v2_241 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ย้ายอุปกรณ์เองได้ไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 242. v2_242 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: ทำอุปกรณ์เสียหายต้องจ่ายไหม
- คำตอบหลัก:

```text
ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 243. v2_243 [pass]

- หมวด: `penalty` | route: `service_fee` | score: `4/4`
- คำถาม: รอยขีดข่วนเล็กน้อยโดนปรับเท่าไหร่
- คำตอบหลัก:

```text
ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100–500 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 244. v2_244 [pass]

- หมวด: `penalty` | route: `service_fee` | score: `4/4`
- คำถาม: เบาะขาดต้องจ่ายกี่บาท
- คำตอบหลัก:

```text
ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 245. v2_245 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: หูฟังสายขาดค่าปรับเท่าไหร่
- คำตอบหลัก:

```text
ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 246. v2_246 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: จอแตกต้องชดเชยยังไง
- คำตอบหลัก:

```text
กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 247. v2_247 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: คอมพังต้องจ่ายเต็มไหม
- คำตอบหลัก:

```text
กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 248. v2_248 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน
- คำตอบหลัก:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 249. v2_249 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: โดนแบนชั่วคราวกี่วัน
- คำตอบหลัก:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 250. v2_250 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: กรณีไหนแบนถาวร
- คำตอบหลัก:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 251. v2_251 [pass]

- หมวด: `penalty` | route: `penalty` | score: `4/4`
- คำถาม: อุทธรณ์การลงโทษได้ภายในกี่วัน
- คำตอบหลัก:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 252. v2_252 [pass]

- หมวด: `penalty` | route: `knowledge` | score: `4/4`
- คำถาม: ศูนย์เก็บประวัติคนทำผิดไหม
- คำตอบหลัก:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 253. v2_253 [pass]

- หมวด: `overview` | route: `overview` | score: `4/4`
- คำถาม: ศูนย์นี้คืออะไรแบบสั้นๆ
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 254. v2_254 [pass]

- หมวด: `overview` | route: `knowledge` | score: `4/4`
- คำถาม: PSU Esports Studio Phuket คืออะไร
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 255. v2_255 [pass]

- หมวด: `overview` | route: `overview` | score: `4/4`
- คำถาม: ใครเป็นคนก่อตั้งศูนย์นี้
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 256. v2_256 [pass]

- หมวด: `overview` | route: `overview` | score: `4/4`
- คำถาม: หน่วยงานที่ดำเนินการคือใคร
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 257. v2_257 [pass]

- หมวด: `overview` | route: `overview` | score: `4/4`
- คำถาม: mission ของศูนย์คืออะไร
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 258. v2_258 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ศูนย์อยู่ตรงไหน
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 259. v2_259 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ที่ตั้งของ studio คือที่ไหน
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 260. v2_260 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอ email ติดต่อ
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 261. v2_261 [pass]

- หมวด: `contact` | route: `reservation` | score: `4/4`
- คำถาม: Facebook ศูนย์ชื่ออะไร
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 262. v2_262 [pass]

- หมวด: `contact` | route: `reservation` | score: `4/4`
- คำถาม: เบอร์โทรระบบจองมีเบอร์อะไร
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 263. v2_263 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: อีสปอร์ตคืออะไรแบบเข้าใจง่าย
- คำตอบหลัก:

```text
อีสปอร์ตคือกีฬาอิเล็กทรอนิกส์ เป็นการแข่งขันวิดีโอเกมที่ใช้ทักษะและความสามารถ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 264. v2_264 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: esports เริ่มครั้งแรกที่ไหน
- คำตอบหลัก:

```text
ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 265. v2_265 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง
- คำตอบหลัก:

```text
ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 266. v2_266 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: เกมประเภท MOBA คืออะไร
- คำตอบหลัก:

```text
MOBA คือ Multiplayer Online Battle Arena เป็นหนึ่งในประเภทเกมยอดนิยมของอีสปอร์ต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 267. v2_267 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: อาชีพในวงการ esports มีอะไรบ้าง
- คำตอบหลัก:

```text
อาชีพในวงการอีสปอร์ตมีนักกีฬาอีสปอร์ต โค้ช ผู้จัดการทีม นักพากย์ ผู้จัดการแข่งขัน นักวิเคราะห์ และสายสนับสนุนอื่น ๆ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 268. v2_268 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: Overcooked 2 ฝึกทักษะอะไร
- คำตอบหลัก:

```text
Overcooked 2 ช่วยฝึกการทำงานเป็นทีม การสื่อสาร การวางแผน และการจัดการสถานการณ์กดดัน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 269. v2_269 [pass]

- หมวด: `knowledge` | route: `knowledge` | score: `4/4`
- คำถาม: Mario Kart 8 Deluxe ฝึกอะไร
- คำตอบหลัก:

```text
Mario Kart 8 Deluxe ช่วยฝึกไหวพริบ การตัดสินใจ และการตอบสนองระหว่างเล่น
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 270. v2_270 [pass]

- หมวด: `events_news` | route: `events_news` | score: `4/4`
- คำถาม: วันที่ 25 เมษายน 2569 แข่งเกมอะไร
- คำตอบหลัก:

```text
วันที่ 25 เมษายน 2569 เป็นข่าว PSU Phuket CS 2 2026
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 271. v2_271 [pass]

- หมวด: `events_news` | route: `events_news` | score: `4/4`
- คำถาม: VALORANT 2026 จัดวันไหน
- คำตอบหลัก:

```text
PSU Phuket VALORANT 2026 จัดวันที่ 21 กุมภาพันธ์ 2569
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 272. v2_272 [pass]

- หมวด: `events_news` | route: `events_news` | score: `4/4`
- คำถาม: SURAT SMASH ส่งตัวแทนกี่คน
- คำตอบหลัก:

```text
SURAT SMASH ส่งตัวแทน 4 คน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 273. v2_273 [pass]

- หมวด: `events_news` | route: `events_news` | score: `4/4`
- คำถาม: นักศึกษาชาวจีนมีกี่คน
- คำตอบหลัก:

```text
ข่าวระบุว่านักศึกษาชาวจีนมี 11 คน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 274. v2_274 [pass]

- หมวด: `events_news` | route: `events_news` | score: `4/4`
- คำถาม: GAME ON เปิดโลกอีสปอร์ตจัดให้ใคร
- คำตอบหลัก:

```text
กิจกรรม GAME ON จัดให้นักเรียน ม.3 โรงเรียนท้ายเหมืองวิทยา
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 275. v2_275 [pass]

- หมวด: `about_us` | route: `overview` | score: `4/4`
- คำถาม: อธิการบดีในหน้าสมาชิกคือใคร
- คำตอบหลัก:

```text
ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ (PSU)
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 276. v2_276 [pass]

- หมวด: `about_us` | route: `overview` | score: `4/4`
- คำถาม: คณบดีวิทยาลัยการคอมพิวเตอร์คือใคร
- คำตอบหลัก:

```text
รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์ PSU
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 277. v2_277 [pass]

- หมวด: `about_us` | route: `overview` | score: `4/4`
- คำถาม: ผู้จัดการศูนย์คือใคร
- คำตอบหลัก:

```text
นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 278. v2_278 [pass]

- หมวด: `about_us` | route: `overview` | score: `4/4`
- คำถาม: ประธาน PSU Phuket Esports Club คือใคร
- คำตอบหลัก:

```text
นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 279. v2_279 [pass]

- หมวด: `about_us` | route: `overview` | score: `4/4`
- คำถาม: Gallery มีหมวดภาพอะไร
- คำตอบหลัก:

```text
หน้า Gallery ของ PSU Esports Studio - Phuket มีหมวดภาพ Nintendo Switch และ PlayStation 5
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 280. v2_280 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีบริการซ่อมคอมส่วนตัวไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 281. v2_281 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: ส่งอาหารถึงโต๊ะเกมได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 282. v2_282 [pass]

- หมวด: `no_answer` | route: `general` | score: `4/4`
- คำถาม: เอาแมวเข้าได้ไหม
- คำตอบหลัก:

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 283. v2_283 [pass]

- หมวด: `no_answer` | route: `service_fee` | score: `4/4`
- คำถาม: สมัครสมาชิกรายปีราคาเท่าไหร่
- คำตอบหลัก:

```text
ยังไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี ข้อมูลราคาที่มีตอนนี้เป็นค่าบริการตามประเภทอุปกรณ์และกลุ่มผู้ใช้ เช่น PSU Student and Staff, PSU Alumni and General Student และ General Adult
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 284. v2_284 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: เช่าโน้ตบุ๊กกลับบ้านได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 285. v2_285 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีห้องนอนพักค้างคืนไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 286. v2_286 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: ขายคีย์บอร์ดเกมมิ่งไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 287. v2_287 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: รับซ่อมจอย PS5 ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 288. v2_288 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีบริการส่งเครื่องเกมไปบ้านไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 289. v2_289 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: ซื้อเกม Steam ผ่านศูนย์ได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 290. v2_290 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีคอร์สสอนเล่น Valorant ส่วนตัวไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 291. v2_291 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: จ่ายด้วยคริปโตได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 292. v2_292 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: ผ่อนชำระค่าเล่นได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 293. v2_293 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีส่วนลดวันเกิดไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 294. v2_294 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: จองแบบเหมาทั้งวันได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 295. v2_295 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: เอาเครื่อง PC ตัวเองมาตั้งได้ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 296. v2_296 [pass]

- หมวด: `no_answer` | route: `games` | score: `4/4`
- คำถาม: มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม
- คำตอบหลัก:

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 297. v2_297 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีอาหารบุฟเฟต์ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 298. v2_298 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: รับจัดงานแต่งในศูนย์ไหม
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 299. v2_299 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง
- คำตอบหลัก:

```text
ถ้าจองแล้วไม่ชำระภายใน 10 นาที ระบบจะยกเลิกและต้องจองใหม่ หากเช็คอินไม่ทันก่อนเริ่มรอบ การจองจะถูกยกเลิกและไม่มีการคืนเงิน
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 300. v2_300 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ
- คำตอบหลัก:

```text
สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 301. v2_301 [pass]

- หมวด: `reservation` | route: `service_fee` | score: `4/4`
- คำถาม: จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที
- คำตอบหลัก:

```text
การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และหลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 302. v2_302 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม
- คำตอบหลัก:

```text
ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 303. v2_303 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง
- คำตอบหลัก:

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 304. v2_304 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง
- คำตอบหลัก:

```text
กลุ่ม PSU Student and Staff ให้ดูราคา 0 บาทในแถวบริการที่เกี่ยวข้อง
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 305. v2_305 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า
- คำตอบหลัก:

```text
Nintendo Switch 3-4 คน แพงกว่า 80 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
- Nintendo Switch 3-4 คน ราคา 280 บาท
- Cockpit ราคา 200 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 306. v2_306 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม
- คำตอบหลัก:

```text
เท่ากัน สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 ราคา 50 บาท
- Nintendo Switch 1-2 คน ราคา 50 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 307. v2_307 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม
- คำตอบหลัก:

```text
ไม่ต้องจ่าย ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- VR 1 ชั่วโมง ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 308. v2_308 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่
- คำตอบหลัก:

```text
ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที 185 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 309. v2_309 [pass]

- หมวด: `rules` | route: `penalty` | score: `4/4`
- คำถาม: ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง
- คำตอบหลัก:

```text
เกี่ยวกับกฎอาหารและเสียงดัง: อาหาร/เครื่องดื่มทำได้เฉพาะพื้นที่ที่กำหนด, กรุณางดส่งเสียงดัง และหากทำอุปกรณ์เสียหายต้องรับผิดชอบค่าปรับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 310. v2_310 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม
- คำตอบหลัก:

```text
ทรัพย์สินสูญหายศูนย์ไม่รับผิดชอบ แต่ถ้าผู้ใช้ทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้ต้องรับผิดชอบค่าปรับ/ค่าซ่อม
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 311. v2_311 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 312. v2_312 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง
- คำตอบหลัก:

```text
อุปกรณ์และแผ่นเกมที่เบิกไปใช้งานต้องคืนหลังจากใช้งานเสร็จ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 313. v2_313 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร
- คำตอบหลัก:

```text
หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 314. v2_314 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ ตอบสั้นๆ
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 315. v2_315 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ตอบสั้นๆ
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 316. v2_316 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ตอบสั้นๆ
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 317. v2_317 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม ตอบสั้นๆ
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 318. v2_318 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที ตอบสั้นๆ
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 319. v2_319 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ ตอบสั้นๆ
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 320. v2_320 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม ตอบสั้นๆ
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 321. v2_321 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอเฟสศูนย์หน่อย ตอบสั้นๆ
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 322. v2_322 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 323. v2_323 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 324. v2_324 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 325. v2_325 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 326. v2_326 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 327. v2_327 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 328. v2_328 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 329. v2_329 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอเฟสศูนย์หน่อย ในเว็บบอกว่าไง
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 330. v2_330 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ ถามแทนเพื่อน
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 331. v2_331 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถามแทนเพื่อน
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 332. v2_332 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถามแทนเพื่อน
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 333. v2_333 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม ถามแทนเพื่อน
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 334. v2_334 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที ถามแทนเพื่อน
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 335. v2_335 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ ถามแทนเพื่อน
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 336. v2_336 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม ถามแทนเพื่อน
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 337. v2_337 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอเฟสศูนย์หน่อย ถามแทนเพื่อน
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 338. v2_338 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 339. v2_339 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 340. v2_340 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 341. v2_341 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 342. v2_342 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 343. v2_343 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 344. v2_344 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 345. v2_345 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอเฟสศูนย์หน่อย แบบภาษาคนทั่วไป
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 346. v2_346 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 347. v2_347 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 348. v2_348 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 349. v2_349 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 350. v2_350 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 351. v2_351 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 352. v2_352 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 353. v2_353 [pass]

- หมวด: `contact` | route: `contact` | score: `4/4`
- คำถาม: ขอเฟสศูนย์หน่อย ขอสรุปเร็วๆ
- คำตอบหลัก:

```text
PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 354. v2_354 [pass]

- หมวด: `reservation` | route: `schedule` | score: `4/4`
- คำถาม: เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 355. v2_355 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 356. v2_356 [pass]

- หมวด: `service_fee` | route: `service_fee` | score: `4/4`
- คำถาม: ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 357. v2_357 [pass]

- หมวด: `games` | route: `games` | score: `4/4`
- คำถาม: คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 358. v2_358 [pass]

- หมวด: `reservation` | route: `reservation` | score: `4/4`
- คำถาม: เชคอินก่อนกี่นาที ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 359. v2_359 [pass]

- หมวด: `rules` | route: `rules` | score: `4/4`
- คำถาม: สูบบุหรี่ได้ปะ ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

### 360. v2_360 [pass]

- หมวด: `no_answer` | route: `no_answer` | score: `4/4`
- คำถาม: มีให้เช่าจอไปบ้านไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง
- คำตอบหลัก:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```
- เหตุผล audit: ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก

