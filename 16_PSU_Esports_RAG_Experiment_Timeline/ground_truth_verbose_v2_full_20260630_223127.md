# Ground Truth Verbose Report

- ไฟล์: `c:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
- ข้อที่รัน: 1 - 360
- รวม: 360
- ถูก: 244
- ผิด/error: 116
- Accuracy: 67.78%
- Average latency: 0.579 sec
- Generated: 2026-06-30 22:31:27

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 9. [PASS] ถูก

**คำถาม:** วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม

**คำตอบ(จาก AI):**

คำตอบ: ในช่วง Morning (09:00 – 12:00) มีการ Maintenance และในช่วง Afternoon (13:00 – 16:00) เปิด Open for Service. ดังนั้น, คุณไม่สามารถเล่นได้ในช่วง Morning แต่สามารถใช้งานได้ในช่วง Afternoon.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.690` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 16. [PASS] ถูก

**คำถาม:** ศูนย์เปิดกีโมงปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
เปิด 09:00 น. และปิด 16:00 น. โดยแบ่งรอบบริการเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / curated_schedule_morning, curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.003` sec


---

## 17. [PASS] ถูก

**คำถาม:** เปิดปิดกี่โมงนะ

**คำตอบ(จาก AI):**

คำตอบ:
เปิด 09:00 น. และปิด 16:00 น. โดยแบ่งรอบบริการเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / curated_schedule_morning, curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 18. [PASS] ถูก

**คำถาม:** เวลาเปิดให้บริการคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
เปิด 09:00 น. และปิด 16:00 น. โดยแบ่งรอบบริการเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / curated_schedule_morning, curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 19. [PASS] ถูก

**คำถาม:** service hours คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
เปิด 09:00 น. และปิด 16:00 น. โดยแบ่งรอบบริการเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_service_schedule / curated_schedule_morning, curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 20. [PASS] ถูก

**คำถาม:** เปิดถึง 16:00 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เปิด 09:00 น. และปิด 16:00 น.
- ตารางบริการช่วง Morning คือ 09:00 – 12:00
- ตารางบริการช่วง Afternoon คือ 13:00 – 16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_schedule_morning)
- https://esports.computing.psu.ac.th/ (curated_schedule_afternoon)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.046` sec


---

## 21. [PASS] ถูก

**คำถาม:** ช่วงเช้าของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 22. [PASS] ถูก

**คำถาม:** Morning คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 23. [PASS] ถูก

**คำถาม:** รอบเช้า 09 ถึง 12 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 24. [PASS] ถูก

**คำถาม:** ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 25. [PASS] ถูก

**คำถาม:** ตอนเช้าเปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 26. [PASS] ถูก

**คำถาม:** รอบเช้าเริ่มตอนไหน

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Morning คือ 09:00–12:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 27. [PASS] ถูก

**คำถาม:** morning session time?

**คำตอบ(จาก AI):**

Answer:
The Morning service slot is 09:00-12:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 28. [PASS] ถูก

**คำถาม:** morning slot time

**คำตอบ(จาก AI):**

Answer:
The Morning service slot is 09:00-12:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_morning_time / Reservation, curated_schedule_morning, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 09:00, 12:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 29. [PASS] ถูก

**คำถาม:** ช่วงบ่ายของตารางคือเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Afternoon คือ 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 30. [PASS] ถูก

**คำถาม:** Afternoon คือกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Afternoon คือ 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 31. [PASS] ถูก

**คำถาม:** รอบบ่าย 13 ถึง 16 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Afternoon คือ 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 32. [PASS] ถูก

**คำถาม:** ช่วงบ่ายเปิดกี่โมงปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Afternoon คือ 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 33. [PASS] ถูก

**คำถาม:** รอบบ่ายปิดกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ตารางบริการช่วง Afternoon คือ 13:00–16:00

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 34. [PASS] ถูก

**คำถาม:** afternoon session time?

**คำตอบ(จาก AI):**

Answer:
The Afternoon service slot is 13:00-16:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 35. [PASS] ถูก

**คำถาม:** afternoon slot time

**คำตอบ(จาก AI):**

Answer:
The Afternoon service slot is 13:00-16:00.

Sources:
- https://esports.computing.psu.ac.th/ (rule_schedule_afternoon_time / Reservation, curated_schedule_afternoon, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 36. [PASS] ถูก

**คำถาม:** วันศุกร์ maintenance คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 37. [PASS] ถูก

**คำถาม:** Friday maintenance ทำอะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 38. [PASS] ถูก

**คำถาม:** maintenance weekly hardware inspection คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 39. [PASS] ถูก

**คำถาม:** วันศุกร์มีตรวจอุปกรณ์ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 40. [PASS] ถูก

**คำถาม:** ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning หรือการตรวจสอบฮาร์ดแวร์และทำความสะอาดรายสัปดาห์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance_general / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 41. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.001` sec


---

## 42. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 43. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 44. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 45. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง PS5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 46. [PASS] ถูก

**คำถาม:** PlayStation 5 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 47. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 48. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 49. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 50. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 51. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['50']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 52. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['50']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 53. [PASS] ถูก

**คำถาม:** บุคคลทั่วไป เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 54. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 55. [PASS] ถูก

**คำถาม:** PS5 สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 56. [PASS] ถูก

**คำถาม:** คนนอก เล่น PlayStation 5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.002` sec


---

## 57. [PASS] ถูก

