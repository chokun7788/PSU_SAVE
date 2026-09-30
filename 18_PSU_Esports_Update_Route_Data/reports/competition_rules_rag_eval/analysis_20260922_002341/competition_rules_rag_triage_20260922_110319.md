# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260922_002341.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| th | 209 | 264 | 55 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `source_coverage_gap` | 36 | The selected rulebook has no retrieved section that directly proves the requested facet. |
| `gold_or_section_contract_gap` | 17 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `routing_or_target_failure` | 2 | The request did not retain the expected competition route or rulebook target. |

## Review Queue

### th / gold_or_section_contract_gap / disconnect (3 cases)

- `COMP-RAG-TH-123` — ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการหลุดจากเกมหรือการเชื่อมต่อ หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.5.2....
- `COMP-RAG-TH-124` — กำลังจะลงแข่ง RoV อยากรู้เรื่องการหลุดจากเกมหรือการเชื่อมต่อ
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.2....
- `COMP-RAG-TH-125` — Arena of Valor มีข้อกำหนดเรื่องการหลุดจากเกมหรือการเชื่อมต่อ ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที...

### th / gold_or_section_contract_gap / penalty_matrix (6 cases)

- `COMP-RAG-TH-073` — กติกา CS2 เรื่องตารางบทลงโทษ ว่าอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-074` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับตารางบทลงโทษ เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-075` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อตารางบทลงโทษ หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-076` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องตารางบทลงโทษ
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-077` — Counter-Strike 2 มีข้อกำหนดเรื่องตารางบทลงโทษ ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-078` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...

### th / gold_or_section_contract_gap / pre_match_on_site (5 cases)

- `COMP-RAG-TH-247` — กติกา VALORANT เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-248` — Valorant แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-249` — ขออ้างอิงกติกา วาโล ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-250` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-252` — ตาม rulebook วาโล การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...

### th / gold_or_section_contract_gap / team_size (3 cases)

- `COMP-RAG-TH-254` — Valorant แข่งจริง กฎเกี่ยวกับจำนวนผู้เล่นและองค์ประกอบทีม เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...
- `COMP-RAG-TH-256` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องจำนวนผู้เล่นและองค์ประกอบทีม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...
- `COMP-RAG-TH-257` — Valorant มีข้อกำหนดเรื่องจำนวนผู้เล่นและองค์ประกอบทีม ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...

### th / routing_or_target_failure / match_settings (2 cases)

- `COMP-RAG-TH-189` — ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย
  - Expected: `answer_available`; actual: `clarification` via `pipeline:competition_target_clarification`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT
- `COMP-RAG-TH-192` — ตาม rulebook เทคเค่น 8 การตั้งค่าในเกม ต้องทำยังไง
  - Expected: `answer_available`; actual: `clarification` via `pipeline:competition_target_clarification`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### th / source_coverage_gap / conduct (6 cases)

- `COMP-RAG-TH-205` — กติกา VALORANT เรื่องมารยาทและพฤติกรรมผู้เล่น ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-206` — Valorant แข่งจริง กฎเกี่ยวกับมารยาทและพฤติกรรมผู้เล่น เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-207` — ขออ้างอิงกติกา วาโล ในหัวข้อมารยาทและพฤติกรรมผู้เล่น หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-208` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องมารยาทและพฤติกรรมผู้เล่น
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-209` — Valorant มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-210` — ตาม rulebook วาโล มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / fair_play_conduct (6 cases)

- `COMP-RAG-TH-217` — กติกา VALORANT เรื่องfair play และข้อห้าม ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-218` — Valorant แข่งจริง กฎเกี่ยวกับfair play และข้อห้าม เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-219` — ขออ้างอิงกติกา วาโล ในหัวข้อfair play และข้อห้าม หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-220` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องfair play และข้อห้าม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-221` — Valorant มีข้อกำหนดเรื่องfair play และข้อห้าม ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-222` — ตาม rulebook วาโล fair play และข้อห้าม ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / in_match_operations (6 cases)

- `COMP-RAG-TH-223` — กติกา VALORANT เรื่องขั้นตอนระหว่างการแข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-224` — Valorant แข่งจริง กฎเกี่ยวกับขั้นตอนระหว่างการแข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-225` — ขออ้างอิงกติกา วาโล ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-226` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องขั้นตอนระหว่างการแข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-227` — Valorant มีข้อกำหนดเรื่องขั้นตอนระหว่างการแข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-228` — ตาม rulebook วาโล ขั้นตอนระหว่างการแข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / match_configuration (6 cases)

- `COMP-RAG-TH-049` — กติกา CS2 เรื่องเวอร์ชันเกมและการตั้งค่าแมตช์ ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-050` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับเวอร์ชันเกมและการตั้งค่าแมตช์ เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-051` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อเวอร์ชันเกมและการตั้งค่าแมตช์ หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-052` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องเวอร์ชันเกมและการตั้งค่าแมตช์
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-053` — Counter-Strike 2 มีข้อกำหนดเรื่องเวอร์ชันเกมและการตั้งค่าแมตช์ ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-054` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 เวอร์ชันเกมและการตั้งค่าแมตช์ ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / pre_match_on_site (12 cases)

- `COMP-RAG-TH-079` — กติกา CS2 เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-080` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-081` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-082` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-083` — Counter-Strike 2 มีข้อกำหนดเรื่องการรายงานตัวและพื้นที่แข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-084` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-139` — กติกา RoV เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-140` — Arena of Valor แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-141` — ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-142` — กำลังจะลงแข่ง RoV อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-143` — Arena of Valor มีข้อกำหนดเรื่องการรายงานตัวและพื้นที่แข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-144` — ตาม rulebook อารีน่าออฟเวเลอร์ การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
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
