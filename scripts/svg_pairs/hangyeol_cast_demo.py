#!/usr/bin/env python3
"""Demo of the 4-step situation-SVG convention (see hangyeol_cast.py). Writes /tmp/hangyeol_demo/demo.svg only.
Run: python3 scripts/svg_pairs/hangyeol_cast_demo.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403

OUT = Path("/tmp/hangyeol_demo")


def demo():
    a = new()
    bubble_s = "고객 도면은 안전해요?"
    bw = tw(bubble_s, 18) + 36
    body = [line(450, 130, 450, 400, LINE, 3, "10 8"),
            pill(225, 395, "고객사 현장", MUTED, 17), pill(705, 395, "본사", MUTED, 17),
            # 박 팀장: normal in step 1, worried afterwards
            a.vis(person(150, 235, "박 팀장", "normal"), 1, 1), a.vis(person(150, 235, "박 팀장", "worried"), 2, 4),
            a.vis(person(620, 235, "지우", "normal", role=False), 1, 2), a.vis(person(620, 235, "지우", "thinking"), 3, 4),
            a.vis(person(850, 235, "서 이사", "normal", facing="left"), 1, 2), a.vis(person(850, 235, "서 이사", "worried", facing="left"), 3, 4),
            mark(a, 106, 203, 88, 160, 1),
            a.vis(monitor(320, 290, "error", "AI 연결 안 됨"), 2, 4), mark(a, 218, 228, 204, 124, 2),
            a.vis(bubble(190, 168, "AI가 안 열려요", tail_to=(158, 208), color=TERRACOTTA), 2, 2),
            a.vis(bubble(795, 168, bubble_s, tail_to=(850, 208), color=VIOLET), 3, 3), mark(a, 795 - bw / 2 - 5, 139, bw + 10, 58, 3),
            a.vis(thought(560, 160, "어떤 길로?\n어떤 장비?", tail_to=(612, 208), color=BLUE), 3, 4),
            question(a, "AI 요청은 어떤 길을 지날까?")]
    caps = ["고객사의 박 팀장, 본사의 지우와 서 이사예요", "박 팀장 모니터에서 사내 AI가 열리지 않아요",
            "서 이사는 도면이 걱정, 지우는 길을 떠올려요", "이 Page에서 그 길을 따라가 봐요"]
    return scene(a, "고객사에서 사내 AI가 안 열려요", "박 팀장의 요청은 어디서 막혔을까요?", caps, "".join(body), bg="office")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, "demo", demo())
    print(OUT / "demo.svg")
