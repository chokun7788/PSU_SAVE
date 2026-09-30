# Implementation Plan: Crash-Resilient Stage Observability

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **unit_verified** (2 กันยายน 2026; Parent JSONL, worker IPC events และ privacy smoke test ผ่านแล้ว)

Owner ที่แนะนำ: Observability / Evaluation Infrastructure

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือสร้าง Performance Trace ที่ยังบอก stageสุดท้ายและเวลาที่ใช้ได้แม้ Pipeline Worker:

- ไม่คืนผล
- ถูก hard timeout terminate
- เกิด native crash
- disconnectจาก Parent

หลักการคือ **Worker ส่ง event แต่ Parent เป็นผู้เขียน JSONL** เพื่อไม่ให้ข้อมูลทั้งหมดหายพร้อม child process และต้องแยก Performance Log ออกจาก Chat Logอย่างชัดเจน

ผลลัพธ์ที่ต้องมี:

- per-case timelineเรียง sequence
- stage status started/progress/finished/skipped/failed
- elapsedและ remaining budgetทุก boundary
- resolver/retrieval/LLM counters
- worker exit markerจาก Parent
- critical pathที่ไม่บวก stageซ้อนกันซ้ำ
- P50/P95/P99/Max และ timeout taxonomy

งานนี้ไม่ log raw conversation, prompt, evidence body, booking PIIหรือ slip

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- MB-0500 และ KIA-0487 มีสถานะ crash/unobserved จึงไม่มี final stage breakdownที่น่าเชื่อถือครบ
- Harness Timeout 7 ข้อมี elapsedเพดานประมาณ 30 วินาที แต่แยกไม่ได้ว่าค้างตรง internal loopช่วงใดทุก case
- KIA-0487 ไม่สามารถผูกกับคำถาม Hollow Knightได้ เพราะ worker logล่าสุดก่อนตายอยู่ที่ KIA-0486
- MB-0501/MB-0519 มี stage timingบางส่วน แต่ critical pathรวมต้องระวัง stage nested/overlap
- raw outputsถูกเก็บไว้แล้วและไม่ควรถูกแก้ย้อนหลังเพื่อทำให้ผลผ่าน

### 2.2 สิ่งที่ยืนยันจาก Code/Architecture

- Pipeline ปัจจุบันสะสม traceใน memoryและคืนพร้อม PipelineAnswerเป็นหลัก
- ถ้า processตายก่อน return traceช่วงท้ายอาจไม่ถูกเขียน
- ThreadingHTTPServerไม่มี Parent Logger process/queue contractสำหรับ stage events
- LLM metadataมี timingบางส่วนแต่ไม่ได้ normalizeเป็น queue/load/eval/generationทุก call
- fuzzy matchingไม่มี progress counterระดับ candidate/comparison

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- event queue overheadจะต่ำพอเมื่อ progress samplingถูกจำกัด
- multiprocessing queueบน Windows spawn modeต้องทดสอบ shutdown/crash semantics
- JSONL fsyncทุก eventอาจแพงเกินไป จึงต้องใช้ priority flush
- Parent Logger threadอาจเพียงพอ;ไม่จำเป็นต้องเป็น processแยกจนกว่าจะวัด

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **Child-owned final trace**: ข้อมูลสำคัญอยู่ใน processที่อาจตาย
2. **No event durability policy**: stage start/failureไม่มี parent flush guarantee
3. **Inconsistent stage schema**: แต่ละ componentส่ง metadataต่างกัน
4. **No monotonic sequence**: correlationระหว่าง concurrent/parallel stagesทำได้ยาก
5. **No explicit nesting identifiers**: analyzerอาจบวก elapsedของ parentและchildซ้ำ
6. **Performance/Chat concernsปะปน**: ต้องแยกข้อมูลส่วนบุคคลออกตั้งแต่ schema

### สิ่งที่ยังพิสูจน์ไม่ได้

- bottleneckจริงของทุก slow case
- event rateสูงสุดของ bounded parallel question
- storage volumeต่อวันใน Production
- retention periodที่ PSUอนุมัติ

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ต้องวัด overhead และ privacy ก่อน Production

### Target Behavior

1. Parentสร้าง request_id, trace_idและ worker assignment
2. Workerสร้าง sequenceต่อ requestแบบเพิ่มขึ้น
3. Workerส่ง eventsเข้า bounded IPC queue
4. Parent Logger validate schema, stamp received_atและเขียน JSONL
5. stage_started, stage_failed และ worker exit flushทันที
6. stage_progress batch flush
7. Parentสร้าง synthetic terminal eventเมื่อ childไม่คืนผล
8. Analyzerรวม eventตาม run/request/workerและสร้าง timeline
9. Analyzerคำนวณ exclusive/critical pathจาก parent_span_id

