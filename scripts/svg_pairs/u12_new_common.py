"""Shared helpers for the new Unit 12 example SVGs (u12_new_l01..l05). Imports old generators, never edits them."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur, person  # noqa: F401
from u7_l01 import mv as _mv
from u12_l01_router import net, rt, cloud  # noqa: F401
from u12_l02_nat_table import table, ledger  # noqa: F401
from u12_l05_upnp import usb  # noqa: F401

ROOT = Path(__file__).resolve().parents[2]
Y = 300
AI, AI_PORT, WAN = "192.168.10.50", "8080", "198.51.100.25"


def lesson_dir(n):
    return next((ROOT / "units").glob(f"08-router-and-nat/lessons/restructured/{n:02d}-*"))


class Pg:
    """One 4-step page. at(inner, t0, t1, mark) shows `inner` over steps t0..t1; mark draws an orange frame at step t0 only."""

    def __init__(self, title, sub, caps):
        self.a, self.title, self.sub, self.caps, self.parts = Anim(4, dur(False)), title, sub, caps, []

    def base(self, *x):
        self.parts += x

    def at(self, inner, t0, t1=4, mark=None):
        self.parts.append(self.a.vis(inner, t0, t1))
        if mark:
            self.parts.append(self.a.vis(hl(*mark), t0, t0))

    def mark(self, rect, t):
        self.parts.append(self.a.vis(hl(*rect), t, t))

    def fly(self, inner, pts, step, f0=0.1, f1=0.9):
        self.parts.append(_mv(self.a, inner, pts, step, step, step, f0, f1))

    def render(self):
        return frame(self.a, self.title, self.sub, self.caps, "".join(self.parts))


def dsrv(x, y, label="AI 서버", c=GREEN):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, label, 18, TXT, 700))


def card(x, y, src, dst, c=BLUE, w=300):
    """Packet header card: two lines (출발/도착). Use cl() for the frame around one line."""
    return (box(x, y, w, 76, c, PANEL, 8, sw=3) + text(x + 14, y + 30, "출발 " + src, 15, TXT, anchor="start")
            + text(x + 14, y + 60, "도착 " + dst, 15, TXT, anchor="start"))


def cl(x, y, i, w=300):
    return (x + 6, y + 10 + i * 30, w - 12, 26)


def lbl(x, y, s, c=MUTED, fs=17):
    return text(x, y, s, fs, c, 700)


def done(out, name, fn):
    write(out, name, fn())


def wire_pages(lesson_md, items):
    """items[i] = (file, title, alt, caption) for Page i+1 (after_paragraph 0). Replaces each Page's illustrations."""
    pages = [[(f, t, al, c, 0)] for f, t, al, c in items]
    wire_items(lesson_md, pages)
