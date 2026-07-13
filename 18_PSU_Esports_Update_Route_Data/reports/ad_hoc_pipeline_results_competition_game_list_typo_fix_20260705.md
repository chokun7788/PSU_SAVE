# Ad Hoc Pipeline Test Log

- Generated: 2026-07-05T17:42:46
- JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_competition_game_list_typo_fix_20260705.jsonl`
- Total questions: 3

## Summary

- events_news/news_lookup: 1
- games/competition_game_list: 2

## Results

### 1. ตอนนี้รายการแข่งมเกมอะไรบ้าง

- mode: `pipeline:competition_game_list_fast_path`
- route: `games/competition_game_list`
- confidence: `0.95`
- elapsed: `0.0085` sec

คำตอบ:

เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้:
- Counter-Strike 2: PSU Phuket CS2 2026 Tournament
- VALORANT: PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย
- TEKKEN 8: PSU Esports / Tekken 8 Tournament
หมายเหตุ: นี่คือรายการที่มีเอกสารกติกาหรือข้อมูลการแข่งขันในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้
แหล่งข้อมูล: data/competition_rules

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 2. ตอนนี้มีเกมแข่งอะไรบ้าง

- mode: `pipeline:competition_game_list_fast_path`
- route: `games/competition_game_list`
- confidence: `0.95`
- elapsed: `0.0063` sec

คำตอบ:

เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้:
- Counter-Strike 2: PSU Phuket CS2 2026 Tournament
- VALORANT: PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย
- TEKKEN 8: PSU Esports / Tekken 8 Tournament
หมายเหตุ: นี่คือรายการที่มีเอกสารกติกาหรือข้อมูลการแข่งขันในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้
แหล่งข้อมูล: data/competition_rules

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 3. SURAT SMASH ส่งตัวแทนกี่คน

- mode: `pipeline:news_fast_path`
- route: `events_news/news_lookup`
- confidence: `0.9`
- elapsed: `0.0114` sec

คำตอบ:

SURAT SMASH ส่งตัวแทน 4 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/events-news/news

แหล่งข้อมูล:
- News | https://esports.computing.psu.ac.th/events-news/news
