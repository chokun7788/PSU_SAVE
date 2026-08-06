# Broad Usage Eval v1

- Generated at: 2026-07-30T17:18:57
- Cases: 75
- Turn checks: 75
- Passed: 64
- Failed: 11
- Pass rate: 0.8533
- Total wall sec: 8.413
- Allow LLM: False
- RAG fallback: False

## By Group
- competition_rules: 64/75 pass, 11 fail

## By Strategy
- fast/rule: 55
- rag/retrieval: 15
- structured: 5

## Common Problems
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 7
- route_category expected ['competition_rules'], got reservation: 5
- missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1

## Top Failures

### CR-003 competition_rules
- Question: VALORANT มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-018 competition_rules
- Question: CS2 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-032 competition_rules
- Question: Counter-Strike 2 ใช้ผู้เล่นกี่คน
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 ใช้ผู้เล่นทีมละ 5 คนครับ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-033 competition_rules
- Question: Counter-Strike 2 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-034 competition_rules
- Question: Counter-Strike 2 pause ได้ไหม
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีทั้ง Technical Pause และ Tactical Timeout ครับ •    Technical Pause ใช้กรณีปัญหาขัดข้อง •    Tactical Timeout ใช้ตามเงื่อนไขช่วง Freeze time แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-041 competition_rules
- Question: Counter-Strike 2 ถ้าใช้ bug จะโดนอะไร
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีบทลงโทษครับ •    ตัวอย่าง: ใช้บัค/โกง/พฤติกรรมไม่เหมาะสม อาจถูกปรับแพ้เป็นรอบ แมตช์ หรือตัดสิทธิ์ตามความรุนแรง แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-042 competition_rules
- Question: Counter-Strike 2 ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 ต้องยืนยัน/รายงานตัวตามเวลาที่ผู้จัดกำหนดครับ •    หากไม่ยืนยันก่อนแมตช์มีความเสี่ยงถูกตัดสิทธิ์ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-044 competition_rules
- Question: Counter-Strike 2 แผนที่มีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีข้อมูล map pool ครับ •    แผนที่ที่พบ: Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-045 competition_rules
- Question: Counter-Strike 2 สรุปกติกาสั้นๆ
- Resolved: -
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-048 competition_rules
- Question: TEKKEN 8 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-063 competition_rules
- Question: ROV มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/
