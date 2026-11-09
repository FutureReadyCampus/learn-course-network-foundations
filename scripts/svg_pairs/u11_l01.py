#!/usr/bin/env python3
"""Unit 11 Lesson 1 (심화편 소개: 내 서비스가 커질 때 필요한 네트워크). Run from the repo root:
python3 scripts/svg_pairs/u11_l01.py   (add --svg-only to skip the lesson.md edit).

One light storyboard SVG per Page (8 Pages) that follows the 동아리 신청 사이트 story. Each is placed right after
the Page's opening paragraph. The Lesson had no `page_metadata`, so this script adds it (terms: [] + illustrations)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv


def at(x, y, inner):
    return f'<g transform="translate({x},{y})">{inner}</g>'


def role(x, y, w, h, title, sub, c, fs=19):
    return (box(x, y, w, h, c, PANEL, 12, sw=3) + text(x + w / 2, y + 30, title, fs, c, 700)
            + (text(x + w / 2, y + h - 16, sub, 14, MUTED) if sub else ""))


ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/01-*"))
OUT = LESSON / "assets" / "animations"


def wifi(x, y, c=GREEN):
    return "".join(f'<path d="M{x - r} {y} A{r} {r} 0 0 1 {x + r} {y}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"/>' for r in (14, 26, 38))


def bubble(x, y, s, c, w=None):
    return pill(x, y, s, c, 18, True, w)


def server(x, y, label=None, c=GREEN):
    s = (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
         + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3)))
    return s + (text(x, y + 62, label, 18, TXT, 700) if label else "")


def crowd(x0, y, n, c=BLUE, gap=26):
    return "".join(f'<circle cx="{x0 + i * gap}" cy="{y}" r="9" fill="{c}"/>' for i in range(n))


# 1 -------------------------------------------------------------------------------------------
def p1():
    a = Anim(4, dur(False))
    body = [laptop(120, 300, "내 컴퓨터"), phone(360, 300, "같은 와이파이 친구"), house(840, 280, "친구 집"), wifi(240, 245),
            a.vis(bubble(250, 175, "신청도 되고 목록도 잘 나와요", GREEN, 330), 1, 1),
            a.vis(bubble(360, 175, "친구도 열려요", GREEN, 190) + check(425, 285), 2, 2),
            mv(a, phone(0, 0), [(360, 300), (720, 300)], 3, 3, 4, 0.1, 0.8),
            a.vis(bubble(760, 175, "나는 안 열리는데?", RED, 230) + cross(780, 345), 4, 4),
            a.vis("".join(bubble(x, 440, s_, ORANGE, 220) for x, s_ in ((160, "사람이 몰리면?"), (480, "서버를 늘리면?"), (800, "관리 화면은?"))), 4, 4)]
    caps = ["동아리 행사 신청 사이트를 내 컴퓨터에서 만들었어요", "같은 와이파이의 친구에게도 잘 보여요", "그런데 친구가 집에 돌아가자…", "“나는 안 열리는데?” 다음 질문들이 기다려요"]
    return frame(a, "내 컴퓨터에서는 잘 되는데", "동아리 신청 사이트 이야기가 시작돼요", caps, "".join(body))


# 2 -------------------------------------------------------------------------------------------
def p2():
    a = Anim(4, dur(False))
    chips = [("IP 주소", BLUE), ("포트", GREEN), ("패킷", ORANGE), ("소켓", VIOLET)]
    body = [phone(100, 250, "친구"), line(170, 250, 560, 250, LINE, 4, "10 8"), laptop(620, 250, "내 컴퓨터"), role(750, 205, 170, 90, "서버 프로그램", "", GREEN, 16),
            a.vis(bubble(150, 150, "안 열려!", RED, 130), 1, 4),
            a.vis(pill(390, 205, "길 위에서 막혔나?", ORANGE, 17, False, 220) + pill(815, 165, "도착했는데 못 받았나?", ORANGE, 15, False, 210), 2, 4),
            a.vis("".join(cell(110 + i * 190, 340, 170, 46, t, c, 18) for i, (t, c) in enumerate(chips)), 3, 4),
            a.vis(bubble(480, 440, "중간 장치를 만나면: 무엇을 보고 어디로 넘길까?", GREEN, 700), 4, 4)]
    caps = ["친구가 “안 열려”라고 했어요", "그 말만으로는 어디가 문제인지 알 수 없어요", "기본편에서 배운 IP·포트·패킷·소켓이 단서가 돼요", "중간 장치를 만나면 이 질문을 떠올려요"]
    return frame(a, "“안 열려”만으로는 알 수 없어요", "기본편의 지식이 다시 쓰이는 순간이에요", caps, "".join(body))


# 3 -------------------------------------------------------------------------------------------
def p3():
    a = Anim(4, dur(False))
    home = box(40, 135, 330, 250, GREEN, PANEL, 16, dash=True, sw=3) + text(205, 168, "집 안(내부 네트워크)", 18, GREEN, 700)
    net = box(590, 135, 330, 250, BLUE, PANEL, 16, dash=True, sw=3) + text(755, 168, "인터넷", 18, BLUE, 700)
    body = [home, net, laptop(110, 280, "내 서버"), phone(300, 280, "안쪽 친구"), router(480, 280, "공유기"), phone(800, 280, "바깥 친구"),
            a.vis(line(180, 280, 255, 280, GREEN, 5) + bubble(205, 225, "같은 와이파이는 OK", GREEN, 220), 1, 4),
            a.vis(line(760, 280, 540, 280, ORANGE, 5, "8 6") + cross(520, 280) + bubble(750, 225, "사설 IP만으로는 못 찾아요", ORANGE, 290), 2, 4),
            a.vis(hl(430, 230, 100, 100, BLUE, 14) + bubble(480, 422, "경계에서 만나는 장치", BLUE, 260), 3, 4),
            a.vis(text(480, 462, "공유기가 있다는 사실만으로 원인을 정하지는 않아요", 17, MUTED, 700), 4, 4)]
    caps = ["같은 와이파이 안에서는 잘 연결돼요", "집 밖에서는 내 컴퓨터의 사설 주소를 찾을 수 없어요", "안과 밖의 경계에는 공유기가 있어요", "접속 실패에는 다른 원인도 있을 수 있어요"]
    return frame(a, "서비스와 인터넷 사이에는 무엇이 있을까", "집 안과 집 밖은 길이 달라요", caps, "".join(body))


# 4 -------------------------------------------------------------------------------------------
def p4():
    a = Anim(4, dur(False))
    col = lambda x, title, c: box(x, 135, 280, 270, c, PANEL, 14, sw=3) + text(x + 140, 168, title, 21, c, 700)
    inline = (col(30, "Inline", GREEN) + line(60, 290, 130, 290, LINE, 4) + box(130, 255, 60, 70, GREEN, GREEN, 8, sw=0) + line(190, 290, 260, 290, LINE, 4)
              + text(160, 360, "경로 위에서 처리", 16, MUTED, 700))
    outp = (col(340, "Out of path", ORANGE) + line(370, 290, 570, 290, LINE, 4) + line(470, 290, 470, 340, ORANGE, 3, "6 5") + eye(470, 355) + text(470, 395, "복사본을 관찰", 16, MUTED, 700))
    prox = (col(650, "Proxy", BLUE) + circle_node(690, 290, BLUE) + circle_node(880, 290, BLUE) + box(750, 255, 60, 70, BLUE, BLUE, 8, sw=0)
            + line(700, 290, 750, 290, BLUE, 4) + line(810, 290, 870, 290, BLUE, 4) + text(780, 360, "양쪽과 따로 연결", 16, MUTED, 700))
    body = [a.vis(inline, 1, 4), a.vis(outp, 2, 4), a.vis(prox, 3, 4),
            mv(a, packet(0, 0, GREEN), [(60, 290), (260, 290)], 1, 1, 1, 0.1, 0.8),
            a.vis(bubble(480, 450, "데이터가 지나가나? 복사본인가? 대신 연결하나?", ORANGE, 640), 4, 4)]
    caps = ["길에서 처리하는 Inline", "옆에서 복사본을 보는 Out of path", "대신 연결해 주는 Proxy", "이름보다 “데이터와 어떻게 만나는지”를 물어봐요"]
    return frame(a, "길에서 처리하고, 옆에서 보고, 대신 연결하고", "중간 장치의 세 가지 구조를 가볍게 만나 봐요", caps, "".join(body))


def circle_node(x, y, c):
    return f'<circle cx="{x}" cy="{y}" r="16" fill="{PANEL}" stroke="{c}" stroke-width="4"/>'


# 5 -------------------------------------------------------------------------------------------
def p5():
    a = Anim(4, dur(False))
    body = [line(190, 300, 420, 300, LINE, 3, "8 6"), line(540, 300, 800, 300, LINE, 3, "8 6"), laptop(110, 300, "내 컴퓨터"), router(480, 300, "공유기 (NAT)"), server(850, 280, "외부 사이트"),
            a.vis(arrow(180, 400, 285, GREEN, 5) + arrow(420, 180, 330, ORANGE, 5) + text(300, 255, "안에서 먼저 → 응답이 돌아와요", 16, GREEN, 700), 1, 2),
            a.vis(pill(480, 220, "주소와 포트를 바꿔 이어 줘요", BLUE, 17, True, 330), 2, 2),
            a.vis(arrow(780, 540, 285, RED, 5) + ask(480, 230) + bubble(480, 190, "밖에서 먼저 오면 어느 컴퓨터로?", RED, 380), 3, 4),
            a.vis(pill(480, 440, "포트 포워딩은 길 안내 규칙 하나일 뿐이에요", GREEN, 18, True, 560), 4, 4)]
    caps = ["안에서 먼저 시작한 접속은 응답이 돌아와요", "공유기는 주소와 포트를 바꿔 내부와 이어 줘요", "밖에서 먼저 들어오는 접속은 기준이 더 필요해요", "포트 포워딩 하나로 모든 문제가 풀리지는 않아요"]
    return frame(a, "밖으로 나가는 길, 밖에서 들어오는 길", "Unit 12에서 더 자세히 만나요", caps, "".join(body))


# 6 -------------------------------------------------------------------------------------------
def p6():
    a = Anim(4, dur(False))
    users = crowd(60, 170, 14, BLUE, 30)
    lb = lambda: box(400, 245, 160, 56, GREEN, PANEL, 10, sw=3) + text(480, 280, "대표 접점", 18, GREEN, 700)
    body = [users + text(480, 148, "신청 시작! 사람이 몰려요", 18, MUTED, 700),
            a.vis(server(480, 360, "서버 한 대", RED) + bubble(620, 340, "응답이 느려져요", RED, 210), 1, 1),
            a.vis("".join(server(x, 380) for x in (250, 480, 710)) + text(480, 450, "서버를 세 대로 늘렸어요", 18, GREEN, 700), 2, 2),
            a.vis("".join(server(x, 380) for x in (250, 480, 710)) + lb()
                  + "".join(line(480, 301, x, 340, GREEN, 4) for x in (250, 480, 710)), 3, 3),
            a.vis("".join(server(x, 380, None, GREEN if x != 480 else MUTED) for x in (250, 480, 710)) + lb() + cross(480, 330)
                  + line(480, 301, 250, 340, GREEN, 4) + line(480, 301, 710, 340, GREEN, 4) + bubble(480, 450, "응답 없는 서버는 빼고 보내요", ORANGE, 380), 4, 4)]
    caps = ["신청 시간이 되자 사람이 한꺼번에 몰렸어요", "서버를 세 대로 늘렸어요", "하나의 대표 접점이 요청을 나눠 줘요", "응답하지 않는 서버는 빼고 나눠요"]
    return frame(a, "신청자가 몰려 서버를 늘렸어요", "누가 요청을 나눠 줄까요?", caps, "".join(body))


# 7 -------------------------------------------------------------------------------------------
def p7():
    a = Anim(4, dur(False))
    stranger = lambda x: person(x, 280, None)
    panel = box(700, 190, 210, 190, VIOLET, PANEL, 12, sw=3) + text(805, 225, "관리 화면", 20, VIOLET, 700)
    body = [panel, a.vis(lock(805, 280, MUTED), 1, 1), a.vis(lock(805, 280, GREEN), 2, 4),
            a.vis("".join(stranger(x) for x in (80, 170)) + arrow(220, 690, 300, RED, 4) + text(450, 275, "아무나 열 수 있다면?", 17, RED, 700), 1, 1),
            a.vis(person(110, 280, "운영자") + line(180, 300, 690, 300, GREEN, 8, "14 8"), 2, 4),
            a.vis(text(430, 255, "운영자만 암호화 터널로", 17, GREEN, 700), 2, 2),
            a.vis(box(380, 225, 70, 150, ORANGE, PANEL, 8, sw=3) + text(415, 305, "방화벽", 17, ORANGE, 700) + stranger(260) + line(300, 395, 370, 395, RED, 4) + cross(375, 395), 3, 4),
            a.vis(bubble(480, 440, "VPN으로 연결돼도 모든 권한이 생기는 건 아니에요", GREEN, 560), 4, 4)]
    caps = ["관리 화면을 아무에게나 열어 두면 위험해요", "허용된 운영자만 터널(VPN)로 들어와요", "방화벽·IPS가 통신을 허용할지 정해요", "연결됐다고 모든 자원에 접근할 권한이 생기지는 않아요"]
    return frame(a, "어디서든 관리하되, 아무에게나 열지는 않기", "Unit 14에서 만나요", caps, "".join(body))


# 8 -------------------------------------------------------------------------------------------
def p8():
    a = Anim(4, dur(False))
    stops = [("Unit 11", "중간 장치의 위치", BLUE, 290), ("Unit 12", "공유기 안팎의 접속", GREEN, 450), ("Unit 13", "요청 나누기", ORANGE, 610), ("Unit 14", "원격 접속·보안", VIOLET, 770)]
    body = [phone(80, 300, "친구"), server(880, 300, "내 서비스"), line(130, 300, 835, 300, LINE, 5)]
    for k, (u, t, c, x) in enumerate(stops, 1):
        body.append(circle_node(x, 300, MUTED))
        body.append(a.vis(box(x - 74, 190, 148, 90, c, PANEL, 12, sw=3) + text(x, 222, u, 20, c, 700) + text(x, 256, t, 15, TXT, 600) + line(x, 280, x, 284, c, 3)
                          + f'<circle cx="{x}" cy="300" r="16" fill="{c}"/>', k, 4))
    body.append(a.vis(bubble(480, 400, "이름보다 위치와 역할이 보여요", GREEN, 420), 4, 4))
    caps = ["중간 장치는 길 위 어디에 있을까?", "공유기 안팎의 접속은 어떻게 이어질까?", "여러 서버에 요청을 어떻게 나눌까?", "원격 접속은 어떻게 허용하고 막을까?"]
    return frame(a, "이제 장비의 이름보다 위치와 역할이 보여요", "심화편은 이 질문들을 하나씩 풀어 가요", caps, "".join(body))


# (file, title, alt, caption, after_paragraph, fn)
ITEMS = [
    ("u11-intro-works-on-my-laptop", "내 컴퓨터에서는 잘 되는데",
     "내 컴퓨터와 같은 와이파이 친구에게는 신청 사이트가 잘 열리지만, 친구가 집으로 돌아가자 “나는 안 열리는데?”라는 말풍선이 나오고, 사람이 몰리면, 서버를 늘리면, 관리 화면은이라는 질문이 이어집니다.",
     "내 컴퓨터에서는 잘 되던 사이트가 집 밖에서는 열리지 않는 데서 이야기가 시작됩니다.", 0, p1),
    ("u11-intro-basics-come-back", "“안 열려”만으로는 알 수 없어요",
     "친구의 “안 열려”라는 말만으로는 길 위에서 막혔는지 도착했지만 서버 프로그램이 못 받았는지 알 수 없고, IP 주소, 포트, 패킷, 소켓이 살펴볼 단서가 되며 중간 장치를 만나면 무엇을 보고 어디로 넘기는지 묻습니다.",
     "기본편의 IP 주소, 포트, 패킷, 소켓은 비슷해 보이는 상황을 나누어 볼 단서입니다.", 0, p2),
    ("u11-intro-between-service-and-internet", "서비스와 인터넷 사이에는 무엇이 있을까",
     "집 안 네트워크에서는 내 서버와 안쪽 친구가 연결되지만 집 밖의 친구는 사설 IP 주소만으로 찾아올 수 없고, 안과 밖의 경계에 공유기가 있으며 공유기가 있다는 사실만으로 원인을 정하지는 않는다고 표시됩니다.",
     "같은 내부 네트워크와 인터넷을 건너는 상황은 경로가 다르며, 경계에서 자주 만나는 장치가 공유기입니다.", 0, p3),
    ("u11-intro-three-structures", "길에서 처리하고, 옆에서 보고, 대신 연결하고",
     "Inline은 데이터가 지나가는 경로 위의 장치에서 처리하고, Out of path는 경로 밖의 센서가 복사본을 관찰하며, Proxy는 양쪽과 따로 연결을 맺어 중계합니다. 이름보다 데이터와 어떻게 만나는지를 물어본다고 표시됩니다.",
     "Inline, Out of path, Proxy는 장치를 세 상자에 가두는 규칙이 아니라 데이터와 만나는 방식을 구별하는 질문입니다.", 0, p4),
    ("u11-intro-out-and-in", "밖으로 나가는 길, 밖에서 들어오는 길",
     "내 컴퓨터에서 먼저 시작한 접속은 공유기가 주소와 포트를 바꿔 이어 주어 응답이 돌아오지만, 밖에서 먼저 들어오는 접속은 어느 안쪽 컴퓨터로 보낼지 기준이 더 필요하고 포트 포워딩은 길 안내 규칙 하나일 뿐이라고 표시됩니다.",
     "가정용 IPv4 공유기는 보통 NAT를 쓰며, 포트 포워딩 하나로 모든 접속 문제가 해결되지는 않습니다.", 0, p5),
    ("u11-intro-scale-up", "신청자가 몰려 서버를 늘렸어요",
     "신청 시작 시간에 사람이 몰려 서버 한 대의 응답이 느려지자 서버를 세 대로 늘리고, 하나의 대표 접점이 요청을 나누어 주며, 응답하지 않는 서버는 빼고 보냅니다.",
     "서버를 늘렸다면 누가 요청을 나누고 장애가 나면 어느 경로로 보낼지가 새 질문이 됩니다. 요청을 나눠도 모든 지연이 사라지지는 않습니다.", 0, p6),
    ("u11-intro-manage-from-anywhere", "어디서든 관리하되, 아무에게나 열지는 않기",
     "관리 화면을 아무에게나 열어 두면 위험하므로 허용된 운영자만 암호화 터널로 들어오고, 방화벽과 IPS가 통신을 허용할지 정하며, VPN으로 연결되어도 모든 권한이 생기는 것은 아니라고 표시됩니다.",
     "원격 접속과 접근 통제는 함께 생각해야 하며, VPN 연결이 곧 모든 자원에 대한 권한은 아닙니다.", 0, p7),
    ("u11-intro-where-and-what", "이제 장비의 이름보다 위치와 역할이 보여요",
     "친구에서 내 서비스까지 이어진 길 위에 Unit 11의 중간 장치, Unit 12의 공유기 안팎 접속, Unit 13의 요청 나누기, Unit 14의 원격 접속과 보안이 차례로 나타나며 이름보다 위치와 역할이 보인다고 표시됩니다.",
     "표는 구축 순서가 아니라 심화편에서 어떤 질문을 어디서 다룰지 찾아보는 지도입니다.", 0, p8),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    if "page_metadata:" in fm:  # re-run: drop the previous generated block
        fm = fm[:fm.index("page_metadata:")]
    lines = ["page_metadata:"]
    for f, t, al, c, ap, _ in ITEMS:
        lines += ["- terms: []", "  illustrations:", f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
    fm = fm.rstrip("\n") + "\n" + "\n".join(lines) + "\n"
    Path(lesson_md).write_text(head + "---\n" + fm + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
    print("ok", len(ITEMS), "svgs")
