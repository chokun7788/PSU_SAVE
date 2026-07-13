# Ground Truth Verbose Result

- Total: 228
- PASS: 203
- FAIL: 25
- ERROR: 0
- Pass rate: 89.04%
- Average latency: 0.0192s
- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_results_competition_rules_v1_228_verbose.jsonl`
- Report MD: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_verbose_report_competition_rules_v1_228_verbose.md`

## Mode Summary
- `pipeline:competition_fact_card`: 195
- `pipeline:rag_direct_curated`: 33

## Route Summary
- `competition_rules`: 228
## 1. [PASS] ถูก

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

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0129` sec

## 2. [PASS] ถูก

**คำถาม:** Counter-Strike 2 ทีมละกี่คนตามกติกา

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0079` sec

## 3. [PASS] ถูก

**คำถาม:** กติกา CS2 ต้องมีผู้เล่นกี่คนต่อทีม

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0119` sec

## 4. [PASS] ถูก

**คำถาม:** CS2 สมาชิกทีมต้องมีกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0106` sec

## 5. [PASS] ถูก

**คำถาม:** CS2 ลงแข่งพร้อมกันกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.008` sec

## 6. [PASS] ถูก

**คำถาม:** CS2 roster ผู้เล่นหลักมีกี่คน

**คำตอบ(จาก AI):**

คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
- 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s50_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s50_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s18_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s36_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s36_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.036` sec

## 7. [PASS] ถูก

**คำถาม:** รายการ PSU Phuket CS2 2026 ทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0193` sec

## 8. [PASS] ถูก

**คำถาม:** CS2 ต้องส่งผู้เล่นกี่คนในทีม

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0114` sec

## 9. [PASS] ถูก

**คำถาม:** CS2 แข่งแบบทีม 5 คนใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0147` sec

## 10. [PASS] ถูก

**คำถาม:** Counter Strike 2 ในรายการนี้ผู้เล่นต่อทีมกี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0111` sec

## 11. [PASS] ถูก

**คำถาม:** CS2 ถ้าถามเรื่องจำนวนคนในทีมตอบว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0141` sec

## 12. [PASS] ถูก

**คำถาม:** CS2 กติกาองค์ประกอบทีมกำหนดไว้กี่คน

**คำตอบ(จาก AI):**

คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน

หลักฐานจากกติกา:
- เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_team_size_players / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: CS2, ผู้เล่น 5 คน | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0126` sec

## 13. [PASS] ถูก

**คำถาม:** CS2 ใช้ map อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0189` sec

## 14. [PASS] ถูก

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

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.018` sec

## 15. [PASS] ถูก

**คำถาม:** CS2 แผนที่ที่ใช้แข่งมีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.017` sec

## 16. [PASS] ถูก

**คำถาม:** กติกา CS2 ระบุแผนที่อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0174` sec

## 17. [PASS] ถูก

**คำถาม:** PSU Phuket CS2 2026 ใช้แผนที่ไหน

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0159` sec

## 18. [PASS] ถูก

**คำถาม:** CS2 มี Ancient กับ Anubis ใน map pool ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.035` sec

## 19. [PASS] ถูก

**คำถาม:** CS2 รายการนี้ใช้ Dust 2 หรือ Train ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0293` sec

## 20. [PASS] ถูก

**คำถาม:** ขอรายชื่อ map ที่ใช้แข่ง CS2

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.025` sec

## 21. [PASS] ถูก

**คำถาม:** Counter-Strike 2 map pool ในกติกาคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0177` sec

## 22. [FAIL] ผิด

**คำถาม:** CS2 แข่งบนแผนที่อะไรได้บ้าง

**คำตอบ(จาก AI):**

คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
- 3. แผนที่ในการแข่งขัน
- 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s51_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s51_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s28_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s28_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0268` sec
- missing_keywords: `['Ancient', 'Anubis', 'Dust 2', 'Train']`

## 23. [PASS] ถูก

**คำถาม:** CS2 ban map จาก pool ไหน

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0197` sec

## 24. [PASS] ถูก

**คำถาม:** CS2 แผนที่ทั้งหมดตามกติกามีอะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

หลักฐานจากกติกา:
- เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_map_pool / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Ancient, Anubis, Dust 2, Train | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0116` sec

## 25. [PASS] ถูก

**คำถาม:** CS2 แข่งรูปแบบอะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0121` sec

## 26. [PASS] ถูก

**คำถาม:** CS2 เป็น Single Elimination ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0147` sec

## 27. [PASS] ถูก

**คำถาม:** CS2 รอบรองกับรอบชิงเป็น BO อะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.016` sec

## 28. [PASS] ถูก

**คำถาม:** กติกา CS2 format การแข่งขันเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0146` sec

## 29. [FAIL] ผิด

**คำถาม:** PSU Phuket CS2 2026 ใช้ระบบแข่งแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

รายละเอียดที่เกี่ยวข้อง:
- 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s04_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s38_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s38_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0203` sec
- missing_keywords: `['Single Elimination', 'BO3']`

## 30. [PASS] ถูก

**คำถาม:** CS2 รอบชิงใช้ BO3 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0117` sec

## 31. [FAIL] ผิด

