# PSU Esports Chatbot: Local Owner Package

ชุดนี้คือหน้าเว็บ Chatbot สำหรับเปิดใช้บนเครื่องของผู้ดูแล โดยข้อมูลคำถามและประวัติการใช้งานจะอยู่ในเครื่องนี้ ไม่ได้เรียก Cloud Chatbot API

## ก่อนเริ่มครั้งแรก

1. ติดตั้ง Python 3.11 หรือใหม่กว่า โดยเปิดตัวเลือก **Add Python to PATH** ระหว่างติดตั้ง
2. ติดตั้ง Ollama จาก https://ollama.com/download
3. เชื่อมต่ออินเทอร์เน็ตชั่วคราว แล้วดับเบิลคลิก `Setup-Local-Models.cmd`
4. รอให้ดาวน์โหลด Local Model และ RAG embedding model จนขึ้นข้อความ `Setup complete`

การดาวน์โหลดในข้อ 3 เป็นครั้งแรกครั้งเดียว หลังจากนั้นการตอบ Chatbot ใช้โมเดลในเครื่อง ไม่ใช่ Chatbot API ภายนอก

## วิธีเปิดใช้งาน

1. ดับเบิลคลิก `Start-PSU-Esports-Chatbot.cmd`
2. เบราว์เซอร์จะเปิดที่ `http://127.0.0.1:8080/`
3. เก็บหน้าต่าง PowerShell ที่เปิดอยู่ไว้ตลอดเวลาที่ใช้งาน Chatbot
4. เมื่อต้องการปิดระบบ ให้กด `Ctrl + C` ที่หน้าต่าง PowerShell นั้น

หน้าเว็บรองรับ Auto / ไทย / English และใช้ Semantic RAG กับ Local LLM เพื่อช่วยเข้าใจคำถามที่เขียนได้หลายรูปแบบ

## ข้อมูลและความเป็นส่วนตัว

- ฐานความรู้, vector index, Local LLM และประวัติสนทนาอยู่ในเครื่องนี้
- Chat log จะอยู่ที่ `data\logs\` และ session history อยู่ใน `data\logs\chat_history.sqlite3`
- ห้ามส่งโฟลเดอร์ `data\logs\` ให้บุคคลอื่น เพราะอาจมีข้อความที่ผู้ใช้พิมพ์ไว้
- แหล่งข้อมูลที่ปรากฏท้ายคำตอบเป็น URL อ้างอิงเท่านั้น ระบบไม่ได้ดึงข้อมูลเว็บสดในขณะตอบ

## การแก้ปัญหาเบื้องต้น

| อาการ | วิธีแก้ |
|---|---|
| ขึ้นว่าไม่พบ Python | ติดตั้ง Python แล้วปิด/เปิด PowerShell ใหม่ |
| ขึ้นว่าไม่พบ Ollama หรือ model | เปิด `Setup-Local-Models.cmd` อีกครั้ง |
| เปิดเว็บไม่ได้ | ตรวจว่าหน้าต่าง Start ยังเปิดอยู่ แล้วเข้า `http://127.0.0.1:8080/` ด้วยตนเอง |
| Port 8080 ถูกใช้งาน | เปิด PowerShell ในโฟลเดอร์นี้ แล้วใช้ `./Start-PSU-Esports-Chatbot.ps1 -Port 8090 -OpenBrowser` |
| คำตอบช้า | รอให้ Local Model warm up ในคำถามแรก และหลีกเลี่ยงการเปิดหลายหน้าต่างพร้อมกัน |

## ข้อควรรู้

- ชุดนี้ใช้ข้อมูล release ที่แพ็กมาด้วย ไม่อัปเดตข้อมูล WordPress/Facebook แบบ real-time
- การเพิ่มข้อมูลใหม่ต้องผ่าน workflow content/review แล้ว rebuild structured projection และ RAG index ก่อนแทนที่ชุดนี้
- ระบบสำหรับ Check Slot, Booking และยืนยันการจ่ายเงินยังไม่รวมอยู่ใน Local Owner Package นี้ เพราะต้องเชื่อมกับ API/ผู้ให้บริการจริงก่อน
