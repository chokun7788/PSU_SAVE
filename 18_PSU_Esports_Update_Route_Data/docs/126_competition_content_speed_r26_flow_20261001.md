# Flow r26: ตรวจเนื้อหากติกาและลดเวลาตอบ — 2026-10-01

## เป้าหมายและขอบเขต
ให้คำถามกติกาที่ระบุเกมและหัวข้อชัดเจนถึงข้อมูลที่ตรงคำถามเร็วขึ้น ตรวจทั้งเนื้อหา เงื่อนไข หน่วย ประเภทกฎ และสถานะที่ยังไม่มีหลักฐาน เก็บ log / ผลดิบ / Ground Truth / ไฟล์เจ้าของเดิมทั้งหมดไว้ ใช้เอกสารกฎที่บันทึกในโปรเจกต์ ไม่ได้ยืนยันว่าเป็นกฎล่าสุดจากผู้จัด

## หลักฐานก่อนแก้
- r25 เว็บจริง: คำถาม RoV การหลุดจากเกมพร้อมคำเกริ่นใช้ 8.5317 วินาที โดยเลือก intent ด้วยโมเดล 8.0848 วินาที ทั้งที่รู้เกมและหมวดกติกาแล้ว
- Tekken การตั้งค่าพร้อมคำเกริ่นใช้ 2.6093 วินาที เสียเวลาค้นหมวดด้วย semantic 1.4204 วินาที ต่อมาจึงได้ frame เกมและหัวข้อที่ถูก
- ตัวตรวจเนื้อหา 80 เคส: ผ่านดิบ 68/80; 5 เคส RoV ไทยคาดคำว่า “ไม่สามารถ” แต่ต้นฉบับและคำตอบใช้ “ไม่อนุญาต” จึงเป็นข้อผิดพลาดตัวตรวจ; อีก 7 เคสเป็นปัญหาจริง (5 คำถามประเภทบทลงโทษไทยขาด 3 ประเภท; 2 คำถามอังกฤษที่พิมพ์ tournament เบิ้ลหลุดหมวด/หัวข้อ)
- ภาษาไทย technical pause ระยะเวลาให้ข้อความไม่พบข้อกฎถูก แต่ mode ยังถูกนับเป็นคำตอบข้อเท็จจริง

## ลำดับทำงาน
1. เก็บสำเนาโค้ด, hash แหล่งข้อมูล/คำแปลที่ใช้งาน/ตารางเจ้าของ/คิว review/GT 2,000 และสถานะ Git ลง report ใหม่
2. สร้าง fixture 16 ประเด็น × 5 รูปคำถาม = 80 เคส ไทย 40 อังกฤษ 40; เก็บต้นฉบับพร้อม hash; assertions เขียนจากข้อกฎ ไม่คำนวณจาก renderer
3. เก็บ baseline ดิบ; ตรวจข้อผิดพลาดตัวประเมินด้วย source แล้วสร้าง fixture v2 โดยไม่เขียนทับ baseline หรือ fixture v1
4. ล็อกเฉพาะเส้นทางคำถามเมื่อ: มีสัญญาณกติกา + เกมเดียวที่ registry รู้จัก + facet ชัด; ใช้ frame/intent ที่มีแล้วข้ามการค้นหมวดและเลือก intent ซ้ำ ความครอบคลุมของข้อกฎยังต้องตรวจภายหลังตามเดิม
5. รับคำเบิ้ลใน task word อังกฤษด้วย edit distance 1 เมื่อมีชื่อเกมที่ลงทะเบียน ห้ามแก้ชื่อเกม/เลข/คำจริงที่มีความหมายอื่น ห้ามเพิ่ม alias คำสะกดผิดทีละคำ
6. คำถามประเภทบทลงโทษไทย: ต่อรายการลำดับจากเอกสารเดียวกันที่มีครบทั้ง 5 ข้อและหัวข้อกำกับ แสดงเงื่อนไขเต็มพร้อม source ทุกข้อ จำกัดให้คำถามทั่วไป/ขอประเภท ไม่ใช้กับคำถามความผิดเฉพาะ
7. เมื่อถามคุณสมบัติของ pause ชนิดหนึ่งแต่ไม่พบ clause ยืนยัน: ส่ง mode no_answer + warning + trace ของ source ที่ตรวจ ไม่ยืมเวลาจากชนิดอื่น
8. ทดสอบเนื้อหา 80 เคส, การป้องกันผิดเกม/ข้ามหมวด/เติมข้อกฎ, regression เดิม และ GT ใหญ่ 2,000 ไทย/อังกฤษ เก็บผลคะแนนเดิมแยกจาก review source-presence
9. สร้างแพ็กเกจใหม่ที่มี version ใหม่ ทดสอบผ่าน HTTP พร้อมโมเดลและ semantic เปิด รวมคำถามช้าเดิมและ negative controls ตรวจเวลาเทียบก่อน/หลังจาก trace
10. ทบทวน flow: (ก) การยืนยันหลักฐานก่อนแก้ (ข) ขอบเขต fast route ไม่สร้าง fact (ค) fixture ไม่ยืนยันเกินที่ตรวจได้ (ง) ทดสอบแพ็กเกจที่เปิดให้ใช้จริง แล้วบันทึกผล/ข้อจำกัด

