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
const localeSwitchEl = document.querySelector("#locale-switch");
const samplesHeadingEl = document.querySelector("#samples-heading");
const metricsHeadingEl = document.querySelector("#metrics-heading");
const runtimeHeadingEl = document.querySelector("#runtime-heading");
const runtimeListEl = document.querySelector("#runtime-list");
const sourcesHeadingEl = document.querySelector("#sources-heading");
const questionLabelEl = document.querySelector("#question-label");
const debugSummaryEl = document.querySelector("#debug-summary");
const sidePanelEl = document.querySelector(".side-panel");
const conversationEl = document.querySelector(".conversation");

const localeCopy = {
  th: {
    samples: "ตัวอย่างคำถาม",
    metrics: "ข้อมูลคำตอบล่าสุด",
    runtime: "สถานะระบบที่กำลังใช้งาน",
    sources: "แหล่งข้อมูล",
    noSources: "ยังไม่มีแหล่งข้อมูล",
    empty: "เริ่มถามได้เลย ระบบจะแสดงคำตอบพร้อม route, mode และแหล่งข้อมูลที่ใช้",
    placeholder: "พิมพ์คำถามเกี่ยวกับราคา เวลาเปิด-ปิด การจอง กฎศูนย์ หรือกติกาการแข่งขัน",
    clear: "ล้าง",
    send: "ส่ง",
    waiting: "รอคำตอบ",
    pending: "กำลังค้นข้อมูลและตรวจคำตอบ...",
    answering: "กำลังตอบ",
    user: "คุณ",
    retype: "กรุณาพิมพ์ใหม่",
    checkAgain: "ตรวจคำอีกครั้ง",
    debug: "ดู JSON debug ล่าสุด",
    noDebug: "ยังไม่มีข้อมูล",
    apiFailure: "เรียก API ไม่สำเร็จ",
    sideLabel: "ตัวอย่างคำถามและข้อมูลระบบ",
    conversationLabel: "บทสนทนา",
    languageLabel: "ภาษาคำตอบ",
    localApi: "Local API",
    apiError: "API ขัดข้อง",
    apiOffline: "API ออฟไลน์",
    feedbackCorrect: "ถูกต้อง",
    feedbackIncorrect: "ไม่ตรง",
    feedbackSaved: "บันทึกแล้ว",
  },
  en: {
    samples: "Example questions",
    metrics: "Latest answer",
    runtime: "Active runtime",
    sources: "Sources",
    noSources: "No sources yet",
    empty: "Ask a question to see the answer, route, mode, and verified sources.",
    placeholder: "Ask about prices, opening hours, booking, studio rules, or competition rules",
    clear: "Clear",
    send: "Send",
    waiting: "Waiting",
    pending: "Finding evidence and checking the answer...",
    answering: "Answering",
    user: "You",
    retype: "Please retype",
    checkAgain: "Check the text",
    debug: "View latest JSON debug data",
    noDebug: "No data yet",
    apiFailure: "API request failed",
    sideLabel: "Example questions and system information",
    conversationLabel: "Conversation",
    languageLabel: "Answer language",
    localApi: "Local API",
    apiError: "API error",
    apiOffline: "API offline",
    feedbackCorrect: "Correct",
    feedbackIncorrect: "Not quite",
    feedbackSaved: "Saved",
  },
};

const storedLocale = localStorage.getItem("psu-chat-locale");
let selectedLocale = ["auto", "th", "en"].includes(storedLocale) ? storedLocale : "auto";
let uiLocale = selectedLocale === "en" ? "en" : "th";
let englishEnabled = false;

function applyEnglishFeatureAvailability(enabled) {
  englishEnabled = Boolean(enabled);
  const englishButton = localeSwitchEl.querySelector('[data-locale="en"]');
  if (englishButton) englishButton.hidden = !englishEnabled;
  if (!englishEnabled && selectedLocale === "en") {
    selectedLocale = "auto";
    localStorage.setItem("psu-chat-locale", selectedLocale);
    applyUiLanguage("th");
  }
}

