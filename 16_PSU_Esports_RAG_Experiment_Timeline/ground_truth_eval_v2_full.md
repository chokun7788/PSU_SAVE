# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-30

## Summary

- Total: 360
- PASS: 272
- FAIL: 88
- ERROR: 0
- Pass rate: 75.56%
- Average latency: 0.631s
- Keyword fail: 88
- Source fail: 6
- Answers containing `ไม่พบข้อมูล`: 41
- Chinese character leakage: 0

## Mode Distribution

- `deterministic_calculator`: 133
- `rule_fast_path`: 86
- `rag_direct_curated`: 77
- `rag_llm`: 64

## Answer Type Distribution

- `fact`: 160
- `calculation`: 113
- `no_answer`: 34
- `list`: 31
- `summary`: 12
- `multi_fact`: 10

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| service_fee | 119 | 139 | 85.61% |
| no_answer | 21 | 26 | 80.77% |
| equipment | 8 | 10 | 80.00% |
| overview | 4 | 5 | 80.00% |
| penalty | 8 | 11 | 72.73% |
| reservation | 67 | 93 | 72.04% |
| rules | 14 | 23 | 60.87% |
| knowledge | 4 | 7 | 57.14% |
| games | 7 | 26 | 26.92% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 95 | 113 | 84.07% |
| no_answer | 28 | 34 | 82.35% |
| fact | 124 | 160 | 77.50% |
| summary | 8 | 12 | 66.67% |
| list | 14 | 31 | 45.16% |
| multi_fact | 3 | 10 | 30.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| medium | 212 | 270 | 78.52% |
| hard | 60 | 90 | 66.67% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| rule_fast_path | 79 | 86 | 91.86% |
| deterministic_calculator | 114 | 133 | 85.71% |
| rag_direct_curated | 53 | 77 | 68.83% |
| rag_llm | 26 | 64 | 40.62% |

## Failed Cases

