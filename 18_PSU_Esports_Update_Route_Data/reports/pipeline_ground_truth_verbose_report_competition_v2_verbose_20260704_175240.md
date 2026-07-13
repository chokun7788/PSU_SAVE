# Ground Truth Verbose Result

- Total: 184
- PASS: 184
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0183s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_competition_v2_verbose_20260704_175240.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_competition_v2_verbose_20260704_175240.md`

## Mode Summary
- `pipeline:rag_direct_curated`: 105
- `pipeline:competition_fact_card`: 79

## Route Summary
- `competition_rules`: 184
## 1. [PASS] ถูก

**คำถาม:** PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: นักศึกษา, มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: eligibility

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0237` sec

## 2. [PASS] ถูก

**คำถาม:** คนนอก PSU Phuket ลงแข่ง CS2 รายการนี้ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s34_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เฉพาะ, นักศึกษา, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: eligibility

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0235` sec

## 3. [PASS] ถูก

**คำถาม:** CS2 แข่งทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0078` sec

## 4. [PASS] ถูก

**คำถาม:** Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0114` sec

## 5. [PASS] ถูก

**คำถาม:** CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s36_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s36_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Steam, ห้าม, ดัดแปลง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_version

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0204` sec

## 6. [PASS] ถูก

**คำถาม:** รายการ CS2 ใช้เวอร์ชันเกมแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- รายการ PSU Phuket CS2 2026 Tournament

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่าสุด, CS2, Steam | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_version

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0177` sec

## 7. [PASS] ถูก

**คำถาม:** ภาษาทางการของการแข่งขัน CS2 คือภาษาอะไร

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

ต้องมีคำสำคัญ: ภาษาไทย | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0252` sec

## 8. [PASS] ถูก

**คำถาม:** ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร

**คำตอบ(จาก AI):**

คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ภาษาไทย | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: language

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0214` sec

## 9. [PASS] ถูก

**คำถาม:** CS2 แข่งกี่วันและแข่งที่ไหน

**คำตอบ(จาก AI):**

คำตอบ: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 7. พื้นที่การแข่งขันและกฎระเบียบ

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s49_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s49_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 วัน, PSU Esports Studio, Phuket | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_location

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0155` sec

## 10. [PASS] ถูก

**คำถาม:** สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน

**คำตอบ(จาก AI):**

คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

รายละเอียดที่เกี่ยวข้อง:
- 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s26_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s26_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s57_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s57_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU Esports Studio, Phuket | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_location

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.021` sec

## 11. [PASS] ถูก

**คำถาม:** CS2 ใช้ช่องทางสื่อสารหลักอะไร

**คำตอบ(จาก AI):**

คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Discord | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: communication

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0161` sec

## 12. [PASS] ถูก

**คำถาม:** ผู้เข้าแข่ง CS2 ต้องใช้เซิร์ฟเวอร์ไหนในการสื่อสาร

**คำตอบ(จาก AI):**

คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s15_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Discord, ศูนย์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: communication

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0213` sec

## 13. [PASS] ถูก

**คำถาม:** CS2 เปลี่ยนสมาชิกทีมระหว่างทัวร์นาเมนต์ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s11_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s11_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s18_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s23_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s23_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่มีการเปลี่ยนแปลง, สมาชิก | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: roster_change

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0185` sec

## 14. [PASS] ถูก

**คำถาม:** หลังปิดรับสมัคร CS2 ลงทะเบียนผู้เล่นเพิ่มได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s12_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s12_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, ปิดรับสมัคร | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: registration

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0209` sec

## 15. [PASS] ถูก

**คำถาม:** ถ้าผู้เล่น CS2 ถอนตัวทีมจะเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s13_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s13_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ถอนตัว, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: eligibility

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0203` sec

## 16. [PASS] ถูก

**คำถาม:** ผู้เล่น CS2 เล่นให้สองทีมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- 2. คุณสมบัติของทีมและผู้เล่น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s14_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s14_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s16_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s16_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ทีมเดียว | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: eligibility

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.019` sec

## 17. [PASS] ถูก

**คำถาม:** สายการแข่งขัน CS2 จะประกาศก่อนแข่งนานแค่ไหน

**คำตอบ(จาก AI):**

คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 7. พื้นที่การแข่งขันและกฎระเบียบ

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s15_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s49_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s49_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่วงหน้า, 1 วัน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0239` sec

## 18. [PASS] ถูก

**คำถาม:** CS2 มาสายหรือไม่ยืนยันเข้าแข่งก่อนแมตช์เสี่ยงอะไร

**คำตอบ(จาก AI):**

คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s15_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: มาสาย, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0194` sec

## 19. [PASS] ถูก

**คำถาม:** รูปแบบทัวร์นาเมนต์ CS2 เป็นแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0128` sec

## 20. [PASS] ถูก

**คำถาม:** CS2 รอบรองกับรอบชิงแข่ง BO อะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รอบรอง, รอบชิง, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0157` sec

## 21. [PASS] ถูก

**คำถาม:** โหมดในเกม CS2 ใช้โหมดอะไร

**คำตอบ(จาก AI):**

คำตอบ: 1. โหมด Competitive (5v5)

รายละเอียดที่เกี่ยวข้อง:
- 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด
- 2. การตั้งค่าในเกม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s23_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s23_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s22_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s22_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Competitive, 5v5 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.02` sec

## 22. [PASS] ถูก

**คำถาม:** CS2 เวลาต่อรอบกับ Freeze time เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที

รายละเอียดที่เกี่ยวข้อง:
- 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s24_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s24_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s34_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1:55, 15 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0282` sec

## 23. [PASS] ถูก

**คำถาม:** CS2 เงินเริ่มต้นกับเวลาระเบิดตั้งไว้เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

รายละเอียดที่เกี่ยวข้อง:
- 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s25_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s25_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: $800, 40 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.019` sec

## 24. [PASS] ถูก

**คำถาม:** CS2 ชนะกี่รอบก่อนถึงชนะในแผนที่

**คำตอบ(จาก AI):**

คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s26_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s26_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s21_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s21_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13 รอบ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0169` sec

## 25. [PASS] ถูก

**คำถาม:** CS2 เล่นสูงสุดกี่รอบก่อน overtime

**คำตอบ(จาก AI):**

คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s26_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s26_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 24 รอบ, 12 รอบ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0186` sec

## 26. [PASS] ถูก

**คำถาม:** CS2 overtime เล่นยังไง

**คำตอบ(จาก AI):**

คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ฝั่งละ 3 รอบ, 4 ใน 6, $10,000 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0178` sec

## 27. [PASS] ถูก

**คำถาม:** CS2 ต่อเวลาได้จำกัดกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s34_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s24_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s24_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่จำกัด | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0167` sec

## 28. [PASS] ถูก

**คำถาม:** CS2 map pool มีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0139` sec

## 29. [PASS] ถูก

**คำถาม:** CS2 มี Mirage กับ Nuke ในแผนที่แข่งไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Mirage, Nuke | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0173` sec

## 30. [PASS] ถูก

**คำถาม:** CS2 เลือกแผนที่ผ่านอะไร

**คำตอบ(จาก AI):**

คำตอบ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG

รายละเอียดที่เกี่ยวข้อง:
- 3. แผนที่ในการแข่งขัน
- 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s31_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s31_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s28_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s28_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s37_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s37_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: MAPBAN.GG | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0171` sec

## 31. [PASS] ถูก

**คำถาม:** CS2 เลือกฝั่งด้วยวิธีไหน

**คำตอบ(จาก AI):**

คำตอบ: 2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง

รายละเอียดที่เกี่ยวข้อง:
- 1. การเลือกแผนที่ ใช้ MAPBAN.GG
- 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s32_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s32_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s31_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s31_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s26_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s26_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ดวลมีด, เลือกฝั่ง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: side_selection

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0181` sec

