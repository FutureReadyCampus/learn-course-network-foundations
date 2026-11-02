#!/usr/bin/env python3
"""Unit 4 Lesson 5 paired SVGs (data units per layer). Run from the repo root:
python3 scripts/svg_pairs/u4_l05.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/05-*"))
OUT = LESSON / "assets" / "animations"


def dur(daily, n=4):
    return round(n * (3.75 if daily else 4))  # ~4s per step


def cell(x, y, w, h, label, c, fs=16, fill=PANEL):
    return box(x, y, w, h, c, fill, 6, sw=3) + text(x + w / 2, y + h / 2 + fs * 0.36, label, fs, c, 700)


def brace(x0, x1, y, c, label, up=True, fs=17):
    d = 12 if up else -12
    return (line(x0, y, x1, y, c, 4) + line(x0, y, x0, y + d, c, 4) + line(x1, y, x1, y + d, c, 4)
            + pill((x0 + x1) / 2, y - 26 if up else y + 26, label, c, fs, True))


# ---------- Page 1: the same data, named per layer ----------
def page1(daily):
    a = Anim(4, dur(daily))
    D = (560, 100)  # data cell x, w
    names = (("작은 상자", "중간 상자", "큰 상자", "도로 위 이동") if daily else ("세그먼트", "IP 패킷", "프레임", "비트 · 신호"))
    heads = (("작은 라벨", "중간 라벨", "큰 라벨") if daily else ("TCP", "IP", "프레임"))
    data, tail = ("책", "봉인") if daily else ("데이터", "FCS")
    layers = ["L4", "L3", "L2", "L1"]
    ys = [150, 225, 300, 375]
    cols = [ORANGE, BLUE, VIOLET]
    rows = []
    for k in range(3):
        y = ys[k]
        s = cell(D[0], y, D[1], 50, data, GREEN)
        spans = [(490, 70, 0)]
        if k >= 1:
            spans.append((420, 70, 1))
        if k >= 2:
            spans.append((350, 70, 2))
        for x, w, ci in spans:
            s += cell(x, y, w, 50, heads[ci], cols[ci], 15)
        left = 490 if k == 0 else 420 if k == 1 else 350
        right = 660
        if k == 2:
            s += cell(660, y, 60, 50, tail, VIOLET, 15)
            right = 720
        s += box(left - 5, y - 5, right - left + 10, 60, cols[k], "none", 8, sw=2)
        rows.append(s)
    if daily:
        l1 = line(350, 410, 720, 410, MUTED, 4) + f'<rect x="440" y="382" width="90" height="30" rx="4" fill="{VIOLET}"/><rect x="530" y="392" width="34" height="20" rx="3" fill="{MUTED}"/><circle cx="462" cy="418" r="8" fill="{BG}" stroke="{MUTED}" stroke-width="3"/><circle cx="512" cy="418" r="8" fill="{BG}" stroke="{MUTED}" stroke-width="3"/>'
    else:
        l1 = "".join(box(350 + i * 31, 380, 28, 40, MUTED, PANEL, 5, sw=2) + text(364 + i * 31, 408, "01101001"[i % 8] if True else "", 20, TXT, 700) for i in range(12))
    body = []
    for k in range(4):
        y = ys[k]
        lab = text(60, y + 34, layers[k], 26, cols[k] if k < 3 else MUTED, 700, "start") + text(740, y + 33, names[k], 20, cols[k] if k < 3 else MUTED, 700, "start")
        body.append(a.vis(lab + (rows[k] if k < 3 else l1), k + 1, 4))
    body.append(a.vis(text(480, 450, "트럭은 새 상자가 아니라, 큰 상자를 실어 날라요" if daily else "L1은 새 단위가 아니라 프레임을 비트와 신호로 전달해요", 21, MUTED, 700), 4, 4))
    if daily:
        t, sub = "같은 책, 보는 곳마다 달라지는 이름", "겹쳐 포장될수록 바깥 상자의 이름으로 불러요"
        caps = ["작은 상자는 책에 라벨 하나를 더한 단위예요", "중간 상자는 작은 상자를 담은 단위예요",
                "큰 상자는 라벨과 봉인이 붙은 가장 바깥 단위예요", "도로 위에서는 큰 상자가 그대로 실려 가요"]
    else:
        t, sub = "계층마다 달라지는 데이터 이름", "L4 세그먼트 → L3 패킷 → L2 프레임, L1은 비트와 신호"
        caps = ["L4(TCP)가 다루는 단위는 세그먼트예요", "L3(IP)가 다루는 단위는 패킷이에요",
                "L2가 다루는 단위는 프레임이에요", "L1은 프레임을 비트와 신호로 전달해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: socket stream vs. write/read counts ----------
def page2(daily):
    a = Anim(4, dur(daily))
    X0, W = 300, 38
    cols_w = [ORANGE] * 3 + [BLUE] * 5 + [GREEN] * 2
    tube = box(X0 - 6, 244, 10 * W + 12, 62, MUTED, PANEL, 10, sw=3)
    mk = lambda cs: "".join(box(X0 + i * W + 2, 250, W - 4, 50, cs[i], cs[i], 4, sw=1) for i in range(10))
    sender = box(60, 215, 160, 120, BLUE, PANEL, 12, sw=3) + text(140, 282, "물 붓는 사람" if daily else "보내는 앱", 20, TXT, 700)
    recv = box(760, 215, 140, 120, BLUE, PANEL, 12, sw=3) + text(830, 282, "물 받는 사람" if daily else "받는 앱", 20, TXT, 700)
    wl = ("붓기 1회", "붓기 2회", "붓기 3회") if daily else ("쓰기 1", "쓰기 2", "쓰기 3")
    rl = ("받기 1회", "받기 2회") if daily else ("읽기 1", "읽기 2")
    gx = lambda i: X0 + i * W
    wb = (brace(gx(0) + 2, gx(3) - 2, 232, ORANGE, wl[0]) + brace(gx(3) + 2, gx(8) - 2, 232, BLUE, wl[1])
          + brace(gx(8) + 2, gx(10) - 2, 232, GREEN, wl[2]))
    rb = brace(gx(0) + 2, gx(5) - 2, 318, VIOLET, rl[0], up=False) + brace(gx(5) + 2, gx(10) - 2, 318, ORANGE, rl[1], up=False)
    flow = "".join(f'<polygon points="{X0 + 20 + i * 120},262 {X0 + 40 + i * 120},275 {X0 + 20 + i * 120},288" fill="{BG}" fill-opacity=".55"/>' for i in range(3))
    uni = [BLUE] * 10
    body = [sender, recv, tube + line(220, 275, 294, 275, LINE, 3) + line(686, 275, 760, 275, LINE, 3),
            a.vis(mk(cols_w) + wb, 1, 1),
            a.vis(mk(uni) + flow + text(490, 380, "이어진 하나의 흐름이에요" if daily else "이어진 하나의 바이트 흐름(Stream)이에요", 22, BLUE, 700), 2, 2),
            a.vis(mk(uni) + rb, 3, 3),
            a.vis(mk(uni) + wb + rb + text(490, 405, "넣은 횟수와 꺼낸 횟수는 같지 않아도 돼요" if daily else "쓴 횟수와 읽은 횟수는 같지 않아도 돼요", 21, TXT, 700), 4, 4)]
    if daily:
        t, sub = "호스로 이어지는 물줄기", "붓는 횟수와 받는 횟수가 같을 필요는 없어요"
        caps = ["물을 세 번에 나눠 붓는다고 해 볼게요", "호스 안에서는 하나로 이어진 물줄기예요",
                "받는 쪽은 자기 편한 만큼씩 받아요", "횟수가 달라도 같은 물이 도착해요"]
    else:
        t, sub = "소켓과 스트림", "TCP 소켓에서는 데이터가 이어진 흐름으로 다뤄져요"
        caps = ["앱이 데이터를 세 번에 나눠 써요", "TCP에서는 이어진 하나의 흐름(Stream)이에요",
                "받는 앱은 자기 단위로 읽어요", "쓴 횟수와 읽은 횟수가 같다고 가정하면 안 돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: MTU vs MSS ----------
def page3(daily):
    a = Anim(3, dur(daily, 3))
    X, Y, H = 130, 215, 64
    if daily:
        lab = ("포장", "송장", "물건")
        mtu, mss = "큰 상자 한도 15kg", "담을 수 있는 물건의 한도"
    else:
        lab = ("IP 헤더", "TCP 헤더", "TCP 데이터")
        mtu, mss = "MTU 1,500B (IP 패킷 전체의 상한)", "MSS: TCP 데이터의 상한"
    whole = cell(X, Y, 700, H, "IP 패킷 전체" if not daily else "중간 상자 전체", MUTED, 18)
    three = cell(X, Y, 110, H, lab[0], BLUE, 15) + cell(X + 110, Y, 110, H, lab[1], ORANGE, 15) + cell(X + 220, Y, 480, H, lab[2], GREEN, 20)
    top = brace(X, X + 700, 190, BLUE, mtu)
    body = [a.vis(top, 1, 3), a.vis(whole, 1, 1), a.vis(three, 2, 3),
            a.vis(brace(X + 220, X + 700, Y + H + 14, GREEN, mss, up=False), 3, 3),
            a.vis(text(480, 400, "물건 한도는 상자 한도보다 작아요" if daily else "MSS는 MTU보다 작은 값이에요", 22, MUTED, 700), 3, 3)]
    if daily:
        t, sub = "상자 한도와 물건 한도는 다르다", "상자 전체의 한도와 담을 수 있는 물건의 한도는 달라요"
        caps = ["중간 상자 전체에는 한도 15kg이 있어요", "포장과 송장이 자리를 차지해요",
                "그래서 물건 한도는 상자 한도와 같지 않아요"]
    else:
        t, sub = "MTU는 패킷 전체, MSS는 TCP 데이터", "재는 범위가 달라서 MTU와 MSS는 같은 값이 아니에요"
        caps = ["MTU 1,500B는 IP 패킷 전체의 상한이에요", "IP 헤더와 TCP 헤더가 자리를 차지해요",
                "MSS는 TCP 데이터만의 상한이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: segmentation (5 steps) ----------
def page4(daily):
    a = Anim(5, dur(daily, 5))
    widths = [150, 150, 150, 150, 70]
    cuts = [240, 400, 560, 720]
    stream = box(80, 150, 720, 44, GREEN, PANEL, 6, sw=3) + text(440, 180, "긴 리본" if daily else "긴 Stream (예: 4MB 파일)", 20, GREEN, 700)
    ruler = "".join(line(x, 138, x, 206, ORANGE, 3, "5 4") for x in cuts) + brace(80, 240, 132, ORANGE, "한 칸 길이" if daily else "MSS", up=True, fs=15)
    ruler = ruler.replace('y2="132"', 'y2="132"')
    pieces3 = ""
    x = 117
    for i, w in enumerate(widths):
        pieces3 += cell(x, 262, w, 44, str(i + 1), GREEN, 18)
        x += w + 14
    short = pill(117 + 4 * 164 + 35, 336, "마지막은 짧아요", ORANGE, 16)
    pieces4 = ""
    x = 47
    for i, w in enumerate(widths):
        pieces4 += cell(x, 262, 28, 44, "", ORANGE, 14) + cell(x + 28, 262, w, 44, str(i + 1), GREEN, 18)
        x += w + 28 + 14
    tag4 = pill(480, 232, "조각마다 송장" if daily else "조각마다 TCP 헤더 → Segment", ORANGE, 17, True)
    merged = (box(80, 376, 720, 44, GREEN, PANEL, 6, sw=3) + text(440, 406, "다시 이어 붙은 리본" if daily else "연속된 Stream", 20, GREEN, 700)
              + f'<polygon points="440,326 428,344 452,344" fill="{BLUE}"/>' + line(440, 344, 440, 370, BLUE, 4)
              + text(470, 360, "받는 쪽에서 이어 붙여요" if daily else "수신 TCP가 이어 붙여요", 18, BLUE, 700, "start"))
    body = [a.vis(stream, 1, 2), a.vis(ruler, 2, 2),
            a.vis(pieces3 + short, 3, 3), a.vis(pieces4 + tag4, 4, 5), a.vis(merged, 5, 5)]
    if daily:
        t, sub = "긴 리본을 한 칸 길이로 잘라 담는다", "나머지가 남으면 마지막 조각이 짧아요"
        caps = ["아주 긴 리본을 보낸다고 해 볼게요", "한 칸에 담을 길이대로 눈금을 그어요",
                "눈금대로 자르면 마지막 조각은 더 짧아요", "조각마다 송장을 붙여 상자에 담아요", "받는 쪽에서 다시 이어 붙여요"]
    else:
        t, sub = "긴 Stream을 Segment로 나눈다", "이 과정이 세그멘테이션(분할)이에요"
        caps = ["보낼 Stream이 MSS보다 훨씬 길어요", "TCP가 MSS 크기대로 나눌 곳을 정해요",
                "나누어 떨어지지 않으면 마지막은 더 짧아요", "조각마다 TCP 헤더가 붙어 Segment가 돼요", "수신 TCP가 이어 붙여 Stream으로 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: frame is bigger than the MTU; the chain ----------
def page5(daily):
    a = Anim(4, dur(daily))
    pk = cell(300, 210, 360, 60, "중간 상자" if daily else "IP 패킷", BLUE, 20)
    fh = cell(190, 210, 110, 60, "큰 상자 송장" if daily else "프레임 헤더", VIOLET, 15)
    tl = cell(660, 210, 100, 60, "봉인 테이프" if daily else "FCS", VIOLET, 15)
    mtu = brace(300, 660, 190, BLUE, "한도 15kg (중간 상자 기준)" if daily else "MTU 1,500B (IP 패킷 기준)")
    allb = brace(190, 760, 294, VIOLET, "큰 상자 전체" if daily else "프레임 전체", up=False)
    neq = text(480, 392, "큰 상자 전체 ≠ 중간 상자 한도" if daily else "프레임 전체 크기 ≠ MTU", 26, TXT, 700)
    chips = ([("이어진 리본", "프로그램"), ("조각 상자", "나눠 담기"), ("중간 상자", "한도가 있어요"), ("큰 상자", "링크용 포장"), ("도로", "트럭 이동")] if daily else
             [("Stream", "소켓"), ("Segment", "TCP · MSS"), ("IP Packet", "IP · MTU"), ("Frame", "Ethernet"), ("비트 · 신호", "L1")])
    cc = [GREEN, ORANGE, BLUE, VIOLET, MUTED]
    chain = ""
    for i, (n, r) in enumerate(chips):
        x = 110 + i * 185
        chain += box(x - 78, 365, 156, 66, cc[i], PANEL, 12, sw=3) + text(x, 394, n, 19, cc[i], 700) + text(x, 418, r, 15, MUTED, 700)
        if i < 4:
            chain += text(x + 92, 406, "→", 24, TXT, 700)
    body = [a.vis(pk + mtu, 1, 4), a.vis(fh + tl + allb, 2, 4), a.vis(neq, 3, 3), a.vis(chain, 4, 4)]
    if daily:
        t, sub = "큰 상자는 중간 상자 한도보다 크다", "송장과 봉인은 한도 밖에 붙어요"
        caps = ["한도 15kg은 중간 상자에 적용돼요", "큰 상자에는 송장과 봉인이 더 붙어요",
                "큰 상자 전체를 한도와 같다고 보면 안 돼요", "리본 → 조각 → 중간 상자 → 큰 상자 → 도로"]
    else:
        t, sub = "프레임 전체 크기와 MTU는 다르다", "MTU는 IP 패킷, 프레임에는 링크 헤더와 FCS가 더 붙어요"
        caps = ["MTU 1,500B는 IP 패킷의 상한이에요", "프레임에는 링크 헤더와 FCS가 더 붙어요",
                "프레임 전체 크기를 MTU와 같게 보면 안 돼요", "Stream → Segment → Packet → Frame 순서예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: TCP segment vs UDP datagram, both inside IP packets ----------
def page6(daily):
    a = Anim(4, dur(daily))
    L, R = 130, 530
    if daily:
        tn, un = ("이어진 리본", "조각 상자"), ("엽서", "엽서 한 장")
        p_t, p_u, p_ip = "리본 방식", "엽서 방식", "배달 상자"
        tt, ut = "조각", "낱장"
    else:
        tn, un = ("Stream", "Segment"), ("메시지", "Datagram")
        p_t, p_u, p_ip = "TCP", "UDP", "IP Packet"
        tt, ut = "TCP", "UDP"
    lane = lambda x, col: ""
    tcp1 = box(L, 170, 340, 44, GREEN, PANEL, 6, sw=3) + text(L + 170, 200, tn[0], 19, GREEN, 700)
    tcp2 = "".join(cell(L + i * 150, 250, 140, 44, "", ORANGE, 14) + cell(L + i * 150, 250, 30, 44, tt, ORANGE, 12) + text(L + i * 150 + 90, 279, "데이터", 15, GREEN, 700) for i in range(2))
    tcp2 += pill(L + 170, 316, tn[1], ORANGE, 15, True)
    udp1 = "".join(cell(R + i * 150, 170, 110, 44, "메시지" if not daily else "엽서", GREEN, 17) for i in range(2))
    udp2 = "".join(cell(R + i * 150, 250, 140, 44, "", BLUE, 14) + cell(R + i * 150, 250, 30, 44, ut, BLUE, 12) + text(R + i * 150 + 90, 279, "데이터", 15, GREEN, 700) for i in range(2))
    udp2 += pill(R + 170 - 20, 316, un[1], BLUE, 15, True)
    ip = lambda x, inner: "".join(cell(x + i * 175, 350, 165, 44, "", VIOLET, 14) + cell(x + i * 175, 350, 30, 44, "IP", VIOLET, 13)
                                  + box(x + i * 175 + 32, 352, 131, 40, MUTED, BG, 4, sw=1) + text(x + i * 175 + 98, 378, inner, 14, MUTED, 700) for i in range(2))
    body = [a.vis(pill(L + 170, 140, p_t, ORANGE, 18, True) + tcp1 + tcp2, 1, 4),
            a.vis(pill(R + 170, 140, p_u, BLUE, 18, True) + udp1 + udp2, 2, 4),
            a.vis(ip(L - 5, un[1] if False else tn[1]) + ip(R - 5, un[1]) + pill(480, 418, p_ip + " 안에 담겨 가요", VIOLET, 17, True), 3, 4),
            a.vis(text(480, 456, "말할 땐 ‘패킷’이라 불러도, 정확히는 이름이 달라요" if not daily else "다 같이 ‘택배’라 불러도, 정확히는 이름이 달라요", 19, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "리본 방식과 엽서 방식", "둘 다 배달 상자에 담겨 가요"
        caps = ["리본은 이어진 흐름을 조각으로 나눠요", "엽서는 낱장 하나가 한 단위예요",
                "두 방식 모두 배달 상자 안에 담겨요", "일상에서는 다 ‘택배’라고도 불러요"]
    else:
        t, sub = "TCP 세그먼트와 UDP 데이터그램", "L4 단위는 다르고, 둘 다 IP 패킷에 담겨요"
        caps = ["TCP는 Stream을 나눈 Segment를 써요", "UDP는 메시지 하나가 Datagram이에요",
                "둘 다 IP 패킷의 페이로드로 가요", "정확히 말할 땐 이름을 구별해요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    ("l15-daily-name-by-box", "l15-unit-names-by-layer", page1),
    ("l15-daily-hose-flow", "l15-stream-vs-write-read", page2),
    ("l15-daily-box-limit", "l15-mtu-vs-mss", page3),
    ("l15-daily-ribbon-cut", "l15-stream-segmentation", page4),
    ("l15-daily-outer-box", "l15-frame-vs-mtu", page5),
    ("l15-daily-ribbon-postcard", "l15-segment-vs-datagram", page6),
]

COPY = [
    (("같은 책, 보는 곳마다 달라지는 이름",
      "위에서 아래로 작은 상자, 중간 상자, 큰 상자가 한 줄씩 나타납니다. 책에 작은 라벨이 붙은 것이 작은 상자, 거기에 중간 라벨이 더해진 것이 중간 상자, 큰 라벨과 봉인이 더해진 것이 큰 상자입니다. 마지막 줄에는 트럭이 큰 상자를 그대로 싣고 도로를 달립니다.",
      "겹쳐 포장될수록 바깥 상자의 이름으로 부릅니다. 트럭은 새 상자를 만들지 않고 큰 상자를 실어 나릅니다."),
     ("계층마다 달라지는 데이터 이름",
      "위에서 아래로 L4 세그먼트, L3 패킷, L2 프레임이 한 줄씩 나타납니다. 데이터에 TCP 헤더가 붙으면 세그먼트, IP 헤더가 더해지면 패킷, 프레임 헤더와 FCS가 더해지면 프레임입니다. 마지막 줄 L1에는 비트가 늘어서 있고, 새 단위가 아니라 프레임을 비트와 신호로 전달한다는 설명이 나타납니다.",
      "같은 데이터가 어느 계층에서 보이느냐에 따라 세그먼트, 패킷, 프레임으로 불립니다. L1은 프레임을 비트와 신호로 전달해요."), 1),
    (("호스로 이어지는 물줄기",
      "물 붓는 사람이 호스에 물을 세 번에 나눠 붓습니다. 호스 안에서는 하나로 이어진 물줄기가 되고, 물 받는 사람은 두 번에 나눠 받습니다. 마지막에 붓는 횟수와 받는 횟수가 같지 않아도 된다는 설명이 나타납니다.",
      "나눠 붓는 횟수와 받는 횟수가 달라도 같은 물이 도착합니다."),
     ("소켓과 스트림",
      "보내는 앱이 데이터를 세 번에 나눠 씁니다. TCP 소켓 안에서는 이어진 하나의 바이트 흐름이 되고, 받는 앱은 두 번에 나눠 읽습니다. 마지막에 쓴 횟수와 읽은 횟수가 같지 않을 수 있다는 설명이 나타납니다.",
      "TCP에서는 쓴 횟수와 읽은 횟수가 같다고 가정하면 안 되고, 메시지 경계는 애플리케이션이 약속해야 해요."), 1),
    (("상자 한도와 물건 한도는 다르다",
      "중간 상자 전체에 한도 15kg이 있습니다. 포장과 송장이 차례로 자리를 차지하고, 마지막에 담을 수 있는 물건의 한도가 표시되며 물건 한도는 상자 한도보다 작다는 설명이 나타납니다.",
      "상자 전체의 한도와 담을 수 있는 물건의 한도는 다릅니다."),
     ("MTU는 패킷 전체, MSS는 TCP 데이터",
      "IP 패킷 전체에 MTU 1,500B 상한이 있습니다. IP 헤더와 TCP 헤더가 차례로 자리를 차지하고, 마지막에 남은 TCP 데이터 부분의 상한이 MSS로 표시되며 MSS는 MTU보다 작은 값이라는 설명이 나타납니다. 칸의 너비는 실제 비율이 아닙니다.",
      "MTU는 IP 패킷 전체, MSS는 TCP 데이터 부분의 상한입니다. 계산은 Unit 7에서 해 봅니다. 칸의 너비는 실제 비율이 아니에요."), 2),
    (("긴 리본을 한 칸 길이로 잘라 담는다",
      "아주 긴 리본에 한 칸 길이 눈금이 그어지고, 눈금대로 자르면 다섯 조각이 되며 마지막 조각은 짧습니다. 조각마다 송장이 붙어 상자에 담기고, 마지막에 받는 쪽에서 다시 이어 붙입니다.",
      "나누어 떨어지지 않으면 마지막 조각은 더 짧아요."),
     ("긴 Stream을 Segment로 나눈다",
      "긴 Stream에 MSS 크기 눈금이 그어지고, 눈금대로 나누면 다섯 조각이 되며 마지막 조각은 짧습니다. 조각마다 TCP 헤더가 붙어 Segment가 되고, 마지막에 수신 TCP가 이어 붙여 연속된 Stream으로 줍니다.",
      "세그멘테이션은 긴 Stream을 MSS에 맞는 조각으로 나누는 과정이에요. 그림의 조각 수는 예시예요."), 2),
    (("큰 상자는 중간 상자 한도보다 크다",
      "중간 상자에 한도 15kg이 표시됩니다. 그 양옆에 큰 상자 송장과 봉인 테이프가 붙어 큰 상자 전체가 만들어지고, 큰 상자 전체는 중간 상자 한도와 같지 않다고 표시됩니다. 마지막에 이어진 리본, 조각 상자, 중간 상자, 큰 상자, 도로가 화살표로 이어집니다.",
      "한도는 중간 상자에 적용되고, 큰 상자에는 송장과 봉인이 더 붙습니다."),
     ("프레임 전체 크기와 MTU는 다르다",
      "IP 패킷에 MTU 1,500B 상한이 표시됩니다. 그 양옆에 프레임 헤더와 FCS가 붙어 프레임 전체가 만들어지고, 프레임 전체 크기는 MTU와 같지 않다고 표시됩니다. 마지막에 Stream, Segment, IP Packet, Frame, 비트·신호가 화살표로 이어집니다.",
      "MTU는 기본 예에서 IP 패킷의 상한이고, 프레임에는 링크 헤더와 FCS가 더 붙어요."), 1),
    (("리본 방식과 엽서 방식",
      "왼쪽에서는 이어진 리본이 조각 상자로 나뉘고, 오른쪽에서는 엽서가 낱장 하나씩 낱장 단위가 됩니다. 두 방식의 조각과 낱장이 모두 배달 상자 안에 담기고, 마지막에 일상에서는 모두 택배라 불러도 정확히는 이름이 다르다는 설명이 나타납니다.",
      "이어진 흐름을 나누는 방식과 낱장을 그대로 보내는 방식은 이름이 다릅니다."),
     ("TCP 세그먼트와 UDP 데이터그램",
      "왼쪽에서는 TCP가 Stream을 나눈 Segment를 만들고, 오른쪽에서는 UDP가 메시지 하나를 Datagram으로 만듭니다. 둘 다 IP 패킷의 페이로드로 담기고, 마지막에 일상에서는 모두 패킷이라 불러도 정확히 말할 땐 이름을 구별한다는 설명이 나타납니다.",
      "TCP의 L4 단위는 Segment, UDP의 L4 단위는 Datagram, IP의 L3 단위는 Packet입니다."), 2),
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
