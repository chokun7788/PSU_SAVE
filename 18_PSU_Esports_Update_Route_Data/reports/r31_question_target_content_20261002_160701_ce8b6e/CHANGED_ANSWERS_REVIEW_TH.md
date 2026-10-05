# คำตอบที่เปลี่ยนจาก G6 — 57 inputs

รายการนี้เก็บคำถาม/คำตอบเดิม/คำตอบใหม่/เกณฑ์เพื่อreview ไม่รับรองsemanticcorrectnessทั้งหมด ชื่อเกมที่กู้ได้มีคำตอบหัวข้อผิดหรือขาดรายละเอียดอยู่ ดูFINAL_RESULTS_TH

## 1. ตาม rulebook เตาน์เตอร์สไตรก์ 2 คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 18d42e5cf54b1783f6ed5f32a51935f138c157f6d80cf814d9092a07770468dc

## 2. ขอสอบถามหน่อยครับ ตาม rulebook เคานน์เตอร์สไตรก์ 2 ขอบเขตและข้อมูลของรายการ ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key c9874df48b9d5c655cdba37f5e16b299041a67f9a7aa54e817abeb44ebbe2c4f

## 3. ขออ้างอิงกติกา อารีน่สออฟเวเลอร์ ในหัวข้อจำนวผู้เล่นต่อทีม หน่อย

ภาษา: th; modeเดิม `pipeline:ambiguity_clarification` → ใหม่ `pipeline:competition_source_rag`

### เดิม

คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: กติกาการแข่งขัน, สมาชิกทีม

### ใหม่

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "competition rule terms found before reservation/check-in; operation_first=competition_rule_lookup"}; confidence: 0.84

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key c80ad25fd328c5f068fa2d4e3534ac15b42f39bc5f7e82723c2158817390651a

## 4. ตาม rulebook เคานน์เตอร์สไตรก์ 2 การตั้งค่าในเกม ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_source_rag`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 2. การตั้งค่าในเกม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "one registered game and an explicit rule facet; source coverage remains required; operation_first=competition_rule_lookup"}; confidence: 0.84

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 1db3aa26b2cf2ae9eebfedb50f68121ac923eca83b8689ec71fa05356ad969cd

## 5. ขอสอบถามหน่อยครับ ตาม rulebook เค่น์เตอร์สไตรก์ 2 ตารงบทลงโทษ ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_source_rag`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 8. ตารางบทลงโทษ (Penalties)

รายละเอียดที่เกี่ยวข้อง:
•    7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
•    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
•    ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "one registered game and an explicit rule facet; source coverage remains required; operation_first=competition_rule_lookup"}; confidence: 0.84

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key bc741eba8965b548617f7260a2115cd81d6f433b2bcc386b2b8550d82bac23ed

## 6. ตาม rulebook เคาน์เเตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_source_rag`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "one registered game and an explicit rule facet; source coverage remains required; operation_first=competition_rule_lookup"}; confidence: 0.84

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 6a948db7d54468835edde70ab80546a2ce235863d4a5537dbb15ecce1d31b815

## 7. ขออ้างอิงกติกา เคาน์เตอร์สไรก์ 2 ในหัวข้ออุปกรณ์ที่ใช้แข่งขัน หน่อย

ภาษา: th; modeเดิม `pipeline:competition_target_clarification` → ใหม่ `pipeline:competition_source_rag`

### เดิม

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### ใหม่

คำตอบ: 1. อุปกรณ์ที่อนุญาต

รายละเอียดที่เกี่ยวข้อง:
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "one registered game and an explicit rule facet; source coverage remains required; operation_first=competition_rule_lookup"}; confidence: 0.84

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key d0e17609a8b98d52175883fc2ca94666ea6a2f8fa81e93f93cc8d8da13c14fdf

## 8. กติกา CS2 เรื่องการ pause และ timeout ว่าอย่างไร

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key add7e47720c340bbdd5c5f7246d8aff0ef3b3bc11bb5ebe06a9bf34e27758208

## 9. Counter-Strike 2 มีข้อกำหนดเรื่องการ pause และ timeout ไหม

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 1a0a1611e4bf84af6ba95a192bada6b078fc10d86f5d9d98bdfa15073172cb0d

## 10. What do the CS2 tournament rules say about pauses and timeouts?

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 0b96ba2b3de63483962511be3e0e3a94be5fded3392d46b1fb1537a9ae6b54d9

## 11. Counter-Strike 2 แข่งจริง กฎเกี่ยวกับการ pause และ timeout เป็นแบบไหน

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 6e5620fcac22b422cf2369e116326266a1f03b1577186331347390590b9886c3

## 12. Please retrieve the official CS2 rulebook evidence for pauses and timeouts.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key fdc072196ee1c88db9cd6ef010943f3cd6cd9017da2835f4f2e8cfdfd1728507

## 13. กำลังจะลงแข่ง CS2 อยากรู้เรื่องการ pause และ timeout

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 9fd1491c9cc37f7470cc3481119210389e45a5f2ffc6d69326084ec449e75b37

