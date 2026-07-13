# Ground Truth Verbose Report

- ไฟล์: `c:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
- ข้อที่รัน: 1 - 360
- รวม: 360
- ถูก: 360
- ผิด/error: 0
- Accuracy: 100.00%
- Average latency: 0.218 sec
- Generated: 2026-07-01 22:43:37

---
## 1. [PASS] ถูก

**คำถาม:** วันจันทร์เปิดให้เล่นกีโมง ปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.073` sec


---

## 2. [PASS] ถูก

**คำถาม:** วันจันทร์เปิดให้เล่นกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.057` sec


---

## 3. [PASS] ถูก

**คำถาม:** จันทร์เปิดปิดยังไง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.032` sec


---

## 4. [PASS] ถูก

**คำถาม:** วันจันทร์เล่นได้ตั้งแต่กี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* ยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service จึงเล่นได้ช่วง 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_play_window / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 5. [PASS] ถูก

**คำถาม:** วันจันทร์มีรอบเล่นช่วงไหนบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* ยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service จึงเล่นได้ช่วง 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_play_window / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 6. [PASS] ถูก

**คำถาม:** Monday open close time?

**คำตอบ(จาก AI):**

Answer:
On Monday, Morning 09:00-12:00 is Maintenance*, not an open service slot. Afternoon 13:00-16:00 is Open for Service, so Monday play/service hours are 13:00-16:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.041` sec


---

## 7. [PASS] ถูก

**คำถาม:** monday hours for play

**คำตอบ(จาก AI):**

Answer:
On Monday, Morning 09:00-12:00 is Maintenance*, not an open service slot. Afternoon 13:00-16:00 is Open for Service, so Monday play/service hours are 13:00-16:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.030` sec


---

## 8. [PASS] ถูก

**คำถาม:** ถ้าไปวันจันทร์เช้าเล่นได้ไหม แล้วเปิดจริงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.078` sec


---

## 9. [PASS] ถูก

**คำถาม:** วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวัน: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น
- ตารางบริการช่วง Morning คือ 09:00 – 12:00
- ตารางบริการช่วง Afternoon คือ 13:00 – 16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_schedule_morning)
- https://esports.computing.psu.ac.th/ (curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.191` sec


---

## 10. [PASS] ถูก

**คำถาม:** จันทร์เช้า maintenance แล้วบ่ายเปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.110` sec


---

## 11. [PASS] ถูก

**คำถาม:** วันจันทร์ช่วงเช้าเปิดไหม

**คำตอบ(จาก AI):**

คำตอบ:
วัน Monday ช่วง Morning 09:00–12:00 เป็น Maintenance* ไม่ใช่ช่วง Open for Service

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.043` sec


---

## 12. [PASS] ถูก

**คำถาม:** จันทร์ 9 โมงเล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* ไม่ใช่ช่วง Open for Service ดังนั้นช่วง 9 โมงเช้าวันจันทร์ยังเล่นไม่ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning_specific / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 13. [PASS] ถูก

**คำถาม:** Monday morning available?

**คำตอบ(จาก AI):**

Answer:
On Monday morning, 09:00-12:00 is Maintenance*, not Open for Service.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.050` sec


---

## 14. [PASS] ถูก

**คำถาม:** วันจันทร์ 09:00-12:00 เป็นอะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* ไม่ใช่ช่วง Open for Service ดังนั้นช่วง 9 โมงเช้าวันจันทร์ยังเล่นไม่ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning_specific / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.039` sec


---

## 15. [PASS] ถูก

**คำถาม:** เช้าวันจันทร์เป็น maintenance ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* ไม่ใช่ช่วง Open for Service ดังนั้นช่วง 9 โมงเช้าวันจันทร์ยังเล่นไม่ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning_specific / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.080` sec


---

## 16. [PASS] ถูก

**คำถาม:** ศูนย์เปิดกีโมงปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 17. [PASS] ถูก

**คำถาม:** เปิดปิดกี่โมงนะ

**คำตอบ(จาก AI):**

คำตอบ:
ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.025` sec


---

## 18. [PASS] ถูก

**คำถาม:** เวลาเปิดให้บริการคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 19. [PASS] ถูก

**คำถาม:** service hours คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.032` sec


---

## 20. [PASS] ถูก

**คำถาม:** เปิดถึง 16:00 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวัน: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น
- ตารางบริการช่วง Morning คือ 09:00 – 12:00
- ตารางบริการช่วง Afternoon คือ 13:00 – 16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_schedule_morning)
- https://esports.computing.psu.ac.th/ (curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.080` sec


---

## 21. [PASS] ถูก

**คำถาม:** เปิด 24 ชม ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่ได้เปิด 24 ชั่วโมง ให้ยึดตาม timeline การให้บริการ: วันจันทร์ (Monday) เช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิด 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_not_24_hours / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.013` sec


---

## 22. [PASS] ถูก

**คำถาม:** ช่วงเช้าของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 23. [PASS] ถูก

**คำถาม:** Morning คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 24. [PASS] ถูก

**คำถาม:** รอบเช้า 09 ถึง 12 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.028` sec


---

## 25. [PASS] ถูก

**คำถาม:** ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.056` sec


---

## 26. [PASS] ถูก

**คำถาม:** ตอนเช้าเปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.028` sec


---

## 27. [PASS] ถูก

**คำถาม:** รอบเช้าเริ่มตอนไหน

**คำตอบ(จาก AI):**

คำตอบ:
ใช่ รอบเช้า Morning คือ 09:00–12:00 แต่ถ้าไม่ได้ระบุวันควรดู timeline ทั้งสัปดาห์ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.022` sec


---

## 28. [PASS] ถูก

**คำถาม:** morning session time?

**คำตอบ(จาก AI):**

Answer:
Yes, the Morning slot is 09:00-12:00, but if no day is specified you should check the weekly timeline: Monday morning 09:00-12:00 is Maintenance* and not playable, while Monday afternoon 13:00-16:00 is open; Tuesday-Thursday follow the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 29. [PASS] ถูก

**คำถาม:** morning slot time

**คำตอบ(จาก AI):**

Answer:
Yes, the Morning slot is 09:00-12:00, but if no day is specified you should check the weekly timeline: Monday morning 09:00-12:00 is Maintenance* and not playable, while Monday afternoon 13:00-16:00 is open; Tuesday-Thursday follow the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.022` sec


---

## 30. [PASS] ถูก

**คำถาม:** ช่วงบ่ายของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ:
รอบบ่าย Afternoon คือ 13:00–16:00 แต่ถ้าไม่ได้ระบุวันต้องดู timeline ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดทั้งรอบเช้า 09:00–12:00 และรอบบ่าย 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.041` sec


---

## 31. [PASS] ถูก

**คำถาม:** Afternoon คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
รอบบ่าย Afternoon คือ 13:00–16:00 แต่ถ้าไม่ได้ระบุวันต้องดู timeline ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดทั้งรอบเช้า 09:00–12:00 และรอบบ่าย 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 32. [PASS] ถูก

**คำถาม:** รอบบ่าย 13 ถึง 16 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
รอบบ่าย Afternoon คือ 13:00–16:00 แต่ถ้าไม่ได้ระบุวันต้องดู timeline ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดทั้งรอบเช้า 09:00–12:00 และรอบบ่าย 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.028` sec


---

## 33. [PASS] ถูก

