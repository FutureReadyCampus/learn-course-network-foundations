#!/usr/bin/env python3
"""Check every course animation for a visible, upper-left step counter."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ANIMATION_TAGS = {"animate", "animateMotion", "animateTransform", "set"}
STEP_TEXT = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def is_at(element: ET.Element, **expected: str) -> bool:
    return all(element.get(name) == value for name, value in expected.items())


def has_step_badge(path: Path) -> tuple[bool, str]:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        return False, f"invalid SVG XML: {error}"

    animated = any(local_name(node) in ANIMATION_TAGS for node in root.iter())
    if not animated:
        return True, "static SVG (no playback stages)"

    groups = []
    for node in root.iter():
        if local_name(node) != "g":
            continue
        classes = set(node.get("class", "").split())
        if node.get("aria-label") == "재생 단계" or "stage-indicator" in classes:
            groups.append(node)

    for group in groups:
        descendants = list(group.iter())
        badge = any(
            local_name(node) == "rect"
            and is_at(node, x="40", y="28", width="88", height="40")
            for node in descendants
        )
        fractions: set[tuple[int, int]] = set()
        for node in descendants:
            if local_name(node) != "text" or not is_at(node, x="84", y="55"):
                continue
            match = STEP_TEXT.match("".join(node.itertext()))
            if match:
                fractions.add((int(match.group(1)), int(match.group(2))))
        if not badge or not fractions:
            continue
        totals = {total for _, total in fractions}
        if len(totals) != 1:
            continue
        total = next(iter(totals))
        if {step for step, _ in fractions} != set(range(1, total + 1)):
            continue
        return True, f"{total} stages at x=40, y=28"

    return False, "animated SVG lacks a complete upper-left 1/N stage badge"


def main() -> int:
    animations = []
    static = []
    errors = []
    asset_files = sorted(
        path
        for path in (ROOT / "units").glob("*/lessons/*/assets/**/*.svg")
        if any(directory in path.parts for directory in ("diagrams", "animations", "animation-source"))
    )
    for path in asset_files:
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid SVG XML: {error}")
            continue
        animated = any(local_name(node) in ANIMATION_TAGS for node in root.iter())
        if animated:
            animations.append(path)
        elif "diagrams" in path.parts:
            static.append(path)

    for path in animations:
        ok, detail = has_step_badge(path)
        if not ok:
            errors.append(f"{path.relative_to(ROOT)}: {detail}")

    if errors:
        print("SVG step audit failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"SVG step audit passed: {len(animations)} animated SVGs; {len(static)} static diagrams need no playback steps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
