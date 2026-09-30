# Implementation Plan: Windows Worker Crash Diagnosis and Recovery

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: Runtime Reliability / Windows Diagnostics

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายมีสองส่วนที่ต้องทำคู่กัน:

1. ทำให้ crash ของ python.exe บน Windows ทำซ้ำหรือ isolate สาเหตุได้ด้วยหลักฐาน
2. ทำให้ Web API รอดจาก worker crash และรับ request ถัดไปได้โดยไม่ restart server

อาการที่ผู้ใช้เห็นคือ dialog **python.exe - Application Error** พร้อมข้อความ memory could not be read ระหว่าง benchmark และ run ล่าสุดมี worker crash ที่สังเกตอย่างน้อย 2 เหตุการณ์ อย่างไรก็ตามยังไม่มีหลักฐานพอระบุว่าเกิดจาก RAM, GPU, fuzzy matching, Python runtime หรือ native dependency ใด

งานนี้จึงห้ามแก้แบบเดาสาเหตุ และแยก taxonomy ระหว่าง:

- application_exception
- hard_timeout_termination
- native_access_violation
- unknown_worker_exit

Diagnostics ใช้เฉพาะ synthetic/non-PII workload ในเครื่องทดสอบ ไม่เปิด full memory dump กับ Production request ที่มีข้อมูลผู้ใช้

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log/การสังเกต

- Run 2,116 ข้อมีสถานะ worker crash อย่างน้อย 2 case ใน summary: FAQ 1 และ Keyboard 1
- **MB-0500** มี elapsed ประมาณ 29.842 วินาทีและถูกจัดเป็น crash/unobserved
- **KIA-0487** มี elapsed ประมาณ 18.064 วินาทีและ worker crash/unobserved
- Worker logสุดท้ายก่อน KIA-0487 ชี้ถึงการทำงานของ KIA-0486 จึงไม่สามารถระบุว่า KIA-0487 หรือคำว่า Hollow Knightทำให้ crash
- มี Windows Application Error dialog ที่ระบุ memory read failure
- มี harness timeout 7 case ซึ่งต้องแยกจาก process crash; timeout ไม่ได้แปลว่า access violation

### 2.2 สิ่งที่ยืนยันจาก Code/Architecture

- Web API ปัจจุบันใช้ ThreadingHTTPServer และ pipeline ทำงานใน request process/thread
- outer deadline แบบ cooperative ไม่สามารถหยุด native loopหรือ workerที่ไม่คืน control
- ไม่มี persistent Pipeline Worker Supervisorที่แยก processและสร้าง replacementอัตโนมัติ
- fuzzy/entity codeใช้ Python standard libraryส่วนหนึ่ง แต่ embedding/LLM/runtimeอาจแตะ native librariesหรือ external process
- Windows process exitและ Event Logยังไม่ได้ถูกรวมเป็น per-request evidenceแบบมาตรฐาน

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- SequenceMatcher หรือ fuzzy workloadอาจสัมพันธ์กับ crash แต่ยังไม่ยืนยัน
- bundled Pythonกับ system Pythonอาจให้ผลต่างกัน
- worker reuseอาจสะสม memory/stateจน crash
- native extension, GPU driver, Ollama, antivirus หรือ runtime DLLอาจเกี่ยวข้อง
- forced process terminationจาก harnessอาจทำให้ผู้ใช้เห็น dialogคล้าย native crashในบางสถานการณ์

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้ในระดับระบบ

1. **Failure containment ไม่พอ**: Pipeline อยู่ใน processที่ Web APIพึ่งพา
2. **Exit taxonomy ไม่ครบ**: timeout, forced kill และ native crashถูกมองคล้ายกัน
3. **Last-stage evidenceหายเมื่อ workerไม่ return**: parentรอ final resultมากกว่ารับ stage events
4. **No automatic replacement guarantee**: workerตายแล้ว requestถัดไปอาจติด state/lock
5. **Runtime matrixไม่ได้ควบคุม**: ยังไม่มี runเทียบ Python/runtime/diagnostic/process lifecycle

### สิ่งที่ยังพิสูจน์ไม่ได้

- faulting module และ exception code
- access violationเป็น read/write/executeและ address pattern
- memory leakมีจริงหรือไม่
- RSS thresholdที่เหมาะสม
- GPU/VRAM exhaustionหรือ driver reset
- crashเกิดใน Python interpreter, native extension, subprocess หรือ forced termination

จนกว่าจะมี Event Log/dump/exit code ต้องใช้คำว่า **unknown_worker_exit** ไม่ระบุสาเหตุ

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ไม่ใช่ข้อสรุปสาเหตุของ access violation

### Target Behavior

