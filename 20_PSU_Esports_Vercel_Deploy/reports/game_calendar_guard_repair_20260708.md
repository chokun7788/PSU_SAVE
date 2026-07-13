# Game / Calendar Guard Repair 2026-07-08

## สาเหตุที่พบ

- มี vector index แล้ว แต่เป็น local sparse/hash vector สำหรับ runtime บน Vercel ไม่ใช่ neural vector DB แบบ e5/FAISS
- ชื่อเกมภาษาไทยที่พิมพ์เพี้ยนบางแบบยังไม่ผ่าน entity match เช่น `พั้บจี`, `เรสิเด้นอีวิล`
- คำถาม family เช่น `มาริโอ้มีเกมอะไรบ้าง` ถูก game detail จับเกมเดียวก่อน family answer
- คำถาม genre เช่น `เกม Action มีอะไรบ้าง` ยังไม่มี fast path เฉพาะแนวเกม
- คำถามช่วงเวลา `อาทิตย์หน้า` ถูกตอบเป็นตารางเปิดปิดทั่วไปแทนการ resolve เป็นช่วงวันที่จริง
- ปฏิทินวันหยุดอ่านไฟล์ปี 2026 ไฟล์เดียว ทำให้ปี 2027 ตอบว่าไม่มีข้อมูล

## สิ่งที่แก้

- `app/core/normalization.py`
  - เพิ่ม soft alias match สำหรับชื่อภาษาไทยโดยตัดวรรณยุกต์/การันต์บางส่วน
  - เพิ่ม raw-soft match ก่อน mapping เป็นอังกฤษ เพื่อให้ `พั้บจี` เทียบกับ `พับจี` ได้
- `app/runtime/fast_answer.py`
  - เพิ่ม fuzzy family match สำหรับ Resident Evil
  - เพิ่ม genre fast path สำหรับคำถามแนวเกม เช่น Action, MOBA, FPS, Battle Royale, Fighting, Racing, Sports, Horror
  - ปรับลำดับ family answer ให้มาก่อน detail answer เมื่อผู้ใช้ถามแบบกว้าง เช่น `มาริโอ้มีเกมอะไรบ้าง`
  - เพิ่มคำตอบช่วงสัปดาห์หน้า โดย resolve เป็นวันจันทร์-วันอาทิตย์ของสัปดาห์ถัดไป
- `app/calendar/service_calendar.py`
  - เปลี่ยนการโหลดวันหยุดไทยให้รวม `data/calendar/thai_holidays_*.jsonl` ทุกปี
- `data/calendar/thai_holidays_2027.jsonl`
  - เพิ่มข้อมูลวันหยุด/เทศกาลไทยปี 2027 จาก Time and Date Thailand holidays 2027

## Smoke ที่ตรวจ

- `อะไรคือเกม เรสิเด้นอีวิล`
  - ตอบ Resident Evil family ถูก ไม่ดึง God of War
- `อะไรคือเกมเรสสิเด้นอีวิว`
  - ตอบ Resident Evil family ถูก
- `อะไรคือเกมพั้บจี`
  - ตอบ PUBG: BATTLEGROUNDS ถูก
- `เกม Action มีอะไรบ้าง`
  - ตอบรายชื่อเกมแนว Action / Action-Adventure จากรายการเกม ไม่หลุดกติกา RoV
- `มาริโอ้มีเกมอะไรบ้าง`
  - ตอบรวมเกมในกลุ่ม Mario
- `อาทิตย์หน้ามีหยุดไหม`
  - ตอบช่วงวันที่ของอาทิตย์หน้าและวันหยุดในช่วงนั้น
- `อาทิตย์หน้าเล่นได้ไหม`
  - ตอบช่วงวันที่และตารางให้บริการรายวันของอาทิตย์หน้า
- `ปี 2027 มีวันหยุดอะไรบ้าง`
  - ตอบรายการปฏิทินไทยปี 2027 จากไฟล์ local
- `เกม abcxyz คืออะไร`
  - ยัง no-answer ไม่ดึงเกมอื่นมาตอบ

## หมายเหตุ

- ยังไม่ได้ deploy production
- ไม่ได้ run Ground Truth ชุดใหญ่ตามคำขอประหยัด token
- ข้อมูลวันหยุดปี 2027 เป็นข้อมูล local ที่อ้างอิงจาก Time and Date ไม่ใช่ paid API runtime
