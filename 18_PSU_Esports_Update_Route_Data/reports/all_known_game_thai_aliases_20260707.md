# All Known Game Thai Aliases - 2026-07-07

## เป้าหมาย

เพิ่มการรองรับชื่อเกมภาษาไทย/ชื่อที่ผู้ใช้มักพิมพ์ สำหรับเกมทั้งหมดที่ระบบรู้จักตอนนี้ ทั้งเกมในอุปกรณ์/โซนและเกมแข่ง โดยไม่ดึงข้อมูลใหม่หรือเพิ่ม dependency หนัก

## แนวทาง

- ใช้ normalization แปลงชื่อไทยเป็น alias/canonical term ที่ matcher เดิมรู้จัก
- ไม่เพิ่ม alias กระจายทุกจุดเท่าที่ไม่จำเป็น
- เพิ่ม router terms สำหรับ canonical game terms ที่ยังไม่ถูก route เฉพาะ
- กัน broad family name ไม่ให้หลุดไป RAG ผิดเกม เช่น `Resident Evil`, `Call of Duty`

## ไฟล์ที่แก้

- `app/core/normalization.py`
- `app/pipeline/router.py`
- `app/runtime/fast_answer.py`

## กลุ่ม alias ที่เพิ่ม

ตัวอย่างชื่อไทย/คำเรียกที่ normalize แล้ว:

- `วาโลแรนท์`, `วาโลแรน`, `วาโล` -> `valorant`
- `อาโอวี`, `เอโอวี`, `อาร์โอวี` -> `rov`
- `เทคเคน8`, `เทกเคน` -> `เทคเคน 8` / `เทคเคน`
- `เคาน์เตอร์สไตรค์`, `เคาเตอร์` -> `counter-strike`
- `พับจี` -> `pubg`
- `วอร์โซน` -> `warzone`
- `คอลออฟดิวตี้` -> `call of duty`
- `ลีกออฟเลเจนด์`, `ลีคออฟเลเจนด์` -> `league of legends`
- `สไปเดอร์แมน` -> `spider-man`
- `ฟอร์ทไนท์` -> `fortnite`
- `ก็อดออฟวอร์` -> `god of war`
- `บีทเซเบอร์` -> `beat saber`
- `ฮอไรซอน` -> `horizon`
- `แกรนทัวริสโม`, `จีที7` -> `gran turismo` / `gt7`
- `ไฟนอลแฟนตาซี` -> `final fantasy`
- `ฮอกวอตส์` -> `hogwarts`
- `เรสซิเดนต์อีวิล` -> `resident evil`
- `นารูโตะ`, `โบรูโตะ` -> `naruto`, `boruto`
- `เดอะลาสต์ออฟอัส` -> `last of us`
- `อันชาร์ตเต็ด` -> `uncharted`
- `มาริโอคาร์ท` -> `mario kart`
- `โอเวอร์คุก` -> `overcooked`
- `สแมชบรอส` -> `smash bros`
- `สวิตช์สปอร์ต` -> `switch sports`
- `แอนิมอลครอสซิ่ง` -> `animal crossing`
- `อิทเทคส์ทู` -> `it takes two`
- `ลุยจิ` -> `luigi`
- `มาริโอปาร์ตี้` -> `mario party`
- `มอนสเตอร์ฮันเตอร์` -> `monster hunter`
- `มูฟวิ่งเอาท์` -> `moving out`
- `ซูเปอร์มาริโอ` -> `super mario`
- `ริงฟิต` -> `ring fit`
- `เซลด้า` -> `zelda`
- `ลิตเติลไนท์แมร์` -> `little nightmares`

## การจัดการเกมที่มีหลายภาค/หลายรายการ

- `Resident Evil` ตอบเป็นกลุ่มเกมที่เกี่ยวข้อง คือ Resident Evil 4 และ Resident Evil Village
- `Call of Duty` ตอบเป็นกลุ่มเกมที่เกี่ยวข้อง คือ Warzone และ Modern Warfare III
- `Mario` ยังใช้ family match เดิมเพื่อตอบเกม Mario ที่เกี่ยวข้อง
- `RoV / Arena of Valor` เป็น known unsupported สำหรับ service game catalog แต่ยังตอบกติกาแข่งได้

## ผลทดสอบ

รัน compile:

- โฟลเดอร์ 18: `python -m compileall app` ผ่าน
- โฟลเดอร์ 20: `python -m compileall app` ผ่าน

Smoke test ในโฟลเดอร์ 20:

- `วิธีเล่น พับจี` -> `game_detail_fast_path`
- `อยากเล่น คอลออฟดิวตี้` -> `games_family_availability_fast_path`
- `วิธีเล่น ลีกออฟเลเจนด์` -> `game_detail_fast_path`
- `วิธีเล่น สไปเดอร์แมน` -> `game_detail_fast_path`
- `อยากเล่น ฟอร์ทไนท์` -> `games_availability_fast_path`
- `วิธีเล่น ก็อดออฟวอร์` -> `game_detail_fast_path`
- `วิธีเล่น ไฟนอลแฟนตาซี` -> `game_detail_fast_path`
- `วิธีเล่น ฮอกวอตส์` -> `game_detail_fast_path`
- `วิธีเล่น เรสซิเดนต์อีวิล` -> `games_family_availability_fast_path`
- `วิธีเล่น นารูโตะ` -> `game_detail_fast_path`
- `วิธีเล่น มาริโอคาร์ท` -> `game_detail_fast_path`
- `วิธีเล่น โอเวอร์คุก` -> `game_detail_fast_path`
- `วิธีเล่น เซลด้า` -> `game_detail_fast_path`
- `วิธีเล่น ลิตเติลไนท์แมร์` -> `game_detail_fast_path`
- `วิธีเล่น อาโอวี` -> `games_known_unsupported_fast_path`

ไม่ได้ run Ground Truth ชุดใหญ่ตามคำสั่งผู้ใช้

## สถานะ Deploy

sync ไปโฟลเดอร์ 20 แล้ว แต่ยังไม่ได้ deploy production ผู้ใช้จะ deploy เอง

## ข้อจำกัด

- “ครบ” ในที่นี้หมายถึงครบตามรายชื่อเกมที่ระบบรู้จักใน `GAME_DETAILS`, `SUPPORTED_GAME_CATALOG`, และ known competition/unsupported aliases ตอนนี้
- ไม่ใช่ฐาน alias ภาษาไทยของทุกเกมในโลก
- ถ้ามีเกมใหม่เพิ่ม ควรเพิ่ม canonical game + alias ไทยใน normalization หรือย้ายต่อไปเป็น resolver กลางในอนาคต