- Pipeline requestรันใน supervised worker process
- Parent Web APIมี hard wait 9.25 วินาที
- workerส่ง heartbeats/stage eventsอย่างต่อเนื่อง
- เมื่อ worker return success/controlled timeout Parentส่ง responseตาม contract
- เมื่อ workerตาย Parentจำแนก exitจาก exit code, supervisor actionและ Event Log correlation
- Parentปลด request semaphore/session lock
- Parentสร้าง replacement worker
- requestถัดไปใช้ replacementโดยไม่ restart server
- crash artifactsผูก run_id/request_id/worker_id/timestamp

### Invariants

- Web API processไม่ล้มตาม Pipeline Worker
- hard timeout terminationไม่ถูกนับเป็น native access violation
- worker crashไม่คืน HTTP 200เสมือนคำตอบปกติ
- hard worker failureคืน HTTP 503 และ retryable=true
- controlled pipeline timeoutคืน HTTP 200 Safe Outcomeตามเอกสาร 69
- locks/semaphoreคืนใน Parent finally ไม่พึ่ง child cleanup
- dump captureใช้ synthetic inputเท่านั้น
- dump directoryมี access controlและ retention
- replacement workerต้องผ่าน health probeก่อนรับงาน
- ห้ามสรุป hardware faultจากเหตุการณ์เดียว

## 5. Mermaid Flow/Sequence Diagram

### Diagnosis Matrix

~~~mermaid
flowchart TD
    C[Fixed synthetic corpus] --> R{Python runtime}
    R -->|bundled| D{Diagnostics}
    R -->|system| D
    D -->|off| W{Worker lifecycle}
    D -->|faulthandler + Event Log| W
    D -->|Local Dump test only| W
    W -->|reuse worker| L[Run repeated workload]
    W -->|fresh process| L
    L --> E[Collect exit, RSS, threads, stage events]
    E --> T[Classify exit taxonomy]
    T --> I[Reproduce or isolate]
~~~

### Supervisor Recovery

~~~mermaid
sequenceDiagram
    participant A as Web API Parent
    participant S as Supervisor
    participant W as Pipeline Worker
    participant L as Parent Logger
    A->>S: submit request
    S->>W: execute with request ID
    W->>L: stage_started/progress
    alt worker returns
        W-->>S: result
        S-->>A: response
    else worker exits
        S->>S: capture exit code and last event
        S-->>A: 503 retryable
        S->>S: release parent-owned resources
        S->>W: spawn replacement
        W-->>S: startup health ready
    else hard timeout
        S->>W: terminate after 9.25s
        S-->>A: 503 retryable
        S->>W: spawn replacement
    end
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 WorkerExitRecord

~~~python
@dataclass(frozen=True)
class WorkerExitRecord:
    run_id: str
    request_id: str
    worker_id: str
    started_at: str
    exited_at: str
    exit_code: int | None
    classification: Literal[
        "application_exception",
        "hard_timeout_termination",
        "native_access_violation",
        "unknown_worker_exit"
    ]
    supervisor_action: str
    last_stage: str | None
    last_sequence: int | None
    rss_bytes: int | None
    thread_count: int | None
    event_log_correlation: str | None
    dump_path: str | None
~~~

dump_pathอยู่ใน restricted diagnostic report ไม่ส่งใน API response

### 6.2 Exit classification

~~~python
def classify_exit(process, supervisor_record, event_record):
    if supervisor_record.termination_reason == "hard_deadline":
        return "hard_timeout_termination"
    if supervisor_record.received_python_exception:
        return "application_exception"
    if event_record and event_record.exception_code == ACCESS_VIOLATION:
        return "native_access_violation"
    if process.exit_code not in (None, 0):
        return "unknown_worker_exit"
    return "unknown_worker_exit"
~~~

Priority สำคัญ: supervisor-initiated killต้องชนะการตีความจาก nonzero exit code

### 6.3 Reproduction matrix

| Dimension | Values |
|---|---|
| Python runtime | bundled workspace Python, system Pythonที่รองรับ |
| Diagnostics | off, faulthandler + Event Log, Local Dump synthetic-only |
| Worker lifecycle | persistent reuse, fresh process per case |
| Workload | MB-0500, KIA-0486, fuzzy-known, fuzzy-unknown, synthetic loop |
| LLM | disabled for resolver isolation, enabled for end-to-end |
| Embedding | stubbed, real BGE |
| Iterations | 1, 10, 100, 500 ตาม tier |

เปลี่ยนทีละ dimensionและบันทึก manifest/hash เพื่อไม่ผสมสาเหตุ

### 6.4 Diagnostic collection

ต่อ worker:

