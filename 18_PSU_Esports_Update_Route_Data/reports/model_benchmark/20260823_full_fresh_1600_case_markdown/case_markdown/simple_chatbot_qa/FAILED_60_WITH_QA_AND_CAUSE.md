# Failure Diagnosis - 60 ข้อ

รายงานนี้อ่านโจทย์ คำตอบจริง route/mode เวลา และ judge error ของทุก failure จาก Typhoon run ใหม่

## สรุป

- Failure ทั้งหมด: `60`
- Chatbot ผิดจริง: `40`
- Judge ตรวจพลาด: `19`
- ต้องตัดสิน Product Policy: `1`

| Root-cause bucket | จำนวน |
|---|---:|
| `general_concept_misrouted_equipment` | 26 |
| `judge_false_negative_thanks_synonym` | 11 |
| `substring_collision_price_in_kho_sia` | 9 |
| `judge_false_negative_latency_synonym` | 7 |
| `system_exception` | 2 |
| `substring_collision_animal_crossing` | 1 |
| `wrong_route_game_ranking` | 1 |
| `unsupported_freshness_hallucination` | 1 |
| `product_scope_policy_mismatch` | 1 |
| `judge_false_negative_activity_synonym` | 1 |

## 1. MB-0189-G-101 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_animal_crossing`
- เวลา: `1.2776` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing:Animal Crossing`
- Root cause: Raw substring `cross` ในชื่อ Animal Crossing ถูกตีความเป็นคำสั่งปุ่ม/controls และ ambiguity margin ทับ exact game entity
- ทำไมจึงผิด/ถูกมองว่าผิด: ชื่อเกม resolve แบบ exact แล้ว แต่ระบบยังถามกลับแทนการตอบข้อมูลเกม
- วิธีแก้: ใช้ token-boundary matcher และให้ exact entity + explicit detail question veto ambiguity ระหว่าง list/detail

**โจทย์**

````text
Animal Crossing: New Horizons คือเกมอะไร
````

**คำตอบจาก Chatbot**

````text
คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0189-G-101.md)

## 2. MB-0240-G-152 - Chatbot ผิดจริง

- Root-cause bucket: `wrong_route_game_ranking`
- เวลา: `20.4899` วินาที
- Mode: `pipeline:no_answer`
- Judge error: `category_mismatch:equipment, missing_any:เกม|Zone|TEKKEN|Mario|Gran Turismo`
- Root cause: คำถามจัดอันดับจำนวนเกมถูกเปลี่ยนเป็น equipment/list แล้วเข้า hybrid retrieval ผิดหมวด
- ทำไมจึงผิด/ถูกมองว่าผิด: ถามว่าโซนหรืออุปกรณ์ใดมีเกมมากสุด แต่ตอบว่าไม่พบข้อมูลหมวด equipment
- วิธีแก้: ให้ game-zone ranking route มี deterministic veto, ใช้ structured game catalog และหยุด retrieval เมื่อ source domain ไม่ตรง

**โจทย์**

````text
อุปกรณ์ไหนเกมเยอะสุด
````

**คำตอบจาก Chatbot**

````text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0240-G-152.md)

## 3. MB-0607-CR-071 - Chatbot ผิดจริง

- Root-cause bucket: `system_exception`
- เวลา: `0.4354` วินาที
- Mode: `exception`
- Judge error: `exception:UnboundLocalError`
- Root cause: Request state ไม่ถูก initialize ทุกเส้นทาง จึงเกิด UnboundLocalError ก่อนสร้างคำตอบ
- ทำไมจึงผิด/ถูกมองว่าผิด: ผู้ใช้ไม่ได้รับคำตอบเลยและ answer เป็นค่าว่าง
- วิธีแก้: กำหนดค่า request/RAG state ตั้งแต่ต้น request และเพิ่ม regression test สำหรับ route นี้

**โจทย์**

````text
ROV ถ้าใช้ bug จะโดนอะไร
````

**คำตอบจาก Chatbot**

````text
[ไม่มีคำตอบ: Chatbot ส่ง answer เป็นค่าว่าง]
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0607-CR-071.md)

## 4. MB-0636-ANA-010 - Chatbot ผิดจริง

- Root-cause bucket: `system_exception`
- เวลา: `1.3052` วินาที
- Mode: `exception`
- Judge error: `exception:UnboundLocalError`
- Root cause: Request state ไม่ถูก initialize ทุกเส้นทาง จึงเกิด UnboundLocalError ก่อนสร้างคำตอบ
- ทำไมจึงผิด/ถูกมองว่าผิด: ผู้ใช้ไม่ได้รับคำตอบเลยและ answer เป็นค่าว่าง
- วิธีแก้: กำหนดค่า request/RAG state ตั้งแต่ต้น request และเพิ่ม regression test สำหรับ route นี้

**โจทย์**

````text
จอง
````

**คำตอบจาก Chatbot**

````text
[ไม่มีคำตอบ: Chatbot ส่ง answer เป็นค่าว่าง]
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0636-ANA-010.md)

## 5. MB-0649-ANA-023 - Chatbot ผิดจริง

- Root-cause bucket: `unsupported_freshness_hallucination`
- เวลา: `13.901` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`
- Root cause: คำถาม `ตอนนี้` ถูกส่งเข้า General LLM โดยไม่มี live Web/API evidence หรือ freshness guard
- ทำไมจึงผิด/ถูกมองว่าผิด: โมเดลยกชื่อเพลงเก่ามาอ้างว่าเป็นเพลงฮิตปัจจุบัน จึงเป็น unsupported freshness claim
- วิธีแก้: บังคับ freshness query ใช้ live provider ที่มี timestamp หรือ no-answer/ชี้แหล่งตรวจสอบเมื่อไม่มี provider

