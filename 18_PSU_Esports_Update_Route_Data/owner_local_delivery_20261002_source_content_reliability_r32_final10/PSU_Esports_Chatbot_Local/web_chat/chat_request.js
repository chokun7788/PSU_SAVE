/* Bounded retry for rejected queue admission only. A timeout, network failure,
 * server exception or successful answer is never replayed automatically. */
(function (root) {
  async function requestChat(payload, options = {}) {
    const fetchImpl = options.fetchImpl || root.fetch.bind(root);
    const sleep = options.sleep || ((ms) => new Promise((resolve) => setTimeout(resolve, ms)));
    const now = options.now || (() => Date.now());
    const started = now();
    const body = JSON.stringify(payload);
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
