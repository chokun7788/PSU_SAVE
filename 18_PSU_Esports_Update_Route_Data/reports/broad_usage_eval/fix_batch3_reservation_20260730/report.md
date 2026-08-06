# Broad Usage Eval v1

- Generated at: 2026-07-30T17:06:37
- Cases: 20
- Turn checks: 20
- Passed: 19
- Failed: 1
- Pass rate: 0.95
- Total wall sec: 21.685
- Allow LLM: False
- RAG fallback: False

## By Group
- reservation: 19/20 pass, 1 fail

## By Strategy
- compound: 1
- fast/rule: 3
- rag/retrieval: 2
- structured: 14

## Common Problems
- route_category expected ['reservation'], got multi_question: 1

## Top Failures

### R-018 reservation
- Question: จองแล้วไม่สามารถยกเลิกได้ใช่ไหม
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['reservation'], got multi_question
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    จอง ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/  •    ไม่สามารถยกเลิกได้ใช่ไหม เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต...