### Invariants

- Parentเป็น writerเดียวต่อ output file
- eventมี request_id, worker_id, sequenceและ monotonic timestamp
- sequenceไม่ซ้ำภายใน request/worker epoch
- stage_startedมี terminalคู่หรือ Parent synthetic terminal
- performance logไม่มี raw query/answer/prompt/document body/PII
- booking/slip dataห้ามเข้าช่อง trace
- progress eventเป็น bounded/sampled
- queueเต็มห้าม block requestเกิน budget;ต้องนับ dropped progress
- start/failure/finish eventsมี priorityสูงและห้าม dropตามปกติ
- analyzerไม่ถือ missing finishว่า elapsed=0

## 5. Mermaid Flow/Sequence Diagram

### Event Transport

~~~mermaid
flowchart LR
    API[Web API Parent] -->|request assigned| W[Pipeline Worker]
    W -->|high priority events| Q[Bounded IPC Queue]
    W -->|sampled progress| Q
    Q --> L[Parent Logger]
    L --> J[(Performance JSONL)]
    API -->|worker exit/hard kill| L
    J --> A[Analyzer]
    A --> T[Per-case timeline]
    A --> S[Slow-stage summary]
    A --> P[P50/P95/P99/Max]
    A --> X[Timeout/crash taxonomy]
    API --> C[(Chat Log separate)]
~~~

### Crash Sequence

~~~mermaid
sequenceDiagram
    participant W as Worker
    participant Q as Event Queue
    participant L as Parent Logger
    participant S as Supervisor
    W->>Q: stage_started game_resolution seq=20
    Q->>L: persist and flush
    W->>Q: stage_progress comparisons=16 seq=21
    Q->>L: batch persist
    W-xS: native exit before stage_finished
    S->>L: worker_exit_detected seq=parent
    L->>L: create synthetic stage_failed
    Note over L: Timeline retains last known stage and elapsed
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 Event schema

~~~python
@dataclass(frozen=True)
class PerformanceEvent:
    schema_version: str
    run_id: str
    trace_id: str
    request_id: str
    worker_id: str
    worker_epoch: int
    sequence: int
    event: str
    stage: str
    span_id: str
    parent_span_id: str | None
    wall_time_utc: str
    monotonic_ns: int
    received_at_utc: str | None
    elapsed_ms: float
    remaining_ms: float
    route: Mapping[str, str]
    status: str
    counters: Mapping[str, int | float]
    attributes: Mapping[str, str | int | float | bool | None]
~~~

ใช้ wall clockสำหรับ correlationและ monotonicสำหรับ duration ห้ามคำนวณ stage durationจาก wall clockล้วน

### 6.2 Event names

ทุก stageใช้:

- stage_started
- stage_progress
- stage_finished
- stage_skipped
- stage_failed

Parent/runtimeใช้:

- request_received
- request_admitted/rejected
- worker_assigned
- worker_exit_detected
- worker_hard_terminated
- synthetic_stage_failed
- response_sent
- logger_queue_drop
- logger_flush_failed

### 6.3 Required attributes

Common:

- timing_status
- deadline_source
- route category/intent
- executed capabilityถ้ารู้แล้ว
- release/catalog/index/model version IDs

Game Resolver:

- method
- candidate_count
- comparison_count
- score/margin bucket
- cache_hit

Retrieval:

- prefiltered_count
- scored_count
- evidence_count
- embedding_ms
- rerank_ms
- target_mismatch_count

LLM:

- purpose/call number
- queue_ms
- model_load_ms
- prompt_eval_ms
- generation_ms
- parse_ms
- token counts
- error type/circuit state

ห้าม attribute:

- raw query
- answer text
- person name, student ID, phone, email
- booking payload
- QR/slip/transaction reference
- document bodyหรือ prompt

### 6.4 Span model

ตัวอย่าง nesting:

~~~text
request
  pipeline
    understanding
      question_frame
      game_resolution
    execution
      retrieval
        embedding
        scoring
        rerank
      llm_composer
    finalizer
~~~

Parallel subquestionsมี sibling spansและ task_index attribute Analyzerต้องหา unionของเวลา ไม่บวก sibling overlapทั้งหมด

### 6.5 Worker emitter

~~~python
class EventEmitter:
    def emit(self, event, stage, priority, **attributes):
        item = build_validated_event(
            sequence=self.next_sequence(),
            event=event,
            stage=stage,
            attributes=sanitize(attributes),
        )
        if priority == "critical":
            queue_put_with_short_bounded_wait(item)
        else:
            queue_put_nowait_or_increment_drop_counter(item)
