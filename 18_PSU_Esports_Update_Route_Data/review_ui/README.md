# PSU Esports Human Review UI

เปิดไฟล์ `index.html` เพื่อรีวิวคำตอบแบบกดคลิก

สิ่งที่ทำได้:

- เลือกข้อจากรายการ 360 ข้อ
- กด decision: `pass`, `minor_fix`, `major_fix`, `needs_data`, `needs_policy`
- กดคะแนน 0-4 ในแต่ละมิติ
- ใส่หมายเหตุและสิ่งที่ควรแก้
- กด export เป็น JSON หรือ Markdown

ข้อมูลที่กดจะถูกเก็บใน `localStorage` ของ browser เครื่องนี้ ถ้าต้องการส่งผลให้ทีม/AI แก้ต่อ ให้กด `Export JSON` หรือ `Export Markdown`

ถ้าข้อมูลต้นทางเปลี่ยน ให้รัน:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\create_review_ui_data.py
```