**คำถาม:** General Adult เล่น PS5 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 58. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง PlayStation 5 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 150 บาท/session × 1 session(s) = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, 60, 150
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 59. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 60. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 61. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 62. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 63. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง Nintendo 1-2 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 64. [PASS] ถูก

**คำถาม:** Switch 1-2 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 65. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 66. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 67. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 68. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.003` sec


---

## 69. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['50']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 70. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 50
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['50']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.001` sec


---

## 71. [PASS] ถูก

**คำถาม:** บุคคลทั่วไป เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 72. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 73. [PASS] ถูก

**คำถาม:** Nintendo 1-2 คน สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 74. [PASS] ถูก

**คำถาม:** คนนอก เล่น Switch 1-2 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 75. [PASS] ถูก

**คำถาม:** General Adult เล่น Nintendo 1-2 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 76. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Switch 1-2 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 140 บาท/session × 1 session(s) = 140 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 1-2, 140
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 77. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.001` sec


---

## 78. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 79. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 80. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 81. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง Nintendo 3-4 คน ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 82. [PASS] ถูก

**คำถาม:** Switch 3-4 สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 83. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 100 บาท/session × 1 session(s) = 100 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 84. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 100 บาท/session × 1 session(s) = 100 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 85. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 100 บาท/session × 1 session(s) = 100 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 86. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 100 บาท/session × 1 session(s) = 100 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 87. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['100']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 88. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 100
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['100']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 89. [PASS] ถูก

**คำถาม:** บุคคลทั่วไป เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 90. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 91. [PASS] ถูก

**คำถาม:** Nintendo 3-4 คน สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 92. [PASS] ถูก

**คำถาม:** คนนอก เล่น Switch 3-4 กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 93. [PASS] ถูก

**คำถาม:** General Adult เล่น Nintendo 3-4 คน กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 94. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง Switch 3-4 ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, 3-4, 280
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 95. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 96. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 97. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 98. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 99. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง Cockpit ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 100. [PASS] ถูก

**คำถาม:** พวงมาลัยขับรถ สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 101. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 65 บาท/session × 1 session(s) = 65 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 102. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 65 บาท/session × 1 session(s) = 65 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 103. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 65 บาท/session × 1 session(s) = 65 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 104. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 65 บาท/session × 1 session(s) = 65 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 105. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['65']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 106. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 65
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['65']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 107. [PASS] ถูก

**คำถาม:** บุคคลทั่วไป เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 108. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 109. [PASS] ถูก

**คำถาม:** Cockpit สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 110. [PASS] ถูก

**คำถาม:** คนนอก เล่น พวงมาลัยขับรถ กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 111. [PASS] ถูก

**คำถาม:** General Adult เล่น Cockpit กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 112. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง พวงมาลัยขับรถ ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 200 บาท/session × 1 session(s) = 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Cockpit, 60, 200
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 113. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 114. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 115. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 116. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 117. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง VR 30 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 118. [PASS] ถูก

**คำถาม:** VR ครึ่งชั่วโมง สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 119. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 190 บาท/session × 1 session(s) = 190 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.003` sec


---

## 120. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 190 บาท/session × 1 session(s) = 190 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 121. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 190 บาท/session × 1 session(s) = 190 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 122. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 190 บาท/session × 1 session(s) = 190 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 123. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['190']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 124. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 190
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['190']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 125. [PASS] ถูก

**คำถาม:** บุคคลทั่วไป เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 126. [PASS] ถูก

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 127. [PASS] ถูก

**คำถาม:** VR 30 นาที สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 128. [PASS] ถูก

**คำถาม:** คนนอก เล่น VR ครึ่งชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 129. [PASS] ถูก

**คำถาม:** General Adult เล่น VR 30 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 130. [PASS] ถูก

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR ครึ่งชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 525 บาท/session × 1 session(s) = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 30, 525
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 131. [PASS] ถูก

**คำถาม:** นักศึกษา มอ เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 132. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษา มอ จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 133. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักเรียน ม.อ. จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.001` sec


---

## 134. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับนักเรียน ม.อ. ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 135. [PASS] ถูก

**คำถาม:** ถ้าเป็นเด็ก PSU จอง VR 1 ชั่วโมง ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 136. [PASS] ถูก

**คำถาม:** VR 60 นาที สำหรับเด็ก PSU ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 0, 0, บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 137. [PASS] ถูก

**คำถาม:** นักศึกษาทั่วไป เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 375 บาท/session × 1 session(s) = 375 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 138. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาทั่วไป จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 375 บาท/session × 1 session(s) = 375 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 139. [PASS] ถูก

**คำถาม:** นักศึกษาต่างมหาลัย เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 375 บาท/session × 1 session(s) = 375 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 140. [PASS] ถูก

**คำถาม:** ถ้าเป็นนักศึกษาต่างมหาลัย จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 375 บาท/session × 1 session(s) = 375 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 141. [FAIL] ผิด

**คำถาม:** ศิษย์เก่า PSU เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['375']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 142. [FAIL] ผิด

**คำถาม:** ถ้าเป็นศิษย์เก่า PSU จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 375
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['375']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 143. [FAIL] ผิด

**คำถาม:** บุคคลทั่วไป เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 144. [FAIL] ผิด

**คำถาม:** ถ้าเป็นบุคคลทั่วไป จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 145. [FAIL] ผิด

**คำถาม:** VR 1 ชั่วโมง สำหรับคนนอก ต้องจ่ายกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 146. [FAIL] ผิด

**คำถาม:** คนนอก เล่น VR 60 นาที กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 147. [FAIL] ผิด

**คำถาม:** General Adult เล่น VR 1 ชั่วโมง กี่บาทต่อชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 148. [FAIL] ผิด

**คำถาม:** ถ้าเป็นGeneral Adult จอง VR 60 นาที ราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 1,050 บาท/session × 1 session(s) = 1,050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, 1 ชั่วโมง, 1050
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['1050']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 149. [PASS] ถูก

**คำถาม:** ราคา PC ต่อชั่วโมงเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 150. [PASS] ถูก

**คำถาม:** นักเรียน มอ เล่น PC ฟรีไหม

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: นักศึกษา/บุคลากร PSU
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 151. [PASS] ถูก

**คำถาม:** คนนอกเล่นคอมต้องจ่ายเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: บุคคลทั่วไป
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 152. [PASS] ถูก

**คำถาม:** PC มีราคาใน service fee ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 153. [PASS] ถูก

**คำถาม:** ทำไมคำนวณ PC ไม่ได้

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 154. [PASS] ถูก

**คำถาม:** จอง PC 9 ถึง 11 ต้องเสียกี่บาท

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 09:00-11:00 = 2 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 2 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 155. [FAIL] ผิด

**คำถาม:** ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง

**คำตอบ(จาก AI):**

คำตอบ: ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['PC', 'Service Fee']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.180` sec


