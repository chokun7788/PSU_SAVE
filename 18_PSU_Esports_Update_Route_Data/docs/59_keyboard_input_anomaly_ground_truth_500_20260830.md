# Keyboard Input Anomaly Ground Truth 500

วันที่: 2026-08-30  
สถานะ: Dataset v1 สำหรับออกแบบและประเมิน Detector เท่านั้น ยังไม่ใช้แก้ข้อความผู้ใช้อัตโนมัติ

## 1. เป้าหมาย

ชุดข้อมูลนี้ใช้ทดสอบระบบตรวจจับ Input สองปัญหาโดยแยก Label ออกจากกัน:

1. `keyboard_layout_mismatch` ผู้ใช้ตั้งใจพิมพ์ภาษาไทยแต่คีย์บอร์ดอยู่ภาษาอังกฤษ หรือกลับกัน
2. `repeated_character_typo` ผู้ใช้กดตัวอักษร สระ หรือวรรณยุกต์ซ้ำโดยไม่ตั้งใจ

หลักการสำคัญคือ Detector มีหน้าที่แจ้งเตือนเท่านั้น ข้อความที่สงสัยว่าผิดภาษาต้องไม่ถูกนำไปตอบด้วย Fast/Structured, RAG หรือ LLM โดยอัตโนมัติ

## 2. ไฟล์

- `data/eval/keyboard_input_anomaly_ground_truth_500_20260830.jsonl` เป็นไฟล์หลักสำหรับโปรแกรม
- `data/eval/keyboard_input_anomaly_ground_truth_500_20260830.csv` ใช้เปิดตรวจใน Excel
- `data/eval/keyboard_input_anomaly_ground_truth_500_20260830.summary.json` สรุปจำนวนและผลตรวจโครงสร้าง
- `tools/generate_keyboard_input_anomaly_ground_truth_500.py` สร้างชุดข้อมูลแบบ deterministic

## 3. เหตุผลที่ไม่ใช้ Alias ทีละคำ

Alias รายคำเหมาะกับคำเฉพาะที่มีขอบเขต เช่น ชื่อเกม ชื่อโซน หรือชื่ออุปกรณ์ แต่ไม่เหมาะกับการตรวจภาษาคีย์บอร์ด เพราะประโยคใหม่สร้างได้ไม่จำกัด

งานวิจัยภาษาไทยเสนอทางเลือกที่กว้างกว่า:

- Chawannakul และ Prasitjutrakul ใช้พจนานุกรมแบบ depth-limited trie ร่วมกับ heuristic และ certainty score สำหรับตรวจ Thai/English keyboard mismatch
- Potipiti, Sornlertlamvanich และ Thanadkran ใช้ character bigram/trigram และ error-correction rules สำหรับ Thai-English language identification
- งาน Language Detection Engine ใช้ character n-gram ร่วมกับ logistic regression เพื่อให้ทำงานเบาและรองรับคำที่ไม่ได้กำหนดเป็น Alias

ชุด Ground Truth นี้จึงสร้างความผิดจากตำแหน่งแป้น Thai Kedmanee และการกดซ้ำโดยตรง ไม่ได้สร้างจากรายการคำแปลผิดทีละคำ

## 4. รูปแบบความผิดที่ครอบคลุม

### 4.1 ผิดคีย์บอร์ดทั้งข้อความ

ผู้ใช้ลืมสลับภาษาก่อนเริ่มพิมพ์ ตัวอย่าง:

```text
Observed:  g]jo
Intended:  เล่น
Label:     keyboard_layout_mismatch
Action:    request_retype
```

คำถามที่มีชื่อเกมหรืออุปกรณ์ภาษาอังกฤษจะเก็บ Entity เดิมไว้ แล้วเปลี่ยนเฉพาะตัวอักษรไทยตามตำแหน่งปุ่ม เช่น `PS5 ik8k` สำหรับ `PS5 ราคา`

### 4.2 ผิดเฉพาะคำหรือช่วงหนึ่ง

ผู้ใช้เปลี่ยนภาษาไม่ทันระหว่างประโยค:

```text
Observed:  ถ้าจะg]jo Counter-Strike 2 ต้องจองอะไร
Intended:  ถ้าจะเล่น Counter-Strike 2 ต้องจองอะไร
```

กลุ่มนี้ยากกว่าการผิดทั้งข้อความ เพราะ Input ยังมีภาษาไทยที่ถูกต้องและ Entity ภาษาอังกฤษอยู่พร้อมกัน

### 4.3 เปลี่ยนภาษากลางประโยค

ช่วงต้นถูกต้อง แต่ช่วงท้ายถูกพิมพ์ด้วย Layout อื่น:

```text
Observed:  บุคคลทั่วไป เล่น PC 30 นาที เสียduj[km
Intended:  บุคคลทั่วไป เล่น PC 30 นาที เสียกี่บาท
```

