#!/usr/bin/env python3
"""Unit 12 Lesson 5 (UPnP와 자동 포트 설정): 4-step example SVG per Page (8). Run from repo root:
python3 scripts/svg_pairs/u12_l05_upnp.py   (--svg-only skips lesson.md edit / stale diagram removal).

One running example: 집 PC 192.168.0.10의 Torrent 프로그램이 공유기(바깥 198.51.100.25)에게 6881번 문을 열어 달라고 요청한다.
Step arc per page: ① 상황 → ② 동작 → ③ 결과(✓/✗) → ④ 기억할 점. 새로 바뀐 요소는 그 단계에서만 주황 테두리."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur, person
from u7_l01 import mv
from u11_structures import srv
from u12_l01_router import net, rt, cloud
from u12_l02_nat_table import table, ledger

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-router-and-nat/lessons/restructured/05-*"))
OUT = LESSON / "assets" / "animations"
Y = 300
PCIP, WAN, PORT = "192.168.0.10", "198.51.100.25", "6881"


def home(extra=""):
    """집 안(LAN) 상자 + Torrent PC + 공유기 (공통 배경)."""
    return net(40, 150, 280, 270, "우리 집", GREEN) + pc(180, 300, f"PC {PCIP}") + rt(480, Y) + extra


def peer(x=820, label="바깥 상대"):
    return person(x, Y - 10, label)


def mark(x, y, w, h, s, t):
    """주황 테두리: 단계 t에서만 보이는 '방금 바뀐 것' 표시."""
    return a_.vis(hl(x, y, w, h, ORANGE, 12), t, t)


a_ = None  # current Anim, set by each page


def new(n=4):
    global a_
    a_ = Anim(n, dur(False))
    return a_


# 1 Torrent와 P2P ---------------------------------------------------------------
def p1():
    a = new()
    body = [home(line(250, Y, 450, Y, LINE, 4, "8 6") + line(510, Y, 770, Y, LINE, 4, "8 6")), peer(),
            a.vis(pill(480, 200, "UPnP 실행 중", GREEN, 17, True, 150), 1, 4), mark(400, 183, 160, 34, 0, 1),
            mv(a, packet(0, 0, ORANGE), [(770, Y), (520, Y)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, ORANGE), [(440, Y), (250, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(check(180, 225), 3, 4), mark(150, 205, 60, 40, 0, 3),
            a.vis(pill(480, 450, "수동 설정 없이도 P2P 연결", GREEN, 18, False, 300), 4, 4)]
    caps = ["공유기의 UPnP 기능이 켜져 있어요", "바깥 상대가 Torrent에게 연결을 보내요", "공유기를 지나 PC까지 도착해요", "UPnP 덕분에 직접 설정하지 않아도 돼요"]
    return frame(a, "Torrent와 P2P", "공유기가 알아서 문을 열어 주는 이야기예요", caps, "".join(body))


def usb(x, y):
    return (f'<rect x="{x - 14}" y="{y - 30}" width="28" height="44" rx="5" fill="{PANEL}" stroke="{ORANGE}" stroke-width="3"/>'
            f'<rect x="{x - 9}" y="{y + 14}" width="18" height="16" fill="{MUTED}"/>')


# 2 UPnP라는 기능 ----------------------------------------------------------------
def p2():
    a = new()
    body = [pc(380, Y, "PC"),
            a.vis(usb(600, 290) + pill(600, 200, "USB 저장장치", ORANGE, 16, False, 150), 1, 1),
            mv(a, usb(0, 0), [(600, 290), (440, 290)], 2, 2, 2, 0.1, 0.8),
            a.vis(usb(440, 290), 3, 4),
            a.vis(check(380, 205) + pill(380, 410, "설정 없이 바로 사용", GREEN, 17, True, 210), 3, 4), mark(285, 393, 190, 34, 0, 3),
            a.vis(pill(720, 300, "UPnP = 네트워크판 PnP", BLUE, 18, True, 260), 4, 4)]
    caps = ["USB 저장장치를 쓰고 싶어요", "PC에 꽂기만 해요", "복잡한 설정 없이 바로 쓸 수 있어요", "UPnP는 이 생각을 네트워크로 넓힌 거예요"]
    return frame(a, "UPnP라는 기능", "Universal Plug and Play · 꽂으면 바로", caps, "".join(body))


# 3 Plug and Play의 배경 ----------------------------------------------------------
def p3():
    a = new()
    L, R = 60, 500
    body = [box(L, 140, 400, 290, MUTED, PANEL, 16, sw=2) + text(L + 200, 172, "예전", 20, MUTED, 700),
            box(R, 140, 400, 290, GREEN, PANEL, 16, sw=2) + text(R + 200, 172, "PnP 이후", 20, GREEN, 700),
            printer(L + 200, 240), printer(R + 200, 240),
            a.vis(pill(L + 200, 320, "드라이버 설치·설정", RED, 16, False, 200) + cross(L + 200, 385), 2, 4), mark(L + 96, 303, 208, 34, 0, 2),
            a.vis(pill(R + 200, 320, "자동 인식·준비", GREEN, 16, False, 180) + check(R + 200, 385), 3, 4), mark(R + 106, 303, 188, 34, 0, 3),
            a.vis(pill(480, 455, "UPnP도 연결·설정을 자동으로", BLUE, 17, True, 320), 4, 4)]
    caps = ["예전과 지금, 프린터 연결을 비교해요", "예전엔 사람이 직접 설치하고 설정했어요", "PnP는 인식과 준비를 자동으로 해요", "UPnP도 같은 생각으로 자동화해요"]
    return frame(a, "Plug and Play의 배경", "사람이 하던 설정을 기계가 대신해요", caps, "".join(body))


def tv(x, y):
    return (box(x - 50, y - 36, 100, 66, BLUE, PANEL, 8, sw=3) + line(x - 20, y + 42, x + 20, y + 42, BLUE, 4)
            + text(x, y + 6, "홈쇼핑", 17, BLUE, 700))


# 4 P2P가 여러 상대와 만나는 구조 (쿠폰 인쇄) ---------------------------------------
def p4():
    a = new()
    body = [home(printer(270, 392)), line(510, Y, 770, Y, LINE, 4, "8 6"), tv(820, Y),
            a.vis(pill(820, 200, "쿠폰 인쇄 버튼", BLUE, 16, False, 160), 1, 4), mark(736, 183, 168, 34, 0, 1),
            mv(a, packet(0, 0, ORANGE), [(760, Y), (530, Y)], 2, 2, 4, 0.1, 0.9),
            a.vis(cross(480, 225), 3, 4), mark(456, 201, 48, 48, 0, 3),
            a.vis(pill(480, 455, "NAT 뒤 PC로는 바로 못 들어와요", RED, 17, False, 340), 4, 4)]
    caps = ["홈쇼핑에서 쿠폰 인쇄 버튼을 눌렀어요", "바깥 서비스의 요청이 집으로 와요", "공유기에서 막혀 PC·프린터에 못 가요", "밖에서 먼저 온 연결은 NAT가 막아요"]
    return frame(a, "밖에서 집 안 프린터까지", "버튼 하나로 집 프린터를 쓰려면?", caps, "".join(body))


# 5 NAT가 가로막는 접속 · 수동 vs 자동 ---------------------------------------------
def p5():
    a = new()
    L, R = 60, 500
    body = [box(L, 140, 400, 290, MUTED, PANEL, 16, sw=2) + text(L + 200, 172, "수동 포트 포워딩", 19, MUTED, 700),
            box(R, 140, 400, 290, GREEN, PANEL, 16, sw=2) + text(R + 200, 172, "UPnP 자동 설정", 19, GREEN, 700),
            person(L + 110, 235, "사용자"), rt(L + 300, 260), rt(R + 300, 260), pc(R + 100, 260, "Torrent"),
            a.vis(pill(L + 200, 360, "설정 화면 직접 입력", RED, 16, False, 210) + cross(L + 200, 405), 1, 4), mark(L + 91, 343, 218, 34, 0, 1),
            mv(a, packet(0, 0, ORANGE), [(R + 150, 260), (R + 260, 260)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(R + 200, 360, "SSDP로 서비스 찾기", BLUE, 16, False, 200), 2, 4), mark(R + 96, 343, 208, 34, 0, 2),
            a.vis(check(R + 200, 405), 3, 4), mark(R + 176, 381, 48, 48, 0, 3),
            a.vis(pill(480, 455, "프로그램이 공유기와 대신 설정해요", GREEN, 17, True, 350), 4, 4)]
    caps = ["사용자에게 포워딩 설정을 맡기기는 어려워요", "UPnP 프로그램은 SSDP로 공유기를 찾아요", "사람이 손대지 않아도 설정이 끝나요", "이 자동화가 UPnP의 역할이에요"]
    return frame(a, "NAT가 가로막는 접속", "직접 설정할까, 프로그램이 대신할까", caps, "".join(body))


# 6 프로그램이 매핑을 요청하기 ------------------------------------------------------
def p6():
    a = new()
    head, rows = table(560, 380, ["바깥 포트", "안쪽 대상"], [[f"{WAN}:{PORT}", f"{PCIP}:{PORT}"]], [190, 180], ORANGE, 13)
    body = [home(line(250, Y, 450, Y, LINE, 4, "8 6") + line(510, Y, 770, Y, LINE, 4, "8 6")), peer(),
            mv(a, packet(0, 0, BLUE), [(250, Y), (440, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(390, 205, "설정 도우미 있나요?", BLUE, 15, True, 190), 1, 1),
            a.vis(pill(480, 205, f"{PORT}번 열어 주세요", ORANGE, 15, True, 180), 2, 2),
            a.vis(head + rows[0] + ledger(480, 380), 2, 4), mark(560, 424, 364, 42, 0, 2),
            mv(a, packet(0, 0, GREEN), [(770, Y), (520, Y), (440, Y), (250, Y)], 3, 3, 3, 0.05, 0.95),
            a.vis(check(180, 225), 3, 4), mark(150, 205, 60, 40, 0, 3),
            a.vis(pill(480, 160, "프로그램이 포워딩을 자동으로", GREEN, 17, False, 300), 4, 4)]
    caps = ["Torrent가 자동 설정 서비스를 찾아요", "공유기에게 6881번 매핑을 요청해요", "바깥 상대의 연결이 PC까지 들어와요", "필요한 포트 포워딩을 자동으로 협의해요"]
    return frame(a, "프로그램이 매핑을 요청하기", "찾고 → 요청하고 → 들어와요", caps, "".join(body))


# 7 UPnP와 NAT를 함께 살펴보기 -------------------------------------------------------
def p7():
    a = new()
    head, rows = table(140, 160, ["", "누가 입력하나", "결과"], [["수동", "사용자가 직접", "번거로워요"], ["UPnP", "프로그램이 요청", "자동으로 열려요"]], [140, 260, 280], GREEN, 17)
    body = [head, a.vis(rows[0], 1, 4), mark(140, 204, 674, 42, 0, 1),
            a.vis(rows[1], 2, 4), mark(140, 254, 674, 42, 0, 2),
            a.vis(pill(480, 360, "공유기 지원 + 기능 켜짐이 전제", ORANGE, 17, True, 330), 3, 4), mark(311, 343, 338, 34, 0, 3),
            a.vis(pill(480, 430, "입력 부담을 줄여 P2P를 도와요", GREEN, 18, False, 340), 4, 4)]
    caps = ["수동 설정은 사용자가 직접 입력해요", "UPnP는 프로그램이 대신 요청해요", "단, 공유기가 지원하고 켜져 있어야 해요", "사람의 설정 부담을 줄이는 게 핵심이에요"]
    return frame(a, "UPnP와 NAT를 함께 보기", "같은 포워딩, 입력하는 주체가 달라요", caps, "".join(body))


# 8 P2P 프로그램 개발로 이어 보기 ------------------------------------------------------
def p8():
    a = new()
    items = [("① 서비스 발견 (SSDP)", BLUE), ("② 매핑 요청", ORANGE), ("③ 주소·포트 매핑 이해", GREEN)]
    body = [pc(170, 280, "내 P2P 프로그램")]
    for i, (t, c) in enumerate(items):
        y = 160 + i * 80
        body.append(a.vis(cell(330, y, 420, 56, t, c, 20) + check(790, y + 28), i + 1, 4))
        body.append(mark(330, y, 420, 56, 0, i + 1))
    body.append(a.vis(pill(480, 445, "다음 기술도 이 매핑 위에 있어요", GREEN, 18, True, 340), 4, 4))
    caps = ["P2P 프로그램은 먼저 공유기를 찾아야 해요", "그리고 필요한 매핑을 요청해요", "주소·포트 매핑을 알면 연결 문제가 보여요", "앞으로 배울 기술의 바탕이 돼요"]
    return frame(a, "P2P 프로그램 개발로", "설계할 때 챙길 것들", caps, "".join(body))


ITEMS = [
    ("u12-upnp-torrent", "Torrent와 P2P", "공유기의 UPnP가 켜진 상태에서 바깥 상대의 연결이 공유기를 지나 집 PC의 Torrent까지 도착하는 모습입니다.", "UPnP가 있으면 수동 설정 없이 P2P 연결이 이어질 수 있습니다.", p1),
    ("u12-upnp-pnp", "UPnP라는 기능", "USB 저장장치를 PC에 꽂으면 설정 없이 바로 쓰이는 모습으로 Plug and Play를 설명합니다.", "UPnP는 Plug and Play의 생각을 네트워크로 넓힌 기능입니다.", p2),
    ("u12-upnp-history", "Plug and Play의 배경", "예전에는 프린터 드라이버를 직접 설치·설정해야 했고, PnP 이후에는 자동으로 인식·준비되는 것을 나란히 비교합니다.", "사람이 하던 설정을 자동화하는 것이 PnP와 UPnP의 공통점입니다.", p3),
    ("u12-upnp-coupon", "밖에서 집 안 프린터까지", "홈쇼핑 쿠폰 인쇄 요청이 집으로 오지만 NAT 공유기에서 막혀 PC와 프린터에 닿지 못하는 모습입니다.", "NAT 뒤 PC로는 바깥에서 먼저 시작한 연결이 바로 들어오지 못합니다.", p4),
    ("u12-upnp-manual-vs-auto", "NAT가 가로막는 접속", "왼쪽은 사용자가 설정 화면에 직접 입력하는 수동 포트 포워딩, 오른쪽은 프로그램이 SSDP로 공유기를 찾아 자동 설정하는 UPnP를 비교합니다.", "UPnP는 포트 포워딩 설정을 프로그램이 대신하게 합니다.", p5),
    ("u12-upnp-mapping-request", "프로그램이 매핑을 요청하기", "Torrent가 자동 설정 서비스를 찾고 6881번 매핑을 요청하면 공유기 표에 198.51.100.25:6881 → 192.168.0.10:6881이 생기고 바깥 연결이 PC까지 들어옵니다.", "프로그램이 필요한 포트 포워딩을 공유기와 협의해 자동으로 설정합니다.", p6),
    ("u12-upnp-compare", "UPnP와 NAT를 함께 보기", "수동 설정은 사용자가, UPnP는 프로그램이 입력한다는 비교표와 공유기 지원·설정이 전제라는 조건을 보여 줍니다.", "UPnP는 사용자의 입력 부담을 줄여 P2P 연결을 돕습니다.", p7),
    ("u12-upnp-dev", "P2P 프로그램 개발로", "P2P 프로그램을 만들 때 서비스 발견, 매핑 요청, 주소·포트 매핑 이해를 차례로 챙기는 체크리스트입니다.", "서비스 발견과 매핑 요청은 NAT 환경 P2P 설계의 기본입니다.", p8),
]
assert len(ITEMS) == 8


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    fm = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-16\.svg\n(?:    .*\n)+", "", fm, count=1)
    for i, (f, t, al, c, _) in enumerate(ITEMS, 1):
        pid = f"advanced-source-16-page-{i:02d}"
        if f"assets/animations/{f}.svg" in fm:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        if f"- page_id: {pid}\n" in fm:
            fm = fm.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
        else:
            fm = fm.rstrip("\n") + f"\n- page_id: {pid}\n{blk}"
    md.write_text(head + "---\n" + fm + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        (LESSON / "assets" / "diagrams" / "source-16.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
