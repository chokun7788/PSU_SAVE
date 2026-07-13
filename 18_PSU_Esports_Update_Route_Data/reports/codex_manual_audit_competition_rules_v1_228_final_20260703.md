# Codex Manual Audit - Competition Rules v1 228 Final

วันที่ตรวจ: 2026-07-03

สรุป: อ่านผลเรียงข้อ 1-228 จากผลลัพธ์ pipeline และ strict audit รอบสุดท้าย ทุกข้ออยู่ในสถานะ PASS ตามเกณฑ์ strict ไม่มี major/minor ค้างในชุด competition rules

## Metrics

- Evaluator: PASS 228/228
- Strict audit: PASS 228/228
- Average latency: 0.0118 sec
- Max latency: 0.0260 sec

## Ordered Review

### 1. [PASS] competition_v1_001

- คำถาม: CS2 แข่งทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 2. [PASS] competition_v1_002

- คำถาม: Counter-Strike 2 ทีมละกี่คนตามกติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 3. [PASS] competition_v1_003

- คำถาม: กติกา CS2 ต้องมีผู้เล่นกี่คนต่อทีม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 4. [PASS] competition_v1_004

- คำถาม: CS2 สมาชิกทีมต้องมีกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 5. [PASS] competition_v1_005

- คำถาม: CS2 ลงแข่งพร้อมกันกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 6. [PASS] competition_v1_006

- คำถาม: CS2 roster ผู้เล่นหลักมีกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 7. [PASS] competition_v1_007

- คำถาม: รายการ PSU Phuket CS2 2026 ทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 8. [PASS] competition_v1_008

- คำถาม: CS2 ต้องส่งผู้เล่นกี่คนในทีม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 9. [PASS] competition_v1_009

- คำถาม: CS2 แข่งแบบทีม 5 คนใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 10. [PASS] competition_v1_010

- คำถาม: Counter Strike 2 ในรายการนี้ผู้เล่นต่อทีมกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 11. [PASS] competition_v1_011

- คำถาม: CS2 ถ้าถามเรื่องจำนวนคนในทีมตอบว่าอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 12. [PASS] competition_v1_012

- คำถาม: CS2 กติกาองค์ประกอบทีมกำหนดไว้กี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Expected keywords: CS2, ผู้เล่น 5 คน
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 13. [PASS] competition_v1_013

- คำถาม: CS2 ใช้ map อะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 14. [PASS] competition_v1_014

- คำถาม: CS2 map pool มีอะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 15. [PASS] competition_v1_015

- คำถาม: CS2 แผนที่ที่ใช้แข่งมีอะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 16. [PASS] competition_v1_016

- คำถาม: กติกา CS2 ระบุแผนที่อะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 17. [PASS] competition_v1_017

- คำถาม: PSU Phuket CS2 2026 ใช้แผนที่ไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 18. [PASS] competition_v1_018

- คำถาม: CS2 มี Ancient กับ Anubis ใน map pool ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 19. [PASS] competition_v1_019

- คำถาม: CS2 รายการนี้ใช้ Dust 2 หรือ Train ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 20. [PASS] competition_v1_020

- คำถาม: ขอรายชื่อ map ที่ใช้แข่ง CS2
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 21. [PASS] competition_v1_021

- คำถาม: Counter-Strike 2 map pool ในกติกาคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 22. [PASS] competition_v1_022

- คำถาม: CS2 แข่งบนแผนที่อะไรได้บ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 23. [PASS] competition_v1_023

- คำถาม: CS2 ban map จาก pool ไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 24. [PASS] competition_v1_024

- คำถาม: CS2 แผนที่ทั้งหมดตามกติกามีอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Expected keywords: Ancient, Anubis, Dust 2, Train
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 25. [PASS] competition_v1_025

- คำถาม: CS2 แข่งรูปแบบอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 26. [PASS] competition_v1_026

- คำถาม: CS2 เป็น Single Elimination ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 27. [PASS] competition_v1_027

- คำถาม: CS2 รอบรองกับรอบชิงเป็น BO อะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 28. [PASS] competition_v1_028

- คำถาม: กติกา CS2 format การแข่งขันเป็นยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 29. [PASS] competition_v1_029

