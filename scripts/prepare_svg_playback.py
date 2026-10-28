#!/usr/bin/env python3
"""Build per-asset runtime copies using the reviewed loop durations."""

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
config = yaml.safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))["animation_assets"]
source = ROOT / config["source_dir"]
runtime = ROOT / config["runtime_dir"]
durations = yaml.safe_load((ROOT / config["durations_file"]).read_text(encoding="utf-8"))["animations"]
files = sorted(source.glob("*.svg"))
if set(durations) != {path.name for path in files}:
    raise ValueError("Playback map must contain each source SVG exactly once")
runtime.mkdir(parents=True, exist_ok=True)
pattern = re.compile(r'(\bdur=["\'])([0-9]+(?:\.[0-9]+)?)(s)(["\'])')
for path in files:
    target = float(durations[path.name])
    if target <= 0:
        raise ValueError(f"Invalid loop duration for {path.name}: {target}")
    text, count = pattern.subn(lambda match: f"{match.group(1)}{float(match.group(2)) * target / 10:g}{match.group(3)}{match.group(4)}", path.read_text(encoding="utf-8"))
    if not count:
        raise ValueError(f"No SMIL durations found in {path.name}")
    ET.fromstring(text)
    (runtime / path.name).write_text(text, encoding="utf-8")
print(f"Prepared {len(files)} source SVGs with individual playback durations in {runtime.relative_to(ROOT)}")
