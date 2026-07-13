# 03 - Production Checklist

ใช้ checklist นี้ก่อนเปิดให้ผู้ใช้จริงทดลอง

---

## Data Checklist

- [ ] scrape ข้อมูลล่าสุดแล้ว
- [ ] clean text แล้ว
- [ ] ลบ menu/footer ซ้ำแล้ว
- [ ] แบ่ง chunk แล้ว
- [ ] มี metadata เช่น url/title/category
- [ ] มี curated facts
- [ ] มี manifest บอกวันที่ดึงข้อมูล
- [ ] มีวิธี re-scrape

---

## RAG Checklist

- [ ] embedding สำเร็จทุก chunk
- [ ] vector db persistent
- [ ] search top-k ทำงาน
- [ ] category filter ทำงาน
- [ ] prompt ห้ามเดา
- [ ] citation แสดงได้
- [ ] no-answer behavior ทำงาน
- [ ] ทดสอบคำถามสำคัญแล้ว

---

## API Checklist

- [ ] API key อยู่ใน server เท่านั้น
- [ ] ไม่มี key ใน frontend
- [ ] timeout/retry ตั้งค่าแล้ว
- [ ] fallback provider หรือ fallback answer
- [ ] token usage logging
- [ ] budget guard
- [ ] rate limit

---

## Local Checklist

- [ ] GPU memory เพียงพอ
- [ ] model โหลดหลัง reboot ได้
- [ ] inference server health check ได้
- [ ] concurrent limit ตั้งแล้ว
- [ ] monitoring GPU มี
- [ ] local model ผ่าน eval
- [ ] API fallback มี

---

## Backend Checklist

- [ ] `/health` endpoint
- [ ] `/chat` endpoint
- [ ] `/feedback` endpoint
- [ ] input validation
- [ ] CORS ถูกต้อง
- [ ] structured logs
- [ ] error handling
- [ ] request id

---

## Frontend Checklist

- [ ] ส่งคำถามได้
- [ ] loading state
- [ ] streaming หรือ progress
- [ ] แสดง citation
- [ ] แสดงข้อความเมื่อ error
- [ ] feedback button
- [ ] ใช้งานบนมือถือได้

---

## Security Checklist

- [ ] HTTPS
- [ ] firewall
- [ ] rate limit
- [ ] admin auth
- [ ] secret ไม่อยู่ใน git
- [ ] dependency update
- [ ] log ไม่เก็บข้อมูลส่วนตัวเกินจำเป็น

---

## Monitoring Checklist

- [ ] latency
- [ ] error rate
- [ ] request count
- [ ] token usage
- [ ] cost estimate
- [ ] no-answer rate
- [ ] feedback negative rate
- [ ] GPU usage ถ้า local

---

## Evaluation Checklist

- [ ] testset อย่างน้อย 50-100 ข้อ
- [ ] ครอบคลุม reservation
- [ ] ครอบคลุม services/games
- [ ] ครอบคลุม competition
- [ ] ครอบคลุม no-answer
- [ ] rerun ทุกครั้งที่เปลี่ยน prompt/model/chunking

---

## Launch Checklist

- [ ] backup แล้ว
- [ ] rollback plan
- [ ] domain พร้อม
- [ ] SSL พร้อม
- [ ] monitoring พร้อม
- [ ] budget guard พร้อม
- [ ] มีคนรับผิดชอบดู logs
- [ ] มีแผนอัปเดตข้อมูลเว็บ

