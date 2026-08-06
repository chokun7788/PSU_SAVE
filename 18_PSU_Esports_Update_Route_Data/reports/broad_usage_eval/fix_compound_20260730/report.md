# Broad Usage Eval v1

- Generated at: 2026-07-30T17:22:15
- Cases: 15
- Turn checks: 15
- Passed: 12
- Failed: 3
- Pass rate: 0.8
- Total wall sec: 6.377
- Allow LLM: False
- RAG fallback: False

## By Group
- compound: 12/15 pass, 3 fail

## By Strategy
- compound: 12
- structured: 3

## Common Problems
- mode expected prefix ['pipeline: 3
- route_category expected ['multi_question'], got games: 2
- missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']: 1
- route_category expected ['multi_question'], got overview: 1

## Top Failures

### C-004 compound
- Question: Gran Turismo 7 เล่นยังไง แล้วปุ่มเร่งกดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: route_category expected ['multi_question'], got games, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_game_controls
- Answer: Gran Turismo 7 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R2: คันเร่ง - กดเพื่อเร่งเครื่อง •    R3: ไนตรัส / เร่งแซง - ใช้งานระบบเพิ่มความเร็วพิเศษที่มีติดตั้งในรถบางรุ่น แหล่งข้อมูล: https://gameinputdatabase.com/game/135

### C-007 compound
- Question: สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['multi_question'], got overview, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_members_role_lookup, missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']
- Answer: ตำแหน่ง อธิการบดี มี 1 คนครับ •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี (มหาวิทยาลัยสงขลานครินทร์)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### C-011 compound
- Question: Call of Duty ปุ่มยิงอะไร แล้วเล่นได้ที่ไหน
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: route_category expected ['multi_question'], got games, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_game_controls
- Answer: Call of Duty: Modern Warfare III ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R2: ยิงอาวุธ - กดยิงปืน แหล่งข้อมูล: https://www.gamepur.com/guides/best-modern-warfare-3-controller-settings-aim-assist-deadzones-button-layout
