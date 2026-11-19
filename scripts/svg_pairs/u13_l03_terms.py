#!/usr/bin/env python3
"""Unit 13 Lesson 3 용어 보강 SVG (초보자용 비유 블록). Run from repo root: python3 scripts/svg_pairs/u13_l03_terms.py
lesson.md는 건드리지 않는다(illustrations는 손으로 추가).
Page 2: 리졸버 = 안내 데스크, 레코드 = 번호부 한 줄, 캐시 = 메모, TTL = 메모 유효 시간."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u13_l03_gslb import *  # noqa: F401,F403
from u12_new_common import done  # noqa: F401


def p2_desk():
    a = new()
    R, B, M = (250, 205, 230, 70), (700, 205, 220, 70), (250, 345, 230, 64)
    body = [person(80, 240), arrow(130, 245, 240, MUTED, 5),
            cell(*R, "안내 데스크(리졸버)", VIOLET, 17),
            arrow(480, 695, 240, MUTED, 5),
            a.vis(cell(*B, "번호부(DNS 레코드)", BLUE, 17), 1, 2), a.vis(cell(*B, "번호부 고침(도쿄 뺌)", GREEN, 17), 3, 3),
            a.vis(cell(*B, "번호부(새 주소)", GREEN, 17), 4, 4),
            mk(a, 246, 201, 238, 78, 1),
            a.vis(cell(*M, "메모(캐시) 도쿄 .20 · 1시간", ORANGE, 16) + line(365, 275, 365, 345, MUTED, 4), 2, 2), mk(a, 246, 341, 238, 72, 2),
            a.vis(cell(*M, "메모에서 옛 번호를 읽어 줘요", RED, 16) + line(365, 275, 365, 345, RED, 4) + cross(500, 345), 3, 3), mk(a, 246, 341, 238, 72, 3),
            a.vis(cell(*M, "1시간 지나 메모를 버려요(TTL)", GREEN, 16) + check(500, 345), 4, 4), mk(a, 246, 341, 238, 72, 4)]
    caps = ["손님은 안내 데스크(리졸버)에 이름을 물어요", "안내 데스크가 번호를 메모(캐시)에 적어 둬요",
            "번호부를 고쳐도 메모가 남아 있으면 옛 번호를 읽어 줘요", "메모의 유효 시간(TTL)이 끝나면 새로 찾아요"]
    return frame(a, "리졸버, 캐시, TTL은 무엇일까?", "안내 데스크가 번호를 메모해 두는 시간이에요", caps, "".join(body))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    done(OUT, "u13-l03-p02-desk-memo", p2_desk)
    print("ok")
