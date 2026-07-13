const messagesEl = document.querySelector("#messages");
const formEl = document.querySelector("#chat-form");
const questionEl = document.querySelector("#question");
const sendButtonEl = document.querySelector("#send-button");
const clearButtonEl = document.querySelector("#clear-chat");
const debugOutputEl = document.querySelector("#debug-output");
const statusEl = document.querySelector("#status");
const dateChipEl = document.querySelector("#date-chip");
const sourceListEl = document.querySelector("#source-list");
const metricModeEl = document.querySelector("#metric-mode");
const metricRouteEl = document.querySelector("#metric-route");
const metricLatencyEl = document.querySelector("#metric-latency");
const metricConfidenceEl = document.querySelector("#metric-confidence");

function makeSessionId() {
  return window.crypto && crypto.randomUUID
    ? crypto.randomUUID()
    : `session-${Date.now()}`;
}

function saveMessages() {
  // Keep conversation context only in the current page lifetime.
}

let clientSessionId = makeSessionId();
const messages = [];
const experimentalRagFallback = true;
const experimentalAllowLlm = true;

function formatSeconds(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "-";
  if (number < 1) return `${Math.round(number * 1000)} ms`;
  return `${number.toFixed(2)} s`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function sourceLabel(source) {
  return source.id || source.url || "source";
}

function renderSources(sources) {
  sourceListEl.innerHTML = "";
  if (!sources || sources.length === 0) {
    sourceListEl.textContent = "ยังไม่มีแหล่งข้อมูล";
    return;
  }

  for (const source of sources) {
    const item = document.createElement("div");
    item.className = "source-item";
    const label = sourceLabel(source);
    if (source.url && source.url.startsWith("http")) {
      const link = document.createElement("a");
      link.href = source.url;
      link.target = "_blank";
      link.rel = "noreferrer";
      link.textContent = label;
      item.appendChild(link);
    } else {
      item.textContent = source.url ? `${label} (${source.url})` : label;
    }
    sourceListEl.appendChild(item);
  }
}

function renderMessages() {
  messagesEl.innerHTML = "";
  if (messages.length === 0) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "เริ่มถามได้เลย ระบบจะส่งคำถามเข้า local API แล้วแสดงคำตอบพร้อม route, mode และแหล่งข้อมูลที่ใช้";
    messagesEl.appendChild(empty);
    saveMessages();
    return;
  }

  for (const item of messages) {
    const wrapper = document.createElement("article");
    wrapper.className = `message ${item.role}`;

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = item.text;

    const meta = document.createElement("div");
    meta.className = "meta";
    meta.textContent = item.meta || (item.role === "user" ? "คุณ" : "AI");

    wrapper.appendChild(bubble);
    wrapper.appendChild(meta);
    messagesEl.appendChild(wrapper);
  }
  messagesEl.scrollTop = messagesEl.scrollHeight;
  saveMessages();
}

function recentHistory() {
  return messages
    .filter((item) => item.role === "user" || item.role === "assistant")
    .slice(-10)
    .map((item) => ({
      role: item.role,
      text: item.text,
    }));
}

function setLoading(isLoading) {
  sendButtonEl.disabled = isLoading;
  clearButtonEl.disabled = isLoading;
  questionEl.disabled = isLoading;
  sendButtonEl.textContent = isLoading ? "รอคำตอบ" : "ส่ง";
}

function setStatus(ok, text) {
  statusEl.classList.toggle("is-error", !ok);
  statusEl.querySelector("span:last-child").textContent = text;
}

function updateMetrics(data) {
  metricModeEl.textContent = data.mode || "-";
  metricRouteEl.textContent = data.route_category && data.route_intent
    ? `${data.route_category}/${data.route_intent}`
    : "-";
  metricLatencyEl.textContent = formatSeconds(data.latency_sec);
  metricConfidenceEl.textContent = Number.isFinite(Number(data.confidence))
    ? Number(data.confidence).toFixed(2)
    : "-";
  if (data.server_date && data.server_date.label) {
    const timeSuffix = data.server_date.time ? ` ${data.server_date.time} น.` : "";
    dateChipEl.textContent = `${data.server_date.label}${timeSuffix}`;
  }
  renderSources(data.sources);
}

