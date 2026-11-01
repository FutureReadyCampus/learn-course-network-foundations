#!/usr/bin/env python3
"""Unit 4 Lesson 2 paired SVGs: a daily-life scene, then the same layout as a network concept.

Run from the repo root:  python3 scripts/svg_pairs/u4_l02.py   (writes SVGs into the Lesson's assets/animations
and rewires its Page metadata; `--svg-only` skips the lesson.md edit).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/02-*"))
OUT = LESSON / "assets" / "animations"
DUR = {True: 15, False: 16}  # daily / network loop seconds: ~4s per step


def accent(daily):
    return ORANGE if daily else BLUE


# ---------- Page 1: one big thing -> small pieces with a label each ----------
def page1(daily):
    a = Anim(4, DUR[daily])
    ac = accent(daily)
    me = house(100, 300, "나") if daily else phone(100, 300, "내 휴대전화")
    fr = house(860, 300, "친구") if daily else phone(860, 300, "친구 휴대전화")
    X = [345, 435, 525, 615]
    END = [530, 614, 698, 782]

    def piece(n, tag=False):
        s = (f'<rect x="-38" y="-26" width="76" height="52" rx="6" fill="{ac}"/>'
             + text(0, 8, str(n), 22, BG, 700))
        return s + (pill(0, -44, "송장" if daily else "헤더", GREEN, 14) if tag else "")

    big = (box(370, 235, 220, 130, ac, PANEL, 8, sw=3) + f'<circle cx="420" cy="275" r="12" fill="{ORANGE}"/>'
           + f'<polygon points="380,355 450,290 500,335 530,305 580,355" fill="{LINE}"/>'
           + text(480, 388, "큰 그림 한 점" if daily else "사진 파일 (큰 데이터)", 20, TXT, 700))
    body = [me, fr, line(170, 430, 790, 430, LINE, 3, "4 6"),
            a.vis(big, 1, 1),
            a.vis("".join(f'<g transform="translate({X[i]},300)">{piece(i + 1)}</g>' for i in range(4))
                  + text(480, 388, "작은 단위로 나눠요", 20, MUTED, 700), 2, 2),
            a.vis("".join(f'<g transform="translate({X[i]},300)">{piece(i + 1, True)}</g>' for i in range(4)), 3, 3)]
    for i in range(4):
        body.append(a.vis(a.move(piece(i + 1, True), [(X[i], 300), (END[i], 300)], 4, 0.05 + 0.12 * i, 0.5 + 0.12 * i), 4, 4))
    body.append(a.vis(check(860, 225), 4.8, 4))
    if daily:
        t, sub = "큰 물건은 작은 상자로 나눠 보낸다", "상자마다 송장을 붙여서 운반해요"
        caps = ["큰 그림 한 점을 친구에게 보낸다고 해 볼게요", "운반하기 좋게 작은 상자로 나눠요",
                "상자마다 받는 곳 송장을 붙여요", "상자들이 길을 따라 친구에게 가요"]
    else:
        t, sub = "데이터는 패킷이라는 작은 단위로 간다", "사진 한 장도 나누고, 전달 정보를 붙여 보내요"
        caps = ["사진 한 장은 꽤 큰 데이터예요", "작은 단위로 나눈 전달 단위가 패킷이에요",
                "패킷마다 전달에 필요한 정보(헤더)를 붙여요", "패킷들이 네트워크를 지나 친구에게 가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: header + payload, and a box inside a box ----------
def page2(daily):
    a = Anim(4, DUR[daily])
    hl, pl = ("송장", "내용물") if daily else ("헤더", "페이로드")
    outer, inner = ("큰 상자", "작은 상자") if daily else ("이더넷 프레임", "IP 패킷")
    body = [box(130, 190, 160, 130, ORANGE, PANEL, 8, sw=3), text(210, 262, hl, 28, ORANGE, 700),
            box(290, 190, 540, 130, GREEN, PANEL, 8, sw=3), text(310, 218, pl, 20, GREEN, 700, "start"),
            a.vis(text(560, 275, "내용물 (물건)" if daily else "내용 (데이터)", 24, MUTED, 700), 1, 2),
            a.vis(box(290, 190, 540, 130, BLUE, "none", 8, sw=6) + text(560, 362, "열어 보면…?", 26, BLUE, 700), 2, 2)]
    inn = (box(310, 232, 100, 72, ORANGE, BG, 6, sw=3) + text(360, 276, hl, 20, ORANGE, 700)
           + box(410, 232, 400, 72, GREEN, BG, 6, sw=3) + text(610, 276, pl, 20, GREEN, 700))
    body.append(a.vis(inn, 3, 4))
    body.append(a.vis(pill(220, 160, outer, BLUE, 18, True) + pill(610, 350, inner, GREEN, 18, True)
                      + line(610, 334, 610, 306, GREEN, 3)
                      + text(480, 420, "작은 상자는 큰 상자의 내용물이기도 해요" if daily else "IP 패킷은 프레임의 내용물이기도 해요",
                             24, TXT, 700), 4, 4))
    if daily:
        t, sub = "송장 붙은 상자 안의 상자", "송장은 길 안내, 내용물은 실어 나르는 물건"
        caps = ["송장은 길 안내, 내용물은 물건이에요", "큰 상자의 내용물을 열어 보면…",
                "안에 송장 붙은 작은 상자가 나와요", "같은 덩어리가 안팎에서 역할이 달라요"]
    else:
        t, sub = "패킷은 헤더와 페이로드로 이뤄진다", "프레임의 페이로드 안에 IP 패킷이 들어가요"
        caps = ["헤더는 전달 정보, 페이로드는 내용이에요", "프레임의 페이로드를 열어 보면…",
                "안에 헤더가 붙은 IP 패킷이 나와요", "IP 패킷도 헤더와 페이로드를 가져요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: a size limit (MTU) ----------
def page3(daily):
    a = Anim(4, DUR[daily])
    ac = accent(daily)
    gl = "트럭 한 칸에 실을 수 있는 최대 크기" if daily else "한 번에 보낼 수 있는 최대 크기 (MTU)"

    def gauge(y, w, label, dash=False, lx=None):
        s = box(250, y, w, 26, ORANGE if not dash else MUTED, PANEL, 4, dash=dash, sw=3)
        s += "".join(line(250 + k * w / 6, y, 250 + k * w / 6, y + 8, ORANGE if not dash else MUTED, 2) for k in range(1, 6))
        return s + text(250 + w / 2, y - 10, label, 19, ORANGE if not dash else MUTED, 700)

    def bar(y, w, label_in="", color=None):
        return box(250, y, w, 40, color or ac, PANEL, 6, sw=3) + (text(250 + w / 2, y + 28, label_in, 20, TXT, 700) if label_in else "")

    body = [gauge(160, 420, gl)]
    body.append(text(690, 180, "1,500 B" if not daily else "한계", 20, ORANGE, 700, "start"))
    s1 = bar(220, 120) + check(394, 240) + text(422, 247, "작은 상자" if daily else "작은 메시지 → 작은 패킷", 20, TXT, 700, "start")
    s2 = (bar(220, 420) + f'<rect x="670" y="220" width="220" height="40" rx="6" fill="{PANEL}" stroke="{RED}" stroke-width="3"/>'
          + cross(920, 240) + text(250, 292, "큰 가구 → 한 칸에 안 들어가요" if daily else "큰 사진 → 한 번에는 너무 커요", 20, RED, 700, "start"))
    s3 = "".join(bar(220 + 54 * k, 200, str(k + 1)) + check(472, 240 + 54 * k) for k in range(3)) \
        + text(510, 300, "여러 상자로 나눠 실어요" if daily else "여러 패킷으로 나눠 보내요", 20, TXT, 700, "start")
    s4 = (gauge(228, 300, "다른 길은 한계가 다를 수 있어요" if daily else "다른 연결은 MTU가 다를 수 있어요", True)
          + text(570, 248, "?" if not daily else "다른 한계", 20, MUTED, 700, "start")
          + text(480, 350, "한계는 길(구간)마다 정해져요" if daily else "MTU는 링크가 감당하는 크기 기준이에요", 24, TXT, 700))
    body += [a.vis(s1, 1, 1), a.vis(s2, 2, 2), a.vis(s3, 3, 3), a.vis(s4, 4, 4)]
    if daily:
        t, sub = "상자 크기에는 한계가 있다", "한 칸에 들어가는 크기를 넘으면 나눠 실어요"
        caps = ["작은 상자는 한 칸에 쉽게 들어가요", "한계보다 큰 짐은 한 칸에 못 실어요",
                "여러 상자로 나누면 모두 실을 수 있어요", "길마다 실을 수 있는 한계가 달라요"]
    else:
        t, sub = "MTU는 한 번에 보낼 크기의 한계다", "예: 이더넷에서 IP 패킷은 최대 1,500바이트"
        caps = ["작은 메시지는 작은 패킷으로 가요", "한계보다 큰 데이터는 한 패킷에 못 담아요",
                "여러 패킷으로 나누면 모두 보낼 수 있어요", "연결마다 MTU가 다를 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: a row of numbers split into fields ----------
def page4(daily):
    a = Anim(4, DUR[daily])
    vals = ["31", "04", "07", "12", "55", "02", "18", "36", "22", "09", "41", "60", "08", "00", "45", "00"] if daily else \
           ["a4", "83", "e7", "11", "22", "33", "3c", "52", "82", "44", "55", "66", "08", "00", "45", "00"]
    W, G, X0, Y = 50, 4, 50, 170
    cx_ = lambda i: X0 + i * (W + G) + W / 2
    groups = [(0, 5, BLUE, "받는 곳 칸" if daily else "목적지 MAC"), (6, 11, GREEN, "보낸 곳 칸" if daily else "출발지 MAC"),
              (12, 13, ORANGE, "종류 칸" if daily else "Type")]

    def cells(colored):
        out = []
        for i, v in enumerate(vals):
            col = LINE
            if colored:
                col = next((c for s_, e_, c, _ in groups if s_ <= i <= e_), LINE)
            out.append(box(cx_(i) - W / 2, Y, W, 50, col, PANEL, 6, sw=3 if col != LINE else 2)
                       + text(cx_(i), Y + 33, v, 22, TXT if col == LINE else col, 700))
        return "".join(out)

    def brackets():
        out = []
        for s_, e_, c, lab in groups:
            x0, x1 = cx_(s_) - W / 2, cx_(e_) + W / 2
            out.append(line(x0, 236, x1, 236, c, 3) + text((x0 + x1) / 2, 266, lab, 20, c, 700))
        return "".join(out)

    typ = cx_(12) - W / 2, cx_(13) + W / 2
    s3 = (box(typ[0] - 4, Y - 4, typ[1] - typ[0] + 8, 58, ORANGE, "none", 8, sw=5)
          + text((cx_(14) + cx_(15)) / 2, 266, "안쪽 송장 시작" if daily else "IPv4 패킷 시작", 20, MUTED, 700)
          + line(cx_(14) - W / 2, 236, cx_(15) + W / 2, 236, MUTED, 3)
          + text(480, 330, "종류 0800 → 뒤에 안쪽 송장이 이어져요" if daily else "Type 0800 → 뒤에 IPv4 패킷이 이어져요", 24, ORANGE, 700))
    rows = ["바깥 송장", "안쪽 송장", "내용물"] if daily else ["Ethernet", "Internet Protocol", "TCP / UDP"]
    s4 = "".join(box(300 + 24 * k, 310 + 44 * k, 360, 36, [BLUE, GREEN, ORANGE][k], PANEL, 6, sw=2)
                 + text(318 + 24 * k, 335 + 44 * k, "▸ " + rows[k], 20, [BLUE, GREEN, ORANGE][k], 700, "start") for k in range(3))
    body = [a.vis(cells(False), 1, 1), a.vis(cells(True), 2, 4),
            a.vis(ask(480, 290) + text(480, 340, "어디가 주소이고 어디가 내용일까?", 24, ORANGE, 700), 1, 1),
            a.vis(brackets(), 2, 4), a.vis(s3, 3, 3), a.vis(s4, 4, 4)]
    if daily:
        t, sub = "송장번호 한 줄을 칸으로 나눠 읽기", "해독표를 보면 번호의 어느 칸이 무엇인지 알 수 있어요"
        caps = ["숫자만 보면 어디가 무슨 칸인지 몰라요", "정해진 칸대로 나누면 의미가 보여요",
                "종류 칸이 다음에 올 내용을 알려 줘요", "바깥 송장에서 안쪽으로 펼쳐 읽어요"]
    else:
        t, sub = "16진수 숫자 줄에서 헤더 읽기", "Wireshark는 규칙대로 필드를 나눠 보여 줘요"
        caps = ["숫자만 보면 어디가 주소인지 몰라요", "프로토콜 규칙대로 나누면 필드가 보여요",
                "Type 필드가 뒤에 올 내용을 알려 줘요", "이더넷 → IP → 전송 계층 순서로 펼쳐요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: three different "where"s ----------
def page5(daily):
    a = Anim(4, DUR[daily])
    me = house(110, 250, "나") if daily else laptop(110, 250, "내 노트북")
    hub = warehouse(480, 250, "물류센터") if daily else router(480, 250)
    c1, c2 = ("101호 민수", "102호 지영") if daily else ("브라우저 :50123", "메신저 :50456")
    dst = (box(710, 170, 220, 170, MUTED, PANEL, 12, sw=3)
           + text(820, 196, "받는 건물" if daily else "받는 PC", 18, MUTED, 700)
           + box(730, 212, 180, 44, BLUE, BG, 8, sw=2) + text(820, 241, c1, 19, TXT, 700)
           + box(730, 272, 180, 44, GREEN, BG, 8, sw=2) + text(820, 301, c2, 19, TXT, 700))
    cards = [(60, BLUE, "이번 구간 인수자" if daily else "MAC 주소", "지금 연결된 길에서 받는 사람" if daily else "현재 링크의 인터페이스"),
             (360, GREEN, "최종 주소" if daily else "IP 주소", "도착해야 할 건물" if daily else "네트워크 사이의 목적지"),
             (660, ORANGE, "호수" if daily else "포트 번호", "건물 안에서 받을 사람" if daily else "기기 안의 프로그램")]

    def card(x, col, ttl, sub):
        return box(x, 395, 240, 64, col, PANEL, 10, sw=2) + text(x + 120, 423, ttl, 21, col, 700) + text(x + 120, 447, sub, 16, MUTED)

    def bracket(x0, x1, col, label):
        return (line(x0, 160, x1, 160, col, 4) + line(x0, 160, x0, 176, col, 4) + line(x1, 160, x1, 176, col, 4)
                + pill((x0 + x1) / 2, 136, label, col, 17, True))

    body = [f'<g transform="translate(0,12)">{me}{hub}{dst}' + line(180, 250, 440, 250, LINE, 3) + line(520, 250, 710, 250, LINE, 3) + "</g>",
            "".join(f'<g opacity="0.4">{card(*c)}</g>' for c in cards),
            a.vis(ask(480, 344) + text(480, 382, "한 번에 ‘어디’ 하나만 쓰는 게 아니에요", 22, TXT, 700), 1, 1),
            a.vis(bracket(110, 480, BLUE, "이번 구간 인수자" if daily else "MAC: 이 링크에서 받을 쪽") + card(*cards[0]), 2, 2),
            a.vis(bracket(110, 820, GREEN, "최종 목적지 건물" if daily else "IP: 네트워크 사이의 목적지") + card(*cards[1]), 3, 3),
            a.vis(f'<g transform="translate(0,12)">' + box(726, 208, 188, 52, ORANGE, "none", 10, sw=5) + line(690, 235, 724, 235, ORANGE, 4) + "</g>"
                  + pill(820, 374, "건물 안의 호수" if daily else "포트: 기기 안의 프로그램", ORANGE, 17, True) + card(*cards[2]), 4, 4)]
    if daily:
        t, sub = "배송에는 세 가지 ‘어디’가 있다", "구간 인수자, 최종 건물, 건물 안의 받을 사람"
        caps = ["‘어디로’라는 정보가 여러 종류예요", "이번 구간을 넘겨받을 사람을 정해요",
                "길이 바뀌어도 최종 건물은 그대로예요", "건물에 도착하면 호수로 받을 사람을 찾아요"]
    else:
        t, sub = "MAC·IP·포트는 범위가 달라요", "링크, 네트워크 사이, 기기 안의 프로그램"
        caps = ["‘어디로’를 나타내는 번호가 여러 가지예요", "MAC은 현재 링크에서 받을 인터페이스예요",
                "IP는 네트워크 사이의 목적지를 가리켜요", "포트는 기기 안에서 받을 프로그램이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: watch the traffic (capture), safely ----------
def page6(daily):
    a = Anim(4, DUR[daily])
    me = house(110, 200, "나") if daily else laptop(110, 200, "내 PC")
    sv = house(850, 200, "받는 곳") if daily else pc(850, 200, "서버")
    yl = 240
    rows = ["→ 접수됨", "← 수령 확인", "← 이후 기록 없음"] if daily else ["→ 요청 나감", "← 응답 도착", "← 응답 없음"]
    mon = (box(330, 300, 300, 130, GREEN, PANEL, 10, sw=3)
           + text(480, 326, "배송 기록판" if daily else "캡처 도구 (Wireshark)", 17, MUTED, 700)
           + line(480, yl + 12, 480, 300, GREEN, 3, "4 6"))
    perm = (box(250, 290, 460, 150, LINE, PANEL, 12, sw=2)
            + check(290, 330) + text(320, 337, "내 장비 · 허가받은 네트워크" if not daily else "내 택배 · 허가받은 기록", 21, GREEN, 700, "start")
            + cross(290, 380) + text(320, 387, "허가 없는 남의 통신" if not daily else "남의 택배 정보", 21, RED, 700, "start")
            + text(480, 424, "공개 전에 개인정보 확인" if not daily else "함부로 알려 주지 않아요", 18, MUTED, 700))
    body = [me, sv, line(170, yl, 780, yl, LINE, 3),
            a.vis(mon, 1, 3),
            a.vis(text(350, 358, rows[0], 20, BLUE, 700, "start"), 1, 3),
            a.vis(text(350, 388, rows[1], 20, GREEN, 700, "start"), 2, 2),
            a.vis(text(350, 388, rows[2], 20, RED, 700, "start"), 3, 3),
            a.vis(a.move(packet(0, 0, BLUE), [(170, yl), (780, yl)], 1, 0.1, 0.6), 1, 1),
            a.vis(a.move(packet(0, 0, GREEN), [(780, yl), (170, yl)], 2, 0.1, 0.6), 2, 2),
            a.vis(a.move(packet(0, 0, BLUE), [(170, yl), (780, yl)], 3, 0.1, 0.5), 3, 3),
            a.vis(ask(850, 130), 3.55, 3),
            a.vis(perm, 4, 4)]
    if daily:
        t, sub = "배송 기록을 보고 문제를 찾는다", "기록을 보면 어디서 멈췄는지 알 수 있어요"
        caps = ["보낸 택배가 접수됐는지 기록을 봐요", "받은 확인이 돌아왔는지도 봐요",
                "기록이 끊긴 곳에서 문제를 좁혀요", "내 택배나 허가받은 기록만 조회해요"]
    else:
        t, sub = "캡처로 통신을 안전하게 관찰한다", "요청이 나갔는지, 응답이 왔는지 확인해요"
        caps = ["요청이 실제로 나갔는지 캡처로 확인해요", "응답이 돌아왔는지도 볼 수 있어요",
                "응답이 없으면 문제 위치를 좁혀요", "본인 장비나 허가받은 네트워크에서만 봐요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [  # (daily name, network name, builder)
    ("l12-daily-split-parcels", "l12-packet-split", page1),
    ("l12-daily-box-in-box", "l12-header-payload-nesting", page2),
    ("l12-daily-truck-limit", "l12-mtu-limit", page3),
    ("l12-daily-code-row", "l12-hex-fields", page4),
    ("l12-daily-three-wheres", "l12-mac-ip-port-scope", page5),
    ("l12-daily-tracking-log", "l12-capture-observe", page6),
]

# Page text for lesson.md: (title, alt, caption) per (daily, network), and where the network SVG goes.
COPY = [
    (("큰 물건은 작은 상자로 나눠 보낸다",
      "왼쪽에 ‘나’의 집, 오른쪽에 ‘친구’의 집이 있고 가운데에 큰 그림 한 점이 놓입니다. 그림이 작은 상자 네 개로 나뉘고, 상자마다 송장이 붙은 뒤 한 줄로 길을 따라 친구의 집으로 이동해 도착 표시가 나타납니다.",
      "큰 물건도 작은 상자로 나누고, 상자마다 송장을 붙여서 보냅니다."),
     ("데이터는 패킷이라는 작은 단위로 간다",
      "왼쪽에 내 휴대전화, 오른쪽에 친구 휴대전화가 있고 가운데에 큰 사진 파일이 놓입니다. 파일이 작은 패킷 네 개로 나뉘고, 패킷마다 헤더가 붙은 뒤 차례로 친구 휴대전화로 이동해 도착 표시가 나타납니다.",
      "사진 한 장도 작은 패킷으로 나누고, 각 패킷에 헤더를 붙여 보냅니다. 사라진 패킷을 다시 보내는 일은 IP가 아니라 TCP 같은 전송 계층이 맡아요."), 1),
    (("송장 붙은 상자 안의 상자",
      "긴 상자의 왼쪽은 송장, 나머지는 내용물 칸입니다. 내용물 칸을 열자 안에서 송장과 내용물을 가진 작은 상자가 나타나고, 바깥은 큰 상자, 안쪽은 작은 상자라는 이름표가 붙습니다.",
      "송장은 길 안내, 내용물은 실어 나르는 물건입니다. 작은 상자는 큰 상자의 내용물이기도 해요."),
     ("패킷은 헤더와 페이로드로 이뤄진다",
      "이더넷 프레임이 헤더와 페이로드 칸으로 나뉘어 있습니다. 페이로드 칸을 열자 안에서 헤더와 페이로드를 가진 IP 패킷이 나타나고, 바깥은 이더넷 프레임, 안쪽은 IP 패킷이라는 이름표가 붙습니다.",
      "헤더는 전달 정보, 페이로드는 내용입니다. 이더넷 프레임의 페이로드 안에 IP 패킷이 들어 있어요."), 2),
    (("상자 크기에는 한계가 있다",
      "위쪽에 트럭 한 칸에 실을 수 있는 최대 크기를 나타내는 눈금이 있습니다. 작은 상자는 눈금 안에 들어가 통과하고, 눈금보다 큰 가구는 넘쳐서 안 됩니다. 큰 짐을 여러 상자로 나누면 각각 눈금 안에 들어갑니다. 마지막에 길마다 한계가 다를 수 있다는 점선 눈금이 나타납니다.",
      "한계보다 큰 짐은 여러 상자로 나눠 싣습니다. 길마다 한계는 다를 수 있어요."),
     ("MTU는 한 번에 보낼 크기의 한계다",
      "위쪽에 한 번에 보낼 수 있는 최대 크기(MTU) 눈금이 있습니다. 작은 메시지는 눈금 안에 들어가고, 큰 사진은 눈금을 넘어 한 패킷에 못 담깁니다. 여러 패킷으로 나누면 각각 눈금 안에 들어갑니다. 마지막에 연결마다 MTU가 다를 수 있다는 점선 눈금이 나타납니다.",
      "예로 든 이더넷의 MTU 1,500바이트는 IP 패킷(헤더와 페이로드)의 최대 크기입니다. 연결마다 값이 다를 수 있어요."), 1),
    (("송장번호 한 줄을 칸으로 나눠 읽기",
      "숫자 열여섯 칸이 한 줄로 놓여 있고 어디가 무슨 뜻인지 물음표가 뜹니다. 앞 여섯 칸은 받는 곳, 다음 여섯 칸은 보낸 곳, 그다음 두 칸은 종류로 색이 나뉩니다. 종류 칸이 0800이면 뒤에 안쪽 송장이 이어진다고 표시되고, 마지막에 바깥 송장, 안쪽 송장, 내용물이 차례로 펼쳐집니다.",
      "정해진 칸대로 나누어 읽으면 숫자의 의미가 보입니다. 이 숫자 값은 설명용 예시예요."),
     ("16진수 숫자 줄에서 헤더 읽기",
      "16진수 열여섯 칸이 한 줄로 놓여 있고 어디가 주소인지 물음표가 뜹니다. 앞 여섯 칸은 목적지 MAC, 다음 여섯 칸은 출발지 MAC, 그다음 두 칸은 Type으로 색이 나뉩니다. Type이 0800이면 뒤에 IPv4 패킷이 이어진다고 표시되고, 마지막에 이더넷, IP, TCP 또는 UDP가 차례로 펼쳐집니다.",
      "Wireshark는 프로토콜 규칙대로 필드를 나누어 보여 줍니다. 그림의 숫자 값은 설명용 예시예요."), 2),
    (("배송에는 세 가지 ‘어디’가 있다",
      "왼쪽 집에서 가운데 물류센터를 거쳐 오른쪽 건물로 가는 길이 있고, 건물에는 101호와 102호가 있습니다. 먼저 이번 구간 인수자가 첫 구간을, 그다음 최종 주소 건물이 전체 길을, 마지막으로 호수가 건물 안의 받을 사람을 가리킨다고 강조됩니다.",
      "구간 인수자, 최종 건물, 건물 안의 받을 사람은 서로 다른 범위를 가리킵니다."),
     ("MAC·IP·포트는 범위가 달라요",
      "왼쪽 내 노트북에서 가운데 라우터를 거쳐 오른쪽 PC로 가는 길이 있고, PC에는 브라우저와 메신저가 있습니다. 먼저 MAC이 첫 링크를, 그다음 IP가 전체 길의 목적지를, 마지막으로 포트가 PC 안의 프로그램을 가리킨다고 강조됩니다.",
      "MAC은 현재 링크, IP는 네트워크 사이의 목적지, 포트는 기기 안의 프로그램을 가리킵니다. 이 포트는 스위치의 물리 포트가 아니에요. 포트 번호는 예시예요."), 3),
    (("배송 기록을 보고 문제를 찾는다",
      "왼쪽 집에서 오른쪽 받는 곳으로 가는 길 아래에 배송 기록판이 있습니다. 접수됨과 수령 확인이 차례로 기록되고, 한 번은 접수만 되고 이후 기록이 없어 물음표가 뜹니다. 마지막에 내 택배나 허가받은 기록만 조회해야 하고 남의 택배 정보는 안 된다고 표시됩니다.",
      "기록을 보면 어디서 끊겼는지 좁힐 수 있지만, 남의 정보는 함부로 볼 수 없습니다."),
     ("캡처로 통신을 안전하게 관찰한다",
      "왼쪽 내 PC에서 오른쪽 서버로 가는 길 아래에 캡처 도구 화면이 있습니다. 요청 나감과 응답 도착이 차례로 기록되고, 한 번은 요청만 나가고 응답이 없어 서버 쪽에 물음표가 뜹니다. 마지막에 내 장비나 허가받은 네트워크에서만 관찰해야 하고 허가 없는 남의 통신은 안 된다고 표시됩니다.",
      "캡처를 보면 요청과 응답을 확인해 문제 위치를 좁힐 수 있어요. 본인 장비나 허가받은 네트워크에서만 관찰하고, 파일을 공개하기 전에는 개인정보를 확인하세요."), 1),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for (dn, nn, fn), (d, n, after) in zip(PAGES, [(c[0], c[1], c[2]) for c in COPY]):
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        rows.append((dn, *d, nn, *n, after))
        print(dn, nn)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", rows)
