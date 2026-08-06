# Broad Usage Eval v1

- Generated at: 2026-07-30T17:25:14
- Cases: 25
- Turn checks: 25
- Passed: 18
- Failed: 7
- Pass rate: 0.72
- Total wall sec: 10.937
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 18/25 pass, 7 fail

## By Strategy
- clarification: 6
- fast/rule: 1
- no_answer: 7
- pipeline: 2
- rag/retrieval: 4
- structured: 5

## Common Problems
- missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']: 4
- missing any of ['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง']: 3

## Top Failures

### ANA-006 ambiguity_no_answer
- Question: เครื่องไหนดีที่สุด
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-008 ambiguity_no_answer
- Question: มีอะไรแนะนำไหม
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-015 ambiguity_no_answer
- Question: สรุปคือทำยังไง
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-020 ambiguity_no_answer
- Question: เกม Valorant Mobile มีไหม
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-021 ambiguity_no_answer
- Question: ขอเบอร์โทรส่วนตัวเจ้าหน้าที่
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-022 ambiguity_no_answer
- Question: ขอข้อมูลที่ไม่ได้อยู่ในเว็บ PSU Esports
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-023 ambiguity_no_answer
- Question: วันนี้มีข่าว esports อะไรล่าสุด
- Resolved: -
- Mode: `pipeline:guard_no_answer`
- Route: `no_answer/guard_no_answer`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
