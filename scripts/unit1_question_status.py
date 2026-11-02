#!/usr/bin/env python3
"""Print Unit 1 Page and question counts, rejecting duplicate YAML keys."""
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "units/01-before-networking"


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            mark = key_node.start_mark
            raise ValueError(
                f"duplicate YAML key {key!r} at {mark.name}:{mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def load_yaml(text, source):
    try:
        return yaml.load(text, Loader=UniqueKeyLoader) or {}
    except (yaml.YAMLError, ValueError) as error:
        raise ValueError(f"{source}: {error}") from error


def main():
    unit_data = load_yaml((UNIT / "unit.md").read_text(encoding="utf-8").split("---", 2)[1], UNIT / "unit.md")
    print("| Lesson | Title | Pages | Questions |")
    print("|---|---|---:|---:|")
    for item in unit_data.get("lessons", []):
        path = UNIT / item["path"]
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3:
            raise ValueError(f"Missing YAML front matter: {path}")
        metadata = load_yaml(parts[1], path)
        page_count = len(re.findall(r"^## .+?\s*$", parts[2], re.M))
        pages = metadata.get("pages", [])
        if len(pages) != page_count:
            raise ValueError(f"Page metadata mismatch in {path}: {page_count} headings, {len(pages)} entries")

        quiz_file = metadata.get("quiz_file")
        if quiz_file:
            quiz_path = path.parent / quiz_file
            quiz_data = load_yaml(quiz_path.read_text(encoding="utf-8"), quiz_path)
            quizzes = quiz_data.get("quizzes", {})
            placed = re.findall(r"<!--\s*quiz:\s*([\w-]+)\s*-->", parts[2])
            if len(placed) != len(set(placed)) or set(placed) != set(quizzes):
                raise ValueError(f"Quiz markers do not match quiz sets in {path}")
            question_count = sum(
                len(quizzes[quiz_id].get("questions", [])) for quiz_id in placed
            )
        else:
            question_count = sum(len(page.get("questions", [])) for page in pages)
        print(f"| `{metadata['id']}` | {metadata['title']} | {page_count} | {question_count} |")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