**คำถาม:** ช่วงบ่ายเปิดกี่โมงปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
รอบบ่าย Afternoon คือ 13:00–16:00 แต่ถ้าไม่ได้ระบุวันต้องดู timeline ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดทั้งรอบเช้า 09:00–12:00 และรอบบ่าย 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.040` sec


---

## 34. [PASS] ถูก

**คำถาม:** รอบบ่ายปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
รอบบ่าย Afternoon คือ 13:00–16:00 แต่ถ้าไม่ได้ระบุวันต้องดู timeline ด้วย: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดทั้งรอบเช้า 09:00–12:00 และรอบบ่าย 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.017` sec


---

## 35. [PASS] ถูก

**คำถาม:** afternoon session time?

**คำตอบ(จาก AI):**

Answer:
The Afternoon slot is 13:00-16:00, but if no day is specified you should check the weekly timeline: Monday morning 09:00-12:00 is Maintenance* and Monday afternoon 13:00-16:00 is open; Tuesday-Thursday are open in both slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.043` sec


---

## 36. [PASS] ถูก

**คำถาม:** afternoon slot time

**คำตอบ(จาก AI):**

Answer:
The Afternoon slot is 13:00-16:00, but if no day is specified you should check the weekly timeline: Monday morning 09:00-12:00 is Maintenance* and Monday afternoon 13:00-16:00 is open; Tuesday-Thursday are open in both slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_morning, curated_schedule_afternoon, curated_reservation_schedule_monday_morning, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Monday, Friday, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 37. [PASS] ถูก

**คำถาม:** วันศุกร์ maintenance คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์ช่วง Morning 09:00–12:00 เปิดตามรอบเช้าได้ แต่ช่วง Afternoon 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น/ให้บริการ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.058` sec


---

## 38. [PASS] ถูก

**คำถาม:** Friday maintenance ทำอะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์ช่วง Morning 09:00–12:00 เปิดตามรอบเช้าได้ แต่ช่วง Afternoon 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น/ให้บริการ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.052` sec


---

## 39. [PASS] ถูก

**คำถาม:** maintenance weekly hardware inspection คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์ช่วง Afternoon 13:00–16:00 เป็น Maintenance** หมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์ ส่วนช่วง Morning 09:00–12:00 ยังเป็นรอบเช้า

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.175` sec


---

## 40. [PASS] ถูก

**คำถาม:** วันศุกร์มีตรวจอุปกรณ์ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์ช่วง Afternoon 13:00–16:00 เป็น Maintenance** หมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์ ส่วนช่วง Morning 09:00–12:00 ยังเป็นรอบเช้า

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 41. [PASS] ถูก

**คำถาม:** ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์ช่วง Afternoon 13:00–16:00 เป็น Maintenance** หมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์ ส่วนช่วง Morning 09:00–12:00 ยังเป็นรอบเช้า

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 42. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.133` sec


---

## 43. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.155` sec


---

## 44. [PASS] ถูก

**คำถาม:** PS5 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.122` sec


---

## 45. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.140` sec


---

## 46. [PASS] ถูก

**คำถาม:** PS5 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.114` sec


---

## 47. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.124` sec


---

## 48. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.046` sec


---

## 49. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.059` sec


---

## 50. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.069` sec


---

## 51. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.077` sec


---

## 52. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.041` sec


---

## 53. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.045` sec


---

## 54. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.124` sec


---

## 55. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.159` sec


---

## 56. [PASS] ถูก

**คำถาม:** คนนอก เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.055` sec


---

## 57. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.156` sec


---

## 58. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.149` sec


---

## 59. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.173` sec


---

## 60. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.191` sec


---

## 61. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.148` sec


---

## 62. [PASS] ถูก

**คำถาม:** Nintendo 1-2 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.175` sec


---

## 63. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.145` sec


---

## 64. [PASS] ถูก

**คำถาม:** Nintendo 1-2 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.181` sec


---

## 65. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.145` sec


---

## 66. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.086` sec


---

## 67. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาท (50 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.061` sec


---

## 68. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.116` sec


---

## 69. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาท (50 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.083` sec


---

## 70. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.081` sec


---

## 71. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 50 บาท (50 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.070` sec


---

## 72. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.202` sec


---

## 73. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาท (140 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.155` sec


---

## 74. [PASS] ถูก

**คำถาม:** คนนอก เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.121` sec


---

## 75. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาท (140 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.138` sec


---

## 76. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาทต่อ 60 นาที (Nintendo Switch 1-2 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.202` sec


---

## 77. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 140 บาท (140 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.173` sec


---

## 78. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.193` sec


---

## 79. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.150` sec


---

## 80. [PASS] ถูก

**คำถาม:** Nintendo 3-4 คน สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.158` sec


---

## 81. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.146` sec


---

## 82. [PASS] ถูก

**คำถาม:** Nintendo 3-4 คน สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.176` sec


---

## 83. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาท (0 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.129` sec


---

## 84. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.081` sec


---

## 85. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาท (100 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.058` sec


---

## 86. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.124` sec


---

## 87. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาท (100 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.086` sec


---

## 88. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.082` sec


---

## 89. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 100 บาท (100 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.068` sec


---

## 90. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.184` sec


---

## 91. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาท (280 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.146` sec


---

## 92. [PASS] ถูก

**คำถาม:** คนนอก เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.107` sec


---

## 93. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาท (280 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.125` sec


---

## 94. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาทต่อ 60 นาที (Nintendo Switch 3-4 คน)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.209` sec


---

## 95. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 280 บาท (280 บาท/session × 1 session(s))
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.174` sec


---

## 96. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.181` sec


---

## 97. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.190` sec


---

## 98. [PASS] ถูก

**คำถาม:** Cockpit สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.161` sec


---

## 99. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.176` sec


---

## 100. [PASS] ถูก

**คำถาม:** Cockpit สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.173` sec


---

## 101. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.159` sec


---

## 102. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.097` sec


---

## 103. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.084` sec


---

## 104. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.139` sec


---

## 105. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.147` sec


---

## 106. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.094` sec


---

## 107. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 65 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.079` sec


---

## 108. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.186` sec


---

## 109. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.202` sec


---

## 110. [PASS] ถูก

**คำถาม:** คนนอก เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.127` sec


---

## 111. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.193` sec


---

## 112. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.210` sec


---

## 113. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 200 บาทต่อ 60 นาที (Cockpit)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.223` sec


---

## 114. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.204` sec


---

## 115. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.194` sec


---

## 116. [PASS] ถูก

**คำถาม:** VR 30 นาที สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.194` sec


---

## 117. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.174` sec


---

## 118. [PASS] ถูก

**คำถาม:** VR 30 นาที สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.201` sec


---

## 119. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.158` sec


---

## 120. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.102` sec


---

## 121. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.094` sec


---

## 122. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.138` sec


---

## 123. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.126` sec


---

## 124. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.116` sec


---

## 125. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.095` sec


---

## 126. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.194` sec


---

## 127. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.181` sec


---

## 128. [PASS] ถูก

**คำถาม:** คนนอก เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.108` sec


---

## 129. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.154` sec


---

## 130. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.207` sec


---

## 131. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 525 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.203` sec


---

## 132. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.195` sec


---

## 133. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษา มอ ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.173` sec


---

## 134. [PASS] ถูก

**คำถาม:** VR 1 ชั่วโมง สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.169` sec


---

## 135. [PASS] ถูก

**คำถาม:** นักเรียน ม.อ. เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.161` sec


---

## 136. [PASS] ถูก

**คำถาม:** VR 1 ชั่วโมง สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.159` sec


---

## 137. [PASS] ถูก

**คำถาม:** เด็ก PSU เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.149` sec


---

## 138. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.103` sec


---

## 139. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษาทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.088` sec


---

## 140. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.129` sec


---

## 141. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักศึกษาต่างมหาลัย ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.118` sec


---

## 142. [PASS] ถูก

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.095` sec


---

## 143. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับศิษย์เก่า PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 375 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.088` sec


