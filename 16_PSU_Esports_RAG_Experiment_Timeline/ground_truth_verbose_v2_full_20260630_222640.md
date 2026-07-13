# Ground Truth Verbose Report

- ไฟล์: `c:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
- ข้อที่รัน: 1 - 20
- รวม: 20
- ถูก: 20
- ผิด/error: 0
- Accuracy: 100.00%
- Average latency: 0.205 sec
- Generated: 2026-06-30 22:26:40

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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rag_llm` | model: `qwen2.5:3b` | elapsed: `4.037` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.001` sec


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
- route: `rule_fast_path` | model: `rule_based` | elapsed: `0.000` sec


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
- route: `rag_direct_curated` | model: `direct_from_retrieved_curated_fact` | elapsed: `0.048` sec