---

## 156. [PASS] ถูก

**คำถาม:** PC price for general student?

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้ที่ถาม: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, ไม่พบ, Service Fee
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 157. [FAIL] ผิด

**คำถาม:** ราคาค่าบริการทั้งหมดมีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.059` sec


---

## 158. [FAIL] ผิด

**คำถาม:** สรุป service fee ให้หน่อย

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.042` sec


---

## 159. [FAIL] ผิด

**คำถาม:** ตารางราคา 2026 มีอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.049` sec


---

## 160. [FAIL] ผิด

**คำถาม:** ค่าเล่นแต่ละเครื่องเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท
- ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท
- ค่าบริการ Cockpit ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 65 บาท, บุคคลทั่วไป 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_60_rates)
- https://esports.computing.p
... [trimmed output]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.050` sec


---

## 161. [FAIL] ผิด

**คำถาม:** service fee table includes what

**คำตอบ(จาก AI):**

Answer:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC

Sources:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.043` sec


---

## 162. [FAIL] ผิด

**คำถาม:** ขอเรทราคา PS5 Switch Cockpit VR

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 50 บาท/session × 1 = 50 บาท
- บุคคลทั่วไป: 150 บาท/session × 1 = 150 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Nintendo Switch, Cockpit, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Nintendo Switch', 'Cockpit', 'VR']`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 163. [PASS] ถูก

**คำถาม:** จองต้องล่วงหน้ากี่ชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.043` sec


---

## 164. [PASS] ถูก

**คำถาม:** ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 165. [PASS] ถูก

**คำถาม:** ต้อง book ล่วงหน้ากี่ hr

**คำตอบ(จาก AI):**

คำตอบ: 1 ชั่วโมง

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.797` sec


---

## 166. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 167. [PASS] ถูก

**คำถาม:** walk in ได้ไหมหรือต้องจองก่อน

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ชั่วโมง
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 168. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 169. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.036` sec


---

## 170. [PASS] ถูก

**คำถาม:** one booking max sessions?

**คำตอบ(จาก AI):**

คำตอบ: One booking can include a maximum of 3 sessions. This information is consistent across multiple sources provided, including SOURCE 1 and SOURCE 2.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 Sessions
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.867` sec


---

## 171. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.166` sec


---

## 172. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 173. [FAIL] ผิด

**คำถาม:** หลังจองต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
- ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท
- ค่าบริการ Cockpit ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 65 บาท, บุคคลทั่วไป 200 บาท
- บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_30_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_60_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_cockpit_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_pc_unknown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที', 'ยกเลิก']`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.037` sec


---

## 174. [PASS] ถูก

**คำถาม:** ไม่จ่ายใน 10 นาทีจะเกิดอะไร

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 175. [FAIL] ผิด

**คำถาม:** payment timeout กี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที', 'ยกเลิก']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.032` sec


---

## 176. [FAIL] ผิด

**คำถาม:** จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.035` sec


---

## 177. [PASS] ถูก

**คำถาม:** ชำระเงินหลัง booking ต้องเร็วแค่ไหน

**คำตอบ(จาก AI):**

คำตอบ:
- ผู้ใช้งานต้องชำระค่าบริการหลังจากจองเสร็จเรียบร้อยทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, ยกเลิก
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.037` sec


---

## 178. [PASS] ถูก

**คำถาม:** กดจองแล้วแก้ไขได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.039` sec


---

## 179. [PASS] ถูก

**คำถาม:** ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.036` sec


---

## 180. [FAIL] ผิด

**คำถาม:** แก้เวลา booking ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_time_change_policy)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ยกเลิก', 'สลิป']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.037` sec


---

## 181. [PASS] ถูก

**คำถาม:** ต้องยกเลิกแล้วจองใหม่ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.034` sec


---

## 182. [PASS] ถูก

**คำถาม:** แนบสลิปเดิมตอนจองใหม่ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_no_edit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเลิก, 1 ชั่วโมง, สลิป
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 183. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.039` sec


---

## 184. [PASS] ถูก