### 4.4 ตั้งใจพิมพ์อังกฤษแต่คีย์บอร์ดเป็นไทย

ครอบคลุมทิศทางกลับกันด้วย เช่นคำถามภาษาอังกฤษทั้งประโยคที่แสดงออกมาเป็นตัวอักษรไทยตามตำแหน่งปุ่ม

### 4.5 ตัวอักษรไทยเบิ้ลภายในคำ

```text
Observed:  PC ราคคาเท่าไหร่
Intended:  PC ราคาเท่าไหร่
Label:     repeated_character_typo
Action:    soft_flag_typo
```

### 4.6 สระและวรรณยุกต์เบิ้ล

```text
Observed:  Gaming Monitor ใช้้ทำอะไร
Intended:  Gaming Monitor ใช้ทำอะไร
```

กลุ่มนี้ต้องทดสอบแยก เพราะภาษาไทยมี Combining Marks และการเทียบเฉพาะพยัญชนะจะตรวจไม่ครบ

### 4.7 ตัวอักษรอังกฤษในชื่อเกมหรือคำเทคนิคเบิ้ล

```text
Observed:  มี Call of Duty: Warzzone ไหม
Intended:  มี Call of Duty: Warzone ไหม
```

### 4.8 ผิดคีย์บอร์ดและตัวอักษรเบิ้ลพร้อมกัน

เคสนี้มี Label สองตัว ระบบควรหยุดขอให้พิมพ์ใหม่เพราะ `keyboard_layout_mismatch` มีความเสี่ยงสูงกว่า

## 5. Hard Negatives ที่ต้องไม่ตรวจผิด

Ground Truth ไม่ได้มีแต่ Input ผิด มีข้อความปกติ 120 ข้อสำหรับวัด False Positive ด้วย

### 5.1 ภาษาไทยผสม Entity ภาษาอังกฤษ

```text
VR ราคาเท่าไหร่
Minecraft มีใน PC #03 ไหม
Counter-Strike 2 ใช้ Steam เวอร์ชันไหน
```

### 5.2 URL, Email, ID, วันที่ และเวลา

```text
https://esports.phuket.psu.ac.th
esports@phuket.psu.ac.th
booking_id=BK-2026-000456
2026-09-01 เวลา 13:30
```

### 5.3 การยืดคำเพื่อแสดงอารมณ์

```text
เล่นได้ไหมมม
ขอบคุณค่าาา
อยากเล่นมากกก
```

Dataset v1 กำหนดให้ข้อความเหล่านี้เป็น `expressive` และไม่ถือเป็น accidental repeated-character typo เพื่อไม่ให้ Chatbot ขัดจังหวะภาษาพูดมากเกินไป

### 5.4 ตัวซ้ำที่เป็นส่วนหนึ่งของคำจริง

```text
TEKKEN 8
Overcooked! 2
Football Manager
กรรมการการแข่งขัน
บรรยากาศ
```

Detector ห้ามใช้กฎง่าย ๆ ว่า "เจอตัวติดกันเหมือนกันแล้วเป็น Typo" เพราะจะเกิด False Positive กับคำจริงเหล่านี้

## 6. สัดส่วนข้อมูล

| กลุ่ม | จำนวน |
|---|---:|
| Thai intended, English layout ทั้งข้อความ | 90 |
| ผิด Layout เฉพาะช่วง | 45 |
| เปลี่ยน Layout กลางประโยค | 20 |
| English intended, Thai layout | 25 |
| ตัวอักษรไทยเบิ้ลภายในคำ | 60 |
| สระหรือวรรณยุกต์ไทยเบิ้ล | 40 |
| ตัวอักษรอังกฤษเบิ้ล | 25 |
| คำสั้นที่มีตัวอักษรเบิ้ล | 15 |
| ผิด Layout และตัวอักษรเบิ้ลพร้อมกัน | 60 |
| Input ปกติจาก Benchmark | 50 |
| Mixed/Protected Input | 30 |
| การยืดคำโดยตั้งใจ | 20 |
| ตัวซ้ำที่ถูกต้องตามคำ | 20 |
| **รวม** | **500** |

เมื่อนับ Label ที่ซ้อนกัน:

- `keyboard_layout_mismatch`: 240 ข้อ
- `repeated_character_typo`: 200 ข้อ
- มีทั้งสอง Label: 60 ข้อ
- ไม่ควรติด Label ใด: 120 ข้อ

อัตราส่วนนี้ออกแบบเพื่อให้ครอบคลุม Edge Cases ไม่ใช่การประมาณสัดส่วนความผิดจริงของผู้ใช้งาน Production

## 7. Schema สำคัญ

