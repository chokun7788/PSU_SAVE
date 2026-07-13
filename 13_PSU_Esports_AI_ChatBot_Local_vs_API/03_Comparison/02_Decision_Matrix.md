# 02 - Decision Matrix: ควรเลือก API หรือ Local

ใช้ไฟล์นี้เป็น checklist ตัดสินใจ

---

## ถามตัวเองก่อน

ให้ตอบ 0-3 คะแนน:

```text
0 = ไม่ใช่เลย
1 = นิดหน่อย
2 = ค่อนข้างใช่
3 = ใช่มาก
```

---

## คะแนนฝั่ง API

| คำถาม | คะแนน |
|---|---:|
| ต้อง deploy ให้ทันภายใน 2 เดือน |  |
| ยังไม่มี GPU ที่พร้อมใช้ |  |
| ทีมยังไม่ถนัด LLM serving |  |
| ต้องการคุณภาพดีเร็ว |  |
| traffic ยังไม่แน่นอน |  |
| อยาก focus ที่ RAG/data/UI |  |
| ต้องการ fallback/provider ง่าย |  |
| ไม่อยากดูแล infra เยอะ |  |

รวม:

```text
API_SCORE = ...
```

---

## คะแนนฝั่ง Local

| คำถาม | คะแนน |
|---|---:|
| มี GPU หรือ budget เช่า GPU |  |
| ต้องการคุมข้อมูลมาก |  |
| คาดว่า traffic สูง |  |
| มีคนดูแล server ได้ |  |
| ยอมรับ latency/quality tuning ได้ |  |
| อยากลด cost ระยะยาวจริงจัง |  |
| มีเวลาทำ benchmark หลายโมเดล |  |
| ต้องการระบบ self-hosted |  |

รวม:

```text
LOCAL_SCORE = ...
```

---

## วิธีอ่านผล

```text
API_SCORE สูงกว่า LOCAL_SCORE มาก:
เริ่มด้วย API

LOCAL_SCORE สูงกว่า API_SCORE มาก:
ทำ Local ได้ แต่ควรมี API fallback

คะแนนใกล้กัน:
ทำ Hybrid
```

---

## Matrix แบบเร็ว

| สถานการณ์ | แนะนำ |
|---|---|
| Deadline สำคัญสุด | API |
| มี GPU อยู่แล้ว | Local + API fallback |
| ไม่รู้จำนวนผู้ใช้ | API ก่อน |
| ผู้ใช้เยอะมากแน่ ๆ | Hybrid หรือ Local |
| ต้องการ demo ที่มั่นใจ | API |
| ต้องการโชว์ AI รันเอง | Local prototype |
| ข้อมูลเป็น public website | API ใช้ได้ |
| ข้อมูลอ่อนไหวมาก | Local หรือ private cloud |

---

## Decision สำหรับ PSU Esports

ถ้าโปรเจกต์นี้เป็นงานภายใน 2 เดือน:

```text
เส้นทางหลัก:
API-based RAG

เส้นทางเสริม:
Local benchmark

เป้าหมายสุดท้าย:
Hybrid
```

---

## เกณฑ์เปลี่ยนจาก API ไป Local

ควรย้ายบางส่วนไป local ถ้า:

- API cost ต่อเดือนสูงเกิน budget
- local model ตอบถูกใกล้เคียง API
- latency local พอรับได้
- มี server ที่ uptime ดี
- มี monitoring แล้ว
- มี API fallback แล้ว

ไม่ควรย้ายถ้า:

- local hallucination สูง
- ตอบไทยไม่ดี
- ต้องใช้เวลารอนานมาก
- ไม่มีคนดูแล server
- ไม่มี eval set

