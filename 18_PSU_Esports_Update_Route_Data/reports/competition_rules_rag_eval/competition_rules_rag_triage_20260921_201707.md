# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260921_201631.json`
- `competition_rules_rag_eval_20260921_201611.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 108 | 141 | 33 |
| th | 113 | 141 | 28 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `source_coverage_gap` | 36 | The selected rulebook has no retrieved section that directly proves the requested facet. |
| `english_localization_gap` | 15 | The Thai target source was found, but no approved English overlay was available. |
| `gold_or_section_contract_gap` | 10 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |

## Review Queue

### en / english_localization_gap / disconnect (3 cases)

- `COMP-RAG-V2-EN-070` — What happens if someone disconnects in Arena of Valor?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Arena of Valor (RoV) competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competi...
- `COMP-RAG-V2-EN-071` — Can a Arena of Valor match restart after a connection loss?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Arena of Valor (RoV) competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competi...
- `COMP-RAG-V2-EN-072` — How do Arena of Valor rules handle an internet disconnection?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Arena of Valor (RoV) competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competi...

### en / english_localization_gap / fair_play_conduct (3 cases)

- `COMP-RAG-V2-EN-016` — What fair-play rules apply to Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-017` — Which unsporting behaviours are prohibited in Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-018` — Where can I check the sportsmanship rules for Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...

### en / english_localization_gap / pause_timeout (3 cases)

- `COMP-RAG-V2-EN-064` — Could you compare the pause rules for CS2 and VALORANT?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-065` — Do CS2 and VALORANT handle an in-match pause differently?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-066` — I want to compare timeout rules between CS2 and VALORANT.
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...

### en / english_localization_gap / penalty_matrix (3 cases)

- `COMP-RAG-V2-EN-037` — Is there a penalty table for Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-038` — How do penalties differ by violation in Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...
- `COMP-RAG-V2-EN-039` — Where are the Counter-Strike 2 tournament penalties listed?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...

### en / english_localization_gap / schedule (1 cases)

- `COMP-RAG-V2-EN-053` — When is Counter-Strike 2 played and how is the time announced?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition...

### en / english_localization_gap / team_size (2 cases)

- `COMP-RAG-V2-EN-139` — How many players must a VALORANT team have?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified VALORANT competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_v...
- `COMP-RAG-V2-EN-141` — What is the permitted roster size for VALORANT?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified VALORANT competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_v...

### en / source_coverage_gap / conduct (3 cases)

- `COMP-RAG-V2-EN-115` — What conduct is expected from VALORANT players?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-116` — What behaviour is not allowed during a VALORANT match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-117` — What do the VALORANT rules say about player sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / fair_play_conduct (3 cases)

- `COMP-RAG-V2-EN-121` — What fair-play rules apply to VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-122` — Which unsporting behaviours are prohibited in VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-123` — Where can I check the sportsmanship rules for VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / in_match_operations (3 cases)

- `COMP-RAG-V2-EN-124` — How should players contact officials during a VALORANT match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-125` — What is the in-match procedure for VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-126` — Who should we notify if an issue occurs during VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / pre_match_on_site (6 cases)

