# คู่มือเจ้าของข้อมูลกลาง

## สิ่งที่ต้องเตรียม

ใช้เครื่อง Windows ที่เปิดระบบเดิมได้ Python 3.12 x64 รวมในชุดนี้ แบบฟอร์มใช้ port 8097 เฉพาะ 127.0.0.1 ไม่ต้องใช้โมเดลเพื่อกรอก ตรวจ อนุมัติ หรือ preview แบบดึงค่า ส่วนแชทและ optional query planner ใช้ Ollama เดิม

ฐานจริง: `data/knowledge/approved.sqlite` ภายในโฟลเดอร์เดียวกับ app ถ้ากำหนด PSU_KNOWLEDGE_DB ให้ owner และ chat ใช้ path เดียวกัน อย่าชี้ไป fixtures และอย่าตั้ง PSU_COMMON_ALLOW_DEMO=1 สำหรับการใช้งานจริง

## 1. ID / aliases / ภาษา

ID ต้องขึ้นต้น a-z และใช้ a-z, 0-9, _, :, - ยาว 3–100 ตัว ใช้ชื่อถาวรเช่น `game_coral_trail` ไม่เปลี่ยน ID เพื่อแก้สะกด ใช้ aliases สำหรับชื่อเรียกที่คนใช้จริง ไม่ต้องกรอกสะกดผิดทุกแบบ ชื่อใหม่มาจากข้อมูล ไม่อยู่ใน dictionary โค้ด

text มี {th,en} ใช้ null เมื่อไม่มีคำแปล ตัวเลข เงิน เวลา IDs ใช้ร่วมกันทั้งสองภาษา เก็บ English status: missing/draft/agent_translated/reviewed/stale ถ้าแปลด้วยระบบแต่ยังไม่มีคนตรวจใช้ agent_translated คำตอบ EN ระบุสถานะนี้ ถ้าข้อความไทยเปลี่ยน review hash เดิมไม่ valid ต้องตรวจใหม่ ช่องติ๊ก “ตรวจภาษาอังกฤษ” ถูก reset ทุกครั้งที่เปิดรายการ

## 2. ช่องข้อมูลและสถานะ

- known: มีค่าตรงตามหลักฐาน เจ้าของยืนยันเมื่อบันทึก และตรวจอีกครั้งก่อนเผยแพร่
- unknown: ยังไม่ยืนยัน ใช้ null ห้ามกรอก 0, false หรือ “ไม่มี” เพื่อแทนไม่ทราบ
- not_applicable: ช่องไม่เกี่ยวกับรายการนี้ ไม่ใช่ไม่มีข้อมูล
- conflicted: หลักฐานขัดกัน เก็บร่าง/หลักฐานแยกและตัดสินใจก่อนเผยแพร่ หน้าฟอร์มยังไม่รองรับการเพิ่มหลักฐานขัดกันสองชุด ใช้ importer JSON สำหรับงานขั้นสูง

ดาว ★ คือ core ที่ต้อง known ก่อน publish ไม่จำเป็นต้องรู้ทุก optional field จึงเพิ่มเกมแล้วตอบเฉพาะที่ทราบได้ ปุ่ม/แพลตฟอร์มที่ไม่ทราบจะตอบว่ายังไม่มีข้อมูล ไม่ยืมจากเกมอื่น

## 3. เวลาและเงิน

ฟอร์มวันเวลาเป็นเวลาไทยและบันทึก +07:00 ต้องระบุ timezone ราคาหรือ event/rules/schedule/closure/news ต้องมี validity ที่ยืนยัน effective_from; effective_until เว้นว่างได้เมื่อมีหลักฐานว่าไม่กำหนดวันหมดอายุ ขอบเวลาใช้ start inclusive / end exclusive

amount_minor คือสตางค์: 35 บาท=3500; 4000 บาท=400000 ค่า string “35 บาท”, จำนวนติดลบ หรือ unknown ที่ value=0 ถูกปฏิเสธ สกุลเงินและหน่วย/ระยะเวลา/กลุ่มคนต้องกรอกแยก ห้ามใช้ราคาหนึ่งกลุ่มแทนทุกคน แพ็กเกจเหมาไม่ใช่การคูณเรทรายชั่วโมงและไม่สับสนจำนวนเครื่องกับจำนวนที่นั่ง

schedule แยก open_periods, bookable_periods, maintenance_periods การเปิดห้องไม่เท่ากับเปิดจอง; maintenance ห้ามทับช่วง bookable วันปิดพิเศษมี closure แยก อย่าแก้ 12:00/13:00 โดยเดา

