# Ground Truth Verbose Result

- Total: 20
- PASS: 20
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0228s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_competition_challenger_v2_verbose_20260704_175254.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_competition_challenger_v2_verbose_20260704_175254.md`

## Mode Summary
- `pipeline:rag_direct_curated`: 14
- `pipeline:competition_fact_card`: 6

## Route Summary
- `competition_rules`: 20
## 1. [PASS] ถูก

**คำถาม:** ในกติกา PSU Phuket cs2 2026 รับเฉพาะนักศึกษาแบบไหน เขียนไว้ยังไง

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s36_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s36_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: นักศึกษา, มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0252` sec

## 2. [PASS] ถูก

**คำถาม:** ถามแบบคนจะไปแข่งจริง: คนนอก PSU Phuket ลงแข่ง Counter Strike รายการนี้ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s38_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s38_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, นักศึกษา, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.027` sec

## 3. [PASS] ถูก

**คำถาม:** เคาเตอร์ แข่งทีมละกี่คน ขอคำตอบสั้นๆแต่ต้องอ้างอิงกติกา

**คำตอบ(จาก AI):**

คำตอบ: CS2 ต้องมีผู้เล่น 5 คนต่อทีม ดังนั้นถ้าเหลือ 4 คนยังไม่ครบตามกติกาทีม 5 คน
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_four_missing_challenger / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0161` sec

## 4. [PASS] ถูก

**คำถาม:** CS2 ต้องส่งผู้เล่นหลักกี่คน ถ้าผมเป็นผู้เข้าแข่งต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0188` sec

## 5. [PASS] ถูก

**คำถาม:** cs2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม สรุปให้ตรงประเด็นก่อน

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- หยุดเกมโดยไม่ได้รับอนุญาต
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- การด่าทอ/ใช้ความรุนแรงทางวาจา
- ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
- ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Steam, ห้าม, ดัดแปลง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0206` sec

## 6. [PASS] ถูก

**คำถาม:** รายการ Counter Strike ใช้เวอร์ชันเกมแบบไหน แบบตอบให้เอาไปบอกเพื่อนได้เลย

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- หยุดเกมโดยไม่ได้รับอนุญาต
- การพิมพ์แชทในเกมที่ไม่เหมาะสม
- การด่าทอ/ใช้ความรุนแรงทางวาจา
- การใช้บัค

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่าสุด, CS2, Steam | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.026` sec

## 7. [PASS] ถูก

**คำถาม:** ในกติกา ภาษาทางการของการแข่งขัน เคาเตอร์ คือภาษาอะไร เขียนไว้ยังไง

**คำตอบ(จาก AI):**

คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ภาษาไทย | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0268` sec

## 8. [PASS] ถูก

**คำถาม:** ถามแบบคนจะไปแข่งจริง: ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร

**คำตอบ(จาก AI):**

คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ภาษาไทย | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0234` sec

## 9. [PASS] ถูก

**คำถาม:** cs2 แข่งกี่วันและแข่งที่ไหน ขอคำตอบสั้นๆแต่ต้องอ้างอิงกติกา

**คำตอบ(จาก AI):**

คำตอบ: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 วัน, PSU Esports Studio, Phuket | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0213` sec

## 10. [PASS] ถูก

**คำถาม:** สถานที่จัด PSU Phuket Counter Strike 2026 คือที่ไหน ถ้าผมเป็นผู้เข้าแข่งต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

รายละเอียดที่เกี่ยวข้อง:
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU Esports Studio, Phuket | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0272` sec

## 11. [PASS] ถูก

**คำถาม:** เคาเตอร์ ใช้ช่องทางสื่อสารหลักอะไร สรุปให้ตรงประเด็นก่อน

**คำตอบ(จาก AI):**

คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Discord | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0209` sec

## 12. [PASS] ถูก

**คำถาม:** ผู้เข้าแข่ง CS2 ต้องใช้เซิร์ฟเวอร์ไหนในการสื่อสาร แบบตอบให้เอาไปบอกเพื่อนได้เลย

**คำตอบ(จาก AI):**

คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Discord, ศูนย์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0265` sec

## 13. [PASS] ถูก

**คำถาม:** ในกติกา cs2 เปลี่ยนสมาชิกทีมระหว่างทัวร์นาเมนต์ได้ไหม เขียนไว้ยังไง

**คำตอบ(จาก AI):**

คำตอบ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
- 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s11_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s11_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s18_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่มีการเปลี่ยนแปลง, สมาชิก | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0254` sec

## 14. [PASS] ถูก

**คำถาม:** ถามแบบคนจะไปแข่งจริง: หลังปิดรับสมัคร Counter Strike ลงทะเบียนผู้เล่นเพิ่มได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

รายละเอียดที่เกี่ยวข้อง:
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s12_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s12_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, ปิดรับสมัคร | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0295` sec

## 15. [PASS] ถูก

**คำถาม:** ถ้าผู้เล่น เคาเตอร์ ถอนตัวทีมจะเป็นยังไง ขอคำตอบสั้นๆแต่ต้องอ้างอิงกติกา

**คำตอบ(จาก AI):**

คำตอบ: ถ้าผู้เล่น CS2 ถอนตัว ทีมเสี่ยงถูกตัดสิทธิ์ตามเงื่อนไขของกติกา
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`round5_cs2_member_withdraw / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ถอนตัว, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0191` sec

## 16. [PASS] ถูก

**คำถาม:** ผู้เล่น CS2 เล่นให้สองทีมได้ไหม ถ้าผมเป็นผู้เข้าแข่งต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s14_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s14_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ทีมเดียว | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0243` sec

## 17. [PASS] ถูก

**คำถาม:** สายการแข่งขัน cs2 จะประกาศก่อนแข่งนานแค่ไหน สรุปให้ตรงประเด็นก่อน

**คำตอบ(จาก AI):**

คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s15_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่วงหน้า, 1 วัน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0241` sec

## 18. [PASS] ถูก

**คำถาม:** Counter Strike มาสายหรือไม่ยืนยันเข้าแข่งก่อนแมตช์เสี่ยงอะไร แบบตอบให้เอาไปบอกเพื่อนได้เลย

**คำตอบ(จาก AI):**

คำตอบ: CS2 หากมาสายหรือไม่ยืนยันเข้าแข่งขันก่อนแมตช์ ทีมเสี่ยงถูกตัดสิทธิ์

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`round5_cs2_late_may_disqualify / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มาสาย, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0201` sec

## 19. [PASS] ถูก

**คำถาม:** ในกติกา รูปแบบทัวร์นาเมนต์ เคาเตอร์ เป็นแบบไหน เขียนไว้ยังไง

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0179` sec

## 20. [PASS] ถูก

**คำถาม:** ถามแบบคนจะไปแข่งจริง: CS2 รอบรองกับรอบชิงแข่ง BO อะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รอบรอง, รอบชิง, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: challenger | variant: derived_natural_language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0158` sec
