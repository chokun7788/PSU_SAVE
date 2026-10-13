# ผลทดสอบและวิเคราะห์ความผิดพลาด r58

## สรุปหลักฐาน

- common unit gate: 26/26 ใน unit_results_9.json
- regression เดิม: 137/137 ใน regression_results.json
- final targeted suite รวม 164 เคส: ผ่าน 164/164
- เว็บจริงผ่าน HTTP: 25/25 ใน web_results_7.json มี health/worker gate ก่อนเริ่ม; ไม่มี full GT/20k/load test
- browser จริง: กรอกเกมสมมุติ Coral Trail → บันทึก → อนุมัติ → เผยแพร่ → preview และเว็บตอบตามค่าที่เพิ่งกรอก ไม่เพิ่มชื่อเกมในโค้ด มี owner_ui_publish_proof.jpg และ chat_ui_new_record_proof.jpg
- โปรเจกต์จริงนำเข้า 41 drafts, pending_errors={}, active='' จึงยังไม่เปิดข้อมูลร่างให้แชทตอบ ตรวจ source_preservation_after.json: เปลี่ยนไฟล์เดิมเฉพาะ engine/supervisor/server/builder, unexpected_changes=[], missing=[]
- การตรวจ hash ไม่รวม directories logs/chat_logs/state/ground_truth/vector/eval และ __pycache__ ไม่มีคำสั่งลบหรือ truncate log เดิม แต่ไม่อ้างว่า checksum ตรวจ log ทุกไฟล์

## ทำไมเคยเลือกคำตอบผิด และแก้อย่างไร

| อาการ | หลักฐานจาก trace/โค้ด | ควรตอบ | แก้ |
|---|---|---|---|
| แล้วปุ่มล่ะ ไม่ต่อเกมเดิม | method none; parent history เป็น text ไม่ใช่ content | ปุ่มของเกมล่าสุดใน user turn ที่ acknowledge แล้ว | context อ่านสองรูปแบบ และส่ง request_id เป็น last_seen_response_id |
| ขอรายละเอียดเกมเลือก body | registry label รายละเอียด ของ news มาเข้า field_requests ทุกหมวด | ข้อมูลเกม ไม่ใช่ field body ของข่าว | จำกัด label lookup ตาม kinds ที่เลือก เก็บ semantic cues สำหรับ relations แยก |
| ไม่พบเกม 9 แต่ดึงเกม 8 | named ไม่มี match แต่ category game+controls เปิด fallback ทุกเกม | ไม่ยืนยันเกมคนละภาค | generic category fallback เฉพาะ list/all หรือ center/contact/schedule ที่เหมาะสม เลขรุ่น protected |
| PS4 controls ตอบปุ่ม PC | platform detection เดิมดูแต่ values ที่มีในฐาน ทำให้ PS4 ที่ไม่มี data กลายเป็นไม่มี filter | แจ้งไม่มีข้อมูล scope PS4 | parse device edition และ filter children; ไม่ reuse PC |
| เกมหมดอายุยังตอบ control child | ตรวจ validity parent เฉพาะ block แต่ยัง join ลูกต่อ | ไม่ assert current controls | effective checks และหยุด join หาก parent/reference ไม่ current |
| ถอนแล้ว publish อีก record ทำชื่อที่ถอนหาย | names ใน release ใหม่ลบ retired record → legacy อาจกลับมา | แจ้งรายการถูกถอน | cc_names เก็บชื่อเคยเผยแพร่และ retired_names กัน fallback |
| English nested bindings ผ่าน missing status | ตรวจเฉพาะ top-level bilingual value | ต้อง explicit agent_translated/reviewed หรือแสดง Thai source | recursive translated_texts; reviewed ผูก content_hash |
| overlap ราคาใช้ ISO text compare | Z กับ +07:00 เรียงตัวอักษรต่างจากเวลาจริง | ขอบ [start,end) ตรงกันไม่ overlap | compare timezone-aware instants และ exact adjacent fixture |
| คำบังคับตัวละคร ได้เรื่องย่อ | no field match/LLM invalid plan แล้ว default overview | เลือก bindings ถ้ามั่นใจ มิฉะนั้นถามเพิ่ม | จำกัด plan fields และใช้ clarification เมื่อคำถามไม่ใช่ overview |
| แหล่งข้อมูลว่างแม้มี [S1] | server ข้าม hit ที่ public_url ว่าง | label ข้อมูลศูนย์ที่อนุมัติ พร้อม release ไม่สร้าง URL ปลอม | allow common_approved metadata เป็น plain source label |
| 10 connection errors ใน web round 5 | requests เริ่มก่อน HTTP bind/worker ready | รอ startup ready ก่อนทดสอบคำตอบ | แยก startup gate กับ answer oracle ไม่แก้ logic เพื่อซ่อน transport error |
| 35 failures/2 errors ใน combined unit ครั้งแรก | candidate ฐาน V3 รุ่นต้นมี draft แต่ไม่มี cc_names; snapshot ไปอ่าน table ที่ไม่มี แล้ว common_unavailable ขวาง legacy | ฐานไม่มี release ต้องส่งกลับ legacy | อ่าน retired names เฉพาะเมื่อมี release+withdrawn และเพิ่ม empty-old-DB regression; final rerun 164 ผ่าน |