---

## 144. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.187` sec


---

## 145. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับบุคคลทั่วไป ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.174` sec


---

## 146. [PASS] ถูก

**คำถาม:** คนนอก เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.089` sec


---

## 147. [PASS] ถูก

**คำถาม:** ถ้าเป็นคนนอก จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.156` sec


---

## 148. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.208` sec


---

## 149. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับGeneral Adult ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 1,050 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.217` sec


---

## 150. [PASS] ถูก

**คำถาม:** ราคา PC ต่อชั่วโมงเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.059` sec


---

## 151. [PASS] ถูก

**คำถาม:** นักเรียน มอ เล่น PC ฟรีไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: นักศึกษา/บุคลากร PSU
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.069` sec


---

## 152. [PASS] ถูก

**คำถาม:** คนนอกเล่นคอมต้องจ่ายเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: บุคคลทั่วไป
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.090` sec


---

## 153. [PASS] ถูก

**คำถาม:** PC มีราคาใน service fee ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.074` sec


---

## 154. [PASS] ถูก

**คำถาม:** ทำไมคำนวณ PC ไม่ได้

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.048` sec


---

## 155. [PASS] ถูก

**คำถาม:** จอง PC 9 ถึง 11 ต้องเสียกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- ช่วงเวลาที่ถามคือ 09:00-11:00 = 2 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 2 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.080` sec


---

## 156. [PASS] ถูก

**คำถาม:** ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.098` sec


---

## 157. [PASS] ถูก

**คำถาม:** PC price for general student?

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.032` sec


---

## 158. [PASS] ถูก

**คำถาม:** ราคาค่าบริการทั้งหมดมีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.106` sec


---

## 159. [PASS] ถูก

**คำถาม:** สรุป service fee ให้หน่อย

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.106` sec


---

## 160. [PASS] ถูก

**คำถาม:** ตารางราคา 2026 มีอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.080` sec


---

## 161. [PASS] ถูก

**คำถาม:** ค่าเล่นแต่ละเครื่องเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.105` sec


---

## 162. [PASS] ถูก

**คำถาม:** service fee table includes what

**คำตอบ(จาก AI):**

Answer:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

Sources:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.137` sec


---

## 163. [PASS] ถูก

**คำถาม:** ขอเรทราคา PS5 Switch Cockpit VR

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.088` sec


---

## 164. [PASS] ถูก

**คำถาม:** จองต้องล่วงหน้ากี่ชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / Reservation, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 165. [PASS] ถูก

**คำถาม:** ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / Reservation, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.068` sec


---

## 166. [PASS] ถูก

**คำถาม:** ต้อง book ล่วงหน้ากี่ hr

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / Reservation, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 167. [PASS] ถูก

**คำถาม:** จองก่อน 1 ชั่วโมงใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_cancel_1_hour)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.074` sec


---

## 168. [PASS] ถูก

**คำถาม:** walk in ได้ไหมหรือต้องจองก่อน

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / Reservation, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.051` sec


---

## 169. [PASS] ถูก

**คำถาม:** จองได้สูงสุดกี่ session

**คำตอบ(จาก AI):**

คำตอบ:
การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_max_sessions / curated_reservation_max_sessions)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.039` sec


---

## 170. [PASS] ถูก

**คำถาม:** ครั้งนึงจองได้กี่รอบ

**คำตอบ(จาก AI):**

คำตอบ:
- การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_max_sessions)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.119` sec


---

## 171. [PASS] ถูก

**คำถาม:** one booking max sessions?

**คำตอบ(จาก AI):**

คำตอบ:
One booking can include a maximum of 3 sessions. This information is found in both SOURCE 1 and SOURCE 2, which are identical except for the language used.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `9.500` sec


---

## 172. [PASS] ถูก

**คำถาม:** จองทีเดียว 4 sessions ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_max_sessions)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.179` sec


---

## 173. [PASS] ถูก

**คำถาม:** จองสามรอบได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_max_sessions)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.076` sec


---

## 174. [PASS] ถูก

**คำถาม:** หลังจองต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 175. [PASS] ถูก

**คำถาม:** ไม่จ่ายใน 10 นาทีจะเกิดอะไร

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.029` sec


---

## 176. [PASS] ถูก

**คำถาม:** payment timeout กี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 177. [PASS] ถูก

**คำถาม:** จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.052` sec


---

## 178. [PASS] ถูก

**คำถาม:** ชำระเงินหลัง booking ต้องเร็วแค่ไหน

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, จองใหม่
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.063` sec


---

## 179. [PASS] ถูก

**คำถาม:** กดจองแล้วแก้ไขได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.093` sec


---

## 180. [PASS] ถูก

**คำถาม:** ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ:
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_edit_booking / Reservation, curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.065` sec


---

## 181. [PASS] ถูก

**คำถาม:** แก้เวลา booking ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_edit_booking / Reservation, curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.033` sec


---

## 182. [PASS] ถูก

**คำถาม:** ต้องยกเลิกแล้วจองใหม่ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.110` sec


---

## 183. [PASS] ถูก

**คำถาม:** แนบสลิปเดิมตอนจองใหม่ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_edit_booking / Reservation, curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.065` sec


---

## 184. [PASS] ถูก

**คำถาม:** สิทธิ์การจองโอนให้เพื่อนได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_non_transferable)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.142` sec


---

## 185. [PASS] ถูก

**คำถาม:** ให้คนอื่นมาใช้ booking แทนได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_non_transferable / Reservation, curated_booking_non_transferable)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.077` sec


---

## 186. [PASS] ถูก

**คำถาม:** transfer booking ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_non_transferable / Reservation, curated_booking_non_transferable)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 187. [PASS] ถูก

**คำถาม:** จองแทนกันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_non_transferable / Reservation, curated_booking_non_transferable)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.014` sec


---

## 188. [PASS] ถูก

**คำถาม:** เช็คอินล่วงหน้าได้กี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.038` sec


---

## 189. [PASS] ถูก

**คำถาม:** check in ได้เร็วสุดกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: Check-in สามารถทำได้ล่วงหน้าสูงสุดถึง 30 นาทีเท่านั้น ตามข้อมูลจากแหล่งที่มา [SOURCE 2]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.700` sec


---

## 190. [PASS] ถูก

**คำถาม:** เช็คอินก่อนเวลาได้ 1800 วินาทีไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.162` sec


---

## 191. [PASS] ถูก

**คำถาม:** ต้องเช็คอินก่อนเริ่มรอบใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.132` sec


---

## 192. [PASS] ถูก

**คำถาม:** ถ้า check-in ไม่ทันจะโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ:
ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_late / curated_checkin_late_cancel)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, ไม่มีการคืนเงิน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 193. [PASS] ถูก

**คำถาม:** เช็คอินต้องใช้บัตรอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_id_required)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บัตรประชาชน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.104` sec


---

## 194. [PASS] ถูก

**คำถาม:** แสดงบัตรประชาชนได้ไหมตอนเช็คอิน

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_id_required)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บัตรประชาชน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.115` sec


---

## 195. [PASS] ถูก

**คำถาม:** ชำระเงินผ่านอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ชำระเงินโดยโอนเข้าบัญชี Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.082` sec


---

## 196. [PASS] ถูก

**คำถาม:** โอนเงินไปบัญชีไหน

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 197. [PASS] ถูก

**คำถาม:** ชื่อบัญชีจ่ายค่าจองคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 198. [PASS] ถูก

**คำถาม:** เลขบัญชีธนาคารสำหรับจองคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 199. [PASS] ถูก

**คำถาม:** ธนาคารที่ใช้รับเงินคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคารไทยพาณิชย์, 795-276244-1
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 200. [PASS] ถูก

**คำถาม:** PS5 มี Spider-Man 2 ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม PlayStation 5 ที่มีในรายการรวมถึง Marvel’s Spider-Man 2, Fortnite, God of War Ragnarok และ TEKKEN 8

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_ps5_specific_games / Reservation, curated_games_ps5, reservation-service-ps5)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Spider-Man 2
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.042` sec


