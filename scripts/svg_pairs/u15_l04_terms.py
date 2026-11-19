#!/usr/bin/env python3
"""Unit 15 Lesson 4 용어 보강 SVG. Run from repo root: python3 scripts/svg_pairs/u15_l04_terms.py
lesson.md는 건드리지 않는다. Page 1: 세 기록장을 총괄 경비 담당(SIEM)이 시간순으로 잇는 상관 분석."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

OUT = lesson_dir(4) / "assets" / "animations"


def p1_ledgers():
    a = new()
    ys = [165, 290, 415]
    names = [("NAC 명부 02:41", BLUE), ("방화벽 일지 02:45", BLUE), ("IPS 일지 02:49", BLUE)]
    base = "".join(doc(110, y, c, n) for y, (n, c) in zip(ys, names))
    desk = node(490, 290, "SIEM", GREEN, 130, 64)
    joins = "".join(line(150, y, 425, 290, GREEN, 3, "8 6") for y in ys)
    card = box(690, 225, 240, 130, GREEN, PANEL, 12, sw=3) + text(810, 280, "한 사건", 22, GREEN, 700) + text(810, 316, "02:41~02:49, 8분", 17, TXT, 700)
    body = [base,
            st(a, 2, desk + joins, (425, 258, 130, 64)),
            P(a, 3, 810, 190, "같은 주소를 시간순으로", GREEN, 17, False, 3, False),
            st(a, 3, card, (690, 225, 240, 130)),
            P(a, 4, 560, 440, "방화벽 시계 10분 빠름: 02:55", RED, 18, True, 4),
            a.vis(cross(905, 245), 4, 4)]
    caps = ["기록장 세 권이 따로 있어요", "총괄 담당 SIEM이 한 책상에 모아요", "같은 주소의 줄을 시간순으로 이어 한 사건으로 읽어요", "시계가 어긋나면 순서가 뒤집혀 사건이 틀어져요"]
    return frame(a, "세 기록장을 한 책상에서 이으면", "상관 분석은 시간순으로 이어 붙이는 일이라 시계가 맞아야 해요", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "u15-l04-p01-ledgers-siem", p1_ledgers())
    print("ok")