session_minutes และ occupancy_minutes แยกกัน เช่น VR ใช้ 30 นาทีแต่กันสถานะเครื่องเป็น 60 นาทีตามนโยบายที่ยืนยันไว้ live_binding เชื่อม physical pool ของบริการเข้ากับ API; ฟอร์มนี้ไม่ได้ดึงสถานะจองมาเป็นข้อมูลถาวร

## 4. ลำดับการกรอกสัมพันธ์

1. zone/equipment_model → resource → service
2. game และ policy ที่เกี่ยวข้อง → game_service / game_mode / control_set
3. audience + service → rate; audience + zone → rental_package
4. contact → procedure → policy (ถ้า policy อ้าง procedure)
5. game → competition → competition_rule; dependency rules ต้องครบ ไม่วงกลม ไม่ข้ามงานแข่งขัน
6. schedule/closure ผูก zone; resolution policy ต้องเผยแพร่ก่อนใช้
7. person/news เชื่อม public contacts/audience; ไม่ใส่ข้อมูลส่วนตัวหรือข้อมูลการจองของลูกค้าในเนื้อหาสาธารณะ

ถ้ามีหลาย records ที่ต้องอัปเดตพร้อมกัน approve ทุกฉบับก่อนแล้วส่ง /api/publish พร้อม ids หลายตัวและ expected_active เดียว ใช้สิทธิ์ local owner เดิม หากกดทีละรายการแล้ว dependency ยัง draft การเผยแพร่จะถูกปฏิเสธโดยไม่สลับ release

## 5. ค้นปัญหา / แก้ข้อมูล

preview ใช้ release ที่เผยแพร่ แสดง query_plan (เลือก record/field/platform/method), obligations (known/unknown/not_current/needs_clarification) และ release_id ถ้าร่างเปลี่ยนแต่คำตอบยังเก่า ให้ดูว่าอนุมัติ+publish แล้วหรือยัง ถ้าผิด platform ตรวจ control_set; ถ้าความสัมพันธ์หายตรวจ IDs; ถ้าราคาไม่ current ตรวจ validity; ถ้า English stale ตรวจการแปลผูก revision

history ใน preview เก็บเฉพาะหน้า เปิดหน้าใหม่เพื่อเริ่มบทสนทนาใหม่ เว็บแชทใช้ session/delivery acknowledgment ของระบบเดิม ความสำเร็จของ API แยกจากความถูกต้องของเนื้อหา คำตอบไม่ครบต้องดู obligations ไม่ใช้แค่ status=200

withdraw เก็บประวัติและกัน fallback ไปข้อมูลที่ถอน หากยังมี published records อ้างอยู่ต้องถอนลูกก่อน rollback ไม่อนุญาตให้ชุบชีวิตรายการที่ถอนแล้ว การแก้ร่างใหม่ยังคง release เก่าจนกว่าจะเผยแพร่

## 6. สำรอง / ตรวจ / import (ผู้ดูแล)

เปิด PowerShell ในโฟลเดอร์ชุดใช้งาน ใช้ runtime\python\python.exe -B -m app.knowledge.common.manage --db data\knowledge\approved.sqlite status

ตรวจ gate สำหรับทุก draft: `runtime\python\python.exe -B -m app.knowledge.common.manage check`

สำรองด้วย SQLite API: `runtime\python\python.exe -B -m app.knowledge.common.manage backup data\backups\content_20261010.sqlite` ใช้ชื่อใหม่ทุกครั้ง ไม่คัดลอก .sqlite ไฟล์เดียวขณะมี WAL

rollback: `runtime\python\python.exe -B -m app.knowledge.common.manage rollback RELEASE_ID --expected-active CURRENT_RELEASE_ID` ตรวจ release_id จาก trace/audit ก่อน ใช้ backup เดิมสำหรับการกู้ระดับไฟล์หลังหยุดผู้เขียนทั้งหมดเท่านั้น

import: `runtime\python\python.exe -B -m app.knowledge.common.importer BUNDLE.json --actor local-owner` bundle มี schema_version/sources/records importer นำเข้า drafts เท่านั้น รายงาน saved และ pending_errors โดยไม่ทำ full-bundle transaction; ID ซ้ำไม่ทับของเดิม ให้แก้ revision ผ่านฟอร์ม

## 7. การดูแลสิทธิ์

ตัว editor เป็น local single-operator ในบัญชี Windows นี้ เปิดหลายแท็บได้แต่ revision guard กันทับร่าง ไม่ใช่ระบบ shared-admin/LAN/public authentication เก็บ capability ใน owner-session.json เพื่อเปิดซ้ำ อย่าแชร์ไฟล์นี้หรือ URL ที่มี token ปิดด้วย Stop-Owner-Content.cmd เมื่อต้องการหยุด editor ไม่เปลี่ยน permission ของบัญชี Windows อื่น
