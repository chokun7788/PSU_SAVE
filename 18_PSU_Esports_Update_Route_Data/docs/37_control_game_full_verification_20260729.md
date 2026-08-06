# สถานะตรวจครบข้อมูลปุ่มเกม ณ วันที่ 2026-07-29

## สรุปสั้น

เช็คจริงแล้ว: เกมใน catalog หลักครบ 36/36 เกมในแง่ที่ระบบมีข้อมูลปุ่มและ route ตอบได้ครบทุกเกมแล้ว

แต่ยังไม่ใช่ “ถูกต้องยืนยัน 100% ทุกปุ่มจาก official source” เพราะยังมี 26 เกมที่ source เป็น `local://control_game/...` และมี 5 เกมที่ใช้ secondary source จึงควรให้คนเปิดเครื่องจริงหรือหา official manual เพิ่มก่อน mark เป็น complete

## สิ่งที่ตรวจในรอบนี้

1. เทียบ `data/curated/game_item_details.jsonl` กับ `data/curated/game_control_facts.jsonl`
2. Rebuild control facts, split files, vector index และ audit ด้วย `python tools/validate_game_controls.py`
3. ยิงคำถามจริงแบบ batch ทุกเกมใน catalog ด้วยรูปแบบ `{ชื่อเกม} ปุ่มทั้งหมดมีอะไรบ้าง`
4. ยิง regression case ที่เคยพัง เช่น `call of เล่นยังไง`, `mario kart liveเล่นยังไง`, `Resident Evil 4 ปุ่มยิงกดอะไร`, `God of War Ragnarok ปุ่มโจมตีกดอะไร`
5. ตรวจ source URL ที่เป็นเว็บภายนอกว่ากด/เปิดได้ระดับ HTTP
6. ตรวจ semantic spot-check แล้วเจอว่า `FINAL FANTASY XVI.json` เดิมเป็นข้อมูลของ `FINAL FANTASY XV` จึงแก้เป็น FFXVI Type A controls ใหม่

## ผลตรวจหลังแก้

| รายการ | ผล |
|---|---:|
| เกมใน catalog หลัก | 36 |
| เกมใน control facts | 38 |
| source `.json` ใน `data/control_game` | 38 |
| curated game control rows | 465 |
| เกมใน catalog ที่ batch query ผ่าน structured controls | 36/36 |
| เกมใน catalog ที่ยัง no-data หลังแก้ | 0 |
| เกมที่มี external URL ใน source | 12 |
| เกมที่ยัง local-only source | 26 |

หมายเหตุ: control facts มี 38 ชื่อ เพราะบางรายการแยกละเอียดกว่า catalog เช่น `The Last of Us Part I` และ `The Last of Us Part II` แยกไฟล์กัน ส่วน `Mario Kart Live: Home Circuit` มีข้อมูลปุ่มเป็น control-only แต่ไม่ได้อยู่ใน catalog หลักแบบชื่อแยก

## Canonical name mapping ที่ต้องรู้

ชื่อใน catalog กับชื่อใน control facts บางเกมไม่ตรงกันแบบตัวอักษร แต่เป็นเกมเดียวกัน ระบบแก้ lookup ให้ map ได้แล้ว

| ชื่อใน catalog | ชื่อใน control facts |
|---|---|
| God of War Ragnarok | God of War Ragnarök |
| NARUTO X BORUTO Ultimate Ninja Storm Connections | NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS |
| Resident Evil 4 | Resident Evil 4 (Remake) |
| Super Smash Bros Ultimate | Super Smash Bros. Ultimate |
| The Last of Us Part I / Part II | The Last of Us Part I + The Last of Us Part II |

## ผล batch query ทุกเกมใน catalog

ทุกเกมด้านล่างตอบด้วย `pipeline:structured_game_controls` ยกเว้น The Last of Us รายการรวมที่ตอบด้วย `pipeline:structured_game_controls_family_summary`

