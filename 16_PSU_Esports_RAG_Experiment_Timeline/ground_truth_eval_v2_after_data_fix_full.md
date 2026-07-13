# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-30

## Summary

- Total: 360
- PASS: 338
- FAIL: 22
- ERROR: 0
- Pass rate: 93.89%
- Average latency: 0.320s
- Keyword fail: 22
- Source fail: 4
- Answers containing `ไม่พบข้อมูล`: 31
- Chinese character leakage: 0

## Mode Distribution

- `rule_fast_path`: 141
- `deterministic_calculator`: 131
- `rag_direct_curated`: 57
- `rag_llm`: 31

## Answer Type Distribution

- `fact`: 172
- `calculation`: 113
- `no_answer`: 34
- `list`: 19
- `summary`: 12
- `multi_fact`: 10

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| equipment | 10 | 10 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| no_answer | 26 | 26 | 100.00% |
| overview | 5 | 5 | 100.00% |
| service_fee | 137 | 139 | 98.56% |
| reservation | 88 | 93 | 94.62% |
| games | 23 | 26 | 88.46% |
| rules | 17 | 23 | 73.91% |
| penalty | 8 | 11 | 72.73% |
| knowledge | 4 | 7 | 57.14% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| no_answer | 34 | 34 | 100.00% |
| calculation | 112 | 113 | 99.12% |
| fact | 163 | 172 | 94.77% |
| list | 16 | 19 | 84.21% |
| summary | 9 | 12 | 75.00% |
| multi_fact | 4 | 10 | 40.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| medium | 255 | 270 | 94.44% |
| hard | 83 | 90 | 92.22% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| deterministic_calculator | 131 | 131 | 100.00% |
| rule_fast_path | 137 | 141 | 97.16% |
| rag_direct_curated | 50 | 57 | 87.72% |
| rag_llm | 20 | 31 | 64.52% |

## Failed Cases