**โจทย์**

````text
เพลงฮิตตอนนี้คืออะไร
````

**คำตอบจาก Chatbot**

````text
เพลงฮิตตอนนี้อาจแตกต่างกันไปตามประเทศและแพลตฟอร์ม เช่น TikTok, YouTube โดยเพลงที่กำลังมาแรงในขณะนี้ได้แก่ "Flowers" โดย Miley Cyrus และ "Unholy" โดย Sam Smith และ Kim Petras เป็นต้น แต่ข้อมูลอาจเปลี่ยนแปลงอยู่ตลอดเวลา กรุณาตรวจสอบจากแหล่งข้อมูลอัปเดตเพื่อรับความแม่นยำสูงสุดครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0649-ANA-023.md)

## 6. MB-0650-ANA-024 - ต้องตัดสิน Product Policy

- Root-cause bucket: `product_scope_policy_mismatch`
- เวลา: `15.4026` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`
- Root cause: เป้าหมาย broad assistant ของ product ยังขัดกับ expected contract เดิมที่ให้ decline คำถามนอก PSU
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามยังไม่มีโจทย์คณิตให้คำนวณ คำตอบที่เหมาะกว่าอาจเป็นการขอให้ส่งโจทย์ ไม่ใช่ปฏิเสธแบบกว้าง
- วิธีแก้: กำหนด scope ให้ชัด แล้วแก้ policy/contract ให้ถามขอรายละเอียดหรือช่วยอธิบายวิธีทำโดยไม่เดาคำตอบ

**โจทย์**

````text
ช่วยทำการบ้านคณิตให้หน่อย
````

**คำตอบจาก Chatbot**

````text
ขออภัยครับ แต่ผมไม่สามารถช่วยทำการบ้านคณิตได้โดยตรง เพราะเป็นการให้คำตอบที่ต้องใช้ข้อมูลเฉพาะตัวหรือการคำนวณซึ่งไม่สามารถทำได้ในบริบทนี้ครับ หากมีคำถามอื่น ๆ ที่ต้องการความช่วยเหลือ ผมยินดีช่วยเสมอครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-0650-ANA-024.md)

## 7. MB-1333-GL-008 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.747` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1333-GL-008.md)

## 8. MB-1336-GL-011 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `2.2989` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าในการตอบสนองระหว่างอุปกรณ์ต่าง ๆ ในระบบคอมพิวเตอร์ เช่น เวลาที่ข้อมูลจากผู้ใช้ถูกส่งไปยังเซิร์ฟเวอร์แล้วได้รับผลตอบแทนกลับมาอีกครั้ง
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1336-GL-011.md)

## 9. MB-1343-GL-018 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.7276` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1343-GL-018.md)

## 10. MB-1353-GL-028 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.8241` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบเข้าใจง่าย
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1353-GL-028.md)