- คำถาม: PSU Phuket CS2 2026 ใช้ระบบแข่งแบบไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 30. [PASS] competition_v1_030

- คำถาม: CS2 รอบชิงใช้ BO3 ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 31. [PASS] competition_v1_031

- คำถาม: CS2 รอบรองชนะเลิศแข่งกี่เกม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 32. [PASS] competition_v1_032

- คำถาม: Counter-Strike 2 tournament format คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 33. [PASS] competition_v1_033

- คำถาม: CS2 แข่งแพ้คัดออกหรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 34. [PASS] competition_v1_034

- คำถาม: CS2 รูปแบบทัวร์นาเมนต์ในเอกสารคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 35. [PASS] competition_v1_035

- คำถาม: CS2 รอบสำคัญเป็น Best of 3 ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 36. [PASS] competition_v1_036

- คำถาม: CS2 กติกาบอกว่า single elimination หรือไม่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Expected keywords: Single Elimination, BO3
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 37. [PASS] competition_v1_037

- คำถาม: CS2 technical pause ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 38. [PASS] competition_v1_038

- คำถาม: CS2 tactical timeout ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 39. [PASS] competition_v1_039

- คำถาม: CS2 pause ได้กี่ครั้งตามกติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 40. [PASS] competition_v1_040

- คำถาม: CS2 ขอหยุดเกม technical ได้กี่ครั้งและกี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 41. [PASS] competition_v1_041

- คำถาม: กติกา CS2 tactical timeout ครั้งละกี่วินาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 42. [PASS] competition_v1_042

- คำถาม: CS2 Technical Pause รวมได้ไม่เกินกี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 43. [PASS] competition_v1_043

- คำถาม: CS2 เวลานอก tactical timeout ได้ทีมละกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 44. [PASS] competition_v1_044

- คำถาม: CS2 ถ้าเครื่องมีปัญหาขอ pause ได้เท่าไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 45. [PASS] competition_v1_045

- คำถาม: Counter-Strike 2 pause policy เป็นยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 46. [PASS] competition_v1_046

- คำถาม: CS2 technical กับ tactical timeout ต่างกันยังไงในกติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 47. [PASS] competition_v1_047

- คำถาม: CS2 ขอ Tactical Timeout 4 ครั้งใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 48. [PASS] competition_v1_048

- คำถาม: CS2 หยุดเกมได้กี่ครั้งและใช้เวลากี่วินาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Expected keywords: Technical Pause, 2 ครั้ง, 10 นาที, Tactical Timeout, 4 ครั้ง, 30 วินาที
- Expected sources: competition_rules_cs2_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 49. [PASS] competition_v1_049

- คำถาม: VALORANT แข่งทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 50. [PASS] competition_v1_050

- คำถาม: วาโลทีมละกี่คนตามกติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 51. [PASS] competition_v1_051

- คำถาม: VALORANT สมาชิกทีมกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 52. [PASS] competition_v1_052

- คำถาม: กติกา VALORANT ต้องมีผู้เล่นกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 53. [PASS] competition_v1_053

- คำถาม: PSU Phuket VALORANT 2026 แข่งทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 54. [PASS] competition_v1_054

- คำถาม: VALORANT ลงแข่งพร้อมกันกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 55. [PASS] competition_v1_055

- คำถาม: วาโลผู้เล่นตัวจริงกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 56. [PASS] competition_v1_056

- คำถาม: VALORANT ทีม 5 คนใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 57. [PASS] competition_v1_057

- คำถาม: VALORANT roster ตัวจริงกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 58. [PASS] competition_v1_058

- คำถาม: กฎแข่งวาโลจำนวนผู้เล่นต่อทีมคือเท่าไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 59. [PASS] competition_v1_059

- คำถาม: VALORANT ในรายการนี้ใช้ทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 60. [PASS] competition_v1_060

- คำถาม: วาโลแข่งแบบกี่คนต่อทีม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Expected keywords: VALORANT, 5 คน
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 61. [PASS] competition_v1_061

- คำถาม: VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 62. [PASS] competition_v1_062

- คำถาม: VALORANT map pool มีอะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 63. [PASS] competition_v1_063

