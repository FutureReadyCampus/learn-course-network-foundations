#!/usr/bin/env python3
"""Unit 14 Lesson 3 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u14_l03_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 2: IKE = 협상 회의, SA = 합의서. Page 3: 인증서 = 신분증(Unit 11 Lesson 6 출입 경비 비유와 같음)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403
from u12_new_common import Pg, done

OUT = next((ROOT / "units").glob("10-vpn-and-security/lessons/restructured/03-*")) / "assets" / "animations"
Yc = 300


def p2_meeting():
    p = Pg("IKE는 협상 회의, SA는 합의서", "처음 만난 두 회사가 계약서를 쓰는 것과 같아요",
           ["두 SG가 협상 회의를 열어요", "서로 제안을 주고받아요", "합의 결과를 합의서(SA)로 한 부씩 가져요", "기간이 끝나면 새 회의로 새 열쇠를 정해요"])
    p.base(booth(150, Yc, "도쿄 SG"), booth(810, Yc, "서울 SG"), line(200, Yc, 760, Yc, LINE, 4, "8 6"))
    p.at(pill(480, 200, "협상 회의 = IKE", BLUE, 18, False, 240), 1, 1, mark=(360, 180, 240, 40))
    p.at(pill(480, 200, "UDP 500으로 제안", VIOLET, 18, False, 240), 2, 2, mark=(360, 180, 240, 40))
    p.fly(packet(0, 0, VIOLET), [(230, 280), (730, 280)], 2)
    p.fly(packet(0, 0, BLUE), [(730, 320), (230, 320)], 2)
    A, B = (40, 400, 220, 56), (700, 400, 220, 56)
    p.at(pill(480, 200, "합의서 = SA", GREEN, 18, False, 240) + cell(*A, "합의서 한 부", GREEN, 17) + cell(*B, "합의서 한 부", GREEN, 17)
         + check(480, Yc), 3, 3, mark=(360, 180, 240, 40))
    p.at(pill(480, 200, "기간 끝 = 새 회의", BLUE, 18, False, 240) + cell(*A, "새 열쇠로 다시", GREEN, 17) + cell(*B, "새 열쇠로 다시", GREEN, 17), 4, 4,
         mark=(360, 180, 240, 40))
    return p.render()


def p3_id_card():
    p = Pg("인증서는 장비의 신분증", "경비실 명단과 맞춰 보는 방식이에요",
           ["서울 SG가 \"누구세요?\" 하고 물어요", "도쿄 SG가 신분증(인증서)을 내밀어요", "서울 SG가 명단과 이름을 맞춰 봐요", "통과하면 협상을 이어 가요"])
    p.base(booth(110, Yc, "도쿄 SG"), booth(850, Yc, "서울 SG"), line(160, Yc, 800, Yc, LINE, 4, "10 8"))
    p.at(pill(480, 190, "당신이 누구죠?", BLUE, 18, False, 210), 1, 1, mark=(375, 169, 210, 42))
    card_ = (box(335, 150, 290, 190, VIOLET, PANEL, 12, sw=3) + text(480, 195, "이름: 도쿄 지사 SG", 17, TXT, 700)
             + text(480, 245, "그 장비의 공개 키", 17, TXT, 700)
             + f'<circle cx="400" cy="300" r="20" fill="none" stroke="{VIOLET}" stroke-width="3"/>'
             + text(535, 306, "발급 기관 도장", 17, VIOLET, 700))
    p.at(card_, 2, 2, mark=(335, 150, 290, 190))
    p.at(box(250, 150, 460, 190, GREEN, PANEL, 12, sw=3) + text(480, 195, "경비실 명단(신뢰 목록)과 맞춰요", 18, TXT, 700)
         + text(500, 250, "도장 기관이 명단에 있다", 18, TXT) + check(285, 244)
         + text(500, 305, "이름이 상대가 말한 이름과 같다", 18, TXT) + check(285, 299), 3, 3, mark=(250, 150, 460, 190))
    p.at(lock(480, 190, GREEN) + pill(480, 360, "통과하면 협상을 이어 가요", GREEN, 18, True, 400), 4, 4, mark=(280, 339, 400, 42))
    return p.render()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    done(OUT, "u14-l03-p02-meeting-sa", p2_meeting)
    done(OUT, "u14-l03-p03-cert-id-card", p3_id_card)
    print("ok")