## 14. For Counter-Strike 2, can you verify the rule on pauses and timeouts?

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 07a06bede2fa20cfa118a081ddbe107ad4106fa8e4679fea956a42c6c056f337

## 15. How is pauses and timeouts handled in the Counter-Strike 2 tournament rules?

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 1b67656a8d9cc6688c4e532c563ed85b81d8b85bca839aad23f32d370182b924

## 16. ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการ pause และ timeout หน่อย

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key cc3298de47a0b7e63467158328e6e8b13df2da1f86bd122a9cdd56d1cfe4c816

## 17. Could you cite the Counter Strike 2 rule concerning pauses and timeouts?

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key c9205d64a640e1c01818d32fd8b2fc6dbeb05c16437bb3e39b8619c8401cbb36

## 18. ตาม rulebook เคาน์เตอร์สไตรก์ 2 การ pause และ timeout ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 6fc4f9406ed0b5a7f149c668ee7d3c2d684f49c6e7954062a950f0141be2bc3f

## 19. I am preparing for a Counter Strike 2 match. What is the policy for pauses and timeouts?

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key ea82daec0bcf300ef336c6d34eb16c6001bf8a21c43f250ca5a8bea991ab2101

## 20. How do timeout and technical pause rules work in Counter-Strike 2?

ภาษา: en; modeเดิม `pipeline:competition_rule_detail_source` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key a557b66121527e4a7a1fa01e214a510641db2bc68994df6b99c1c9c6c838a2b3

## 21. CS2 มี timeout หรือ technical pause อย่างไร

ภาษา: th; modeเดิม `pipeline:competition_rule_detail_source` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key ba5d73c90a98d22de10bcde1fb9df70a7a6297efef209a4ae9b3038fa42a2c2b

## 22. ช่วยดูหน่อย กติกา CS2 เรื่องการ pause และ timeout ว่าอย่างไร ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key f5112eefd67f4661e2cbbc22fe68447c2bec34191379dbc7ddd17c14c8df5945

## 23. ช่วยดูหน่อย Counter-Strike 2 มีข้อกำหนดเรื่องการ pause และ timeout ไหม ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 9b454243da4e05ec233c1dc874746592ce0f200a75dadeef62e8f038053f4ad1

## 24. ช่วยดูหน่อย ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการ pause และ timeout หน่อย ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 1e977dc6630041c5551b1b11fc58e0e1478afd52994a9f30bfda9f5bc2b32729

## 25. ช่วยดูหน่อย Counter-Strike 2 แข่งจริง กฎเกี่ยวกับการ pause และ timeout เป็นแบบไหน ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key d20fb5a3db2d695c3b4bdf43992fa3de3b9e3b97fa3af498423e848b487965e5

## 26. ช่วยดูหน่อย กำลังจะลงแข่ง CS2 อยากรู้เรื่องการ pause และ timeout ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key f8eeb1ac85868dcaf29d9a18309e09f397cfdb63c0004f44b7766fae32cd95bf

## 27. ช่วยดูหน่อย ตาม rulebook เคาน์เตอร์สไตรก์ 2 การ pause และ timeout ต้องทำยังไง ครับ

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 314dcabfedcd470fdb8b283f77056f7ec6361b7bad5ad5f194565c16edf97b84

## 28. Please check: For Counter-Strike 2, can you verify the rule on pauses and timeouts? please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 631b473e98ac5e15abe134d3390e2b0262744783fd8a4aae018d20e90c038a32

## 29. Please check: What do the CS2 tournament ruls say about pauses and timeouts? please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key f7d3c3e29739cb8bd98306a268bf7241a12fc4b380b6fd82dceb4eb2dc9dc074

## 30. Please check: Please retrieve the official CS2 rulebook evidence for pauses and timeouts. please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key d57129deb1e6d4d24cd26cb601ebd34f5296c45d2ebcc12f20270f89ed981cd3

## 31. Please check: Could you cite the Counter Strike 2 rule concerning pauses and timeouts? please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 743f47172b45bb3275b42210e43b697bfc2c773d14dcce9cc2688c2350210727

## 32. Please check: How is pauses and timeouts handled in the Counter-Strike 2 tournament ruls? please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key d09ff75968e723277b3b6e4bfd38a579e056aba28dca3ca6ce308392813ab7f1

## 33. Please check: I am preparing for a Counter Strike 2 match. What is the policy for pauses and timeouts? please.

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 49c37689c3acf942cef5a4916c0c7354dc80843aeb3e03a044635347d660851b

## 34. ขอสอบถามหน่อยครับ Counter-Strike 2 มีข้อกำหนดเรื่องการ pause และ timeout ไหม

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 6c7d1186713e7fc53b2549dec604da4f634d8647f80c15cf538af5a6290a5268

## 35. ขอสอบถามหน่อยครับ กติกา CS2 เรื่องการ pause และ timeout ว่าอย่างไร

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 3d2b9a1693d4828179c17dbddda7b64eb4ddc54f6f07436f45be443363811afd