**คำถาม:** ให้คนอื่นมาใช้ booking แทนได้ไหม

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.037` sec


---

## 185. [FAIL] ผิด

**คำถาม:** transfer booking ได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่สามารถโอนสิทธิ์']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.126` sec


---

## 186. [FAIL] ผิด

**คำถาม:** จองแทนกันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_time_change_policy)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่สามารถโอนสิทธิ์']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.053` sec


---

## 187. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 188. [PASS] ถูก

**คำถาม:** check in ได้เร็วสุดกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: 30 นาที

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.908` sec


---

## 189. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.050` sec


---

## 190. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.035` sec


---

## 191. [FAIL] ผิด

**คำถาม:** ถ้า check-in ไม่ทันจะโดนอะไร

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.062` sec


---

## 192. [FAIL] ผิด

**คำถาม:** เช็คอินต้องใช้บัตรอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_id_required)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.046` sec


---

## 193. [FAIL] ผิด

**คำถาม:** แสดงบัตรประชาชนได้ไหมตอนเช็คอิน

**คำตอบ(จาก AI):**

คำตอบ:
- เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_checkin_id_required)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.034` sec


---

## 194. [PASS] ถูก

**คำถาม:** ชำระเงินผ่านอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ชำระเงินโดยโอนเข้าบัญชี Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคาร, โอน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.031` sec


---

## 195. [PASS] ถูก

**คำถาม:** โอนเงินไปบัญชีไหน

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคาร, โอน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 196. [PASS] ถูก

**คำถาม:** ชื่อบัญชีจ่ายค่าจองคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_booking_steps)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคาร, โอน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 197. [PASS] ถูก

**คำถาม:** เลขบัญชีธนาคารสำหรับจองคืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
ชำระเงินผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคาร, โอน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 198. [FAIL] ผิด

**คำถาม:** ธนาคารที่ใช้รับเงินคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: ธนาคารที่ใช้รับเงินคือ Siam Commercial Bank (ธนาคารไทยพาณิชย์)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ธนาคาร, โอน
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['โอน']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.093` sec


---

## 199. [FAIL] ผิด

**คำถาม:** PS5 มี Spider-Man 2 ไหม

**คำตอบ(จาก AI):**

คำตอบ:
มีเกม Marvel's Spider-Man 2 ใน PlayStation 5

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['TEKKEN 8']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.048` sec


---

## 200. [FAIL] ผิด

**คำถาม:** เพลย์ห้ามี tekken 8 หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ:
- กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_return_equipment)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['PlayStation 5', 'TEKKEN 8']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.060` sec


---

## 201. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 202. [FAIL] ผิด

**คำถาม:** PS5 เล่น Fortnite ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: PS5 เล่น Fortnite ได้. ในรายการเกมที่ปรากฏใน PlayStation 5 (ดูจากแหล่งข้อมูลที่ 1) มี Fortnite อยู่ในรายชื่อ.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['TEKKEN 8']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.416` sec


---

## 203. [FAIL] ผิด

**คำถาม:** มี God of War Ragnarok ไหม

**คำตอบ(จาก AI):**

คำตอบ: มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, TEKKEN 8
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['PlayStation 5', 'TEKKEN 8']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.094` sec


---

## 204. [PASS] ถูก

**คำถาม:** Switch มี Mario Kart ไหม

**คำตอบ(จาก AI):**

คำตอบ: พบในรายการที่เกี่ยวข้องกับเกมบน Nintendo Switch ได้แก่ Mario Kart 8 Deluxe

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.175` sec


---

## 205. [FAIL] ผิด

**คำถาม:** นินเทนโดมี Overcooked 2 ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Nintendo Switch', 'Mario Kart']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.915` sec


---

## 206. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 207. [FAIL] ผิด

**คำถาม:** เล่น Super Smash Bros ที่ศูนย์ได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Nintendo Switch', 'Mario Kart']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.891` sec


---

## 208. [FAIL] ผิด

**คำถาม:** Switch Sports มีไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nintendo Switch, Mario Kart
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Nintendo Switch', 'Mario Kart']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.105` sec


---

## 209. [FAIL] ผิด

