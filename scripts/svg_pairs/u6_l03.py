#!/usr/bin/env python3
"""Unit 6 Lesson 3 (ARP) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u6_l03.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/13-*"))
OUT = LESSON / "assets" / "animations"
MAC = "AA:BB:CC:00:11:22"  # example only


def dur(daily, n=4):
    return round(n * (3.75 if daily else 4))


def cell(x, y, w, h, label, c, fs=16, fill=PANEL):
    return box(x, y, w, h, c, fill, 6, sw=3) + text(x + w / 2, y + h / 2 + fs * 0.36, label, fs, c, 700)


def hl(x, y, w, h, c=ORANGE, rx=10):
    return box(x - 4, y - 4, w + 8, h + 8, c, "none", rx, sw=5)


def arrow(x0, x1, y, c, w=6):
    d = 1 if x1 > x0 else -1
    return (line(x0, y, x1 - d * 16, y, c, w) + f'<polygon points="{x1},{y} {x1 - d * 24},{y - w - 6} {x1 - d * 24},{y + w + 6}" fill="{c}"/>')


def brace(x0, x1, y, c, label, up=True, fs=17):
    d = 12 if up else -12
    return (line(x0, y, x1, y, c, 4) + line(x0, y, x0, y + d, c, 4) + line(x1, y, x1, y + d, c, 4)
            + pill((x0 + x1) / 2, y - 26 if up else y + 26, label, c, fs, True))


def person(x, y, label=None):
    s = f'<circle cx="{x}" cy="{y - 20}" r="16" fill="{BLUE}"/><rect x="{x - 18}" y="{y}" width="36" height="46" rx="12" fill="{BLUE}"/>'
    return s + (text(x, y + 72, label, 18, TXT, 700) if label else "")


def me(daily, x, y, label=None):
    return person(x, y - 8, label) if daily else laptop(x, y, label)


def dst_icon(daily, x, y, label):
    return house(x, y - 20, label) if daily else pc(x, y, label)


MID = lambda daily, x, y, label: booth(x, y, label) if daily else router(x, y, label)


# ---------- Page 1: IP finds the network, MAC names this link's receiver ----------
def page1(daily):
    a = Anim(4, dur(daily))
    src, mid, dst = (me(daily, 100, 320, "나" if daily else "노트북"), MID(daily, 480, 320, "접수창구" if daily else "공유기"),
                     dst_icon(daily, 860, 320, "먼 도시 친구" if daily else "서버"))
    body = [src, mid, dst, line(160, 335, 440, 335, LINE, 3), line(520, 335, 800, 335, LINE, 3),
            a.vis(brace(100, 860, 200, BLUE, "최종 주소: 어느 동네의 누구인가" if daily else "IP: 목적지가 있는 네트워크"), 1, 1),
            a.vis(brace(100, 480, 200, VIOLET, "이번 구간 인수자" if daily else "MAC: 이번 링크에서 프레임을 받을 인터페이스"), 2, 2),
            a.vis(brace(100, 860, 170, BLUE, "최종 주소" if daily else "IP (최종)") + brace(100, 480, 240, VIOLET, "이번 구간 인수자" if daily else "MAC (이번 링크)"), 3, 4),
            a.vis(pill(290, 392, "인수자 이름: ?" if daily else "받을 MAC: ?", ORANGE, 19, True) + ask(150, 392)
                  + text(480, 440, "주소는 아는데, 이번 구간 인수자는 몰라요" if daily else "IP는 아는데, 이번 링크의 MAC은 몰라요", 20, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "최종 주소와 이번 구간 인수자", "택배에는 두 가지 정보가 모두 필요해요"
        caps = ["최종 주소는 어느 동네의 누구인지 알려 줘요", "이번 구간 인수자는 지금 구간에서 받을 사람이에요",
                "상자에는 두 가지가 함께 필요해요", "그런데 인수자의 이름을 모를 수 있어요"]
    else:
        t, sub = "IP는 네트워크, MAC은 이번 링크", "ARP는 IP로 MAC을 찾는 일을 해요"
        caps = ["IP 주소는 목적지가 있는 네트워크를 찾아요", "MAC 주소는 이번 링크의 받을 인터페이스예요",
                "프레임을 보내려면 둘 다 필요해요", "IP는 아는데 MAC을 모를 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: IP can change with the network, MAC stays with the NIC ----------
def page2(daily):
    a = Anim(4, dur(daily))
    ip1, ip2 = ("서울 3동 12호", "부산 5동 7호") if daily else ("192.168.0.100", "10.0.0.7")
    nm = "김철수" if daily else MAC
    zone = lambda x, lab: box(x, 140, 290, 235, MUTED, PANEL, 14, dash=True, sw=3) + text(x + 145, 178, lab, 18, MUTED, 700)
    tags = lambda x, ipv, c: (pill(x, 205, ("주소 " if daily else "IP ") + ipv, BLUE, 17, True) + pill(x, 245, ("이름 " if daily else "MAC ") + nm, VIOLET, 15, True))
    frame_sk = (cell(110, 394, 200, 40, "받는 MAC: ?" if not daily else "인수자: ?", ORANGE, 17) + cell(320, 394, 200, 40, "출발 MAC", VIOLET, 17)
                + cell(530, 394, 220, 40, "IP 패킷", BLUE, 17))
    body = [zone(40, "옛 동네" if daily else "집 Wi-Fi 네트워크"), zone(630, "새 동네" if daily else "카페 Wi-Fi 네트워크"),
            a.vis(me(daily, 185, 300, "나" if daily else "내 노트북") + tags(185, ip1, BLUE), 1, 1),
            a.vis(f'<g opacity=".35">{me(daily, 185, 300)}</g>' + me(daily, 775, 300, "나" if daily else "내 노트북") + tags(775, ip2, BLUE)
                  + arrow(335, 585, 300, ORANGE, 6) + text(460, 270, "이사 · 이동" if daily else "네트워크 이동", 18, ORANGE, 700)
                  + text(480, 440, "주소는 바뀌었지만 이름은 그대로" if daily else "IP는 바뀌어도 MAC은 같은 NIC 것", 20, TXT, 700), 2, 2),
            a.vis(me(daily, 775, 300, None) + tags(775, ip2, BLUE) + frame_sk + text(430, 388, "프레임을 보내려면", 18, MUTED, 700), 3, 4),
            a.vis(pill(480, 458, "받을 MAC은 ARP로 찾아요" if not daily else "인수자는 따로 물어서 알아내요", GREEN, 17, True), 4, 4)]
    if daily:
        t, sub = "이사해도 이름은 그대로예요", "주소는 바뀌고, 이름은 사람에 붙어요"
        caps = ["옛 동네에서는 주소와 이름이 있어요", "이사하면 주소는 바뀌지만 이름은 같아요",
                "택배에는 이번 구간 인수자도 필요해요", "인수자는 따로 물어서 알아내요"]
    else:
        t, sub = "IP는 바뀌고 MAC은 NIC에 붙어요", "MAC은 예시 값이에요"
        caps = ["집 Wi-Fi에서 IP와 MAC이 있어요", "카페로 옮기면 IP는 바뀌지만 MAC은 같아요",
                "프레임에는 받을 MAC도 있어야 해요", "그 MAC을 ARP가 찾아 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: ARP asks the LAN "who has this IP?" ----------
def page3(daily):
    a = Anim(4, dur(daily))
    names = [("21번 책상", "21"), ("30번 책상", "30"), ("5번 책상", "5")] if daily else [("PC", ".21"), ("프린터", ".30"), ("서버", ".5")]
    xs = [440, 640, 840]
    dv = lambda i: (house(xs[i], 300, names[i][0]) if daily else (pc if i != 1 else printer)(xs[i], 310, names[i][0]))
    ipt = lambda i: pill(xs[i], 215, (names[i][1] + "번") if daily else "192.168.0" + names[i][1], MUTED, 15)
    body = [me(daily, 110, 320, "나" if daily else "노트북"), "".join(dv(i) + ipt(i) for i in range(3)), line(160, 330, 400, 330, LINE, 3),
            a.vis(pill(640, 215, "30번 책상" if daily else "192.168.0.30", ORANGE, 17, True) + pill(150, 245, "담당자: ?" if daily else "MAC: ?", ORANGE, 17), 1, 1),
            a.vis(pill(480, 160, "30번 책상 담당자 누구세요?" if daily else "192.168.0.30을 쓰는 장치는 누구인가요?", BLUE, 18, True)
                  + arrow(170, 400, 360, BLUE, 5) + arrow(170, 880, 395, BLUE, 3), 2, 2),
            a.vis(pill(640, 150, "저예요!" if daily else f"저예요, MAC은 {MAC}", GREEN, 17, True) + arrow(600, 170, 395, GREEN, 5) + hl(xs[1] - 70, 215, 140, 150, GREEN, 12), 3, 3),
            a.vis(cell(110, 405, 240, 44, "받는 MAC: 프린터" if not daily else "인수자: 30번 담당", GREEN, 18) + arrow(360, 570, 427, GREEN, 6)
                  + text(480, 462, "이제 프레임을 보낼 수 있어요" if not daily else "이제 상자를 건넬 수 있어요", 18, TXT, 700), 4, 4)]
    if daily:
        t, sub = "책상 번호는 아는데 이름을 몰라요", "같은 사무실에 물어보면 알 수 있어요"
        caps = ["30번 책상에 보낼 건데 담당자를 몰라요", "사무실에 ‘30번 책상 담당자 누구세요?’ 하고 물어요",
                "30번 책상 담당자가 대답해요", "이제 담당자에게 상자를 건네요"]
    else:
        t, sub = "IP는 아는데 MAC을 몰라요", "같은 LAN에 ‘이 IP 주인이 누구냐’고 물어요"
        caps = ["프린터의 IP는 아는데 MAC은 몰라요", "같은 LAN에 그 IP의 주인을 물어요",
                "주인인 프린터가 MAC을 알려 줘요", "이제 프린터 MAC으로 프레임을 보낼 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: DHCP gives the gateway's IP, not its MAC ----------
def page4(daily):
    a = Anim(4, dur(daily))
    vals = [("내 호수", "302호"), ("정문 위치", "1동 앞"), ("정문 경비 이름", "?")] if daily else [("내 IP", "192.168.0.100"), ("게이트웨이 IP", "192.168.0.1"), ("게이트웨이 MAC", "?")]
    card = (box(60, 140, 380, 170, BLUE, PANEL, 12, sw=3) + text(250, 168, "입주 안내 카드" if daily else "DHCP로 받은 설정", 18, BLUE, 700)
            + "".join(text(80, 205 + 36 * i, k, 17, MUTED, 700, "start") + text(420, 205 + 36 * i, v, 18, ORANGE if v == "?" else GREEN, 700, "end") for i, (k, v) in enumerate(vals)))
    nodes = [me(daily, 110, 420, "나" if daily else "내 PC"), MID(daily, 480, 420, "정문" if daily else "게이트웨이"), (house(850, 400, "바깥 동네") if daily else pc(850, 420, "인터넷"))]
    pathv = line(170, 435, 440, 435, LINE, 3) + line(520, 435, 790, 435, LINE, 3)
    body = [card, pathv] + nodes + [
        a.vis(hl(75, 222, 350, 28, GREEN, 8), 1, 2),
        a.vis(arrow(180, 430, 380, ORANGE, 6) + text(305, 360, "밖으로 나가려면 먼저 정문으로" if daily else "밖으로 나가려면 먼저 게이트웨이로", 17, ORANGE, 700), 2, 2),
        a.vis(hl(75, 258, 350, 28, ORANGE, 8) + ask(480, 370) + text(620, 372, "카드에는 이름이 없어요" if daily else "DHCP는 IP까지만 알려 줘요", 18, ORANGE, 700), 3, 3),
        a.vis(pill(600, 372, "따로 알아내야 해요" if daily else "별도로 알아내야 해요 → ARP", GREEN, 18, True) + hl(75, 258, 350, 28, ORANGE, 8), 4, 4)]
    if daily:
        t, sub = "정문 위치는 알아도 경비는 몰라요", "카드에는 위치만 있고 이름은 없어요"
        caps = ["안내 카드에 정문 위치가 적혀 있어요", "밖으로 나가려면 먼저 정문으로 가요",
                "하지만 정문 경비의 이름은 카드에 없어요", "이름은 따로 물어서 알아내야 해요"]
    else:
        t, sub = "게이트웨이 MAC은 따로 알아내요", "예: PC 192.168.0.100, 게이트웨이 192.168.0.1"
        caps = ["DHCP가 게이트웨이의 IP를 알려 줬어요", "인터넷으로 나가려면 먼저 게이트웨이로 보내요",
                "그 IP에 대응하는 MAC은 모르는 상태예요", "MAC은 ARP로 따로 알아내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: for an outside site the MAC needed is the gateway's ----------
def page5(daily):
    a = Anim(4, dur(daily))
    nodes = [me(daily, 90, 330, "나" if daily else "내 PC"), MID(daily, 340, 330, "접수창구" if daily else "게이트웨이"),
             f'<ellipse cx="600" cy="330" rx="90" ry="45" fill="{PANEL}" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 6"/>' + text(600, 337, "여러 구간", 18, MUTED, 700),
             dst_icon(daily, 860, 330, "먼 도시 친구" if daily else "네이버 3.3.3.3(예시)")]
    wires = line(150, 345, 300, 345, LINE, 3) + line(380, 345, 510, 345, LINE, 3) + line(690, 345, 810, 345, LINE, 3)
    body = [wires] + nodes + [
        a.vis(pill(860, 235, "목적지: 친구" if daily else "목적지 IP 3.3.3.3", BLUE, 18, True), 1, 4),
        a.vis(arrow(150, 300, 290, ORANGE, 6) + text(225, 262, "먼저 여기로" if daily else "먼저 게이트웨이로", 18, ORANGE, 700), 2, 4),
        a.vis(brace(90, 340, 410, VIOLET, "필요한 인수자는 접수창구 담당" if daily else "필요한 MAC은 게이트웨이의 것", up=False) + cross(860, 418)
              + text(860, 452, "친구의 이름이 아니에요" if daily else "서버의 MAC이 아니에요", 17, RED, 700), 3, 4),
        a.vis(arrow(390, 540, 290, MUTED, 4) + text(465, 262, "그다음은 라우팅" if not daily else "그다음은 접수창구가 이어서", 17, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "먼 친구에게는 접수창구에 맡겨요", "우리 구간의 인수자는 접수창구 담당이에요"
        caps = ["먼 도시 친구에게 상자를 보내요", "먼저 우리 동네 접수창구에 맡겨요",
                "필요한 이름은 접수창구 담당의 것이에요", "그다음은 접수창구가 이어서 보내요"]
    else:
        t, sub = "외부 사이트는 게이트웨이 MAC이 필요", "목적지 IP는 3.3.3.3 (설명용 예시)"
        caps = ["목적지 IP는 인터넷 너머 서버예요", "PC는 먼저 게이트웨이로 프레임을 보내요",
                "필요한 MAC은 서버가 아니라 게이트웨이의 것", "그다음 경로는 게이트웨이가 정해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: ARP Request is broadcast on the LAN ----------
def page6(daily):
    a = Anim(4, dur(daily))
    pk = packet if not daily else parcel
    sw = booth(330, 280, "층 방송") if daily else switch(330, 280)
    cli = me(daily, 100, 290, "나" if daily else "내 PC")
    gw = MID(daily, 640, 290, "1번 책상" if daily else "게이트웨이")
    n2 = house(200, 395, "2번 책상") if daily else pc(200, 395, "PC 2")
    n3 = house(430, 395, "3번 책상") if daily else printer(430, 395, "프린터")
    wires = (line(160, 295, 280, 295, LINE, 3) + line(380, 295, 590, 295, LINE, 3) + line(300, 312, 220, 350, LINE, 3) + line(360, 312, 430, 350, LINE, 3))
    body = [wires, cli, sw, gw, n2, n3,
            a.vis(pill(240, 170, "ARP 요청: 1번 책상 담당자?" if daily else "ARP 요청: 192.168.0.1은 누구?", BLUE, 17, True)
                  + pill(240, 138, "받는 사람: 모두" if daily else "목적지 MAC FF:FF:FF:FF:FF:FF", BLUE, 15), 1, 2),
            a.vis(a.move(pk(), [(100, 290), (330, 280)], 1, 0.1, 0.8), 1, 1),
            a.vis(a.move(pk(), [(330, 285), (210, 365)], 2, 0.1, 0.8) + a.move(pk(), [(330, 285), (430, 365)], 2, 0.1, 0.8) + a.move(pk(), [(330, 280), (600, 280)], 2, 0.1, 0.8), 2, 2),
            a.vis(cross(200, 335) + cross(430, 335) + text(480, 215, "내 번호가 아니라서 대답하지 않아요" if daily else "내 IP가 아니라서 응답하지 않아요", 19, MUTED, 700), 3, 3),
            a.vis(hl(585, 225, 110, 120, GREEN, 12) + eye(640, 190) + text(640, 168, "나를 찾는 요청이다!" if daily else "나를 찾는 요청이다!", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "책상 번호를 방 전체에 묻는다", "‘1번 책상 담당자 누구세요?’ 하고 방송해요"
        caps = ["‘1번 책상 담당자 누구세요?’ 하고 방송해요", "방송은 같은 층의 모두에게 들려요",
                "다른 책상 담당자는 자기 번호가 아니라 가만히 있어요", "1번 책상 담당자는 나를 찾는 걸 알아채요"]
    else:
        t, sub = "ARP Request는 모두에게 묻는다", "목적지 MAC은 브로드캐스트예요"
        caps = ["PC가 ‘192.168.0.1 누구?’ 하고 물어요", "스위치가 같은 범위의 모두에게 전달해요",
                "주인이 아닌 호스트들은 응답하지 않아요", "게이트웨이는 자신을 찾는 요청임을 알아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: ARP Reply carries the MAC back ----------
def page7(daily):
    a = Anim(4, dur(daily))
    cli = me(daily, 110, 300, "나" if daily else "내 PC")
    gw = MID(daily, 850, 300, "1번 책상 담당" if daily else "게이트웨이")
    mac = "김철수" if daily else MAC
    ans = (box(300, 130, 360, 74, GREEN, PANEL, 12, sw=3) + text(480, 160, "1번 책상 = " if daily else "192.168.0.1 =", 19, TXT, 700)
           + text(480, 190, mac, 20, GREEN, 700))
    fr = (cell(150, 400, 240, 50, "받는 MAC: " + ("김철수" if daily else "게이트웨이"), GREEN, 17) + cell(400, 400, 200, 50, "출발 MAC", VIOLET, 17)
          + cell(610, 400, 200, 50, "IP 패킷", BLUE, 17))
    body = [cli, gw, line(170, 315, 790, 315, LINE, 3),
            a.vis(hl(795, 245, 110, 120, GREEN, 12) + pill(850, 190, "내가 1번이에요" if daily else "내 IP를 찾는 요청", GREEN, 16), 1, 1),
            a.vis(arrow(800, 190, 300, GREEN, 6) + pill(480, 255, "ARP 응답: 내 IP와 MAC" if not daily else "손들고 대답: 내 번호와 이름", GREEN, 18, True)
                  + text(480, 350, "나에게만 보내요 (유니캐스트)" if not daily else "나에게만 대답해요", 17, MUTED, 700), 2, 2),
            a.vis(ans + pill(480, 290, "받았어요", GREEN, 16, True), 3, 4),
            a.vis(fr + text(480, 380, "이제 받는 MAC을 정할 수 있어요" if not daily else "이제 인수자를 정할 수 있어요", 20, TXT, 700), 4, 4)]
    if daily:
        t, sub = "담당자만 손들고 대답한다", "대답은 나에게만 보내요"
        caps = ["1번 책상 담당자가 자기 번호임을 알아채요", "손을 들고 번호와 이름을 알려 줘요",
                "나는 ‘1번 책상 = 김철수’를 알게 돼요", "이제 상자의 인수자를 정할 수 있어요"]
    else:
        t, sub = "ARP Reply로 MAC을 알려 준다", f"MAC은 48비트 주소 (예시 {MAC})"
        caps = ["게이트웨이가 자신을 찾는 요청을 봐요", "ARP Reply로 자신의 IP와 MAC을 알려 줘요",
                "PC는 192.168.0.1의 MAC을 알게 돼요", "이제 프레임의 받는 MAC을 정할 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: two destinations: IP (final) and MAC (this LAN) ----------
def page8(daily):
    a = Anim(4, dur(daily))
    c1 = [("보내는 곳 서울" if daily else "출발 IP 192.168.0.100", 150, BLUE), ("받는 곳 부산" if daily else "목적 IP 3.3.3.3", 130, BLUE), ("물건" if daily else "데이터", 100, GREEN)]
    pk, y1 = [], 190
    x = 290
    for lab, w, c in c1:
        pk.append(cell(x, y1, w, 56, lab, c, 15))
        x += w
    pkt = "".join(pk)  # x 290..670
    fh = cell(100, 290, 190, 56, "받는 MAC: 접수창구" if daily else "받는 MAC: 게이트웨이", VIOLET, 15) + cell(680 - 0, 290, 90, 56, "봉인" if daily else "FCS", VIOLET, 15)
    fh = (cell(100, 290, 95, 56, "받는 MAC" if not daily else "받는 인수자", VIOLET, 15) + cell(195, 290, 95, 56, "출발 MAC" if not daily else "보낸 쪽", VIOLET, 15)
          + box(290, 290, 380, 56, BLUE, PANEL, 6, sw=3) + text(480, 324, "IP 패킷" if not daily else "송장 붙은 상자", 17, BLUE, 700) + cell(670, 290, 90, 56, "FCS" if not daily else "봉인", VIOLET, 15))
    qa = (text(480, 280 + 100, "", 1, TXT) + box(100, 380, 330, 66, BLUE, PANEL, 10, sw=2) + text(265, 408, "IP 목적지", 17, BLUE, 700) + text(265, 434, "최종적으로 누구에게?" if not daily else "최종 도착지는 어디?", 16, TXT, 700)
          + box(530, 380, 330, 66, VIOLET, PANEL, 10, sw=2) + text(695, 408, "MAC 목적지", 17, VIOLET, 700) + text(695, 434, "이번 LAN에서 누구에게 맡길까?" if not daily else "이번 구간에서 누구에게 맡길까?", 16, TXT, 700))
    body = [a.vis(pkt + pill(480, 160, "IP 패킷" if not daily else "송장 붙은 상자", BLUE, 17, True), 1, 4),
            a.vis(fh, 2, 4), a.vis(qa, 3, 3),
            a.vis(arrow(300, 640, 408, ORANGE, 6) + text(470, 450, "먼저 게이트웨이로, 그다음 IP 목적지를 보고 라우팅" if not daily else "먼저 접수창구로, 그다음 도착지를 보고 이어서 보내요", 19, TXT, 700), 4, 4)]
    if daily:
        t, sub = "상자 주소와 트럭 인수자는 달라요", "상자는 끝까지, 인수자는 구간마다 바뀌어요"
        caps = ["상자에는 보내는 곳과 받는 곳이 있어요", "이번 구간 인수자와 봉인이 겉에 붙어요",
                "최종 도착지와 이번 구간 인수자는 다른 질문이에요", "먼저 접수창구에 맡기면 이어서 보내 줘요"]
    else:
        t, sub = "IP 패킷을 프레임에 담는다", "IP는 최종 목적지, MAC은 이번 LAN의 수신자"
        caps = ["IP 패킷에는 출발 IP와 목적 IP가 있어요", "프레임에는 받는 MAC과 출발 MAC이 붙어요",
                "두 목적지는 서로 다른 질문에 답해요", "프레임은 먼저 게이트웨이로 가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: the ARP cache remembers pairs ----------
def page9(daily):
    a = Anim(4, dur(daily))
    pk = packet if not daily else parcel
    cli = me(daily, 110, 400, "나" if daily else "내 PC")
    gw = MID(daily, 850, 400, "1번 책상" if daily else "게이트웨이")
    memo = lambda row, c=GREEN: box(80, 190 + 50 * row, 360, 44, c, BG, 8, sw=2)
    hdr = box(60, 140, 400, 160, MUTED, PANEL, 12, sw=3) + text(260, 168, "메모장" if daily else "ARP 캐시", 18, MUTED, 700) + text(100, 198, "번호" if daily else "IP 주소", 15, MUTED, 700, "start") + text(250, 198, "이름" if daily else "MAC", 15, MUTED, 700, "start")
    row0 = (box(75, 208, 370, 40, GREEN, BG, 8, sw=2) + text(100, 235, "1번" if daily else "192.168.0.1", 17, TXT, 700, "start") + text(250, 235, "김철수" if daily else "AA:BB:CC:00:11:22", 16 if not daily else 18, GREEN, 700, "start"))
    qa = (arrow(170, 790, 345, BLUE, 4) + text(480, 332, "누구세요?", 16, BLUE, 700) + arrow(790, 170, 385, GREEN, 4) + text(480, 412, "저예요!" if daily else "대응 관계 응답", 16, GREEN, 700))
    body = [hdr, cli, gw,
            a.vis(qa, 1, 1),
            a.vis(row0 + pill(260, 270, "한 줄 적어 둬요" if daily else "대응 관계를 저장해요", GREEN, 16, True), 2, 4),
            a.vis(a.move(pk(), [(170, 400), (790, 400)], 3, 0.1, 0.8) + check(480, 340) + text(480, 440, "다시 묻지 않아도 돼요", 20, GREEN, 700), 3, 3),
            a.vis(box(75, 208, 370, 40, ORANGE, "none", 8, dash=True, sw=3) + text(480, 440, "잠시 저장해요, 오래되면 사라질 수 있어요" if not daily else "잠깐 적어 둔 메모라서, 오래되면 지워질 수 있어요", 18, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "알아낸 이름을 메모해 둔다", "다음에는 다시 묻지 않고 메모를 봐요"
        caps = ["처음에는 번호를 방송해서 물어봐요", "알아낸 번호와 이름을 메모장에 적어요",
                "다음에는 메모를 보고 바로 건네요", "메모는 오래되면 지워질 수 있어요"]
    else:
        t, sub = "ARP 캐시에 대응 관계를 남긴다", "IP와 MAC의 한 쌍을 잠시 저장해요"
        caps = ["처음에는 ARP로 물어서 알아내요", "알아낸 IP와 MAC 쌍을 ARP 캐시에 저장해요",
                "다음 통신에서는 다시 묻지 않아도 돼요", "캐시는 잠시 저장이라 항목이 없을 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 10: reading the cache with arp -a / ip neigh ----------
def page10(daily):
    a = Anim(4, dur(daily))
    tabs = ["메모장 열기", "다른 메모장 열기"] if daily else ["arp -a (Windows · macOS)", "ip neigh (Linux)"]
    lines = [("1번", "김철수"), ("30번", "박영희"), ("5번", "이민수")] if daily else [("192.168.0.1", "aa:bb:cc:00:11:22"), ("192.168.0.30", "aa:bb:cc:44:55:66"), ("192.168.0.5", "aa:bb:cc:77:88:99")]
    tb = "".join(box(40, 165 + 66 * i, 250, 52, LINE, PANEL, 10, sw=2) + text(165, 198 + 66 * i, tabs[i], 16 if not daily else 19, MUTED, 700) for i in range(2))
    panel = box(320, 150, 600, 250, LINE, BG, 10, sw=2) + text(340, 178, "출력 예시" if not daily else "메모장 (예시)", 16, MUTED, 700, "start") + text(360, 212, "IP 주소" if not daily else "번호", 16, MUTED, 700, "start") + text(640, 212, "MAC 주소" if not daily else "이름", 16, MUTED, 700, "start")
    ly = lambda i: 250 + 44 * i
    rows = "".join(text(360, ly(i), lines[i][0], 20, TXT, 700, "start") + text(640, ly(i), lines[i][1], 20, TXT, 700, "start") for i in range(3))
    body = [tb, panel,
            a.vis(rows + box(40, 165, 250, 52, GREEN, PANEL, 10, sw=4) + text(165, 198, tabs[0], 16 if not daily else 19, GREEN, 700), 1, 3),
            a.vis(box(350, 190, 560, 34, BLUE, "none", 6, sw=4) + pill(480, 430, "IP와 MAC이 한 쌍으로 보여요" if not daily else "번호와 이름이 한 쌍으로 보여요", BLUE, 17), 2, 2),
            a.vis(box(350, ly(0) - 24, 560, 38, GREEN, "none", 6, sw=4) + pill(480, 430, "게이트웨이 주소가 있는지 봐요" if not daily else "정문 번호가 있는지 봐요", GREEN, 17), 3, 3),
            a.vis(text(620, 280, "(아직 항목이 없어요)" if not daily else "(아직 적힌 게 없어요)", 20, MUTED, 700) + pill(620, 330, "게이트웨이에 통신을 한 번 시도해요" if not daily else "1번 책상에 말을 한 번 걸어요", ORANGE, 17, True)
                  + text(620, 376, "→ 다시 확인하면 새 기록이 생겨요" if not daily else "→ 다시 보면 새 메모가 생겨요", 18, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "메모장에서 이름 쌍을 찾아본다", "비어 있으면 한 번 말을 걸고 다시 봐요"
        caps = ["메모장을 열어요", "번호와 이름이 한 쌍씩 적혀 있어요",
                "정문 번호가 있는지 살펴봐요", "없으면 말을 걸어 보고 다시 확인해요"]
    else:
        t, sub = "arp -a로 ARP 캐시 확인하기", "표시되는 모양은 운영체제마다 달라요 (예시)"
        caps = ["운영체제에 맞는 명령을 실행해요", "IP와 MAC이 한 쌍으로 표시돼요",
                "게이트웨이 주소가 있는지 찾아봐요", "항목이 없으면 통신을 시도한 뒤 다시 봐요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    ("l23-daily-final-vs-leg", "l23-ip-network-mac-link", page1),
    ("l23-daily-move-keep-name", "l23-ip-changes-mac-stays", page2),
    ("l23-daily-ask-desk-owner", "l23-know-ip-not-mac", page3),
    ("l23-daily-gate-guard-name", "l23-gateway-mac-needed", page4),
    ("l23-daily-far-friend-desk", "l23-outside-site-gateway", page5),
    ("l23-daily-call-out-desk", "l23-arp-request-broadcast", page6),
    ("l23-daily-owner-raises-hand", "l23-arp-reply", page7),
    ("l23-daily-box-and-truck", "l23-packet-in-frame-pair", page8),
    ("l23-daily-memo-pad", "l23-arp-cache", page9),
    ("l23-daily-read-memo", "l23-arp-a-command", page10),
]

COPY = {
    "l23-daily-final-vs-leg": ("최종 주소와 이번 구간 인수자",
        "나, 접수창구, 먼 도시의 친구가 한 줄로 있습니다. 최종 주소는 전체 길에, 이번 구간 인수자는 첫 구간에 대응하며 상자에 둘이 함께 필요하다고 표시됩니다. 마지막에 인수자의 이름을 모를 수 있다는 물음표가 나타납니다.",
        "택배에는 최종 주소와 이번 구간 인수자가 모두 필요합니다."),
    "l23-ip-network-mac-link": ("IP는 네트워크, MAC은 이번 링크",
        "노트북, 공유기, 서버가 한 줄로 있습니다. IP는 전체 길의 목적지 네트워크를, MAC은 첫 링크에서 프레임을 받을 인터페이스를 가리키며 둘 다 필요합니다. 마지막에 IP는 아는데 받을 MAC은 모르는 상태가 물음표로 표시됩니다.",
        "IP 주소는 목적지가 있는 네트워크를, MAC 주소는 현재 링크에서 프레임을 받을 인터페이스를 가리킵니다.", 0),
    "l23-daily-move-keep-name": ("이사해도 이름은 그대로예요",
        "옛 동네에서 주소와 이름이 있는 사람이 새 동네로 이사하면 주소는 바뀌지만 이름은 그대로입니다. 택배에는 이번 구간 인수자도 필요한데 그것은 따로 물어서 알아낸다고 표시됩니다.",
        "주소는 바뀌어도 이름은 사람에게 붙어 있습니다."),
    "l23-ip-changes-mac-stays": ("IP는 바뀌고 MAC은 NIC에 붙어요",
        "집 Wi-Fi 네트워크에서 IP와 MAC을 가진 노트북이 카페 Wi-Fi 네트워크로 옮겨 가면 IP는 바뀌지만 MAC은 같은 NIC의 것으로 그대로입니다. 프레임에는 받는 MAC이 필요한데 아직 물음표이고, 이는 ARP로 찾는다고 표시됩니다.",
        "IP 주소는 네트워크 설정이나 이동에 따라 달라지고 MAC 주소는 NIC에 연결된 식별자입니다. 그림의 값은 예시예요.", 0),
    "l23-daily-ask-desk-owner": ("책상 번호는 아는데 이름을 몰라요",
        "나와 21번, 30번, 5번 책상이 있고 30번 책상 담당자의 이름을 모릅니다. 사무실에 30번 책상 담당자가 누구인지 물으면 30번 책상 담당자가 대답하고, 이제 담당자에게 상자를 건넬 수 있습니다.",
        "같은 사무실에 물어보면 번호의 주인을 알 수 있습니다."),
    "l23-know-ip-not-mac": ("IP는 아는데 MAC을 몰라요",
        "노트북과 같은 LAN의 PC, 프린터, 서버가 있고 프린터의 IP 192.168.0.30은 아는데 MAC은 모릅니다. LAN에 그 IP를 쓰는 장치가 누구인지 묻자 프린터가 자신의 MAC을 알려 주고, 이제 프린터의 MAC으로 프레임을 보낼 수 있습니다.",
        "ARP는 같은 LAN에서 알고 있는 IPv4 주소에 대응하는 MAC 주소를 알아냅니다. 그림의 주소와 MAC은 예시예요.", 0),
    "l23-daily-gate-guard-name": ("정문 위치는 알아도 경비는 몰라요",
        "입주 안내 카드에 내 호수와 정문 위치는 적혀 있지만 정문 경비의 이름은 없습니다. 밖으로 나가려면 먼저 정문으로 가야 하는데 카드에는 이름이 없어서 따로 알아내야 한다고 표시됩니다.",
        "안내 카드에는 위치만 있고 이름은 없어서 따로 알아내야 합니다."),
    "l23-gateway-mac-needed": ("게이트웨이 MAC은 따로 알아내요",
        "DHCP로 받은 설정에 내 IP 192.168.0.100과 게이트웨이 IP 192.168.0.1은 있지만 게이트웨이 MAC은 물음표입니다. 인터넷으로 나가려면 먼저 게이트웨이로 보내야 하는데 DHCP는 IP까지만 알려 주므로, MAC은 ARP로 따로 알아내야 한다고 표시됩니다.",
        "DHCP는 게이트웨이의 IP 주소는 알려 주지만 그 IP에 대응하는 MAC 주소까지 알려 주지는 않습니다.", 0),
    "l23-daily-far-friend-desk": ("먼 친구에게는 접수창구에 맡겨요",
        "나, 접수창구, 여러 구간, 먼 도시 친구가 한 줄로 있습니다. 먼저 접수창구에 맡기고, 필요한 인수자는 친구가 아니라 접수창구 담당이며, 그다음은 접수창구가 이어서 보냅니다.",
        "내 구간에서 필요한 인수자는 접수창구 담당입니다."),
    "l23-outside-site-gateway": ("외부 사이트는 게이트웨이 MAC이 필요",
        "내 PC, 게이트웨이, 여러 구간, 목적지 IP 3.3.3.3인 외부 서버가 한 줄로 있습니다. PC는 먼저 게이트웨이로 프레임을 보내며, 필요한 MAC은 서버가 아니라 게이트웨이의 것이고, 그다음 경로는 게이트웨이가 정합니다.",
        "외부 사이트의 IP는 설명용 예시입니다. 같은 구간에서 필요한 MAC은 다음으로 패킷을 받을 게이트웨이의 것이에요.", 0),
    "l23-daily-call-out-desk": ("책상 번호를 방 전체에 묻는다",
        "나, 층 방송 장치, 1번 책상이 있고 2번·3번 책상이 아래에 있습니다. ‘1번 책상 담당자 누구세요?’를 모두에게 방송하면 같은 층 모두에게 전달되고, 다른 책상은 자기 번호가 아니라 대답하지 않으며, 1번 책상 담당자는 자신을 찾는 줄 압니다.",
        "방송은 같은 층에만 들리고, 번호의 주인만 알아챕니다."),
    "l23-arp-request-broadcast": ("ARP Request는 모두에게 묻는다",
        "내 PC, 스위치, 게이트웨이가 있고 PC 2와 프린터가 아래에 있습니다. PC가 목적지 MAC FF:FF:FF:FF:FF:FF로 ‘192.168.0.1은 누구?’를 보내면 스위치가 같은 범위로 전달하고, 주인이 아닌 호스트는 응답하지 않으며 게이트웨이는 자신을 찾는 요청임을 알아챕니다.",
        "ARP Request는 브로드캐스트로 보내고, 해당 IP의 주인만 응답합니다. 그림의 주소는 예시예요.", 0),
    "l23-daily-owner-raises-hand": ("담당자만 손들고 대답한다",
        "1번 책상 담당자가 자기 번호임을 알아채고, 손을 들고 번호와 이름을 나에게만 알려 줍니다. 나는 ‘1번 책상 = 김철수’를 알게 되어 이제 상자의 인수자를 정할 수 있습니다.",
        "대답은 물어본 나에게만 갑니다."),
    "l23-arp-reply": ("ARP Reply로 MAC을 알려 준다",
        "게이트웨이가 자신의 IP를 찾는 요청을 알아채고 ARP Reply로 자신의 IP와 MAC을 PC에게 알려 줍니다. PC는 192.168.0.1의 MAC을 알게 되어 프레임의 받는 MAC을 정할 수 있습니다.",
        "ARP Reply는 물어본 PC에게 보내집니다. 그림의 MAC은 48비트 주소의 예시예요.", 0),
    "l23-daily-box-and-truck": ("상자 주소와 트럭 인수자는 달라요",
        "송장 붙은 상자에 보내는 곳 서울과 받는 곳 부산이 있고, 상자 겉에 이번 구간 인수자와 봉인이 붙습니다. 최종 도착지와 이번 구간 인수자는 다른 질문이며, 상자는 먼저 접수창구에 맡겨져 이어서 보내집니다.",
        "상자의 주소는 끝까지 같고 인수자는 구간마다 달라집니다."),
    "l23-packet-in-frame-pair": ("IP 패킷을 프레임에 담는다",
        "출발 IP 192.168.0.100, 목적 IP 3.3.3.3, 데이터로 이뤄진 IP 패킷에 받는 MAC과 출발 MAC, FCS가 붙어 프레임이 됩니다. IP 목적지는 최종적으로 누구에게 보낼지, MAC 목적지는 이번 LAN에서 누구에게 맡길지에 답하며, 프레임은 먼저 게이트웨이로 갑니다.",
        "IP 목적지와 프레임의 목적지 MAC은 서로 다른 질문에 답합니다. IP 주소는 설명용 예시예요.", 0),
    "l23-daily-memo-pad": ("알아낸 이름을 메모해 둔다",
        "처음에는 번호를 방송해서 물어보고, 알아낸 번호와 이름을 메모장에 한 줄 적습니다. 다음에는 메모를 보고 다시 묻지 않고 바로 건네며, 메모는 오래되면 지워질 수 있습니다.",
        "알아낸 대응은 잠깐 적어 두어 매번 다시 묻지 않도록 합니다."),
    "l23-arp-cache": ("ARP 캐시에 대응 관계를 남긴다",
        "PC가 게이트웨이에 ARP로 묻고 대답을 받으면 IP 192.168.0.1과 MAC의 한 쌍이 ARP 캐시에 저장됩니다. 다음 통신에서는 다시 묻지 않고 바로 보내며, 캐시는 잠시 저장이라 오래되면 사라질 수 있습니다.",
        "ARP 캐시는 알아낸 IP와 MAC의 대응을 잠시 저장합니다. 그림의 주소와 MAC은 예시예요.", 0),
    "l23-daily-read-memo": ("메모장에서 이름 쌍을 찾아본다",
        "메모장을 열면 번호와 이름이 한 쌍씩 적혀 있고, 정문 번호가 있는지 살펴봅니다. 아직 적힌 게 없으면 1번 책상에 말을 한 번 걸고 다시 보면 새 메모가 생깁니다.",
        "메모가 비어 있으면 한 번 말을 걸어 본 뒤 다시 확인합니다."),
    "l23-arp-a-command": ("arp -a로 ARP 캐시 확인하기",
        "왼쪽에 arp -a(Windows·macOS)와 ip neigh(Linux) 명령이 있고 오른쪽에 IP 주소와 MAC 주소가 한 쌍씩 표시된 출력 예시가 있습니다. IP와 MAC의 짝을 보고 게이트웨이 주소가 있는지 찾으며, 항목이 없으면 게이트웨이에 통신을 한 번 시도한 뒤 다시 확인하면 새 기록이 생깁니다.",
        "운영체제마다 표시 모양이 다릅니다. 그림의 주소와 MAC은 예시예요.", 0),
}


def build_pages():
    pages = []
    for dn, nn, fn in PAGES:
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