## 32. [PASS] ถูก

**คำถาม:** CS2 technical pause ขอได้กี่ครั้งและนานเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 2 ครั้ง, 10 นาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0153` sec

## 33. [PASS] ถูก

**คำถาม:** CS2 เครื่องมีปัญหาต้องแจ้งใครตอน technical pause

**คำตอบ(จาก AI):**

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s33_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s33_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s57_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s57_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: กรรมการ, ทันที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0217` sec

## 34. [PASS] ถูก

**คำถาม:** CS2 tactical timeout ได้กี่ครั้ง ครั้งละกี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0161` sec

## 35. [PASS] ถูก

**คำถาม:** CS2 ขอเวลานอกใช้ได้ช่วงไหน

**คำตอบ(จาก AI):**

คำตอบ: CS2 Tactical Timeout ใช้ได้ในช่วง Freeze time

หลักฐานจากกติกา:
- เอกสารระบุการขอเวลานอกทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_tactical_timeout_freeze_time / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Freeze time | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0103` sec

## 36. [PASS] ถูก

**คำถาม:** CS2 ใช้บัคแผนที่หรือ Engine ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- การใช้บัค
- หยุดเกมโดยไม่ได้รับอนุญาต
- 1. การเลือกแผนที่ ใช้ MAPBAN.GG
- การพิมพ์แชทในเกมที่ไม่เหมาะสม
- การด่าทอ/ใช้ความรุนแรงทางวาจา

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s37_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s37_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s31_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s31_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, บัค, ปรับแพ้ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.025` sec

## 37. [PASS] ถูก

**คำถาม:** CS2 ดูสตรีมสดระหว่างแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 ห้ามผู้เล่นดูสตรีมสดระหว่างแมตช์ เพราะเป็นการได้ข้อมูลนอกเกมและเสี่ยงผิดกติกา

หลักฐานจากกติกา:
- เอกสารระบุห้ามดูสตรีมสดระหว่างการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_stream_during_match_challenger / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, สตรีม | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0096` sec

## 38. [PASS] ถูก

**คำถาม:** CS2 พฤติกรรมเหยียดหรือวาจาสร้างความเกลียดชังผิดกติกาไหม

**คำตอบ(จาก AI):**

คำตอบ: ห้ามพฤติกรรมก้าวร้าวและวาจาสร้างความเกลียดชัง เช่น การเหยียดเชื้อชาติหรือศาสนา

หลักฐานจากกติกา:
- เอกสารระบุมารยาทผู้เล่นว่าห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง และการกระทำที่ไม่มีน้ำใจนักกีฬา

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_hate_speech_forbidden / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s36_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, เกลียดชัง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0129` sec

## 39. [PASS] ถูก

**คำถาม:** CS2 นำคีย์บอร์ดเมาส์ส่วนตัวไปเองได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

รายละเอียดที่เกี่ยวข้อง:
- 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s42_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s42_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: คีย์บอร์ด, เมาส์, มาเองได้ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0188` sec

## 40. [PASS] ถูก

**คำถาม:** CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้บ้าง

**คำตอบ(จาก AI):**

คำตอบ: 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้

รายละเอียดที่เกี่ยวข้อง:
- 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง
- 6. อุปกรณ์และการตั้งค่าเกม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s43_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s43_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s42_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s42_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s39_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s39_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PC, จอภาพ, โต๊ะ, เก้าอี้ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.016` sec

## 41. [PASS] ถูก

**คำถาม:** CS2 ปรับ crosshair หรือ resolution ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Crosshair, Resolution, Brightness | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0238` sec

## 42. [PASS] ถูก

**คำถาม:** CS2 ใช้ macro หรือ script ได้หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s46_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s46_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, สคริปต์, มาโคร | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0233` sec

## 43. [PASS] ถูก

**คำถาม:** CS2 ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

รายละเอียดที่เกี่ยวข้อง:
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- 6. อุปกรณ์และการตั้งค่าเกม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s47_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s47_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s39_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s39_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ติดตั้งโปรแกรม | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0179` sec

## 44. [PASS] ถูก

**คำถาม:** CS2 เข้าโซเชียลบนคอมแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
- 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s48_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s48_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, โซเชียลมีเดีย | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0169` sec

## 45. [PASS] ถูก

**คำถาม:** CS2 ช่วงเตรียมตัวมีคนในพื้นที่ได้ไม่เกินกี่คน

**คำตอบ(จาก AI):**

คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
- 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- 1. โหมด Competitive (5v5)

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s18_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s23_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s23_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่เกิน 6 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0186` sec

## 46. [PASS] ถูก

**คำถาม:** CS2 เอามือถือหรือ smart watch เข้าพื้นที่แข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
- 7. พื้นที่การแข่งขันและกฎระเบียบ
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s49_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s49_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0251` sec

## 47. [PASS] ถูก

**คำถาม:** CS2 หัวหน้าทีมนำเอกสารเข้าไปได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: หัวหน้าทีม, เอกสาร, กรรมการ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.018` sec

## 48. [PASS] ถูก

**คำถาม:** CS2 อนุญาตอาหารหรือเครื่องดื่มอะไรในพื้นที่แข่ง

**คำตอบ(จาก AI):**

คำตอบ: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s53_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s53_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s39_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s39_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: น้ำดื่ม, ปิดสนิท, หมากฝรั่ง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.017` sec

## 49. [PASS] ถูก

**คำถาม:** Blueket Games RoV แข่งวันไหน

**คำตอบ(จาก AI):**

คำตอบ: 1.1. แข่งขันออฟไลน์ วันที่ 11 กันยายน 2568

รายละเอียดที่เกี่ยวข้อง:
- กติกาการแข่งขัน Blueket Games 2025
- เวลา 8.30-8.40 แบ่งสายการแข่งขัน
- 1. กำหนดการแข่งขัน
- เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s01_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 11 กันยายน 2568 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0193` sec

## 50. [PASS] ถูก

**คำถาม:** RoV ลงทะเบียนช่วงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 8.00-8.30 ลงทะเบียน

รายละเอียดที่เกี่ยวข้อง:
- เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
- เวลา 8.30-8.40 แบ่งสายการแข่งขัน
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 8.00, 8.30 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0175` sec

## 51. [PASS] ถูก

**คำถาม:** RoV แบ่งสายการแข่งขันกี่โมง

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 8.30-8.40 แบ่งสายการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
- เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
- เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
- เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 8.30, 8.40 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0204` sec

## 52. [PASS] ถูก

**คำถาม:** RoV รอบ 5 ทีมแข่งช่วงเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ: RoV รอบ 5 ทีมแข่งขันเวลา 8.40-10.00 น. และแข่งแบบ BO3

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`round5_rov_five_team_round / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 8.40, 10.00, BO3 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0182` sec

## 53. [PASS] ถูก

**คำถาม:** RoV รอบรองคู่ที่ 1 เริ่มประมาณกี่โมง

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3

รายละเอียดที่เกี่ยวข้อง:
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
- เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10.00, 11.30 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0252` sec

## 54. [PASS] ถูก

**คำถาม:** RoV รอบรองคู่ที่ 2 อยู่ช่วงเวลาไหน

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3

รายละเอียดที่เกี่ยวข้อง:
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
- เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
- เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3
- เวลา 8.30-8.40 แบ่งสายการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 12.30, 14.00 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0239` sec

## 55. [PASS] ถูก

**คำถาม:** RoV รอบชิงอันดับ 3 แข่งกี่โมงถึงกี่โมง

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3

รายละเอียดที่เกี่ยวข้อง:
- เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3
- เวลา 8.30-8.40 แบ่งสายการแข่งขัน
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
- เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 14.00, 15.30 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0294` sec

## 56. [PASS] ถูก

**คำถาม:** RoV รอบชิงชนะเลิศแข่งช่วงไหน

**คำตอบ(จาก AI):**

คำตอบ: · เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3

รายละเอียดที่เกี่ยวข้อง:
- เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3
- เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
- เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
- เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
- เวลา 8.30-8.40 แบ่งสายการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s03_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15.30, 17.00 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0212` sec