**คำถาม:** PC มี valorant ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['PC', 'VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.751` sec


---

## 210. [FAIL] ผิด

**คำถาม:** คอมเล่น CS2 ได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['PC', 'VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.969` sec


---

## 211. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 212. [FAIL] ผิด

**คำถาม:** มี PUBG บน PC ไหม

**คำตอบ(จาก AI):**

คำตอบ: มี PUBG: BATTLEGROUNDS ในรายการเกมที่ปรากฏในรายการ PC

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.976` sec


---

## 213. [FAIL] ผิด

**คำถาม:** Warzone อยู่เครื่อง PC ไหน

**คำตอบ(จาก AI):**

คำตอบ:
- ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.052` sec


---

## 214. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 215. [FAIL] ผิด

**คำถาม:** Beat Saber มีไหม

**คำตอบ(จาก AI):**

คำตอบ: Beat Saber เป็นเกมแนว Rhythm ในระบบ Virtual Reality ที่ผู้เล่นต้องใช้ดาบสีแดงและน้ำเงินฟัน Block ตามจังหวะเพลง และหลบหลีกกำแพงและระเบิดที่พุ่งเข้ามาหาตัว.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VR']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.751` sec


---

## 216. [FAIL] ผิด

**คำถาม:** แว่น VR มี Horizon ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Beat Saber']`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.044` sec


---

## 217. [FAIL] ผิด

**คำถาม:** Cockpit เล่นเกมอะไร

**คำตอบ(จาก AI):**

คำตอบ:
Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_cockpit_games / Reservation, curated_games_cockpit, reservation-service-cockpit)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VR', 'Beat Saber']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 218. [FAIL] ผิด

**คำถาม:** พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: ใช่ พวงมาลัยใช้เล่นเกม Gran Turismo 7 (Single Player) โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VR, Beat Saber
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VR', 'Beat Saber']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.564` sec


---

## 219. [PASS] ถูก

**คำถาม:** PC Zone มีอุปกรณ์อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
- ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 220. [PASS] ถูก

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
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.045` sec


---

## 221. [PASS] ถูก

**คำถาม:** Gaming PC รุ่นอะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 222. [FAIL] ผิด

**คำถาม:** เก้าอี้เกมมิ่งมีไหมใน PC zone

**คำตอบ(จาก AI):**

คำตอบ:
เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_pc_games / Reservation, curated_games_pc, reservation-service-pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Gaming PC', '10 Units']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 223. [FAIL] ผิด

**คำถาม:** เมาส์กับหูฟังมีให้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ใน Home PC Zone มีให้ใช้ Mouse และ Headset แต่ไม่มีการระบุว่ามีเมาส์หรือไม่

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Gaming PC, 10 Units
Expected source keywords: home
หมวด: equipment
ชนิดคำตอบ: list

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['Gaming PC', '10 Units']`
- source_ok: `True` | matched: `['home']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.560` sec


---

## 224. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.057` sec


---

## 225. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.039` sec


---

## 226. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 227. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.039` sec


---

## 228. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.031` sec


---

## 229. [FAIL] ผิด

**คำถาม:** เอาขนมเข้าไปกินตรงโต๊ะได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.971` sec


---

## 230. [FAIL] ผิด

**คำถาม:** กินน้ำในพื้นที่เล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_food_drink / curated_rule_food_drinks)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 231. [FAIL] ผิด

**คำถาม:** ต้องฝากกระเป๋าก่อนไหม

**คำตอบ(จาก AI):**

คำตอบ: ตามข้อมูลที่ได้จากแหล่งข้อมูล ไม่มีคำอธิบายเกี่ยวกับเรื่องของการฝากสัมภาระ กรุณาตรวจสอบแหล่งอื่นเพื่อความแน่ใจ.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.484` sec


---

## 232. [PASS] ถูก

**คำถาม:** ใช้เสียงดังได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น ตามนโยบายใน [SOURCE 1]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.477` sec


---

## 233. [FAIL] ผิด

**คำถาม:** พูดจาเสียดสีคนอื่นได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.908` sec


---

## 234. [PASS] ถูก

**คำถาม:** ทิ้งขยะไว้ในโซนเล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_trash_personal_items)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.043` sec


---

## 235. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 236. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 237. [FAIL] ผิด

**คำถาม:** พกมีดเข้าไปได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.189` sec


---

## 238. [FAIL] ผิด

**คำถาม:** เล่นพนันในห้องได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.944` sec


---

## 239. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.063` sec


---

## 240. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.056` sec


---

## 241. [FAIL] ผิด

**คำถาม:** ทำอุปกรณ์เสียหายต้องจ่ายไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
- ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท
- ค่าบริการ Cockpit ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 65 บาท, บุคคลทั่วไป 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_30_rates)
- https://esports.computing.p
... [trimmed output]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.046` sec


---

## 242. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 243. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 244. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 245. [FAIL] ผิด

**คำถาม:** จอแตกต้องชดเชยยังไง

**คำตอบ(จาก AI):**

คำตอบ:
ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_severe_damage / curated_damage_severe)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['บาท']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 246. [PASS] ถูก

**คำถาม:** คอมพังต้องจ่ายเต็มไหม

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PC คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- ยังไม่ทราบกลุ่มผู้ใช้ จึงยังเทียบเรตราคาเฉพาะกลุ่มไม่ได้
- ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา
- จากภาพ Service Fee 2026 ที่มีตอนนี้ มีราคา PlayStation 5, Nintendo Switch, Cockpit และ VR แต่ไม่ปรากฏราคา PC
- ถ้าได้รับราคา PC ต่อ 1 session แล้ว ระบบจะคำนวณได้ทันทีด้วยสูตร: จำนวน session × ราคาต่อ session

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset (service duration)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (service fee image; PC price not shown)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 247. [PASS] ถูก

**คำถาม:** ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน

**คำตอบ(จาก AI):**

คำตอบ:
- หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_penalty_temp_suspension)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.043` sec


---

## 248. [FAIL] ผิด

**คำถาม:** โดนแบนชั่วคราวกี่วัน

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ระงับสิทธิ์']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.953` sec


---

## 249. [PASS] ถูก

**คำถาม:** กรณีไหนแบนถาวร

**คำตอบ(จาก AI):**

คำตอบ: การระงับสิทธิ์ถาวร (Reservation Penalty) จะเกิดขึ้นเมื่อผู้ใช้งานกระทำการละเมิดกฎอย่างร้ายแรง เช่น การทำลายทรัพย์สินหรือพฤติกรรมที่เป็นภัยต่อความปลอดภัยของผู้อื่น ซึ่งสามารถดูได้จากแหล่งข้อมูล [SOURCE 1]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.201` sec


---

## 250. [PASS] ถูก

**คำถาม:** อุทธรณ์การลงโทษได้ภายในกี่วัน

**คำตอบ(จาก AI):**

คำตอบ:
- หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_penalty_temp_suspension)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.054` sec


