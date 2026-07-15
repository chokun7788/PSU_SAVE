# User Question Bank Evaluation

- Generated at: 2026-07-15T21:38:06
- Total questions: 100
- Total wall time: 50.14s

## Summary By Strategy
- fastpath/rulebase: 19
- pipeline: 80
- rag/vector: 1

## Results

### GR-001 game_rules ข้อ 1
- Question: ROV คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.6271s | Wall: 0.6577s
- Sources: competition_rules: data/competition_rules
- Answer: RoV / Arena of Valor: RoV หรือ Arena of Valor คือเกม MOBA บนมือถือที่ผู้เล่นแบ่งเป็นทีม เลือกฮีโร่ และร่วมกันทำลายป้อม/ฐานของฝ่ายตรงข้าม แนวเกม: เกม MOBA แบบทีม วิธีเล่นโดยสรุป: โดยทั่วไปผู้เล่นต้องเลือกตำแหน่งและฮีโร่ให้เหมาะกับทีม เก็บเลเวล คุมแผนที่ ช่วยทีม...

### GR-002 game_rules ข้อ 2
- Question: ROV เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:related_guidance_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `fastpath/rulebase`
- Latency: 0.1796s | Wall: 0.1796s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: สรุปแนวเกมที่มีข้อมูลยืนยันได้: - FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone - MOBA: League of Legends - Fighting: TEKKEN 8 - Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone - VR/Rhythm: Beat Saber ใน VR Zone - Party/เล่นกับเพื่อน: Mario K...

### GR-003 game_rules ข้อ 3
- Question: ROV มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.8668s | Wall: 0.8669s
- Sources: rov_team_size_active_players: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้  หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเ...

### GR-004 game_rules ข้อ 4
- Question: ROV แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2039s | Wall: 0.2039s
- Sources: rov_team_size_active_players: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้  หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเ...

### GR-005 game_rules ข้อ 5
- Question: ROV มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.1924s | Wall: 0.1924s
- Sources: rov_team_size_active_players: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้  หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเ...

### GR-006 game_rules ข้อ 6
- Question: ROV ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3299s | Wall: 0.33s
- Sources: rov_late_start_forfeit: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น  หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: lo...

### GR-007 game_rules ข้อ 7
- Question: ROV ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5421s | Wall: 0.5421s
- Sources: rov_pause_disconnect: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ  หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง  อ้างอิงจากกติกา: Arena of V...

### GR-008 game_rules ข้อ 8
- Question: ROV ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3496s | Wall: 0.3497s
- Sources: rov_pause_disconnect: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ  หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง  อ้างอิงจากกติกา: Arena of V...

### GR-009 game_rules ข้อ 9
- Question: ROV มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6027s | Wall: 0.6028s
- Sources: competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที  รายละเอียดที่เกี่ยวข้อง: - 6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที -...

### GR-010 game_rules ข้อ 10
- Question: ROV ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:games_known_unsupported_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2917s | Wall: 0.2917s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบ RoV / Arena of Valor ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ  เกมที่มีข้...

### GR-011 game_rules ข้อ 11
- Question: ROV ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.437s | Wall: 0.437s
- Sources: competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม  รายละเอียดที่เกี่ยวข้อง: - 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมส...

### GR-012 game_rules ข้อ 12
- Question: ROV รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5182s | Wall: 0.5182s
- Sources: rov_format_bo3_all_rounds: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ  หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล...

### GR-013 game_rules ข้อ 13
- Question: ROV รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2114s | Wall: 0.2114s
- Sources: rov_format_bo3_all_rounds: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ  หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล...

### GR-014 game_rules ข้อ 14
- Question: ROV มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5428s | Wall: 0.5429s
- Sources: competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick  รายละเอียดที่เกี่ยวข้อง: - 4.6.3.2. ครั้งที่ 2: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 1 ครั้ง - 4.6.3.3. ครั้งที่ 3: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 2 ครั้ง - 6.1.1.1. บทลงโทษ: ปรับแพ้...

