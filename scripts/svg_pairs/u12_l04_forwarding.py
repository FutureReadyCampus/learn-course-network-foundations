#!/usr/bin/env python3
"""Unit 12 Lesson 4 (포트 포워딩으로 내부 서비스 연결하기): 4-step example SVG per Page (8). Run from repo root:
python3 scripts/svg_pairs/u12_l04_forwarding.py   (--svg-only skips lesson.md edit / stale diagram removal).

Running example (lesson text values): 집 안 웹 서버 192.168.0.12:80, 공유기 공인 주소 3.3.3.3, 바깥 친구.
Step arc per page: ① 상황 → ② 동작(움직이는 패킷) → ③ 결과·대비(✓/✗) → ④ 기억할 점 한 줄.
The element that changes in a step gets an orange highlight only during that step."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur, person
from u7_l01 import mv
from u11_structures import srv
from u12_l01_router import net, rt
from u12_l02_nat_table import env, ledger

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-router-and-nat/lessons/restructured/04-*"))
OUT = LESSON / "assets" / "animations"
Y = 300
SRV, PUB = "192.168.0.12:80", "3.3.3.3:80"


def new(a, step, x, y, w, h):
    """Orange highlight around the element that changed in `step` (only during that step)."""
    return a.vis(hl(x, y, w, h, ORANGE, 12), step, step)


def home(x=30, w=560):
    """집 안 네트워크 상자 + 웹 서버 + 공유기(오른쪽 경계)."""
    return net(x, 150, w, 270, "집 안", GREEN) + srv(140, Y) + rt(x + w, Y)


def friend(x=850):
    return person(x, Y - 10, "친구")


def rule(x, y, txt, w=250):
    return cell(x, y, w, 44, txt, ORANGE, 16)


# 1 ---
def p1():
    a = Anim(4, dur(False))
    T, B = 205, 375
    body = [laptop(110, T, "내 PC"), rt(480, T, ""), srv(850, T - 12),
            line(170, T, 450, T, LINE, 4, "10 8"), line(510, T, 800, T, LINE, 4, "10 8"),
            srv(110, B - 12), rt(480, B, ""), person(850, B - 10),
            line(160, B, 450, B, LINE, 4, "10 8"), line(510, B, 820, B, LINE, 4, "10 8"),
            text(300, T - 40, "안 → 밖", 18, BLUE, 700), text(660, B - 40, "밖 → 안", 18, RED, 700),
            mv(a, packet(0, 0), [(190, T), (790, T)], 1, 1, 1, 0.1, 0.9),
            a.vis(ledger(560, T - 40) + check(850, T - 85), 2, 4), new(a, 2, 538, T - 66, 44, 52),
            mv(a, packet(0, 0, RED), [(800, B), (545, B)], 3, 3, 4, 0.1, 0.8),
            a.vis(cross(480, B - 55), 3, 4), new(a, 3, 460, B - 75, 40, 40),
            a.vis(pill(480, 455, "밖에서 먼저 오면 매핑을 직접 정해요", ORANGE, 17, True, 380), 4, 4)]
    caps = ["내 PC가 먼저 바깥 서버에 접속해요", "나갈 때 NAT Table에 자동으로 기록돼요", "바깥에서 먼저 오면 기록이 없어 막혀요", "반대 방향은 대응 관계를 직접 넣어야 해요"]
    return frame(a, "자동 매핑은 안에서 시작할 때만", "나갈 때 적은 대장만 있으면 답장은 와요", caps, "".join(body))


# 2 ---
def p2():
    a = Anim(4, dur(False))
    body = [box(40, 140, 420, 280, BLUE, PANEL, 16, dash=True, sw=3) + text(250, 172, "동적 매핑", 20, BLUE, 700),
            box(500, 140, 420, 280, ORANGE, PANEL, 16, dash=True, sw=3) + text(710, 172, "정적 매핑", 20, ORANGE, 700),
            ledger(250, 250), text(250, 310, "Outbound가 자동으로", 16, MUTED, 700),
            a.vis(person(600, 260) + text(600, 345, "관리자", 16, MUTED, 700), 2, 4),
            a.vis(rule(660, 215, f":80 → {SRV}", 240), 2, 4), new(a, 2, 660, 215, 240, 44),
            mv(a, packet(0, 0, ORANGE), [(900, 300), (690, 300)], 3, 3, 4, 0.1, 0.8),
            a.vis(check(780, 360) + text(780, 400, "외부 :80 → 서버로", 15, GREEN, 700), 3, 4), new(a, 3, 760, 340, 40, 40),
            a.vis(pill(480, 455, "포트 포워딩 = 직접 넣은 정적 매핑", ORANGE, 18, True, 380), 4, 4)]
    caps = ["동적 매핑은 나갈 때 자동으로 생겨요", "관리자가 규칙을 한 줄 직접 넣어요", "바깥에서 :80으로 오면 내부 서버로 전달돼요", "직접 넣는 매핑을 포트 포워딩이라 불러요"]
    return frame(a, "정적 매핑을 직접 추가", "경비실에 '이 택배는 12호로' 미리 적어 둬요", caps, "".join(body))


# 3 ---
def p3():
    a = Anim(4, dur(False))
    heads = ["규칙 이름", "외부 포트", "내부 IP", "내부 포트", "원격지 IP"]
    vals = ["웹 서버", "80", "192.168.0.12", "80", "제한 없음"]
    ws = [150, 130, 200, 130, 160]
    xs = [80 + sum(ws[:i]) for i in range(5)]
    win = (box(60, 130, 840, 175, LINE, PANEL, 12, sw=3) + f'<rect x="60" y="130" width="840" height="40" rx="12" fill="{LINE}"/>'
           + text(480, 157, "포트 포워딩 설정", 18, TXT, 700)
           + "".join(cell(xs[i], 190, ws[i] - 8, 38, h, MUTED, 15, BG) for i, h in enumerate(heads)))
    row = "".join(cell(xs[i], 240, ws[i] - 8, 44, v, GREEN, 16) for i, v in enumerate(vals))
    body = [win, a.vis(text(480, 270, "아직 규칙이 없어요", 17, MUTED, 700), 1, 1),
            a.vis(row, 2, 4), new(a, 2, 80, 240, 802, 44),
            a.vis("".join(person(x, 370) for x in (620, 710, 800)) + "".join(check(x + 26, 342) for x in (620, 710, 800)), 3, 4),
            new(a, 3, xs[4], 240, ws[4] - 8, 44),
            a.vis(pill(300, 375, "원격지 제한 없음 = 누구나", VIOLET, 16, True, 260), 3, 4),
            a.vis(pill(480, 460, "Rule은 방화벽 규칙과 같은 뜻", ORANGE, 17, True, 320), 4, 4)]
    caps = ["공유기 관리 화면에 포트 포워딩 메뉴가 있어요", "외부 80번을 192.168.0.12의 80번으로 연결해요", "원격지를 비워 두면 어느 바깥 주소든 들어와요", "이 한 줄을 Rule(규칙)이라고 불러요"]
    return frame(a, "공유기의 포트 포워딩 설정", "관리 화면에 규칙 한 줄을 적어요", caps, "".join(body))


# 4 ---
def p4():
    a = Anim(4, dur(False))
    body = [home(), friend(),
            pill(140, 210, SRV, GREEN, 15, True, 180),
            line(620, Y, 800, Y, LINE, 4, "10 8"),
            a.vis(pill(400, 215, "“192.168.0.12로 들어와!”", BLUE, 17, False, 280), 2, 4), new(a, 2, 260, 197, 280, 36),
            mv(a, packet(0, 0, RED), [(810, Y), (650, Y)], 3, 3, 4, 0.1, 0.8),
            a.vis(cross(700, Y - 55) + text(720, Y + 70, "인터넷엔 그 주소가 없어요", 16, RED, 700), 3, 4), new(a, 3, 680, Y - 75, 40, 40),
            a.vis(pill(480, 455, "사설 주소는 바깥에서 못 찾아요", ORANGE, 18, True, 340), 4, 4)]
    caps = ["집 안 PC에 웹 서버를 켰어요(TCP 80)", "친구에게 내부 주소를 알려 줬어요", "친구의 요청은 그 주소로 도착하지 못해요", "공유기 뒤의 사설 주소는 바깥용이 아니에요"]
    return frame(a, "내부 웹 서버를 공개하는 상황", "아파트 호수만 알려 주면 택배가 못 와요", caps, "".join(body))


# 5 ---
def p5():
    a = Anim(4, dur(False))
    body = [home(), friend(), pill(140, 210, SRV, GREEN, 15, True, 180), pill(590, 380, "공인 3.3.3.3", BLUE, 16, True, 150),
            line(620, Y, 800, Y, LINE, 4, "10 8"), line(170, Y, 560, Y, LINE, 4, "10 8"),
            a.vis(env(630, 130, "친구", PUB, BLUE, "dst"), 1, 4), new(a, 1, 630, 130, 270, 74),
            mv(a, packet(0, 0), [(810, Y), (630, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(rule(410, 220, f":80 → {SRV}", 220), 2, 4), new(a, 2, 410, 220, 220, 44),
            a.vis(env(60, 380, "친구", SRV, GREEN, "dst"), 3, 4), new(a, 3, 60, 380, 270, 74),
            mv(a, packet(0, 0, GREEN), [(550, Y), (200, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(check(140, 235), 3, 4),
            a.vis(pill(720, 455, "공유기는 전달만 해요", ORANGE, 18, True, 240), 4, 4)]
    caps = ["친구는 공유기의 공인 주소 3.3.3.3:80으로 접속해요", "공유기에 외부 80 → 내부 192.168.0.12:80 규칙이 있어요", "목적지를 바꿔 안쪽 웹 서버로 보내요", "웹 서버는 공유기가 아니라 안쪽 PC예요"]
    return frame(a, "바깥에서 접속할 주소", "건물 대표 주소로 보내면 경비실이 호수로 넘겨요", caps, "".join(body))


# 6 ---
def p6():
    a = Anim(4, dur(False))
    body = [home(), friend(), line(620, Y, 800, Y, LINE, 4, "10 8"), line(170, Y, 560, Y, LINE, 4, "10 8"),
            a.vis(packet(200, Y - 50, ORANGE) + text(140, 210, "요청 도착", 16, ORANGE, 700), 1, 1),
            mv(a, packet(0, 0, GREEN), [(200, Y), (550, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(330, 380, "응답: 192.168.0.12", GREEN, 15, True, 190), 2, 4), new(a, 2, 235, 364, 190, 32),
            mv(a, packet(0, 0, GREEN), [(620, Y), (810, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(check(850, Y - 85) + pill(720, 210, "보이는 건 3.3.3.3", BLUE, 15, True, 180), 3, 4), new(a, 3, 630, 194, 180, 32),
            a.vis(pill(480, 448, "응답을 만드는 건 안쪽 서버예요", ORANGE, 18, True, 330), 4, 4)]
    caps = ["친구의 요청이 내부 웹 서버에 도착했어요", "서버가 만든 응답이 공유기로 가요", "친구는 3.3.3.3이 답한 것처럼 받아요", "미리 정한 규칙으로 바깥 유입을 허용한 결과예요"]
    return frame(a, "내부·외부 접속 결과", "답장도 경비실을 거쳐 나가요", caps, "".join(body))


# 7 ---
def p7():
    a = Anim(4, dur(False))
    body = [net(20, 150, 380, 270, "집 1", GREEN) + laptop(110, Y, "PC 1") + rt(400, Y, "공유기 1"),
            net(560, 150, 380, 270, "집 2", BLUE) + laptop(850, Y, "PC 2") + rt(560, Y, "공유기 2"),
            line(430, Y, 530, Y, LINE, 4, "8 6"), line(170, Y, 370, Y, LINE, 4, "8 6"), line(590, Y, 790, Y, LINE, 4, "8 6"),
            a.vis(text(110, 210, ":30000", 18, GREEN, 700) + text(850, 210, ":40000", 18, BLUE, 700), 1, 4),
            a.vis(rule(185, 365, ":30000 → PC 1", 180) + rule(595, 365, ":40000 → PC 2", 180), 2, 4),
            new(a, 2, 185, 365, 180, 44) + new(a, 2, 595, 365, 180, 44),
            mv(a, packet(0, 0, ORANGE), [(160, Y), (800, Y)], 3, 3, 3, 0.05, 0.95),
            a.vis(check(850, 400), 3, 4), new(a, 3, 830, 380, 40, 40),
            a.vis(pill(480, 455, "프로그램마다 규칙을 따로", ORANGE, 17, True, 280), 4, 4)]
    caps = ["P2P 프로그램이 PC 1은 30000, PC 2는 40000을 써요", "각 공유기에 자기 PC로 가는 규칙을 넣어요", "그러면 양쪽 NAT를 넘어 직접 통신할 수 있어요", "포트마다, 공유기마다 규칙이 필요해요"]
    return frame(a, "여러 서비스와 Port를 열기", "집마다 경비실에 따로 부탁해요", caps, "".join(body))


# 8 ---
def p8():
    a = Anim(4, dur(False))
    steps = ["메뉴 찾기", "포트 입력", "재시작"]
    body = [person(110, 270, "나"), laptop(270, 290, "게임"),
            a.vis(pill(270, 190, "방 입장!", BLUE, 17, True, 120), 1, 4),
            a.vis("".join(cell(400 + i * 170, 260, 150, 50, s, ORANGE, 17) for i, s in enumerate(steps))
                  + "".join(text(400 + i * 170 + 160, 291, "→", 20, MUTED, 700) for i in range(2)), 2, 4),
            new(a, 2, 400, 260, 490, 50),
            a.vis(text(645, 360, "방마다 또? 공유기마다 또?", 18, RED, 700) + cross(840, 355), 3, 4), new(a, 3, 820, 335, 40, 40),
            a.vis(pill(480, 450, "자동으로 요청하는 방법 → UPnP", GREEN, 18, True, 340), 4, 4)]
    caps = ["게임 방에 들어갈 때마다 포트가 필요해요", "제조사 화면을 찾아 입력하고 재시작해요", "매번 이렇게 하기는 너무 번거로워요", "다음 Lesson의 UPnP가 이 일을 자동화해요"]
    return frame(a, "매번 설정해야 하는 불편", "택배마다 경비실에 직접 가서 적는 셈이에요", caps, "".join(body))


ITEMS = [
    ("u12-fwd-auto-review", "advanced-source-15-page-01", "자동 매핑은 안에서 시작할 때만", "위쪽은 내 PC가 먼저 접속해 NAT Table에 자동 기록이 생기고 응답이 오는 모습, 아래쪽은 바깥에서 먼저 온 패킷이 기록이 없어 막히는 모습을 나란히 보여 줍니다.", "바깥에서 먼저 접속하려면 매핑을 직접 지정해야 합니다.", p1),
    ("u12-fwd-static", "advanced-source-15-page-02", "정적 매핑을 직접 추가", "왼쪽은 Outbound로 자동 생기는 동적 매핑, 오른쪽은 관리자가 외부 80 → 192.168.0.12:80 규칙을 직접 넣어 바깥 요청이 전달되는 정적 매핑입니다.", "직접 넣은 정적 매핑이 포트 포워딩입니다.", p2),
    ("u12-fwd-settings", "advanced-source-15-page-03", "공유기의 포트 포워딩 설정", "공유기 관리 화면에 외부 포트 80, 내부 IP 192.168.0.12, 내부 포트 80, 원격지 제한 없음 규칙이 추가되고 여러 바깥 사용자가 들어올 수 있는 모습입니다.", "포트 포워딩 규칙 한 줄로 외부 포트를 내부 서버와 잇습니다.", p3),
    ("u12-fwd-private-fail", "advanced-source-15-page-04", "내부 웹 서버를 공개하는 상황", "집 안 웹 서버 192.168.0.12:80의 주소를 친구에게 알려 줘도 바깥에서 보낸 요청이 도착하지 못하는 모습입니다.", "사설 주소만으로는 바깥에서 접속할 수 없습니다.", p4),
    ("u12-fwd-public-address", "advanced-source-15-page-05", "바깥에서 접속할 주소", "친구가 공인 주소 3.3.3.3:80으로 보낸 요청이 공유기 규칙에 따라 목적지가 192.168.0.12:80으로 바뀌어 내부 웹 서버에 도착하는 모습입니다.", "공유기는 목적지를 바꿔 내부 서버로 전달합니다.", p5),
    ("u12-fwd-response", "advanced-source-15-page-06", "내부·외부 접속 결과", "내부 웹 서버가 만든 응답이 공유기를 거쳐 친구에게 가고, 친구에게는 3.3.3.3이 답한 것처럼 보이는 모습입니다.", "응답을 만드는 주체는 내부 서버입니다.", p6),
    ("u12-fwd-two-homes", "advanced-source-15-page-07", "여러 서비스와 Port를 열기", "두 집의 공유기에 각각 30000번을 PC 1로, 40000번을 PC 2로 보내는 규칙을 넣어 P2P 통신이 이어지는 모습입니다.", "포트와 공유기마다 포워딩 규칙이 필요합니다.", p7),
    ("u12-fwd-manual-pain", "advanced-source-15-page-08", "매번 설정해야 하는 불편", "게임 방에 들어갈 때마다 메뉴 찾기, 포트 입력, 재시작을 반복해야 하는 번거로움과 이를 자동화하는 UPnP로 이어지는 흐름입니다.", "반복 설정을 자동화하는 방법으로 UPnP가 등장합니다.", p8),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    fm = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-15\.svg\n(?:    .*\n)+", "", fm, count=1)
    for f, pid, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in fm:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        if f"- page_id: {pid}\n" in fm:
            fm = fm.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
        else:  # page has no metadata entry yet: append one to the end of page_metadata
            fm = fm.rstrip("\n") + f"\n- page_id: {pid}\n{blk}"
    md.write_text(head + "---\n" + fm + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        (LESSON / "assets" / "diagrams" / "source-15.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