- `COMP-RAG-V2-EN-040` — How do players check in for Counter-Strike 2?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-041` — What must players do on site before a Counter-Strike 2 match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-042` — Does the Counter-Strike 2 event have a check-in time or venue requirement?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-079` — How do players check in for Arena of Valor?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-080` — What must players do on site before a Arena of Valor match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-081` — Does the Arena of Valor event have a check-in time or venue requirement?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / team_size (3 cases)

- `COMP-RAG-V2-EN-056` — How many starters and substitutes can a Counter-Strike 2 roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-089` — How many starters and substitutes can a Arena of Valor roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-140` — How many starters and substitutes can a VALORANT roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### th / gold_or_section_contract_gap / disconnect (1 cases)

- `COMP-RAG-V2-TH-213` — กติกา RoV ว่าด้วยการเชื่อมต่อขาดหายเป็นอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.5.2....

### th / gold_or_section_contract_gap / penalty_matrix (3 cases)

- `COMP-RAG-V2-TH-178` — ขอตารางบทลงโทษของ CS2
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-V2-TH-179` — ความผิดแต่ละแบบใน CS2 โดนโทษต่างกันอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-V2-TH-180` — มีรายการบทลงโทษการแข่งขัน CS2 ให้ดูไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...

### th / gold_or_section_contract_gap / pre_match_on_site (3 cases)

- `COMP-RAG-V2-TH-277` — วันแข่ง VALORANT ต้องไปรายงานตัวอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง •    ผู้เล่นต้อง ปิด...
- `COMP-RAG-V2-TH-278` — ก่อนเริ่ม VALORANT ผู้เล่นต้องทำอะไรที่หน้างาน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง  รายละเอียดที่เกี่ยวข้อง: •    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง •    ผู้เล่นต้อง ปิด...
- `COMP-RAG-V2-TH-279` — VALORANT กำหนดเวลา check-in หรือพื้นที่แข่งไว้ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง  รายละเอียดที่เกี่ยวข้อง: •    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง •    Check-in time •...

### th / gold_or_section_contract_gap / schedule (2 cases)

- `COMP-RAG-V2-TH-194` — CS2 แข่งวันไหนและมีประกาศเวลาอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: •    3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้...
- `COMP-RAG-V2-TH-195` — ช่วยดูเรื่องกำหนดการแข่งขัน CS2 ให้หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: •    1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน ...

### th / gold_or_section_contract_gap / team_size (1 cases)

- `COMP-RAG-V2-TH-280` — ทีม VALORANT ต้องส่งผู้เล่นกี่คน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

### th / source_coverage_gap / conduct (3 cases)

- `COMP-RAG-V2-TH-256` — ผู้เล่น VALORANT มีข้อควรระวังเรื่องการวางตัวอะไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-257` — ระหว่างแข่ง VALORANT พูดหรือทำแบบไหนถึงผิดมารยาท
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-258` — กฎความประพฤติของผู้แข่ง VALORANT ระบุไว้อย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / fair_play_conduct (3 cases)

- `COMP-RAG-V2-TH-262` — การแข่งขัน VALORANT มีหลัก fair play อะไรที่ต้องทำตาม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-263` — VALORANT ห้ามมีพฤติกรรมที่ไม่เป็นนักกีฬาแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-264` — อยากเช็กเรื่องน้ำใจนักกีฬาของ VALORANT ต้องดูข้อไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / in_match_operations (3 cases)

- `COMP-RAG-V2-TH-265` — ระหว่างแมตช์ VALORANT ต้องประสานกับกรรมการอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-266` — ขั้นตอนทำงานระหว่างการแข่งขัน VALORANT เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-267` — ถ้าเกิดเรื่องระหว่างแข่ง VALORANT ต้องแจ้งใคร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / pre_match_on_site (6 cases)

- `COMP-RAG-V2-TH-181` — วันแข่ง CS2 ต้องไปรายงานตัวอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-182` — ก่อนเริ่ม CS2 ผู้เล่นต้องทำอะไรที่หน้างาน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-183` — CS2 กำหนดเวลา check-in หรือพื้นที่แข่งไว้ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-220` — วันแข่ง RoV ต้องไปรายงานตัวอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-221` — ก่อนเริ่ม RoV ผู้เล่นต้องทำอะไรที่หน้างาน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-222` — RoV กำหนดเวลา check-in หรือพื้นที่แข่งไว้ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / team_size (3 cases)

- `COMP-RAG-V2-TH-198` — จำนวนตัวจริงและตัวสำรองของ CS2 กำหนดไว้อย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-231` — จำนวนตัวจริงและตัวสำรองของ RoV กำหนดไว้อย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-V2-TH-282` — จำนวนตัวจริงและตัวสำรองของ VALORANT กำหนดไว้อย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

## Next Action by Class

- `routing_or_target_failure`: inspect Question Frame and target lock before touching retrieval.
- `source_coverage_gap`: add or approve a source section; keep the safe no-answer until then.
- `gold_or_section_contract_gap`: review section bundles and create reviewed Gold, without widening current Gold silently.
- `english_localization_gap`: approve an English overlay tied to the current Thai source hash.
- `safe_outcome_contract_gap`: decide whether the corpus expects clarification or no-answer, then make that distinction explicit.
- `answer_contract_failure`: inspect the validator error and evidence metadata before changing wording.