| เกม | สถานะ route |
|---|---|
| Animal Crossing: New Horizons | ผ่าน structured controls |
| Beat Saber | ผ่าน structured controls |
| Call of Duty: Modern Warfare III | ผ่าน structured controls |
| Call of Duty: Warzone | ผ่าน structured controls |
| Counter-Strike 2 | ผ่าน structured controls |
| EA Sports FC 24 | ผ่าน structured controls |
| FINAL FANTASY XVI | ผ่าน structured controls |
| Fortnite | ผ่าน structured controls |
| God of War Ragnarok | ผ่าน structured controls |
| Gran Turismo 7 | ผ่าน structured controls |
| Hogwarts Legacy | ผ่าน structured controls |
| Horizon Call of the Mountain | ผ่าน structured controls |
| It Takes Two | ผ่าน structured controls |
| League of Legends | ผ่าน structured controls |
| Little Nightmares II | ผ่าน structured controls |
| Luigi's Mansion 3 | ผ่าน structured controls |
| Mario Kart 8 Deluxe | ผ่าน structured controls |
| Mario Party Superstars | ผ่าน structured controls |
| Marvel's Spider-Man 2 | ผ่าน structured controls |
| Monster Hunter Rise | ผ่าน structured controls |
| Moving Out 2 | ผ่าน structured controls |
| NARUTO X BORUTO Ultimate Ninja Storm Connections | ผ่าน structured controls |
| New Super Mario Bros. U Deluxe | ผ่าน structured controls |
| Nintendo Switch Sports | ผ่าน structured controls |
| Overcooked 2 | ผ่าน structured controls |
| PUBG: BATTLEGROUNDS | ผ่าน structured controls |
| Resident Evil 4 | ผ่าน structured controls |
| Resident Evil Village | ผ่าน structured controls |
| Ring Fit Adventure | ผ่าน structured controls |
| Super Mario Odyssey | ผ่าน structured controls |
| Super Smash Bros Ultimate | ผ่าน structured controls |
| TEKKEN 8 | ผ่าน structured controls |
| The Last of Us Part I / Part II | ผ่าน family summary |
| The Legend of Zelda: Breath of the Wild | ผ่าน structured controls |
| Uncharted: Legacy of Thieves Collection | ผ่าน structured controls |
| VALORANT | ผ่าน structured controls |

## เกมที่มี external source URL แล้ว

| เกม | coverage_status | source |
|---|---|---|
| Beat Saber | partial_official | https://www.playstation.com/en-us/games/beat-saber/ |
| Counter-Strike 2 | secondary_needs_manual_verify | https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc |
| FINAL FANTASY XVI | secondary_needs_manual_verify | https://gamewith.net/final-fantasy-16/article/show/39644 |
| Fortnite | partial_official | https://www.epicgames.com/help/c-202300000001636/c-202300000001719/how-can-i-change-my-fortnite-controls-on-pc-or-console-a202300000014546 |
| Horizon Call of the Mountain | partial_official | https://www.playstation.com/en-us/support/games/horizon-call-of-the-mountain/ |
| League of Legends | secondary_needs_manual_verify | https://dignitas.gg/articles/blogs/Unknown/8721/improving-inputs-effective-keybinds-for-lol |
| Mario Party Superstars | partial_official | https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/ |
| New Super Mario Bros. U Deluxe | partial_official | https://www.nintendo.com/sg/switch/adal/index.html |
| Nintendo Switch Sports | partial_official | https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq |
| PUBG: BATTLEGROUNDS | secondary_needs_manual_verify | https://gamefaqs.gamespot.com/pc/206545-playerunknowns-battlegrounds/faqs/76480/controls |
| Ring Fit Adventure | partial_official | https://en-americas-support.nintendo.com/app/answers/detail/a_id/47833/~/how-do-i-control-the-game%3F-%28ring-fit-adventure%29 |
| VALORANT | secondary_needs_manual_verify | https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings |

HTTP check: 10 URL ได้ status 200, ส่วน Epic Fortnite และ GameFAQs PUBG ได้ 403 จากสคริปต์ HTTP เพราะเว็บบล็อก bot/request บางแบบ ไม่ได้แปลว่าลิงก์เสียทันที

## เกมที่ยัง local-only source

กลุ่มนี้ระบบตอบได้แล้ว แต่ source ยังเป็นไฟล์ภายใน ไม่ใช่ลิงก์เว็บที่ผู้ใช้กดดูได้

