#!/usr/bin/env python3
"""Unit 12 Lesson 4 Page 4: 「줄에도 기한이 있다」 4-step SVG (안내 데스크 대장 비유, 유지 시간).
Run from repo root: python3 scripts/svg_pairs/u12_l04_terms.py  (lesson.md is edited by hand)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

OUT = lesson_dir(4) / "assets" / "animations"
PC37 = "192.168.10.37"


def lease_ledger():
    p = Pg("줄에도 기한이 있어요", "대장에 적은 줄은 기한 안에 갱신하고 끝나면 지워요",
           ["줄을 적을 때 유지 시간(기한)도 같이 적어요", "프로그램이 기한 전에 갱신해요",
            "끝날 때는 줄을 지워 달라고 말해요", "갑자기 꺼지면 줄이 대장에 남아요"])
    p.base(pc(130, 270, PC37), rt(480, 270), line(190, 270, 450, 270, LINE, 4, "8 6"),
           lbl(790, 155, "공유기 대장", MUTED, 17), box(630, 170, 320, 56, MUTED, PANEL, 6, dash=True, sw=2))
    row = cell(640, 178, 300, 40, "TCP 6881 → .37  기한 1시간", GREEN, 16)
    p.at(row, 1, 2, mark=(640, 178, 300, 40))
    p.at(pill(480, 400, "줄과 기한을 함께 적어요", GREEN, 17, True, 300), 1, 1)
    p.at(pill(480, 400, "기한 전에 \"연장해 주세요\"", BLUE, 17, True, 300), 2, 2, mark=(330, 380, 300, 40))
    p.at(pill(480, 400, "\"제 줄을 지워 주세요\"", BLUE, 17, True, 300), 3, 3, mark=(330, 380, 300, 40))
    p.at(cell(640, 178, 300, 40, "TCP 6881 → .37  (주인 없음)", RED, 16)
         + pill(480, 400, "삭제 못 하고 꺼졌어요", RED, 17, True, 300) + cross(130, 340), 4, 4, mark=(640, 178, 300, 40))
    return p.render()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    done(OUT, "u12-l04-p04-lease-ledger", lease_ledger)
    print("ok")
