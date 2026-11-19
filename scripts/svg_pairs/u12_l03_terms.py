#!/usr/bin/env python3
"""Unit 12 Lesson 3 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u12_l03_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 6: 서버가 기다리는 주소 = 방의 두 문(안쪽 127.0.0.1 / 복도 192.168.10.50)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"


def p6_door():
    p = Pg("서버가 기다리는 주소는 어느 문일까?", "서버 방에는 안쪽 문과 복도 쪽 문이 있어요",
           ["그룹웨어 서버 방에는 문이 둘 있어요", "방이 안쪽 문에서만 받도록 설정돼 있어요",
            "복도에서 온 손님은 들어오지 못해요", "복도 쪽 문까지 열면 들어와요"])
    p.base(rt(120, 300, "공유기"), line(170, 300, 330, 300, LINE, 4, "8 6"),
           box(330, 140, 560, 300, MUTED, PANEL, 16, dash=True, sw=3), dsrv(790, 290, "서버 프로그램"))
    DA, DB = (360, 340, 250, 56), (360, 170, 250, 56)  # 안쪽 문 / 복도 쪽 문
    p.base(cell(*DB, "복도 쪽 문 192.168.10.50", MUTED, 16), cell(*DA, "안쪽 문 127.0.0.1", MUTED, 16))
    p.at(cell(*DA, "안쪽 문 127.0.0.1", GREEN, 16) + line(610, 368, 756, 310, GREEN, 4), 2, 4, mark=DA)
    p.fly(packet(0, 0), [(180, 300), (340, 255)], 3)
    p.at(cross(335, 255) + pill(480, 275, "복도 쪽 문이 닫혀 있어요", RED, 16, False, 250), 3, 3)
    p.at(cell(*DB, "복도 쪽 문 192.168.10.50", GREEN, 16) + line(610, 198, 756, 270, GREEN, 4) + check(335, 255), 4, 4, mark=DB)
    return p.render()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    done(OUT, "u12-l03-p06-door-listen", p6_door)
    print("ok")
