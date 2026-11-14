#!/usr/bin/env python3
"""Unit 11 Lesson 6 (AI 앱이 실제로 보내는 것 읽기): new SVGs for Pages 1, 2, 6 (replace the versions that named real tools).
Run from repo root: python3 scripts/svg_pairs/u11_l06_new_scenes.py   (--svg-only skips lesson.md edit).
Running example: 지우 PC 192.168.10.41 · 회사 프록시 192.168.10.5:8080 · 외부 AI API 203.0.113.80:443 · 로컬 프록시 127.0.0.1:8080."""
import sys
from u11_new_common import *
from u12_l01_router import net  # noqa: F401,F403


def p1():
    a = new()
    ey = 160
    body = [dev("지우 PC", 110, 230, "192.168.10.41", laptop), node(480, 230, "회사 프록시", "192.168.10.5:8080", 170, 70), server(850, 230, "외부 AI API", "203.0.113.80:443"),
            line(165, 230, 395, 230, LINE, 4, "10 8"), line(565, 230, 810, 230, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, 230), (390, 230)], 1, 1, 1, 0.05, 0.45), mv(a, packet(0, 0), [(570, 230), (800, 230)], 1, 1, 1, 0.55, 0.95), mark(a, 62, 192, 96, 64, 1),
            a.vis(eye(295, ey) + line(295, ey + 18, 295, 222, VIOLET, 3, "6 6") + lbl(295, 122, "패킷 캡처 도구", TXT, 17, 700), 2, 4), mark(a, 262, ey - 24, 66, 48, 2),
            a.vis(cell(150, 350, 190, 50, "IP 헤더", GREEN, 18) + check(316, 375) + cell(350, 350, 190, 50, "TCP 헤더", GREEN, 18) + check(516, 375)
                  + cell(550, 350, 260, 50, "Payload (HTTPS)", RED, 18) + cross(786, 375), 3, 4), mark(a, 550, 350, 260, 50, 3),
            a.vis(pill(480, 440, "잡는 것과 읽는 것은 달라요", BLUE, 18, True, 320), 4, 4), mark(a, 320, 421, 320, 38, 4)]
    caps = ["플러그인 요청이 회사 프록시를 거쳐 나가요", "지우가 PC에서 패킷을 캡처해 봐요", "헤더는 읽히지만 내용은 암호문이에요", "내용을 보려면 중계 지점이 필요해요"]
    return frame(a, "패킷은 잡았는데 왜 못 읽을까?", "플러그인 요청을 캡처한 화면이에요", caps, "".join(body))


def p2():
    a = new()
    body = [net(40, 135, 520, 290, "지우 PC 192.168.10.41", GREEN), node(140, 285, "AI 플러그인", None, 150, 70, VIOLET), server(850, 285, "외부 AI API", "203.0.113.80:443"),
            a.vis(line(215, 285, 810, 285, LINE, 4, "10 8") + pill(710, 220, "요청이 바로 나가요", ORANGE, 17, False, 220), 1, 1),
            mv(a, packet(0, 0), [(220, 285), (790, 285)], 1, 1, 1, 0.1, 0.9),
            a.vis(node(430, 285, "로컬 프록시", "127.0.0.1:8080", 160, 70, BLUE) + line(215, 285, 350, 285, LINE, 4, "10 8") + line(510, 285, 810, 285, LINE, 4, "10 8"), 2, 4), mark(a, 350, 250, 160, 70, 2),
            mv(a, packet(0, 0), [(220, 285), (345, 285)], 2, 2, 2, 0.05, 0.45), mv(a, packet(0, 0), [(515, 285), (790, 285)], 2, 2, 2, 0.55, 0.95),
            a.vis(box(85, 375, 430, 42, GREEN, PANEL, 8, sw=2) + text(280, 402, "요청 한 건씩 URL · 헤더 · 본문 목록", 18, TXT, 700) + check(490, 396), 3, 4), mark(a, 85, 375, 430, 42, 3),
            a.vis(pill(480, 450, "내 PC · 승인된 범위만, 가짜 평면도로 실험해요", BLUE, 17, True, 480), 4, 4), mark(a, 235, 431, 490, 38, 4)]
    caps = ["플러그인은 AI 서비스와 바로 이야기해요", "PC 안에 로컬 프록시를 먼저 세워요", "요청이 한 건씩 목록으로 보여요", "내 통신이거나 승인된 범위만 봐요"]
    return frame(a, "내 PC 안에 중계소 세우기", "로컬 프록시는 프록시 하나가 더 생기는 거예요", caps, "".join(body))