## 57. [PASS] ถูก

**คำถาม:** RoV แข่งที่อาคารไหนของ PSU Esports Studio Phuket

**คำตอบ(จาก AI):**

คำตอบ: RoV จัดที่ PSU Esports Studio - Phuket อาคาร 5102A หรืออาคาร 5 ชั้น 1

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`round5_rov_location / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อาคาร 5, ชั้น 1 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: schedule_location

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0184` sec

## 58. [PASS] ถูก

**คำถาม:** RoV แข่งออนไลน์หรือออฟไลน์

**คำตอบ(จาก AI):**

คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ

หลักฐานจากกติกา:
- เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_format_bo3_all_rounds / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ออฟไลน์ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0147` sec

## 59. [PASS] ถูก

**คำถาม:** แข่ง ROV ต้องเล่นกี่เกม

**คำตอบ(จาก AI):**

คำตอบ: RoV รายการนี้แข่ง Best of 3 (BO3) ทุกรอบ จึงต้องชนะให้ครบ 2 เกมก่อน

หลักฐานจากกติกา:
- เอกสารรูปแบบการแข่งขันระบุ Best of 3 (BO3) ทุกรอบ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_format_bo3_challenger / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: BO3, ทุกรอบ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 60. [PASS] ถูก

**คำถาม:** RoV รายการนี้เป็น Best of 3 ทุกด่านไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV แข่ง Best of 3 (BO3) ทุกรอบ

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`round5_rov_format_bo3 / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Best of 3, ทุกรอบ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0208` sec

## 61. [PASS] ถูก

**คำถาม:** RoV เกมแรกใครได้ฝั่งสีน้ำเงิน

**คำตอบ(จาก AI):**

คำตอบ: 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

รายละเอียดที่เกี่ยวข้อง:
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
- 4.5.6.การหยุดพักเกมโดยผู้เข้าแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s01_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ด้านบน, สายการแข่งขัน, สีน้ำเงิน | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: side_selection

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0183` sec

## 62. [PASS] ถูก

**คำถาม:** RoV เกมถัดไปใครเลือกฝั่ง

**คำตอบ(จาก AI):**

คำตอบ: 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

รายละเอียดที่เกี่ยวข้อง:
- 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick
- 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s01_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ผู้ที่แพ้, เลือกฝั่ง | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: side_selection

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0172` sec

## 63. [PASS] ถูก

**คำถาม:** กรรมการ RoV แจ้งอะไรให้ทีมเข้าห้องแข่ง

**คำตอบ(จาก AI):**

คำตอบ: 4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้

รายละเอียดที่เกี่ยวข้อง:
- 4. ระเบียบและกติกาการแข่งขัน
- 4.2. กติกาการแข่งขัน
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
- 4.2.4.ในการแข่งขัน ผู้เข้าแข่งขันทุกคนสามารถเลือกเล่นฮีโร่ได้ทั้งหมด
- 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s08_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s08_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: หมายเลขห้อง | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: match_process

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0162` sec

## 64. [PASS] ถูก

**คำถาม:** RoV มาสายเกิน 15 นาทีเป็นอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0168` sec

## 65. [PASS] ถูก

**คำถาม:** กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง

**คำตอบ(จาก AI):**

คำตอบ: RoV หากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

หลักฐานจากกติกา:
- เอกสารข้อ 4.1.4 ระบุว่าหากเริ่มการแข่งขันช้าเกินเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้ทันที

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_delay_wording / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่าช้า, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0185` sec

## 66. [PASS] ถูก

**คำถาม:** RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว

**คำตอบ(จาก AI):**

คำตอบ: 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)

รายละเอียดที่เกี่ยวข้อง:
- 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick
- 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
- 6.1.5.ห้ามมิให้ผู้เข้าแข่งขันเสพ ค้า หรือดำเนินการใด ๆ อันเกี่ยวกับยาเสพติด บุหรี่ และอาวุธ และอื่น ๆ ที่ต้องห้ามตามกฎหมายการแข่งขันทันที
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลักฐานและยุติการแข่งขันในทันที แต่หากมีการแข่งขันจนจบเกม จะถือว่าทั้งสองทีมยินยอมให้เกิดการแข่งขันขึ้น ทางทีมงานจะไม่รับฟังข้อโต้แย้งใด ๆ ทั้งสิ้น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s08_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 18 ตัว | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: hero_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0186` sec

## 67. [PASS] ถูก

**คำถาม:** RoV ใช้ระบบแบนเลือกฮีโร่แบบไหน

**คำตอบ(จาก AI):**

คำตอบ: 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick

รายละเอียดที่เกี่ยวข้อง:
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
- 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
- 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น
- 4.6.3.2. ครั้งที่ 2: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 1 ครั้ง
- 4.6.3.3. ครั้งที่ 3: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 2 ครั้ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s08_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s08_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Global Ban/Pick | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: hero_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0176` sec

## 68. [PASS] ถูก

**คำถาม:** RoV ใส่รูนและพลังเสริมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ

รายละเอียดที่เกี่ยวข้อง:
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รูน, พลังเสริม, ตามความต้องการ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: hero_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0195` sec

## 69. [PASS] ถูก

**คำถาม:** RoV เลือกฮีโร่ซ้ำได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี

รายละเอียดที่เกี่ยวข้อง:
- 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick
- 4.2.4.ในการแข่งขัน ผู้เข้าแข่งขันทุกคนสามารถเลือกเล่นฮีโร่ได้ทั้งหมด
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ฮีโร่ซ้ำ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: hero_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0179` sec

## 70. [PASS] ถูก

**คำถาม:** RoV ใช้สกินพิเศษได้หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0136` sec

## 71. [PASS] ถูก

**คำถาม:** RoV แต่ละทีม pause ได้กี่ครั้ง ครั้งละเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0232` sec

## 72. [PASS] ถูก

**คำถาม:** RoV ถ้า pause เกิน 1 นาทีอีกทีมทำอะไรได้

**คำตอบ(จาก AI):**

คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ

รายละเอียดที่เกี่ยวข้อง:
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
- 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม
- 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Resume | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0255` sec

## 73. [PASS] ถูก

**คำถาม:** RoV หลุดเพราะเน็ตล่มหรือเซิร์ฟเวอร์พังต้องทำยังไง

**คำตอบ(จาก AI):**

คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่

รายละเอียดที่เกี่ยวข้อง:
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
- 4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
- 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: แจ้งทีมงาน, ดุลยพินิจ, กรรมการ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.02` sec

## 74. [PASS] ถูก

**คำถาม:** RoV ขอเริ่มเกมใหม่ได้ตอนไหนก่อน First Blood

**คำตอบ(จาก AI):**

คำตอบ: 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่

รายละเอียดที่เกี่ยวข้อง:
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
- 4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
- 4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที, เริ่มเกมใหม่ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0243` sec

## 75. [PASS] ถูก

**คำถาม:** RoV ถ้าเกิด First Blood แล้วขอ remake ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ

รายละเอียดที่เกี่ยวข้อง:
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น
- 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, อนุญาต, คู่แข่ง, กรรมการ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0295` sec

## 76. [PASS] ถูก

**คำถาม:** RoV เจตนากด pause ก่อกวนโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: 4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
- 5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที
- 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น
- 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s07_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้, ตัดสิทธิ์ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0223` sec

## 77. [PASS] ถูก

**คำถาม:** RoV พักหลังจบทุกสองเกมกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม

รายละเอียดที่เกี่ยวข้อง:
- 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
- 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
- 4.6.2.2. ห้ามมิให้ผู้เข้าร่วมการแข่งขันพูดคุย ติดต่อสื่อสาร หรือดำเนินการใดๆ อันเป็นการสื่อสารในระหว่างการหยุดพักเกม
- 4.5. การหยุดพักเกมในการแข่งขัน
- 4.5.1.การหยุดพักเกมทั่วไป

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: break_time

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0155` sec