## Negative oracle ที่ผิด และวิธีนับผล

web round1 เคสเอาคีย์บอร์ดมาเองตอบ “ไม่อนุญาต” ถูก แต่ must_not “อนุญาตให้นำ” เป็น substring ของ “ไม่อนุญาตให้นำ” จึงถูกนับผิด แก้ expected ตามความหมายและคง log รอบแรกไว้

web round3 center location ในฐาน fixture เป็น unknown แต่ oracle ไปคาด address จริงของ legacy จึงผิด oracle ใหม่คาด unknown สำหรับ fixture และตรวจ address จริงอีกครั้งในฐานใช้งานที่ไม่มี release fixture ผลนั้นแยกใน ready_smoke_results.json

ทดสอบ API สำเร็จแยกจากคำตอบถูก: oracle ตรวจคำ/ค่าที่ต้องปรากฏและห้ามปรากฏ, route common สำหรับ new title, platform filtering, requested facets, history และ count 105 รายการ บางเคส out-of-scope ตรวจเฉพาะไม่ปน fact เกม ไม่ใช่ rubric ครบทุกมิติ ข้อมูลจริงยังต้อง review ตาม metadata

## คะแนน/การเลือกคำตอบ

- exact entity: ชื่อ/aliases จาก release ไม่ใช่ ownerกรอกสะกดผิดทุกแบบ
- bounded fuzzy: SequenceMatcher threshold .88, margin .06 และ numeric edition equality เมื่อหลาย candidates ใกล้กันไม่เลือกมั่ว Threshold เหล่านี้เป็น engineering settings ยังไม่ใช่ calibrated confidence
- field cues: คำเกี่ยวกับ facet + key/description เฉพาะชนิดข้อมูล ถ้าไม่ตรงแล้ว optional LLM เลือก field ผ่าน schema เฉพาะหมวดและมี bounded deadline
- confidence=1 ใน route common หมายถึง extractive typed path นี้เลือก snapshot/field ตามเงื่อนไข ไม่ใช่คะแนนเจ้าของยืนยัน 100% หรือความแม่นยำ LLM ทางสถิติ unknown/not_current ยังต้องดู obligations
- known values ผูก source_id/JSON pointer/hash; trust/approval/release เป็นคนละ gate ความถูกต้องของ pointer/hash ไม่พิสูจน์ว่าข้อมูลต้นทางเป็นความจริง
- finalizer active/epoch change → retry; withdrawal/validity/unapproved drafts ไม่ใช้ fact assertion

## ข้อจำกัดของ LLM ที่ทดสอบจริง

คำถาม: Starfish Quest บังคับตัวละครด้วยอะไร

คำตอบ: ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?

เวลารวม: 2.280 วินาที; mode=pipeline:common_clarification

เคสนี้ผ่านเกณฑ์ปลอดภัย “ไม่ตอบเรื่องย่อแทนปุ่ม” แต่ **ไม่ใช่ความสำเร็จในการเข้าใจความหมาย** โมเดลยังไม่ให้ valid plan ที่ใช้ตอบ bindings ได้ ต้องเก็บเป็น semantic planner backlog ไม่เอาผล pass มารวมว่าเข้าใจ paraphrases ทั้งหมด

## เวลาในเครื่องนี้

คำตอบ common_answer ใน web round7: n=18, median=0.235s, min=0.153s, max=0.430s หลัง health gate ใช้ HTTP end-to-end (แยกจาก latency_sec ภายใน engine)

รอบก่อน cold import มีคำถามแรกประมาณ6–8วินาที จึง preload validator ใน worker ก่อน ready เพิ่ม startup time แทนรอ import ในคำถามแรก ตัวเลขรอบ7เป็น sequential fixture/local-model machine measurements ไม่มีหลักฐานว่าผู้ใช้พร้อมกันทุกคนได้เวลาเดียวกัน

## ต้องอ่านร่วมกับ

FLOW_IMPLEMENTATION_TH.md, OWNER_MANUAL_TH.md, FIELD_REFERENCE_TH.md, REMAINING_AND_DECISIONS_TH.md และไฟล์ผล JSON/log ทุก round เก็บไว้ในโฟลเดอร์ r58 เดิม ไม่มีการ overwrite ผลผิดด้วยผลผ่าน