### GR-015 game_rules ข้อ 15
- Question: ROV ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:hybrid_guarded_rerank`
- Route: `games/games_lookup`
- Strategy: `rag/vector`
- Latency: 4.9977s | Wall: 4.9985s
- Sources: our_games_scraped_moving_out_2: https://esports.phuket.psu.ac.th/Services/our-games | game_detail_valorant: https://esports.computing.psu.ac.th/reservation | our_games_scraped_mario_party_superstars: https://esports.phuket.psu.ac.th/Services/our-games | our_games_scraped_super_mario_odyssey: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: Moving Out 2: Moving Out 2 เป็นภาคต่อสุดแหวกแนวของเกมจำลองการเคลื่อนที่ตามหลักฟิสิกส์ที่มีชื่อเสียงระดับโลก ทำงานเป็น F.A.R.T เดี่ยวหรือกับเพื่อนอีกสามคนสวมเครื่องแบบ Smooth Moves ของคุณและช่วยเหลือชาว Packmore และที่อื่น ๆ ให้แพ็คของและส่งออก! อยู่ในรายการเกม...

### GR-016 game_rules ข้อ 16
- Question: ROV เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3249s | Wall: 0.325s
- Sources: competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: - 4.3.4.หากเกิ...

### GR-017 game_rules ข้อ 17
- Question: ROV ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.278s | Wall: 0.278s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใ...

### GR-018 game_rules ข้อ 18
- Question: ROV ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.1732s | Wall: 0.1732s
- Sources: rov_device_mobile_only: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad  หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local...

### GR-019 game_rules ข้อ 19
- Question: ROV ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3917s | Wall: 0.3917s
- Sources: rov_pause_disconnect: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ  หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมหรือขัดข้อง  อ้างอิงจากกติกา: Arena of V...

### GR-020 game_rules ข้อ 20
- Question: ROV ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3327s | Wall: 0.3328s
- Sources: rov_rematch_first_blood: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน  หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้น...

### GR-021 game_rules ข้อ 21
- Question: ROV มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:games_known_unsupported_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.465s | Wall: 0.465s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบ RoV / Arena of Valor ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ  เกมที่มีข้...

### GR-022 game_rules ข้อ 22
- Question: ROV ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5099s | Wall: 0.5099s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที  รายละเอียดที่เกี่ยวข้อง: - 6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบ...

### GR-023 game_rules ข้อ 23
- Question: ROV มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.621s | Wall: 0.621s
- Sources: rov_rematch_first_blood: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน  หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน First Blood และก่อน 2 นาที พร้อมข้อยกเว้น...

### GR-024 game_rules ข้อ 24
- Question: ROV ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5531s | Wall: 0.5532s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใ...

### GR-025 game_rules ข้อ 25
- Question: ROV แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4482s | Wall: 0.4482s
- Sources: rov_team_size_active_players: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้  หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่ได้ระบุจำนวน roster รวม/ตัวสำรองแบบชัดเ...

### GR-026 game_rules ข้อ 26
- Question: VALORANT คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2087s | Wall: 0.2087s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-027 game_rules ข้อ 27
- Question: VALORANT เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:related_guidance_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `fastpath/rulebase`
- Latency: 0.2478s | Wall: 0.2478s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: สรุปแนวเกมที่มีข้อมูลยืนยันได้: - FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone - MOBA: League of Legends - Fighting: TEKKEN 8 - Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone - VR/Rhythm: Beat Saber ใน VR Zone - Party/เล่นกับเพื่อน: Mario K...

### GR-028 game_rules ข้อ 28
- Question: VALORANT มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.9296s | Wall: 0.9296s
- Sources: valorant_team_size_players: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน  หลักฐานจากกติกา: - เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...

### GR-029 game_rules ข้อ 29
- Question: VALORANT แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4002s | Wall: 0.4003s
- Sources: valorant_team_size_players: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน  หลักฐานจากกติกา: - เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...

### GR-030 game_rules ข้อ 30
- Question: VALORANT มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3554s | Wall: 0.3554s
- Sources: valorant_team_size_players: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน  หลักฐานจากกติกา: - เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...

### GR-031 game_rules ข้อ 31
- Question: VALORANT ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.7807s | Wall: 0.7808s
- Sources: competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้  รายละเอียดที่เกี่ยวข้อง: - อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) - อ...

### GR-032 game_rules ข้อ 32
- Question: VALORANT ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6773s | Wall: 0.6773s
- Sources: valorant_emergency_pause: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที  หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026...

### GR-033 game_rules ข้อ 33
- Question: VALORANT ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4318s | Wall: 0.4318s
- Sources: valorant_emergency_pause: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที  หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026...

### GR-034 game_rules ข้อ 34
- Question: VALORANT มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4422s | Wall: 0.4423s
- Sources: competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s10_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: บทลงโทษ  รายละเอียดที่เกี่ยวข้อง: - ประเภทบทลงโทษในเกม - เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) - ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ - การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผล...

### GR-035 game_rules ข้อ 35
- Question: VALORANT ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.3434s | Wall: 0.3434s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น VALORANT ได้ครับ มีให้เล่นที่: PC Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-036 game_rules ข้อ 36
- Question: VALORANT ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4722s | Wall: 0.4722s
- Sources: competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน  รายละเอียดที่เกี่ยวข้อง: - อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ - เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แ...

### GR-037 game_rules ข้อ 37
- Question: VALORANT รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6672s | Wall: 0.6673s
- Sources: competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: กฎระเบียบและรูปแบบการแข่งขัน VALORANT  รายละเอียดที่เกี่ยวข้อง: - ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม - เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้...

### GR-038 game_rules ข้อ 38
- Question: VALORANT รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3436s | Wall: 0.3436s
- Sources: competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน  รายละเอียดที่เกี่ยวข้อง: - รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน - Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความ...

### GR-039 game_rules ข้อ 39
- Question: VALORANT มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6778s | Wall: 0.6778s
- Sources: competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * แบนจนเหลือ 3 แผนที่  รายละเอียดที่เกี่ยวข้อง: - การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 - เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง - แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเ...

### GR-040 game_rules ข้อ 40
- Question: VALORANT ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:games_fast_path`
- Route: `games/games_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.8564s | Wall: 0.8577s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: PC Zone มีเกมที่ยืนยันได้ดังนี้  PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty: Warzone • TEKKEN 8 • League of Legends แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-041 game_rules ข้อ 41
- Question: VALORANT เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4846s | Wall: 0.4847s
- Sources: competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ  รายละเอียดที่เกี่ยวข้อง: - อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ - เอกสารและโน้ต ผู้เ...

### GR-042 game_rules ข้อ 42
- Question: VALORANT ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3009s | Wall: 0.301s
- Sources: competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้  รายละเอียดที่เกี่ยวข้อง: - Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพ...

### GR-043 game_rules ข้อ 43
- Question: VALORANT ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2602s | Wall: 0.2603s
- Sources: valorant_map_pool: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset  หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แ...

### GR-044 game_rules ข้อ 44
- Question: VALORANT ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4904s | Wall: 0.4904s
- Sources: valorant_agent_map_restriction: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง  หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT...

### GR-045 game_rules ข้อ 45
- Question: VALORANT ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5008s | Wall: 0.5008s
- Sources: valorant_agent_map_restriction: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง  หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT...

### GR-046 game_rules ข้อ 46
- Question: VALORANT มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.5847s | Wall: 0.5848s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น VALORANT ได้ครับ มีให้เล่นที่: PC Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-047 game_rules ข้อ 47
- Question: VALORANT ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6002s | Wall: 0.6002s
- Sources: competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s14_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ  รายละเอียดที่เกี่ยวข้อง: - 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น - การปรับแพ้ (Forfe...

### GR-048 game_rules ข้อ 48
- Question: VALORANT มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.7783s | Wall: 0.7784s
- Sources: competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น  รายละเอียดที่เกี่ยวข้อง: - ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์ - อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไป...

### GR-049 game_rules ข้อ 49
- Question: VALORANT ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6046s | Wall: 0.6046s
- Sources: competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: - ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน - อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ -...

### GR-050 game_rules ข้อ 50
- Question: VALORANT แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5403s | Wall: 0.5403s
- Sources: valorant_agent_map_restriction: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง  หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT...

### GR-051 game_rules ข้อ 51
- Question: CS2 คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.1264s | Wall: 0.1265s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็ง...

### GR-052 game_rules ข้อ 52
- Question: CS2 เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:related_guidance_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `fastpath/rulebase`
- Latency: 0.1728s | Wall: 0.1728s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: สรุปแนวเกมที่มีข้อมูลยืนยันได้: - FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone - MOBA: League of Legends - Fighting: TEKKEN 8 - Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone - VR/Rhythm: Beat Saber ใน VR Zone - Party/เล่นกับเพื่อน: Mario K...

### GR-053 game_rules ข้อ 53
- Question: CS2 มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6307s | Wall: 0.6307s
- Sources: cs2_map_pool: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train  หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026...

### GR-054 game_rules ข้อ 54
- Question: CS2 แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2363s | Wall: 0.2364s
- Sources: cs2_team_size_players: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน  หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2...

### GR-055 game_rules ข้อ 55
- Question: CS2 มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2134s | Wall: 0.2134s
- Sources: cs2_team_size_players: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน  หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2...

### GR-056 game_rules ข้อ 56
- Question: CS2 ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5316s | Wall: 0.5317s
- Sources: competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s41_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s58_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: - 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่...

### GR-057 game_rules ข้อ 57
- Question: CS2 ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5454s | Wall: 0.5454s
- Sources: cs2_pause_policy: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที  หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 คร...

### GR-058 game_rules ข้อ 58
- Question: CS2 ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3295s | Wall: 0.3296s
- Sources: cs2_pause_policy: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที  หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 คร...

### GR-059 game_rules ข้อ 59
- Question: CS2 มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3012s | Wall: 0.3013s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s35_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 8. ตารางบทลงโทษ (Penalties)  รายละเอียดที่เกี่ยวข้อง: - 5. พฤติกรรมและบทลงโทษ - บทลงโทษ - 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ - ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิ...

### GR-060 game_rules ข้อ 60
- Question: CS2 ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2989s | Wall: 0.2989s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น Counter-Strike 2 ได้ครับ มีให้เล่นที่: PC Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-061 game_rules ข้อ 61
- Question: CS2 ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3365s | Wall: 0.3366s
- Sources: competition_rules_cs2_psu_phuket_2026_s17_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s52_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น  รายละเอียดที่เกี่ยวข้อง: - 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง -...

### GR-062 game_rules ข้อ 62
- Question: CS2 รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4708s | Wall: 0.4708s
- Sources: cs2_format_single_elim_bo3: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)  หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อ...

### GR-063 game_rules ข้อ 63
- Question: CS2 รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2279s | Wall: 0.228s
- Sources: cs2_format_single_elim_bo3: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)  หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อ...

### GR-064 game_rules ข้อ 64
- Question: CS2 มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5705s | Wall: 0.5706s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s37_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s28_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: - 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ - การพิมพ์แชทในเกมที่ไม่เหมาะสม - 3. แผนที่ในการแข่งขัน - ตักเตือน → ปรับแพ้...

### GR-065 game_rules ข้อ 65
- Question: CS2 ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:games_fast_path`
- Route: `games/games_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.6795s | Wall: 0.6801s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: PC Zone มีเกมที่ยืนยันได้ดังนี้  PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty: Warzone • TEKKEN 8 • League of Legends แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-066 game_rules ข้อ 66
- Question: CS2 เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4367s | Wall: 0.4367s
- Sources: competition_rules_cs2_psu_phuket_2026_s11_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s50_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s18_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: - 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน - 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 To...

### GR-067 game_rules ข้อ 67
- Question: CS2 ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2926s | Wall: 0.2926s
- Sources: competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที  รายละเอียดที่เกี่ยวข้อง: - 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น...

### GR-068 game_rules ข้อ 68
- Question: CS2 ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.1965s | Wall: 0.1966s
- Sources: cs2_pause_policy: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที  หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 คร...

### GR-069 game_rules ข้อ 69
- Question: CS2 ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4635s | Wall: 0.4635s
- Sources: cs2_pause_policy: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที  หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 คร...

### GR-070 game_rules ข้อ 70
- Question: CS2 ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3346s | Wall: 0.3347s
- Sources: cs2_team_size_players: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน  หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2...

### GR-071 game_rules ข้อ 71
- Question: CS2 มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.493s | Wall: 0.4931s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น Counter-Strike 2 ได้ครับ มีให้เล่นที่: PC Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-072 game_rules ข้อ 72
- Question: CS2 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.497s | Wall: 0.497s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s37_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: - ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน - 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ - ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ - ป...

### GR-073 game_rules ข้อ 73
- Question: CS2 มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6859s | Wall: 0.6859s
- Sources: competition_rules_cs2_psu_phuket_2026_s58_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s32_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น  รายละเอียดที่เกี่ยวข้อง: - 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น - 2. การเ...

### GR-074 game_rules ข้อ 74
- Question: CS2 ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.51s | Wall: 0.5101s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s38_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด  รายละเอียดที่เกี่ยวข้อง: - ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน - 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง - การด่าทอ/ใช้ความรุนแรงทางวาจา - หยุดเกมโดยไม่ได้รับอ...

### GR-075 game_rules ข้อ 75
- Question: CS2 แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3742s | Wall: 0.3742s
- Sources: cs2_pause_policy: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที  หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 คร...

### GR-076 game_rules ข้อ 76
- Question: TEKKEN 8 คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.159s | Wall: 0.1591s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-077 game_rules ข้อ 77
- Question: TEKKEN 8 เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:related_guidance_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `fastpath/rulebase`
- Latency: 0.2464s | Wall: 0.2464s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: สรุปแนวเกมที่มีข้อมูลยืนยันได้: - FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone - MOBA: League of Legends - Fighting: TEKKEN 8 - Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone - VR/Rhythm: Beat Saber ใน VR Zone - Party/เล่นกับเพื่อน: Mario K...

### GR-078 game_rules ข้อ 78
- Question: TEKKEN 8 มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.8451s | Wall: 0.8451s
- Sources: tekken8_format_ps5_1v1: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที  หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที  อ้างอิงจากกติกา: Tekken 8 / PSU Es...

### GR-079 game_rules ข้อ 79
- Question: TEKKEN 8 แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3937s | Wall: 0.3937s
- Sources: competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: การหยุดเกม  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

### GR-080 game_rules ข้อ 80
- Question: TEKKEN 8 มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3108s | Wall: 0.3108s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: กติกาการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: - แข่งขันแบบ ออฟไลน์ (Offline) - ใช้เครื่องเกม PlayStation 5 - แข่งขันแบบ เดี่ยว (1v1) - รูปแบบการแข่งขัน:  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/compet...

### GR-081 game_rules ข้อ 81
- Question: TEKKEN 8 ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5264s | Wall: 0.5264s
- Sources: competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ  รายละเอียดที่เกี่ยวข้อง: - หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที - ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด - สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น...

### GR-082 game_rules ข้อ 82
- Question: TEKKEN 8 ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5624s | Wall: 0.5625s
- Sources: tekken8_pause_penalty: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร  หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอ...

### GR-083 game_rules ข้อ 83
- Question: TEKKEN 8 ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3835s | Wall: 0.3836s
- Sources: tekken8_pause_penalty: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร  หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round และ Pause ได้เฉพาะกรณีทั้งสองฝ่ายยินยอ...

### GR-084 game_rules ข้อ 84
- Question: TEKKEN 8 มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.3666s | Wall: 0.3667s
- Sources: competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที  รายละเอียดที่เกี่ยวข้อง: - ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น - ผู้เข้าแข่ง...

### GR-085 game_rules ข้อ 85
- Question: TEKKEN 8 ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.3419s | Wall: 0.3419s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น TEKKEN 8 ได้ครับ มีให้เล่นที่: PC Zone และ PlayStation 5 Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-086 game_rules ข้อ 86
- Question: TEKKEN 8 ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4303s | Wall: 0.4304s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ  รายละเอียดที่เกี่ยวข้อง: - หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที - การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน - หากก...

### GR-087 game_rules ข้อ 87
- Question: TEKKEN 8 รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5577s | Wall: 0.5577s
- Sources: tekken8_format_ps5_1v1: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที  หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที  อ้างอิงจากกติกา: Tekken 8 / PSU Es...

### GR-088 game_rules ข้อ 88
- Question: TEKKEN 8 รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.332s | Wall: 0.3321s
- Sources: tekken8_format_ps5_1v1: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที  หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที  อ้างอิงจากกติกา: Tekken 8 / PSU Es...

### GR-089 game_rules ข้อ 89
- Question: TEKKEN 8 มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.6878s | Wall: 0.6878s
- Sources: competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที  รายละเอียดที่เกี่ยวข้อง: - สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) - ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ) - ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความ...

### GR-090 game_rules ข้อ 90
- Question: TEKKEN 8 ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:games_fast_path`
- Route: `games/games_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.8853s | Wall: 0.8863s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้  PlayStation 5 Zone (18 เกม) • TEKKEN 8 • Marvel's Spider-Man 2 • Fortnite • God of War Ragnarok • Overcooked 2 • Gran Turismo 7 • Beat Saber • It Takes Two • LITTLE NIGHTMARES II • Monster Hunter Rise • EA Sports FC...

### GR-091 game_rules ข้อ 91
- Question: TEKKEN 8 เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4943s | Wall: 0.4944s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า  รายละเอียดที่เกี่ยวข้อง: - คำตัดสินของกรรมการถือเป็นที่สิ้นสุด - แข่งขันแบบ เดี่ยว (1v1) - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน...

### GR-092 game_rules ข้อ 92
- Question: TEKKEN 8 ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2934s | Wall: 0.2934s
- Sources: competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที  รายละเอียดที่เกี่ยวข้อง: - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข - ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของ...

### GR-093 game_rules ข้อ 93
- Question: TEKKEN 8 ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.2344s | Wall: 0.2345s
- Sources: tekken8_character_dlc_rule: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน  หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะท...

### GR-094 game_rules ข้อ 94
- Question: TEKKEN 8 ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4316s | Wall: 0.4316s
- Sources: tekken8_format_ps5_1v1: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที  หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที  อ้างอิงจากกติกา: Tekken 8 / PSU Es...

### GR-095 game_rules ข้อ 95
- Question: TEKKEN 8 ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.425s | Wall: 0.425s
- Sources: tekken8_equipment_ps5: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5  หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

### GR-096 game_rules ข้อ 96
- Question: TEKKEN 8 มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:games_availability_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.5452s | Wall: 0.5452s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เล่น TEKKEN 8 ได้ครับ มีให้เล่นที่: PC Zone และ PlayStation 5 Zone แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### GR-097 game_rules ข้อ 97
- Question: TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.5816s | Wall: 0.5816s
- Sources: competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที  รายละเอียดที่เกี่ยวข้อง: - หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที - ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่า...

### GR-098 game_rules ข้อ 98
- Question: TEKKEN 8 มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.708s | Wall: 0.7081s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ใช้เครื่องเกม PlayStation 5  รายละเอียดที่เกี่ยวข้อง: - ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) - ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข - ในกรณีเกิดข้อโต้แย้งหรือการประ...

### GR-099 game_rules ข้อ 99
- Question: TEKKEN 8 ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:rag_direct_curated`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.7277s | Wall: 0.7277s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)  รายละเอียดที่เกี่ยวข้อง: - เวลาแข่งขันต่อรอบ (Timer): 60 วินาที - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรร...

### GR-100 game_rules ข้อ 100
- Question: TEKKEN 8 แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `pipeline`
- Latency: 0.4817s | Wall: 0.4817s
- Sources: tekken8_format_ps5_1v1: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที  หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วินาที  อ้างอิงจากกติกา: Tekken 8 / PSU Es...
