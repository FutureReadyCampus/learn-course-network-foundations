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
  const renderProse = (paragraphs = [], illustrations = []) => {
    const prose = document.createElement("div");
    prose.className = "net-prose";
    let list = [];
    const flush = () => {
      if (!list.length) return;
      const ul = document.createElement("ul");
      list.forEach((item) => {
        const li = document.createElement("li");
        li.innerHTML = inline(item);
        ul.append(li);
      });
      prose.append(ul);
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
    appendIllustrations(-1);
    for (const [index, text] of paragraphs.entries()) {
      const lines = String(text).split("\n");
      const heading = lines.length === 1 ? text.match(/^(#{3,4})\s+(.+)$/) : null;
      if (heading) {
        flush();
        // ## is the page boundary and renders as the page H1; body ###/#### become H2/H3.
        const element = document.createElement(heading[1].length === 3 ? "h2" : "h3");
        element.innerHTML = inline(heading[2]);
        prose.append(element);
      } else if (lines.length > 1 && lines.every((line) => /^\s*(?:[-*]|\d+\.)\s+/.test(line))) {
        list.push(...lines.map((line) => line.replace(/^\s*(?:[-*]|\d+\.)\s+/, "")));
      } else {
        flush();
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
    }
    flush();
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
        try { object.contentDocument?.documentElement.unpauseAnimations?.(); } catch { /* Browser may block an inaccessible SVG document. */ }
      });
      figure.append(object, controlFor(object));
    } else {
      const image = document.createElement("img");
      image.src = src;
      image.alt = illustration.alt || "";
      figure.append(image);
    }
    if (illustration.caption) {
      const caption = document.createElement("figcaption");
      caption.textContent = illustration.caption;
      figure.append(caption);
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
  const render = (course, state) => {
    const list = allItems(course);
    if (!list.length) return;
    const item = list[state.lessonIndex] || list[0];
    state.lessonIndex = list.indexOf(item);
    const pages = item.lesson.pages || [];
    state.pageIndex = Math.min(Math.max(0, state.pageIndex), Math.max(0, pages.length - 1));
    const page = pages[state.pageIndex] || { title: item.lesson.title, paragraphs: [] };
    const unitIndex = course.units.findIndex((unit) => unit.id === item.unit.id);
    state.unitIndex = unitIndex;
    byId.set(item.lesson.id, item);
    document.title = `${page.title} · ${item.unit.title} · 외워서 공부하는 네트워크`;
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
    const prose = renderProse(page.paragraphs || [], page.illustrations || []);
    main.append(prose);
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
    const nextPage = document.createElement("button");
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
    const unitLessonIndex = course.lessons.filter((lesson) => lesson.unit === item.unit.id).indexOf(item.lesson);
    const url = routeFor(unitIndex, unitLessonIndex, state.pageIndex);
    history.replaceState({ ...state }, "", url);
    document.querySelectorAll(".lesson-link, .page-link").forEach((anchor) => anchor.addEventListener("click", (event) => {
      event.preventDefault();
      const targetLesson = Number(anchor.dataset.lesson);
      state.lessonIndex = targetLesson;
      state.pageIndex = Number(anchor.dataset.page || 0);
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
      render(course, state);
    })
    .catch(() => { document.getElementById("network-lesson").innerHTML = '<p class="empty">콘텐츠를 불러오지 못했습니다. 미리보기 빌드 상태를 확인해 주세요.</p>'; });
})();
