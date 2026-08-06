# Broad Usage Eval v1

- Generated at: 2026-07-30T17:23:12
- Cases: 15
- Turn checks: 15
- Passed: 13
- Failed: 2
- Pass rate: 0.8667
- Total wall sec: 6.358
- Allow LLM: False
- RAG fallback: False

## By Group
- compound: 13/15 pass, 2 fail

## By Strategy
- compound: 14
- structured: 1

## Common Problems
- missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']: 1
- mode expected prefix ['pipeline: 1
- route_category expected ['multi_question'], got games: 1

## Top Failures

### C-007 compound
- Question: สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    สมาชิกมีกี่คน สมาชิกในหน้า Members แบ่งเป็น 3 หมวดครับ •    Members: 7 คน •    cooperative education and Internship student: 5 คน •    PSU Phuket Esports Club - PSU Phuket: 13 คน รวมทั้งหมด 25 คน แหล่งข้อมูล: https...

### C-011 compound
- Question: Call of Duty ปุ่มยิงอะไร แล้วเล่นได้ที่ไหน
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: route_category expected ['multi_question'], got games, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_game_controls
- Answer: Call of Duty: Modern Warfare III ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R2: ยิงอาวุธ - กดยิงปืน แหล่งข้อมูล: https://www.gamepur.com/guides/best-modern-warfare-3-controller-settings-aim-assist-deadzones-button-layout