- คำถาม: วาโลใช้ map อะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 64. [PASS] competition_v1_064

- คำถาม: กติกา VALORANT ระบุแผนที่อะไรบ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 65. [PASS] competition_v1_065

- คำถาม: PSU Phuket VALORANT 2026 ใช้ map ไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 66. [PASS] competition_v1_066

- คำถาม: VALORANT มี Abyss กับ Ascent ใน map pool ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 67. [PASS] competition_v1_067

- คำถาม: วาโลแข่งบน Sunset ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 68. [PASS] competition_v1_068

- คำถาม: ขอรายชื่อแผนที่แข่ง VALORANT
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 69. [PASS] competition_v1_069

- คำถาม: VALORANT map pool ทั้งหมดมีอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 70. [PASS] competition_v1_070

- คำถาม: วาโล ban map จากแผนที่ชุดไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 71. [PASS] competition_v1_071

- คำถาม: VALORANT แข่งแผนที่อะไรได้บ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 72. [PASS] competition_v1_072

- คำถาม: กฎวาโลเรื่อง map pool คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Expected keywords: Abyss, Ascent, Sunset
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 73. [PASS] competition_v1_073

- คำถาม: VALORANT Tactical Timeout ขอได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 74. [PASS] competition_v1_074

- คำถาม: วาโล timeout ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 75. [PASS] competition_v1_075

- คำถาม: VALORANT เวลานอกได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 76. [PASS] competition_v1_076

- คำถาม: VALORANT tactical timeout ครั้งละกี่วินาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 77. [PASS] competition_v1_077

- คำถาม: กติกา VALORANT timeout ต่อแผนที่ได้เท่าไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 78. [PASS] competition_v1_078

- คำถาม: VALORANT เข้า Overtime ได้ timeout เพิ่มไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 79. [PASS] competition_v1_079

- คำถาม: วาโล Tactical Timeout ได้ทีมละกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 80. [PASS] competition_v1_080

- คำถาม: VALORANT ขอเวลานอก 60 วินาทีใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 81. [PASS] competition_v1_081

- คำถาม: VALORANT timeout ในรอบปกติได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 82. [PASS] competition_v1_082

- คำถาม: PSU Phuket VALORANT 2026 tactical timeout rule คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 83. [PASS] competition_v1_083

- คำถาม: วาโลเวลานอก tactical ต่อ map ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 84. [PASS] competition_v1_084

- คำถาม: VALORANT ถามเรื่อง tactical timeout ให้ตอบยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Expected keywords: Tactical Timeout, 2 ครั้ง, 60 วินาที, Overtime
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 85. [PASS] competition_v1_085

- คำถาม: VALORANT emergency pause ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 86. [PASS] competition_v1_086

- คำถาม: VALORANT technical pause รวมได้กี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 87. [PASS] competition_v1_087

- คำถาม: VALORANT pause ฉุกเฉินได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 88. [PASS] competition_v1_088

- คำถาม: วาโลหลุดเกมขอ emergency pause ได้เท่าไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 89. [PASS] competition_v1_089

- คำถาม: กติกา VALORANT หยุดฉุกเฉินได้ทีมละกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 90. [PASS] competition_v1_090

- คำถาม: VALORANT technical pause สูงสุดกี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 91. [PASS] competition_v1_091

- คำถาม: VALORANT Emergency Pause ต่อแผนที่ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 92. [PASS] competition_v1_092

- คำถาม: วาโลหยุดเกมฉุกเฉินรวมกี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 93. [PASS] competition_v1_093

- คำถาม: VALORANT ถ้า hardware มีปัญหาขอ pause ยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 94. [PASS] competition_v1_094

- คำถาม: VALORANT emergency pause policy คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 95. [PASS] competition_v1_095

- คำถาม: วาโล technical pause 10 นาทีใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 96. [PASS] competition_v1_096

- คำถาม: VALORANT pause ฉุกเฉินตามกฎตอบว่าอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Expected keywords: Emergency, 1 ครั้ง, 10 นาที
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 97. [PASS] competition_v1_097

- คำถาม: VALORANT agent ใหม่ใช้ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 98. [PASS] competition_v1_098

