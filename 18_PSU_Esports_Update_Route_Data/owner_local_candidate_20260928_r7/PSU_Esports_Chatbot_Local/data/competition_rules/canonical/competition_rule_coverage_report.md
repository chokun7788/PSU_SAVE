# Competition Rule Canonical Coverage

เอกสารนี้สร้างอัตโนมัติจากข้อมูลกติกาที่ระบบใช้อยู่เดิม เพื่อแสดงความครอบคลุมของรูปแบบกลาง ไม่ได้ยืนยันว่ากติกาแต่ละรายการได้รับการอนุมัติใหม่แล้ว.

## สถานะข้อมูล

- `present`: พบทั้ง Rule Record และ Fact Projection
- `partial`: พบอย่างน้อยหนึ่งชั้นข้อมูล แต่ควรเติมอีกชั้นก่อน publish release ใหม่
- `not_found`: ยังไม่พบข้อมูลหัวข้อนั้นในเอกสารที่นำเข้า ไม่ได้หมายความว่ากติกาอนุญาตหรือห้ามโดยปริยาย

## Release Safety

- Active releases: 0
- Inactive releases awaiting review: 4
- English fields awaiting approved localization: 104
- Release ที่ยัง inactive ห้ามถูกใช้ตอบว่าเป็นกติกาปัจจุบัน; ระบบต้องขอชื่อรายการ/ช่วงเวลาหรือ no-answer.

## หลักการใช้งาน

- `common` คือหัวข้อที่ทุกเกมใช้โครงเดียวกันได้
- โมดูลชื่อเกม เช่น `cs2_map_veto_and_side_selection` คือรายละเอียดเฉพาะเกมและเป็น optional module
- ไฟล์ต้นทางใน `data/competition_rules` ไม่ถูกแก้ไข; runtime เดิมยังอ่านไฟล์เดิมจนกว่าจะมีการอนุมัติและสลับ release แบบ atomic

## Counter-Strike 2

- Rule records: 58
- Fact projections: 27
- ต้องจัดหมวดเพิ่ม: Rule 0 / Fact 0
- Evidence: candidate_review_required=11, declared_chunk_reference_pending_text_check=2, document_level_only=14
- Fact คำตอบซ้ำที่ต้องรวม/ตรวจ: 0

| หัวข้อกลาง | สถานะ | Rule | Fact |
| --- | --- | ---: | ---: |
| ข้อมูลเอกสารและขอบเขต | partial | 3 | 0 |
| คุณสมบัติและการลงทะเบียน | present | 10 | 8 |
| รูปแบบการแข่งขัน | present | 4 | 1 |
| การตั้งค่าแมตช์ | present | 14 | 2 |
| ก่อนแข่งและหน้างาน | present | 8 | 3 |
| ระหว่างการแข่งขัน | present | 3 | 5 |
| ความเป็นธรรมและพฤติกรรม | partial | 9 | 0 |
| บทลงโทษ | present | 4 | 8 |
| การประท้วงและข้อพิพาท | partial | 3 | 0 |
| แหล่งอ้างอิงและประวัติการแก้ไข | not_found | 0 | 0 |

โมดูลเฉพาะเกมที่ตรวจพบ:
- `cs2_map_veto_and_side_selection` (4 rule records)
- `cs2_overtime` (1 rule records)

## Arena of Valor (RoV)

- Rule records: 12
- Fact projections: 50
- ต้องจัดหมวดเพิ่ม: Rule 0 / Fact 0
- Evidence: candidate_review_required=2, declared_chunk_reference_pending_text_check=7, document_level_only=41
- Fact คำตอบซ้ำที่ต้องรวม/ตรวจ: 0

