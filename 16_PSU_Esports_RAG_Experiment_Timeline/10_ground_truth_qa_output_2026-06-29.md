# Ground Truth QA Output - PSU Esports Local RAG

- จำนวน Ground Truth ทั้งหมด: 105 ข้อ
- จำนวนที่แสดงในไฟล์นี้: 105 ข้อ
- ผลประเมินล่าสุด: PASS 105 / FAIL 0
- หมายเหตุ: ไฟล์ ground_truth_full.jsonl ตอนนี้ยังไม่มีเฉลยเป็นประโยคเต็มทุกข้อ จึงแสดงเฉลยจาก expected_keywords และ expected_source_keywords

1.คำถาม : PSU Esports Studio Phuket คืออะไร
คำตอบ(จากAI) : คำตอบ: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (rule_overview_identity / curated_overview_identity)
เฉลย : ต้องมีคำสำคัญ: ศูนย์พัฒนาการเรียนรู้, อีสปอร์ต, ภูเก็ต | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.01 | retrieved_ids: rule_overview_identity

2.คำถาม : ศูนย์อีสปอร์ตนี้ก่อตั้งโดยหน่วยงานไหน
คำตอบ(จากAI) : คำตอบ: - Mission ของ PSU Esports Studio - Phuket คือการยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต ผ่านสิ่งอำนวยความสะดวกและอุปกรณ์ที่ช่วยเสริมสร้างการเรียนรู้ให้กับนักเล่นเกม นักศึกษา และผู้สนใจ โดยก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ - PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_overview_mission) - https://esports.phuket.psu.ac.th/home (curated_overview_identity)
เฉลย : ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาลัยการคอมพิวเตอร์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.035 | retrieved_ids: curated_overview_mission, curated_overview_identity, home-overview-001

3.คำถาม : What is the mission of PSU Esports Studio Phuket?
คำตอบ(จากAI) : Answer: The studio was established by Prince of Songkla University and operated by the College of Computing. Its mission is to elevate esports education and excellence by providing facilities and equipment that support learning for gamers, students, and interested learners. Sources: - https://esports.phuket.psu.ac.th/home (rule_overview_mission / curated_overview_mission)
เฉลย : ต้องมีคำสำคัญ: esports education, College of Computing | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_overview_mission

4.คำถาม : ศูนย์นี้เน้นช่วยกลุ่มผู้ใช้แบบไหนบ้าง
คำตอบ(จากAI) : คำตอบ: - PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ - Mission ของ PSU Esports Studio - Phuket คือการยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต ผ่านสิ่งอำนวยความสะดวกและอุปกรณ์ที่ช่วยเสริมสร้างการเรียนรู้ให้กับนักเล่นเกม นักศึกษา และผู้สนใจ โดยก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_overview_identity) - https://esports.phuket.psu.ac.th/home (curated_overview_mission)
เฉลย : ต้องมีคำสำคัญ: นักเล่นเกม, นักศึกษา, ผู้สนใจ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.037 | retrieved_ids: curated_overview_identity, curated_overview_mission, home-overview-001

5.คำถาม : ศูนย์มี Gaming PC กี่เครื่อง
คำตอบ(จากAI) : คำตอบ: - ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)
เฉลย : ต้องมีคำสำคัญ: MSI MAG Infinite S3 14th, 10 Units | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.028 | retrieved_ids: curated_home_equipment_pc_zone, home-equipment-pc-001, curated_home_equipment_cockpit_zone, curated_home_equipment_vr_zone

6.คำถาม : ใน PC Zone มีอุปกรณ์อะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_pc_zone)
เฉลย : ต้องมีคำสำคัญ: Gaming Monitor, Gaming Chair, Gaming Keyboard, Gaming Headset, Gaming Mouse, Gaming PC | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.03 | retrieved_ids: curated_home_equipment_pc_zone, curated_home_equipment_vr_zone, curated_home_equipment_ps5_zone, curated_home_equipment_cockpit_zone

7.คำถาม : Cockpit Zone มีอุปกรณ์อะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - Cockpit Zone มี TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 Steering Wheel Stand with Seat Set 2 Units และ Pulse Elite Wireless Headset 2 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_cockpit_zone)
เฉลย : ต้องมีคำสำคัญ: Logitech G923, Driving Force Shifter, Racezone Full Cockpit | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.029 | retrieved_ids: curated_home_equipment_cockpit_zone, curated_home_equipment_pc_zone, curated_home_equipment_vr_zone, curated_home_equipment_nintendo_zone

8.คำถาม : Cockpit Zone มีจอหรือทีวีอะไรให้ใช้
คำตอบ(จากAI) : คำตอบ: - Cockpit Zone มี TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 Steering Wheel Stand with Seat Set 2 Units และ Pulse Elite Wireless Headset 2 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_cockpit_zone)
เฉลย : ต้องมีคำสำคัญ: TV 65, 2 Units | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.03 | retrieved_ids: curated_home_equipment_cockpit_zone, curated_home_equipment_nintendo_zone, curated_home_equipment_pc_zone, curated_home_equipment_vr_zone

9.คำถาม : Nintendo Switch Zone มีทีวีขนาดกี่นิ้ว
คำตอบ(จากAI) : คำตอบ: - Nintendo Switch Zone มี TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch (OLED model) Neon Red Neon Blue set 1 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_nintendo_zone)
เฉลย : ต้องมีคำสำคัญ: TV 86, 1 Units | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.03 | retrieved_ids: curated_home_equipment_nintendo_zone, home-equipment-nintendo-001, curated_home_equipment_cockpit_zone, curated_home_equipment_vr_zone

10.คำถาม : Nintendo Switch ที่ศูนย์เป็นรุ่นอะไร
คำตอบ(จากAI) : คำตอบ: - Nintendo Switch Zone มี TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch (OLED model) Neon Red Neon Blue set 1 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_nintendo_zone)
เฉลย : ต้องมีคำสำคัญ: Nintendo Switch, OLED model, Neon Red Neon Blue | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.031 | retrieved_ids: curated_home_equipment_nintendo_zone, home-equipment-nintendo-001, curated_home_equipment_pc_zone, curated_home_equipment_vr_zone

11.คำถาม : ศูนย์มี PlayStation 5 กี่เครื่อง
คำตอบ(จากAI) : คำตอบ: - PLAYstation5 Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_ps5_zone)
เฉลย : ต้องมีคำสำคัญ: PlayStation 5 Slim, 2 Units | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.029 | retrieved_ids: curated_home_equipment_ps5_zone, curated_home_equipment_vr_zone, curated_home_equipment_cockpit_zone, home-equipment-ps5-001

