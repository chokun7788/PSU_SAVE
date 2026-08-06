# Broad Usage Eval v1

- Generated at: 2026-07-30T17:19:50
- Cases: 75
- Turn checks: 75
- Passed: 74
- Failed: 1
- Pass rate: 0.9867
- Total wall sec: 8.188
- Allow LLM: False
- RAG fallback: False

## By Group
- competition_rules: 74/75 pass, 1 fail

## By Strategy
- fast/rule: 60
- rag/retrieval: 15

## Common Problems
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1

## Top Failures

### CR-045 competition_rules
- Question: Counter-Strike 2 สรุปกติกาสั้นๆ
- Resolved: -
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
