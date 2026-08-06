# Control Game Source Coverage - 2026-07-29

เอกสารนี้สรุปสถานะข้อมูลปุ่มควบคุมเกมในโฟลเดอร์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\control_game
```

โฟกัสของรอบนี้คือทำให้ chatbot ตอบเกมที่ยังไม่มีข้อมูลได้มากขึ้น พร้อมใส่ลิงก์อ้างอิงที่กดเปิดดูได้จริง โดยไม่เดาปุ่มที่ไม่มีแหล่งยืนยัน

## สรุปที่ทำเพิ่มวันนี้

1. เพิ่มให้ `tools/build_game_control_facts.py` รองรับ `source_url` / `source_urls` จากไฟล์ `.json`
2. เพิ่มให้ builder รองรับ platform ใหม่:
   - `vr`
   - `pc`
3. เพิ่มไฟล์ `.json` และ `.jsonl` สำหรับเกมที่ยังไม่มีข้อมูลปุ่ม/วิธีควบคุมและมีแหล่ง official พอให้ยืนยัน:
   - Beat Saber
   - Horizon Call of the Mountain
   - Ring Fit Adventure
   - Nintendo Switch Sports
   - Mario Party Superstars
   - New Super Mario Bros. U Deluxe
4. เพิ่มไฟล์ `.json` และ `.jsonl` รอบเสริมสำหรับเกมที่ยังขาด control facts จาก catalog:
   - VALORANT
   - Counter-Strike 2
   - PUBG: BATTLEGROUNDS
   - League of Legends
   - Fortnite
4. ตั้ง `coverage_status` เป็น `partial_official` สำหรับเกมที่ official source มีข้อมูลวิธีควบคุม/ชนิด controller แต่ไม่มี full per-button mapping
5. ซ่อม JSONL เดิมของ `TEKKEN 8 Standard Edition.jsonl` ที่มี syntax ผิด 1 บรรทัด
6. แก้ route ที่คำถามกำกวมเรื่องปุ่มไม่มีชื่อเกม ให้ถามกลับพร้อม preview เกมที่มีข้อมูลปุ่มแล้ว
7. แก้ family alias ของ Call of Duty ไม่ให้คำว่า `Call of` ไปชนกับ `Horizon Call of the Mountain`
8. เพิ่ม action-first สำหรับคำถามปุ่มใน family เช่น `ปุ่มกระโดดใน Call of Duty กดอะไร`

## ไฟล์ที่เพิ่มวันนี้

| เกม | ไฟล์ข้อมูล | สถานะ |
|---|---|---|
| Beat Saber | `data/control_game/nintendo/Beat Saber.json` + `.jsonl` | partial official |
| Horizon Call of the Mountain | `data/control_game/nintendo/Horizon Call of the Mountain.json` + `.jsonl` | partial official |
| Ring Fit Adventure | `data/control_game/nintendo/Ring Fit Adventure.json` + `.jsonl` | partial official |
| Nintendo Switch Sports | `data/control_game/nintendo/Nintendo Switch Sports.json` + `.jsonl` | partial official |
| Mario Party Superstars | `data/control_game/nintendo/Mario Party Superstars.json` + `.jsonl` | partial official |
| New Super Mario Bros. U Deluxe | `data/control_game/nintendo/New Super Mario Bros. U Deluxe.json` + `.jsonl` | partial official |

หมายเหตุ: โฟลเดอร์ยังชื่อ `nintendo` ตามโครงสร้างเดิม แต่ภายในมีหลาย platform ปนกันอยู่ เช่น PS5 / VR / Nintendo / PC-ready

## แหล่งอ้างอิงที่ใช้เติมวันนี้

| เกม | ใช้ข้อมูลอะไร | ลิงก์อ้างอิง |
|---|---|---|
| Beat Saber | PS VR2 required, PS VR2 Sense controllers required, VR play style และข้อมูล support ของ Beat Saber | [PlayStation - Beat Saber](https://www.playstation.com/en-us/games/beat-saber/), [Beat Saber FAQ](https://beatsaber.com/faq.html) |
| Horizon Call of the Mountain | Gesture / Analogue control schemes, PS VR2 Sense controllers, grip button / VR interaction | [PlayStation Support - Horizon Call of the Mountain](https://www.playstation.com/en-us/support/games/horizon-call-of-the-mountain/), [PlayStation - Horizon Call of the Mountain](https://www.playstation.com/en-us/games/horizon-call-of-the-mountain/) |
| Ring Fit Adventure | Joy-Con (R) menu navigation, X confirm, A cancel, Ring-Con tilt/press/pull | [Nintendo Support - How Do I Control the Game? Ring Fit Adventure](https://en-americas-support.nintendo.com/app/answers/detail/a_id/47833/~/how-do-i-control-the-game%3F-%28ring-fit-adventure%29), [Nintendo Support - How to Start a New Game](https://en-americas-support.nintendo.com/app/answers/detail/a_id/47820/~/how-to-start-a-new-game-%28ring-fit-adventure%29) |
| Nintendo Switch Sports | Joy-Con/Joy-Con 2 support, Leg Strap mode, X/+ สำหรับ Soccer Leg-Strap Mode | [Nintendo Support - Nintendo Switch Sports FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq), [Nintendo Switch Sports Official Site](https://nintendoswitchsports.nintendo.com/) |
| Mario Party Superstars | button controls, controller styles ที่รองรับ | [Play Nintendo - Mario Party Superstars](https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/), [Mario Party Superstars Minigames](https://mariopartysuperstars.nintendo.com/minigames/) |
| New Super Mario Bros. U Deluxe | one Joy-Con support, simple controls, run/leap/stomp gameplay | [Nintendo SG - New Super Mario Bros. U Deluxe](https://www.nintendo.com/sg/switch/adal/index.html) |
| VALORANT | default PC controls/keybindings จาก secondary guide | [Shacknews - Valorant PC controls and keybindings](https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings), [Riot VALORANT Support](https://support.riotgames.com/valorant) |
| Counter-Strike 2 | standard PC keyboard/mouse bindings จาก secondary guide | [HolyHosting - Counter-Strike 2 Keyboard and Mouse Controls for PC](https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc), [Steam - Counter-Strike 2](https://store.steampowered.com/app/730/CounterStrike_2/) |
| PUBG: BATTLEGROUNDS | common PC controls/keybindings จาก secondary guide | [GameFAQs - PUBG Controls](https://gamefaqs.gamespot.com/pc/206545-playerunknowns-battlegrounds/faqs/76480/controls), [PUBG Official](https://pubg.com/) |
| League of Legends | default ability/camera/self-cast hotkey notes จาก secondary esports guide + Riot hotkey FAQ | [Dignitas - Improving Inputs: Effective Keybinds for LoL](https://dignitas.gg/articles/blogs/Unknown/8721/improving-inputs-effective-keybinds-for-lol), [Riot Support - Hotkeys FAQ](https://support.riotgames.com/id/league-of-legends/performance/hotkeys-keybindings-faq) |
| Fortnite | วิธีดู/แก้ controls และ controller presets จาก Epic official | [Epic Games - Change Fortnite controls](https://www.epicgames.com/help/c-202300000001636/c-202300000001719/how-can-i-change-my-fortnite-controls-on-pc-or-console-a202300000014546), [Epic Games - Configure controller](https://www.epicgames.com/help/c-202300000001636/c-202300000001721/how-to-configure-a-controller-in-fortnite-a202300000017260), [PlayStation - Fortnite](https://www.playstation.com/en-us/fortnite/) |

## Coverage ปัจจุบันหลัง build

ผลจาก `tools/build_game_control_facts.py` และ `tools/audit_game_control_data.py`:

| platform_key | จำนวนเกมที่มี control facts | จำนวน detail rows |
|---|---:|---:|
| ps5 | 20 | 259 |
| nintendo | 12 | 101 |
| vr | 2 | 6 |
| pc | 4 | 58 |

รวม source `.json` ใน `data/control_game/nintendo`: 38 ไฟล์  
รวม curated `game_controls`: 462 rows

## เกมที่ยังขาดข้อมูลปุ่มแบบใช้งานจริง

กลุ่มนี้คือมีเกมอยู่ใน catalog แต่ยังไม่มี control facts ที่ยืนยันและเข้า pipeline ได้ครบ

| เกม | โซน | สถานะตอนนี้ | ต้องเติมอะไร |
|---|---|---|---|
| VALORANT | PC Zone | เพิ่ม control facts แล้ว | ใช้ secondary source ต้อง manual verify จากเครื่องจริงก่อน mark complete |
| Counter-Strike 2 | PC Zone | เพิ่ม control facts แล้ว | ใช้ secondary source ต้อง manual verify จากเครื่องจริงก่อน mark complete |
| PUBG: BATTLEGROUNDS | PC Zone | เพิ่ม control facts แล้ว | ใช้ secondary source ต้อง manual verify จากเครื่องจริงก่อน mark complete |
| League of Legends | PC Zone | เพิ่ม control facts แล้ว | ใช้ secondary source ต้อง manual verify จากเครื่องจริงก่อน mark complete |
| Fortnite | PlayStation 5 Zone | เพิ่ม partial official facts แล้ว | Epic official มีวิธีดู/เปลี่ยน controls แต่ไม่มี full PS5 button mapping |
| Call of Duty: Warzone | PC Zone + PS5 Zone | มี control facts เดิม แต่ source ยังเป็น local | ต้องเพิ่ม external source หรือ manual verified source |
| FINAL FANTASY XVI | PS5 Zone | มีไฟล์เดิม แต่ควรตรวจซ้ำ | ไฟล์ `.json` เดิมมีสัญญาณว่าข้อมูลอาจเป็น FINAL FANTASY XV ไม่ใช่ XVI |

## เกมที่มีข้อมูลแล้วแต่ยังควร source audit เพิ่ม

ไฟล์เดิมจำนวนมากมี `source_url` เป็น `local://control_game/...` เพราะก่อนหน้านี้ builder ยังไม่รองรับลิงก์เว็บจริงจากไฟล์ `.json`

