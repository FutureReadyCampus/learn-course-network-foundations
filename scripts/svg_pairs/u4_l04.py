#!/usr/bin/env python3
"""Unit 4 Lesson 4 paired SVGs (how a packet is built and delivered). Run from the repo root:
python3 scripts/svg_pairs/u4_l04.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/04-*"))
OUT = LESSON / "assets" / "animations"
DUR = {True: 15, False: 16}


def hl(x, y, w, h, c=ORANGE, rx=10):
    return box(x - 4, y - 4, w + 8, h + 8, c, "none", rx, sw=5)


# ---------- Page 1: content + header = packet; routers read the destination ----------
def page1(daily):
    a = Anim(4, DUR[daily])
    item = parcel if daily else packet
    me = house(100, 380, "철수") if daily else laptop(100, 380, "내 PC")
    hub = warehouse(480, 380, "물류센터") if daily else router(480, 380)
    fr = house(860, 380, "영희") if daily else pc(860, 380, "서버")
    ca, cb = (("보내는 곳", "철수 집"), ("받는 곳", "영희 집")) if daily else (("출발지 IP", "192.168.0.10"), ("목적지 IP", "203.0.113.20"))

    def hcell(x, lab, val, c):
        return (box(x, 180, 150, 70, c, PANEL, 6, sw=3) + text(x + 75, 208, lab, 15, MUTED, 700)
                + text(x + 75, 236, val, 19, c, 700))
    pay = box(500, 180, 260, 70, GREEN, PANEL, 6, sw=3) + text(630, 224, "책" if daily else "페이로드 (보낼 데이터)", 22, GREEN, 700)
    body = [me, hub, fr, line(170, 395, 440, 395, LINE, 3), line(520, 395, 790, 395, LINE, 3),
            a.vis(pay, 1, 4), a.vis(hcell(200, *ca, ORANGE) + hcell(350, *cb, BLUE), 2, 4),
            a.vis(pill(480, 160, "상자(겉)에 송장" if daily else "헤더", ORANGE, 17, True), 2, 2),
            a.vis(hl(350, 180, 150, 70, BLUE) + line(480, 345, 480, 300, ORANGE, 3, "4 4") + eye(480, 280)
                  + text(500, 318, "최종 주소만 봐요" if daily else "목적지 IP를 봐요", 18, ORANGE, 700, "start"), 3, 3),
            a.vis(a.move(item(), [(100, 395), (480, 395)], 3, 0.1, 0.7), 3, 3),
            a.vis(a.move(item(), [(480, 395), (860, 395)], 4, 0.1, 0.7), 4, 4), a.vis(check(860, 320), 4.8, 4)]
    if daily:
        t, sub = "책에 송장을 붙여 택배로 보낸다", "내용물은 책, 겉의 송장이 어디로 갈지 알려 줘요"
        caps = ["철수가 영희에게 보낼 책이에요", "겉에 보내는 곳과 받는 곳을 적은 송장을 붙여요",
                "물류센터는 받는 곳 주소를 보고 방향을 정해요", "책은 그대로 영희에게 도착해요"]
    else:
        t, sub = "패킷은 페이로드와 헤더로 이뤄진다", "라우터는 헤더의 목적지 IP를 보고 방향을 정해요"
        caps = ["보낼 데이터가 페이로드예요", "출발지·목적지 IP가 든 헤더를 붙이면 IP 패킷이에요",
                "라우터는 목적지 IP를 보고 다음 방향을 골라요", "페이로드는 그대로 서버에 도착해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: IP finds the host, port picks the program ----------
def page2(daily):
    a = Anim(4, DUR[daily])
    item = parcel if daily else packet
    chips = ["101호 철수", "102호 지영", "103호 영희"] if daily else ["웹 서버 :443", "메신저 :50456", "게임 :50999"]
    ipill, ppill = ("건물 주소", "103호") if daily else ("IP 203.0.113.20", "포트 443")
    tgt = 2 if daily else 0
    host = box(640, 150, 280, 230, MUTED, PANEL, 14, sw=3) + text(780, 180, "영희네 아파트" if daily else "서버 203.0.113.20", 19, MUTED, 700)
    cy = [200, 262, 324]
    chip = lambda i, c: box(670, cy[i], 220, 46, c, BG, 8, sw=2) + text(780, cy[i] + 30, chips[i], 20, TXT, 700)
    me = house(100, 270, "철수") if daily else laptop(100, 270, "내 PC")
    body = [me, host,
            a.vis(hl(640, 150, 280, 230, ORANGE, 16), 1, 1),
            a.vis("".join(chip(i, BLUE) for i in range(3)), 2, 4),
            a.vis(a.move(item() + pill(0, -36, ipill, ORANGE, 15), [(190, 280), (560, 280)], 1, 0.1, 0.75), 1, 1),
            a.vis(f'<g transform="translate(560,280)">{item()}{pill(0, -36, ipill, ORANGE, 15)}</g>', 2, 2),
            a.vis(f'<g transform="translate(560,280)">{item()}{pill(0, -36, ppill, GREEN, 15)}</g>'
                  + line(590, 280, 668, cy[tgt] + 23, GREEN, 4) + hl(670, cy[tgt], 220, 46, GREEN, 10), 3, 4),
            a.vis(text(780, 420, "숫자 표식일 뿐, 물리 구멍은 아니에요" if not daily else "호수는 건물 안의 받을 사람 표식이에요", 19, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "건물 주소로 찾고 호수로 받을 사람 고르기", "주소는 건물까지, 호수는 건물 안의 수신자까지"
        caps = ["건물 주소를 보고 영희네 아파트에 도착해요", "건물 안에는 여러 가구가 살고 있어요",
                "호수를 보고 받을 사람을 골라요", "호수는 건물 안의 수신자 표식이에요"]
    else:
        t, sub = "IP 주소로 호스트, 포트로 프로그램", "한 호스트 안의 여러 프로그램 중 받을 쪽을 골라요"
        caps = ["IP 주소를 보고 서버(호스트)에 도착해요", "한 호스트에서 여러 프로그램이 실행 중이에요",
                "전송 계층 헤더의 포트로 받을 프로그램을 골라요", "포트는 헤더에 적힌 숫자예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: process, host, interface, default gateway ----------
def page3(daily):
    a = Anim(4, DUR[daily])
    gw = booth(520, 275, "접수창구") if daily else router(520, 265, "기본 게이트웨이")
    body = [box(50, 170, 240, 180, MUTED, PANEL, 14, sw=3), text(170, 198, "철수네 집 (호스트)" if daily else "내 PC (호스트)", 18, MUTED, 700),
            box(90, 220, 160, 50, BLUE, BG, 8, sw=2) + text(170, 252, "철수" if daily else "브라우저", 21, TXT, 700),
            box(282, 245, 16, 50, GREEN, GREEN, 3), line(298, 270, 480, 270, LINE, 3),
            gw, line(560, 270, 700, 270, LINE, 3),
            box(700, 170, 220, 180, MUTED, PANEL, 14, dash=True, sw=3), text(810, 198, "다른 동네" if daily else "다른 네트워크", 18, MUTED, 700),
            box(740, 240, 140, 50, BLUE, BG, 8, sw=2) + text(810, 272, "영희 집" if daily else "영희 서버", 20, TXT, 700),
            box(330, 400, 200, 46, MUTED, PANEL, 8, dash=True, sw=2) + text(430, 430, "같은 동네 이웃" if daily else "같은 네트워크 장비", 18, MUTED, 700),
            a.vis(hl(50, 170, 240, 180, ORANGE, 16) + pill(170, 150, "프로세스 + 호스트" if daily else "프로세스 + 호스트", ORANGE, 16, True), 1, 1),
            a.vis(hl(280, 241, 20, 58, GREEN, 5) + pill(400, 232, "현관문 = 인터페이스" if daily else "네트워크 인터페이스", GREEN, 16, True), 2, 2),
            a.vis(hl(450, 222, 140, 110, BLUE, 12) + pill(520, 202, "처음 맡기는 곳" if daily else "기본 게이트웨이", BLUE, 16, True), 3, 3),
            a.vis(line(298, 290, 400, 398, GREEN, 4, "6 4") + text(300, 372, "같은 곳은 직접", 17, GREEN, 700, "end")
                  + line(298, 262, 700, 262, BLUE, 4) + text(490, 215, "다른 곳은 출구를 거쳐요" if daily else "다른 곳은 게이트웨이를 거쳐요", 17, BLUE, 700), 4, 4)]
    if daily:
        t, sub = "집 안의 철수에서 동네 밖으로", "프로세스·호스트·인터페이스·기본 게이트웨이의 역할"
        caps = ["철수는 데이터를 만드는 프로세스예요", "집과 바깥길이 이어지는 곳이 인터페이스예요",
                "다른 동네로 갈 때 처음 맡기는 곳이 게이트웨이예요", "같은 동네는 직접, 다른 동네는 출구를 거쳐요"]
    else:
        t, sub = "프로세스에서 기본 게이트웨이까지", "데이터를 만드는 쪽부터 네트워크 밖으로 나가는 출구까지"
        caps = ["프로세스가 데이터를 만들고 받는 호스트 안에 있어요", "호스트는 인터페이스로 네트워크에 연결돼요",
                "다른 네트워크로 갈 때 첫 라우터가 기본 게이트웨이예요", "같은 네트워크는 직접, 다른 곳은 게이트웨이를 거쳐요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: reading IP:port on both ends ----------
def page4(daily):
    a = Anim(4, DUR[daily])
    li, lp_old, lp_new = ("철수 집", "번호표 7", "번호표 8") if daily else ("192.0.2.15", "51707", "51722")
    ri, rp = ("영희 집", "101호") if daily else ("203.0.113.20", "443")
    sep = " : "

    def side(x, ip, port, col, label, strong=False):
        s = box(x, 210, 380, 90, col, PANEL, 12, sw=5 if strong else 3) + text(x + 190, 238, label, 16, MUTED, 700)
        return s + text(x + 190, 280, f'{ip}{sep}<tspan fill="{col}">{port}</tspan>', 28, TXT, 700, raw=True)

    arrow = text(480, 266, "→", 34, TXT, 700)
    old = side(80, li, lp_old, ORANGE, "내 쪽" if daily else "내 컴퓨터") + side(500, ri, rp, GREEN, "받는 쪽" if daily else "원격 호스트")
    new = side(80, li, lp_new, ORANGE, "내 쪽" if daily else "내 컴퓨터") + side(500, ri, rp, GREEN, "받는 쪽" if daily else "원격 호스트")
    body = [a.vis(old + arrow, 1, 3), a.vis(new + arrow, 4, 4),
            a.vis(text(480, 360, "연결 목록의 한 줄" if not daily else "접수 기록의 한 줄", 22, MUTED, 700), 1, 1),
            a.vis(hl(80, 210, 380, 90, ORANGE, 14) + text(270, 360, "내 쪽: 주소 + 임시 번호" if daily else "내 쪽: 주소 + 임시 포트", 22, ORANGE, 700), 2, 2),
            a.vis(hl(500, 210, 380, 90, GREEN, 14) + text(690, 360, "받는 쪽: 주소 + 101호" if daily else "서버 쪽: 주소 + 443 (보통 HTTPS)", 22, GREEN, 700), 3, 3),
            a.vis(pill(270, 160, "새 연결 → 새 번호" if daily else "새 연결 → 새 임시 포트", ORANGE, 17, True)
                  + text(690, 360, "받는 쪽은 그대로" if daily else "서버 포트는 보통 그대로", 22, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "접수 기록을 양쪽 끝으로 읽기", "주소 뒤의 번호가 각 끝에서 누구를 가리키는지 봐요"
        caps = ["기록 한 줄에 양쪽 끝이 함께 적혀 있어요", "내 쪽은 집 주소와 그때그때 받는 번호표예요",
                "받는 쪽은 집 주소와 정해진 호수예요", "다음 접수 때는 번호표만 바뀌어요"]
    else:
        t, sub = "IP 주소:포트 번호를 양쪽 끝으로 읽기", "숫자는 설명용 예시예요"
        caps = ["연결 한 줄에 양쪽 끝이 함께 적혀 있어요", "내 쪽은 내 주소와 임시 포트예요",
                "서버 쪽은 서버 주소와 보통 443(HTTPS)이에요", "새 연결에서는 임시 포트만 바뀔 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: socket = window between program and OS ----------
def page5(daily):
    a = Anim(4, DUR[daily])
    item = parcel if daily else packet
    apps = ("손님 가", "손님 나") if daily else ("브라우저", "메신저")
    sock = ("창구 1", "창구 2") if daily else ("소켓", "소켓")
    body = []
    for i, y in enumerate((200, 300)):
        body += [box(60, y, 160, 50, BLUE, PANEL, 8, sw=2) + text(140, y + 32, apps[i], 20, TXT, 700),
                 line(220, y + 25, 290, y + 25, LINE, 3),
                 box(290, y - 6, 70, 62, GREEN, PANEL, 8, sw=3) + text(325, y + 31, sock[i], 16, GREEN, 700),
                 line(360, y + 25, 420, y + 25, LINE, 3)]
    body += [box(420, 170, 240, 200, MUTED, PANEL, 14, sw=3) + text(540, 200, "우체국 안쪽 작업장" if daily else "운영체제 (커널)", 18, MUTED, 700)
             + box(450, 235, 180, 50, BLUE, BG, 8, sw=2) + text(540, 267, "분류·포장" if daily else "TCP/IP 처리", 19, TXT, 700),
             line(660, 270, 740, 270, LINE, 3),
             box(740, 235, 150, 70, ORANGE, PANEL, 10, sw=3) + text(815, 262, "트럭 출구" if daily else "네트워크 장치", 18, ORANGE, 700)]
    direct = (f'<path d="M140,200 V150 H815 V235" fill="none" stroke="{RED}" stroke-width="4" stroke-dasharray="8 6"/>'
              + cross(480, 150) + text(480, 132, "직접 다루지 않아요", 17, RED, 700))
    body += [a.vis(direct, 1, 1),
             a.vis(a.move(item(), [(140, 225), (325, 225)], 2, 0.1, 0.7), 2, 2),
             a.vis(a.move(item(), [(325, 225), (540, 260), (815, 290)], 3, 0.1, 0.8), 3, 3),
             a.vis(a.move(item(), [(815, 290), (540, 262), (325, 225)], 4, 0.1, 0.8) + hl(290, 194, 70, 62, GREEN, 10) + check(325, 170), 4, 4)]
    if daily:
        t, sub = "접수 창구가 손님과 작업장을 잇는다", "창구마다 맡은 손님이 정해져 있어요"
        caps = ["손님은 트럭을 직접 다루지 않아요", "손님이 자기 창구에 짐을 맡겨요",
                "작업장이 분류·포장해서 트럭으로 내보내요", "답이 오면 맞는 창구로 돌려줘요"]
    else:
        t, sub = "소켓은 프로그램과 운영체제를 잇는 창구", "프로그램은 네트워크 장치를 직접 다루지 않아요"
        caps = ["프로그램이 네트워크 장치를 직접 다루지 않아요", "프로그램은 소켓으로 운영체제에 요청해요",
                "커널이 TCP/IP 처리를 하고 장치로 내보내요", "응답은 연결에 맞는 소켓으로 돌아가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: data -> segment -> packet -> frame (flat layers) ----------
def page6(daily):
    a = Anim(4, DUR[daily])
    cells = [(150, 140, "구간 라벨" if daily else "MAC 주소", VIOLET), (290, 140, "건물 주소" if daily else "IP 주소", BLUE),
             (430, 140, "호수" if daily else "포트", ORANGE), (570, 140, "책" if daily else "요청 데이터", GREEN),
             (710, 140, "봉인 테이프" if daily else "FCS", VIOLET)]
    def cell(i):
        x, w, lab, c = cells[i]
        return box(x, 190, w, 70, c, PANEL, 6, sw=3) + text(x + w / 2, 233, lab, 20, c, 700)
    def span(x0, x1, y, lab, c):
        return box(x0, y, x1 - x0, 36, c, PANEL, 18, sw=2) + text((x0 + x1) / 2, y + 25, lab, 19, c, 700)
    un = ("작은 상자", "중간 상자", "큰 상자") if daily else ("세그먼트", "IP 패킷", "프레임")
    body = [a.vis(cell(3), 1, 4), a.vis(cell(2) + span(430, 710, 290, un[0], ORANGE), 2, 4),
            a.vis(cell(1) + span(290, 710, 338, un[1], BLUE), 3, 4),
            a.vis(cell(0) + cell(4) + span(150, 850, 386, un[2], VIOLET), 4, 4)]
    lay = [("L4 TCP", 500), ("L3 IP", 360), ("L2 링크", 500)]
    body += [a.vis(pill(480, 160, "소켓에서 받은 데이터" if not daily else "보낼 책", GREEN, 18, True), 1, 1),
             a.vis(pill(500, 160, "L4: 포트 정보를 더해요" if not daily else "호수를 적어요", ORANGE, 18, True), 2, 2),
             a.vis(pill(360, 160, "L3: IP 주소를 더해요" if not daily else "건물 주소를 붙여요", BLUE, 18, True), 3, 3),
             a.vis(pill(480, 160, "L2: MAC 주소와 FCS를 더해요" if not daily else "구간 라벨과 봉인을 더해요", VIOLET, 18, True), 4, 4)]
    if daily:
        t, sub = "책에 겹겹이 정보를 붙여 간다", "겉으로 나올수록 더 큰 상자가 돼요"
        caps = ["상자에 넣을 책이에요", "작은 상자에 받을 사람(호수)을 적어요",
                "중간 상자에 건물 주소를 붙여요", "큰 상자에 구간 라벨과 봉인을 붙여요"]
    else:
        t, sub = "데이터에서 프레임까지 차례로 만든다", "TCP를 쓰는 예: 보낼 때는 안쪽부터 감싸요"
        caps = ["프로그램이 소켓에 넘긴 데이터예요", "TCP 헤더(포트)를 더하면 세그먼트예요",
                "IP 헤더(IP 주소)를 더하면 IP 패킷이에요", "프레임 헤더와 FCS를 더하면 프레임이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: the whole trip through switch and router ----------
def page7(daily):
    a = Anim(4, DUR[daily])
    item = parcel if daily else packet
    X = [90, 270, 450]
    nodes = ([house(X[0], 235, "철수"), booth(X[1], 250, "동네 접수소"), warehouse(X[2], 250, "물류센터")] if daily else
             [laptop(X[0], 240, "내 PC"), switch(X[1], 250), router(X[2], 250)])
    host = (box(640, 150, 280, 230, MUTED, PANEL, 14, sw=3) + text(780, 180, "영희네 아파트" if daily else "서버 (목적지 호스트)", 18, MUTED, 700)
            + box(670, 215, 220, 50, BLUE, BG, 8, sw=2) + text(780, 247, "103호 영희" if daily else "웹 서버 프로세스", 20, TXT, 700)
            + box(670, 285, 220, 46, GREEN, BG, 8, sw=2) + text(780, 315, "창구(소켓)" if daily else "수신 소켓", 19, GREEN, 700))
    notes = [("이번 구간 인수자를 봐요" if daily else "목적지 MAC을 봐요", GREEN, X[1]),
             ("받는 건물 주소를 봐요" if daily else "목적지 IP를 봐요", BLUE, X[2])]
    body = [line(X[0], 345, 640, 345, LINE, 3)] + nodes + [host]
    body += [a.vis(a.move(item(), [(X[0], 345), (X[1], 345)], 1, 0.1, 0.8), 1, 1),
             a.vis(eye(X[1], 180) + line(X[1], 198, X[1], 212, GREEN, 3, "4 4") + text(X[1], 154, notes[0][0], 17, GREEN, 700), 1, 1),
             a.vis(a.move(item(), [(X[1], 345), (X[2], 345)], 2, 0.1, 0.8), 2, 2),
             a.vis(eye(X[2], 180) + line(X[2], 198, X[2], 212, BLUE, 3, "4 4") + text(X[2], 154, notes[1][0], 17, BLUE, 700)
                   + text(360, 420, "주소는 그대로, 구간 정보만 새로" if daily else "IP는 그대로, 프레임은 새로", 19, MUTED, 700), 2, 2),
             a.vis(a.move(item(), [(X[2], 345), (620, 345)], 3, 0.1, 0.7) + hl(640, 150, 280, 230, ORANGE, 16)
                   + text(780, 410, "주소로 호스트를 찾아요", 19, ORANGE, 700), 3, 3),
             a.vis(hl(670, 215, 220, 50, GREEN, 10) + line(780, 285, 780, 265, GREEN, 3) + check(910, 240)
                   + text(780, 410, "포트·소켓으로 프로그램에 전달", 19, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "접수소와 물류센터를 거쳐 영희에게", "각 곳에서 맡은 정보만 확인해요"
        caps = ["동네 접수소가 이번 구간 인수자를 봐요", "물류센터가 건물 주소를 보고 다음 곳을 골라요",
                "건물 주소로 영희네 아파트를 찾아요", "호수에 맞는 창구로 영희에게 전달돼요"]
    else:
        t, sub = "스위치와 라우터를 거쳐 웹 서버까지", "NAT가 없는 일반적인 예예요"
        caps = ["스위치가 목적지 MAC을 보고 LAN 안에서 전달해요", "라우터가 목적지 IP를 보고 다음 홉을 골라요",
                "IP 주소로 목적지 호스트를 찾아요", "포트와 소켓 정보로 웹 서버 프로세스에 전달돼요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    ("l14-daily-parcel-with-label", "l14-packet-header-payload", page1),
    ("l14-daily-building-and-unit", "l14-ip-host-port-program", page2),
    ("l14-daily-house-and-exit", "l14-process-host-gateway", page3),
    ("l14-daily-record-both-ends", "l14-ip-port-both-ends", page4),
    ("l14-daily-service-windows", "l14-socket-window", page5),
    ("l14-daily-layered-labels", "l14-data-to-frame", page6),
    ("l14-daily-whole-trip", "l14-whole-delivery", page7),
]

COPY = [
    (("책에 송장을 붙여 택배로 보낸다",
      "아래에 철수의 집, 물류센터, 영희의 집이 있고 위쪽에 책이 놓입니다. 책 앞에 보내는 곳과 받는 곳이 적힌 송장이 붙고, 상자가 물류센터에서 받는 곳 주소를 확인한 뒤 영희의 집에 도착합니다.",
      "내용물은 책이고, 겉의 송장이 어디로 보낼지 알려 줍니다."),
     ("패킷은 페이로드와 헤더로 이뤄진다",
      "아래에 내 PC, 라우터, 서버가 있고 위쪽에 보낼 데이터인 페이로드가 놓입니다. 앞에 출발지 IP와 목적지 IP가 든 헤더가 붙고, 패킷이 라우터에서 목적지 IP를 확인한 뒤 서버에 도착합니다.",
      "이 Lesson의 패킷은 주로 L3의 IP 패킷입니다. 라우터는 헤더의 목적지 IP를 보고 다음 방향을 고릅니다."), 2),
    (("건물 주소로 찾고 호수로 받을 사람 고르기",
      "택배가 건물 주소를 보고 영희네 아파트에 도착합니다. 건물 안에 101호, 102호, 103호가 나타나고, 호수 103호를 보고 영희가 선택됩니다.",
      "주소는 건물까지, 호수는 건물 안의 수신자까지 찾아갑니다."),
     ("IP 주소로 호스트, 포트로 프로그램",
      "패킷이 IP 주소를 보고 서버에 도착합니다. 서버 안에 웹 서버, 메신저, 게임 프로그램이 나타나고, 포트 443을 보고 웹 서버가 선택됩니다. 마지막에 포트는 물리적인 구멍이 아닌 숫자 표식이라고 표시됩니다.",
      "IP 주소는 호스트를, 포트 번호는 호스트 안에서 데이터를 받을 프로그램을 구분합니다. 포트 번호 중 443 외에는 예시예요."), 2),
    (("집 안의 철수에서 동네 밖으로",
      "철수가 사는 집 안에서 현관문과 접수창구를 거쳐 다른 동네의 영희 집으로 이어지는 길이 있습니다. 집, 현관문, 처음 맡기는 곳이 차례로 강조되고, 같은 동네 이웃에게는 직접, 다른 동네에는 출구를 거쳐 간다고 표시됩니다.",
      "철수는 프로세스, 집은 호스트, 현관문은 인터페이스, 처음 맡기는 곳은 기본 게이트웨이에 해당합니다."),
     ("프로세스에서 기본 게이트웨이까지",
      "내 PC 안의 브라우저에서 네트워크 인터페이스를 거쳐 기본 게이트웨이와 다른 네트워크의 서버로 이어지는 길이 있습니다. 호스트, 인터페이스, 기본 게이트웨이가 차례로 강조되고, 같은 네트워크 장비에는 직접, 다른 네트워크에는 게이트웨이를 거쳐 간다고 표시됩니다.",
      "같은 네트워크 안의 목적지는 게이트웨이 없이 직접 전달되고, 다른 네트워크로 갈 때는 기본 게이트웨이로 먼저 보냅니다."), 3),
    (("접수 기록을 양쪽 끝으로 읽기",
      "접수 기록 한 줄에 ‘철수 집 : 번호표 7’과 ‘영희 집 : 101호’가 화살표로 이어져 있습니다. 내 쪽은 집 주소와 번호표, 받는 쪽은 집 주소와 호수라고 강조되고, 마지막에는 번호표만 8로 바뀝니다.",
      "연결의 양쪽 끝은 각각 주소와 번호로 구별됩니다. 내 쪽 번호는 연결마다 달라질 수 있어요."),
     ("IP 주소:포트 번호를 양쪽 끝으로 읽기",
      "연결 목록 한 줄에 ‘192.0.2.15 : 51707’과 ‘203.0.113.20 : 443’이 화살표로 이어져 있습니다. 내 컴퓨터 쪽은 주소와 임시 포트, 서버 쪽은 주소와 보통 HTTPS를 뜻하는 443이라고 강조되고, 마지막에는 임시 포트만 51722로 바뀝니다.",
      "왼쪽은 내 컴퓨터, 오른쪽은 원격 호스트의 주소와 포트입니다. 숫자는 설명용 예시예요."), 2),
    (("접수 창구가 손님과 작업장을 잇는다",
      "손님 가와 손님 나가 각자 창구 1, 창구 2를 통해 우체국 작업장과 트럭 출구에 이어져 있습니다. 손님이 트럭을 직접 다루지 못한다는 표시가 나오고, 짐이 창구를 거쳐 작업장에서 트럭으로 나갑니다. 답이 오면 짐이 손님 가의 창구로만 돌아옵니다.",
      "창구를 통해서만 작업장과 트럭을 쓰고, 돌아오는 짐은 맞는 창구로 갑니다."),
     ("소켓은 프로그램과 운영체제를 잇는 창구",
      "브라우저와 메신저가 각자 소켓을 통해 운영체제와 네트워크 장치에 이어져 있습니다. 프로그램이 장치를 직접 다루지 못한다는 표시가 나오고, 요청이 소켓을 거쳐 커널의 TCP/IP 처리를 지나 장치로 나갑니다. 응답이 오면 브라우저의 소켓으로만 돌아옵니다.",
      "소켓은 포트 번호 자체가 아니라, 프로그램이 운영체제의 네트워크 기능을 쓰는 통신 창구입니다."), 2),
    (("책에 겹겹이 정보를 붙여 간다",
      "책 하나에서 시작해 호수 라벨이 붙은 작은 상자, 건물 주소가 붙은 중간 상자, 구간 라벨과 봉인 테이프가 붙은 큰 상자가 차례로 만들어집니다.",
      "겉으로 나올수록 정보가 더해져 더 큰 단위가 됩니다."),
     ("데이터에서 프레임까지 차례로 만든다",
      "요청 데이터에서 시작해 TCP 헤더의 포트가 붙은 세그먼트, IP 주소가 붙은 IP 패킷, MAC 주소와 FCS가 붙은 프레임이 차례로 만들어집니다.",
      "TCP를 쓰는 예입니다. 한 계층에서 완성된 단위는 바깥 계층의 페이로드로 실려 갑니다."), 3),
    (("접수소와 물류센터를 거쳐 영희에게",
      "철수의 집에서 동네 접수소와 물류센터를 지나 영희네 아파트에 도착하는 길이 있습니다. 접수소는 이번 구간 인수자를, 물류센터는 건물 주소를 확인하고, 아파트에 도착하면 호수에 맞는 창구로 영희에게 전달됩니다.",
      "각 곳은 자기가 맡은 정보만 확인하고, 건물 주소는 끝까지 그대로입니다."),
     ("스위치와 라우터를 거쳐 웹 서버까지",
      "내 PC에서 스위치와 라우터를 지나 서버에 도착하는 길이 있습니다. 스위치는 목적지 MAC을, 라우터는 목적지 IP를 확인하고, 서버에서는 IP로 호스트를 찾은 뒤 포트와 소켓 정보로 웹 서버 프로세스에 전달됩니다.",
      "NAT가 없는 일반적인 예입니다. 목적지 IP는 그대로이고, 프레임과 MAC은 구간마다 새로 정해집니다."), 2),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for (dn, nn, fn), (d, n, after) in zip(PAGES, COPY):
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        rows.append((dn, *d, nn, *n, after))
        print(dn, nn)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", rows)
