#!/usr/bin/env python3
"""Build the Learn Network catalog from the course Markdown source."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


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


def reading_pages(path: Path, lesson_meta: dict, animation_assets: dict) -> list[dict]:
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
    page_groups = lesson_meta.get("page_groups")
    if page_groups:
        grouped_sections = []
        for group in page_groups:
            indices = group["sections"]
            if not indices or any(index < 1 or index > len(sections) for index in indices):
                raise ValueError(f"Invalid page group sections in {path}")
            grouped_sections.append((group["title"], "\n\n".join(sections[index - 1][1] for index in indices)))
        sections = grouped_sections
>>>>>>> cfffb2b (content: combine short Unit 1 Lesson 1 pages)
    diagram_ref = lesson_meta.get("wiki_diagram")
    diagram_path = ROOT / diagram_ref if diagram_ref else None
    illustrated_pages = lesson_meta.get("illustrated_pages", [])
    lesson_animation_dir = lesson_meta.get("animations_dir")
    pages = []
    for index, (heading, body) in enumerate(sections):
        title = re.sub(r"\s*·\s*\d+:\d+.*$", "", heading).strip()
<<<<<<< HEAD
        concept = concepts[min(index, len(concepts) - 1)] if concepts else {}
        page_meta = page_metadata[index] if index < len(page_metadata) else {}
        page = {
            "title": title,
            "paragraphs": split_paragraphs(body),
            "terms": page_meta.get("terms", [item["term"] for item in concept.get("terms", [])]),
=======
        concept_indices = [section_index - 1 for section_index in page_groups[index]["sections"]] if page_groups else ([min(index, len(concepts) - 1)] if concepts else [])
        page_concepts = [concepts[concept_index] for concept_index in concept_indices if concept_index < len(concepts)]
        page_meta = page_metadata[index] if index < len(page_metadata) else {}
        page = {
            "title": title,
            "paragraphs": split_paragraphs(body),
            "terms": page_meta.get("terms", list(dict.fromkeys(item["term"] for concept in page_concepts for item in concept.get("terms", [])))),
>>>>>>> cfffb2b (content: combine short Unit 1 Lesson 1 pages)
            "questions": [],
        }
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
                candidates = []
                if lesson_animation_dir:
                    candidates.append(ROOT / lesson_animation_dir / anim["file"])
                runtime_dir = animation_assets.get("runtime_dir")
                if runtime_dir:
                    candidates.append(ROOT / runtime_dir / anim["file"])
                source_dir = animation_assets.get("source_dir", "sources/wiki/oeweo-network/newbie/anim")
                candidates.append(ROOT / source_dir / anim["file"])
                asset = next((candidate for candidate in candidates if candidate.is_file()), None)
                if asset is None:
                    raise FileNotFoundError(f"Missing SVG animation {anim['file']} for {path}")
                illustrations.append({
                    "src": f"/api/v1/network-course-assets/{asset.relative_to(ROOT).as_posix()}",
                    "title": anim["title"],
                    "alt": anim["alt"],
                    "caption": anim["caption"],
                })
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
                "source_path": lesson_meta["source_wiki"],
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
