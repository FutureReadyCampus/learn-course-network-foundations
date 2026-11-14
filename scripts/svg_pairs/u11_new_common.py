"""Shared helpers for the Unit 11 "new" example SVGs (u11_l{LL}_new_*.py).

Imports the existing kit/u11 helpers without modifying them. Each Page SVG is 4 steps:
① 상황 → ② 동작 → ③ 결과(✓/✗) → ④ 기억할 점; only the element that changes in a step gets the orange outline.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import hl, dur, cell  # noqa: F401
from u7_l01 import mv  # noqa: F401

ROOT = Path(__file__).resolve().parents[2]
Y = 300
UNIT = ROOT / "units" / "07-network-devices" / "lessons" / "restructured"


def lesson_dir(n):
    return next(UNIT.glob(f"{n:02d}-*"))


def new():
    return Anim(4, dur(False))


def mark(a, x, y, w, h, t):
    """Orange outline shown only in step t (the one thing that changed)."""
    return a.vis(hl(x, y, w, h), t, t)


def lbl(x, y, s, c=MUTED, fs=15, weight=None):
    return text(x, y, s, fs, c, weight)


def node(x, y, label, sub=None, w=150, h=70, c=BLUE, fs=18):
    """Rounded device box centred at (x, y) with an optional address line under it."""
    s = box(x - w / 2, y - h / 2, w, h, c, PANEL, 12, sw=3) + text(x, y + fs * 0.36, label, fs, c, 700)
    return s + (lbl(x, y + h / 2 + 22, sub) if sub else "")


def server(x, y, label="AI 서비스", sub=None, c=GREEN):
    s = (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
         + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
         + text(x, y + 62, label, 18, TXT, 700))
    return s + (lbl(x, y + 82, sub) if sub else "")


def cloud(x, y, label="인터넷"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
            + text(x, y + 7, label, 20, BLUE, 700))


def doc(x, y, c=ORANGE):
    return (f'<rect x="{x - 16}" y="{y - 20}" width="32" height="40" rx="3" fill="{c}"/>'
            f'<rect x="{x - 9}" y="{y - 10}" width="18" height="3" fill="{BG}"/><rect x="{x - 9}" y="{y - 2}" width="18" height="3" fill="{BG}"/>')


def dev(label, x, y, sub=None, fn=None):
    """Icon device (kit helpers) with an address line under its label."""
    s = fn(x, y, label)
    return s + (lbl(x, y + 72, sub) if sub else "")


def wire_pages(lesson, items):
    """items: [(page_id, file_stem, title, alt, caption, after_paragraph)].
    Replace that Page's whole `illustrations:` block with the single new item (inserted right after `- page_id:`)."""
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = lesson / "lesson.md"
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    want = {it[0]: it for it in items}
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        out.append(l)
        i += 1
        if l.startswith("- page_id: ") and l[len("- page_id: "):] in want:
            _, f, t, al, c, ap = want.pop(l[len("- page_id: "):])
            out += ["  illustrations:", f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}",
                    f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            if i < len(lines) and lines[i] == "  illustrations:":
                i += 1
                while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                    i += 1
    assert not want, f"page ids not found: {list(want)}"
    md.write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")


def run(lesson_no, scenes, argv):
    """scenes: [(page_id, stem, title, alt, caption, after_paragraph, fn)]"""
    d = lesson_dir(lesson_no)
    out = d / "assets" / "animations"
    out.mkdir(parents=True, exist_ok=True)
    for _p, stem, *_r, fn in scenes:
        write(out, stem, fn())
    if "--svg-only" not in argv:
        wire_pages(d, [s[:6] for s in scenes])
    print("ok", len(scenes), "svgs", d.name)
