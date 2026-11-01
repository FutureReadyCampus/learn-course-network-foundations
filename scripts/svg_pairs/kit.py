"""Helpers for course-style SMIL SVGs (960x540, 1/N step badge, caption bar).

Animations are written with their final loop length (`Anim(n, dur)`), straight into a
Lesson's assets/animations/. They need no animation-source copy or svg-playback.yaml row.
"""
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from svg_opening import apply_opening

BG, PANEL, LINE, TXT, MUTED = "#0f1115", "#171a21", "#3d4b60", "#e6e8ec", "#9aa3b2"
GREEN, BLUE, ORANGE, RED = "#7ee7c7", "#6ea8fe", "#ffb454", "#ff7b72"
VIOLET = "#c792ea"
EPS = 0.015


def tw(text, fs):
    """Approximate rendered width of mixed Hangul/ASCII text."""
    return sum(0.98 if ord(c) > 0x1100 else 0.3 if c in ". " else 0.6 for c in text) * fs


class Anim:
    def __init__(self, n, dur=15):
        self.n = n
        self.dur = dur

    def window(self, start, end=None):
        n = self.n
        end = n if end is None else end
        # integer end = end of that step; fractional end = that point inside the step
        t1 = end / n if float(end).is_integer() else (end - 1) / n
        return max(0.0, (start - 1) / n), min(1.0, t1)

    def vis(self, inner, start=1, end=None):
        t0, t1 = self.window(start, end)
        if t0 <= 0 and t1 >= 1:
            return f"<g>{inner}</g>"
        if t0 <= 0:
            vals, keys, init = "1;1;0;0", f"0;{t1 - EPS:.3f};{t1:.3f};1", 1
        elif t1 >= 1:
            vals, keys, init = "0;0;1;1", f"0;{t0:.3f};{t0 + EPS:.3f};1", 0
        else:
            vals, keys, init = "0;0;1;1;0;0", f"0;{t0:.3f};{t0 + EPS:.3f};{t1 - EPS:.3f};{t1:.3f};1", 0
        return (f'<g opacity="{init}"><animate attributeName="opacity" values="{vals}" keyTimes="{keys}" '
                f'dur="{self.dur:g}s" repeatCount="indefinite"/>{inner}</g>')

    def move(self, inner, pts, step, f0=0.1, f1=0.6):
        """Translate along pts during [f0, f1] of `step`; hold endpoints outside."""
        n = self.n
        ta, tb = (step - 1 + f0) / n, (step - 1 + f1) / n
        k = len(pts) - 1
        times = [ta + (tb - ta) * i / k for i in range(k + 1)]
        vals = [pts[0]] + list(pts) + [pts[-1]]
        keys = [0.0] + times + [1.0]
        v = ";".join(f"{x},{y}" for x, y in vals)
        kt = ";".join(f"{t:.3f}" for t in keys)
        return (f'<g><animateTransform attributeName="transform" type="translate" values="{v}" keyTimes="{kt}" '
                f'dur="{self.dur:g}s" repeatCount="indefinite"/>{inner}</g>')


def text(x, y, s, fs=20, fill=TXT, weight=None, anchor="middle", raw=False):
    w = f' font-weight="{weight}"' if weight else ""
    body = s if raw else escape(s)
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{fs}"{w} fill="{fill}">{body}</text>'


def pill(x, y, s, color=GREEN, fs=18, filled=False, w=None):
    """Rounded tag centred at (x, y)."""
    w = w or tw(s, fs) + 28
    h = fs + 16
    fill, tfill = (color, BG) if filled else (BG, color)
    return (f'<rect x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h}" rx="{h / 2:.0f}" fill="{fill}" '
            f'stroke="{color}" stroke-width="2"/>' + text(x, y + fs * 0.36, s, fs, tfill, 700))


def box(x, y, w, h, stroke=LINE, fill=PANEL, rx=10, dash=False, sw=2):
    d = ' stroke-dasharray="8 6"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, color=LINE, w=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>'


def check(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="16" fill="{GREEN}"/>'
            f'<path d="M{x - 8} {y} l6 6 l11 -12" fill="none" stroke="{BG}" stroke-width="4"/>')


def cross(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="16" fill="{RED}"/>'
            f'<path d="M{x - 7} {y - 7} l14 14 M{x + 7} {y - 7} l-14 14" stroke="{BG}" stroke-width="4"/>')


def ask(x, y):
    return f'<circle cx="{x}" cy="{y}" r="16" fill="{ORANGE}"/>' + text(x, y + 7, "?", 22, BG, 700)


def parcel(x=0, y=0):
    return (f'<rect x="{x - 18}" y="{y - 14}" width="36" height="28" rx="3" fill="{ORANGE}"/>'
            f'<rect x="{x - 4}" y="{y - 14}" width="8" height="28" fill="{BG}" fill-opacity="0.25"/>')


