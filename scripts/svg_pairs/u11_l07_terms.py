#!/usr/bin/env python3
"""Unit 11 Lesson 7 Page 3: 앞단 안내 데스크가 신분증을 내밀고 봉투를 뜯는다 (4-step SVG).
Run from repo root: python3 scripts/svg_pairs/u11_l07_terms.py  (lesson.md is edited by hand)."""
from u11_new_common import *

Yc = 270


def front_desk():
    a = new()
    card = (box(330, 120, 300, 120, VIOLET, PANEL, 12, sw=3)
            + text(480, 160, "서비스 주소: gw.company.example", 16, TXT, 700)
            + f'<circle cx="400" cy="205" r="16" fill="none" stroke="{VIOLET}" stroke-width="3"/>'
            + text(540, 211, "발급 기관 도장", 16, VIOLET, 700))
    body = [dev("외근 직원 PC", 110, Yc, None, laptop), node(480, Yc + 20, "앞단(안내 데스크)", None, 210, 70),
            server(850, Yc, "그룹웨어 서버"),
            line(165, Yc, 375, Yc + 20, LINE, 4, "10 8"), line(585, Yc + 20, 800, Yc, LINE, 4, "10 8"),
            a.vis(pill(480, 400, "안내 데스크에 닿았어요", BLUE, 18, False, 300), 1, 1), mark(a, 330, 385, 300, 42, 1),
            a.vis(card, 2, 2), mark(a, 330, 120, 300, 120, 2),
            a.vis(box(300, 120, 360, 110, GREEN, PANEL, 12, sw=3)
                  + text(500, 165, "도장 기관이 명단에 있다", 17, TXT) + check(335, 159)
                  + text(500, 205, "이름이 주소와 같다", 17, TXT) + check(335, 199), 3, 3), mark(a, 300, 120, 360, 110, 3),
            a.vis(pill(660, 410, "봉투를 뜯어 읽을 수 있는 글로 전해요", ORANGE, 16, False, 340), 4, 4), mark(a, 490, 389, 340, 42, 4)]
    caps = ["직원이 안내 데스크(앞단)에 닿아요", "앞단이 서비스 신분증(인증서)을 내밀어요", "직원이 도장과 이름을 확인해요", "앞단이 봉투를 뜯어 서버로 전해요"]
    return frame(a, "TLS는 안내 데스크에서 끝나요", "신분증 확인은 앞단이, 일 처리는 서버가 해요", caps, "".join(body))


if __name__ == "__main__":
    out = lesson_dir(7) / "assets" / "animations"
    write(out, "u11-l07-p03-front-desk", front_desk())
    print("ok")
