# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-30

## Summary

- Total: 360
- PASS: 356
- FAIL: 4
- ERROR: 0
- Pass rate: 98.89%
- Average latency: 0.245s
- Keyword fail: 4
- Source fail: 1
- Answers containing `ไม่พบข้อมูล`: 27
- Chinese character leakage: 0

## Mode Distribution

- `rule_fast_path`: 155
- `deterministic_calculator`: 131
- `rag_direct_curated`: 50
- `rag_llm`: 24

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
| games | 26 | 26 | 100.00% |
| knowledge | 7 | 7 | 100.00% |
| no_answer | 26 | 26 | 100.00% |
| overview | 5 | 5 | 100.00% |
| rules | 23 | 23 | 100.00% |
| service_fee | 138 | 139 | 99.28% |
| reservation | 91 | 93 | 97.85% |
| penalty | 10 | 11 | 90.91% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 113 | 113 | 100.00% |
| multi_fact | 10 | 10 | 100.00% |
| no_answer | 34 | 34 | 100.00% |
| summary | 12 | 12 | 100.00% |
| fact | 169 | 172 | 98.26% |
| list | 18 | 19 | 94.74% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| hard | 90 | 90 | 100.00% |
| medium | 266 | 270 | 98.52% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| rule_fast_path | 155 | 155 | 100.00% |
| deterministic_calculator | 130 | 131 | 99.24% |
| rag_direct_curated | 48 | 50 | 96.00% |
| rag_llm | 23 | 24 | 95.83% |

## Failed Cases

| ID | Category | Mode | Problem | Retrieved IDs | Answer Short |
|---|---|---|---|---|---|
| v2_160 | service_fee | `rag_llm` | missing keywords: PlayStation 5, Nintendo Switch, Cockpit, VR; missing sources: service_fee | curated_reservation_service_pc_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_vr_duration, curated_reservation_service_ps5_duration | ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี |
| v2_179 | reservation | `rag_direct_curated` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่ | curated_booking_steps, curated_reservation_advance_time, curated_payment_10_minutes, curated_user_info_required | คำตอบ: - ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking... |
| v2_182 | reservation | `rag_direct_curated` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่ | curated_booking_steps, curated_reservation_advance_time, curated_payment_10_minutes, curated_user_info_required | คำตอบ: - ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking... |
| v2_246 | penalty | `deterministic_calculator` | missing keywords: ชดเชย, เต็มจำนวน | calculator_pc | คำตอบ: - ราคา PC: ยังไม่พบราคาค่าบริการ PC ในฐานข้อมูล/Service Fee 2026 ที่ดึงมา จึงยังไม่ควรคำนวณยอดเงินบาทแบบฟันธง - คำถามเป็นราคาแบบต่อรอบ/ต่อชั่วโมง จึงคิดเป็น 1 session = 1 ชั่วโมง - บริการ PC คิดเป็นรอบละ 60 นาที ด... |

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_v2_data_fix_final.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_v2_data_fix_final.jsonl`
