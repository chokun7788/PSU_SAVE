# Thai Style Guide Rules from ORST Sources - 2026-07-07

## เป้าหมาย

ทำให้การจัดรูปคำตอบภาษาไทยของ PSU Esports Chatbot อิง style guide แบบมีแหล่งที่มา ไม่ใช่ regex ที่ฝังไว้ในโค้ดโดยไม่มีที่มา และยังต้องทำงานเร็วใน production โดยไม่เรียก API ภายนอกตอนตอบคำถามจริง

## สิ่งที่ทำ

- เพิ่มไฟล์กฎแบบ data-driven:
  - `data/style/thai_style_rules.jsonl`
- ปรับ formatter:
  - `app/core/thai_style.py`
- sync ไปโฟลเดอร์ deploy:
  - `C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\data\style\thai_style_rules.jsonl`
  - `C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\app\core\thai_style.py`

## แหล่งข้อมูลราชบัณฑิตฯ ที่ใช้

ใช้แหล่งข้อมูลจากสำนักงานราชบัณฑิตยสภาเกี่ยวกับการเว้นวรรคและไม้ยมก:

- `https://legacy.orst.go.th/?page_id=629`
- `https://legacy.orst.go.th/?page_id=10427`
- `https://www.orst.go.th/iwfm_table.asp?a=36`

กฎที่นำมาใช้โดยตรงตอนนี้:

- เว้นวรรคเล็กหน้าและหลังไม้ยมก `ๆ`
- ตัวอย่างผลลัพธ์:
  - `หลายๆอย่าง` -> `หลาย ๆ อย่าง`
  - `ตอบสั้นๆได้ไหม` -> `ตอบสั้น ๆ ได้ไหม`

## กฎที่เป็นของโปรเจกต์ ไม่ใช่กฎราชบัณฑิตฯ โดยตรง

กฎต่อไปนี้ติดป้ายเป็น `project_style_guide` ในไฟล์ data เพื่อแยกจากกฎทางการ:

- เว้นวรรคระหว่างตัวเลขอารบิกกับคำไทยเพื่อให้อ่านง่ายในคำตอบ chatbot
  - `ข้อ1` -> `ข้อ 1`
  - `30นาที` -> `30 นาที`
  - `5คน` -> `5 คน`
- ลดช่องว่างซ้ำหลังจากจัดรูป

เหตุผลที่แยก:

- ราชบัณฑิตฯ มีหลักเกณฑ์เรื่องการเว้นวรรคจำนวนมาก แต่ไม่ได้แปลว่าทุก regex ในระบบเป็นกฎทางการโดยตรง
- การแยก `official_orst` กับ `project_style_guide` ช่วยป้องกันการอ้างแหล่งข้อมูลเกินจริง

## วิธีทำงาน

`format_thai_response_style()` จะ:

1. ป้องกันข้อความที่ไม่ควรแก้ เช่น URL, `local://...`, และข้อความใน backtick
2. โหลดกฎจาก `data/style/thai_style_rules.jsonl`
3. ใช้เฉพาะกฎที่ `enabled: true`
4. ถ้าไฟล์กฎหายหรืออ่านไม่ได้ จะใช้ fallback rule ในโค้ดเพื่อไม่ให้ระบบล้ม
5. คืน URL/source เดิมกลับเข้าไป

## ผลทดสอบ

รันในโฟลเดอร์ 18:

- `python -m compileall app` ผ่าน

รันในโฟลเดอร์ 20:

- `python -m compileall app` ผ่าน
- smoke formatter:
  - input: `หลายๆอย่าง ข้อ1 ใช้เวลา30นาที มีผู้เล่น5คน และ PS5 แหล่งข้อมูล: https://example.com/a?x=1`
  - output: `หลาย ๆ อย่าง ข้อ 1 ใช้เวลา 30 นาที มีผู้เล่น 5 คน และ PS5 แหล่งข้อมูล: https://example.com/a?x=1`
- smoke pipeline:
  - `ตอบสั้นๆ ราคา VR เท่าไหร่`
  - route: `service_fee/service_fee_query`
  - mode: `pipeline:deterministic_calculator_fast`
  - source: `https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png`
- smoke pipeline:
  - `วันนี้วันที่เท่าไหร่`
  - route: `schedule/schedule_query`
  - mode: `pipeline:calendar_date_context_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้เพื่อประหยัด token/time

## ข้อจำกัด

- ระบบนี้เป็น post-processor สำหรับรูปแบบคำตอบ ไม่ใช่ grammar checker เต็มรูปแบบ
- ยังไม่ตรวจความถูกต้องเชิงวากยสัมพันธ์ทั้งหมด เช่น การเลือกคำ, ระดับภาษา, หรือกรณีเว้นวรรคตามดุลยพินิจ
- ถ้าต้องการครอบคลุมหลักราชบัณฑิตฯ มากขึ้น ควรเพิ่มกฎทีละชุดพร้อม source และ test case แยก ไม่ควรใส่ regex กว้างเกินไปจนเปลี่ยนความหมายคำตอบ
