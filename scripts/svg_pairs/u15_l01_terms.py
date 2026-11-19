#!/usr/bin/env python3
"""Unit 15 Lesson 1 용어 보강 SVG. Run from repo root: python3 scripts/svg_pairs/u15_l01_terms.py
lesson.md는 건드리지 않는다. Page 4: 서버인 척 끼어든 응답은 진짜 신분증(인증서)이 없다 (U11 L6 출입 경비 비유)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

OUT = lesson_dir(1) / "assets" / "animations"


def p4_cert():
    a, Y = new(), 380
    base = (laptop(110, Y, "박 팀장 브라우저") + line(170, Y, 765, Y, LINE, 4, "8 6") + server(830, Y, "https 사내 위키")
            + eye(230, 200) + text(230, 238, "Probe", 16, MUTED))
    card = box(340, 150, 290, 110, VIOLET, PANEL, 12, sw=3) + text(485, 195, "직접 만든 신분증", 18, TXT, 700) + text(485, 232, "도장: 처음 보는 기관", 17, VIOLET, 700)
    body = [base,
            pk(a, 1, [(150, Y), (700, Y)], BLUE), P(a, 1, 480, 320, "https로 사내 위키 열기", BLUE, 16, False, 1, False),
            st(a, 2, card, (340, 150, 290, 110), 3), P(a, 2, 480, 300, "서버인 척 응답해요", ORANGE, 16, False, 2, False),
            P(a, 3, 480, 310, "경비실 명단에 없는 도장", RED, 17, False, 3), st(a, 3, cross(655, 205), bb(655, 205, 50, 50), 3),
            P(a, 4, 480, 430, "인증서 경고 또는 연결 실패", RED, 18, True, 4, False)]
    caps = ["브라우저가 https로 사내 위키를 열어요", "끼어든 응답이 직접 만든 신분증을 내밀어요", "브라우저가 명단에서 도장을 못 찾아요", "경고가 뜨거나 연결이 끊겨요"]
    return frame(a, "서버인 척하면 신분증에서 걸려요", "https는 진짜 서버의 인증서(신분증)를 확인해요", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "u15-l01-p04-cert-fake-server", p4_cert())
    print("ok")
