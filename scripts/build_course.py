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


def build() -> dict:
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
    for path in sorted(ROOT.glob("units/**/lessons/**/lesson.md")):
        metadata, _ = read_front_matter(path)
        step_paths = sorted((path.parent / "steps").glob("*.md"))
        pages = []
        for step_path in step_paths:
            body = step_path.read_text(encoding="utf-8").strip()
            heading, _, content = body.partition("\n")
            title = heading.removeprefix("# ").strip()
            pages.append({
                "title": title,
                "paragraphs": split_paragraphs(content),
                "terms": [],
                "questions": [],
            })
        if not pages:
            raise ValueError(f"Lesson has no step Markdown files: {path.parent}")
        lesson = {
            "id": metadata["id"],
            "unit": metadata["unit"],
            "title": metadata["title"],
            "terms": [],
            "pages": pages,
            "source": "learn-course-network-foundations",
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
        lessons.append((unit_order[metadata["unit"]], metadata.get("order", 0), lesson))
    lessons = [lesson for _, _, lesson in sorted(lessons, key=lambda item: (item[0], item[1]))]
    return {
        "version": "network-foundations-local-draft",
        "title": course_meta["course"]["title"],
        "units": units,
        "lessons": lessons,
        "limits": "LOCAL PREVIEW ONLY · Generated from Markdown; not published",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "preview/learn-network-course.json")
    args = parser.parse_args()
    catalog = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(catalog['units'])} units and {len(catalog['lessons'])} lessons: {args.output}")


if __name__ == "__main__":
    main()
