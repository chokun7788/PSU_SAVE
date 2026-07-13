# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 80
- PASS: 74
- FAIL: 6
- ERROR: 0
- Pass rate: 92.50%
- Average latency: 0.0225s
- P95 latency: 0.0342s
- Keyword fail: 6
- Source fail: 1
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 42
- `pipeline:competition_fact_card`: 37
- `pipeline:games_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 78
- `games`: 1
- `general`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_cs2_010 | competition_rules | `competition_rules` | แมตช์ | คำตอบ: การใช้บัค รายละเอียดที่เกี่ยวข้อง: - 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ - 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ท... |
| competition_challenger_cs2_017 | competition_rules | `games` | ห้าม; เกลียดชัง; ศาสนา; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_challenger_cs2_019 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น รายละเอียดที่เกี่ยวข้อง: - 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง - 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีส... |
| competition_challenger_rov_014 | competition_rules | `competition_rules` | ปรับแพ้; ตัดสิทธิ์ | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_challenger_valorant_014 | competition_rules | `competition_rules` | ปิด | คำตอบ: VALORANT ต้องตั้งค่า Blood และ Bodies เป็น Off หลักฐานจากกติกา: - เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด อ้างอิงจากกติกา: VALORANT / PSU Ph... |
| competition_challenger_valorant_019 | competition_rules | `competition_rules` | 24 รอบแรก | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v1_after_challenger_v2_20260704.jsonl`
