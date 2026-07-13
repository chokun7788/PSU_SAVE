# Ground Truth Verbose Result

- Total: 20
- PASS: 13
- FAIL: 7
- ERROR: 0
- Pass rate: 65.00%
- Average latency: 0.0213s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_competition_challenger_v1_verbose_20260704_014112.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_competition_challenger_v1_verbose_20260704_014112.md`

## Mode Summary
- `pipeline:rag_direct_curated`: 13
- `pipeline:competition_fact_card`: 6
- `pipeline:games_fast_path`: 1

## Route Summary
- `competition_rules`: 19
- `games`: 1
## 1. [FAIL] ผิด

**คำถาม:** CS2 เลทแล้วเปลี่ยนตัวตอนหน้างานได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s45_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s45_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่มีการเปลี่ยนแปลงสมาชิก, ตลอดระยะเวลาการแข่งขัน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0218` sec
- missing_keywords: `['ไม่มีการเปลี่ยนแปลงสมาชิก', 'ตลอดระยะเวลาการแข่งขัน']`

## 2. [PASS] ถูก

**คำถาม:** CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ

**คำตอบ(จาก AI):**

คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s12_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s12_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, หลังจากปิดรับสมัคร | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0297` sec

## 3. [PASS] ถูก

**คำถาม:** CS2 ถ้าคนในทีมถอนตัวกลางทัวร์ ทีมจะโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
- 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
- ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
- ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
- ปรับแพ้ในรอบนั้น / ตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s13_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s13_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s37_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s37_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ถอนตัว, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0255` sec

## 4. [PASS] ถูก

**คำถาม:** แข่ง CS2 ต้องคุยผ่านอะไร Discord ใช่ปะ

**คำตอบ(จาก AI):**

คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

รายละเอียดที่เกี่ยวข้อง:
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Discord | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0231` sec

## 5. [PASS] ถูก

**คำถาม:** CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย

**คำตอบ(จาก AI):**

คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s58_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s58_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ภาษาไทย, ประท้วง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0222` sec

## 6. [PASS] ถูก

**คำถาม:** CS2 แข่งกี่วันแล้วจัดที่ไหน แบบสรุป

**คำตอบ(จาก AI):**

คำตอบ: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

รายละเอียดที่เกี่ยวข้อง:
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s15_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s15_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1 วัน, PSU Esports Studio, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0235` sec

## 7. [PASS] ถูก

**คำถาม:** cs2 ใช้ steam เวอร์ล่าสุดใช่มั้ย ห้าม mod ด้วยไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s09_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s09_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s36_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s36_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ล่าสุด, Steam, ห้าม, ดัดแปลง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0281` sec

## 8. [PASS] ถูก

**คำถาม:** CS2 ขอ technical pause รวมได้กี่นาทีต่อทีม

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 2 ครั้ง, 10 นาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0195` sec

## 9. [PASS] ถูก

**คำถาม:** CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
- 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s34_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s24_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s24_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 4 ครั้ง, 30 วินาที, Freeze time | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0281` sec

## 10. [FAIL] ผิด

**คำถาม:** CS2 ใช้บัคถ้าโดนจับได้มีโทษไร

**คำตอบ(จาก AI):**

คำตอบ: การใช้บัค

รายละเอียดที่เกี่ยวข้อง:
- 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- หยุดเกมโดยไม่ได้รับอนุญาต
- การด่าทอ/ใช้ความรุนแรงทางวาจา
- ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s37_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s37_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ปรับแพ้, รอบ, แมตช์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0217` sec
- missing_keywords: `['แมตช์']`

## 11. [FAIL] ผิด

**คำถาม:** CS2 ดูสตรีมไปด้วยตอนแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 8. ตารางบทลงโทษ (Penalties)

รายละเอียดที่เกี่ยวข้อง:
- การละเมิด
- บทลงโทษ
- การด่าทอ/ใช้ความรุนแรงทางวาจา
- ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s54_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s54_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s38_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s38_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ดูสตรีม, ปรับแพ้, แมตช์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.018` sec
- missing_keywords: `['ดูสตรีม', 'แมตช์']`

## 12. [FAIL] ผิด

**คำถาม:** CS2 toxic ด่าในแชทหรือพูดแรง ๆ โดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ตักเตือน, ปรับแพ้, ตัดสิทธิ์ | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0148` sec
- missing_keywords: `['ตักเตือน', 'ปรับแพ้', 'ตัดสิทธิ์']`

## 13. [PASS] ถูก

**คำถาม:** CS2 map pool มี Nuke กับ Train อยู่ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Nuke, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 14. [PASS] ถูก

**คำถาม:** CS2 รอบรองเล่น BO3 หรือ BO1

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: รอบรอง, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: easy | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0148` sec

## 15. [PASS] ถูก

**คำถาม:** CS2 technical timeout กับ tactical timeout ต่างกันไงแบบสั้นๆ

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical, 2 ครั้ง, Tactical, 4 ครั้ง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: summary | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0187` sec

## 16. [FAIL] ผิด

**คำถาม:** CS2 ขอเวลานอกกลางรอบที่ยิงกันอยู่ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Freeze time | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: hard | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0102` sec
- missing_keywords: `['Freeze time']`

## 17. [FAIL] ผิด

**คำถาม:** CS2 hate speech หรือเหยียดศาสนาผิดไหม

**คำตอบ(จาก AI):**

PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**แหล่งข้อมูล:**

- [https://esports.computing.psu.ac.th/reservation](https://esports.computing.psu.ac.th/reservation) (`Reservation / reservation / Reservation`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, เกลียดชัง, ศาสนา | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `games` | intent: `games_lookup`
- mode: `pipeline:games_fast_path` | elapsed: `0.0132` sec
- missing_keywords: `['ห้าม', 'เกลียดชัง', 'ศาสนา']`
- missing_source_keywords: `['competition_rules_cs2_psu_phuket_2026']`

## 18. [PASS] ถูก

**คำถาม:** CS2 ใช้ config หรือ mod แปลก ๆ ในตัวเกมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
- 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s05_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ห้าม, ดัดแปลง | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: policy | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0337` sec

## 19. [FAIL] ผิด

**คำถาม:** CS2 มีแค่ 4 คนพอลงแข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s38_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s38_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s41_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s41_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0208` sec
- missing_keywords: `['ผู้เล่น 5 คน']`

## 20. [PASS] ถูก

**คำถาม:** Counter Strike รายการนี้แข่งในมอภูเก็ตใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s17_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s17_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PSU Esports Studio, ภูเก็ต | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: weird_user_question

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0214` sec
