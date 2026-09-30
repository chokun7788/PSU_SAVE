# Implementation Plan: End-to-End SLA, Load Test and Rollout

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: QA / Runtime / Release Owner

Target Production Hardware: **Intel i5-14400, RAM 32GB, NVIDIA RTX 5060 8GB**

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือพิสูจน์ว่าแผน 68–76 เมื่อนำไป Implement แล้ว:

- ผู้ใช้ได้รับ HTTP responseภายใน 10 วินาทีจริง
- ไม่มี Harness Timeout
- ไม่มี Worker Crash
- factual accuracyไม่ต่ำกว่า baseline
- รองรับ concurrent usersตามรูปแบบ workloadที่กำหนด
- rollout/rollbackได้ทีละ featureโดยระบุสาเหตุได้

เอกสารนี้เป็น gateสุดท้ายก่อน Production ไม่อนุญาตให้เปลี่ยน Acceptance Criteriaย้อนหลังเพื่อทำให้ runผ่าน และไม่อนุญาตให้ใช้ serial benchmarkแทน HTTP concurrency test

สถานะปัจจุบัน:

- Full model-enabled runมี 2,116 cases
- FAQ strict 1,456/1,600 = 91.00%
- baselineก่อนหน้าที่ต้องพยายามกลับไปหา 1,509/1,600 = 94.31%
- FAQเกิน 10 วินาที 10ข้อ
- Keyboardเกิน 10 วินาที 3ข้อ
- Harness Timeout 7ข้อ
- Worker Crashที่สังเกตอย่างน้อย 2เหตุการณ์
- Canonicalต้องตรวจตามเกณฑ์อย่างน้อย 15/16
- ผลเดิมมาจาก RTX 4050 Laptop 6GB ไม่ใช่ target server

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- MB-0499, MB-0500, MB-0501, MB-0503, MB-0507, MB-0518, MB-0519, MB-0618, MB-1229 และ MB-1232เป็น FAQ slow setหลัก
- KIA-0460, KIA-0486 และ KIA-0487เป็น Keyboard slow/crash setหลัก
- KIA-0460/KIA-0486ช้าโดยไม่ใช้ LLM
- MB-0501/MB-0519มี Intent, deterministicและretrieval stagesแพงต่อกัน
- current runมีสถานะ completed, pipeline/harness timeoutและworker crashปะปน จึงต้องใช้ taxonomyจาก 68/76

### 2.2 สิ่งที่ยืนยันจาก Code/Config

- Web APIเดิมมี active request limit default 16และ LLM concurrency 1
- start/runtime configใช้ Local Typhoon2.5-Qwen3-4B
- Production SLAกำหนด 10วินาที แต่ cooperative pipeline timeoutเดิมไม่ใช่ hard API ceiling
- Structured/Fast/RAG/LLMมีเส้นทางต่างกัน จึงต้องทดสอบ workload mix ไม่ใช่เฉลี่ยรวมอย่างเดียว

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- active requests 32และ pipeline workers 4เป็นค่าเริ่มต้นที่เสนอ ไม่ใช่ค่าที่พิสูจน์แล้ว
- scaling 4→6→8 workersต้องวัด RSS/CPUจริง
- projected RSSรวมไม่เกิน 12GBเป็น worker-pool budgetเริ่มต้น ไม่รวมระบบทั้งหมด
- target RTX 5060อาจลด LLM latencyแต่ไม่แก้ CPU fuzzyหรือroutingเอง
- 30 concurrent usersจะผ่านได้หรือไม่ต้องพิสูจน์ด้วย HTTP load test

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ระดับ Release Process