## 78. [PASS] ถูก

**คำถาม:** RoV ไม่กลับมาหลังเวลาพักที่กำหนดเสี่ยงอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV หากไม่กลับมาภายในเวลาพักที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่งขัน

หลักฐานจากกติกา:
- เอกสารข้อ 4.4.2 ระบุว่าหากผู้เข้าแข่งขันไม่กลับมาภายในเวลาที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_break_absent_forfeit / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับ, แพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: break_time

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.015` sec

## 79. [PASS] ถูก

**คำถาม:** RoV เกมหยุดเกิน 10 นาทีทีมงานทำอะไรได้

**คำตอบ(จาก AI):**

คำตอบ: 4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งให้หยุดพักเกมดังกล่าว และให้ผู้เข้าแข่งขันกลับเข้าสู่การแข่งขันใหม่อีกครั้งภายหลังจากผู้เข้าแข่งขันที่ไม่ได้เชื่อมต่อได้กลับเข้ามาในเกมแล้ว

รายละเอียดที่เกี่ยวข้อง:
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.5.5.การหลุดการเชื่อมต่อโดยไม่เจตนา

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที, เริ่มเกมใหม่ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0219` sec

## 80. [PASS] ถูก

**คำถาม:** RoV เครื่องร้อนพักได้กี่นาที

**คำตอบ(จาก AI):**

คำตอบ: 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม

รายละเอียดที่เกี่ยวข้อง:
- 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม
- 4.6.1.การหยุดพักเกมอันเนื่องมากจากปัญหาเครื่องร้อนของอุปกรณ์พกพา
- 4.6.2.2. ห้ามมิให้ผู้เข้าร่วมการแข่งขันพูดคุย ติดต่อสื่อสาร หรือดำเนินการใดๆ อันเป็นการสื่อสารในระหว่างการหยุดพักเกม
- 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เครื่องร้อน, 5 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0194` sec

## 81. [PASS] ถูก

**คำถาม:** RoV ระหว่าง pause ผู้เล่นคุยกันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ระหว่าง Pause ห้ามผู้เล่นสื่อสารกันโดยไม่ได้รับอนุญาตจากผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุข้อห้ามเกี่ยวกับการสื่อสารระหว่างการหยุดพักเกมและให้ยึดคำสั่งผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_no_communication / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, สื่อสาร | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0173` sec

## 82. [PASS] ถูก

**คำถาม:** RoV บทลงโทษการ pause ผิดครั้งแรกคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV การ Pause ผิดครั้งที่ 1 จะถูกตักเตือน

หลักฐานจากกติกา:
- เอกสารบทลงโทษการ Pause ผิดระบุครั้งที่ 1 เป็นการตักเตือน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_wrong_first_penalty / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ครั้งที่ 1, ตักเตือน | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0173` sec

## 83. [PASS] ถูก

**คำถาม:** RoV pause ผิดครั้งที่ 2 โดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV Pause ผิดครั้งที่ 2 จะเพิ่มสิทธิการแบนฮีโร่ให้ฝ่ายตรงข้าม 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารบทลงโทษการ Pause ผิดระบุครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_wrong_second_penalty / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.019` sec

## 84. [PASS] ถูก

**คำถาม:** RoV pause ผิดครั้งที่ 3 โดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV Pause ผิดครั้งที่ 3 จะเพิ่มสิทธิการแบนฮีโร่ให้ฝ่ายตรงข้าม 2 ครั้ง

หลักฐานจากกติกา:
- เอกสารบทลงโทษการ Pause ผิดระบุครั้งที่ 3 เพิ่มสิทธิการแบนฮีโร่ 2 ครั้ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_wrong_third_penalty / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0171` sec

## 85. [PASS] ถูก

**คำถาม:** RoV ใช้อุปกรณ์อะไรแข่ง

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.012` sec

## 86. [PASS] ถูก

**คำถาม:** RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ไม่อนุญาตให้ใช้ Tablet หรือ iPad ลงแข่งขัน ต้องใช้โทรศัพท์มือถือเท่านั้น

หลักฐานจากกติกา:
- เอกสารข้อ 5.3 ระบุไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นที่ไม่ใช่โทรศัพท์มือถือ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_tablet_ipad_not_allowed / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0183` sec

## 87. [PASS] ถูก

**คำถาม:** RoV เอาปลั๊กพ่วงกับอุปกรณ์ชาร์จส่วนตัวได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว

รายละเอียดที่เกี่ยวข้อง:
- 5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที
- 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
- 4.5.6.1.2. อุปกรณ์พกพาหรือซอฟต์แวร์ทำงานผิดปกติ
- 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
- 4.6.2.การหยุดพักเกมตามการตัดสินใจของผู้เข้าร่วมการแข่งขัน โดยไม่ได้รับอนุญาตจากผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s07_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s07_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปลั๊กพ่วง, อุปกรณ์ชาร์จ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0253` sec

## 88. [PASS] ถูก

**คำถาม:** RoV ใช้คำพูดไม่สุภาพหรือเสียดสีโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV หากใช้คำพูดไม่สุภาพหรือเสียดสี จะถูกปรับแพ้ในเกมที่พบการกระทำผิด

หลักฐานจากกติกา:
- เอกสารข้อ 4.1.1 ห้ามใช้คำพูดหยาบคายหรือเสียดสี และบทลงโทษระบุปรับแพ้ในเกมที่พบการกระทำผิด

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rude_speech_penalty / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้, เกมที่พบ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 89. [PASS] ถูก

**คำถาม:** RoV ส่งผลการแข่งขันเท็จโดนลงโทษยังไง

**คำตอบ(จาก AI):**

คำตอบ: 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
- 6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
- 6.1.4.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
- 6.1.5.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจาก
- 6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที
- 6. การกระทำความผิดและบทลงโทษ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s08_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s08_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้, ตัดสิทธิ์ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0201` sec

## 90. [PASS] ถูก

**คำถาม:** RoV ให้คนอื่นที่ไม่ได้ลงทะเบียนมาแข่งแทนได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ห้ามให้ผู้เล่นที่ไม่ตรงตามที่ลงทะเบียนมาแข่งแทน หากฝ่าฝืนจะถูกปรับแพ้และตัดสิทธิ์

หลักฐานจากกติกา:
- เอกสารบทลงโทษระบุการส่งผู้เล่นไม่ตรงตามที่ลงทะเบียนเป็นความผิดที่นำไปสู่การปรับแพ้และตัดสิทธิ์

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_unregistered_player_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0149` sec

## 91. [PASS] ถูก

**คำถาม:** RoV ห้ามให้คนอื่นเล่นแทนตัวเองไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ห้ามให้คนอื่นเล่นแทนตัวเองหรือเล่นแทนผู้ที่ลงทะเบียนไว้

หลักฐานจากกติกา:
- เอกสารบทลงโทษระบุข้อห้ามเกี่ยวกับการให้บุคคลอื่นเล่นแทนผู้เข้าแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_playing_for_other_forbidden / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เล่นแทน, ห้าม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0146` sec

## 92. [PASS] ถูก

**คำถาม:** RoV ถามสรุปรูปแบบแข่งกับสถานที่แบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ: RoV แข่งขันออฟไลน์ที่ PSU Esports Studio - Phuket และใช้รูปแบบ Best of 3 (BO3) ทุกรอบ
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_format_location_summary / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s04_c01, competition_rules_rov_blueket_2025_men_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ออฟไลน์, BO3, PSU Esports Studio | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0148` sec

## 93. [PASS] ถูก

**คำถาม:** RoV ถ้าถามเรื่องเวลาแข่งทั้งวันควรตอบหัวข้ออะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ

