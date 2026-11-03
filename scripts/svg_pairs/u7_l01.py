#!/usr/bin/env python3
"""Unit 7 Lesson 1 (TCP/UDP overview) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u7_l01.py   (add --svg-only to skip the lesson.md edit).

Pages 4-6 already had good network SVGs (l25-*), so only a daily-life partner is made for them
and the old file is reused as the network SVG."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, me, dur  # reuse local helpers

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("05-tcp-and-udp/lessons/01-*"))
OUT = LESSON / "assets" / "animations"


def mv(a, inner, pts, step, s0, s1, f0=0.1, f1=0.65):
    """Moving item that is only visible from step s0 to s1."""
    return a.vis(a.move(inner, pts, step, f0, f1), s0, s1)


# ---------- Page 1: ping answered != program received ----------
def page1(daily):
    a = Anim(4, dur(daily))
    cli = me(daily, 110, 255, "나" if daily else "내 PC")
    srv = (box(520, 122, 400, 232, LINE, PANEL, 14, dash=True, sw=3)
           + text(720, 150, "회사 건물" if daily else "서버 컴퓨터", 18, MUTED, 700)
           + cell(550, 166, 340, 56, "안내데스크 (벨에 대답)" if daily else "ping 응답 (ICMP)", BLUE, 18)
           + cell(550, 256, 340, 56, "담당 직원" if daily else "웹 서버 프로그램", GREEN, 18))
    body = [srv, cli, line(190, 255, 520, 255, LINE, 3, "8 6"),
            mv(a, parcel() if daily else packet(), [(200, 194), (545, 194)], 1, 1, 1, 0.1, 0.7),
            a.vis(hl(550, 166, 340, 56, BLUE), 1, 2),
            mv(a, packet(0, 0, GREEN), [(545, 194), (200, 194)], 2, 2, 2, 0.1, 0.7),
            a.vis(check(870, 194) + pill(300, 330, "건물에 사람은 있어요" if daily else "서버가 응답했어요 · 왕복 시간", BLUE, 17, True), 2, 3),
            a.vis(hl(550, 256, 340, 56, ORANGE) + ask(870, 284)
                  + text(480, 420, "서류가 담당 직원에게 갔는지는 몰라요" if daily else "프로그램이 요청을 받았는지는 몰라요", 20, ORANGE, 700), 3, 3),
            a.vis(arrow(200, 540, 284, GREEN, 6) + hl(550, 256, 340, 56, GREEN)
                  + pill(300, 330, "등기 · 엽서" if daily else "TCP · UDP", GREEN, 18, True)
                  + text(480, 420, "프로그램에 전달하는 일을 맡아요", 20, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "벨에 대답해도 서류가 전달됐을까?", "건물에 사람이 있다는 것과 담당자가 받았다는 것은 달라요"
        caps = ["안내데스크 벨을 눌러 봐요", "안내데스크가 대답했어요", "담당 직원이 서류를 받았는지는 몰라요", "담당 직원에게 전달하는 방법이 따로 있어요"]
    else:
        t, sub = "ping 응답과 프로그램 전달은 달라요", "TCP와 UDP는 프로그램 사이의 전달을 맡아요"
        caps = ["ping 요청을 보내요", "서버가 ping에 응답했어요", "웹 서버 프로그램이 받았는지는 몰라요", "프로그램 전달은 TCP와 UDP가 맡아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: ACK and retransmission ----------
def page2(daily):
    a = Anim(4, dur(daily))
    s = person(110, 275, "판매자") if daily else pc(110, 290, "서버")
    r = house(850, 300, "내 집") if daily else laptop(850, 290, "내 PC")
    pk = parcel if daily else packet
    ack = pill(0, 0, "수령 문자" if daily else "ACK: 여기까지 받음", GREEN, 17, True)
    body = [s, r, line(180, 305, 780, 305, LINE, 3),
            mv(a, pk(), [(200, 305), (800, 305)], 1, 1, 1),
            a.vis(pk(800, 305), 2, 2),
            mv(a, ack, [(800, 250), (220, 250)], 2, 2, 2, 0.15, 0.8),
            a.vis(check(250, 250), 2.75, 2) + a.vis(text(480, 400, "받은 범위를 알려 줘요" if not daily else "받았다는 소식이 돌아와요", 20, GREEN, 700), 2, 2),
            mv(a, pk(), [(200, 305), (480, 305)], 3, 3, 3, 0.1, 0.55),
            a.vis(cross(480, 305), 3.7, 3),
            a.vis(ask(110, 195) + text(480, 400, "소식이 오지 않아요" if daily else "확인이 오지 않아요", 20, ORANGE, 700), 3, 3),
            mv(a, pk(), [(200, 305), (800, 305)], 4, 4, 4, 0.1, 0.7),
            a.vis(pk(800, 305) + check(850, 215), 4.7, 4)
            + a.vis(text(480, 400, "같은 물건을 다시 보내요" if daily else "확인되지 않은 데이터를 다시 보내요 (재전송)", 20, BLUE, 700), 4, 4)]
    if daily:
        t, sub = "받았다는 소식이 돌아와요", "소식이 없으면 같은 물건을 다시 보내요"
        caps = ["판매자가 택배를 보내요", "집에서 받았다는 문자가 와요", "다음 택배는 소식이 오지 않아요", "소식이 없어서 같은 물건을 다시 보내요"]
    else:
        t, sub = "ACK는 받은 범위를 알려 줘요", "확인되지 않은 데이터는 다시 보낼 수 있어요"
        caps = ["서버 TCP가 데이터를 보내요", "받은 범위를 ACK로 알려 줘요", "다음 데이터는 확인이 오지 않아요", "확인되지 않은 데이터를 재전송해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: receive buffer / window ----------
def page3(daily):
    a = Anim(4, dur(daily))
    x0, step, y = 272, 52, 280
    unit = lambda x, c: box(x, y, 46, 60, c, c if c != PANEL else PANEL, 6, sw=3)
    slots = "".join(box(x0 + i * step, y, 46, 60, LINE, PANEL, 6, sw=3) for i in range(8))
    fill = lambda lo, hi: "".join(box(x0 + i * step, y, 46, 60, ORANGE if daily else BLUE, ORANGE if daily else BLUE, 6, sw=3) for i in range(lo, hi))
    srv = person(100, 270, "판매자") if daily else pc(100, 300, "서버")
    rdr = person(850, 270, "주인") if daily else laptop(850, 300, "브라우저")
    cap = text(x0 + 4 * step - 3, 255, "보관함" if daily else "수신 버퍼", 18, MUTED, 700)
    body = [slots, cap, srv, rdr,
            a.vis(fill(0, 4), 1, 4), a.vis(fill(4, 6), 1, 2),
            a.vis(brace(x0, x0 + 6 * step - 6, 372, ORANGE if daily else BLUE, "아직 안 꺼낸 6칸" if daily else "아직 안 읽은 6칸", False), 1, 1),
            a.vis(brace(x0 + 6 * step, x0 + 8 * step - 6, 372, GREEN, "남은 자리 2칸" if daily else "수신 윈도 2칸", False) + ask(150, 190)
                  + text(150, 160, "더 보내도 될까?", 17, ORANGE, 700), 2, 2),
            a.vis(arrow(800, 740, 310, GREEN, 6) + text(770, 288, "꺼내 가요" if daily else "읽어 가요", 18, GREEN, 700), 3, 3),
            a.vis(brace(x0 + 4 * step, x0 + 8 * step - 6, 372, GREEN, "남은 자리 4칸" if daily else "수신 윈도 4칸", False)
                  + arrow(160, 262, 310, GREEN, 6) + text(480, 455, "여유가 늘어난 만큼 알려 줘요", 20, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "보관함에 남은 자리를 알려 줘요", "주인이 꺼내 가면 자리가 늘어나요"
        caps = ["택배가 보관함에 6칸 들어 있어요", "남은 자리는 2칸이라 조심해야 해요", "주인이 2칸을 꺼내 갔어요", "남은 자리 4칸을 판매자에게 알려 줘요"]
    else:
        t, sub = "수신 윈도는 남은 버퍼 공간이에요", "한 칸은 예시로 1,000바이트예요"
        caps = ["수신 버퍼에 읽지 않은 6칸이 있어요", "남은 공간은 2칸, 수신 윈도도 2칸이에요", "브라우저가 2칸을 읽어 갔어요", "수신 윈도 4칸을 서버에 알려 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: connection memory vs none (daily partner of l25-tcp-connection-vs-udp) ----------
def page4_daily():
    a = Anim(4, dur(True))
    panel = lambda x, lab, c: box(x, 125, 440, 300, LINE, PANEL, 14, sw=3) + text(x + 220, 160, lab, 24, c, 700)
    body = [panel(30, "전화 통화", GREEN), panel(490, "엽서", ORANGE),
            phone(110, 280, "나"), phone(390, 280, "친구"), phone(570, 280, "나"), phone(850, 280, "친구"),
            a.vis(pill(250, 200, "연결: 서로 통화 중", GREEN, 19, True), 2, 4),
            a.vis(pill(110, 200, "기억 중", GREEN, 15) + pill(390, 200, "기억 중", GREEN, 15), 2, 4),
            mv(a, pill(0, 0, "들려요", GREEN, 16, True), [(390, 395), (110, 395)], 3, 3, 4, 0.1, 0.7),
            mv(a, packet(0, 0, ORANGE), [(600, 240), (820, 240)], 3, 3, 4, 0.1, 0.7),
            a.vis(text(710, 360, "돌아오는 대답은 없어요", 17, MUTED), 4, 4),
            a.vis(text(250, 460, "연결을 서로 기억해요", 20, GREEN, 700) + text(710, 460, "연결이 없어요", 20, ORANGE, 700), 4, 4)]
    caps = ["전화는 서로 연결된 약속이에요", "먼저 연결하고, 양쪽이 그 사실을 기억해요", "통화는 ‘들려요’가 돌아오고 엽서는 그냥 보내요", "전화는 연결을 기억하고, 엽서에는 연결이 없어요"]
    return frame(a, "연결 있는 전화, 연결 없는 엽서", "TCP와 UDP의 차이를 일상에서 비교해요", caps, "".join(body))


# ---------- Page 5: layered wrapping (daily partner of l25-layers-data-units) ----------
def page5_daily():
    a = Anim(4, dur(True))
    ys = [215, 305, 395]
    rows = [("받을 담당자", "30번 책상", GREEN), ("받을 건물", "서울 3동 12호", ORANGE), ("이번 구간 인수자", "택배 기사", VIOLET)]
    body = [text(30, 150, "보낼 내용", 20, BLUE, 700, "start")]
    for (lab, val, c), y in zip(rows, ys):
        body.append(line(20, y - 48, 940, y - 48, LINE, 2))
        body.append(text(30, y - 14, lab, 20, c, 700, "start") + text(30, y + 16, val, 18, MUTED, anchor="start"))
    chip = lambda x, lab, c: box(x, 0, 90, 44, c, PANEL, 8, sw=3) + text(x + 45, 29, lab, 17, c, 700)
    names = [("책상", GREEN), ("건물", ORANGE), ("구간", VIOLET)]

    def chips(y, k):
        parts = []
        for i in range(k, 0, -1):  # outermost wrapper is leftmost
            lab, c = names[i - 1]
            parts.append(f'<g transform="translate({380 + (k - i) * 98},{y - 22})">{chip(0, lab, c)}</g>')
        parts.append(f'<g transform="translate({380 + k * 98},{y - 22})">{chip(0, "내용", BLUE)}</g>')
        return "".join(parts)

    labels = ["내용만", "책상 번호를 붙인 것", "건물 주소를 붙인 것", "구간 인수자를 붙인 것"]
    for k in range(4):
        y = 142 if k == 0 else ys[k - 1]
        body.append(a.vis(chips(y, k) + pill(860, y, labels[k], [BLUE, GREEN, ORANGE, VIOLET][k], 14, True, 130), k + 1, k + 1))
    caps = ["보낼 내용을 먼저 준비해요", "먼저 받을 담당자의 책상 번호를 붙여요", "그 위에 받을 건물 주소를 붙여요", "마지막으로 이번 구간 인수자를 붙여요"]
    return frame(a, "겹겹이 붙는 주소", "같은 내용도 겹마다 이름이 달라져요", caps, "".join(body))


# ---------- Page 6: ports (daily partner of l25-client-server-ports) ----------
def page6_daily():
    a = Anim(4, dur(True))
    body = [box(30, 125, 270, 230, LINE, PANEL, 14, sw=3) + text(165, 156, "A동 12호", 20, TXT, 700),
            person(120, 235) + text(120, 305, "나", 17, TXT, 700),
            box(660, 125, 270, 230, LINE, PANEL, 14, sw=3) + text(795, 156, "B동 20호", 20, TXT, 700)
            + box(690, 186, 210, 80, ORANGE, BG, 8, sw=3) + text(795, 238, "80번 창구", 28, ORANGE, 700)
            + text(795, 300, "대기 중", 17, GREEN, 700),
            line(300, 245, 660, 245, LINE, 3, "8 6"),
            a.vis(line(300, 245, 660, 245, GREEN, 6), 4, 4),
            booth(400, 245, "경비실"), warehouse(560, 245, "물류센터"),
            a.vis(hl(690, 186, 210, 80, ORANGE) + pill(795, 330, "80번 창구가 열려 있어요", ORANGE, 15), 1, 1),
            a.vis(pill(215, 230, "번호표 3000", ORANGE, 17, True), 2, 4),
            mv(a, parcel(), [(240, 245), (680, 245)], 3, 3, 3, 0.1, 0.7),
            a.vis(box(150, 380, 660, 60, LINE, PANEL, 10, sw=2)
                  + text(480, 420, "A동 12호 번호표 3000 → B동 20호 80번 창구", 21, TXT, 700), 3, 4),
            a.vis(hl(690, 186, 210, 80, GREEN)
                  + pill(480, 160, "동·호수 + 번호 = 하나의 길", GREEN, 18), 4, 4)]
    caps = ["B동 20호는 80번 창구를 열고 기다려요", "나는 번호표 3000을 받아요", "내 요청은 경비실과 물류센터를 지나 80번으로 가요", "양 끝의 주소와 번호가 하나의 길을 만들어요"]
    return frame(a, "3000번 번호표에서 80번 창구로", "건물 주소와 창구 번호로 받는 곳을 구분해요", caps, "".join(body))


# ---------- Page 7: Listen ----------
def page7(daily):
    a = Anim(4, dur(daily))
    cli = me(daily, 110, 270, "손님" if daily else "클라이언트")
    wnd = lambda y, lab, c: box(560, y, 330, 76, c, PANEL, 10, sw=3) + text(725, y + 46, lab, 22, c, 700)
    srv = (box(520, 120, 410, 270, LINE, PANEL, 14, dash=True, sw=3) + text(725, 150, "가게" if daily else "서버 컴퓨터", 18, MUTED, 700)
           + wnd(170, "80번 창구: 영업 중" if daily else "80번 소켓: Listen", GREEN)
           + wnd(280, "81번 창구: 닫힘" if daily else "8080번: 대기 소켓 없음", MUTED))
    body = [srv, cli,
            a.vis(hl(560, 170, 330, 76, GREEN), 1, 1),
            mv(a, packet(0, 0, BLUE) if not daily else parcel(), [(200, 208), (545, 208)], 2, 2, 2, 0.1, 0.7),
            a.vis(check(905, 208), 2.75, 3) + a.vis(pill(300, 340, "손님을 받아요" if daily else "연결을 받아 줘요", GREEN, 17, True), 2, 3),
            mv(a, packet(0, 0, BLUE) if not daily else parcel(), [(200, 318), (545, 318)], 3, 3, 3, 0.1, 0.7),
            a.vis(cross(905, 318), 3.75, 3) + a.vis(pill(300, 340, "받을 창구가 없어요" if daily else "받을 소켓이 없어요", RED, 17, True), 3, 3),
            a.vis(text(480, 430, "연결을 받으려면 먼저 기다리는 상태여야 해요", 20, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "문을 연 창구만 손님을 받아요", "서버는 창구를 열고 기다려요"
        caps = ["80번 창구는 열려 있고 손님을 기다려요", "손님이 오면 80번 창구가 받아요", "닫힌 창구에는 받을 사람이 없어요", "창구를 먼저 열어 두고 기다려야 해요"]
    else:
        t, sub = "Listen은 연결을 기다리는 상태예요", "접속하려면 IP 주소와 포트 번호를 알아야 해요"
        caps = ["서버 프로그램이 80번에서 Listen해요", "연결 요청이 오면 연결을 받아 줘요", "기다리는 소켓이 없는 포트는 받을 수 없어요", "먼저 Listen 상태여야 연결을 받아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: UDP datagrams ----------
def page8(daily):
    a = Anim(4, dur(daily))
    s = person(110, 275, "나") if daily else pc(110, 290, "송신 프로그램")
    r = person(850, 275, "친구") if daily else laptop(850, 290, "수신 프로그램")
    msg = lambda lab, c: (packet(0, 0, c) + text(0, -24, lab, 15, c, 700))
    body = [s, r, line(180, 305, 780, 305, LINE, 3),
            mv(a, msg("A" if daily else "데이터그램 1", ORANGE), [(200, 305), (480, 305)], 1, 1, 2, 0.1, 0.7),
            a.vis(cross(480, 305), 1.75, 2),
            mv(a, msg("B" if daily else "데이터그램 2", BLUE), [(200, 305), (760, 305)], 2, 2, 3, 0.1, 0.7),
            a.vis(text(480, 400, "연결 절차 없이 바로 보내요", 20, MUTED, 700), 1, 1),
            a.vis(text(480, 400, "각각 따로 보낸 별개의 메시지예요", 20, BLUE, 700), 2, 2),
            a.vis(pill(790, 215, "받은 것: B 한 통" if daily else "받은 것: 데이터그램 2", GREEN, 17, True) + ask(110, 215) + text(480, 400, "A는 잘 갔는지 알려 주지 않아요" if daily else "데이터그램 1이 갔는지 알려 주지 않아요", 20, ORANGE, 700), 3, 3),
            a.vis(pill(480, 200, "확인 · 재전송 · 윈도 없음", ORANGE, 19, True)
                  + text(480, 400, "필요하면 프로그램이 직접 마련해요", 20, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "엽서는 따로따로 가요", "보낸 뒤 확인해 주는 사람은 없어요"
        caps = ["엽서 A를 그냥 보내요", "엽서 B를 따로 보내요", "B만 도착해도 A가 갔는지는 알려 주지 않아요", "필요하면 보내는 사람이 직접 확인해야 해요"]
    else:
        t, sub = "UDP는 데이터그램을 따로 보내요", "연결도 수신 확인도 없어요"
        caps = ["데이터그램 1을 연결 없이 보내요", "데이터그램 2는 별개의 메시지예요", "하나만 도착해도 나머지는 알려 주지 않아요", "필요한 기능은 프로그램이 마련해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, daily fn, net fn or None, network after_paragraph)
PAGES = [
    ("l25-daily-bell-vs-delivered", "l25-ping-vs-program", page1, 2),
    ("l25-daily-parcel-receipt-resend", "l25-ack-and-retransmit", page2, 3),
    ("l25-daily-locker-slots", "l25-receive-window-slots", page3, 2),
    ("l25-daily-call-vs-postcard", "l25-tcp-connection-vs-udp", page4_daily, 3),
    ("l25-daily-address-layers", "l25-layers-data-units", page5_daily, 0),
    ("l25-daily-counter-80", "l25-client-server-ports", page6_daily, 3),
    ("l25-daily-open-counter", "l25-listen-socket", page7, 0),
    ("l25-daily-postcards-separate", "l25-udp-datagrams", page8, 0),
]

COPY = {
    "l25-daily-bell-vs-delivered": ("벨에 대답해도 서류가 전달됐을까?",
        "나와 회사 건물이 있습니다. 안내데스크 벨을 누르면 안내데스크가 대답하지만 담당 직원이 서류를 받았는지는 물음표로 남습니다. 마지막에 담당 직원에게 전달하는 방법이 따로 있다고 표시됩니다.",
        "건물에 사람이 있다는 것과 담당 직원이 받았다는 것은 다릅니다."),
    "l25-ping-vs-program": ("ping 응답과 프로그램 전달은 달라요",
        "내 PC와 서버 컴퓨터가 있습니다. ping 요청에 서버의 ICMP 응답이 돌아오지만 웹 서버 프로그램이 요청을 받았는지는 물음표입니다. 마지막에 프로그램 사이의 전달은 TCP와 UDP가 맡는다고 표시됩니다.",
        "ping 응답은 서버가 응답했다는 뜻이고, 프로그램 사이의 데이터 전달은 TCP와 UDP가 맡습니다."),
    "l25-daily-parcel-receipt-resend": ("받았다는 소식이 돌아와요",
        "판매자가 택배를 보내면 집에서 받았다는 문자가 돌아옵니다. 다음 택배는 도중에 사라지고 소식이 오지 않아 판매자가 같은 물건을 다시 보내고 집에 도착합니다.",
        "받았다는 소식이 없으면 같은 물건을 다시 보낼 수 있습니다."),
    "l25-ack-and-retransmit": ("ACK는 받은 범위를 알려 줘요",
        "서버가 PC로 데이터를 보내면 PC의 TCP가 받은 범위를 ACK로 돌려보냅니다. 다음 데이터는 도중에 사라져 확인이 오지 않고, 서버가 확인되지 않은 데이터를 다시 보내 PC에 도착합니다.",
        "ACK는 상대 TCP가 받은 범위를 알리고, 확인되지 않은 데이터는 재전송할 수 있습니다.", 3),
    "l25-daily-locker-slots": ("보관함에 남은 자리를 알려 줘요",
        "8칸 보관함에 택배 6칸이 차 있고 남은 자리는 2칸입니다. 주인이 2칸을 꺼내 가면 택배는 4칸, 남은 자리는 4칸이 되고 이 소식을 판매자에게 알립니다.",
        "주인이 꺼내 가면 남은 자리가 늘어납니다. 한 칸은 설명용 단위입니다."),
    "l25-receive-window-slots": ("수신 윈도는 남은 버퍼 공간이에요",
        "수신 버퍼 8칸 중 읽지 않은 데이터가 6칸이고 수신 윈도는 2칸입니다. 브라우저가 2칸을 읽으면 데이터는 4칸, 수신 윈도는 4칸이 되어 서버에 알립니다.",
        "수신 윈도는 더 받아 둘 수 있는 바이트 범위입니다. 한 칸은 예시로 1,000바이트입니다.", 2),
    "l25-daily-call-vs-postcard": ("연결 있는 전화, 연결 없는 엽서",
        "왼쪽 전화 통화 칸에서는 두 전화기가 연결되어 서로 기억하고 ‘들려요’가 돌아옵니다. 오른쪽 엽서 칸에서는 연결 없이 엽서가 한 방향으로 가고 돌아오는 대답이 없습니다.",
        "전화는 연결을 기억하고, 엽서에는 연결이 없습니다."),
    "l25-daily-address-layers": ("겹겹이 붙는 주소",
        "보낼 내용에 책상 번호, 건물 주소, 이번 구간 인수자가 차례로 겹겹이 붙습니다. 겹이 늘 때마다 해당 행이 강조됩니다.",
        "같은 내용도 어떤 겹을 붙였는지에 따라 이름이 달라집니다."),
    "l25-daily-counter-80": ("3000번 번호표에서 80번 창구로",
        "A동 12호의 내가 번호표 3000을 받고, 요청이 경비실과 물류센터를 지나 B동 20호의 80번 창구로 갑니다. 건물 주소와 창구 번호가 하나의 길을 만든다고 표시됩니다.",
        "건물 주소와 창구 번호가 함께 받는 곳을 구분합니다."),
    "l25-daily-open-counter": ("문을 연 창구만 손님을 받아요",
        "가게에 80번 창구는 영업 중이고 81번 창구는 닫혀 있습니다. 손님이 80번에 가면 받아 주고, 닫힌 창구에 가면 받을 사람이 없다고 표시됩니다.",
        "연결을 받으려면 서버가 먼저 기다리는 상태여야 합니다."),
    "l25-listen-socket": ("Listen은 연결을 기다리는 상태예요",
        "서버 컴퓨터의 80번 소켓은 Listen 상태이고 8080번에는 기다리는 소켓이 없습니다. 클라이언트의 연결 요청은 80번에서는 받아지고, 기다리는 소켓이 없는 포트에서는 받을 수 없습니다. 포트 번호는 예시입니다.",
        "서버는 포트에서 Listen 상태로 연결을 기다립니다. 그림의 포트 번호는 예시입니다.", 0),
    "l25-daily-postcards-separate": ("엽서는 따로따로 가요",
        "내가 엽서 A와 B를 연결 없이 차례로 보냅니다. A는 도중에 사라지고 B만 친구에게 도착하지만 A가 어떻게 됐는지는 아무도 알려 주지 않습니다. 필요하면 보내는 사람이 직접 확인해야 한다고 표시됩니다.",
        "엽서는 따로 가며 보낸 뒤 확인해 주는 사람이 없습니다."),
    "l25-udp-datagrams": ("UDP는 데이터그램을 따로 보내요",
        "송신 프로그램이 데이터그램 1과 2를 연결 없이 차례로 보냅니다. 데이터그램 1은 도중에 사라지고 2만 수신 프로그램에 도착하지만 1에 대한 알림은 없습니다. 확인, 재전송, 윈도가 없으므로 필요하면 프로그램이 마련해야 합니다.",
        "UDP 자체에는 수신 확인, 재전송, 수신 윈도 흐름 제어가 없습니다.", 0),
}

# reused network SVGs keep their existing text
OLD = {
    "l25-tcp-connection-vs-udp": ("연결이 있는 TCP, 연결이 없는 UDP",
        "화면 왼쪽에서는 두 컴퓨터 사이에 점선 통로가 생기고 확인 신호가 오갑니다. 오른쪽에서는 두 컴퓨터 사이에 아무 통로 없이 엽서 모양 짐이 한 방향으로 날아갑니다.",
        "TCP는 먼저 연결을 맺고 확인을 주고받으며, UDP는 연결 없이 그냥 보냅니다."),
    "l25-layers-data-units": ("층을 지날 때마다 이름이 바뀌는 데이터",
        "작은 데이터 상자에 먼저 포트 봉투, 다음 IP 봉투, 마지막으로 MAC 봉투가 차례로 씌워지고, 각 단계마다 Segment, Packet, Frame 이름표가 붙습니다.",
        "같은 데이터가 포트, IP, MAC 순으로 겹겹이 감싸지며 Segment, Packet, Frame이 됩니다."),
    "l25-client-server-ports": ("클라이언트의 3000번에서 서버의 80번으로",
        "왼쪽의 클라이언트(192.168.0.10, 포트 3000)에서 오른쪽의 서버(192.168.1.20, 포트 80)로 요청 봉투가 스위치와 라우터를 거쳐 이동하는 장면입니다.",
        "각 호스트의 IP 주소와 포트 번호로 연결의 양 끝을 구분합니다. 이 예에서는 서로 다른 /24 네트워크 사이를 라우터가 연결합니다."),
}

# existing static diagrams on pages 2 and 3 (kept as they are)
STATIC = {
    2: ("assets/diagrams/tcp-receipt.svg", "데이터를 보내는 방향과 확인 응답이 돌아오는 방향",
        "서버에서 PC의 TCP로 사진 데이터가 가고, 반대 방향으로 TCP 확인 응답이 돌아온다. PC의 TCP 수신과 브라우저가 읽는 단계는 별도로 표시되어 있다.",
        "ACK는 상대 TCP가 받은 범위를 알려 준다. 브라우저가 사진을 읽거나 저장했다는 확인은 아니다.", 3),
    3: ("assets/diagrams/receive-capacity.svg", "프로그램이 읽으면 수신 버퍼의 여유가 늘어난다",
        "8칸의 수신 버퍼에 데이터 6칸과 빈칸 2칸이 있다. 브라우저가 2칸을 읽은 뒤에는 데이터 4칸과 빈칸 4칸이 된다. 한 칸은 예시로 1,000바이트를 뜻한다.",
        "수신 윈도는 더 받아 둘 수 있는 바이트 범위를 알린다. 그림은 수신 버퍼의 용량과 읽기의 관계를 단순화한 예시이며, 회선 속도나 세그먼트 하나의 크기를 뜻하지 않는다.", 3),
}


def build_pages():
    pages = []
    for i, (dn, nn, fn, after) in enumerate(PAGES, 1):
        daily_fn = fn if fn.__code__.co_argcount == 0 else (lambda f=fn: f(True))
        write(OUT, dn, daily_fn())
        items = [(dn, *COPY[dn], -1)]
        if nn in OLD:
            items.append((nn, *OLD[nn], after))
        else:
            write(OUT, nn, fn(False))
            c = COPY[nn]
            items.append((nn, c[0], c[1], c[2], after))
        if i in STATIC:
            items.append(STATIC[i])
        pages.append(items)
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
