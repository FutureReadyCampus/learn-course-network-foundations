#!/usr/bin/env python3
"""Build the static GitHub Pages reader from the authored Unit/Lesson Markdown."""

from __future__ import annotations

import argparse
from html import escape as html_escape
import json
import shutil
from urllib.parse import quote
from pathlib import Path

from build_course import ROOT, build


SITE = ROOT / "site"


def emit(course: dict, output: Path, baseurl: str, revision: str, dispatch: dict | None = None) -> None:
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

    data_dir = output / "data"
    data_dir.mkdir()
    (data_dir / "course.json").write_text(json.dumps(course, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "assets").mkdir(exist_ok=True)
    for name in ("reader.css", "reader.js"):
        shutil.copyfile(SITE / "assets" / name, output / "assets" / name)

    html = (SITE / "index.html").read_text(encoding="utf-8")
    if baseurl.count("/exercises/"):  # exercise reader: show its own course title
        html = html.replace("외워서 공부하는 네트워크", html_escape(course["title"]))
    html = html.replace('window.NETWORK_SITE_BASE = "";', f'window.NETWORK_SITE_BASE = {json.dumps(baseurl)};')
    revision_query = f"?v={quote(revision, safe='')}"
    html = html.replace('window.NETWORK_COURSE_URL = "/data/course.json";', f'window.NETWORK_COURSE_URL = {json.dumps(baseurl + "/data/course.json" + revision_query)};')
    for name in ("/assets/reader.css", "/assets/reader.js"):
        html = html.replace(f'"{name}"', json.dumps(baseurl + name + revision_query))
    (output / "index.html").write_text(html, encoding="utf-8")
    # GitHub Pages serves this copy for deep links; the reader restores the route from pathname.
    # The root 404 also serves /exercises/<id>/ deep links, so it switches base and data to that course.
    if dispatch:
        script = (f"<script>(function(){{var m=location.pathname.match({json.dumps('^' + baseurl + '/exercises/([^/]+)/')});"
                  f"var d={json.dumps(dispatch, ensure_ascii=False)};if(m&&d[m[1]]){{window.NETWORK_SITE_BASE={json.dumps(baseurl)}+'/exercises/'+m[1];"
                  f"window.NETWORK_COURSE_URL=window.NETWORK_SITE_BASE+'/data/course.json{revision_query}';"
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
    links, dispatch = [], {}
    exercises = {f.parent.name: build(args.source_revision, args.source_label, f) for f in sorted((ROOT / "exercises").glob("*/course.yaml"))}
    emit(course, output, baseurl, args.source_revision, {k: v["title"] for k, v in exercises.items()})
    for slug, exercise in exercises.items():
        emit(exercise, output / "exercises" / slug, f"{baseurl}/exercises/{slug}", args.source_revision)
        links.append(f'<li><a href="{baseurl}/exercises/{slug}/">{html_escape(exercise["title"])}</a> · {len(exercise["units"])} Units</li>')
    if links:
        (output / "exercises" / "index.html").write_text(
            '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Exercises</title><h1>실습 과정</h1><ul>{"".join(links)}</ul>'
            f'<p><a href="{baseurl}/">← 네트워크 기초(Foundations)</a></p>', encoding="utf-8")

    print(f"Built static reader: {len(course['units'])} Units, {len(course['lessons'])} Lessons at {output}")


if __name__ == "__main__":
    main()