1. **Serial benchmarkไม่แทน concurrency**: ไม่เห็น queue/admission/lock contention
2. **Internal elapsedไม่เท่ากับ user latency**: ต้องวัดตั้งแต่ clientส่งจนรับ responseครบ
3. **Accuracyและlatencyไม่ได้ gateร่วมกัน**: optimizationอาจเร็วขึ้นแต่ตอบผิด
4. **Crash/timeout taxonomyเดิมไม่พอ**: pass rateรวมซ่อน reliability failure
5. **Hardware mismatch**: benchmarkเครื่องเดิมไม่ยืนยัน Production
6. **No staged feature rollout contract**: เปลี่ยนหลายส่วนพร้อมกันแล้วหา regressionยาก

### สิ่งที่ยังพิสูจน์ไม่ได้

- worker countที่เหมาะสม
- admission thresholdที่รักษา latencyดีที่สุด
- LLM queue behaviorเมื่อ all-LLM-attempt 30 users
- warmup durationและ steady-state throughput
- memory slopeระยะยาว

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** และจะกลายเป็น release policy เมื่อผู้รับผิดชอบอนุมัติ

### Test Invariants

- ทุก runมี run ID, manifestและ file hashesใหม่
- Full runเป็น Model-enabled flowจริง
- ไม่สร้าง No-LLM baselineซ้ำโดยไม่มีวัตถุประสงค์
- วัด client-observed latencyและserver stage latencyแยกกัน
- timeout ceilingวัด response bodyได้รับครบ
- expected route/answer/sourceเทียบ Goldรายข้อ
- previously-passing caseถูก trackเป็น named regression set
- load scenariosใช้ fixed workload manifestเพื่อ compareได้

### Runtime Invariants

- active request admission default 32
- persistent pipeline workersเริ่ม 4
- CPU worker scaleสูงสุด 8ภายใต้ RSS gate
- LLM concurrency 1
- LLM queue wait 0.2 วินาที
- requestที่ไม่ได้ LLM slotใช้ deterministic/verified RAG draft
- session isolation
- parent supervisorคืน resourceทุก terminal state
- responseเกิน 10วินาทีเป็น failureแม้คำตอบถูก

### Release Invariants

- feature flagsเปิดทีละขั้น
- ทุกขั้นมี observation windowและrollback trigger
- acceptanceไม่ถูกลด
- Structured/RAG release versionตรงกัน
- Local-only model policyคงอยู่

## 5. Mermaid Flow/Sequence Diagram

### Verification Pyramid

~~~mermaid
flowchart TD
    U[Unit tests per component] --> S[13 slow cases]
    S --> F[Focused 100+ cases]
    F --> A[Full model-enabled 2,116]
    A --> H[HTTP concurrency 5 users]
    H --> H10[10 users]
    H10 --> H20[20 users]
    H20 --> H30[30 users]
    H30 --> HW[Repeat on target hardware]
    HW --> G{All acceptance gates pass?}
    G -->|yes| RO[Staged rollout]
    G -->|no| B[Block release + root-cause report]
~~~

### Feature Rollout

~~~mermaid
flowchart LR
    O[Observability minimum] --> RS[Resolver shadow]
    RS --> RC[Route correction]
    RC --> HD[Hard deadline]
    HD --> WS[Worker supervisor]
    WS --> RG[Retrieval budgets]
    RG --> LG[LLM budgets + health]
    LG --> P[Production ready]
    RS -. rollback .-> O
    RC -. rollback .-> RS
    HD -. rollback .-> RC
    WS -. rollback .-> HD
    RG -. rollback .-> WS
    LG -. rollback .-> RG
~~~

### Load Request Sequence

~~~mermaid
sequenceDiagram
    participant C as Load Client
    participant A as Admission Control
    participant P as Pipeline Worker Pool
    participant L as LLM Slot
    participant R as Response
    C->>A: HTTP request + unique request/session IDs
    alt capacity available
        A->>P: assign worker
        alt LLM eligible and slot <= 0.2s
            P->>L: bounded call
            L-->>P: result or fallback
        else no slot/not eligible
            P->>P: deterministic or verified draft
        end
        P-->>R: finalized response
        R-->>C: body complete <= 10s
    else admission full
        A-->>C: bounded retryable response
    end
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 RunManifest