~~~

Critical queueเต็มถือเป็น reliability signal; emitterยังห้าม blockเกิน configured waitเช่น 20msเพื่อไม่ทำลาย SLA

### 6.6 Parent writer

~~~python
def parent_logger_loop(queue, jsonl_writer):
    while running_or_pending():
        event = queue.get(timeout=0.1)
        validate_schema(event)
        event.received_at_utc = utc_now()
        jsonl_writer.write(event)
        if event.event in CRITICAL_FLUSH_EVENTS:
            jsonl_writer.flush()
        elif batch_due():
            jsonl_writer.flush()
~~~

Critical flush events:

- request_received
- stage_started
- stage_failed
- worker_exit_detected
- worker_hard_terminated
- response_sent

stage_progressใช้ batchทุก 100 eventsหรือ 250ms แล้วแต่ว่าอะไรถึงก่อน

### 6.7 Progress sampling

Game fuzzy:

- emitที่ comparison 1, 8, 16, 32, 64
- ไม่ emitทุก alias

Retrieval:

- emitหลัง prefilter, embedding, scoring, rerank

LLM:

- ไม่มี token-by-token log
- emit queue acquired, response receivedและparsed

CPU loopอื่น:

- emitตาม work unitsหรือทุก 100msโดยมี hard max events

### 6.8 Queue/backpressure

| Config | Default |
|---|---:|
| PSU_PERF_EVENT_QUEUE_SIZE | 8192 |
| PSU_PERF_CRITICAL_PUT_MS | 20 |
| PSU_PERF_BATCH_EVENTS | 100 |
| PSU_PERF_BATCH_MS | 250 |
| PSU_PERF_MAX_EVENTS_PER_REQUEST | 256 |
| PSU_PERF_PROGRESS_ENABLED | true |
| PSU_PERF_LOG_SCHEMA | 1.0 |

หาก progressถูก drop:

- เพิ่ม dropped_progress_countใน worker-local counter
- terminal eventต้องส่ง countนี้
- Parent summaryระบุ trace_incomplete=true

### 6.9 JSONL file layout

~~~text
reports/performance_runs/
  RUN_ID/
    manifest.json
    events.jsonl
    worker_exits.jsonl
    analysis/
      per_case_timeline.jsonl
      slow_stage_ranking.csv
      latency_summary.json
      timeout_taxonomy.json
      report.md
~~~

ทุก run directoryใหม่ ห้ามเขียนทับ baseline/rawเดิม

### 6.10 Analyzer critical path

Algorithm:

1. sort eventตาม worker_epoch + sequence
2. pair startedกับ terminalโดย span_id
3. missing terminalใช้ Parent exit/response timestampและ mark censored
4. สร้าง intervalต่อ span
5. parent exclusive time = parent intervalลบ unionของ child intervals
6. parallel critical path = longest dependency chain ไม่ใช่ผลรวมทุก child
7. request elapsedอ้าง response_sent - request_received
8. stage rankingแสดง inclusiveและexclusiveแยกกัน

Harness timeoutที่ไม่มี response_sentใช้ harness terminal timestampและ mark hard_timeout/unobservedตาม evidence

## 7. ขั้นตอน Implement ตามลำดับ

1. Freeze schema versionและ privacy allowlist
2. สร้าง sanitizer testsก่อน emitter
3. Implement Parent Logger writerและ run directory manifest
4. Implement Worker EventEmitterพร้อม critical/progress priority
5. ส่ง request/admission/worker lifecycle eventsจาก Parent
6. Instrument RequestBudgetทุก stage boundary
7. Instrument Game Resolver counters
8. Instrument Retrieval phase timing
9. Instrument LLM queue/load/eval/generation/parse
10. เพิ่ม synthetic terminal eventเมื่อ worker exit/hard kill
11. Implement analyzer pairing/nesting/critical path
12. สร้าง per-case timelineและ aggregate reports
13. Inject worker killกลาง fuzzy loop
14. ตรวจ log completeness/overhead/privacy
15. ใช้ formatนี้กับ slow corpus, full 2,116 และ load test

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| progress queueเต็ม | put_nowait failure | drop progressและนับ;ไม่ block request |
| critical eventส่งไม่ได้ | bounded put failure | Parentใช้ lifecycle stateสร้าง synthetic event |
| Parent Loggerเขียนไม่ได้ | I/O exception | alert, rotate/fail benchmark run; APIยังตอบถ้า policyอนุญาต |
| malformed event | schema validation | quarantine event + invalid count |
| workerตายก่อน first event | supervisor exit | worker_exit eventพร้อม last_stage unknown |
| missing terminal | analyzer pairing | censored span ไม่ถือ completed |
| clock skew | wall/monotonic mismatch | ใช้ monotonicภายใน processและ Parent correlation |
| log diskเต็ม | free-space guard | stop new benchmark/admissionตาม severity |
| PIIหลุด sanitizer | privacy test/scan | quarantine runและincident handling |

