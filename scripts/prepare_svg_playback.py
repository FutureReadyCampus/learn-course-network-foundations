#!/usr/bin/env python3
"""Build per-Lesson runtime animation copies from Lesson-owned SVG sources."""

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
config = yaml.safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))["animation_assets"]
durations = yaml.safe_load((ROOT / config["durations_file"]).read_text(encoding="utf-8"))["animations"]
source_files = sorted(ROOT.glob("units/*/lessons/*/assets/animation-source/*.svg"))
if {path.name for path in source_files} != set(durations):
    raise ValueError("Playback map must contain each Lesson-owned source SVG exactly once by filename")
pattern = re.compile(r'(\bdur=["\'])([0-9]+(?:\.[0-9]+)?)(s)(["\'])')
for path in source_files:
    target = float(durations[path.name])
    if target <= 0:
        raise ValueError(f"Invalid loop duration for {path.name}: {target}")
    text, count = pattern.subn(lambda match: f"{match.group(1)}{float(match.group(2)) * target / 10:g}{match.group(3)}{match.group(4)}", path.read_text(encoding="utf-8"))
    if not count:
        raise ValueError(f"No SMIL durations found in {path.name}")
    ET.fromstring(text)
    destination = path.parent.parent / "animations" / path.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
print(f"Prepared {len(source_files)} Lesson-owned source SVGs with individual playback durations")