~~~python
@dataclass(frozen=True)
class RunManifest:
    run_id: str
    started_at: str
    git_commit: str
    dirty_worktree_fingerprint: str
    dataset_hashes: Mapping[str, str]
    config_snapshot: Mapping[str, str | int | float | bool]
    feature_flags: Mapping[str, bool]
    python_runtime: str
    model_id: str
    embedding_model_id: str
    hardware: Mapping[str, str]
    warmup_protocol: str
    concurrency_scenario: str
~~~

ห้ามเก็บ secret/environment credentialใน manifest

### 6.2 PerRequestResult

~~~python
@dataclass(frozen=True)
class PerRequestResult:
    case_id: str
    request_id: str
    session_id_hash: str
    status: Literal[
        "completed", "pipeline_timeout", "hard_timeout",
        "worker_crash", "admission_rejected", "unobserved"
    ]
    http_status: int | None
    client_latency_ms: float
    server_elapsed_ms: float | None
    queue_ms: float | None
    route: str | None
    capability: str | None
    llm_calls: int
    answer_contract_pass: bool
    strict_pass: bool
    regression_from_prior_pass: bool
~~~

### 6.3 Test tiers

| Tier | Dataset | Purpose | Stop condition |
|---|---|---|---|
| T0 | Unit/fault injection | interfaceและfailure semantics | unit failureใดๆ |
| T1 | 13 slow cases | latency root fixes | caseใดเกิน 10s/crash |
| T2 | focusedอย่างน้อย 100 | members/games/RAG/keyboard | accuracyหรือroute regression |
| T3 | full 2,116 | global accuracy/reliability | global gate fail |
| T4 | HTTP 5/10/20/30 | queue/load/admission | SLA/crash/resource fail |
| T5 | target hardware repeat | Production evidence | gateใดไม่ผ่าน |

Focused corpusควรดึง:

- slow 13ทั้งหมด
- member/roleอย่างน้อย 25–50
- known/unknown/non-game title
- RAG target mismatch
- keyboard layout positive/negative
- canonical pilot

เอกสาร 68อาจมี corpusมากกว่า 100; Tier T2เลือก fixed representative 100เป็น fast gateและยังรัน corpusเต็มก่อน T3

### 6.4 Workload scenarios

#### Fast-heavy

- 80% Structured/Fast exact
- 15% RAG
- 5% LLM eligible

#### Mixed

- 50% Structured/Fast
- 30% RAG
- 20% LLM eligible

#### All-LLM-attempt

- 100% queryที่ eligibilityอาจขอ LLM
- แต่ policyยังต้อง fallbackเมื่อ slotไม่ว่าง
- เป้าหมายวัด queue gate ไม่ใช่บังคับทุก requestให้ generate

ทุก scenarioรัน concurrency 5, 10, 20และ30 พร้อม:

- warmup phase
- steady phaseอย่างน้อยจำนวน requestที่กำหนด
- cooldown/worker health capture
- unique request ID
- session distributionทั้ง unique sessionsและcontrolled same-session sequence

### 6.5 Admission/Worker defaults

| Config | Initial value |
|---|---:|
| PSU_MAX_ACTIVE_REQUESTS | 32 |
| PSU_PIPELINE_WORKERS | 4 |
| PSU_PIPELINE_WORKERS_MAX | 8 |
| PSU_CPU_WORKERS_MAX | 8 |
| PSU_WORKER_POOL_RSS_BUDGET_GB | 12 |
| PSU_LLM_CONCURRENCY | 1 |
| PSU_LLM_QUEUE_WAIT_SEC | 0.2 |
| PSU_REQUEST_PIPELINE_SEC | 9.0 |
| PSU_WORKER_HARD_SEC | 9.25 |
| PSU_API_RESPONSE_CEILING_SEC | 10.0 |