def p6():
    a = new()
    rows = [(255, "무료 우회 프록시", "회사 밖 인터넷", "모르는 외부 운영자", False),
            (315, "회사 프록시", "사내 서버실 192.168.10.5:8080", "회사 IT·보안 담당", True),
            (375, "로컬 프록시", "분석하는 PC 안 127.0.0.1:8080", "그 PC를 쓰는 사람", True)]
    sk = [node(180, 160, "클라이언트", None, 150, 50), node(480, 160, "프록시", None, 150, 50), node(780, 160, "서버", None, 150, 50),
          line(255, 160, 405, 160, LINE, 4, "10 8"), line(555, 160, 705, 160, LINE, 4, "10 8"),
          a.vis(pill(480, 215, "뼈대는 하나: 연결 둘, 그 사이에서 Stream 전달", BLUE, 17, False, 500), 1, 1), mark(a, 100, 130, 760, 60, 1)]
    t = []
    for y, name, where, who, ok in rows:
        t.append(a.vis(box(60, y, 840, 52, LINE, PANEL, 8, sw=2) + text(80, y + 33, name, 19, TXT, 700, "start"), 2, 4))
        t.append(a.vis(text(300, y + 32, where, 17, TXT, None, "start"), 2, 4))
        t.append(a.vis(text(680, y + 32, who, 17, GREEN if ok else RED, 700, "start") + (check(880, y + 26) if ok else cross(880, y + 26)), 3, 4))
    hd = [a.vis(text(300, 247, "어디에 있나", 15, MUTED, 700, "start"), 2, 4), a.vis(text(680, 247, "누가 관리하나", 15, MUTED, 700, "start"), 3, 4)]
    body = sk + hd + t + [mark(a, 290, 228, 380, 206, 2), mark(a, 670, 228, 235, 206, 3),
                          a.vis(pill(480, 455, "어디에 · 누가 · TLS는 누가 · 무엇을 기록, 네 가지만 물어요", GREEN, 17, True, 640), 4, 4), mark(a, 160, 436, 640, 38, 4)]
    caps = ["세 프록시 모두 뼈대는 같아요", "놓인 자리가 서로 달라요", "누가 관리하느냐가 성격을 정해요", "새 프록시를 만나면 네 가지를 물어요"]
    return frame(a, "우회 · 회사 · 로컬, 같은 모양일까?", "프록시 세 개를 나란히 비교해요", caps, "".join(body))


SCENES = [
    ("advanced-source-09-page-01", "u11-l06-p01-capture-limit", "패킷은 잡았는데 왜 못 읽을까?",
     "지우 PC의 플러그인 요청을 패킷 캡처하면 IP·TCP 헤더는 보이지만 HTTPS Payload는 암호문이라 읽을 수 없는 모습입니다.",
     "패킷을 잡는 것과 내용을 읽는 것은 다르며, 내용을 보려면 중계 지점이 필요합니다.", 2, p1),
    ("advanced-source-09-page-02", "u11-l06-p02-local-proxy", "내 PC 안에 중계소 세우기",
     "지우 PC 안에 로컬 프록시 127.0.0.1:8080을 세우면 AI 플러그인의 요청이 먼저 도착해 한 건씩 목록으로 보이는 모습입니다.",
     "로컬 프록시는 내 PC 안의 포워드 프록시이며, 내 통신이거나 승인된 범위만 봅니다.", 1, p2),
    ("advanced-source-09-page-06", "u11-l06-p06-three-proxies", "우회 · 회사 · 로컬, 같은 모양일까?",
     "무료 우회 프록시, 회사 프록시, 로컬 프록시가 같은 뼈대이고 놓인 자리와 관리자가 다른 것을 비교합니다.",
     "프록시의 성격은 어디에 있고 누가 관리하는지가 정합니다.", 2, p6),
]

if __name__ == "__main__":
    run(6, SCENES, sys.argv)