**คำถาม:** CS2 รอบรองชนะเลิศแข่งกี่เกม

**คำตอบ(จาก AI):**

คำตอบ: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)

รายละเอียดที่เกี่ยวข้อง:
- กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2
- 3. รูปแบบการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s21_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s21_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s19_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s19_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0162` sec
- missing_keywords: `['Single Elimination']`

## 32. [PASS] ถูก

**คำถาม:** Counter-Strike 2 tournament format คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0137` sec

## 33. [PASS] ถูก

**คำถาม:** CS2 แข่งแพ้คัดออกหรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0098` sec

## 34. [FAIL] ผิด

**คำถาม:** CS2 รูปแบบทัวร์นาเมนต์ในเอกสารคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

รายละเอียดที่เกี่ยวข้อง:
- 1. รูปแบบทัวร์นาเมนต์ Single Elimination
- กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s20_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s20_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s52_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s52_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0168` sec
- missing_keywords: `['BO3']`

## 35. [PASS] ถูก

**คำถาม:** CS2 รอบสำคัญเป็น Best of 3 ไหม

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 36. [PASS] ถูก

**คำถาม:** CS2 กติกาบอกว่า single elimination หรือไม่

**คำตอบ(จาก AI):**

คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)

หลักฐานจากกติกา:
- เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_format_single_elim_bo3 / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Single Elimination, BO3 | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0177` sec

## 37. [PASS] ถูก

**คำถาม:** CS2 technical pause ได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 38. [PASS] ถูก

**คำถาม:** CS2 tactical timeout ได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0134` sec

## 39. [PASS] ถูก

**คำถาม:** CS2 pause ได้กี่ครั้งตามกติกา

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0072` sec

## 40. [PASS] ถูก

**คำถาม:** CS2 ขอหยุดเกม technical ได้กี่ครั้งและกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0216` sec

## 41. [PASS] ถูก

**คำถาม:** กติกา CS2 tactical timeout ครั้งละกี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 42. [PASS] ถูก

**คำถาม:** CS2 Technical Pause รวมได้ไม่เกินกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 43. [FAIL] ผิด

**คำถาม:** CS2 เวลานอก tactical timeout ได้ทีมละกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s34_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s34_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s33_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s33_c01`)
- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`competition_rules_cs2_psu_phuket_2026_s27_c01 / competition_rules / competition_rules_cs2_psu_phuket_2026, competition_rules_cs2_psu_phuket_2026_s27_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0232` sec
- missing_keywords: `['Technical Pause', '2 ครั้ง', '10 นาที', 'Tactical Timeout']`

## 44. [PASS] ถูก

**คำถาม:** CS2 ถ้าเครื่องมีปัญหาขอ pause ได้เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0161` sec

## 45. [PASS] ถูก

**คำถาม:** Counter-Strike 2 pause policy เป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0342` sec

## 46. [PASS] ถูก

**คำถาม:** CS2 technical กับ tactical timeout ต่างกันยังไงในกติกา

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0506` sec

## 47. [PASS] ถูก

