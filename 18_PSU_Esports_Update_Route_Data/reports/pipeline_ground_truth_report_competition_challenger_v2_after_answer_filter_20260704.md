# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 369
- PASS: 355
- FAIL: 14
- ERROR: 0
- Pass rate: 96.21%
- Average latency: 0.0304s
- P95 latency: 0.0472s
- Keyword fail: 14
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 237
- `pipeline:rag_direct_curated`: 132

## Route Category Distribution

- `competition_rules`: 369

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_derived_009 | competition_rules | `competition_rules` | 1 วัน; PSU Esports Studio | คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026 |
| competition_challenger_v2_derived_011 | competition_rules | `competition_rules` | Discord | คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: lo... |
| competition_challenger_v2_derived_016 | competition_rules | `competition_rules` | ทีมเดียว | คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournam... |
| competition_challenger_v2_derived_021 | competition_rules | `competition_rules` | Competitive; 5v5 | คำตอบ: เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026 |
| competition_challenger_v2_derived_025 | competition_rules | `competition_rules` | 24 รอบ; 12 รอบ | คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/... |
| competition_challenger_v2_derived_042 | competition_rules | `competition_rules` | สคริปต์; มาโคร | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: - 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนกา... |
| competition_challenger_v2_derived_044 | competition_rules | `competition_rules` | โซเชียลมีเดีย | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: - 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นร... |
| competition_challenger_v2_derived_131 | competition_rules | `competition_rules` | KAY/O; ZERO/POINT; Texture | คำตอบ: * หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้ รายละเอียดที่เกี่ยวข้อง: - หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge - บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม... |
| competition_challenger_v2_derived_158 | competition_rules | `competition_rules` | อนุญาต; Assist | คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) รายละเอียดที่เกี่ยวข้อง: - แข่งขันแบบ ออฟไลน์ (Offline) - แข่งขันแบบ เดี่ยว (1v1) - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - ใช้เคร... |
| competition_challenger_v2_derived_167 | competition_rules | `competition_rules` | คำตัดสิน; กรรมการ | คำตอบ: * FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน รายละเอียดที่เกี่ยวข้อง: - ใช้เครื่องเกม PlayStation 5 - ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) - แข่งขันแบบ เดี่ยว (1v1) - หากเสมอกันที... |
| competition_challenger_v2_derived_188 | competition_rules | `competition_rules` | Discord | คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: lo... |
| competition_challenger_v2_derived_211 | competition_rules | `competition_rules` | รูน; พลังเสริม | คำตอบ: 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีก... |
| competition_challenger_v2_derived_248 | competition_rules | `competition_rules` | ห้าม; Cypher; Texture | คำตอบ: * Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้ รายละเอียดที่เกี่ยวข้อง: - Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทาง... |
| competition_challenger_v2_derived_261 | competition_rules | `competition_rules` | ผู้ดูแล; สิ้นสุด | คำตอบ: * ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v2_after_answer_filter_20260704.jsonl`