กลุ่มนี้ควรไล่เพิ่มแหล่งอ้างอิงจริงทีละเกม:

| กลุ่ม | ตัวอย่างเกม |
|---|---|
| PS5 action/adventure | God of War Ragnarok, Marvel's Spider-Man 2, Hogwarts Legacy, Resident Evil 4, Resident Evil Village, The Last of Us Part I, The Last of Us Part II, Uncharted |
| PS5 racing/sport/fighting | Gran Turismo 7, EA Sports FC 24, TEKKEN 8 |
| Nintendo | Animal Crossing, Luigi's Mansion 3, Mario Kart 8 Deluxe, Mario Kart Live, Monster Hunter Rise, Overcooked 2, Super Mario Odyssey, Super Smash Bros Ultimate, Zelda BOTW, Little Nightmares II |

## ปัญหาชื่อไฟล์/ชื่อเกมที่ควรแก้รอบถัดไป

| จุด | ปัญหา | ผลกระทบ |
|---|---|---|
| `It_Take_Two.json` | ชื่อไฟล์สะกดไม่ตรงกับชื่อเกม `It Takes Two` | อาจทำให้ audit เทียบชื่อกับ catalog สับสน |
| `Movine_Out_2.json` | ชื่อไฟล์สะกดผิด แต่ builder override เป็น `Moving Out 2` แล้ว | ยังควร rename ไฟล์ภายหลังเพื่อให้อ่านง่าย |
| `Overcooked + Overcooked! 2.json` | internal `game_name` เดิมเป็น `Overcooked!` แต่ builder override เป็น `Overcooked 2` แล้ว | ยังควรแยก/ยืนยันภาคและ platform ให้ชัดภายหลัง |
| `The Last of Us Part I / Part II` | เป็นชื่อรวมใน catalog แต่ control facts แยกเป็น Part I และ Part II | ระบบตอบแบบสรุปแยกภาคแล้ว ถ้าต้องการปุ่มละเอียดให้ user ระบุภาค |
| `Naruto X Boruto Ultimate Ninja Storm Connections.json.jsonl` | นามสกุลซ้อน `.json.jsonl` | อ่านยากและเสี่ยงเข้าใจผิดว่าเป็น JSON |
| `FINAL FANTASY XVI.json` | internal `game_name` และเนื้อหาควบคุมเดิมดูเหมือน FFXV | เสี่ยงตอบปุ่มผิดเกม ต้องตรวจจาก source ใหม่ก่อนใช้จริง |