---

## 251. [FAIL] ผิด

**คำถาม:** ศูนย์เก็บประวัติคนทำผิดไหม

**คำตอบ(จาก AI):**

คำตอบ: พบในฐานข้อมูลที่มี ระบุไว้ว่าการละเมิดกฎจะถูกบันทึกในประวัติการใช้บริการของผู้ใช้งาน (Reservation Penalty - บันทึกประวัติการละเมิด)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ระงับสิทธิ์
Expected source keywords: Reservation
หมวด: penalty
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ระงับสิทธิ์']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.703` sec


---

## 252. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 253. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 254. [FAIL] ผิด

**คำถาม:** ใครเป็นคนก่อตั้งศูนย์นี้

**คำตอบ(จาก AI):**

คำตอบ:
- หน้าสมาชิกระบุว่า นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_manager)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['มหาวิทยาลัยสงขลานครินทร์', 'วิทยาลัยการคอมพิวเตอร์']`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.038` sec


---

## 255. [PASS] ถูก

**คำถาม:** หน่วยงานที่ดำเนินการคือใคร

**คำตอบ(จาก AI):**

คำตอบ:
- Mission ของ PSU Esports Studio - Phuket คือการยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต ผ่านสิ่งอำนวยความสะดวกและอุปกรณ์ที่ช่วยเสริมสร้างการเรียนรู้ให้กับนักเล่นเกม นักศึกษา และผู้สนใจ โดยก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์
- PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_overview_mission)
- https://esports.phuket.psu.ac.th/home (curated_overview_identity)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์
Expected source keywords: home
หมวด: overview
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['home']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.035` sec


---

## 256. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 257. [PASS] ถูก

**คำถาม:** ศูนย์อยู่ตรงไหน

**คำตอบ(จาก AI):**

คำตอบ: PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU
Expected source keywords: Contact
หมวด: contact
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Contact']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.052` sec


---

## 258. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 259. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 260. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 261. [PASS] ถูก

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 262. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.059` sec


---

## 263. [FAIL] ผิด

**คำถาม:** esports เริ่มครั้งแรกที่ไหน

**คำตอบ(จาก AI):**

คำตอบ:
Esports เริ่มครั้งแรกที่มหาวิทยาลัยสแตนฟอร์ด (Stanford University) ในวันที่ 19 ตุลาคม ค.ศ. 1972 ในการแข่งขันเกม Spacewar ภายใต้ชื่องาน Intergalactic Spacewar Olympics

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['อีสปอร์ต']`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.855` sec


---

## 264. [PASS] ถูก

**คำถาม:** Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- อีสปอร์ตเกิดขึ้นครั้งแรกในวันที่ 19 ตุลาคม ค.ศ. 1972 ณ มหาวิทยาลัยสแตนฟอร์ด (Standford University) จากการแข่งขันเกม Spacewar ภายใต้ชื่องาน Intergalactic Spacewar Olympics

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_origin)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.042` sec


---

## 265. [PASS] ถูก

**คำถาม:** เกมประเภท MOBA คืออะไร

**คำตอบ(จาก AI):**

คำตอบ:
- ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_categories)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.052` sec


---

## 266. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.037` sec


---

## 267. [FAIL] ผิด

**คำถาม:** Overcooked 2 ฝึกทักษะอะไร

**คำตอบ(จาก AI):**

คำตอบ: Overcooked! 2 ฝึกทักษะการทำงานเป็นทีม, การจัดการสถานการณ์กดดัน, การสื่อสารอย่างชัดเจน และการวางแผน

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['อีสปอร์ต']`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.472` sec


---

## 268. [FAIL] ผิด

**คำถาม:** Mario Kart 8 Deluxe ฝึกอะไร

**คำตอบ(จาก AI):**

Mario Kart 8 Deluxe ฝึกไหวพริบและการตัดสินใจผ่านการควบคุมตัวละครบนสนามที่เต็มไปด้วยทางโค้ง, สิ่งกีดขวาง และไอเทมหลากหลายรูปแบบ. การตัดสินใจว่าจะเร่ง เบรก ดริฟต์ หรือใช้ไอเทมเมื่อไร ล้วนต้องอาศัยไหวพริบและการคิดอย่างรวดเร็ว.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อีสปอร์ต
Expected source keywords: Knowledge
หมวด: knowledge
ชนิดคำตอบ: summary

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['อีสปอร์ต']`
- source_ok: `True` | matched: `['Knowledge']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.580` sec


---

## 269. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.050` sec


---

## 270. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.039` sec


---

## 271. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 272. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.036` sec


---

## 273. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 274. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.032` sec


---

## 275. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.032` sec


---

## 276. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.033` sec


---

## 277. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 278. [PASS] ถูก

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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.029` sec


---

## 279. [PASS] ถูก

**คำถาม:** มีบริการซ่อมคอมส่วนตัวไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่พบข้อมูลเรื่องบริการซ่อมคอมพิวเตอร์ส่วนตัวในฐานข้อมูลที่มี

แหล่งข้อมูล:
- missing source URL (rule_no_answer_repair_personal_pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 280. [PASS] ถูก

**คำถาม:** เปิด 24 ชม ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่พบข้อมูลว่าเปิดให้บริการ 24 ชั่วโมงในฐานข้อมูลที่มี

แหล่งข้อมูล:
- missing source URL (rule_no_answer_24_hours)

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

## 281. [PASS] ถูก

**คำถาม:** ส่งอาหารถึงโต๊ะเกมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่พบข้อมูลเรื่องบริการจัดส่งอาหารถึงโต๊ะเล่นเกมในฐานข้อมูลที่มี

แหล่งข้อมูล:
- missing source URL (rule_no_answer_food_delivery)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 282. [PASS] ถูก

**คำถาม:** เอาแมวเข้าได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.048` sec


