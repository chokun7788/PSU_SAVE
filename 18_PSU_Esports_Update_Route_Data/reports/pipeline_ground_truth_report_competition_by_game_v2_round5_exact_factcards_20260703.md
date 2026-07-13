# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 184
- PASS: 174
- FAIL: 10
- ERROR: 0
- Pass rate: 94.57%
- Average latency: 0.0166s
- P95 latency: 0.0264s
- Keyword fail: 10
- Source fail: 2
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 119
- `pipeline:competition_fact_card`: 63
- `pipeline:games_fast_path`: 2

## Route Category Distribution

- `competition_rules`: 182
- `games`: 2

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_rov_v2_017 | competition_rules | `competition_rules` | ล่าช้า | คำตอบ: 4. ระเบียบและกติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 4.1. กติกาพื้นฐาน - 4.2. กติกาการแข่งขัน - 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง คร... |
| competition_rov_v2_035 | competition_rules | `competition_rules` | ครั้งที่ 2; เพิ่มสิทธิการแบนฮีโร่; 1 ครั้ง | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_rov_v2_036 | competition_rules | `competition_rules` | ครั้งที่ 3; เพิ่มสิทธิการแบนฮีโร่; 2 ครั้ง | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_rov_v2_038 | competition_rules | `competition_rules` | ไม่อนุญาต; Tablet; iPad | คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น รายละเอียดที่เกี่ยวข้อง: - 6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รั... |
| competition_rov_v2_042 | competition_rules | `competition_rules` | ไม่ตรงตามที่ลงทะเบียน; ปรับแพ้; ตัดสิทธิ์ | คำตอบ: · เวลา 8.00-8.30 ลงทะเบียน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_rov_v2_044 | competition_rules | `competition_rules` | ออฟไลน์; BO3 | คำตอบ: 2.1. PSU Esports Studio – Phuket (อาคาร 5 ชั้น 1) แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_valorant_v2_029 | competition_rules | `competition_rules` | Game-Breaking | คำตอบ: * Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้ รายละเอียดที่เกี่ยวข้อง: - หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที - Play Through Bug บั... |
| competition_valorant_v2_030 | competition_rules | `games` | ก่อน; ดาเมจ; ย้อนรอบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_032 | competition_rules | `games` | ผิด; ได้เปรียบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_047 | competition_rules | `competition_rules` | Agent; Abyss | คำตอบ: * การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่ รายละเอียดที่เกี่ยวข้อง: - แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive - เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_round5_exact_factcards_20260703.jsonl`
