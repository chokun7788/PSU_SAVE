# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 369
- PASS: 363
- FAIL: 6
- ERROR: 0
- Pass rate: 98.37%
- Average latency: 0.0313s
- P95 latency: 0.0475s
- Keyword fail: 5
- Source fail: 4
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 234
- `pipeline:rag_direct_curated`: 132
- `pipeline:equipment_fast_path`: 2
- `pipeline:no_answer`: 1

## Route Category Distribution

- `competition_rules`: 366
- `games`: 1
- `general`: 1
- `contact`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_derived_216 | competition_rules | `games` | แจ้งทีมงาน; ดุลยพินิจ; กรรมการ; competition_rules_rov_blueket_2025_men | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| competition_challenger_v2_edge_005 | competition_rules | `competition_rules` | ไม่มีการเปลี่ยนแปลง; สมาชิก | คำตอบ: หยุดเกมโดยไม่ได้รับอนุญาต รายละเอียดที่เกี่ยวข้อง: - 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา - 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นไ... |
| competition_challenger_v2_edge_034 | competition_rules | `general` | เซิร์ฟเวอร์; แจ้งทีมงาน; competition_rules_rov_blueket_2025_men | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| competition_challenger_v2_edge_038 | competition_rules | `competition_rules` | quality first sentence mismatch: ต่างกัน | คำตอบ: RoV Pause ผิดมีโทษเป็นขั้น: ครั้งที่ 1 ตักเตือน, ครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง, และโทษรุนแรงอาจถึงปรับแพ้ หลักฐานจากกติกา: - เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรง... |
| competition_challenger_v2_edge_044 | competition_rules | `contact` | อาคาร; 5102A; competition_rules_rov_blueket_2025_men | PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us, https://esports.computing.psu.ac.th/ |
| competition_challenger_v2_edge_069 | competition_rules | `competition_rules` | หมดสิทธิ์; ตัวสำรอง; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v2_afterfix2_20260704.jsonl`