- PID, parent PID, worker ID
- Python executable pathและversion
- package/runtime manifest
- process start/exit timestamps
- exit code
- RSS warm baseline, before case, peak, after case
- thread count
- Windows Application Event Logช่วงเวลาเดียวกัน
- Python faulthandler output
- parent stage events
- model/embedding process healthแยกจาก worker

Local Dump policy:

- enableเฉพาะ executable/processชื่อทดสอบหรือ isolated environment
- ใช้ synthetic corpusที่ไม่มี chat, booking PII, slipหรือ credential
- directory restrictedต่อผู้ทดสอบ
- hashและmanifest artifact
- retentionเริ่มต้น 7 วันหรือตาม PSU policy
- ห้าม uploadออกนอกองค์กรโดยไม่ได้อนุมัติ

### 6.5 Worker health

~~~python
@dataclass(frozen=True)
class WorkerHealth:
    worker_id: str
    pid: int
    state: Literal["starting", "ready", "busy", "draining", "dead"]
    requests_completed: int
    warm_rss_bytes: int
    current_rss_bytes: int
    last_heartbeat_at: float
~~~

Ready probeต้องตรวจ:

- child process alive
- IPC round trip
- release/index loaded
- no active request
- Parent Logger queue connected

### 6.6 Recycle policy

ค่าเริ่มต้นที่เสนอ:

- recycleหลัง 500 completed requests
- หรือ RSSสูงกว่า warm baseline 1.5 เท่า
- workerที่ busyไม่ถูก recycleกลาง request เว้น hard deadline/crash
- stateเปลี่ยนเป็น draining,หยุดรับงาน,จบงานปัจจุบันแล้ว replace
- recycleปกติไม่ถูกนับเป็น crash

Absolute RSS capต้องหาใน benchmarkเป้าหมายก่อน Production; 1.5xเป็น relative triggerเริ่มต้น

### 6.7 Supervisor pseudocode

~~~python
def supervise(job):
    worker = pool.acquire_ready_worker()
    parent_resources = acquire_request_resources(job)
    try:
        worker.send(job)
        outcome = wait_for_result_or_exit(worker, timeout=9.25)
        if outcome.kind == "result":
            return outcome.response
        if outcome.kind == "exit":
            record_exit(worker, outcome)
            schedule_replacement(worker)
            return retryable_503("pipeline_worker_restarting")
        terminate(worker, reason="hard_deadline")
        record_exit(worker, classification="hard_timeout_termination")
        schedule_replacement(worker)
        return retryable_503("pipeline_worker_restarting")
    finally:
        release_request_resources(parent_resources)
~~~

### 6.8 Config

| Config | Default |
|---|---:|
| PSU_PIPELINE_WORKER_SUPERVISOR | false แล้ว rollout |
| PSU_PIPELINE_WORKERS | 4 |
| PSU_PIPELINE_WORKER_HARD_SEC | 9.25 |
| PSU_WORKER_RECYCLE_REQUESTS | 500 |
| PSU_WORKER_RSS_MULTIPLIER | 1.5 |
| PSU_WORKER_HEARTBEAT_SEC | 0.25 |
| PSU_WORKER_READY_TIMEOUT_SEC | 15 |
| PSU_WINDOWS_DIAGNOSTICS | off ใน Production |
| PSU_WINDOWS_DUMP_RETENTION_DAYS | 7 test-only |

## 7. ขั้นตอน Implement ตามลำดับ

1. Freeze crash/slow casesและ hashesตาม 68
2. เพิ่ม Parent Logger/worker event channelตาม 76
3. เพิ่ม process/runtime/RSS/thread manifestใน benchmark
4. สร้าง isolated runnerที่รับหนึ่ง caseและคืน structured exit record
5. รัน matrixโดย diagnostics offเพื่อ baseline
6. เปิด faulthandlerและ Event Log correlationใน synthetic runner
7. ถ้ายังเกิด native exit ให้เปิด Local Dumpเฉพาะ synthetic process
8. วิเคราะห์ faulting module/exception code/stackจาก artifactที่ได้รับอนุมัติ
9. แยก resolver-only, embedding-only, LLM-only และ full pipeline
10. เปรียบเทียบ persistent workerกับ fresh process
11. Implement Supervisorและ parent-owned resource cleanup
12. Implement replacement + ready probe
13. Implement recycle 500 requests / 1.5x RSS
14. Inject crash/hangเพื่อทดสอบ containment
15. รัน full 2,116 และ HTTP concurrencyบน target server

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| Python exception | child structured error | controlled error/no-answerตาม stage |
| Hard timeout | Parent 9.25s timer | terminate, 503 retryable, replace |
| Native access violation | exit + Event Log | 503 retryable, preserve synthetic artifact, replace |
| Unknown exit | nonzero/no record | 503 retryable, alert, replace |
| Replacement start fail | ready timeout | reduce capacity, admission reject 503 |
| Parent Logger queue break | heartbeat/event timeout | kill suspect workerและreplace |
| lock/semaphore leak | parent resource registry | force release by request token |
| recycle thrash | repeated RSS threshold | stop scaling, alert, keep minimum healthy pool |
| dump contains sensitive data | policy violation check | quarantine/deleteตาม incident policy |

