# User Question Bank Evaluation

- Generated at: 2026-07-15T21:40:52
- Total questions: 100
- Total wall time: 166.032s

## Summary By Strategy
- fastpath/rulebase: 39
- llm: 2
- pipeline: 16
- rag/vector: 43

## Results

### PBC-001 play_booking_controls ข้อ 1
- Question: จอง PS5 ต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.1515s | Wall: 0.1516s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ถ้าต้องการจอง PlayStation 5 ให้เลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล...

### PBC-002 play_booking_controls ข้อ 2
- Question: จอง Nintendo Switch ต้องเลือกอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:equipment_game_catalog_fast_path`
- Route: `equipment/equipment_game_catalog`
- Strategy: `fastpath/rulebase`
- Latency: 0.4932s | Wall: 0.4933s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: สรุปเกมที่เล่นได้ในโซนที่ถาม:  Nintendo Switch Zone (16 เกม) • Mario Kart 8 Deluxe • Mario Kart Live: Home Circuit • Overcooked 2 • Super Smash Bros Ultimate • Nintendo Switch Sports • Animal Crossing: New Horizons • It Takes Two • LITTLE NIGHTMARES II • Luigi...

### PBC-003 play_booking_controls ข้อ 3
- Question: จอง VR ครึ่งชั่วโมงได้ไหม
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 11.059s | Wall: 11.059s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: VR Zone มีเกมที่ยืนยันได้ดังนี้  VR Zone (2 เกม) • Beat Saber • Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### PBC-004 play_booking_controls ข้อ 4
- Question: จอง Cockpit ต้องจองล่วงหน้ากี่ชั่วโมง
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 23.1214s | Wall: 23.1214s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Cockpit Zone มีเกมที่ยืนยันได้ดังนี้  Cockpit Zone (1 เกม) • Gran Turismo 7 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### PBC-005 play_booking_controls ข้อ 5
- Question: จอง PC ต้องกรอกข้อมูลอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:equipment_game_catalog_fast_path`
- Route: `equipment/equipment_game_catalog`
- Strategy: `fastpath/rulebase`
- Latency: 0.2074s | Wall: 0.2074s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: สรุปเกมที่เล่นได้ในโซนที่ถาม:  PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty: Warzone • TEKKEN 8 • League of Legends  อุปกรณ์หลักของ PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำน...

### PBC-006 play_booking_controls ข้อ 6
- Question: หลังจองต้องจ่ายเงินภายในกี่นาที
- Expected: in_kb
- Mode: `pipeline:payment_fast_path`
- Route: `reservation/payment_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.3015s | Wall: 0.3015s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-007 play_booking_controls ข้อ 7
- Question: ถ้าจองผิดเวลาต้องแก้ยังไง
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1737s | Wall: 0.1737s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-008 play_booking_controls ข้อ 8
- Question: ยกเลิกการจองต้องทำก่อนกี่ชั่วโมง
- Expected: in_kb
- Mode: `pipeline:booking_cancel_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.2677s | Wall: 0.2677s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมงครับ หากต้องการแก้ไขข้อมูลหรือเวลาใช้งาน ต้องยกเลิกการจองเดิมก่อนแล้วจองใหม่ตามขั้นตอนของระบบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-009 play_booking_controls ข้อ 9
- Question: ตอนเช็คอินต้องใช้บัตรอะไร
- Expected: in_kb
- Mode: `pipeline:checkin_fast_path`
- Route: `reservation/checkin_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1881s | Wall: 0.1882s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-010 play_booking_controls ข้อ 10
- Question: เช็คอินล่วงหน้าได้กี่นาที
- Expected: in_kb
- Mode: `pipeline:checkin_fast_path`
- Route: `reservation/checkin_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1628s | Wall: 0.1629s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-011 play_booking_controls ข้อ 11
- Question: จองได้สูงสุดกี่ session ต่อครั้ง
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1889s | Wall: 0.1889s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-012 play_booking_controls ข้อ 12
- Question: ถ้าแนบสลิปผิดต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:mixed_reservation_fast`
- Route: `reservation/payment_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1614s | Wall: 0.1614s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-013 play_booking_controls ข้อ 13
- Question: จองแทนเพื่อนได้ไหม
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.0859s | Wall: 0.0859s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-014 play_booking_controls ข้อ 14
- Question: ถ้าไม่จ่ายเงินหลัง booking จะเกิดอะไรขึ้น
- Expected: in_kb
- Mode: `pipeline:category_rule_fast_path`
- Route: `reservation/payment_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.5434s | Wall: 0.5434s
- Sources: rule_payment_10_minutes: https://esports.computing.psu.ac.th/
- Answer: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก และหากต้องการใช้บริการต้องทำรายการจองใหม่ แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-015 play_booking_controls ข้อ 15
- Question: อยากจองเครื่องเล่นเกมกับเพื่อนต้องเริ่มตรงไหน
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `contact/contact_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.3105s | Wall: 0.3106s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน...

### PBC-016 play_booking_controls ข้อ 16
- Question: ถ้าไม่มีบัตรนักศึกษาตอนจองทำยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.5362s | Wall: 0.5362s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน...

### PBC-017 play_booking_controls ข้อ 17
- Question: จอง VR 1 ชั่วโมงกับ 30 นาทีต่างกันยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `fastpath/rulebase`
- Latency: 0.7118s | Wall: 0.7119s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ถ้าต้องการจอง VR ให้เลือกบริการ VR Station และเลือกรอบ 30 นาทีหรือ 1 ชั่วโมงตามที่ระบบมีให้เลือก ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National I...

