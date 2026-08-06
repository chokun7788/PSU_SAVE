# Broad Usage Eval v1

- Generated at: 2026-07-30T17:16:40
- Cases: 159
- Turn checks: 159
- Passed: 156
- Failed: 3
- Pass rate: 0.9811
- Total wall sec: 16.029
- Allow LLM: False
- RAG fallback: False

## By Group
- game_controls: 156/159 pass, 3 fail

## By Strategy
- compound: 2
- pipeline: 7
- structured: 150

## Common Problems
- mode expected prefix ['pipeline: 3
- route_category expected ['games'], got multi_question: 2
- missing any of ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู']: 1
- route_category expected ['games'], got overview: 1

## Top Failures

### GC-075 game_controls
- Question: Mario Party Superstars ปุ่มเล่นบอร์ดและมินิเกมด้วยปุ่มกดอะไร
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['games'], got multi_question, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:multi_question_splitter
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    Mario Party Superstars ปุ่มเล่นบอร์ด กดอะไร Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button control...

### GC-096 game_controls
- Question: New Super Mario Bros. U Deluxe ปุ่มวิ่ง กระโดด และเหยียบศัตรูกดอะไร
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['games'], got multi_question, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:multi_question_splitter
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    New Super Mario Bros. U Deluxe ปุ่มวิ่ง กระโดด กดอะไร New Super Mario Bros. U Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    Simple controls: วิ่ง กระโดด และเหยียบศัตรู - หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side...

### GC-148 game_controls
- Question: Uncharted: Legacy of Thieves Collection ปุ่มมาร์กตำแหน่งศัตรูกดอะไร
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['games'], got overview, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:structured_members_group_list, missing any of ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู']
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...
