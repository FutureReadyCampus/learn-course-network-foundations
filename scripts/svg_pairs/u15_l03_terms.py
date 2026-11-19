#!/usr/bin/env python3
"""Unit 15 Lesson 3 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u15_l03_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 3: TLS 종료 위치 = 우편물 접수실. 봉투(암호문) 앞 검사원은 겉면만, 뜯은 뒤 검사원은 편지 내용까지 본다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

OUT = lesson_dir(3) / "assets" / "animations"
Y = 330


def envelope(x, y, c=BLUE):
    return (box(x - 34, y - 24, 68, 48, c, PANEL, 5, sw=3) + f'<path d="M{x - 34} {y - 24} L{x} {y + 4} L{x + 34} {y - 24}" fill="none" stroke="{c}" stroke-width="3"/>')


def p3_room():
    a = new()
    base = (text(110, Y + 70, "바깥에서 온 편지", 16, TXT, 700) + road(150, 400, Y) + node(470, Y, "접수실", BLUE, 110, 64, 18)
            + road(525, 800, Y) + node(850, Y, "받는 사람", GREEN, 120, 56, 16)
            + node(300, 170, "복도 검사원", MUTED, 140, 52, 16) + node(650, 170, "안쪽 검사원", MUTED, 140, 52, 16))
    body = [base,
            st(a, 1, "", None, 1),
            a.vis(mvi(a, 1, envelope(0, 0), [(110, Y - 60), (260, Y - 60), (380, Y - 60)], 0.05, 0.95), 1, 1),
            st(a, 1, text(250, 450, "봉인된 봉투(TLS 암호문)", 16, BLUE, 700), (95, 430, 310, 28), 4),
            st(a, 2, eye(300, 232) + line(300, 196, 300, 250, ORANGE, 2), bb(300, 170, 150, 60), 2),
            P(a, 2, 300, 275, "겉면만 보여요", RED, 16, False, 2, False),
            st(a, 3, doc(470, Y - 110, BLUE) + line(470, Y - 70, 470, Y - 38, BLUE, 2, "6 5"), bb(470, Y, 120, 74), 3),
            P(a, 3, 470, 430, "봉투를 뜯어요(TLS 종료)", ORANGE, 16, False, 3, False),
            st(a, 4, eye(650, 232) + line(650, 196, 650, 250, ORANGE, 2) + doc(650, Y - 35, BLUE) + check(700, 232), bb(650, 170, 150, 60), 4),
            P(a, 4, 650, 430, "편지 속 문구까지 읽어요", GREEN, 16, False, 4, False)]
    caps = ["바깥 편지는 봉인된 봉투로 와요", "복도 검사원은 봉투 겉만 봐요", "접수실이 봉투를 뜯어 편지를 꺼내요", "안쪽 검사원은 편지 내용을 읽어요"]
    return frame(a, "봉투는 어디서 뜯길까", "센서가 내용을 보려면 봉투가 뜯긴 뒤여야 해요", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "u15-l03-p03-tls-mailroom", p3_room())
    print("ok")
