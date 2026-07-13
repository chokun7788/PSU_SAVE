# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 80
- PASS: 74
- FAIL: 6
- ERROR: 0
- Pass rate: 92.50%
- Average latency: 0.0237s
- P95 latency: 0.0380s
- Keyword fail: 6
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 41
- `pipeline:rag_direct_curated`: 39

## Route Category Distribution

- `competition_rules`: 79
- `general`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_cs2_004 | competition_rules | `competition_rules` | Discord | คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: lo... |
| competition_challenger_rov_001 | competition_rules | `general` | 15 นาที | คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ... |
| competition_challenger_rov_007 | competition_rules | `competition_rules` | รูน; พลังเสริม | คำตอบ: 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ รายละเอียดที่เกี่ยวข้อ... |
| competition_challenger_rov_010 | competition_rules | `competition_rules` | First Blood; 2 นาที | คำตอบ: 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม รายละเอียดที่เกี่ยวข้อง: - 4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งใ... |
| competition_challenger_rov_011 | competition_rules | `competition_rules` | First Blood; ห้าม; อนุญาต | คำตอบ: 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม รายละเอียดที่เกี่ยวข้อง: - 4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งใ... |
| competition_challenger_tekken8_012 | competition_rules | `competition_rules` | ผู้ดูแล | คำตอบ: * ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข รายละเอียดที่เกี่ยวข้อง: - คำตัดสินของกรรมการถือเป็นที่สิ้นสุด - กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรร... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v1_after_answer_filter_20260704.jsonl`
