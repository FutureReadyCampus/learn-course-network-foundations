#!/usr/bin/env python3
"""Unit 14 Lesson 2 situation SVGs (4 steps each, one per Page): 터널을 지나는 패킷.
Run from the repo root: python3 scripts/svg_pairs/u14_l02_story.py"""
from pathlib import Path

from u11_l01_story import ppl, mk_bubble, mk_person  # noqa: F401  (reuse the Unit 11 reference helpers; also applies the admin ROLES)
from hangyeol_cast import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("10-*/lessons/restructured/02-*")) / "assets" / "animations"
HY = 225


def p1():
    a = new()
    q = "지사 PC에서 본사 그룹웨어가\n열리는지 봐 주실 수 있어요?"
    t = "서버 주소는 사설 주소인데\n요청은 어떻게 서울까지?"
    b = [a.vis(pill(480, 150, "도쿄 지사 SG 설치 첫날", MUTED, 17), 1, 1),
         ppl(a, 150, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 800, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(bubble(310, 160, q, tail_to=(168, 203), color=TERRACOTTA, w=300), 2, 2), mk_bubble(a, 310, 160, q, 2),
         a.vis(monitor(480, 285, "ok", "그룹웨어"), 3, 4), mark(a, 380, 229, 200, 112, 3),
         a.vis(thought(640, 150, t, tail_to=(790, 200), color=BLUE, w=320), 3, 3),
         question(a, "요청은 가장 먼저 어디로 갈까?")]
    caps = ["도쿄 지사에 SG를 설치한 첫날이에요", "박 팀장이 그룹웨어가 열리는지 봐 달라고 해요",
            "화면은 뜨는데 지우는 신기해요", "이 Page에서 요청의 첫 걸음을 따라가 봐요"]
    return scene(a, "지사 PC의 요청은 어디로", "박 팀장의 티켓을 받은 지우예요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(pc(350, 275, "지사 PC"), 1, 4),
         a.vis(packet(480, 275, BLUE) + text(480, 320, "목적지 192.168.10.50", 17, TXT, 700), 1, 4),
         a.vis(line(520, 275, 650, 275, LINE, 4, "10 8") + router(700, 275, "인터넷 라우터"), 2, 4), mark(a, 652, 237, 96, 100, 2),
         a.vis(thought(280, 150, "그대로 인터넷에\n내보내면 어떻게 될까?", tail_to=(150, 200), color=BLUE), 3, 3),
         question(a, "사설 주소 패킷이 인터넷을 건너려면?")]
    caps = ["지사 PC가 만든 원본 패킷의 목적지는 사설 주소예요", "패킷이 인터넷 라우터 쪽으로 향해요",
            "지우는 그대로 내보내면 어떻게 될지 떠올려요", "이 Page에서 건너는 방법을 알아봐요"]
    return scene(a, "사설 주소 패킷은 왜 못 건널까", "인터넷 라우터는 사설 주소로 가는 길을 몰라요", caps, "".join(b), bg="office")


def p3():
    a = new()
    t = "주소의 주인이 섞이면\n엉뚱한 곳을 보게 돼"
    asks = "".join(ask(x, y) for x, y in ((570, 240), (570, 330), (710, 240), (710, 330)))
    b = [ppl(a, 300, "지우", [("normal", 1, 1), ("worried", 2, 4)]),
         a.vis(doc(640, 285, "패킷 그림"), 1, 4),
         a.vis(asks + text(640, 392, "주소가 네 개", 17, TXT, 700), 2, 4), mark(a, 540, 205, 200, 160, 2),
         a.vis(thought(300, 150, t, tail_to=(300, 200), color=BLUE), 3, 3),
         question(a, "네 주소는 각각 누구의 것일까?")]
    caps = ["지우가 패킷 그림을 그리고 있어요", "출발지 두 개, 목적지 두 개 앞에서 손이 멈춰요",
            "주소의 주인이 섞이면 장애 때 엉뚱한 곳을 보게 돼요", "이 Page에서 주소의 주인을 정해 봐요"]
    return scene(a, "안쪽 IP와 바깥 IP", "지우가 주소 네 개 앞에서 멈췄어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    t = "지사의 요청은 서버에\n어떤 모습으로 도착할까?"
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         monitor(700, 285, "ok", "그룹웨어 서버"), a.vis(text(700, 392, "서울 본사", 17, MUTED), 1, 1),
         a.vis(lock(700, 190, GREEN) + text(700, 160, "외부 접속 차단", 17, TXT, 700), 2, 4), mark(a, 660, 170, 80, 64, 2),
         a.vis(thought(330, 150, t, tail_to=(210, 200), color=BLUE), 3, 3),
         question(a, "서울 SG를 지나면 어떤 모습일까?")]
    caps = ["본사 그룹웨어 서버는 사설망 안에서만 응답해요", "인터넷에서 직접 오는 접속은 받지 않아요",
            "그래도 지사의 요청은 받아 줘야 해요", "이 Page에서 서울 SG를 따라가 봐요"]
    return scene(a, "본사 SG는 포장을 어떻게 풀까", "서버는 인터넷에서 오는 요청을 직접 받지 못해요", caps, "".join(b), bg="office")


def p5():
    a = new()
    s = "VPN을 쓰면 통신사는 우리가 도쿄와 통신하는 것도 모르죠?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 4)], role_step1=True),
         ppl(a, 800, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(router(480, 285, "통신사") + eye(480, 215), 2, 4), mark(a, 430, 185, 100, 165, 2),
         a.vis(bubble(310, 150, s, tail_to=(168, 203), color=VIOLET, w=340), 3, 3), mk_bubble(a, 310, 150, s, 3, w=340),
         question(a, "통신사에게는 무엇이 보일까?")]
    caps = ["서 이사가 지우에게 다시 물어요", "통신사가 터널 구간의 패킷을 본다고 가정해요",
            "서 이사는 통신사가 도쿄와의 통신을 모를 거라고 생각해요", "이 Page에서 보이는 것과 가려지는 것을 나눠 봐요"]
    return scene(a, "터널 밖에서는 무엇이 보일까", "반은 맞고 반은 틀린 질문이에요", caps, "".join(b), bg="office")


def p6():
    a = new()
    s = "짧은 글은 잘 열리는데\n큰 첨부 파일을 올리면 멈춰요"
    t = "'한 겹 더 포장'이\n원인일 수 있어"
    b = [ppl(a, 150, "직원", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 800, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 285, "큰 첨부 파일"), 2, 4), mark(a, 435, 245, 90, 110, 2),
         a.vis(bubble(310, 150, s, tail_to=(168, 203), color=GREY, w=320), 2, 2),
         a.vis(thought(640, 150, t, tail_to=(790, 200), color=BLUE), 3, 3),
         question(a, "큰 파일만 멈추는 이유는?")]
    caps = ["지사 직원이 티켓을 올려요", "짧은 글은 되는데 큰 첨부 파일만 멈춰요",
            "터널도 그룹웨어도 정상이라 지우는 포장을 의심해요", "이 Page에서 포장의 대가를 알아봐요"]
    return scene(a, "포장 한 겹의 대가", "큰 첨부 파일만 멈춘다는 티켓이에요", caps, "".join(b), bg="office")


NAMES = {"p1": "first-hop", "p2": "private-wrap", "p3": "four-addresses", "p4": "unwrap", "p5": "isp-view", "p6": "big-file"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u14-l02-p{k[1]}-story-{NAMES[k]}", fn())
        print(f"u14-l02-p{k[1]}-story-{NAMES[k]}.svg")
