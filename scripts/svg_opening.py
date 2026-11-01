"""Shared two-second title cover and segmented playback bar for animated SVGs."""

from __future__ import annotations

import html
import re
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


ANIMATION_TAGS = {"animate", "animateTransform", "animateMotion", "set"}
STEP_TEXT = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")
GROUP_TAG = re.compile(r"</?g\b[^>]*>")
TEXT_TAG = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.DOTALL)
ANIMATE_TAG = re.compile(r"<(?:animate|animateTransform|animateMotion|set)\b[^>]*>", re.DOTALL)
ATTR = re.compile(r"([\w:-]+)\s*=\s*(['\"])(.*?)\2", re.DOTALL)


def _attributes(tag: str) -> dict[str, str]:
    return {match.group(1): match.group(3) for match in ATTR.finditer(tag)}


def _group_ranges(svg: str) -> list[tuple[int, int, dict[str, str], str]]:
    stack: list[tuple[int, dict[str, str]]] = []
    ranges = []
    for match in GROUP_TAG.finditer(svg):
        token = match.group(0)
        if token.startswith("</"):
            if stack:
                start, attrs = stack.pop()
                ranges.append((start, match.end(), attrs, svg[start:match.end()]))
        elif not token.rstrip().endswith("/>"):
            stack.append((match.start(), _attributes(token)))
    return sorted(ranges, key=lambda item: item[0])


def _counter_values(fragment: str) -> dict[int, tuple[int, str]]:
    values: dict[int, tuple[int, str]] = {}
    for attrs, body in TEXT_TAG.findall(fragment):
        text = html.unescape(re.sub(r"<[^>]*>", "", body)).strip()
        match = STEP_TEXT.fullmatch(text)
        if not match:
            continue
        stage, total = int(match.group(1)), int(match.group(2))
        if stage not in values:
            values[stage] = (total, body)
    return values


def _stage_start(body: str) -> float | None:
    animate = next(
        (tag for tag in ANIMATE_TAG.findall(body) if _attributes(tag).get("attributeName") == "opacity"),
        None,
    )
    if not animate:
        return None
    attrs = _attributes(animate)
    values = attrs.get("values", "").split(";")
    times = attrs.get("keyTimes", "").split(";")
    if len(values) != len(times):
        return None
    for value, time in zip(values, times):
        try:
            if float(value) >= 0.99:
                return float(time)
        except ValueError:
            return None
    return None


def _counter_group_ranges(svg: str) -> list[tuple[int, int, dict[str, str], str]]:
    candidates = []
    for start, end, attrs, fragment in _group_ranges(svg):
        numbers = _counter_values(fragment)
        totals = {total for total, _ in numbers.values()}
        if not numbers or len(totals) != 1:
            continue
        total = next(iter(totals))
        if set(numbers) != set(range(1, total + 1)):
            continue
        marked = attrs.get("aria-label") == "재생 단계" or "stage-indicator" in attrs.get("class", "").split()
        badge = re.search(r"<rect\b[^>]*\bx=['\"]40['\"][^>]*\by=['\"]28['\"][^>]*\bwidth=['\"]88['\"][^>]*\bheight=['\"]40['\"]", fragment)
        if marked or badge:
            candidates.append((start, end, attrs, fragment))
    return [
        candidate
        for candidate in candidates
        if not any(
            other[0] > candidate[0] and other[1] < candidate[1]
            for other in candidates
        )
    ]


def stage_model(svg: str) -> tuple[int, list[float]] | None:
    """Return stage count and normalized stage start times from the topmost indicator."""
    # Preserve an already-generated progress bar when re-running the asset builder.
    try:
        root = ET.fromstring(svg)
    except ET.ParseError:
        root = None
    if root is not None:
        for group in root.iter():
            if group.tag.rsplit("}", 1)[-1] != "g" or group.get("aria-label") != "재생 진행 막대":
                continue
            try:
                total = int(group.get("data-stage-count", ""))
            except ValueError:
                continue
            starts: dict[int, float] = {}
            for segment in group:
                if segment.tag.rsplit("}", 1)[-1] != "g":
                    continue
                try:
                    stage = int(segment.get("data-stage", ""))
                except ValueError:
                    continue
                animation = next(
                    (node for node in segment.iter() if node.tag.rsplit("}", 1)[-1] == "animate" and node.get("attributeName") == "width"),
                    None,
                )
                if animation is None:
                    continue
                times = animation.get("keyTimes", "").split(";")
                try:
                    starts[stage] = 0.0 if stage == 1 else float(times[1])
                except (IndexError, ValueError):
                    continue
            if set(starts) == set(range(1, total + 1)):
                return total, [starts[index] for index in range(1, total + 1)]

    groups = _counter_group_ranges(svg)
    if not groups:
        return None
    # Later SVG groups are painted last, which resolves legacy duplicate counters.
    _, _, _, fragment = groups[-1]
    records = _counter_values(fragment)
    total = next(iter(records.values()))[0]
    starts = []
    for stage in range(1, total + 1):
        parsed = _stage_start(records[stage][1])
        starts.append(0.0 if stage == 1 else parsed if parsed is not None else -1.0)
    if starts[0] != 0.0 or any(value < 0 for value in starts) or any(a >= b for a, b in zip(starts, starts[1:])) or starts[-1] >= 1:
        starts = [(index - 1) / total for index in range(1, total + 1)]
    return total, starts