- คำถาม: VALORANT map ใหม่ใช้ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 99. [PASS] competition_v1_099

- คำถาม: วาโลเอเจนท์ใหม่ใช้แข่งได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 100. [PASS] competition_v1_100

- คำถาม: กติกา VALORANT agent ใหม่ต้องรอกี่สัปดาห์
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 101. [PASS] competition_v1_101

- คำถาม: VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนแข่ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 102. [PASS] competition_v1_102

- คำถาม: VALORANT ใช้เอเจนท์ที่เพิ่งออกใหม่ได้ทันทีไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 103. [PASS] competition_v1_103

- คำถาม: วาโล map ใหม่ใช้แข่งได้เลยหรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 104. [PASS] competition_v1_104

- คำถาม: VALORANT new agent restriction คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 105. [PASS] competition_v1_105

- คำถาม: VALORANT new map restriction ในกติกาคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 106. [PASS] competition_v1_106

- คำถาม: วาโล agent ใหม่รอ 2 สัปดาห์ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 107. [PASS] competition_v1_107

- คำถาม: VALORANT map ใหม่รอ 4 สัปดาห์ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 108. [PASS] competition_v1_108

- คำถาม: กฎวาโลเรื่อง content ใหม่เป็นยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Expected keywords: Agent, 2 สัปดาห์, 4 สัปดาห์
- Expected sources: competition_rules_valorant_psu_phuket_2026
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 109. [PASS] competition_v1_109

- คำถาม: สมาชิกในทีม ROV ต้องมีกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 110. [PASS] competition_v1_110

- คำถาม: RoV ทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 111. [PASS] competition_v1_111

- คำถาม: ROV แข่งกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 112. [PASS] competition_v1_112

- คำถาม: สมาชิกในทีม RoV กี่คนตามกติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 113. [PASS] competition_v1_113

- คำถาม: กติกา RoV บอกว่าลงแข่งฝ่ายละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 114. [PASS] competition_v1_114

- คำถาม: RoV เป็น 5v5 ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 115. [PASS] competition_v1_115

- คำถาม: Blueket Games RoV ทีมละกี่คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 116. [PASS] competition_v1_116

- คำถาม: RoV roster รวมมีกี่คนในไฟล์กติกา
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 117. [PASS] competition_v1_117

- คำถาม: ROV มีตัวสำรองกี่คนในเอกสาร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 118. [PASS] competition_v1_118

- คำถาม: RoV ถามจำนวนสมาชิกทีมควรตอบยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 119. [PASS] competition_v1_119

- คำถาม: Arena of Valor แข่งโหมดกี่ต่อกี่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 120. [PASS] competition_v1_120

- คำถาม: RoV ยืนยันได้ไหมว่าลงแข่งฝ่ายละ 5 คน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Expected keywords: 5v5, ฝ่ายละ 5 คน, ยังไม่พบจำนวนสมาชิกทีม
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 121. [PASS] competition_v1_121

- คำถาม: RoV ใช้สกินได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 122. [PASS] competition_v1_122

- คำถาม: ROV ใช้ skin ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 123. [PASS] competition_v1_123

- คำถาม: RoV ต้องใช้สกินอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 124. [PASS] competition_v1_124

- คำถาม: กติกา RoV อนุญาตให้ใช้สกินไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 125. [PASS] competition_v1_125

- คำถาม: Blueket Games RoV ใช้ Default Skin ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 126. [PASS] competition_v1_126

- คำถาม: RoV ห้ามใช้สกินอื่นไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 127. [PASS] competition_v1_127

- คำถาม: Arena of Valor แข่งต้องใช้ skin แบบไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 128. [PASS] competition_v1_128

- คำถาม: RoV ใช้สกินพิเศษได้หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 129. [PASS] competition_v1_129

- คำถาม: กฎ RoV เรื่องสกินคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 130. [PASS] competition_v1_130

- คำถาม: ROV default skin เท่านั้นไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 131. [PASS] competition_v1_131

- คำถาม: RoV ถ้าใช้สกินนอก default ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 132. [PASS] competition_v1_132

- คำถาม: RoV ในรายการนี้สกินต้องเป็นอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Expected keywords: Default Skin
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 133. [PASS] competition_v1_133