---

## 283. [PASS] ถูก

**คำถาม:** สมัครสมาชิกรายปีราคาเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
ไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี

แหล่งข้อมูล:
- missing source URL (rule_no_answer_annual_membership)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 284. [PASS] ถูก

**คำถาม:** เช่าโน้ตบุ๊กกลับบ้านได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
ไม่พบข้อมูลเรื่องบริการเช่าโน้ตบุ๊กกลับบ้านในฐานข้อมูลที่มี

แหล่งข้อมูล:
- missing source URL (rule_no_answer_laptop_rental_home)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 285. [PASS] ถูก

**คำถาม:** มีห้องนอนพักค้างคืนไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.961` sec


---

## 286. [PASS] ถูก

**คำถาม:** ขายคีย์บอร์ดเกมมิ่งไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.865` sec


---

## 287. [PASS] ถูก

**คำถาม:** รับซ่อมจอย PS5 ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.068` sec


---

## 288. [FAIL] ผิด

**คำถาม:** มีบริการส่งเครื่องเกมไปบ้านไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber
- เกมที่ปรากฏในรายการ PlayStation 5 ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection
- เกมที่ปรากฏในรายการ PC ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.phuket.psu.ac.th/home (curated_home_popular_games_list)
- https://esports.phuket.psu.ac.th/home (curated_games_popular)
- https://esports.computing.psu.ac.th/ (curated_games_ps5)
- https://esports.computing.psu.ac.th/ (curated_games_pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่พบข้อมูล']`
- source_ok: `True`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.045` sec


---

## 289. [FAIL] ผิด

**คำถาม:** ซื้อเกม Steam ผ่านศูนย์ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- เกมที่ปรากฏในรายการ PC ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_games_pc)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่พบข้อมูล']`
- source_ok: `True`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.035` sec


---

## 290. [PASS] ถูก

**คำถาม:** มีคอร์สสอนเล่น Valorant ส่วนตัวไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.895` sec


---

## 291. [PASS] ถูก

**คำถาม:** จ่ายด้วยคริปโตได้ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.949` sec


---

## 292. [FAIL] ผิด

**คำถาม:** ผ่อนชำระค่าเล่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
- บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท
- ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_2026_full_table)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_pc_unkn
... [trimmed output]

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่พบข้อมูล']`
- source_ok: `True`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.047` sec


---

## 293. [PASS] ถูก

**คำถาม:** มีส่วนลดวันเกิดไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.971` sec


---

## 294. [FAIL] ผิด

**คำถาม:** จองแบบเหมาทั้งวันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ:
- สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_time_change_policy)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่พบข้อมูล']`
- source_ok: `True`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.043` sec


---

## 295. [PASS] ถูก

**คำถาม:** เอาเครื่อง PC ตัวเองมาตั้งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.185` sec


---

## 296. [PASS] ถูก

**คำถาม:** มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.908` sec


---

## 297. [PASS] ถูก

**คำถาม:** มีอาหารบุฟเฟต์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.899` sec


---

## 298. [PASS] ถูก

**คำถาม:** รับจัดงานแต่งในศูนย์ไหม

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.069` sec


---

## 299. [PASS] ถูก

**คำถาม:** ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: จอง, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 300. [FAIL] ผิด

**คำถาม:** ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_booking_advance / curated_reservation_advance_time)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: จอง, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 301. [FAIL] ผิด

**คำถาม:** จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที

**คำตอบ(จาก AI):**

คำตอบ:
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท
- ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท
- บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
- ค่าบริการ Cockpit ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 65 บาท, บุคคลทั่วไป 200 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_60_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_30_rates)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_pc_unknown)
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_cockpit_rates)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: จอง, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที']`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.044` sec


---

## 302. [FAIL] ผิด

**คำถาม:** กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_user_info_required)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: จอง, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.034` sec


---

## 303. [FAIL] ผิด

**คำถาม:** ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง

**คำตอบ(จาก AI):**

คำตอบ:
- สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_time_change_policy)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: จอง, 10 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['10 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.034` sec


---

## 304. [FAIL] ผิด

**คำถาม:** นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ:
- ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (curated_service_fee_vr_60_rates)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.061` sec


---

## 305. [PASS] ถูก

**คำถาม:** คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: บุคคลทั่วไป
- ราคา 280 บาท/session × 1 session(s) = 280 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 306. [PASS] ถูก

**คำถาม:** General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม

**คำตอบ(จาก AI):**

คำตอบ:
- ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student)
- ราคา 50 บาท/session × 1 session(s) = 50 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 307. [PASS] ถูก

**คำถาม:** ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 308. [PASS] ถูก

**คำถาม:** ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: บาท
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: calculation

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 309. [FAIL] ผิด

**คำถาม:** ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง

**คำตอบ(จาก AI):**

คำตอบ:
- กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_rule_noise_language)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.047` sec


---

## 310. [FAIL] ผิด

**คำถาม:** ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม

**คำตอบ(จาก AI):**

คำตอบ:
กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_lost_personal_items / Reservation, curated_rule_lost_items, reservation-studio-rules)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 311. [FAIL] ผิด

