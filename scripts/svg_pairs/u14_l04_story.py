#!/usr/bin/env python3
"""Unit 14 Lesson 4 situation SVGs (4 steps each, one per Page): 지우 + 박 팀장 remote-access VPN tickets.
Run from the repo root: python3 scripts/svg_pairs/u14_l04_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from u11_l01_story import ppl, mk_bubble, HY  # also applies the admin-tutorial ROLES

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("10-*/lessons/restructured/04-*")) / "assets" / "animations"


def say(a, x, y, s, who_x, color, t, w=None):
    return a.vis(bubble(x, y, s, tail_to=(who_x, 203), color=color, w=w), t, t) + mk_bubble(a, x, y, s, t, w)


def p1():
    a = new()
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "loading", "그룹웨어 열기"), 1, 1), a.vis(monitor(480, 285, "error", "응답이 없어요"), 2, 4), mark(a, 380, 229, 200, 112, 2),
         a.vis(pill(480, 150, "재택 첫날 아침 9시", MUTED, 17), 1, 1),
         say(a, 270, 150, "집에서는 사내 그룹웨어가\n안 열려요", 160, TERRACOTTA, 3),
         a.vis(thought(660, 150, "지사는 SG 두 대로 풀었는데\n집은 왜 다를까?", tail_to=(808, 200), color=BLUE), 3, 3),
         question(a, "집에는 어떤 입구가 필요할까?")]
    caps = ["박 팀장의 재택 첫날 아침 9시예요", "노트북에서 사내 그룹웨어를 열어도 응답이 없어요",
            "박 팀장의 티켓에 지우가 고민해요", "이 Page에서 집에 필요한 입구를 알아봐요"]
    return scene(a, "집에서는 왜 안 열릴까", "신입 네트워크 관리자 지우의 첫 번째 티켓이에요", caps, "".join(b), bg="home")


def p2():
    a = new()
    form = (box(380, 232, 200, 96, BLUE, PANEL, 10, sw=3) + text(480, 258, "VPN 클라이언트", 16, TXT, 700)
            + text(400, 290, "서버 주소", 16, MUTED, anchor="start") + box(400, 298, 160, 22, LINE, BG, 4, sw=2))
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(laptop(480, 285, "박 팀장 노트북"), 1, 1), a.vis(form, 2, 4), mark(a, 380, 232, 200, 96, 2),
         a.vis(thought(620, 150, "그룹웨어 주소를\n적고 싶겠지만…", tail_to=(480, 220), color=BLUE), 3, 3),
         question(a, "서버 주소 칸에 무엇을 적을까?")]
    caps = ["지우가 박 팀장 노트북에 VPN 클라이언트를 설치했어요", "설정 화면에 서버 주소를 적는 칸이 있어요",
            "그룹웨어 주소를 적고 싶겠지만 목적지가 아니에요", "이 Page에서 알맞은 주소를 알아봐요"]
    return scene(a, "서버 주소 칸에 뭘 적을까", "지우가 VPN 클라이언트 설정 화면을 열었어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    chips = "".join(box(x - 82, y - 17, 164, 34, c, BG, 8, sw=2) + text(x, y + 6, s, 16, TXT, 700)
                    for x, y, s, c in ((480, 262, "192.168.0.20", LINE), (480, 308, "10.10.99.23", LINE)))
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "VPN을 켠 노트북"), 1, 1),
         a.vis(box(380, 232, 200, 112, BLUE, PANEL, 10, sw=4) + chips + text(480, 224, "네트워크 화면", 16, MUTED), 2, 4), mark(a, 398, 291, 164, 34, 2),
         say(a, 290, 150, "IP가 두 개 생겼어요.\n해킹당한 거 아니에요?", 160, TERRACOTTA, 3),
         question(a, "새 주소는 정상일까?")]
    caps = ["VPN을 켠 박 팀장이 지우에게 메시지를 보내요", "네트워크 화면에 처음 보는 주소가 하나 더 보여요",
            "박 팀장이 해킹당한 건 아닌지 걱정해요", "이 Page에서 주소가 두 개인 이유를 알아봐요"]
    return scene(a, "노트북에 주소가 두 개", "박 팀장이 새 주소를 보고 놀랐어요", caps, "".join(b), bg="home")


def p4():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(laptop(400, 285, "집 노트북"), 1, 4), a.vis(booth(720, 285, "본사 SG"), 1, 4),
         a.vis(line(450, 285, 670, 285, LINE, 4, "10 8"), 2, 4),
         a.vis(parcel(520, 285) + ask(560, 250) + text(560, 330, "포장은 누가?", 17, TXT, 700), 2, 2), mark(a, 462, 228, 200, 134, 2),
         a.vis(thought(450, 150, "지사는 도쿄 SG가 대신\n포장해 줬는데…", tail_to=(190, 205), color=BLUE), 3, 3),
         question(a, "집 패킷은 누가 포장할까?")]
    caps = ["집과 본사 사이에는 SG가 하나뿐이에요", "노트북 쪽에는 포장해 줄 SG가 없어요",
            "도쿄 지사는 SG가 대신 포장해 줬어요", "이 Page에서 포장하는 쪽을 알아봐요"]
    return scene(a, "집에서 나간 패킷은 누가 포장할까", "지우가 집과 본사 사이를 그려 봐요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "서울 집 노트북"), 1, 1), a.vis(monitor(480, 285, "loading", "유난히 느려요"), 2, 4), mark(a, 380, 229, 200, 112, 2),
         a.vis(doc(660, 290, "지난달 출장 프로필"), 3, 3), mark(a, 622, 246, 76, 80, 3),
         a.vis(thought(660, 150, "서울 집에서 서울 본사로\n가는데 왜 느릴까?", tail_to=(808, 200), color=BLUE), 3, 3),
         question(a, "프로필은 어디로 접속할까?")]
    caps = ["박 팀장이 서울 집에서 그룹웨어를 열어요", "사내 그룹웨어가 유난히 느려요",
            "지난달 출장 때 쓰던 프로필이 남아 있어요", "이 Page에서 느린 이유를 알아봐요"]
    return scene(a, "그룹웨어가 왜 느릴까", "연결은 되는데 유난히 느리다는 티켓이에요", caps, "".join(b), bg="home")


def p6():
    a = new()
    log = (box(350, 232, 260, 112, BLUE, PANEL, 10, sw=4) + text(480, 256, "그룹웨어 접속 로그", 16, MUTED)
           + box(370, 270, 220, 34, LINE, BG, 8, sw=2) + text(480, 293, "출발지 10.10.99.23", 16, TXT, 700))
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(monitor(480, 285, "ok", "그룹웨어 관리 화면"), 1, 1), a.vis(log, 2, 4), mark(a, 368, 268, 224, 38, 2),
         a.vis(pill(700, 150, "박 팀장이 재택하는 날", MUTED, 17), 2, 2),
         a.vis(thought(660, 150, "이게 누구지?", tail_to=(190, 205), color=BLUE), 3, 3),
         question(a, "이 주소는 누구일까?")]
    caps = ["지우가 사내 그룹웨어 관리 화면을 열어요", "재택하는 날의 로그에 낯선 출발지가 찍혀 있어요",
            "지우가 이게 누구인지 질문을 받아요", "이 Page에서 서버가 보는 주소를 알아봐요"]
    return scene(a, "서버는 박 팀장을 누구로 볼까", "접속 로그를 읽는 지우예요", caps, "".join(b), bg="server_room")


def p7():
    a = new()
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "사내 그룹웨어"), 1, 1), a.vis(monitor(480, 285, "error", "화상회의가 끊겨요"), 2, 4), mark(a, 370, 229, 220, 112, 2),
         a.vis(thought(660, 150, "영상 사이트도 느리대요", tail_to=(808, 200), color=BLUE), 2, 2),
         say(a, 290, 150, "VPN 켜기 전에는\n잘 되던 건데요?", 160, TERRACOTTA, 3),
         question(a, "어느 트래픽을 터널로 보낼까?")]
    caps = ["VPN을 켜도 사내 그룹웨어는 열려요", "그런데 화상회의가 끊기고 있어요",
            "박 팀장이 켜기 전에는 잘 됐다고 말해요", "이 Page에서 터널로 보낼 범위를 알아봐요"]
    return scene(a, "VPN을 켜자 인터넷이 덜컥거려요", "박 팀장의 새 티켓이에요", caps, "".join(b), bg="home")


NAMES = ["cant-open", "server-address", "two-addresses", "who-packs", "slow-profile", "who-is-this", "video-cuts"]

if __name__ == "__main__":
    for i, (n, fn) in enumerate(zip(NAMES, (p1, p2, p3, p4, p5, p6, p7)), 1):
        write(OUT, f"u14-l04-p{i}-story-{n}", fn())
        print(f"u14-l04-p{i}-story-{n}.svg")