## เงื่อนไขยอมรับ
- ประเภทบทลงโทษ VALORANT ครบ 5 ประเภท พร้อมเงื่อนไขที่แยก intent ไม่ทราบ / ตั้งใจ / ความผิดครั้งแรก / ซ้ำหรือร้ายแรง / cheating หรือ match fixing
- technical communication มีข้อห้ามและข้อยกเว้นในประโยคแรก; ไม่มีเวลาจาก Tactical/Emergency
- technical duration ที่ไม่มีหลักฐานต้องเป็น no_answer ทั้งข้อความและสถานะ
- CS2 ตารางมี 9 คู่การละเมิด–บทลงโทษ และ source ต่อท้าย s55
- ค่าตั้ง Tekken 3 รอบ 60 วินาที; ขนาดทีม CS2 5 คน; RoV tablet/iPad ห้ามและตัดสิทธิ์
- เกมหาย/หลายเกม/เกมไม่รองรับ/หัวข้อไม่ชัดไม่เข้าทางลัด ส่วน catalog, booking, controls ยังต้องตอบหมวดเดิม
- คำถามเกม+facet ชัดไม่เรียก semantic route refiner / LLM intent ซ้ำ แต่ยังตรวจ scope, evidence contract, ambiguity และ answer validation

## สิ่งที่ยังต้องให้ผู้จัดยืนยัน
- Tekken s03 ห้ามหยุดทุกเหตุผล กับ s07 อนุญาตบางกรณี: s07 เป็นข้อยกเว้นหรือไม่ ต้องได้รับอนุญาตกรรมการหรือไม่? บทลงโทษเสีย Round, Game หรือ FT2 Match ในแต่ละกรณี?
- V2 104 รายการในคิว review ยังไม่ได้รับรอง ห้ามเปิดใช้เป็นข้อกฎยืนยัน
- คำแปลอังกฤษตรวจเทียบต้นฉบับได้ แต่ไม่ใช่การรับรองอย่างเป็นทางการจากเจ้าของ