| หัวข้อกลาง | สถานะ | Rule | Fact |
| --- | --- | ---: | ---: |
| ข้อมูลเอกสารและขอบเขต | partial | 2 | 0 |
| คุณสมบัติและการลงทะเบียน | present | 2 | 1 |
| รูปแบบการแข่งขัน | present | 1 | 5 |
| การตั้งค่าแมตช์ | present | 1 | 3 |
| ก่อนแข่งและหน้างาน | present | 1 | 11 |
| ระหว่างการแข่งขัน | present | 3 | 14 |
| ความเป็นธรรมและพฤติกรรม | partial | 2 | 0 |
| บทลงโทษ | partial | 0 | 16 |
| การประท้วงและข้อพิพาท | not_found | 0 | 0 |
| แหล่งอ้างอิงและประวัติการแก้ไข | not_found | 0 | 0 |

โมดูลเฉพาะเกมที่ตรวจพบ:
- `rov_break_time` (1 rule records)
- `rov_hero_and_skin` (3 rule records)

## Tekken 8

- Rule records: 8
- Fact projections: 34
- ต้องจัดหมวดเพิ่ม: Rule 0 / Fact 0
- Evidence: candidate_review_required=6, document_level_only=28
- Fact คำตอบซ้ำที่ต้องรวม/ตรวจ: 0

| หัวข้อกลาง | สถานะ | Rule | Fact |
| --- | --- | ---: | ---: |
| ข้อมูลเอกสารและขอบเขต | partial | 1 | 0 |
| คุณสมบัติและการลงทะเบียน | not_found | 0 | 0 |
| รูปแบบการแข่งขัน | present | 1 | 8 |
| การตั้งค่าแมตช์ | present | 2 | 13 |
| ก่อนแข่งและหน้างาน | partial | 0 | 3 |
| ระหว่างการแข่งขัน | present | 1 | 8 |
| ความเป็นธรรมและพฤติกรรม | partial | 0 | 2 |
| บทลงโทษ | not_found | 0 | 0 |
| การประท้วงและข้อพิพาท | partial | 3 | 0 |
| แหล่งอ้างอิงและประวัติการแก้ไข | not_found | 0 | 0 |

โมดูลเฉพาะเกมที่ตรวจพบ:
- `tekken8_character_and_stage` (2 rule records)

## VALORANT

- Rule records: 26
- Fact projections: 55
- ต้องจัดหมวดเพิ่ม: Rule 0 / Fact 0
- Evidence: candidate_review_required=9, document_level_only=46
- Fact คำตอบซ้ำที่ต้องรวม/ตรวจ: 4

| หัวข้อกลาง | สถานะ | Rule | Fact |
| --- | --- | ---: | ---: |
| ข้อมูลเอกสารและขอบเขต | not_found | 0 | 0 |
| คุณสมบัติและการลงทะเบียน | partial | 0 | 1 |
| รูปแบบการแข่งขัน | not_found | 0 | 0 |
| การตั้งค่าแมตช์ | present | 8 | 13 |
| ก่อนแข่งและหน้างาน | present | 3 | 10 |
| ระหว่างการแข่งขัน | present | 9 | 16 |
| ความเป็นธรรมและพฤติกรรม | present | 2 | 8 |
| บทลงโทษ | present | 4 | 7 |
| การประท้วงและข้อพิพาท | not_found | 0 | 0 |
| แหล่งอ้างอิงและประวัติการแก้ไข | not_found | 0 | 0 |

โมดูลเฉพาะเกมที่ตรวจพบ:
- `valorant_agent_selection` (4 rule records)
- `valorant_pause_taxonomy` (10 rule records)

## ขั้นตอนเมื่อต้องเพิ่มกติกาใหม่

1. เพิ่มเอกสารต้นทางและสร้าง chunk/fact card ตามกระบวนการเดิมใน staging.
2. รัน `py -3 tools/build_competition_rule_canonical.py --write` เพื่อสร้างมุมมองกลางใหม่.
3. ตรวจ `competition_rule_coverage.json`, `competition_rule_fact_projections.jsonl` และ evidence status; Fact ที่เป็น candidate/document-level ต้องได้รับ owner review ก่อน.
4. เติมวันที่มีผลและ approval ที่ hash ตรงกันใน `release_overrides.jsonl`; ห้ามแก้ generated registry โดยตรง.
5. สร้าง Structured/RAG projection จาก active release เดียวกัน แล้วจึงสลับ runtime แบบ atomic.
