# ชุดใหญ่ 2,000: ข้อผิดจริงและข้อจำกัดตัวตรวจ

## การตีความผล

รอบแรก legacy 1,941/2,000; source-grade 1,988/2,000. ข้อผิดจริง 12 ข้อเป็น CS2 dispute resolution. อีก 47 ข้อเป็น source-presence false failures. หลังแก้เฉพาะบริบท resolution ทดสอบ 59 ข้อเดิมซ้ำ: ข้อผิดจริงทั้ง 12 ผ่าน legacy; 47 ข้อยังไม่ผ่าน legacy แต่ source-grade ตรวจพบ clause สมบูรณ์. ไม่มีการเขียน Gold ใหม่.

## สาเหตุข้อผิดจริง

`custom_display` เดิมจับคำ Resolution โดยไม่มีบริบท จึงได้ source s45 (brightness/resolution/crosshair) และ confidence ที่ตั้งไว้ 0.97. ผล source เกมเดียวกันและ validation ผ่าน ไม่พอจะบอกว่าตอบประเด็นถูก. แก้โดยตัด collocation dispute/conflict resolution เฉพาะตอนตรวจแนวคิดหน้าจอ แล้วให้เส้นทาง protest_dispute เดิมเลือก s06/s58. ถ้ายังมี screen resolution ในประโยคเดียวกัน จะเก็บ display intent นั้นไว้. ชุดนี้ไม่ได้พิสูจน์การรวมข้อพิพาท+หน้าจอในคำตอบเดียว.

## ข้อผิดจริงทั้ง 12 และคำตอบที่แก้แล้ว

### R24-EN-cs2-089

คำถาม: What do the CS2 tournament rules say about dispute resolution?

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-090

คำถาม: For Counter-Strike 2, can you verify the rule on dispute resolution?

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-091

คำถาม: I am preparing for a Counter Strike 2 match. What is the policy for dispute resolution?

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-092

คำถาม: Please retrieve the official CS2 rulebook evidence for dispute resolution.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-093

คำถาม: How is dispute resolution handled in the Counter-Strike 2 tournament rules?

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-094

คำถาม: Could you cite the Counter Strike 2 rule concerning dispute resolution?

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-207

คำถาม: Please check: What do the CS2 tournament ruls say about dispute resolution? please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-208

คำถาม: Please check: For Counter-Strike 2, can you verify the rule on dispute resolution? please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-209

คำถาม: Please check: I am preparing for a Counter Strike 2 match. What is the policy for dispute resolution? please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-210

คำถาม: Please check: Please retrieve the official CS2 rulebook evidence for dispute resolution. please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-211

คำถาม: Please check: How is dispute resolution handled in the Counter-Strike 2 tournament ruls? please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

### R24-EN-cs2-212

คำถาม: Please check: Could you cite the Counter Strike 2 rule concerning dispute resolution? please.

คำตอบผิด:

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.

คำตอบหลังแก้:

```text
Answer: Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Details:
• Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Source IDs หลังแก้: canonical::competition_rules_cs2_psu_phuket_2026_s06_c01, canonical::competition_rules_cs2_psu_phuket_2026_s58_c01, competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Legacy failures หลังแก้: []

## 47 ข้อที่ตัวตรวจเดิมจับ source ไม่พบ

ตัวตรวจเดิมแบ่งด้วย newline และใช้ fragment ยาว/keyword จำกัด บางคำตอบอังกฤษที่สั้นหรือหลายข้อในย่อหน้าเดียวจึงไม่ถูกนับ. ตัวตรวจ r27 แยก atomic clauses และเอาเลข outline ออกโดยไม่ลบค่าจำนวน จากนั้นตรวจ literal complete-clause presence. เก็บ route/status/target/facet/time/validation gate เดิมทั้งหมด. สิ่งนี้ยืนยันว่ามีข้อความต้นฉบับอยู่ในคำตอบ; ไม่ยืนยันว่าประเด็นที่ผู้ถามต้องการครบทั้งหมด.

| ID | แหล่ง clause ที่ตรวจพบ | Clause ตัวอย่าง |
|---|---|---|
| R24-EN-tekken8-023 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-024 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-025 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-026 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-027 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-028 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-069 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-070 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-071 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-072 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-073 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-074 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-115 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-116 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-117 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-118 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-119 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-120 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-161 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-162 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-163 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-164 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-165 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-166 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-207 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-208 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-209 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-210 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-211 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-tekken8-212 | competition_rules_tekken8_psu_esports_s02_c01 | PlayStation 5 console used |
| R24-EN-valorant-041 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-042 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-043 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-044 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-045 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-107 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-108 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-109 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-110 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-111 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-173 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-174 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-175 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-176 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-177 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-239 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |
| R24-EN-valorant-240 | competition_rules_valorant_psu_phuket_2026_s25_c01 | Warning - For first offenses with low impact. |

## ข้ามวันกับ fixture การจอง

ระหว่างงานวันที่จริงเปลี่ยนเป็น 2 ตุลาคม. CSV fixture ตั้งไว้ 1 ตุลาคม แต่คำถามใช้ “วันนี้” จึงเกิด date mismatch และระบบปฏิเสธยืนยันสถานะอย่างถูกต้อง. Unit Candidate D ล้ม 3 test methods ด้านการจองเพราะ fixture-clock ไม่สอดคล้อง; ไม่มีเหตุให้แก้ runtime ให้ยอมรับวันที่ผิด. Snapshot tests เก็บก่อนแก้ แล้ว freeze now_bangkok เฉพาะ test ให้ตรง 1 ตุลาคม. Candidate E ผ่าน 153/153. ข้อ dispute unit อีก 1 ข้อแก้เลข source assertion จากที่เดา s54/s57 เป็น s58 หลังอ่านต้นฉบับจริง พร้อมตรวจเนื้อหา 15 minutes/captain/coach.

## ขอบเขตผลรวม

ไฟล์ full_r28_corrected_merged_details_v2.jsonl เป็นผลรอบแรก 1,941 ข้อที่ผ่าน กับรอบ retest 59 ข้อ ไม่ได้รันครบ 2,000 รอบสอง. Audit ตรวจว่าทั้ง 12 query ของ CS2 ที่มี collocation ตรงการแก้ถูก retest แล้ว. เก็บผลรอบแรกครบเพื่อเห็นข้อผิดก่อนแก้. ชุดใหม่ 280 และเว็บจริงมีเกณฑ์ครบทุก expected clauses แยกจาก source presence.

การเชื่อม API สำเร็จ/ตอบ HTTP 200 ไม่ใช่การยืนยัน booked/free ของ booking จริง; smoke ด้าน booking ตรวจการเข้าถึงเส้นทางเท่านั้น. Oracle booked/free เป็น fixture อัตโนมัติ ส่วนข้อมูลจริงกับเจ้าของเก็บภายหลังตามคำสั่งผู้ใช้.
