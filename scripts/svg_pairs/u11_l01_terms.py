#!/usr/bin/env python3
"""Unit 11 Lesson 1 Page 4: 봉인된 봉투와 신분증(HTTPS·인증서·CA) 4-step SVG (심부름꾼 비유 이어 쓰기).
Run from repo root: python3 scripts/svg_pairs/u11_l01_terms.py  (lesson.md is edited by hand)."""
from u11_new_common import *

Yc = 250


def sealed_envelope():
    a = new()
    body = [dev("박 팀장 PC", 110, Yc, None, laptop), node(480, Yc, "프록시", "심부름꾼", 150, 80, BLUE), server(850, Yc, "저장소 서비스"),
            line(165, Yc, 405, Yc, LINE, 4, "10 8"), line(555, Yc, 800, Yc, LINE, 4, "10 8"),
            a.vis(box(250, 130, 130, 60, MUTED, PANEL, 10, sw=3) + text(315, 168, "봉인 봉투", 17, TXT, 700), 1, 1), mark(a, 250, 130, 130, 60, 1),
            a.vis(box(610, 118, 230, 84, VIOLET, PANEL, 12, sw=3) + text(725, 150, "신분증(인증서)", 17, VIOLET, 700)
                  + text(725, 183, "도장: 발급 기관", 16, TXT), 2, 2), mark(a, 610, 118, 230, 84, 2),
            a.vis(box(330, 330, 300, 80, GREEN, PANEL, 12, sw=3) + text(480, 362, "경비 명단에 회사 도장 추가", 17, TXT, 700)
                  + text(480, 392, "(회사 CA 설치)", 16, MUTED), 3, 3), mark(a, 330, 330, 300, 80, 3),
            a.vis(box(405, 130, 150, 60, ORANGE, PANEL, 10, sw=3) + text(480, 168, "뜯어 보고 재봉인", 16, TXT, 700), 4, 4), mark(a, 405, 130, 150, 60, 4)]
    caps = ["HTTPS 요청은 봉인된 봉투(암호문)로 가요", "상대 회사는 도장 찍힌 신분증(인증서)을 내밀어요", "회사 경비 명단에 회사 도장을 올려 둬요(CA 설치)", "프록시가 뜯어 보고 다시 봉인해요(TLS 검사)"]
    return frame(a, "봉인된 봉투를 프록시가 읽으려면", "신분증과 명단 설정이 있어야 해요", caps, "".join(body))


if __name__ == "__main__":
    out = lesson_dir(1) / "assets" / "animations"
    write(out, "u11-l01-p04-sealed-envelope", sealed_envelope())
    print("ok")