12.คำถาม : VR Zone มีอุปกรณ์อะไร
คำตอบ(จากAI) : คำตอบ: - VR Zone มี PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 Units และ PlayStation VR รุ่น Sony PlayStation VR2 1 Unit แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_equipment_vr_zone)
เฉลย : ต้องมีคำสำคัญ: PlayStation VR, Sony PlayStation VR2, 1 Unit | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.028 | retrieved_ids: curated_home_equipment_vr_zone, curated_home_equipment_pc_zone, curated_home_equipment_cockpit_zone, curated_home_equipment_nintendo_zone

13.คำถาม : เกมยอดนิยมของศูนย์มีอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber - เกมที่ปรากฏในรายการ PlayStation 5 ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection - เกมที่ปรากฏในรายการ PC ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/home (curated_home_popular_games_list) - https://esports.phuket.psu.ac.th/home (curated_games_popular) - https://esports.computing.psu.ac.th/ (curated_games_ps5) - https://esports.computing.psu.ac.th/ (curated_games_pc)
เฉลย : ต้องมีคำสำคัญ: Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8, Beat Saber | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.032 | retrieved_ids: curated_home_popular_games_list, curated_games_popular, curated_games_ps5, curated_games_pc

14.คำถาม : PS5 มีเกมอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: เกม PlayStation 5 ที่มีในรายการ ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_ps5_games / Reservation, curated_games_ps5, reservation-service-ps5)
เฉลย : ต้องมีคำสำคัญ: Call of Duty, God of War Ragnarok, TEKKEN 8 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_ps5_games

15.คำถาม : PlayStation 5 มีเกม Marvel’s Spider-Man 2 ไหม
คำตอบ(จากAI) : คำตอบ: เกม PlayStation 5 ที่มีในรายการ ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_ps5_games / Reservation, curated_games_ps5, reservation-service-ps5)
เฉลย : ต้องมีคำสำคัญ: Marvel’s Spider-Man 2 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_ps5_games

16.คำถาม : Nintendo Switch มีเกม Mario Kart 8 Deluxe ไหม
คำตอบ(จากAI) : คำตอบ: เกม Nintendo Switch ที่มีในรายการ ได้แก่ Pokémon Champions, Animal Crossing: New Horizon, It Takes Two, Little Nightmares II, Luigi’s Mansion 3, Mario Kart 8 Deluxe, Mario Party Superstars, Monster Hunter Rise, Moving Out 2, New Super Mario Bros. U Deluxe, Nintendo Switch Sports, Overcooked, Overcooked 2, Ring Fit Adventure, Super Mario Odyssey, Super Smash Bros Ultimate และ The Legend of Zelda: Breath of The Wild แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_switch_games / Reservation, curated_games_switch, reservation-service-nintendo)
เฉลย : ต้องมีคำสำคัญ: Mario Kart 8 Deluxe | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_switch_games

17.คำถาม : Nintendo Switch มีเกมอะไรบ้าง ยกตัวอย่างให้หน่อย
คำตอบ(จากAI) : คำตอบ: เกม Nintendo Switch ที่มีในรายการ ได้แก่ Pokémon Champions, Animal Crossing: New Horizon, It Takes Two, Little Nightmares II, Luigi’s Mansion 3, Mario Kart 8 Deluxe, Mario Party Superstars, Monster Hunter Rise, Moving Out 2, New Super Mario Bros. U Deluxe, Nintendo Switch Sports, Overcooked, Overcooked 2, Ring Fit Adventure, Super Mario Odyssey, Super Smash Bros Ultimate และ The Legend of Zelda: Breath of The Wild แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_switch_games / Reservation, curated_games_switch, reservation-service-nintendo)
เฉลย : ต้องมีคำสำคัญ: Animal Crossing, It Takes Two, Mario Party, Overcooked | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_switch_games

18.คำถาม : PC มีเกมอะไรให้เล่นบ้าง
คำตอบ(จากAI) : คำตอบ: เกม PC ที่มีในรายการ ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_pc_games / Reservation, curated_games_pc, reservation-service-pc)
เฉลย : ต้องมีคำสำคัญ: Counter-Strike 2, League of Legends, PUBG, VALORANT | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_pc_games

19.คำถาม : VR Station มีเกมอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: เกม VR Station ที่มีในรายการ ได้แก่ Beat Saber และ Horizon Call of the Mountain แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_vr_games / Reservation, curated_games_vr, reservation-service-vr)
เฉลย : ต้องมีคำสำคัญ: Beat Saber, Horizon Call of the Mountain | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_vr_games

20.คำถาม : Cockpit ใช้เล่นเกมอะไรได้
คำตอบ(จากAI) : คำตอบ: Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_cockpit_games / Reservation, curated_games_cockpit, reservation-service-cockpit)
เฉลย : ต้องมีคำสำคัญ: Gran Turismo 7 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_cockpit_games

21.คำถาม : บริการ Nintendo Switch รองรับกี่คน
คำตอบ(จากAI) : คำตอบ: - บริการ Nintendo Switch ในระบบจองมี Nintendo Swich (1-2 Persons) 60 min และ Nintendo Swich (1-4 Persons) 60 min - บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_nintendo_capacity) - https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration) - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration)
เฉลย : ต้องมีคำสำคัญ: 1-2 Persons, 1-4 Persons | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.031 | retrieved_ids: curated_reservation_service_nintendo_capacity, curated_reservation_service_ps5_duration, curated_reservation_service_pc_duration, curated_reservation_service_cockpit_game

22.คำถาม : PC แต่ละเครื่องให้บริการกี่นาที
คำตอบ(จากAI) : คำตอบ: - บริการ PC #01 ถึง PC #10 ในระบบจองเป็นบริการสำหรับ 1 Person และกำหนดระยะเวลา 60 min ต่อรอบ - บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min - บริการ Nintendo Switch ในระบบจองมี Nintendo Swich (1-2 Persons) 60 min และ Nintendo Swich (1-4 Persons) 60 min แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_pc_duration) - https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration) - https://esports.computing.psu.ac.th/ (curated_reservation_service_nintendo_capacity)
เฉลย : ต้องมีคำสำคัญ: 60 min | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.034 | retrieved_ids: curated_reservation_service_pc_duration, curated_reservation_service_ps5_duration, curated_reservation_service_nintendo_capacity, curated_reservation_service_cockpit_game

