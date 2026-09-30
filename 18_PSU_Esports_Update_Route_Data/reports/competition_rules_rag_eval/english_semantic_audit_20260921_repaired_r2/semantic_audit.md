# Competition English Draft Semantic Audit

> This is a Local-LLM audit only. It identifies review priorities and never approves or publishes translations.

- Generated: 2026-09-21T22:31:02+07:00
- Draft input: `data\locales\en\localization_review_drafts_competition_20260921_repaired.jsonl`
- Text fields checked: **104**
- Verdicts: `{'pass': 83, 'review': 21}`
- Issue counts: `{"omits material condition: the Thai source specifies 'การจับฉลาก' (drawing of lots) as a procedural step, while the English draft only mentions 'Drawing of lots ": 1, 'numeric_tokens_changed': 14, "adds a fact (teams must immediately notify the referees) not in Thai source; Thai says 'must immediately inform referees' but does not specify who is responsibl": 1, 'adds a fact (chewing gum) not in Thai source': 1, "changes actor from 'drinking water' to 'chewing gum'": 1, "omits material condition of 'only allowed for drinking water'": 1, 'adds a fact (organizing side reserves the right to amend rules) not in Thai source': 1, "changes certainty from 'may' to 'reserves the right' implying stronger obligation": 1, 'audit_invalid_json': 1, "adds a fact: 'Each round played as Best of 3' implies a default format not stated in Thai source which says 'แข่ง Best of 3 (BO3) ทุกรอบ' but does not specify i": 1, "Food and drinks: changed from 'only drinking water in sealed containers and mahjong pieces' to 'only drinking water in sealed containers and chewing gum'": 1, "Documents and notes: changed from 'must give documents to referees before every match' to 'must give the documents to the referees before every match' (minor wo": 1, "omits material condition 'the match result will be recorded as 13-0' in Thai source; adds fact 'Game pause' not present in Thai source": 1, "omits material condition: 'in cases of cheating or match fixing' is vague and lacks specificity; Thai source specifies 'กรณีทุจริต (Cheating) หรือล็อกผล (Match ": 1}`

## Manual Review Required

### competition_rules_cs2_psu_phuket_2026_s07_c01
- Issues: `omits material condition: the Thai source specifies 'การจับฉลาก' (drawing of lots) as a procedural step, while the English draft only mentions 'Drawing of lots `
- Thai: 4. การจับฉลากและตารางเวลา
- English: Drawing of lots and schedule

### competition_rules_cs2_psu_phuket_2026_s14_c01
- Issues: `numeric_tokens_changed`
- Thai: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น
- English: Players may compete under only one team.

### competition_rules_cs2_psu_phuket_2026_s24_c01
- Issues: `numeric_tokens_changed`
- Thai: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- English: Match duration per round: 1 minute and 55 seconds | Freeze time: 15 seconds

### competition_rules_cs2_psu_phuket_2026_s33_c01
- Issues: `adds a fact (teams must immediately notify the referees) not in Thai source; Thai says 'must immediately inform referees' but does not specify who is responsibl`
- Thai: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
- English: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

### competition_rules_cs2_psu_phuket_2026_s53_c01
- Issues: `adds a fact (chewing gum) not in Thai source, changes actor from 'drinking water' to 'chewing gum', omits material condition of 'only allowed for drinking water'`
- Thai: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- English: 4. Only drinking water in sealed containers and chewing gum are permitted.

### competition_rules_cs2_psu_phuket_2026_s57_c01
- Issues: `adds a fact (organizing side reserves the right to amend rules) not in Thai source, changes certainty from 'may' to 'reserves the right' implying stronger obligation`
- Thai: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม
- English: Judgment authority: The referees' decisions and the organizers' rulings are final. The organizing side reserves the right to amend rules as appropriate for fairness.

