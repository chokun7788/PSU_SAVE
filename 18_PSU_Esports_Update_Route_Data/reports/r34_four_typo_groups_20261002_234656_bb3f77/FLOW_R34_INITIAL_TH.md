# Flow r34 — แก้ 4 กลุ่มคำผิดและตรวจวนซ้ำ

## ขอบเขต
แก้ validator ของคำถามราคา, วิธีชำระที่เสียคำจอง, คำพูดกับปฏิเสธที่ผิดพร้อมกัน, และกติกา/จำนวนผู้เล่นที่ผิดพร้อมกัน ใช้แหล่งเดิม ไม่แก้นโยบายหรือ Gold งานเก็บสถานะจองจริงยังพัก

## วิธีทำแต่ละรอบ
1. อ่าน source และ trace ก่อนตั้งคำตอบคาดหวัง; แยกเนื้อหาจาก route/status
2. เตรียม clean/noisy/ประโยคใหม่ และคำจริง/คำปฏิเสธ/เลข/ชื่อ/คำถามหลายส่วนเป็น controls
3. รัน baseline → ระบุว่าหลุดที่ recovery, frame, routing, source หรือ validator
4. เปลี่ยนเฉพาะสาเหตุที่มีหลักฐาน โดยคง validation และบันทึกการแก้ทุก span
5. ทดสอบคำตอบกับเนื้อหาและแหล่งจริง วิเคราะห์ failed ใหม่แล้วปรับ flow ก่อนรอบต่อไป

## ลำดับวงรอบ
A. ราคา: comparative price + ทุกบริการที่ระบุ ต้องใช้ price frame แม้คำนำเสีย; ไม่เปลี่ยนคำถาม compare อุปกรณ์ธรรมดาเป็นราคา
B. ชำระ: วิธีชำระมีหลักฐานอิสระ ไม่สะกดคำจริง ของ เป็น จอง แบบทั่วประโยค แยก bank transfer/booking transfer/deadline/ยอดเงิน
C. คำพูด: กู้คำบอก speech และ spelling ของปฏิเสธเฉพาะกรอบที่รองรับ; ห้ามเพิ่ม/ลบ ไม่ ในข้อความที่ไม่มีหลักฐาน
D. การแข่งขัน: เจอ target ที่ลงทะเบียนก่อนกู้ศัพท์กติกา/จำนวน; ไม่แก้ชื่อหรือปีเพื่อยืมข้อกฎ และไม่แทน roster ด้วย 5v5 เมื่อไม่มี roster source
E. ประโยคใหม่/controlled mutation: ทบทวนข้อผิดใหม่พร้อม negative และ compound controls; แก้เมื่อยืนยันสาเหตุได้

## Gates ก่อนเปลี่ยนเว็บ
source/content fixtures; negative literal/meaning; existing unit + meaningful regression; ทั้ง 2,000 clean/noisy pairs และ affected corpus; HTTP ของ package ใหม่พร้อม LLM/semantic profile; preservation hashes; เปิด8090เฉพาะหลังตรวจผ่าน เก็บผลทุกวงรอบ/failed แยก ไม่อ้าง full fresh หากเป็น replay

## การตรวจ flow
ก่อนแก้แต่ละรอบและหลังผลใหม่ ตรวจ scope/negation/ambiguity/source/edition/compound/grader/provenance/dirty files/deployment รวม 10หัวข้อ บันทึกผลจริง ไม่สร้างชื่อรอบทบทวนที่ไม่ได้ทำ