def packet(x=0, y=0, color=BLUE):
    return (f'<rect x="{x - 22}" y="{y - 14}" width="44" height="28" rx="5" fill="{color}"/>'
            f'<path d="M{x - 22} {y - 12} l22 14 l22 -14" fill="none" stroke="{BG}" stroke-width="2"/>')


def house(x, y, label=None, stroke=MUTED):
    s = (f'<polygon points="{x - 40},{y - 6} {x},{y - 40} {x + 40},{y - 6}" fill="{stroke}"/>'
         f'<rect x="{x - 32}" y="{y - 6}" width="64" height="48" fill="{PANEL}" stroke="{stroke}" stroke-width="3"/>'
         f'<rect x="{x - 9}" y="{y + 14}" width="18" height="28" fill="{LINE}"/>')
    return s + (text(x, y + 66, label, 18, TXT, 700) if label else "")


def laptop(x, y, label=None, stroke=BLUE):
    s = (f'<rect x="{x - 34}" y="{y - 34}" width="68" height="44" rx="4" fill="{PANEL}" stroke="{stroke}" stroke-width="3"/>'
         f'<rect x="{x - 26}" y="{y - 27}" width="52" height="30" fill="{LINE}"/>'
         f'<polygon points="{x - 44},{y + 12} {x + 44},{y + 12} {x + 52},{y + 24} {x - 52},{y + 24}" fill="{stroke}"/>')
    return s + (text(x, y + 50, label, 18, TXT, 700) if label else "")


def printer(x, y, label=None):
    s = (f'<rect x="{x - 18}" y="{y - 36}" width="36" height="22" fill="{TXT}"/>'
         f'<rect x="{x - 36}" y="{y - 16}" width="72" height="36" rx="5" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
         f'<rect x="{x - 22}" y="{y + 20}" width="44" height="4" fill="{BLUE}"/>')
    return s + (text(x, y + 50, label, 18, TXT, 700) if label else "")


def pc(x, y, label=None):
    s = (f'<rect x="{x - 34}" y="{y - 36}" width="68" height="46" rx="4" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
         f'<rect x="{x - 26}" y="{y - 29}" width="52" height="32" fill="{LINE}"/>'
         f'<rect x="{x - 5}" y="{y + 10}" width="10" height="10" fill="{BLUE}"/>'
         f'<rect x="{x - 22}" y="{y + 20}" width="44" height="5" fill="{BLUE}"/>')
    return s + (text(x, y + 50, label, 18, TXT, 700) if label else "")


def switch(x, y, label="스위치"):
    s = (f'<rect x="{x - 52}" y="{y - 16}" width="104" height="32" rx="6" fill="{PANEL}" stroke="{GREEN}" stroke-width="3"/>'
         + "".join(f'<rect x="{x - 40 + i * 17}" y="{y - 5}" width="11" height="10" fill="{GREEN}" fill-opacity="0.7"/>' for i in range(5)))
    return s + text(x, y + 40, label, 17, MUTED)


def booth(x, y, label="경비실"):
    s = (f'<rect x="{x - 34}" y="{y - 22}" width="68" height="40" rx="4" fill="{PANEL}" stroke="{GREEN}" stroke-width="3"/>'
         f'<rect x="{x - 40}" y="{y - 30}" width="80" height="10" rx="3" fill="{GREEN}"/>'
         f'<rect x="{x - 22}" y="{y - 12}" width="44" height="18" fill="{LINE}"/>')
    return s + text(x, y + 40, label, 17, MUTED)


def router(x, y, label="라우터"):
    s = (f'<circle cx="{x}" cy="{y}" r="28" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
         f'<path d="M{x - 15} {y - 6} h28 l-7 -7 M{x + 15} {y + 6} h-28 l7 7" fill="none" stroke="{BLUE}" stroke-width="3"/>')
    return s + text(x, y + 50, label, 17, MUTED)


def warehouse(x, y, label="물류센터"):
    s = (f'<polygon points="{x - 40},{y - 10} {x},{y - 34} {x + 40},{y - 10}" fill="{BLUE}"/>'
         f'<rect x="{x - 36}" y="{y - 10}" width="72" height="38" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
         f'<rect x="{x - 20}" y="{y + 6}" width="40" height="22" fill="{LINE}"/>')
    return s + text(x, y + 50, label, 17, MUTED)