**คำถาม:** CS2 ขอ Tactical Timeout 4 ครั้งใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0293` sec

## 48. [PASS] ถูก

**คำถาม:** CS2 หยุดเกมได้กี่ครั้งและใช้เวลากี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

หลักฐานจากกติกา:
- เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_cs2_psu_phuket_2026` (`cs2_pause_policy / competition_rules / competition_rules_cs2_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที | Expected source keywords: competition_rules_cs2_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_cs2_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0236` sec

## 49. [PASS] ถูก

**คำถาม:** VALORANT แข่งทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0229` sec

## 50. [PASS] ถูก

**คำถาม:** วาโลทีมละกี่คนตามกติกา

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0135` sec

## 51. [PASS] ถูก

**คำถาม:** VALORANT สมาชิกทีมกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 52. [PASS] ถูก

**คำถาม:** กติกา VALORANT ต้องมีผู้เล่นกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0284` sec

## 53. [PASS] ถูก

**คำถาม:** PSU Phuket VALORANT 2026 แข่งทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0263` sec

## 54. [PASS] ถูก

**คำถาม:** VALORANT ลงแข่งพร้อมกันกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0175` sec

## 55. [PASS] ถูก

**คำถาม:** วาโลผู้เล่นตัวจริงกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0153` sec

## 56. [PASS] ถูก

**คำถาม:** VALORANT ทีม 5 คนใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0255` sec

## 57. [PASS] ถูก

**คำถาม:** VALORANT roster ตัวจริงกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0228` sec

## 58. [PASS] ถูก

**คำถาม:** กฎแข่งวาโลจำนวนผู้เล่นต่อทีมคือเท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0183` sec

## 59. [PASS] ถูก

**คำถาม:** VALORANT ในรายการนี้ใช้ทีมละกี่คน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0175` sec

## 60. [PASS] ถูก

**คำถาม:** วาโลแข่งแบบกี่คนต่อทีม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน

หลักฐานจากกติกา:
- เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_team_size_players / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: VALORANT, 5 คน | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0138` sec

## 61. [PASS] ถูก

**คำถาม:** VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0201` sec

## 62. [PASS] ถูก

**คำถาม:** VALORANT map pool มีอะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0178` sec

## 63. [PASS] ถูก

**คำถาม:** วาโลใช้ map อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0159` sec

## 64. [PASS] ถูก

**คำถาม:** กติกา VALORANT ระบุแผนที่อะไรบ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0212` sec

## 65. [PASS] ถูก

**คำถาม:** PSU Phuket VALORANT 2026 ใช้ map ไหน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0211` sec

## 66. [PASS] ถูก

**คำถาม:** VALORANT มี Abyss กับ Ascent ใน map pool ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0306` sec

## 67. [PASS] ถูก

**คำถาม:** วาโลแข่งบน Sunset ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0187` sec

## 68. [PASS] ถูก

**คำถาม:** ขอรายชื่อแผนที่แข่ง VALORANT

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0148` sec

## 69. [PASS] ถูก

**คำถาม:** VALORANT map pool ทั้งหมดมีอะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 70. [PASS] ถูก

**คำถาม:** วาโล ban map จากแผนที่ชุดไหน

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0178` sec

## 71. [PASS] ถูก

**คำถาม:** VALORANT แข่งแผนที่อะไรได้บ้าง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0154` sec

## 72. [PASS] ถูก

**คำถาม:** กฎวาโลเรื่อง map pool คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

หลักฐานจากกติกา:
- เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_map_pool / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Abyss, Ascent, Sunset | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_map_pool

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0186` sec

## 73. [PASS] ถูก

**คำถาม:** VALORANT Tactical Timeout ขอได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0182` sec

## 74. [PASS] ถูก

**คำถาม:** วาโล timeout ได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0146` sec

## 75. [PASS] ถูก

**คำถาม:** VALORANT เวลานอกได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 76. [PASS] ถูก

**คำถาม:** VALORANT tactical timeout ครั้งละกี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0227` sec

## 77. [PASS] ถูก

**คำถาม:** กติกา VALORANT timeout ต่อแผนที่ได้เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0179` sec

## 78. [FAIL] ผิด

**คำถาม:** VALORANT เข้า Overtime ได้ timeout เพิ่มไหม

**คำตอบ(จาก AI):**

คำตอบ: * เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

รายละเอียดที่เกี่ยวข้อง:
- During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over.
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
- ขอได้ 1 ครั้งต่อแผนที่
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s21_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s21_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0252` sec
- missing_keywords: `['Tactical Timeout']`

## 79. [FAIL] ผิด

**คำถาม:** วาโล Tactical Timeout ได้ทีมละกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0274` sec
- missing_keywords: `['Tactical Timeout', '2 ครั้ง', '60 วินาที', 'Overtime']`

## 80. [PASS] ถูก

**คำถาม:** VALORANT ขอเวลานอก 60 วินาทีใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0272` sec

## 81. [PASS] ถูก

**คำถาม:** VALORANT timeout ในรอบปกติได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0196` sec

## 82. [PASS] ถูก

**คำถาม:** PSU Phuket VALORANT 2026 tactical timeout rule คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0217` sec

## 83. [PASS] ถูก

**คำถาม:** วาโลเวลานอก tactical ต่อ map ได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: * ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
- ขอได้ 1 ครั้งต่อแผนที่
- 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0282` sec

## 84. [PASS] ถูก

**คำถาม:** VALORANT ถามเรื่อง tactical timeout ให้ตอบยังไง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข้าสู่ Overtime จะได้รับ Tactical Timeout เพิ่ม 1 ครั้ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_tactical_timeout / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0223` sec

## 85. [PASS] ถูก

**คำถาม:** VALORANT emergency pause ได้กี่ครั้ง

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

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.023` sec

## 86. [PASS] ถูก

**คำถาม:** VALORANT technical pause รวมได้กี่นาที

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.019` sec

## 87. [PASS] ถูก

**คำถาม:** VALORANT pause ฉุกเฉินได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0166` sec

## 88. [PASS] ถูก

**คำถาม:** วาโลหลุดเกมขอ emergency pause ได้เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause)

รายละเอียดที่เกี่ยวข้อง:
- 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- ขอได้ 1 ครั้งต่อแผนที่
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0272` sec

## 89. [FAIL] ผิด

**คำถาม:** กติกา VALORANT หยุดฉุกเฉินได้ทีมละกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0258` sec
- missing_keywords: `['Emergency', '1 ครั้ง', '10 นาที']`

## 90. [PASS] ถูก

**คำถาม:** VALORANT technical pause สูงสุดกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: * ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- ขอได้ 1 ครั้งต่อแผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0256` sec

## 91. [PASS] ถูก

**คำถาม:** VALORANT Emergency Pause ต่อแผนที่ได้กี่ครั้ง

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

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0285` sec

## 92. [PASS] ถูก

**คำถาม:** วาโลหยุดเกมฉุกเฉินรวมกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0097` sec

## 93. [PASS] ถูก

**คำถาม:** VALORANT ถ้า hardware มีปัญหาขอ pause ยังไง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0231` sec

## 94. [FAIL] ผิด

**คำถาม:** VALORANT emergency pause policy คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)

