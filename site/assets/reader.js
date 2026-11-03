(() => {
  const base = window.NETWORK_SITE_BASE || "";
  const byId = new Map();
  const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char]);
  const inline = (value) => esc(value)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/\[([^\]]+)\]\((https?:[^\s)]+)\)/g, '<a href="$2" rel="noreferrer">$1</a>');
  const routeFor = (unitIndex, lessonIndex, pageIndex) => `${base}/m2-network/unit/${unitIndex + 1}/lesson/${lessonIndex + 1}/page/${pageIndex + 1}`;
  const parseRoute = (course) => {
    const path = location.pathname.slice(base.length) || "/";
    const found = path.match(/\/m2-network\/unit\/(\d+)\/lesson\/(\d+)\/page\/(\d+)/);
    if (!found) return { unitIndex: 0, lessonIndex: 0, pageIndex: 0 };
    const unitIndex = Number(found[1]) - 1;
    const unit = course.units[unitIndex];
    const unitLessons = course.lessons.filter((lesson) => lesson.unit === unit?.id);
    const lesson = unitLessons[Number(found[2]) - 1];
    const lessonIndex = course.lessons.indexOf(lesson);
    return { unitIndex, lessonIndex: Math.max(0, lessonIndex), pageIndex: Number(found[3]) - 1 };
  };
  const imageSrc = (src) => src?.startsWith("/api/v1/network-course-assets/")
    ? `${base}/assets/course-assets/${src.slice("/api/v1/network-course-assets/".length)}`
    : src;
  const renderProse = (paragraphs = [], illustrations = [], inlineQuizzes = [], renderInlineQuiz = () => null) => {
    const prose = document.createElement("div");
    prose.className = "net-prose";
    let list = [];
    let ralSummary = null;
    let ralList = null;
    const ralLevel = (label) => ({
      R: "R", "기억해 두기": "R", "기억하기 (Recall)": "R", "회상할 핵심": "R",
      A: "A", "적용해 보기": "A", "적용하기 (Apply)": "A", "사례에 적용할 것": "A",
      L: "L", "필요할 때 찾아보기": "L", "찾아보기 (Lookup)": "L", "필요할 때 찾아볼 것": "L",
    })[label.trim().replace(/^[RAL]\s*·\s*/, "")] || null;
    const parseRalLine = (item) => {
      const match = item.match(/^(?:\*\*([^:*]+):\*\*|\*\*([^:*]+)\*\*:|([^:]+):)\s*([\s\S]+)$/);
      if (!match) return null;
      const level = ralLevel(match[1] || match[2] || match[3]);
      return level ? { level, detail: match[4] } : null;
    };
    const tableCells = (line) => line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((cell) => cell.trim());
    const isTable = (lines) => {
      if (lines.length < 2 || !lines[0].includes("|")) return false;
      const header = tableCells(lines[0]);
      const separator = tableCells(lines[1]);
      return header.length > 1 && separator.length === header.length && separator.every((cell) => /^:?-{3,}:?$/.test(cell));
    };
    const renderTable = (lines) => {
      const wrapper = document.createElement("div");
      wrapper.className = "net-table-scroll";
      wrapper.tabIndex = 0;
      wrapper.setAttribute("role", "region");
      wrapper.setAttribute("aria-label", "비교 표를 가로로 살펴보기");
      const hint = document.createElement("p");
      hint.className = "net-table-hint";
      hint.textContent = "좁은 화면에서는 표를 좌우로 움직여 전체 내용을 볼 수 있습니다.";
      const table = document.createElement("table");
      table.className = "net-table";
      const head = document.createElement("thead");
      const headRow = document.createElement("tr");
      tableCells(lines[0]).forEach((cell) => {
        const th = document.createElement("th");
        th.scope = "col";
        th.innerHTML = inline(cell);
        headRow.append(th);
      });
      head.append(headRow);
      table.append(head);
      const body = document.createElement("tbody");
      lines.slice(2).filter((line) => line.includes("|")).forEach((line) => {
        const row = document.createElement("tr");
        tableCells(line).forEach((cell) => {
          const td = document.createElement("td");
          td.innerHTML = inline(cell);
          row.append(td);
        });
        body.append(row);
      });
      table.append(body);
      wrapper.append(hint);
      wrapper.append(table);
      return wrapper;
    };
    const flush = () => {
      if (!list.length) return;
      const ul = document.createElement("ul");
      const ralItems = list.map(parseRalLine);
      if (ralSummary && ralItems.every(Boolean)) {
        ralList ||= (() => {
          const items = document.createElement("ul");
          items.className = "ral-summary__items";
          ralSummary.append(items);
          return items;
        })();
        ralItems.forEach((match) => {
          const { level, detail } = match;
          const li = document.createElement("li");
          li.className = "ral-summary__item";

          const marker = document.createElement("span");
          marker.className = "ral-summary__marker";
          marker.textContent = ({ R: "Recall", A: "Apply", L: "Lookup" })[level];

          const content = document.createElement("div");
          content.className = "ral-summary__content";
          const paragraph = document.createElement("p");
          paragraph.className = "ral-summary__detail";
          paragraph.innerHTML = inline(detail);
          content.append(paragraph);
          li.append(marker, content);
          ralList.append(li);
        });
      } else {
        list.forEach((item) => {
          const li = document.createElement("li");
          li.innerHTML = inline(item);
          ul.append(li);
        });
        (ralSummary || prose).append(ul);
      }
      list = [];
    };
    const byParagraph = new Map();
    illustrations.forEach((illustration) => {
      const index = Number.isInteger(illustration.after_paragraph) ? illustration.after_paragraph : -1;
      if (!byParagraph.has(index)) byParagraph.set(index, []);
      byParagraph.get(index).push(illustration);
    });
    const appendIllustrations = (index) => {
      const items = byParagraph.get(index) || [];
      if (!items.length) return;
      flush();
      items.forEach((illustration) => prose.append(renderIllustration(illustration)));
    };
    const appendQuizzes = (index) => {
      const items = inlineQuizzes.filter((quiz) => quiz.after_paragraph === index);
      if (!items.length) return;
      flush();
      items.forEach((quiz) => prose.append(renderInlineQuiz(quiz)));
    };
    appendIllustrations(-1);
    appendQuizzes(0);
    const blocks = paragraphs.flatMap((text) => {
      const headingAt = String(text).indexOf("\n### 이 Lesson에서 가져갈 것");
      if (headingAt < 0) return [text];
      return [String(text).slice(0, headingAt), "### 이 Lesson에서 가져갈 것"];
    }).filter((text) => String(text).length > 0);
    for (const [index, text] of blocks.entries()) {
      const lines = String(text).split("\n");
      const heading = lines.length === 1 ? text.match(/^(#{3,4})\s+(.+)$/) : null;
      if (heading) {
        flush();
        // ## is the page boundary and renders as the page H1; body ###/#### become H2/H3.
        if (heading[2].trim() === "이 Lesson에서 가져갈 것") {
          const section = document.createElement("section");
          section.className = "ral-summary";
          section.setAttribute("aria-label", "Lesson recap: Recall, Apply, Lookup");
          ralList = document.createElement("ul");
          ralList.className = "ral-summary__items";
          section.append(ralList);
          prose.append(section);
          ralSummary = section;
        } else {
          ralSummary = null;
          const element = document.createElement(heading[1].length === 3 ? "h2" : "h3");
          element.innerHTML = inline(heading[2]);
          prose.append(element);
        }
      } else if (isTable(lines)) {
        flush();
        prose.append(renderTable(lines));
      } else if (lines.length === 1 && /^\s*[-*]\s+/.test(text) && ralSummary && parseRalLine(text.replace(/^\s*[-*]\s+/, ""))) {
        const item = text.replace(/^\s*[-*]\s+/, "");
        if (!list.length) list.push(item);
        else list.push(item);
        flush();
      } else if (lines.length > 1 && lines.every((line) => /^\s*(?:[-*]|\d+\.)\s+/.test(line))) {
        list.push(...lines.map((line) => line.replace(/^\s*(?:[-*]|\d+\.)\s+/, "")));
      } else {
        flush();
        ralSummary = null;
        if (lines.length > 1) {
          const pre = document.createElement("pre");
          const code = document.createElement("code");
          code.textContent = text;
          pre.append(code);
          prose.append(pre);
        } else {
          const p = document.createElement("p");
          p.innerHTML = inline(text);
          prose.append(p);
        }
      }
      appendIllustrations(index);
      appendQuizzes(index + 1);
    }
    flush();
    if (ralSummary) prose.append(ralSummary);
    return prose;
  };
  const allItems = (course) => {
    const out = [];
    for (const unit of course.units) {
      for (const lesson of course.lessons.filter((item) => item.unit === unit.id)) out.push({ unit, lesson });
    }
    return out;
  };
  const controlFor = (object) => {
    const button = document.createElement("button");
    button.className = "illustration-control";
    button.type = "button";
    button.textContent = "❚❚ 일시정지";
    button.setAttribute("aria-label", "SVG 애니메이션 일시정지");
    let paused = false;
    const svg = () => { try { return object.contentDocument?.documentElement; } catch { return null; } };
    button.addEventListener("click", () => {
      const root = svg();
      if (!root) return;
      const doc = root.ownerDocument;
      if (paused) doc.documentElement.unpauseAnimations?.();
      else doc.documentElement.pauseAnimations?.();
      paused = !paused;
      button.textContent = paused ? "▶ 재생" : "❚❚ 일시정지";
      button.setAttribute("aria-label", paused ? "SVG 애니메이션 재생" : "SVG 애니메이션 일시정지");
    });
    return button;
  };
  const renderIllustration = (illustration) => {
    const figure = document.createElement("figure");
    figure.className = "illustration";
    const src = imageSrc(illustration.src);
    if (src?.toLowerCase().endsWith(".svg")) {
      const object = document.createElement("object");
      object.type = "image/svg+xml";
      object.data = src;
      object.setAttribute("aria-label", illustration.alt || illustration.title || "");
      object.setAttribute("title", illustration.alt || illustration.title || "");
      object.addEventListener("load", () => {
        try {
          const root = object.contentDocument?.documentElement;
          if (!root || !root.querySelector("animate, animateMotion, animateTransform, set")) return;
          figure.classList.add("has-animation-control");
          figure.append(controlFor(object));
          root.unpauseAnimations?.();
        } catch { /* Browser may block an inaccessible SVG document. */ }
      });
      figure.append(object);
    } else {
      const image = document.createElement("img");
      image.src = src;
      image.alt = illustration.alt || "";
      figure.append(image);
    }
    if (illustration.credit || illustration.source_url || illustration.license_url) {
      const credit = document.createElement("p");
      credit.className = "illustration-credit";
      if (illustration.credit) credit.append(document.createTextNode(`${illustration.credit} · `));
      if (illustration.source_url) {
        const source = document.createElement("a");
        source.href = illustration.source_url;
        source.target = "_blank";
        source.rel = "noreferrer noopener";
        source.textContent = "원본 출처";
        credit.append(source);
      }
      if (illustration.source_url && illustration.license_url) credit.append(document.createTextNode(" · "));
      if (illustration.license_url) {
        const license = document.createElement("a");
        license.href = illustration.license_url;
        license.target = "_blank";
        license.rel = "noreferrer noopener";
        license.textContent = illustration.license_label || "사용 허가";
        credit.append(license);
      }
      figure.append(credit);
    }
    return figure;
  };
  const renderVideo = (video) => {
    if (!video || !/^[A-Za-z0-9_-]{11}$/.test(video.video_id || "")) return null;
    const section = document.createElement("section");
    section.className = "page-video";
    section.setAttribute("aria-label", `보충 영상 · ${video.title || "YouTube"}`);
    const iframe = document.createElement("iframe");
    iframe.className = "page-video-player";
    iframe.title = video.title || "YouTube 영상";
    iframe.src = `https://www.youtube-nocookie.com/embed/${video.video_id}?autoplay=0&playsinline=1`;
    iframe.loading = "lazy";
    iframe.allow = "encrypted-media; picture-in-picture; fullscreen";
    iframe.referrerPolicy = "strict-origin-when-cross-origin";
    iframe.allowFullscreen = true;
    section.append(iframe);
    const note = document.createElement("p");
    note.className = "page-video-note";
    note.textContent = "[참고용] 가볍게 시청해 보세요.";
    section.append(note);
    const details = [video.title, video.creator].filter(Boolean);
    if (Number.isSafeInteger(video.duration_seconds) && video.duration_seconds > 0) {
      const minutes = Math.floor(video.duration_seconds / 60);
      const seconds = String(video.duration_seconds % 60).padStart(2, "0");
      details.push(`${minutes}:${seconds}`);
    }
    if (details.length) {
      const caption = document.createElement("p");
      caption.className = "page-video-caption";
      caption.textContent = details.join(" · ");
      section.append(caption);
    }
    return section;
  };
  const renderQuiz = (questions, startIndex = 0) => {
    const section = document.createElement("section");
    section.className = "page-quiz";
    section.setAttribute("aria-label", "이 페이지의 퀴즈");
    questions.forEach((question, index) => {
      const card = document.createElement("fieldset");
      card.className = "page-quiz-question";
      const legend = document.createElement("legend");
      legend.textContent = `${startIndex + index + 1}. ${question.prompt}`;
      card.append(legend);
      const result = document.createElement("p");
      result.className = "page-quiz-result";
      result.setAttribute("role", "status");
      result.setAttribute("aria-live", "polite");
      const grade = (answer, feedback) => {
        const correct = question.kind === "short"
          ? question.answers.some((value) => value.trim().toLowerCase() === answer.trim().toLowerCase())
          : answer === question.answer;
        result.dataset.correct = String(correct);
        result.textContent = `${correct ? "정답입니다." : "다시 생각해 보세요."} ${feedback}`;
      };
      if (question.kind === "choice") {
        const choices = [...question.choices];
        for (let position = choices.length - 1; position > 0; position -= 1) {
          const swapWith = Math.floor(Math.random() * (position + 1));
          [choices[position], choices[swapWith]] = [choices[swapWith], choices[position]];
        }
        choices.forEach((choice) => {
          const label = document.createElement("label");
          label.className = "page-quiz-choice";
          const input = document.createElement("input");
          input.type = "radio";
          input.name = question.id;
          input.value = choice.id;
          input.addEventListener("change", () => grade(choice.id, choice.feedback));
          const text = document.createElement("span");
          text.textContent = choice.text;
          label.append(input, text);
          card.append(label);
        });
      } else {
        const form = document.createElement("form");
        const input = document.createElement("input");
        input.type = "text";
        input.maxLength = 80;
        input.autocomplete = "off";
        input.value = question.answers?.[0] || "";
        input.setAttribute("aria-label", question.prompt);
        const submit = document.createElement("button");
        submit.type = "submit";
        submit.textContent = "확인";
        form.append(input, submit);
        form.addEventListener("submit", (event) => {
          event.preventDefault();
          if (input.value.trim()) grade(input.value, question.feedback);
        });
        card.append(form);
      }
      card.append(result);
      section.append(card);
    });
    return section;
  };
  // --- Glossary terms (#94): emoji, hover/focus/tap explanation, "더 자세히 보기" link. ---
  const isWordChar = (ch) => /[A-Za-z0-9가-힣]/.test(ch || "");
  const termAt = (text, alias) => {
    // Earliest boundary-respecting match of alias (case-insensitive) in text, or -1.
    const lower = text.toLowerCase(); const needle = alias.toLowerCase(); const ascii = /^[\x00-\x7f]+$/.test(needle);
    for (let from = 0; ;) {
      const at = lower.indexOf(needle, from);
      if (at < 0) return -1;
      const before = text[at - 1]; const after = text[at + needle.length];
      if (!isWordChar(before) && (!ascii || !isWordChar(after))) return at;
      from = at + 1;
    }
  };
  const decorateTerms = (prose, course, item, page) => {
    if (!course.glossary?.length) return;
    const lessonId = item.lesson.id;
    const excluded = new Set(page.term_exclude || []);
    const position = new Map(); let offset = 0;
    for (const entry of allItems(course)) { position.set(entry.lesson.id, offset); offset += (entry.lesson.pages || []).length; }
    const here = position.get(lessonId) + (course.lessons.find((l) => l.id === lessonId)?.pages || []).indexOf(page);
    const candidates = course.glossary.filter((term) => !excluded.has(term.id)
      && (!term.only_in || term.only_in.includes(lessonId)) && !(term.not_in || []).includes(lessonId)
      && (term.aliases || []).length);
    const used = new Set();
    const where = (term) => {
      const a = term.anchor; const target = a && allItems(course).find((entry) => entry.lesson.id === a.lesson);
      if (!target) return null;
      const unitIndex = course.units.findIndex((unit) => unit.id === target.unit.id);
      const lessonIndex = course.lessons.filter((l) => l.unit === target.unit.id).indexOf(target.lesson);
      return { unitIndex, lessonIndex, pageIndex: a.page_index - 1, pos: position.get(a.lesson) + a.page_index - 1 };
    };
    const make = (term, text) => {
      const dest = where(term); const later = dest && dest.pos > here;
      const wrap = document.createElement("span"); wrap.className = "term-wrap";
      const button = document.createElement("button"); button.type = "button";
      button.className = `term${later ? " term--later" : ""}${term.emoji ? "" : " term--plain"}`;
      if (term.emoji && !later) { const e = document.createElement("span"); e.className = "term-emoji"; e.setAttribute("aria-hidden", "true"); e.textContent = term.emoji; button.append(e); }
      button.append(document.createTextNode(text));
      const id = `term-pop-${term.id}`; button.setAttribute("aria-describedby", id);
      const pop = document.createElement("span"); pop.className = "term-pop"; pop.id = id; pop.setAttribute("role", "note");
      if (later) pop.textContent = `뒤에서 배워요 (Unit ${dest.unitIndex + 1} · Lesson ${dest.lessonIndex + 1} · Page ${dest.pageIndex + 1})`;
      else {
        pop.textContent = term.hover || "";
        if (dest && dest.pos !== here) {
          const link = document.createElement("a"); link.className = "term-more"; link.textContent = "더 자세히 보기";
          link.href = routeFor(dest.unitIndex, dest.lessonIndex, dest.pageIndex); link.target = "_blank"; link.rel = "noopener";
          pop.append(link);
        }
      }
      wrap.append(button, pop);
      const place = () => { pop.style.left = "0"; const r = pop.getBoundingClientRect(); const over = r.right - (document.documentElement.clientWidth - 8); if (over > 0) pop.style.left = `${-over}px`; };
      const close = () => { wrap.classList.remove("open"); wrap.classList.remove("dismissed"); };
      button.addEventListener("click", () => { wrap.classList.toggle("open"); wrap.classList.remove("dismissed"); place(); });
      wrap.addEventListener("mouseenter", () => { wrap.classList.remove("dismissed"); place(); });
      wrap.addEventListener("focusin", place);
      wrap.addEventListener("mouseleave", () => wrap.classList.remove("dismissed"));
      wrap.addEventListener("focusout", (event) => { if (!wrap.contains(event.relatedTarget)) close(); });
      wrap.addEventListener("keydown", (event) => { if (event.key === "Escape") { wrap.classList.remove("open"); wrap.classList.add("dismissed"); button.focus(); event.stopPropagation(); } });
      return wrap;
    };
    const nodes = [];
    prose.querySelectorAll(":scope > p, :scope > ul > li").forEach((block) => {
      const walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
      for (let node = walker.nextNode(); node; node = walker.nextNode()) if (!node.parentElement.closest("code, a, .term-wrap")) nodes.push(node);
    });
    for (let node of nodes) {
      for (;;) {
        const text = node.nodeValue; let best = null;
        for (const term of candidates) {
          if (used.has(term.id)) continue;
          for (const alias of term.aliases) {
            const at = termAt(text, alias);
            if (at >= 0 && (!best || at < best.at || (at === best.at && alias.length > best.alias.length))) best = { term, alias, at };
          }
        }
        if (!best) break;
        used.add(best.term.id);
        const matched = node.splitText(best.at); const rest = matched.splitText(best.alias.length);
        const wrap = make(best.term, matched.nodeValue);
        matched.replaceWith(wrap);
        node = rest;
      }
    }
  };
  const render = (course, state) => {
    const list = allItems(course);
    if (!list.length) return;
    const item = list[state.lessonIndex] || list[0];
    state.lessonIndex = list.indexOf(item);
    const pages = item.lesson.pages || [];
    state.pageIndex = Math.min(Math.max(0, state.pageIndex), Math.max(0, pages.length - 1));
    const page = pages[state.pageIndex] || { title: item.lesson.title, paragraphs: [] };
    const unitIndex = course.units.findIndex((unit) => unit.id === item.unit.id);
    const unitLessonIndex = course.lessons.filter((lesson) => lesson.unit === item.unit.id).indexOf(item.lesson);
    state.unitIndex = unitIndex;
    byId.set(item.lesson.id, item);
    document.title = `${page.title} · ${item.unit.title} · 외워서 공부하는 네트워크`;
    document.getElementById("topbar-location").textContent = `Unit ${String(unitIndex + 1).padStart(2, "0")} · Lesson ${String(unitLessonIndex + 1).padStart(2, "0")} · Page ${String(state.pageIndex + 1).padStart(2, "0")}`;
    const progress = `${state.lessonIndex + 1} / ${list.length} Lesson · Page ${state.pageIndex + 1} / ${pages.length}`;
    const nav = document.getElementById("network-nav");
    nav.innerHTML = `<a class="sidebar-course-title" href="${base}/">전체 학습과정 <span aria-hidden="true">›</span></a><p class="net-progress">${esc(progress)}</p>${course.units.map((unit, ui) => {
      const lessons = course.lessons.map((lesson, li) => ({ lesson, li })).filter(({ lesson }) => lesson.unit === unit.id);
      return `<section class="unit-nav"><h2>UNIT ${String(ui + 1).padStart(2, "0")}</h2><h3>${esc(unit.title)}</h3><ol>${lessons.map(({ lesson, li }, localIndex) => {
        const active = li === state.lessonIndex;
        const steps = lesson.pages || [];
        return `<li><a class="lesson-link" data-lesson="${li}" href="${routeFor(ui, localIndex, 0)}" ${active ? 'aria-current="page"' : ""}><span class="nav-number">${String(localIndex + 1).padStart(2, "0")}</span><span>${esc(lesson.title)}</span></a>${active ? `<ol class="sidebar-steps">${steps.map((step, si) => `<li><a class="page-link" data-lesson="${li}" data-page="${si}" href="${routeFor(ui, localIndex, si)}" ${si === state.pageIndex ? 'aria-current="page"' : ""}>${esc(step.title)}</a></li>`).join("")}</ol>` : ""}</li>`;
      }).join("")}</ol></section>`;
    }).join("")}`;
    const banner = document.getElementById("source-banner");
    const sha = course.preview_source?.sha || "local draft";
    const sourceUrl = course.preview_source?.url;
    banner.innerHTML = `<strong>Learn 콘텐츠 후보</strong><span>${esc(course.preview_source?.label || "develop 미리보기")}</span>${sourceUrl ? `<a href="${esc(sourceUrl)}" target="_blank" rel="noreferrer" title="${esc(sha)}">${esc(sha.slice(0, 12))}</a>` : ""}`;
    const main = document.getElementById("network-lesson");
    main.replaceChildren();
    const title = document.createElement("h1");
    title.textContent = page.title;
    main.append(title);
    const questions = page.questions || [];
    const inlineQuizzes = page.inline_quizzes || [];
    let nextPage;
    const prose = renderProse(page.paragraphs || [], page.illustrations || [], inlineQuizzes,
      (quiz) => renderQuiz(quiz.questions, quiz.start_index || 0));
    const recap = prose.querySelector(":scope > .ral-summary");
    main.append(prose);
    decorateTerms(prose, course, item, page);
    recap?.remove();
    const video = renderVideo(page.video);
    if (video) main.append(video);
    if (questions.length) main.append(renderQuiz(questions, page.question_start_index || 0));
    if (recap) main.append(recap);
    const previous = list[state.lessonIndex - 1];
    const next = list[state.lessonIndex + 1];
    const navFooter = document.createElement("nav");
    navFooter.className = "page-nav";
    navFooter.setAttribute("aria-label", "페이지 이동");
    const prevPage = document.createElement("button");
    prevPage.type = "button";
    prevPage.textContent = "← 이전 페이지";
    prevPage.disabled = state.pageIndex === 0 && !previous;
    prevPage.addEventListener("click", () => {
      if (state.pageIndex > 0) state.pageIndex--;
      else if (previous) { state.lessonIndex--; state.pageIndex = (previous.lesson.pages || []).length - 1; }
      visit(course, state);
    });
    nextPage = document.createElement("button");
    nextPage.type = "button";
    nextPage.textContent = "다음 페이지 →";
    nextPage.disabled = state.pageIndex >= pages.length - 1 && !next;
    nextPage.addEventListener("click", () => {
      if (state.pageIndex < pages.length - 1) state.pageIndex++;
      else if (next) { state.lessonIndex++; state.pageIndex = 0; }
      visit(course, state);
    });
    navFooter.append(prevPage, nextPage);
    main.append(navFooter);
    const url = routeFor(unitIndex, unitLessonIndex, state.pageIndex);
    history.replaceState({ ...state }, "", url);
    document.querySelectorAll(".lesson-link, .page-link").forEach((anchor) => anchor.addEventListener("click", (event) => {
      event.preventDefault();
      const targetLesson = Number(anchor.dataset.lesson);
      const targetPage = Number(anchor.dataset.page || 0);
      state.lessonIndex = targetLesson;
      state.pageIndex = targetPage;
      visit(course, state);
    }));
    document.getElementById("sidebar-toggle").setAttribute("aria-expanded", "true");
  };
  const visit = (course, state) => {
    const list = allItems(course);
    const item = list[state.lessonIndex] || list[0];
    const unitIndex = course.units.findIndex((unit) => unit.id === item.unit.id);
    const lessonIndex = course.lessons.filter((lesson) => lesson.unit === item.unit.id).indexOf(item.lesson);
    history.pushState({ ...state }, "", routeFor(unitIndex, lessonIndex, state.pageIndex));
    render(course, state);
    window.scrollTo({ top: 0, behavior: "instant" });
  };
  fetch(window.NETWORK_COURSE_URL || `${base}/data/course.json`)
    .then((response) => { if (!response.ok) throw new Error("course data unavailable"); return response.json(); })
    .then((course) => {
      let state = parseRoute(course);
      document.getElementById("sidebar-toggle").addEventListener("click", () => {
        const workspace = document.querySelector(".course-workspace");
        workspace.classList.toggle("sidebar-open");
        document.getElementById("sidebar-toggle").setAttribute("aria-expanded", String(workspace.classList.contains("sidebar-open")));
      });
      const overlay = document.createElement("button");
      overlay.className = "mobile-overlay";
      overlay.type = "button";
      overlay.setAttribute("aria-label", "목차 닫기");
      overlay.addEventListener("click", () => document.querySelector(".course-workspace").classList.remove("sidebar-open"));
      document.querySelector(".course-workspace").prepend(overlay);
      window.addEventListener("popstate", () => { state = parseRoute(course); render(course, state); });
      window.addEventListener("keydown", (event) => {
        if ((event.key !== "ArrowLeft" && event.key !== "ArrowRight") || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
        if (event.target.closest?.("input, textarea, select, button, a, [contenteditable='true'], object")) return;
        const list = allItems(course);
        const item = list[state.lessonIndex] || list[0];
        const pages = item.lesson.pages || [];
        const previous = state.pageIndex > 0 || state.lessonIndex > 0;
        const next = state.pageIndex < pages.length - 1 || state.lessonIndex < list.length - 1;
        if (event.key === "ArrowLeft" && previous) {
          event.preventDefault();
          const target = list[state.lessonIndex - 1];
          if (state.pageIndex > 0) state.pageIndex--;
          else { state.lessonIndex--; state.pageIndex = (target.lesson.pages || []).length - 1; }
          visit(course, state);
        } else if (event.key === "ArrowRight" && next) {
          event.preventDefault();
          if (state.pageIndex < pages.length - 1) state.pageIndex++;
          else { state.lessonIndex++; state.pageIndex = 0; }
          visit(course, state);
        }
      });
      render(course, state);
    })
    .catch(() => { document.getElementById("network-lesson").innerHTML = '<p class="empty">콘텐츠를 불러오지 못했습니다. 미리보기 빌드 상태를 확인해 주세요.</p>'; });
})();