def frame(a, title, subtitle, captions, body):
    n = a.n
    assert tw(title, 32) <= 700 and tw(subtitle, 22) <= 880, f"title/subtitle too wide: {title}"
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540" '
           f'font-family="-apple-system,\'Apple SD Gothic Neo\',\'Segoe UI\',sans-serif">',
           f'<title>{escape(title)}</title>',
           f'<rect width="960" height="540" fill="{BG}"/>',
           text(480, 58, title, 32, TXT, 700),
           text(480, 98, subtitle, 22, MUTED),
           body,
           '<rect x="0" y="478" width="960" height="62" fill="#171a21"/>']
    for i, c in enumerate(captions, 1):
        assert tw(c, 24) <= 900, f"caption too wide: {c}"
        out.append(a.vis(text(480, 518, c, 24, TXT), i, i))
    badge = [f'<rect x="40" y="28" width="88" height="40" rx="20" fill="#171a21" stroke="#3d4b60" stroke-width="2"/>']
    for i in range(1, n + 1):
        t0, t1 = a.window(i, i)
        if i == 1:
            vals, keys, init = "1;1;0;0", f"0;{t1 - 0.01:.3f};{t1:.3f};1", 1
        elif i == n:
            vals, keys, init = "0;0;1;1", f"0;{t0 - 0.01:.3f};{t0:.3f};1", 0
        else:
            vals, keys, init = "0;0;1;1;0;0", f"0;{t0 - 0.01:.3f};{t0:.3f};{t1 - 0.01:.3f};{t1:.3f};1", 0
        badge.append(f'<text x="84" y="55" text-anchor="middle" font-size="20" font-weight="700" fill="#e6e8ec" opacity="{init}">'
                     f'{i} / {n}<animate attributeName="opacity" values="{vals}" keyTimes="{keys}" calcMode="discrete" '
                     f'dur="{a.dur:g}s" repeatCount="indefinite"/></text>')
    out.append('<g aria-label="재생 단계">' + "".join(badge) + "</g>")
    out.append("</svg>\n")
    return apply_opening("\n".join(out), loop_seconds=a.dur, title=title)


def phone(x, y, label=None, stroke=BLUE):
    s = (f'<rect x="{x - 22}" y="{y - 40}" width="44" height="76" rx="8" fill="{PANEL}" stroke="{stroke}" stroke-width="3"/>'
         f'<rect x="{x - 15}" y="{y - 30}" width="30" height="50" rx="2" fill="{LINE}"/>'
         f'<circle cx="{x}" cy="{y + 28}" r="3" fill="{stroke}"/>')
    return s + (text(x, y + 62, label, 18, TXT, 700) if label else "")


def eye(x, y):
    return (f'<ellipse cx="{x}" cy="{y}" rx="26" ry="15" fill="{BG}" stroke="{ORANGE}" stroke-width="3"/>'
            f'<circle cx="{x}" cy="{y}" r="7" fill="{ORANGE}"/>')


def lock(x, y, c=MUTED):
    return (f'<rect x="{x - 20}" y="{y - 4}" width="40" height="32" rx="5" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            f'<path d="M{x - 11} {y - 4} v-10 a11 11 0 0 1 22 0 v10" fill="none" stroke="{c}" stroke-width="3"/>')


def write(out_dir, name, svg):
    ET.fromstring(svg)  # fail fast on malformed XML
    Path(out_dir, f"{name}.svg").write_text(svg, encoding="utf-8")


def wire(lesson_md, rows):
    """Replace each Page's `animations:` block with a daily SVG on top and a network SVG after a paragraph.

    rows[i] = (daily_file, title, alt, caption, net_file, title, alt, caption, after_paragraph) for Page i+1.
    """
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines, out, page, i = fm.split("\n"), [], -1, 0
    assert sum(l.startswith("- terms:") for l in lines) == len(rows), "page count != rows"
    while i < len(lines):
        l = lines[i]
        if l.startswith("- terms:"):
            page += 1
            out.append(l); i += 1
            while i < len(lines) and lines[i].startswith("  - ") and not lines[i].startswith("  - id:"):
                out.append(lines[i]); i += 1
            df, dt, da, dc, nf, nt, na, nc, after = rows[page]
            out += ["  illustrations:"]
            for f, t, a, c, ap in ((df, dt, da, dc, -1), (nf, nt, na, nc, after)):
                out += [f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}", f"    alt: {q(a)}",
                        f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            continue
        if page >= 0 and l == "  animations:":
            i += 1
            while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                i += 1
            continue
        out.append(l); i += 1
    Path(lesson_md).write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")


def wire_items(lesson_md, pages):
    """Replace each Page's `animations:`/`illustrations:` blocks with the given items.

    pages[i] = [(file, title, alt, caption, after_paragraph), ...] for Page i+1, in display order.
    `file` is a name under assets/animations/ (no slash) or a path relative to lesson.md.
    """
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines, out, page, i = fm.split("\n"), [], -1, 0
    assert sum(l.startswith("- terms:") for l in lines) == len(pages), "page count != pages"
    while i < len(lines):
        l = lines[i]
        if l.startswith("- terms:"):
            page += 1
            out.append(l); i += 1
            while i < len(lines) and lines[i].startswith("  - ") and not lines[i].startswith("  - id:"):
                out.append(lines[i]); i += 1
            out.append("  illustrations:")
            for f, t, a, c, ap in pages[page]:
                path = f if "/" in f else f"assets/animations/{f}.svg"
                out += [f"  - file: {path}", f"    title: {q(t)}", f"    alt: {q(a)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            continue
        if page >= 0 and l in ("  animations:", "  illustrations:"):
            i += 1
            while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                i += 1
            continue
        out.append(l); i += 1
    Path(lesson_md).write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")