---

## 201. [PASS] ถูก

**คำถาม:** เพลย์ห้ามี tekken 8 หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ:
เกม PlayStation 5 ที่มีในรายการรวมถึง Marvel’s Spider-Man 2, Fortnite, God of War Ragnarok และ TEKKEN 8

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_ps5_specific_games / Reservation, curated_games_ps5, reservation-service-ps5)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.040` sec


---

## 202. [PASS] ถูก

**คำถาม:** เกมบน PlayStation มีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
เกม PlayStation 5 ที่มีในรายการ ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_ps5_games / Reservation, curated_games_ps5, reservation-service-ps5)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.051` sec


---

## 203. [PASS] ถูก

**คำถาม:** PS5 เล่น Fortnite ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม PlayStation 5 ที่มีในรายการรวมถึง Marvel’s Spider-Man 2, Fortnite, God of War Ragnarok และ TEKKEN 8

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_ps5_specific_games / Reservation, curated_games_ps5, reservation-service-ps5)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Fortnite
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 204. [PASS] ถูก

**คำถาม:** มี God of War Ragnarok ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม PlayStation 5 ที่มีในรายการรวมถึง Marvel’s Spider-Man 2, Fortnite, God of War Ragnarok และ TEKKEN 8

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_ps5_specific_games / Reservation, curated_games_ps5, reservation-service-ps5)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, God of War Ragnarok
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 205. [PASS] ถูก

**คำถาม:** Switch มี Mario Kart ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_switch_specific_games / Reservation, curated_games_switch, reservation-service-nintendo)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.050` sec


---

## 206. [PASS] ถูก

**คำถาม:** นินเทนโดมี Overcooked 2 ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_switch_specific_games / Reservation, curated_games_switch, reservation-service-nintendo)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Overcooked 2
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.049` sec


---

## 207. [PASS] ถูก

**คำถาม:** เกม Nintendo มีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
เกม Nintendo Switch ที่มีในรายการ ได้แก่ Pokémon Champions, Animal Crossing: New Horizon, It Takes Two, Little Nightmares II, Luigi’s Mansion 3, Mario Kart 8 Deluxe, Mario Party Superstars, Monster Hunter Rise, Moving Out 2, New Super Mario Bros. U Deluxe, Nintendo Switch Sports, Overcooked, Overcooked 2, Ring Fit Adventure, Super Mario Odyssey, Super Smash Bros Ultimate และ The Legend of Zelda: Breath of The Wild

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_switch_games / Reservation, curated_games_switch, reservation-service-nintendo)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.043` sec


---

## 208. [PASS] ถูก

**คำถาม:** เล่น Super Smash Bros ที่ศูนย์ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_switch_specific_games / Reservation, curated_games_switch, reservation-service-nintendo)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Super Smash
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.070` sec


---

## 209. [PASS] ถูก

**คำถาม:** Switch Sports มีไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_switch_specific_games / Reservation, curated_games_switch, reservation-service-nintendo)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Switch Sports
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 210. [PASS] ถูก

**คำถาม:** PC มี valorant ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 211. [PASS] ถูก

**คำถาม:** คอมเล่น CS2 ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, Counter-Strike 2
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.027` sec


---

## 212. [PASS] ถูก

**คำถาม:** PC games list

**คำตอบ(จาก AI):**

Answer:
PC games include Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT, and Call of Duty: Warzone.

Sources:
- https://esports.computing.psu.ac.th/ (rule_pc_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.012` sec


---

## 213. [PASS] ถูก

**คำถาม:** มี PUBG บน PC ไหม

**คำตอบ(จาก AI):**

คำตอบ: ในรายการเกมที่ปรากฏในรายการเกมบน PC (SOURCE 1) มี PUBG: BATTLEGROUNDS เป็นหนึ่งในเกมที่แสดงให้เห็นว่ามี PUBG บน PC

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, PUBG
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.701` sec


---

## 214. [PASS] ถูก

**คำถาม:** Warzone อยู่เครื่อง PC ไหน

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, Warzone
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 215. [PASS] ถูก

**คำถาม:** VR เล่นเกมอะไร

**คำตอบ(จาก AI):**

คำตอบ:
เกม VR Station ที่มีในรายการ ได้แก่ Beat Saber และ Horizon Call of the Mountain

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_vr_games / Reservation, curated_games_vr, reservation-service-vr)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 216. [PASS] ถูก

**คำถาม:** Beat Saber มีไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม VR Station ที่มีในรายการ ได้แก่ Beat Saber และ Horizon Call of the Mountain

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_vr_specific_games / Reservation, curated_games_vr, reservation-service-vr)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.018` sec


---

## 217. [PASS] ถูก

**คำถาม:** แว่น VR มี Horizon ไหม

**คำตอบ(จาก AI):**

คำตอบ:
เกม VR Station ที่มีในรายการ ได้แก่ Beat Saber และ Horizon Call of the Mountain

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_vr_specific_games / Reservation, curated_games_vr, reservation-service-vr)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Horizon
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 218. [PASS] ถูก

**คำถาม:** Cockpit เล่นเกมอะไร

**คำตอบ(จาก AI):**

คำตอบ:
Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_cockpit_games / Reservation, curated_games_cockpit, reservation-service-cockpit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, Gran Turismo 7
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.038` sec


---

## 219. [PASS] ถูก

**คำถาม:** พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
Cockpit หรือพวงมาลัยใช้เล่นเกม Gran Turismo 7 (Single Player) ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_cockpit_gran_turismo / Reservation, curated_games_cockpit, reservation-service-cockpit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gran Turismo 7
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.103` sec


---

## 220. [PASS] ถูก

**คำถาม:** PC Zone มีอุปกรณ์อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_equipment_pc_zone / home, curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, Gaming Monitor, Gaming Chair
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 221. [PASS] ถูก

**คำถาม:** คอมที่ศูนย์มีทั้งหมดกี่เครื่อง

**คำตอบ(จาก AI):**

คำตอบ:
- ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units
- Cockpit Zone มี TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 Steering Wheel Stand with Seat Set 2 Units และ Pulse Elite Wireless Headset 2 Units
- VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_cockpit_zone)
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.145` sec


---

## 222. [PASS] ถูก

**คำถาม:** Gaming PC รุ่นอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: MSI MAG Infinite S3, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.098` sec


---

## 223. [PASS] ถูก

**คำถาม:** เก้าอี้เกมมิ่งมีไหมใน PC zone

**คำตอบ(จาก AI):**

คำตอบ:
ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_equipment_pc_zone / home, curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming Chair, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.073` sec


---

## 224. [PASS] ถูก

**คำถาม:** เมาส์กับหูฟังมีให้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_equipment_pc_zone / home, curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming Mouse, Gaming Headset
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.026` sec


---

## 225. [PASS] ถูก

**คำถาม:** Cockpit zone มีทีวีขนาดกี่นิ้ว

**คำตอบ(จาก AI):**

คำตอบ:
- Cockpit Zone มี TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 Steering Wheel Stand with Seat Set 2 Units และ Pulse Elite Wireless Headset 2 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_cockpit_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.158` sec


---

## 226. [PASS] ถูก

**คำถาม:** พวงมาลัยใช้รุ่นอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- Cockpit Zone มี TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 Steering Wheel Stand with Seat Set 2 Units และ Pulse Elite Wireless Headset 2 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_cockpit_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.115` sec


