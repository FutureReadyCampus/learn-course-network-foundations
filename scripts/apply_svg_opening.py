#!/usr/bin/env python3
"""Apply the shared opening and segmented progress bar to every animated course SVG."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from svg_opening import ANIMATION_TAGS, apply_opening, lesson_title, scene_loop_seconds, stage_model


def animated(text: str) -> bool:
    root = ET.fromstring(text)
    return any(node.tag.rsplit("}", 1)[-1] in ANIMATION_TAGS for node in root.iter())


def main() -> int:
    paths = sorted(path for path in ROOT.glob("units/*/lessons/*/assets/**/*.svg") if path.is_file())
    paths += sorted(path for path in ROOT.glob("units/*/lessons/*/assets/*.svg") if path.is_file())
    paths = sorted(set(paths))
    totals = Counter()
    errors = []

    for path in paths:
        try:
            source = path.read_text(encoding="utf-8")
            if not animated(source):
                continue
            model = stage_model(source)
            if model is None:
                canonical = path.parent / "animations" / path.name
                if not canonical.is_file():
                    raise ValueError("no stage counter and no canonical animation counterpart")
                model = stage_model(canonical.read_text(encoding="utf-8"))
            if model is None:
                raise ValueError("no complete stage model")
            loop_seconds = scene_loop_seconds(source)
            title = lesson_title(path)
            updated = apply_opening(source, loop_seconds=loop_seconds, title=title, model=model)
            path.write_text(updated, encoding="utf-8")
            totals[path.parent.name] += 1
        except Exception as error:  # report all problem assets before failing
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    print("Updated animated SVGs by asset directory:")
    for name, count in sorted(totals.items()):
        print(f"  {name}: {count}")
    print(f"Total: {sum(totals.values())}")
    if errors:
        print("Errors:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