### competition_rules_rov_blueket_2025_men_s03_c01
- Issues: `numeric_tokens_changed, audit_invalid_json`
- Thai: 1. กำหนดการแข่งขัน
1.1. แข่งขันออฟไลน์ วันที่ 11 กันยายน 2568
· เวลา 8.00-8.30 ลงทะเบียน
· เวลา 8.30-8.40 แบ่งสายการแข่งขัน
· เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
· เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
· เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
· เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
· เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3
- English: Competition Schedule 1.1. Offline event on September 11, 2025 · Registration: 8:00–8:30 AM · Draw of brackets: 8:30–8:40 AM · Round of 5 teams, Single Elimination BO3: 8:40–10:00 AM · Semifinal Match 1, Single Elimination BO3: 10:00–11:30 AM · Semifinal Match 2, Single Elimination BO3: 12:30–2:00 PM · Bronze Medal Match, Single Elimination BO3: 2:00–3:30 PM · Grand Final, Single Elimination BO3: 3:30–5:00 PM

### competition_rules_rov_blueket_2025_men_s05_c01
- Issues: `numeric_tokens_changed, adds a fact: 'Each round played as Best of 3' implies a default format not stated in Thai source which says 'แข่ง Best of 3 (BO3) ทุกรอบ' but does not specify i`
- Thai: 3. รูปแบบการแข่งขัน
3.1. แข่งแบบออฟไลน์
3.2. แข่ง Best of 3 (BO3) ทุกรอบ
- English: Competition Format 3.1. Offline Mode 3.2. Each round played as Best of 3 (BO3)

### competition_rules_rov_blueket_2025_men_s06_c01
- Issues: `numeric_tokens_changed`
- Thai: 4. ระเบียบและกติกาการแข่งขัน
4.1. กติกาพื้นฐาน
4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น
4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้
* ฝ่ายทีมสีฟ้าอยู่ด้านบน
* ฝ่ายทีมสีเเดงอยู่ข้างล่าง
4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
4.2. กติกาการแข่งขัน
4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick
4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ
4.2.4.ในการแข่งขัน ผู้เข้าแข่งขันทุกคนสามารถเลือกเล่นฮีโร่ได้ทั้งหมด
4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น
4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
4.3. การหลุดออกจากเกม (Disconnect) และการเริ่มเกมใหม่ (Rematch)
4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
- English: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others. 4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side. 4.1.3. The referees will announce the room number so both teams can enter the designated room. * The blue team is on top * The red team is on bottom 4.1.4. If a team starts the match more than 15 minutes after the scheduled time, the delayed team will be immediately forfeited. 4.2. Competition Rules 4.2.1. All participants must have at least 18 heroes for the "5v5" mode (formerly known as Tournament Mode). 4.2.2. Use Global Ban/Pick hero selection. 4.2.3. Runes and item bonuses may be used as desired. 4.2.4. In competition, all participants may choose any hero they wish. 4.2.5. Regarding skins, only Default skins may be used. 4.2.6. No duplicate hero selection or any other actions that cause system issues are permitted under any circumstances. 4.3. Disconnection and Rematch 4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.

### competition_rules_rov_blueket_2025_men_s06_c02
- Issues: `numeric_tokens_changed`
- Thai: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
4.4. เวลาพัก
4.4.1.ผู้ตัดสินจะแจ้งให้ผู้เข้าแข่งขันทราบถึงระยะเวลาที่เหลือก่อนที่เกมถัดไปจะเริ่มขึ้น
4.4.2.หากผู้เข้าแข่งขันไม่กลับมาภายในเวลาที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่งขัน
4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม
4.5. การหยุดพักเกมในการแข่งขัน
4.5.1.การหยุดพักเกมทั่วไป
4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ
- English: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.
4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.
4.3.5. If there is evidence that a competitor intentionally pauses the game, whether at a critical moment or to disrupt play, the offending team immediately forfeits the game in which the violation occurred and is immediately disqualified from the competition.
4.4. Break Time
4.4.1. The referee will inform competitors of the remaining time before the next game begins.
4.4.2. If competitors do not return within the stated time, the referee may declare that team to have forfeited the competition.
4.4.3. A 5-minute break follows every two games.
4.5. Game Pauses During Competition
4.5.1. General Game Pauses
4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.

