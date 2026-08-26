# Simple Chatbot Q&A - Typhoon

ชุดนี้สร้างเพื่ออ่านคำถามและคำตอบจริงจาก Chatbot โดยไม่ต้องเปิด raw trace ก่อน

- ทั้งหมด: `1600` ข้อ
- ผ่านอัตโนมัติ: `1540`
- ไม่ผ่านอัตโนมัติ: `60`
- เกิน 10 วินาที: `44`
- ไม่ผ่านและเกิน 10 วินาที: `3`
- Explicit timeout exception: `0`

## เปิดไฟล์

- [Index Q&A ครบ 1,600 ข้อ](INDEX.md)
- [Failure 60 ข้อ พร้อมโจทย์ คำตอบ และ root cause](FAILED_60_WITH_QA_AND_CAUSE.md)
- [Slow 44 ข้อ พร้อมโจทย์ คำตอบ และ latency cause](SLOW_OVER_10S_44_WITH_QA.md)
- [บทวิเคราะห์ Failure กับเวลา](FAILURE_AND_LATENCY_ANALYSIS_TH.md)
- `cases/`: Markdown แยกหนึ่งไฟล์ต่อหนึ่งโจทย์

หมายเหตุ: `FAIL` มาจาก heuristic judge จึงมีบางข้อที่คำตอบถูกความหมายแต่ keyword judge ตรวจพลาด
