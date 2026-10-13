/* Bounded retry for rejected queue admission only. A timeout, network failure,
 * server exception or successful answer is never replayed automatically. */
(function (root) {
  async function requestChat(payload, options = {}) {
    const fetchImpl = options.fetchImpl || root.fetch.bind(root);
    const sleep = options.sleep || ((ms) => new Promise((resolve) => setTimeout(resolve, ms)));
    const now = options.now || (() => Date.now());
    const started = now();
    const body = JSON.stringify(payload);
    const readJson = async (response) => {
      const raw = await response.text();
      try { return raw ? JSON.parse(raw) : {}; }
      catch (_) { throw new Error(`API returned non-JSON (${response.status}): ${raw.slice(0,160) || 'empty response'}`); }
    };
    // Admission is durable before 202. Never replay after an ambiguous network failure.
    const jobResponse = await fetchImpl('/api/chat/jobs', {method:'POST',headers:{'Content-Type':'application/json'},body});
    let jobData = await readJson(jobResponse);
    if (jobResponse.status !== 404 || !['jobs_disabled','not_found'].includes(jobData.error)) {
      if (jobResponse.status !== 202) return {response:jobResponse,data:jobData};
      const jobId = jobData.job_id;
      const sessionId = jobData.session_id;
      while (true) {
        const english = payload.locale === 'en';
        const elapsed = Number((jobData.timing || {}).elapsed_sec);
        const elapsedText = Number.isFinite(elapsed) ? (english ? ` (${Math.floor(elapsed)} s elapsed)` : ` (ผ่านไป ${Math.floor(elapsed)} วินาที)`) : '';
        if (options.onRetry) options.onRetry({job_status:jobData.status,language:{effective:english?'en':'th'},message:(jobData.status === 'running' ? (english?'Processing your question…':'กำลังประมวลผลคำถาม…') : (english?'Question received. Waiting in the queue…':'รับคำถามแล้ว กำลังรอคิว…')) + elapsedText},0);
        if (jobData.status === 'completed') return {response:jobResponse,data:jobData.result};
        if (['failed','cancelled'].includes(jobData.status)) return {response:jobResponse,data:{ok:false,error:jobData.error || jobData.status,job_id:jobId,session_id:sessionId,retryable:false,message:jobData.error === 'queue_expired' ? (english?'The queue time limit was reached. Please try again.':'หมดเวลารอคิว กรุณาลองใหม่') : (english?'The request did not complete. Please try again.':'ยังตอบคำถามนี้ไม่สำเร็จ กรุณาลองใหม่')}};
        if (now()-started > 185000) throw new Error(`Job polling timed out; job ${jobId} remains available for recovery.`);
        await sleep(400);
        const polled = await fetchImpl(`/api/chat/jobs/${encodeURIComponent(jobId)}?session_id=${encodeURIComponent(sessionId)}`);
        jobData = await readJson(polled);
        if (!polled.ok || !jobData.ok) return {response:polled,data:jobData};
      }
    }
    for (let attempt = 0; attempt < 3; attempt += 1) {
      const response = await fetchImpl('/api/chat', {method: 'POST', headers: {'Content-Type': 'application/json'}, body});
      const raw = await response.text();
      let data;
      try { data = raw ? JSON.parse(raw) : {}; }
      catch (_) { throw new Error(`API returned non-JSON (${response.status}): ${raw.slice(0,160) || 'empty response'}`); }
      const queueRejected = response.status === 503 && data.ok === false && data.retryable === true
        && ['server_busy', 'pipeline_worker_restarting'].includes(data.error);
      const suggested = Number(data.retry_after_ms);
      const delay = Number.isFinite(suggested) && suggested > 0 ? Math.min(1500, Math.max(250,suggested)) : 500;
      if (!queueRejected || attempt === 2 || now() - started + delay > 12000) return {response, data};
      if (options.onRetry) options.onRetry(data, attempt + 1);
      await sleep(delay);
    }
  }
  root.PSUChatRequest = {requestChat};
  if (typeof module !== 'undefined' && module.exports) module.exports = root.PSUChatRequest;
})(typeof globalThis !== 'undefined' ? globalThis : this);
