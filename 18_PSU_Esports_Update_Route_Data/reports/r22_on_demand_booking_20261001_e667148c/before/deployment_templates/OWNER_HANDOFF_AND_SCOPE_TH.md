# ขอบเขตชุดใช้งาน Local

## สิ่งที่รวมอยู่ในชุดนี้

- FAQ Chatbot ของ PSU Esports Studio พร้อมแหล่งอ้างอิง
- คำตอบภาษาไทยและภาษาอังกฤษด้วยตัวเลือก Auto / ไทย / English
- Fast/Structured สำหรับข้อเท็จจริงที่ยืนยันได้, Semantic RAG สำหรับเอกสาร/รายละเอียด และ Local LLM สำหรับช่วยเข้าใจคำถามที่เขียนได้หลายรูปแบบ
- Input Quality Guard สำหรับกรณีพิมพ์สลับภาษาและตัวอักษรซ้ำบางรูปแบบ
- บริบทการสนทนาต่อเนื่องภายในหน้าเว็บ/Session เดียว; refresh จะเริ่ม Session ใหม่แต่เก็บ audit log เดิมครบ
- Log, Session ID, transcript และรายงานสำหรับผู้ดูแลในเครื่อง
- ข้อมูลตารางการให้บริการและ Maintenance ที่อยู่ใน release นี้
- การอ่านสถานะ Slot จาก Booking Dashboard แบบ read-only เมื่อ WordPress CSV สดพร้อมใช้งาน โดยไม่ส่งข้อมูลผู้จองเข้า Chatbot

## สิ่งที่ยังไม่ใช่บริการจริงในชุดนี้

- Booking write, Slot Hold และ Payment Verification: ยังต้องมี WordPress/Booking API ที่มีสิทธิ์เขียนและ Payment Provider ที่ยืนยันธุรกรรมได้ก่อน
- Booking และการชำระเงิน: ต้องมี API เขียนข้อมูล, hold semantics และ payment provider จริง
- Slip verification และ Dynamic QR: ต้องใช้ provider credential, webhook HTTPS และนโยบายจัดการข้อมูลส่วนบุคคล
- Admin Dual Publish: workflow ออกแบบไว้แล้ว แต่ยังไม่ใช่หน้า Admin สำหรับเจ้าของในชุด Local นี้
- การอัปเดต WordPress, Facebook หรือเอกสารสด: ชุดนี้ใช้ knowledge release ที่แพ็กมา ไม่ดึงเว็บสดระหว่างตอบ

## วิธีเพิ่มข้อมูลในอนาคต

ข้อมูลใหม่ควรเข้าสู่ canonical content format แล้วผ่าน review ก่อนสร้าง Structured Projection และ RAG Index ใหม่ จากนั้นจึงสร้าง package release ใหม่แทนที่ชุดเดิม เพื่อให้ทุกเส้นทางตอบใช้ข้อมูล version เดียวกัน