---

## 227. [PASS] ถูก

**คำถาม:** Nintendo zone มีทีวีกี่นิ้ว

**คำตอบ(จาก AI):**

คำตอบ:
- Nintendo Switch Zone มี TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch (OLED model) Neon Red Neon Blue set 1 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_nintendo_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.127` sec


---

## 228. [PASS] ถูก

**คำถาม:** PS5 zone มีเครื่องกี่เครื่อง

**คำตอบ(จาก AI):**

คำตอบ:
- PLAYstation5 Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_ps5_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.135` sec


---

## 229. [PASS] ถูก

**คำถาม:** VR zone ใช้แว่นรุ่นอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.136` sec


---

## 230. [PASS] ถูก

**คำถาม:** เอาขนมเข้าไปกินตรงโต๊ะได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_food_drink / Reservation, curated_rule_food_drinks)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, พื้นที่ที่กำหนด
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 231. [PASS] ถูก

**คำถาม:** กินน้ำในพื้นที่เล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_food_drink / Reservation, curated_rule_food_drinks)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, พื้นที่ที่กำหนด
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 232. [PASS] ถูก

**คำถาม:** ต้องฝากกระเป๋าก่อนไหม

**คำตอบ(จาก AI):**

คำตอบ: ในแหล่งข้อมูลที่ให้มีคำแนะนำเกี่ยวกับการฝากสัมภาระว่า "กรุณาฝากสัมภาระก่อนเข้าใช้บริการ" ซึ่งหมายความว่าผู้ใช้งานต้องฝากกระเป๋าหรือสัมภาระก่อนที่จะเข้าใช้บริการ

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ฝากสัมภาระ
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.099` sec


---

## 233. [PASS] ถูก

**คำถาม:** ใช้เสียงดังได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_noise_language / Reservation, curated_rule_noise_language)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: งด, เสียงดัง
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.020` sec


---

## 234. [PASS] ถูก

**คำถาม:** พูดจาเสียดสีคนอื่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_noise_language / Reservation, curated_rule_noise_language)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, เสียดสี
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.029` sec


---

## 235. [PASS] ถูก

**คำถาม:** ทิ้งขยะไว้ในโซนเล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_trash_personal_items)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ทิ้งขยะ
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.131` sec


---

## 236. [PASS] ถูก

**คำถาม:** สูบบุหรี่ในศูนย์ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 237. [PASS] ถูก

**คำถาม:** เอาแอลกอฮอล์เข้าได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.022` sec


---

## 238. [PASS] ถูก

**คำถาม:** พกมีดเข้าไปได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_weapons_gambling / Reservation, curated_rule_weapons_gambling)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.017` sec


---

## 239. [PASS] ถูก

**คำถาม:** เล่นพนันในห้องได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_weapons_gambling / Reservation, curated_rule_weapons_gambling)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.030` sec


---

## 240. [PASS] ถูก

**คำถาม:** เอาปลั๊กไฟส่วนตัวมาใช้ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัวมาใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_power_outlet)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.105` sec


---

## 241. [PASS] ถูก

**คำถาม:** ย้ายอุปกรณ์เองได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ห้ามเคลื่อนย้ายอุปกรณ์หรือสิ่งของใด ๆ โดยไม่ได้รับอนุญาต

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_move_equipment)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.088` sec


---

## 242. [PASS] ถูก

**คำถาม:** ทำอุปกรณ์เสียหายต้องจ่ายไหม

**คำตอบ(จาก AI):**

คำตอบ:
ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_damage_responsibility / Reservation, curated_damage_minor, curated_damage_moderate, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รับผิดชอบ, ค่าปรับ
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 243. [PASS] ถูก

**คำถาม:** รอยขีดข่วนเล็กน้อยโดนปรับเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100–500 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_minor_damage / curated_damage_minor)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 244. [PASS] ถูก

**คำถาม:** เบาะขาดต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_moderate_damage / curated_damage_moderate)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 245. [PASS] ถูก

**คำถาม:** หูฟังสายขาดค่าปรับเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_moderate_damage / curated_damage_moderate)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 246. [PASS] ถูก

**คำถาม:** จอแตกต้องชดเชยยังไง

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_severe_damage / Reservation, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ชดเชย, เต็มจำนวน
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 247. [PASS] ถูก

**คำถาม:** คอมพังต้องจ่ายเต็มไหม

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_severe_damage / Reservation, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ชดเชย, เต็มจำนวน
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.005` sec


---

## 248. [PASS] ถูก

**คำถาม:** ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน

**คำตอบ(จาก AI):**

คำตอบ:
หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_penalty_temp_suspension / Reservation, curated_penalty_temp_suspension, reservation-penalty-001)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 249. [PASS] ถูก

**คำถาม:** โดนแบนชั่วคราวกี่วัน

**คำตอบ(จาก AI):**

คำตอบ:
หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_penalty_temp_suspension / Reservation, curated_penalty_temp_suspension, reservation-penalty-001)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์, 1-7 วัน
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.029` sec


---

## 250. [PASS] ถูก

**คำถาม:** กรณีไหนแบนถาวร

**คำตอบ(จาก AI):**

คำตอบ: การระงับสิทธิ์ถาวรเกิดขึ้นเมื่อผู้ใช้งานกระทำการละเมิดกฎอย่างร้ายแรง เช่น การทำลายทรัพย์สินหรือพฤติกรรมที่เป็นภัยต่อความปลอดภัยของผู้อื่น ซึ่งสามารถดูได้จากข้อมูลใน [SOURCE 1]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์, ถาวร
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.378` sec


---

## 251. [PASS] ถูก

**คำถาม:** อุทธรณ์การลงโทษได้ภายในกี่วัน

**คำตอบ(จาก AI):**

คำตอบ:
- หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_penalty_temp_suspension)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 7 วัน
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.122` sec


---

## 252. [PASS] ถูก

**คำถาม:** ศูนย์เก็บประวัติคนทำผิดไหม

**คำตอบ(จาก AI):**

คำตอบ: ศูนย์จะบันทึกประวัติการละเมิดผ่านการใช้บริการ และอาจส่งผลต่อสิทธิ์ในการใช้บริการในอนาคต. ดังนี้คือข้อมูลที่เกี่ยวข้อง: [SOURCE 1]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บันทึก, ประวัติ
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.100` sec


---

## 253. [PASS] ถูก

**คำถาม:** ศูนย์นี้คืออะไรแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_overview_identity / curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.023` sec


---

## 254. [PASS] ถูก

**คำถาม:** PSU Esports Studio Phuket คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_overview_identity / curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.080` sec


---

## 255. [PASS] ถูก

**คำถาม:** ใครเป็นคนก่อตั้งศูนย์นี้

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_overview_founder / home, curated_overview_mission, curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.044` sec


---

## 256. [PASS] ถูก

**คำถาม:** หน่วยงานที่ดำเนินการคือใคร

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_overview_founder / home, curated_overview_mission, curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.039` sec


---

## 257. [PASS] ถูก

**คำถาม:** mission ของศูนย์คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_overview_identity / curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 258. [PASS] ถูก

**คำถาม:** ศูนย์อยู่ตรงไหน

**คำตอบ(จาก AI):**

คำตอบ: ศูนย์ PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.316` sec


---

## 259. [PASS] ถูก

**คำถาม:** ที่ตั้งของ studio คือที่ไหน

**คำตอบ(จาก AI):**

