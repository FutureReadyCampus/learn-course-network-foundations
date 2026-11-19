#!/usr/bin/env python3
"""Unit 15 Lesson 2 Page 5: 「봉인된 봉투로 보는 SNI·TLS 검사」 4-step SVG (우체부 비유).
Run from repo root: python3 scripts/svg_pairs/u15_l02_terms.py  (lesson.md is edited by hand)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

OUT = lesson_dir(2) / "assets" / "animations"


def envelope():
    a = new()
    env = box(330, 190, 300, 170, MUTED, PANEL, 10, sw=3) + line(330, 190, 480, 280, LINE, 2) + line(630, 190, 480, 280, LINE, 2)
    front = box(375, 300, 210, 44, BLUE, BG, 8, sw=2) + text(480, 329, "받는 곳: 저장소 도메인", 17, TXT, 700)
    seal = lock(480, 255, MUTED)
    eyes = eye(150, 270) + text(150, 335, "Proxy형", 17, BLUE, 700)
    body = [env, front, seal, eyes,
            st(a, 1, "", (375, 300, 210, 44)),
            P(a, 2, 150, 215, "겉면은 읽혀요", GREEN, 17, False, 2), a.vis(line(210, 270, 370, 318, GREEN, 3, "6 5"), 2, 2),
            P(a, 3, 790, 255, "내용은 못 읽어요", RED, 17, False, 3), st(a, 3, "", bb(480, 262, 80, 80)),
            st(a, 4, box(690, 260, 220, 60, ORANGE, PANEL, 10, sw=3) + text(800, 285, "회사 CA 도장", 17, ORANGE, 700) + text(800, 308, "등록해야 다시 봉인해요", 16, TXT, 700), (690, 260, 220, 60))]
    caps = ["봉투 겉면에는 받는 곳 이름이 적혀 있어요", "겉면의 이름은 봉투를 뜯지 않아도 읽혀요", "봉인된 편지 내용은 읽을 수 없어요", "내용을 보려면 회사 CA 도장을 등록하고 뜯어요"]
    return frame(a, "봉인된 봉투로 보는 HTTPS", "겉면은 읽히고 내용은 봉인돼 있어요", caps, "".join(body))


if __name__ == "__main__":
    write(OUT, "u15-l02-p05-sealed-envelope", envelope())
    print("ok")