23.คำถาม : VR Station มีรอบกี่นาทีบ้าง
คำตอบ(จากAI) : คำตอบ: - VR Station ในระบบจองมีบริการ 2 แบบ คือ VR Station (1-5 Persons) 1 Hour 60 min และ VR Station (1-5 Persons) 30 Mins 30 min - บริการ PlayStation 5 ในระบบจองมี PlayStation 5 #1 (1-2 Persons) 60 min และ PlayStation 5 #2 (1-2 Persons) 60 min แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_reservation_service_vr_duration) - https://esports.computing.psu.ac.th/ (curated_reservation_service_ps5_duration)
เฉลย : ต้องมีคำสำคัญ: 1 Hour, 60 min, 30 Mins, 30 min | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.034 | retrieved_ids: curated_reservation_service_vr_duration, curated_reservation_service_ps5_duration, reservation-service-vr-001, reservation-service-list-002

24.คำถาม : ต้องจองล่วงหน้าอย่างน้อยกี่ชั่วโมง
คำตอบ(จากAI) : คำตอบ: ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_booking_advance / curated_reservation_advance_time)
เฉลย : ต้องมีคำสำคัญ: อย่างน้อย 1 ชั่วโมง | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_booking_advance

25.คำถาม : การจอง 1 ครั้งจองได้สูงสุดกี่ sessions
คำตอบ(จากAI) : คำตอบ: การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_booking_max_sessions / curated_reservation_max_sessions)
เฉลย : ต้องมีคำสำคัญ: สูงสุด 3 Sessions | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_booking_max_sessions

26.คำถาม : หลังจองต้องชำระเงินภายในกี่นาที
คำตอบ(จากAI) : คำตอบ: - ผู้ใช้งานต้องชำระค่าบริการหลังจากจองเสร็จเรียบร้อยทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_payment_10_minutes)
เฉลย : ต้องมีคำสำคัญ: 10 นาที | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.039 | retrieved_ids: curated_payment_10_minutes, curated_reservation_advance_time, curated_time_change_policy, curated_booking_no_edit

27.คำถาม : ถ้าไม่ชำระเงินภายในเวลาที่กำหนดจะเกิดอะไรขึ้น
คำตอบ(จากAI) : คำตอบ: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)
เฉลย : ต้องมีคำสำคัญ: การจองจะถูกยกเลิก | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_payment_10_minutes

28.คำถาม : เมื่อกดจองแล้วแก้ไขข้อมูลได้ไหม
คำตอบ(จากAI) : คำตอบ: - เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking_no_edit)
เฉลย : ต้องมีคำสำคัญ: ไม่สามารถแก้ไขข้อมูลได้, ยกเลิกการจอง | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.033 | retrieved_ids: curated_booking_no_edit, curated_booking_steps, curated_time_change_policy, curated_reservation_advance_time

29.คำถาม : ถ้าต้องการแก้ไขการจองต้องทำยังไง
คำตอบ(จากAI) : คำตอบ: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_edit_booking / curated_booking_no_edit)
เฉลย : ต้องมีคำสำคัญ: ยกเลิกการจองผ่านทางอีเมล, อย่างน้อย 1 ชั่วโมง, จองใหม่ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_edit_booking

30.คำถาม : โอนสิทธิ์การจองให้คนอื่นได้ไหม
คำตอบ(จากAI) : คำตอบ: - ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking_non_transferable)
เฉลย : ต้องมีคำสำคัญ: ไม่สามารถโอนสิทธิ์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.035 | retrieved_ids: curated_booking_non_transferable, curated_booking_no_edit, curated_booking_steps, curated_reservation_advance_time

31.คำถาม : การจองอาจถูกยกเลิกโดยไม่แจ้งล่วงหน้าในกรณีใด
คำตอบ(จากAI) : คำตอบ: การจองอาจถูกยกเลิกโดยไม่ต้องแจ้งให้ทราบล่วงหน้า หากข้อมูลไม่ถูกต้องหรือไม่ปฏิบัติตามกฎ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_booking_cancel_invalid_info / Reservation, curated_reservation_cancel_invalid_info, reservation-booking-rules)
เฉลย : ต้องมีคำสำคัญ: ข้อมูลไม่ถูกต้อง, ไม่ปฏิบัติตามกฎ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_booking_cancel_invalid_info

32.คำถาม : เช็คอินล่วงหน้าได้สูงสุดกี่นาที
คำตอบ(จากAI) : คำตอบ: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)
เฉลย : ต้องมีคำสำคัญ: ล่วงหน้าสูงสุด 30 นาที | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_checkin_advance

33.คำถาม : ต้องเช็คอินก่อนเวลาเริ่มรอบไหม
คำตอบ(จากAI) : คำตอบ: - ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_checkin_30_minutes)
เฉลย : ต้องมีคำสำคัญ: ต้องเช็คอินก่อน, เวลาเริ่มต้น | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.03 | retrieved_ids: curated_checkin_30_minutes, curated_checkin_late_cancel, curated_reservation_advance_time, curated_time_change_policy

34.คำถาม : ถ้าไม่เช็คอินก่อนเวลาเริ่มรอบจะเกิดอะไรขึ้น
คำตอบ(จากAI) : คำตอบ: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_checkin_late / curated_checkin_late_cancel)
เฉลย : ต้องมีคำสำคัญ: ระบบจะยกเลิกการจองทันที, ไม่มีการคืนเงิน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_checkin_late

35.คำถาม : ตอนเช็คอินต้องแสดงบัตรอะไร
คำตอบ(จากAI) : คำตอบ: - เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_checkin_id_required)
เฉลย : ต้องมีคำสำคัญ: บัตรประจำตัวนักศึกษา, บัตรประจำตัวบุคลากร, บัตรประชาชน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.036 | retrieved_ids: curated_checkin_id_required, curated_checkin_30_minutes, curated_checkin_late_cancel, curated_reservation_advance_time

36.คำถาม : การยกเลิกการจองต้องทำล่วงหน้ากี่ชั่วโมง
คำตอบ(จากAI) : คำตอบ: การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_cancel_advance / curated_cancel_1_hour)
เฉลย : ต้องมีคำสำคัญ: อย่างน้อย 1 ชั่วโมง | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_cancel_advance