### competition_rules_rov_blueket_2025_men_s06_c03
- Issues: `numeric_tokens_changed`
- Thai: 4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งให้หยุดพักเกมดังกล่าว และให้ผู้เข้าแข่งขันกลับเข้าสู่การแข่งขันใหม่อีกครั้งภายหลังจากผู้เข้าแข่งขันที่ไม่ได้เชื่อมต่อได้กลับเข้ามาในเกมแล้ว
4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
4.5.5.การหลุดการเชื่อมต่อโดยไม่เจตนา
4.5.5.1. หากผู้เข้าแข่งขันรายใดตกอยู่ในสภาวะที่เป็นอันตรายต่อชีวิต กล่าวคือ ไม่มีความปลอดภัยในการบริเวณการแข่งขัน หรือตกอยู่ในสถานการณ์อื่นใดที่ทำให้เกิดปัญหาในการดำเนินเกมต่อไป
4.5.5.2. ภัยธรรมชาติที่ทำให้เกมหยุดชะงัก
4.5.6.การหยุดพักเกมโดยผู้เข้าแข่งขัน
4.5.6.1. ผู้เข้าแข่งขันอาจหยุดพักเกมการแข่งขันได้ภายหลังจากเกิดเหตุการณ์ใดเหตุการณ์หนึ่งดังต่อไปนี้ โดยผู้เข้าแข่งขันดังกล่าวจะต้องส่งสัญญาณให้ผู้ตัดสินทราบโดยทันทีภายหลังจากการหยุดเกมและชี้แจงเหตุผลแห่งการหยุดเกมดังกล่าว
- English: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected. 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game. 4.5.3 After reconnection, the event staff may order both competing teams to immediately restart the game and/or continue playing anew, as they deem appropriate. 4.5.4 The referee may pause the game for any reason. 4.5.5 Unintentional disconnections. 4.5.5.1 If a player is in a life-threatening situation, such as being unsafe in the competition area or facing other circumstances that prevent continued gameplay. 4.5.5.2 Natural disasters causing game interruptions. 4.5.6 Player-initiated game pauses. 4.5.6.1 A player may pause the game following any of the following events, and must immediately signal the referee upon pausing the game to explain the reason for the pause.

### competition_rules_rov_blueket_2025_men_s06_c04
- Issues: `numeric_tokens_changed`
- Thai: 4.5.6.1.1. มีการรบกวนทางกายภาพระหว่างผู้เข้าแข่งขัน เช่น การก่อความวุ่นวาย ความโกลาหล และเสียงดังซึ่งรบกวนเกม เป็นต้น
4.5.6.1.2. อุปกรณ์พกพาหรือซอฟต์แวร์ทำงานผิดปกติ
4.5.6.1.3. การลดลงของเฟรมหรือ การเพิ่มขึ้นของ PING อันนอกเหนือจากการควบคุม
4.5.6.1.4. เมื่อผู้เข้าแข่งขันฝ่ายตรงข้ามโกงหรือดูถูกอย่างร้ายแรง เป็นต้น
4.6. ความเจ็บป่วยบาดเจ็บ หรือปัญหาทางกายภาพของผู้เข้าแข่งขันไม่เป็นเหตุที่สามารถยอมรับได้สำหรับการหยุดพักของผู้เข้าแข่งขัน
4.6.1.การหยุดพักเกมอันเนื่องมากจากปัญหาเครื่องร้อนของอุปกรณ์พกพา
4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
4.6.2.การหยุดพักเกมตามการตัดสินใจของผู้เข้าร่วมการแข่งขัน โดยไม่ได้รับอนุญาตจากผู้ตัดสิน
4.6.2.1. ทางทีมงานมีสิทธิเตือนและ/หรือปรับทีมผู้เข้าร่วมการแข่งขันดังกล่าวแพ้ทันที
4.6.2.2. ห้ามมิให้ผู้เข้าร่วมการแข่งขันพูดคุย ติดต่อสื่อสาร หรือดำเนินการใดๆ อันเป็นการสื่อสารในระหว่างการหยุดพักเกม
4.6.3.บทลงโทษ:
4.6.3.1. ครั้งที่ 1: ตักเตือน
4.6.3.2. ครั้งที่ 2: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 1 ครั้ง
4.6.3.3. ครั้งที่ 3: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 2 ครั้ง
- English: 4.5.6.1.1 Physical disturbances between competitors, such as causing chaos, noise, and loud sounds that interfere with gameplay. 4.5.6.1.2 Portable devices or software malfunctioning. 4.5.6.1.3 Frame drops or increased ping outside of player control. 4.5.6.1.4 When the opposing team engages in severe cheating or disrespect. 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay. 4.6.1. Game pauses due to portable device overheating. 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay. 4.6.2. Game pauses made by competitors without referee authorization. 4.6.2.1 Staff have the right to warn and/or immediately penalize the offending team by awarding a loss. 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication. 4.6.3. Penalties: 4.6.3.1 First offense: Warning. 4.6.3.2 Second offense: Award the opposing team one hero ban. 4.6.3.3 Third offense: Award the opposing team two hero bans.