รายละเอียดที่เกี่ยวข้อง:
- 3. Player Emergency Pause
- Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
- Each team may request 1 pause per map.
- การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- ขอได้ 1 ครั้งต่อแผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s23_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s23_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s05_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0287` sec
- missing_keywords: `['10 นาที']`

## 95. [PASS] ถูก

**คำถาม:** วาโล technical pause 10 นาทีใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0181` sec

## 96. [PASS] ถูก

**คำถาม:** VALORANT pause ฉุกเฉินตามกฎตอบว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_emergency_pause / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Emergency, 1 ครั้ง, 10 นาที | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0159` sec

## 97. [PASS] ถูก

**คำถาม:** VALORANT agent ใหม่ใช้ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0238` sec

## 98. [PASS] ถูก

**คำถาม:** VALORANT map ใหม่ใช้ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.018` sec

## 99. [PASS] ถูก

**คำถาม:** วาโลเอเจนท์ใหม่ใช้แข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0122` sec

## 100. [PASS] ถูก

**คำถาม:** กติกา VALORANT agent ใหม่ต้องรอกี่สัปดาห์

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0203` sec

## 101. [PASS] ถูก

**คำถาม:** VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนแข่ง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0171` sec

## 102. [PASS] ถูก

**คำถาม:** VALORANT ใช้เอเจนท์ที่เพิ่งออกใหม่ได้ทันทีไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0195` sec

## 103. [PASS] ถูก

**คำถาม:** วาโล map ใหม่ใช้แข่งได้เลยหรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0221` sec

## 104. [PASS] ถูก

**คำถาม:** VALORANT new agent restriction คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0252` sec

## 105. [PASS] ถูก

**คำถาม:** VALORANT new map restriction ในกติกาคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0297` sec

## 106. [PASS] ถูก

**คำถาม:** วาโล agent ใหม่รอ 2 สัปดาห์ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0283` sec

## 107. [PASS] ถูก

**คำถาม:** VALORANT map ใหม่รอ 4 สัปดาห์ไหม

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0289` sec

## 108. [PASS] ถูก

**คำถาม:** กฎวาโลเรื่อง content ใหม่เป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง

หลักฐานจากกติกา:
- เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`valorant_agent_map_restriction / competition_rules / competition_rules_valorant_psu_phuket_2026`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Agent, 2 สัปดาห์, 4 สัปดาห์ | Expected source keywords: competition_rules_valorant_psu_phuket_2026 | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_valorant_psu_phuket_2026']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0243` sec

## 109. [PASS] ถูก

**คำถาม:** สมาชิกในทีม ROV ต้องมีกี่คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0296` sec

## 110. [PASS] ถูก

**คำถาม:** RoV ทีมละกี่คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0136` sec

## 111. [PASS] ถูก

**คำถาม:** ROV แข่งกี่คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0132` sec

## 112. [PASS] ถูก

**คำถาม:** สมาชิกในทีม RoV กี่คนตามกติกา

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0122` sec

## 113. [PASS] ถูก

**คำถาม:** กติกา RoV บอกว่าลงแข่งฝ่ายละกี่คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0156` sec

## 114. [PASS] ถูก

**คำถาม:** RoV เป็น 5v5 ใช่ไหม

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0142` sec

## 115. [PASS] ถูก

**คำถาม:** Blueket Games RoV ทีมละกี่คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 116. [FAIL] ผิด

**คำถาม:** RoV roster รวมมีกี่คนในไฟล์กติกา

**คำตอบ(จาก AI):**

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
- 4.1. กติกาพื้นฐาน
- 4.2. กติกาการแข่งขัน
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- กติกาการแข่งขัน Blueket Games 2025
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s01_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s01_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0252` sec
- missing_keywords: `['ฝ่ายละ 5 คน', 'ยังไม่พบจำนวนสมาชิกทีม']`

## 117. [PASS] ถูก

**คำถาม:** ROV มีตัวสำรองกี่คนในเอกสาร

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0174` sec

## 118. [PASS] ถูก

**คำถาม:** RoV ถามจำนวนสมาชิกทีมควรตอบยังไง

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0151` sec

## 119. [FAIL] ผิด

**คำถาม:** Arena of Valor แข่งโหมดกี่ต่อกี่

**คำตอบ(จาก AI):**

คำตอบ: * แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive

รายละเอียดที่เกี่ยวข้อง:
- เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- New agents are restricted for approximately 2 weeks after being released in Competitive mode.
- New maps are restricted for approximately 4 weeks after being released in Competitive mode.
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s18_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s18_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0219` sec
- missing_keywords: `['5v5', 'ฝ่ายละ 5 คน', 'ยังไม่พบจำนวนสมาชิกทีม']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 120. [PASS] ถูก

**คำถาม:** RoV ยืนยันได้ไหมว่าลงแข่งฝ่ายละ 5 คน

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

ต้องมีคำสำคัญ: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: inferred_fact | ระดับ: hard | variant: competition_team_size

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0231` sec

## 121. [PASS] ถูก

**คำถาม:** RoV ใช้สกินได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0163` sec

## 122. [PASS] ถูก

**คำถาม:** ROV ใช้ skin ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.017` sec

## 123. [PASS] ถูก

