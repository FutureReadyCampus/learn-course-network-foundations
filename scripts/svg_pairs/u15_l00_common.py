"""Unit 15 shared helpers (예시 SVG 4단계: ① 상황 → ② 동작 → ③ 결과 → ④ 기억할 점).
주황 테두리는 그 단계에서 새로 바뀐 요소에만 붙인다. 방어 장면만 그린다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from kit import Anim, box, check, cross, eye, frame, laptop, line, lock, packet, phone, pill, switch, text, tw, wire_items, write  # noqa: F401
from u6_l03 import cell, dur, hl, person
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
U15 = ROOT / "units" / "15-network-security-solutions" / "lessons" / "restructured"


def lesson_dir(n):
    return next(U15.glob(f"{n:02d}-*"))


def new():
    return Anim(4, dur(False))


def bb(x, y, w=96, h=96):
    return (x - w / 2, y - h / 2, w, h)


def st(a, t, inner, hi=None, end=4):
    """단계 t부터 end까지 보이는 요소. hi=(x,y,w,h)면 단계 t에서만 주황 테두리."""
    s = a.vis(inner, t, end)
    return s + a.vis(hl(*hi), t, t) if hi else s


def P(a, t, x, y, s, c=GREEN, fs=16, filled=False, end=4, hi=True):
    w = round(tw(s, fs) + 28)
    h = fs + 16
    return st(a, t, pill(x, y, s, c, fs, filled, w), (x - w / 2, y - h / 2, w, h) if hi else None, end)


def pk(a, t, pts, color=BLUE, f0=0.1, f1=0.9):
    """단계 t 안에서만 움직이는 패킷."""
    return mv(a, packet(0, 0, color), pts, t, t, t, f0, f1)


def mvi(a, t, inner, pts, f0=0.1, f1=0.9):
    return mv(a, inner, pts, t, t, t, f0, f1)


def server(x, y, label="AI 서버", c=GREEN, sub=None):
    s = (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
         + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
         + text(x, y + 62, label, 16, TXT, 700))
    return s + (text(x, y + 80, sub, 14, MUTED) if sub else "")


def wall(x, y, label=None, c=ORANGE):
    s = (box(x - 42, y - 34, 84, 68, c, PANEL, 6, sw=3) + line(x - 42, y - 11, x + 42, y - 11, c, 2)
         + line(x - 42, y + 12, x + 42, y + 12, c, 2) + line(x - 14, y - 34, x - 14, y - 11, c, 2)
         + line(x + 14, y - 11, x + 14, y + 12, c, 2) + line(x - 14, y + 12, x - 14, y + 34, c, 2))
    return s + (text(x, y + 56, label, 16, TXT, 700) if label else "")


def node(x, y, label, c=BLUE, w=96, h=56, fs=17, sub=None):
    s = box(x - w / 2, y - h / 2, w, h, c, PANEL, 8, sw=3) + text(x, y + fs * 0.36, label, fs, c, 700)
    return s + (text(x, y + h / 2 + 20, sub, 14, MUTED) if sub else "")


def cloudi(x, y, label="인터넷", c=BLUE):
    return (f'<ellipse cx="{x}" cy="{y}" rx="68" ry="40" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + text(x, y + 7, label, 18, c, 700))


def doc(x, y, c=BLUE, label=None):
    s = (f'<rect x="{x - 26}" y="{y - 34}" width="52" height="68" rx="5" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
         + "".join(line(x - 14, y - 16 + i * 14, x + 14, y - 16 + i * 14, c, 3) for i in range(3)))
    return s + (text(x, y + 56, label, 16, TXT, 700) if label else "")


def pkt(x, y, bad=False):
    """헤더+내용 패킷. bad=True면 내용에 공격이 들어 있다."""
    pc = RED if bad else GREEN
    return (f'<rect x="{x - 50}" y="{y - 22}" width="38" height="44" rx="4" fill="{BLUE}"/>'
            f'<rect x="{x - 12}" y="{y - 22}" width="62" height="44" rx="4" fill="{pc}"/>'
            + text(x - 31, y + 5, "헤더", 13, BG, 700) + text(x + 19, y + 5, "내용", 13, BG, 700))


def zone(x, y, w, h, label, c, fs=16):
    return box(x, y, w, h, c, PANEL, 14, dash=True, sw=3) + text(x + w / 2, y + 28, label, fs, c, 700)


def road(x1, x2, y, c=LINE):
    return line(x1, y, x2, y, c, 4, "8 6")


def rtable(x, y, heads, rows, widths, colors, fs=14):
    hx = [x + sum(widths[:i]) for i in range(len(widths))]
    head = "".join(cell(hx[i], y, widths[i] - 6, 32, h, MUTED, 14, BG) for i, h in enumerate(heads))
    out = [("".join(cell(hx[i], y + 40 + r * 46, widths[i] - 6, 40, v, colors[r], fs) for i, v in enumerate(row)),
            (x, y + 40 + r * 46, sum(widths) - 6, 40)) for r, row in enumerate(rows)]
    return head, out


def build(out_dir, items):
    out_dir.mkdir(parents=True, exist_ok=True)
    for f, _t, _al, _c, _ap, fn in items:
        write(out_dir, f, fn())


def wire(lesson_md, items):
    wire_items(lesson_md, [[(f, t, al, c, ap)] for f, t, al, c, ap, _ in items])