### competition_rules_rov_blueket_2025_men_s07_c01
- Issues: `numeric_tokens_changed`
- Thai: 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
5.1. อุปกรณ์โทรศัพท์มือถือและอินเตอร์เน็ตส่วนตัว และ/หรืออินเทอร์เน็ตของทางมหาวิทยาลัย
5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว
5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที
- English: 5. Match sets and competition equipment 5.1. Personal mobile phones and internet, and/or university internet 5.2. Power adapters and personal charging devices 5.3. Tablets and iPads are not permitted for use during competition, nor any other equipment other than a mobile phone (Mobile Phone). If detected, the team will be disqualified immediately.

### competition_rules_rov_blueket_2025_men_s08_c01
- Issues: `numeric_tokens_changed`
- Thai: 6. การกระทำความผิดและบทลงโทษ
6.1. ห้ามมิให้ผู้เข้าแข่งขันทุกคนกระทำการอย่างหนึ่งอย่างใดดังต่อไปนี้
6.1.1.ห้ามใช้คำพูดหรือแสดงกิริยาไม่สุภาพ หรือเสียดสีผู้อื่น
6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที
6.1.2.ห้ามส่งผลการแข่งขันอันเป็นเท็จ หรือบิดเบือน
6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลักฐานและยุติการแข่งขันในทันที แต่หากมีการแข่งขันจนจบเกม จะถือว่าทั้งสองทีมยินยอมให้เกิดการแข่งขันขึ้น ทางทีมงานจะไม่รับฟังข้อโต้แย้งใด ๆ ทั้งสิ้น
6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.4.ห้ามมิให้ผู้เข้าแข่งขันทุกคนอนุญาตให้บุคคลอื่นเล่นแทนตนเองในขณะทำการแข่งขัน
6.1.4.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.5.ห้ามมิให้ผู้เข้าแข่งขันเสพ ค้า หรือดำเนินการใด ๆ อันเกี่ยวกับยาเสพติด บุหรี่ และอาวุธ และอื่น ๆ ที่ต้องห้ามตามกฎหมายการแข่งขันทันที
6.1.5.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจาก
- English: 6. Misconduct and Penalties 6.1. No competitor shall engage in any of the following acts: 6.1.1. No player shall use inappropriate language or display disrespectful behavior or make offensive remarks about others. 6.1.1.1. Penalty: Immediate loss of game upon detection of misconduct. 6.1.2. No competitor shall submit false results or manipulate outcomes. 6.1.2.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.3. No team may allow any individual not listed on their official roster to participate in the competition. If it is discovered that a competitor’s name does not match the registered list, evidence must be recorded and the match shall be terminated immediately. However, if the match proceeds to completion, both teams shall be deemed to have consented to the competition, and no appeals will be entertained by the organizing team. 6.1.3.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.4. No competitor may allow any other individual to play in their place during a match. 6.1.4.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.5. No competitor shall consume, trade, or engage in any activity involving prohibited substances such as narcotics, tobacco, weapons, or other items banned under competition regulations. 6.1.5.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition.

