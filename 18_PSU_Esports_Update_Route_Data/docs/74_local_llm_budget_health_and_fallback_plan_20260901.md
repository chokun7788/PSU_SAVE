# Implementation Plan: Local LLM Budget, Health และ Verified Fallback

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **unit_verified** (2 กันยายน 2026; circuit breaker, queue gate และ deterministic fallback ผ่าน smoke tests)

Owner ที่แนะนำ: Local Model Runtime / Pipeline

Model scope: **Typhoon2.5-Qwen3-4B ผ่าน Local Ollama เท่านั้น**

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือกำหนดบทบาทและขอบเขตเวลาของ Local LLM ให้ชัดเจนภายใต้ SLA 10 วินาที โดยคำขอที่มี verified deterministic answer ต้องไม่รอ model และคำขอที่ใช้ model ต้องสามารถ fallback จาก evidence/draft ที่ตรวจแล้วได้ทันเวลา

Local LLM ใช้เฉพาะ:

- Intent Review เมื่อ deterministic routing ยังมีความกำกวมและมี budget
- Query Planning สำหรับ dependent multi-question ที่จำเป็นจริง
- Composer เรียบเรียง verified evidence เป็นภาษาอ่านง่าย
- Repair รูปแบบเฉพาะเมื่อ budget และ repair limit อนุญาต

Local LLM ห้าม:

- สร้างข้อเท็จจริง PSU ใหม่
- ยืนยันราคา ตารางเวลา slot การจอง หรือธุรกรรม
- เปลี่ยน target, source หรือ version
- Publish ข้อมูล
- เป็น fallback แบบ general guessing เมื่อไม่มีหลักฐาน

ระบบไม่เพิ่ม Cloud LLM หรือ Chatbot API ภายนอก

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- MB-0501 ใช้ Intent LLM ประมาณ 7.777 วินาที
- MB-0519 ใช้ Intent LLM ประมาณ 7.810 วินาที
- ค่านี้ใกล้ timeout configuration เดิม 8 วินาทีและกิน Global SLA เกือบทั้งหมดก่อน stage อื่น
- FAQ เกิน 10 วินาที 10 ข้อ และ Keyboard เกิน 10 วินาที 3 ข้อใน run 2,116 ข้อ
- KIA-0460 และ KIA-0486 ช้าโดยไม่ใช้ LLM จึงต้องแก้ deterministic path แยก ไม่ควรโยนทุกปัญหาให้ model
- baseline รันบน RTX 4050 Laptop 6GB ขณะที่ target server คือ RTX 5060 8GB; ห้ามอนุมาน latency target จากฮาร์ดแวร์ใหม่โดยไม่ทดสอบ

### 2.2 สิ่งที่ยืนยันจาก Code/Config

- start configuration ใช้ Typhoon2.5 Qwen3 4B
- Intent context เดิม 2,048 และ Facts/Composer context 3,072
- Intent timeout เดิมประมาณ 8 วินาที
- Facts Composer default ใน source ประมาณ 5 วินาที
- Pipeline รองรับ LLM call count สูงสุด 2 และ LLM concurrency 1
- queue wait default ประมาณ 0.2 วินาที
- facts_composer มี global deadline-aware timeout บางส่วน
- experimental fallback มี circuit breaker บางรูปแบบ แต่ต้องรวม health policy ให้เป็น contract กลาง

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- 7.8 วินาทีเกิดจาก queue, model load, prompt evaluation, generation หรือ socket timeoutเท่าใดยังไม่ทราบ
- context 2,048/3,072 ไม่ได้ยืนยันว่า VRAM เพียงพอทุก concurrent scenario
- timeout 1.2/4.0 วินาทีอาจทำให้ generationไม่จบในเครื่องทดสอบเดิม ต้องวัดและปรับ prompt/token limitsโดยไม่ขยาย Global SLA
- Ollama response metadataอาจให้ timingไม่ครบทุก error path

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **Per-call timeout ใหญ่กว่า stage budgetที่ควรมี**: Intent 8 วินาทีแทบใช้ SLA ทั้งหมด
2. **Queue time ไม่ถูกมองเป็นงานที่ควร skip**: concurrency 1 ทำให้ request สามารถรอ modelแม้มี verified fallback
3. **LLM eligibility กว้างเกินไป**: exact factual requestบางชนิดยังเข้าถึง Intent/Composer
4. **Timing telemetryไม่แยก phase**: จึงแก้ model โดยไม่รู้ queue/load/eval/generation
5. **Fallback contractไม่เป็นศูนย์กลาง**: หลาย call siteมี policyต่างกัน
6. **Circuit stateกระจาย**: health/cooldownต้องบังคับก่อนจอง slot

