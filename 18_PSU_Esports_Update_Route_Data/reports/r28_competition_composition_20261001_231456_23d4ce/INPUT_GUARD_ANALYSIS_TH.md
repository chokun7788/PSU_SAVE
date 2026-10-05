# วิเคราะห์ input guard และเว็บจริง r28

## ข้อผิดจริงที่พบเฉพาะเว็บ

คำถามอังกฤษ 3 แบบเรื่องนำอุปกรณ์มาและรับผิดชอบคุณภาพถูกหยุดก่อน routing. ตัวกรองเดิมไม่รู้จัก `its` ซึ่งเป็นสรรพนามอังกฤษ จึงแปลงสมมติฐานเป็น “ระห” แล้วพบใน corpus ไทย: source_quality 0.499681, target_quality 0.601378, target_seen=True. สูตรให้ score ของ span 0.525159 และ score รวม 0.52728 ซึ่งเกิน threshold 0.39. สิ่งนี้ไม่ใช่หลักฐานว่าประโยคอังกฤษเป็นภาษาแป้นผิด แต่ระบบเดิมยอมให้ span เดียวตัดสินทั้งประโยค.

## สิ่งที่แก้และเหตุผล

เพิ่ม closed-class English pronouns/คำหน้าที่ลงใน language prior เดิม. นี่คือคำจริงที่ไม่ควรตีเป็น wrong-layout ไม่มี mapping typo ไปยังคำตอบหรือ alias ของทั้งประโยค. คำว่า its ได้รับ lexical protection; ไม่ปิด guard และไม่เปลี่ยน threshold. Profile ID รวม prior แล้ว เพราะ prior มีผลต่อโมเดล. ชุดคำศัพท์เพิ่มเติม: both, each, either, every, he, her, herself, him, himself, it, its, itself, neither, nor, not, our, ours, ourselves, she, their, theirs, them, themselves, they, us, we, who, whom, whose, why, you, your, yours, yourself, yourselves

ตรวจ guard ก่อน/หลังกับ 4283 ข้อ: ถูกหยุดก่อน 41, หลัง 38; ปลดการหยุด 3 และเพิ่มการหยุด 0. การตรวจนี้ไม่ใช่การตรวจคำตอบหรือการแปลครบทั้ง 4,283 ข้อ.

## ข้อความผิดแป้นที่ใช้ตรวจ

`g]jo` และ “อยากถามว่า g]jo ได้ไหม” ถูกหยุดทั้งก่อนและหลัง. `l;ylfu` ไม่ถูกหยุดทั้งก่อนและหลัง: score ประมาณ 0.245 ต่ำกว่า 0.39. จึงเอาออกจาก unit ที่เพิ่งเพิ่มซึ่งเดิมสมมติว่าควรถูกหยุด; เก็บ diagnostic ใน audit ให้เห็น ไม่ปรับ threshold ตามข้อนี้ และไม่ได้ทดสอบ end-to-end ของคำทักทายนี้ในรอบนี้. ไม่อ้างว่าตรวจ wrong-layout ได้ทุกกรณี.

## สถานะระบบไม่ว่างระหว่างทดสอบ

final_http280 รอบแรกได้ HTTP 503 สองคำขอแรกเพราะสอง test clients รันพร้อมกันกับคำถาม clarification ที่ใช้เวลาประมาณ 11 วินาที ขณะ backend รับงานทีละคำถามและ queue รอ 3 วินาที. เป็นข้อผิดของวิธีรันทดสอบกับการจำกัด concurrency ที่มีอยู่; เก็บผลเดิมทั้งหมด ไม่แก้ worker ให้ปล่อยงานชนกัน. ชุด verified รันทีละชุดและรายงาน transport แยกจากความถูกของเนื้อหา. ข้อจำกัดผู้ใช้พร้อมกันหลายคนยังมีอยู่ และ retry UI ต้องใช้ retryable/server_busy ตามที่ระบบส่งกลับ.

## สิ่งที่ยังต้องตรวจต่อจากชุดเก่า

