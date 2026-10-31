#!/usr/bin/env python3
"""Build the Learn Network catalog from the course Markdown source."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAGE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
PAGE_ID_MARKER_RE = re.compile(r"\A\s*<!--\s*learn-page-id:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*-->\s*")


def page_marker(body: str, path: Path) -> tuple[str | None, str]:
    match = PAGE_ID_MARKER_RE.match(body)
    if match:
        return match.group(1), body[match.end():]
    if "learn-page-id:" in body:
        raise ValueError(f"Page ID marker must appear immediately after a Page heading in {path}")
    return None, body


def page_metadata_by_id(metadata: list, path: Path) -> dict[str, dict]:
    result = {}
    for item in metadata:
        if not isinstance(item, dict):
            raise ValueError(f"Page metadata entries must be objects in {path}")
        page_id = item.get("page_id")
        if page_id is None:
            if "video" in item:
                raise ValueError(f"Page video metadata requires page_id in {path}")
            continue
        if not isinstance(page_id, str) or not PAGE_ID_RE.fullmatch(page_id):
            raise ValueError(f"Invalid page_id in {path}: {page_id!r}")
        if page_id in result:
            raise ValueError(f"Duplicate page_id metadata in {path}: {page_id}")
        result[page_id] = item
    return result


def validate_page_video(metadata: dict, page_id: str, path: Path) -> dict:
    video = metadata.get("video")
    if video is None:
        return {}
    if not isinstance(video, dict) or not isinstance(video.get("video_id"), str) or not YOUTUBE_ID_RE.fullmatch(video["video_id"]):
        raise ValueError(f"Page video needs an 11-character YouTube video_id in {path}: {page_id}")
    if not isinstance(video.get("title"), str) or not video["title"].strip():
        raise ValueError(f"Page video needs a title in {path}: {page_id}")
    if "creator" in video and (not isinstance(video["creator"], str) or not video["creator"].strip()):
        raise ValueError(f"Page video creator must be non-empty text in {path}: {page_id}")
    if "duration_seconds" in video and (
        isinstance(video["duration_seconds"], bool)
        or not isinstance(video["duration_seconds"], (int, float))
        or video["duration_seconds"] <= 0
    ):
        raise ValueError(f"Page video duration_seconds must be positive in {path}: {page_id}")
    return {"video": {
        key: video[key] for key in ("video_id", "title", "creator", "duration_seconds") if key in video
    }}


def page_questions(value, path: Path, page_number: int) -> list[dict]:
    if not isinstance(value, list):
        raise ValueError(f"Page questions must be a list in {path}, page {page_number}")
    if not value:
        return []
    if len(value) < 3:
        raise ValueError(f"Page needs at least three questions in {path}, page {page_number}")
    expected = [("choice", "easy"), ("choice", "medium")]
    for index, question in enumerate(value, 1):
        where = f"{path}, page {page_number}, question {index}"
        if not isinstance(question, dict) or not isinstance(question.get("prompt"), str) or not question["prompt"].strip():
            raise ValueError(f"Question needs a prompt in {where}")
        kind = question.get("kind")
        if index <= len(expected) and (kind, question.get("difficulty")) != expected[index - 1]:
            raise ValueError(f"Unexpected question kind or difficulty in slot {index} in {where}")
        if index == 3 and (kind, question.get("difficulty")) not in {("short", None), ("choice", "medium")}:
            raise ValueError(f"Unexpected question kind or difficulty in slot {index} in {where}")
        if kind == "choice":
            choices = question.get("choices")
            if not isinstance(choices, list) or len(choices) != 5 or any(not isinstance(choice, dict) for choice in choices):
                raise ValueError(f"Choice question needs exactly five choices in {where}")
            ids = [choice.get("id") for choice in choices]
            if any(not isinstance(choice_id, str) or not choice_id.strip() for choice_id in ids) or len(set(ids)) != 5 or question.get("answer") not in ids:
                raise ValueError(f"Choice question needs five unique choices and a valid answer in {where}")
            if any(not isinstance(choice.get("text"), str) or not choice["text"].strip()
                   or not isinstance(choice.get("feedback"), str) or not choice["feedback"].strip()
                   for choice in choices):
                raise ValueError(f"Every choice needs text and feedback in {where}")
        elif kind == "short":
            answers = question.get("answers")
            if not isinstance(answers, list) or not answers or any(not isinstance(answer, str) or not answer.strip() for answer in answers):
                raise ValueError(f"Short question needs accepted answers in {where}")
        else:
            raise ValueError(f"Question kind must be choice or short in {where}")
    return value


def read_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"Missing YAML front matter: {path}")
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, match.group(2).strip()


def split_paragraphs(text: str) -> list[str]:
    paragraphs = []
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        block = re.sub(r"^```[^\n]*\n|\n```$", "", block)
        lines = block.splitlines()
        if len(lines) > 1 and all(re.match(r"^(?:\d+\.|[-*])\s+", line) for line in lines):
            paragraphs.extend(lines)
        else:
            paragraphs.append(block)
    paragraphs = [re.sub(r"\*\*(.*?)\*\*", r"\1", item) for item in paragraphs]
    return paragraphs


def lesson_asset(
    path: Path,
    filename: str,
    lesson_meta: dict,
    animation_assets: dict,
    animated: bool = False,
) -> Path:
    relative = Path(filename)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Unsafe Lesson asset path {filename!r} in {path}")
    candidates = []
    if animated:
        lesson_animation_dir = lesson_meta.get("animations_dir")
        if lesson_animation_dir:
            candidates.append(ROOT / lesson_animation_dir / relative.name)
        lesson_runtime_dir = lesson_meta.get("runtime_assets_dir")
        if lesson_runtime_dir:
            candidates.append(path.parent / lesson_runtime_dir / relative.name)
    candidates.append(path.parent / relative)
    asset = next((candidate for candidate in candidates if candidate.is_file()), None)
    if asset is None:
        raise FileNotFoundError(f"Missing Lesson asset {filename} for {path}")
    return asset


def authored_reading_pages(path: Path, lesson_meta: dict, animation_assets: dict) -> list[dict]:
    _, source = read_front_matter(path)
    sections = re.findall(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", source, re.M | re.S)
    pages_meta = lesson_meta.get("pages", [])
    concepts = {item["id"]: item for item in lesson_meta.get("concepts", [])}
    quiz_file = lesson_meta.get("quiz_file")
    quiz_sets = {}
    if quiz_file:
        quiz_path = lesson_asset(path, quiz_file, lesson_meta, animation_assets)
        quiz_data = yaml.safe_load(quiz_path.read_text(encoding="utf-8")) or {}
        quiz_sets = quiz_data.get("quizzes", {})
        if not isinstance(quiz_sets, dict):
            raise ValueError(f"Quiz file needs a quizzes mapping: {quiz_path}")
    if not sections or len(sections) != len(pages_meta):
        raise ValueError(f"Page metadata does not match Lesson headings in {path}")

    illustrated = set(lesson_meta.get("illustrated_concepts", []))
    diagram = lesson_meta.get("diagram", {}).get("file")
    pages = []
    used_quizzes = set()
    for index, (heading, body) in enumerate(sections):
        metadata = pages_meta[index]
        concept_ids = metadata.get("concepts", [])
        missing = [concept_id for concept_id in concept_ids if concept_id not in concepts]
        if missing:
            raise ValueError(f"Unknown Page concepts in {path}: {', '.join(missing)}")
        selected = [concepts[concept_id] for concept_id in concept_ids]
        inline_quizzes = []
        markers = list(re.finditer(r"<!--\s*quiz:\s*([\w-]+)\s*-->", body))
        for marker in markers:
            quiz_id = marker.group(1)
            if quiz_id not in quiz_sets or quiz_id in used_quizzes:
                raise ValueError(f"Unknown or repeated quiz marker {quiz_id!r} in {path}, page {index + 1}")
            before_marker = re.sub(r"<!--\s*quiz:\s*[\w-]+\s*-->", "", body[:marker.start()])
            inline_quizzes.append({
                "id": quiz_id,
                "after_paragraph": len(split_paragraphs(before_marker)),
                "questions": page_questions(quiz_sets[quiz_id].get("questions"), path, index + 1),
            })
            used_quizzes.add(quiz_id)
        clean_body = re.sub(r"<!--\s*quiz:\s*[\w-]+\s*-->", "", body)
        page = {
            "title": re.sub(r"\s*·\s*\d+:\d+.*$", "", heading).strip(),
            "paragraphs": split_paragraphs(clean_body),
            "terms": list(dict.fromkeys(
                term["term"] for concept in selected for term in concept.get("terms", [])
            )),
            "questions": page_questions(metadata.get("questions", []), path, index + 1),
        }
        if inline_quizzes:
            page["inline_quizzes"] = inline_quizzes
        illustrations = []
        if index == 0 and diagram:
            asset = lesson_asset(path, diagram, lesson_meta, animation_assets)
            illustrations.append({
                "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                "title": f"{page['title']} · 학습 흐름",
                "alt": f"{page['title']}의 개념 순서를 보여 주는 그림",
                "caption": "개념이 이어지는 순서를 확인해 보세요.",
            })
        for concept_id, concept in zip(concept_ids, selected):
            if concept_id not in illustrated:
                continue
            animations = ([concept["anim"]] if concept.get("anim") else []) + concept.get("additional_anims", [])
            for animation in animations:
                asset = lesson_asset(path, animation["file"], lesson_meta, animation_assets, animated=True)
                illustrations.append({
                    "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                    "title": animation["title"],
                    "alt": animation["alt"],
                    "caption": animation["caption"],
                })
        positions = metadata.get("illustration_after_paragraph")
        if positions is not None:
            if len(positions) != len(illustrations):
                raise ValueError(f"Illustration positions do not match Page assets in {path}, page {index + 1}")
            for illustration, after_paragraph in zip(illustrations, positions):
                if after_paragraph < -1 or after_paragraph >= len(page["paragraphs"]):
                    raise ValueError(f"Illustration position is outside Page paragraphs in {path}, page {index + 1}")
                illustration["after_paragraph"] = after_paragraph
        for illustration in metadata.get("illustrations", []):
            asset = lesson_asset(path, illustration["file"], lesson_meta, animation_assets, animated=True)
            after_paragraph = illustration["after_paragraph"]
            if after_paragraph < -1 or after_paragraph >= len(page["paragraphs"]):
                raise ValueError(f"Illustration position is outside Page paragraphs in {path}, page {index + 1}")
            illustrations.append({
                "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                "title": illustration.get("title", page["title"]),
                "alt": illustration["alt"],
                "caption": illustration["caption"],
                "after_paragraph": after_paragraph,
            })
        if illustrations:
            page["illustrations"] = illustrations
        pages.append(page)
    if used_quizzes != set(quiz_sets):
        unused = sorted(set(quiz_sets) - used_quizzes)
        raise ValueError(f"Quiz file has unplaced quizzes in {path}: {', '.join(unused)}")
    return pages


def reading_pages(path: Path, lesson_meta: dict, animation_assets: dict) -> list[dict]:
    if "pages" in lesson_meta and "concepts" in lesson_meta:
        return authored_reading_pages(path, lesson_meta, animation_assets)
    source = path.read_text(encoding="utf-8")
    sections = re.findall(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", source, re.M | re.S)
    if not sections:
        title = lesson_meta["title"]
        body = re.sub(r"\A---\s*\n.*?\n---\s*\n?", "", source, count=1, flags=re.S)
        body = re.sub(r"\A#\s+.+\n", "", body, count=1, flags=re.M).strip()
        sections = [(title, body)]
    guide_path = lesson_meta.get("beginner_guide")
    concepts = json.loads((ROOT / guide_path).read_text(encoding="utf-8"))["concepts"] if guide_path else []
    page_metadata = lesson_meta.get("page_metadata", [])
    anchored_metadata = page_metadata_by_id(page_metadata, path)
    marked_sections = []
    seen_page_ids = set()
    for heading, body in sections:
        page_id, body = page_marker(body, path)
        if page_id and page_id in seen_page_ids:
            raise ValueError(f"Duplicate learn-page-id marker in {path}: {page_id}")
        if page_id:
            seen_page_ids.add(page_id)
        marked_sections.append((heading, body, page_id))
    missing_ids = set(anchored_metadata) - seen_page_ids
    if missing_ids:
        raise ValueError(f"Page metadata references unknown page_id in {path}: {', '.join(sorted(missing_ids))}")
    page_groups = lesson_meta.get("page_groups")
    if page_groups:
        grouped_sections = []
        for group in page_groups:
            indices = group["sections"]
            if not indices or any(index < 1 or index > len(sections) for index in indices):
                raise ValueError(f"Invalid page group sections in {path}")
            members = [marked_sections[index - 1] for index in indices]
            ids = {member[2] for member in members if member[2]}
            if len(ids) > 1:
                raise ValueError(f"A page group cannot combine multiple learn-page-id markers in {path}")
            grouped_sections.append((group["title"], "\n\n".join(member[1] for member in members), next(iter(ids), None)))
        sections = grouped_sections
    else:
        sections = marked_sections
    diagram_ref = lesson_meta.get("wiki_diagram")
    diagram_path = ROOT / diagram_ref if diagram_ref else None
    illustrated_pages = lesson_meta.get("illustrated_pages", [])
    lesson_animation_dir = lesson_meta.get("animations_dir")
    pages = []
    for index, (heading, body, page_id) in enumerate(sections):
        title = re.sub(r"\s*·\s*\d+:\d+.*$", "", heading).strip()
        concept_indices = [section_index - 1 for section_index in page_groups[index]["sections"]] if page_groups else ([min(index, len(concepts) - 1)] if concepts else [])
        page_concepts = [concepts[concept_index] for concept_index in concept_indices if concept_index < len(concepts)]
        page_meta = anchored_metadata.get(page_id, page_metadata[index] if index < len(page_metadata) else {})
        page = {
            "title": title,
            "paragraphs": split_paragraphs(body),
            "terms": page_meta.get("terms", list(dict.fromkeys(item["term"] for concept in page_concepts for item in concept.get("terms", [])))),
            "questions": page_questions(page_meta.get("questions", []), path, index + 1),
        }
        if page_id and page_id in anchored_metadata:
            page.update(validate_page_video(page_meta, page_id, path))
        illustrations = []
        if index == 0 and diagram_path and diagram_path.is_file():
            illustrations.append({
                "src": f"/api/v1/network-course-assets/{diagram_path.relative_to(ROOT).as_posix()}",
                "title": f"{title} · 학습 흐름",
                "alt": f"{title}의 개념 순서와 강의 시점을 보여 주는 학습 흐름도",
                "caption": "개념이 이어지는 순서를 확인해 보세요.",
            })
        animations = page_meta.get("animations")
        if animations is None and index + 1 in illustrated_pages:
            animations = [anim for concept in page_concepts for anim in ([concept["anim"]] if concept.get("anim") else []) + concept.get("additional_anims", [])]
        if animations:
            for anim in animations:
                animation_dir = ROOT / lesson_animation_dir if lesson_animation_dir else path.parent / "assets" / "animations"
                asset = animation_dir / anim["file"]
                if not asset.is_file():
                    asset = None
                if asset is None:
                    raise FileNotFoundError(f"Missing SVG animation {anim['file']} for {path}")
                illustrations.append({
                    "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                    "title": anim["title"],
                    "alt": anim["alt"],
                    "caption": anim["caption"],
                })
        for extra in page_meta.get("illustrations", []):
            asset = lesson_asset(path, extra["file"], lesson_meta, animation_assets)
            after_paragraph = extra.get("after_paragraph", -1)
            if after_paragraph < -1 or after_paragraph >= len(page["paragraphs"]):
                raise ValueError(f"Illustration position is outside Page paragraphs in {path}, page {index + 1}")
            item = {
                "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                "title": extra.get("title", title),
                "alt": extra["alt"],
                "caption": extra["caption"],
                "after_paragraph": after_paragraph,
            }
            for key in ("credit", "source_url", "license_label", "license_url"):
                if key in extra:
                    item[key] = extra[key]
            illustrations.append(item)
        if illustrations:
            page["illustrations"] = illustrations
        pages.append(page)
    if not pages:
        raise ValueError(f"Lesson source has no Page headings: {path}")
    return pages


def build(source_revision: str = "local-draft", source_label: str = "local draft") -> dict:
    course_meta = yaml.safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))
    units = []
    for item in course_meta["units"]:
        unit_path = ROOT / item["path"]
        if unit_path.exists():
            metadata, _ = read_front_matter(unit_path)
            title = metadata.get("title", item["title"])
            unit_id = metadata.get("id", item["id"])
        else:
            title, unit_id = item["title"], item["id"]
        units.append({"id": unit_id, "title": title})

    lessons = []
    unit_order = {item["id"]: index for index, item in enumerate(course_meta["units"])}
    for unit_config in course_meta["units"]:
        unit_path = ROOT / unit_config["path"]
        if not unit_path.exists():
            continue
        unit_meta, _ = read_front_matter(unit_path)
        for order, lesson_ref in enumerate(unit_meta.get("lessons", [])):
            lesson_path = unit_path.parent / lesson_ref["path"]
            lesson_meta, _ = read_front_matter(ROOT / lesson_path)
            lesson = {
                "id": lesson_meta["id"],
                "unit": unit_config["id"],
                "title": lesson_meta["title"],
                "terms": [],
                "pages": reading_pages(ROOT / lesson_path, lesson_meta, course_meta.get("animation_assets", {})),
                "source": "oeweo-network-wiki",
                "source_path": lesson_meta.get("source_wiki")
                or (lesson_meta.get("source", {}).get("lesson_path", "")
                    if isinstance(lesson_meta.get("source"), dict) else ""),
                "reading": [],
                "question": "",
                "choices": [],
                "scenario": "",
                "commands": [],
                "controls": [],
                "hint": "",
                "explain": "",
                "kind": "reading",
            }
            lessons.append((unit_order[unit_config["id"]], order, lesson))
    lessons = [lesson for _, _, lesson in sorted(lessons, key=lambda item: (item[0], item[1]))]
    active_units = {lesson["unit"] for lesson in lessons}
    return {
        "version": f"network-{source_revision}",
        "title": course_meta["course"]["title"],
        "units": [unit for unit in units if unit["id"] in active_units],
        "lessons": lessons,
        "limits": f"PREVIEW ONLY · {source_label} · not published",
        "preview_source": {
            "label": source_label,
            "sha": source_revision,
            "url": f"https://github.com/FutureReadyCampus/learn-course-network-foundations/commit/{source_revision}",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "preview/learn-network-course.json")
    parser.add_argument("--source-revision", default="local-draft")
    parser.add_argument("--source-label", default="local draft")
    args = parser.parse_args()
    catalog = build(args.source_revision, args.source_label)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(catalog['units'])} units and {len(catalog['lessons'])} lessons: {args.output}")


if __name__ == "__main__":
    main()