### สิ่งที่ยังพิสูจน์ไม่ได้

- model context ไม่ใช่ 262k และไม่มีหลักฐานว่า context length ใหญ่เป็นสาเหตุ;ค่าที่ใช้อยู่คือ 2,048/3,072
- ยังสรุปไม่ได้ว่า GPU, RAM หรือ Ollamaเสีย
- ยังไม่ทราบ token rateบน RTX 5060 จนกว่าจะ benchmarkจริง
- ยังไม่ทราบว่า model load cold startควรอยู่ใน startup warmupหรือ worker lifecycleใด

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ค่า timeout และ token limits ต้องยืนยันบน target hardware

### Eligibility

| Request | Intent LLM | Composer | Fallback |
|---|---:|---:|---|
| exact game/member/equipment fact | ไม่ใช้ | ไม่ใช้ | Structured answer |
| price calculation | ไม่ใช้ | ไม่ใช้ | Deterministic calculation |
| schedule/slot/booking status | ไม่ใช้ | ไม่ใช้ | API/Structured Safe Outcome |
| clear RAG query + strong evidence | ไม่ใช้โดย default | optional 1 call | verified evidence draft |
| ambiguous intent | optional 1 call | ไม่ใช้ | deterministic clarification |
| dependent multi-question | optional planner 1 call | optional composer callที่ 2 | bounded plan/drafts |
| no verified evidence | ไม่ใช้เพื่อเดา | ไม่ใช้ | clarification/no-answer |

### Budget Invariants

- Simple request ใช้ LLM สูงสุด 1 call
- Dependent multi-question ใช้สูงสุด 2 calls
- call ที่สองเริ่มได้เมื่อ call แรกเสร็จและ Budget gateผ่าน
- Intent LLM timeout 1.2 วินาที
- Composer timeout 4.0 วินาที
- queue waitสูงสุด 0.2 วินาทีและนับใน Global Deadline
- Intent num_ctx 2,048
- Composer num_ctx 3,072
- socket timeout = minimum ของ stage cap และ remaining budget
- finalizer reserve 1.0 วินาทีห้ามถูก modelใช้
- LLM ไม่ได้รับ unverified evidence
- outputทุกครั้งผ่าน parser + Answer Contract

### Health Invariants

- circuit เปิดหลัง timeout/errorต่อเนื่อง 2 ครั้ง
- cooldown 60 วินาที
- half-open อนุญาต probe 1 call
- requestทั่วไปไม่เป็น probeพร้อมกัน
- circuit stateเป็น process/shared runtime stateที่ thread-safe
- model unavailableไม่ทำให้ API workerค้าง

## 5. Mermaid Flow/Sequence Diagram

### LLM Gate

~~~mermaid
flowchart TD
    R[Request + verified draft/evidence] --> E{LLM eligible?}
    E -->|no| F[Use verified draft]
    E -->|yes| B{Budget sufficient?}
    B -->|no| F
    B -->|yes| H{Circuit healthy?}
    H -->|open| F
    H -->|closed/half-open| Q{Acquire slot <= 0.2s}
    Q -->|no| F
    Q -->|yes| C[Bounded Local LLM call]
    C --> V{Parse + validate}
    V -->|pass| O[Use composed result]
    V -->|fail| F
    C -->|timeout/error| CB[Record health failure]
    CB --> F
~~~

### Timed Call Sequence

