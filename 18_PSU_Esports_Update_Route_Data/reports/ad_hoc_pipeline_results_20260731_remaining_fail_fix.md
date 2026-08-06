# Ad Hoc Pipeline Test Log

- Generated: 2026-07-31T15:25:12
- JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_20260731_remaining_fail_fix.jsonl`
- Total questions: 4

## Summary

- games/game_control_lookup: 3
- service_fee/service_fee_query: 1

## Results

### 1. Overcooked 2 ราคาเท่าไหร่

- mode: `pipeline:structured_service_fee_by_game`
- route: `service_fee/service_fee_query`
- confidence: `0.86`
- elapsed: `0.7861` sec

คำตอบ:

Overcooked 2 / Overcooked! 2 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

Nintendo Switch Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา Nintendo Switch ทุกกลุ่มให้เทียบก่อน

Nintendo Switch 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 140 บาท

Nintendo Switch 1 ชั่วโมง (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท
•    บุคคลทั่วไป (General Adult): 280 บาท
หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

แหล่งข้อมูล:
- Overcooked! 2 | https://esports.phuket.psu.ac.th/Services/our-games
- service_fee_image_2026 | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### 2. Mario Kart Live: Home Circuit ปุ่มทั้งหมดมีอะไรบ้าง

- mode: `pipeline:structured_game_controls_no_current_game`
- route: `games/game_control_lookup`
- confidence: `0.93`
- elapsed: `0.1073` sec

คำตอบ:

ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ
จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน
เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Mario Bros. U Deluxe, Super Mario Odyssey
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

แหล่งข้อมูล:
- service_game_availability | https://esports.computing.psu.ac.th/

### 3. The Last of Us Part II ปุ่มเคลื่อนที่กดอะไร

- mode: `pipeline:structured_game_controls`
- route: `games/game_control_lookup`
- confidence: `0.96`
- elapsed: `0.1508` sec

คำตอบ:

The Last of Us Part II ปุ่มที่ตรงกับคำถาม:
PlayStation / PS5
•    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดิน การย่อง หรือการวิ่งของตัวละครไปตามฉาก
แหล่งข้อมูล: https://gameinputdatabase.com/game/16

แหล่งข้อมูล:
- game_controls_thelastofuspartii | https://gameinputdatabase.com/game/16

### 4. The Last of Us Part II ปุ่มหันมองจุดสนใจกดอะไร

- mode: `pipeline:structured_game_controls`
- route: `games/game_control_lookup`
- confidence: `0.96`
- elapsed: `0.1113` sec

คำตอบ:

The Last of Us Part II ปุ่มที่ตรงกับคำถาม:
PlayStation / PS5
•    L3 (Click Left Stick): หันมองจุดสนใจ - กดคลิกลงไปเพื่อหันมุมกล้องล็อกไปยังวัตถุ เบาะแส หรือเหตุการณ์สำคัญที่เกมต้องการให้สังเกตทันที
แหล่งข้อมูล: https://gameinputdatabase.com/game/16

แหล่งข้อมูล:
- game_controls_thelastofuspartii | https://gameinputdatabase.com/game/16
