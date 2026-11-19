#!/usr/bin/env python3
"""Unit 13 Lesson 1 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u13_l01_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 6: HTTPS 요청 = 봉인한 택배 상자. L4는 겉봉만, L7은 열쇠로 열어 읽는다."""
from u13_l01_lb import *  # noqa: F401,F403


def p6_sealed():
    a = new()
    cx, cy = 330, 290
    sealed = (box(cx - 110, cy - 65, 220, 130, MUTED, PANEL, 10, sw=3) + lock(cx, cy - 20, MUTED)
              + text(cx, cy + 50, "봉인된 상자 (HTTPS)", 16, MUTED, 700))
    opened = (box(cx - 110, cy - 65, 220, 130, BLUE, PANEL, 10, sw=3)
              + text(cx, cy - 20, "경로 /api/estimate", 17, TXT, 700) + text(cx, cy + 15, "쿠키 (손님 번호표)", 17, TXT, 700))
    body = [laptop(110, 290, "손님"),
            a.vis(sealed, 1, 2), a.vis(opened, 3, 4),
            line(165, 290, 215, 290, LINE, 3),
            a.vis(pill(cx, 190, "겉봉 203.0.113.10:443", BLUE, 16, False, 250), 1, 2), mk(a, cx - 125, 172, 250, 36, 2),
            a.vis(pill(cx, 400, "L4는 겉봉만 읽어요", MUTED, 18, True, 240), 2, 2),
            a.vis(pill(cx, 400, "L7이 열쇠로 열어 읽어요", BLUE, 18, True, 280), 3, 3), mk(a, cx - 125, cy - 80, 250, 160, 3),
            sv(800, 200, "작은 서버", GREEN, 130, 46), sv(800, 380, "큰 서버", VIOLET, 130, 46),
            a.vis(line(450, 290, 735, 380, GREEN, 4) + check(770, 340)
                  + pill(620, 440, "열린 내용은 이 장비 안에서 평문", ORANGE, 16, False, 330), 4, 4),
            mk(a, 735, 357, 130, 46, 4)]
    caps = ["HTTPS 요청은 봉인한 택배 상자예요", "L4는 겉봉의 주소와 포트만 봐요", "L7은 열쇠로 상자를 열어 경로를 읽어요", "읽은 뒤 알맞은 서버로 보내요"]
    return frame(a, "봉인된 상자는 누가 열까?", "겉봉만 보는 L4, 열어서 읽는 L7", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "u13-l01-p06-sealed-box", p6_sealed())
    print("ok")
