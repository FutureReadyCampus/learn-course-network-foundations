#!/usr/bin/env python3
"""Unit 12 Lesson 3 (NAT의 매핑과 수신 허용 방식): one 4-step SVG per Page (7). Run from repo root:
python3 scripts/svg_pairs/u12_l03_mapping.py   (--svg-only skips lesson.md edit / stale diagram removal).

Step arc on every page: ① 상황/질문 → ② 동작(움직이는 패킷) → ③ 결과(✓/✗, 대비) → ④ 기억할 점 한 줄.
Each step adds exactly one thing (orange highlight marks it). Running example = the lesson's own values:
A 192.168.0.10:3000 → NAT 바깥 203.0.113.8:42000, 상대 15.15.15.15:5555 (다른 포트 :7777, 다른 IP 9.9.9.9:40000)."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur
from u7_l01 import mv
from u11_structures import srv
from u12_l01_router import rt

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-router-and-nat/lessons/restructured/03-*"))
OUT = LESSON / "assets" / "animations"
IN, EXT, R1 = "192.168.0.10:3000", "203.0.113.8:42000", "15.15.15.15:5555"


def peers(y=300):
    """A ─ NAT A ······ NAT B ─ B (fixed positions on every peer page)."""
    return (laptop(80, y, "A") + rt(230, y, "A의 공유기") + rt(730, y, "B의 공유기") + laptop(880, y, "B")
            + line(130, y, 200, y, LINE, 4) + line(260, y, 700, y, LINE, 4, "10 8") + line(760, y, 830, y, LINE, 4))


def panel(x, title, c):
    return box(x, 130, 420, 290, c, PANEL, 16, dash=True, sw=3) + text(x + 210, 162, title, 19, c, 700)


# 1 ---
def p1():
    a = Anim(4, dur(False))
    body = [peers(),
            a.vis(pill(480, 190, "A ↔ B 직접 주고받고 싶어요", BLUE, 18, False, 300), 1, 4),
            mv(a, packet(0, 0, RED), [(700, 300), (275, 300)], 2, 2, 2, 0.1, 0.85),
            a.vis(hl(200, 270, 60, 60, ORANGE, 30), 3, 3),
            a.vis(cross(230, 240) + pill(230, 395, "어느 기기로?", ORANGE, 17, True, 150), 3, 4),
            a.vis(pill(560, 420, "매핑 + 허용 조건이 둘 다 맞아야", GREEN, 18, True, 340), 4, 4)]
    caps = ["A와 B는 각자 공유기 뒤에 있어요", "B가 먼저 A의 공유기로 패킷을 보내요", "A의 공유기는 어느 기기로 보낼지 몰라 막혀요", "직접 통신엔 매핑과 허용 조건이 모두 필요해요"]
    return frame(a, "NAT 뒤의 피어끼리 만나기", "모르는 사람이 경비실에 찾아온 상황이에요", caps, "".join(body))


# 2 ---
def p2():
    a = Anim(4, dur(False))
    body = [panel(40, "매핑 · 어떤 바깥 주소로?", BLUE), panel(500, "필터링 · 누구 걸 받나?", VIOLET),
            a.vis(cell(70, 200, 360, 44, f"안쪽 {IN}", BLUE, 16), 1, 4),
            a.vis(cell(530, 200, 360, 44, f"바깥 {EXT}", VIOLET, 16), 1, 4),
            a.vis(cell(70, 300, 360, 44, f"→ 바깥 {EXT}", BLUE, 16), 2, 4), a.vis(hl(70, 300, 360, 44), 2, 2),
            mv(a, packet(0, 0), [(250, 252), (250, 292)], 2, 2, 2, 0.1, 0.8),
            a.vis(cell(530, 300, 360, 44, f"{R1}에서 옴", GREEN, 16) + check(870, 370), 3, 4), a.vis(hl(530, 300, 360, 44), 3, 3),
            a.vis(pill(480, 450, "두 질문은 따로 봐요", GREEN, 19, True, 260), 4, 4)]
    caps = ["NAT에는 두 가지 질문이 있어요", "매핑: 안쪽 통신을 바깥 주소·포트에 짝지어요", "필터링: 들어온 패킷의 보낸 사람을 확인해요", "한 이름으로 뭉뚱그리지 말고 따로 봐요"]
    return frame(a, "매핑과 필터링은 다른 질문", "나가는 문 번호 정하기 vs 손님 확인하기", caps, "".join(body))


# 3 ---
def p3():
    a = Anim(4, dur(False))
    body = [panel(40, "목적지 독립 매핑 (EIM)", GREEN), panel(500, "목적지 종속 매핑", ORANGE)]
    for x in (70, 530):
        body += [a.vis(cell(x, 200, 360, 40, f"상대 {R1} → :42000", MUTED, 15), 1, 4),
                 a.vis(cell(x, 260, 360, 40, "상대 9.9.9.9:40000 (새 상대)", BLUE, 15), 2, 4), a.vis(hl(x, 260, 360, 40), 2, 2)]
    body += [mv(a, packet(0, 0), [(250, 330), (250, 360)], 2, 2, 2, 0.1, 0.8),
             mv(a, packet(0, 0), [(710, 330), (710, 360)], 2, 2, 2, 0.1, 0.8),
             a.vis(cell(70, 320, 360, 44, ":42000 그대로 재사용", GREEN, 17), 3, 4), a.vis(hl(70, 320, 360, 44), 3, 3),
             a.vis(cell(530, 320, 360, 44, "다른 바깥 포트 배정", ORANGE, 17), 3, 4), a.vis(hl(530, 320, 360, 44), 3, 3),
             a.vis(pill(480, 450, "같은 바깥 주소를 계속 쓰나?", GREEN, 19, True, 320), 4, 4)]
    caps = ["A는 15.15.15.15와 통신하며 :42000을 받았어요", "같은 A가 이번엔 9.9.9.9와 통신해요", "왼쪽은 :42000을 다시 쓰고, 오른쪽은 새 포트를 써요", "매핑은 상대가 바뀌어도 같은지 물어요"]
    return frame(a, "매핑은 상대에 따라 달라질 수 있어요", "단골 창구 번호 vs 손님마다 새 창구", caps, "".join(body))


# 4 ---
def p4():
    a = Anim(4, dur(False))
    cols = [("EIF · 누구든", GREEN), ("ADF · 같은 IP", BLUE), ("APDF · 같은 IP·포트", VIOLET)]
    body = [a.vis(pill(480, 150, f"A가 먼저 {R1}로 보냈어요", MUTED, 17, False, 380), 1, 4)]
    for i, (n, c) in enumerate(cols):
        body.append(cell(60 + i * 290, 190, 260, 50, n, c, 18))
    body += [a.vis(cell(330, 270, 300, 44, "15.15.15.15:7777 도착", ORANGE, 17), 2, 4), a.vis(hl(330, 270, 300, 44), 2, 2),
             mv(a, packet(0, 0, ORANGE), [(480, 330), (480, 360)], 2, 2, 2, 0.1, 0.8),
             a.vis(check(190, 380) + check(480, 380) + cross(770, 380), 3, 4), a.vis(hl(640, 190, 260, 50), 3, 3),
             a.vis(pill(480, 445, "누구든 → 같은 IP → 같은 IP·포트", GREEN, 18, True, 380), 4, 4)]
    caps = ["A는 15.15.15.15:5555와 먼저 통신했어요", "같은 IP지만 다른 포트 7777에서 패킷이 와요", "포트까지 보는 APDF만 막을 수 있어요", "비교가 자세할수록 받는 범위가 좁아져요"]
    return frame(a, "필터링은 받을 상대를 정해요", "손님 확인을 얼마나 꼼꼼히 하나의 차이예요", caps, "".join(body))


# 5 ---
def p5():
    a = Anim(4, dur(False))
    rows = [("Full Cone", "목적지 독립", "누구든 허용"), ("Restricted Cone", "목적지 독립", "같은 IP"),
            ("Port Restricted", "목적지 독립", "같은 IP·포트"), ("Symmetric", "목적지마다 다름", "상대와 연관")]
    body = [a.vis(cell(330, 130, 260, 36, "매핑", BLUE, 16, BG), 2, 4), a.vis(cell(610, 130, 260, 36, "필터링", VIOLET, 16, BG), 3, 4)]
    for i, (n, m, f) in enumerate(rows):
        y = 176 + i * 58
        body += [a.vis(cell(90, y, 220, 48, n, MUTED, 17), 1, 4),
                 a.vis(cell(330, y, 260, 48, m, ORANGE if i == 3 else BLUE, 17), 2, 4),
                 a.vis(cell(610, y, 260, 48, f, VIOLET, 17), 3, 4)]
    body += [a.vis(hl(330, 130, 260, 266), 2, 2), a.vis(hl(610, 130, 260, 266), 3, 3),
             a.vis(pill(480, 432, "이름보다 두 기준을 따로 확인", GREEN, 18, True, 340), 4, 4)]
    caps = ["예전 자료엔 Cone 이름이 네 가지 나와요", "매핑 칸: Symmetric만 목적지마다 달라요", "필터링 칸: 받는 상대가 점점 좁아져요", "실제 장비는 두 기준을 따로 확인해요"]
    return frame(a, "옛 Cone 이름 풀어 읽기", "이름 하나에 두 기준이 묶여 있어요", caps, "".join(body))


# 6 ---
def p6():
    a = Anim(4, dur(False))
    body = [peers(330), srv(480, 165),
            mv(a, packet(0, 0), [(260, 310), (400, 190)], 1, 1, 1, 0.1, 0.85),
            mv(a, packet(0, 0), [(700, 310), (560, 190)], 1, 1, 1, 0.1, 0.85),
            a.vis(pill(230, 255, "A의 바깥 주소", BLUE, 15, True, 150) + pill(730, 255, "B의 바깥 주소", BLUE, 15, True, 150), 2, 4),
            a.vis(hl(130, 230, 200, 50) + hl(630, 230, 200, 50), 2, 2),
            mv(a, packet(0, 0, ORANGE), [(270, 330), (455, 330)], 3, 3, 3, 0.1, 0.8),
            mv(a, packet(0, 0, ORANGE), [(690, 330), (505, 330)], 3, 3, 3, 0.1, 0.8),
            a.vis(check(480, 395), 3, 4),
            a.vis(pill(480, 445, "양쪽이 먼저 보내 길을 열어요", GREEN, 18, True, 320), 4, 4)]
    caps = ["A와 B가 소개 서버에 먼저 연락해요", "서버가 서로의 바깥 주소·포트를 알려 줘요", "A와 B가 동시에 서로에게 보내 매핑이 생겨요", "필터링까지 맞으면 직접 연결돼요"]
    return frame(a, "UDP 홀 펀칭", "소개해 준 친구 덕분에 서로 먼저 인사해요", caps, "".join(body))


# 7 ---
def p7():
    a = Anim(4, dur(False))
    ya, yb = 200, 345

    def row(y):
        return laptop(110, y, None) + text(110, y + 44, "A", 16, TXT, 700) + laptop(850, y, None) + text(850, y + 44, "B", 16, TXT, 700)
    body = [text(480, 150, "직접 (홀 펀칭)", 18, BLUE, 700), row(ya), line(170, ya, 790, ya, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(190, ya), (450, ya)], 1, 1, 2, 0.1, 0.8),
            a.vis(cross(480, ya), 2, 4), a.vis(hl(440, ya - 30, 80, 60), 2, 2),
            a.vis(text(480, 285, "중계 (TURN)", 18, GREEN, 700) + row(yb) + srv(480, yb)
                  + line(170, yb, 440, yb, GREEN, 4) + line(520, yb, 790, yb, GREEN, 4), 3, 4),
            mv(a, packet(0, 0, GREEN), [(190, yb), (430, yb), (530, yb), (770, yb)], 3, 3, 4, 0.05, 0.9),
            a.vis(check(850, yb - 60), 3, 4),
            a.vis(pill(480, 455, "STUN은 주소 확인 · TURN은 데이터 중계", ORANGE, 17, True, 400), 4, 4)]
    caps = ["A가 B에게 직접 보내 보지만…", "NAT·방화벽 조건이 안 맞으면 막혀요", "그럴 땐 TURN 서버가 대신 전달해요", "중계는 비용이 들지만 연결을 이어 줘요"]
    return frame(a, "직접이 안 되면 중계로", "직접 전화가 안 되면 교환원을 거쳐요", caps, "".join(body))


ITEMS = [
    ("u12-mapping-peers", "advanced-nat-mapping-filtering-page-01", "NAT 뒤의 피어끼리 만나기", "공유기 뒤의 A와 B 중 B가 먼저 보낸 패킷이 A의 공유기에서 어느 기기로 보낼지 몰라 막히는 모습입니다.", "직접 통신에는 매핑과 허용 조건이 모두 맞아야 합니다.", p1),
    ("u12-mapping-vs-filtering", "advanced-nat-mapping-filtering-page-02", "매핑과 필터링은 다른 질문", "왼쪽은 안쪽 192.168.0.10:3000을 바깥 203.0.113.8:42000에 짝짓는 매핑, 오른쪽은 15.15.15.15:5555에서 온 패킷을 받는 필터링을 나란히 보여 줍니다.", "매핑은 나가는 주소, 필터링은 받을 상대를 정합니다.", p2),
    ("u12-mapping-eim", "advanced-nat-mapping-filtering-page-03", "매핑은 상대에 따라 달라질 수 있어요", "같은 A가 9.9.9.9와 새로 통신할 때 목적지 독립 매핑은 :42000을 재사용하고 목적지 종속 매핑은 다른 바깥 포트를 쓰는 것을 비교합니다.", "상대가 바뀌어도 같은 바깥 주소를 쓰는지 봅니다.", p3),
    ("u12-mapping-filtering", "advanced-nat-mapping-filtering-page-04", "필터링은 받을 상대를 정해요", "15.15.15.15:7777에서 패킷이 오면 EIF와 ADF는 허용할 수 있고 포트까지 비교하는 APDF는 막을 수 있음을 보여 줍니다.", "필터링은 누구든, 같은 IP, 같은 IP·포트 순으로 좁아집니다.", p4),
    ("u12-mapping-cone", "advanced-nat-mapping-filtering-page-05", "옛 Cone 이름 풀어 읽기", "Full Cone, Restricted Cone, Port Restricted, Symmetric 이름을 매핑 칸과 필터링 칸으로 나누어 차례로 풀어 읽는 표입니다.", "옛 이름은 매핑과 필터링 두 기준으로 나누어 읽습니다.", p5),
    ("u12-mapping-hole-punching", "advanced-nat-mapping-filtering-page-06", "UDP 홀 펀칭", "A와 B가 소개 서버에 연락하고, 서버가 서로의 바깥 주소를 알려 준 뒤, 두 피어가 동시에 서로에게 패킷을 보내 직접 연결되는 모습입니다.", "양쪽이 먼저 보낸 패킷으로 직접 경로를 시도합니다.", p6),
    ("u12-mapping-relay", "advanced-nat-mapping-filtering-page-07", "직접이 안 되면 중계로", "A가 B에게 직접 보낸 패킷이 막히자 TURN 서버를 거쳐 B에게 전달되는 중계 경로를 위아래로 비교합니다.", "직접 연결이 안 되면 TURN 같은 중계 서버를 씁니다.", p7),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-1[234]\.svg\n(?:    .*\n)+", "", s)
    for f, pid, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in s:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        assert f"- page_id: {pid}\n" in s, pid
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        for n in (12, 13, 14):
            (LESSON / "assets" / "diagrams" / f"source-{n}.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
