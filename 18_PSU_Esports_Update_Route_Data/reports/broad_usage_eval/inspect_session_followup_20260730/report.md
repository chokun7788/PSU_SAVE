# Broad Usage Eval v1

- Generated at: 2026-07-30T17:25:57
- Cases: 12
- Turn checks: 24
- Passed: 23
- Failed: 1
- Pass rate: 0.9583
- Total wall sec: 6.882
- Allow LLM: False
- RAG fallback: False

## By Group
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 5
- fast/rule: 1
- structured: 18

## Common Problems
- missing 'PC': 1

## Top Failures

### SF-007 session_followup
- Question: จอง
- Resolved: PC จองยังไง
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: missing 'PC'
- Answer: ขั้นตอนจองโดยสรุป: •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลาที่ต้องการ •    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ •    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง •    แนบสลิปและยืนยันการจอง แหล่ง...