function copy() {
  return localeCopy[uiLocale];
}

function renderDate() {
  dateChipEl.textContent = new Intl.DateTimeFormat(uiLocale === "en" ? "en-GB" : "th-TH", {
    dateStyle: "medium",
    timeZone: "Asia/Bangkok",
  }).format(new Date());
}

function applyUiLanguage(language) {
  uiLocale = language === "en" ? "en" : "th";
  const text = copy();
  document.documentElement.lang = uiLocale;
  localeSwitchEl.setAttribute("aria-label", text.languageLabel);
  sidePanelEl.setAttribute("aria-label", text.sideLabel);
  conversationEl.setAttribute("aria-label", text.conversationLabel);
  samplesHeadingEl.textContent = text.samples;
  metricsHeadingEl.textContent = text.metrics;
  runtimeHeadingEl.textContent = text.runtime;
  sourcesHeadingEl.textContent = text.sources;
  questionLabelEl.textContent = text.placeholder;
  questionEl.placeholder = text.placeholder;
  clearButtonEl.textContent = text.clear;
  sendButtonEl.textContent = text.send;
  debugSummaryEl.textContent = text.debug;
  for (const button of document.querySelectorAll(".sample-button")) {
    button.textContent = uiLocale === "en" ? button.dataset.labelEn : button.dataset.labelTh;
  }
  for (const button of localeSwitchEl.querySelectorAll("button")) {
    button.setAttribute("aria-pressed", String(button.dataset.locale === selectedLocale));
  }
  if (!sourceListEl.querySelector(".source-item")) {
    sourceListEl.textContent = text.noSources;
  }
  if (debugOutputEl.textContent === localeCopy.th.noDebug || debugOutputEl.textContent === localeCopy.en.noDebug) {
    debugOutputEl.textContent = text.noDebug;
  }
  renderDate();
  renderMessages();
}

function makeSessionId() {
  return window.crypto && crypto.randomUUID
    ? crypto.randomUUID()
    : `session-${Date.now()}`;
}

const sessionStorageKey = "psu-chat-session-id";
const transcriptStorageKey = "psu-chat-transcript-v1";
const maxSavedMessages = 500;

function loadOrCreateSessionId() {
  const saved = localStorage.getItem(sessionStorageKey);
  if (saved && /^[A-Za-z0-9][A-Za-z0-9._-]{15,127}$/.test(saved)) return saved;
  const created = makeSessionId();
  localStorage.setItem(sessionStorageKey, created);
  return created;
}

function saveMessages() {
  // Browser storage makes refresh resilient immediately; SQLite remains the
  // authoritative local transcript and is loaded on startup below.
  const serializable = messages
    .filter((item) => !item.pending && (item.role === "user" || item.role === "assistant" || item.role === "system"))
    .slice(-maxSavedMessages)
    .map((item) => ({
      role: item.role,
      text: String(item.text || ""),
      meta: String(item.meta || ""),
      universalIntent: item.universalIntent || null,
      routeCategory: item.routeCategory || "",
      routeIntent: item.routeIntent || "",
      resolvedText: item.resolvedText || "",
      contextEligible: item.contextEligible !== false,
      notice: item.notice || "",
      answerLanguage: item.answerLanguage || "",
      requestId: item.requestId || "",
      question: item.question || "",
      inputRecovery: item.inputRecovery || null,
      feedback: item.feedback || "",
    }));
  try {
    localStorage.setItem(transcriptStorageKey, JSON.stringify(serializable));
  } catch (_error) {
    // The server transcript remains available when browser storage is full.
  }
}

function restoreCachedMessages() {
  try {
    const cached = JSON.parse(localStorage.getItem(transcriptStorageKey) || "[]");
    if (!Array.isArray(cached)) return;
    for (const item of cached.slice(-maxSavedMessages)) {
      if (!item || !["user", "assistant", "system"].includes(item.role) || !String(item.text || "").trim()) continue;
      messages.push({ ...item, pending: false });
    }
  } catch (_error) {
    localStorage.removeItem(transcriptStorageKey);
  }
}

