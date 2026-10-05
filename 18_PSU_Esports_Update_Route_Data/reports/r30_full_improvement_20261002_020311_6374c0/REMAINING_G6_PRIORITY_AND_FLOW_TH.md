# ข้อที่ยังผิดจริงหลัง G6 และ Flow รอบถัดไป

ข้อเหล่านี้ตรวจจากคำตอบ/trace และต้นฉบับแล้ว แยกจาก keyword รูปแบบเก่า ยังไม่ได้แก้ใน G6 และไม่ต้องเดานโยบายใหม่

## สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน

- คำตอบจริง: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- Concept ที่ระบบรู้จัก: ไม่มี
- สาเหตุที่ยืนยัน: Venue vocabulary does not recognize สถานที่จัด before the event title; no recognized detail concept, so coverage safely refuses.
- คำตอบที่ควรได้ตามเอกสารเดิม: ตามเอกสารกติกา CS2 ที่มี: แข่งขัน 1 วัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ข้อ source: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- งานต่อ: Add bounded proposition vocabulary plus TH/EN, clean/noisy, negative controls; validate requested quantity, duration and condition; never substitute freeze-time duration for timeout.

## CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง

- คำตอบจริง: คำตอบ: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Concept ที่ระบบรู้จัก: round_time
- สาเหตุที่ยืนยัน: Bare timeout is not tactical_timeout vocabulary; freeze time matches round_time, so the duration of the round is answered while the requested timeout quantity/duration is omitted.
- คำตอบที่ควรได้ตามเอกสารเดิม: ตามเอกสารกติกา CS2 ที่มี: ขอเวลานอกได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- ข้อ source: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- งานต่อ: Add bounded proposition vocabulary plus TH/EN, clean/noisy, negative controls; validate requested quantity, duration and condition; never substitute freeze-time duration for timeout.

## Gate รอบถัดไป

1. เพิ่ม content contract ของ venue/timeout ก่อนแก้ รวมคำถามที่ถามเฉพาะสถานที่หรือเฉพาะจำนวน/เวลา และคำถามสองเรื่อง
2. ตรวจ negative: timeout ของ VALORANT, เวลา freeze time ปกติ, เวลานอกทางเทคนิค, ตำแหน่งปุ่ม, วันจัดรายการใหม่ที่ไม่มี source
3. แก้ matcher/coverage แบบ proposition ที่ผูกเกมและ source ไม่เพิ่ม whole-question alias
4. ตรวจ first line + quantities + condition + source + recorded-event qualifier; focused → unit → competition corpora → actual API
5. เปรียบเทียบ clean/noisy และทำ source/Gold preservation audit ก่อน release

หลักฐาน JSON มี actual trace/grades, source hash และต้นฉบับครบ ไม่ใช้จำนวนเกณฑ์ไม่ผ่านแทนจำนวนคำตอบผิดทั้งหมด