37.คำถาม : มีการคืนเงินไหมถ้ายกเลิกการจอง
คำตอบ(จากAI) : คำตอบ: โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_refund_policy / curated_refund_policy)
เฉลย : ต้องมีคำสำคัญ: ไม่มีการคืนเงิน, ยกเว้น, ศูนย์เป็นฝ่ายผิดพลาด | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_refund_policy

38.คำถาม : กรณีไหนถึงจะมีข้อยกเว้นเรื่องคืนเงิน
คำตอบ(จากAI) : คำตอบ: โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_refund_policy / curated_refund_policy)
เฉลย : ต้องมีคำสำคัญ: อุปกรณ์ขัดข้อง, เหตุสุดวิสัย, ศูนย์ต้องปิดให้บริการ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_refund_policy

39.คำถาม : เปลี่ยนเวลาใช้งานได้ไหม
คำตอบ(จากAI) : คำตอบ: สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา
เฉลย : ต้องมีคำสำคัญ: สามารถเปลี่ยนแปลงเวลา, แจ้งล่วงหน้า, อย่างน้อย 1 ชั่วโมง | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_llm | latency_sec: 4.014 | retrieved_ids: curated_time_change_policy, curated_booking_no_edit, curated_reservation_advance_time, reservation-cancel-change-001

40.คำถาม : ชำระเงินจองผ่านอะไร
คำตอบ(จากAI) : คำตอบ: - ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_booking_steps)
เฉลย : ต้องมีคำสำคัญ: โอนเข้าบัญชีธนาคาร, แนบสลิป | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.047 | retrieved_ids: curated_booking_steps, curated_payment_10_minutes, curated_booking_no_edit, curated_reservation_advance_time

41.คำถาม : บัญชีธนาคารสำหรับชำระเงินชื่อบัญชีอะไร
คำตอบ(จากAI) : คำตอบ: ชำระเงินผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)
เฉลย : ต้องมีคำสำคัญ: PSU Esports Studio - Phuket | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_payment_bank

42.คำถาม : เลขบัญชีธนาคารสำหรับจ่ายค่าจองคืออะไร
คำตอบ(จากAI) : คำตอบ: ชำระเงินผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)
เฉลย : ต้องมีคำสำคัญ: 795-276244-1 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_payment_bank

43.คำถาม : ธนาคารที่ใช้รับชำระเงินคือธนาคารอะไร
คำตอบ(จากAI) : คำตอบ: ชำระเงินผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_payment_bank / Reservation, curated_payment_bank)
เฉลย : ต้องมีคำสำคัญ: Siam Commercial Bank, ธนาคารไทยพาณิชย์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_payment_bank

44.คำถาม : ขั้นตอนจองใช้งานศูนย์มีอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_booking_steps / curated_booking_steps)
เฉลย : ต้องมีคำสำคัญ: เลือกบริการ, เลือกวันและเวลา, กรอกข้อมูล, ชำระเงิน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_booking_steps

45.คำถาม : ตอนกรอกข้อมูลจองต้องกรอกอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_user_info_required)
เฉลย : ต้องมีคำสำคัญ: Student ID, Staff ID, National ID, ชื่อ, อีเมล, เบอร์โทรศัพท์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.036 | retrieved_ids: curated_user_info_required, curated_booking_steps, curated_booking_no_edit, curated_reservation_advance_time

46.คำถาม : ช่วงเช้าของตารางให้บริการคือเวลาอะไร
คำตอบ(จากAI) : คำตอบ: ช่วงเช้าของตารางให้บริการเริ่มตั้งแต่เวลา 09:00 และสิ้นสุดที่ 12:00
เฉลย : ต้องมีคำสำคัญ: 09:00, 12:00 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_llm | latency_sec: 3.549 | retrieved_ids: curated_schedule_morning, curated_reservation_schedule_monday_morning, curated_time_change_policy, curated_schedule_afternoon

47.คำถาม : ช่วงบ่ายของตารางให้บริการคือเวลาอะไร
คำตอบ(จากAI) : คำตอบ: ช่วงเวลาบ่ายของตารางให้บริการเปิดทำการในช่วง 13:00 – 16:00
เฉลย : ต้องมีคำสำคัญ: 13:00, 16:00 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_llm | latency_sec: 3.364 | retrieved_ids: curated_reservation_schedule_monday_morning, curated_schedule_morning, curated_schedule_afternoon, curated_booking_steps

48.คำถาม : วันจันทร์ช่วงเช้าเปิดให้บริการไหม
คำตอบ(จากAI) : คำตอบ: วัน Monday ช่วง Morning 09:00–12:00 เป็น Maintenance* ไม่ใช่ช่วง Open for Service แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_schedule_monday_morning / Reservation, curated_reservation_schedule_monday_morning, reservation-intro-schedule)
เฉลย : ต้องมีคำสำคัญ: Monday, Maintenance | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_schedule_monday_morning

49.คำถาม : วันศุกร์มี maintenance แบบไหน
คำตอบ(จากAI) : คำตอบ: วันศุกร์มี Maintenance** ซึ่งหมายถึง Weekly hardware inspection and cleaning แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_schedule_friday_maintenance / Reservation, curated_reservation_schedule_friday_maintenance, reservation-intro-schedule)
เฉลย : ต้องมีคำสำคัญ: Maintenance, Weekly hardware inspection, cleaning | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_schedule_friday_maintenance

50.คำถาม : ศูนย์ให้รับประทานอาหารและเครื่องดื่มตรงไหน
คำตอบ(จากAI) : คำตอบ: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_food_drink / curated_rule_food_drinks)
เฉลย : ต้องมีคำสำคัญ: เฉพาะในพื้นที่ที่กำหนด | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_food_drink

51.คำถาม : ต้องฝากสัมภาระก่อนเข้าใช้บริการไหม
คำตอบ(จากAI) : คำตอบ: - กรุณาฝากสัมภาระก่อนเข้าใช้บริการ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_belongings)
เฉลย : ต้องมีคำสำคัญ: ฝากสัมภาระก่อนเข้าใช้บริการ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.061 | retrieved_ids: curated_rule_belongings, curated_rule_report_problem, curated_rule_lost_items, reservation-studio-rules-001

52.คำถาม : ยืมอุปกรณ์หรือแผ่นเกมแล้วต้องทำอะไรหลังใช้งาน
คำตอบ(จากAI) : คำตอบ: กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_return_equipment_games / Reservation, curated_rule_return_equipment, reservation-studio-rules)
เฉลย : ต้องมีคำสำคัญ: นำอุปกรณ์, แผ่นเกม, มาคืน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_return_equipment_games

