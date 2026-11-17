#!/usr/bin/env python3
"""Unit 12 Lesson 2 situation SVGs (4 steps each, one per Page 1-7): 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u12_l02_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from u11_l01_story import HY, mk_bubble, ppl  # noqa: F401  (also sets the admin-tutorial ROLES)

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("08-*/lessons/restructured/02-*")) / "assets" / "animations"
IP, EXT = "198.51.100.25", "198.51.100.25:53001"


def card(x, y, head, body, c=BLUE, w=300):
    """Two-line info card centred at (x, y): small head, bold body."""
    return box(x - w / 2, y - 34, w, 68, c, PANEL, 10, sw=3) + text(x, y - 8, head, 16, MUTED) + text(x, y + 20, body, 18, TXT, 700)


def srv(x, y, label="클라우드 저장소"):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{GREEN}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{GREEN}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, label, 18, TXT, 700))


def panel(x, y, w, h, title, c=BLUE):
    return box(x - w / 2, y - h / 2, w, h, c, PANEL, 10, sw=4) + text(x, y - h / 2 + 28, title, 17, TXT, 700)


def bars(x, y, n, w=260):
    return "".join(f'<rect x="{x - w / 2}" y="{y + i * 26}" width="{w}" height="12" rx="6" fill="{MUTED}" fill-opacity="0.45"/>' for i in range(n))


def p1():
    a = new()
    sp, sq = "동시에 올려도 답이\n안 섞이는 이유가 궁금해요", "공유기 주소로 보낸 요청이\n사라졌어요"
    tk = (box(535, 252, 210, 36, BLUE, BG, 6, sw=2) + text(640, 276, "서 이사의 질문", 16, TXT, 700)
          + box(535, 296, 210, 36, TERRACOTTA, BG, 6, sw=2) + text(640, 320, "박 팀장의 요청", 16, TXT, 700))
    b = [ppl(a, 130, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 400, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 860, "서 이사", [("normal", 1, 4)], facing="left", role_step1=True),
         box(525, 228, 230, 130, BLUE, PANEL, 10, sw=4) + a.vis(tk, 2, 4) + a.vis(text(640, 392, "티켓 두 건", 17, TXT, 700), 2, 2),
         mark(a, 520, 223, 240, 140, 2),
         a.vis(bubble(190, 150, sq, tail_to=(130, 203), color=TERRACOTTA), 2, 2), mk_bubble(a, 190, 150, sq, 2),
         a.vis(bubble(700, 150, sp, tail_to=(852, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, sp, 3),
         question(a, "답장은 어떻게 내 PC를 찾을까?")]
    caps = ["지우, 박 팀장, 서 이사가 한 사무실에 있어요", "지우의 모니터에 티켓 두 건이 올라왔어요",
            "서 이사는 답이 안 섞이는 이유를 궁금해해요", "이 Page에서 답이 제자리를 찾는 길을 알아봐요"]
    return scene(a, "티켓 두 건이 올라왔어요", "서 이사의 질문과 박 팀장의 요청이에요", caps, "".join(b), bg="office")


def p2():
    a = new()
    t = "같은 요청인데 숫자가 다르다\n도대체 어디가 바뀐 걸까?"
    b = [ppl(a, 120, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         pc(280, 290, "지우 PC"), srv(860, 290),
         line(330, 290, 800, 290, LINE, 4, "10 8"),
         card(580, 245, "공유기 안쪽 출발지", "192.168.10.41:3000", BLUE),
         a.vis(card(580, 335, "공유기 바깥쪽 출발지", EXT, MUTED), 2, 4), mark(a, 428, 300, 304, 72, 2),
         a.vis(thought(270, 150, t, tail_to=(125, 200), color=BLUE), 3, 3), mk_bubble(a, 270, 150, t, 3),
         question(a, "바뀐 곳은 어디일까?")]
    caps = ["지우 PC가 클라우드 저장소로 요청을 보냈어요", "공유기 바깥쪽에서는 출발지 숫자가 달라져 있어요",
            "지우는 같은 요청인데 왜 다른지 궁금해해요", "이 Page에서 무엇이 바뀌었는지 찾아봐요"]
    return scene(a, "같은 요청인데 숫자가 달라요", "안쪽과 바깥쪽에서 본 출발지를 지우가 비교해요", caps, "".join(b), bg="office")


def p3():
    a = new()
    s = "이 IP로 누가 썼는지\n알 수 있나요?"
    rows = "".join(box(340, 262 + i * 34, 280, 28, MUTED, BG, 5, sw=2) + text(480, 282 + i * 34, "출발지 " + IP, 16, TXT, 700) for i in range(3))
    b = [ppl(a, 140, "서 이사", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         panel(480, 300, 320, 160, "클라우드 저장소 접속 기록"), a.vis(rows, 2, 4), mark(a, 330, 252, 300, 112, 2),
         a.vis(bubble(300, 150, s, tail_to=(150, 203), color=VIOLET), 3, 3), mk_bubble(a, 300, 150, s, 3),
         question(a, "IP만 보고 사람을 알 수 있을까?")]
    caps = ["서 이사가 클라우드 저장소 관리 화면을 열어 봐요", "접속 기록의 출발지가 직원 전원 똑같아요",
            "서 이사가 누가 썼는지 물어요", "이 Page에서 서버가 무엇을 보는지 알아봐요"]
    return scene(a, "접속 기록이 전부 똑같아요", "서 이사가 고개를 갸웃했어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    t = "열 이름이 낯설다\n무엇이 어디에 적힐까?"
    hd = "".join(text(x, 276, s, 17, TXT, 700) for x, s in ((470, "Local"), (590, "Remote"), (710, "External")))
    b = [ppl(a, 190, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         panel(590, 300, 400, 170, "공유기 NAT 세션 목록"), a.vis(hd, 2, 4), bars(590, 302, 3, 340),
         mark(a, 410, 254, 360, 32, 2),
         a.vis(thought(300, 150, t, tail_to=(195, 200), color=BLUE), 3, 3), mk_bubble(a, 300, 150, t, 3),
         question(a, "변환표 한 줄에는 무엇이 적힐까?")]
    caps = ["지우가 공유기 관리 화면에서 NAT 세션 목록을 열어요", "Local, Remote, External이라는 열 이름이 보여요",
            "지우는 열 이름이 낯설어요", "이 Page에서 한 줄을 읽는 법을 알아봐요"]
    return scene(a, "열 이름이 낯설어요", "공유기 관리 화면의 NAT 세션 목록이에요", caps, "".join(b), bg="office")


def p5():
    a = new()
    t = "공유기는 이 응답을 어떻게\n지우 PC로 돌려보낼까?"
    b = [srv(120, 290), router(610, 290, "공유기"), line(170, 290, 570, 290, LINE, 4, "10 8"),
         ppl(a, 850, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(card(380, 235, "저장소가 보낸 응답의 목적지", EXT, GREEN, 330), 2, 4), mark(a, 213, 199, 334, 74, 2),
         a.vis(thought(660, 150, t, tail_to=(840, 200), color=BLUE), 3, 3), mk_bubble(a, 660, 150, t, 3),
         question(a, "응답은 어느 PC로 갈까?")]
    caps = ["클라우드 저장소가 응답을 보낼 차례예요", "응답의 목적지는 지우 PC가 아니라 바깥 주소와 포트예요",
            "지우는 공유기가 어떻게 돌려보낼지 궁금해요", "이 Page에서 돌아오는 길을 따라가 봐요"]
    return scene(a, "답장이 공유기에 도착했어요", "목적지가 지우 PC의 주소가 아니에요", caps, "".join(b), bg="office")


def p6():
    a = new()
    t = "둘 다 출발지가 똑같은데\n답은 어떻게 안 섞일까?"
    lg = "".join(box(470, 255 + i * 34, 220, 28, MUTED, BG, 5, sw=2) + text(580, 275 + i * 34, "출발지 " + IP, 16, TXT, 700) for i in range(2))
    b = [ppl(a, 100, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         pc(250, 290, "지우 PC"), pc(390, 290, "동료 PC"), srv(850, 290),
         line(440, 290, 800, 290, LINE, 4, "10 8"),
         a.vis(text(250, 395, "192.168.10.41", 16, MUTED) + text(390, 395, "192.168.10.43", 16, MUTED), 1, 1),
         a.vis(lg, 2, 4), mark(a, 460, 245, 240, 80, 2),
         a.vis(thought(270, 150, t, tail_to=(105, 200), color=BLUE), 3, 3), mk_bubble(a, 270, 150, t, 3),
         question(a, "두 응답은 어떻게 구별될까?")]
    caps = ["지우 PC와 동료 PC가 같은 저장소에 동시에 요청해요", "저장소가 보는 출발지는 둘 다 똑같아요",
            "그런데도 응답은 서로 섞이지 않아요", "이 Page에서 구별하는 방법을 알아봐요"]
    return scene(a, "동시에 물어도 답이 안 섞여요", "두 PC가 같은 저장소에 요청을 보냈어요", caps, "".join(b), bg="office")


def p7():
    a = new()
    t = "요청은 공유기에 도착하는데\n화면은 왜 안 나타날까?"
    b = [ppl(a, 120, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 860, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         router(640, 290, "공유기"),
         a.vis(pill(330, 200, "198.51.100.25:8080", TXT, 17), 2, 4) + a.vis(monitor(330, 290, "error", "열리지 않음"), 2, 4), mark(a, 220, 232, 220, 118, 2),
         a.vis(thought(690, 150, t, tail_to=(850, 200), color=BLUE), 3, 3), mk_bubble(a, 690, 150, t, 3),
         question(a, "요청은 왜 공유기에서 사라질까?")]
    caps = ["박 팀장은 거래처에서 그룹웨어에 접속해 봐요", "공유기 바깥 주소로 열어 봐도 화면이 나타나지 않아요",
            "지우는 요청이 도착하는데 왜 안 열리는지 생각해요", "이 Page에서 요청이 사라지는 이유를 알아봐요"]
    return scene(a, "박 팀장의 화면이 열리지 않아요", "거래처에서 그룹웨어에 접속하는 중이에요", caps, "".join(b), bg="office")


NAMES = ["reply-ticket", "numbers-differ", "same-ip-log", "table-columns", "reply-arrives", "two-pcs", "groupware-blocked"]

if __name__ == "__main__":
    for i, (nm, fn) in enumerate(zip(NAMES, (p1, p2, p3, p4, p5, p6, p7)), 1):
        write(OUT, f"u12-l02-p0{i}-story-{nm}", fn())
        print(f"u12-l02-p0{i}-story-{nm}.svg")