## 11. MB-1360-GL-035 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.9174` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณอย่างสุดหัวใจสำหรับความช่วยเหลือและความใส่ใจเสมอมา
ยังคงรู้สึกซาบซึ้งและประทับใจอย่างยิ่งครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1360-GL-035.md)

## 12. MB-1363-GL-038 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.8561` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบเป็นภาษาไทย
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1363-GL-038.md)

## 13. MB-1366-GL-041 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `2.2492` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ไม่ต้องยาว
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าในการตอบสนองของระบบคอมพิวเตอร์ระหว่างการส่งข้อมูลจากผู้ใช้ไปยังอุปกรณ์ปลายทางหรือกลับคืนมา โดยมักวัดเป็นเวลา เช่น มิลลิวินาที (ms)
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1366-GL-041.md)

## 14. MB-1370-GL-045 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.7709` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ไม่ต้องยาว
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและโอกาสที่ได้รับ
ขอบใจที่ให้เกียรติและสนับสนุนเสมอครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1370-GL-045.md)

## 15. MB-1373-GL-048 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.7131` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ไม่ต้องยาว
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1373-GL-048.md)

## 16. MB-1380-GL-055 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.7866` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอ 1 ย่อหน้า
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณที่ให้โอกาสและสนับสนุนอย่างยิ่ง
ขอบใจเป็นอย่างยิ่งสำหรับความช่วยเหลือและความใส่ใจเสมอมาครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1380-GL-055.md)

## 17. MB-1383-GL-058 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.7329` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอ 1 ย่อหน้า
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1383-GL-058.md)

## 18. MB-1390-GL-065 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `2.1058` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายให้มือใหม่เข้าใจ
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและคำแนะนำที่ให้มาครับ
ขอบใจที่ได้แบ่งปันความรู้และประสบการณ์ดี ๆ มาให้ผมได้เรียนรู้ครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1390-GL-065.md)

## 19. MB-1393-GL-068 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.2596` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายให้มือใหม่เข้าใจ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1393-GL-068.md)

## 20. MB-1403-GL-078 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.3092` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบเด็กปีหนึ่งเข้าใจได้
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1403-GL-078.md)

## 21. MB-1406-GL-081 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `1.9327` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอแบบไม่ใช้ศัพท์ยาก
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าในการตอบสนองของเครื่องคอมพิวเตอร์ เช่น เครื่องตอบสนองช้าเมื่อคลิกหรือป้อนข้อมูล เพราะต้องรอให้ระบบประมวลผลเสร็จก่อนครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1406-GL-081.md)

## 22. MB-1413-GL-088 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.026` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบไม่ใช้ศัพท์ยาก
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1413-GL-088.md)

## 23. MB-1423-GL-098 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.8877` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอสรุปเป็น 2 ข้อ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1423-GL-098.md)

## 24. MB-1433-GL-108 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.2004` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอคำตอบไม่เกิน 3 บรรทัด
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1433-GL-108.md)

## 25. MB-1443-GL-118 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.2325` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายแบบใช้ในงาน chatbot
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1443-GL-118.md)

## 26. MB-1450-GL-125 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `2.096` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายแบบใช้กับวงการเกม
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและคำแนะนำที่ให้มาครับ
นับเป็นเกียรติอย่างยิ่งที่ได้มีโอกาสทำงานร่วมกันในวงการเกมครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1450-GL-125.md)

## 27. MB-1452-GL-127 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_activity_synonym`
- เวลา: `3.0301` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:กิจกรรม`
- Root cause: Keyword judge ต้องเห็น `กิจกรรม` แต่คำตอบใช้ `งานแข่งขันเกม` ซึ่งสื่อความหมายเดียวกัน
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบเป็นประโยคประชาสัมพันธ์งานตามโจทย์ แม้ถ้อยคำยาวและโฆษณาเกินจำเป็น
- วิธีแก้: ใช้ semantic evaluator สำหรับ activity/event และตรวจความยาว/รูปแบบด้วย style contract แยกต่างหาก

**โจทย์**

````text
เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค อธิบายแบบใช้กับวงการเกม
````

**คำตอบจาก Chatbot**

````text
เรียนผู้สนใจเกมทุกท่าน ขอเชิญร่วมตื่นเต้นเข้าสู่เวทีแห่งความบันเทิงและทักษะระดับพรีเมียมในงานแข่งขันเกมครั้งยิ่งใหญ่ที่จะพาให้ทุกคนได้แสดงออกถึงจิตวิญญาณแห่งการเล่นเกมอย่างมีสไตล์และสร้างสรรค์!
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1452-GL-127.md)

## 28. MB-1453-GL-128 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.1743` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายแบบใช้กับวงการเกม
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1453-GL-128.md)