คำตอบ:
PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_location / curated_contact_location)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.049` sec


---

## 260. [PASS] ถูก

**คำถาม:** ขอ email ติดต่อ

**คำตอบ(จาก AI):**

คำตอบ:
อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_email / curated_contact_email)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.018` sec


---

## 261. [PASS] ถูก

**คำถาม:** Facebook ศูนย์ชื่ออะไร

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 262. [PASS] ถูก

**คำถาม:** เบอร์โทรระบบจองมีเบอร์อะไร

**คำตอบ(จาก AI):**

คำตอบ:
เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_contact_phone / curated_contact_phone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 263. [PASS] ถูก

**คำถาม:** อีสปอร์ตคืออะไรแบบเข้าใจง่าย

**คำตอบ(จาก AI):**

คำตอบ:
- อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_definition)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.179` sec


---

## 264. [PASS] ถูก

**คำถาม:** esports เริ่มครั้งแรกที่ไหน

**คำตอบ(จาก AI):**

คำตอบ:
Esports เริ่มขึ้นครั้งแรกที่มหาวิทยาลัยสแตนฟอร์ด (Stanford University) ในวันที่ 19 ตุลาคม ค.ศ. 1972 โดยการแข่งขันเกม Spacewar ภายใต้ชื่องาน Intergalactic Spacewar Olympics

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Stanford, 1972
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.417` sec


---

## 265. [PASS] ถูก

**คำถาม:** Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- อีสปอร์ตเกิดขึ้นครั้งแรกในวันที่ 19 ตุลาคม ค.ศ. 1972 ณ มหาวิทยาลัยสแตนฟอร์ด (Standford University) จากการแข่งขันเกม Spacewar ภายใต้ชื่องาน Intergalactic Spacewar Olympics

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_origin)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Spacewar, 1972
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.176` sec


---

## 266. [PASS] ถูก

**คำถาม:** เกมประเภท MOBA คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_categories)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: MOBA
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.110` sec


---

## 267. [PASS] ถูก

**คำถาม:** อาชีพในวงการ esports มีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
- อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ
- อาชีพที่เกี่ยวข้องกับกีฬาอีสปอร์ต ได้แก่ นักกีฬาอีสปอร์ต, โค้ชอีสปอร์ต, ผู้จัดการทีมอีสปอร์ต, นักพากย์การแข่งขันอีสปอร์ต, ผู้จัดการแข่งขันอีสปอร์ต, นักวิเคราะห์อีสปอร์ต, นักเขียนข่าวอีสปอร์ต, นักจิตวิทยาอีสปอร์ต, นักโภชนาการอีสปอร์ต และนักกายภาพบำบัดอีสปอร์ต

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_definition)
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_careers)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.121` sec


---

## 268. [PASS] ถูก

**คำถาม:** Overcooked 2 ฝึกทักษะอะไร

**คำตอบ(จาก AI):**

คำตอบ:
Overcooked! 2 ฝึกทักษะการทำงานเป็นทีม, การจัดการสถานการณ์กดดัน, การสื่อสารอย่างชัดเจน, และการวางแผน.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: การทำงานเป็นทีม, สื่อสาร
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.785` sec


---

## 269. [PASS] ถูก

**คำถาม:** Mario Kart 8 Deluxe ฝึกอะไร

**คำตอบ(จาก AI):**

Mario Kart 8 Deluxe ฝึกไหวพริบและการตัดสินใจในการแข่งขัน. ในเกมนี้ผู้เล่นต้องควบคุมตัวละครและรถบนสนามที่เต็มไปด้วยทางโค้ง, สิ่งกีดขวาง และไอเทมหลากหลายรูปแบบ ทำให้จำเป็นต้องใช้วาทีและการคิดอย่างรวดเร็ว. นอกจากนี้ยังฝึกทักษะการประเมินสถานการณ์แบบเรียล

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไหวพริบ, การตัดสินใจ
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.785` sec


---

## 270. [PASS] ถูก

**คำถาม:** วันที่ 25 เมษายน 2569 แข่งเกมอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/events-news/news (curated_news_cs2_2026)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: News
หมวด: events_news
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.160` sec


---

## 271. [PASS] ถูก

**คำถาม:** VALORANT 2026 จัดวันไหน

**คำตอบ(จาก AI):**

คำตอบ:
- PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/events-news/news (curated_news_valorant_2026)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: News
หมวด: events_news
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.124` sec


---

## 272. [PASS] ถูก

**คำถาม:** SURAT SMASH ส่งตัวแทนกี่คน

**คำตอบ(จาก AI):**

คำตอบ:
- ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/events-news/news (curated_news_surat_smash_tekken8)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: News
หมวด: events_news
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.133` sec


---

## 273. [PASS] ถูก

**คำถาม:** นักศึกษาชาวจีนมีกี่คน

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/events-news/news (curated_news_chinese_students_game_based_learning)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: News
หมวด: events_news
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.092` sec


---

## 274. [PASS] ถูก

**คำถาม:** GAME ON เปิดโลกอีสปอร์ตจัดให้ใคร

**คำตอบ(จาก AI):**

คำตอบ:
- กิจกรรม GAME ON! เปิดโลกอีสปอร์ต จัดสำหรับนักเรียนชั้นมัธยมศึกษาปีที่ 3 (ม.3) จากโรงเรียนท้ายเหมืองวิทยา จำนวน 21 คน

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/events-news/news (curated_news_game_on_thaimuang)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: News
หมวด: events_news
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['News']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.126` sec


---

## 275. [PASS] ถูก

**คำถาม:** อธิการบดีในหน้าสมาชิกคือใคร

**คำตอบ(จาก AI):**

คำตอบ:
- หน้าสมาชิกระบุว่า ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_president)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Members
หมวด: about_us
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.111` sec


---

## 276. [PASS] ถูก

**คำถาม:** คณบดีวิทยาลัยการคอมพิวเตอร์คือใคร

**คำตอบ(จาก AI):**

คำตอบ:
- หน้าสมาชิกระบุว่า รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_dean)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Members
หมวด: about_us
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.126` sec


---

## 277. [PASS] ถูก

**คำถาม:** ผู้จัดการศูนย์คือใคร

**คำตอบ(จาก AI):**

คำตอบ:
- หน้าสมาชิกระบุว่า นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_manager)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Members
หมวด: about_us
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.076` sec


---

## 278. [PASS] ถูก

**คำถาม:** ประธาน PSU Phuket Esports Club คือใคร

**คำตอบ(จาก AI):**

คำตอบ:
- หน้าสมาชิกระบุว่า นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_club_president)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Members
หมวด: about_us
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.149` sec


---

## 279. [PASS] ถูก

**คำถาม:** Gallery มีหมวดภาพอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- หน้า Gallery มีหมวดภาพ Nintendo Switch และ PlayStation 5

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Gallery (curated_about_gallery_categories)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Members
หมวด: about_us
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Members']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.103` sec


---

## 280. [PASS] ถูก

**คำถาม:** มีบริการซ่อมคอมส่วนตัวไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์มีบริการซ่อมคอมพิวเตอร์ส่วนตัวในฐานข้อมูลที่มี ข้อมูลที่มีตอนนี้เน้นการจองใช้อุปกรณ์ภายในศูนย์และกฎการใช้งาน หากต้องการยืนยันเรื่องซ่อมอุปกรณ์ส่วนตัวควรติดต่อเจ้าหน้าที่ศูนย์โดยตรง