~~~mermaid
sequenceDiagram
    participant E as Engine
    participant B as RequestBudget
    participant H as LLM Health
    participant S as LLM Semaphore
    participant O as Ollama
    E->>B: allow_stage(intent or composer)
    B-->>E: cap from remaining budget
    E->>H: can_attempt
    H-->>E: closed or half-open
    E->>S: acquire max 0.2s
    alt slot unavailable
        S-->>E: fallback immediately
    else acquired
        E->>O: socket timeout bounded by budget
        O-->>E: response or timeout/error
        E->>S: release in finally
        E->>H: success/failure
    end
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 LLMCallPolicy

~~~python
@dataclass(frozen=True)
class LLMCallPolicy:
    purpose: Literal["intent_review", "query_planner", "composer", "repair"]
    timeout_sec: float
    queue_wait_sec: float
    num_ctx: int
    num_predict: int
    temperature: float
    required_remaining_sec: float
    max_input_chars: int
    output_contract: str
~~~

ค่า num_predict ต้องกำหนดจาก benchmark:

- intent JSON: เริ่มต้น 64 tokens
- planner concise JSON: เริ่มต้น 128 tokens
- composer: เริ่มต้น 160 tokens
- repair: เริ่มต้น 96 tokens

ต้องมี hard maximum และ stop sequencesตาม model adapter

### 6.2 LLMCallResult

~~~python
@dataclass(frozen=True)
class LLMCallResult:
    status: Literal[
        "completed", "queue_skipped", "circuit_open",
        "budget_skipped", "timeout", "invalid_output",
        "provider_error", "empty_output"
    ]
    text: str
    parsed: Mapping[str, object] | None
    model_id: str
    queue_ms: float
    model_load_ms: float | None
    prompt_eval_ms: float | None
    generation_ms: float | None
    parse_ms: float
    token_counts: Mapping[str, int]
    elapsed_ms: float
~~~

### 6.3 Circuit state

~~~python
@dataclass
class CircuitState:
    state: Literal["closed", "open", "half_open"]
    consecutive_failures: int
    opened_at: float | None
    half_open_probe_in_flight: bool
    last_error_type: str | None
~~~

State transitions:

- closed + success → reset failures
- closed + timeout/errorครั้งที่ 1 → failures=1
- closed + timeout/errorครั้งที่ 2 → open
- open และยังไม่ครบ 60s → skip
- open ครบ 60s → half_open
- half_open success → closed
- half_open failure → open/reset cooldown

Invalid JSON ที่ modelตอบทันเวลาเป็น quality failure;นับ circuit failureเมื่อเกิดซ้ำตาม config แยกจาก infrastructure error

### 6.4 LLM gate pseudocode

~~~python
def maybe_call_llm(policy, evidence, draft, context):
    if not eligibility(policy.purpose, context):
        return fallback("not_eligible", draft)
    if context.llm_calls >= context.max_llm_calls:
        return fallback("call_limit", draft)
    if context.budget.remaining() < policy.required_remaining_sec:
        return fallback("budget_skipped", draft)
    if not health.can_attempt():
        return fallback("circuit_open", draft)

    wait = min(0.2, context.budget.remaining_for_stage())
    if not semaphore.acquire(timeout=wait):
        return fallback("queue_skipped", draft)

    try:
        context.llm_calls += 1
        timeout = min(policy.timeout_sec, context.budget.remaining_for_stage())
        result = ollama_adapter.call(
            verified_evidence=evidence,
            draft=draft,
            timeout=timeout,
            policy=policy,
        )
        parsed = parse_bounded(result)
        validated = validate_against_evidence(parsed, evidence, context.frame)
        return validated if validated.ok else fallback("invalid_output", draft)
    finally:
        semaphore.release()
~~~

### 6.5 Verified Draft fallback

Draft ต้องถูกสร้างก่อน LLM จาก:

- Structured fields ที่ผ่าน schema/version
- deterministic calculation output
- RAG evidenceที่ผ่าน target/source guard
- source links/IDs
- answer type requirement

LLM แก้ได้เฉพาะ presentation:

- รวมประโยคซ้ำ
- เรียง bullet
- เปลี่ยนภาษาที่ไม่เปลี่ยนความหมาย
- สรุปภายใต้ข้อเท็จจริงเดิม

Validator เปรียบ claim/target/source กับ draft; ถ้าไม่ผ่านให้ใช้ draftเดิม ไม่เรียก modelซ้ำ

