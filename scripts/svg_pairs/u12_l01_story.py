#!/usr/bin/env python3
"""Unit 12 Lesson 1 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u12_l01_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES
from u11_l01_story import ppl, HY  # same cast helper as the reference story

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("08-*/lessons/restructured/01-*")) / "assets" / "animations"


def bm(a, x, y, s, t, fs=18):
    ls = wrap(s, fs)
    w, h = max(tw(ln, fs) for ln in ls) + 36, 26 * len(ls) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def screen(x, y, title, val):
    return (box(x - 95, y - 56, 190, 112, BLUE, PANEL, 10, sw=4) + text(x, y - 18, title, 16, MUTED)
            + text(x, y + 16, val, 20, TXT, 700)
            + f'<rect x="{x - 8}" y="{y + 56}" width="16" height="14" fill="{LINE}"/>'
            f'<rect x="{x - 36}" y="{y + 70}" width="72" height="7" rx="3" fill="{LINE}"/>')


def p1():
    a = new()
    s2 = "같은 주소를 입력해도\n화면이 안 떠요"
    s3 = "밖에서 못 쓰면 그룹웨어를\n들여놓은 보람이 없잖아요"
    b = [ppl(a, 120, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 560, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 880, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(340, 285, "ok", "사무실에선 열려요"), 1, 1), mark(a, 230, 229, 220, 112, 1),
         a.vis(monitor(340, 285, "error", "화면이 안 떠요"), 2, 4), mark(a, 230, 229, 220, 112, 2),
         a.vis(pill(120, 390, "거래처에서", MUTED, 17), 2, 4),
         a.vis(bubble(260, 150, s2, tail_to=(126, 203), color=TERRACOTTA), 2, 2),
         a.vis(bubble(700, 150, s3, tail_to=(872, 203), color=VIOLET), 3, 3), bm(a, 700, 150, s3, 3),
         question(a, "이 주소는 공유기 어느 쪽 주소일까?")]
    caps = ["사무실에서는 그룹웨어가 잘 열려요", "거래처에 간 박 팀장의 화면에는 아무것도 뜨지 않아요",
            "서 이사도 밖에서 못 쓰면 곤란하다고 해요", "이 Page에서 안 열리는 이유부터 물어봐요"]
    return scene(a, "사무실에선 되는데 밖에선 왜?", "박 팀장의 티켓이 들어왔어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    s = "주소를 정확히\n입력했다니까요"
    t = "주소가 틀리지 않았는데\n왜 안 될까?"
    b = [ppl(a, 120, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 830, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(doc(630, 285, "192.168.10.50"), 1, 4), mark(a, 560, 245, 140, 126, 1),
         a.vis(monitor(340, 285, "error", "응답이 없어요"), 2, 4), mark(a, 230, 229, 220, 112, 2),
         a.vis(bubble(260, 150, s, tail_to=(126, 203), color=TERRACOTTA), 3, 3), bm(a, 260, 150, s, 3),
         a.vis(thought(660, 150, t, tail_to=(822, 200), color=BLUE), 3, 3),
         question(a, "이 주소는 어떤 종류의 주소일까?")]
    caps = ["지우가 설치할 때 알려 준 주소는 192.168.10.50이에요", "고객사 노트북에서는 응답이 없어요",
            "박 팀장은 억울해요, 지우도 고개를 갸웃해요", "이 Page에서 주소의 종류를 알아봐요"]
    return scene(a, "주소는 맞게 입력했는데", "박 팀장은 억울하고 지우는 의문이에요", caps, "".join(b), bg="client")


def p3():
    a = new()
    s = "어느 게 진짜\n제 주소예요?"
    b = [ppl(a, 120, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 840, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(screen(340, 285, "네트워크 설정", "172.20.4.31"), 1, 4), mark(a, 240, 229, 200, 112, 1),
         a.vis(screen(600, 285, "내 IP 확인 사이트", "192.0.2.77"), 2, 4), mark(a, 500, 229, 200, 112, 2),
         a.vis(bubble(270, 150, s, tail_to=(126, 203), color=TERRACOTTA), 3, 3), bm(a, 270, 150, s, 3),
         question(a, "두 주소는 어디가 다를까?")]
    caps = ["고객사에서 연 노트북 설정에는 172.20.4.31이 적혀 있어요", "내 IP 확인 사이트에는 전혀 다른 192.0.2.77이 나와요",
            "박 팀장이 지우에게 전화를 걸어요", "이 Page에서 두 주소를 가려 봐요"]
    return scene(a, "내 주소가 둘이래요", "고객사의 박 팀장이 전화를 걸었어요", caps, "".join(b), bg="client")


def p4():
    a = new()
    s = "40명이 쓰면 주소도\n40개를 사야 하나요?"
    pcs = "".join(pc(x, 295) for x in (90, 170, 250))
    cloud = box(530, 229, 190, 112, MUTED, PANEL, 10, sw=3) + text(625, 278, "외부 클라우드", 17, TXT, 700) + text(625, 304, "저장소", 17, TXT, 700)
    b = [a.vis(pcs + text(170, 350, "직원 40명", 17, TXT, 700), 1, 4), mark(a, 50, 250, 240, 120, 1),
         ppl(a, 400, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 880, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left"),
         a.vis(cloud, 1, 4),
         a.vis(pill(625, 395, "회사 바깥 주소는 198.51.100.25 하나뿐", MUTED, 17), 2, 3), mark(a, 420, 375, 410, 42, 2),
         a.vis(bubble(640, 150, s, tail_to=(872, 203), color=VIOLET, fs=17), 3, 3), bm(a, 640, 150, s, 3, 17),
         question(a, "주소 하나로 40명이 쓸 수 있을까?")]
    caps = ["직원 40명이 동시에 외부 클라우드 저장소를 쓰고 있어요", "그런데 회사가 받은 바깥 주소는 하나뿐이에요",
            "서 이사가 비용부터 물어요", "이 Page에서 주소 하나로 되는 이유를 알아봐요"]
    return scene(a, "주소가 40개 필요할까", "서 이사의 질문을 받은 지우예요", caps, "".join(b), bg="office")


def p5():
    a = new()
    s2 = "밖에서 먼저는 못\n들어온다면서요."
    s3 = "NAT 뒤 서버는 안전한 거죠?\n방화벽 비용은 아껴도 되겠네요"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 1), ("happy", 2, 4)]),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         monitor(480, 285, "ok", "그룹웨어 서버"), mark(a, 380, 229, 200, 112, 1),
         a.vis(bubble(430, 150, s2, tail_to=(160, 203), color=VIOLET), 2, 2), bm(a, 430, 150, s2, 2),
         a.vis(bubble(450, 150, s3, tail_to=(160, 203), color=VIOLET, fs=17), 3, 3), bm(a, 450, 150, s3, 3, 17),
         question(a, "NAT 뒤에 있으면 정말 안전할까?")]
    caps = ["점심시간에 공유기 이야기를 들은 서 이사가 자신 있어 보여요", "서 이사가 들은 이야기를 되짚어요",
            "방화벽 비용을 아껴도 되겠냐고 물어요", "이 Page에서 이 추론의 빈틈을 찾아봐요"]
    return scene(a, "NAT 뒤라서 안전하겠죠?", "자신감이 붙은 서 이사의 질문이에요", caps, "".join(b), bg="office")


def p6():
    a = new()
    t = "박 팀장에게\n한 번에 설명해야 해"
    cards = "".join(a.vis(pill(480, y, s, TXT, 17), 2, 4) for y, s in ((215, "첫째 사설 주소를 알려 줬다"), (275, "둘째 공유기가 어디로 보낼지 모른다")))
    b = [ppl(a, 120, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 840, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], facing="left"),
         a.vis(doc(260, 300, "티켓 메모"), 1, 1), mark(a, 205, 262, 110, 118, 1),
         a.vis(clock(740, 330, "고객사 일정"), 1, 4),
         cards, mark(a, 290, 190, 380, 110, 2),
         a.vis(thought(300, 150, t, tail_to=(130, 200), color=BLUE), 3, 3),
         question(a, "공유기 한 상자를 기능별로 나누면?")]
    caps = ["고객사 일정이 코앞이라 박 팀장이 기다려요", "지우는 티켓 메모의 원인을 두 칸으로 정리해요",
            "한 번에 설명할 방법을 고민해요", "이 Page에서 공유기와 NAT를 구분해 봐요"]
    return scene(a, "박 팀장에게 뭐라고 설명할까", "티켓 메모를 정리하는 지우예요", caps, "".join(b), bg="office")


NAMES = ["office-vs-outside", "same-address-fails", "two-addresses", "forty-pcs-one-address", "nat-safe-question", "explain-to-park"]

if __name__ == "__main__":
    for i, (fn, n) in enumerate(zip((p1, p2, p3, p4, p5, p6), NAMES), 1):
        write(OUT, f"u12-l01-p0{i}-story-{n}", fn())
        print(f"u12-l01-p0{i}-story-{n}.svg")