แหล่งข้อมูล:
- ฐานข้อมูลที่มี (rule_no_answer_repair_personal_pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.003` sec


---

## 281. [PASS] ถูก

**คำถาม:** ส่งอาหารถึงโต๊ะเกมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่ามีบริการจัดส่งอาหารถึงโต๊ะเล่นเกมในฐานข้อมูลที่มี และตามกฎที่มี อาหารและเครื่องดื่มควรรับประทานเฉพาะในพื้นที่ที่กำหนดเท่านั้น จึงไม่ควรสรุปว่าสามารถส่งหรือทานที่โต๊ะเล่นเกมได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_food_delivery / Reservation, curated_rule_food_drinks)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.035` sec


---

## 282. [PASS] ถูก

**คำถาม:** เอาแมวเข้าได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องการนำสัตว์เลี้ยงเข้าศูนย์ในฐานข้อมูลที่มี จึงยังไม่ควรตอบว่าอนุญาต หากจำเป็นต้องนำสัตว์เลี้ยงมาด้วยควรติดต่อเจ้าหน้าที่ศูนย์ก่อนเข้าใช้บริการ

แหล่งข้อมูล:
- ฐานข้อมูลที่มี (rule_no_answer_pets)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.018` sec


---

## 283. [PASS] ถูก

**คำถาม:** สมัครสมาชิกรายปีราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี ข้อมูลราคาที่มีตอนนี้เป็นค่าบริการตามประเภทอุปกรณ์และกลุ่มผู้ใช้ เช่น PSU Student and Staff, PSU Alumni and General Student และ General Adult

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (rule_no_answer_annual_membership / service_fee)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.038` sec


---

## 284. [PASS] ถูก

**คำถาม:** เช่าโน้ตบุ๊กกลับบ้านได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการเช่าโน้ตบุ๊กกลับบ้านในฐานข้อมูลที่มี ข้อมูลที่มีระบุการจองใช้อุปกรณ์ภายในศูนย์เป็นรอบเวลา จึงยังไม่ควรสรุปว่าสามารถนำอุปกรณ์กลับไปใช้นอกสถานที่ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_laptop_rental_home / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 285. [PASS] ถูก

**คำถาม:** มีห้องนอนพักค้างคืนไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องห้องนอนหรือบริการพักค้างคืนในฐานข้อมูลที่มี ข้อมูลเวลาที่มีระบุการใช้งานเป็นรอบเวลาในช่วง 09:00-16:00 และมีช่วง Maintenance ตามตาราง จึงไม่ควรสรุปว่ามีบริการพักค้างคืน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_overnight_room / Reservation, curated_schedule_weekly)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.031` sec


---

## 286. [PASS] ถูก

**คำถาม:** ขายคีย์บอร์ดเกมมิ่งไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_no_answer_keyboard_sales / home, curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 287. [PASS] ถูก

**คำถาม:** รับซ่อมจอย PS5 ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์รับซ่อมจอย PS5 หรือคอนโทรลเลอร์ส่วนตัวในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์และกฎการรับผิดชอบเมื่อทำอุปกรณ์ของศูนย์เสียหาย หากต้องการซ่อมอุปกรณ์ส่วนตัวควรสอบถามเจ้าหน้าที่โดยตรง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_controller_repair / Reservation, curated_damage_moderate, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 288. [PASS] ถูก

**คำถาม:** มีบริการส่งเครื่องเกมไปบ้านไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.056` sec


---

## 289. [PASS] ถูก

**คำถาม:** ซื้อเกม Steam ผ่านศูนย์ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์มีบริการซื้อเกม Steam ผ่านศูนย์ในฐานข้อมูลที่มี ข้อมูลที่มีตอนนี้เป็นรายการเกมและบริการใช้อุปกรณ์ภายในศูนย์ ไม่ใช่บริการจำหน่ายเกม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_steam_purchase / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.049` sec


---

## 290. [PASS] ถูก

**คำถาม:** มีคอร์สสอนเล่น Valorant ส่วนตัวไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องคอร์สสอนเล่นเกมแบบส่วนตัวในฐานข้อมูลที่มี ข้อมูลที่มีระบุรายการเกมและกิจกรรม/การแข่งขันของศูนย์ แต่ยังไม่มีรายละเอียดบริการสอนส่วนตัว หากสนใจควรถามเจ้าหน้าที่หรือเพจของศูนย์อีกครั้ง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_private_course / Reservation, Events_and_News)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.071` sec


---

## 291. [PASS] ถูก

**คำถาม:** จ่ายด้วยคริปโตได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์รับชำระด้วยคริปโตในฐานข้อมูลที่มี ข้อมูลการชำระเงินที่ยืนยันได้คือชำระโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงินในระบบจอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_crypto_payment / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.030` sec


---

## 292. [PASS] ถูก

**คำถาม:** ผ่อนชำระค่าเล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องการผ่อนชำระค่าใช้บริการในฐานข้อมูลที่มี ข้อมูลที่มีระบุว่าหลังจองต้องชำระเงินทันที และหากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก จึงควรยึดตามการชำระเงินตามรอบจองก่อน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_installment / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.028` sec


---

## 293. [PASS] ถูก

**คำถาม:** มีส่วนลดวันเกิดไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องส่วนลดวันเกิดในฐานข้อมูลที่มี ข้อมูลราคาที่มีตอนนี้เป็นตารางค่าบริการตามประเภทอุปกรณ์และกลุ่มผู้ใช้ หากมีโปรโมชันพิเศษควรตรวจสอบกับเพจหรือเจ้าหน้าที่ศูนย์ก่อนจอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (rule_no_answer_birthday_discount / service_fee)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.025` sec


---

## 294. [PASS] ถูก

**คำถาม:** จองแบบเหมาทั้งวันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องการจองแบบเหมาทั้งวันในฐานข้อมูลที่มี ข้อมูลการจองที่มีระบุว่าการจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions และต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง จึงควรใช้เงื่อนไขนี้ก่อนหากไม่มีประกาศอื่นเพิ่มเติม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_full_day_booking / Reservation, curated_reservation_max_sessions, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 295. [PASS] ถูก

**คำถาม:** เอาเครื่อง PC ตัวเองมาตั้งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าสามารถนำ PC หรือคอมพิวเตอร์ส่วนตัวมาตั้งใช้งานในศูนย์ได้ในฐานข้อมูลที่มี ข้อมูลที่มีระบุบริการและอุปกรณ์ของศูนย์สำหรับจองใช้งานภายในสถานที่ จึงควรสอบถามเจ้าหน้าที่ก่อนนำอุปกรณ์ส่วนตัวเข้ามา

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_no_answer_own_pc_setup / home, Reservation, curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.061` sec


---

## 296. [PASS] ถูก

**คำถาม:** มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการถ่ายรูปโปรไฟล์เกมเมอร์ในฐานข้อมูลที่มี ข้อมูลที่มีครอบคลุมบริการใช้อุปกรณ์ พื้นที่เล่นเกม และกิจกรรมของศูนย์ แต่ยังไม่พบรายละเอียดบริการถ่ายภาพ

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_no_answer_photo_profile / Services, Events_and_News)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.056` sec


---

## 297. [PASS] ถูก

**คำถาม:** มีอาหารบุฟเฟต์ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์มีบริการอาหารบุฟเฟต์ในฐานข้อมูลที่มี และกฎที่มีระบุว่าอาหารและเครื่องดื่มควรรับประทานเฉพาะในพื้นที่ที่กำหนดเท่านั้น จึงไม่ควรสรุปว่ามีบริการบุฟเฟต์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_food_buffet / Reservation, curated_rule_food_drinks)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.020` sec


---

## 298. [PASS] ถูก