function historyItemFromServer(item) {
  const metadata = item && typeof item.metadata === "object" && item.metadata ? item.metadata : {};
  const role = ["user", "assistant", "system"].includes(item.role) ? item.role : "system";
  const language = metadata.language && typeof metadata.language === "object" ? metadata.language.effective || "" : "";
  const routeCategory = String(item.route_category || "");
  const routeIntent = String(item.route_intent || "");
  const meta = role === "user"
    ? copy().user
    : role === "assistant"
      ? [String(item.mode || "unknown"), routeCategory && routeIntent ? `${routeCategory}/${routeIntent}` : "no-route", formatSeconds(item.latency_sec)].join(" | ")
      : "system";
  return {
    role,
    text: String(item.content || ""),
    meta,
    universalIntent: metadata.universal_intent || null,
    routeCategory,
    routeIntent,
    resolvedText: String(item.resolved_question || ""),
    contextEligible: role !== "system",
    answerLanguage: language,
    inputRecovery: metadata.input_recovery || null,
  };
}

async function restoreServerHistory() {
  try {
    const response = await fetch(`/api/session-history?session_id=${encodeURIComponent(clientSessionId)}`);
    const data = await response.json();
    if (!response.ok || !data.ok || !Array.isArray(data.messages) || data.messages.length === 0) return;
    const restored = data.messages.map(historyItemFromServer).filter((item) => item.text.trim());
    if (restored.length === 0) return;
    messages.length = 0;
    messages.push(...restored);
    const latestAssistant = [...data.messages].reverse().find((item) => item.role === "assistant");
    if (latestAssistant) renderSources(latestAssistant.sources || []);
    renderMessages();
  } catch (_error) {
    // Keep the local browser copy visible if the local service is not ready yet.
  }
}

let clientSessionId = loadOrCreateSessionId();
const messages = [];
const experimentalRagFallback = true;
const experimentalAllowLlm = ["localhost", "127.0.0.1"].includes(window.location.hostname);

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
    sourceListEl.textContent = copy().noSources;
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
    empty.textContent = copy().empty;
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
    meta.textContent = item.meta || (item.role === "user" ? copy().user : "AI");

    wrapper.appendChild(bubble);
    if (item.notice) {
      const notice = document.createElement("div");
      notice.className = "input-quality-notice";
      notice.textContent = item.notice;
      wrapper.appendChild(notice);
    }
    if (item.role === "assistant" && item.requestId) {
      const feedback = document.createElement("div");
      feedback.className = "answer-feedback";
      if (item.feedback) {
        feedback.textContent = copy().feedbackSaved;
      } else {
        const correct = document.createElement("button");
        correct.type = "button";
        correct.className = "feedback-button";
        correct.textContent = copy().feedbackCorrect;
        correct.addEventListener("click", () => submitIntentFeedback(item, "confirmed"));

        const incorrect = document.createElement("button");
        incorrect.type = "button";
        incorrect.className = "feedback-button";
        incorrect.textContent = copy().feedbackIncorrect;
        incorrect.addEventListener("click", () => submitIntentFeedback(item, "unclear"));
        feedback.append(correct, incorrect);
      }
      wrapper.appendChild(feedback);
    }
    wrapper.appendChild(meta);
    messagesEl.appendChild(wrapper);
  }
  messagesEl.scrollTop = messagesEl.scrollHeight;
  saveMessages();
}

async function submitIntentFeedback(item, outcome) {
  if (item.feedback) return;
  item.feedback = "pending";
  renderMessages();
  try {
    const response = await fetch("/api/intent-feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        request_id: item.requestId,
        question: item.question || "",
        observed_category: item.routeCategory || "",
        observed_intent: item.routeIntent || "",
        outcome,
        locale: item.answerLanguage || uiLocale,
        input_recovery: item.inputRecovery || {},
      }),
    });
    const data = await response.json();
    if (!response.ok || !data.ok) throw new Error(data.detail || data.error || "feedback failed");
    item.feedback = "saved";
  } catch (error) {
    item.feedback = "";
  }
  renderMessages();
}