## แนวทางเติม PC controls แบบไม่เดา

1. ใช้แหล่ง official ก่อนเสมอ
2. ถ้า official ไม่มีตาราง default keybind:
   - ใช้เครื่องจริงเปิดเกมแล้ว export/screenshot settings
   - หรือใช้แหล่งรองที่เชื่อถือได้ แล้วตั้ง `coverage_status` เป็น `secondary_needs_manual_verify`
3. สำหรับเกมที่ปรับ keybind ได้เยอะ เช่น VALORANT / Fortnite / CS2:
   - ควรเก็บ `preset_name`
   - ควรเก็บ `verified_on`
   - ควรเก็บ `verified_by`
   - ควรแยก `default_controls` กับ `studio_custom_controls`
4. ถ้าไม่มีหลักฐานพอ ให้ chatbot ตอบว่า “ยังไม่มีข้อมูลปุ่มที่ยืนยันได้” พร้อมบอกว่ามีเกมนี้ใน catalog แทน

## รูปแบบ source ที่ควรใช้ต่อจากนี้

ในไฟล์ `.json` ควรใส่:

```json
{
  "game_controls": {
    "game_name": "Example Game",
    "platform": "PC",
    "source_url": "https://example.com/official-controls",
    "source_urls": [
      "https://example.com/official-controls",
      "https://example.com/support-page"
    ],
    "coverage_status": "complete_official",
    "note": "อธิบายข้อจำกัดของข้อมูล",
    "button_mappings": []
  }
}
```

ค่า `coverage_status` ที่แนะนำ:

| ค่า | ใช้เมื่อ |
|---|---|
| `complete_official` | แหล่ง official ให้ full mapping |
| `partial_official` | แหล่ง official ให้ข้อมูลบางส่วน เช่น controller type / control scheme |
| `secondary_needs_manual_verify` | ใช้แหล่งรองและต้องให้คนตรวจอีกครั้ง |
| `manual_verified` | ตรวจจากเครื่องจริงของ studio แล้ว |
| `needs_source` | มีข้อมูลแต่ยังไม่มีแหล่งอ้างอิงที่กดดูได้ |

## Verification ล่าสุด

ผ่าน:

```text
python tools/validate_game_controls.py
```

ผลสำคัญ:

```text
GAME CONTROL VALIDATION OK
JSONL OK
```
