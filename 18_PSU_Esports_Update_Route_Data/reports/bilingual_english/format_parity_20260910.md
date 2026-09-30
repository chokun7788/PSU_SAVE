# Thai-English Format Parity Audit

> Scope: representative core FAQ pairs. This checks route and response shape, not translation quality.

## Summary
- Pairs checked: 8
- Status counts: {'format_aligned': 7, 'source_format_gap': 1}

## Pair Results

| Case | Thai route/mode | English route/mode | Thai shape | English shape | Status |
|---|---|---|---:|---:|---|
| catalog | games/list / pipeline:structured_games_catalog | games/games_lookup / pipeline:structured_games_catalog_en | 52 lines, 45 bullets | 52 lines, 45 bullets | format_aligned |
| price | service_fee/service_fee_query / pipeline:deterministic_calculator_fast | service_fee/service_fee_query / pipeline:structured_service_fee_en | 6 lines, 3 bullets | 6 lines, 3 bullets | format_aligned |
| schedule_tomorrow | schedule/schedule_query / pipeline:calendar_schedule_fast_path | schedule/schedule_query / pipeline:structured_schedule_en | 10 lines, 4 bullets | 10 lines, 4 bullets | format_aligned |
| booking | reservation/booking_policy / pipeline:structured_reservation_fact | reservation/booking_steps / pipeline:rule_en | 8 lines, 6 bullets | 8 lines, 6 bullets | format_aligned |
| studio_rules | rules/studio_rules / pipeline:studio_rules_overview_fast_path | rules/studio_rules_summary / pipeline:rule_en | 9 lines, 7 bullets | 9 lines, 7 bullets | format_aligned |
| member_role | overview/members_lookup / pipeline:structured_members_role_lookup | overview/members_lookup / pipeline:structured_members_source_th | 4 lines, 1 bullets | 3 lines, 1 bullets | format_aligned |
| vr_equipment | equipment/list / pipeline:structured_equipment_catalog | equipment/equipment_catalog / pipeline:structured_equipment_catalog_en | 4 lines, 1 bullets | 4 lines, 2 bullets | format_aligned |
| unknown_game | games/game_availability_lookup / pipeline:no_answer | games/unknown_game / pipeline:games_unknown_target_en | 1 lines, 0 bullets | 2 lines, 0 bullets | source_format_gap |

## Answer Previews

### catalog
- Thai: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ / PC Zone (6 เกม)
- English: There are currently 42 verified games available. / PC Zone (6 games)
- Assessment: format_aligned

### price
- Thai: ราคา PC 1 ชั่วโมง (1 คน) / •    PSU Student and Staff: 0 บาท
- English: PC - 1 hour (1 people) / - PSU students and staff: 0 THB
- Assessment: format_aligned

### schedule_tomorrow
- Thai: พรุ่งนี้ 11/09/2026 (วันศุกร์): วันศุกร์เปิดช่วงเช้า 09:00-12:00 แต่ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์ / วันที่อ้างอิงของระบบ: วันนี้คือ 10/09/2026 (วันพฤหัสบดี) ตามเวลาไทย
- English: Tomorrow, Friday, 11/09/2026: 09:00-12:00 is open for play and booking; 13:00-16:00 is a maintenance period for equipment inspection and cleaning; play and booking are unavailable. / System reference date: today is Thurs
- Assessment: format_aligned

### booking
- Thai: ขั้นตอนจองโดยสรุป: / •    เลือกบริการหรือโซนที่ต้องการใช้
- English: Booking steps: / • Select a service.
- Assessment: format_aligned

### studio_rules
- Thai: กติกาการใช้บริการในศูนย์โดยสรุปครับ / •    ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย
- English: Key studio rules: / • Leave belongings before using the service; the studio is not responsible for lost property.
- Assessment: format_aligned

### member_role
- Thai: ตำแหน่ง ผู้จัดการ มี 1 คนครับ / •    นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ (PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)
- English: PSU Esports Studio - Phuket member record(s) for the requested role (names and roles are shown exactly as in the official Thai source): / - นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการค
- Assessment: format_aligned

### vr_equipment
- Thai: อุปกรณ์ใน PlayStation 5 Zone: / PlayStation 5 Zone / VR Zone
- English: Verified equipment in VR Zone: / - PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Assessment: format_aligned

### unknown_game
- Thai: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ
- English: I could not find Minecraft in the verified PSU game records. I will not substitute another game. / Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- Assessment: source_format_gap
