#!/usr/bin/env python3
"""Unit 11 Lesson 3 Page 4: 「자물쇠 상자는 열쇠 없이 못 연다」 4-step SVG (택배 상자 비유).
Run from repo root: python3 scripts/svg_pairs/u11_l03_terms.py  (lesson.md is edited by hand)."""
from u11_new_common import *

Yc = 200


def tls_locked_box():
    a = new()
    box_ = parcel(480, Yc) + lock(480, Yc + 22, ORANGE)
    body = [dev("직원 PC", 110, Yc, None, laptop), server(850, Yc, "저장소 서비스"),
            line(165, Yc, 800, Yc, LINE, 4, "10 8"), box_,
            a.vis(pill(480, 140, "상자에 자물쇠를 달아 보내요", BLUE, 18, False, 330), 1, 1), mark(a, 315, 119, 330, 42, 1),
            a.vis(text(110, 290, "열쇠", 18, VIOLET, 700) + text(850, 300, "열쇠", 18, VIOLET, 700)
                  + pill(480, 300, "열쇠는 PC와 서비스만 있어요", VIOLET, 18, False, 340), 2, 2), mark(a, 310, 279, 340, 42, 2),
            a.vis(eye(480, 340) + lbl(480, 385, "센서(복사본만 받음)", TXT, 16, 700)
                  + line(480, 240, 480, 318, VIOLET, 3, "6 6")
                  + text(250, 346, "겉 송장은 읽혀요", 18, TXT, 700) + check(380, 340)
                  + text(710, 346, "안의 내용은 못 읽어요", 18, TXT, 700) + cross(850, 340), 3, 3), mark(a, 160, 318, 760, 44, 3),
            a.vis(pill(480, 420, "열쇠가 없어서 파일 내용은 못 봐요", GREEN, 18, True, 400), 4, 4), mark(a, 280, 399, 400, 42, 4)]
    caps = ["PC가 상자에 자물쇠를 달아 보내요", "열쇠는 PC와 서비스만 가지고 있어요", "센서는 복사본의 겉 송장만 읽어요", "열쇠가 없으니 안은 볼 수 없어요"]
    return frame(a, "자물쇠 상자는 열쇠 없이 못 열어요", "택배 상자에 자물쇠를 달아 보내는 일이 암호화예요", caps, "".join(body))


if __name__ == "__main__":
    out = lesson_dir(3) / "assets" / "animations"
    write(out, "u11-l03-p04c-lock-box", tls_locked_box())
    print("ok")