## 36. ขอสอบถามหน่อยครับ Counter-Strike 2 แข่งจริง กฎเกี่ยวกับการ pause และ timeout เป็นแบบไหน

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 8ce27f1a15fc7fb7d211a444a83672904fbf31d9498582338b921651bdd0f3ad

## 37. ขอสอบถามหน่อยครับ ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการ pause และ timeout หน่อย

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 67f674b56b0d7f7fa36e324d25a92da957dfe8eee51957db5e6a8454669cf59c

## 38. ขอสอบถามหน่อยครับ กำลังจะลงแข่ง CS2 อยากรู้เรื่องการ pause และ timeout

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 6b0d5b76131d3c585d1ce1a48aca88773978180890ac05edab92941a5ddccca8

## 39. ขอสอบถามหน่อยครับ ตาม rulebook เคาน์เตอร์สไตรก์ 2 การ pause และ timeout ต้องทำยังไง

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key d542262815198a6c9170d7c637e623b6d5c5c2af25b2897a9d747f3a120d7953

## 40. What do the CS2 tournament rules say about pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 05f505e994a0c04b7408a8bf32593a96a6e5c300a25d6cc768d9741afda93790

## 41. Please retrieve the official CS2 rulebook evidence for pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 7c47c2acbe853a6cc338f2b1988e5d51612159cd99a0415a8176913796f478e3

## 42. For Counter-Strike 2, can you verify the rule on pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 33ee7d17b8ca9a465be9f54c14dfe93cd8d3d305a0f7f3f847af9639958e497b

## 43. Could you cite the Counter Strike 2 rule concerning pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 1d229682ef43475e07afebe58d87fbbc583caaf4312d1c27c9ab430eae43ac2d

## 44. How is pauses and timeouts handled in the Counter-Strike 2 tournament rules

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 2993fdee710190154c802e970836be8e9212d71b73fa6dce31a686d773387c42

## 45. I am preparing for a Counter Strike 2 match. What is the policy for pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key ca0f9a9cdbf8f7c222ec9cfea66bd26cba44497c2ae6449280ade63703c53f95

## 46. Could you please help me with this: For Counter-Strike 2, can you verify the rule on pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 04cb68d9c128af26b1cdc3c36d07c79323810da2263d778b7ed5d3952d0dd620

## 47. Could you please help me with this: What do the CS2 tournament rules say about pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 8b3b5c5f9b48ff2f468c736dd02271a844cab7478a9ea341bd1f1590233392ee

## 48. Could you please help me with this: Please retrieve the official CS2 rulebook evidence for pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 0b31bbabf028878174d394c631de1d37989f32baed7bee7303037995ddaecf2e

## 49. Could you please help me with this: I am preparing for a Counter Strike 2 match. What is the policy for pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key b2927eeaf40b9a6a0dc0fbec9c8c4ec3b46e0f233f3ec206cc0e56e425c7f9d9

## 50. Could you please help me with this: Could you cite the Counter Strike 2 rule concerning pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 9fd6171096f65c0ea7be22b407cdee590e59a720d45536ae6ce67cba87e4e242

## 51. Could you please help me with this: How is pauses and timeouts handled in the Counter-Strike 2 tournament rules

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key e083a7debd70838d8dbfa05c702644f5c9e4b01f301bc846b6b297a14dd24e1b

## 52. ขอสอบามหน่อยครับ ตาม rulebook เคาน์เตอร์สไตรก์ 2 การ pause และ timeout ต้องทพยังไง

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key bed4a226487f9244073bf5b3911092f719690d83abce420122ba0967003941f7

## 53. กติกาา CS2 เรื่องการ pause และ timeout ว่าอย่างไร

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key ada9484b1bd7153d33e189532067684f4ca6904595ce3d8543fc6f6e9b9fad72

## 54. ขอสอบถามหน่อยครับบ กติกา CS2 เรื่องการ pause และ timeout ว่าอย่างไร

ภาษา: th; modeเดิม `pipeline:competition_source_rag` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 4a13376bbff109c665320f790676047b23805a67670b0b01ef0dfd85ab8e389d

## 55. Could yoi please help me with this: Could you cite the Counter Strike 2 rule concerning pauses and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key c90faf5213f50b43109541ed297da023a5df3684e8e57974e18af999e26a7a85

## 56. For Counter-Strike 2, can you verify the rule on pause and timeouts

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Details:
• Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 4c9454a62832a80a4f8c56fb75d9601f1248a9c92628966f60783e255c0bb86f

## 57. How is pauses and timeouts handled in the Counter-Strike 2 turnament rules

ภาษา: en; modeเดิม `pipeline:structured_competition_rules_en` → ใหม่ `pipeline:competition_rule_detail_source`

### เดิม

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### ใหม่

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Details:
• Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Route: {"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}; confidence: 0.97

Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key 143e6ea059ae1c39005b05d71142d736725621060679ddfb805acaf38507fac2
