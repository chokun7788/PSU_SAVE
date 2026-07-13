# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 228
- PASS: 223
- FAIL: 5
- ERROR: 0
- Pass rate: 97.81%
- Average latency: 0.0119s
- P95 latency: 0.0187s
- Keyword fail: 4
- Source fail: 0
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 228

## Route Category Distribution

- `competition_rules`: 228

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_v1_009 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3) หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3 อ้างอิงจากกติกา: Counter-Strike 2 / P... |
| competition_v1_011 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: CS2 Technical Pause ต่างจาก Tactical Timeout คือ Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ที... |
| competition_v1_046 | competition_rules | `competition_rules` | quality first sentence mismatch: ต่างกัน | คำตอบ: CS2 Technical Pause ต่างจาก Tactical Timeout คือ Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ที... |
| competition_v1_188 | competition_rules | `competition_rules` | 1v1; FT2; 60 วินาที | คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit... |
| competition_v1_222 | competition_rules | `competition_rules` | ไม่อนุญาต; Pause; แพ้ 1 Round | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_rules_v1_228_round_fix_20260703.jsonl`