## 29. MB-1463-GL-138 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.0041` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ช่วยยกตัวอย่างสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1463-GL-138.md)

## 30. MB-1470-GL-145 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `2.0552` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค เปรียบเทียบแบบสั้น
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและคำแนะนำที่ให้มา
ทำให้รู้สึกประทับใจและได้เรียนรู้เพิ่มเติมอย่างมากครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1470-GL-145.md)

## 31. MB-1473-GL-148 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.0242` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น เปรียบเทียบแบบสั้น
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1473-GL-148.md)

## 32. MB-1480-GL-155 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.7435` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบสุภาพ
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณที่ให้โอกาสและสนับสนุนอย่างยิ่ง
ขอบใจเป็นอย่างยิ่งสำหรับความช่วยเหลือและความใส่ใจครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1480-GL-155.md)

## 33. MB-1483-GL-158 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.7547` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบสุภาพ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1483-GL-158.md)

## 34. MB-1490-GL-165 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.6708` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบให้เหมาะกับนักศึกษา
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและโอกาสในการเรียนรู้ครับ/ค่ะ
นับถือครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1490-GL-165.md)

## 35. MB-1493-GL-168 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.1323` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบให้เหมาะกับนักศึกษา
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1493-GL-168.md)

## 36. MB-1496-GL-171 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `3.6651` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ เขียนเป็นภาษาไทยธรรมชาติ
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าหรือเวลาที่ใช้ในการตอบสนองระหว่างการส่งคำสั่งจากเครื่องหนึ่งไปยังอีกเครื่องหนึ่งในระบบคอมพิวเตอร์ เช่น เครื่องใช้งานอินเทอร์เน็ตหรือเกมออนไลน์ โดยมักนับเป็นช่วงเวลาสั้น ๆ เช่น มิลลิวินาที (ms) ที่ใช้ในการส่งข้อมูลผ่านเครือข่ายแล้วได้รับคำตอบกลับมาอีกครั้ง
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1496-GL-171.md)

## 37. MB-1503-GL-178 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.1793` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น เขียนเป็นภาษาไทยธรรมชาติ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1503-GL-178.md)

## 38. MB-1506-GL-181 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `1.4349` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอแบบไม่เป็นทางการมาก
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าระหว่างการกระทำกับการตอบกลับในเครื่องคอมฯ เลยครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1506-GL-181.md)

## 39. MB-1513-GL-188 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.1458` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบไม่เป็นทางการมาก
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1513-GL-188.md)

## 40. MB-1520-GL-195 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `2.1489` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบเป็นทางการ
````

**คำตอบจาก Chatbot**

````text
ขอแสดงความนับถืออย่างยิ่งสำหรับความช่วยเหลือและโอกาสในการร่วมงานครั้งนี้
ขอบพระคุณอย่างสุดหัวใจสำหรับความใส่ใจและความเข้าใจที่มีต่อเราตลอดมาครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1520-GL-195.md)

## 41. MB-1523-GL-198 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.0` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบเป็นทางการ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1523-GL-198.md)

## 42. MB-1533-GL-208 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.0842` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ช่วยสรุปใจความสำคัญ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1533-GL-208.md)

## 43. MB-1536-GL-211 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `2.4644` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบแบบ bullet สั้น ๆ
````

**คำตอบจาก Chatbot**

````text
•    เวลาที่ใช้ในการส่งข้อมูลจากเครื่องหนึ่งไปยังอีกเครื่องหนึ่ง
•    มีผลต่อความล่าช้าในการตอบสนองของระบบ
•    สั้น ๆ คือ “เวลาตอบสนอง” ระหว่างการส่งและรับข้อมูล
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1536-GL-211.md)

## 44. MB-1543-GL-218 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.9724` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบ bullet สั้น ๆ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1543-GL-218.md)

## 45. MB-1550-GL-225 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.4511` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบประโยคเดียว
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและโอกาสในการร่วมงานครั้งนี้นะคะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1550-GL-225.md)