53.คำถาม : ศูนย์ห้ามทิ้งขยะหรือสิ่งของไว้ตรงไหน
คำตอบ(จากAI) : คำตอบ: - ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_trash_personal_items)
เฉลย : ต้องมีคำสำคัญ: ห้ามทิ้งขยะ, บริเวณที่ไม่ได้กำหนด | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.039 | retrieved_ids: curated_rule_trash_personal_items, curated_rule_smoking_alcohol_drugs, curated_rule_move_equipment, curated_rule_lost_items

54.คำถาม : ศูนย์มีกฎเรื่องเสียงดังหรือคำพูดไม่เหมาะสมไหม
คำตอบ(จากAI) : คำตอบ: - กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_noise_language)
เฉลย : ต้องมีคำสำคัญ: งดส่งเสียงดัง, ห้ามพูดจาดูหมิ่น | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.039 | retrieved_ids: curated_rule_noise_language, curated_rule_report_problem, curated_rule_smoking_alcohol_drugs, reservation-studio-rules-002

55.คำถาม : ทำอุปกรณ์เสียหายต้องรับผิดชอบไหม
คำตอบ(จากAI) : คำตอบ: ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_damage_responsibility / Reservation, curated_damage_minor, curated_damage_moderate, curated_damage_severe)
เฉลย : ต้องมีคำสำคัญ: รับผิดชอบ, ค่าปรับ, ค่าชดเชย | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_damage_responsibility

56.คำถาม : ความเสียหายเล็กน้อยมีค่าปรับเท่าไหร่
คำตอบ(จากAI) : คำตอบ: ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_damage_responsibility / Reservation, curated_damage_minor, curated_damage_moderate, curated_damage_severe)
เฉลย : ต้องมีคำสำคัญ: 100, 500 บาท | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_damage_responsibility

57.คำถาม : ความเสียหายปานกลางมีค่าซ่อมหรือค่าปรับเท่าไหร่
คำตอบ(จากAI) : คำตอบ: ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_damage_responsibility / Reservation, curated_damage_minor, curated_damage_moderate, curated_damage_severe)
เฉลย : ต้องมีคำสำคัญ: 500, 2,000 บาท | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_damage_responsibility

58.คำถาม : ถ้าทำจอแตกหรือคอมพิวเตอร์พังต้องชดเชยยังไง
คำตอบ(จากAI) : คำตอบ: ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_severe_damage / curated_damage_severe)
เฉลย : ต้องมีคำสำคัญ: ชดเชยราคาทรัพย์สินเต็มจำนวน, ราคากลาง | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_severe_damage

59.คำถาม : ย้ายอุปกรณ์เองได้ไหม
คำตอบ(จากAI) : คำตอบ: - ห้ามเคลื่อนย้ายอุปกรณ์หรือสิ่งของใด ๆ โดยไม่ได้รับอนุญาต แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_move_equipment)
เฉลย : ต้องมีคำสำคัญ: ห้ามเคลื่อนย้าย, ไม่ได้รับอนุญาต | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.038 | retrieved_ids: curated_rule_move_equipment, curated_rule_return_equipment, curated_rule_lost_items, curated_rule_power_outlet

60.คำถาม : นำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัวมาใช้ปลั๊กไฟได้ไหม
คำตอบ(จากAI) : คำตอบ: - ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัวมาใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_rule_power_outlet)
เฉลย : ต้องมีคำสำคัญ: ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัว, ไม่ได้รับอนุญาต | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.033 | retrieved_ids: curated_rule_power_outlet, curated_rule_move_equipment, curated_rule_return_equipment, curated_rule_lost_items

61.คำถาม : ศูนย์ห้ามสูบบุหรี่ไหม
คำตอบ(จากAI) : คำตอบ: ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)
เฉลย : ต้องมีคำสำคัญ: ห้ามสูบบุหรี่ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_smoking_alcohol

62.คำถาม : ศูนย์ห้ามดื่มแอลกอฮอล์ไหม
คำตอบ(จากAI) : คำตอบ: ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)
เฉลย : ต้องมีคำสำคัญ: ห้าม, เครื่องดื่มแอลกอฮอล์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_smoking_alcohol

63.คำถาม : ห้ามนำอาวุธหรือของมีคมเข้าศูนย์ไหม
คำตอบ(จากAI) : คำตอบ: ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_weapons_gambling / curated_rule_weapons_gambling)
เฉลย : ต้องมีคำสำคัญ: ห้ามพกอาวุธ, ของมีคม | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_weapons_gambling

64.คำถาม : ห้ามเล่นการพนันในศูนย์ไหม
คำตอบ(จากAI) : คำตอบ: ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_weapons_gambling / curated_rule_weapons_gambling)
เฉลย : ต้องมีคำสำคัญ: ห้ามเล่นการพนัน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_weapons_gambling

65.คำถาม : ถ้าทรัพย์สินส่วนตัวสูญหาย ศูนย์รับผิดชอบไหม
คำตอบ(จากAI) : คำตอบ: กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_lost_personal_items / Reservation, curated_rule_lost_items, reservation-studio-rules)
เฉลย : ต้องมีคำสำคัญ: สงวนสิทธิ์ไม่รับผิดชอบ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_lost_personal_items

66.คำถาม : ถ้าพบปัญหาการใช้งานควรทำอย่างไร
คำตอบ(จากAI) : คำตอบ: หากพบปัญหาการใช้งาน โปรดแจ้งเจ้าหน้าที่ทันที โดยตรงตามข้อกำหนดใน "Reservation Rules" ซึ่งระบุว่าหากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ โปรดแจ้งเจ้าหน้าที่ทันที (พบปัญหาให้แจ้งเจ้าหน้าที่)
เฉลย : ต้องมีคำสำคัญ: แจ้งเจ้าหน้าที่ทันที | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_llm | latency_sec: 4.424 | retrieved_ids: curated_rule_report_problem, curated_reservation_advance_time, curated_penalty_warning_suspension, reservation-studio-rules-001

67.คำถาม : ถ้าละเมิดกฎจะโดนอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_penalty_warning_suspension)
เฉลย : ต้องมีคำสำคัญ: คำเตือน, ระงับสิทธิ์, ชั่วคราว, ถาวร | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.127 | retrieved_ids: curated_penalty_warning_suspension, curated_penalty_violation_record, curated_penalty_temp_suspension, curated_penalty_permanent_suspension