def _strip_svg_groups(svg: str, predicate) -> str:
    ranges = [item for item in _group_ranges(svg) if predicate(item[2], item[3])]
    ranges = [
        item for item in ranges
        if not any(other[0] > item[0] and other[1] < item[1] for other in ranges)
    ]
    for start, end, _, _ in sorted(ranges, reverse=True):
        svg = svg[:start] + svg[end:]
    return svg


def _strip_generated_groups(svg: str) -> str:
    svg = _strip_svg_groups(
        svg,
        lambda attrs, _: attrs.get("id") in {"intro", "title-intro"}
        or attrs.get("aria-label") in {"재생 진행 막대", "재생 단계"}
        or "stage-indicator" in attrs.get("class", "").split(),
    )
    ranges = _counter_group_ranges(svg)
    for start, end, _, _ in sorted(ranges, reverse=True):
        svg = svg[:start] + svg[end:]
    return svg


def scene_loop_seconds(svg: str) -> float:
    cleaned = _strip_generated_groups(svg)
    root = ET.fromstring(cleaned)
    durations = Counter()
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] not in ANIMATION_TAGS:
            continue
        match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)s", node.get("dur", ""))
        if match:
            durations[float(match.group(1))] += 1
    if not durations:
        raise ValueError("animated SVG has no timed SMIL elements")
    return durations.most_common(1)[0][0]


def lesson_title(path: Path, filename: str | None = None) -> str:
    """Find the authored illustration title in the owning lesson metadata."""
    import yaml

    lesson = next((parent / "lesson.md" for parent in path.parents if (parent / "lesson.md").is_file()), None)
    if lesson:
        content = lesson.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) == 3:
            metadata = yaml.safe_load(parts[1]) or {}
            wanted = filename or path.name

            def search(value):
                if isinstance(value, dict):
                    if Path(str(value.get("file", ""))).name == wanted and value.get("title"):
                        return str(value["title"])
                    for child in value.values():
                        found = search(child)
                        if found:
                            return found
                elif isinstance(value, list):
                    for child in value:
                        found = search(child)
                        if found:
                            return found
                return None

            found = search(metadata)
            if found:
                return found
    return " ".join(Path(filename or path.name).stem.replace("_", "-").split("-"))


def _title(svg: str, fallback: str | None) -> str:
    root = ET.fromstring(svg)
    for node in root:
        if node.tag.rsplit("}", 1)[-1] == "title" and "".join(node.itertext()).strip():
            return " ".join("".join(node.itertext()).split())
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] != "text" or node.get("x") not in {"480", "560"}:
            continue
        try:
            if float(node.get("y", "9999")) > 110:
                continue
        except ValueError:
            continue
        value = " ".join("".join(node.itertext()).split())
        if value:
            return value
    return fallback or "lesson scene"


def _delay_animations(svg: str) -> str:
    def delay(match: re.Match[str]) -> str:
        tag = match.group(0)
        attrs = _attributes(tag)
        if "begin" not in attrs:
            self_closing = tag.rstrip().endswith("/>")
            body = tag[:-2] if self_closing else tag[:-1]
            return body + ' begin="2s"' + ("/>" if self_closing else ">")
        if attrs["begin"] == "2s":
            return tag
        begin_match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)s", attrs["begin"])
        if begin_match:
            new_begin = f"{float(begin_match.group(1)) + 2:g}s"
        else:
            new_begin = f"2s;{attrs['begin']}"
        return re.sub(r"\bbegin\s*=\s*(['\"]).*?\1", f'begin="{new_begin}"', tag, count=1)

    return ANIMATE_TAG.sub(delay, svg)