## ผลการดำเนินงาน — รุ่นพร้อมใช้
แพ็กเกจ: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_content_speed_r26_ready\PSU_Esports_Chatbot_Local`
เวอร์ชัน: `2026.10.01-competition-content-speed-r26`
เว็บ: http://127.0.0.1:8090/

| การตรวจ | ผล | ขอบเขต |
| --- | --- | --- |
| Unit/regression รอบ F | 113/113 | source scope, first line, negative controls, coverage, route, booking และ typo |
| เนื้อหาเว็บจริง | 80/80 | ไทย 40 อังกฤษ 40, 16 ประเด็น × 5 รูปคำถาม; ไม่ใช่ทุกความหมายที่ผู้ใช้อาจถาม |
| HTTP รุ่นพร้อมใช้ | 36/36 | คำถามเดิมของผู้ใช้, history เปลี่ยนเกม, source gap, catalog, booking, penalty, typo; LLM/semantic เปิด |
| HTTP เวลา | 0.0609–3.4503s | 36 เคสที่วัด ไม่ใช่คำรับประกันทุกคำถาม |
| GT ใหญ่ รอบ D | 1953/2000 ดิบ | ไทย 1000 อังกฤษ 1000; LLM/semantic ปิด |
| review ของ 47 fails | พบ source clause เต็ม 47/47 | ยืนยัน source presence เพิ่ม ไม่ใช่ตรวจ semantic ครบทุกคำตอบ |
| hash ไฟล์ป้องกัน | 7/7 เหมือนก่อนแก้ | source, Gold, review queue, English CURRENT, ownerschedule, r25 flow, bilingual English |
| package/code snapshot | 7/7 runtime files ตรง | สำเนา ready_code 8 ไฟล์รวม test |

### การวนตรวจและแก้ที่ทำจริง
1. Baseline fixture v1: 68/80; แยก 5 oracle wording errors ออกจาก 7 response errors ด้วย source
2. รอบ A: content 80/80 แต่ unit พบ no_answer mode และ age detail guard ยังผิด
3. รอบ B/C: mode และ age guard ถูก; เพิ่ม positive/negative age-value tests, unit 112/112
4. ตรวจ UI จริง: notice ขอพิมพ์ใหม่หลังตอบสำเร็จ แก้ copy ไทย/อังกฤษ; ไม่เปลี่ยน guard/log
5. ตรวจคำตอบเต็ม HTTP: English tournament format ประโยคแรกเป็น hardware; เพิ่ม facet และ first-line assertions
6. Fixture v3 รอบ D: 75/80 แสดงว่าหัวข้อไทยยังแทนคำตอบตรงประเด็นอยู่
7. รอบ E: เริ่มด้วย 1v1/FT2 แต่ regression พบค่า 60 วินาทีหาย จึงคืน settings ที่ผูกกับส่วนรูปแบบเดียวกัน
8. รอบ F: unit 113/113 และ fixture 80/80; freeze โค้ดก่อน full GT รุ่นพร้อมใช้
9. full A=1953/2000; B=1952/2000 มี timeout หนึ่งเคส; replay เคสนั้นผ่าน; C=1953/2000; D รุ่นพร้อมใช้=1953/2000 ไม่มี timeout; ทุกผลดิบยังอยู่
10. ตรวจ package + เว็บ 8090 + DOM ของคำตอบอังกฤษ 1v1/FT2 + hash + ผลแยก source review ก่อนสรุป

### การปรับ flow หลังอ่านคำตอบเต็ม
- เพิ่ม gate ว่า first line ต้องเป็น clause ที่ตอบหัวข้อ ไม่ใช่แค่มีคำตอบจริงที่ส่วนรายละเอียด
- gate “หัวข้อเดียวกัน” ยังไม่พอ: age ต้องมีค่า/หน่วย และ pause ต้องมี proposition ที่ถามใน subtype นั้น
- completeness ของรายการต้องมี source ทุกข้อ; negative control ที่เอกสารขาดท้ายรายการต้องไม่เติมเอง
- source presence / bounded content acceptance / organizer policy confirmation เป็นหลักฐานคนละระดับ
- ไม่อ้างทุกคำถามเร็วจาก median: r25 มี cache hit; เก็บ cold/preface/repeated requests และ trace LLM attempts แยกกัน
- ไม่อ้าง source review แก้ timeout: รอบ B เหตุการณ์ 719.2584s ยังบันทึกเป็น timeout จริง ต้นเหตุยังยืนยันไม่ได้ รีเทสผ่าน 1.5759s และรอบสุดท้ายไม่พบซ้ำ

### ข้อจำกัดที่ยังเหลือ
- ตัวให้คะแนน GT ใหญ่ยังมีข้อจำกัดกับ clause อังกฤษสั้น/penalty; ใช้ review แยกและไม่แก้ Gold
- fixture ใหม่ตรวจ 16 ประเด็น ต้องขยายรายละเอียด/ข้อยกเว้นจากคำถามจริงเมื่อเก็บได้
- คำถามไม่ระบุเกมยังใช้การถามกลับ; เวลาอาจนานกว่าคำถาม game+facet ชัด
- กติกา Tekken pause ที่ขัดกันและ V2 104 รายการยังรอผู้จัด ไม่แก้นโยบายโดยเดา
- รอบ B มี timeout ที่รีเทสไม่เกิดซ้ำ ยังระบุต้นเหตุเครื่องหรือ preflight ไม่ได้ หากเกิดอีกต้องเก็บ timing ช่วงที่ยังไม่ถูกวัด

## เอกสารและหลักฐาน
- รายงานสรุป: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r26_competition_content_speed_20261001_195338_2e1f80\FINAL_RESULTS_TH.md`
- วิเคราะห์เหตุและสิ่งที่ควรตอบ: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r26_competition_content_speed_20261001_195338_2e1f80\CAUSE_ANALYSIS_TH.md`
- ผลดิบ GT: `full_r26_A/B/C/D_ready_*`; ผลรอบ D ใช้ชื่อ `full_r26_D_ready_*`
- คำตอบเว็บเต็มพร้อม trace: `http_final_ready.json`, `final_ready_live_8090_content.json`
- fixture v1/v2/v3 และผล baseline เก็บแยก ไม่เขียนทับ
- ผลยืนยัน snapshot / source review / owner pending: `FINAL_VERIFICATION.json`