68.คำถาม : การระงับสิทธิ์ชั่วคราวมีกี่วัน
คำตอบ(จากAI) : คำตอบ: - หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_penalty_temp_suspension)
เฉลย : ต้องมีคำสำคัญ: 1-7 วัน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.056 | retrieved_ids: curated_penalty_temp_suspension, curated_penalty_permanent_suspension, curated_penalty_booking_suspension, curated_penalty_warning_suspension

69.คำถาม : กรณีไหนอาจถูกระงับสิทธิ์ถาวร
คำตอบ(จากAI) : คำตอบ: - ในกรณีที่ผู้ใช้งานกระทำการละเมิดกฎอย่างร้ายแรง หรือมีการละเมิดซ้ำหลายครั้ง เช่น การทำลายทรัพย์สินหรือพฤติกรรมที่เป็นภัยต่อความปลอดภัยของผู้อื่น ผู้ใช้งานอาจถูกระงับสิทธิ์การใช้งานถาวร แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_penalty_permanent_suspension)
เฉลย : ต้องมีคำสำคัญ: ละเมิดกฎอย่างร้ายแรง, ละเมิดซ้ำ, ทำลายทรัพย์สิน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.076 | retrieved_ids: curated_penalty_permanent_suspension, curated_penalty_temp_suspension, curated_penalty_warning_suspension, curated_penalty_booking_suspension

70.คำถาม : ถ้าไม่พอใจการลงโทษสามารถอุทธรณ์ได้ภายในกี่วัน
คำตอบ(จากAI) : คำตอบ: - หากผู้ใช้งานไม่พอใจการตัดสินใจเกี่ยวกับการลงโทษ สามารถยื่นคำร้องขอการพิจารณาใหม่ได้ภายใน 7 วันหลังจากการถูกลงโทษ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_penalty_appeal)
เฉลย : ต้องมีคำสำคัญ: ยื่นคำร้อง, 7 วัน | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.051 | retrieved_ids: curated_penalty_appeal, curated_penalty_temp_suspension, curated_penalty_warning_suspension, curated_penalty_booking_suspension

71.คำถาม : ศูนย์บันทึกประวัติการละเมิดกฎไหม
คำตอบ(จากAI) : คำตอบ: - การละเมิดกฎจะถูกบันทึกในประวัติการใช้บริการของผู้ใช้งาน และอาจส่งผลต่อสิทธิ์ในการใช้บริการในอนาคต หากการละเมิดเป็นกรณีร้ายแรง ศูนย์อาจไม่ให้สิทธิ์ในการใช้บริการอีกต่อไป แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (curated_penalty_violation_record)
เฉลย : ต้องมีคำสำคัญ: บันทึกในประวัติการใช้บริการ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.041 | retrieved_ids: curated_penalty_violation_record, curated_penalty_booking_suspension, curated_penalty_temp_suspension, curated_penalty_warning_suspension

72.คำถาม : ศูนย์ตั้งอยู่ที่ไหน
คำตอบ(จากAI) : คำตอบ: PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_location / curated_contact_location)
เฉลย : ต้องมีคำสำคัญ: มหาวิทยาลัยสงขลานครินทร์, วิทยาเขตภูเก็ต, 80 หมู่ 1 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Contact
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_contact_location

73.คำถาม : อีเมลติดต่อศูนย์คืออะไร
คำตอบ(จากAI) : คำตอบ: อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_email / curated_contact_email)
เฉลย : ต้องมีคำสำคัญ: psuesportspkt, gmail.com | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Contact
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_contact_email

74.คำถาม : Facebook ของศูนย์คืออะไร
คำตอบ(จากAI) : คำตอบ: Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_facebook / curated_contact_facebook)
เฉลย : ต้องมีคำสำคัญ: facebook.com/psuesportsphuket | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Contact
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_contact_facebook

75.คำถาม : เบอร์ติดต่อจากระบบจองมีเบอร์อะไรบ้าง
คำตอบ(จากAI) : คำตอบ: เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045 แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_contact_phone / curated_contact_phone)
เฉลย : ต้องมีคำสำคัญ: 7627 6004, 7627 6045 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_contact_phone

76.คำถาม : Esports คืออะไร
คำตอบ(จากAI) : คำตอบ: - อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_definition)
เฉลย : ต้องมีคำสำคัญ: กีฬาอิเล็กทรอนิกส์, การแข่งขัน, วิดีโอเกม | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.031 | retrieved_ids: curated_knowledge_esports_definition, knowledge-esports-คืออะไร-14-001, knowledge-knowledge-01-001, curated_knowledge_esports_origin

77.คำถาม : อีสปอร์ตเกิดขึ้นครั้งแรกเมื่อไหร่และที่ไหน
คำตอบ(จากAI) : คำตอบ: - อีสปอร์ตเกิดขึ้นครั้งแรกในวันที่ 19 ตุลาคม ค.ศ. 1972 ณ มหาวิทยาลัยสแตนฟอร์ด (Standford University) จากการแข่งขันเกม Spacewar ภายใต้ชื่องาน Intergalactic Spacewar Olympics แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_origin)
เฉลย : ต้องมีคำสำคัญ: 19 ตุลาคม, 1972, มหาวิทยาลัยสแตนฟอร์ด, Spacewar | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.035 | retrieved_ids: curated_knowledge_esports_origin, curated_knowledge_esports_definition, knowledge-ประวัติของ-esports-13-001, knowledge-knowledge-01-001

78.คำถาม : ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ตมีอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS) - อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_categories) - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_definition)
เฉลย : ต้องมีคำสำคัญ: MOBA, FPS, Battle Royale, Fighting Games | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.039 | retrieved_ids: curated_knowledge_esports_categories, curated_knowledge_esports_definition, knowledge-ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต-12-001, knowledge-knowledge-01-001

79.คำถาม : ตัวอย่างเกมที่นิยมในปัจจุบันมีอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_current_popular_games)
เฉลย : ต้องมีคำสำคัญ: VALORANT, Mobile Legends, Tekken, Mario Kart | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.036 | retrieved_ids: curated_knowledge_current_popular_games, knowledge-เกมที่นิยมในปัจจุบัน-11-001, knowledge-ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต-12-001, knowledge-ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต-12-003

