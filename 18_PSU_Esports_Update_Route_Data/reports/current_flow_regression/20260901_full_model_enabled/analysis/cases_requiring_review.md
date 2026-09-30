# Per-case diagnostic review

Automatically grouped from actual traces. Tags are hypotheses, not a human-verified accuracy score.
The previous answer is a comparison only, not a ground-truth reference. Expected contracts are constraints, not necessarily a full ideal answer.

## MB-0089-G-001

Question: VALORANT คือเกมอะไร

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.21019689994864166
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "VALORANT"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.538865; margin=0.033946
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0091-G-003

Question: VALORANT เล่นยังไง

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2069860000628978
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.524442; margin=0.524442
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0092-G-004

Question: VALORANT เป็นเกมแนวไหน

### Actual answer
•    VALORANT เป็นเกมยิงเชิงกลยุทธ์แนว Tactical FPS
•    เล่นแบบทีม 5v5 โดยเลือก Agent มีสกิลเฉพาะ
•    เน้นการสื่อสาร การวาง Spike และการป้องกันพื้นที่
•    เล่นได้บน PC Zone เท่านั้นตามข้อมูลจาก PSU Esports Studio Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Mode: pipeline:structured_game_detail; status: completed; seconds: 2.9311162000522017
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมยิง Tactical FPS แบบทีม 5v5"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกมยิง Tactical FPS แบบทีม 5v5"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0093-G-005