หลักฐานจากกติกา:
- เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_full_day_schedule_topics / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ลงทะเบียน, รอบรอง, รอบชิง | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: schedule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 94. [PASS] ถูก

**คำถาม:** RoV ขอกฎ disconnect แบบเข้าใจง่าย

**คำตอบ(จาก AI):**

คำตอบ: RoV กรณี Disconnect ให้ Pause ได้ และถ้ายังไม่มี First Blood ภายใน 2 นาทีแรกสามารถขอเริ่มเกมใหม่ได้ตามเงื่อนไข

หลักฐานจากกติกา:
- เอกสารข้อ 4.3 ระบุการ Pause เมื่อหลุดเกม และเงื่อนไข Rematch ก่อน First Blood/ก่อน 2 นาที

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_disconnect_simple_summary / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01, competition_rules_rov_blueket_2025_men_s06_c02`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: pause, First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0161` sec

## 95. [PASS] ถูก

**คำถาม:** RoV มีข้อมูลตัวสำรองชัดเจนไหมในไฟล์นี้

**คำตอบ(จาก AI):**

คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้

หลักฐานจากกติกา:
- เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเจน

หมายเหตุ: คำตอบนี้เป็นการสรุปจากข้อมูลที่มีในไฟล์กติกา ไม่ใช่ข้อมูล roster/ตัวสำรองที่ระบุเป็นตัวเลขแยกไว้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_team_size_active_players / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5v5 | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 96. [PASS] ถูก

**คำถาม:** สมาชิกในทีม ROV ต้องเล่นพร้อมกันฝั่งละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้

หลักฐานจากกติกา:
- เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเจน

หมายเหตุ: คำตอบนี้เป็นการสรุปจากข้อมูลที่มีในไฟล์กติกา ไม่ใช่ข้อมูล roster/ตัวสำรองที่ระบุเป็นตัวเลขแยกไว้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_team_size_active_players / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0112` sec

## 97. [PASS] ถูก

**คำถาม:** VALORANT ทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0112` sec

## 98. [PASS] ถูก

**คำถาม:** วาโลต้องส่งผู้เล่นตัวจริงกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ตัวจริง 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0117` sec

## 99. [PASS] ถูก

**คำถาม:** VALORANT Match Prep มีคนได้ไม่เกินกี่คน

**คำตอบ(จาก AI):**

คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- ขอได้ 1 ครั้งต่อแผนที่
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- รายการ PSU Phuket VALORANT 2026 Tournament

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่เกิน 6 | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0219` sec

## 100. [PASS] ถูก

**คำถาม:** VALORANT เอามือถือเข้าพื้นที่แข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)

รายละเอียดที่เกี่ยวข้อง:
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, โทรศัพท์มือถือ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0196` sec

## 101. [PASS] ถูก

**คำถาม:** VALORANT หัวหน้าทีมนำโน้ตเข้าได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

รายละเอียดที่เกี่ยวข้อง:
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
- อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: หัวหน้าทีม, กรรมการ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.02` sec

## 102. [PASS] ถูก

**คำถาม:** VALORANT อาหารเครื่องดื่มที่อนุญาตมีอะไร

**คำตอบ(จาก AI):**

คำตอบ: * อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต
- อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: น้ำดื่ม, ปิดสนิท, หมากฝรั่ง | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: area_rules

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0189` sec

## 103. [PASS] ถูก

**คำถาม:** VALORANT ต้องมารายงานตัวก่อนแข่งกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ต้องมารายงานตัวก่อนการแข่งขัน 30 นาที

หลักฐานจากกติกา:
- เอกสารระบุให้ผู้เล่นมารายงานตัวก่อนการแข่งขัน 30 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_report_30_minutes / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 30 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: checkin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0143` sec

## 104. [PASS] ถูก

**คำถาม:** วาโล agent ใหม่ใช้ได้ทันทีไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 105. [PASS] ถูก

**คำถาม:** VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนใช้แข่ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0135` sec

## 106. [PASS] ถูก

**คำถาม:** VALORANT ต้องปิด setting อะไรก่อนแข่ง

**คำตอบ(จาก AI):**

คำตอบ: * ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)

รายละเอียดที่เกี่ยวข้อง:
- เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- Players must turn OFF blood and body displays.
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s18_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เลือด, ศพ, OFF | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0226` sec

## 107. [PASS] ถูก

**คำถาม:** VALORANT เปิดกราฟ FPS หรือ latency ระหว่างแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive

รายละเอียดที่เกี่ยวข้อง:
- แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
- ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน
- อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, FPS, Latency | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0303` sec

## 108. [PASS] ถูก

**คำถาม:** VALORANT map pool มีทั้งหมดกี่ map และชื่ออะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Map Pool มีทั้งหมด 7 แผนที่ ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ Map Pool 7 แผนที่ ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool_count_7 / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 7, Abyss, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0217` sec

## 109. [PASS] ถูก

**คำถาม:** วาโลมี Haven Lotus Sunset ใน map pool ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Haven, Lotus, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 110. [PASS] ถูก

**คำถาม:** VALORANT ban map จนเหลือกี่แผนที่

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แบนแผนที่จนเหลือ 3 แผนที่

หลักฐานจากกติกา:
- เอกสารขั้นตอนเลือกแผนที่ระบุให้แบนจนเหลือ 3 แผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_ban_until_three_maps / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 แผนที่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 111. [PASS] ถูก

**คำถาม:** VALORANT เลือกฝั่งด้วยวิธีอะไร

**คำตอบ(จาก AI):**

คำตอบ: * ใช้วิธีการโยนเหรียญ

รายละเอียดที่เกี่ยวข้อง:
- การเลือกฝั่ง
- การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่
- ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- แบนจนเหลือ 3 แผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โยนเหรียญ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: side_selection

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0185` sec

## 112. [PASS] ถูก

**คำถาม:** หลังจบแมตช์ VALORANT ใครยืนยันและบันทึกผล

**คำตอบ(จาก AI):**

คำตอบ: * การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที

รายละเอียดที่เกี่ยวข้อง:
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0
- พื้นที่การแข่งขันและกฎระเบียบ
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เจ้าหน้าที่, บันทึกผล | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: post_match

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0218` sec

## 113. [PASS] ถูก

**คำถาม:** VALORANT ถ้า forfeit แผนที่นั้นบันทึกผลเป็นเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: * การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0

รายละเอียดที่เกี่ยวข้อง:
- แบนจนเหลือ 3 แผนที่
- แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 13-0 | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0281` sec

## 114. [PASS] ถูก

**คำถาม:** VALORANT pause มีกี่ประเภทหลัก

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Pause มี 3 ประเภทหลัก ได้แก่ Tactical Timeout, Technical Pause และ Emergency Pause

หลักฐานจากกติกา:
- เอกสารระบุการหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก ได้แก่ Tactical, Technical และ Emergency

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_pause_three_types / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3, Tactical, Technical, Emergency | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0152` sec

## 115. [PASS] ถูก

**คำถาม:** VALORANT tactical timeout ได้กี่ครั้งต่อแผนที่

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 2, ต่อแผนที่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0163` sec

## 116. [PASS] ถูก

**คำถาม:** วาโล tactical timeout ครั้งละกี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 60 วินาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0162` sec

## 117. [PASS] ถูก

