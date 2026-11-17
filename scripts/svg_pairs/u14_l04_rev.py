#!/usr/bin/env python3
"""Unit 14 Lesson 4 (집에서 사내 그룹웨어 열기: 원격 접속 VPN) SVG review: replaces the u14-l04-p?-* set of u14_l04_remote_vpn.py.
Run from repo root: python3 scripts/svg_pairs/u14_l04_rev.py   (--svg-only skips the lesson.md edit).

Running example: 박 팀장 노트북 192.168.0.20 / 집 공유기 192.0.2.123 / VPN 풀 10.10.99.0/24 (10.10.99.23) / 서울 SG 198.51.100.25
/ 도쿄 SG 198.51.100.20 / 사내 그룹웨어 192.168.10.50:8080.
Colour language: 안쪽 헤더 BLUE, 바깥 헤더·터널 VIOLET, 통과 GREEN, 막힘 RED, 주황은 방금 바뀐 요소만.
Moving packets are drawn before the device icons so they pass *behind* them (never over a label)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from kit import wire_items
from u14_l04_remote_vpn import mk, pmk, new, lap, mv, net, cloud, rt, srv, cell, hl  # noqa: F401
from u6_l03 import brace

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("10-vpn-and-security/lessons/restructured/04-*"))
OUT = LESSON / "assets" / "animations"

PRIV = "192.168.10.50"
SGIP = "198.51.100.25"


def L(x, y, s, c=MUTED, fs=16, w=None):
    return text(x, y, s, fs, c, w)


def sg(x, y, label="SG"):
    return booth(x, y, label)


# ================================================================ Page 1 (a): 집에서는 왜 안 열릴까?
def p1():
    a = new()
    Y = 265
    ip = PRIV + ":8080"
    body = [net(30, 125, 230, 280, "집", GREEN), net(680, 125, 250, 280, "서울 본사", BLUE),
            a.vis(line(200, Y, 695, Y, GREEN, 6), 4, 4),
            mv(a, packet(0, 0, ORANGE), [(235, Y), (585, Y)], 2, 2, 3, 0.1, 0.9),
            lap(145, Y, "노트북"), sg(735, Y), srv(875, Y), cloud(470, Y),
            pill(805, 195, ip, BLUE, 16, False), pmk(a, 805, 195, ip, 1),
            a.vis(cross(632, Y), 3, 3), mk(a, 608, Y - 24, 48, 48, 3),
            a.vis(pill(470, 360, "사설 주소라 길이 없어요", RED, 17, False), 3, 3),
            a.vis(pill(480, 442, "서버를 열지 않고 노트북을 안으로", GREEN, 18, True), 4, 4),
            pmk(a, 480, 442, "서버를 열지 않고 노트북을 안으로", 4, 18)]
    caps = ["박 팀장이 집에서 사내 그룹웨어를 열어요", "요청이 집을 나와 인터넷으로 가요", "사내 사설 주소는 인터넷에서 길이 없어요", "서버를 열지 않고 인증한 노트북을 들여요"]
    return frame(a, "집에서는 왜 안 열릴까?", "주소를 알아도 사설망 안쪽에는 못 가요", caps, "".join(body))


# ================================================================ Page 1 (b): 집 주소만 허용하면?
def p1b():
    a = new()
    Y = 270
    rule = "허용 192.0.2.123"
    body = [net(30, 125, 270, 280, "집", GREEN), net(650, 125, 280, 280, "서울 본사", BLUE),
            line(140, 225, 207, 262, LINE, 4, "8 6"), line(135, 322, 207, 285, LINE, 4, "8 6"),
            line(263, Y, 400, Y, LINE, 4, "8 6"), line(540, Y, 685, Y, LINE, 4, "8 6"), line(750, Y, 836, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, ORANGE), [(160, 312), (300, 271), (550, 270), (805, 270)], 2, 2, 2, 0.05, 0.6),
            lap(95, 205, "노트북"), phone(95, 325, "가족 기기"), rt(235, Y, "집 공유기"), cloud(470, Y),
            sg(715, Y, "방화벽"), srv(870, Y),
            a.vis(pill(235, 352, "192.0.2.123", BLUE, 16, False), 1, 2), a.vis(pill(235, 352, "192.0.2.123", BLUE, 16, False), 4, 4),
            a.vis(pill(235, 352, "주소가 바뀜", RED, 16, True), 3, 3), pmk(a, 235, 352, "주소가 바뀜", 3),
            pill(790, 190, rule, GREEN, 16, False), pmk(a, 790, 190, rule, 1),
            mk(a, 73, 285, 44, 76, 2),
            a.vis(pill(480, 440, "가족 기기도 같은 주소로 통과해요", RED, 17, False), 2, 2),
            a.vis(cross(630, Y), 3, 3), mk(a, 606, Y - 24, 48, 48, 3),
            a.vis(pill(480, 440, "주소가 바뀌면 박 팀장도 막혀요", RED, 17, False), 3, 3),
            a.vis(pill(480, 440, "내용은 암호화 없이 그대로 가요", RED, 17, False), 4, 4), pmk(a, 480, 440, "내용은 암호화 없이 그대로 가요", 4, 17)]
    caps = ["집 공유기의 공인 주소만 방화벽에서 허용해요", "가족 기기도 같은 주소라 그대로 통과해요", "집 주소가 바뀌면 박 팀장이 막혀요", "접속 내용도 보호되지 않아요"]
    return frame(a, "집 주소만 허용하면", "주소만 믿으면 사람과 기기를 못 가려요", caps, "".join(body))


# ================================================================ Page 2: VPN 클라이언트는 누구에게 말을 걸까?
def p2():
    a = new()
    Y = 300

    def card(val, c):
        s = box(45, 165, 200, 70, MUTED, PANEL, 8, sw=2) + L(145, 188, "VPN 서버 주소", MUTED, 16)
        s += box(60, 198, 170, 30, c, BG, 6, sw=2)
        return s + (text(145, 220, val, 17, c, 700) if val else "")

    body = [net(30, 125, 230, 290, "집", GREEN), net(660, 125, 280, 290, "서울 본사", BLUE),
            a.vis(line(200, Y, 685, Y, GREEN, 6), 3, 3),
            mv(a, packet(0, 0, ORANGE), [(235, Y), (585, Y)], 2, 2, 2, 0.1, 0.9),
            lap(145, Y, "노트북"), sg(725, Y), L(725, Y + 62, SGIP, BLUE, 15), srv(870, Y), L(870, Y + 84, PRIV, BLUE, 15), cloud(470, Y),
            a.vis(card("", MUTED), 1, 1), mk(a, 45, 165, 200, 70, 1),
            a.vis(card(PRIV, RED), 2, 2), mk(a, 60, 198, 170, 30, 2),
            a.vis(card(SGIP, GREEN), 3, 4), mk(a, 60, 198, 170, 30, 3),
            a.vis(cross(632, Y), 2, 2), mk(a, 608, Y - 24, 48, 48, 2),
            a.vis(pill(725, 215, "인증 통과", GREEN, 16, False) + check(725, 248), 3, 3), mk(a, 709, 232, 32, 32, 3),
            a.vis(pill(480, 442, "서버 주소 칸에는 SG의 공인 주소를 적어요", GREEN, 18, True), 4, 4),
            pmk(a, 480, 442, "서버 주소 칸에는 SG의 공인 주소를 적어요", 4, 18)]
    caps = ["VPN 설정에 서버 주소 칸이 있어요", "그룹웨어 서버 주소를 적으면 길이 없어요", "SG의 공인 주소를 적으면 SG가 인증해요", "그룹웨어 서버가 아니라 SG가 터널의 목적지예요"]
    return frame(a, "VPN 클라이언트가 말을 거는 곳", "터널의 목적지는 그룹웨어 서버가 아니라 SG예요", caps, "".join(body))


# ================================================================ Page 3: 노트북에 주소가 왜 두 개일까?
def p3():
    a = new()
    Y = 250
    pool = "풀 10.10.99.0/24"
    vp = "10.10.99.23"
    body = [line(165, Y, 420, Y, LINE, 4, "8 6"), line(540, Y, 785, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, BLUE), [(190, Y), (390, Y)], 1, 1, 1, 0.1, 0.9),
            mv(a, pill(0, 0, vp, ORANGE, 16, True), [(730, Y), (600, Y)], 2, 2, 2, 0.1, 0.9),
            rt(130, Y, "집 공유기"), lap(480, Y, "노트북"), sg(830, Y),
            a.vis(pill(830, 185, pool, GREEN, 16, False), 2, 3), pmk(a, 830, 185, pool, 2),
            a.vis(cell(330, 322, 300, 40, "집 구간  192.168.0.20", BLUE, 16), 1, 4), mk(a, 330, 322, 300, 40, 1),
            a.vis(cell(330, 370, 300, 40, "VPN 주소  " + vp, GREEN, 16) + check(668, 390), 3, 4), mk(a, 330, 370, 300, 40, 3),
            a.vis(pill(480, 448, "두 번째 주소는 사내망 참여 신호예요", GREEN, 18, True), 4, 4),
            pmk(a, 480, 448, "두 번째 주소는 사내망 참여 신호예요", 4, 18)]
    caps = ["집 공유기에서 받은 주소가 하나 있어요", "SG가 주소 풀에서 하나를 빌려줘요", "노트북에 VPN 주소가 하나 더 생겨요", "해킹이 아니라 사내망에 들어왔다는 뜻이에요"]
    return frame(a, "노트북에 주소가 두 개", "집 구간용 하나, 사내망용 하나예요", caps, "".join(body))


# ================================================================ Page 4: 집에서 나간 패킷은 어떻게 포장될까?
def p4():
    a = new()
    Y = 340
    inner = "안쪽 10.10.99.23 → " + PRIV
    o_home = "바깥 192.168.0.20 → " + SGIP
    o_nat = "바깥 192.0.2.123 → " + SGIP

    def hdr(x0, outer, with_frame=True):
        s = ""
        if outer:
            s += box(x0, 140, 360, 100, VIOLET, PANEL, 10, sw=3) + text(x0 + 180, 168, outer, 16, VIOLET, 700)
        return s + cell(x0 + 12, 188, 336, 42, inner, BLUE, 16)

    def ptr(x):
        return line(x, 244, x, 300, MUTED, 3, "4 5")

    def two(x0):
        r1 = f'<text x="{x0 + 180}" y="168" text-anchor="middle" font-size="16" font-weight="700" fill="{VIOLET}">집 192.0.2.123 → <tspan fill="{GREEN}">{SGIP}</tspan></text>'
        r2 = f'<text x="{x0 + 180}" y="204" text-anchor="middle" font-size="16" font-weight="700" fill="{VIOLET}">호텔 192.0.2.150 → <tspan fill="{GREEN}">{SGIP}</tspan></text>'
        return box(x0, 140, 360, 100, VIOLET, PANEL, 10, sw=3) + r1 + r2

    body = [line(165, Y, 418, Y, LINE, 4, "8 6"), line(542, Y, 806, Y, LINE, 4, "8 6"),
            lap(110, Y, "노트북"), rt(480, Y, "집 공유기"), sg(850, Y),
            a.vis(hdr(20, None) + ptr(110), 1, 1), mk(a, 32, 188, 336, 42, 1),
            a.vis(hdr(20, o_home) + ptr(110), 2, 2), mk(a, 20, 140, 360, 100, 2),
            a.vis(hdr(300, o_nat) + ptr(480), 3, 3), mk(a, 308, 148, 344, 40, 3),
            a.vis(pill(480, 432, "NAT-T: UDP 4500", BLUE, 16, False), 3, 3),
            a.vis(two(580) + ptr(850), 4, 4), mk(a, 580, 140, 360, 100, 4),
            a.vis(pill(480, 440, "집이든 호텔이든 출구는 같은 SG", GREEN, 18, True), 4, 4)]
    caps = ["원본 패킷은 안쪽 주소만 가지고 있어요", "노트북의 VPN 클라이언트가 한 겹 포장해요", "공유기가 바깥 출발지를 공인 주소로 바꿔요", "바깥 출발지가 바뀌어도 목적지는 SG예요"]
    return frame(a, "집에서 나간 패킷의 포장", "안쪽과 바깥 헤더를 따로 읽어요", caps, "".join(body))


# ================================================================ Page 5: 다른 지사 SG에 붙으면 길이 어떻게 될까?
def p5():
    a = new()
    tk = (460, 195)
    body = [a.vis(line(180, 322, 420, 207, LINE, 4, "8 6") + line(500, 207, 755, 325, LINE, 4, "8 6"), 1, 3),
            a.vis(line(190, 340, 745, 340, GREEN, 6), 4, 4),
            mv(a, packet(0, 0, ORANGE), [(180, 322), (460, 200), (750, 326)], 2, 2, 2, 0.1, 0.9),
            lap(130, 340, "노트북"), sg(*tk, ""), L(tk[0], 150, "도쿄 SG", MUTED, 17), sg(790, 340, "서울 SG"), srv(905, 340),
            a.vis(pill(240, 190, "도쿄 접속 프로필", ORANGE, 16, False), 1, 3), pmk(a, 240, 190, "도쿄 접속 프로필", 1),
            a.vis(pill(240, 190, "서울 SG 프로필", GREEN, 16, True), 4, 4), pmk(a, 240, 190, "서울 SG 프로필", 4),
            a.vis(pill(300, 240, "1구간", BLUE, 16, True) + pill(650, 240, "2구간", BLUE, 16, True), 2, 3), mk(a, 420, 160, 80, 48, 2),
            a.vis(cross(460, 275), 3, 3), mk(a, 436, 251, 48, 48, 3),
            a.vis(pill(480, 440, "서울 집 → 도쿄 → 서울", RED, 18, False), 3, 3),
            a.vis(check(470, 305), 4, 4), mk(a, 446, 281, 48, 48, 4)]
    caps = ["노트북에 지난 출장의 도쿄 프로필이 남아 있어요", "집에서 도쿄 SG, 다시 서울 SG로 두 번 터널을 지나요", "연결은 되지만 길이 돌아가 느려져요", "본사 SG로 직접 접속하게 프로필을 바꿔요"]
    return frame(a, "다른 지사 SG에 붙으면", "서울에서 서울로 가는데 도쿄를 거쳐요", caps, "".join(body))


# ================================================================ Page 6 (a): 서버는 박 팀장을 누구로 볼까?
def p6():
    a = new()
    Y = 330
    logcard = (box(700, 140, 240, 100, BLUE, PANEL, 10, sw=3) + L(820, 164, "서버 접속 로그", MUTED, 16)
               + cell(712, 174, 216, 30, "출발지 10.10.99.23", BLUE, 16) + L(820, 226, "192.0.2.123은 없어요", RED, 16, 700))
    vpncard = (box(300, 140, 260, 100, VIOLET, PANEL, 10, sw=3) + L(430, 164, "VPN 접속 기록", MUTED, 16)
               + cell(312, 174, 236, 30, "박 팀장 = 10.10.99.23", VIOLET, 16) + L(430, 226, "받은 시각도 함께 남아요", MUTED, 16))
    ok = "사내 PC와 같은 규칙 적용"
    body = [line(170, Y, 440, Y, LINE, 4, "8 6"), line(520, Y, 810, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, GREEN), [(810, Y), (480, Y), (170, Y)], 2, 2, 2, 0.05, 0.95),
            lap(110, Y, "노트북"), sg(480, Y), srv(850, Y),
            logcard, line(850, 244, 850, 288, MUTED, 3, "4 5"), mk(a, 700, 140, 240, 100, 1),
            a.vis(pill(480, 250, "10.10.99.23으로 응답", ORANGE, 16, True), 2, 2), pmk(a, 480, 250, "10.10.99.23으로 응답", 2),
            a.vis(pill(700, 440, ok, GREEN, 16, False) + check(572, 440), 3, 3), pmk(a, 700, 440, ok, 3),
            a.vis(vpncard + line(480, 244, 480, 296, MUTED, 3, "4 5") + line(560, 190, 700, 190, VIOLET, 3, "8 6")
                  + pill(630, 190, "맞춰 보기", VIOLET, 16, True), 4, 4), mk(a, 300, 140, 260, 100, 4)]
    caps = ["서버 로그의 출발지는 10.10.99.23이에요", "서버는 이 주소로 응답하고 SG가 포장해 줘요", "사내 PC처럼 사내용 허용 규칙을 받아요", "누구인지는 VPN 접속 기록과 맞춰 봐요"]
    return frame(a, "서버는 박 팀장을 누구로 볼까?", "서버에 남는 주소는 VPN 할당 주소예요", caps, "".join(body))


# ================================================================ Page 6 (b): 주소 네 종류
def p6b():
    a = new()
    Y = 262

    def tag(x, l1, l2, c):
        return box(x - 75, 118, 150, 58, c, PANEL, 8, sw=3) + L(x, 142, l1, MUTED, 16) + L(x, 164, l2, c, 16, 700) + line(x, 180, x, 224, MUTED, 3, "4 5")

    body = [line(165, Y, 298, Y, LINE, 4, "8 6"), line(362, Y, 570, Y, LINE, 4, "8 6"), line(650, Y, 810, Y, LINE, 4, "8 6"),
            lap(110, Y, "노트북"), rt(330, Y, "집 공유기"), sg(610, Y), srv(850, Y),
            a.vis(tag(330, "공유기 공인 주소", "192.0.2.123", VIOLET), 1, 1), mk(a, 255, 118, 150, 58, 1),
            a.vis(tag(110, "VPN 할당 주소", "10.10.99.23", BLUE), 2, 3), mk(a, 35, 118, 150, 58, 2),
            a.vis(tag(330, "공유기 공인 주소", "192.0.2.123", VIOLET), 2, 2),
            a.vis(brace(110, 850, 420, BLUE, "안쪽 통신 10.10.99.23 → " + PRIV, up=False, fs=17), 3, 3), a.vis(line(110, 340, 110, 408, BLUE, 3, "4 5") + line(850, 342, 850, 408, BLUE, 3, "4 5"), 3, 3), mk(a, 307, 430, 346, 34, 3),
            a.vis(tag(330, "공유기 공인 주소", "192.0.2.123", VIOLET), 4, 4),
            a.vis(brace(330, 610, 345, VIOLET, "바깥 터널 192.0.2.123 → " + SGIP, up=False, fs=17), 4, 4), mk(a, 290, 354, 360, 34, 4)]
    caps = ["집 공유기의 공인 주소는 바깥 출발지예요", "VPN 할당 주소는 사내망 안의 이름표예요", "안쪽 통신은 VPN 주소에서 서버로 가요", "바깥 터널은 공인 주소에서 SG로 가요"]
    return frame(a, "주소 네 종류 구분하기", "안쪽에서 쓰는 주소와 바깥에서 쓰는 주소", caps, "".join(body))


# ================================================================ Page 7: 전체 터널과 분할 터널
def p7():
    a = new()

    def panel(x0, title, c, full):
        s = box(x0, 120, 420, 275, c, PANEL, 16, sw=2) + text(x0 + 210, 152, title, 20, c, 700)
        s += line(x0 + 117, 270, x0 + 165, 270, LINE, 4, "8 6") + line(x0 + 245, 255, x0 + 310, 225, LINE, 4, "8 6")
        if full:
            s += line(x0 + 235, 290, x0 + 275, 322, LINE, 4, "8 6")
        else:
            s += line(x0 + 110, 294, x0 + 110, 355, LINE, 4, "8 6") + line(x0 + 110, 355, x0 + 265, 355, LINE, 4, "8 6")
        return s

    def icons(x0):
        return laptop(x0 + 65, 270, "노트북") + booth(x0 + 205, 270, "SG") + srv(x0 + 345, 200) + cloud(x0 + 335, 345, "외부 사이트")

    Lx, Rx = 40, 500
    ptL, ptR = "모든 트래픽에 회사 정책 적용", "사내 밖 트래픽은 보호 밖"
    body = [panel(Lx, "전체 터널", MUTED, True), panel(Rx, "분할 터널", GREEN, False),
            mv(a, packet(0, 0, BLUE), [(Lx + 125, 262), (Lx + 205, 262), (Lx + 285, 228)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, ORANGE), [(Lx + 125, 284), (Lx + 215, 286), (Lx + 260, 332)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(Rx + 125, 262), (Rx + 205, 262), (Rx + 285, 228)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, ORANGE), [(Rx + 110, 300), (Rx + 110, 355), (Rx + 215, 355)], 2, 2, 2, 0.1, 0.9),
            icons(Lx), icons(Rx),
            mk(a, Lx + 13, 236, 104, 60, 1), mk(a, Rx + 13, 236, 104, 60, 1),
            mk(a, Lx + 265, 305, 140, 80, 2), mk(a, Rx + 265, 305, 140, 80, 2),
            a.vis(pill(Lx + 235, 440, ptL, GREEN, 16, False, 310) + check(Lx + 50, 440)
                  + pill(Rx + 235, 440, ptR, RED, 16, False, 310) + cross(Rx + 50, 440), 3, 3),
            mk(a, Lx + 80, 423, 310, 34, 3), mk(a, Rx + 80, 423, 310, 34, 3),
            a.vis(pill(480, 440, "어느 쪽이든 대가가 있어 정책으로 정해요", GREEN, 18, True), 4, 4),
            pmk(a, 480, 440, "어느 쪽이든 대가가 있어 정책으로 정해요", 4, 18)]
    caps = ["VPN을 켠 노트북의 두 가지 설정을 비교해요", "밖으로 가는 트래픽의 길이 서로 달라요", "왼쪽은 정책 적용, 오른쪽은 보호 밖이에요", "속도와 통제를 맞바꾸니 정책으로 정해요"]
    return frame(a, "전체 터널과 분할 터널", "외부 사이트로 가는 길이 달라져요", caps, "".join(body))


ITEMS = [
    ("u14-l04-p1-private-no-route", "집에서는 왜 안 열릴까?",
     "박 팀장 노트북의 사내 그룹웨어 요청이 사설 주소라 인터넷에서 길을 찾지 못하고, 해결 방향은 서버를 열지 않고 인증한 노트북을 사내망으로 들이는 것임을 보여 줍니다.",
     "서버를 열지 않고 인증한 노트북을 사내망으로 들입니다.", p1, 2),
    ("u14-l04-p1b-allow-list-limits", "집 주소만 허용하면",
     "집 공유기의 공인 주소만 방화벽에서 허용하면 가족 기기도 통과하고, 주소가 바뀌면 박 팀장이 막히며, 접속 내용도 보호되지 않는다는 한계를 순서대로 보여 줍니다.",
     "주소만 믿는 방식은 누가, 어떤 기기인지 가려내지 못합니다.", p1b, 3),
    ("u14-l04-p2-server-address-box", "VPN 클라이언트가 말을 거는 곳",
     "VPN 서버 주소 칸에 그룹웨어 서버 주소를 적으면 길이 없고, SG의 공인 주소 198.51.100.25를 적으면 SG가 사용자를 확인한다는 순서를 보여 줍니다.",
     "서버 주소 칸에는 그룹웨어 서버가 아니라 회사 SG의 공인 주소를 적습니다.", p2, 1),
    ("u14-l04-p3-two-addresses-card", "노트북에 주소가 두 개",
     "노트북이 집 공유기에서 받은 집 구간 주소 192.168.0.20에 더해 SG의 주소 풀 10.10.99.0/24에서 10.10.99.23을 받는 과정을 보여 줍니다.",
     "두 번째 주소는 노트북이 사내망의 구성원이 되었다는 정상 신호입니다.", p3, 2),
    ("u14-l04-p4-header-card-path", "집에서 나간 패킷의 포장",
     "안쪽 10.10.99.23에서 192.168.10.50 패킷을 노트북이 포장하고, 집 공유기가 바깥 출발지를 192.0.2.123으로 바꾸어 SG 198.51.100.25로 보내며, 호텔에서 접속해도 목적지는 같은 SG임을 보여 줍니다.",
     "바깥 출발지가 집이든 호텔이든 터널의 출구는 같은 SG입니다.", p4, 3),
    ("u14-l04-p5-tokyo-detour", "다른 지사 SG에 붙으면",
     "서울 집의 노트북이 남아 있는 도쿄 프로필로 도쿄 SG를 거쳐 서울 SG로 가면 길이 돌아가 느려지고, 프로필을 서울 SG로 바꾸면 직접 접속하는 모습을 보여 줍니다.",
     "본사 SG로 직접 접속하도록 프로필을 바꾸면 경유지가 하나 줄어듭니다.", p5, 3),
    ("u14-l04-p6-server-log-view", "서버는 박 팀장을 누구로 볼까?",
     "사내 그룹웨어 서버 로그에는 출발지 10.10.99.23이 남고 192.0.2.123은 남지 않으며, 서버는 사내 PC처럼 응답하고 누구인지는 VPN 접속 기록과 맞춰 확인하는 모습입니다.",
     "서버에 남는 주소는 VPN 할당 주소이고, 사람은 VPN 기록으로 찾습니다.", p6, 2),
    ("u14-l04-p6b-four-addresses", "주소 네 종류 구분하기",
     "집 공유기의 공인 주소 192.0.2.123, VPN 할당 주소 10.10.99.23, 안쪽 통신, 바깥 터널을 한 길 위에 하나씩 올려 구분하는 그림입니다.",
     "안쪽 통신은 VPN 주소에서 서버로, 바깥 터널은 공인 주소에서 SG로 갑니다.", p6b, 4),
    ("u14-l04-p7-full-vs-split", "전체 터널과 분할 터널",
     "왼쪽 전체 터널은 외부 사이트 트래픽도 SG를 거치고, 오른쪽 분할 터널은 사내 서버 트래픽만 SG로 보내고 외부 사이트는 집 인터넷으로 바로 나가는 모습을 비교합니다.",
     "전체 터널은 정책 적용, 분할 터널은 속도라는 대가가 있어 정책으로 정합니다.", p7, 2),
]
WIRING = [[0, 1], [2], [3], [4], [5], [6, 7], [8]]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, _t, _al, _c, fn, _ap in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        pages = [[(ITEMS[i][0], ITEMS[i][1], ITEMS[i][2], ITEMS[i][3], ITEMS[i][5]) for i in grp] for grp in WIRING]
        wire_items(LESSON / "lesson.md", pages)
    print("ok", len(ITEMS), "svgs")
