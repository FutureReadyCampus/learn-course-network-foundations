#!/usr/bin/env python3
"""Unit 11 Lesson 4 (AI에 대신 다녀오는 심부름꾼): new SVGs replacing stale Page 2 (example.net wording) and Page 4 (no ledger addresses).
Run from repo root: python3 scripts/svg_pairs/u11_l04_new_scenes.py   (--svg-only skips lesson.md edit).
Running example: 지우 PC 192.168.10.41 + 프록시 192.168.10.5:8080 + AI 서비스 203.0.113.80, 본사 공인 주소 198.51.100.25."""
import sys
from u11_new_common import *  # noqa: F401,F403


def p2():
    a = new()
    px, py = 480, 270
    body = [dev("지우 PC", 110, 320, "192.168.10.41", laptop), pill(110, 205, "브라우저", BLUE, 16, False, 110), pill(110, 245, "회의록 앱", VIOLET, 16, False, 110),
            node(px, py, "프록시", "192.168.10.5:8080"), server(850, 320, "AI 서비스", "203.0.113.80"),
            line(165, 300, 405, py, LINE, 4, "10 8"), line(555, py, 810, 300, LINE, 4, "10 8"),
            a.vis(box(270, 132, 420, 56, BLUE, PANEL, 10, sw=2) + text(480, 167, "프록시 192.168.10.5 · 포트 8080", 20, TXT, 700), 1, 2), mark(a, 270, 132, 420, 56, 1),
            mv(a, packet(0, 0), [(170, 300), (395, py)], 2, 2, 2, 0.05, 0.45), mv(a, packet(0, 0), [(565, py), (800, 300)], 2, 2, 2, 0.55, 0.95), mark(a, 405, 235, 150, 70, 2),
            a.vis(check(480, 205) + pill(620, 205, "프록시 기록에 한 줄", GREEN, 17, False, 220), 3, 3),
            a.vis(line(170, 355, 790, 355, LINE, 4, "10 8") + cross(700, 355) + pill(480, 395, "회의록 앱은 기록이 없어요", RED, 17, False, 280), 3, 3), mark(a, 165, 340, 630, 30, 3),
            mv(a, packet(0, 0, VIOLET), [(170, 355), (640, 355)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(480, 440, "설정을 읽는 프로그램만 프록시를 거쳐요", BLUE, 18, True, 420), 4, 4), mark(a, 270, 421, 420, 38, 4)]
    caps = ["브라우저 설정에 프록시 주소를 넣어요", "브라우저는 먼저 프록시에 요청을 맡겨요", "같은 PC의 회의록 앱은 바로 나가요", "프로그램마다 프록시 설정을 확인해요"]
    return frame(a, "브라우저에 프록시 주소 넣기", "같은 PC인데 어떤 요청만 거쳐요", caps, "".join(body))


def row(a, i, y, left, right, rc, s):
    inner = (box(60, y, 840, 65, LINE, PANEL, 10, sw=2) + text(85, y + 41, left, 21, TXT, 700, "start")
             + text(560, y + 43, "→", 28, MUTED) + pill(740, y + 33, right, rc, 19, i < 2, 250))
    if i == 2:
        inner += cross(884, y + 33)
    return a.vis(inner, s, 4) + mark(a, 60, y, 840, 65, s)


def p4():
    a = new()
    body = [text(250, 140, "접속 방법", 18, MUTED, 700) + text(740, 140, "AI 서비스에 보이는 주소", 18, MUTED, 700),
            row(a, 0, 160, "직접 접속 (회사 경계 NAT를 거쳐요)", "198.51.100.25", GREEN, 1),
            row(a, 1, 245, "회사 프록시 192.168.10.5 경유", "198.51.100.25", GREEN, 2),
            row(a, 2, 330, "해외 우회 프록시 경유", "해외 프록시 서버 주소", ORANGE, 3),
            a.vis(pill(480, 440, "주소가 바뀌어도 로그인하면 서비스는 사용자를 알아요", BLUE, 18, True, 560), 4, 4), mark(a, 200, 421, 560, 38, 4)]
    caps = ["직접 접속하면 본사 공인 주소가 보여요", "회사 프록시를 거쳐도 같은 주소예요", "해외 프록시를 거치면 그 서버 주소예요", "주소가 바뀐다고 신원이 숨는 건 아니에요"]
    return frame(a, "AI 서비스에는 누구 주소가 보일까?", "접속 방법마다 찍히는 주소를 비교해요", caps, "".join(body))


SCENES = [
    ("advanced-source-06-page-03", "u11-l04-p02-browser-proxy", "브라우저에 프록시 주소 넣기",
     "지우 PC 브라우저에 프록시 192.168.10.5 포트 8080을 넣으면 요청이 프록시를 거쳐 AI 서비스로 가고, 설정을 읽지 않는 회의록 앱은 기록 없이 바로 나가는 모습입니다.",
     "프록시 설정은 그것을 읽는 프로그램에만 통합니다.", 1, p2),
    ("advanced-source-06-page-02", "u11-l04-p04-seen-address", "AI 서비스에는 누구 주소가 보일까?",
     "직접 접속과 회사 프록시 경유는 본사 공인 주소 198.51.100.25로, 해외 우회 프록시 경유는 그 서버의 주소로 보이는 것을 비교합니다.",
     "주소가 바뀌어도 로그인하면 신원이 감춰지지 않으며, 어느 PC인지는 회사 프록시 기록에서 찾습니다.", 3, p4),
]

if __name__ == "__main__":
    run(4, SCENES, sys.argv)