**คำถาม:** VALORANT overtime ได้ timeout เพิ่มไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Overtime, เพิ่ม, 1 ครั้ง | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0166` sec

## 118. [PASS] ถูก

**คำถาม:** VALORANT Technical Pause ใช้กรณีไหน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Technical Pause ใช้กรณีปัญหาทางเทคนิค เช่น อุปกรณ์ขัดข้อง, หลุดจากเกม หรือปัญหาซอฟต์แวร์

หลักฐานจากกติกา:
- เอกสาร Technical Pause ระบุปัญหาอุปกรณ์ขัดข้อง หลุด และซอฟต์แวร์เป็นตัวอย่างกรณีใช้ Technical Pause

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_technical_pause_cases / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 119. [PASS] ถูก

**คำถาม:** ตอน Technical Pause วาโลคุยกันได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ตอน Technical Pause ห้ามผู้เล่นสื่อสารกัน เว้นแต่ได้รับอนุญาตจากเจ้าหน้าที่

หลักฐานจากกติกา:
- เอกสาร Technical Pause ระบุข้อจำกัดการสื่อสารระหว่างหยุดเกมและข้อยกเว้นเมื่อเจ้าหน้าที่อนุญาต

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_technical_pause_no_talk / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, สื่อสาร, เว้นแต่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0181` sec

## 120. [PASS] ถูก

**คำถาม:** VALORANT Emergency Pause ขอได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: * ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
- 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- ขอได้ 1 ครั้งต่อแผนที่
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- 2. การหยุดเกมทางเทคนิค (Technical Pause)
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 ครั้ง, ต่อแผนที่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.021` sec

## 121. [PASS] ถูก

**คำถาม:** VALORANT Emergency Pause รวมเวลาได้ไม่เกินกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)

รายละเอียดที่เกี่ยวข้อง:
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0225` sec

## 122. [PASS] ถูก

**คำถาม:** VALORANT ถ้า emergency pause เกินเวลาผู้เล่นอาจเป็นอะไร

**คำตอบ(จาก AI):**

คำตอบ: ถ้า VALORANT Emergency Pause เกินเวลาที่กำหนด ผู้เล่นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

หลักฐานจากกติกา:
- เอกสาร Emergency Pause ระบุหากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_over_time_substitute / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: หมดสิทธิ์, ตัวสำรอง | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0206` sec

## 123. [PASS] ถูก

**คำถาม:** VALORANT Play Through Bug คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: * Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้

รายละเอียดที่เกี่ยวข้อง:
- Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
- Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้
- หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที
- Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested.
- In the case of a Game-Breaking Bug, officials will immediately roll back to the start of the round.

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s24_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s24_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s23_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s23_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่ส่งผลกระทบ, เล่นต่อ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: bug_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0209` sec

## 124. [PASS] ถูก

**คำถาม:** VALORANT Major Bug ขอ Challenge ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้

รายละเอียดที่เกี่ยวข้อง:
- Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
- Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้
- Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested.
- Bugs that significantly affect gameplay or core mechanics and cannot be immediately resolved. Teams may request a challenge for review.
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s24_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s24_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Major Bug, Challenge | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: bug_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0227` sec

## 125. [PASS] ถูก

**คำถาม:** VALORANT Game Breaking Bug จัดการยังไง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Game-Breaking Bug จะให้เจ้าหน้าที่ย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที

หลักฐานจากกติกา:
- เอกสารระบุ Game-Breaking Bug เป็นบั๊กที่ทำลายความยุติธรรมของรอบ และเจ้าหน้าที่จะสั่งย้อนรอบไปจุดเริ่มต้นทันที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_game_breaking_bug_hyphen / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Game-Breaking, ย้อนรอบ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: bug_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0176` sec

## 126. [PASS] ถูก

**คำถาม:** VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้

**คำตอบ(จาก AI):**

คำตอบ: ถ้า VALORANT เกิดบั๊กก่อนมี damage เจ้าหน้าที่อาจย้อนรอบ (Round Rollback) ได้

หลักฐานจากกติกา:
- เอกสาร Round Rollback ระบุหากบั๊กเกิดก่อนมีการทำดาเมจ เจ้าหน้าที่อาจย้อนรอบได้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_bug_before_damage_rollback / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ก่อน, ดาเมจ, ย้อนรอบ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: bug_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0196` sec

## 127. [PASS] ถูก

**คำถาม:** VALORANT ถ้าทำ damage ไปแล้ว rollback ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ถ้าทำ damage ไปแล้ว โดยปกติ VALORANT จะไม่ rollback ยกเว้นได้รับอนุมัติผ่านกระบวนการ Challenge

หลักฐานจากกติกา:
- เอกสาร Round Rollback ระบุหากมีการทำ damage ไปแล้ว จะไม่มีการย้อนรอบ ยกเว้นผ่านกระบวนการ Challenge

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_damage_after_rollback / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: damage, ไม่, Challenge | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: bug_rule

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0191` sec

## 128. [PASS] ถูก

**คำถาม:** VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม

**คำตอบ(จาก AI):**

คำตอบ: ผิด กติกา VALORANT ถือว่าการใช้บั๊กเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจเป็นความผิด

หลักฐานจากกติกา:
- เอกสาร Exploit Adjudication ระบุการใช้บั๊กหรือ unintended mechanics เพื่อสร้างความได้เปรียบถือเป็นความผิด

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_exploit_wrong_advantage / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ผิด, ได้เปรียบ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 129. [PASS] ถูก

**คำถาม:** VALORANT วางกล้อง Cypher จุดมองไม่เห็นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่

รายละเอียดที่เกี่ยวข้อง:
- Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
- ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
- Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, Cypher | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0219` sec

## 130. [PASS] ถูก

**คำถาม:** VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ห้ามใช้สกิลนอกขอบเขตแผนที่เพื่อหาข้อมูลหรือสร้างความได้เปรียบ

หลักฐานจากกติกา:
- เอกสารระบุห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่เพื่อหาข้อมูลหรือสร้างความได้เปรียบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_out_of_bounds_forbidden / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, นอกขอบเขต | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0152` sec

## 131. [PASS] ถูก

**คำถาม:** VALORANT ข้อยกเว้น KAY/O ZERO/POINT คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: * หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge

รายละเอียดที่เกี่ยวข้อง:
- ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
- Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: KAY/O, ZERO/POINT, Texture | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0247` sec

## 132. [PASS] ถูก

**คำถาม:** VALORANT ใช้เพื่อนกระโดดต่อตัวขึ้นจุดสูงได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ห้ามใช้ตัวละครเพื่อนร่วมทีมกระโดดต่อตัวไปยังจุดที่สูงกว่าระยะกระโดดปกติ

หลักฐานจากกติกา:
- เอกสาร Player Boosting ระบุห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_player_boosting_forbidden / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, กระโดด | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0153` sec

## 133. [PASS] ถูก

**คำถาม:** VALORANT ความผิดครั้งแรกผลกระทบต่ำโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ความผิดครั้งแรกที่มีผลกระทบต่ำจะได้รับ Warning หรือการตักเตือน

หลักฐานจากกติกา:
- เอกสาร In-Game Penalty Types ระบุ Warning สำหรับ first offenses with low impact

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_warning_low_impact / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Warning, ตักเตือน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0153` sec

## 134. [PASS] ถูก

**คำถาม:** VALORANT Round Rollback ใช้เมื่อไหร่

**คำตอบ(จาก AI):**

คำตอบ: * การย้อนรอบ (Round Rollback)

รายละเอียดที่เกี่ยวข้อง:
- Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
- ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
- การใช้ช่องโหว่ (Exploit Adjudication)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Round Rollback, ช่องโหว่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0205` sec

## 135. [PASS] ถูก

**คำถาม:** VALORANT Round Loss เกิดจากอะไร

**คำตอบ(จาก AI):**

คำตอบ: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

