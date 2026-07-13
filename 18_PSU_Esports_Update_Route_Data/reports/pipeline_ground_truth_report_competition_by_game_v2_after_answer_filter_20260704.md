# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 184
- PASS: 175
- FAIL: 9
- ERROR: 0
- Pass rate: 95.11%
- Average latency: 0.0261s
- P95 latency: 0.0383s
- Keyword fail: 9
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 105
- `pipeline:competition_fact_card`: 79

## Route Category Distribution

- `competition_rules`: 184

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_cs2_v2_011 | competition_rules | `competition_rules` | Discord | คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: lo... |
| competition_cs2_v2_015 | competition_rules | `competition_rules` | ถอนตัว; ตัดสิทธิ์ | คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournam... |
| competition_cs2_v2_018 | competition_rules | `competition_rules` | มาสาย; ตัดสิทธิ์ | คำตอบ: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_... |
| competition_cs2_v2_025 | competition_rules | `competition_rules` | 24 รอบ; 12 รอบ | คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/... |
| competition_cs2_v2_042 | competition_rules | `competition_rules` | สคริปต์; มาโคร | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_... |
| competition_cs2_v2_044 | competition_rules | `competition_rules` | โซเชียลมีเดีย | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: - 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นร... |
| competition_rov_v2_027 | competition_rules | `competition_rules` | First Blood; อนุญาต; คู่แข่ง; กรรมการ | คำตอบ: 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม รายละเอียดที่เกี่ยวข้อง: - 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแ... |
| competition_valorant_v2_038 | competition_rules | `competition_rules` | Round Rollback; ช่องโหว่ | คำตอบ: * ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์ รายละเอียดที่เกี่ยวข้อง: - ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 20... |
| competition_tekken8_v2_024 | competition_rules | `competition_rules` | ปรับเปลี่ยนกฎ | คำตอบ: * หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที รายละเอียดที่เกี่ยวข้อง: - หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า - ในกรณีเกิดข้อโต้แย้งหรือการประท้วง... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_after_answer_filter_20260704.jsonl`
