# Broad Usage Eval v1

- Generated at: 2026-07-30T17:06:20
- Cases: 10
- Turn checks: 10
- Passed: 9
- Failed: 1
- Pass rate: 0.9
- Total wall sec: 4.057
- Allow LLM: False
- RAG fallback: False

## By Group
- schedule: 9/10 pass, 1 fail

## By Strategy
- fast/rule: 3
- rag/retrieval: 1
- structured: 6

## Common Problems
- missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']: 1
- route_category expected ['schedule', 'reservation'], got general: 1

## Top Failures

### S-010 schedule
- Question: ตารางเวลาให้บริการเป็นยังไง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['schedule', 'reservation'], got general, missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
