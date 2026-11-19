#!/usr/bin/env python3
"""Unit 11 Lesson 6 Page 4: 「인증서는 신분증이다」 4-step SVG (회사 출입 경비 비유).
Run from repo root: python3 scripts/svg_pairs/u11_l06_cert.py  (lesson.md is edited by hand)."""
from u11_new_common import *

Yc = 250


def cert_id_card():
    a = new()
    card = (box(335, 150, 290, 190, VIOLET, PANEL, 12, sw=3)
            + text(480, 195, "서비스 주소: files.example", 17, TXT, 700)
            + text(480, 245, "그 서비스의 공개 키", 17, TXT, 700)
            + f'<circle cx="400" cy="300" r="20" fill="none" stroke="{VIOLET}" stroke-width="3"/>'
            + text(535, 306, "발급 기관 도장", 17, VIOLET, 700))
    body = [dev("내 PC의 앱", 110, Yc, None, laptop), server(850, Yc, "저장소 서비스"),
            line(165, Yc, 800, Yc, LINE, 4, "10 8"),
            a.vis(pill(330, 190, "당신이 누구죠?", BLUE, 18, False, 210), 1, 1), mark(a, 225, 169, 210, 42, 1),
            a.vis(card, 2, 2), mark(a, 335, 150, 290, 190, 2),
            a.vis(box(250, 150, 460, 190, GREEN, PANEL, 12, sw=3)
                  + text(480, 195, "경비실 명단(신뢰 목록)과 맞춰 봐요", 18, TXT, 700)
                  + text(500, 250, "도장 찍은 기관이 명단에 있다", 18, TXT) + check(285, 244)
                  + text(500, 305, "이름이 찾아간 주소와 같다", 18, TXT) + check(285, 299), 3, 3), mark(a, 250, 150, 460, 190, 3),
            a.vis(lock(480, 190, GREEN) + pill(480, 360, "통과하면 암호 대화를 시작해요", GREEN, 18, True, 400), 4, 4), mark(a, 280, 339, 400, 42, 4)]
    caps = ["앱이 서버에게 \"당신이 누구죠?\" 하고 물어요", "서버가 신분증(인증서)을 내밀어요", "앱이 명단에서 도장과 이름을 확인해요", "통과하면 그때부터 암호로 말해요"]
    return frame(a, "인증서는 신분증이에요", "회사 출입 경비가 신분증을 확인하듯이 해요", caps, "".join(body))


if __name__ == "__main__":
    out = lesson_dir(6) / "assets" / "animations"
    write(out, "u11-l06-p04-cert-id-card", cert_id_card())
    print("ok")