รายละเอียดที่เกี่ยวข้อง:
- Round Loss - When a player or team is found to have intentionally used an exploit for advantage.
- Match Forfeit - In cases of cheating or match fixing.
- Warning - For first offenses with low impact.
- Map Forfeit - For severe offenses or repeated violations that affect the map result.
- แบนจนเหลือ 3 แผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s13_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s13_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s25_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s25_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Round Loss, เจตนา, ช่องโหว่ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.023` sec

## 136. [PASS] ถูก

**คำถาม:** VALORANT Map Forfeit ใช้กรณีไหน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Map Forfeit ใช้กับความผิดร้ายแรงหรือการทำผิดซ้ำ

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`round5_valorant_map_forfeit / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Map Forfeit, ร้ายแรง, ซ้ำ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0143` sec

## 137. [PASS] ถูก

**คำถาม:** VALORANT Match Forfeit ใช้กับความผิดแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)

รายละเอียดที่เกี่ยวข้อง:
- Match Forfeit - In cases of cheating or match fixing.
- 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น
- Map Forfeit - For severe offenses or repeated violations that affect the map result.
- Warning - For first offenses with low impact.
- Round Loss - When a player or team is found to have intentionally used an exploit for advantage.

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s15_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s25_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s25_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s14_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s14_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Match Forfeit, Cheating, Match fixing | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0206` sec

## 138. [PASS] ถูก

**คำถาม:** VALORANT ใช้ keyboard Snap Tap หรือ SOCD ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
- The use of Snap Tap, SOCD, or equivalent technologies is permitted, unless otherwise instructed by officials.
- อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
- อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s16_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s16_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Snap Tap, SOCD, permitted | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0298` sec

## 139. [PASS] ถูก

**คำถาม:** VALORANT ใช้ macro ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์

รายละเอียดที่เกี่ยวข้อง:
- อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต
- ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
- ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, Macros | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0199` sec

## 140. [PASS] ถูก

**คำถาม:** VALORANT ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
- ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
- ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ติดตั้งโปรแกรม | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0198` sec

## 141. [PASS] ถูก

**คำถาม:** VALORANT เข้าเว็บสื่อสารหรือโซเชียลบนคอมแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ห้ามเข้า social media หรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขัน ยกเว้นโปรแกรมที่ผู้จัดเตรียมไว้

หลักฐานจากกติกา:
- เอกสาร Key Prohibitions ระบุห้าม access social media หรือ communication websites บนคอมพิวเตอร์แข่งขัน ยกเว้นโปรแกรมที่ผู้จัดเตรียมไว้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_social_media_forbidden_english / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, social media | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0141` sec

## 142. [PASS] ถูก

**คำถาม:** VALORANT สรุป pause แต่ละประเภทแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Pause มี 3 ประเภทหลัก ได้แก่ Tactical Timeout, Technical Pause และ Emergency Pause
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_pause_three_types / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical, Technical, Emergency | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0162` sec

## 143. [PASS] ถูก

**คำถาม:** VALORANT สรุปกฎเนื้อหาใหม่กับ map pool

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ แผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ และ Map Pool ใช้ 7 แผนที่ ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset

หลักฐานจากกติกา:
- เอกสารระบุ Agent ใหม่ 2 สัปดาห์ แผนที่ใหม่ 4 สัปดาห์ และ Map Pool 7 แผนที่ ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_new_content_and_map_pool_summary / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์, Abyss | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0189` sec

## 144. [PASS] ถูก

**คำถาม:** VALORANT สรุปบทลงโทษในเกมว่ามีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: บทลงโทษในเกมของ VALORANT ได้แก่ Warning, Round Rollback, Round Loss, Map Forfeit และ Match Forfeit

หลักฐานจากกติกา:
- เอกสาร In-Game Penalty Types ระบุ Warning, Round Rollback, Round Loss, Map Forfeit และ Match Forfeit

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_penalty_types_summary / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0138` sec

## 145. [PASS] ถูก

**คำถาม:** Tekken 8 แข่งออนไลน์หรือออฟไลน์

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ออฟไลน์ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0123` sec

## 146. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้เครื่องอะไรแข่ง

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ใช้เครื่อง PlayStation 5 เป็นแพลตฟอร์มการแข่งขัน

หลักฐานจากกติกา:
- เอกสารกติกาพื้นฐานระบุ Platform เป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_platform_ps5_challenger / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0109` sec

## 147. [PASS] ถูก

**คำถาม:** Tekken 8 แข่งแบบกี่ต่อกี่

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0115` sec

## 148. [PASS] ถูก

**คำถาม:** Tekken 8 FT2 คือชนะกี่เกมก่อน

**คำตอบ(จาก AI):**

คำตอบ: * FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

รายละเอียดที่เกี่ยวข้อง:
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- จำนวนรอบต่อเกม (Round): 3
- ใช้เครื่องเกม PlayStation 5
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน
- เวลาแข่งขันต่อรอบ (Timer): 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s04_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ชนะครบ 2 เกม | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0112` sec

## 149. [PASS] ถูก

**คำถาม:** Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร

**คำตอบ(จาก AI):**

คำตอบ: * หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

รายละเอียดที่เกี่ยวข้อง:
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
- แข่งขันแบบ เดี่ยว (1v1)
- แข่งขันแบบ ออฟไลน์ (Offline)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s01_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s01_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เกมตัดสิน | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0171` sec

## 150. [PASS] ถูก