Active requestsรวม runningและbounded queueตาม implementation;ต้องนิยาม metricให้ชัดไม่ใช้ชื่อเดียวคนละความหมาย

### 6.6 Worker scaling policy

Scale up:

- current workers 4
- queue wait P95เกิน 500msต่อเนื่องใน observation windowsอย่างน้อย 3ช่วง
- healthy CPU headroomตาม target threshold
- projected pool RSSหลังเพิ่มไม่เกิน 12GB
- เพิ่ม 4→6 แล้ววัดใหม่;เพิ่ม 6→8เมื่อเกณฑ์ยังคงอยู่

Scale down:

- queue P95ต่ำกว่า 100ms
- utilizationต่ำกว่า 20%
- idleต่อเนื่องอย่างน้อย 5นาที
- drain workerทีละ 1–2ตัว ไม่ kill active request
- ไม่ต่ำกว่า 4ใน Production defaultจนมี evidenceใหม่

Projected RSS:

~~~python
projected = current_pool_rss + warm_worker_rss * workers_to_add
allow_scale = projected <= 12 * GiB and cpu_headroom_ok
~~~

ห้าม scaleจาก queueของ LLM เพราะ LLM concurrencyคง 1และ requestควร fallbackแทน

### 6.7 Load runner behavior

~~~python
async def run_scenario(cases, concurrency, duration):
    warm_up_system()
    limiter = FixedConcurrency(concurrency)
    for scheduled_case in deterministic_schedule(cases, duration):
        launch(
            send_http_request(
                case=scheduled_case,
                request_id=new_uuid(),
                deadline_sec=10.5,
            ),
            limiter=limiter,
        )
    await collect_all()
    write_new_run_directory()
    fail_if_missing_result()
~~~

Client timeoutตั้งมากกว่า server ceilingเล็กน้อย เช่น 10.5วินาทีเพื่อแยก server responseเกิน 10จาก harnessตัดที่ 10พอดี แต่ acceptanceใช้ client latency 10.0วินาที

### 6.8 Accuracy gates

FAQ:

- strict passไม่ต่ำกว่า 91.00%
- previously-passing caseห้ามตก
- milestoneกลับสู่ไม่น้อยกว่า 94.31%

Keyboard:

- precision/recallไม่ต่ำกว่าค่าที่สังเกตใน baseline
- false positiveบนข้อความปกติไม่เพิ่ม
- detected wrong-layout outputตาม Guard contract

Canonical:

- อย่างน้อย 15/16
- ไม่มี latencyเกิน 10วินาที

Routing/RAG:

- member casesไม่เข้า Game Resolver
- evidence target mismatchเป็น 0
- resolver false cross-game matchเป็น 0

### 6.9 Reports

แต่ละ runสร้าง:

- manifest.json
- results.jsonl
- performance events
- latency_summary.json
- accuracy_summary.json
- regressions_from_prior_pass.md
- timeout_crash_taxonomy.md
- resource_summary.json
- rollout_decision.md

rollout_decisionต้องเป็น pass/blockพร้อม failed criterionรายข้อ ห้ามสรุปด้วยค่าเฉลี่ยอย่างเดียว

## 7. ขั้นตอน Implement ตามลำดับ

### Implementation Verification Order

1. Freeze baseline/corpusตาม 68
2. เพิ่ม minimum observabilityจาก 76
3. Implement Hard Deadlineจาก 69ใน isolated/staging
4. Implement route/member correction 70
5. Implement GameResolverและdedup 71–72
6. Implement RAG/LLM budgets 73–74
7. Implement/verify crash supervision 75
8. ผ่าน T0 Unit/fault injection
9. ผ่าน T1 slow 13
10. ผ่าน T2 focused 100+
11. ผ่าน T3 full 2,116 model-enabled
12. ผ่าน T4 HTTP concurrencyทุก scenario
13. ทำซ้ำ T3/T4บน target hardware

