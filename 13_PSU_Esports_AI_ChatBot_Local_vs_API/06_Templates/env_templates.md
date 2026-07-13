# Environment Templates

ไฟล์นี้เป็นตัวอย่าง `.env` สำหรับ API, Local และ Hybrid

ห้าม commit `.env` จริงขึ้น Git

---

## API `.env`

```env
APP_ENV=development
APP_NAME=psu-esports-chatbot

FRONTEND_ORIGIN=http://localhost:3000

LLM_PROVIDER=openai
LLM_MODEL=latest-mini-model
LLM_TEMPERATURE=0.2
LLM_MAX_OUTPUT_TOKENS=800
LLM_TIMEOUT_SECONDS=30

OPENAI_API_KEY=replace_me
GEMINI_API_KEY=replace_me
ANTHROPIC_API_KEY=replace_me
TYPHOON_API_KEY=replace_me

EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=latest-small-embedding-model

VECTOR_DB=chroma
CHROMA_PATH=./data/chroma
QDRANT_URL=http://localhost:6333

TOP_K=8
MAX_CONTEXT_TOKENS=6000

DATABASE_URL=sqlite:///./logs/app.db

RATE_LIMIT_PER_MINUTE=20
ENABLE_CACHE=true
ENABLE_CITATIONS=true
```

---

## Local `.env`

```env
APP_ENV=development
APP_NAME=psu-esports-chatbot-local

LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=qwen-or-llama-model
LLM_TEMPERATURE=0.2
LLM_MAX_OUTPUT_TOKENS=800
LLM_TIMEOUT_SECONDS=60

EMBEDDING_PROVIDER=local
LOCAL_EMBEDDING_MODEL=BAAI/bge-m3

VECTOR_DB=chroma
CHROMA_PATH=./data/chroma

TOP_K=8
MAX_CONTEXT_TOKENS=5000
MAX_CONCURRENT_REQUESTS=2

DATABASE_URL=sqlite:///./logs/app.db

ENABLE_CACHE=true
ENABLE_CITATIONS=true
ENABLE_API_FALLBACK=false
```

---

## Hybrid `.env`

```env
APP_ENV=production
APP_NAME=psu-esports-chatbot-hybrid

ROUTING_MODE=hybrid

LOCAL_LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://ollama:11434
LOCAL_LLM_MODEL=qwen-or-llama-model

API_LLM_PROVIDER=openai
API_LLM_MODEL=latest-mini-model
OPENAI_API_KEY=replace_me

EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=latest-small-embedding-model

VECTOR_DB=qdrant
QDRANT_URL=http://qdrant:6333

USE_CURATED_FACTS_FIRST=true
USE_CACHE=true
USE_LOCAL_FOR_SIMPLE=true
USE_API_FOR_HARD=true
ENABLE_API_FALLBACK=true

TOP_K=8
MAX_CONTEXT_TOKENS=6000
LOCAL_TIMEOUT_SECONDS=30
API_TIMEOUT_SECONDS=30

DAILY_COST_LIMIT_USD=5
RATE_LIMIT_PER_MINUTE=20
```

---

## Production Secrets

ควรเก็บใน:

- cloud secret manager
- Docker secrets
- environment variables ของ platform
- `.env` บน server ที่ไม่ commit

ห้ามเก็บใน:

- frontend code
- GitHub public repo
- Markdown docs ที่มี key จริง
- screenshot

