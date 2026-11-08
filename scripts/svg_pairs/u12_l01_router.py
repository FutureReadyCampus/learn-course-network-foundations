#!/usr/bin/env python3
"""Unit 12 Lesson 1 (사설 주소·공인 주소와 공유기): light example SVG per Page (9). Run from repo root:
python3 scripts/svg_pairs/u12_l01_router.py   (--svg-only skips lesson.md edit / stale diagram removal)."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, dur
from u7_l01 import mv
from u11_structures import srv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-router-and-nat/lessons/restructured/01-*"))
OUT = LESSON / "assets" / "animations"
Y = 300


def net(x, y, w, h, label, c):
    return box(x, y, w, h, c, PANEL, 16, dash=True, sw=3) + text(x + w / 2, y + 30, label, 18, c, 700)


def rt(x, y, label="공유기"):
    return router(x, y, label)


def cloud(x, y, label="인터넷"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
            + text(x, y + 7, label, 20, BLUE, 700))


# 1 ---
def p1():
    a = Anim(4, dur(False))
    body = [phone(100, 250, "휴대폰"), laptop(100, 390, "노트북"), rt(480, Y), cloud(830, Y),
            a.vis(line(150, 250, 450, Y, GREEN, 4) + line(150, 380, 450, Y, GREEN, 4) + pill(250, 195, "집 안 네트워크(LAN)", GREEN, 17, True, 230), 2, 4),
            a.vis(line(510, Y, 760, Y, BLUE, 4) + pill(640, 255, "바깥(WAN) → ISP", BLUE, 17, True, 180), 3, 4),
            a.vis(pill(480, 440, "기기마다 회선 X, 공유기 하나로 함께", ORANGE, 18, False, 380), 4, 4)]
    caps = ["휴대폰과 노트북이 같은 인터넷을 써요", "둘 다 공유기 안쪽(LAN)에 연결돼요", "공유기 바깥(WAN)이 인터넷 회사로 이어져요", "공유기는 인터넷 출입구 역할을 해요"]
    return frame(a, "공유기는 인터넷 출입구", "여러 기기가 한 출입구를 함께 써요", caps, "".join(body))


# 2 ---
def p2():
    a = Anim(4, dur(False))
    body = [a.vis(house(200, 270, "우리 집") + pill(200, 380, "노트북 192.168.0.25", BLUE, 16, False, 230), 1, 4),
            a.vis(house(760, 270, "옆 동네 집") + pill(760, 380, "노트북 192.168.0.25", BLUE, 16, False, 230), 2, 4),
            a.vis(text(480, 300, "같은 번호!", 22, ORANGE, 700), 3, 4),
            a.vis(pill(480, 190, "각자 자기 집 안에서만 의미가 있어요", GREEN, 18, True, 400), 3, 3),
            a.vis(cloud(480, 200, "인터넷") + pill(480, 440, "인터넷에서는 공인 IP로 구분해요", BLUE, 18, True, 360), 4, 4)]
    caps = ["우리 집 노트북은 192.168.0.25예요", "옆 동네 집도 같은 번호를 써도 괜찮아요", "사설 주소는 집 안에서만 통해요", "인터넷에서는 공인 주소가 필요해요"]
    return frame(a, "사설 IP와 공인 IP", "아파트 호수와 도로명 주소 같아요", caps, "".join(body))


# 3 ---
def p3():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "노트북"), rt(480, Y), srv(850, Y), line(170, Y, 450, Y, LINE, 4, "10 8"), line(510, Y, 800, Y, LINE, 4, "10 8"),
            a.vis(pill(300, 235, "출발지 192.168.0.25", BLUE, 15, True, 200), 1, 2),
            mv(a, packet(0, 0), [(190, Y), (440, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(660, 235, "출발지 203.0.113.7", ORANGE, 15, True, 200) + pill(480, 400, "공유기가 출발지 주소를 바꿔요", ORANGE, 18, False, 320), 2, 3),
            mv(a, packet(0, 0, ORANGE), [(520, Y), (790, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 190, "응답은 통신 기록을 보고 돌아와요", GREEN, 18, True, 340), 3, 4),
            mv(a, packet(0, 0, GREEN), [(790, Y), (200, Y)], 3, 3, 3, 0.05, 0.95),
            a.vis(check(110, 225), 4, 4)]
    caps = ["노트북의 요청은 사설 주소로 출발해요", "공유기가 바깥 주소로 바꿔 내보내요", "응답은 변환 기록을 보고 돌아와요", "노트북까지 응답이 도착해요"]
    return frame(a, "NAT가 주소를 바꿔 줘요", "요청은 바꿔 보내고 응답은 기록대로 돌려줘요", caps, "".join(body))


# 4 ---
def p4():
    a = Anim(4, dur(False))
    body = [rt(480, Y), cloud(800, Y, "바깥"), laptop(150, Y, "내 기기"),
            a.vis(pill(480, 190, "NAT = 주소 바꾸기", ORANGE, 19, True, 240), 1, 4),
            a.vis(mv(a, packet(0, 0, RED), [(740, Y), (560, Y)], 2, 2, 3, 0.1, 0.9) + cross(530, Y - 50), 2, 3),
            a.vis(pill(480, 400, "바깥에서 먼저 온 패킷은 기록과 안 맞아요", RED, 17, False, 400), 2, 2),
            a.vis(box(400, 230, 160, 140, VIOLET, "none", 14, dash=True, sw=3) + pill(480, 410, "방화벽 = 규칙으로 허용·차단", VIOLET, 18, True, 340), 3, 3),
            a.vis(pill(480, 410, "NAT가 있어도 방화벽은 따로 필요해요", GREEN, 18, True, 400), 4, 4)]
    caps = ["NAT의 일은 주소를 바꾸는 거예요", "기록에 없는 바깥 패킷은 전달되지 않아요", "방화벽은 규칙으로 허용·차단해요", "둘은 목적이 달라서 따로 봐요"]
    return frame(a, "NAT ≠ 방화벽", "막히는 효과가 있어도 보안 장치는 아니에요", caps, "".join(body))


# 5 ---
def p5():
    a = Anim(4, dur(False))
    body = [rt(480, 260, "공유기"),
            a.vis(cell(130, 150, 300, 70, "① 바깥 주소·포트는?", ORANGE, 20), 1, 4),
            a.vis(cell(530, 150, 300, 70, "② 들여보낼 조건은?", BLUE, 20), 2, 4),
            a.vis(text(280, 255, "새 통신마다 포트를 다르게?", 16, MUTED), 3, 4),
            a.vis(text(680, 255, "먼저 말 건 상대만 허용?", 16, MUTED), 3, 4),
            a.vis(pill(480, 400, "이름 외우기 X · 두 질문으로 구분", GREEN, 19, True, 380), 4, 4)]
    caps = ["NAT의 동작에는 두 질문이 있어요", "첫째, 바깥에 어떤 주소·포트로 보일까?", "둘째, 바깥 패킷은 어떤 조건에 들여보낼까?", "유형 이름보다 이 두 질문을 기억해요"]
    return frame(a, "NAT의 동작은 한 가지가 아니에요", "두 질문으로 나눠서 봐요", caps, "".join(body))


# 6 ---
def p6():
    a = Anim(4, dur(False))
    body = [a.vis(net(40, 150, 320, 250, "LAN · 공유기 안쪽", GREEN) + phone(110, 290) + laptop(250, 290), 1, 4), rt(480, 290, "공유기"),
            a.vis(net(600, 150, 320, 250, "WAN · 공유기 바깥쪽", BLUE) + text(760, 290, "ISP 연결", 22, BLUE, 700), 2, 4),
            a.vis(pill(200, 430, "사설 주소 사용", GREEN, 17, True, 170), 3, 4),
            a.vis(pill(760, 430, "ISP가 준 주소", BLUE, 17, True, 170), 3, 4),
            a.vis(pill(480, 440, "이 주소는 어느 쪽 주소일까?", ORANGE, 18, False, 300), 4, 4)]
    caps = ["LAN은 공유기 안쪽의 집 네트워크예요", "WAN은 인터넷 회사 쪽 연결이에요", "안쪽은 사설, 바깥쪽은 ISP가 준 주소예요", "그림을 볼 때 어느 쪽 주소인지 먼저 물어요"]
    return frame(a, "안쪽(LAN)과 바깥쪽(WAN)", "같은 공유기, 서로 다른 두 네트워크예요", caps, "".join(body))


# 7 ---
def p7():
    a = Anim(4, dur(False))
    rows = [("10.0.0.0/8", "예 10.4.2.8", ORANGE), ("172.16.0.0/12", "예 172.20.1.9", BLUE), ("192.168.0.0/16", "예 192.168.0.25", GREEN)]
    body = []
    for i, (r, e, c) in enumerate(rows):
        y = 140 + i * 90
        body.append(a.vis(cell(150, y, 330, 64, r, c, 24) + cell(500, y, 310, 64, e, c, 20), i + 1, 4))
    body.append(a.vis(pill(480, 430, "172로 시작해도 16~31만 사설이에요", RED, 18, True, 400), 4, 4))
    caps = ["사설 주소 첫째 범위는 10.x.x.x예요", "둘째는 172.16 ~ 172.31이에요", "셋째는 192.168.x.x예요", "첫 숫자만 보고 판단하지 않아요"]
    return frame(a, "사설 IPv4는 세 범위", "공유기 화면에서 자주 보여요", caps, "".join(body))


# 8 ---
def p8():
    a = Anim(4, dur(False))
    body = [house(110, 270, "우리 집"), rt(260, Y, "집 공유기"), box(400, 240, 150, 120, VIOLET, PANEL, 14, sw=3) + text(475, 285, "ISP NAT", 20, VIOLET, 700) + text(475, 320, "CGNAT", 16, MUTED), cloud(790, Y),
            line(300, Y, 400, Y, LINE, 4, "8 6"), line(550, Y, 720, Y, LINE, 4, "8 6"),
            a.vis(pill(260, 215, "① 집 공유기 NAT", ORANGE, 16, True, 170), 2, 4),
            a.vis(pill(475, 195, "② 통신사 NAT", VIOLET, 16, True, 160), 3, 4),
            a.vis(pill(300, 400, "WAN 주소 100.64.x.x", BLUE, 16, False, 210), 1, 4),
            a.vis(pill(600, 440, "공유기 포트 포워딩만으론 안 될 수 있어요", RED, 17, False, 420), 4, 4)]
    caps = ["집 공유기 뒤에 통신사 장비가 있을 수 있어요", "먼저 집 공유기가 한 번 바꾸고", "통신사 NAT가 또 한 번 바꿔요", "그래서 바깥 접속이 어려울 수 있어요"]
    return frame(a, "주소를 한 번 더 바꾸는 CGNAT", "건물 출입구를 여러 집이 함께 쓰는 것과 비슷해요", caps, "".join(body))


# 9 ---
def p9():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "192.168.0.25"), rt(430, Y), srv(820, Y), line(170, Y, 400, Y, LINE, 4, "10 8"), line(460, Y, 770, Y, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(190, Y), (390, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(430, 215, "NAT", ORANGE, 19, True, 90), 2, 3),
            mv(a, packet(0, 0, ORANGE), [(470, Y), (760, Y)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, GREEN), [(760, Y), (190, Y)], 3, 3, 3, 0.05, 0.95),
            a.vis(pill(480, 160, "사설 IP · 공인 IP · 공유기 · NAT", GREEN, 18, False, 430) + check(110, 225), 4, 4)]
    caps = ["노트북이 사설 IP로 요청을 보내요", "공유기가 NAT로 주소를 바꿔 내보내요", "응답은 통신 기록을 따라 돌아와요", "네 가지 용어를 구분해서 기억해요"]
    return frame(a, "공유기와 NAT 한눈에 정리", "사설 주소가 바깥 통신에 쓰이는 길이에요", caps, "".join(body))


ITEMS = [
    ("u12-router-door", "advanced-source-10-page-01", "공유기는 인터넷 출입구", "휴대폰과 노트북이 집 안 네트워크(LAN)에서 공유기를 거쳐 바깥(WAN)의 인터넷 회사로 이어지는 모습입니다.", "여러 기기가 공유기 하나를 통해 인터넷을 함께 씁니다.", p1),
    ("u12-router-public-private", "advanced-source-10-page-02", "사설 IP와 공인 IP", "서로 다른 두 집에서 같은 사설 주소 192.168.0.25를 써도 괜찮고, 인터넷에서는 공인 주소로 구분하는 그림입니다.", "사설 주소는 각 집 안에서만 의미가 있습니다.", p2),
    ("u12-router-nat", "advanced-source-10-page-03", "NAT가 주소를 바꿔 줘요", "노트북의 요청 출발지 주소를 공유기가 바깥 주소로 바꾸고, 돌아온 응답을 기록에 따라 노트북으로 전달하는 모습입니다.", "공유기는 나갈 때 주소를 바꾸고 응답은 기록대로 돌려줍니다.", p3),
    ("u12-router-firewall", "advanced-source-10-page-04", "NAT ≠ 방화벽", "기록에 없는 바깥 패킷이 전달되지 않는 효과가 있지만 NAT는 주소 변환이고 방화벽은 규칙에 따른 허용·차단임을 구분하는 그림입니다.", "NAT와 방화벽은 목적이 다릅니다.", p4),
    ("u12-router-nat-types", "advanced-source-10-page-05", "NAT의 동작은 한 가지가 아니에요", "바깥 주소·포트를 어떻게 정하는지, 외부 패킷을 어떤 조건에 들여보내는지 두 질문으로 NAT를 나누는 그림입니다.", "NAT 동작은 두 질문으로 구분합니다.", p5),
    ("u12-router-lan-wan", "advanced-source-10-page-06", "안쪽(LAN)과 바깥쪽(WAN)", "공유기 안쪽 LAN에는 사설 주소의 기기가, 바깥쪽 WAN에는 인터넷 회사가 준 주소가 있는 모습입니다.", "LAN은 공유기 안쪽, WAN은 바깥쪽 연결입니다.", p6),
    ("u12-router-private-ranges", "advanced-source-10-page-07", "사설 IPv4는 세 범위", "10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 세 사설 범위와 예시 주소를 보여 주는 표입니다.", "자주 보는 사설 대역은 세 가지입니다.", p7),
    ("u12-router-cgnat", "advanced-source-10-page-08", "주소를 한 번 더 바꾸는 CGNAT", "집 공유기의 NAT 뒤에 통신사 NAT가 한 번 더 있어 포트 포워딩만으로 외부 접속이 안 될 수 있음을 보여 줍니다.", "통신사 NAT가 있으면 주소 변환이 두 번 일어날 수 있습니다.", p8),
    ("u12-router-summary", "advanced-source-10-page-09", "공유기와 NAT 한눈에 정리", "사설 주소의 노트북 요청이 공유기와 NAT를 거쳐 웹사이트로 가고 응답이 같은 기록을 따라 돌아오는 정리 그림입니다.", "사설 IP, 공인 IP, 공유기, NAT의 역할을 구분합니다.", p9),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-10\.svg\n(?:    .*\n)+", "", s, count=1)
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
        (LESSON / "assets" / "diagrams" / "source-10.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
