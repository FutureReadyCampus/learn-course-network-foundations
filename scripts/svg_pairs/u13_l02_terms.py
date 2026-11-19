#!/usr/bin/env python3
"""Unit 13 Lesson 2 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u13_l02_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 3: 이웃 장비의 주소록(ARP)이 옛 장비를 가리키면 일을 넘겨받아도 요청이 빈 장비로 간다 (회사 내선 번호부 비유)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u13_l01_lb import *  # noqa: F401,F403
from u13_l01_lb import lesson_dir

OUT = lesson_dir(2) / "assets" / "animations"


def p3_phonebook():
    a = new()
    book = lambda who, c: (box(40, 215, 300, 150, c, PANEL, 12, sw=3) + text(190, 248, "이웃 장비의 주소록", 17, MUTED, 700)
                           + text(190, 295, "203.0.113.10", 18, TXT, 700) + text(190, 335, "→ " + who, 18, c, 700))
    body = [text(190, 190, "이웃 장비", 17, TXT, 700) + book("장비 A", MUTED),
            lbx(740, 190, "장비 A", None, GREEN, 150, 60) + lbx(740, 360, "장비 B", None, MUTED, 150, 60, dash=True),
            line(340, 270, 665, 190, LINE, 3) + line(340, 310, 665, 360, LINE, 3, "6 6"),
            a.vis(book("장비 A", GREEN) + fl(a, [(360, 262), (640, 200)], 1, BLUE) + check(520, 200), 1, 1),
            a.vis(lbx(740, 190, "장비 A", None, RED, 150, 60, dash=True) + cross(850, 190) + text(740, 244, "멈춤", 17, RED, 700), 2, 4),
            mk(a, 660, 158, 160, 64, 2),
            a.vis(lbx(740, 360, "장비 B", None, GREEN, 150, 60) + pill(740, 420, "VIP를 넘겨받음", GREEN, 16, False, 180), 3, 4),
            mk(a, 660, 328, 160, 64, 3),
            fl(a, [(360, 262), (640, 200)], 3, RED), a.vis(cross(520, 215) + text(520, 168, "빈 장비로 가요", 16, RED, 700), 3, 3),
            a.vis(book("장비 B", GREEN) + fl(a, [(360, 318), (640, 352)], 4, BLUE) + check(520, 360)
                  + text(190, 410, "주소록 갱신을 알려요", 16, ORANGE, 700), 4, 4),
            mk(a, 60, 314, 260, 38, 4, 8)]
    caps = ["주소록에는 대표 번호가 장비 A로 적혀 있어요", "장비 A가 멈춰도 주소록은 그대로예요", "장비 B가 넘겨받아도 요청은 옛 장비로 가요", "주소록을 갱신하면 요청이 장비 B로 가요"]
    return frame(a, "대표 번호는 책상이 아니라 당직 자리에", "주소록이 옛 장비를 가리키면 넘겨받아도 소용없어요", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "u13-l02-p3-phonebook", p3_phonebook())
    print("ok")
