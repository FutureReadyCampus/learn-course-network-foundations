#!/usr/bin/env python3
"""Unit 11 Lesson 7 (사내 AI 서버 앞에 경비를 세우자): new SVGs for Page 1 and Page 5 (were missing).
Run from repo root: python3 scripts/svg_pairs/u11_l07_new_scenes.py   (--svg-only skips lesson.md edit).
Running example: 고객 192.0.2.77 → ai.hangyeol.example(198.51.100.25:443) 앞단 → AI 서버 192.168.10.50:8080."""
import sys
from u11_new_common import *  # noqa: F401,F403


def p1():
    a = new()
    body = [dev("고객", 110, Y, "192.0.2.77", laptop), node(480, Y, "앞단 리버스 프록시", "198.51.100.25:443", 210, 80, BLUE, 17), server(850, Y, "AI 서버", "192.168.10.50:8080"),
            a.vis(pill(480, 190, "ai.hangyeol.example → 198.51.100.25", ORANGE, 18, False, 440), 1, 1), mark(a, 260, 169, 440, 42, 1),
            a.vis(line(165, Y, 375, Y, LINE, 4, "10 8") + lbl(270, 275, "TCP ① 443번 포트", TXT, 16, 700), 2, 4),
            mv(a, packet(0, 0), [(170, Y), (370, Y)], 2, 2, 2, 0.1, 0.9), mark(a, 375, 255, 210, 90, 2),
            a.vis(line(585, Y, 810, Y, LINE, 4, "10 8") + lbl(700, 275, "TCP ② 새 연결", TXT, 16, 700), 3, 4),
            mv(a, packet(0, 0), [(590, Y), (790, Y)], 3, 3, 3, 0.1, 0.9), a.vis(check(110, 235) + pill(480, 190, "고객에게는 앞단이 곧 서버예요", GREEN, 18, False, 340), 3, 3), mark(a, 585, 285, 225, 30, 3),
            a.vis(pill(480, 430, "자리만 생겼을 뿐, 보안은 앞단에 얹는 것이 정해요", BLUE, 18, True, 520), 4, 4), mark(a, 215, 411, 530, 38, 4)]
    caps = ["DNS는 사설 주소가 아닌 공인 주소를 알려 줘요", "고객은 앞단의 443번 포트에 연결해요", "앞단이 안쪽 AI 서버와 새로 연결해요", "구조만으로 보안이 보장되지는 않아요"]
    return frame(a, "고객 요청은 앞단에서 받아요", "접속 주소와 처리 서버를 나눠요", caps, "".join(body))


def p5():
    a = new()
    front = node(480, Y, "앞단 (한 대)", "198.51.100.25:443", 190, 80, BLUE, 18)
    body = [dev("고객", 110, Y, "192.0.2.77", laptop), front, server(850, Y, "AI 서버", "192.168.10.50:8080"),
            line(165, Y, 385, Y, LINE, 4, "10 8"), line(575, Y, 810, Y, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, Y), (380, Y)], 1, 1, 1, 0.05, 0.45), mv(a, packet(0, 0), [(580, Y), (790, Y)], 1, 1, 1, 0.55, 0.95),
            a.vis(pill(480, 190, "모든 시연 요청이 앞단 한 대를 지나요", BLUE, 18, False, 400), 1, 1), mark(a, 385, 260, 190, 80, 1),
            a.vis(node(480, Y, "재시작 · 과부하", "198.51.100.25:443", 190, 80, ORANGE, 17), 2, 3), a.vis(pill(480, 190, "앞단이 멈췄어요", ORANGE, 18, False, 240), 2, 2), mark(a, 385, 260, 190, 80, 2),
            a.vis(cross(480, 225) + check(850, 235) + packet(300, Y) + pill(480, 175, "고객에게는 서비스 전체가 멈춰 보여요", RED, 18, False, 400), 3, 3), mark(a, 810, 205, 80, 62, 3),
            a.vis(node(480, 410, "앞단 한 대 더 (이중화)", None, 250, 56, GREEN), 4, 4),
            a.vis(pill(480, 175, "한 대가 멈춰도 이어받아요 · 비용과 설정이 늘어요", GREEN, 17, True, 520), 4, 4), mark(a, 350, 378, 260, 66, 4)]
    caps = ["고객 요청은 모두 앞단 한 대를 지나요", "앞단이 재시작하거나 과부하에 걸려요", "AI 서버는 멀쩡해도 서비스가 멈춰요", "앞단도 이중화해 단일 장애점을 줄여요"]
    return frame(a, "앞단 한 대에 기대면?", "한곳에 모은 기능은 한곳이 약점이 돼요", caps, "".join(body))


SCENES = [
    ("advanced-source-08-page-01", "u11-l07-p01-front-flow", "고객 요청은 앞단에서 받아요",
     "고객이 ai.hangyeol.example을 조회해 공인 주소 198.51.100.25의 앞단에 연결하면, 앞단이 안쪽 AI 서버 192.168.10.50:8080과 새로 연결해 응답을 돌려주는 모습입니다.",
     "리버스 프록시는 접속 주소와 처리 서버를 나누지만 구조만으로 보안이 보장되지는 않습니다.", 3, p1),
    ("advanced-source-08-page-05", "u11-l07-p05-single-front", "앞단 한 대에 기대면?",
     "모든 시연 요청이 지나는 앞단 한 대가 멈추면 AI 서버가 멀쩡해도 서비스 전체가 멈추고, 앞단을 이중화해 대비하는 모습입니다.",
     "앞단은 단일 장애점이므로 이중화가 필요하고 그만큼 비용과 설정이 늘어납니다.", 2, p5),
]

if __name__ == "__main__":
    run(7, SCENES, sys.argv)