### 6.6 Intent JSON contract

~~~json
{
  "operation": "member_lookup",
  "domain": "overview",
  "target_text": "",
  "dependent": false,
  "confidence": 0.0
}
~~~

Parser:

- รับ JSON objectเดียว
- reject extra prose
- whitelist operation/domain
- จำกัด string length
- targetจาก LLMเป็น proposalเท่านั้น ต้องผ่าน deterministic resolver

### 6.7 Config defaults

| Config | Default |
|---|---:|
| PSU_LLM_MODEL | Typhoon2.5-Qwen3-4B local model ID |
| PSU_INTENT_LLM_TIMEOUT_SEC | 1.2 |
| PSU_FACTS_LLM_TIMEOUT_SEC | 4.0 |
| PSU_INTENT_LLM_NUM_CTX | 2048 |
| PSU_FACTS_LLM_NUM_CTX | 3072 |
| PSU_LLM_QUEUE_WAIT_SEC | 0.2 |
| PSU_LLM_CONCURRENCY | 1 |
| PSU_LLM_SIMPLE_MAX_CALLS | 1 |
| PSU_LLM_DEPENDENT_MAX_CALLS | 2 |
| PSU_LLM_CIRCUIT_FAILURES | 2 |
| PSU_LLM_CIRCUIT_COOLDOWN_SEC | 60 |
| PSU_LLM_HEALTH_ENABLED | true |

Start script ต้อง validateค่ากับ hard ceilingและ log resolved configโดยไม่เผย credential

## 7. ขั้นตอน Implement ตามลำดับ

1. เพิ่ม phase timing ใน Ollama adapterก่อนเปลี่ยน timeout
2. Freeze model-enabled slow cases และ verified fallback expected output
3. นิยาม LLMCallPolicy/Result และ central adapter
4. รวม semaphore/queue waitให้ทุก call siteใช้จุดเดียว
5. ผูก queue waitและsocket timeoutกับ RequestBudget
6. เพิ่ม eligibility matrixและ exact deterministic bypass
7. เปลี่ยน Intent timeoutเป็น 1.2 วินาที พร้อม concise JSON/token cap
8. เปลี่ยน Composer timeoutเป็น 4.0 วินาทีและ inputเฉพาะ verified evidence
9. บังคับ max calls 1/2 ตาม request type
10. Implement circuit breaker thread-safe และ half-open probe
11. ทำ verified draftเป็น first-class artifactก่อน LLM
12. เพิ่ม parser/claim-target-source validation
13. เปิด feature flagsทีละ intent แล้ว composer
14. รัน fake delayed model, Ollama unavailable และ real local model
15. รัน full model-enabled regression และ concurrency test

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| LLM slotไม่ว่าง | acquire > 0.2s | verified draft |
| circuit open | health gate | verified draft |
| budgetไม่พอ | allow_stage false | verified draft |
| socket timeout | bounded exception | verified draft + health failure |
| Ollama unavailable | connection/provider error | verified draft + circuit |
| invalid JSON | strict parser | deterministic route/clarification |
| zero-token/empty response | empty output | verified draft |
| unsupported claim | Answer Contract | discard LLM output |
| targetเปลี่ยน | frame comparison | discard LLM output |
| callแรกช้า | remaining gate | ห้าม callที่สอง |

ถ้าไม่มี verified draftหรือ evidence ให้ clarification/no-answer ไม่ใช้ general model answer

## 9. Logging/Metrics ที่ต้องเพิ่ม

Events:

- llm_eligibility_evaluated
- llm_budget_skipped
- llm_queue_started/acquired/skipped
- llm_call_started/finished/failed
- llm_parse_finished/failed
- llm_output_validation_passed/failed
- llm_fallback_used
- llm_circuit_opened/half_opened/closed

Fields:

- request_id, worker_id, purpose, call_number
- model_id, policy_version
- queue_ms, model_load_ms, prompt_eval_ms, generation_ms, parse_ms
- input_chars, evidence_count, prompt/eval/output token counts
- timeout_sec, elapsed_ms, remaining_before/after
- status, error_type, circuit_state
- fallback_source เช่น structured_draft หรือ rag_draft