### Production Enablement Order

Implementation orderกับ enablement orderต่างกันได้:

1. Observability minimum เปิดก่อนเพื่อมีหลักฐาน
2. Resolver shadow ไม่มีผลต่อคำตอบ
3. Route correction
4. Hard deadline
5. Worker supervisor
6. Retrieval budget/target grounding
7. LLM budget/health

แต่ละขั้น:

- deploy flag off/shadow
- run health probe
- เปิด canary trafficภายใน
- observeตาม request count/time window
- compareกับ prior stage
- promoteหรือ rollback
- บันทึก decisionใน Master Plan 67

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback/Decision |
|---|---|---|
| slow caseเกิน 10s | client latency | blockขั้นถัดไป |
| accuracyลด | gold comparison | rollback featureล่าสุด |
| previously-passingตก | named regression | blockแม้คะแนนรวมยังผ่าน |
| worker crash | supervisor taxonomy | rollback/diagnose; 503 runtime |
| memoryสูง | RSS gate | ไม่ scaleเพิ่ม, drain/rollback |
| LLM queueสูง | queue P95 | fallback draft ไม่เพิ่ม LLM concurrency |
| admissionเต็ม | active limit | bounded retryable response |
| target mismatch | Answer Contract | no-answerและrollback retrieval |
| logไม่ครบ | trace completeness | run invalid ต้องรันใหม่ |
| target hardwareต่าง config | manifest diff | runเทียบกันไม่ได้ |

ห้าม rerunเฉพาะ failed casesแล้วประกาศ full pass; full suiteต้องรันใหม่หลัง fix

## 9. Logging/Metrics ที่ต้องเพิ่ม

### User-observed

- client latency P50/P95/P99/Max
- response over 10s count
- HTTP status distribution
- admission reject rate
- incomplete response count

### Runtime

- active requests, bounded queue depth/wait
- healthy/busy/draining worker counts
- worker RSS/CPUและpool RSS
- LLM queue/call/fallback/circuit
- stage critical path ranking
- timeout/crash taxonomy
- resource release failures

### Quality

- strict pass per dataset/category/route
- previously-passing regressions
- member route violations
- target/source/version violations
- keyboard precision/recall/false positives
- canonical score

Dashboard/reportต้องแยก scenarioและconcurrency ห้ามรวมเป็นค่าเฉลี่ยเดียว

## 10. Unit, Integration, Regression และ Load Tests

### Unit

- load schedule deterministic
- manifest/hash
- percentile calculation
- >10s boundaryเช่น 9.999 vs 10.001
- scale gate RSS projection
- regression-from-prior-pass detection
- rollout decision fail closed

### Integration

- HTTP response optional timing fields
- controlled timeout 200 vs worker failure 503
- request IDsตรง Parent Logger
- feature flags snapshotตรง runtime
- worker replacementระหว่าง load
- LLM busy fallback
- Structured/RAG version consistency

### Regression

- slow 13
- focused 100+
- full 2,116 model-enabled
- FAQ 1,600
- Keyboard 500
- Canonical 16
- no additional No-LLM runเว้นแต่ isolate root causeตามเอกสารอื่น

### Load

รันตารางเต็ม:

| Scenario | 5 | 10 | 20 | 30 |
|---|---:|---:|---:|---:|
| fast-heavy | required | required | required | required |
| mixed | required | required | required | required |
| all-LLM-attempt | required | required | required | required |

อย่างน้อยหนึ่ง runต้องรวม:

- worker recycle
- circuit breaker open/recovery
- one injected worker crashใน staging
- index reloadนอก active release windowหรือ controlled switch
- same-session sequential questions

## 11. Acceptance Criteria แบบวัดค่าได้

### Global Release Gate

