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