| Field | ความหมาย |
|---|---|
| `observed_input` | ข้อความที่ Chatbot ได้รับจริง |
| `canonical_question` | ข้อความที่ผู้ใช้ตั้งใจพิมพ์ ใช้เป็น Ground Truth เท่านั้น |
| `expected_flags` | รายการปัญหาที่ Detector ควรตรวจพบ |
| `should_detect_keyboard_layout` | ควรตรวจผิด Layout หรือไม่ |
| `should_detect_repeated_character` | ควรตรวจตัวอักษรเบิ้ลแบบผิดพลาดหรือไม่ |
| `should_block_answer` | ต้องหยุดก่อนเข้า Answer Pipeline หรือไม่ |
| `expected_action` | `request_retype`, `soft_flag_typo` หรือ `continue` |
| `repeat_interpretation` | `accidental`, `expressive`, `lexical` หรือ `none` |
| `anomaly_family` | กลุ่มย่อยสำหรับวิเคราะห์ Error |
| `layout_direction` | ทิศทางภาษาและ Layout ที่ไม่ตรงกัน |
| `corruption_scope` | ผิดทั้งข้อความ เฉพาะช่วง หรือเฉพาะตัวอักษร |
| `split` | `calibration` หรือ `test` |

## 8. การแบ่งข้อมูล

- `calibration`: 100 ข้อ ใช้เลือก Threshold และปรับ Rule
- `test`: 400 ข้อ ใช้วัดผลหลังล็อก Threshold แล้ว

ห้ามปรับ Threshold จากผลของ Test Split เพราะจะทำให้คะแนนไม่สะท้อนการใช้งานกับข้อความใหม่

## 9. Metric ที่ควรรายงาน

รายงานแยกอย่างน้อยดังนี้:

1. Precision, Recall และ F1 ของ `keyboard_layout_mismatch`
2. Precision, Recall และ F1 ของ `repeated_character_typo`
3. False Positive Rate บน 120 ข้อที่ไม่ควรติด Label
4. False Positive แยก `expressive`, `lexical double`, `URL/ID` และ `mixed language`
5. Recall แยกข้อความสั้น, ผิดเฉพาะช่วง และผิดสองแบบพร้อมกัน
6. Action accuracy สำหรับ `request_retype`, `soft_flag_typo` และ `continue`

สำหรับ Product นี้ควรให้ความสำคัญกับ Precision ของ Layout Detector ก่อน Recall เพราะ False Positive จะทำให้ผู้ใช้ที่พิมพ์ถูกต้องถูกบังคับให้พิมพ์ใหม่

## 10. Quality Checks ที่ผ่านแล้ว

- จำนวน JSONL: 500 แถว
- จำนวน CSV: 500 แถว
- ID ไม่ซ้ำ
- `observed_input` ไม่ซ้ำ
- Calibration 100 / Test 400
- จำนวนแต่ละ Family ตรงตามแผน
- ทุกข้อที่ Label ว่าตัวอักษรเบิ้ลมีอักขระซ้ำติดกันจริง
- ครอบคลุมคำถามต้นทาง 17 กลุ่ม รวมราคา เกม อุปกรณ์ เวลา การจอง สมาชิก กฎการแข่งขัน และคำถามหลายส่วน

## 11. ข้อจำกัด

1. ข้อมูลส่วนใหญ่เป็น Synthetic Error จากคำถามที่สะอาด ไม่ใช่ Keystroke Log จริง
2. รองรับ Thai Kedmanee เป็นหลัก ยังไม่ครอบคลุม Pattachote หรือ Layout เฉพาะอุปกรณ์
3. Mobile keyboard, swipe typing และ voice input อาจมีรูปแบบความผิดต่างออกไป
4. การแยก accidental repetition กับ expressive repetition เป็น Product Policy และมีความกำกวมตามบริบท
5. ผลความแม่นจาก Paper ไม่ควรถูกนำมาใช้แทนคะแนนบน Dataset นี้

ระยะถัดไปควรเก็บข้อความผิดจริงแบบไม่เก็บข้อมูลส่วนบุคคล แล้วให้ผู้ตรวจอย่างน้อยสองคน Label เพิ่ม ก่อนนำมารวมเป็น Ground Truth v2

## 12. References

- Chawannakul, C. and Prasitjutrakul, S. (2011). [Keyboard layout mismatch error detection and correction system utility](https://doi.org/10.1109/ECTICON.2011.5947881)
- Potipiti, T., Sornlertlamvanich, V. and Thanadkran, K. (2001). [Towards an Intelligent Multilingual Keyboard System](https://aclanthology.org/www.mt-archive.info/00/HLT-2001-Potipiti.pdf)
- Gothe, S. V. et al. (2021). [Language Detection Engine for Multilingual Texting on Mobile Devices](https://arxiv.org/abs/2101.03963)
- Lee, S., Lee, J. and Lee, G. (2019). [Diagnosing and Coping with Mode Errors in Korean-English Dual-language Keyboard](https://doi.org/10.1145/3290605.3300255)
- Khumsap, R. et al. (2026). [P.L.I.C.K.: Personalized Language Interface for Correction and Keyboard Switching](https://doi.org/10.1109/JCSSE68839.2026.11596992)