Performance logging failureต้องไม่ทำให้คำตอบ factualเปลี่ยน แต่ Production readinessจะไม่ผ่านถ้า traceสำคัญหาย

## 9. Logging/Metrics ที่ต้องเพิ่ม

เอกสารนี้เป็นเจ้าของ schemaกลาง Metricsของระบบ loggingเอง:

- event queue depth P50/P95/Max
- critical/progress events sent
- dropped progress count
- invalid event count
- flush latency
- writer errors
- bytes per request
- events per request P50/P95/Max
- trace complete rate
- censored span rate
- parent-child pairing errors
- performance logging overhead

SLA overhead acceptance:

- fast request P95เพิ่มไม่เกิน 5%หรือ 20ms แล้วแต่ว่าค่าใดสูงกว่า
- event queueไม่ blockเกิน critical put cap

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- schema required fields
- sanitizer reject forbidden keys/values
- sequence monotonic
- progress sampling boundaries
- queue drop counter
- span pairing
- missing terminal/censored status
- nested exclusive time
- parallel interval union
- percentile calculation

### Integration Tests

- successful request timelineครบ
- controlled timeout timelineครบ
- hard worker killมี last stage
- native/unknown exitมี Parent terminal
- multi-question parallel spansไม่ถูกบวกซ้ำ
- LLM failureแสดง phaseก่อนล้ม
- log rotation/run directoryไม่ทับกัน

### Crash Test ที่บังคับ

1. เริ่ม synthetic request
2. เข้า game_resolution
3. emit comparison progressอย่างน้อยหนึ่ง event
4. kill workerก่อน stage_finished
5. Parentบันทึก worker_exit_detected
6. Analyzerรายงาน last_stage=game_resolution
7. elapsedก่อนตายต้องมากกว่า 0และไม่ถูกนับ completed

### Load/Privacy Tests

- 30 concurrent users
- queue saturation
- 2,116 full run
- scan JSONLหา name/email/phone/student ID/slip patterns
- disk interruption
- Parent Logger restartใน staging

## 11. Acceptance Criteria แบบวัดค่าได้

- kill workerกลาง fuzzy loopแล้วยังเห็น stageล่าสุดและ elapsedก่อนตาย
- stage_startedทุกอันมี terminalจริงหรือ synthetic
- trace complete rate 100%สำหรับ completed requests
- crash/hard timeoutมี censored terminal 100%
- analyzerไม่บวก nested/parallelเวลาซ้ำ
- reportมี per-case timeline, slow-stage ranking, P50/P95/P99/Maxและ timeout taxonomy
- dropped critical eventsเป็น 0
- progress dropถ้ามีถูกนับครบ
- performance logไม่มี Chat content, booking PIIหรือ slip
- run directoryไม่เขียนทับ Raw Outputเดิม
- logging overheadผ่านเกณฑ์ P95

## 12. Rollback และ Compatibility

- Performance schemaใหม่แยกจาก Chat Logและ API response
- trace metadataเดิมยังเก็บได้ผ่าน adapter
- instrumentationเปิด/ปิดราย componentด้วย feature flags
- หาก overheadสูง ให้ลด progress samplingก่อน ห้ามปิด critical stage events
- analyzerรองรับ schema versionและ reject unknown major version
- Parent Loggerสามารถเขียน parallel formatเก่าชั่วคราวเพื่อ compare

Rollback triggers:

- P95 latencyเพิ่มเกินเกณฑ์
- critical event drop
- writerทำให้ API processไม่เสถียร
- PIIพบใน performance JSONL
- queue memoryเกิน bound

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Run IDs](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 RequestBudget/Supervisor](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member Route Events](70_member_about_us_routing_correction_plan_20260901.md)
- [71 Game Resolver Counters](71_bounded_game_entity_resolver_plan_20260901.md)
- [72 Request Context Counters](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [73 Retrieval Timings](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [74 LLM Phase Timings](74_local_llm_budget_health_and_fallback_plan_20260901.md)
- [75 Windows Crash Diagnosis](75_windows_worker_crash_diagnosis_and_recovery_plan_20260901.md)
- [77 SLA, Load Test และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: ต้องทำขั้นต่ำของเอกสารนี้ก่อน Hard Deadline/Crash diagnosis verification เพราะหากไม่มี Parent eventsจะยังไม่ทราบว่า workerถูกหยุดหรือเสียที่ stageใด
