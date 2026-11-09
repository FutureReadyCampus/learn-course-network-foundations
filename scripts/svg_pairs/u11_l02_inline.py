#!/usr/bin/env python3
"""Unit 11 Lesson 2 (인라인 구조와 트래픽 처리). Run from the repo root:
python3 scripts/svg_pairs/u11_l02_inline.py   (--svg-only skips lesson.md edit).
One light 4-stage example SVG per Page (9). Deletes the stale wiki diagram source-03.svg."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, arrow, dur
from u7_l01 import mv
from u11_structures import srv, ends, road, gate, Y

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/restructured/02-*"))
OUT = LESSON / "assets" / "animations"


def A(): return Anim(4, dur(False))
def P(x, y, s, c, w=None, f=18, filled=False): return pill(x, y, s, c, f, filled, w)


# 1
def p1():
    a = A()
    body = [ends(), line(170, Y, 454, Y, LINE, 4, "10 8"), line(506, Y, 800, Y, LINE, 4, "10 8"), gate(480, Y),
            a.vis(P(480, 215, "서버로 가는 길목에 놓아요", ORANGE, 280), 1, 4),
            mv(a, packet(0, 0), [(190, Y), (770, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(P(480, 400, "모든 패킷이 장치를 지나가요", BLUE, 320), 2, 2),
            a.vis(P(480, 400, "그래서 직접 검사할 수 있어요", GREEN, 320), 3, 4)]
    caps = ["검사할 장치를 서버 가는 길목에 놓아요", "요청 패킷은 반드시 장치를 지나가요", "지나가니까 내용을 직접 살펴볼 수 있어요", "이렇게 길 위에 놓는 구조가 Inline이에요"]
    return frame(a, "Inline · 지나가는 길목에 놓기", "지나가는 길에 있어야 직접 검사해요", caps, "".join(body))


# 2
def p2():
    a = A()
    body = [ends(gate(480, Y)), line(170, Y, 454, Y, LINE, 4, "10 8"), line(506, Y, 800, Y, LINE, 4, "10 8"),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(P(480, 430, "Bypass · 내보내요", GREEN, 220, 18, True), 1, 1),
            mv(a, packet(0, 0, RED), [(190, Y), (440, Y)], 2, 2, 2, 0.1, 0.6),
            a.vis(cross(480, 365) + P(480, 430, "Drop · 여기서 멈춰요", RED, 240, 18, True), 2, 2),
            a.vis(P(300, 200, "허용 규칙", GREEN, 130) + P(660, 200, "차단 규칙", RED, 130), 3, 4),
            a.vis(P(480, 430, "규칙에 따라 둘 중 하나를 골라요", BLUE, 340), 4, 4)]
    caps = ["정상 패킷은 다음 장치로 넘겨요", "막아야 할 패킷은 여기서 멈춰요", "허용·차단은 규칙으로 정해요", "통과(Bypass)와 차단(Drop), 이 두 동작이 기본이에요"]
    return frame(a, "Packet의 통과와 차단", "넘길지, 멈출지 장치가 결정해요", caps, "".join(body))


# 3
def p3():
    a = A()
    names = [(110, "내 컴퓨터"), (330, "공유기"), (550, "라우터"), (770, "서버 네트워크")]
    body = [line(150, Y, 770, Y, LINE, 4, "10 8")]
    for i, (x, n) in enumerate(names):
        body.append(cell(x - 70, Y - 30, 140, 60, n, BLUE if i in (0, 3) else MUTED, 17))
    body += [mv(a, packet(0, 0), [(150, Y - 50), (770, Y - 50)], 1, 1, 2, 0.1, 0.9),
             a.vis(P(330, 215, "여기도 길목", MUTED, 140) + P(550, 215, "여기도 길목", MUTED, 140), 2, 4),
             a.vis(hl_(550), 3, 4), a.vis(P(550, 400, "검사 장치를 놓을 자리는?", ORANGE, 280), 3, 4),
             a.vis(P(480, 448, "패킷이 반드시 지나는 곳이 Inline 자리예요", GREEN, 460), 4, 4)]
    caps = ["데이터는 여러 장치를 차례로 지나가요", "어느 장치나 길목이 될 수 있어요", "검사 장치를 놓을 자리를 골라요", "지도에서 지나는 곳을 찾는 일이에요"]
    return frame(a, "망 구성에서 위치 찾기", "길목이 어디인지 지도에서 확인해요", caps, "".join(body))


def hl_(x): return box(x - 76, Y - 36, 152, 72, ORANGE, "none", 10, sw=4)


# 4
def p4():
    a = A()
    dev = box(380, Y - 55, 200, 110, GREEN, PANEL, 14, sw=3) + text(480, Y + 8, "장치", 22, GREEN, 700)
    body = [text(110, Y - 60, "내부망", 18, MUTED, 700), laptop(110, Y, ""), line(170, Y, 380, Y, LINE, 4), dev,
            line(580, Y, 790, Y, LINE, 4), text(850, Y - 60, "인터넷", 18, MUTED, 700), srv(850, Y),
            a.vis(P(380, Y, "A", BLUE, 44, 20, True) + P(580, Y, "B", ORANGE, 44, 20, True), 2, 4),
            a.vis(P(380, 215, "안쪽 인터페이스", BLUE, 180, 16) + P(580, 215, "바깥쪽 인터페이스", ORANGE, 190, 16), 2, 4),
            mv(a, packet(0, 0), [(200, Y), (760, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(P(480, 410, "A로 들어와 B로 나가요", GREEN, 260), 3, 3),
            a.vis(P(480, 410, "포트 하나하나가 인터페이스예요", GREEN, 330), 4, 4)]
    caps = ["내부망과 인터넷 사이에 장치를 놓아요", "각 포트를 인터페이스라고 불러요", "나가는 요청은 A로 들어와 B로 나가요", "A·B로 방향과 안팎을 구분해요"]
    return frame(a, "Interface와 안쪽·바깥쪽", "포트마다 이름을 붙여 방향을 나눠요", caps, "".join(body))


# 5
def p5():
    a = A()
    pcb = box(300, 140, 360, 250, GREEN, PANEL, 16, sw=3) + text(480, 175, "범용 컴퓨터", 20, GREEN, 700)
    body = [pcb,
            a.vis(cell(330, 300, 130, 60, "NIC 1", BLUE, 20) + cell(500, 300, 130, 60, "NIC 2", ORANGE, 20), 1, 4),
            a.vis(cell(330, 200, 300, 60, "라우팅 소프트웨어", VIOLET, 20), 2, 4),
            a.vis(P(480, 440, "드라이버가 NIC와 소프트웨어를 이어 줘요", BLUE, 400), 3, 3),
            a.vis(P(480, 440, "NIC가 둘이면 장치처럼 일해요", GREEN, 320), 4, 4),
            a.vis(line(395, 300, 395, 260, BLUE, 4) + line(565, 300, 565, 260, ORANGE, 4), 3, 4)]
    caps = ["컴퓨터에 네트워크 카드(NIC)가 둘 꽂혀 있어요", "그 위에서 라우팅 소프트웨어가 돌아가요", "드라이버가 둘 사이를 이어 줘요", "그래서 컴퓨터도 네트워크 장치가 돼요"]
    return frame(a, "커널·드라이버의 구현", "NIC 둘 + 소프트웨어면 장치 모양이 돼요", caps, "".join(body))


# 6
def p6():
    a = A()
    dev = box(380, Y - 55, 200, 110, GREEN, PANEL, 14, sw=3) + text(480, Y + 8, "분류장", 22, GREEN, 700)
    body = [laptop(110, Y, ""), srv(850, Y), line(170, Y - 20, 380, Y - 20, LINE, 3), line(580, Y - 20, 790, Y - 20, LINE, 3), line(170, Y + 25, 380, Y + 25, LINE, 3), line(580, Y + 25, 790, Y + 25, LINE, 3), dev,
            mv(a, parcel(0, 0), [(190, Y - 20), (770, Y - 20)], 1, 1, 2, 0.1, 0.9),
            a.vis(P(480, 215, "요청: A → B", ORANGE, 170), 2, 4),
            mv(a, packet(0, 0, GREEN), [(770, Y + 25), (190, Y + 25)], 3, 3, 4, 0.1, 0.9),
            a.vis(P(480, 400, "응답: B → A", GREEN, 170), 3, 4),
            a.vis(P(480, 448, "택배 분류장처럼 들어온 쪽의 반대로 보내요", BLUE, 440), 4, 4)]
    caps = ["요청은 A로 들어와요", "허용되면 B쪽으로 넘겨 보내요", "응답은 반대 방향으로 돌아와요", "분류장에서 상자를 넘기는 모습이에요"]
    return frame(a, "들어온 패킷을 넘겨 보내기", "A로 들어와 B로, 응답은 반대로", caps, "".join(body))


# 7
def p7():
    a = A()
    body = [srv(850, Y), box(430, Y - 40, 100, 80, ORANGE, PANEL, 10, sw=3) + text(480, Y + 8, "장치", 18, ORANGE, 700), line(530, Y, 800, Y, LINE, 4, "10 8"),
            a.vis("".join(packet(120 + i * 50, Y, BLUE) for i in range(5)) + line(160, Y, 425, Y, LINE, 4, "10 8"), 1, 4),
            a.vis(P(480, 215, "요청이 갑자기 늘었어요", BLUE, 250), 2, 4),
            a.vis(P(300, 400, "줄이 길어져요", ORANGE, 150) + cross(255, 335), 3, 4),
            a.vis(P(660, 400, "서버만 키워도 소용없어요", RED, 280), 4, 4)]
    caps = ["평소엔 패킷이 술술 지나가요", "행사 신청으로 요청이 몰렸어요", "장치가 처리 못 하면 줄이 길어져요", "길목 장치의 속도가 전체 성능을 정해요"]
    return frame(a, "처리 속도와 전체 성능", "길목이 좁으면 전체가 느려져요", caps, "".join(body))


# 8
def p8():
    a = A()
    rows = [("주소·포트만 보기", "빠르고 가벼워요", GREEN), ("내용까지 보기", "더 많이 걸려요", ORANGE)]
    body = [packet(480, 150, BLUE)]
    for i, (l, r, c) in enumerate(rows):
        y = 220 + i * 90
        body.append(a.vis(cell(180, y, 280, 60, l, c, 20) + cell(500, y, 280, 60, r, c, 20), i + 1, 4))
    body += [a.vis(P(480, 150, "헤더: 주소 · 포트", BLUE, 220, 16), 1, 1),
             a.vis(P(480, 420, "규칙이 단순할수록 빨라요", GREEN, 280), 3, 3),
             a.vis(P(480, 420, "그래서 전용 하드웨어도 써요", VIOLET, 300), 4, 4)]
    caps = ["패킷 겉의 헤더에는 주소와 포트가 있어요", "헤더만 보는 규칙은 가벼워요", "내용까지 보면 더 오래 걸려요", "고성능이 필요하면 구현을 달리해요"]
    return frame(a, "필터링과 고성능 구현", "무엇을 볼지에 따라 속도가 달라요", caps, "".join(body))


# 9
def p9():
    a = A()
    body = [a.vis(cell(110, 190, 320, 90, "전용 장비 상자", BLUE, 22) + text(270, 310, "하드웨어로 만든 장치", 16, MUTED), 1, 4),
            a.vis(cell(530, 190, 320, 90, "범용 컴퓨터 + 소프트웨어", ORANGE, 20) + text(690, 310, "NIC 여러 개에 라우팅 프로그램", 16, MUTED), 2, 4),
            a.vis(arrow(270, 270, 340, BLUE) if False else line(270, 330, 270, 375, BLUE, 4) + line(690, 330, 690, 375, ORANGE, 4) + line(270, 375, 690, 375, GREEN, 4), 3, 4),
            a.vis(P(480, 415, "둘 다 패킷을 전달해요", GREEN, 260, 18, True), 3, 4),
            a.vis(P(480, 150, "역할은 상자 모양으로 정해지지 않아요", VIOLET, 400), 4, 4)]
    caps = ["전용 장비 상자가 먼저 떠올라요", "일반 컴퓨터에 소프트웨어를 올려도 돼요", "둘 다 패킷을 받아 넘겨요", "모양보다 하는 일이 장치를 정해요"]
    return frame(a, "소프트웨어·하드웨어의 구현", "상자든 컴퓨터든 역할은 같아요", caps, "".join(body))


ITEMS = [
    ("u11-inline-path", 1, "Inline · 지나가는 길목에 놓기", "서버로 가는 길목에 놓인 장치를 모든 요청 패킷이 지나가며 검사받는 모습입니다.", "Inline 장치는 패킷이 지나가는 길목에 놓입니다.", p1),
    ("u11-inline-bypass-drop", 2, "Packet의 통과와 차단", "허용된 패킷은 Bypass로 내보내고 차단 규칙에 맞는 패킷은 Drop으로 멈추는 모습입니다.", "장치는 패킷을 통과시키거나 멈춥니다.", p2),
    ("u11-inline-position", 3, "망 구성에서 위치 찾기", "내 컴퓨터에서 서버까지 여러 장치가 이어진 지도에서 검사 장치를 놓을 길목을 고르는 모습입니다.", "지도에서 패킷이 반드시 지나는 곳을 찾습니다.", p3),
    ("u11-inline-interface", 4, "Interface와 안쪽·바깥쪽", "내부망 쪽 A 인터페이스로 들어온 패킷이 인터넷 쪽 B 인터페이스로 나가는 모습입니다.", "포트를 인터페이스로 부르며 안쪽과 바깥쪽을 나눕니다.", p4),
    ("u11-inline-nic", 5, "커널·드라이버의 구현", "NIC 두 개와 라우팅 소프트웨어가 있는 범용 컴퓨터가 드라이버로 이어져 네트워크 장치처럼 동작하는 모습입니다.", "NIC 여러 개와 소프트웨어로 장치를 구현합니다.", p5),
    ("u11-inline-forward", 6, "들어온 패킷을 넘겨 보내기", "분류장처럼 A로 들어온 요청을 B로 넘기고 응답은 반대 방향으로 돌려 보내는 모습입니다.", "요청은 A에서 B로, 응답은 B에서 A로 전달됩니다.", p6),
    ("u11-inline-speed", 7, "처리 속도와 전체 성능", "요청이 몰리자 길목 장치 앞에 패킷이 줄지어 서고 서버만 키워도 소용없는 모습입니다.", "길목 장치의 처리 속도가 전체 성능을 좌우합니다.", p7),
    ("u11-inline-filter", 8, "필터링과 고성능 구현", "주소와 포트만 보는 규칙은 빠르고 내용까지 보면 더 오래 걸리는 차이를 보여 줍니다.", "무엇을 보느냐에 따라 처리 속도가 달라집니다.", p8),
    ("u11-inline-hw-sw", 9, "소프트웨어·하드웨어의 구현", "전용 장비 상자와 범용 컴퓨터에 소프트웨어를 올린 경우 모두 패킷을 전달하는 모습입니다.", "장치의 역할은 상자 모양이 아니라 하는 일로 정해집니다.", p9),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-03\.svg\n(?:    .*\n)+", "", s, count=1)
    for f, n, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in s:
            continue
        pid = f"advanced-source-03-page-{n:02d}"
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_r, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        (LESSON / "assets" / "diagrams" / "source-03.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