**คำถาม:** Tekken 8 ในแต่ละเกมแข่งกี่รอบ

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ในแต่ละเกมแข่ง 3 รอบ (R3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบ R3 หมายถึงแข่ง 3 รอบต่อเกม

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_rounds_per_game_thai / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 รอบ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0126` sec

## 151. [PASS] ถูก

**คำถาม:** Tekken 8 จำกัดเวลาต่อรอบกี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

รายละเอียดที่เกี่ยวข้อง:
- เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
- จำนวนรอบต่อเกม (Round): 3
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s04_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s04_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0147` sec

## 152. [PASS] ถูก

**คำถาม:** Tekken 8 ตั้งค่า Advantage เป็นอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ตั้งค่า Advantage เป็น No advantage

หลักฐานจากกติกา:
- เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`round5_tekken8_advantage / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: No advantage | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0141` sec

## 153. [PASS] ถูก

**คำถาม:** Tekken 8 เลือก Stage อย่างไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ให้เลือก Stage แบบ Random

หลักฐานจากกติกา:
- เอกสารการตั้งค่าเกมระบุ Stage: Random

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_stage_random / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Random | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 154. [PASS] ถูก

**คำถาม:** Tekken 8 เลือกตัวละคร DLC ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้น, DLC | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 155. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ตัวละครตัวไหนก็ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ทุกตัว, ยกเว้น, DLC | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0162` sec

## 156. [PASS] ถูก

**คำถาม:** Tekken 8 ปรับแต่งชุดหรือทรงผมตัวละครได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ห้ามปรับแต่งตัวละคร เช่น ชุดหรือทรงผม ให้ใช้ชุด/สกินมาตรฐานเท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุไม่อนุญาตให้ใช้ Customization และให้ใช้ชุด/สกินมาตรฐาน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_customization_no_thai / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ปรับแต่ง | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0275` sec

## 157. [PASS] ถูก

**คำถาม:** Tekken 8 ต้องใช้สกินแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: * ต้องใช้ สกินมาตรฐาน เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- แข่งขันแบบ ออฟไลน์ (Offline)
- แข่งขันแบบ เดี่ยว (1v1)
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: สกินมาตรฐาน | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0196` sec

## 158. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ปุ่ม Assist ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ

รายละเอียดที่เกี่ยวข้อง:
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ต้องใช้ สกินมาตรฐาน เท่านั้น

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s04_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อนุญาต, Assist | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0181` sec

## 159. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ bug หรือ glitch ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

รายละเอียดที่เกี่ยวข้อง:
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, Bug, Glitch | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0203` sec

## 160. [PASS] ถูก

**คำถาม:** Tekken 8 เมื่อเริ่มเกมแล้ว pause ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, หยุดเกม | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0207` sec

## 161. [PASS] ถูก

**คำถาม:** Tekken 8 ตั้งใจกด pause โดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 หากตั้งใจกด Pause จะถูกปรับแพ้ 1 รอบ

หลักฐานจากกติกา:
- เอกสารระบุการ Pause โดยตั้งใจทำให้แพ้ 1 Round

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty_thai_round / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้ 1 รอบ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0284` sec

## 162. [PASS] ถูก

**คำถาม:** Tekken 8 กดหยุดเกมได้ในกรณีไหน

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 กดหยุดเกมได้เฉพาะกรณีอุปกรณ์ขัดข้องหรือเหตุฉุกเฉินที่สมควร และต้องได้รับการยินยอมหรืออนุญาตตามกติกา

หลักฐานจากกติกา:
- เอกสารระบุ Pause ได้เฉพาะกรณีมีเหตุผลสมควร เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน และต้องอยู่ภายใต้การยินยอม/การอนุญาต

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_allowed_emergency_equipment / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยินยอม, อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0173` sec

## 163. [PASS] ถูก

**คำถาม:** Tekken 8 ถ้าออกจากเกมก่อนจบโดยไม่ได้รับอนุญาตโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

รายละเอียดที่เกี่ยวข้อง:
- ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s05_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s05_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้ทันที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0158` sec

## 164. [PASS] ถูก

**คำถาม:** Tekken 8 หยุดเกมโดยไม่จำเป็นลงโทษเหมือนอะไร

**คำตอบ(จาก AI):**

คำตอบ: * หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที

รายละเอียดที่เกี่ยวข้อง:
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
- หากกดหยุดเกมโดยไม่จำเป็น จะได้รับโทษเช่นเดียวกับการออกจากเกมก่อนจบ
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ออกจากเกมก่อนจบ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0216` sec

## 165. [PASS] ถูก

**คำถาม:** Tekken 8 เยาะเย้ยหรือไม่สุภาพต่อคู่แข่งโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

รายละเอียดที่เกี่ยวข้อง:
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s05_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s05_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้ทันที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0169` sec

## 166. [PASS] ถูก

**คำถาม:** Tekken 8 ดูถูกผู้ตัดสินหรือผู้เข้าแข่งคนอื่นได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

รายละเอียดที่เกี่ยวข้อง:
- ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s05_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s05_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ปรับแพ้ทันที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0152` sec

## 167. [PASS] ถูก

**คำถาม:** Tekken 8 ผู้เข้าแข่งขันต้องยอมรับอะไรเกี่ยวกับคำตัดสิน

**คำตอบ(จาก AI):**

คำตอบ: * ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

รายละเอียดที่เกี่ยวข้อง:
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
- กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม
- กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ
- หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s01_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: คำตัดสิน, กรรมการ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: policy

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0156` sec

## 168. [PASS] ถูก

**คำถาม:** ผู้จัด Tekken 8 เปลี่ยนกฎได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
- ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
- ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: policy

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0164` sec

## 169. [PASS] ถูก

**คำถาม:** Tekken 8 คำตัดสินของกรรมการถือว่าอย่างไร

**คำตอบ(จาก AI):**

คำตอบ: * ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข

รายละเอียดที่เกี่ยวข้อง:
- คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
- ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด
- กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน
- หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ถือเป็นที่สิ้นสุด | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: policy

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0112` sec

## 170. [PASS] ถูก

**คำถาม:** Tekken 8 ถ้าเกิดข้อโต้แย้งต้องฟังคำตัดสินใคร

**คำตอบ(จาก AI):**

คำตอบ: * ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

รายละเอียดที่เกี่ยวข้อง:
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
- หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที
- กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ผู้ดูแล, กรรมการ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: dispute

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0155` sec

## 171. [PASS] ถูก

**คำถาม:** Tekken 8 หากเกิดปัญหาใดๆ ต้องแจ้งใคร

**คำตอบ(จาก AI):**

คำตอบ: * หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
- ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด
- หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ผู้จัดการแข่งขัน, ทันที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: dispute

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0159` sec

## 172. [PASS] ถูก

**คำถาม:** Tekken 8 สรุปรูปแบบการแข่งขันแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ออฟไลน์, PlayStation 5, 1v1, FT2 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0126` sec

## 173. [PASS] ถูก

**คำถาม:** Tekken 8 สรุปกฎตัวละครและสกิน

**คำตอบ(จาก AI):**

คำตอบ: * ต้องใช้ สกินมาตรฐาน เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: DLC, ปรับแต่ง, สกินมาตรฐาน | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0163` sec

## 174. [PASS] ถูก

**คำถาม:** Tekken 8 สรุปกฎ pause แบบเข้าใจง่าย

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Pause, ยินยอม, ปรับแพ้ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: summary

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0163` sec

## 175. [PASS] ถูก

**คำถาม:** Tekken 8 รอบละ 60 วิและ R3 หมายถึงอะไร

**คำตอบ(จาก AI):**

คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

รายละเอียดที่เกี่ยวข้อง:
- เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
- จำนวนรอบต่อเกม (Round): 3
- หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s04_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s04_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 3 รอบ, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0221` sec

## 176. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ PS5 กับ Stage Random ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: ใช่ Tekken 8 ใช้เครื่อง PlayStation 5 และการเลือก Stage เป็นแบบ Random

หลักฐานจากกติกา:
- เอกสารระบุใช้เครื่องเกม PlayStation 5 และ Stage: Random

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_ps5_stage_random_combined / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, Random | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: game_setting

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0194` sec

## 177. [PASS] ถูก

**คำถาม:** Tekken 8 ถามว่าแข่งกี่เกมควรตอบว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ใช้ FT2 ผู้ชนะคือคนที่ชนะครบ 2 เกมก่อน

หลักฐานจากกติกา:
- เอกสารระบุ FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_ft2_win_two_games / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: FT2, ชนะครบ 2 เกม | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 178. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ customization เอฟเฟกต์หรือออร่าได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

รายละเอียดที่เกี่ยวข้อง:
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, เอฟเฟกต์, ออร่า | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0205` sec

## 179. [PASS] ถูก

**คำถาม:** Tekken 8 เหตุผลด้านอุปกรณ์ขัดข้องสามารถ pause ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน

รายละเอียดที่เกี่ยวข้อง:
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: อุปกรณ์ขัดข้อง, ยินยอม | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.023` sec

## 180. [PASS] ถูก

**คำถาม:** Tekken 8 เหตุฉุกเฉินใช้เป็นเหตุผล pause ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน

รายละเอียดที่เกี่ยวข้อง:
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ
- หากกดหยุดเกมโดยไม่จำเป็น จะได้รับโทษเช่นเดียวกับการออกจากเกมก่อนจบ
- ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เหตุฉุกเฉิน | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0256` sec

## 181. [PASS] ถูก

**คำถาม:** Tekken 8 กติกาบอกว่าผู้จัดขอสงวนสิทธิ์อะไร

**คำตอบ(จาก AI):**

คำตอบ: หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า

รายละเอียดที่เกี่ยวข้อง:
- หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- คำตัดสินของกรรมการถือเป็นที่สิ้นสุด

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: เปลี่ยนแปลง, กฎระเบียบ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: policy

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0167` sec

## 182. [PASS] ถูก

**คำถาม:** Tekken 8 ถ้าฝ่าฝืนมารยาทมีข้อยกเว้นไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

รายละเอียดที่เกี่ยวข้อง:
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
- ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
- ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s05_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่มีข้อยกเว้น, ปรับแพ้ | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: penalty

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0156` sec

## 183. [PASS] ถูก

**คำถาม:** Tekken 8 เลือกตัวละคร DLC ไม่ได้แต่ใช้ Assist ได้ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

รายละเอียดที่เกี่ยวข้อง:
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: DLC, Assist | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0228` sec

## 184. [PASS] ถูก

**คำถาม:** Tekken 8 ต้องเล่นบนแพลตฟอร์มอะไรและเป็นเดี่ยวไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันแบบเดี่ยว 1v1 บนแพลตฟอร์ม PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ 1v1 และ Platform เป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_platform_ps5_and_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5, เดี่ยว, 1v1 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.012` sec
