#!/usr/bin/env python3
"""Unit 12 Lesson 5 Page 6: 「안내 데스크 장부로 보는 홀 펀칭」 4-step SVG (안내 데스크 비유).
Run from repo root: python3 scripts/svg_pairs/u12_l05_terms.py  (lesson.md is edited by hand)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

OUT = lesson_dir(5) / "assets" / "animations"
YY = 250
LX, RX = 250, 710


def desk_ledger():
    p = Pg("안내 데스크 장부로 보는 홀 펀칭", "양쪽이 먼저 보내면 양쪽 장부에 기록이 생겨요",
           ["두 데스크는 먼저 연락한 손님만 들여요", "박 팀장이 먼저 보내면 박 팀장 장부에만 기록이 남아요",
            "지우도 먼저 보내면 지우 장부에도 기록이 남아요", "양쪽 장부에 기록이 있어 그 뒤의 연락은 통과해요"])
    p.base(laptop(90, YY, "박 팀장"), rt(LX, YY, "박 팀장 쪽 데스크"), rt(RX, YY, "지우 쪽 데스크"), laptop(870, YY, "지우"),
           line(140, YY, LX - 28, YY, LINE, 4, "8 6"), line(LX + 28, YY, RX - 28, YY, LINE, 4, "10 8"), line(RX + 28, YY, 820, YY, LINE, 4, "8 6"))
    p.at(pill(480, 150, "먼저 연락한 손님만 들여요", MUTED, 18, False, 320), 1, 1, mark=(320, 129, 320, 42))
    L = (LX - 130, 365, 260, 46)
    R = (RX - 130, 365, 260, 46)
    p.at(cell(*L, "장부: 지우 쪽으로 보냄", GREEN, 16), 2, mark=L)
    p.fly(packet(0, 0, BLUE), [(LX + 30, YY), (RX - 60, YY)], 2, 0.05, 0.9)
    p.at(pill(RX, 175, "첫 연락은 돌려보내요", RED, 17, False, 230), 2, 2)
    p.at(cell(*R, "장부: 박 팀장 쪽으로 보냄", GREEN, 16), 3, mark=R)
    p.at(line(LX + 30, YY, RX - 30, YY, ORANGE, 6, "12 8") + pill(480, 175, "그 뒤의 연락은 통과해요", GREEN, 18, True, 300), 4, 4,
         mark=(LX + 30, YY - 20, RX - LX - 60, 40))
    return p.render()


if __name__ == "__main__":
    write(OUT, "u12-l05-p06c-desk-ledger", desk_ledger())
    print("ok")