function recentHistory() {
  return messages
    .filter((item) => (item.role === "user" || item.role === "assistant") && item.contextEligible !== false)
    .slice(-10)
    .map((item) => ({
      role: item.role,
      text: item.text,
      universal_intent: item.universalIntent || null,
      route_category: item.routeCategory || "",
      route_intent: item.routeIntent || "",
      resolved_text: item.resolvedText || "",
      answer_language: item.answerLanguage || "",
    }));
}

function setLoading(isLoading) {
  sendButtonEl.disabled = isLoading;
  clearButtonEl.disabled = isLoading;
  questionEl.disabled = isLoading;
  sendButtonEl.textContent = isLoading ? copy().waiting : copy().send;
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
    const iso = String(data.server_date.iso || "");
    const parsed = /^\d{4}-\d{2}-\d{2}$/.test(iso) ? new Date(`${iso}T12:00:00+07:00`) : null;
    const label = parsed
      ? new Intl.DateTimeFormat(uiLocale === "en" ? "en-GB" : "th-TH", {dateStyle: "medium", timeZone: "Asia/Bangkok"}).format(parsed)
      : data.server_date.label;
    const timeSuffix = data.server_date.time
      ? (uiLocale === "en" ? ` ${data.server_date.time}` : ` ${data.server_date.time} น.`)
      : "";
    dateChipEl.textContent = `${label}${timeSuffix}`;
  }
  renderSources(data.sources);
}

function clearMetrics() {
  metricModeEl.textContent = "-";
  metricRouteEl.textContent = "-";
  metricLatencyEl.textContent = "-";
  metricConfidenceEl.textContent = "-";
  sourceListEl.textContent = copy().noSources;
  debugOutputEl.textContent = copy().noDebug;
}

function renderRuntime(runtime) {
  if (!runtime) return;
  const isEnglish = uiLocale === "en";
  const on = isEnglish ? "On" : "เปิด";
  const off = isEnglish ? "Off" : "ปิด";
  const llm = runtime.local_llm || {};
  const rag = runtime.semantic_rag || {};
  const english = runtime.english || {};
  const rows = [
    ["Profile", runtime.profile || "-"],
    ["Version", runtime.version || "-"],
    ["Local LLM", llm.enabled ? `${on}: ${llm.model || "-"}` : off],
    ["Semantic RAG", rag.enabled ? `${on}: ${rag.embedding_model || "-"}` : off],
    ["English", english.enabled ? on : off],
    [isEnglish ? "English drafts" : "คำแปล Draft", english.draft_preview ? (isEnglish ? "Local preview only" : "ตัวอย่างเฉพาะเครื่อง") : off],
    [isEnglish ? "Answer limit" : "เวลาสูงสุด", `${runtime.answer_timeout_sec || "-"} s`],
  ];
  runtimeListEl.innerHTML = "";
  for (const [label, value] of rows) {
    const row = document.createElement("div");
    const term = document.createElement("dt");
    const description = document.createElement("dd");
    term.textContent = label;
    description.textContent = value;
    row.append(term, description);
    runtimeListEl.append(row);
  }
}