- คำถาม: RoV ถ้าเริ่มแข่งช้าเกิน 15 นาทีโดนอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 134. [PASS] competition_v1_134

- คำถาม: RoV มาสายเกิน 15 นาทีเป็นอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 135. [PASS] competition_v1_135

- คำถาม: ROV late start 15 นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 136. [PASS] competition_v1_136

- คำถาม: กติกา RoV เริ่มแข่งล่าช้าเกิน 15 นาทีลงโทษยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 137. [PASS] competition_v1_137

- คำถาม: Blueket Games RoV ถ้ามาสายโดนปรับแพ้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 138. [PASS] competition_v1_138

- คำถาม: RoV ถ้าทีมทำให้เริ่มช้าจะโดนอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 139. [PASS] competition_v1_139

- คำถาม: RoV เริ่มช้ากี่นาทีถึงปรับแพ้
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 140. [PASS] competition_v1_140

- คำถาม: Arena of Valor ล่าช้า 15 นาทีตามกฎเป็นยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 141. [PASS] competition_v1_141

- คำถาม: RoV แข่งช้าเกินเวลาที่กำหนดถูกปรับแพ้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 142. [PASS] competition_v1_142

- คำถาม: ROV ถ้าเริ่ม match ไม่ทัน 15 นาทีตอบว่าอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 143. [PASS] competition_v1_143

- คำถาม: กฎ RoV เรื่องมาสายคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 144. [PASS] competition_v1_144

- คำถาม: RoV late start rule ในเอกสารคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Expected keywords: 15 นาที, ปรับแพ้
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 145. [PASS] competition_v1_145

- คำถาม: RoV pause ได้กี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 146. [PASS] competition_v1_146

- คำถาม: RoV หลุดเกมหยุดได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 147. [PASS] competition_v1_147

- คำถาม: RoV disconnect ทำยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 148. [PASS] competition_v1_148

- คำถาม: กติกา RoV หยุดเกมได้ทีมละกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 149. [PASS] competition_v1_149

- คำถาม: RoV pause ครั้งละกี่นาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 150. [PASS] competition_v1_150

- คำถาม: Blueket Games RoV ถ้าเกมหลุดขอหยุดได้เท่าไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 151. [PASS] competition_v1_151

- คำถาม: RoV แต่ละทีมมีสิทธิ์หยุดเกมกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 152. [PASS] competition_v1_152

- คำถาม: Arena of Valor pause ได้สูงสุดกี่ครั้ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 153. [PASS] competition_v1_153

- คำถาม: RoV หยุดเกมได้ 5 ครั้งใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 154. [PASS] competition_v1_154

- คำถาม: ROV pause 1 นาทีต่อครั้งใช่หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 155. [PASS] competition_v1_155

- คำถาม: RoV disconnect แล้วกลับมาเล่นต่อเมื่อไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 156. [PASS] competition_v1_156

- คำถาม: กฎ RoV เรื่อง pause/disconnect คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Expected keywords: 5 ครั้ง, 1 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 157. [PASS] competition_v1_157

- คำถาม: RoV ขอเริ่มใหม่ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 158. [PASS] competition_v1_158

- คำถาม: RoV ก่อน first blood remake ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 159. [PASS] competition_v1_159

- คำถาม: RoV แข่งใหม่ได้ตอนไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 160. [PASS] competition_v1_160

- คำถาม: กติกา RoV rematch ทำได้เมื่อไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 161. [PASS] competition_v1_161

- คำถาม: RoV ขอแข่งใหม่ก่อน 2 นาทีได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 162. [PASS] competition_v1_162

- คำถาม: Blueket Games RoV ถ้าเกิด First Blood แล้ว remake ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 163. [PASS] competition_v1_163

- คำถาม: Arena of Valor เริ่มใหม่ได้ก่อน First Blood ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 164. [PASS] competition_v1_164

- คำถาม: RoV ถ้าเกิน 2 นาทีแล้วขอแข่งใหม่ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 165. [PASS] competition_v1_165

- คำถาม: RoV ต้องให้ฝ่ายตรงข้ามยินยอมเมื่อไหร่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 166. [PASS] competition_v1_166

