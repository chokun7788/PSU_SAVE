# Flow r28 — ความครบของคำถามกติกาหลายประเด็น

## ขอบเขต

ใช้ source และคำแปลที่ hash ตรง เพิ่มคำถามและคำตอบที่คาดหวังจาก clause ต้นฉบับก่อนแก้ selector. เก็บ owner pending, Gold, นโยบายศูนย์ และ logs เดิม. การตรวจคำแปลทำเองต่อได้ ส่วนกฎที่ขัดหรือ source ขาดต้องรอผู้จัด

## ขั้นตอน

1. ตรึงชุดประเด็นที่ยังไม่ครอบคลุมใน r27 รวมคำถามหลายเรื่องเกมเดียวและ controls: ไม่ระบุเกม, เกมไม่รองรับ, อายุ/ราคาไม่พบ, pause ที่ขัดกัน
2. แต่ละ expected clause มาจาก source ID/hash + approved English overlay; runtime ไม่อ่าน fixture และผล runtime ไม่ใช้สร้าง Gold
3. รัน baseline แยก clean/polite/typo, single/composite/controls. วิเคราะห์ทุก failure ตาม trace พร้อมเนื้อหาที่ควรปรากฏ
4. แก้การตรวจคำถามและการเลือก clause แบบแยกความหมาย ใช้แนวคิดทั่วไป ไม่ใช้ whole-question aliases. ตรวจว่า concept ที่จับหลายเรื่องไม่ตัดเรื่องอื่นและไม่มี head-only answer
5. ตรวจ local scope: ข้อห้าม macro/การติดตั้ง/เงื่อนไขการปรับค่า กับหัวข้ออื่นต้องไม่ถูก exclude ด้วยคำจากคำถามทั้งประโยค
6. เพิ่ม tests เฉพาะ failure จริง รวมคำที่ถูก, negation, game/number preservation และความกำกวม
7. รันชุดใหม่ซ้ำ, ชุดเดิม 320/128/80 และ unit; เมื่อเลือกคำตอบเปลี่ยนให้รัน Gold 2,000 อีกครั้ง เก็บ raw กับ source presence grade แยก
8. สร้าง package รุ่นใหม่ ไม่ทับแพ็กเกจเดิม ตรวจเว็บจริงก่อนนำขึ้น 8090. ใช้ผล r27 worker recycle เป็นหลักฐานเดิม; repeat เฉพาะ gate ที่ implementation ใหม่มีผล
9. สรุปสิ่งที่แก้ได้ ผลจริง ขอบเขต synthetic cases และคำถามเจ้าของที่ยังขาด. อัปเดต Flow ตามความผิดที่พบ

## การรับผล

Positive: game/source ถูก, complete expected clauses ทุกข้อ, first line ตรงหนึ่งประเด็นที่ถาม, validation ผ่าน. Safe controls: clarification/no-answer/conflict ตามหลักฐาน ไม่มีการแต่งข้อมูลอายุ/ค่าธรรมเนียม/คำที่ source ขาด. ไม่ใช้ source-presence pass แทน completeness

## ยังรอข้อมูล

Tekken s03/s07, RoV 6.1.5–6.1.5.1 ฉบับเต็ม, ขอบเขต/ฉบับที่มีผลและ V2 104. รุ่นจอย/นโยบายภาพ/ชื่ออังกฤษทางการเติมได้เมื่อมีข้อมูล. Booking oracle ยังเก็บภายหลัง
