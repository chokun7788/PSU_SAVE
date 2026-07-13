# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 40
- PASS: 9
- FAIL: 31
- ERROR: 0
- Pass rate: 22.50%
- Average latency: 0.0116s
- P95 latency: 0.0177s
- Keyword fail: 31
- Source fail: 11
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 29
- `pipeline:games_fast_path`: 9
- `pipeline:no_answer`: 2

## Route Category Distribution

- `competition_rules`: 31
- `games`: 9

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_tekken8_v2_004 | competition_rules | `competition_rules` | ชนะครบ 2 เกม | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_005 | competition_rules | `games` | เกมตัดสิน; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_006 | competition_rules | `competition_rules` | 3 รอบ | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_008 | competition_rules | `games` | No advantage; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_009 | competition_rules | `competition_rules` | Random | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_012 | competition_rules | `competition_rules` | ปรับแต่ง | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_013 | competition_rules | `competition_rules` | สกินมาตรฐาน | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_014 | competition_rules | `games` | อนุญาต; Assist; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_015 | competition_rules | `competition_rules` | Bug; Glitch | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_017 | competition_rules | `competition_rules` | ปรับแพ้ 1 รอบ | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_018 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง; เหตุฉุกเฉิน | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_019 | competition_rules | `games` | ปรับแพ้ทันที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_020 | competition_rules | `competition_rules` | ออกจากเกมก่อนจบ | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_021 | competition_rules | `competition_rules` | ปรับแพ้ทันที | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_022 | competition_rules | `competition_rules` | ห้าม; ปรับแพ้ทันที; competition_rules_tekken8_psu_esports | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_tekken8_v2_023 | competition_rules | `competition_rules` | คำตัดสิน; กรรมการ; competition_rules_tekken8_psu_esports | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_tekken8_v2_024 | competition_rules | `competition_rules` | ปรับเปลี่ยนกฎ; ไม่ต้องแจ้ง | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_025 | competition_rules | `games` | ถือเป็นที่สิ้นสุด; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_026 | competition_rules | `games` | ผู้ดูแล; กรรมการ; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_027 | competition_rules | `games` | ผู้จัดการแข่งขัน; ทันที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_029 | competition_rules | `competition_rules` | ปรับแต่ง | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_031 | competition_rules | `competition_rules` | 3 รอบ; 60 วินาที | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_032 | competition_rules | `competition_rules` | Random | คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit... |
| competition_tekken8_v2_033 | competition_rules | `competition_rules` | ชนะครบ 2 เกม | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_034 | competition_rules | `competition_rules` | เอฟเฟกต์; ออร่า | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_035 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_036 | competition_rules | `competition_rules` | เหตุฉุกเฉิน | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_037 | competition_rules | `competition_rules` | เปลี่ยนแปลง; กฎระเบียบ | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_038 | competition_rules | `games` | ไม่มีข้อยกเว้น; ปรับแพ้; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_tekken8_v2_039 | competition_rules | `competition_rules` | Assist | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_040 | competition_rules | `games` | เดี่ยว; 1v1; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_tekken8_20260703.jsonl`
