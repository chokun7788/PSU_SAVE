# 04 - GPU และ Server Sizing สำหรับ Local

ไฟล์นี้ช่วยคิดคร่าว ๆ ว่าถ้ารัน LLM เองต้องใช้เครื่องประมาณไหน

หมายเหตุ: ตัวเลขเป็นแนวทาง ไม่ใช่ค่าตายตัว เพราะขึ้นกับ model architecture, quantization, context length, batch size, serving engine และ concurrent users

---

## สิ่งที่กิน VRAM

1. Model weights
2. KV cache
3. batch/concurrent requests
4. context length
5. runtime overhead

---

## ขนาดโมเดลแบบคร่าว ๆ

### 7B-9B

เหมาะกับ:

- ทดลอง
- MVP local
- คำถาม RAG ทั่วไป
- GPU เล็ก/กลาง

ประมาณ:

```text
4-bit quantized:
อาจใช้ VRAM ประมาณ 5-8 GB+

FP16/BF16:
อาจใช้ VRAM ประมาณ 14-20 GB+
```

### 14B

เหมาะกับ:

- คุณภาพดีขึ้น
- ยังพอรันบน GPU เดี่ยวระดับกลาง/สูง

ประมาณ:

```text
4-bit quantized:
อาจใช้ VRAM ประมาณ 10-16 GB+

FP16/BF16:
อาจใช้ VRAM ประมาณ 28-36 GB+
```

### 32B

เหมาะกับ:

- คุณภาพสูงขึ้น
- production local ที่จริงจัง

ประมาณ:

```text
4-bit quantized:
อาจใช้ VRAM ประมาณ 22-30 GB+

FP16/BF16:
อาจใช้ VRAM ประมาณ 64GB+
```

### 70B

เหมาะกับ:

- คุณภาพสูง
- ต้องใช้ GPU ใหญ่หรือ multi-GPU

ประมาณ:

```text
4-bit quantized:
อาจใช้ VRAM ประมาณ 45-55 GB+

FP16/BF16:
อาจใช้ VRAM ประมาณ 140GB+
```

---

## เครื่องที่แนะนำตามระดับ

### ระดับทดลอง

```text
GPU:
8-12 GB VRAM

Model:
7B quantized

Serving:
Ollama หรือ llama.cpp

เหมาะกับ:
demo ส่วนตัว, test retrieval, low traffic
```

### ระดับ MVP local

```text
GPU:
16-24 GB VRAM

Model:
7B-14B quantized

Serving:
Ollama หรือ vLLM

เหมาะกับ:
demo ให้คนใช้กลุ่มเล็ก
```

### ระดับ production เบื้องต้น

```text
GPU:
24-48 GB VRAM

Model:
14B quantized หรือ 7B/14B FP16

Serving:
vLLM/TGI

เหมาะกับ:
ผู้ใช้จริงปานกลาง, latency พอรับได้
```

### ระดับ production จริงจัง

```text
GPU:
48-80 GB VRAM หรือ multi-GPU

Model:
32B หรือ 70B quantized/optimized

Serving:
vLLM/TGI

เหมาะกับ:
traffic สูง, คุณภาพสูง, concurrent users มาก
```

---

## CPU/RAM/Disk

### CPU

ควรมี:

```text
8 cores ขึ้นไปสำหรับ MVP
16 cores ขึ้นไปสำหรับ production
```

### RAM

ควรมี:

```text
32 GB สำหรับ MVP
64 GB+ สำหรับ production
```

### Disk

ควรมี:

```text
SSD/NVMe
100-500 GB ตามจำนวนโมเดลและ logs
```

โมเดลหลายตัวใช้พื้นที่เยอะ ต้องเผื่อ disk

---

## Network

ถ้า server อยู่ cloud:

- latency จากผู้ใช้ถึง server
- bandwidth ตอนโหลดโมเดล
- bandwidth ระหว่าง backend/vector db/LLM

ถ้าทุกอย่างอยู่เครื่องเดียวกัน latency ต่ำกว่า แต่ scale ยากกว่า

---

## Concurrent Users

Local model ต้องคิดเรื่องผู้ใช้พร้อมกัน

ตัวอย่าง:

```text
1-3 คนพร้อมกัน:
Ollama อาจพอ

5-20 คนพร้อมกัน:
ควรใช้ vLLM/TGI และ GPU ที่เหมาะ

20+ คนพร้อมกัน:
ต้อง benchmark, queue, autoscale หรือ API fallback
```

---

## Latency ที่ควรตั้งเป้า

สำหรับ chatbot:

```text
ดี:
ตอบเริ่ม streaming ภายใน 1-3 วินาที

พอรับได้:
คำตอบเสร็จภายใน 5-15 วินาที

เริ่มแย่:
เกิน 20-30 วินาทีบ่อย ๆ
```

ควรเปิด streaming response เพื่อลดความรู้สึกช้า

---

## Sizing Recommendation สำหรับโปรเจกต์นี้

ถ้าต้องทำ local path ใน 2 เดือน:

```text
เริ่ม:
Ollama + 7B/14B quantized บนเครื่องที่มี 16-24GB VRAM

ถ้าคุณภาพผ่าน:
ย้ายไป vLLM/TGI บน GPU server 24GB+

ถ้าคุณภาพไม่ผ่าน:
ใช้ local เฉพาะ FAQ/simple
API ตอบคำถามยาก
```

---

## สิ่งที่ต้องวัดจริง

อย่าตัดสินจาก spec อย่างเดียว ต้องวัด:

- model load time
- first token latency
- tokens/sec
- total response time
- VRAM used
- GPU utilization
- answer correctness
- hallucination
- crash rate
- concurrent users

---

## สูตรคิดแบบง่าย

```text
ถ้า traffic น้อย:
API มักคุ้มกว่า

ถ้า traffic สูงและมี GPU พร้อม:
Local อาจคุ้มกว่า

ถ้าต้องการทั้งคุณภาพและประหยัด:
Hybrid
```