- 0 requestมี client-observed latencyเกิน 10.0วินาที
- 0 Harness Timeout
- 0 Worker Crashใน non-injected verification
- synthetic/injected crashไม่ล้ม Web APIและ requestถัดไปผ่าน
- member routeไม่แตะ Game Resolver
- resolver P99ต่ำกว่า 250ms
- retrievalทุก requestไม่เกิน 1.5s
- Intentไม่เกิน 1.2s; Composerไม่เกิน 4.0sหรือ fallback
- lock/semaphore/context leakเป็น 0

### Accuracy Gate

- FAQ strictไม่น้อยกว่า 91.00%
- ไม่มี previously-passing FAQตกจากการแก้ latency
- เป้าหมายถัดไปไม่น้อยกว่า 94.31%
- Keyboard precision/recallไม่ต่ำกว่าผล baselineที่บันทึกใน run manifest
- Keyboard normal-text false positiveไม่เพิ่ม
- Canonicalอย่างน้อย 15/16และทุก caseต่ำกว่า 10วินาที
- evidence target mismatch 0
- false game cross-match 0

### Concurrency Gate

- scenarios 5/10/20/30 usersรันครบ
- 30-user runรักษา Global Release Gate
- LLM queue waitไม่เกิน 0.2s; requestที่พลาด slot fallback
- active requestsไม่เกิน 32
- workersไม่เกิน 8
- projected/measured worker pool RSSไม่เกิน 12GB
- scaling eventไม่ kill active request

หากข้อใดข้อหนึ่งไม่ผ่าน สถานะสูงสุดคือ **regression_verified=false** และห้ามตั้ง production_ready

## 12. Rollback และ Compatibility

### Feature flags

- PSU_GAME_RESOLVER_SHADOW
- PSU_MEMBER_FRAME_BEFORE_SEMANTIC
- PSU_MEMBER_CLOSED_ROUTE
- PSU_REQUEST_BUDGET_ENABLED
- PSU_PIPELINE_WORKER_SUPERVISOR
- PSU_RETRIEVAL_TARGET_GROUNDING
- PSU_LLM_HEALTH_ENABLED
- PSU_LLM_BUDGET_POLICY

### Rollback triggerร่วม

- accuracyลด
- timeoutเพิ่ม
- crashเพิ่ม
- memoryเกิน threshold
- target/source violation
- performance traceไม่ครบ
- admission rejectsเกิน approved capacity target

### Compatibility

- API fieldsใหม่ optionalเท่านั้น
- ไม่ลบ/เปลี่ยน fieldเดิม
- controlled timeoutใช้ Safe Outcomeเดิม
- hard worker failureใช้ retryable 503
- runtime route overview; about_us evidence category
- ไม่มี route/handlerรายเกม
- ไม่มี Cloud LLM
- Structured/RAG releaseเดียวกัน
- Performance Logแยก Chat Log/PII

Rollbackทีละ flagย้อนลำดับ enablementและบันทึก:

- trigger
- affected run/cases
- before/after metrics
- restored config
- follow-up owner

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Regression Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 Hard Deadline และ Worker Supervisor](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member/About Us Routing](70_member_about_us_routing_correction_plan_20260901.md)
- [71 Bounded Game Resolver](71_bounded_game_entity_resolver_plan_20260901.md)
- [72 Structured/Fast Deduplication](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [73 Target-grounded RAG](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [74 Local LLM Budget/Health](74_local_llm_budget_health_and_fallback_plan_20260901.md)
- [75 Windows Crash Diagnosis](75_windows_worker_crash_diagnosis_and_recovery_plan_20260901.md)
- [76 Crash-resilient Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Final dependency: Master Plan 67ต้องอัปเดตสถานะและลิงก์ผลจริงหลังแต่ละ gate โดยห้ามแก้ acceptanceเพื่อให้ผลดูผ่าน Production approvalเกิดได้เมื่อ T0–T5ผ่านบน target serverเท่านั้น