1. Animal Crossing: New Horizons
2. Call of Duty: Modern Warfare III
3. Call of Duty: Warzone
4. EA Sports FC 24
5. God of War Ragnarök
6. Gran Turismo 7
7. Hogwarts Legacy
8. It Takes Two
9. Little Nightmares II
10. Luigi's Mansion 3
11. Mario Kart 8 Deluxe
12. Mario Kart Live: Home Circuit
13. Marvel's Spider-Man 2
14. Monster Hunter Rise
15. Moving Out 2
16. NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS
17. Overcooked 2
18. Resident Evil 4 (Remake)
19. Resident Evil Village
20. Super Mario Odyssey
21. Super Smash Bros. Ultimate
22. TEKKEN 8
23. The Last of Us Part I
24. The Last of Us Part II
25. The Legend of Zelda: Breath of the Wild
26. Uncharted: Legacy of Thieves Collection

## จุดที่แก้ในรอบตรวจนี้

1. แก้ `FINAL FANTASY XVI.json` จากข้อมูลผิดเกม
   - เดิมมีสัญญาณว่าเป็น FFXV เช่น Noctis, Regalia, Warp
   - ใหม่เป็น FFXVI Type A controls เช่น Square = sword/melee attack, Triangle = magic attack, Circle = Eikonic Feat, R1 = evade, L2 = switch Eikons
   - ใช้ source หลักจาก GameWith และ cross-check กับ Jegged

2. แก้ canonical lookup ใน structured controls
   - ใช้ key แบบเดียวกันตอน match เกมกับ control rows
   - รองรับ accent เช่น `Ragnarök` กับ `Ragnarok`
   - รองรับชื่อที่มี `(Remake)` เช่น `Resident Evil 4` กับ `Resident Evil 4 (Remake)`

3. แก้ fast path control lookup
   - ทำให้ game detail/how-to ที่ include controls ดึงปุ่มจากชื่อ canonical ได้เหมือน structured path

## Regression case ที่เช็คแล้ว

| คำถาม | ผลหลังแก้ |
|---|---|
| `FINAL FANTASY XVI ปุ่มโจมตีกดอะไร` | ตอบ Square/Triangle ของ FFXVI ไม่ใช่ FFXV |
| `call of เล่นยังไง` | ไม่หลุดไป Naruto แล้ว |
| `mario kart liveเล่นยังไง` | ตอบข้อมูลปุ่ม Mario Kart Live |
| `Mario Kart Live ปุ่มเร่งเครื่องกดอะไร` | ตอบ A = เร่งเครื่อง |
| `Resident Evil 4 ปุ่มยิงกดอะไร` | ตอบปุ่มจาก Resident Evil 4 (Remake) ได้ |
| `God of War Ragnarok ปุ่มโจมตีกดอะไร` | ตอบ R1/R2/Square ได้ |
| `NARUTO X BORUTO Ultimate Ninja Storm Connections ปุ่มโจมตีกดอะไร` | ตอบ Naruto ได้ถูกเกม |
| `Super Smash Bros Ultimate ปุ่มกระโดดกดอะไร` | ตอบ X/Y = กระโดด |

## ข้อสรุปเรื่อง “ครบไหม”

ครบในเชิงระบบตอบ: ใช่ ครบ 36/36 เกมใน catalog หลัก

ครบในเชิง source/correctness ระดับ production: ยังไม่ครบ เพราะ local-only ยังเยอะ และบางเกมใช้ secondary source

## สิ่งที่ควรทำต่อ

1. ไล่เติม external source ให้ 26 เกม local-only
2. แยก `default_controls` กับ `studio_custom_controls` โดยเฉพาะ PC games ที่ผู้ใช้เปลี่ยน keybind ได้ง่าย
3. เพิ่ม field `verified_on`, `verified_by`, `verified_device`, `coverage_status`
4. ทำ manual verification รอบสุดท้ายจากเครื่องจริงใน Studio ก่อนเปิดใช้งาน production
5. ทำ test เพิ่มสำหรับ canonical name mismatch เช่น Ragnarok/Ragnarök, Resident Evil 4/(Remake), Smash มีจุด/ไม่มีจุด