ห้าม retry requestอัตโนมัติภายใน Web APIหาก operationอาจมี side effect; Chatbot FAQ read-onlyสามารถให้ client retryด้วย request IDใหม่ตาม policy

## 9. Logging/Metrics ที่ต้องเพิ่ม

Events:

- worker_spawn_started/ready/failed
- worker_job_assigned
- worker_heartbeat
- worker_exit_detected
- worker_exit_classified
- worker_hard_terminated
- worker_replacement_started/ready
- worker_draining/recycled
- parent_resource_released
- diagnostic_artifact_created

Metrics:

- worker exitsแยก taxonomy
- replacement time P50/P95
- healthy worker count
- worker RSS ratioและpeak
- requests per workerก่อน recycle
- heartbeat age
- 503 worker_restarting rate
- lock/semaphore forced-release count
- crash recurrenceตาม runtime/matrix dimension

Performance logไม่เก็บ dump content, raw query, PIIหรือ slip

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- exit classification priority
- supervisor killถูกจำแนก hard_timeout
- nonzero exitไม่มี Event Logเป็น unknown
- resource release idempotent
- recycle threshold
- ready probe
- replacement backoff

### Fault Injection

- Python exception
- os-level immediate exitใน test worker
- synthetic infinite loop
- worker freezeไม่ heartbeat
- malformed IPC response
- parent logger queue disconnect
- RSS synthetic threshold
- replacement startup failure

### Reproduction Tests

- MB-0500 isolated
- KIA-0486 isolated
- KIA-0487 harness boundary
- fuzzy known/unknown 500 iterations
- bundled vs system Python
- persistent vs fresh process
- diagnostics off/on

### End-to-end Tests

- crash workerกลาง fuzzy stageแล้วยังตอบ 503ภายใน 10 วินาที
- requestถัดไปใช้ replacementและสำเร็จ
- concurrent requestsอื่นบน workerต่างตัวไม่ล้ม
- session/admission locksคืนครบ
- full 2,116มี 0 worker crash

## 11. Acceptance Criteria แบบวัดค่าได้

- root causeทำซ้ำได้หรือถูก isolateเป็น dimensionที่แคบพร้อมหลักฐาน
- ทุก exitมี taxonomy ไม่ใช้คำว่า crashแบบรวม
- native_access_violationต้องมี Event Log/exception evidence
- hard timeout terminationไม่ถูกนับเป็น native crash
- workerตายไม่ล้ม Web API parent
- APIตอบ hard worker failureภายใน 10 วินาทีด้วย HTTP 503, retryable=true
- replacement workerพร้อมโดยไม่ restart server
- requestถัดไปสำเร็จ
- lock/semaphore/session resource leakเป็น 0
- full verificationมี worker crash 0
- dump testไม่มีข้อมูลผู้ใช้และเป็นไปตาม retention/access policy

## 12. Rollback และ Compatibility

- Supervisorอยู่หลัง feature flag
- API fieldใหม่เป็น optional; HTTP 503ใช้เฉพาะ hard worker failure
- controlled timeout HTTP 200เดิมไม่เปลี่ยน
- เริ่ม worker pool 1ใน stagingก่อนขยายเป็น 4
- หาก IPC/supervisorไม่เสถียร ให้ rollback process isolationแต่คง hard API deadlineและ diagnostics; ห้ามนำไป Productionจน containmentผ่าน
- Event Log/faulthandlerเปิดได้โดยไม่เปิด dumps
- diagnostics artifactsแยกจาก application reports

Rollback triggers:

- parent API crash
- replacement loopมากกว่า 3ครั้งใน 60วินาที
- resource leak
- worker startup P95เกิน thresholdจน capacityหาย
- sensitive dataปรากฏใน diagnostic artifact

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 Hard Deadline และ Supervisor Contract](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [71 Bounded Game Resolver](71_bounded_game_entity_resolver_plan_20260901.md)
- [72 Request Context Cleanup](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [74 Local LLM Health](74_local_llm_budget_health_and_fallback_plan_20260901.md)
- [76 Crash-resilient Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 Load Test และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: Parent Logger 76ต้องมาก่อน diagnosis matrix; RequestBudget/Supervisor interface 69ต้องเป็น authorityเดียวของ termination และ rolloutสุดท้ายต้องยืนยันบน target hardwareตาม 77