| ID | Category | Mode | Problem | Retrieved IDs | Answer Short |
|---|---|---|---|---|---|
| v2_051 | service_fee | `deterministic_calculator` | missing keywords: 50 | calculator_ps5 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s)... |
| v2_052 | service_fee | `deterministic_calculator` | missing keywords: 50 | calculator_ps5 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s)... |
| v2_069 | service_fee | `deterministic_calculator` | missing keywords: 50 | calculator_nintendo_1_2 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 se... |
| v2_070 | service_fee | `deterministic_calculator` | missing keywords: 50 | calculator_nintendo_1_2 | คำตอบ: - ช่วงเวลาที่ถามคือ 01:00-02:00 = 1 ชั่วโมง - บริการ Nintendo Switch 1-2 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บาท แหล่งข้อ... |
| v2_087 | service_fee | `deterministic_calculator` | missing keywords: 100 | calculator_nintendo_3_4 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 se... |
| v2_088 | service_fee | `deterministic_calculator` | missing keywords: 100 | calculator_nintendo_3_4 | คำตอบ: - ช่วงเวลาที่ถามคือ 03:00-04:00 = 1 ชั่วโมง - บริการ Nintendo Switch 3-4 คน คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บาท แหล่งข้อ... |
| v2_105 | service_fee | `deterministic_calculator` | missing keywords: 65 | calculator_cockpit | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บา... |
| v2_106 | service_fee | `deterministic_calculator` | missing keywords: 65 | calculator_cockpit | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ Cockpit คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บา... |
| v2_123 | service_fee | `deterministic_calculator` | missing keywords: 190 | calculator_vr_30 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที - บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บ... |
| v2_124 | service_fee | `deterministic_calculator` | missing keywords: 190 | calculator_vr_30 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 30 นาที - บริการ VR 30 นาที คิดเป็นรอบละ 30 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) = 0 บ... |
| v2_141 | service_fee | `deterministic_calculator` | missing keywords: 375 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) =... |
| v2_142 | service_fee | `deterministic_calculator` | missing keywords: 375 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: นักศึกษา/บุคลากร PSU - ราคา 0 บาท/session × 1 session(s) =... |
| v2_143 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_144 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_145 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_146 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_147 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_148 | service_fee | `deterministic_calculator` | missing keywords: 1050 | calculator_vr_60 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ VR 1 ชั่วโมง คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - กลุ่มผู้ใช้: บุคคลทั่วไป - ราคา 1,050 บาท/session × 1 session(s) = 1,05... |
| v2_155 | service_fee | `rag_llm` | missing keywords: PC, Service Fee | curated_service_fee_pc_unknown, curated_home_equipment_pc_zone, curated_service_fee_2026_full_table, reservation-studio-rules-002 | คำตอบ: ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_162 | service_fee | `deterministic_calculator` | missing keywords: Nintendo Switch, Cockpit, VR | calculator_ps5 | คำตอบ: - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ PlayStation 5 คิดเป็นรอบละ 60 นาที ดังนั้นต้องใช้ 1 session(s) - นักศึกษา/บุคลากร PSU: 0 บาท/session × 1 = 0 บาท - ศิษย์เก่า PSU / นักศ... |
| v2_173 | reservation | `rag_direct_curated` | missing keywords: 10 นาที, ยกเลิก | curated_service_fee_vr_30_rates, curated_service_fee_vr_60_rates, curated_service_fee_cockpit_rates, curated_service_fee_pc_unknown | คำตอบ: - ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท - ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท,... |
| v2_175 | reservation | `rag_direct_curated` | missing keywords: 10 นาที, ยกเลิก | curated_reservation_service_ps5_duration, curated_reservation_service_pc_duration, curated_reservation_service_vr_duration, curated_reservation_service_nintendo_capacity | คำตอบ: - บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration) |
| v2_176 | reservation | `rag_direct_curated` | missing keywords: 10 นาที | curated_booking_no_edit, curated_payment_10_minutes, curated_checkin_late_cancel, curated_reservation_cancel_invalid_info | คำตอบ: - เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: - https://esports.computing.psu.ac... |
| v2_180 | reservation | `rag_direct_curated` | missing keywords: ยกเลิก, สลิป | curated_time_change_policy, curated_booking_no_edit, reservation-booking-rules-001, curated_cancel_1_hour | คำตอบ: - สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curat... |
| v2_185 | reservation | `rag_llm` | missing keywords: ไม่สามารถโอนสิทธิ์ | reservation-booking-rules-002, curated_time_change_policy, curated_booking_non_transferable, curated_booking_no_edit | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_186 | reservation | `rag_direct_curated` | missing keywords: ไม่สามารถโอนสิทธิ์ | curated_time_change_policy, curated_booking_non_transferable, curated_booking_no_edit, curated_checkin_late_cancel | คำตอบ: - สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curat... |
| v2_191 | reservation | `rag_llm` | missing keywords: 30 นาที | reservation-checkin-001, reservation-penalty-002, curated_checkin_late_cancel, curated_time_change_policy | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_192 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_checkin_id_required, curated_checkin_30_minutes, curated_booking_steps, curated_reservation_advance_time | คำตอบ: - เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_checkin_id_required) |
| v2_193 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_checkin_id_required, curated_checkin_30_minutes, curated_checkin_late_cancel, curated_time_change_policy | คำตอบ: - เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_checkin_id_required) |
| v2_198 | reservation | `rag_llm` | missing keywords: โอน | curated_payment_bank, curated_booking_steps, curated_time_change_policy, reservation-howto-001 | คำตอบ: ธนาคารที่ใช้รับเงินคือ Siam Commercial Bank (ธนาคารไทยพาณิชย์) |
| v2_199 | games | `rag_llm` | missing keywords: TEKKEN 8 | curated_home_equipment_ps5_zone, curated_reservation_service_ps5_duration, curated_home_equipment_vr_zone, curated_games_ps5 | คำตอบ: มีเกม Spider-Man 2 บน PlayStation 5 |
| v2_200 | games | `rag_direct_curated` | missing keywords: PlayStation 5, TEKKEN 8 | curated_rule_return_equipment, curated_rule_report_problem, curated_rule_lost_items, curated_rule_belongings | คำตอบ: - กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_return_equipment) |
| v2_202 | games | `rag_llm` | missing keywords: TEKKEN 8 | curated_games_ps5, curated_reservation_service_ps5_duration, curated_home_equipment_ps5_zone, curated_about_gallery_categories | คำตอบ: PS5 เล่น Fortnite ได้. ในรายการเกมที่ปรากฏใน PlayStation 5 (ดูจากแหล่งข้อมูลที่ 1) มี Fortnite อยู่ในรายชื่อ. |
| v2_203 | games | `rag_llm` | missing keywords: PlayStation 5, TEKKEN 8 | curated_games_ps5, services-our-games-01-026, services-our-games-01-027, services-our-games-01-018 | คำตอบ: มี |
| v2_205 | games | `rag_llm` | missing keywords: Nintendo Switch, Mario Kart | curated_games_switch, curated_home_equipment_nintendo_zone, curated_reservation_service_nintendo_capacity, curated_about_gallery_categories | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_207 | games | `rag_llm` | missing keywords: Nintendo Switch, Mario Kart; missing sources: Reservation | services-our-games-01-017, services-our-games-01-016, services-our-games-01-015, services-our-games-01-009 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_208 | games | `rag_llm` | missing keywords: Nintendo Switch, Mario Kart | curated_home_equipment_nintendo_zone, curated_games_switch, curated_about_gallery_categories, curated_reservation_service_nintendo_capacity | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_209 | games | `rag_llm` | missing keywords: PC, VALORANT | curated_home_equipment_pc_zone, curated_games_pc, home-equipment-pc-001, curated_about_gallery_categories | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_210 | games | `rag_llm` | missing keywords: PC, VALORANT | curated_home_equipment_pc_zone, curated_games_pc, curated_rule_return_equipment, curated_news_cs2_2026 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_213 | games | `rag_direct_curated` | missing keywords: VALORANT; missing sources: Reservation | curated_home_equipment_pc_zone, curated_home_equipment_vr_zone, home-equipment-pc-001, curated_home_equipment_cockpit_zone | คำตอบ: - ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/ho... |
| v2_215 | games | `rag_llm` | missing keywords: VR; missing sources: Reservation | services-our-games-01-023, knowledge-beat-saber-เมื่อจังหวะดนตรี-กลายเป็นหยาดเหงื่อและสมาธิระดับพระกาฬ-05-002, knowledge-beat-saber-เมื่อจังหวะดนตรี-กลายเป็นหยาดเหงื่อและสมาธิระดับพระกาฬ-05-004, knowledge-beat-saber-เมื่อจังหวะดนตรี-กลายเป็นหยาดเหงื่อและสมาธิระดับพระกาฬ-05-003 | คำตอบ: Beat Saber เป็นเกมแนว Rhythm ในระบบ Virtual Reality ที่ผู้เล่นต้องใช้ดาบสีแดงและน้ำเงินฟัน Block ตามจังหวะเพลง และหลบหลีกกำแพงและระเบิดที่พุ่งเข้ามาหาตัว. |
| v2_216 | games | `rag_direct_curated` | missing keywords: Beat Saber; missing sources: Reservation | curated_home_equipment_vr_zone, curated_home_equipment_ps5_zone, curated_home_equipment_cockpit_zone, home-equipment-vr-001 | คำตอบ: - VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone) |
| v2_217 | games | `rule_fast_path` | missing keywords: VR, Beat Saber | rule_cockpit_games | คำตอบ: Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_cockpit_games / Reservation, curated_games_cockpit, reservation-service-cockpit) |
| v2_218 | games | `rag_llm` | missing keywords: VR, Beat Saber | knowledge-gran-turismo-7-สนามจำลองการฝึกทักษะการ-ผ่านความเร็วระดับ-300-กม-ชม-03-001, curated_reservation_service_cockpit_game, curated_games_cockpit, knowledge-gran-turismo-7-สนามจำลองการฝึกทักษะการ-ผ่านความเร็วระดับ-300-กม-ชม-03-004 | คำตอบ: ใช่ พวงมาลัยเป็นส่วนสำคัญในการควบคุมการขับขี่ในเกม Gran Turismo 7. |
| v2_222 | equipment | `rule_fast_path` | missing keywords: Gaming PC, 10 Units; missing sources: home | rule_pc_games | คำตอบ: เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_pc_games / Reservation,... |
| v2_223 | equipment | `rag_llm` | missing keywords: Gaming PC, 10 Units | curated_home_equipment_pc_zone, reservation-studio-rules-002, curated_damage_moderate, curated_rule_report_problem | คำตอบ: ใน Home PC Zone มีให้ใช้ Mouse และ Headset แต่ไม่มีการระบุว่ามีเมาส์หรือไม่ |
| v2_229 | rules | `rag_llm` | missing keywords: ห้าม | reservation-studio-rules-001, reservation-studio-rules-002, home-studio-rules-001, home-studio-rules-002 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_230 | rules | `rule_fast_path` | missing keywords: ห้าม | rule_food_drink | คำตอบ: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_food_drink / curated_rule_food_drinks) |
| v2_231 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_belongings, curated_time_change_policy, curated_reservation_advance_time, curated_booking_no_edit | คำตอบ: ตามข้อมูลที่ให้มานั้นไม่มีคำอธิบายเกี่ยวกับเรื่องของการฝากสัมภาระ กรุณาตรวจสอบข้อมูลเพิ่มเติมหรือติดต่อศูนย์บริการของ PSU Esports Studio สำหรับรายละเอียดที่แน่นอน. |
| v2_233 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_noise_language, curated_booking_non_transferable, curated_rule_lost_items, curated_rule_weapons_gambling | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_237 | rules | `rag_llm` | missing keywords: ห้าม | curated_time_change_policy, reservation-studio-rules-002, reservation-checkin-001, home-studio-rules-001 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_238 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_weapons_gambling, reservation-studio-rules-002, home-studio-rules-001, services-our-games-01-011 | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_245 | penalty | `rule_fast_path` | missing keywords: บาท | rule_severe_damage | คำตอบ: ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_severe_damag... |
| v2_248 | penalty | `rag_llm` | missing keywords: ระงับสิทธิ์ | curated_penalty_temp_suspension, curated_penalty_appeal, curated_penalty_booking_suspension, curated_penalty_permanent_suspension | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_251 | penalty | `rag_llm` | missing keywords: ระงับสิทธิ์ | curated_penalty_violation_record, curated_penalty_booking_suspension, curated_time_change_policy, curated_rule_lost_items | คำตอบ: พบในฐานข้อมูลที่มี ระบุไว้ว่าการละเมิดกฎจะถูกบันทึกในประวัติการใช้บริการของผู้ใช้งาน (Reservation Penalty - บันทึกประวัติการละเมิด) |
| v2_254 | overview | `rag_direct_curated` | missing keywords: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์; missing sources: home | curated_about_members_manager, curated_about_members_dean, curated_about_members_president, about-members-club-001 | คำตอบ: - หน้าสมาชิกระบุว่า นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_manager) |
| v2_263 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | curated_knowledge_esports_origin, knowledge-ประวัติของ-esports-13-001, curated_knowledge_esports_definition, knowledge-knowledge-01-001 | คำตอบ: Esports เริ่มขึ้นครั้งแรกที่มหาวิทยาลัยสแตนฟอร์ด (Stanford University) ในวันที่ 19 ตุลาคม ค.ศ. 1972 |
| v2_267 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | curated_knowledge_overcooked2_skills, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-002, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-001, knowledge-knowledge-01-002 | คำตอบ: Overcooked! 2 ฝึกทักษะการทำงานเป็นทีม, การจัดการสถานการณ์กดดัน, การสื่อสารอย่างชัดเจน, และการวางแผน. |
| v2_268 | knowledge | `rag_llm` | missing keywords: อีสปอร์ต | knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-002, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-001, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-003, services-our-games-01-004 | Mario Kart 8 Deluxe ฝึกไหวพริบและการตัดสินใจผ่านการควบคุมตัวละครบนสนามที่เต็มไปด้วยทางโค้ง, สิ่งกีดขวาง และไอเทมหลากหลายรูปแบบ. การตัดสินใจว่าจะเร่ง เบรก ดริฟต์ หรือใช้ไอเทมเมื่อไร ล้วนต้องอาศัยไหวพริบและการคิดอย่างรวดเร... |
| v2_288 | no_answer | `rag_direct_curated` | missing keywords: ไม่พบข้อมูล | curated_home_popular_games_list, curated_games_popular, curated_games_ps5, curated_games_pc | คำตอบ: - เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber - เกมที่ปรากฏในรายการ PlayStation 5 ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootb... |
| v2_289 | no_answer | `rag_direct_curated` | missing keywords: ไม่พบข้อมูล | curated_games_pc, services-our-games-01-017, services-our-games-01-002, services-our-games-01-030 | คำตอบ: - เกมที่ปรากฏในรายการ PC ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_games_pc) |
| v2_292 | no_answer | `rag_direct_curated` | missing keywords: ไม่พบข้อมูล | curated_service_fee_2026_full_table, curated_service_fee_pc_unknown, curated_service_fee_vr_60_rates, curated_service_fee_vr_30_rates | คำตอบ: - ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch... |
| v2_294 | no_answer | `rag_direct_curated` | missing keywords: ไม่พบข้อมูล | curated_time_change_policy, curated_booking_steps, curated_reservation_advance_time, curated_booking_no_edit | คำตอบ: - สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curat... |
| v2_300 | reservation | `rule_fast_path` | missing keywords: 10 นาที | rule_booking_advance | คำตอบ: ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_booking_advance / curated_reservation_advance_time) |
| v2_301 | reservation | `rag_direct_curated` | missing keywords: 10 นาที | curated_service_fee_vr_60_rates, curated_service_fee_vr_30_rates, curated_service_fee_pc_unknown, curated_service_fee_cockpit_rates | คำตอบ: - ค่าบริการ VR 1 ชั่วโมง: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 375 บาท, บุคคลทั่วไป 1050 บาท - ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท... |
| v2_302 | reservation | `rag_direct_curated` | missing keywords: 10 นาที | curated_user_info_required, curated_booking_no_edit, curated_booking_steps, curated_checkin_id_required | คำตอบ: - ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_user_info_required) |
| v2_303 | reservation | `rag_direct_curated` | missing keywords: 10 นาที | curated_time_change_policy, curated_booking_no_edit, curated_reservation_advance_time, curated_cancel_1_hour | คำตอบ: - สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curat... |
| v2_310 | rules | `rule_fast_path` | missing keywords: ห้าม | rule_lost_personal_items | คำตอบ: กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_lost_personal_items / Reservation, curated_ru... |
| v2_312 | rules | `rule_fast_path` | missing keywords: ห้าม | rule_return_equipment_games | คำตอบ: กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_return_equipment_games / Reservation, curated_rule_return_equipment, reservation-studio-rule... |
| v2_313 | rules | `rag_llm` | missing keywords: ห้าม | curated_rule_report_problem, curated_time_change_policy, reservation-studio-rules-002, curated_reservation_advance_time | คำตอบ: ควรแจ้งเจ้าหน้าที่ทันที หากพบปัญหาการใช้งาน |
| v2_314 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_cancel_1_hour, curated_booking_no_edit, curated_checkin_late_cancel, curated_time_change_policy | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_317 | games | `rag_llm` | missing keywords: VALORANT | curated_home_equipment_pc_zone, curated_games_pc, curated_about_members_dean, curated_rule_return_equipment | ไม่มี |
| v2_318 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_ps5_duration, curated_reservation_service_vr_duration | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) |
| v2_322 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_booking_no_edit, curated_time_change_policy, curated_checkin_late_cancel, curated_reservation_advance_time | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_325 | games | `rag_llm` | missing keywords: VALORANT | curated_home_equipment_pc_zone, curated_games_pc, curated_about_members_dean, curated_rule_return_equipment | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_326 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_ps5_duration, curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_vr_duration | คำตอบ: - บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration) |
| v2_330 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_cancel_1_hour, curated_time_change_policy, curated_checkin_late_cancel, curated_booking_no_edit | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_333 | games | `rag_llm` | missing keywords: VALORANT | curated_home_equipment_pc_zone, curated_about_members_dean, curated_games_pc, curated_rule_return_equipment | คำตอบ: มี Valora ในรายการเกมบน PC ที่ปรากฏในเว็บไซต์ https://esports.computing.psu.ac.th/ |
| v2_334 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_ps5_duration, curated_reservation_service_vr_duration | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) |
| v2_338 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_user_group_alias_general_adult, curated_cancel_1_hour, curated_booking_no_edit, curated_time_change_policy | คำตอบ: เปิด-ปิด วันจันกลงมือแบบภาษาบุคคลทั่วไปคือ "เปิด-ปิด วันจันกิ้มงอม" |
| v2_341 | games | `rag_llm` | missing keywords: VALORANT | curated_user_group_alias_general_adult, curated_home_equipment_pc_zone, curated_about_members_dean, curated_rule_return_equipment | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_342 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_pc_duration, curated_reservation_service_vr_duration, curated_reservation_service_ps5_duration, curated_reservation_service_nintendo_capacity | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) |
| v2_346 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_cancel_1_hour, curated_booking_no_edit, curated_time_change_policy, curated_checkin_late_cancel | คำตอบ: การจองและการยกเลิกต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง (SOURCE 1, SOURCE 4). หากต้องการเปลี่ยนแปลงข้อมูลหลังจากจอง, ต้องยกเลิกการจองผ่านอีเมลและจองใหม่อีกครั้งพร้อมแนบสลิปการโอนเงินเดิม (SOURCE 2). การเปลี่ยนแปลงเวลา... |
| v2_349 | games | `rag_llm` | missing keywords: VALORANT | curated_home_equipment_pc_zone, curated_about_members_dean, curated_games_pc, curated_rule_return_equipment | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_350 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_pc_duration, curated_reservation_service_ps5_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_vr_duration | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) |
| v2_354 | reservation | `rag_llm` | missing keywords: 13:00, 16:00, Maintenance | curated_time_change_policy, curated_booking_no_edit, curated_cancel_1_hour, curated_checkin_late_cancel | คำตอบ: ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_358 | reservation | `rag_direct_curated` | missing keywords: 30 นาที | curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_vr_duration, curated_reservation_service_ps5_duration | คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) |
| v2_360 | no_answer | `rag_llm` | missing keywords: ไม่พบข้อมูล | curated_damage_severe, curated_reservation_advance_time, curated_time_change_policy, reservation-studio-rules-002 | คำตอบ: ไม่มีการให้เช่าจอไปบ้านในระบบของศูนย์ esports studio. ผู้ใช้งานควรจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาที่จะใช้งานอย่างน้อย 1 ชั่วโมง โดยมีนโยบายเปลี่ยนแปลงเวลาใช้งานที่ต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้ |

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_v2_full.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_v2_full.jsonl`
