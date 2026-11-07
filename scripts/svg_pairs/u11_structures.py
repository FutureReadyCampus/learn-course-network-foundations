#!/usr/bin/env python3
"""Unit 11 Lesson 1 (장치가 트래픽을 다루는 세 가지 구조). Run from the repo root:
python3 scripts/svg_pairs/u11_structures.py   (add --svg-only to skip the lesson.md edit).

Light example SVG per Page (6): previews what the advanced course does (길 위 검문 / 옆에서 관찰 / 대리 연결).
Replaces the stale wiki flow diagram (assets/diagrams/source-02.svg), which is deleted + unwired."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, arrow, dur
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/restructured/01-*"))
OUT = LESSON / "assets" / "animations"
Y = 300  # road line


def srv(x, y, c=GREEN):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, "서버", 18, TXT, 700))


def ends(extra=""):
    return laptop(110, Y, "내 컴퓨터") + srv(850, Y) + extra


def road(c=LINE, dash="10 8"):
    return line(170, Y, 800, Y, c, 4, dash)


def gate(x, y, c=ORANGE):
    """검문소: pillar + bar."""
    return (f'<rect x="{x - 26}" y="{y - 50}" width="52" height="100" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + text(x, y + 8, "검문", 18, c, 700))


def sensor(x, y, c=VIOLET):
    return eye(x, y)


def agent(x, y, c=BLUE):
    return box(x - 55, y - 40, 110, 80, c, PANEL, 12, sw=3) + text(x, y + 8, "대리인", 20, c, 700)


# 1 ---------------------------------------------------------------------------------
def p1():
    a = Anim(4, dur(False))
    body = [ends(), road(),
            mv(a, packet(0, 0), [(190, Y), (770, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(gate(480, Y) + pill(480, 215, "Inline · 길에서 직접", ORANGE, 17, False, 220), 2, 2),
            a.vis(sensor(480, 215) + line(480, 235, 480, Y - 10, VIOLET, 3, "6 6") + pill(480, 165, "Out of path · 옆에서", VIOLET, 17, False, 220), 3, 3),
            a.vis(agent(480, Y) + pill(480, 215, "Proxy · 대신 연결", BLUE, 17, False, 200), 4, 4)]
    caps = ["내 컴퓨터의 요청은 길을 따라 서버로 가요", "길 한가운데서 검문하면 Inline이에요", "길 옆에서 복사본만 보면 Out of path예요", "중간에서 대신 연결해 주면 Proxy예요"]
    return frame(a, "중간 장치가 하는 세 가지 일", "앞으로 이 Unit에서 하나씩 만나요", caps, "".join(body))


# 2 ---------------------------------------------------------------------------------
def p2():
    a = Anim(4, dur(False))
    body = [ends(gate(480, Y)), line(170, Y, 454, Y, LINE, 4, "10 8"), line(506, Y, 800, Y, LINE, 4, "10 8"),
            a.vis(pill(480, 215, "길 한가운데 놓인 필터", ORANGE, 18, False, 260), 1, 4),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 430, "허용 → 통과(Bypass)", GREEN, 18, True, 220), 2, 2),
            mv(a, packet(0, 0, RED), [(190, Y), (440, Y)], 3, 3, 3, 0.1, 0.6),
            a.vis(cross(480, 365) + pill(480, 430, "차단 규칙 → 버림(Drop)", RED, 18, True, 240), 3, 3),
            a.vis(pill(480, 430, "라우터·방화벽이 대표적인 Inline이에요", BLUE, 18, False, 420), 4, 4)]
    caps = ["Inline 장치는 패킷이 지나는 길 위에 있어요", "허용된 패킷은 그대로 통과해요", "차단 규칙에 맞으면 버려져요", "통과시키고 막는 일이 핵심이에요"]
    return frame(a, "Inline · 통과와 차단", "검문소처럼 길 위에서 직접 걸러요", caps, "".join(body))


# 3 ---------------------------------------------------------------------------------
def p3():
    a = Anim(4, dur(False))
    body = [ends(), road(),
            mv(a, packet(0, 0), [(190, Y), (770, Y)], 1, 1, 4, 0.1, 0.9),
            a.vis(sensor(480, 215) + pill(480, 165, "보안 센서", VIOLET, 18, False, 130), 2, 4),
            a.vis(circle_tap(480, Y) + line(480, 235, 480, Y - 14, VIOLET, 3, "6 6") + pill(560, 265, "복사본", VIOLET, 16, True, 90), 2, 4),
            a.vis(pill(480, 400, "복사본만 분석 → 이상하면 알려요", VIOLET, 18, True, 400), 3, 3),
            a.vis(check(850, 235) + pill(640, 400, "원래 통신은 그대로 도착", GREEN, 18, False, 300), 4, 4)]
    caps = ["원래 통신은 길을 따라 서버로 가요", "길 옆 Tapping Point에서 복사본을 받아요", "센서는 복사본을 분석해 알려 줘요", "원래 통신은 끊기지 않아요"]
    return frame(a, "Out of path · 관찰과 수집", "CCTV처럼 옆에서 지켜봐요", caps, "".join(body))


def circle_tap(x, y):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{VIOLET}"/>'


# 4 ---------------------------------------------------------------------------------
def p4():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "내 컴퓨터"), srv(850, Y), agent(480, Y),
            a.vis(line(170, Y, 425, Y, BLUE, 5) + pill(300, 255, "연결 ①", BLUE, 17, True, 90), 2, 4),
            a.vis(line(535, Y, 800, Y, GREEN, 5) + pill(660, 255, "연결 ②", GREEN, 17, True, 90), 3, 4),
            a.vis(pill(480, 150, "대신 받아서 대신 전달", BLUE, 18, False, 260), 1, 4),
            a.vis("".join(cell(330 + i * 56, 390, 50, 34, c, VIOLET, 15) for i, c in enumerate("GET /")) + text(480, 450, "이어진 바이트 흐름(Stream)을 읽어요", 17, MUTED, 700), 4, 4)]
    caps = ["Proxy는 요청을 받아 주는 대리인이에요", "나와 대리인 사이에 연결 ①을 맺어요", "대리인과 서버 사이에 연결 ②를 맺어요", "그래서 내용의 흐름 전체를 볼 수 있어요"]
    return frame(a, "Proxy · 대신 연결해 주는 대리인", "양쪽과 따로 연결을 맺어요", caps, "".join(body))


# 5 ---------------------------------------------------------------------------------
def p5():
    a = Anim(4, dur(False))
    rows = [("Inline", "경로 안", "패킷", ORANGE), ("Out of path", "경로 밖 (복사본)", "패킷", VIOLET), ("Proxy", "중간 대리", "소켓 Stream", BLUE)]
    hdr = cell(330, 120, 250, 40, "어디에 있나?", MUTED, 17, BG) + cell(600, 120, 250, 40, "무엇을 보나?", MUTED, 17, BG)
    body = [hdr]
    for i, (n, where, unit, c) in enumerate(rows):
        y = 180 + i * 80
        body.append(a.vis(cell(90, y, 220, 60, n, c, 22) + cell(330, y, 250, 60, where, c, 20) + cell(600, y, 250, 60, unit, c, 20), i + 1, 4))
    body.append(a.vis(pill(480, 440, "이름보다 위치와 단위를 먼저 물어봐요", GREEN, 19, True, 440), 4, 4))
    caps = ["Inline은 경로 안에서 패킷을 봐요", "Out of path는 복사본 패킷을 봐요", "Proxy는 소켓의 Stream을 봐요", "두 질문이면 대부분 구분돼요"]
    return frame(a, "장치를 구조로 나눠 보기", "위치와 처리 단위, 두 가지 질문이에요", caps, "".join(body))


# 6 ---------------------------------------------------------------------------------
def p6():
    a = Anim(4, dur(False))
    body = [box(300, 150, 360, 190, GREEN, PANEL, 18, sw=3) + text(480, 188, "보안 장비 한 대", 22, TXT, 700),
            a.vis(cell(330, 215, 150, 50, "Inline", ORANGE, 20) + text(405, 295, "경로 안에서 통과·차단", 15, MUTED), 2, 4),
            a.vis(cell(500, 215, 130, 50, "Proxy", BLUE, 20) + text(565, 295, "내용을 대신 중계", 15, MUTED), 3, 4),
            a.vis(pill(380, 385, "경로 안에 있나?", GREEN, 18, False, 190) + pill(580, 385, "패킷? Stream?", GREEN, 18, False, 190), 4, 4),
            a.vis(pill(480, 440, "다음 Lesson: Inline이 패킷을 전달하는 방법", MUTED, 17, False, 430), 4, 4)]
    caps = ["장치 하나가 여러 구조를 함께 가질 수 있어요", "경로 안에서 패킷을 통과·차단하고", "프록시 기능으로 내용도 중계해요", "그래서 이름 대신 두 질문으로 봐요"]
    return frame(a, "여러 구조가 한 장치에", "하나만 고집해서 분류하지 않아요", caps, "".join(body))


ITEMS = [
    ("u11-structures-preview", "advanced-source-02-page-01", "중간 장치가 하는 세 가지 일",
     "내 컴퓨터와 서버 사이 길 위에서 검문하는 Inline, 길 옆에서 복사본을 보는 Out of path, 대신 연결해 주는 Proxy를 차례로 미리 보여 줍니다.",
     "Inline, Out of path, Proxy를 일상 비유로 미리 살펴봅니다.", p1),
    ("u11-structures-inline", "advanced-source-02-page-02", "Inline · 통과와 차단",
     "길 한가운데 놓인 검문소가 허용된 패킷은 통과시키고 차단 규칙에 맞는 패킷은 버리는 모습입니다.",
     "Inline 장치는 패킷을 통과시키거나 버립니다.", p2),
    ("u11-structures-out-of-path", "advanced-source-02-page-03", "Out of path · 관찰과 수집",
     "원래 통신은 서버로 계속 가고, 길 옆 Tapping Point에서 복사본을 받은 센서가 분석해 알려 주는 모습입니다.",
     "Out of path 센서는 복사본만 분석하고 원래 통신은 그대로 둡니다.", p3),
    ("u11-structures-proxy", "advanced-source-02-page-04", "Proxy · 대신 연결해 주는 대리인",
     "내 컴퓨터와 대리인, 대리인과 서버 사이에 연결을 따로 맺고 이어진 Stream을 읽는 모습입니다.",
     "Proxy는 양쪽과 따로 연결을 맺어 Stream을 중계합니다.", p4),
    ("u11-structures-classify", "advanced-source-02-page-05", "장치를 구조로 나눠 보기",
     "Inline은 경로 안·패킷, Out of path는 경로 밖 복사본·패킷, Proxy는 중간 대리·소켓 Stream으로 구분하는 표입니다.",
     "위치와 처리 단위 두 가지로 장치를 나눕니다.", p5),
    ("u11-structures-combined", "advanced-source-02-page-06", "여러 구조가 한 장치에",
     "보안 장비 한 대가 Inline과 Proxy 기능을 함께 가질 수 있어 경로 안인가, 패킷인가 Stream인가를 묻는다는 그림입니다.",
     "한 장치가 여러 구조를 결합할 수 있습니다.", p6),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    # drop the old wiki diagram illustration block (page 1)
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-02\.svg\n(?:    .*\n)+", "", s, count=1)
    for f, pid, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in s:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        old = LESSON / "assets" / "diagrams" / "source-02.svg"
        old.unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