**คำถาม:** RoV ต้องใช้สกินอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0116` sec

## 124. [PASS] ถูก

**คำถาม:** กติกา RoV อนุญาตให้ใช้สกินไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0154` sec

## 125. [PASS] ถูก

**คำถาม:** Blueket Games RoV ใช้ Default Skin ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0229` sec

## 126. [PASS] ถูก

**คำถาม:** RoV ห้ามใช้สกินอื่นไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0132` sec

## 127. [FAIL] ผิด

**คำถาม:** Arena of Valor แข่งต้องใช้ skin แบบไหน

**คำตอบ(จาก AI):**

คำตอบ: กฎระเบียบและรูปแบบการแข่งขัน VALORANT

รายละเอียดที่เกี่ยวข้อง:
- ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
- ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
- ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0249` sec
- missing_keywords: `['Default Skin']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 128. [PASS] ถูก

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

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0132` sec

## 129. [PASS] ถูก

**คำถาม:** กฎ RoV เรื่องสกินคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0212` sec

## 130. [PASS] ถูก

**คำถาม:** ROV default skin เท่านั้นไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 131. [PASS] ถูก

**คำถาม:** RoV ถ้าใช้สกินนอก default ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0172` sec

## 132. [PASS] ถูก

**คำถาม:** RoV ในรายการนี้สกินต้องเป็นอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_skin_default_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: Default Skin | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_skin

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0135` sec

## 133. [PASS] ถูก

**คำถาม:** RoV ถ้าเริ่มแข่งช้าเกิน 15 นาทีโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0193` sec

## 134. [PASS] ถูก

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

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0229` sec

## 135. [PASS] ถูก

**คำถาม:** ROV late start 15 นาที

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0222` sec

## 136. [PASS] ถูก

**คำถาม:** กติกา RoV เริ่มแข่งล่าช้าเกิน 15 นาทีลงโทษยังไง

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0211` sec

## 137. [PASS] ถูก

**คำถาม:** Blueket Games RoV ถ้ามาสายโดนปรับแพ้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0219` sec

## 138. [PASS] ถูก

**คำถาม:** RoV ถ้าทีมทำให้เริ่มช้าจะโดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0116` sec

## 139. [PASS] ถูก

**คำถาม:** RoV เริ่มช้ากี่นาทีถึงปรับแพ้

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0141` sec

## 140. [FAIL] ผิด

**คำถาม:** Arena of Valor ล่าช้า 15 นาทีตามกฎเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: * การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที

รายละเอียดที่เกี่ยวข้อง:
- การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที
- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s04_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s04_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0202` sec
- missing_keywords: `['15 นาที']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 141. [PASS] ถูก

**คำถาม:** RoV แข่งช้าเกินเวลาที่กำหนดถูกปรับแพ้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0168` sec

## 142. [PASS] ถูก

**คำถาม:** ROV ถ้าเริ่ม match ไม่ทัน 15 นาทีตอบว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0233` sec

## 143. [PASS] ถูก

**คำถาม:** กฎ RoV เรื่องมาสายคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.02` sec

## 144. [PASS] ถูก

**คำถาม:** RoV late start rule ในเอกสารคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น

หลักฐานจากกติกา:
- เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_late_start_forfeit / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 15 นาที, ปรับแพ้ | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_late_start

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0211` sec

## 145. [PASS] ถูก

**คำถาม:** RoV pause ได้กี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 146. [PASS] ถูก

**คำถาม:** RoV หลุดเกมหยุดได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0165` sec

## 147. [PASS] ถูก

**คำถาม:** RoV disconnect ทำยังไง

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0183` sec

## 148. [FAIL] ผิด

**คำถาม:** กติกา RoV หยุดเกมได้ทีมละกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้

รายละเอียดที่เกี่ยวข้อง:
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0231` sec
- missing_keywords: `['5 ครั้ง', '1 นาที']`

## 149. [PASS] ถูก

**คำถาม:** RoV pause ครั้งละกี่นาที

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0177` sec

## 150. [PASS] ถูก

**คำถาม:** Blueket Games RoV ถ้าเกมหลุดขอหยุดได้เท่าไหร่

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0224` sec

## 151. [PASS] ถูก

**คำถาม:** RoV แต่ละทีมมีสิทธิ์หยุดเกมกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0143` sec

## 152. [FAIL] ผิด

**คำถาม:** Arena of Valor pause ได้สูงสุดกี่ครั้ง

**คำตอบ(จาก AI):**

คำตอบ: * เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

รายละเอียดที่เกี่ยวข้อง:
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
- ขอได้ 1 ครั้งต่อแผนที่
- 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
- 2. การหยุดเกมทางเทคนิค (Technical Pause)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0287` sec
- missing_keywords: `['5 ครั้ง', '1 นาที']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 153. [PASS] ถูก

**คำถาม:** RoV หยุดเกมได้ 5 ครั้งใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0283` sec

## 154. [PASS] ถูก

**คำถาม:** ROV pause 1 นาทีต่อครั้งใช่หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0253` sec

## 155. [PASS] ถูก

**คำถาม:** RoV disconnect แล้วกลับมาเล่นต่อเมื่อไหร่

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0216` sec

## 156. [PASS] ถูก

