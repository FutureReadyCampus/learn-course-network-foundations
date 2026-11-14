#!/usr/bin/env python3
"""Unit 11 Lesson 2 (회사 PC에서만 AI가 안 열리는 이유): new SVGs for Page 1 (replaces the stale 2) and Page 6 (was missing).
Run from repo root: python3 scripts/svg_pairs/u11_l02_new_scenes.py   (--svg-only skips lesson.md edit).
Running example: 박 팀장 노트북 192.168.10.42 → 스위치 → 본사 게이트웨이(192.168.10.1 / 198.51.100.25) → ISP → AI 서비스 203.0.113.80."""
import sys
from u11_new_common import *  # noqa: F401,F403


def p1():
    a = new()
    xs = [100, 270, 450, 640, 850]
    body = [dev("노트북", 100, Y, "192.168.10.42", laptop), dev("스위치", 270, Y, None, switch), router(450, Y, "본사 게이트웨이"),
            lbl(450, 374, "192.168.10.1"), lbl(450, 392, "198.51.100.25"), router(640, Y, "ISP 라우터"), server(850, Y, "AI 서비스", "203.0.113.80"),
            line(150, Y, 215, Y, LINE, 4, "10 8"), line(325, Y, 420, Y, LINE, 4, "10 8"), line(480, Y, 610, Y, LINE, 4, "10 8"), line(670, Y, 810, Y, LINE, 4, "10 8"),
            a.vis(pill(480, 190, "박 팀장 노트북의 요청", BLUE, 18, False, 260), 1, 1), mark(a, 55, 245, 92, 75, 1),
            mv(a, packet(0, 0), [(150, Y), (380, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 190, "지나가는 장치는 모두 Inline", BLUE, 18, False, 300), 2, 2), mark(a, 214, 268, 112, 44, 2),
            a.vis(packet(380, Y) + cross(450, 235) + pill(480, 190, "이 목적지만 안 열려요", RED, 18, False, 260), 3, 3), mark(a, 412, 252, 76, 76, 3),
            a.vis(pill(480, 440, "의심할 곳은 출구 장치부터", GREEN, 18, True, 320), 4, 4), mark(a, 316, 421, 328, 38, 4)]
    caps = ["박 팀장 노트북의 요청이 출발해요", "스위치와 게이트웨이를 차례로 지나요", "다른 사이트는 열리고 이 서비스만 막혀요", "원인은 경로 위 출구 장치에서 찾아요"]
    return frame(a, "AI 요청이 지나는 길목", "집과 달리 회사에는 장치가 여러 개예요", caps, "".join(body))


def p6():
    a = new()
    gw = node(480, 265, "본사 게이트웨이", "192.168.10.1", 190, 80)
    body = [pc(110, 230), pc(110, 340), lbl(110, 410, "사무실 PC 40대", TXT, 17, 700), gw, cloud(850, 265),
            line(150, 230, 385, 255, LINE, 4, "10 8"), line(150, 340, 385, 285, LINE, 4, "10 8"), line(575, 265, 780, 265, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, 235), (350, 252)], 1, 1, 1, 0.05, 0.5), mv(a, packet(0, 0), [(610, 265), (770, 265)], 1, 1, 1, 0.5, 0.95),
            a.vis(pill(480, 175, "평소엔 모든 통신이 여기를 지나요", BLUE, 18, False, 360), 1, 1), mark(a, 380, 220, 200, 90, 1),
            a.vis(node(480, 265, "재부팅 중", "192.168.10.1", 190, 80, ORANGE), 2, 3),
            a.vis(pill(480, 175, "토요일 보안 업데이트 → 재부팅", ORANGE, 18, False, 380), 2, 2), mark(a, 380, 220, 200, 90, 2),
            a.vis(cross(700, 265) + packet(300, 250) + pill(480, 175, "사무실 전체 인터넷이 끊겨요", RED, 18, False, 340), 3, 3), mark(a, 676, 241, 48, 48, 3),
            a.vis(node(480, 405, "두 번째 장치 (이중화)", None, 230, 56, GREEN) + line(480, 338, 480, 377, GREEN, 3, "6 6"), 4, 4),
            a.vis(pill(480, 175, "이중화도 Bypass도 대가가 있어요", GREEN, 18, True, 360), 4, 4), mark(a, 360, 373, 240, 66, 4)]
    caps = ["게이트웨이 하나가 모든 통신을 맡아요", "업데이트하려고 재부팅을 걸었어요", "재부팅하는 몇 분 동안 인터넷이 끊겨요", "장치를 두 대 두거나 Bypass를 두어요"]
    return frame(a, "길목 장치가 멈추면?", "단일 장애점이 만드는 일이에요", caps, "".join(body))


SCENES = [
    ("advanced-source-03-page-01", "u11-l02-p01-office-path", "AI 요청이 지나는 길목",
     "박 팀장 노트북의 요청이 스위치와 본사 게이트웨이, ISP 라우터를 지나 AI 서비스로 가고, 게이트웨이에서 이 목적지만 막히는 모습입니다.",
     "지나가는 장치는 모두 Inline이며, 이 서비스만 안 열리면 출구 장치를 먼저 의심합니다.", 1, p1),
    ("u11-l02-page-07", "u11-l02-p06-reboot-spof", "길목 장치가 멈추면?",
     "본사 게이트웨이를 재부팅하자 사무실 PC 전체의 인터넷이 끊기고, 장치를 두 대 두는 이중화가 대안으로 나오는 모습입니다.",
     "Inline 장치는 단일 장애점이 될 수 있어 이중화나 Bypass로 대비하되 각각 대가가 있습니다.", 2, p6),
]

if __name__ == "__main__":
    run(2, SCENES, sys.argv)
