#!/usr/bin/env python3
"""Build the static GitHub Pages reader from the authored Unit/Lesson Markdown."""

from __future__ import annotations

import argparse
from html import escape as html_escape
import json
import re
import shutil

import yaml
from urllib.parse import quote
from pathlib import Path

from build_course import ROOT, build


SITE = ROOT / "site"


PORTFOLIO_FILES = [  # (path in portfolio-starter/, level, what it is) - order = the order learners create them
    ("_config.yml", "필수", "사이트 이름과 주소 설정입니다. 붙여 넣은 뒤 `# ← 내 것으로 바꾸기` 줄을 내 것으로 고칩니다."),
    ("index.md", "필수", "첫 화면입니다. 최신 글 목록이 자동으로 나옵니다."),
    ("about.md", "필수", "소개 페이지입니다. 빈칸 안내 문구를 내 소개로 바꿉니다."),
    ("_posts/2026-01-01-hello.md", "필수", "샘플 글입니다. 내 첫 글을 쓸 때는 파일 이름의 날짜와 제목(영문 권장)을 바꿔 새 파일로 만듭니다."),
    (".gitignore", "권장", "비밀키 파일이 실수로 올라가지 않게 막아 줍니다."),
    ("_templates/post-practice.md", "권장", "실습 한 개를 글 한 편으로 남기는 기본 글 틀입니다. 복사해서 `_posts/` 아래 새 글로 씁니다."),
    ("_templates/post-short.md", "선택", "5분 안에 쓰는 짧은 글 틀입니다."),
    ("_templates/post-stuck.md", "선택", "막혔던 일을 남기는 글 틀입니다."),
    ("code/README.md", "선택", "실습 코드를 두는 폴더 안내입니다. 이 파일을 만들면 `code/` 폴더가 함께 만들어집니다."),
    ("code/hello_example.py", "선택", "파이썬 예시 코드 한 개입니다."),
    ("check_publish.py", "권장", "공개 전 점검 스크립트입니다. 내 컴퓨터에서 `python check_publish.py` 로 돌립니다."),
    ("README.md", "선택", "저장소 첫 화면 설명입니다."),
]


def _inline_code(text: str) -> str:
    return re.sub(r"`([^`]+)`", lambda m: f"<code>{html_escape(m.group(1))}</code>", html_escape(text, quote=False))