**คำถาม:** กฎ RoV เรื่อง pause/disconnect คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ

หลักฐานจากกติกา:
- เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_pause_disconnect / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 5 ครั้ง, 1 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0298` sec

## 157. [PASS] ถูก

**คำถาม:** RoV ขอเริ่มใหม่ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 158. [PASS] ถูก

**คำถาม:** RoV ก่อน first blood remake ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0268` sec

## 159. [PASS] ถูก

**คำถาม:** RoV แข่งใหม่ได้ตอนไหน

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0209` sec

## 160. [PASS] ถูก

**คำถาม:** กติกา RoV rematch ทำได้เมื่อไหร่

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0188` sec

## 161. [PASS] ถูก

**คำถาม:** RoV ขอแข่งใหม่ก่อน 2 นาทีได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0222` sec

## 162. [PASS] ถูก

**คำถาม:** Blueket Games RoV ถ้าเกิด First Blood แล้ว remake ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ

รายละเอียดที่เกี่ยวข้อง:
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
- 4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0352` sec

## 163. [FAIL] ผิด

**คำถาม:** Arena of Valor เริ่มใหม่ได้ก่อน First Blood ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)

รายละเอียดที่เกี่ยวข้อง:
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
- เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s08_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s08_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s03_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s03_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s06_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0279` sec
- missing_keywords: `['First Blood', '2 นาที']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 164. [PASS] ถูก

**คำถาม:** RoV ถ้าเกิน 2 นาทีแล้วขอแข่งใหม่ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0181` sec

## 165. [PASS] ถูก

**คำถาม:** RoV ต้องให้ฝ่ายตรงข้ามยินยอมเมื่อไหร่

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0152` sec

## 166. [FAIL] ผิด

**คำถาม:** ROV rematch rule ตามเอกสารคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ

รายละเอียดที่เกี่ยวข้อง:
- 4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
- 4.5.5.1. หากผู้เข้าแข่งขันรายใดตกอยู่ในสภาวะที่เป็นอันตรายต่อชีวิต กล่าวคือ ไม่มีความปลอดภัยในการบริเวณการแข่งขัน หรือตกอยู่ในสถานการณ์อื่นใดที่ทำให้เกิดปัญหาในการดำเนินเกมต่อไป
- 4.3. การหลุดออกจากเกม (Disconnect) และการเริ่มเกมใหม่ (Rematch)
- 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
- 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s01_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s01_c01`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c01 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.027` sec
- missing_keywords: `['First Blood', '2 นาที']`

## 167. [PASS] ถูก

**คำถาม:** RoV remake ก่อน First Blood และก่อน 2 นาทีใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่

รายละเอียดที่เกี่ยวข้อง:
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
- 4.5.6.1.1. มีการรบกวนทางกายภาพระหว่างผู้เข้าแข่งขัน เช่น การก่อความวุ่นวาย ความโกลาหล และเสียงดังซึ่งรบกวนเกม เป็นต้น
- 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
- 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c02 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c02`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c03 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c03`)
- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`competition_rules_rov_blueket_2025_men_s06_c04 / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s06_c04`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0364` sec

## 168. [PASS] ถูก

**คำถาม:** กฎ RoV เรื่องขอแข่งใหม่ตอบยังไง

**คำตอบ(จาก AI):**

คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน

หลักฐานจากกติกา:
- เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้นโดยฝ่ายตรงข้าม/ผู้ตัดสิน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_rematch_first_blood / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: First Blood, 2 นาที | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_rematch

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 169. [PASS] ถูก

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

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0135` sec

## 170. [PASS] ถูก

**คำถาม:** RoV ใช้ iPad แข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0169` sec

## 171. [PASS] ถูก

**คำถาม:** RoV ใช้ tablet ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0149` sec

## 172. [PASS] ถูก

**คำถาม:** RoV แข่งด้วยเครื่องอะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.014` sec

## 173. [PASS] ถูก

**คำถาม:** กติกา RoV ต้องใช้มือถือไหม

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0146` sec

## 174. [PASS] ถูก

