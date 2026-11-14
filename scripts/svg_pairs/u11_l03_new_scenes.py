#!/usr/bin/env python3
"""Unit 11 Lesson 3 (숨은 AI 사용을 찾아라): new SVG for Page 1 (was missing).
Run from repo root: python3 scripts/svg_pairs/u11_l03_new_scenes.py   (--svg-only skips lesson.md edit).
Running example: 지우 PC 192.168.10.41 → 코어 스위치 → 게이트웨이 192.168.10.1, 옆에 센서 192.168.10.250."""
import sys
from u11_new_common import *  # noqa: F401,F403


def p1():
    a = new()
    sx, sy = 400, 185
    base = [dev("지우 PC", 110, Y, "192.168.10.41", laptop), dev("코어 스위치", 400, Y, None, switch), router(650, Y, "게이트웨이"),
            lbl(650, 374, "192.168.10.1"), cloud(870, Y), line(165, Y, 345, Y, LINE, 4, "10 8"), line(455, Y, 620, Y, LINE, 4, "10 8"), line(680, Y, 800, Y, LINE, 4, "10 8"),
            eye(sx, sy) + lbl(sx, sy - 40, "센서 192.168.10.250", TXT, 17, 700)]
    body = base + [
        mv(a, packet(0, 0), [(165, Y), (620, Y)], 1, 1, 1, 0.1, 0.9),
        a.vis(ask(sx + 70, sy) + pill(690, sy, "센서에는 아무것도 안 와요", ORANGE, 18, False, 280), 1, 1), mark(a, sx - 34, sy - 24, 68, 48, 1),
        a.vis(line(sx, 284, sx, sy + 24, VIOLET, 3, "6 6"), 2, 4), a.vis(pill(690, sy, "포트 미러링 · TAP으로 복사", VIOLET, 18, False, 300), 2, 2), mark(a, sx - 10, 215, 20, 70, 2),
        mv(a, packet(0, 0, VIOLET), [(sx, 280), (sx, sy + 34)], 3, 3, 3, 0.1, 0.8), mv(a, packet(0, 0), [(165, Y), (620, Y)], 3, 3, 3, 0.1, 0.9),
        a.vis(check(sx + 70, sy) + pill(690, sy, "원래 통신은 그대로 가요", GREEN, 18, False, 280), 3, 3), mark(a, sx - 34, sy - 24, 68, 48, 3),
        a.vis(pill(480, 440, "센서는 기록만 해요 · 막는 일은 Inline이 해요", GREEN, 18, True, 480), 4, 4), mark(a, 236, 421, 488, 38, 4)]
    caps = ["스위치는 목적지 포트로만 보내요", "복사 경로를 만들어 센서에 연결해요", "복사본은 센서로, 원본은 그대로 가요", "센서는 지켜볼 뿐 막지는 못해요"]
    return frame(a, "센서에 복사본 보내기", "업무 통신 경로는 하나도 안 바꿔요", caps, "".join(body))


SCENES = [
    ("advanced-source-05-page-01", "u11-l03-p01-sensor-copy", "센서에 복사본 보내기",
     "지우 PC에서 게이트웨이로 가는 통신은 그대로 두고, 스위치의 복사본만 관리 주소 192.168.10.250의 센서로 보내는 모습입니다.",
     "센서를 쓰려면 복사 경로가 필요하고, 센서는 관찰만 할 뿐 막지는 못합니다.", 2, p1),
]

if __name__ == "__main__":
    run(3, SCENES, sys.argv)