- คำถาม: ROV rematch rule ตามเอกสารคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 167. [PASS] competition_v1_167

- คำถาม: RoV remake ก่อน First Blood และก่อน 2 นาทีใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 168. [PASS] competition_v1_168

- คำถาม: กฎ RoV เรื่องขอแข่งใหม่ตอบยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Expected keywords: First Blood, 2 นาที
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 169. [PASS] competition_v1_169

- คำถาม: RoV ใช้อุปกรณ์อะไรแข่ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 170. [PASS] competition_v1_170

- คำถาม: RoV ใช้ iPad แข่งได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 171. [PASS] competition_v1_171

- คำถาม: RoV ใช้ tablet ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 172. [PASS] competition_v1_172

- คำถาม: RoV แข่งด้วยเครื่องอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 173. [PASS] competition_v1_173

- คำถาม: กติกา RoV ต้องใช้มือถือไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 174. [PASS] competition_v1_174

- คำถาม: Blueket Games RoV อนุญาต iPad หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 175. [PASS] competition_v1_175

- คำถาม: Arena of Valor แข่งด้วยโทรศัพท์มือถือเท่านั้นไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 176. [PASS] competition_v1_176

- คำถาม: RoV ใช้ Tablet ในการแข่งขันได้หรือไม่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 177. [PASS] competition_v1_177

- คำถาม: ROV device rule คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 178. [PASS] competition_v1_178

- คำถาม: RoV อุปกรณ์ที่ใช้แข่งกำหนดยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 179. [PASS] competition_v1_179

- คำถาม: RoV ถ้าจะใช้ iPad ต้องได้ไหมตามกฎ
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 180. [PASS] competition_v1_180

- คำถาม: กฎ RoV เรื่องอุปกรณ์แข่งคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Expected keywords: โทรศัพท์มือถือ, ไม่อนุญาต, Tablet, iPad
- Expected sources: competition_rules_rov_blueket_2025_men
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 181. [PASS] competition_v1_181

- คำถาม: Tekken 8 เล่นแบบไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 182. [PASS] competition_v1_182

- คำถาม: Tekken 8 รูปแบบการแข่งขัน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 183. [PASS] competition_v1_183

- คำถาม: Tekken 8 แข่งกี่ต่อกี่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 184. [PASS] competition_v1_184

- คำถาม: กติกา Tekken 8 ใช้ format อะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 185. [PASS] competition_v1_185

- คำถาม: Tekken 8 เป็น 1v1 ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 186. [PASS] competition_v1_186

- คำถาม: Tekken 8 FT2 คือรูปแบบแข่งใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 187. [PASS] competition_v1_187

- คำถาม: Tekken 8 แข่งบน PS5 และเวลา 60 วินาทีไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 188. [PASS] competition_v1_188

- คำถาม: PSU Esports Tekken 8 แข่งแบบ offline หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 189. [PASS] competition_v1_189

- คำถาม: Tekken 8 รอบหนึ่งตั้งเวลากี่วินาที
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 190. [PASS] competition_v1_190

- คำถาม: Tekken 8 ใช้ Round 3 ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 191. [PASS] competition_v1_191

- คำถาม: Tekken 8 format ในเอกสารคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 192. [PASS] competition_v1_192

- คำถาม: Tekken 8 กติกาการแข่งขันสรุปยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Expected keywords: 1v1, PlayStation 5, FT2, 60 วินาที
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 193. [PASS] competition_v1_193

- คำถาม: Tekken 8 ใช้เครื่องอะไรแข่ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 194. [PASS] competition_v1_194

- คำถาม: Tekken 8 แข่งบนอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 195. [PASS] competition_v1_195

- คำถาม: Tekken 8 platform อะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 196. [PASS] competition_v1_196

- คำถาม: กติกา Tekken 8 ระบุเครื่องแข่งว่าอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 197. [PASS] competition_v1_197

- คำถาม: Tekken 8 ใช้ PS5 แข่งใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 198. [PASS] competition_v1_198

- คำถาม: PSU Esports Tekken 8 ใช้ PlayStation 5 หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 199. [PASS] competition_v1_199

