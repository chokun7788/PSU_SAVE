# Web API Smoke Test

Generated: 2026-07-04T19:16:56
JSONL: `reports\web_api_smoke_equipment_update_20260704.jsonl`

## 1. Sony PlayStation VR2 คืออะไร

- mode: `pipeline:equipment_item_fast_path`
- route: `equipment/equipment_item_lookup`
- latency: `0.0098`

Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone

## 2. Logitech G923 คืออะไร

- mode: `pipeline:equipment_item_fast_path`
- route: `equipment/equipment_item_lookup`
- latency: `0.0072`

Logitech G923 TRUEFORCE Racing Wheel: ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone

## 3. เล่น Minecraft ได้ไหม

- mode: `pipeline:games_unknown_fast_path`
- route: `games/game_availability_lookup`
- latency: `0.0094`

ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ

## 4. VR Zone คืออะไร

- mode: `pipeline:equipment_zone_fast_path`
- route: `equipment/zone_equipment_lookup`
- latency: `0.0072`

VR Zone คือโซนเล่นเกม VR โดยใช้ PlayStation VR2 เหมาะกับประสบการณ์เกมเสมือนจริง