## 46. MB-1553-GL-228 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.9928` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบประโยคเดียว
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1553-GL-228.md)

## 47. MB-1557-GL-232 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.243` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:เฟรม|ความละเอียด`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
เฟรมเรตกับความละเอียดต่างกันยังไง อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1557-GL-232.md)

## 48. MB-1558-GL-233 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.2098` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:API|เชื่อมต่อ`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
API คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1558-GL-233.md)

## 49. MB-1559-GL-234 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.2067` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:JSON|ข้อมูล`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
JSON คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1559-GL-234.md)

## 50. MB-1560-GL-235 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.1954` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:ขอบคุณ`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1560-GL-235.md)

## 51. MB-1561-GL-236 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.2927` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:จอง`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
แปลคำว่า reservation เป็นภาษาไทย อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1561-GL-236.md)

## 52. MB-1562-GL-237 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.2593` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:กิจกรรม`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1562-GL-237.md)

## 53. MB-1563-GL-238 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.315` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1563-GL-238.md)

## 54. MB-1564-GL-239 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.2904` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:GPU|กราฟิก`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
GPU คืออะไรแบบเข้าใจง่าย อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1564-GL-239.md)

## 55. MB-1565-GL-240 - Chatbot ผิดจริง

- Root-cause bucket: `substring_collision_price_in_kho_sia`
- เวลา: `0.3156` วินาที
- Mode: `pipeline:ambiguity_clarification`
- Judge error: `category_mismatch:clarification, missing_any:server|client`
- Root cause: คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target
- ทำไมจึงผิด/ถูกมองว่าผิด: คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา
- วิธีแก้: เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`

**โจทย์**

````text
server กับ client ต่างกันยังไง อธิบายข้อดีข้อเสียสั้น ๆ
````

**คำตอบจาก Chatbot**

````text
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1565-GL-240.md)

## 56. MB-1573-GL-248 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.0872` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ให้คำจำกัดความแบบสั้น
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1573-GL-248.md)

## 57. MB-1583-GL-258 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `0.9716` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายด้วยคำง่าย ๆ
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1583-GL-258.md)

## 58. MB-1586-GL-261 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_latency_synonym`
- เวลา: `2.3542` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:latency|หน่วง`
- Root cause: Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`
- ทำไมจึงผิด/ถูกมองว่าผิด: เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword
- วิธีแก้: เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time

**โจทย์**

````text
อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบแบบไม่ต้องมีตัวอย่างยาว
````

**คำตอบจาก Chatbot**

````text
ความล่าช้าในการตอบสนองระหว่างอุปกรณ์กับระบบคอมพิวเตอร์ เช่น เวลาที่คลิกแล้วจอแสดงผลตอบสนองนานเกินไป โดยนับจากเวลาที่สั่งงานจนได้ผลลัพธ์จริง ๆ ครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1586-GL-261.md)

## 59. MB-1590-GL-265 - Judge ตรวจพลาด

- Root-cause bucket: `judge_false_negative_thanks_synonym`
- เวลา: `1.9904` วินาที
- Mode: `pipeline:general_llm_fallback`
- Judge error: `missing_any:ขอบคุณ`
- Root cause: Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`
- ทำไมจึงผิด/ถูกมองว่าผิด: คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ
- วิธีแก้: เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score

**โจทย์**

````text
ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบไม่ต้องมีตัวอย่างยาว
````

**คำตอบจาก Chatbot**

````text
ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและโอกาสที่ได้รับ
ขอบใจที่ให้เกียรติและสนับสนุนอย่างสุดหัวใจครับ/ค่ะ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1590-GL-265.md)

## 60. MB-1593-GL-268 - Chatbot ผิดจริง

- Root-cause bucket: `general_concept_misrouted_equipment`
- เวลา: `1.2173` วินาที
- Mode: `pipeline:structured_equipment_catalog`
- Judge error: `category_mismatch:equipment, missing_any:คีย์บอร์ด|mechanical`
- Root cause: คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป
- ทำไมจึงผิด/ถูกมองว่าผิด: ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร
- วิธีแก้: ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`

**โจทย์**

````text
คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบไม่ต้องมีตัวอย่างยาว
````

**คำตอบจาก Chatbot**

````text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
````

[เปิดไฟล์ Q&A รายข้อ](cases/MB-1593-GL-268.md)