**คำถาม:** ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม

**คำตอบ(จาก AI):**

คำตอบ:
ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 312. [FAIL] ผิด

**คำถาม:** ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ:
กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (rule_return_equipment_games / Reservation, curated_rule_return_equipment, reservation-studio-rules)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.002` sec


---

## 313. [FAIL] ผิด

**คำถาม:** ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร

**คำตอบ(จาก AI):**

คำตอบ: ควรแจ้งเจ้าหน้าที่ทันที หากพบปัญหาการใช้งาน

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม
Expected source keywords: Reservation
หมวด: rules
ชนิดคำตอบ: multi_fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ห้าม']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.943` sec


---

## 314. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ตอบสั้นๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.014` sec


---

## 315. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 316. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 317. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

ไม่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.906` sec


---

## 318. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที ตอบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.041` sec


---

## 319. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 320. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ตอบสั้นๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.870` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 322. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.969` sec


---

## 323. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 324. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 325. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.841` sec


---

## 326. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.044` sec


---

## 327. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 328. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ในเว็บบอกว่าไง

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.895` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 330. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.030` sec


---

## 331. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 332. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 333. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ: มี Valora ในรายการเกมบน PC ที่ปรากฏในเว็บไซต์ esports.computing.psu.ac.th

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.116` sec


---

## 334. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที ถามแทนเพื่อน

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.040` sec


---

## 335. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 336. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถามแทนเพื่อน

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.806` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 338. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ: เปิด-ปิด วันจันกลงมือแบบภาษาบุคคลทั่วไปคือ "เปิด-ปิด วันจันกิ้มงอม"

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.368` sec


---

## 339. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 340. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 341. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.040` sec


---

## 342. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.050` sec


---

## 343. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 344. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม แบบภาษาคนทั่วไป

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.960` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 346. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ: การจองและการยกเลิกต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง (SOURCE 1, SOURCE 4). หากต้องการเปลี่ยนแปลงข้อมูลหลังจากจอง, ต้องยกเลิกการจองผ่านอีเมลและจองใหม่อีกครั้งพร้อมแนบสลิปการโอนเงินเดิม (SOURCE 2). การเปลี่ยนแปลงเวลาใช้งานต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง (SOURCE 3).

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.774` sec


---

## 347. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 348. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 349. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['VALORANT']`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.921` sec


---

## 350. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.054` sec


---

## 351. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


---

## 352. [PASS] ถูก

**คำถาม:** มีให้เช่าจอไปบ้านไหม ขอสรุปเร็วๆ

**คำตอบ(จาก AI):**

ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.995` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 354. [FAIL] ผิด

**คำถาม:** เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ: ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13:00, 16:00, Maintenance
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['13:00', '16:00', 'Maintenance']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `2.887` sec


---

## 355. [PASS] ถูก

**คำถาม:** เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง
- บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s)
- กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU
- ราคา 0 บาท/session × 1 session(s) = 0 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 0, PlayStation 5
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 356. [PASS] ถูก

**คำถาม:** ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที
- บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s)
- นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท
- ศิษย์เก่า PSU / นักศึกษาทั่วไป (General Student): 190 บาท/session × 1 = 190 บาท
- บุคคลทั่วไป: 525 บาท/session × 1 = 525 บาท

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 190, VR
Expected source keywords: Reservation
หมวด: service_fee
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ถูก**
- keyword_ok: `True`
- source_ok: `True` | matched: `['Reservation']`
- route: `deterministic_calculator` | model: `calculator` | elapsed: `0.000` sec


---

## 357. [FAIL] ผิด

**คำถาม:** คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
ในรายการเกมที่นิยมในปัจจุบันบน PC Zone มี VALORANT อยู่ครับ. กรุณาตรวจสอบอุปกรณ์และแผ่นเกมก่อนนำมาใช้งานเพื่อความปลอดภัยและความถูกต้อง.

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT
Expected source keywords: Reservation
หมวด: games
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `3.696` sec


---

## 358. [FAIL] ผิด

**คำถาม:** เชคอินก่อนกี่นาที ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ:
- บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ

แหล่งข้อมูล:
- https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที
Expected source keywords: Reservation
หมวด: reservation
ชนิดคำตอบ: fact

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['30 นาที']`
- source_ok: `True` | matched: `['Reservation']`
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.042` sec


---

## 359. [FAIL] ผิด

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
- สถานะ: **ผิด**
- keyword_ok: `True`
- source_ok: `False`
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


---

## 360. [FAIL] ผิด

**คำถาม:** มีให้เช่าจอไปบ้านไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง

**คำตอบ(จาก AI):**

คำตอบ: ไม่มีการให้เช่าจอไปบ้านในบริการนี้ ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาที่จะใช้งานอย่างน้อย 1 ชั่วโมง (ข้อ 2.1) และไม่มีนโยบายเปลี่ยนแปลงเวลาใช้งานหรือยกเลิกการเช่าได้โดยไม่ต้องแจ้งล่วงหน้า (ข้อ 3.4)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่พบข้อมูล
หมวด: no_answer
ชนิดคำตอบ: no_answer

**ผลตรวจ:**
- สถานะ: **ผิด**
- keyword_ok: `False` | missing: `['ไม่พบข้อมูล']`
- source_ok: `True`
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.307` sec