Metrics:

- LLM eligibility/call/bypass rates
- queue skip rate
- timeout/error/invalid/empty rates
- circuit open duration
- phase P50/P95/P99
- fallback Answer Contract pass rate
- average calls per request
- no-LLM exact path latency

Prompt/evidence textและ Chat contentไม่อยู่ใน performance log

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- eligibility matrixทุก request type
- max call limit 1/2
- required remaining gate
- queue timeout 0.2
- socket timeoutใช้ min(stage, remaining)
- circuit transitionsครบ
- half-openมี probeเดียว
- strict JSON parse และ whitelist
- target/source mutationถูก reject
- semaphore releaseใน success/error/timeout

### Fake Provider Tests

- delayed 0.5s, 1.3s และ 5s
- invalid JSON
- extra proseรอบ JSON
- Ollama connection refused
- zero-token response
- thinking-only response
- metadata timingหาย
- cancellationระหว่าง generation

### Integration Tests

- exact member/game/priceไม่เรียก LLM
- RAG strong evidenceใช้ draft fallbackเมื่อ slot busy
- dependent multi-question callที่สองถูก skipเมื่อ remainingไม่พอ
- circuit openไม่รอ queue
- failed composerไม่เปลี่ยน answer/source
- worker restartไม่ทำให้ semaphoreค้าง

### Regression/Load Tests

- MB-0501 และ MB-0519
- full 2,116 model-enabled
- 5/10/20/30 users fast-heavy, mixed และ all-LLM-attempt
- cold Ollama startupแยกจาก warmed production test
- circuit recoveryหลัง cooldown

## 11. Acceptance Criteria แบบวัดค่าได้

- Intent LLMจบหรือ fallbackภายใน 1.2 วินาที
- Composerจบหรือ fallbackภายใน 4.0 วินาที
- queue waitไม่เกิน 0.2 วินาที
- exact facts/member/price/scheduleมี LLM call count 0
- Simple requestมี LLM callsไม่เกิน 1
- Dependent requestไม่เกิน 2 และ callที่สองผ่าน budget gate
- LLM timeout/unavailable/invalid outputยังทำให้ APIตอบภายใน 10 วินาที
- fallbackทุกคำตอบผ่าน Answer Contract
- LLMไม่สร้าง PSU factหรือเปลี่ยน target/sourceใน accepted output
- circuitเปิดหลัง infrastructure failureต่อเนื่อง 2 ครั้งและ recoverผ่าน probeเดียว
- strict FAQ scoreไม่ต่ำกว่า 91.00%
- ไม่มี semaphore leakหลัง timeout/crash

## 12. Rollback และ Compatibility

- model IDและ Local-only deploymentไม่เปลี่ยน
- response schemaเดิมคงอยู่; LLM timingเพิ่มใน performance traceเท่านั้น
- timeout/configใหม่อยู่หลัง feature flags
- central adapterรองรับ call siteเดิมผ่าน compatibility wrapper
- หาก Intent accuracyลด ให้ปิด Intent LLMแล้วใช้ deterministic clarification ไม่เพิ่ม timeout
- หาก Composer qualityลด ให้ปิด Composerและใช้ verified draft
- circuit breakerปิดชั่วคราวได้เฉพาะใน isolated diagnosis; Productionต้องมี health gate

Rollback triggers:

- accepted unsupported claimแม้หนึ่ง case
- target/source mutationผ่าน validator
- FAQ strictลดต่ำกว่า 91.00% หรือ previously-passing caseตก
- requestเกิน 10 วินาทีจาก LLM
- semaphoreไม่คืนหรือ queue growthไม่หยุด

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 Hard Deadline และ Supervisor](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member Routing](70_member_about_us_routing_correction_plan_20260901.md)
- [72 RequestExecutionContext](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [73 Target-grounded RAG](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [75 Worker Crash Diagnosis](75_windows_worker_crash_diagnosis_and_recovery_plan_20260901.md)
- [76 Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 SLA และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: RequestBudget/worker cancellationจาก 69, verified evidenceจาก 73, request call countersจาก 72 และ phase loggingจาก 76 ต้องพร้อมก่อนลด timeoutใน production