**คำถาม:** รับจัดงานแต่งในศูนย์ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลว่าศูนย์รับจัดงานแต่งในฐานข้อมูลที่มี ข้อมูลที่มีเกี่ยวกับบริการศูนย์อีสปอร์ต การจองใช้อุปกรณ์ กิจกรรม และการแข่งขัน หากเป็นงานพิเศษนอกเหนือจากนี้ควรติดต่อเจ้าหน้าที่ศูนย์โดยตรง

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (rule_no_answer_wedding_event / Services, Events_and_News, Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.033` sec


---

## 299. [PASS] ถูก

**คำถาม:** ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
ถ้าหลังจองไม่ชำระเงินภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่ หากมีการจองสำเร็จแล้วแต่เช็คอินไม่ทันก่อนเริ่มรอบ ระบบจะยกเลิกการจองทันทีและไม่มีการคืนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_and_late_checkin / Reservation, curated_payment_10_minutes, curated_checkin_late_cancel)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก, ไม่มีการคืนเงิน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.104` sec


---

## 300. [PASS] ถูก

**คำถาม:** ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
สรุปสั้นๆ: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาทีและต้องเช็คอินก่อนเริ่มรอบ, หากต้องยกเลิกหรือแก้ไขการจองควรดำเนินการล่วงหน้าอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_reservation_quick_summary / Reservation, curated_reservation_advance_time, curated_checkin_30_minutes, curated_cancel_1_hour)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง, 30 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.085` sec


---

## 301. [PASS] ถูก

**คำถาม:** จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และหลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_session_and_payment / Reservation, curated_reservation_max_sessions, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.101` sec


---

## 302. [PASS] ถูก

**คำถาม:** กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม

**คำตอบ(จาก AI):**

คำตอบ:
ตอนจองต้องกรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล, เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี จากนั้นชำระเงินโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_user_info_and_slip / Reservation, curated_user_info_required, curated_booking_steps, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: สลิป, โอนเงิน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.059` sec


---

## 303. [PASS] ถูก

**คำถาม:** ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / Reservation, curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.081` sec


---

## 304. [PASS] ถูก

**คำถาม:** นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.148` sec


---

## 305. [PASS] ถูก

**คำถาม:** คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า

**คำตอบ(จาก AI):**

คำตอบ:
- ค่าบริการ Nintendo Switch 3-4 คน ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 100 บาท, บุคคลทั่วไป 280 บาท
- ค่าบริการ Nintendo Switch 1-2 คน ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 50 บาท, บุคคลทั่วไป 140 บาท
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
- ค่าบริการ Cockpit ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 65 บาท, บุคคลทั่วไป 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_nintendo_3_4_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service
... [trimmed output]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.128` sec


---

## 306. [PASS] ถูก

**คำถาม:** General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ค่าบริการ Nintendo Switch 1-2 คน ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 50 บาท, บุคคลทั่วไป 140 บาท
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
- ค่าบริการ Nintendo Switch 3-4 คน ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 100 บาท, บุคคลทั่วไป 280 บาท
- ค่าบริการ PlayStation 5 ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 50 บาท, บุคคลทั่วไป 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_nintendo_1_2_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_s
... [trimmed output]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.129` sec


---

## 307. [PASS] ถูก

**คำถาม:** ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (VR 1 ชั่วโมง)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.224` sec


---

## 308. [PASS] ถูก

**คำถาม:** ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.231` sec


---

## 309. [PASS] ถูก

**คำถาม:** ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
กรณีนี้เกี่ยวกับหลายกฎพร้อมกัน: อาหารและเครื่องดื่มรับประทานได้เฉพาะพื้นที่ที่กำหนด, ควรงดส่งเสียงดังเกินควร, และถ้าทำอุปกรณ์เสียหายผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_mixed_food_noise_damage / Reservation, curated_rule_food_drinks, curated_rule_noise_language, curated_damage_minor, curated_damage_moderate, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, เสียงดัง
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 310. [PASS] ถูก

**คำถาม:** ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม

**คำตอบ(จาก AI):**

คำตอบ:
กรณีทรัพย์สินส่วนตัวสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี ส่วนกรณีทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_mixed_lost_and_damage / Reservation, curated_rule_lost_items, curated_damage_minor, curated_damage_moderate, curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่รับผิดชอบ, รับผิดชอบ
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 311. [PASS] ถูก

**คำถาม:** ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม

**คำตอบ(จาก AI):**

คำตอบ:
ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_weapons_gambling / Reservation, curated_rule_weapons_gambling)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.062` sec


---

## 312. [PASS] ถูก

**คำถาม:** ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ:
กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_return_equipment_games / Reservation, curated_rule_return_equipment, reservation-studio-rules)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: คืน, หลังจากใช้งานเสร็จ
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.089` sec


---

## 313. [PASS] ถูก

**คำถาม:** ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร

**คำตอบ(จาก AI):**

คำตอบ:
หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_report_problem / Reservation, curated_rule_report_problem)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: แจ้งเจ้าหน้าที่
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.055` sec


---

## 314. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 315. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.127` sec


---

## 316. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.182` sec


---

## 317. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 318. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.033` sec


---

## 319. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.029` sec


---

## 320. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.042` sec


---

## 321. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.030` sec


---

## 322. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 323. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.159` sec


---

## 324. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.215` sec


---

## 325. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 326. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.053` sec


---

## 327. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 328. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.051` sec


---

## 329. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.041` sec


---

## 330. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.050` sec


---

## 331. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.170` sec


---

## 332. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.208` sec


---

## 333. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.049` sec


---

## 334. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.045` sec


---

## 335. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 336. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.049` sec


---

## 337. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.037` sec


---

## 338. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.059` sec


---

## 339. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 150 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: บุคคลทั่วไป

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.142` sec


---

## 340. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.240` sec


---

## 341. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.055` sec


---

## 342. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.058` sec


---

## 343. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.038` sec


---

## 344. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.057` sec


---

## 345. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.046` sec


---

## 346. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.048` sec


---

## 347. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.152` sec


---

## 348. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.187` sec


---

## 349. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.041` sec


---

## 350. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.042` sec


---

## 351. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.034` sec


---

## 352. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.044` sec


---

## 353. [PASS] ถูก

**คำถาม:** ขอเฟสศูนย์หน่อย ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: facebook.com/psuesportsphuket
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.036` sec


---

## 354. [PASS] ถูก

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
วันจันทร์ช่วง Morning 09:00–12:00 เป็น Maintenance* จึงยังไม่ใช่ช่วงเล่น/เปิดให้บริการ ส่วนช่วง Afternoon 13:00–16:00 เป็น Open for Service ดังนั้นวันจันทร์เปิดให้เล่นช่วง 13:00 น. และปิด 16:00 น.

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_monday_open_close / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.081` sec


---

## 355. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 0 บาทต่อ 60 นาที (PlayStation 5)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.194` sec


---

## 356. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- ราคา: 190 บาทต่อ 30 นาที (VR 30 นาที)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: service_fee
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['service_fee']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.286` sec


---

## 357. [PASS] ถูก

**คำถาม:** คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_specific_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.080` sec


---

## 358. [PASS] ถูก

**คำถาม:** เชคอินก่อนกี่นาที ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.070` sec


---

## 359. [PASS] ถูก

**คำถาม:** สูบบุหรี่ได้ปะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.061` sec


---

## 360. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
ยังไม่พบข้อมูลเรื่องบริการส่งหรือให้เช่าเครื่องเกม/จอกลับไปใช้ที่บ้านในฐานข้อมูลที่มี ข้อมูลที่มีเป็นการจองใช้อุปกรณ์ภายใน PSU Esports Studio ตามรอบเวลา ดังนั้นควรจองเพื่อใช้งานที่ศูนย์ หรือสอบถามเจ้าหน้าที่หากต้องการบริการนอกสถานที่

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_no_answer_home_delivery_console / Reservation)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.079` sec