### PBC-018 play_booking_controls ข้อ 18
- Question: จอง Nintendo สำหรับ 4 คนต้องเลือกแบบไหน
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 29.15s | Wall: 29.15s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Nintendo Switch Zone มีเกมที่ยืนยันได้ดังนี้  Nintendo Switch Zone (16 เกม) • Mario Kart 8 Deluxe • Mario Kart Live: Home Circuit • Overcooked 2 • Super Smash Bros Ultimate • Nintendo Switch Sports • Animal Crossing: New Horizons • It Takes Two • LITTLE NIGHTM...

### PBC-019 play_booking_controls ข้อ 19
- Question: อยากเล่นพวงมาลัยต้องจองโซนอะไร
- Expected: in_kb
- Mode: `pipeline:related_guidance_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.4974s | Wall: 0.4975s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: ถ้าอยากเล่นเกมขับรถ แนะนำ Cockpit Zone - เหตุผล: Cockpit Zone คือโซนจำลองการขับรถ/เกมแข่งรถ ใช้เล่น Gran Turismo 7 ด้วยชุดพวงมาลัยและเบาะขับ - อุปกรณ์หลัก: TV 65 นิ้ว 2 เครื่อง (2 Units), Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด (2 Un...

### PBC-020 play_booking_controls ข้อ 20
- Question: ถ้าไปถึงช้ากว่าเวลาจองจะยังเล่นได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.6244s | Wall: 0.6245s
- Sources: curated_checkin_30_minutes: https://esports.computing.psu.ac.th/ | curated_checkin_late_cancel: https://esports.computing.psu.ac.th/ | curated_time_change_policy: https://esports.computing.psu.ac.th/
- Answer: ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-021 play_booking_controls ข้อ 21
- Question: จองแล้วเปลี่ยนคนเล่นได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.2868s | Wall: 0.2879s
- Sources: curated_time_change_policy: https://esports.computing.psu.ac.th/ | curated_booking_no_edit: https://esports.computing.psu.ac.th/ | curated_booking_non_transferable: https://esports.computing.psu.ac.th/
- Answer: สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-022 play_booking_controls ข้อ 22
- Question: จองแล้วขอเลื่อนวันได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.5388s | Wall: 0.5397s
- Sources: curated_booking_no_edit: https://esports.computing.psu.ac.th/ | curated_booking_non_transferable: https://esports.computing.psu.ac.th/ | curated_checkin_30_minutes: https://esports.computing.psu.ac.th/
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-023 play_booking_controls ข้อ 23
- Question: ระบบจองออนไลน์อยู่ที่ไหน
- Expected: in_kb
- Mode: `pipeline:category_rule_fast_path`
- Route: `contact/contact_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2479s | Wall: 0.2479s
- Sources: rule_contact_location: https://esports.phuket.psu.ac.th/Contact-Us
- Answer: PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### PBC-024 play_booking_controls ข้อ 24
- Question: ก่อนเข้าใช้บริการต้องทำอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.4545s | Wall: 0.4545s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### PBC-025 play_booking_controls ข้อ 25
- Question: ถ้าจะจองหลายอุปกรณ์พร้อมกันต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.2586s | Wall: 0.2586s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน...

### PBC-026 play_booking_controls ข้อ 26
- Question: จอง PlayStation 5 ใช้เวลารอบละกี่นาที
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 20.3442s | Wall: 20.3442s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้  PlayStation 5 Zone (18 เกม) • TEKKEN 8 • Marvel's Spider-Man 2 • Fortnite • God of War Ragnarok • Overcooked 2 • Gran Turismo 7 • Beat Saber • It Takes Two • LITTLE NIGHTMARES II • Monster Hunter Rise • EA Sports FC...

### PBC-027 play_booking_controls ข้อ 27
- Question: จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 18.4084s | Wall: 18.4085s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Nintendo Switch Zone มีเกมที่ยืนยันได้ดังนี้  Nintendo Switch Zone (16 เกม) • Mario Kart 8 Deluxe • Mario Kart Live: Home Circuit • Overcooked 2 • Super Smash Bros Ultimate • Nintendo Switch Sports • Animal Crossing: New Horizons • It Takes Two • LITTLE NIGHTM...

