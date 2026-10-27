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


def reading_pages(path: Path, beginner_path: Path, diagram_path: Path, illustrated_pages: list[int]) -> list[dict]:
    source = path.read_text(encoding="utf-8")
    edition = source.split("<!-- reading-edition:start -->", 1)[1].split("<!-- reading-edition:end -->", 1)[0]
    sections = re.findall(r"^### (.+?)\s*\n(.*?)(?=^### |\Z)", edition, re.M | re.S)
    concepts = json.loads(beginner_path.read_text(encoding="utf-8"))["concepts"]
    pages = []
    for index, (heading, body) in enumerate(sections):
        title = re.sub(r"\s*·\s*\d+:\d+.*$", "", heading).strip()
        concept = concepts[min(index, len(concepts) - 1)] if concepts else {}
        page = {
            "title": title,
            "paragraphs": split_paragraphs(body),
            "terms": [item["term"] for item in concept.get("terms", [])],
            "questions": [],
        }
        illustrations = []
        if index == 0:
            illustrations.append({
                "src": f"/api/v1/network-course-assets/{diagram_path.relative_to(ROOT).as_posix()}",
                "title": f"{title} · 학습 흐름",
                "alt": f"{title}의 Wiki 학습 흐름 그림",
                "caption": "Wiki 제공 그림",
            })
        if index + 1 in illustrated_pages and concept.get("anim"):
            anim = concept["anim"]
            asset = ROOT / "sources/wiki/oeweo-network/newbie/anim" / anim["file"]
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
        raise ValueError(f"Wiki reading edition has no sections: {path}")
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
        for order, item in enumerate(unit_meta.get("wiki_lessons", [])):
            lesson = {
                "id": item["id"],
                "unit": unit_config["id"],
                "title": item["title"],
                "terms": [],
                "pages": reading_pages(
                    ROOT / item["path"],
                    ROOT / item["beginner_guide"],
                    ROOT / item["wiki_diagram"],
                    item.get("illustrated_pages", []),
                ),
                "source": "oeweo-network-wiki",
                "source_path": item["path"],
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
    return {
        "version": f"network-{source_revision}",
        "title": course_meta["course"]["title"],
        "units": units,
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