**คำถาม:** Blueket Games RoV อนุญาต iPad หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0208` sec

## 175. [FAIL] ผิด

**คำถาม:** Arena of Valor แข่งด้วยโทรศัพท์มือถือเท่านั้นไหม

**คำตอบ(จาก AI):**

คำตอบ: * อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
- เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
- อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)
- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
- ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
- พื้นที่การแข่งขันและกฎระเบียบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s02_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s02_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s01_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s01_c01`)
- `local://competition_rules/competition_rules_valorant_psu_phuket_2026` (`competition_rules_valorant_psu_phuket_2026_s07_c01 / competition_rules / competition_rules_valorant_psu_phuket_2026, competition_rules_valorant_psu_phuket_2026_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `False` | matched: `[]`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0245` sec
- missing_keywords: `['ไม่อนุญาต', 'Tablet', 'iPad']`
- missing_source_keywords: `['competition_rules_rov_blueket_2025_men']`

## 176. [PASS] ถูก

**คำถาม:** RoV ใช้ Tablet ในการแข่งขันได้หรือไม่

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0174` sec

## 177. [FAIL] ผิด

**คำถาม:** ROV device rule คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ

หลักฐานจากกติกา:
- เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_format_bo3_all_rounds / competition_rules / competition_rules_rov_blueket_2025_men, competition_rules_rov_blueket_2025_men_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0152` sec
- missing_keywords: `['โทรศัพท์มือถือ', 'ไม่อนุญาต', 'Tablet', 'iPad']`

## 178. [PASS] ถูก

**คำถาม:** RoV อุปกรณ์ที่ใช้แข่งกำหนดยังไง

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.014` sec

## 179. [PASS] ถูก

**คำถาม:** RoV ถ้าจะใช้ iPad ต้องได้ไหมตามกฎ

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0127` sec

## 180. [PASS] ถูก

**คำถาม:** กฎ RoV เรื่องอุปกรณ์แข่งคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad

หลักฐานจากกติกา:
- เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_rov_blueket_2025_men` (`rov_device_mobile_only / competition_rules / competition_rules_rov_blueket_2025_men`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad | Expected source keywords: competition_rules_rov_blueket_2025_men | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_rov_blueket_2025_men']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0201` sec

## 181. [PASS] ถูก

**คำถาม:** Tekken 8 เล่นแบบไหน

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0175` sec

## 182. [PASS] ถูก

**คำถาม:** Tekken 8 รูปแบบการแข่งขัน

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0129` sec

## 183. [PASS] ถูก

**คำถาม:** Tekken 8 แข่งกี่ต่อกี่

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0173` sec

## 184. [PASS] ถูก

**คำถาม:** กติกา Tekken 8 ใช้ format อะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0181` sec

## 185. [PASS] ถูก

**คำถาม:** Tekken 8 เป็น 1v1 ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0174` sec

## 186. [PASS] ถูก

**คำถาม:** Tekken 8 FT2 คือรูปแบบแข่งใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0187` sec

## 187. [FAIL] ผิด

**คำถาม:** Tekken 8 แข่งบน PS5 และเวลา 60 วินาทีไหม

**คำตอบ(จาก AI):**

คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

รายละเอียดที่เกี่ยวข้อง:
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน
- เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
- ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
- แข่งขันแบบ ออฟไลน์ (Offline)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s04_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s04_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0322` sec
- missing_keywords: `['1v1', 'PlayStation 5', 'FT2']`

## 188. [PASS] ถูก

**คำถาม:** PSU Esports Tekken 8 แข่งแบบ offline หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0219` sec

## 189. [PASS] ถูก

**คำถาม:** Tekken 8 รอบหนึ่งตั้งเวลากี่วินาที

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0126` sec

## 190. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ Round 3 ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0454` sec

## 191. [FAIL] ผิด

**คำถาม:** Tekken 8 format ในเอกสารคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: * ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด

รายละเอียดที่เกี่ยวข้อง:
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
- กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ
- แข่งขันแบบ ออฟไลน์ (Offline)
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s01_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s01_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0587` sec
- missing_keywords: `['1v1', 'PlayStation 5']`

## 192. [PASS] ถูก

**คำถาม:** Tekken 8 กติกาการแข่งขันสรุปยังไง

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที

หลักฐานจากกติกา:
- เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_format_ps5_1v1 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: 1v1, PlayStation 5, FT2, 60 วินาที | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_format

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0198` sec

## 193. [PASS] ถูก

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

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0153` sec

## 194. [PASS] ถูก

**คำถาม:** Tekken 8 แข่งบนอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0104` sec

## 195. [PASS] ถูก

**คำถาม:** Tekken 8 platform อะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0162` sec

## 196. [PASS] ถูก

**คำถาม:** กติกา Tekken 8 ระบุเครื่องแข่งว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0227` sec

## 197. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ PS5 แข่งใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0201` sec

## 198. [PASS] ถูก

**คำถาม:** PSU Esports Tekken 8 ใช้ PlayStation 5 หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.026` sec

## 199. [PASS] ถูก

**คำถาม:** Tekken 8 อุปกรณ์หลักที่ใช้แข่งคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0146` sec

## 200. [PASS] ถูก

**คำถาม:** Tekken 8 แข่งด้วยเครื่องเกมอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.011` sec

## 201. [PASS] ถูก

**คำถาม:** Tekken 8 platform ตามเอกสารคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0193` sec

## 202. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ console อะไรในการแข่ง

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0158` sec

## 203. [PASS] ถูก

**คำถาม:** Tekken 8 ต้องเล่นบน PlayStation 5 ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 204. [PASS] ถูก

**คำถาม:** กฎ Tekken 8 เรื่อง platform คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5

หลักฐานจากกติกา:
- เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_equipment_ps5 / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: PlayStation 5 | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_equipment

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0164` sec

## 205. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ DLC character ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0147` sec

## 206. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ตัวละคร DLC ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0144` sec

## 207. [PASS] ถูก

**คำถาม:** Tekken 8 เลือกตัวละครอะไรได้บ้าง

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0119` sec

## 208. [PASS] ถูก

**คำถาม:** กติกา Tekken 8 ห้าม DLC ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0163` sec

## 209. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ customization ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0147` sec

## 210. [PASS] ถูก

**คำถาม:** Tekken 8 ใช้ชุดแต่งตัวละครได้หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0125` sec

## 211. [PASS] ถูก

**คำถาม:** PSU Esports Tekken 8 ตัวละคร DLC แข่งได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0184` sec

## 212. [FAIL] ผิด

**คำถาม:** Tekken 8 ใช้ skin custom ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

รายละเอียดที่เกี่ยวข้อง:
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
- เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ต้องใช้ สกินมาตรฐาน เท่านั้น

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s08_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s08_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_character

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0188` sec
- missing_keywords: `['ยกเว้นตัวละคร DLC', 'Customization']`

## 213. [PASS] ถูก

**คำถาม:** Tekken 8 character rule คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0152` sec

## 214. [PASS] ถูก

**คำถาม:** Tekken 8 เลือกได้ทุกตัวยกเว้น DLC ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0168` sec

## 215. [PASS] ถูก

**คำถาม:** Tekken 8 ห้าม customization ตามกฎหรือไม่

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน

หลักฐานจากกติกา:
- เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_character_dlc_rule / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0106` sec

## 216. [FAIL] ผิด

**คำถาม:** กฎ Tekken 8 เรื่องตัวละครและสกินคืออะไร

**คำตอบ(จาก AI):**

คำตอบ: * ต้องใช้ สกินมาตรฐาน เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
- สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ใช้เครื่องเกม PlayStation 5
- ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s06_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s06_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ยกเว้นตัวละคร DLC, Customization | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_character

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0211` sec
- missing_keywords: `['ยกเว้นตัวละคร DLC', 'Customization']`

## 217. [PASS] ถูก

**คำถาม:** Tekken 8 pause ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0121` sec

## 218. [PASS] ถูก

**คำถาม:** Tekken 8 หยุดเกมได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0126` sec

## 219. [PASS] ถูก

**คำถาม:** Tekken 8 กด pause โดนอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0142` sec

## 220. [PASS] ถูก

**คำถาม:** กติกา Tekken 8 ถ้ากด pause หลังเริ่มเกมเป็นยังไง

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0178` sec

## 221. [PASS] ถูก

**คำถาม:** Tekken 8 ตั้งใจกดหยุดเกมโดนปรับแพ้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0142` sec

## 222. [FAIL] ผิด

**คำถาม:** Tekken 8 pause แล้วแพ้ 1 Round ใช่ไหม

**คำตอบ(จาก AI):**

คำตอบ: * เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ

รายละเอียดที่เกี่ยวข้อง:
- กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ
- FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s02_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s02_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s01_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s01_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0207` sec
- missing_keywords: `['ไม่อนุญาต', 'Pause', 'แพ้ 1 Round']`

## 223. [PASS] ถูก

**คำถาม:** PSU Esports Tekken 8 ห้าม pause หรือเปล่า

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0189` sec

## 224. [PASS] ถูก

**คำถาม:** Tekken 8 หยุดเกมได้เฉพาะกรณีไหน

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: medium | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0122` sec

## 225. [PASS] ถูก

**คำถาม:** Tekken 8 ถ้าทั้งสองฝ่ายยินยอม pause ได้ไหม

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0162` sec

## 226. [PASS] ถูก

**คำถาม:** Tekken 8 pause penalty คืออะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0155` sec

## 227. [FAIL] ผิด

**คำถาม:** Tekken 8 กด pause ระหว่างแข่งลงโทษยังไง

**คำตอบ(จาก AI):**

คำตอบ: * ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ

รายละเอียดที่เกี่ยวข้อง:
- หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
- ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
- การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s07_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s07_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s03_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s03_c01`)
- `local://competition_rules/competition_rules_tekken8_psu_esports` (`competition_rules_tekken8_psu_esports_s05_c01 / competition_rules / competition_rules_tekken8_psu_esports, competition_rules_tekken8_psu_esports_s05_c01`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ผิด
- keyword_ok: `False`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:rag_direct_curated` | elapsed: `0.0172` sec
- missing_keywords: `['ไม่อนุญาต', 'แพ้ 1 Round']`

## 228. [PASS] ถูก

**คำถาม:** กฎ Tekken 8 เรื่อง pause ตอบว่าอะไร

**คำตอบ(จาก AI):**

คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร

หลักฐานจากกติกา:
- เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอม/มีเหตุผลสมควร

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

**แหล่งข้อมูล:**

- `local://competition_rules/competition_rules_tekken8_psu_esports` (`tekken8_pause_penalty / competition_rules / competition_rules_tekken8_psu_esports`)

**เฉลย/เกณฑ์ที่ถูก:**

ต้องมีคำสำคัญ: ไม่อนุญาต, Pause, แพ้ 1 Round | Expected source keywords: competition_rules_tekken8_psu_esports | หมวด: competition_rules | ชนิดคำตอบ: fact | ระดับ: hard | variant: competition_pause

**ผลตรวจ:**

- สถานะ: ถูก
- keyword_ok: `True`
- source_ok: `True` | matched: `['competition_rules_tekken8_psu_esports']`
- quality_ok: `True`
- validation_ok: `True`
- route: `competition_rules` | intent: `competition_rules_lookup`
- mode: `pipeline:competition_fact_card` | elapsed: `0.0163` sec