### PBC-028 play_booking_controls ข้อ 28
- Question: ถ้าระบบจองไม่ขึ้นควรถามใคร
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.299s | Wall: 0.299s
- Sources: curated_checkin_late_cancel: https://esports.computing.psu.ac.th/ | curated_booking_no_edit: https://esports.computing.psu.ac.th/ | curated_reservation_max_sessions: https://esports.computing.psu.ac.th/
- Answer: หากไม่เช็คอินก่อนถึงเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงินใด ๆ ทั้งสิ้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-029 play_booking_controls ข้อ 29
- Question: จองแล้วต้องตรวจสอบอีเมลไหม
- Expected: in_kb
- Mode: `pipeline:category_rule_fast_path`
- Route: `contact/contact_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2882s | Wall: 0.2891s
- Sources: rule_contact_email: https://esports.phuket.psu.ac.th/Contact-Us
- Answer: อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### PBC-030 play_booking_controls ข้อ 30
- Question: จ่ายเงินผ่านบัญชีอะไร
- Expected: in_kb
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2189s | Wall: 0.219s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### PBC-031 play_booking_controls ข้อ 31
- Question: สอนขั้นตอนจองแบบสั้นๆ
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1829s | Wall: 0.1829s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-032 play_booking_controls ข้อ 32
- Question: ถ้าอยากเล่นวันนี้ต้องจองทันทีได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.4511s | Wall: 0.4511s
- Sources: curated_checkin_late_cancel: https://esports.computing.psu.ac.th/ | curated_cancel_1_hour: https://esports.computing.psu.ac.th/ | curated_reservation_advance_time: https://esports.computing.psu.ac.th/
- Answer: หากไม่เช็คอินก่อนถึงเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงินใด ๆ ทั้งสิ้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-033 play_booking_controls ข้อ 33
- Question: walk in ได้ไหมหรือต้องจองก่อน
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.3359s | Wall: 0.3359s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-034 play_booking_controls ข้อ 34
- Question: จองแล้วลืมเช็คอินจะเป็นอะไรไหม
- Expected: in_kb
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Strategy: `pipeline`
- Latency: 0.6955s | Wall: 0.6965s
- Sources: curated_reservation_advance_time: https://esports.computing.psu.ac.th/ | curated_reservation_max_sessions: https://esports.computing.psu.ac.th/ | curated_payment_10_minutes: https://esports.computing.psu.ac.th/ | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  1. จอง ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/  2. ลืมเช็คอินจะเป็นอะไรไหม สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าส...

### PBC-035 play_booking_controls ข้อ 35
- Question: ต้องชำระเงินก่อนเล่นไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/payment_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.2901s | Wall: 0.2901s
- Sources: curated_booking_steps: https://esports.computing.psu.ac.th/ | curated_checkin_late_cancel: https://esports.computing.psu.ac.th/ | curated_payment_bank: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-036 play_booking_controls ข้อ 36
- Question: ถ้าอยากเล่น PS5 กับเพื่อนสองคนต้องจองยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.6235s | Wall: 0.6235s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ถ้าต้องการจอง PlayStation 5 ให้เลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล...

### PBC-037 play_booking_controls ข้อ 37
- Question: ถ้าอยากเล่น Switch สี่คนต้องจองยังไง
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.4316s | Wall: 0.4316s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ถ้าต้องการจอง Nintendo Switch ให้เลือกบริการ Nintendo Switch และเลือกจำนวนผู้เล่น/รอบเวลาตามที่ระบบมีให้เลือก ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff...

### PBC-038 play_booking_controls ข้อ 38
- Question: ถ้าอยากลอง VR ครั้งแรกควรจองแบบไหน
- Expected: in_kb
- Mode: `pipeline:games_fast_path`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 25.9154s | Wall: 25.9155s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: VR Zone มีเกมที่ยืนยันได้ดังนี้  VR Zone (2 เกม) • Beat Saber • Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### PBC-039 play_booking_controls ข้อ 39
- Question: ถ้าอยากเล่นเกมขับรถต้องจองอะไร
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.1674s | Wall: 0.1675s
- Sources: curated_cancel_1_hour: https://esports.computing.psu.ac.th/ | curated_reservation_advance_time: https://esports.computing.psu.ac.th/ | curated_booking_steps: https://esports.computing.psu.ac.th/
- Answer: การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-040 play_booking_controls ข้อ 40
- Question: ถ้าจองผิดชื่อแก้ไขได้ไหม
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `fastpath/rulebase`
- Latency: 0.2253s | Wall: 0.2253s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-041 play_booking_controls ข้อ 41
- Question: TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5928s | Wall: 0.5929s
- Sources: game_control_summary_ps5_tekken_8: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_11_heat_smash: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว - Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)...

### PBC-042 play_booking_controls ข้อ 42
- Question: TEKKEN 8 ปุ่มเตะขวากดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5285s | Wall: 0.5286s
- Sources: game_control_ps5_tekken_8_04_right_kick: local://control_game/TEKKEN 8 Standard Edition.json | game_control_summary_ps5_tekken_8: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-043 play_booking_controls ข้อ 43
- Question: TEKKEN 8 ปุ่มต่อยซ้ายคือปุ่มไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5019s | Wall: 0.502s
- Sources: game_control_ps5_tekken_8_01_left_punch: local://control_game/TEKKEN 8 Standard Edition.json | game_control_summary_ps5_tekken_8: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-044 play_booking_controls ข้อ 44
- Question: TEKKEN 8 ปุ่มเปิด Heat คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4208s | Wall: 0.4209s
- Sources: game_control_ps5_tekken_8_10_heat_activate: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_11_heat_smash: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร - R1 (While in Heat): ฮีทสแมช - ปลดปล่อยท่าโจมตีเผด็จศึกอันทรงพลังปิดฉากคอมโบ...

### PBC-045 play_booking_controls ข้อ 45
- Question: TEKKEN 8 ปุ่ม pause คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2276s | Wall: 0.2277s
- Sources: tekken8_pause_penalty: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร  หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอ...

### PBC-046 play_booking_controls ข้อ 46
- Question: Mario Kart 8 Deluxe ปุ่มเร่งเครื่องคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.6466s | Wall: 0.6467s
- Sources: game_control_nintendo_mario_kart_8_deluxe_02_accelerate: local://control_game/Mario_Kart 8_Deluxe.json | game_control_summary_nintendo_mario_kart_8_deluxe: local://control_game/Mario_Kart 8_Deluxe.json
- Answer: Mario Kart 8 Deluxe บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - A: เร่งเครื่อง - กดค้างไว้ตลอดเพื่อเร่งเครื่องยนต์ให้รถวิ่งไปข้างหน้า แหล่งข้อมูล: local://control_game/Mario_Kart 8_Deluxe.json

### PBC-047 play_booking_controls ข้อ 47
- Question: Mario Kart 8 Deluxe ปุ่มดริฟต์กดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.4898s | Wall: 0.4898s
- Sources: game_control_nintendo_mario_kart_8_deluxe_06_drift: local://control_game/Mario_Kart 8_Deluxe.json | game_control_summary_nintendo_mario_kart_8_deluxe: local://control_game/Mario_Kart 8_Deluxe.json
- Answer: Mario Kart 8 Deluxe บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - ZR: ดริฟต์ - ใช้กระโดดและดริฟต์ขณะเข้าโค้งเพื่อทำความเร็ว หรือใช้ทำท่าผาดโผนเมื่อกระโดดออกจากเนินเร่งความเร็ว แหล่งข้อมูล: local://control_game/Mario_Kart 8_Deluxe.json

### PBC-048 play_booking_controls ข้อ 48
- Question: Mario Kart 8 Deluxe ปุ่มใช้ไอเทมคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5657s | Wall: 0.5657s
- Sources: game_control_nintendo_mario_kart_8_deluxe_05_use_item_horn: local://control_game/Mario_Kart 8_Deluxe.json | game_control_summary_nintendo_mario_kart_8_deluxe: local://control_game/Mario_Kart 8_Deluxe.json
- Answer: Mario Kart 8 Deluxe บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - ZL: ใช้ไอเทม / บีบแตร - ใช้ไอเทมที่เก็บมาจากกล่องสุ่ม หากไม่มีไอเทมจะเป็นการบีบแตรรถ แหล่งข้อมูล: local://control_game/Mario_Kart 8_Deluxe.json

### PBC-049 play_booking_controls ข้อ 49
- Question: Mario Kart Live Home Circuit ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.7189s | Wall: 0.719s
- Sources: game_control_summary_nintendo_mario_kart_live_home_circuit: local://control_game/Mario Kart Live Home Circuit.json | game_control_nintendo_mario_kart_live_home_circuit_05_drift: local://control_game/Mario Kart Live Home Circuit.json
- Answer: Mario Kart Live: Home Circuit บน Nintendo Switch มีปุ่มควบคุมดังนี้: ขณะขับ: - Left Stick: เลี้ยว - บังคับพวงมาลัยรถคาร์ทซ้ายหรือขวา - A: เร่งเครื่อง - กดค้างเพื่อเร่งความเร็วรถไปข้างหน้า - B: เบรก / ถอยหลัง - ชะลอรถ หรือกดค้างเพื่อถอยหลัง - L: ใช้ไอเทม - ใช้ง...

### PBC-050 play_booking_controls ข้อ 50
- Question: Mario Kart Live Home Circuit ปุ่มเร่งเครื่องกดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.6686s | Wall: 0.6686s
- Sources: game_control_nintendo_mario_kart_live_home_circuit_02_accelerate: local://control_game/Mario Kart Live Home Circuit.json | game_control_summary_nintendo_mario_kart_live_home_circuit: local://control_game/Mario Kart Live Home Circuit.json
- Answer: Mario Kart Live: Home Circuit บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - A: เร่งเครื่อง - กดค้างเพื่อเร่งความเร็วรถไปข้างหน้า แหล่งข้อมูล: local://control_game/Mario Kart Live Home Circuit.json

### PBC-051 play_booking_controls ข้อ 51
- Question: Call of Duty ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.2814s | Wall: 0.2814s
- Sources: game_control_ps5_call_of_duty_modern_warfare_iii_01_jump_mantle: local://control_game/Call of Duty Modern Warfare III.json | game_control_ps5_the_last_of_us_part_ii_12_jump: local://control_game/The Last of Us Part II.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - L1: กระโดด / ปีนป่าย - กระโดดข้ามสิ่งกีดขวาง (จุดเด่นของ Bumper Jumper) แหล่งข้อมูล: local://control_game/Call of Duty Modern Warfare III.json

### PBC-052 play_booking_controls ข้อ 52
- Question: Call of Duty ปุ่มยิงคือปุ่มไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.4159s | Wall: 0.4159s
- Sources: game_control_summary_ps5_call_of_duty_modern_warfare_iii: local://control_game/Call of Duty Modern Warfare III.json | game_control_ps5_call_of_duty_modern_warfare_iii_09_switch_weapon: local://control_game/Call of Duty Modern Warfare III.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - L1: กระโดด / ปีนป่าย - กระโดดข้ามสิ่งกีดขวาง (จุดเด่นของ Bumper Jumper) - R3: เปลี่ยนท่า / สไลด์ / พุ่งหลบ - กดหรือกดค้างขณะวิ่งเพื่อสไลด์หรือพุ่ง (จุดเด่นของ Tactical) - Cross: ใช้อุป...

### PBC-053 play_booking_controls ข้อ 53
- Question: Call of Duty ปุ่มเล็งคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4335s | Wall: 0.4336s
- Sources: game_control_ps5_call_of_duty_modern_warfare_iii_05_aim_down_sight: local://control_game/Call of Duty Modern Warfare III.json | game_control_summary_ps5_call_of_duty_modern_warfare_iii: local://control_game/Call of Duty Modern Warfare III.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - L2: เล็งผ่านศูนย์เล็ง - กดค้างเพื่อยกปืนเล็ง - Triangle: สลับอาวุธ - สลับปืนหลักและปืนรอง - Circle: โจมตีประชิด - ใช้มีดฟันหรือพานท้ายปืนทุบศัตรู - R2: ยิงอาวุธ - กดยิงปืน...

### PBC-054 play_booking_controls ข้อ 54
- Question: Call of Duty ปุ่มรีโหลดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5018s | Wall: 0.5019s
- Sources: game_control_ps5_call_of_duty_modern_warfare_iii_08_interact_reload: local://control_game/Call of Duty Modern Warfare III.json | game_control_summary_ps5_call_of_duty_modern_warfare_iii: local://control_game/Call of Duty Modern Warfare III.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Square: โต้ตอบ / รีโหลด - เปลี่ยนกระสุนปืนหรือเก็บไอเทม แหล่งข้อมูล: local://control_game/Call of Duty Modern Warfare III.json

### PBC-055 play_booking_controls ข้อ 55
- Question: Naruto X Boruto ปุ่มโจมตีคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4731s | Wall: 0.4731s
- Sources: game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_03_close_range_attack: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json | game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_08_guard: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Circle: โจมตีระยะประชิด - ต่อย/เตะ ทำคอมโบกระบวนท่า - R2: ป้องกัน - ตั้งการ์ดบล็อกการโจมตี - R1: กำลังเสริม 2 - เรียกตัวละครซัพพอร์ตคนที่ 2 - Square: ดาวกระ...

### PBC-056 play_booking_controls ข้อ 56
- Question: Naruto X Boruto ปุ่มคาถานินจาคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5747s | Wall: 0.5748s
- Sources: game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_04_ninjutsu: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json | game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_11_use_battle_item_ninja_tools: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Triangle: คาถานินจา / จักระ - รีดเร้นจักระเพื่อใช้คาถาหรือท่าไม้ตายลับ (Secret Technique) แหล่งข้อมูล: local://control_game/Naruto X Boruto Ultimate Ninja S...

### PBC-057 play_booking_controls ข้อ 57
- Question: Naruto X Boruto ปุ่มสลับร่างคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5284s | Wall: 0.5285s
- Sources: game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_07_substitution_ninjutsu: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json | game_control_summary_ps5_naruto_x_boruto_ultimate_ninja_storm_connections: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - L2: คาถาสลับร่าง - สลับร่างหลบการโจมตี (ใช้เกจหลบหลีก) - Cross: กระโดด - กระโดด หรือพุ่งตัวเข้าหาศัตรู - R2: ป้องกัน - ตั้งการ์ดบล็อกการโจมตี - Square: ดาวก...

### PBC-058 play_booking_controls ข้อ 58
- Question: Little Nightmares II ปุ่มวิ่งคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5188s | Wall: 0.5189s
- Sources: game_control_ps5_little_nightmares_ii_04_sprint: local://control_game/LITTLE_NIGHTMARES_II.json | game_control_ps5_little_nightmares_ii_02_camera: local://control_game/LITTLE_NIGHTMARES_II.json
- Answer: Little Nightmares II บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Square: วิ่งเร็ว - กดเพื่อวิ่งสปรินต์ ใช้เพิ่มความเร็วในการเคลื่อนที่หรือวิ่งหนี - R (Right Stick): มุมกล้อง - แพนมุมกล้องเพื่อดูสภาพแวดล้อม และใช้ควบคุมทิศทางของไฟฉาย - Circle: ไฟฉาย...

### PBC-059 play_booking_controls ข้อ 59
- Question: Little Nightmares II ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.299s | Wall: 0.299s
- Sources: game_control_ps5_little_nightmares_ii_03_jump_throw_attack: local://control_game/LITTLE_NIGHTMARES_II.json | game_control_ps5_little_nightmares_ii_02_camera: local://control_game/LITTLE_NIGHTMARES_II.json
- Answer: Little Nightmares II บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Cross: กระโดด / ขว้าง / โจมตี - ใช้สำหรับกระโดด ขว้างไอเทม หรือใช้เหวี่ยงอาวุธโจมตี แหล่งข้อมูล: local://control_game/LITTLE_NIGHTMARES_II.json

### PBC-060 play_booking_controls ข้อ 60
- Question: It Takes Two ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.295s | Wall: 0.295s
- Sources: game_control_ps5_it_takes_two_05_jump: local://control_game/It_Take_Two.json | game_control_summary_ps5_it_takes_two: local://control_game/It_Take_Two.json
- Answer: It Takes Two บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Cross (กากบาท): กระโดด - ใช้กระโดดข้ามสิ่งกีดขวาง (สามารถประยุกต์ใช้เพื่อ Double Jump ได้) แหล่งข้อมูล: local://control_game/It_Take_Two.json

### PBC-061 play_booking_controls ข้อ 61
- Question: It Takes Two ปุ่มโต้ตอบคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4091s | Wall: 0.4092s
- Sources: game_control_ps5_it_takes_two_07_interact: local://control_game/It_Take_Two.json | game_control_summary_ps5_it_takes_two: local://control_game/It_Take_Two.json
- Answer: It Takes Two บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Triangle (สามเหลี่ยม): โต้ตอบ - ใช้โต้ตอบกับสิ่งแวดล้อม เช่น ดึงคันโยก, หมุนวาล์ว, หรือคุยกับ NPC แหล่งข้อมูล: local://control_game/It_Take_Two.json

### PBC-062 play_booking_controls ข้อ 62
- Question: Overcooked 2 ปุ่มหยิบของคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4837s | Wall: 0.4837s
- Sources: game_control_summary_ps5_overcooked: local://control_game/Overcooked + Overcooked! 2.json | game_control_ps5_overcooked_06_pause: local://control_game/Overcooked + Overcooked! 2.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-063 play_booking_controls ข้อ 63
- Question: Overcooked 2 ปุ่มหั่นของคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4486s | Wall: 0.4486s
- Sources: game_control_summary_ps5_overcooked: local://control_game/Overcooked + Overcooked! 2.json | game_control_ps5_overcooked_03_chop_throw: local://control_game/Overcooked + Overcooked! 2.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-064 play_booking_controls ข้อ 64
- Question: Super Smash Bros Ultimate ปุ่มโจมตีคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5472s | Wall: 0.5473s
- Sources: game_control_nintendo_super_smash_bros_ultimate_03_attack: local://control_game/Super Smash Bros Ultimate.json | game_control_nintendo_super_smash_bros_ultimate_04_special: local://control_game/Super Smash Bros Ultimate.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Super Smash Bros Ultimate ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-065 play_booking_controls ข้อ 65
- Question: Super Smash Bros Ultimate ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3564s | Wall: 0.3564s
- Sources: game_control_nintendo_super_smash_bros_ultimate_05_jump: local://control_game/Super Smash Bros Ultimate.json | game_control_summary_nintendo_super_smash_bros_ultimate: local://control_game/Super Smash Bros Ultimate.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Super Smash Bros Ultimate ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-066 play_booking_controls ข้อ 66
- Question: Nintendo Switch Sports ใช้จอยยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `equipment/zone_equipment_lookup`
- Strategy: `rag/vector`
- Latency: 0.446s | Wall: 0.446s
- Sources: game_control_nintendo_moving_out_01_grab: local://control_game/Movine_Out_2.json | game_control_ps5_ea_sports_fc_24_03_through_pass: local://control_game/EA Sports FC 24.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Nintendo Switch Sports ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-067 play_booking_controls ข้อ 67
- Question: Beat Saber เล่นยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_detail_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.1751s | Wall: 0.1751s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง แนวเกม: เกม VR Rhythm วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง เล่นได้ที่: VR Zone แหล่งข้อมูล: https://e...

### PBC-068 play_booking_controls ข้อ 68
- Question: Gran Turismo 7 ใช้พวงมาลัยยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:games_fast_path`
- Route: `games/games_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2211s | Wall: 0.2212s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Cockpit Zone มีเกมที่ยืนยันได้ดังนี้  Cockpit Zone (1 เกม) • Gran Turismo 7 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### PBC-069 play_booking_controls ข้อ 69
- Question: เกมนี้มีปุ่มอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1379s | Wall: 0.1379s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-070 play_booking_controls ข้อ 70
- Question: เล่นยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0267s | Wall: 0.0268s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-071 play_booking_controls ข้อ 71
- Question: วิธีใช้จอย
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0335s | Wall: 0.0336s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-072 play_booking_controls ข้อ 72
- Question: มีปุ่มอะไรบ้างถ้ายังไม่ได้บอกชื่อเกม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.4249s | Wall: 0.4249s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-073 play_booking_controls ข้อ 73
- Question: ปุ่มทั้งหมดของเกมที่เพิ่งถามคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_meta_clarification`
- Route: `games/game_meta_clarification`
- Strategy: `pipeline`
- Latency: 0.5056s | Wall: 0.5056s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: - `มีเกมอะไรบ้าง` - `PS5 มีเกมอะไรบ้าง` - `TEKKEN 8 คือเกมอะไร` - `TEKKEN 8 มีปุ่มอะไรบ้าง` - `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### PBC-074 play_booking_controls ข้อ 74
- Question: ถ้าถามต่อว่าใช้จอยยังไงระบบจำเกมเดิมไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_meta_clarification`
- Route: `games/game_meta_clarification`
- Strategy: `pipeline`
- Latency: 0.62s | Wall: 0.62s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: - `มีเกมอะไรบ้าง` - `PS5 มีเกมอะไรบ้าง` - `TEKKEN 8 คือเกมอะไร` - `TEKKEN 8 มีปุ่มอะไรบ้าง` - `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### PBC-075 play_booking_controls ข้อ 75
- Question: ถามปุ่มเฉพาะของเกมที่ไม่มีข้อมูลจะตอบยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_meta_clarification`
- Route: `games/game_meta_clarification`
- Strategy: `pipeline`
- Latency: 0.6932s | Wall: 0.6933s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: - `มีเกมอะไรบ้าง` - `PS5 มีเกมอะไรบ้าง` - `TEKKEN 8 คือเกมอะไร` - `TEKKEN 8 มีปุ่มอะไรบ้าง` - `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### PBC-076 play_booking_controls ข้อ 76
- Question: Minecraft มีปุ่มอะไรบ้างในศูนย์
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.3157s | Wall: 0.3157s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-077 play_booking_controls ข้อ 77
- Question: ROV มีปุ่มในเครื่องศูนย์ไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.3223s | Wall: 0.3223s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-078 play_booking_controls ข้อ 78
- Question: เกมที่ไม่มีชื่อชัดเจนควรตอบปุ่มไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.502s | Wall: 0.5021s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-079 play_booking_controls ข้อ 79
- Question: ถ้าอยากรู้ปุ่มของ PS5 ต้องถามแบบไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.167s | Wall: 0.1674s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-080 play_booking_controls ข้อ 80
- Question: controller ของ Nintendo ใช้ยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.2802s | Wall: 0.2803s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-081 play_booking_controls ข้อ 81
- Question: ปุ่ม Options ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.4108s | Wall: 0.4109s
- Sources: game_control_ps5_tekken_8_12_pause: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_09_special_style: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Options: หยุดเกม - หยุดเกมชั่วคราวเพื่อเข้าสู่หน้าต่างเมนู เช่น การเช็ก Move List (รายการท่า) หรือการตั้งค่าอื่น ๆ แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-082 play_booking_controls ข้อ 82
- Question: ปุ่ม Cross ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.3611s | Wall: 0.3611s
- Sources: game_control_ps5_tekken_8_03_left_kick: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_01_left_punch: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-083 play_booking_controls ข้อ 83
- Question: ปุ่ม Circle ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.4261s | Wall: 0.4262s
- Sources: game_control_ps5_tekken_8_04_right_kick: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_03_left_kick: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-084 play_booking_controls ข้อ 84
- Question: ปุ่ม Triangle ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.497s | Wall: 0.497s
- Sources: game_control_ps5_tekken_8_02_right_punch: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_09_special_style: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Triangle: สลับอาวุธ - สลับปืนหลักและปืนรอง แหล่งข้อมูล: local://control_game/Call of Duty Modern Warfare III.json

### PBC-085 play_booking_controls ข้อ 85
- Question: ปุ่ม Square ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.394s | Wall: 0.394s
- Sources: game_control_ps5_tekken_8_01_left_punch: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_03_left_kick: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-086 play_booking_controls ข้อ 86
- Question: D-Pad ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.3873s | Wall: 0.3873s
- Sources: game_control_ps5_tekken_8_05_jump: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_06_move_backward: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - D-Pad Up: กระโดด - ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ - D-Pad Left: ถอยหลัง / บล็อก - บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพ...

### PBC-087 play_booking_controls ข้อ 87
- Question: L1 ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.3182s | Wall: 0.3183s
- Sources: game_control_ps5_tekken_8_09_special_style: local://control_game/TEKKEN 8 Standard Edition.json | game_control_summary_ps5_tekken_8: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - L1: สเปเชียลสไตล์ - กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบและท่าไม้ตายของตัวละครนั้น ๆ ได้ง่ายด้วยปุ่มเดียว แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-088 play_booking_controls ข้อ 88
- Question: R1 ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.303s | Wall: 0.3031s
- Sources: game_control_ps5_tekken_8_10_heat_activate: local://control_game/TEKKEN 8 Standard Edition.json | game_control_ps5_tekken_8_11_heat_smash: local://control_game/TEKKEN 8 Standard Edition.json
- Answer: TEKKEN 8 บน PlayStation / PS5 ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร แหล่งข้อมูล: local://control_game/TEKKEN 8 Standard Edition.json

### PBC-089 play_booking_controls ข้อ 89
- Question: Mario Kart Live ปุ่มจัดการแผนที่คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.7158s | Wall: 0.7159s
- Sources: game_control_nintendo_mario_kart_live_home_circuit_10_map: local://control_game/Mario Kart Live Home Circuit.json | game_control_summary_nintendo_mario_kart_live_home_circuit: local://control_game/Mario Kart Live Home Circuit.json
- Answer: Mario Kart Live: Home Circuit บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - R: จัดการแผนที่ แหล่งข้อมูล: local://control_game/Mario Kart Live Home Circuit.json

### PBC-090 play_booking_controls ข้อ 90
- Question: Mario Kart Live ปุ่มดูข้อมูลรถคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5464s | Wall: 0.5465s
- Sources: game_control_summary_nintendo_mario_kart_live_home_circuit: local://control_game/Mario Kart Live Home Circuit.json | game_control_nintendo_mario_kart_live_home_circuit_10_map: local://control_game/Mario Kart Live Home Circuit.json
- Answer: Mario Kart Live: Home Circuit บน Nintendo Switch มีปุ่มควบคุมดังนี้: ขณะขับ: - Left Stick: เลี้ยว - บังคับพวงมาลัยรถคาร์ทซ้ายหรือขวา - A: เร่งเครื่อง - กดค้างเพื่อเร่งความเร็วรถไปข้างหน้า - B: เบรก / ถอยหลัง - ชะลอรถ หรือกดค้างเพื่อถอยหลัง - L: ใช้ไอเทม - ใช้ง...

### PBC-091 play_booking_controls ข้อ 91
- Question: Mario Kart 8 ปุ่มเบรกคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4213s | Wall: 0.4214s
- Sources: game_control_nintendo_mario_kart_8_deluxe_03_brake: local://control_game/Mario_Kart 8_Deluxe.json | game_control_summary_nintendo_mario_kart_8_deluxe: local://control_game/Mario_Kart 8_Deluxe.json
- Answer: Mario Kart 8 Deluxe บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - B: เบรก / ถอยหลัง - แตะเพื่อเบรกชะลอความเร็ว หรือกดค้างไว้เมื่อรถหยุดนิ่งเพื่อขับถอยหลัง แหล่งข้อมูล: local://control_game/Mario_Kart 8_Deluxe.json

### PBC-092 play_booking_controls ข้อ 92
- Question: Mario Kart 8 ปุ่มมองหลังคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4641s | Wall: 0.4641s
- Sources: game_control_nintendo_mario_kart_8_deluxe_04_look_backward: local://control_game/Mario_Kart 8_Deluxe.json | game_control_nintendo_mario_kart_8_deluxe_03_brake: local://control_game/Mario_Kart 8_Deluxe.json
- Answer: Mario Kart 8 Deluxe บน Nintendo Switch ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้: - X: มองหลัง - หันมุมกล้องไปมองด้านหลังเพื่อเช็กระยะห่างของคู่แข่งหรือไอเทมที่ตามมา แหล่งข้อมูล: local://control_game/Mario_Kart 8_Deluxe.json

### PBC-093 play_booking_controls ข้อ 93
- Question: Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5665s | Wall: 0.5666s
- Sources: game_control_summary_ps5_call_of_duty_modern_warfare_iii: local://control_game/Call of Duty Modern Warfare III.json | game_control_ps5_call_of_duty_modern_warfare_iii_04_melee: local://control_game/Call of Duty Modern Warfare III.json
- Answer: Call of Duty: Modern Warfare III บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - L1: กระโดด / ปีนป่าย - กระโดดข้ามสิ่งกีดขวาง (จุดเด่นของ Bumper Jumper) - R3: เปลี่ยนท่า / สไลด์ / พุ่งหลบ - กดหรือกดค้างขณะวิ่งเพื่อสไลด์หรือพุ่ง (จุดเด่นของ Tactical) - Cross: ใช้อุป...

### PBC-094 play_booking_controls ข้อ 94
- Question: Naruto X Boruto ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5579s | Wall: 0.5579s
- Sources: game_control_ps5_naruto_x_boruto_ultimate_ninja_storm_connections_08_guard: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json | game_control_summary_ps5_naruto_x_boruto_ultimate_ninja_storm_connections: local://control_game/Naruto X Boruto Ultimate Ninja Storm Connections.json
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - LS (Left Stick): เคลื่อนที่ - บังคับทิศทางของตัวละคร - RS (Right Stick) Left/Right: เปลี่ยนตัวละครหลัก - ดันซ้ายหรือขวาเพื่อสลับบังคับเพื่อนร่วมทีมทันที - Circle: โจมตี...

### PBC-095 play_booking_controls ข้อ 95
- Question: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.5288s | Wall: 0.5289s
- Sources: game_control_summary_ps5_overcooked: local://control_game/Overcooked + Overcooked! 2.json | game_control_ps5_overcooked_06_pause: local://control_game/Overcooked + Overcooked! 2.json
- Answer: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ

### PBC-096 play_booking_controls ข้อ 96
- Question: Super Smash Bros ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.6538s | Wall: 0.6539s
- Sources: game_control_summary_nintendo_super_smash_bros_ultimate: local://control_game/Super Smash Bros Ultimate.json | game_control_nintendo_super_smash_bros_ultimate_03_attack: local://control_game/Super Smash Bros Ultimate.json
- Answer: Super Smash Bros. Ultimate บน Nintendo Switch มีปุ่มควบคุมดังนี้: - L (Left Stick): เคลื่อนที่ - ใช้เดิน วิ่ง หรือย่อตัว รวมถึงกำหนดทิศทางการโจมตีท่าต่าง ๆ - R (Right Stick): โจมตีสแมช - ก้านอนาล็อกขวาใช้สำหรับปล่อยท่า Smash Attack ไปตามทิศทางที่ดันอย่างรวดเร็...

### PBC-097 play_booking_controls ข้อ 97
- Question: It Takes Two ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.4991s | Wall: 0.4994s
- Sources: game_control_summary_ps5_it_takes_two: local://control_game/It_Take_Two.json | game_control_ps5_it_takes_two_11_rope_grapple: local://control_game/It_Take_Two.json
- Answer: It Takes Two บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเคลื่อนที่และการเดินของตัวละคร - L3 (Click Left Stick): วิ่งสปรินต์ - กดก้านอนาล็อกซ้ายลงไปเพื่อวิ่งสปรินต์ เพิ่มความเร็วในการเคลื่อนที่ - R (Right Stick): มุมก...

### PBC-098 play_booking_controls ข้อ 98
- Question: Little Nightmares II ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_vector_first`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 0.6939s | Wall: 0.6939s
- Sources: game_control_ps5_little_nightmares_ii_02_camera: local://control_game/LITTLE_NIGHTMARES_II.json | game_control_ps5_little_nightmares_ii_04_sprint: local://control_game/LITTLE_NIGHTMARES_II.json
- Answer: Little Nightmares II บน PlayStation / PS5 มีปุ่มควบคุมดังนี้: - L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดินและเคลื่อนที่ของตัวละคร - R (Right Stick): มุมกล้อง - แพนมุมกล้องเพื่อดูสภาพแวดล้อม และใช้ควบคุมทิศทางของไฟฉาย - Cross: กระโดด / ขว้าง / โจมตี - ใช้...

### PBC-099 play_booking_controls ข้อ 99
- Question: ถ้าไม่รู้ชื่อเกมแต่ถามปุ่ม ระบบควรถามกลับไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_meta_clarification`
- Route: `games/game_meta_clarification`
- Strategy: `pipeline`
- Latency: 0.2303s | Wall: 0.2304s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: - `มีเกมอะไรบ้าง` - `PS5 มีเกมอะไรบ้าง` - `TEKKEN 8 คือเกมอะไร` - `TEKKEN 8 มีปุ่มอะไรบ้าง` - `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### PBC-100 play_booking_controls ข้อ 100
- Question: วิธีเล่นเกมที่ไม่อยู่ในรายการต้องตอบยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.6312s | Wall: 0.6312s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ
