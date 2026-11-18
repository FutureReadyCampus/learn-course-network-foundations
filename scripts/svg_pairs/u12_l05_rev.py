#!/usr/bin/env python3
"""Unit 12 Lesson 5 SVG review: revised / added 4-step SVGs (Page 1-7). Imports only; old generators untouched.
Run from repo root: python3 scripts/svg_pairs/u12_l05_rev.py  (--svg-only skips the lesson.md edit).
Example: 박 팀장 집 192.168.0.20 / 192.0.2.123, 지우 192.168.10.41 / 198.51.100.25, 주소 확인·STUN·TURN 203.0.113.60, 협력사 203.0.113.99 / .15."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403
from kit import wire_items

LESSON = lesson_dir(5)
OUT = LESSON / "assets" / "animations"
HOME, HOMEWAN, STUN, JIWOO, JIWOOWAN = "192.168.0.20", "192.0.2.123", "203.0.113.60", "192.168.10.41", WAN


def pw(s, fs):
    return tw(s, fs) + 28


# ---------------- Page 1 ----------------
def p1():
    p = Pg("포트를 안 열었는데 화상회의는?", "둘 다 바깥으로 먼저 연결하면 막히지 않아요",
           ["양쪽 모두 공유기 뒤에 있고 포트는 안 열었어요", "둘 다 서비스 서버로 먼저 연결해요",
            "영상과 음성이 서버를 거쳐 오가요", "먼저 나간 통신에는 행이 자동으로 생겨요"])
    Y = 320
    p.base(line(146, Y, 222, Y, LINE, 4, "8 6"), line(278, Y, 440, Y, LINE, 4, "8 6"),
           line(520, Y, 682, Y, LINE, 4, "8 6"), line(738, Y, 814, Y, LINE, 4, "8 6"))
    p.fly(packet(0, 0, BLUE), [(146, Y), (440, Y)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, BLUE), [(814, Y), (520, Y)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, GREEN), [(290, Y - 14), (670, Y - 14)], 3, 0.05, 0.95)
    p.fly(packet(0, 0, GREEN), [(670, Y + 14), (290, Y + 14)], 3, 0.05, 0.95)
    p.base(laptop(90, Y, "박 팀장"), rt(250, Y), dsrv(480, Y, "서비스 서버"), rt(710, Y), laptop(870, Y, "협력사"))
    for x in (250, 710):
        p.base(lock(x, 185, MUTED), pill(x, 243, "포트 닫힘", MUTED, 16, False, 120))
    p.mark((446, Y - 38, 68, 76), 2)
    p.at(check(480, Y - 75), 3, 4, mark=(458, Y - 97, 44, 44))
    p.at(pill(480, 435, "먼저 나간 통신은 행이 생겨 포트가 필요 없어요", GREEN, 17, True, 500), 4, 4)
    return p.render()


def p1b():
    p = Pg("서버 없이 직접 주고받으면 어떨까?", "소개 서버는 주소만 알려 주고, 첫 패킷은 막힐 수 있어요",
           ["P2P는 두 기기가 서버 없이 직접 주고받아요", "소개 서버는 상대의 바깥 주소만 알려 줘요",
            "먼저 보낸 패킷은 맞는 행이 없어 막힐 수 있어요", "직접 통신에는 두 가지가 맞아야 해요"])
    Yd, Yl = 365, 300
    p.base(line(90, Yd - 30, 90, Yl, LINE, 4, "8 6"), line(90, Yl, 870, Yl, LINE, 4, "8 6"), line(870, Yl, 870, Yd - 30, LINE, 4, "8 6"))
    p.at(line(452, 215, 266, Yd - 36, BLUE, 3, "8 6") + line(508, 215, 694, Yd - 36, BLUE, 3, "8 6"), 2, 2)
    p.fly(packet(0, 0, BLUE), [(440, 215), (276, Yd - 44)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, BLUE), [(520, 215), (684, Yd - 44)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(110, Yl), (650, Yl)], 3, 0.05, 0.95)
    p.base(laptop(90, Yd, "박 팀장"), rt(250, Yd), rt(710, Yd), laptop(870, Yd, "협력사"), dsrv(480, 175, "") + text(528, 182, "소개 서버", 18, TXT, 700, anchor="start"))
    p.at(pill(480, 440, "P2P: 서버 없이 직접 주고받기", ORANGE, 17, True, 380), 1, 1)
    p.at(pill(480, 440, "소개 서버는 상대의 바깥 주소만 알려 줘요", BLUE, 17, False, 440), 2, 2)
    p.at(cross(690, Yl) + pill(480, 440, "상대 공유기에 맞는 행이 없어 막혀요", RED, 17, False, 400), 3, 3, mark=(668, Yl - 22, 44, 44))
    p.at(pill(290, Yl, "① 내 공유기가 바깥에 어떻게 보이나", ORANGE, 16, True, 360) + pill(670, Yl, "② 상대의 첫 패킷을 받아 주나", ORANGE, 16, True, 320), 4, 4)
    return p.render()


# ---------------- Page 2 ----------------
def p2():
    p = Pg("NAT에게 꼭 따로 물어야 할 두 가지", "이름 하나로 연결 가능성을 판단하지 않아요",
           ["지우의 메모는 이름만 보고 안 될 거라 판단했어요", "첫째 질문은 매핑: 바깥에 어떻게 보이나요",
            "둘째 질문은 필터링: 누가 보낸 패킷을 받나요", "그래서 두 질문을 따로 확인한다고 고쳐요"])
    PX, PY = 175, 228
    p.at(cell(180, 118, 600, 44, "지우 메모: Port Restricted라서 안 될 거야", RED, 17), 1, 3)
    p.at(cell(180, 118, 600, 44, "새 메모: 매핑과 필터링을 따로 확인한다", GREEN, 17) + check(810, 140), 4, 4, mark=(180, 118, 600, 44))
    p.base(line(127, 310, 175, 310, LINE, 3, "8 6"), line(625, 310, 806, 310, LINE, 3, "8 6"))
    p.base(laptop(75, 310, "안쪽 PC"), pc(850, 310, "바깥 상대"))
    p.base(box(PX, PY, 450, 150, LINE, PANEL, 12, sw=2) + lbl(PX + 225, PY + 24, "공유기의 변환표", MUTED, 16)
           + cell(PX + 15, PY + 36, 205, 32, "Internal", MUTED, 16, BG) + cell(PX + 230, PY + 36, 205, 32, "External", MUTED, 16, BG)
           + cell(PX + 15, PY + 76, 205, 44, HOME + ":3000", BLUE, 16) + cell(PX + 230, PY + 76, 205, 44, HOMEWAN + ":40001", BLUE, 16))
    p.base(f'<rect x="652" y="262" width="20" height="96" rx="5" fill="{GREEN}" fill-opacity="0.35" stroke="{GREEN}" stroke-width="3"/>')
    p.at(pill(480, 198, "그런데 회의는 잘 되고 있어요", GREEN, 17, False, 320), 1, 1)
    p.at(pill(400, 198, "① 매핑: 바깥에 어떤 주소·포트로 보이나?", BLUE, 16, False, 420), 2, 4, mark=(PX + 230, PY + 76, 205, 44))
    p.fly(packet(0, 0, BLUE), [(800, 310), (700, 310)], 3, 0.05, 0.95)
    p.at(pill(700, 412, "② 필터링: 누가 보낸 패킷까지 받나?", GREEN, 16, False, 370), 3, 4, mark=(652, 262, 20, 96))
    return p.render()


# ---------------- Page 3 ----------------
def p3():
    p = Pg("상대가 바뀌면 바깥 포트도 바뀔까?", "주소 확인 서버가 본 주소가 협력사에도 맞는지 봐요",
           ["서버가 본 바깥 주소를 협력사에 알려 줬어요", "이제 같은 PC가 협력사와도 통신해요",
            "상대가 바뀌자 오른쪽만 :40017로 달라져요", "소개한 주소가 협력사에는 안 맞아요"])
    cols = [(30, GREEN, "상대와 무관한 매핑", GREEN, GREEN), (490, BLUE, "상대에 따라 달라지는 매핑", BLUE, RED)]
    PCY, SVY, PRY = 335, 252, 410
    p.at(pill(480, 130, "서버가 본 주소 " + HOMEWAN + ":40001 → 협력사에 알려 줌", ORANGE, 16, False, 560), 1, 4, mark=(200, 114, 560, 32))
    for x, c, head, c1, c2 in cols:
        p.base(box(x - 15, 158, 450, 312, c, "none", 14, sw=2), lbl(x + 210, 186, head, c, 18),
               line(x + 110, PCY, x + 157, PCY, LINE, 3, "8 6"), line(x + 211, PCY - 12, x + 338, SVY - 4, LINE, 3, "8 6"))
        p.at(line(x + 211, PCY + 12, x + 336, PRY - 10, LINE, 3, "8 6"), 2, 4)
        p.fly(packet(0, 0, BLUE), [(x + 220, PCY + 18), (x + 322, PRY - 18)], 2, 0.05, 0.95)
    for x, c, head, c1, c2 in cols:
        p.base(laptop(x + 55, PCY, "박 팀장 PC"), rt(x + 185, PCY), dsrv(x + 375, SVY, "주소 확인 서버"), pc(x + 375, PRY, "협력사"))
        p.base(pill(x + 262, PCY - 37, ":40001", c1, 16, False, 86))
        p.at(pill(x + 268, PCY + 39, ":40001" if c2 == GREEN else ":40017", c2, 16, False, 86), 3, 4, mark=((x + 225, PCY + 23, 86, 32) if c2 == RED else None))
        p.mark((x + 341, PRY - 46, 68, 62), 2)
    p.at(check(30 + 410, PRY - 25), 4, 4, mark=(30 + 394, PRY - 41, 32, 32))
    p.at(cross(490 + 410, PRY - 25), 4, 4, mark=(490 + 394, PRY - 41, 32, 32))
    return p.render()


# ---------------- Page 4 ----------------
def p4():
    p = Pg("누가 보낸 패킷까지 받아 줄까?", "필터링은 받는 상대의 범위를 정해요",
           ["지우 PC가 협력사 서버로 먼저 UDP를 보냈어요", "누구든 받는 방식은 두 패킷을 모두 받아요",
            "같은 IP만 받는 방식은 포트가 달라도 받아요", "같은 IP·포트만 받는 방식은 둘 다 막아요"])
    Ys = 195
    p.base(line(124, Ys, 212, Ys, LINE, 4, "8 6"), line(268, Ys, 606, Ys, LINE, 4, "8 6"))
    p.fly(packet(0, 0, BLUE), [(130, Ys), (600, Ys)], 1, 0.05, 0.95)
    p.base(pc(70, Ys, "지우 PC"), rt(240, Ys), dsrv(650, Ys, "협력사 서버"))
    p.base(pill(240, 130, "바깥 매핑 " + JIWOOWAN + ":42000", ORANGE, 16, False, 270), pill(650, 130, "203.0.113.15:5555", BLUE, 16, False, 190))
    p.mark((105, 114, 270, 32), 1)
    X, W = 100, [300, 250, 250]
    cols = [X, X + W[0], X + W[0] + W[1]]
    Yh = 272
    p.base(cell(cols[0], Yh, W[0] - 6, 50, "필터링 방식", MUTED, 16, BG))
    for i, (a_, b_) in enumerate((("203.0.113.15:7777", "같은 IP · 다른 포트"), ("203.0.113.99:40000", "다른 IP"))):
        x = cols[i + 1]
        p.base(box(x, Yh, W[i + 1] - 6, 50, MUTED, BG, 6, sw=3) + text(x + (W[i + 1] - 6) / 2, Yh + 21, "도착 " + a_, 16, MUTED, 700)
               + text(x + (W[i + 1] - 6) / 2, Yh + 40, b_, 14, MUTED))
    rows = [("누구든 받음(EIF)", True, True), ("같은 IP만 받음(ADF)", True, False), ("같은 IP·포트만 받음(APDF)", False, False)]

    def res(x, y, w, ok):
        c = GREEN if ok else RED
        return (box(x, y, w, 40, c, PANEL, 6, sw=3) + (check(x + 34, y + 20) if ok else cross(x + 34, y + 20))
                + text(x + 66, y + 27, "받음" if ok else "받지 않음", 17, c, 700, anchor="start"))
    for i, (n, a_, b_) in enumerate(rows):
        y = 330 + i * 44
        p.at(cell(cols[0], y, W[0] - 6, 40, n, BLUE, 17) + res(cols[1], y, W[1] - 6, a_) + res(cols[2], y, W[2] - 6, b_),
             i + 2, 4, mark=(cols[0], y, sum(W) - 6, 40))
    return p.render()


# ---------------- Page 5 ----------------
def p5():
    p = Pg("Full Cone, Symmetric은 어떻게 읽을까?", "옛 이름을 매핑과 필터링으로 풀어요",
           ["제품 설명서에 Full Cone 문구가 보여요", "Cone 세 가지는 매핑이 같고 필터링이 달라요",
            "Symmetric은 매핑이 상대에 따라 달라져요", "이름은 두 칸으로 풀고 노출도 따져요"])
    X0, CW = 250, 215
    xs = [X0, X0 + CW + 10, X0 + 2 * (CW + 10)]
    p.base(cell(130, 114, 700, 44, "제품 설명서: “Full Cone 지원, P2P에 최적”", ORANGE, 17))
    p.base(lbl(X0 + 332, 186, "필터링: 누구의 패킷까지 받나", MUTED, 16))
    for x, h in zip(xs, ("누구든 받음", "같은 IP만 받음", "같은 IP·포트만 받음")):
        p.base(cell(x, 198, CW, 34, h, MUTED, 16, BG))
    for y, t in ((246, "상대와 무관"), (314, "상대에 따라 달라짐")):
        p.base(box(20, y, 215, 56, BLUE, BG, 6, sw=3) + text(127, y + 22, "매핑", 16, BLUE, 700) + text(127, y + 44, t, 16, TXT, 700))
    for x in xs:
        p.at(box(x, 246, CW, 56, LINE, BG, 6, dash=True, sw=2) + text(x + CW / 2, 282, "?", 22, MUTED, 700), 1, 1)
    p.at(box(X0, 314, 3 * CW + 20, 56, LINE, BG, 6, dash=True, sw=2) + text(X0 + (3 * CW + 20) / 2, 350, "?", 22, MUTED, 700), 1, 2)
    for x, n in zip(xs, ("Full Cone", "Restricted Cone", "Port Restricted Cone")):
        p.at(cell(x, 246, CW, 56, n, GREEN, 16), 2, 4)
    p.mark((X0, 246, 3 * CW + 20, 56), 2)
    p.at(cell(X0, 314, 3 * CW + 20, 56, "Symmetric · 필터링은 상대와 연관된 조건", RED, 17), 3, 4, mark=(X0, 314, 3 * CW + 20, 56))
    p.at(pill(480, 425, "넓게 받는 이름일수록 연결은 쉽지만 노출도 커요", ORANGE, 17, True, 520), 4, 4)
    return p.render()


# ---------------- Page 6 ----------------
def p6():
    p = Pg("서로의 바깥 주소를 어떻게 알까?", "STUN으로 내 주소를 알고, 소개 서버가 서로 알려 줘요",
           ["서로의 바깥 주소를 아직 몰라요", "양쪽이 STUN 서버에 자기 바깥 주소를 물어요",
            "소개 서버가 각자의 바깥 주소를 상대에게 알려 줘요", "서로의 주소를 알았으니 먼저 보내 볼 차례예요"])
    Yd = 400
    LX, RX = 130, 818
    p.base(line(146, Yd, 222, Yd, LINE, 4, "8 6"), line(278, Yd, 682, Yd, LINE, 3, "8 6"), line(738, Yd, 814, Yd, LINE, 4, "8 6"))
    p.at(line(256, Yd - 30, 446, 215, BLUE, 3, "8 6") + line(704, Yd - 30, 514, 215, BLUE, 3, "8 6"), 2, 3)
    p.fly(packet(0, 0, BLUE), [(272, Yd - 38), (420, 245)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, BLUE), [(688, Yd - 38), (540, 245)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(420, 245), (272, Yd - 38)], 3, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(540, 245), (688, Yd - 38)], 3, 0.05, 0.95)
    p.base(laptop(90, Yd, "박 팀장 PC"), rt(250, Yd), rt(710, Yd), pc(870, Yd, "지우 PC"))
    p.at(dsrv(480, 185, "") + text(528, 192, "STUN 서버", 18, TXT, 700, anchor="start"), 2, 2)
    p.at(dsrv(480, 185, "") + text(528, 192, "소개 서버", 18, TXT, 700, anchor="start"), 3, 3)
    p.at(pill(LX, 320, "내 주소 " + HOMEWAN + ":40001", ORANGE, 16, False, 236) + pill(RX, 320, "내 주소 " + JIWOOWAN + ":42000", ORANGE, 16, False, 252), 2, 4)
    p.mark((LX - 118, 304, 236, 32), 2)
    p.mark((RX - 126, 304, 252, 32), 2)
    p.at(pill(LX, 272, "상대 주소 ?", MUTED, 16, False, 140) + pill(RX, 272, "상대 주소 ?", MUTED, 16, False, 140), 1, 2)
    p.at(pill(LX, 272, "상대 " + JIWOOWAN + ":42000", BLUE, 16, False, 236) + pill(RX, 272, "상대 " + HOMEWAN + ":40001", BLUE, 16, False, 236), 3, 4)
    p.mark((LX - 118, 256, 236, 32), 3)
    p.mark((RX - 118, 256, 236, 32), 3)
    p.at(line(300, Yd, 660, Yd, ORANGE, 4, "10 8") + ask(480, Yd - 42), 4, 4, mark=(450, Yd - 68, 60, 52))
    return p.render()


def p6b():
    p = Pg("동시에 먼저 보내면 길이 열릴까?", "첫 패킷은 버려져도 이후 패킷은 통과해요",
           ["서로의 바깥 주소는 알지만 아직 아무도 보내지 않았어요", "양쪽이 거의 동시에 먼저 보내 임시 행이 생겨요",
            "먼저 도착한 첫 패킷은 버려질 수 있어요", "행이 생긴 뒤의 패킷은 응답처럼 받아 줘요"])
    Y, L1, L2 = 290, 272, 308
    p.base(line(146, Y, 222, Y, LINE, 4, "8 6"), line(298, L1, 662, L1, LINE, 3, "8 6"), line(298, L2, 662, L2, LINE, 3, "8 6"), line(738, Y, 814, Y, LINE, 4, "8 6"))
    p.at(line(298, L1, 662, L1, GREEN, 5) + line(298, L2, 662, L2, GREEN, 5), 4, 4)
    p.fly(packet(0, 0, ORANGE), [(300, L1), (650, L1)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(660, L2), (310, L2)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, GREEN), [(300, L1), (650, L1)], 4, 0.05, 0.95)
    p.fly(packet(0, 0, GREEN), [(660, L2), (310, L2)], 4, 0.05, 0.95)
    p.base(laptop(90, Y, "박 팀장 PC"), rt(260, Y), rt(700, Y), pc(870, Y, "지우 PC"))
    p.at(pill(260, 205, "상대를 향한 행 없음", MUTED, 16, False, 200) + pill(700, 205, "상대를 향한 행 없음", MUTED, 16, False, 200), 1, 1)
    p.at(pill(260, 205, "임시 행 생김", ORANGE, 16, True, 160) + pill(700, 205, "임시 행 생김", ORANGE, 16, True, 160), 2, 4,
         mark=(180, 189, 160, 32))
    p.mark((620, 189, 160, 32), 2)
    p.at(cross(322, Y) + cross(638, Y), 3, 3, mark=(300, Y - 22, 44, 44))
    p.mark((616, Y - 22, 44, 44), 3)
    p.at(check(480, Y) + pill(480, 420, "그 뒤 패킷은 응답처럼 받아 줘요", GREEN, 17, True, 380), 4, 4, mark=(458, Y - 22, 44, 44))
    return p.render()


# ---------------- Page 7 (p7 kept) ----------------
def p7b():
    p = Pg("서버 경유, 직접, 중계, 길은 셋이에요", "어느 길이든 공유기에 포트를 열 일은 없어요",
           ["가장 흔한 길은 양쪽이 서비스 서버로 먼저 연결하는 거예요", "지연이 적은 직접 연결도 먼저 시도해요",
            "직접이 안 되면 TURN 서버가 대신 전해 줘요", "어느 길이든 공유기의 포트를 열 필요는 없어요"])
    ys = [190, 300, 410]
    lanes = [("서비스 서버 경유", "서버 부담 · 서비스에 의존", GREEN), ("P2P 직접(홀 펀칭)", "성공이 보장되지 않아요", ORANGE), ("TURN 중계", "서버 비용 · 지연", BLUE)]
    XL, XR, XS = 390, 860, 625
    for i, ((n, sub, c), y) in enumerate(zip(lanes, ys)):
        p.base(box(30, y - 42, 300, 84, c, PANEL, 10, sw=2) + text(180, y - 6, n, 18, TXT, 700) + text(180, y + 22, sub, 16, MUTED))
        if i == 1:
            p.at(line(XL + 52, y, XR - 34, y, ORANGE, 4, "8 6"), 2, 4)
            p.fly(packet(0, 0, ORANGE), [(XL + 56, y), (XR - 40, y)], 2, 0.05, 0.95)
        else:
            p.at(line(XL + 52, y, XR - 34, y, c, 4), i + 1 if i == 0 else 3, 4)
            p.fly(packet(0, 0, c), [(XL + 56, y), (XS, y), (XR - 40, y)], 1 if i == 0 else 3, 0.05, 0.95)
    for i, ((n, sub, c), y) in enumerate(zip(lanes, ys)):
        if i != 1:
            p.at(dsrv(XS, y, "", c), 1 if i == 0 else 3, 4)
        p.at(laptop(XL, y) + pc(XR, y), 1 if i == 0 else i + 1, 4)
    p.mark((30, ys[0] - 42, 300, 84), 1)
    p.mark((30, ys[1] - 42, 300, 84), 2)
    p.mark((30, ys[2] - 42, 300, 84), 3)
    p.at("".join(check(930, y) for y in ys), 4, 4)
    return p.render()


A = "assets/animations/"
ITEMS = [  # (file, fn, title, alt, caption, page, after_paragraph)
    ("u12-l05-p01-outbound-first", p1, "포트를 안 열었는데 화상회의는?",
     "박 팀장과 협력사가 모두 공유기 뒤에서 포트를 닫아 둔 채 서비스 서버로 먼저 연결하면, 영상과 음성이 서버를 거쳐 오가고 먼저 나간 통신에 행이 생겨 포트를 열 일이 없다는 그림입니다.",
     "먼저 나간 통신에는 행이 자동으로 생겨 포트가 필요 없습니다.", 1, 1),
    ("u12-l05-p01b-p2p-first-packet", p1b, "서버 없이 직접 주고받으면 어떨까?",
     "P2P는 박 팀장과 협력사가 서버 없이 직접 주고받는 방식이고, 소개 서버는 상대의 바깥 주소만 알려 줄 뿐이며, 박 팀장이 먼저 보낸 패킷은 협력사 공유기에 맞는 행이 없어 막힐 수 있어 바깥 주소와 첫 패킷 허용이 맞아야 한다는 그림입니다.",
     "직접 통신에는 내 바깥 주소와 상대의 첫 패킷 허용, 두 가지가 맞아야 합니다.", 1, 2),
    ("u12-l05-p02-two-questions-table", p2, "NAT에게 꼭 따로 물어야 할 두 가지",
     "지우의 메모는 이름만 보고 안 될 거라 판단했지만, 공유기의 변환표에서 매핑은 External 칸에 바깥 주소·포트를 정하는 일이고 필터링은 바깥에서 온 패킷을 들여보내기 전의 조건이라서, 두 질문을 따로 확인한다고 고치는 그림입니다.",
     "NAT는 매핑과 필터링을 따로 확인합니다.", 2, 2),
    ("u12-l05-p03-mapping-by-peer-net", p3, "상대가 바뀌면 바깥 포트도 바뀔까?",
     "주소 확인 서버가 본 박 팀장 공유기의 바깥 주소 192.0.2.123:40001을 협력사에 알려 줬는데, 상대와 무관한 매핑은 협력사에도 :40001을 쓰지만 상대에 따라 달라지는 매핑은 협력사에는 :40017을 써서 소개한 주소가 맞지 않는다는 비교입니다.",
     "소개한 주소가 맞으려면 매핑이 상대와 무관해야 합니다.", 3, 2),
    ("u12-l05-p04-filtering-gate", p4, "누가 보낸 패킷까지 받아 줄까?",
     "지우 PC가 203.0.113.15:5555로 먼저 보내 바깥 매핑 198.51.100.25:42000이 생긴 뒤, 203.0.113.15:7777과 203.0.113.99:40000에서 온 패킷을 누구든 받음은 둘 다 받고, 같은 IP만 받음은 앞의 것만 받고, 같은 IP·포트만 받음은 둘 다 받지 않는 비교입니다.",
     "필터링이 꼼꼼할수록 받는 상대의 범위가 좁아집니다.", 4, 2),
    ("u12-l05-p05-cone-grid", p5, "Full Cone, Symmetric은 어떻게 읽을까?",
     "제품 설명서의 Full Cone 같은 옛 이름을 매핑과 필터링 두 칸으로 풀면, Full Cone·Restricted Cone·Port Restricted Cone은 매핑이 상대와 무관하고 필터링만 다르며 Symmetric은 매핑이 상대에 따라 달라지고, 넓게 받는 이름일수록 노출도 커진다는 표입니다.",
     "옛 Cone 이름은 매핑과 필터링으로 풀어 읽습니다.", 5, 2),
    ("u12-l05-p06-learn-addresses", p6, "서로의 바깥 주소를 어떻게 알까?",
     "박 팀장과 지우 PC가 서로의 바깥 주소를 모르는 상태에서, 양쪽이 STUN 서버에 물어 자기 바깥 주소를 알고, 소개 서버가 그 주소를 상대에게 알려 주어 먼저 보내 볼 준비가 되는 과정입니다.",
     "STUN으로 내 주소를 알고, 소개 서버가 서로의 주소를 알려 줍니다.", 6, 2),
    ("u12-l05-p06b-simultaneous-send", p6b, "동시에 먼저 보내면 길이 열릴까?",
     "양쪽이 서로의 바깥 주소를 아는 상태에서 거의 동시에 먼저 보내면 각자의 공유기에 임시 행이 생기고, 먼저 도착한 첫 패킷은 버려질 수 있어도 그 뒤의 패킷은 응답처럼 받아 주어 직접 연결이 이어지는 UDP 홀 펀칭입니다.",
     "UDP 홀 펀칭은 첫 패킷이 버려져도 이후 패킷이 통과합니다.", 6, 3),
    ("u12-l05-p07b-three-ways", p7b, "서버 경유, 직접, 중계, 길은 셋이에요",
     "화상회의 데이터가 가는 길은 서비스 서버 경유, P2P 직접(홀 펀칭), TURN 중계 세 가지이고 각각 서버 부담, 성공 보장 없음, 서버 비용과 지연이라는 대가가 있지만 어느 길도 공유기에 포트를 열 필요는 없다는 그림입니다.",
     "세 가지 길 모두 포트 개방 없이 이어지고, 대가만 다릅니다.", 7, 3),
]
KEEP7 = ("u12-l05-p07-relay", "직접 못 만나면 누가 대신 전해 줄까?",
         "직접 연결이 UDP 차단, 상대별 매핑, 통신사 NAT 때문에 막히면 양쪽이 TURN 서버 203.0.113.60으로 연결해 데이터를 중계받고, 확실한 대신 서버 비용과 지연이 든다는 그림입니다.",
         "중계는 직접 연결이 안 될 때의 확실한 대안이며 비용과 지연이 따릅니다.", 1)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, fn, *_ in ITEMS:
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        pages = [[] for _ in range(7)]
        for f, _, t, al, c, pg, ap in ITEMS:
            pages[pg - 1].append((f, t, al, c, ap))
        f, t, al, c, ap = KEEP7
        pages[6].insert(0, (f, t, al, c, ap))
        wire_items(LESSON / "lesson.md", pages)
    print("ok", len(ITEMS), "svgs")
