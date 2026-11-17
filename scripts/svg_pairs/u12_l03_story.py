#!/usr/bin/env python3
"""Unit 12 Lesson 3 situation SVGs (4 steps each, one per Page), admin-tutorial story: 지우 + 포트 포워딩 티켓.
Run from the repo root: python3 scripts/svg_pairs/u12_l03_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("08-*/lessons/restructured/03-*")) / "assets" / "animations"
HY = 225


def ppl(a, x, who, moods, facing="right"):
    """moods = [(mood, t0, t1), ...]; the role line shows only in the first step of the first segment."""
    out = ""
    for i, (mood, t0, t1) in enumerate(moods):
        if i == 0:
            out += a.vis(person(x, HY, who, mood, facing=facing, role=who in ROLES), t0, t0)
            if t1 > t0:
                out += a.vis(person(x, HY, who, mood, facing=facing), t0 + 1, t1)
        else:
            out += a.vis(person(x, HY, who, mood, facing=facing), t0, t1)
    return out


def mk_bubble(a, x, y, s, t, fs=18):
    lines = wrap(s, fs)
    w = max(tw(ln, fs) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def p1():
    a = new()
    q = "그렇게 열어 두면 아무나\n들어오는 거 아니에요?"
    b = [ppl(a, 110, "박 팀장", [("normal", 1, 4)]),
         ppl(a, 340, "지우", [("normal", 1, 1), ("thinking", 2, 4)]),
         a.vis(thought(240, 140, "출장 중에도 전자결재를\n바로 처리하고 싶다", tail_to=(120, 200), color=TERRACOTTA), 1, 1),
         a.vis(router(600, 262, "공유기") + pill(600, 352, "바깥 8080 → 그룹웨어 서버", GREEN, 17), 2, 4),
         mark(a, 470, 326, 260, 54, 2),
         ppl(a, 850, "서 이사", [("worried", 3, 4)], facing="left"),
         a.vis(bubble(690, 150, q, tail_to=(838, 203), color=VIOLET), 3, 3), mk_bubble(a, 690, 150, q, 3),
         question(a, "줄을 미리 적어 두면 어떨까?")]
    caps = ["박 팀장은 다음 주 거래처 출장 중에도 결재를 하고 싶어요", "지우가 공유기에 한 줄을 적기로 해요",
            "이 말을 들은 서 이사가 물어요", "이 Page에서 미리 적는 줄을 알아봐요"]
    return scene(a, "출장 중에도 결재하고 싶어요", "박 팀장의 요청으로 시작해요", caps, "".join(b), bg="office")


def p2():
    a = new()
    rows = ("서비스(외부) 포트", "프로토콜", "내부 IP", "내부 포트", "원격지")
    form = box(470, 180, 340, 190, BLUE, PANEL, 10, sw=3) + "".join(
        box(486, 192 + i * 34, 308, 28, LINE, BG, 4, sw=2) + text(500, 212 + i * 34, r, 16, TXT, 700, "start") for i, r in enumerate(rows))
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("worried", 3, 4)]),
         a.vis(monitor(560, 285, "ok", "포트 포워딩 메뉴"), 1, 1),
         a.vis(form, 2, 4), mark(a, 462, 172, 356, 206, 2),
         a.vis(thought(330, 158, "엉뚱한 곳으로 가거나\n어디로도 가지 않는다", tail_to=(212, 200), color=BLUE), 3, 3),
         question(a, "칸마다 바깥 값일까, 안쪽 값일까?")]
    caps = ["지우가 공유기 설정 화면의 포트 포워딩 메뉴를 열었어요", "채울 칸이 다섯 개 보여요",
            "한 칸이라도 잘못 채우면 걱정이 돼요", "이 Page에서 칸마다 어느 쪽 값인지 알아봐요"]
    return scene(a, "설정 화면의 칸 채우기", "포트 포워딩 메뉴를 연 지우예요", caps, "".join(b), bg="office")


def p3():
    a = new()
    b = [ppl(a, 160, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 810, "박 팀장", [("normal", 1, 4)], facing="left"),
         a.vis(pill(485, 290, "규칙은 넣었다", GREEN, 20), 1, 1),
         a.vis(pill(485, 290, "192.168.10.50:8080", MUTED, 20) + cross(655, 290) + text(485, 340, "바깥에서 통하지 않아요", 17, TXT, 700), 2, 4),
         mark(a, 330, 258, 350, 94, 2),
         a.vis(thought(340, 158, "박 팀장에게\n어떤 주소를 알려 줄까?", tail_to=(172, 200), color=BLUE), 3, 3),
         question(a, "박 팀장에게 알려 줄 주소는?")]
    caps = ["규칙은 넣었어요", "사설 주소는 바깥에서 통하지 않아요",
            "지우는 박 팀장에게 알려 줄 주소를 고민해요", "이 Page에서 알려 줄 주소를 찾아봐요"]
    return scene(a, "박 팀장에게 어떤 주소를?", "규칙을 넣은 뒤의 지우예요", caps, "".join(b), bg="office")


def p4():
    a = new()
    b = [ppl(a, 160, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(pill(430, 300, "8080 → 그룹웨어 서버", GREEN, 17), 1, 2),
         ppl(a, 840, "직원", [("normal", 2, 4)], facing="left"),
         a.vis(doc(640, 280, "공유 자료 NAS"), 2, 4), mark(a, 570, 236, 140, 130, 2),
         a.vis(pill(640, 200, "밖에서 열어 달라", TERRACOTTA, 17), 2, 2),
         a.vis(thought(340, 158, "규칙을 하나 더\n넣으면 될 것 같다", tail_to=(172, 200), color=BLUE), 3, 3),
         question(a, "규칙 하나는 몇 곳으로 보낼 수 있을까?")]
    caps = ["그룹웨어 서버를 열고 나니 요청이 더 와요", "직원들이 모아 두는 공유 자료 NAS도 열어 달래요",
            "지우는 규칙을 하나 더 넣으면 될 것 같아요", "이 Page에서 규칙 하나의 한계를 확인해요"]
    return scene(a, "요청이 하나 더 들어왔어요", "그룹웨어 서버 다음은 공유 자료 NAS예요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 170, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(pill(430, 200, "198.51.100.25:8080", BLUE, 17), 1, 4),
         a.vis(monitor(430, 300, "error", "화면이 안 떠요"), 1, 4), mark(a, 330, 238, 200, 124, 1),
         a.vis(thought(330, 140, "규칙이 틀렸나?", tail_to=(182, 200), color=BLUE), 2, 2),
         ppl(a, 810, "직원", [("happy", 3, 4)], facing="left"),
         a.vis(bubble(690, 150, "집에서 시험하니\n열려요", tail_to=(798, 203), color=GREY), 3, 3), mk_bubble(a, 690, 150, "집에서 시험하니\n열려요", 3),
         question(a, "안쪽에서만 왜 안 될까?")]
    caps = ["지우가 사무실 자리에서 공인 주소를 쳐 봤어요", "화면이 뜨지 않아 설정을 뒤적여요",
            "같은 규칙으로 집에서 시험한 직원은 열린대요", "이 Page에서 안쪽 시험이 안 되는 이유를 알아봐요"]
    return scene(a, "사무실에서만 안 열려요", "같은 규칙인데 시험하는 자리가 달라요", caps, "".join(b), bg="office")


def p6():
    a = new()
    b = [ppl(a, 170, "지우", [("normal", 1, 2), ("worried", 3, 4)]),
         a.vis(pill(450, 222, "198.51.100.25:8080", BLUE, 17) + phone(450, 290, "휴대폰 데이터"), 1, 4),
         a.vis(cross(520, 290), 2, 4), mark(a, 496, 266, 48, 48, 2),
         a.vis(thought(340, 155, "규칙은 분명히\n넣었는데", tail_to=(182, 200), color=BLUE), 3, 3),
         question(a, "어디부터 확인해 갈까?")]
    caps = ["이번에는 휴대폰 데이터로 시험해요", "그런데도 열리지 않아요",
            "규칙은 분명히 넣었어요", "이 Page에서 확인 순서를 정해 봐요"]
    return scene(a, "밖에서도 안 열려요", "휴대폰 데이터로 시험한 지우예요", caps, "".join(b), bg="office")


def p7():
    a = new()
    q = "8080을 열면 박 팀장만\n들어와요?"
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(monitor(480, 285, "ok", "점검 끝"), 1, 4),
         ppl(a, 830, "서 이사", [("worried", 2, 4)], facing="left"),
         a.vis(bubble(670, 160, q, tail_to=(818, 205), color=VIOLET), 2, 2), mk_bubble(a, 670, 160, q, 2),
         a.vis(thought(340, 158, "서 이사의 질문이\n다시 떠오른다", tail_to=(212, 200), color=BLUE), 3, 3),
         question(a, "포트를 열어도 괜찮을까?")]
    caps = ["지우가 규칙을 모두 점검했어요", "서 이사가 8080에 대해 물어요",
            "지우는 서 이사의 질문이 다시 떠올라요", "이 Page에서 열린 포트의 위험을 따져 봐요"]
    return scene(a, "열어 두면 누가 들어올까", "점검을 끝낸 지우와 서 이사예요", caps, "".join(b), bg="office")


NAMES = ["rule-line", "form-fields", "which-address", "second-request", "office-test", "still-closed", "who-comes-in"]

if __name__ == "__main__":
    for i, (nm, fn) in enumerate(zip(NAMES, (p1, p2, p3, p4, p5, p6, p7)), 1):
        write(OUT, f"u12-l03-p0{i}-story-{nm}", fn())
        print(f"u12-l03-p0{i}-story-{nm}.svg")
