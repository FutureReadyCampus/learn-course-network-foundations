#!/usr/bin/env python3
"""Unit 6 Lesson 2 (DHCP) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u6_l02.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/12-*"))
OUT = LESSON / "assets" / "animations"


def dur(daily, n=4):
    return round(n * (3.75 if daily else 4))


def cell(x, y, w, h, label, c, fs=16, fill=PANEL):
    return box(x, y, w, h, c, fill, 6, sw=3) + text(x + w / 2, y + h / 2 + fs * 0.36, label, fs, c, 700)


def hl(x, y, w, h, c=ORANGE, rx=10):
    return box(x - 4, y - 4, w + 8, h + 8, c, "none", rx, sw=5)


def arrow(x0, x1, y, c, w=6):
    d = 1 if x1 > x0 else -1
    return (line(x0, y, x1 - d * 16, y, c, w) + f'<polygon points="{x1},{y} {x1 - d * 24},{y - w - 6} {x1 - d * 24},{y + w + 6}" fill="{c}"/>')


def varrow(x, y0, y1, c, w=5):
    d = 1 if y1 > y0 else -1
    return (line(x, y0, x, y1 - d * 12, c, w) + f'<polygon points="{x},{y1} {x - 9},{y1 - d * 16} {x + 9},{y1 - d * 16}" fill="{c}"/>')


def dev(daily, x, y, label=None):
    return house(x, y, label) if daily else laptop(x, y, label)


# ---------- Page 1: empty settings get filled by the server ----------
def page1(daily):
    a = Anim(4, dur(daily))
    rows = ["내 호수", "우리 동네 범위", "정문(출구) 위치", "안내 전화"] if daily else ["IP 주소", "서브넷 마스크", "기본 게이트웨이", "DNS 서버"]
    vals = ["302호", "우리 단지", "정문", "안내 데스크"] if daily else ["192.168.0.100", "255.255.255.0", "192.168.0.1", "8.8.8.8"]
    ys = [195 + 52 * i for i in range(4)]
    card = (box(50, 140, 370, 270, MUTED, PANEL, 14, sw=3) + text(235, 172, "새 입주자" if daily else "새 노트북", 20, MUTED, 700)
            + "".join(text(70, y + 28, r, 17, TXT, 700, "start") for y, r in zip(ys, rows)))
    empty = "".join(box(235, y, 170, 42, ORANGE, BG, 8, dash=True, sw=2) + text(320, y + 30, "?", 22, ORANGE, 700) for y in ys)
    filled = "".join(box(235, y, 170, 42, GREEN, BG, 8, sw=2) + text(320, y + 28, v, 16 if not daily else 18, GREEN, 700) for y, v in zip(ys, vals))
    srv = (box(620, 170, 280, 220, BLUE, PANEL, 14, sw=3) + text(760, 200, "관리사무소" if daily else "DHCP 서버", 20, BLUE, 700)
           + box(645, 220, 230, 150, BLUE, BG, 10, dash=True, sw=2) + text(760, 242, "입주 안내 카드" if daily else "설정 서랍", 15, MUTED, 700)
           + "".join(text(760, 270 + 26 * i, v, 16, MUTED, 700) for i, v in enumerate(vals)))
    srv_on = "".join(text(760, 270 + 26 * i, v, 16, GREEN, 700) for i, v in enumerate(vals))
    body = [card, srv, a.vis(empty, 1, 2), a.vis(filled, 3, 4),
            a.vis(pill(235, 124, "손으로 직접 입력", RED, 17) + cross(95, 124)
                  + text(235, 436, "기기·장소를 바꿀 때마다 다시 해야 해요" if not daily else "이사할 때마다 다시 알아봐야 해요", 20, RED, 700), 2, 2),
            a.vis(srv_on + arrow(610, 430, 285, GREEN, 7) + text(520, 262, "채워 줘요", 18, GREEN, 700), 3, 4),
            a.vis(check(120, 436) + text(150, 443, "설정 전달 = 자동 · 회선이 동작해야 인터넷" if not daily else "카드를 받아도 길(회선)이 열려 있어야 해요", 20, TXT, 700, "start"), 4, 4)]
    if daily:
        t, sub = "새 입주자에게 안내 카드를 채워 준다", "호수, 동네 범위, 정문, 안내 전화를 한 번에 알려 줘요"
        caps = ["이사 왔지만 알아야 할 것이 비어 있어요", "하나하나 직접 알아보면 번거로워요",
                "관리사무소가 안내 카드를 채워 줘요", "카드를 받아도 길이 열려 있어야 해요"]
    else:
        t, sub = "DHCP가 네트워크 설정을 채워 준다", "연결하면 IP·마스크·게이트웨이·DNS를 받아 와요"
        caps = ["연결했지만 설정 칸이 비어 있어요", "직접 입력하면 바꿀 때마다 번거로워요",
                "DHCP 서버가 설정 값을 채워 줘요", "‘자동’은 설정 전달이에요, 회선도 필요해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: the four values and what each is for ----------
def page2(daily):
    a = Anim(4, dur(daily))
    names = ["호수", "동네(단지) 경계", "정문 (바깥 출구)", "안내 전화"] if daily else ["IP 주소", "서브넷 마스크", "기본 게이트웨이", "DNS 서버"]
    subs = ["우리 집을 구별해요", "같은 동네인지 가려요", "다른 동네로 나가는 첫 문", "이름 → 호수를 알려 줘요"] if daily else \
           ["내 인터페이스를 구별해요", "같은 네트워크인지 가려요", "다른 네트워크로 가는 첫 라우터", "도메인 이름 → IP 주소"]
    cols = [GREEN, BLUE, ORANGE, VIOLET]
    ys = [150 + 68 * i for i in range(4)]
    lst = "".join(box(40, y, 380, 56, LINE, PANEL, 10, sw=2) + text(60, y + 25, names[i], 20, MUTED, 700, "start") + text(60, y + 46, subs[i], 15, MUTED, 700, "start") for i, y in enumerate(ys))
    on = lambda i: box(40, ys[i], 380, 56, cols[i], PANEL, 10, sw=4) + text(60, ys[i] + 25, names[i], 20, cols[i], 700, "start") + text(60, ys[i] + 46, subs[i], 15, TXT, 700, "start")
    me = lambda x, y: dev(daily, x, y, "나" if daily else "내 PC")
    s1 = me(690, 270) + pill(690, 190, "302호" if daily else "192.168.0.100", GREEN, 20, True) + line(690, 210, 690, 232, GREEN, 3, "4 4")
    s2 = (f'<ellipse cx="690" cy="280" rx="190" ry="115" fill="none" stroke="{BLUE}" stroke-width="4" stroke-dasharray="9 7"/>'
          + text(690, 190, "같은 동네" if daily else "같은 네트워크", 18, BLUE, 700) + me(610, 290)
          + box(730, 250, 70, 46, BLUE, PANEL, 8, sw=2) + text(765, 280, "이웃" if daily else "PC", 17, TXT, 700)
          + box(860, 380, 60, 40, MUTED, PANEL, 8, dash=True, sw=2) + text(890, 405, "밖", 15, MUTED, 700))
    s3 = (me(540, 300) + (booth(690, 300, "정문") if daily else router(690, 300, "첫 라우터")) + line(590, 300, 650, 300, ORANGE, 4) + arrow(735, 800, 300, ORANGE, 5)
          + box(800, 230, 120, 120, MUTED, PANEL, 12, dash=True, sw=2) + text(860, 296, "다른 동네" if daily else "다른 네트워크", 16, MUTED, 700))
    s4 = (me(540, 320) + box(780, 190, 130, 56, VIOLET, PANEL, 10, sw=3) + text(845, 224, "안내 전화" if daily else "DNS 서버", 18, VIOLET, 700)
          + arrow(590, 770, 232, VIOLET, 4) + text(690, 214, "홍길동 집?" if daily else "example.com ?", 17, VIOLET, 700)
          + arrow(770, 590, 292, GREEN, 4) + text(690, 322, "3동 302호" if daily else "203.0.113.20", 17, GREEN, 700))
    body = [lst] + [a.vis(on(i) + s, i + 1, i + 1) for i, s in enumerate((s1, s2, s3, s4))]
    body.append(a.vis(text(480, 440, "관리사무소는 카드를 줄 뿐, 배달·안내는 하지 않아요" if daily else "DHCP는 설정을 전달할 뿐, 운반·이름 변환은 하지 않아요", 19, MUTED, 700), 4, 4))
    if daily:
        t, sub = "안내 카드 네 가지는 서로 다른 일을 한다", "호수, 동네 경계, 정문, 안내 전화"
        caps = ["호수는 우리 집을 구별해요", "동네 경계는 같은 동네인지 가려 줘요",
                "정문은 다른 동네로 나가는 첫 문이에요", "안내 전화는 이름을 호수로 알려 줘요"]
    else:
        t, sub = "DHCP가 알려 주는 네 가지 설정", "값마다 맡은 일이 달라요 (예시 값)"
        caps = ["IP 주소는 내 인터페이스를 구별해요", "서브넷 마스크는 같은 네트워크를 가려요",
                "기본 게이트웨이는 밖으로 나가는 첫 라우터예요", "DNS 서버는 이름을 IP 주소로 알려 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: address pool and lease ----------
def page3(daily):
    a = Anim(4, dur(daily))
    X0, W, G, Y = 104, 84, 12, 200
    cx = lambda i: X0 + i * (W + G)
    labs = ["100", "101", "102", "103", "104", "…", "199", "200"]
    suf = "호" if daily else ""
    pre = "" if daily else "."
    free = "".join(cell(cx(i), Y, W, 56, (pre + labs[i] + suf) if labs[i] != "…" else "…", GREEN if labs[i] != "…" else MUTED, 20) for i in range(8))
    cap = text(480, 172, "객실 100호 ~ 200호" if daily else "주소 풀: 192.168.0.100 ~ .200 (예시)", 20, MUTED, 700)
    taken = (cell(cx(0), Y, W, 56, pre + "100" + suf, ORANGE, 20, ORANGE).replace(f'fill="{ORANGE}"', f'fill="{ORANGE}"') + text(cx(0) + W / 2, Y + 50, "A", 17, BG, 700) +
             cell(cx(1), Y, W, 56, pre + "101" + suf, BLUE, 20, BLUE) + text(cx(1) + W / 2, Y + 50, "B", 17, BG, 700))
    taken = (box(cx(0), Y, W, 56, ORANGE, ORANGE, 6, sw=3) + text(cx(0) + W / 2, Y + 25, pre + "100" + suf, 20, BG, 700) + text(cx(0) + W / 2, Y + 46, "A", 16, BG, 700)
             + box(cx(1), Y, W, 56, BLUE, BLUE, 6, sw=3) + text(cx(1) + W / 2, Y + 25, pre + "101" + suf, 20, BG, 700) + text(cx(1) + W / 2, Y + 46, "B", 16, BG, 700))
    bar = lambda i, w, c: box(cx(i), 268, W, 10, LINE, PANEL, 5, sw=1) + f'<rect x="{cx(i)}" y="268" width="{w}" height="10" rx="5" fill="{c}"/>'
    who = "손님" if daily else "노트북"
    cl = (cell(104, 360, 220, 54, f"{who} A → {pre}100{suf}", ORANGE, 18) + cell(344, 360, 220, 54, f"{who} B → {pre}101{suf}", BLUE, 18))
    conflict = (box(cx(2), Y, W, 56, RED, "none", 6, dash=True, sw=4) + cross(cx(2) + W - 6, Y + 4)
                + cell(620, 360, 250, 54, "따로 쓰는 방" if daily else "수동 설정한 장치 .102", MUTED, 17)
                + line(745, 360, cx(2) + W / 2, 262, RED, 3, "5 4"))
    body = [cap, a.vis(free, 1, 1), a.vis(free + taken + bar(0, W, ORANGE) + bar(1, W, BLUE) + cl
                                         + text(cx(0) + W / 2, 302, "임대 기간" if not daily else "숙박 기간", 14, MUTED, 700), 2, 4)]
    body.append(a.vis(box(cx(0), 268, W, 10, BG, BG, 5, sw=1) + bar(0, W // 2, ORANGE) + bar(1, W // 2, BLUE)
                      + pill(480, 318, "갱신하면 같은 주소를 계속 써요" if not daily else "연장하면 같은 방을 계속 써요", GREEN, 17), 3, 3))
    body.append(a.vis(conflict + text(480, 440, "풀과 고정 주소는 겹치지 않게 해요" if not daily else "고정으로 쓰는 방은 빌려 주는 방에서 빼요", 21, RED, 700), 4, 4))
    if daily:
        t, sub = "객실을 빌려 주고 기간을 관리한다", "방 목록에서 빈 방을 일정 기간 빌려 줘요"
        caps = ["프런트에는 빌려 줄 방 목록이 있어요", "손님마다 방 하나를 숙박 기간만큼 빌려요",
                "기간이 끝나기 전에 연장하면 같은 방이에요", "직원이 쓰는 방을 빌려 주면 충돌해요"]
    else:
        t, sub = "주소 풀에서 주소를 임대한다", "범위와 숫자는 구조를 보여 주는 예시예요"
        caps = ["서버는 나눠 줄 주소 목록(풀)을 가져요", "클라이언트마다 주소 하나를 일정 기간 임대해요",
                "갱신하면 같은 주소를 계속 쓸 수 있어요", "풀의 주소를 따로 설정하면 충돌해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: Discover is shouted to everyone in range ----------
def page4(daily):
    a = Anim(4, dur(daily))
    pk = packet if not daily else parcel
    cli = dev(daily, 90, 270, "새 입주자" if daily else "새 PC")
    sw = booth(300, 280, "층 방송") if daily else switch(300, 280)
    rt = (warehouse(560, 280, "층 사이 문") if daily else router(560, 280))
    n2 = (house(200, 395, "이웃") if daily else pc(200, 395, "PC 2"))
    sv = (booth(400, 400, "안내 데스크") if daily else pc(400, 395, "DHCP 서버"))
    other = (box(690, 190, 230, 190, MUTED, PANEL, 14, dash=True, sw=3) + text(805, 218, "다른 층" if daily else "다른 네트워크", 17, MUTED, 700)
             + (house(805, 310, "이웃") if daily else pc(805, 310, "PC 3")))
    wires = line(150, 280, 250, 280, LINE, 3) + line(350, 280, 520, 280, LINE, 3) + line(600, 280, 690, 280, LINE, 3) + line(272, 296, 210, 350, LINE, 3) + line(328, 296, 390, 350, LINE, 3)
    send = lambda to, st, f0=0.1, f1=0.8: a.vis(a.move(pk(), to, st, f0, f1), st, st)
    body = [cli, sw, rt, n2, sv, other, wires,
            a.vis(pill(180, 200, "내 호수: 아직 없음" if daily else "출발지 IP 0.0.0.0", ORANGE, 17), 1, 2),
            a.vis(pill(200, 166, "받는 사람: 모두" if daily else "목적지 IP 255.255.255.255", BLUE, 16)
                  + pill(200, 134, "방송: 이 층 전체" if daily else "목적지 MAC FF:FF:FF:FF:FF:FF", BLUE, 16), 2, 2),
            send([(90, 270), (300, 280)], 2),
            a.vis(a.move(pk(), [(300, 290), (205, 362)], 3, 0.1, 0.8), 3, 3), a.vis(a.move(pk(), [(300, 290), (398, 362)], 3, 0.1, 0.8), 3, 3),
            a.vis(a.move(pk(), [(300, 280), (520, 280)], 3, 0.1, 0.8), 3, 3),
            a.vis(cross(535, 280) + text(640, 462, "다른 쪽으로 넘기지 않아요" if daily else "라우터는 다른 네트워크로 넘기지 않아요", 18, RED, 700), 4, 4)]
    if daily:
        t, sub = "처음 온 사람은 모두에게 물어본다", "안내 데스크 주소를 모르니 층 전체에 외쳐요"
        caps = ["아직 호수도, 안내 데스크 위치도 몰라요", "‘받는 사람: 모두’로 층 방송을 해요",
                "방송은 같은 층 사람들에게 모두 들려요", "층 사이 문은 방송을 넘기지 않아요"]
    else:
        t, sub = "Discover는 모두에게 방송한다", "서버 주소를 모를 때 같은 범위에 퍼뜨려요"
        caps = ["아직 IP 주소도 서버 주소도 몰라요", "목적지 IP와 MAC을 모두 브로드캐스트로 해요",
                "스위치는 같은 범위의 모든 포트로 전달해요", "라우터는 다른 네트워크로 넘기지 않아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: DORA ----------
def page5(daily):
    a = Anim(4, dur(daily))
    L, R = 170, 790
    ys = [225, 295, 365, 435]
    names = [("D", "문의", "방 있어요?"), ("O", "제안", "이 방 어때요?"), ("R", "선택", "그 방으로 할게요"), ("A", "확인", "배정 확인했어요")] if daily else \
            [("D", "Discover", "DHCP 서버 있나요?"), ("O", "Offer", "이 주소를 쓸 수 있어요"), ("R", "Request", "이 제안을 사용할게요"), ("A", "ACK", "임대를 시작하세요")]
    cols = [ORANGE, BLUE, ORANGE, BLUE]
    base = (pill(L, 150, "손님" if daily else "클라이언트", ORANGE, 19, True) + pill(R, 150, "프런트" if daily else "DHCP 서버", BLUE, 19, True)
            + line(L, 175, L, 462, LINE, 3, "6 6") + line(R, 175, R, 462, LINE, 3, "6 6"))
    body = [base]
    for k in range(4):
        L2R = k % 2 == 0
        y = ys[k]
        msg = (arrow(L + 8, R - 8, y, cols[k], 5) if L2R else arrow(R - 8, L + 8, y, cols[k], 5))
        ox = L + 40 if L2R else R - 40
        lab = (f'<circle cx="{ox}" cy="{y - 24}" r="15" fill="{cols[k]}"/>' + text(ox, y - 18, names[k][0], 18, BG, 700)
               + text(480, y - 10, f"{names[k][1]}", 20, cols[k], 700) + text(480, y + 24, names[k][2], 16, MUTED, 700))
        body.append(a.vis(msg + lab, k + 1, 4))
    body.append(a.vis(text(480, 156, "" if daily else "DHCP의 ACK는 TCP의 ACK와 다른 메시지예요", 17, MUTED, 700), 4, 4))
    if daily:
        t, sub = "호텔 방 배정은 네 번 오가요", "문의 → 제안 → 선택 → 확인"
        caps = ["손님이 빈방이 있는지 문의해요", "프런트가 방을 제안해요", "손님이 그 방을 선택해요", "프런트가 배정을 확인해요"]
    else:
        t, sub = "DORA 네 메시지로 주소를 확정한다", "Discover · Offer · Request · ACK, 메시지는 UDP로 오가요"
        caps = ["클라이언트가 DHCP 서버를 찾아요 (Discover)", "서버가 주소와 설정을 제안해요 (Offer)",
                "클라이언트가 그 제안을 선택해요 (Request)", "서버가 확인하면 임대가 시작돼요 (ACK)"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: relay ----------
def page6(daily):
    a = Anim(4, dur(daily))
    pk = packet if not daily else parcel
    cli = dev(daily, 180, 300, "새 직원" if daily else "새 PC")
    srv = (house(780, 300, "본사 안내센터") if daily else pc(780, 300, "DHCP 서버"))
    rt = (booth(480, 300, "접수원") if daily else router(480, 300, "라우터"))
    nets = (box(40, 150, 280, 270, MUTED, PANEL, 14, dash=True, sw=3) + text(180, 180, "우리 지점" if daily else "클라이언트 네트워크", 18, MUTED, 700)
            + box(640, 150, 280, 270, MUTED, PANEL, 14, dash=True, sw=3) + text(780, 180, "본사" if daily else "서버 네트워크", 18, MUTED, 700))
    wires = line(240, 300, 440, 300, LINE, 3) + line(520, 300, 720, 300, LINE, 3)
    rings = "".join(f'<circle cx="180" cy="300" r="{r}" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-opacity="{o}"/>' for r, o in ((50, .9), (85, .6), (120, .35)))
    body = [nets, wires, cli, srv, rt,
            a.vis(rings + text(180, 440, "같은 네트워크 안에서만 퍼져요" if not daily else "같은 지점 안에서만 들려요", 19, ORANGE, 700), 1, 2),
            a.vis(cross(330, 300) + text(480, 240, "넘어가지 않아요", 18, RED, 700), 2, 2),
            a.vis(pill(480, 240, "DHCP 릴레이" if not daily else "대신 전달하는 접수원", GREEN, 18, True) + hl(436, 262, 88, 84, GREEN, 12)
                  + arrow(530, 720, 300, GREEN, 6) + text(585, 288, "서버로 전달" if not daily else "본사로 전달", 16, GREEN, 700), 3, 3),
            a.vis(pill(480, 240, "DHCP 릴레이" if not daily else "대신 전달하는 접수원", GREEN, 18, True)
                  + arrow(720, 530, 300, BLUE, 6) + arrow(430, 250, 300, BLUE, 6) + text(585, 288, "응답 전달", 16, BLUE, 700), 4, 4),
            a.vis(a.move(pk(), [(180, 300), (440, 300)], 3, 0.1, 0.4), 3, 3)]
    if daily:
        t, sub = "지점 접수원이 본사에 전달한다", "다른 건물의 안내센터는 접수원이 이어 줘요"
        caps = ["새 직원이 지점 안에서 큰 소리로 불러요", "그 소리는 지점 밖으로 넘어가지 않아요",
                "접수원이 본사 안내센터로 전달해요", "본사의 답을 접수원이 가져와요"]
    else:
        t, sub = "릴레이가 다른 네트워크 서버에 잇는다", "브로드캐스트는 라우터를 넘지 않으니까요"
        caps = ["Discover는 같은 네트워크 안에만 퍼져요", "라우터는 브로드캐스트를 넘기지 않아요",
                "릴레이가 설정된 DHCP 서버로 전달해요", "서버의 응답을 릴레이가 가져와요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: reading the settings on my computer ----------
def page7(daily):
    a = Anim(4, dur(daily))
    tabs = ["내 집 안내서", "옛집 안내서", "손님용 안내서"] if daily else ["Wi-Fi 어댑터", "Ethernet 어댑터", "가상 어댑터"]
    lines = (["관리사무소 배정: 예", "내 호수: 302호", "우리 동네: 우리 단지", "정문(출구): 정문", "배정한 곳: 관리사무소", "계약 시작 / 만료: …", "안내 전화: 안내 데스크"] if daily else
             ["DHCP 사용: 예", "IPv4 주소: 192.168.0.100", "서브넷 마스크: 255.255.255.0", "기본 게이트웨이: 192.168.0.1", "DHCP 서버: 192.168.0.1", "임대 시작 / 만료: …", "DNS 서버: 192.168.0.1"])
    # group order for highlights: tab, (1,2,3), (4,5) , (6)
    ty = [165 + 66 * i for i in range(3)]
    tabsv = "".join(box(40, y, 220, 52, LINE, PANEL, 10, sw=2) + text(150, y + 33, tabs[i], 19, MUTED, 700) for i, y in enumerate(ty))
    panel = box(290, 150, 630, 270, LINE, BG, 10, sw=2) + text(305, 176, "입주 안내서 (예시)" if daily else "ipconfig /all (Windows 예시)", 16, MUTED, 700, "start")
    ly = lambda i: 212 + 30 * i
    ltxt = "".join(text(310, ly(i) + 8, s, 19, TXT, 700, "start") for i, s in enumerate(lines))
    row = lambda i, c: box(300, ly(i) - 18, 610, 30, c, "none", 6, sw=4)
    body = [tabsv, panel, ltxt,
            a.vis(box(40, ty[0], 220, 52, GREEN, PANEL, 10, sw=4) + text(150, ty[0] + 33, tabs[0], 19, GREEN, 700)
                  + pill(150, 142, "쓰는 것부터 찾아요" if daily else "연결된 어댑터부터 찾아요", GREEN, 16), 1, 4),
            a.vis(row(1, BLUE) + row(2, BLUE) + row(3, BLUE), 2, 2),
            a.vis(row(4, ORANGE) + row(5, ORANGE), 3, 3),
            a.vis(row(6, VIOLET), 4, 4),
            a.vis(pill(600, 446, "스스로 붙인 임시 번호는 관리사무소가 준 게 아니에요" if daily else "169.254.x.x는 DHCP가 준 주소가 아니에요", RED, 17), 4, 4)]
    if daily:
        t, sub = "안내서에서 받은 값을 찾아 읽기", "여러 안내서 중 지금 쓰는 것부터 골라요"
        caps = ["안내서가 여러 장이면 쓰는 것부터 골라요", "호수, 동네, 정문 항목을 찾아요",
                "배정해 준 곳과 계약 기간을 찾아요", "안내 전화 항목까지 확인해요"]
    else:
        t, sub = "내 컴퓨터에서 DHCP 설정 찾기", "운영체제마다 명령과 표기가 달라요"
        caps = ["여러 어댑터 중 연결된 것을 먼저 찾아요", "IPv4 주소, 마스크, 게이트웨이를 찾아요",
                "DHCP 서버와 임대 기간을 찾아요", "DNS 서버까지 확인해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: what DHCP solves and what it does not ----------
def page8(daily):
    a = Anim(4, dur(daily))
    labs = [("안내 카드", "받았어요"), ("복도(길)", "이어져 있나요"), ("정문", "열려 있나요"), ("안내 전화", "연결되나요"), ("가게", "도착")] if daily else \
           [("DHCP 설정", "받았어요"), ("Wi-Fi 회선", "연결돼 있나요"), ("기본 게이트웨이", "동작하나요"), ("DNS 서버", "도달하나요"), ("웹 사이트", "열려요")]
    xs = [110, 295, 480, 665, 850]

    def node(i, state):  # state: ok / bad / dim
        c = {"ok": GREEN, "bad": RED, "dim": LINE}[state]
        tc = {"ok": TXT, "bad": TXT, "dim": MUTED}[state]
        s = box(xs[i] - 78, 200, 156, 80, c, PANEL, 12, sw=3 if state != "dim" else 2) + text(xs[i], 232, labs[i][0], 18, tc, 700) + text(xs[i], 260, labs[i][1], 15, MUTED, 700)
        if state == "ok":
            s += check(xs[i], 190)
        if state == "bad":
            s += cross(xs[i], 190)
        return s

    links = "".join(line(xs[i] + 80, 240, xs[i + 1] - 80, 240, LINE, 3) for i in range(4))
    chain = lambda states: links + "".join(node(i, s) for i, s in enumerate(states))
    body = [a.vis(chain(["ok", "dim", "dim", "dim", "dim"]), 1, 1),
            a.vis(chain(["ok", "bad", "dim", "dim", "dim"]) + text(480, 340, "주소를 받았어도 웹이 안 열릴 수 있어요", 22, RED, 700), 2, 2),
            a.vis(chain(["ok", "ok", "bad", "bad", "dim"]) + text(480, 340, "게이트웨이나 이름 안내가 막혀도 안 열려요", 22, RED, 700), 3, 3),
            a.vis(chain(["dim", "dim", "dim", "dim", "dim"])
                  + cell(90, 330, 360, 80, "", BLUE) + text(270, 362, "안내 카드" if daily else "DHCP", 21, BLUE, 700) + text(270, 392, "호수·정문·안내 전화" if daily else "IP 주소·게이트웨이 설정", 16, TXT, 700)
                  + cell(510, 330, 360, 80, "", ORANGE) + text(690, 362, "문패 확인" if daily else "ARP", 21, ORANGE, 700) + text(690, 392, "같은 층에서 그 호수의 문 찾기" if daily else "같은 LAN에서 IP에 맞는 MAC 찾기", 16, TXT, 700)
                  + text(480, 378, "≠", 32, TXT, 700), 4, 4)]
    if daily:
        t, sub = "안내 카드가 있어도 길이 막히면 안 돼요", "받은 것과 실제로 되는 것은 달라요"
        caps = ["안내 카드를 받았어요", "복도가 끊기면 나갈 수 없어요",
                "정문이나 안내 전화가 막혀도 안 돼요", "카드와 문패 확인은 서로 다른 일이에요"]
    else:
        t, sub = "DHCP가 해결하는 일, 못 하는 일", "IP 주소를 받았다고 통신이 모두 성공한 건 아니에요"
        caps = ["DHCP로 주소와 설정을 받았어요", "Wi-Fi가 끊기면 웹 사이트가 안 열려요",
                "게이트웨이나 DNS가 막혀도 안 열려요", "IP 설정은 DHCP, MAC 찾기는 ARP가 맡아요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = {
    1: ("l22-daily-welcome-card", "l22-dhcp-fills-settings", page1),
    2: ("l22-daily-four-card-items", "l22-four-settings", page2),
    3: ("l22-daily-room-lease", "l22-address-pool-lease", page3),
    4: ("l22-daily-shout-in-floor", "l22-discover-broadcast", page4),
    5: ("l22-daily-hotel-booking", "l22-dora-messages", page5),
    6: ("l22-daily-branch-receptionist", "l22-dhcp-relay", page6),
    7: ("l22-daily-read-guide", "l22-find-dhcp-settings", page7),
    8: ("l22-daily-card-vs-road", "l22-dhcp-limits", page8),
}
AFTER = {1: 2, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1, 7: 3, 8: 1}

COPY = {
    "l22-daily-welcome-card": (
        "새 입주자에게 안내 카드를 채워 준다",
        "새 입주자의 호수, 우리 동네 범위, 정문 위치, 안내 전화 칸이 모두 ?로 비어 있습니다. 직접 알아보는 것은 이사할 때마다 번거롭다는 표시가 나오고, 관리사무소가 입주 안내 카드의 값을 보내 칸이 채워집니다. 마지막에 카드를 받아도 길이 열려 있어야 한다고 표시됩니다.",
        "관리사무소가 안내 카드를 채워 주듯, 설정은 자동으로 받지만 길이 열려 있어야 합니다."),
    "l22-dhcp-fills-settings": (
        "DHCP가 네트워크 설정을 채워 준다",
        "새 노트북의 IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS 서버 칸이 모두 ?로 비어 있습니다. 직접 입력하면 바꿀 때마다 번거롭다는 표시가 나오고, DHCP 서버가 설정 값을 보내 칸이 채워집니다. 마지막에 설정 전달이 자동일 뿐 회선도 동작해야 인터넷이 된다고 표시됩니다.",
        "‘자동’은 인터넷이 저절로 생긴다는 뜻이 아니라 필요한 설정을 받아 온다는 뜻입니다. 그림의 값은 예시예요.", 2),
    "l22-daily-four-card-items": (
        "안내 카드 네 가지는 서로 다른 일을 한다",
        "왼쪽에 호수, 동네 경계, 정문, 안내 전화가 목록으로 있고, 오른쪽에 항목마다 장면이 나타납니다. 호수는 우리 집을 구별하고, 동네 경계는 같은 동네를 가르고, 정문은 다른 동네로 나가는 첫 문이며, 안내 전화는 이름을 호수로 알려 줍니다. 마지막에 관리사무소는 카드를 줄 뿐 배달과 안내는 하지 않는다고 표시됩니다.",
        "카드의 네 항목은 각자 다른 일을 맡습니다."),
    "l22-four-settings": (
        "DHCP가 알려 주는 네 가지 설정",
        "왼쪽에 IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS 서버가 목록으로 있고, 오른쪽에 항목마다 장면이 나타납니다. IP 주소는 내 인터페이스를 구별하고, 마스크는 같은 네트워크를 가르고, 게이트웨이는 다른 네트워크로 가는 첫 라우터이며, DNS 서버는 이름을 IP 주소로 알려 줍니다. 마지막에 DHCP는 설정을 전달할 뿐 패킷 운반이나 이름 변환은 하지 않는다고 표시됩니다.",
        "DHCP는 설정을 전달하고, 운반은 라우팅이, 이름 변환은 DNS가 합니다. 그림의 값은 예시예요.", 1),
    "l22-daily-room-lease": (
        "객실을 빌려 주고 기간을 관리한다",
        "객실 100호부터 200호까지의 방 목록이 있고, 손님 A와 B가 방을 하나씩 숙박 기간만큼 빌립니다. 기간이 끝나기 전에 연장하면 같은 방을 계속 쓰고, 마지막에 직원이 따로 쓰는 방을 손님에게 빌려 주면 충돌한다고 표시됩니다.",
        "방을 빌리듯 주소도 기간을 두고 빌리며, 따로 쓰는 방은 빌려 주는 목록에서 뺍니다."),
    "l22-address-pool-lease": (
        "주소 풀에서 주소를 임대한다",
        "주소 풀 192.168.0.100부터 200까지의 칸이 한 줄로 있고, 노트북 A와 B가 주소를 하나씩 임대받으며 임대 기간 막대가 생깁니다. 갱신하면 같은 주소를 계속 쓰고, 마지막에 풀 안의 주소를 장치에 수동으로 설정하면 충돌한다고 표시됩니다.",
        "풀의 범위와 값은 구조를 보여 주는 예시이고, 실제 범위는 네트워크마다 다릅니다.", 2),
    "l22-daily-shout-in-floor": (
        "처음 온 사람은 모두에게 물어본다",
        "새 입주자는 호수도 안내 데스크 위치도 모릅니다. ‘받는 사람: 모두’로 층 방송을 하면 방송 장치를 거쳐 같은 층의 이웃과 안내 데스크에 모두 들리고, 층 사이 문은 방송을 다른 층으로 넘기지 않습니다.",
        "방송은 같은 층 안에서만 퍼집니다."),
    "l22-discover-broadcast": (
        "Discover는 모두에게 방송한다",
        "새 PC는 출발지 IP가 0.0.0.0이고, 목적지 IP 255.255.255.255와 목적지 MAC FF:FF:FF:FF:FF:FF로 Discover를 보냅니다. 스위치가 같은 범위의 PC 2와 DHCP 서버, 라우터 쪽으로 복사해 전달하고, 라우터는 다른 네트워크로 넘기지 않는다고 표시됩니다.",
        "IP 브로드캐스트와 MAC 브로드캐스트는 서로 다른 계층의 주소이며 함께 쓰일 수 있습니다. 라우터는 기본적으로 브로드캐스트를 넘기지 않아요.", 1),
    "l22-daily-hotel-booking": (
        "호텔 방 배정은 네 번 오가요",
        "손님과 프런트 사이에 문의, 제안, 선택, 확인이 차례로 화살표로 나타납니다. 손님이 빈방을 묻고, 프런트가 방을 제안하고, 손님이 그 방을 고르고, 프런트가 배정을 확인합니다.",
        "문의, 제안, 선택, 확인이 DORA와 같은 순서입니다."),
    "l22-dora-messages": (
        "DORA 네 메시지로 주소를 확정한다",
        "클라이언트와 DHCP 서버 사이에 Discover, Offer, Request, ACK가 차례로 화살표로 나타납니다. 클라이언트가 서버를 찾고, 서버가 주소를 제안하고, 클라이언트가 그 제안을 선택하고, 서버가 확인하면 임대가 시작됩니다. 마지막에 DHCP의 ACK는 TCP의 ACK와 다른 메시지라고 표시됩니다.",
        "Discover와 Offer만으로 주소가 확정되지 않고 Request와 ACK까지 거칩니다. DHCP ACK와 TCP ACK는 이름만 같아요.", 1),
    "l22-daily-branch-receptionist": (
        "지점 접수원이 본사에 전달한다",
        "왼쪽 우리 지점의 새 직원이 외치는 소리가 지점 안에서만 퍼지고 밖으로 넘어가지 않습니다. 접수원이 대신 본사 안내센터로 전달하고, 본사의 답도 접수원이 가져와 새 직원에게 돌려줍니다.",
        "접수원이 대신 전달해 주기 때문에 다른 건물의 안내센터를 쓸 수 있습니다."),
    "l22-dhcp-relay": (
        "릴레이가 다른 네트워크 서버에 잇는다",
        "왼쪽 클라이언트 네트워크의 새 PC가 Discover를 브로드캐스트하면 같은 네트워크 안에서만 퍼지고 라우터를 넘지 못합니다. 라우터에 설정된 DHCP 릴레이가 이를 받아 설정된 서버 네트워크의 DHCP 서버로 전달하고, 서버의 응답도 릴레이가 클라이언트 쪽으로 가져옵니다.",
        "클라이언트가 직접 먼 서버를 브로드캐스트하는 것이 아니라, 관리자가 설정한 릴레이가 연결합니다.", 1),
    "l22-daily-read-guide": (
        "안내서에서 받은 값을 찾아 읽기",
        "안내서 세 장 가운데 쓰는 것을 먼저 고릅니다. 호수, 동네, 정문 항목을 찾고, 배정해 준 곳과 계약 기간을 찾고, 안내 전화 항목까지 차례로 확인합니다. 마지막에 스스로 붙인 임시 번호는 관리사무소가 준 것이 아니라고 표시됩니다.",
        "여러 장의 안내서가 있을 때는 지금 쓰는 것부터 찾습니다."),
    "l22-find-dhcp-settings": (
        "내 컴퓨터에서 DHCP 설정 찾기",
        "왼쪽에 Wi-Fi, Ethernet, 가상 어댑터가 있고 오른쪽에 ipconfig /all 출력 예시가 있습니다. 연결된 어댑터를 먼저 고르고, IPv4 주소와 서브넷 마스크와 기본 게이트웨이, 다음으로 DHCP 서버와 임대 시작·만료, 마지막으로 DNS 서버를 차례로 찾습니다. 마지막에 169.254.x.x는 DHCP가 준 주소가 아니라고 표시됩니다.",
        "Windows 출력의 예시이고 운영체제마다 명령과 표기가 다릅니다. 그림의 주소 값은 예시예요.", 3),
    "l22-daily-card-vs-road": (
        "안내 카드가 있어도 길이 막히면 안 돼요",
        "안내 카드를 받은 뒤 복도, 정문, 안내 전화, 가게로 이어지는 길이 나타납니다. 복도가 끊기거나 정문이나 안내 전화가 막히면 가게에 갈 수 없다고 표시되고, 마지막에 안내 카드와 문패 확인은 서로 다른 일이라는 두 카드가 나타납니다.",
        "카드를 받은 것과 실제로 갈 수 있는 것은 다릅니다."),
    "l22-dhcp-limits": (
        "DHCP가 해결하는 일, 못 하는 일",
        "DHCP 설정을 받은 뒤 Wi-Fi 회선, 기본 게이트웨이, DNS 서버, 웹 사이트로 이어지는 길이 나타납니다. Wi-Fi가 끊기거나 게이트웨이나 DNS가 막히면 웹 사이트가 열리지 않는다고 표시되고, 마지막에 IP 설정은 DHCP가, 같은 LAN에서 MAC을 찾는 일은 ARP가 맡는다는 두 카드가 나타납니다.",
        "IP 주소를 받았다는 것과 인터넷 통신이 모두 성공했다는 것은 다릅니다. ARP는 다음 Lesson에서 이어집니다.", 1),
}


def build_pages():
    pages = []
    for n in range(1, 9):
        dn, nn, fn = PAGES[n]
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        d, nw = COPY[dn], COPY[nn]
        pages.append([(dn, *d, -1), (nn, nw[0], nw[1], nw[2], nw[3])])
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