เหลือข้อความ 36 ข้อจากชุด multi-error r15 ที่ guard ยังหยุดเหมือนก่อนแก้. ต้องอ่านความหมายกับ mutation ก่อนตัดสินว่า false rejection หรือ input เสียจริง; รอบนี้ไม่ได้ให้คะแนนคำตอบของ 36 ข้อนี้. ลำดับถัดไปควรตรวจ layout_span/source_quality/target_quality/target_seen และบริบทประโยค เพื่อลดการตัดสินทั้งประโยคจาก span เดียวโดยคง wrong-layout controls. ด้านล่างคือรายการจริงที่ยังถูกหยุด (ตัด negative controls ที่ตั้งใจให้หยุดออก).

| ID | ข้อความ | Score | เหตุผล |
|---|---|---|
| MASTER-GT-TH-00190 | PSU Student เลน Cockpit 30 นาที เสียกร่บาท | 0.550655 | Thai-key span maps to English quality=0.895, gain=0.157, known=False |
| MASTER-GT-TH-04581 | รศ.ดร.พันธ์ ทงชุมนุม ทำตำแหน่งอะไร | 0.580085 | Thai-key span maps to English quality=0.913, gain=0.191, known=False |
| MASTER-GT-TH-02939 | ใเนกม Little Nightmares II บน PlayStation / PS5 ปุ่ม Options ใช้ทำอะไร | 0.873168 | Thai-key span maps to English quality=0.938, gain=0.604, known=True |
| MASTER-GT-TH-03031 | ในเกม TEKKEN 8 บน PlayStation / PS5 ปุม R1 ใช้ทำอะไร | 0.63242 | Thai-key span maps to English quality=0.935, gain=0.430, known=False |
| MASTER-GT-TH-03705 | ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลเร่องนำอุปกรณ์ แผ่นเกม คืน | 0.72898 | Thai-key span maps to English quality=0.920, gain=0.006, known=True |
| MASTER-GT-TH-04811 | ขอขอ้มูลที่ยืนยันได้หน่อยครับ: ะ้ฟะ รน ะฟ ไำืะ | 0.900619 | Thai-key span maps to English quality=0.928, gain=0.749, known=True |
| MASTER-GT-TH-04807 | ขอข้อมูลทีายืนยันได้น่อยครับ: g]jo | 0.896031 | English-key span maps to Thai quality=0.966, gain=0.713, seen=True |
| MASTER-GT-TH-02677 | ในเกม Mario Kart 8 Deluxe บน Nintendo Switch ปุม L (Left Stick) ใช้ทำแะไร | 0.630979 | Thai-key span maps to English quality=0.935, gain=0.430, known=False |
| MASTER-GT-TH-04810 | ะ้ฟะ รน ฟ ไำืพ | 0.919407 | Thai-key span maps to English quality=0.928, gain=0.749, known=True |
| MASTER-GT-TH-04809 | g]jo อ | 0.943546 | English-key span maps to Thai quality=0.966, gain=0.713, seen=True |
| MASTER-GT-TH-04382 | ขอสอบถามหน่อยครับ คาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางและเวลาแข่งขัน ต้องทำยังไง | 0.636023 | Thai-key span maps to English quality=0.939, gain=0.447, known=False |
| MASTER-GT-TH-01219 | ตอนนีเ VR Station ว่างไหม ครบ | 0.789585 | Thai-key span maps to English quality=0.941, gain=0.204, known=True |
| MASTER-GT-TH-04507 | ผศ.ดร.ณัฐพงศ์ ทองเทพ ทีตำแหน่งอะไ | 0.5734 | Thai-key span maps to English quality=0.913, gain=0.042, known=True |
| MASTER-GT-TH-04585 | ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร | 0.5734 | Thai-key span maps to English quality=0.913, gain=0.042, known=True |
| MASTER-GT-TH-03683 | ขอสอบถามหน่อยคนับ ขอข้อมูลเรื่องนำอุปกรณ์ แผ่นเกม คืน | 0.729998 | Thai-key span maps to English quality=0.920, gain=0.006, known=True |
| MASTER-GT-TH-03100 | ปุมควบคุมของ Super Mario Odyssey บน Nintendo Switch มีอะไรบ้่ง | 0.56206 | Thai-key span maps to English quality=0.919, gain=0.105, known=False |
| MASTER-GT-EN-00284 | How much does it csot for a general visitor to play VR for 1 hour or 2 hours | 0.435759 | English-key span maps to Thai quality=0.670, gain=0.222, seen=False |
| MASTER-GT-EN-02059 | Could you please helo me wih this: Where can you play League of Legends | 0.587875 | English-key span maps to Thai quality=0.647, gain=0.252, seen=True |
| MASTER-GT-EN-00493 | How do I bok a cockpit | 0.409658 | English-key span maps to Thai quality=0.438, gain=0.000, seen=True |
| MASTER-GT-EN-04855 | Culd you check this using verified information: ะ้ฟะ รน ะฟ ไำืะ | 0.899235 | Thai-key span maps to English quality=0.928, gain=0.749, known=True |
| MASTER-GT-EN-00205 | Slumni play Nintendo Switch for one hour. How much des it cost | 0.501942 | English-key span maps to Thai quality=0.593, gain=0.000, seen=True |
| MASTER-GT-EN-00871 | Could you check this usin verified information: Is PC 2 available right niw | 0.430661 | English-key span maps to Thai quality=0.467, gain=0.000, seen=True |
| MASTER-GT-EN-01933 | What do you need to ook to play Beat Saber | 0.44142 | English-key span maps to Thai quality=0.483, gain=0.000, seen=True |
| MASTER-GT-EN-03708 | Could you check this usin verified information: May I record video inside the studio | 0.430161 | English-key span maps to Thai quality=0.467, gain=0.000, seen=True |
| MASTER-GT-EN-00110 | How muc does it xost for a PSU student to play VR for 1 hour | 0.408024 | English-key span maps to Thai quality=0.435, gain=0.000, seen=True |
| MASTER-GT-EN-04950 | How much does it cot for a PSU stydent to play Nintendo Switch for 2 hours, and how do I book | 0.500606 | English-key span maps to Thai quality=0.568, gain=0.063, seen=True |
| MASTER-GT-EN-03825 | Please answer fom verified studio information: May I record video inside the studio | 0.496099 | English-key span maps to Thai quality=0.559, gain=0.065, seen=True |
| MASTER-GT-EN-01849 | What do you need to bok to play Uncharted | 0.409658 | English-key span maps to Thai quality=0.438, gain=0.000, seen=True |
| MASTER-GT-EN-00661 | Please answer fom verified studio information: Can I get a refund? I need the official answer | 0.495833 | English-key span maps to Thai quality=0.559, gain=0.065, seen=True |
| MASTER-GT-EN-00088 | Hoq much des a Nintendo Switch cost | 0.505065 | English-key span maps to Thai quality=0.593, gain=0.000, seen=True |
| MASTER-GT-EN-04905 | Wht's the current hit song | 0.408932 | English-key span maps to Thai quality=0.437, gain=0.000, seen=True |
| MASTER-GT-EN-04501 | Whay is ผศ.ดร.นิวัติ แก้วประดับ's roe | 0.573126 | Thai-key span maps to English quality=0.913, gain=0.042, known=True |
| MASTER-GT-EN-03056 | What des the D-Pad (Up / Down / Left / Right) buttom do in The Last of Us Part I on PlayStation / PS5 | 0.500516 | English-key span maps to Thai quality=0.593, gain=0.000, seen=True |
| MASTER-GT-EN-01841 | What do you need to ook to play The Last of Us Part I | 0.440306 | English-key span maps to Thai quality=0.483, gain=0.000, seen=True |
| MASTER-GT-EN-00397 | Could you please help me wih this: A general visitor plays Cockpit for 2 hours. How much does it cost | 0.586815 | English-key span maps to Thai quality=0.647, gain=0.252, seen=True |
| MASTER-GT-EN-04652 | Could you please help me with thi: What is ผศ.ดร.นิวัติ แก้วประดับ's role | 0.571142 | Thai-key span maps to English quality=0.913, gain=0.042, known=True |
