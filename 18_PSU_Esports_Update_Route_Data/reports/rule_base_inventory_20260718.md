# Rule Base Inventory - 2026-07-18

## Loaded Rule Base

ระบบ rule matcher โหลด rule จากโฟลเดอร์นี้:

`18_PSU_Esports_Update_Route_Data/data/rules/*.jsonl`

ตัวโหลดอยู่ที่:

`18_PSU_Esports_Update_Route_Data/app/rules/loader.py`

โหลดทุกไฟล์ `.jsonl` ใน `data/rules` แล้ว sort ตาม `priority` จากมากไปน้อย

## Summary

- Total rule files: 8
- Total rules: 78
- Total patterns: 505
- Total intents: 78

## By File

| File | Category | Rules | Patterns | Intents | Priority Range |
|---|---:|---:|---:|---:|---:|
| `contact_rules.jsonl` | contact | 4 | 15 | 4 | 95-100 |
| `equipment_rules.jsonl` | equipment | 1 | 9 | 1 | 128 |
| `games_rules.jsonl` | games | 10 | 78 | 10 | 100-126 |
| `misc_rules.jsonl` | rules | 9 | 60 | 9 | 100-137 |
| `no_answer_rules.jsonl` | no_answer | 20 | 89 | 20 | 120-150 |
| `overview_rules.jsonl` | overview | 3 | 16 | 3 | 95-126 |
| `penalty_rules.jsonl` | penalty | 5 | 30 | 5 | 100-122 |
| `reservation_rules.jsonl` | reservation | 26 | 208 | 26 | 95-136 |

## Category Counts

- `reservation`: 26 rules
- `no_answer`: 20 rules
- `games`: 10 rules
- `rules`: 9 rules
- `penalty`: 5 rules
- `contact`: 4 rules
- `overview`: 3 rules
- `equipment`: 1 rule

## Important Note

คำว่า rule base ในระบบนี้มี 2 ชั้นที่ควรแยกกัน:

1. Rule matcher จริง: `data/rules/*.jsonl`
2. Deterministic fast path / curated facts: อยู่ใน code และ data อื่น เช่น
   - `app/runtime/fast_answer.py`
   - `data/curated/*.jsonl`
   - `data/competition_rules/*.jsonl`
   - `data/curated/game_control_facts.jsonl`

ดังนั้นถ้าถามว่า "rule base ที่ matcher โหลดจริง ๆ มีอะไร" ให้ดู `data/rules`.
แต่ถ้าถามว่า "ระบบตอบแบบ rule/fast ได้จากอะไรบ้าง" ต้องดูทั้ง `data/rules`, `fast_answer.py`, และ curated/fact data ประกอบด้วย