### competition_rules_rov_blueket_2025_men_s08_c02
- Issues: `numeric_tokens_changed`
- Thai: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น
6.2.1.ห้ามผู้เข้าแข่งขันทุกคนใช้โปรแกรมช่วยหรือในการเล่นใด ๆ ทั้งสิ้น
6.2.2.ห้ามผู้เข้าแข่งขันทุกคนกระทำการอย่างหนึ่งอย่างใดอันมีลักษณะเป็นการใช้ข้อผิดพลาดที่เกิดขึ้นภายในตัวเกม
6.2.3.ห้ามผู้เข้าแข่งขันทุกคนกระทำการจงใจหลุดจากการแข่งขัน
6.2.4.ห้ามผู้เข้าแข่งขันทุกคนกระทำการใด ๆ อันเป็นการยินยอมให้ทีมฝ่ายตรงข้ามชนะ
6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รับการร้องเรียนจากผู้อื่น ทีมงานจะมีมาตรการลงโทษผู้เข้าแข่งขันที่ฝ่าฝืนกติกา โดยตัดสิทธิ์การเข้าร่วมแข่งขัน
- English: 6.2. Use of assistive software during gameplay, and/or any action that creates an advantage or disadvantage to oneself or another competitor 6.2.1. No competitor may use any assistive software or tools during gameplay. 6.2.2. No competitor may perform any action involving exploiting in-game errors. 6.2.3. No competitor may intentionally disengage from the competition. 6.2.4. No competitor may take any action that constitutes allowing the opposing team to win. 6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

### competition_rules_valorant_psu_phuket_2026_s01_c01
- Issues: `numeric_tokens_changed`
- Thai: กฎระเบียบและรูปแบบการแข่งขัน VALORANT
รายการ PSU Phuket VALORANT 2026 Tournament
Update: 17/02/2026
English below
อุปกรณ์และอุปกรณ์ต่อพ่วง
ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)
* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
* ข้อห้ามสำคัญ
* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้
- English: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. * Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee, Mouse pad, In-ear headset (wired), Wired headset * Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs. * Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials. * Prohibited items: * Macros (both software- and hardware-based) are strictly prohibited. * Installing any unauthorized programs on the provided computers is strictly prohibited. * Accessing social media or any communication websites on competition computers is strictly prohibited, except for programs provided by organizers.

### competition_rules_valorant_psu_phuket_2026_s02_c01
- Issues: `Food and drinks: changed from 'only drinking water in sealed containers and mahjong pieces' to 'only drinking water in sealed containers and chewing gum', Documents and notes: changed from 'must give documents to referees before every match' to 'must give the documents to the referees before every match' (minor wo`
- Thai: พื้นที่การแข่งขันและกฎระเบียบ
* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
กระบวนการแข่งขัน
- English: Competition Area and Regulations
* Personnel: During Match Prep, no more than 6 players may be present.
* Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.
* Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.
* Food and drinks: Only drinking water in sealed containers and chewing gum are permitted.
Competition Process

### competition_rules_valorant_psu_phuket_2026_s04_c01
- Issues: `omits material condition 'the match result will be recorded as 13-0' in Thai source; adds fact 'Game pause' not present in Thai source`
- Thai: กระบวนการหลังจบแมตช์
* การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที
* การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0
การหยุดเกม
- English: Post-match process * Result recording: Officials will confirm and record the match result immediately. * Forfeiture: If a team forfeits, the map result will be recorded as 13-0. Game pause

### competition_rules_valorant_psu_phuket_2026_s06_c01
- Issues: `numeric_tokens_changed`
- Thai: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
* ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
* เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
- English: Tactical Timeout * Requested twice per map during regular rounds (first 24 rounds), each lasting 60 seconds. * During Overtime, an additional timeout is granted to each team, with quotas from regular rounds not carried over.

### competition_rules_valorant_psu_phuket_2026_s15_c01
- Issues: `omits material condition: 'in cases of cheating or match fixing' is vague and lacks specificity; Thai source specifies 'กรณีทุจริต (Cheating) หรือล็อกผล (Match `
- Thai: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)
- English: 5. Match Forfeit in cases of cheating or match fixing

### competition_rules_valorant_psu_phuket_2026_s23_c01
- Issues: `numeric_tokens_changed`
- Thai: 3. Player Emergency Pause
* Each team may request 1 pause per map.
* Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
Bug Regulations
- English: English translation 3. Player Emergency Pause * Each team may request one pause per map. * Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute Bug Regulations