| ID | Category | Mode | Problem | Retrieved IDs | Answer Short |
|---|---|---|---|---|---|
| v2_160 | service_fee | `rag_direct_curated` | missing keywords: PlayStation 5, Cockpit; missing sources: service_fee | curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_vr_duration, curated_reservation_service_ps5_duration | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ - บริการ Nintendo Switch ในระบบจองมี Nintendo Swich (1-2 Persons) 60 min และ Nintendo Swich (1-4 Persons) 60 min - VR St... |
| v2_177 | reservation | `rag_direct_curated` | missing keywords: จองใหม่ | curated_payment_10_minutes, curated_booking_no_edit, curated_time_change_policy, curated_reservation_advance_time | คำตอบ: - ผู้ใช้งานต้องชำระค่าบริการหลังจากจองเสร็จเรียบร้อยทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_payment_10_minutes) |
| v2_196 | reservation | `rag_direct_curated` | missing keywords: ธนาคารไทยพาณิชย์, 795-276244-1 | curated_booking_steps, curated_user_info_required, curated_booking_no_edit, curated_payment_10_minutes | คำตอบ: - ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking... |
| v2_203 | games | `rag_llm` | missing keywords: PlayStation 5, God of War Ragnarok | curated_games_ps5, services-our-games-01-026, services-our-games-01-027, services-our-games-01-018 | คำตอบ: มี |
| v2_207 | games | `rag_llm` | missing keywords: Nintendo Switch, Mario Kart; missing sources: Reservation | services-our-games-01-017, services-our-games-01-016, services-our-games-01-015, services-our-games-01-009 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_213 | games | `rag_direct_curated` | missing keywords: VALORANT; missing sources: Reservation | curated_home_equipment_pc_zone, curated_home_equipment_vr_zone, home-equipment-pc-001, curated_home_equipment_cockpit_zone | คำตอบ: - ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/ho... |
| v2_233 | rules | `rag_llm` | missing keywords: ห้าม, เสียดสี | curated_rule_noise_language, curated_booking_non_transferable, curated_rule_lost_items, curated_rule_weapons_gambling | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_237 | rules | `rag_llm` | missing keywords: ห้าม | curated_time_change_policy, reservation-studio-rules-002, reservation-checkin-001, home-studio-rules-001 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_238 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_weapons_gambling, reservation-studio-rules-002, home-studio-rules-001, services-our-games-01-011 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_245 | penalty | `rule_fast_path` | missing keywords: บาท | rule_severe_damage | คำตอบ: ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_severe_damag... |
| v2_248 | penalty | `rag_llm` | missing keywords: ระงับสิทธิ์ | curated_penalty_temp_suspension, curated_penalty_appeal, curated_penalty_booking_suspension, curated_penalty_permanent_suspension | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_251 | penalty | `rag_llm` | missing keywords: ระงับสิทธิ์ | curated_penalty_violation_record, curated_penalty_booking_suspension, curated_time_change_policy, curated_rule_lost_items | คำตอบ: พบในฐานข้อมูลที่มี ระบุไว้ว่าการละเมิดกฎจะถูกบันทึกในประวัติการใช้บริการของผู้ใช้งาน (Reservation Penalty - บันทึกประวัติการละเมิด) |
| v2_263 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | curated_knowledge_esports_origin, knowledge-ประวัติของ-esports-13-001, curated_knowledge_esports_definition, knowledge-knowledge-01-001 | คำตอบ: Esports เริ่มขึ้นครั้งแรกที่มหาวิทยาลัยสแตนฟอร์ด (Stanford University) ในวันที่ 19 ตุลาคม ค.ศ. 1972 |
| v2_267 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | curated_knowledge_overcooked2_skills, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-002, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-001, knowledge-knowledge-01-002 | คำตอบ: Overcooked! 2 ฝึกทักษะการทำงานเป็นทีม, การจัดการสถานการณ์กดดัน, การสื่อสารอย่างชัดเจน, และการวางแผน. |
| v2_268 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-002, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-001, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-003, services-our-games-01-004 | คำตอบ: Mario Kart 8 Deluxe ฝึกไหวพริบและการตัดสินใจในการแข่งขัน. ในเกมนี้ผู้เล่นต้องควบคุมตัวละครและรถบนสนามที่เต็มไปด้วยทางโค้ง, สิ่งกีดขวาง และไอเทมหลากหลายรูปแบบ ทำให้จำเป็นต้องใช้วาทีและการคิดอย่างรวดเร็ว. นอกจากนี้ย... |
| v2_299 | reservation | `rule_fast_path` | missing keywords: ไม่มีการคืนเงิน | rule_payment_10_minutes | คำตอบ: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_paym... |
| v2_302 | reservation | `rag_direct_curated` | missing keywords: สลิป, โอนเงิน | curated_user_info_required, curated_booking_no_edit, curated_booking_steps, curated_checkin_id_required | คำตอบ: - ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_user_info_required) |
| v2_303 | reservation | `rag_direct_curated` | missing keywords: ยกเลิก, จองใหม่ | curated_time_change_policy, curated_booking_no_edit, curated_reservation_advance_time, curated_cancel_1_hour | คำตอบ: - สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curat... |
| v2_304 | service_fee | `rag_direct_curated` | missing keywords: บาท; missing sources: service_fee | curated_home_equipment_vr_zone, curated_home_equipment_ps5_zone, curated_home_equipment_pc_zone, curated_home_equipment_cockpit_zone | คำตอบ: - VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone) |
| v2_310 | rules | `rule_fast_path` | missing keywords: ห้าม | rule_lost_personal_items | คำตอบ: กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_lost_personal_items / Reservation, curated_ru... |
| v2_312 | rules | `rule_fast_path` | missing keywords: ห้าม | rule_return_equipment_games | คำตอบ: กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_return_equipment_games / Reservation, curated_rule_return_equipment, reservation-studio-rule... |
| v2_313 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_report_problem, curated_time_change_policy, reservation-studio-rules-002, curated_reservation_advance_time | คำตอบ: ควรแจ้งเจ้าหน้าที่ทันที หากพบปัญหาการใช้งาน, พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ตาม Reservation Rules - พบปัญหาให้แจ้งเจ้าหน้าที่ |

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_v2_after_data_fix_full.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_v2_after_data_fix_full.jsonl`