def _portfolio_slug(path: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def build_portfolio(target: Path, baseurl: str) -> None:
    from markdown_it import MarkdownIt

    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    template = (SITE / "portfolio.html").read_text(encoding="utf-8")
    here = f"{baseurl}/exercises/portfolio"
    nav_items = [("", "가이드"), ("files/", "파일 모음"), ("prompts/", "쓰기 프롬프트")]

    def page(sub: str, title: str, body: str) -> None:
        nav = "".join(
            f'<a href="{here}/{href}"' + (' aria-current="page"' if href == sub else "") + f">{label}</a>"
            for href, label in nav_items
        )
        html = (template.replace("__SITE__", baseurl).replace("__TITLE__", html_escape(title))
                .replace("__NAV__", f'<nav class="portfolio-nav" aria-label="내 기록 남기기">{nav}</nav>').replace("__BODY__", body))
        out = target / sub
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(html, encoding="utf-8")

    guide_text = (ROOT / "portfolio" / "index.md").read_text(encoding="utf-8")
    title = (re.search(r"^# (.+)$", guide_text, re.M) or [None, "내 기록 남기기"])[1]
    page("", title, md.render(guide_text))
    for svg in (ROOT / "portfolio").glob("*.svg"):
        shutil.copyfile(svg, target / svg.name)

    starter = ROOT / "portfolio-starter"
    toc, sections = [], []
    for path, level, note in PORTFOLIO_FILES:
        source = starter / path
        if not source.is_file():
            raise FileNotFoundError(source)
        slug = _portfolio_slug(path)
        toc.append(f'<li><a href="#{slug}"><code>{html_escape(path)}</code></a> <span class="file-level">{level}</span></li>')
        sections.append(
            f'<section class="file-card" id="{slug}"><h2><code>{html_escape(path)}</code> <span class="file-level">{level}</span></h2>'
            f"<p>{_inline_code(note)}</p><pre><code>{html_escape(source.read_text(encoding='utf-8'))}</code></pre></section>"
        )
    intro = ("<h1>파일 모음</h1><p>내 저장소에 만들 파일의 내용입니다. 각 상자의 <strong>복사</strong> 버튼을 누르고, "
             "GitHub 저장소 화면에서 <strong>Add file → Create new file</strong>로 같은 이름의 파일을 만들어 붙여 넣으면 됩니다. "
             "<code>_posts/…</code>처럼 폴더가 붙은 이름은 이름 칸에 그대로 입력하면 폴더도 함께 만들어집니다.</p>")
    page("files/", "파일 모음", intro + f'<ol class="file-toc">{"".join(toc)}</ol>' + "".join(sections))

    prompts = starter / "prompts.md"
    if prompts.is_file():
        page("prompts/", "쓰기 프롬프트", md.render(prompts.read_text(encoding="utf-8")))



def emit(course: dict, output: Path, baseurl: str, revision: str, dispatch: dict | None = None, site: str = "", no_copy: bool = False) -> None:
    output.mkdir(parents=True)
    for lesson in course["lessons"]:
        for page in lesson.get("pages", []):
            for illustration in page.get("illustrations", []):
                source = illustration.get("src", "")
                prefix = "/api/v1/network-course-assets/"
                if not source.startswith(prefix):
                    continue
                relative = Path(source[len(prefix):])
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError(f"unsafe illustration path: {source}")
                source_path = ROOT / relative
                if not source_path.is_file():
                    raise FileNotFoundError(source_path)
                destination = output / "assets/course-assets" / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_path, destination)
                illustration["src"] = f"{baseurl}/assets/course-assets/{relative.as_posix()}"

    # Page figures embedded in page HTML (exercise courses): copy the SVGs and point them at the site.
    prefix = "/api/v1/network-course-assets/"
    for lesson in course["lessons"]:
        for page in lesson.get("pages", []):
            html_text = page.get("html", "")
            for relative_text in set(re.findall(re.escape(prefix) + r'([^"]+)', html_text)):
                relative = Path(relative_text)
                if relative.is_absolute() or ".." in relative.parts or not (ROOT / relative).is_file():
                    raise ValueError(f"bad page figure: {relative_text}")
                destination = output / "assets/course-assets" / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, destination)
                html_text = html_text.replace(prefix + relative_text, f"{baseurl}/assets/course-assets/{relative.as_posix()}")
            if html_text != page.get("html", ""):
                page["html"] = html_text
    for lesson in course["lessons"]:  # links in page HTML use __SITE__ for the site root
        for page in lesson.get("pages", []):
            if "html" in page:
                page["html"] = page["html"].replace("__SITE__", site)

    data_dir = output / "data"
    data_dir.mkdir()
    (data_dir / "course.json").write_text(json.dumps(course, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "assets").mkdir(exist_ok=True)
    for name in ("reader.css", "reader.js"):
        shutil.copyfile(SITE / "assets" / name, output / "assets" / name)

    html = (SITE / "index.html").read_text(encoding="utf-8").replace("__SITE__", site)
    if baseurl.count("/exercises/"):  # exercise reader: show its own course title
        html = html.replace("외워서 공부하는 네트워크", html_escape(course["title"]))
    html = html.replace('window.NETWORK_SITE_BASE = "";', f'window.NETWORK_SITE_BASE = {json.dumps(baseurl)};' + (" window.NETWORK_NO_COPY = true;" if no_copy else ""))
    revision_query = f"?v={quote(revision, safe='')}"
    html = html.replace('window.NETWORK_COURSE_URL = "/data/course.json";', f'window.NETWORK_COURSE_URL = {json.dumps(baseurl + "/data/course.json" + revision_query)};')
    for name in ("/assets/reader.css", "/assets/reader.js"):
        html = html.replace(f'"{name}"', json.dumps(baseurl + name + revision_query))
    (output / "index.html").write_text(html, encoding="utf-8")
    # GitHub Pages serves this copy for deep links; the reader restores the route from pathname.
    # The root 404 also serves /exercises/<id>/ deep links, so it switches base and data to that course.
    if dispatch:
        script = (f"<script>(function(){{var m=location.pathname.match({json.dumps('^' + baseurl + '/exercises/(module/[^/]+)/')});"
                  f"var d={json.dumps(dispatch, ensure_ascii=False)};if(m&&d[m[1]]){{window.NETWORK_SITE_BASE={json.dumps(baseurl)}+'/exercises/'+m[1];"
                  f"window.NETWORK_NO_COPY=true;window.NETWORK_COURSE_URL=window.NETWORK_SITE_BASE+'/data/course.json{revision_query}';"
                  "document.querySelector('.topbar-course').textContent=d[m[1]];}})();</script></body>")
        html = html.replace("</body>", script, 1)
    (output / "404.html").write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SITE / "dist")
    parser.add_argument("--baseurl", default="", help="GitHub Pages project prefix, e.g. /learn-course-network-foundations")
    parser.add_argument("--source-revision", default="local-draft")
    parser.add_argument("--source-label", default="develop local preview")
    args = parser.parse_args()

    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    baseurl = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    course = build(args.source_revision, args.source_label)
    # Exercise courses (exercises/<id>/course.yaml) get their own reader copy under /exercises/<id>/.
    exercises = {f.parent.relative_to(ROOT / "exercises").as_posix(): build(args.source_revision, args.source_label, f) for f in sorted((ROOT / "exercises").glob("module/*/course.yaml"))}
    emit(course, output, baseurl, args.source_revision, {k: v["title"] for k, v in exercises.items()}, baseurl)
    for slug, exercise in exercises.items():
        emit(exercise, output / "exercises" / slug, f"{baseurl}/exercises/{slug}", args.source_revision, site=baseurl, no_copy=True)
    if exercises:
        cards = []
        for slug, exercise in exercises.items():
            meta = yaml.safe_load((ROOT / "exercises" / slug / "course.yaml").read_text(encoding="utf-8"))["course"]
            pages = sum(len(lesson["pages"]) for lesson in exercise["lessons"])
            units = "".join(f"<li>{html_escape(unit['title'])}</li>" for unit in exercise["units"])
            cards.append(
                f'<article class="hub-card"><span class="hub-tag">{html_escape(slug.replace("/", " ").upper())}</span>'
                f'<h2>{html_escape(meta["title"])}</h2><p>{html_escape(meta.get("description", ""))}</p>'
                f'<ul class="hub-stats"><li><strong>{len(exercise["units"])}</strong>Units</li>'
                f'<li><strong>{len(exercise["lessons"])}</strong>Lessons</li><li><strong>{pages}</strong>Pages</li></ul>'
                f'<details><summary>Unit 목록 보기</summary><ol>{units}</ol></details>'
                f'<a class="hub-cta" href="{baseurl}/exercises/{slug}/">시작하기</a></article>')
        page = (SITE / "exercises.html").read_text(encoding="utf-8").replace("__SITE__", baseurl).replace("__CARDS__", "".join(cards))
        (output / "exercises" / "index.html").write_text(page, encoding="utf-8")

    # Learner portfolio: guide + copy-paste file collection + writing prompts under /exercises/portfolio/.
    guide = ROOT / "portfolio" / "index.md"
    if guide.is_file():
        build_portfolio(output / "exercises" / "portfolio", baseurl)

    print(f"Built static reader: {len(course['units'])} Units, {len(course['lessons'])} Lessons at {output}")


if __name__ == "__main__":
    main()