function clearMetrics() {
  metricModeEl.textContent = "-";
  metricRouteEl.textContent = "-";
  metricLatencyEl.textContent = "-";
  metricConfidenceEl.textContent = "-";
  sourceListEl.textContent = "ยังไม่มีแหล่งข้อมูล";
  debugOutputEl.textContent = "ยังไม่มีข้อมูล";
}

function appendPending() {
  messages.push({
    role: "system",
    text: "กำลังค้นข้อมูลและตรวจคำตอบ...",
    meta: "waiting",
    pending: true,
  });
  renderMessages();
}

function removePending() {
  const index = messages.findIndex((item) => item.pending);
  if (index >= 0) {
    messages.splice(index, 1);
  }
}

async function ask(question) {
  const cleanQuestion = question.trim();
  if (!cleanQuestion) return;

  messages.push({ role: "user", text: cleanQuestion, meta: "คุณ" });
  appendPending();
  setLoading(true);
  setStatus(true, "กำลังตอบ");

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: cleanQuestion,
        client_session_id: clientSessionId,
        recent_history: recentHistory(),
        debug: true,
        experimental_rag_fallback: experimentalRagFallback,
        experimental_allow_llm: experimentalAllowLlm,
      }),
    });

    const rawResponse = await response.text();
    let data;
    try {
      data = rawResponse ? JSON.parse(rawResponse) : {};
    } catch (_error) {
      const preview = rawResponse ? rawResponse.slice(0, 160) : "empty response";
      throw new Error(`API returned non-JSON (${response.status}): ${preview}`);
    }
    if (!response.ok || !data.ok) {
      throw new Error(data.detail || data.error || "API error");
    }

    removePending();
    const meta = [
      data.mode || "unknown",
      data.route_category && data.route_intent ? `${data.route_category}/${data.route_intent}` : "no-route",
      formatSeconds(data.latency_sec),
    ].join(" | ");

    messages.push({
      role: "assistant",
      text: data.answer,
      meta,
    });

    updateMetrics(data);
    debugOutputEl.textContent = JSON.stringify({
      mode: data.mode,
      route_category: data.route_category,
      route_intent: data.route_intent,
      confidence: data.confidence,
      latency_sec: data.latency_sec,
      experimental_rag_fallback: data.experimental_rag_fallback,
      experimental_allow_llm: data.experimental_allow_llm,
      server_date: data.server_date,
      sources: data.sources,
      entities: data.entities,
      validation: data.validation,
      trace: data.trace,
    }, null, 2);
    setStatus(true, "Local API");
  } catch (error) {
    removePending();
    messages.push({
      role: "system",
      text: `เรียก API ไม่สำเร็จ: ${error.message}`,
      meta: "error",
    });
    debugOutputEl.textContent = String(error.stack || error);
    setStatus(false, "API error");
  } finally {
    setLoading(false);
    questionEl.value = "";
    questionEl.focus();
    renderMessages();
  }
}

async function checkHealth() {
  try {
    const response = await fetch("/health");
    const data = await response.json();
    if (!response.ok || !data.ok) throw new Error(data.error || "health check failed");
    setStatus(true, "Local API");
  } catch (error) {
    setStatus(false, "API offline");
  }
}

formEl.addEventListener("submit", (event) => {
  event.preventDefault();
  ask(questionEl.value);
});

questionEl.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    formEl.requestSubmit();
  }
});

clearButtonEl.addEventListener("click", () => {
  messages.length = 0;
  clientSessionId = makeSessionId();
  clearMetrics();
  renderMessages();
  questionEl.focus();
});

for (const button of document.querySelectorAll(".sample-button")) {
  button.addEventListener("click", () => {
    questionEl.value = button.dataset.question || "";
    questionEl.focus();
  });
}

dateChipEl.textContent = new Intl.DateTimeFormat("th-TH", {
  dateStyle: "medium",
  timeZone: "Asia/Bangkok",
}).format(new Date());

clearMetrics();
renderMessages();
checkHealth();