- คำถาม: Tekken 8 อุปกรณ์หลักที่ใช้แข่งคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 200. [PASS] competition_v1_200

- คำถาม: Tekken 8 แข่งด้วยเครื่องเกมอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 201. [PASS] competition_v1_201

- คำถาม: Tekken 8 platform ตามเอกสารคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 202. [PASS] competition_v1_202

- คำถาม: Tekken 8 ใช้ console อะไรในการแข่ง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 203. [PASS] competition_v1_203

- คำถาม: Tekken 8 ต้องเล่นบน PlayStation 5 ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 204. [PASS] competition_v1_204

- คำถาม: กฎ Tekken 8 เรื่อง platform คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Expected keywords: PlayStation 5
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 205. [PASS] competition_v1_205

- คำถาม: Tekken 8 ใช้ DLC character ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 206. [PASS] competition_v1_206

- คำถาม: Tekken 8 ใช้ตัวละคร DLC ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 207. [PASS] competition_v1_207

- คำถาม: Tekken 8 เลือกตัวละครอะไรได้บ้าง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 208. [PASS] competition_v1_208

- คำถาม: กติกา Tekken 8 ห้าม DLC ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 209. [PASS] competition_v1_209

- คำถาม: Tekken 8 ใช้ customization ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 210. [PASS] competition_v1_210

- คำถาม: Tekken 8 ใช้ชุดแต่งตัวละครได้หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 211. [PASS] competition_v1_211

- คำถาม: PSU Esports Tekken 8 ตัวละคร DLC แข่งได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 212. [PASS] competition_v1_212

- คำถาม: Tekken 8 ใช้ skin custom ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 213. [PASS] competition_v1_213

- คำถาม: Tekken 8 character rule คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 214. [PASS] competition_v1_214

- คำถาม: Tekken 8 เลือกได้ทุกตัวยกเว้น DLC ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 215. [PASS] competition_v1_215

- คำถาม: Tekken 8 ห้าม customization ตามกฎหรือไม่
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 216. [PASS] competition_v1_216

- คำถาม: กฎ Tekken 8 เรื่องตัวละครและสกินคืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Expected keywords: ยกเว้นตัวละคร DLC, Customization
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 217. [PASS] competition_v1_217

- คำถาม: Tekken 8 pause ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 218. [PASS] competition_v1_218

- คำถาม: Tekken 8 หยุดเกมได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 219. [PASS] competition_v1_219

- คำถาม: Tekken 8 กด pause โดนอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 220. [PASS] competition_v1_220

- คำถาม: กติกา Tekken 8 ถ้ากด pause หลังเริ่มเกมเป็นยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 221. [PASS] competition_v1_221

- คำถาม: Tekken 8 ตั้งใจกดหยุดเกมโดนปรับแพ้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 222. [PASS] competition_v1_222

- คำถาม: Tekken 8 pause แล้วแพ้ 1 Round ใช่ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 223. [PASS] competition_v1_223

- คำถาม: PSU Esports Tekken 8 ห้าม pause หรือเปล่า
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 224. [PASS] competition_v1_224

- คำถาม: Tekken 8 หยุดเกมได้เฉพาะกรณีไหน
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 225. [PASS] competition_v1_225

- คำถาม: Tekken 8 ถ้าทั้งสองฝ่ายยินยอม pause ได้ไหม
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 226. [PASS] competition_v1_226

- คำถาม: Tekken 8 pause penalty คืออะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 227. [PASS] competition_v1_227

- คำถาม: Tekken 8 กด pause ระหว่างแข่งลงโทษยังไง
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic

### 228. [PASS] competition_v1_228

- คำถาม: กฎ Tekken 8 เรื่อง pause ตอบว่าอะไร
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Strict: `pass`
- คำตอบหลัก: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Expected keywords: ไม่อนุญาต, Pause, แพ้ 1 Round
- Expected sources: competition_rules_tekken8_psu_esports
- ตรวจโดย Codex: ผ่าน เพราะ route ถูก แหล่งข้อมูลถูก และคำตอบหลักมี keyword สำคัญตาม Ground Truth
- Audit note: ไม่พบปัญหาจาก strict heuristic