function appendPending() {
  messages.push({
    role: "system",
    text: copy().pending,
    meta: copy().waiting,
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

  const outgoingHistory = recentHistory();
  messages.push({ role: "user", text: cleanQuestion, meta: copy().user, contextEligible: true });
  appendPending();
  setLoading(true);
  setStatus(true, copy().answering);

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: cleanQuestion,
        client_session_id: clientSessionId,
        recent_history: outgoingHistory,
        locale: selectedLocale,
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
      throw new Error(data.message || data.detail || data.error || "API error");
    }

    if (data.session_id && /^[A-Za-z0-9][A-Za-z0-9._-]{15,127}$/.test(data.session_id)) {
      clientSessionId = data.session_id;
      localStorage.setItem(sessionStorageKey, clientSessionId);
    }

    removePending();
    const inputQuality = data.input_quality || null;
    const inputRejected = data.route_category === "input_guard";
    const inputContextExcluded = inputRejected || inputQuality?.applied_action === "warn_and_continue";
    if (inputContextExcluded) {
      const latestUser = [...messages].reverse().find((item) => item.role === "user" && item.contextEligible !== false);
      if (latestUser) {
        latestUser.contextEligible = false;
        latestUser.meta = `${copy().user} | ${inputRejected ? copy().retype : copy().checkAgain}`;
      }
    }
    const meta = [
      data.mode || "unknown",
      data.route_category && data.route_intent ? `${data.route_category}/${data.route_intent}` : "no-route",
      formatSeconds(data.latency_sec),
    ].join(" | ");

    messages.push({
      role: "assistant",
      text: data.answer,
      meta,
      universalIntent: data.universal_intent || null,
      routeCategory: data.route_category || "",
      routeIntent: data.route_intent || "",
      resolvedText: data.context_resolution ? data.context_resolution.resolved_question : "",
      contextEligible: !inputContextExcluded,
      notice: inputQuality && inputQuality.applied_action === "warn_and_continue" ? inputQuality.notice || "" : "",
      answerLanguage: data.language?.effective || uiLocale,
      requestId: data.request_id || "",
      question: cleanQuestion,
      inputRecovery: data.input_recovery || null,
    });

    if (selectedLocale === "auto" && data.language?.effective) {
      applyUiLanguage(data.language.effective);
    }

    updateMetrics(data);
    debugOutputEl.textContent = JSON.stringify({
      mode: data.mode,
      route_category: data.route_category,
      route_intent: data.route_intent,
      universal_intent: data.universal_intent,
      context_resolution: data.context_resolution,
      confidence: data.confidence,
      latency_sec: data.latency_sec,
      input_quality: inputQuality,
      language: data.language,
      experimental_rag_fallback: data.experimental_rag_fallback,
      experimental_allow_llm: data.experimental_allow_llm,
      server_date: data.server_date,
      sources: data.sources,
      entities: data.entities,
      validation: data.validation,
      trace: data.trace,
    }, null, 2);
    setStatus(true, copy().localApi);
  } catch (error) {
    removePending();
    messages.push({
      role: "system",
      text: `${copy().apiFailure}: ${error.message}`,
      meta: "error",
    });
    debugOutputEl.textContent = String(error.stack || error);
    setStatus(false, copy().apiError);
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
    applyEnglishFeatureAvailability(data.features?.bilingual_english === true);
    renderRuntime(data.runtime);
    setStatus(true, copy().localApi);
  } catch (error) {
    setStatus(false, copy().apiOffline);
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
  localStorage.setItem(sessionStorageKey, clientSessionId);
  localStorage.removeItem(transcriptStorageKey);
  clearMetrics();
  renderMessages();
  questionEl.focus();
});

for (const button of document.querySelectorAll(".sample-button")) {
  button.addEventListener("click", () => {
    questionEl.value = uiLocale === "en" ? button.dataset.questionEn || "" : button.dataset.questionTh || "";
    questionEl.focus();
  });
}

for (const button of localeSwitchEl.querySelectorAll("button")) {
  button.addEventListener("click", () => {
    if (button.dataset.locale === "en" && !englishEnabled) return;
    selectedLocale = button.dataset.locale;
    localStorage.setItem("psu-chat-locale", selectedLocale);
    if (selectedLocale === "th" || selectedLocale === "en") {
      applyUiLanguage(selectedLocale);
    } else {
      applyUiLanguage(uiLocale);
    }
    questionEl.focus();
  });
}

restoreCachedMessages();
clearMetrics();
applyEnglishFeatureAvailability(false);
applyUiLanguage(uiLocale);
checkHealth();
restoreServerHistory();