80.คำถาม : อาชีพที่เกี่ยวข้องกับกีฬาอีสปอร์ตมีอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - อาชีพที่เกี่ยวข้องกับกีฬาอีสปอร์ต ได้แก่ นักกีฬาอีสปอร์ต, โค้ชอีสปอร์ต, ผู้จัดการทีมอีสปอร์ต, นักพากย์การแข่งขันอีสปอร์ต, ผู้จัดการแข่งขันอีสปอร์ต, นักวิเคราะห์อีสปอร์ต, นักเขียนข่าวอีสปอร์ต, นักจิตวิทยาอีสปอร์ต, นักโภชนาการอีสปอร์ต และนักกายภาพบำบัดอีสปอร์ต - อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_careers) - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_esports_definition)
เฉลย : ต้องมีคำสำคัญ: นักกีฬาอีสปอร์ต, โค้ชอีสปอร์ต, นักพากย์, นักวิเคราะห์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.04 | retrieved_ids: curated_knowledge_esports_careers, curated_knowledge_esports_definition, knowledge-อาชีพที่เกี่ยวข้องกับกีฬาอีสปอร์ต-10-001, knowledge-knowledge-01-002

81.คำถาม : Overcooked! 2 ช่วยพัฒนาทักษะอะไรตามบทความ
คำตอบ(จากAI) : คำตอบ: - บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_overcooked2_skills)
เฉลย : ต้องมีคำสำคัญ: ทักษะชีวิต, ความสนุก | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.038 | retrieved_ids: curated_knowledge_overcooked2_skills, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-001, knowledge-overcooked-2-เกมสุดมันส์ที่ได้มากกว่าความสนุก-09-002, knowledge-knowledge-01-002

82.คำถาม : Mario Kart 8 Deluxe ช่วยฝึกอะไรตามบทความ
คำตอบ(จากAI) : Mario Kart 8 Deluxe ช่วยฝึกทักษะการประเมินสถานการณ์แบบเรียลไทม์ การตัดสินใจ และไหวพริบ ในโหมด Multiplayer และ Local Co-op. มันยังช่วยพัฒนาทักษะในการควบคุมตัวละคร, การแข่งขันอย่างสร้างสรรค์, การยอมรับผลแพ้-ชนะ และการควบคุมอารมณ์เมื่อสถานการณ์ไม่เป็นใจ รวมถึงทักษะการแก
เฉลย : ต้องมีคำสำคัญ: ไหวพริบ, การตัดสินใจ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_llm | latency_sec: 4.829 | retrieved_ids: knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-002, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-001, knowledge-mario-kart-8-deluxe-เกมแข่งรถที่ฝึกไหวพริบและการตัดสินใจ-08-003, knowledge-knowledge-01-002

83.คำถาม : NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ในบทความเกี่ยวกับอะไร
คำตอบ(จากAI) : คำตอบ: - บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/Knowledge (curated_knowledge_naruto_connections_summary)
เฉลย : ต้องมีคำสำคัญ: บริหารจักระ, การตัดสินใจ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Knowledge
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.047 | retrieved_ids: curated_knowledge_naruto_connections_summary, knowledge-naruto-x-boruto-ultimate-ninja-storm-connections-ศิลปะการบริหารจักระ-02-007, knowledge-naruto-x-boruto-ultimate-ninja-storm-connections-ศิลปะการบริหารจักระ-02-001, knowledge-naruto-x-boruto-ultimate-ninja-storm-connections-ศิลปะการบริหารจักระ-02-002

84.คำถาม : วันที่ 25 เมษายน 2569 ศูนย์จัดการแข่งขันเกมอะไร
คำตอบ(จากAI) : คำตอบ: - เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2 แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/events-news/news (curated_news_cs2_2026)
เฉลย : ต้องมีคำสำคัญ: Counter-Strike 2, PSU Phuket CS 2 2026 Tournament | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: News
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.057 | retrieved_ids: curated_news_cs2_2026, events-news-article-002-001, events-news-article-006-001, events-news-article-005-001

85.คำถาม : PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อไหร่
คำตอบ(จากAI) : คำตอบ: - PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/events-news/news (curated_news_valorant_2026)
เฉลย : ต้องมีคำสำคัญ: 21 กุมภาพันธ์ 2569, VALORANT | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: News
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.045 | retrieved_ids: curated_news_valorant_2026, curated_news_cs2_2026, events-news-article-006-001, events-news-article-002-001

86.คำถาม : ศูนย์ส่งตัวแทนเข้าร่วม SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT กี่คน
คำตอบ(จากAI) : คำตอบ: - ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3 แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/events-news/news (curated_news_surat_smash_tekken8)
เฉลย : ต้องมีคำสำคัญ: 4 คน, Tekken 8 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: News
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.043 | retrieved_ids: curated_news_surat_smash_tekken8, events-news-article-004-001, events-news-page-05-001, events-news-article-023-001

87.คำถาม : นักศึกษาชาวจีนที่เข้าร่วมกิจกรรมมีจำนวนกี่คน
คำตอบ(จากAI) : คำตอบ: - เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/events-news/news (curated_news_chinese_students_game_based_learning)
เฉลย : ต้องมีคำสำคัญ: 11 คน, Game-based Learning | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: News
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.036 | retrieved_ids: curated_news_chinese_students_game_based_learning, events-news-article-005-001, events-news-article-064-001, events-news-article-031-001

88.คำถาม : กิจกรรม GAME ON เปิดโลกอีสปอร์ตเกี่ยวกับใคร
คำตอบ(จากAI) : คำตอบ: - กิจกรรม GAME ON! เปิดโลกอีสปอร์ต จัดสำหรับนักเรียนชั้นมัธยมศึกษาปีที่ 3 (ม.3) จากโรงเรียนท้ายเหมืองวิทยา จำนวน 21 คน แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/events-news/news (curated_news_game_on_thaimuang)
เฉลย : ต้องมีคำสำคัญ: ม.3, โรงเรียนท้ายเหมืองวิทยา | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: News
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.058 | retrieved_ids: curated_news_game_on_thaimuang, events-news-article-007-001, events-news-page-05-001, events-news-page-03-001

89.คำถาม : ใครเป็นอธิการบดีที่ปรากฏในหน้าสมาชิก
คำตอบ(จากAI) : คำตอบ: - หน้าสมาชิกระบุว่า ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_president)
เฉลย : ต้องมีคำสำคัญ: ผศ.ดร.นิวัติ แก้วประดับ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Members
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.042 | retrieved_ids: curated_about_members_president, curated_about_members_dean, curated_about_members_club_president, curated_about_members_manager

