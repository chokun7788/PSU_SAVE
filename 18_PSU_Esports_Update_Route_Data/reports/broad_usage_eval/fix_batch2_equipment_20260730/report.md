# Broad Usage Eval v1

- Generated at: 2026-07-30T17:01:44
- Cases: 58
- Turn checks: 58
- Passed: 56
- Failed: 2
- Pass rate: 0.9655
- Total wall sec: 9.147
- Allow LLM: False
- RAG fallback: False

## By Group
- equipment: 56/58 pass, 2 fail

## By Strategy
- clarification: 4
- structured: 54

## Common Problems
- mode expected prefix ['pipeline: 1
- route_category expected ['equipment'], got games: 1

## Top Failures

### E-041 equipment
- Question: Nintendo Switch OLED คืออะไร
- Resolved: -
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/detail`
- Problems: route_category expected ['equipment'], got games
- Answer: เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:  EA Sports FC 24 •    แนวเกม: เกมฟุตบอล •    เล่นได้ที่: PlayStation 5 Zone  Nintendo Switch Sports •    แนวเกม: เกมกีฬา Motion Control •    เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.phu...

### E-042 equipment
- Question: Nintendo Switch OLED อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/game_availability_lookup`
- Problems: mode expected prefix ['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'], got pipeline:structured_games_genre_list
- Answer: เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:  EA Sports FC 24 •    แนวเกม: เกมฟุตบอล •    เล่นได้ที่: PlayStation 5 Zone  Nintendo Switch Sports •    แนวเกม: เกมกีฬา Motion Control •    เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.phu...
