# Fast Ground Truth Evaluation - PSU Esports Update Runtime

วันที่: 2026-07-01

## Summary

- Total: 360
- PASS: 348
- FAIL: 12
- ERROR: 0
- Pass rate: 96.67%
- Average latency: 0.0001s
- P95 latency: 0.0002s
- Keyword fail: 12
- Source fail: 8

## Mode Distribution

- `deterministic_calculator_fast`: 137
- `schedule_fast_path`: 47
- `games_fast_path`: 32
- `no_answer_fast`: 26
- `rules_fast_path`: 21
- `booking_fast_path`: 20
- `checkin_fast_path`: 13
- `payment_fast_path`: 12
- `penalty_fast_path`: 12
- `contact_fast_path`: 10
- `knowledge_fast_path`: 6
- `equipment_fast_path`: 5
- `overview_fast_path`: 5
- `news_fast_path`: 5
- `members_fast_path`: 5
- `mixed_rules_fast`: 2
- `rule_fast_path`: 1
- `mixed_reservation_fast`: 1

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| games | 26 | 26 | 100.00% |
| no_answer | 25 | 25 | 100.00% |
| overview | 5 | 5 | 100.00% |
| penalty | 11 | 11 | 100.00% |
| rules | 23 | 23 | 100.00% |
| service_fee | 137 | 139 | 98.56% |
| reservation | 90 | 94 | 95.74% |
| knowledge | 6 | 7 | 85.71% |
| equipment | 5 | 10 | 50.00% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| no_answer | 33 | 33 | 100.00% |
| calculation | 112 | 113 | 99.12% |
| fact | 167 | 173 | 96.53% |
| list | 18 | 19 | 94.74% |
| summary | 11 | 12 | 91.67% |
| multi_fact | 7 | 10 | 70.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| medium | 263 | 271 | 97.05% |
| hard | 85 | 89 | 95.51% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| contact_fast_path | 10 | 10 | 100.00% |
| deterministic_calculator_fast | 137 | 137 | 100.00% |
| equipment_fast_path | 5 | 5 | 100.00% |
| knowledge_fast_path | 6 | 6 | 100.00% |
| members_fast_path | 5 | 5 | 100.00% |
| mixed_reservation_fast | 1 | 1 | 100.00% |
| mixed_rules_fast | 2 | 2 | 100.00% |
| news_fast_path | 5 | 5 | 100.00% |
| overview_fast_path | 5 | 5 | 100.00% |
| rule_fast_path | 1 | 1 | 100.00% |
| rules_fast_path | 21 | 21 | 100.00% |
| schedule_fast_path | 47 | 47 | 100.00% |
| no_answer_fast | 25 | 26 | 96.15% |
| booking_fast_path | 19 | 20 | 95.00% |
| checkin_fast_path | 12 | 13 | 92.31% |
| penalty_fast_path | 11 | 12 | 91.67% |
| payment_fast_path | 10 | 12 | 83.33% |
| games_fast_path | 26 | 32 | 81.25% |

## Failed Cases

| ID | Category | Mode | Problem | Answer Short |
|---|---|---|---|---|
| v2_159 | service_fee | `no_answer_fast` | missing keywords: PlayStation 5, Nintendo Switch, Cockpit, VR; missing sources: service_fee | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_180 | reservation | `payment_fast_path` | missing keywords: 1 ชั่วโมง, สลิป | หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่ |
| v2_225 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Cockpit ใช้เล่นเกม Gran Turismo 7 |
| v2_226 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Cockpit ใช้เล่นเกม Gran Turismo 7 |
| v2_227 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ |
| v2_228 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 |
| v2_229 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | VR มีเกม Beat Saber และ Horizon Call of the Mountain |
| v2_265 | knowledge | `penalty_fast_path` | missing keywords: Spacewar, 1972; missing sources: Knowledge | หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน |
| v2_299 | reservation | `payment_fast_path` | missing keywords: ไม่มีการคืนเงิน | หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่ |
| v2_300 | reservation | `checkin_fast_path` | missing keywords: 1 ชั่วโมง, ยกเลิก | เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง |
| v2_301 | reservation | `booking_fast_path` | missing keywords: 10 นาที | การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions |
| v2_307 | service_fee | `games_fast_path` | missing keywords: บาท; missing sources: service_fee | VR มีเกม Beat Saber และ Horizon Call of the Mountain |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\fast_ground_truth_results_v2_fast_update_round2_20260701.jsonl`