def _view_box(svg: str) -> tuple[float, float, float, float]:
    root_tag = re.search(r"<svg\b[^>]*>", svg)
    attrs = _attributes(root_tag.group(0)) if root_tag else {}
    try:
        values = [float(value) for value in re.split(r"[\s,]+", attrs["viewBox"].strip())]
        if len(values) == 4 and values[2] > 0 and values[3] > 0:
            return values[0], values[1], values[2], values[3]
    except (KeyError, ValueError):
        pass
    return 0.0, 0.0, 960.0, 540.0


def _font_size(title: str, width: float) -> float:
    units = sum(0.98 if ord(char) > 0x1100 else 0.3 if char in ". " else 0.6 for char in title)
    return max(40.0, min(82.0, (width - 88) / max(units, 1)))


def apply_opening(
    svg: str,
    *,
    loop_seconds: float | None = None,
    title: str | None = None,
    model: tuple[int, list[float]] | None = None,
) -> str:
    """Replace numeric stage badges with a synchronized title cover and progress bar."""
    model = model or stage_model(svg)
    if model is None:
        raise ValueError("animated SVG has no complete stage indicator")
    loop_seconds = loop_seconds or scene_loop_seconds(svg)
    title = title or _title(svg, None)
    total, starts = model
    end_time = loop_seconds + 2
    enter, hold, end = 0.4 / end_time, 1.7 / end_time, 2 / end_time
    x0, y0, width, height = _view_box(svg)

    svg = _strip_generated_groups(svg)
    svg = _delay_animations(svg)

    margin = min(40.0, width * 0.08)
    gap = min(8.0, max(2.0, (width - 2 * margin) / max(total * 3, 1)))
    bar_width = width - 2 * margin
    segment_width = (bar_width - gap * (total - 1)) / total
    bar_height = max(4.0, min(6.0, height * 0.012))
    bar_y = y0 + height - max(8.0, bar_height + 2)

    segments = []
    for index in range(total):
        x = x0 + margin + index * (segment_width + gap)
        start = starts[index]
        finish = starts[index + 1] if index + 1 < total else 1.0
        if index == 0:
            values = f"0;{segment_width:g};{segment_width:g}"
            key_times = f"0;{finish:.6f};1"
        elif finish >= 1:
            values = f"0;0;{segment_width:g}"
            key_times = f"0;{start:.6f};1"
        else:
            values = f"0;0;{segment_width:g};{segment_width:g}"
            key_times = f"0;{start:.6f};{finish:.6f};1"
        segments.append(
            f'<g class="progress-segment" data-stage="{index + 1}">'
            f'<rect x="{x:g}" y="{bar_y:g}" width="{segment_width:g}" height="{bar_height:g}" rx="{bar_height / 2:g}" fill="#394554"/>'
            f'<rect x="{x:g}" y="{bar_y:g}" width="0" height="{bar_height:g}" rx="{bar_height / 2:g}" fill="#ff3434">'
            f'<animate begin="2s" attributeName="width" values="{values}" keyTimes="{key_times}" dur="{loop_seconds:g}s" repeatCount="indefinite"/>'
            f'</rect></g>'
        )
    progress = f'<g aria-label="재생 진행 막대" data-stage-count="{total}">' + "".join(segments) + "</g>"

    safe_title = html.escape(title, quote=False)
    font_size = _font_size(title, width)
    center_x = x0 + width / 2
    center_y = y0 + height / 2 + font_size * 0.35
    intro = (
        f'<g id="title-intro"><rect x="{x0:g}" y="{y0:g}" width="{width:g}" height="{height:g}" fill="#0f1115"/>'
        f'<g opacity="0"><text x="{center_x:g}" y="{center_y:g}" text-anchor="middle" font-size="{font_size:g}" font-weight="750" letter-spacing="-1" fill="#e6e8ec">{safe_title}</text>'
        f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;{enter:.6f};{hold:.6f};{end:.6f};1" dur="{end_time:g}s" repeatCount="indefinite"/>'
        f'<animateTransform attributeName="transform" type="translate" values="0 28;0 0;0 0;0 -32;0 -32" keyTimes="0;{enter:.6f};{hold:.6f};{end:.6f};1" dur="{end_time:g}s" repeatCount="indefinite"/></g>'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;{hold:.6f};{end:.6f};1" dur="{end_time:g}s" repeatCount="indefinite"/></g>'
    )
    svg = re.sub(r"</svg\s*>\s*$", progress + intro + "</svg>", svg, count=1)
    ET.fromstring(svg)
    return svg
