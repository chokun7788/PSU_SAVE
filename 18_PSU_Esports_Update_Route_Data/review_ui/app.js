(function () {
  const items = Array.isArray(window.REVIEW_ITEMS) ? window.REVIEW_ITEMS : [];
  const storageKey = "psu_esports_human_review_v1";
  const decisions = [
    ["pass", "ผ่าน ใช้ได้เลย"],
    ["minor_fix", "ถูก แต่ควรปรับคำพูด/เรียงคำตอบ"],
    ["major_fix", "ผิดประเด็น ผิดราคา ผิดกฎ หรือเสี่ยงเข้าใจผิด"],
    ["needs_data", "ไม่มีข้อมูลจริง ต้องขอข้อมูลเพิ่ม"],
    ["needs_policy", "ต้องถามศูนย์/ผู้ดูแล เพราะเป็นเรื่องกฎหรือนโยบาย"],
  ];
  const scoreDescriptions = {
    4: "ดีแล้ว ใช้จริงได้ ตอบตรง อ่านง่าย",
    3: "ถูก แต่ยังเรียงคำตอบ/เติมรายละเอียดได้อีกนิด",
    2: "มีส่วนถูก แต่ทำให้ลูกค้าเข้าใจผิดได้",
    1: "ตอบผิดเป็นหลัก แต่ยังเกี่ยวข้องนิดหน่อย",
    0: "ผิด/มั่ว/ไม่มีข้อมูลแต่ตอบเหมือนมี",
  };
  const scoreFields = [
    ["intent_score_0_4", "ตรงเจตนาคำถาม"],
    ["correctness_score_0_4", "ความถูกต้อง"],
    ["completeness_score_0_4", "ความครบถ้วน"],
    ["tone_score_0_4", "น้ำเสียง/อ่านง่าย"],
    ["route_score_0_4", "Route เหมาะไหม"],
  ];
  const errorTags = [
    "intent_miss",
    "wrong_number",
    "incomplete",
    "too_verbose",
    "ambiguous_question",
    "missing_data",
    "wrong_route",
    "source_issue",
    "tone_issue",
  ];

  const state = {
    selectedIndex: 0,
    search: "",
    category: "all",
    decision: "all",
    reviews: loadReviews(),
  };

  const els = {
    summaryText: document.getElementById("summaryText"),
    exportJsonBtn: document.getElementById("exportJsonBtn"),
    exportMdBtn: document.getElementById("exportMdBtn"),
    resetBtn: document.getElementById("resetBtn"),
    searchInput: document.getElementById("searchInput"),
    categoryFilter: document.getElementById("categoryFilter"),
    decisionFilter: document.getElementById("decisionFilter"),
    itemList: document.getElementById("itemList"),
    emptyState: document.getElementById("emptyState"),
    reviewDetail: document.getElementById("reviewDetail"),
    metaLine: document.getElementById("metaLine"),
    questionTitle: document.getElementById("questionTitle"),
    aiAnswer: document.getElementById("aiAnswer"),
    expectedText: document.getElementById("expectedText"),
    decisionButtons: document.getElementById("decisionButtons"),
    scoreGrid: document.getElementById("scoreGrid"),
    notesInput: document.getElementById("notesInput"),
    fixInput: document.getElementById("fixInput"),
    tagButtons: document.getElementById("tagButtons"),
    prevBtn: document.getElementById("prevBtn"),
    markReviewedBtn: document.getElementById("markReviewedBtn"),
    nextBtn: document.getElementById("nextBtn"),
  };

  function defaultReview(item) {
    return {
      question_id: item.question_id,
      human_decision: "",
      intent_score_0_4: null,
      correctness_score_0_4: null,
      completeness_score_0_4: null,
      tone_score_0_4: null,
      route_score_0_4: null,
      error_tags: [],
      reviewer_notes: "",
      fix_suggestion: "",
      reviewed_at: "",
    };
  }

  function loadReviews() {
    try {
      const raw = localStorage.getItem(storageKey);
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  }

  function saveReviews() {
    localStorage.setItem(storageKey, JSON.stringify(state.reviews));
  }

  function getReview(item) {
    if (!state.reviews[item.question_id]) {
      state.reviews[item.question_id] = defaultReview(item);
    }
    return state.reviews[item.question_id];
  }

  function filteredItems() {
    const search = state.search.trim().toLowerCase();
    return items.filter((item) => {
      const review = getReview(item);
      const decision = review.human_decision || "unreviewed";
      const haystack = [
        item.question_id,
        item.question,
        item.ai_answer,
        item.route,
        item.category,
      ].join(" ").toLowerCase();
      const matchSearch = !search || haystack.includes(search);
      const matchCategory = state.category === "all" || item.category === state.category;
      const matchDecision = state.decision === "all" || decision === state.decision;
      return matchSearch && matchCategory && matchDecision;
    });
  }

  function updateSummary() {
    const reviewed = items.filter((item) => getReview(item).human_decision).length;
    const current = items[state.selectedIndex];
    els.summaryText.textContent = `${reviewed}/${items.length} reviewed` + (current ? ` | กำลังดู ${current.question_id}` : "");
  }

  function renderCategoryFilter() {
    const categories = Array.from(new Set(items.map((item) => item.category))).sort();
    els.categoryFilter.innerHTML = "";
    const all = document.createElement("option");
    all.value = "all";
    all.textContent = "ทุกหมวด";
    els.categoryFilter.appendChild(all);
    categories.forEach((category) => {
      const option = document.createElement("option");
      option.value = category;
      option.textContent = category;
      els.categoryFilter.appendChild(option);
    });
  }

  function renderList() {
    const visible = filteredItems();
    els.itemList.innerHTML = "";
    visible.forEach((item) => {
      const originalIndex = items.indexOf(item);
      const review = getReview(item);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "itemButton" + (originalIndex === state.selectedIndex ? " active" : "");
      button.innerHTML = `
        <span class="itemTop">
          <span>${item.review_no}. ${item.question_id}</span>
          <span class="badge ${review.human_decision || ""}">${review.human_decision || "unreviewed"}</span>
        </span>
        <span class="itemQuestion">${escapeHtml(item.question)}</span>
        <span class="itemTop">
          <span>${escapeHtml(item.category || "-")}</span>
          <span>${escapeHtml(item.route || "-")}</span>
        </span>
      `;
      button.addEventListener("click", () => {
        state.selectedIndex = originalIndex;
        render();
      });
      els.itemList.appendChild(button);
    });
  }

  function renderDetail() {
    const item = items[state.selectedIndex];
    if (!item) {
      els.emptyState.classList.remove("hidden");
      els.reviewDetail.classList.add("hidden");
      return;
    }

    els.emptyState.classList.add("hidden");
    els.reviewDetail.classList.remove("hidden");

    const review = getReview(item);
    els.metaLine.innerHTML = `
      <span class="badge">${escapeHtml(item.question_id)}</span>
      <span class="badge">${escapeHtml(item.category || "-")}</span>
      <span class="badge">${escapeHtml(item.answer_type || "-")}</span>
      <span class="badge">${escapeHtml(item.route || "-")}</span>
      <span class="badge ${item.auto_verdict === "PASS" ? "pass" : "major_fix"}">auto ${escapeHtml(item.auto_verdict || "-")}</span>
    `;
    els.questionTitle.textContent = `${item.review_no}. ${item.question}`;
    els.aiAnswer.textContent = item.ai_answer || "";
    els.expectedText.textContent = `keywords: ${(item.expected_keywords || []).join(", ")} | source: ${(item.expected_source_keywords || []).join(", ")}`;
    els.notesInput.value = review.reviewer_notes || "";
    els.fixInput.value = review.fix_suggestion || "";

    renderDecisionButtons(item, review);
    renderScoreButtons(item, review);
    renderTagButtons(item, review);
  }

  function renderDecisionButtons(item, review) {
    els.decisionButtons.innerHTML = "";
    decisions.forEach(([decision, description]) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "choiceButton decisionChoice" + (review.human_decision === decision ? " selected" : "");
      button.innerHTML = `
        <span class="choiceMain">${escapeHtml(decision)}</span>
        <span class="choiceHelp">${escapeHtml(description)}</span>
      `;
      button.addEventListener("click", () => {
        review.human_decision = decision;
        review.reviewed_at = new Date().toISOString();
        saveReviews();
        render();
      });
      els.decisionButtons.appendChild(button);
    });
  }

  function renderScoreButtons(item, review) {
    els.scoreGrid.innerHTML = "";
    scoreFields.forEach(([field, label]) => {
      const row = document.createElement("div");
      row.className = "scoreRow";
      const title = document.createElement("strong");
      title.textContent = label;
      const buttons = document.createElement("div");
      buttons.className = "scoreButtons";
      for (let score = 0; score <= 4; score += 1) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "choiceButton" + (review[field] === score ? " selected" : "");
        button.textContent = String(score);
        button.title = scoreDescriptions[score];
        button.setAttribute("aria-label", `${label} ${score}: ${scoreDescriptions[score]}`);
        button.addEventListener("click", () => {
          review[field] = score;
          review.reviewed_at = new Date().toISOString();
          saveReviews();
          renderDetail();
          renderList();
          updateSummary();
        });
        buttons.appendChild(button);
      }
      row.appendChild(title);
      row.appendChild(buttons);
      els.scoreGrid.appendChild(row);
    });
  }

  function renderTagButtons(item, review) {
    els.tagButtons.innerHTML = "";
    errorTags.forEach((tag) => {
      const selected = (review.error_tags || []).includes(tag);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "tagButton" + (selected ? " selected" : "");
      button.textContent = tag;
      button.addEventListener("click", () => {
        const tags = new Set(review.error_tags || []);
        if (tags.has(tag)) {
          tags.delete(tag);
        } else {
          tags.add(tag);
        }
        review.error_tags = Array.from(tags);
        review.reviewed_at = new Date().toISOString();
        saveReviews();
        renderDetail();
      });
      els.tagButtons.appendChild(button);
    });
  }

  function persistTextFields() {
    const item = items[state.selectedIndex];
    if (!item) return;
    const review = getReview(item);
    review.reviewer_notes = els.notesInput.value;
    review.fix_suggestion = els.fixInput.value;
    review.reviewed_at = new Date().toISOString();
    saveReviews();
  }

  function markReviewed() {
    const item = items[state.selectedIndex];
    if (!item) return;
    const review = getReview(item);
    persistTextFields();
    if (!review.human_decision) {
      review.human_decision = "pass";
    }
    review.reviewed_at = new Date().toISOString();
    saveReviews();
    render();
  }

  function exportRows() {
    return items.map((item) => ({
      ...item,
      human_review: getReview(item),
    }));
  }

  function exportJson() {
    persistTextFields();
    downloadFile(
      "psu_esports_human_review_export.json",
      JSON.stringify(exportRows(), null, 2),
      "application/json"
    );
  }

  function exportMarkdown() {
    persistTextFields();
    const lines = ["# PSU Esports Human Review Export", ""];
    exportRows().forEach((row) => {
      const review = row.human_review;
      lines.push(`## ${row.review_no}. ${row.question_id}`);
      lines.push("");
      lines.push(`คำถาม: ${row.question}`);
      lines.push("");
      lines.push(`Decision: ${review.human_decision || ""}`);
      lines.push(`ตรงเจตนา: ${valueOrBlank(review.intent_score_0_4)}/4`);
      lines.push(`ถูกต้อง: ${valueOrBlank(review.correctness_score_0_4)}/4`);
      lines.push(`ครบถ้วน: ${valueOrBlank(review.completeness_score_0_4)}/4`);
      lines.push(`น้ำเสียง: ${valueOrBlank(review.tone_score_0_4)}/4`);
      lines.push(`Route: ${valueOrBlank(review.route_score_0_4)}/4`);
      lines.push(`Tags: ${(review.error_tags || []).join(", ")}`);
      lines.push("");
      lines.push("หมายเหตุ:");
      lines.push(review.reviewer_notes || "");
      lines.push("");
      lines.push("สิ่งที่ควรแก้:");
      lines.push(review.fix_suggestion || "");
      lines.push("");
    });
    downloadFile("psu_esports_human_review_export.md", lines.join("\n"), "text/markdown");
  }

  function downloadFile(filename, text, type) {
    const blob = new Blob([text], { type: `${type};charset=utf-8` });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  function valueOrBlank(value) {
    return value === null || value === undefined ? "" : value;
  }

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function go(delta) {
    persistTextFields();
    const next = Math.min(Math.max(state.selectedIndex + delta, 0), items.length - 1);
    state.selectedIndex = next;
    render();
  }

  function resetAll() {
    const ok = window.confirm("ลบผลรีวิวที่กดไว้ใน browser นี้ทั้งหมดใช่ไหม?");
    if (!ok) return;
    localStorage.removeItem(storageKey);
    state.reviews = {};
    render();
  }

  function bindEvents() {
    els.searchInput.addEventListener("input", () => {
      state.search = els.searchInput.value;
      renderList();
    });
    els.categoryFilter.addEventListener("change", () => {
      state.category = els.categoryFilter.value;
      renderList();
    });
    els.decisionFilter.addEventListener("change", () => {
      state.decision = els.decisionFilter.value;
      renderList();
    });
    els.notesInput.addEventListener("input", persistTextFields);
    els.fixInput.addEventListener("input", persistTextFields);
    els.prevBtn.addEventListener("click", () => go(-1));
    els.nextBtn.addEventListener("click", () => go(1));
    els.markReviewedBtn.addEventListener("click", markReviewed);
    els.exportJsonBtn.addEventListener("click", exportJson);
    els.exportMdBtn.addEventListener("click", exportMarkdown);
    els.resetBtn.addEventListener("click", resetAll);
    document.addEventListener("keydown", (event) => {
      if (event.target instanceof HTMLTextAreaElement || event.target instanceof HTMLInputElement) {
        return;
      }
      if (event.key === "ArrowLeft") go(-1);
      if (event.key === "ArrowRight") go(1);
    });
  }

  function render() {
    renderList();
    renderDetail();
    updateSummary();
  }

  renderCategoryFilter();
  bindEvents();
  render();
})();