Question: Counter-Strike 2 คือเกมอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.20495609985664487
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "Counter-Strike 2"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.500492; margin=0.500492
- Judge errors: ["category_mismatch:knowledge", "missing:Counter-Strike 2"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0095-G-007

Question: Counter-Strike 2 เล่นยังไง

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.17685459996573627
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike 2",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.498173; margin=0.498173
- Judge errors: ["category_mismatch:knowledge", "missing_any:Counter-Strike 2|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0104-G-016

Question: Call of Duty: Warzone เป็นเกมแนวไหน

### Actual answer
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.20837000012397766
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมยิง Battle Royale"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.491764; margin=0.491764
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกมยิง Battle Royale"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0105-G-017

Question: League of Legends คือเกมอะไร

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 4.405077900039032
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "League of Legends"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.534542; margin=0.04119
- Judge errors: ["category_mismatch:knowledge", "missing:League of Legends"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0107-G-019

Question: League of Legends เล่นยังไง

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.19659300008788705
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "League of Legends",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.492624; margin=0.492624
- Judge errors: ["category_mismatch:knowledge", "missing_any:League of Legends|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0108-G-020

Question: League of Legends เป็นเกมแนวไหน

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 4.3950510998256505
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม MOBA แบบทีม 5v5"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.544826; margin=0.02571
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม MOBA แบบทีม 5v5"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0109-G-021

Question: TEKKEN 8 คือเกมอะไร

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.21867189998738468
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "TEKKEN 8"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.517364; margin=0.517364
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0111-G-023

Question: TEKKEN 8 เล่นยังไง

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2111058000009507
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.486215; margin=0.486215
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0112-G-024

Question: TEKKEN 8 เป็นเกมแนวไหน

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.221772100077942
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมต่อสู้ 1v1"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.493294; margin=0.493294
- Judge errors: ["category_mismatch:events_news", "missing_any:แนวเกม|เกมต่อสู้ 1v1"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0116-G-028

Question: Marvel's Spider-Man 2 เป็นเกมแนวไหน

### Actual answer
•    Marvel's Spider-Man 2 เป็นเกมแนว Action-Adventure
•    เล่นบนแพลตฟอร์ม PlayStation 5 Zone
•    ผู้เล่นรับบท Spider-Man ต่อสู้กับศัตรูและสำรวจเมือง
•    มีระบบโหนใยเดินทางและการต่อสู้แบบคอมโบ
•    อัปเกรดสกิลระหว่างเนื้อเรื่องตามภารกิจต่าง ๆ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.966557800071314
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Action-Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Action-Adventure"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0120-G-032

Question: Fortnite เป็นเกมแนวไหน

### Actual answer
•    Fortnite เป็นเกมแนว Battle Royale
•    เกมแนว Battle Royale นิยมแข่งขันอีสปอร์ตอย่างมาก
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 1.4251298001036048
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Battle Royale"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.529504; margin=0.034693
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Battle Royale"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0132-G-044

Question: Horizon Call of the Mountain เป็นเกมแนวไหน

### Actual answer
•    Horizon Call of the Mountain เป็นเกมแนว Action-Adventure ในโลก VR
•    เน้นการปีนป่าย สำรวจ และต่อสู้กับจักรกลในโลก Horizon
•    เล่นผ่านแว่น VR โดยใช้คอนโทรลเลอร์ควบคุมการเคลื่อนไหวและยิงธนู
•    มีการจัดแสดงหรือเล่นได้ที่ VR Zone ตามข้อมูลจาก PSU Esports Studio Phuket
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Mode: pipeline:structured_game_detail; status: completed; seconds: 4.106352900154889
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม VR Action-Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม VR Action-Adventure"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0148-G-060

Question: FINAL FANTASY XVI เป็นเกมแนวไหน

### Actual answer
•    FINAL FANTASY XVI เป็นเกมแนว Action RPG
•    เน้นการต่อสู้และการพัฒนาตัวละคร
•    เล่นบนแพลตฟอร์ม PlayStation 5 Zone
•    มีเนื้อเรื่องแฟนตาซีเป็นแก่นหลัก
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 2.1843053000047803
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Action RPG"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Action RPG"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0152-G-064

Question: Hogwarts Legacy เป็นเกมแนวไหน

### Actual answer
•    Hogwarts Legacy เป็นเกมแนว Open-world Action RPG
•    เกมเน้นการสำรวจ พัฒนาตัวละคร และทำภารกิจในโลกเวทมนตร์
•    ผู้เล่นเรียนคาถา ต่อสู้ และแก้ปริศนาในฮอกวอตส์และพื้นที่รอบ ๆ
•    เล่นได้บน PlayStation 5 Zone โดยไม่ต้องใช้เครื่องอื่น ๆ
•    เกมเน้นความสมจริงของโลกเวทมนตร์และการโต้ตอบกับสิ่งแวดล้อมอย่างลึกซึ้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.512624599970877
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Open-world Action RPG"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Open-world Action RPG"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0156-G-068

Question: Resident Evil 4 เป็นเกมแนวไหน

### Actual answer
•    Resident Evil 4 เป็นเกมแนวเอาตัวรอดสยองขวัญ
•    เน้นการสำรวจ การต่อสู้ และการบริหารไอเทม
•    มีองค์ประกอบของ Action และ Survival Horror
•    เล่นได้ที่ PlayStation 5 Zone และ VR Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 2.7208984000608325
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Survival Horror"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Survival Horror"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0160-G-072

Question: Resident Evil Village เป็นเกมแนวไหน

### Actual answer
•    Resident Evil Village เป็นเกมแนว Survival Horror
•    เน้นบรรยากาศ การสำรวจ และการต่อสู้กับศัตรูหลากหลายรูปแบบ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 2.1564609000924975
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Survival Horror"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Survival Horror"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0161-G-073

Question: NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมอะไร

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5226066000759602
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "NARUTO X BORUTO Ultimate Ninja Storm Connections"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.659352; margin=0.659352
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0163-G-075

Question: NARUTO X BORUTO Ultimate Ninja Storm Connections เล่นยังไง

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.395457899896428
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "NARUTO X BORUTO Ultimate Ninja Storm Connections",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.647847; margin=0.647847
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0164-G-076

Question: NARUTO X BORUTO Ultimate Ninja Storm Connections เป็นเกมแนวไหน

### Actual answer
•    เกมแนวการต่อสู้แบบนินจา
•    มีองค์ประกอบการวางแผนและการตอบสนองแบบเรียลไทม์ในสนามรบ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 1.4588138000108302
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมต่อสู้จากอนิเมะ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.649177; margin=0.166158
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกมต่อสู้จากอนิเมะ"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0172-G-084

Question: Uncharted: Legacy of Thieves Collection เป็นเกมแนวไหน

### Actual answer
•    Uncharted: Legacy of Thieves Collection เป็นเกมแนว Action-Adventure
•    เน้นการสำรวจ ปีนป่าย แก้ปริศนา และแอ็กชัน
•    เล่นได้บน PlayStation 5 Zone
•    เกมมีบรรยากาศล่าสมบัติแบบผจญภัยเต็มตัว
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.217073200037703
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Action-Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Action-Adventure"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0177-G-089

Question: Overcooked 2 คือเกมอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3678790999110788
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "Overcooked 2"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.690738; margin=0.690738
- Judge errors: ["category_mismatch:knowledge", "missing:Overcooked 2"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0179-G-091

Question: Overcooked 2 เล่นยังไง

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.32341170008294284
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Overcooked 2",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.642098; margin=0.642098
- Judge errors: ["category_mismatch:knowledge", "missing_any:Overcooked 2|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0180-G-092

Question: Overcooked 2 เป็นเกมแนวไหน

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.37816080008633435
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Co-op ทำอาหาร"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.67172; margin=0.67172
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Co-op ทำอาหาร"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0184-G-096

Question: Super Smash Bros Ultimate เป็นเกมแนวไหน

### Actual answer
•    Super Smash Bros Ultimate เป็นเกมต่อสู้แนว Platform Fighter
•    เล่นโดยใช้ตัวละครจากหลายเกมเพื่อผลักคู่ต่อสู้ออกนอกสนาม
•    ผู้เล่นต้องวางแผนการโจมตีและหลบหลีกอย่างชาญฉลาด
•    เกมนี้รองรับการเล่นบน Nintendo Switch Zone เท่านั้น
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.249426699941978
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมต่อสู้แบบ Platform Fighter"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกมต่อสู้แบบ Platform Fighter"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0187-G-099

Question: Nintendo Switch Sports เล่นยังไง

### Actual answer
อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2917823998723179
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch Sports",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_definition; score=0.493368; margin=0.493368
- Judge errors: ["category_mismatch:knowledge", "missing_any:Nintendo Switch Sports|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0192-G-104

Question: Animal Crossing: New Horizons เป็นเกมแนวไหน

### Actual answer
พบชื่อเกมที่ตรงกับคำถามมากกว่า 1 เกมครับ
•    Horizon Call of the Mountain: Horizon Call of the Mountain คือเกม VR ผจญภัยในโลก Horizon ที่เน้นการปีนป่าย สำรวจ และต่อสู้กับจักรกล เล่นได้ที่: VR Zone
•    Animal Crossing: New Horizons: Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation, https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:game_multi_name_mention_fast_path; status: completed; seconds: 7.863742700079456
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Life Simulation"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Life Simulation"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0193-G-105

Question: It Takes Two คือเกมอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.29341160017065704
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "It Takes Two"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.493583; margin=0.493583
- Judge errors: ["category_mismatch:knowledge", "missing:It Takes Two"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0195-G-107

Question: It Takes Two เล่นยังไง

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3266518001910299
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "It Takes Two",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.505626; margin=0.505626
- Judge errors: ["category_mismatch:knowledge", "missing_any:It Takes Two|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0196-G-108

Question: It Takes Two เป็นเกมแนวไหน

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3405718000140041
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Co-op Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.489149; margin=0.489149
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Co-op Adventure"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0200-G-112

Question: Luigi's Mansion 3 เป็นเกมแนวไหน

### Actual answer
•    Luigi's Mansion 3 เป็นเกมแนว Action Puzzle
•    เกมผจญภัยจับผีสำรวจโรงแรมและแก้ปริศนา
•    ใช้เครื่องดูดผีสำรวจห้องจับผีผ่านด่าน
•    เล่นได้บน Nintendo Switch Zone
•    เกมแนว Action Puzzle โดยเน้นการสำรวจและการแก้ปริศนาแบบผจญภัยจับผี
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.598255299963057
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Action Puzzle"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Action Puzzle"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0204-G-116

Question: Mario Party Superstars เป็นเกมแนวไหน

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2693445000331849
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Party"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.481864; margin=0.481864
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Party"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0209-G-121

Question: Moving Out 2 คือเกมอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.21564629999920726
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [
    "Moving Out 2"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.483931; margin=0.483931
- Judge errors: ["category_mismatch:knowledge", "missing:Moving Out 2"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0211-G-123

Question: Moving Out 2 เล่นยังไง

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.20868650008924305
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Moving Out 2",
    "วิธีเล่น",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.480528; margin=0.480528
- Judge errors: ["category_mismatch:knowledge", "missing_any:Moving Out 2|วิธีเล่น|เล่นได้ที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0212-G-124

Question: Moving Out 2 เป็นเกมแนวไหน

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.22059800010174513
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Co-op Puzzle"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.484188; margin=0.484188
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Co-op Puzzle"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0220-G-132

Question: Ring Fit Adventure เป็นเกมแนวไหน

### Actual answer
•    Ring Fit Adventure เป็นเกมแนวออกกำลังกายผสมผสานกับการผจญภัย
•    เล่นด้วยการเคลื่อนไหวร่างกายผ่าน Ring-Con และ Joy-Con
•    ผู้เล่นต้องทำท่าออกกำลังกายเพื่อโจมตีและผ่านด่าน
•    เกมใช้ระบบตรวจจับการเคลื่อนไหวแบบจริงจัง
•    เล่นได้เฉพาะ Nintendo Switch Zone เท่านั้น
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.6375291000586003
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมออกกำลังกาย Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกมออกกำลังกาย Adventure"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0224-G-136

Question: Super Mario Odyssey เป็นเกมแนวไหน

### Actual answer
•    Super Mario Odyssey เป็นเกมแนว Platformer 3D
•    Mario เล่นสำรวจโลกต่าง ๆ และเก็บ Power Moon
•    เกมเน้นการวิ่ง กระโดด และใช้หมวก Cappy ควบคุมสิ่งของ
•    เล่นได้บน Nintendo Switch Zone
•    เป็นเกมผจญภัยที่เน้นการสำรวจและเก็บเป้าหมายต่าง ๆ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 3.432180699892342
Tags: answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Platformer 3D"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["missing_any:แนวเกม|เกม Platformer 3D"]

### Next checks
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0228-G-140

Question: The Legend of Zelda: Breath of the Wild เป็นเกมแนวไหน

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.50116360001266
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Open-world Adventure"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.483351; margin=0.483351
- Judge errors: ["category_mismatch:knowledge", "missing_any:แนวเกม|เกม Open-world Adventure"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0233-G-145

Question: มีเกมทั้งหมดกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04740249994210899
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0234-G-146

Question: ตอนนี้มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.040636599995195866
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0235-G-147

Question: PC มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04698290000669658
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0236-G-148

Question: PS5 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.039805399952456355
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0237-G-149

Question: Nintendo Switch มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04269219981506467
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0238-G-150

Question: VR มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.03760350006632507
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0239-G-151

Question: Cockpit มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.043716799933463335
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0242-G-154

Question: เกมแข่งรถมีอะไรบ้าง

### Actual answer
•    เกมแข่งรถเป็นหนึ่งในประเภทเกมอีสปอร์ต
•    ตัวอย่างเกมแข่งรถได้แก่ Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 1.5498697999864817
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_catalog_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.561321; margin=0.030029
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0243-G-155

Question: เกมยิงมีอะไรบ้าง

### Actual answer
•    Multiplayer Online Battle Arena (MOBA)
•    First-Person Shooter (FPS)
•    Battle Royale
•    Fighting Games
•    Sports Games
•    Racing Games
•    Digital Card Games
•    Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 1.6315914001315832
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_catalog_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.577588; margin=0.036194
- Judge errors: ["category_mismatch:knowledge", "missing_any:เกม|Zone|TEKKEN|Mario|Gran Turismo"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0246-G-158

Question: Tekken 8 มีในเครื่องไหน

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4910544999875128
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.534986; margin=0.534986
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0294-GC-048

Question: Horizon Call of the Mountain ปุ่มเคลื่อนที่ด้วยอนาล็อกกดอะไร

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0045964999590069056
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": "pipeline:structured_game_controls",
  "must_contain": [],
  "must_contain_any": [
    "Analogue control scheme",
    "เคลื่อนที่ด้วยอนาล็อก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_repeat_retype", "missing_any:Analogue control scheme|เคลื่อนที่ด้วยอนาล็อก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0334-GC-088

Question: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปุ่มเปลี่ยนตัวละครหลักกดอะไร

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.005188400158658624
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": "pipeline:structured_game_controls",
  "must_contain": [],
  "must_contain_any": [
    "RS (Right Stick) Left/Right",
    "เปลี่ยนตัวละครหลัก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_repeat_retype", "missing_any:RS (Right Stick) Left/Right|เปลี่ยนตัวละครหลัก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0362-GC-116

Question: Ring Fit Adventure ปุ่มยืนยันการเลือกกดอะไร

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.002992599969729781
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": "pipeline:structured_game_controls",
  "must_contain": [],
  "must_contain_any": [
    "X Button",
    "ยืนยันการเลือก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_repeat_retype", "missing_any:X Button|ยืนยันการเลือก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0390-GC-144

Question: Uncharted: Legacy of Thieves Collection ปุ่มมาร์กตำแหน่งศัตรูกดอะไร

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.00501550012268126
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": "pipeline:structured_game_controls",
  "must_contain": [],
  "must_contain_any": [
    "L3 (Click Left Stick)",
    "มาร์กตำแหน่งศัตรู"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_repeat_retype", "missing_any:L3 (Click Left Stick)|มาร์กตำแหน่งศัตรู"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0462-R-003

Question: จอง PS5 ต้องทำยังไง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0022370999213308096
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "reservation",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง|เช็คอิน|ชำระ|session|ยกเลิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0463-R-004

Question: จอง Nintendo Switch ต้องทำยังไง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0017632001545280218
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "reservation",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง|เช็คอิน|ชำระ|session|ยกเลิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0464-R-005

Question: จอง VR ต้องทำยังไง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0011640999000519514
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "reservation",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง|เช็คอิน|ชำระ|session|ยกเลิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0465-R-006

Question: จอง Cockpit ต้องทำยังไง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0009133000858128071
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "reservation",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง|เช็คอิน|ชำระ|session|ยกเลิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0466-R-007

Question: จอง PC ต้องทำยังไง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.000759099842980504
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "reservation",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง|เช็คอิน|ชำระ|session|ยกเลิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0482-S-003

Question: วันนี้เปิดไหม

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0012018000707030296
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "schedule",
    "reservation"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เปิด",
    "ปิด",
    "เวลา",
    "วัน",
    "ไม่เปิด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:เปิด|ปิด|เวลา|วัน|ไม่เปิด"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0496-M-007

Question: ผศ.ดร.นิวัติ แก้วประดับ ทำตำแหน่งอะไร

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0012197999749332666
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "อธิการบดี",
    "ผศ.ดร.นิวัติ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:อธิการบดี|ผศ.ดร.นิวัติ"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0497-M-008

Question: ใครเป็นอธิการบดี

### Actual answer
หน้าสมาชิกระบุว่า ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 1.0821366000454873
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ผศ.ดร.นิวัติ",
    "อธิการบดี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- overview/members_lookup -> about_us/overview_lookup; top=curated_about_members_president; score=0.543331; margin=0.543331
- Judge errors: ["category_mismatch:about_us"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0499-M-010

Question: ใครเป็นรองอธิการบดี

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.000159099930897
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "รศ.ดร.พันธ์",
    "รองอธิการบดี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0500-M-011

Question: รศ.ดร.อซีส นันทอมรพงศ์ ทำตำแหน่งอะไร

### Actual answer
[No output returned]

Mode: ; status: worker_crash; seconds: 29.842116199899465
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "คณบดี",
    "รศ.ดร.อซีส"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- worker_crash
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0501-M-012

Question: ใครเป็นคณบดี

### Actual answer
ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ

Mode: pipeline:request_timeout_no_answer; status: completed; seconds: 20.473016999894753
Tags: latency_over_10s, semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "รศ.ดร.อซีส",
    "คณบดี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- overview/members_lookup -> about_us/overview_lookup; top=curated_about_members_dean; score=0.517163; margin=0.517163
- Judge errors: ["category_mismatch:no_answer", "missing_any:รศ.ดร.อซีส|คณบดี"]

### Next checks
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0502-M-013

Question: ผศ.ดร.ณัฐพงศ์ ทองเทพ ทำตำแหน่งอะไร

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0012199999764561653
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ผู้ช่วยอธิการบดีฝ่ายวิชาการ",
    "ผศ.ดร.ณัฐพงศ์"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:ผู้ช่วยอธิการบดีฝ่ายวิชาการ|ผศ.ดร.ณัฐพงศ์"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0503-M-014

Question: ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 29.999996199971065
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ผศ.ดร.ณัฐพงศ์",
    "ผู้ช่วยอธิการบดีฝ่ายวิชาการ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0505-M-016

Question: ใครเป็นนักวิชาการคอมพิวเตอร์

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0018715998157858849
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "นายพฤทธิ์",
    "นักวิชาการคอมพิวเตอร์"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:นายพฤทธิ์|นักวิชาการคอมพิวเตอร์"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0507-M-018

Question: นายชนะชัย สิริพันธ์วราภรณ์ ทำตำแหน่งอะไร

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.014035400003195
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ผู้จัดการ",
    "นายชนะชัย"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0518-M-029

Question: นายษุภากรณ์ จิราจินดากุล ทำตำแหน่งอะไร

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.01556590013206
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ประธาน",
    "นายษุภากรณ์"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0519-M-030

Question: ใครเป็นประธาน

### Actual answer
ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ

Mode: pipeline:request_timeout_no_answer; status: completed; seconds: 24.62810910004191
Tags: latency_over_10s, semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "นายษุภากรณ์",
    "ประธาน"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- overview/members_lookup -> about_us/overview_lookup; top=curated_about_members_president; score=0.49196; margin=0.49196
- Judge errors: ["category_mismatch:no_answer", "missing_any:นายษุภากรณ์|ประธาน"]

### Next checks
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0532-M-043

Question: นางสาวสุภาสินี ธนภพ ทำตำแหน่งอะไร

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0008954000659286976
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "members",
    "overview"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "กรรมการ",
    "นางสาวสุภาสินี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:กรรมการ|นางสาวสุภาสินี"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0543-CR-007

Question: VALORANT รูปแบบการแข่งขันเป็นยังไง

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4523571999743581
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.538025; margin=0.538025
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0544-CR-008

Question: VALORANT รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.045690099941566586
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:VALORANT|กติกา|แข่งขัน|ยังไม่พบ"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0548-CR-012

Question: VALORANT ต้องเช็คอินก่อนแข่งไหม

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4863543000537902
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.492179; margin=0.492179
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0549-CR-013

Question: VALORANT ใช้บัญชีอะไรแข่ง

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3884050000924617
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.497753; margin=0.497753
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0558-CR-022

Question: CS2 รูปแบบการแข่งขันเป็นยังไง

### Actual answer
เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.48110740003176033
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "CS2",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_cs2_2026; score=0.480692; margin=0.480692
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0559-CR-023

Question: CS2 รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04716509999707341
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "CS2",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:CS2|กติกา|แข่งขัน|ยังไม่พบ"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0574-CR-038

Question: Counter-Strike 2 รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.038128199987113476
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Counter-Strike|กติกา|แข่งขัน|ยังไม่พบ"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0583-CR-047

Question: TEKKEN 8 ใช้ผู้เล่นกี่คน

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.36075169988907874
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.526338; margin=0.526338
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0588-CR-052

Question: TEKKEN 8 รูปแบบการแข่งขันเป็นยังไง

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5199854001402855
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.517363; margin=0.517363
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0589-CR-053

Question: TEKKEN 8 รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.040331299882382154
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:TEKKEN|กติกา|แข่งขัน|ยังไม่พบ"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0593-CR-057

Question: TEKKEN 8 ต้องเช็คอินก่อนแข่งไหม

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.44487920007668436
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.505829; margin=0.505829
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0594-CR-058

Question: TEKKEN 8 ใช้บัญชีอะไรแข่ง

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.39375349995680153
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.516802; margin=0.516802
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0603-CR-067

Question: ROV รูปแบบการแข่งขันเป็นยังไง

### Actual answer
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4311380998697132
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ROV",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- competition_rules/competition_rules_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.503063; margin=0.503063
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0604-CR-068

Question: ROV รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04527019988745451
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ROV",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:ROV|กติกา|แข่งขัน|ยังไม่พบ"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0607-CR-071

Question: ROV ถ้าใช้ bug จะโดนอะไร

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 0.7621492999605834
Tags: category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ROV",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["category_mismatch:no_answer"]

### Next checks

## MB-0613-C-002

Question: PS5 มีเกมอะไรกับราคาเท่าไหร่

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.03980230004526675
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "mode_mismatch:canonical_clarification", "missing_any:คำถามที่|ราคา|ปุ่ม|Zone|จอง"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0614-C-003

Question: PC มีอุปกรณ์อะไร แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04196270019747317
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "mode_mismatch:canonical_clarification", "missing_any:คำถามที่|ราคา|ปุ่ม|Zone|จอง"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0616-C-005

Question: Nintendo Switch ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.041208700044080615
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "mode_mismatch:canonical_clarification", "missing_any:คำถามที่|ราคา|ปุ่ม|Zone|จอง"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0618-C-007

Question: สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.00067690014839
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-0620-C-009

Question: PS5 กับ Nintendo Switch มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04769190005026758
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "mode_mismatch:canonical_clarification", "missing_any:คำถามที่|ราคา|ปุ่ม|Zone|จอง"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0624-C-013

Question: วันนี้เปิดไหม แล้วจอง PS5 ยังไง

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0016540999058634043
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": "pipeline:multi_question_splitter",
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_repeat_retype", "missing_any:คำถามที่|ราคา|ปุ่ม|Zone|จอง"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0636-ANA-010

Question: จอง

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.000488900113850832
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "clarification",
    "games",
    "equipment",
    "service_fee",
    "reservation",
    "no_answer"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "หมายถึง",
    "พิมพ์",
    "ยังไม่",
    "เกม",
    "อุปกรณ์",
    "ราคา",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-0641-ANA-015

Question: มี Minecraft ไหม

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3209016998298466
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "no_answer",
    "games",
    "general"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ยังไม่พบ",
    "ไม่มี",
    "ไม่ได้อยู่",
    "ตอบจากข้อมูล"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.486946; margin=0.486946
- Judge errors: ["category_mismatch:knowledge", "missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0651-AS-001

Question: PC #01-#02 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.053367899963632226
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "Counter-Strike 2",
    "League of Legends"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:TEKKEN 8|Counter-Strike 2|League of Legends"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0653-AS-003

Question: PC Zone รายการเกมมีอะไรบ้าง

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.30833699996583164
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "Counter-Strike 2",
    "League of Legends"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_catalog_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.481276; margin=0.481276
- Judge errors: ["category_mismatch:knowledge", "missing_any:TEKKEN 8|Counter-Strike 2|League of Legends"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0655-AG-002

Question: มี TEKKEN 8 ไหม

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.29126999992877245
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "PC #01-#02",
    "PC"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.554783; margin=0.554783
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0659-AG-006

Question: มี Counter-Strike 2 ไหม

### Actual answer
เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3587324998807162
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike 2",
    "PC #01-#02",
    "PC"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_cs2_2026; score=0.542968; margin=0.053189
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0663-AG-010

Question: มี League of Legends ไหม

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3237259001471102
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "League of Legends",
    "PC #01-#02",
    "PC"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.536736; margin=0.536736
- Judge errors: ["category_mismatch:knowledge", "missing_any:League of Legends|PC #01-#02|PC"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0671-AG-018

Question: มี VALORANT ไหม

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.31691549997776747
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "PC #01-#02",
    "PC"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_valorant_2026; score=0.53323; margin=0.53323
- Judge errors: ["category_mismatch:events_news"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0674-AS-004

Question: PC #03-#10 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04392389999702573
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Call of Duty: Warzone",
    "Counter-Strike 2",
    "League of Legends"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Call of Duty: Warzone|Counter-Strike 2|League of Legends"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0680-AS-006

Question: PlayStation 5 #01-#02 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.053091200068593025
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Call of Duty: Modern Warfare III",
    "Delta Force",
    "EA Sports FC 24"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Call of Duty: Modern Warfare III|Delta Force|EA Sports FC 24"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0702-AG-044

Question: มี Fortnite ไหม

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2892800997942686
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Fortnite",
    "PlayStation 5 #01-#02",
    "PlayStation 5"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.494208; margin=0.494208
- Judge errors: ["category_mismatch:knowledge", "missing_any:Fortnite|PlayStation 5 #01-#02|PlayStation 5"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0718-AG-060

Question: มี NARUTO X BORUTO Ultimate Ninja Storm Connections ไหม

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.43047109991312027
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "NARUTO X BORUTO Ultimate Ninja Storm Connections",
    "PlayStation 5 #01-#02",
    "PlayStation 5"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.645329; margin=0.645329
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0745-AS-009

Question: Nintendo Switch (1-2 Persons) มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.05855589988641441
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Pokémon Champions",
    "Animal Crossing: New Horizons",
    "It Takes Two"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Pokémon Champions|Animal Crossing: New Horizons|It Takes Two"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0757-AG-096

Question: มี It Takes Two ไหม

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.28252119990065694
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "It Takes Two",
    "Nintendo Switch (1-2 Persons)",
    "Nintendo Switch"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.496565; margin=0.496565
- Judge errors: ["category_mismatch:knowledge", "missing_any:It Takes Two|Nintendo Switch (1-2 Persons)|Nintendo Switch"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0793-AG-132

Question: มี Overcooked! ไหม

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3272645999677479
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Overcooked!",
    "Nintendo Switch (1-2 Persons)",
    "Nintendo Switch"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.640192; margin=0.640192
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0797-AG-136

Question: มี Overcooked! 2 ไหม

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3346297999378294
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Overcooked! 2",
    "Nintendo Switch (1-2 Persons)",
    "Nintendo Switch"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.652346; margin=0.652346
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-0816-AS-012

Question: Nintendo Switch (1-4 Persons) มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04456770000979304
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Pokémon Champions",
    "Animal Crossing: New Horizons",
    "It Takes Two"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Pokémon Champions|Animal Crossing: New Horizons|It Takes Two"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0818-AS-014

Question: Cockpit #01-#02 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.039697700180113316
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Gran Turismo 7"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Gran Turismo 7"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0825-AS-017

Question: VR Station 30 นาที มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04638350009918213
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Beat Saber",
    "Horizon Call of the Mountain",
    "Resident Evil 4"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Beat Saber|Horizon Call of the Mountain|Resident Evil 4"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0836-AS-020

Question: VR Station 1 ชั่วโมง มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.04023369983769953
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Beat Saber",
    "Horizon Call of the Mountain",
    "Resident Evil 4"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge", "missing_any:Beat Saber|Horizon Call of the Mountain|Resident Evil 4"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-0840-AMS-003

Question: PC #03 มี TEKKEN 8 ไหม

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2707878998480737
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ไม่มี",
    "PC #01-#02"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.578368; margin=0.578368
- Judge errors: ["category_mismatch:events_news", "missing_any:ไม่มี|PC #01-#02"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0841-AMS-004

Question: PC #10 มี TEKKEN 8 ไหม

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3012017998844385
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ไม่มี",
    "PC #01-#02"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_availability_lookup -> events_news/news_lookup; top=curated_news_surat_smash_tekken8; score=0.546155; margin=0.546155
- Judge errors: ["category_mismatch:events_news", "missing_any:ไม่มี|PC #01-#02"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0844-GD-001

Question: PUBG เป็นเกมแนวไหน

### Actual answer
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 5.363881999859586
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม Battle Royale",
    "PUBG",
    "แนว"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.550151; margin=0.033162
- Judge errors: ["category_mismatch:knowledge", "missing_any:เกม Battle Royale|PUBG|แนว"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0847-GD-004

Question: Call of Duty เป็นเกมแนวไหน

### Actual answer
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.35098200011998415
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "games",
    "clarification"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Call of Duty",
    "หลายเกม",
    "ยังไม่ชัด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.482822; margin=0.482822
- Judge errors: ["category_mismatch:knowledge", "missing_any:Call of Duty|หลายเกม|ยังไม่ชัด"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0859-GD-016

Question: The Legend of Zelda เป็นเกมแนวไหน

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4200025999452919
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เกม Open-world Adventure",
    "The Legend of Zelda",
    "แนว"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.515143; margin=0.515143
- Judge errors: ["category_mismatch:knowledge", "missing_any:เกม Open-world Adventure|The Legend of Zelda|แนว"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0970-GC-264

Question: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ถ้าจะเคลื่อนที่ต้องกดอะไร

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5532398000359535
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "LS (Left Stick)",
    "เคลื่อนที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.652962; margin=0.652962
- Judge errors: ["category_mismatch:knowledge", "missing_any:LS (Left Stick)|เคลื่อนที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0971-GC-265

Question: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ถ้าจะเปลี่ยนตัวละครหลักต้องกดอะไร

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5976056000217795
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "RS (Right Stick) Left/Right",
    "เปลี่ยนตัวละครหลัก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.60579; margin=0.60579
- Judge errors: ["category_mismatch:knowledge", "missing_any:RS (Right Stick) Left/Right|เปลี่ยนตัวละครหลัก"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0972-GC-266

Question: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ถ้าจะโจมตีระยะประชิดต้องกดอะไร

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5595561000518501
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Circle",
    "โจมตีระยะประชิด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.612766; margin=0.612766
- Judge errors: ["category_mismatch:knowledge", "missing_any:Circle|โจมตีระยะประชิด"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0973-GC-267

Question: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ถ้าจะคาถานินจา / จักระต้องกดอะไร

### Actual answer
บทความ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS กล่าวถึงศิลปะการบริหารจักระ การอ่านใจคู่ต่อสู้ และการตัดสินใจเสี้ยววินาทีในสนามรบนินจา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.5955729000270367
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Triangle",
    "คาถานินจา / จักระ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_naruto_connections_summary; score=0.697358; margin=0.697358
- Judge errors: ["category_mismatch:knowledge", "missing_any:Triangle|คาถานินจา / จักระ"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0984-GC-278

Question: Overcooked! ถ้าจะเคลื่อนที่ต้องกดอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.43124549998901784
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "L (Left Stick) / R (Right Stick)",
    "เคลื่อนที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.548938; margin=0.548938
- Judge errors: ["category_mismatch:knowledge", "missing_any:L (Left Stick) / R (Right Stick)|เคลื่อนที่"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0985-GC-279

Question: Overcooked! ถ้าจะหยิบ / วางต้องกดอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4027786999940872
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Cross / Square / L1 / R1",
    "หยิบ / วาง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.559212; margin=0.559212
- Judge errors: ["category_mismatch:knowledge", "missing_any:Cross / Square / L1 / R1|หยิบ / วาง"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0986-GC-280

Question: Overcooked! ถ้าจะหั่น / ขว้างต้องกดอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.4042819000314921
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "L2 / R2",
    "หั่น / ขว้าง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.53915; margin=0.53915
- Judge errors: ["category_mismatch:knowledge", "missing_any:L2 / R2|หั่น / ขว้าง"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-0987-GC-281

Question: Overcooked! ถ้าจะพุ่งตัวต้องกดอะไร

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.3915428000036627
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Circle / D-Pad Right",
    "พุ่งตัว"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_control_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_overcooked2_skills; score=0.519184; margin=0.519184
- Judge errors: ["category_mismatch:knowledge", "missing_any:Circle / D-Pad Right|พุ่งตัว"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-1228-M-048

Question: ตำแหน่ง อธิการบดี คือใคร

### Actual answer
หน้าสมาชิกระบุว่า ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 4.410100999986753
Tags: semantic_route_or_scope_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "overview",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ผศ.ดร.นิวัติ แก้วประดับ",
    "อธิการบดี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- overview/members_lookup -> about_us/overview_lookup; top=curated_about_members_president; score=0.50656; margin=0.50656
- Judge errors: ["category_mismatch:about_us"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.

## MB-1229-M-049

Question: ตำแหน่ง รองอธิการบดี คือใคร

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.007444000104442
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": "overview",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "รศ.ดร.พันธ์ ทองชุมนุม",
    "รองอธิการบดี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-1232-M-052

Question: ตำแหน่ง นักวิชาการคอมพิวเตอร์ คือใคร

### Actual answer
[No output returned]

Mode: ; status: harness_timeout; seconds: 30.00555650005117
Tags: infrastructure_or_watchdog_failure, latency_over_10s

### Expected contract
```json
{
  "expected_category": "overview",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "นายพฤทธิ์ เกษตรสมบูรณ์",
    "นักวิชาการคอมพิวเตอร์"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- No chatbot output received before the evaluation watchdog; not a product response.
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.

## MB-1252-C-016

Question: PC ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.03520929999649525
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "บาท",
    "เกม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-1254-C-018

Question: PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.03583450010046363
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PS5",
    "บาท",
    "เกม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-1257-C-021

Question: VR ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.02786620007827878
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VR",
    "บาท",
    "เกม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-1259-C-023

Question: Cockpit ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.02490590000525117
Tags: pilot_catalog_ownership_intercept

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Cockpit",
    "บาท",
    "เกม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Legacy question was intercepted by isolated pilot before legacy routing.
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.

## MB-1452-GL-127

Question: เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค อธิบายแบบใช้กับวงการเกม

### Actual answer
เกมที่นิยมในปัจจุบัน ได้แก่ VALORANT, Mobile Legends: Bang Bang, Tekken, Mario Kart และ EA SPORTS FC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.6351575998123735
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

### Observations
- general/general_knowledge_query -> knowledge/knowledge_lookup; top=curated_knowledge_current_popular_games; score=0.49613; margin=0.49613
- Judge errors: ["missing_any:กิจกรรม"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## MB-1456-GL-131

Question: อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.003927099984139204
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:latency|หน่วง"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1457-GL-132

Question: เฟรมเรตกับความละเอียดต่างกันยังไง ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.002167999977245927
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เฟรม",
    "ความละเอียด"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:เฟรม|ความละเอียด"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1458-GL-133

Question: API คืออะไร ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.002645100001245737
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "API",
    "เชื่อมต่อ"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:API|เชื่อมต่อ"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1459-GL-134

Question: JSON คืออะไร ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0028013999108225107
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "JSON",
    "ข้อมูล"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:JSON|ข้อมูล"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1460-GL-135

Question: ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.00317799998447299
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ขอบคุณ"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:ขอบคุณ"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1461-GL-136

Question: แปลคำว่า reservation เป็นภาษาไทย ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0021613999269902706
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:จอง"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1462-GL-137

Question: เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0044998000375926495
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:กิจกรรม"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1463-GL-138

Question: คีย์บอร์ด mechanical คืออะไรแบบสั้น ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.003888299921527505
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "คีย์บอร์ด",
    "mechanical"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:คีย์บอร์ด|mechanical"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1464-GL-139

Question: GPU คืออะไรแบบเข้าใจง่าย ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0031860999297350645
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "GPU",
    "กราฟิก"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:GPU|กราฟิก"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## MB-1465-GL-140

Question: server กับ client ต่างกันยังไง ช่วยยกตัวอย่างสั้น ๆ

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.002121400088071823
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "server",
    "client"
  ],
  "must_not_contain": []
}
```

### Observations
- ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["category_mismatch:input_quality", "missing_any:server|client"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.

## KIA-0018

Question: ;yoouhgxbfws,

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0010735001415014267
Tags: detector_false_positive

### Expected contract
```json
{}
```

### Observations
- Extra flags: repeated_character_typo
- Judge errors: ["source_case_unavailable"]

### Next checks
- Review valid Thai combining marks and English names; calibrate thresholds without training on this test set.

## KIA-0187

Question: เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย

### Actual answer
คำตอบ: เฟรมเรตคือจำนวนเฟรมต่อวินาที ความละเอียดคือขนาดภาพครับ
ข้อดี: เฟรมเรตสูงทำให้เคลื่อนไหวลื่นไหลมากขึ้นครับ
ข้อเสีย: ความละเอียดสูงใช้หน่วยความจำมากกว่าครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 2.825455099809915
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "เฟรม",
    "ความละเอียด"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0190

Question: PUBG อยู่โซซนไหน

### Actual answer
ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_games_catalog; status: completed; seconds: 6.184202699922025
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "PC #01-#02"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0192

Question: Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน

### Actual answer
อุปกรณ์ใน PC Zone:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units)
•    Gaming Monitor (10 Units)
•    Gaming Keyboard
•    Gaming Mouse
•    Gaming Headset
•    Gaming Chair (10 Units)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Mode: pipeline:structured_equipment_catalog; status: completed; seconds: 8.05622289981693
Tags: detector_false_negative, route_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "equipment",
    "games"
  ],
  "expected_mode_prefix": [
    "pipeline:structured_equipment_item",
    "pipeline:equipment_item_location_fast_path"
  ],
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["mode_mismatch:pipeline:structured_equipment_catalog"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0194

Question: VALORANT ถ้าใช้ bug จะโดดนอะไร

### Actual answer
คำตอบ: * Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้

รายละเอียดที่เกี่ยวข้อง:
•    Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
•    Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้
•    หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    การใช้ช่องโหว่ (Exploit Adjudication)

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.7887929999269545
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "VALORANT",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0204

Question: Counter-Strike 2 ใช้จออยยังไง

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

Mode: pipeline:no_answer; status: completed; seconds: 7.287474100012332
Tags: detector_false_negative, answer_text_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike 2",
    "ปุ่ม",
    "จอย",
    "คอนโทรล"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## KIA-0226

Question: ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย

### Actual answer
ขอบคุณสำหรับความช่วยเหลือเสมอครับ
ขอให้ท่านมีวันนี้เป็นไปอย่างดีครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 1.887317799963057
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ขอบคุณ"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0231

Question: Gaming Monitor อยู่โซซนไหน

### Actual answer
อุปกรณ์ใน PC Zone:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units)
•    Gaming Monitor (10 Units)
•    Gaming Keyboard
•    Gaming Mouse
•    Gaming Headset
•    Gaming Chair (10 Units)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Mode: pipeline:structured_equipment_catalog; status: completed; seconds: 1.1325145000591874
Tags: detector_false_negative, route_contract_mismatch

### Expected contract
```json
{
  "expected_category": [
    "equipment",
    "games"
  ],
  "expected_mode_prefix": [
    "pipeline:structured_equipment_item",
    "pipeline:equipment_item_location_fast_path"
  ],
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["mode_mismatch:pipeline:structured_equipment_catalog"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0242

Question: VALORANT อยู่โโซนไหน

### Actual answer
ได้ครับ VALORANT เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_service_game_availability; status: completed; seconds: 0.38731619995087385
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "PC #01-#02"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0252

Question: เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย

### Actual answer
กิจกรรมนี้จะมาถึงแล้วครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 1.2782771999482065
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0261

Question: PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.030301399994641542
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "multi_question",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PS5",
    "บาท",
    "เกม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:knowledge"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0270

Question: Gaming Keyboard อยู่โโซนไหน

### Actual answer
Gaming Keyboard: คีย์บอร์ดสำหรับควบคุมเกมและพิมพ์บน Gaming PC
อยู่ที่: PC Zone
ใช้สำหรับ:
•    ควบคุมเกม PC
•    พิมพ์ข้อมูล
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Mode: pipeline:structured_equipment_item; status: completed; seconds: 0.9996119001880288
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "equipment",
    "games"
  ],
  "expected_mode_prefix": [
    "pipeline:structured_equipment_item",
    "pipeline:equipment_item_location_fast_path"
  ],
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0277

Question: วันนี้มีข่าาว esports อะไรล่าสุด

### Actual answer
โหมดทดลอง RAG: ยังไม่มี context ที่โยงกับคำถามนี้ได้ชัดในฐานข้อมูลหมวด no_answer
ถ้าต้องการให้ตอบได้ ควรเพิ่ม fact/card หรือข้อมูลจริงของเรื่องนั้นเข้า knowledge base ก่อน

Mode: pipeline:experimental_rag_no_context; status: completed; seconds: 0.3228446999564767
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "no_answer",
    "games",
    "general"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ยังไม่พบ",
    "ไม่มี",
    "ไม่ได้อยู่",
    "ตอบจากข้อมูล"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: []

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0310

Question: กี่บบาท

### Actual answer
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

Mode: pipeline:ambiguity_clarification; status: completed; seconds: 0.04563449998386204
Tags: detector_false_negative, unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["source_case_unavailable"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0320

Question: เกมอะไรร

### Actual answer
ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_games_catalog; status: completed; seconds: 0.24383419984951615
Tags: detector_false_negative, unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["source_case_unavailable"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0332

Question: TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0018838001415133476
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "games",
    "multi_question"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "Resident Evil Village",
    "ปุ่ม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0340

Question: Counter3Strike 2 ,klkp0tFffovtwi

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.000705100130289793
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0348

Question: Gaming Headset vp^jF::owso

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0010784000623971224
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "equipment",
    "games"
  ],
  "expected_mode_prefix": [
    "pipeline:structured_equipment_item",
    "pipeline:equipment_item_location_fast_path"
  ],
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_layout_retype", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0351

Question: Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0016676001250743866
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "games",
    "multi_question"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Gran Turismo 7",
    "Overcooked! 2",
    "ปุ่ม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0352

Question: =j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.001743100117892027
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "ขอบคุณ"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any", "llm_required"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0356

Question: Fortnite .=h0vvppy'w'

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0011011001188308
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Fortnite",
    "ปุ่ม",
    "จอย",
    "คอนโทรล"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0361

Question: cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0013156000059098005
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any", "llm_required"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0364

Question: Delta Force vp^jF::owso

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0011980000417679548
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "PlayStation 5",
    "PlayStation 5 #01-#02"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0369

Question: Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0009632001165300608
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "games",
    "multi_question"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Beat Saber",
    "VALORANT",
    "ปุ่ม"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0370

Question: g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0031560000497847795
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any", "llm_required"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0374

Question: Fortnite x6j,gx]ujpo preset 00vpdfvtwi

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.001205699983984232
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": "pipeline:structured_game_controls",
  "must_contain": [],
  "must_contain_any": [
    "Controller Mapping page",
    "เปลี่ยน preset จอย"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_layout_retype", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0375

Question: Gaming Chair vp^jF::owso

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0007038998883217573
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "equipment",
    "games"
  ],
  "expected_mode_prefix": [
    "pipeline:structured_equipment_item",
    "pipeline:equipment_item_location_fast_path"
  ],
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "mode_mismatch:input_guard_layout_retype", "missing_any"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0379

Question: 8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.0013504000380635262
Tags: detector_false_negative

### Expected contract
```json
{
  "expected_category": [
    "general",
    "knowledge"
  ],
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "คีย์บอร์ด",
    "mechanical"
  ],
  "must_not_contain": []
}
```

### Observations
- Missing flags: repeated_character_typo
- Judge errors: ["category_mismatch:input_quality", "missing_any", "llm_required"]

### Next checks
- Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.

## KIA-0385

Question: Counter-Strike 2 รอบชิงเล่นกี่เกม

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.021704599959775805
Tags: unscored_or_review

### Expected contract
```json
{
  "expected_category": "competition_rules",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike",
    "กติกา",
    "แข่งขัน",
    "ยังไม่พบ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- Judge errors: ["category_mismatch:knowledge", "missing_any"]

### Next checks

## KIA-0430

Question: Fortnite เป็นเกมแนวไหน

### Actual answer
ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต ได้แก่ Multiplayer Online Battle Arena (MOBA), First-Person Shooter (FPS), Battle Royale, Fighting Games, Sports Games, Racing Games, Digital Card Games และ Real-Time Strategy (RTS)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.20731769991107285
Tags: semantic_route_or_scope_mismatch, answer_text_contract_mismatch, category_contract_mismatch

### Expected contract
```json
{
  "expected_category": "games",
  "expected_mode_prefix": null,
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกม Battle Royale"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

### Observations
- games/game_detail_lookup -> knowledge/knowledge_lookup; top=curated_knowledge_esports_categories; score=0.529504; margin=0.034693
- Judge errors: ["category_mismatch:knowledge", "missing_any"]

### Next checks
- Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.
- Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.

## KIA-0431

Question: VR ราคาเท่าไหร่

### Actual answer
VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท

VR 1 ชั่วโมง (60 นาที, 1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 375 บาท
•    General Adult: 1,050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Mode: pipeline:deterministic_calculator_fast; status: completed; seconds: 0.13371500000357628
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0432

Question: PS5 มีเกมอะไรบ้าง

### Actual answer
กรุณาระบุชื่อเกมหรือหัวข้อเดียว พร้อมสิ่งที่ต้องการทราบให้ชัดเจนอีกครั้งครับ

Mode: canonical_clarification; status: completed; seconds: 0.019371500005945563
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0433

Question: PC Zone เปิดกี่โมง

### Actual answer
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_schedule; status: completed; seconds: 0.15988980000838637
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0434

Question: VALORANT เล่นเครื่องไหน

### Actual answer
PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.22922390000894666
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0435

Question: Minecraft มีใน PC #03 ไหม

### Actual answer
ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 42 เกม:

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:games_known_unsupported_fast_path; status: completed; seconds: 1.1601334000006318
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0436

Question: TEKKEN 8 อยู่โซนไหน

### Actual answer
ได้ครับ TEKKEN 8 เล่นได้ที่ PC Zone - PC #01-#02, PlayStation 5 Zone - PlayStation 5 #01-#02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_service_game_availability; status: completed; seconds: 0.29374870005995035
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0437

Question: Nintendo Switch OLED ราคาเท่าไหร่

### Actual answer
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 140 บาท

Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 100 บาท
•    General Adult: 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Mode: pipeline:deterministic_calculator_fast; status: completed; seconds: 0.1817147999536246
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0438

Question: Counter-Strike 2 ใช้ Steam เวอร์ชันไหน

### Actual answer
คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
•    5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
•    1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.3634151997976005
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0439

Question: ROV แข่งผ่าน Discord ใช่ไหม

### Actual answer
คำตอบ: 4.5.5.1. หากผู้เข้าแข่งขันรายใดตกอยู่ในสภาวะที่เป็นอันตรายต่อชีวิต กล่าวคือ ไม่มีความปลอดภัยในการบริเวณการแข่งขัน หรือตกอยู่ในสถานการณ์อื่นใดที่ทำให้เกิดปัญหาในการดำเนินเกมต่อไป

รายละเอียดที่เกี่ยวข้อง:
•    4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
•    4.5.6.การหยุดพักเกมโดยผู้เข้าแข่งขัน
•    กติกาการแข่งขัน Blueket Games 2025
•    4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
•    2. สถานที่แข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.5108765999320894
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0440

Question: PUBG: BATTLEGROUNDS มีหรือเปล่า

### Actual answer
PUBG: BATTLEGROUNDS: PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย
แนวเกม: เกม Battle Royale
วิธีเล่นโดยสรุป: เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Mode: pipeline:structured_game_detail; status: completed; seconds: 1.4906899000052363
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0441

Question: ดูข้อมูลที่ https://esports.phuket.psu.ac.th

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.5731835998594761
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0442

Question: ติดต่อ esports@phuket.psu.ac.th ได้ไหม

### Actual answer
Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us, https://esports.computing.psu.ac.th/

Mode: pipeline:rag_direct_curated; status: completed; seconds: 1.2157311998307705
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0443

Question: รหัสนักศึกษา 600584 ใช้สมัครได้ไหม

### Actual answer
รหัสนักศึกษา 600584 ใช้สมัครได้ครับ กรุณาตรวจสอบข้อมูลเพิ่มเติมจากแหล่งที่มาอย่างเป็นทางการครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 2.7822735998779535
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0444

Question: booking ID BK-2026-000123 เช็คที่ไหน

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 4.293066899990663
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0445

Question: จองวันที่ 2026-09-01 เวลา 13:30

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด schedule ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 4.170516100013629
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0446

Question: เปิด 09:00-12:00 และ 13:00-16:00 ใช่ไหม

### Actual answer
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*

รายละเอียดจากตาราง:
•    Morning คือ 09:00-12:00
•    Afternoon คือ 13:00-16:00
•    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
•    Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
•    Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
•    Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Mode: pipeline:schedule_fast_path; status: completed; seconds: 3.719591800123453
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0447

Question: โทร 076-123-4567 ได้หรือเปล่า

### Actual answer
เบอร์โทร 076-123-4567 ไม่ปรากฏอยู่ในข้อมูลติดต่อที่ยืนยันได้ของ PSU Esports Studio - Phuket กรุณาตรวจสอบเบอร์โทรอีกครั้งหรือติดต่อผ่านช่องทางอื่น ๆ เช่น อีเมล psuesportspkt@gmail.com หรือ Facebook https://www.facebook.com/psuesportsphuket เพื่อขอความช่วยเหลือเพิ่มเติมได้ครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

Mode: pipeline:experimental_rag_llm_fallback; status: completed; seconds: 5.46572250011377
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0448

Question: เว็บ local อยู่ที่ http://127.0.0.1:8018/ ใช่ไหม

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 1.0902633999940008
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0449

Question: BGE-M3 ใช้ทำ retrieval ใช่ไหม

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 1.00410300004296
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0450

Question: โมเดล scb10x/typhoon2.5-qwen3-4b ใช้อยู่หรือเปล่า

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 1.2952918000519276
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0451

Question: ราคา 150 บาท/session ใช่ไหม

### Actual answer
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

Mode: pipeline:ambiguity_clarification; status: completed; seconds: 0.13026249990798533
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0452

Question: PC #01-#02 เล่นเกมอะไรได้บ้าง

### Actual answer
PC Zone มีเกมที่ยืนยันได้ดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_service_game_availability; status: completed; seconds: 0.2915849001146853
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0453

Question: QR CODE จากสลิปใช้ซ้ำได้ไหม

### Actual answer
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.36135449982248247
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0454

Question: API /api/slots ใช้งานได้หรือยัง

### Actual answer
API /api/slots ยังใช้งานได้ครับ กรุณาตรวจสอบเชื่อมต่ออีกครั้งหากมีปัญหาครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 2.3508564999792725
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0455

Question: WordPress REST API เชื่อมแล้วหรือยัง

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 1.0668439001310617
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0456

Question: booking_id=BK-2026-000456 มีสถานะอะไร

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 4.55280840001069
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0457

Question: transaction_ref TXN20260830001 ซ้ำหรือเปล่า

### Actual answer
กิจกรรม GAME ON! เปิดโลกอีสปอร์ต จัดสำหรับนักเรียนชั้นมัธยมศึกษาปีที่ 3 (ม.3) จากโรงเรียนท้ายเหมืองวิทยา จำนวน 21 คน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.5672834999859333
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0458

Question: หมายเลข 061-234-5678 ติดต่อเจ้าหน้าที่ได้ไหม

### Actual answer
สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน:
Members (7 คน):
•    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี
•    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี
•    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี
•    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ
•    นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์
•    นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์
•    นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ

cooperative education and Internship student (5 คน):
•    นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer
•    Mr. Amine Abidellaoui: Internship Student
•    นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer
•    Mr. Yanis Igoudjil: Internship Student
•    นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer

PSU Phuket Esports Club - PSU Phuket (13 คน):
•    นายษุภากรณ์ จิราจินดากุล: ประธาน
•    นายนพัทธ์ ฝอยทอง: รองประธาน
•    นายปัณณวิชญ์ หนูเรือง: เลขานุการ
•    นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
•    นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
•    นางสาวกมลวรรณ นวลสาย: กรรมการ
•    นางสาวชญาภา จันทร์เอิบ: กรรมการ
•    นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
•    นางสาวสุภาสินี ธนภพ: กรรมการ
•    นางสาวอาทิตยา แดงประดับ: กรรมการ
•    นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
•    นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
•    นายอรรถนนท์ สุขแก้ว: กรรมการ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

Mode: pipeline:structured_members_group_list; status: completed; seconds: 0.3370110001415014
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0459

Question: eFootball 2026 มีในศูนย์ไหม

### Actual answer
ได้ครับ eFootball เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_service_game_availability; status: completed; seconds: 0.4124956999439746
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0460

Question: ตอบเป็น JSON ได้ไหม เช่น {"zone":"PC"}

### Actual answer
ยังไม่พบ Json ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 42 เกม:

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:games_unknown_fast_path; status: completed; seconds: 19.927326600067317
Tags: latency_over_10s, unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0461

Question: ราคาเท่าไหร่ครับบบ

### Actual answer
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

Mode: pipeline:ambiguity_clarification; status: completed; seconds: 0.08120770007371902
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0462

Question: เล่นได้ไหมมม

### Actual answer
เล่นได้ครับ มมมีความสนุกและเต็มไปด้วยพลังงานเสมอครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 1.3152948999777436
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0463

Question: ขอบคุณค่าาา

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.891158499987796
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0464

Question: อยากเล่นมากกก

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 4.070274400059134
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0465

Question: ช่วยหน่อยยย

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8702232998330146
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0466

Question: ได้มั้ยยย

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8737206000369042
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0467

Question: จริงหรอออ

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8939682999625802
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0468

Question: โอเคคค

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8524589000735432
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0469

Question: ด่วน!!!

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8395374999381602
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0470

Question: วันนี้เปิดไหม???

### Actual answer
ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_repeat_retype; status: completed; seconds: 0.0011338000185787678
Tags: detector_false_positive, legacy_block_policy_disagreement, normal_input_wrongly_blocked

### Expected contract
```json
{}
```

### Observations
- Extra flags: repeated_character_typo
- Block decision differs from original label; inspect detection vs policy separately.
- Judge errors: ["source_case_unavailable"]

### Next checks
- Review valid Thai combining marks and English names; calibrate thresholds without training on this test set.

## KIA-0471

Question: 555555

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.852117900038138
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0472

Question: เยี่ยมมม

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8663397999480367
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0473

Question: อยากจองงง

### Actual answer
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_reservation_fact; status: completed; seconds: 5.166925099911168
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0474

Question: มีเกมใหม่ไหมมม

### Actual answer
ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_games_catalog; status: completed; seconds: 8.059751200024039
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0475

Question: ราคาน่ารักกก

### Actual answer
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

Mode: pipeline:ambiguity_clarification; status: completed; seconds: 0.07245819992385805
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0476

Question: เล่น VR สนุกมากกก

### Actual answer
อุปกรณ์ใน VR Zone:
PlayStation 5 Zone / VR Zone
•    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone)
VR Zone
•    Sony PlayStation VR2 (1 Unit)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Mode: pipeline:structured_equipment_catalog; status: completed; seconds: 5.799230699893087
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0477

Question: ขอรายละเอียดหน่อยยย

### Actual answer
ขอรายละเอียดเพิ่มเติมเกี่ยวกับหัวข้อใดครับ?
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

Mode: pipeline:general_llm_fallback; status: completed; seconds: 2.098380799870938
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0478

Question: ขอบคุณครับบบบ

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.911072300048545
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0479

Question: ได้เลยยย

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8695849999785423
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0480

Question: ว้าววว

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.8676255000755191
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0481

Question: TEKKEN 8 เล่นที่ไหน

### Actual answer
ตัวแทน PSU Esports Studio - Phuket จำนวน 4 คน เข้าร่วมการแข่งขันเกม Tekken 8 ในรายการ SURAT SMASH TEKKEN 8 ONLINE TOURNAMENT Season 3
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.2325951000675559
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0482

Question: Overcooked! 2 มีไหม

### Actual answer
บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:semantic_rag_dynamic; status: completed; seconds: 0.18987609981559217
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0483

Question: Football Manager เล่นได้หรือเปล่า

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

Mode: pipeline:no_answer; status: completed; seconds: 5.834007499972358
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0484

Question: eFootball 2026 อยู่โซนไหน

### Actual answer
ได้ครับ eFootball เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: pipeline:structured_service_game_availability; status: completed; seconds: 0.32412130013108253
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0485

Question: Call of Duty มีในศูนย์ไหม

### Actual answer
พบเกมที่เกี่ยวข้องกับ Call of Duty ในรายการที่ยืนยันได้ครับ
•    Call of Duty: Modern Warfare III: เล่นได้ที่ PlayStation 5 Zone
•    Call of Duty: Warzone: เล่นได้ที่ PC Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_games_family; status: completed; seconds: 0.4367943999823183
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0486

Question: Assassin's Creed มีหรือเปล่า

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

Mode: pipeline:no_answer; status: completed; seconds: 28.102149799931794
Tags: latency_over_10s, unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0487

Question: Hollow Knight เล่นเครื่องไหน

### Actual answer
[No output returned]

Mode: ; status: worker_crash; seconds: 18.06360820005648
Tags: infrastructure_or_watchdog_failure, latency_over_10s, guard_not_observed, unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- worker_crash
- Judge errors: []

### Next checks
- Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.
- Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0488

Question: Pool game มีในเครื่องหรือไม่

### Actual answer
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Mode: pipeline:structured_equipment_catalog; status: completed; seconds: 8.411189199890941
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0489

Question: กรรมการการแข่งขันติดต่อช่องทางไหน

### Actual answer
ยังไม่มีข้อมูลยืนยันเกี่ยวกับช่องทางการติดต่อกรรมการการแข่งขันใน PSU Esports Studio - Phuket กรุณาสอบถามเพิ่มเติมหรือตรวจสอบแหล่งข้อมูลอื่น ๆ เพื่อความถูกต้องและครบถ้วนครับ

Mode: pipeline:experimental_rag_llm_fallback; status: completed; seconds: 6.997036699904129
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0490

Question: กิจกรรมการแข่งขันเริ่มกี่โมง

### Actual answer
คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ

รายละเอียดที่เกี่ยวข้อง:
•    4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
•    4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
•    4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
•    4.4. เวลาพัก
•    4.4.1.ผู้ตัดสินจะแจ้งให้ผู้เข้าแข่งขันทราบถึงระยะเวลาที่เหลือก่อนที่เกมถัดไปจะเริ่มขึ้น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

Mode: pipeline:rag_direct_curated; status: completed; seconds: 1.8405668998602778
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0491

Question: บรรยากาศของ PSU Esports Studio เป็นอย่างไร

### Actual answer
•    พัฒนาทักษะชีวิต เช่น การสื่อสารและการทำงานเป็นทีม
•    ส่งเสริมการวางแผนและการจัดการสถานการณ์กดดัน
•    มีบรรยากาศสนุกสนานและเต็มไปด้วยความตึงเครียดในเกมแข่งขัน
•    เน้นการเรียนรู้ผ่านประสบการณ์จริงในสนามแข่งขันอีสปอร์ต
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

Mode: pipeline:hybrid_guarded_rerank; status: completed; seconds: 7.315309500088915
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0492

Question: แพ็กเกจธรรมดากับเหมาจ่ายต่างกันอย่างไร

### Actual answer
ตอนนี้ยังตอบคำถามความรู้ทั่วไปไม่ได้ชั่วคราวครับ กรุณาลองใหม่อีกครั้ง
สำหรับข้อมูลของ PSU Esports Studio - Phuket ยังถามเรื่องเกม ปุ่ม อุปกรณ์ ราคา การจอง เวลาเปิด และกติกาได้ตามปกติครับ

Mode: pipeline:general_llm_unavailable; status: completed; seconds: 8.190133500145748
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0493

Question: การแข่งขันมีกรรมการกี่คน

### Actual answer
คำตอบ: 4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้

รายละเอียดที่เกี่ยวข้อง:
•    จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
•    4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
•    4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
•    4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ
•    4. ระเบียบและกติกาการแข่งขัน

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

Mode: pipeline:rag_direct_curated; status: completed; seconds: 0.36467109993100166
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0494

Question: Can I access the booking page?

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 2.1917411000467837
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0495

Question: Is the booking process successful?

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 2.6720481999218464
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0496

Question: Please tell staff about this issue.

### Actual answer
สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน:
Members (7 คน):
•    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี
•    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี
•    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี
•    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ
•    นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์
•    นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์
•    นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ

cooperative education and Internship student (5 คน):
•    นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer
•    Mr. Amine Abidellaoui: Internship Student
•    นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer
•    Mr. Yanis Igoudjil: Internship Student
•    นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer

PSU Phuket Esports Club - PSU Phuket (13 คน):
•    นายษุภากรณ์ จิราจินดากุล: ประธาน
•    นายนพัทธ์ ฝอยทอง: รองประธาน
•    นายปัณณวิชญ์ หนูเรือง: เลขานุการ
•    นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
•    นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
•    นางสาวกมลวรรณ นวลสาย: กรรมการ
•    นางสาวชญาภา จันทร์เอิบ: กรรมการ
•    นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
•    นางสาวสุภาสินี ธนภพ: กรรมการ
•    นางสาวอาทิตยา แดงประดับ: กรรมการ
•    นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
•    นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
•    นายอรรถนนท์ สุขแก้ว: กรรมการ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

Mode: pipeline:structured_members_group_list; status: completed; seconds: 5.389102400047705
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0497

Question: Is football available on PlayStation?

### Actual answer
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

Mode: pipeline:candidate_margin_clarification; status: completed; seconds: 0.13875980000011623
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0498

Question: Does the class pass include equipment?

### Actual answer
•    The Last of Us Part I / Part II pass ไม่มีการระบุว่ามีอุปกรณ์ประกอบการเล่นในข้อมูลที่ให้มา
•    เนื้อหาไม่ได้กล่าวถึงการรวมเครื่องมือหรืออุปกรณ์ใด ๆ ในแพ็กเกจเกม
•    ข้อมูลจาก PSU Esports Studio - Phuket ยืนยันเพียงรายละเอียดการเล่นและแหล่งเล่นเท่านั้น
•    ไม่มีหลักฐานสนับสนุนว่ามีอุปกรณ์ประกอบการเล่นในแพ็กเกจเกมนี้
•    สรุปได้ว่าไม่มีข้อมูลยืนยันว่ามี equipment ใน The Last of Us Part I / Part II pass
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

Mode: pipeline:structured_game_detail; status: completed; seconds: 6.875163000077009
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0499

Question: Can staff access my booking status?

### Actual answer
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

Mode: pipeline:answer_contract_no_answer; status: completed; seconds: 8.061608500080183
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## KIA-0500

Question: Is coffee allowed inside the studio?

### Actual answer
ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

Mode: pipeline:ambiguity_clarification; status: completed; seconds: 0.11127169989049435
Tags: unmapped_answer_needs_manual_review

### Expected contract
```json
{}
```

### Observations
- Judge errors: ["source_case_unavailable"]

### Next checks
- Add independent answer gold; no source case means answer correctness is unscored.

## CP-14

Question: จอง Nebula Fields

### Actual answer
เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

Mode: input_guard_layout_retype; status: completed; seconds: 0.000834000064060092
Tags: faq_guard_block_requires_review

### Expected contract
```json
{
  "expected_mode_prefix": "canonical_clarification",
  "must_contain": [],
  "must_not_contain": []
}
```

### Observations
- เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ
- Judge errors: ["mode_mismatch:input_guard_layout_retype"]

### Next checks
- Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.