90.คำถาม : ใครเป็นคณบดีวิทยาลัยการคอมพิวเตอร์ที่ปรากฏในหน้าสมาชิก
คำตอบ(จากAI) : คำตอบ: - หน้าสมาชิกระบุว่า รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์ แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_dean)
เฉลย : ต้องมีคำสำคัญ: รศ.ดร.อซีส นันทอมรพงศ์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Members
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.032 | retrieved_ids: curated_about_members_dean, curated_about_members_president, curated_about_members_manager, curated_about_members_club_president

91.คำถาม : ผู้จัดการ PSU Esports Studio - Phuket คือใคร
คำตอบ(จากAI) : คำตอบ: - หน้าสมาชิกระบุว่า นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_manager)
เฉลย : ต้องมีคำสำคัญ: นายชนะชัย สิริพันธ์วราภรณ์ | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Members
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.032 | retrieved_ids: curated_about_members_manager, curated_about_members_club_president, about-members-club-001, about-members-leadership-001

92.คำถาม : PSU Phuket Esports Club มีใครเป็นประธาน
คำตอบ(จากAI) : คำตอบ: - หน้าสมาชิกระบุว่า นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Members (curated_about_members_club_president)
เฉลย : ต้องมีคำสำคัญ: นายษุภากรณ์ จิราจินดากุล | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Members
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.037 | retrieved_ids: curated_about_members_club_president, curated_about_members_manager, about-members-club-001, about-members-leadership-001

93.คำถาม : หน้า Gallery มีหมวดภาพอะไรบ้าง
คำตอบ(จากAI) : คำตอบ: - หน้า Gallery มีหมวดภาพ Nintendo Switch และ PlayStation 5 แหล่งข้อมูล: - https://esports.phuket.psu.ac.th/about-us/Gallery (curated_about_gallery_categories)
เฉลย : ต้องมีคำสำคัญ: Nintendo Switch, PlayStation 5 | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Gallery
ผลตรวจ : PASS | mode: rag_direct_curated | latency_sec: 0.033 | retrieved_ids: curated_about_gallery_categories, curated_about_members_manager, curated_about_members_dean, about-us-gallery-02-001

94.คำถาม : What is PSU Esports Studio Phuket?
คำตอบ(จากAI) : Answer: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Sources: - https://esports.phuket.psu.ac.th/home (rule_overview_identity / curated_overview_identity)
เฉลย : ต้องมีคำสำคัญ: esports, Prince of Songkla University, College of Computing | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: home
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_overview_identity

95.คำถาม : How many sessions can one booking include?
คำตอบ(จากAI) : Answer: One booking can include a maximum of 3 sessions. Sources: - https://esports.computing.psu.ac.th/ (rule_booking_max_sessions / curated_reservation_max_sessions)
เฉลย : ต้องมีคำสำคัญ: maximum of 3 sessions | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_booking_max_sessions

96.คำถาม : How early can users check in before their reserved time?
คำตอบ(จากAI) : Answer: Check-in is available up to 30 minutes before the reserved time slot, and users must check in before the slot begins. Sources: - https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_minutes)
เฉลย : ต้องมีคำสำคัญ: 30 minutes | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_checkin_advance

97.คำถาม : What happens if payment is not made within 10 minutes?
คำตอบ(จากAI) : Answer: Payment must be made immediately after booking. If payment is not made within 10 minutes, the booking will be automatically cancelled. Sources: - https://esports.computing.psu.ac.th/ (rule_payment_10_minutes / Reservation, curated_payment_10_minutes)
เฉลย : ต้องมีคำสำคัญ: automatically cancelled | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_payment_10_minutes

98.คำถาม : Are smoking and alcohol allowed inside the studio?
คำตอบ(จากAI) : Answer: Smoking, drug use, and alcohol consumption are strictly prohibited inside the studio. Sources: - https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / Reservation, curated_rule_smoking_alcohol_drugs)
เฉลย : ต้องมีคำสำคัญ: strictly prohibited, alcohol | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Reservation
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_smoking_alcohol

99.คำถาม : What is the email address of PSU Esports Studio Phuket?
คำตอบ(จากAI) : Answer: The contact email is psuesportspkt@gmail.com. Sources: - https://esports.phuket.psu.ac.th/Contact-Us (rule_contact_email / curated_contact_email)
เฉลย : ต้องมีคำสำคัญ: psuesportspkt@gmail.com | แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: Contact
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_contact_email

100.คำถาม : ศูนย์มีบริการซ่อมคอมพิวเตอร์ส่วนตัวไหม
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลเรื่องบริการซ่อมคอมพิวเตอร์ส่วนตัวในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_repair_personal_pc)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_no_answer_repair_personal_pc

101.คำถาม : ศูนย์เปิดให้บริการ 24 ชั่วโมงไหม
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลว่าเปิดให้บริการ 24 ชั่วโมงในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_24_hours)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_no_answer_24_hours

102.คำถาม : มีบริการจัดส่งอาหารถึงโต๊ะเล่นเกมไหม
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลเรื่องบริการจัดส่งอาหารถึงโต๊ะเล่นเกมในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_food_delivery)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_no_answer_food_delivery

103.คำถาม : สามารถนำสัตว์เลี้ยงเข้าศูนย์ได้ไหม
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลเรื่องการนำสัตว์เลี้ยงเข้าศูนย์ในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_pets)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.0 | retrieved_ids: rule_no_answer_pets

104.คำถาม : สมัครสมาชิกศูนย์รายปีราคาเท่าไหร่
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_annual_membership)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_no_answer_annual_membership

105.คำถาม : ศูนย์มีบริการเช่าโน้ตบุ๊กกลับบ้านไหม
คำตอบ(จากAI) : คำตอบ: ไม่พบข้อมูลเรื่องบริการเช่าโน้ตบุ๊กกลับบ้านในฐานข้อมูลที่มี แหล่งข้อมูล: - missing source URL (rule_no_answer_laptop_rental_home)
เฉลย : ต้องมีคำสำคัญ: ไม่พบข้อมูล
ผลตรวจ : PASS | mode: rule_fast_path | latency_sec: 0.001 | retrieved_ids: rule_no_answer_laptop_rental_home
