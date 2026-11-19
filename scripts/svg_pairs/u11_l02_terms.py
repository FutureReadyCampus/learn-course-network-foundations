#!/usr/bin/env python3
"""Unit 11 Lesson 2 Page 5(처리량): 직원 부스(소프트웨어) vs 하이패스 차로(가속기) 4-step SVG.
Run from repo root: python3 scripts/svg_pairs/u11_l02_terms.py  (lesson.md is edited by hand)."""
from u11_new_common import *


def toll_hipass():
    a = new()
    car = lambda x, y, c=BLUE: box(x, y, 60, 34, c, PANEL, 8, sw=3)
    booth = (box(330, 150, 200, 110, BLUE, PANEL, 12, sw=3) + text(430, 190, "직원 부스", 18, TXT, 700)
             + text(430, 230, "차를 한 대씩 세워요", 17, TXT))
    lane = (box(330, 330, 200, 110, ORANGE, PANEL, 12, sw=3) + text(430, 370, "하이패스 차로", 18, TXT, 700)
            + text(430, 410, "세우지 않고 읽어요", 17, TXT))
    body = [line(110, 205, 320, 205, LINE, 4, "10 8"), line(110, 385, 320, 385, LINE, 4, "10 8"),
            car(120, 188), car(190, 188), car(250, 188), car(120, 368), car(190, 368), car(250, 368),
            a.vis(booth, 1, 4), mark(a, 330, 150, 200, 110, 1),
            a.vis(pill(700, 205, "느리지만 지시를 바꾸기 쉬워요", BLUE, 17, False, 330), 2, 2), mark(a, 535, 184, 330, 42, 2),
            a.vis(lane, 3, 4), mark(a, 330, 330, 200, 110, 3),
            a.vis(pill(700, 385, "빠르지만 바꾸려면 공사해요", ORANGE, 17, True, 330), 4, 4), mark(a, 535, 364, 330, 42, 4)]
    caps = ["소프트웨어 검사는 직원 부스예요", "직원 부스는 느리지만 바꾸기 쉬워요", "가속기는 하이패스 전용 차로예요", "빠르지만 바꾸려면 공사가 필요해요"]
    return frame(a, "직원 부스와 하이패스 차로", "같은 차를 보내는 두 가지 방법이에요", caps, "".join(body))


if __name__ == "__main__":
    out = lesson_dir(2) / "assets" / "animations"
    write(out, "u11-l02-p07-toll-hipass", toll_hipass())
    print("ok")
