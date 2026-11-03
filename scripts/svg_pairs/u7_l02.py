#!/usr/bin/env python3
"""Unit 7 Lesson 2 (TCP connection setup) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u7_l02.py   (add --svg-only to skip the lesson.md edit).

The daily-life side is the phone call from the lesson text. Pages 5 and 7 already had good network
SVGs (l26-*), so only a daily partner is made for them and the old file is reused."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, dur  # reuse local helpers
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("05-tcp-and-udp/lessons/02-*"))
OUT = LESSON / "assets" / "animations"


def dim(inner):
    return f'<g opacity=".4">{inner}</g>'


def end(daily, x, y, label):
    return phone(x, y, label) if daily else (laptop(x, y, label) if x < 480 else pc(x, y, label))


# ---------- Page 1: three messages ----------
def page1(daily):
    a = Anim(4, dur(daily))
    L, R = 200, 760
    rows = [(210, True, "“여보세요?”" if daily else "SYN", "연결을 시작하고 싶어요" if daily else "연결 요청", GREEN),
            (300, False, "“네, 들려요. 그쪽도 들리나요?”" if daily else "SYN+ACK", "요청을 확인하고 나도 부르는 거예요" if daily else "요청 확인 + 서버도 연결 요청", BLUE),
            (390, True, "“네, 들립니다”" if daily else "ACK", "내 말이 들렸다는 확인이에요" if daily else "서버의 요청에 대한 확인", ORANGE)]
    body = [pill(L, 140, "나 (클라이언트)" if daily else "클라이언트", BLUE, 18, True, 200), pill(R, 140, "가게 (서버)" if daily else "서버", GREEN, 18, True, 200),
            line(L, 165, L, 455, LINE, 3, "8 6"), line(R, 165, R, 455, LINE, 3, "8 6")]
    for k, (y, right, lab, sub, c) in enumerate(rows, 1):
        arr = lambda col: (arrow(L + 8, R - 8, y, col, 5) if right else arrow(R - 8, L + 8, y, col, 5))
        txt = lambda col: pill(480, y - 28, lab, col, 18, True) + text(480, y + 30, sub, 16, MUTED)
        body.append(a.vis(arr(c) + txt(c), k, k))
        if k < 4:
            body.append(a.vis(dim(arr(c) + txt(c)), k + 1, 4))
    body.append(a.vis(pill(480, 445, "세 번의 악수로 연결 준비 끝" if not daily else "세 마디로 서로 들린다는 확인 끝", GREEN, 19, True), 4, 4))
    if daily:
        t, sub = "여보세요, 네 들려요, 네", "전화는 세 마디로 서로 들리는지 확인해요"
        caps = ["먼저 걸어 온 쪽이 “여보세요?” 하고 불러요", "상대가 “들려요, 그쪽도 들리나요?” 하고 답해요", "처음 쪽이 “네, 들립니다” 하고 확인해요", "세 마디가 오가야 서로 들린다고 알아요"]
    else:
        t, sub = "SYN, SYN+ACK, ACK", "TCP 연결 준비는 메시지 세 개예요"
        caps = ["클라이언트가 SYN으로 연결을 요청해요", "서버가 SYN+ACK로 확인하며 나도 요청해요", "클라이언트가 ACK로 마지막 확인을 해요", "세 메시지가 오가면 연결 준비가 끝나요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: RTT ----------
def page2(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 130, 290, "나" if daily else "노트북"), end(daily, 830, 290, "가게" if daily else "웹 서버")
    pk = lambda c: packet(0, 0, c)
    body = [cli, srv, line(200, 300, 760, 300, LINE, 3, "8 6"),
            a.vis(pill(830, 190, "가게 번호 + 내선 80번" if daily else "192.168.0.20 · 포트 80", ORANGE, 17, True), 1, 4),
            a.vis(hl(780, 220, 100, 90, ORANGE, 12), 1, 1),
            a.vis(arrow(230, 740, 245, BLUE, 5) + pill(480, 215, "가는 데 25ms", BLUE, 18, True), 2, 4),
            mv(a, pk(BLUE), [(240, 245), (730, 245)], 2, 2, 2, 0.1, 0.8),
            a.vis(arrow(730, 240, 320, GREEN, 5) + pill(480, 350, "오는 데 25ms", GREEN, 18, True), 3, 4),
            mv(a, pk(GREEN), [(730, 320), (240, 320)], 3, 3, 3, 0.1, 0.8),
            a.vis(brace(230, 740, 392, ORANGE, "왕복 시간 RTT = 50ms", False, 19)
                  + text(480, 464, "서버가 처리하는 시간은 0으로 둔 단순한 예시예요", 16, MUTED), 4, 4)]
    if daily:
        t, sub = "말을 건네고 대답이 오기까지", "걸어 온 쪽이 대답을 들을 때까지가 왕복 시간이에요"
        caps = ["가게 번호와 내선 80번으로 걸어요", "내 목소리가 가게로 가는 데 25ms가 걸려요", "대답이 돌아오는 데 25ms가 걸려요", "가서 돌아오는 전체가 왕복 시간(RTT) 50ms예요"]
    else:
        t, sub = "RTT는 왕복 시간이에요", "연결 준비에도 네트워크 지연이 들어가요"
        caps = ["노트북이 192.168.0.20의 포트 80으로 연결을 요청해요", "메시지가 서버로 가는 데 25ms가 걸려요", "응답이 돌아오는 데 25ms가 걸려요", "가고 오는 전체가 RTT 50ms예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: SYN segment with no payload ----------
def page3(daily):
    a = Anim(4, dur(daily))
    xs = [(57, 230), (312, 330), (667, 230)]
    names = ["받는 곳 · 보내는 곳" if daily else "IP 헤더", "말머리" if daily else "TCP 헤더", "용건" if daily else "Payload"]
    cols = [VIOLET, GREEN, ORANGE]
    body = [text(480, 175, "쪽지 한 장" if daily else "TCP 세그먼트", 19, MUTED, 700)]
    for (x, w), n, c in zip(xs, names, cols):
        body.append(box(x, 200, w, 130, c, PANEL, 10, sw=3) + text(x + w / 2, 236, n, 20, c, 700))
    body += [a.vis(hl(312, 200, 330, 130, GREEN, 12) + pill(477, 285, "연결을 시작해요" if daily else "SYN 표시 켜짐", GREEN, 19, True), 2, 4),
             a.vis(pill(477, 360, "내 시작 번호 1000" if daily else "초기 순서번호 1000", BLUE, 19, True), 3, 4),
             a.vis(text(782, 290, "비어 있어요", 20, MUTED, 700), 4, 4),
             a.vis(hl(667, 200, 230, 130, ORANGE, 12) + pill(480, 415, "파일 내용 없이 연결 준비만 해요" if not daily else "용건 없이 연결 준비만 해요", ORANGE, 18, True), 4, 4)]
    if daily:
        t, sub = "용건 없는 첫 마디", "“여보세요?”에는 용건이 들어 있지 않아요"
        caps = ["쪽지에는 받는 곳, 말머리, 용건 칸이 있어요", "말머리에서 ‘연결을 시작해요’를 켜요", "내 시작 번호 1000을 함께 알려요", "용건 칸은 비어 있고 연결 준비만 해요"]
    else:
        t, sub = "연결 요청도 세그먼트예요", "SYN 세그먼트에는 Payload가 없어요"
        caps = ["IP 헤더, TCP 헤더, Payload로 이루어져요", "TCP 헤더의 SYN 표시를 켜요", "초기 순서번호 1000을 함께 알려요", "Payload는 비어 있고 연결 준비만 해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: ACK number = next expected ----------
def page4(daily):
    a = Anim(4, dur(daily))
    nums = [999, 1000, 1001, 1002, 1003]
    x0, w, gap, y = 130, 110, 20, 270
    X = lambda i: x0 + i * (w + gap)
    base = "".join(cell(X(i), y, w, 64, (f"{n}쪽" if daily else str(n)), LINE, 22) for i, n in enumerate(nums))
    body = [text(480, 190, "책의 쪽번호처럼" if daily else "순서번호", 19, MUTED, 700), base,
            a.vis(hl(X(1), y, w, 64, BLUE) + pill(X(1) + w / 2, 225, "SYN 1000" if not daily else "“내 시작은 1000쪽”", BLUE, 18, True), 1, 4),
            a.vis(box(X(1), y, w, 64, BLUE, BLUE, 6, sw=3) + text(X(1) + w / 2, y + 40, "1000쪽" if daily else "1000", 22, BG, 700)
                  + brace(X(1), X(1) + w, 362, ORANGE, "SYN이 한 자리 차지", False, 17), 2, 2),
            a.vis(hl(X(2), y, w, 64, GREEN), 3, 4),
            a.vis(line(X(2) + w / 2, 340, X(2) + w / 2, 366, GREEN, 4) + pill(X(2) + w / 2, 390, "ACK 1001" if not daily else "“다음은 1001쪽”", GREEN, 18, True), 3, 4),
            a.vis(text(480, 450, "ACK 번호 = 다음에 받고 싶은 번호" if not daily else "책갈피 = 다음에 펼칠 쪽", 22, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "다음에 펼칠 쪽을 알려 줘요", "받았다는 표시는 다음 쪽 번호로 해요"
        caps = ["내가 1000쪽부터 시작한다고 말해요", "그 신호도 한 쪽을 차지한다고 쳐요", "상대는 다음에 펼칠 1001쪽을 알려 줘요", "책갈피는 방금 읽은 쪽이 아니라 다음 쪽이에요"]
    else:
        t, sub = "ACK 번호는 다음 순서번호", "SYN 1000 다음에는 ACK 1001이 와요"
        caps = ["클라이언트가 SYN 1000을 보내요", "SYN도 순서번호의 한 자리를 차지해요", "서버가 다음에 받고 싶은 1001을 알려 줘요", "ACK 번호는 방금 받은 번호가 아니라 다음 번호예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5 daily partner of l26-three-way-handshake ----------
def page5_daily():
    a = Anim(4, dur(True))
    L, R = 330, 650
    pq = lambda x, row: text(x + 230, row, "?", 26, MUTED, 700, "end")
    labs = lambda x, mine, theirs: (text(x + 20, 190, "내 번호", 18, MUTED, anchor="start") + text(x + 20, 255, "상대 번호", 18, MUTED, anchor="start"))
    frame_p = lambda x, ok: box(x, 150, 250, 190, GREEN if ok else LINE, PANEL, 12, sw=3) + labs(x, 0, 0)
    body = [pill(L - 20, 128, "나 (클라이언트)", BLUE, 16, True, 190), pill(R + 20, 128, "가게 (서버)", GREEN, 16, True, 190),
            line(L, 150, L, 460, LINE, 3), line(R, 150, R, 460, LINE, 3),
            a.vis(frame_p(30, False) + frame_p(700, False) + pq(30, 190) + pq(30, 255) + pq(700, 190) + pq(700, 255), 1, 1),
            ]
    # panel values over time (client left, server right)
    states = [
        (1, 1, ("1000", "?"), ("?", "?")),
        (2, 2, ("1000", "?"), ("4000", "1000")),
        (3, 3, ("1000", "4000"), ("4000", "1000")),
        (4, 4, ("1000", "4000"), ("4000", "1000")),
    ]
    for s0, s1, (cm, ct), (sm, st) in states:
        ok = s0 == 4
        val = lambda x, mine, theirs: ("".join(
            text(x + 230, row, v, 26, c if v != "?" else MUTED, 700, "end") for v, row, c in ((mine, 190, BLUE), (theirs, 255, GREEN))))
        body.append(a.vis(frame_p(30, ok) + val(30, cm, ct) + frame_p(700, ok) + val(700, sm, st), s0, s1))
    msgs = [(1, True, 185, "“여보세요, 내 번호는 1000”", None, BLUE),
            (2, False, 270, "“들려요, 다음은 1001”", "내 번호는 4000이에요", GREEN),
            (3, True, 355, "“4000 잘 들었어요”", "다음은 4001이에요", ORANGE)]
    for k, right, y, lab, sub, c in msgs:
        arr = arrow(L + 8, R - 8, y, c, 5) if right else arrow(R - 8, L + 8, y, c, 5)
        inner = arr + text(485, y - 18, lab, 17, c, 700) + (text(485, y + 30, sub, 16, MUTED) if sub else "")
        body.append(a.vis(inner, k, 4))
    body.append(a.vis(pill(485, 440, "서로의 시작 번호를 알고 확인했어요", GREEN, 18, True), 4, 4))
    caps = ["처음 쪽이 “여보세요, 내 번호는 1000”이라고 해요", "상대가 “들려요, 다음은 1001. 내 번호는 4000”이라고 해요",
            "처음 쪽이 “4000 잘 들었어요, 다음은 4001”이라고 해요", "세 번 오가면 양쪽이 서로의 번호를 알고 확인했어요"]
    return frame(a, "여보세요, 번호를 서로 알려 줘요", "예시 번호 1000과 4000으로 세 마디를 따라가요", caps, "".join(body))


# ---------- Page 6: MSS ----------
def page6(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 100, 215, "나" if daily else "클라이언트"), end(daily, 860, 215, "친구" if daily else "서버")
    m1, m2 = ("70자", "60자") if daily else ("1460", "1400")
    chunk = lambda x, y, lab, c: cell(x, y, 80, 40, lab, c, 16)
    body = [cli, srv,
            a.vis(arrow(180, 780, 170, BLUE, 5) + pill(480, 144, f"“나한테는 한 통에 {m1} 이하로”" if daily else f"SYN · MSS {m1}", BLUE, 17, True), 1, 4),
            a.vis(arrow(780, 180, 235, GREEN, 5) + pill(480, 262, f"“나한테는 한 통에 {m2} 이하로”" if daily else f"SYN+ACK · MSS {m2}", GREEN, 17, True), 2, 4),
            a.vis(text(140, 340, "나 → 친구" if daily else "클라 → 서버", 17, GREEN, 700, "start")
                  + "".join(chunk(300 + i * 92, 320, f"≤{m2}", GREEN) for i in range(3))
                  + text(140, 400, "친구 → 나" if daily else "서버 → 클라", 17, BLUE, 700, "start")
                  + "".join(chunk(300 + i * 92, 380, f"≤{m1}", BLUE) for i in range(4)), 3, 4),
            a.vis(pill(480, 456, "방향마다 한 번에 보내는 크기가 달라도 돼요", ORANGE, 18, True), 4, 4)]
    if daily:
        t, sub = "한 통에 보낼 수 있는 길이", "문자는 상대가 정한 길이에 맞춰 나눠 보내요"
        caps = ["내가 먼저 “나한테는 한 통에 70자 이하로” 알려요", "친구도 “나한테는 60자 이하로” 알려요", "긴 내용은 상대가 정한 길이에 맞춰 나눠 보내요", "방향마다 길이가 달라도 돼요"]
    else:
        t, sub = "MSS는 한 세그먼트의 데이터 크기", "연결을 시작할 때 서로 알려 줘요"
        caps = ["클라이언트가 SYN에 MSS 1460을 담아요", "서버가 SYN+ACK에 MSS 1400을 담아요", "각자 상대가 알린 MSS 이하로 나눠 보내요", "방향마다 MSS가 달라도 돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7 daily partner of l26-tcp-states ----------
def page7_daily():
    a = Anim(4, dur(True))
    pan = lambda x, lab: (box(x, 125, 260, 270, LINE, PANEL, 12, sw=3) + text(x + 130, 158, lab, 20, TXT, 700))
    stp = lambda x, lab, c, filled=False: pill(x + 130, 345, lab, c, 20, filled, 220)
    body = [pan(40, "나 (거는 쪽)"), pan(660, "가게 (받는 쪽)"), phone(170, 255), phone(790, 255),
            line(300, 215, 660, 215, LINE, 3, "8 6"), line(300, 255, 660, 255, LINE, 3, "8 6"),
            a.vis(stp(660, "벨 기다림", ORANGE) + stp(40, "아직 아무것도 없음", MUTED) + text(790, 180, "(( 대기 ))", 17, ORANGE, 700), 1, 1),
            a.vis(stp(40, "거는 중", BLUE) + stp(660, "벨 울림", BLUE), 2, 2),
            a.vis(stp(40, "통화 중", GREEN, True) + stp(660, "벨 울림", BLUE)
                  + pill(480, 215, "← 들려요", BLUE, 17, True), 3, 3),
            a.vis(stp(40, "통화 중", GREEN, True) + stp(660, "통화 중", GREEN, True)
                  + pill(480, 215, "네, 들립니다 →", ORANGE, 17, True)
                  + text(480, 440, "받는 쪽은 마지막 대답이 닿은 뒤에 통화 중이 돼요", 18, ORANGE, 700), 4, 4)]
    caps = ["가게는 벨을 열어 두고 전화를 기다려요", "거는 쪽은 거는 중, 받는 쪽은 벨이 울려요", "“들려요”를 받은 거는 쪽이 먼저 통화 중이 돼요", "마지막 대답이 닿으면 받는 쪽도 통화 중이에요"]
    return frame(a, "전화 상태가 바뀌어요", "벨 기다림 → 거는 중·벨 울림 → 통화 중", caps, "".join(body))


# ---------- Page 8: virtual circuit ----------
def page8(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 110, 255, "나" if daily else "클라이언트"), end(daily, 850, 255, "친구" if daily else "서버")
    mids = "".join(router(x, 255, "기지국" if daily else "라우터") for x in (330, 480, 630))
    rec = lambda x, s1, s2: (box(x - 105, 350, 210, 76, GREEN, PANEL, 10, sw=2) + text(x, 380, s1, 16, GREEN, 700) + text(x, 406, s2, 15, MUTED))
    body = [line(170, 262, 790, 262, LINE, 3), cli, srv, mids,
            a.vis(pill(110, 170, "통화 중" if daily else "ESTABLISHED", GREEN, 17, True) + pill(850, 170, "통화 중" if daily else "ESTABLISHED", GREEN, 17, True)
                  + rec(135, "기록하는 것", "상대 번호 · 통화 상태" if daily else "상대 주소·포트") + rec(825, "기록하는 것", "상대 번호 · 통화 상태" if daily else "순서번호·MSS"), 1, 4),
            a.vis(line(150, 205, 810, 205, ORANGE, 3, "10 8") + cross(480, 205)
                  + text(480, 180, "새 전용선은 깔리지 않아요" if daily else "새 케이블이나 전용선은 없어요", 18, ORANGE, 700), 2, 4),
            mv(a, parcel() if daily else packet(), [(180, 262), (780, 262)], 3, 3, 3, 0.1, 0.85),
            a.vis(text(480, 405, "이미 있는 통신망으로 이야기가 가요" if daily else "데이터는 이미 있는 네트워크로 가요", 18, BLUE, 700), 3, 3),
            a.vis(pill(480, 456, "연결됨 ≠ 용건이 처리됨" if daily else "연결 수립 ≠ 앱 데이터 처리 성공", RED, 19, True), 4, 4)]
    if daily:
        t, sub = "통화 중은 새 전선이 아니에요", "양쪽이 통화 상태를 기록해 둔 거예요"
        caps = ["두 전화기는 서로 통화 중이라고 기록해요", "통화한다고 새 전용선이 깔리지는 않아요", "목소리는 이미 있는 통신망을 지나가요", "통화 중이라는 것이 용건 처리를 뜻하지는 않아요"]
    else:
        t, sub = "TCP 연결은 논리적인 관계예요", "양 끝이 상태를 기록해 둔 가상 회선이에요"
        caps = ["양 끝의 TCP가 연결 상태를 기록해요", "새 케이블이나 전용선은 생기지 않아요", "데이터는 기존 IP 패킷과 프레임으로 가요", "연결 수립이 앱의 처리 성공을 뜻하지는 않아요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, daily fn, net fn or None, network after_paragraph)
PAGES = [
    ("l26-daily-hello-3-steps", "l26-syn-synack-ack", page1, 2),
    ("l26-daily-call-round-trip", "l26-rtt-50ms", page2, 2),
    ("l26-daily-note-without-body", "l26-syn-segment-no-payload", page3, 1),
    ("l26-daily-bookmark-next-page", "l26-ack-next-number", page4, 1),
    ("l26-daily-numbers-call", "l26-three-way-handshake", page5_daily, 3),
    ("l26-daily-text-length-limit", "l26-mss-exchange", page6, 1),
    ("l26-daily-call-states", "l26-tcp-states", page7_daily, 2),
    ("l26-daily-no-new-wire", "l26-virtual-circuit", page8, 1),
]

COPY = {
    "l26-daily-hello-3-steps": ("여보세요, 네 들려요, 네",
        "나와 가게 사이에서 먼저 “여보세요?”, 이어서 “네, 들려요. 그쪽도 들리나요?”, 마지막으로 “네, 들립니다”가 차례로 오갑니다. 세 마디가 오가야 서로 들린다고 알게 된다고 표시됩니다.",
        "전화는 세 마디로 서로 들리는지 확인합니다. TCP의 세 메시지도 요청, 응답 겸 요청, 마지막 확인으로 이어집니다."),
    "l26-syn-synack-ack": ("SYN, SYN+ACK, ACK",
        "클라이언트와 서버 사이에서 SYN, SYN+ACK, ACK 세 메시지가 차례로 오가며 연결 준비가 끝납니다.",
        "TCP 연결 준비는 연결 요청, 요청 확인과 서버의 요청, 마지막 확인의 세 메시지로 이루어집니다.", 2),
    "l26-daily-call-round-trip": ("말을 건네고 대답이 오기까지",
        "나와 가게가 있습니다. 가게 번호와 내선 80번으로 걸면 내 목소리가 가는 데 25ms, 대답이 돌아오는 데 25ms가 걸리고 전체가 왕복 시간 50ms라고 표시됩니다.",
        "말을 건네고 대답을 들을 때까지가 왕복 시간입니다. 25ms씩이라는 값은 예시입니다."),
    "l26-rtt-50ms": ("RTT는 왕복 시간이에요",
        "노트북이 192.168.0.20의 포트 80으로 연결을 요청합니다. 서버로 가는 데 25ms, 돌아오는 데 25ms가 걸려 RTT는 50ms이고, 서버 처리 시간은 0으로 둔 단순한 예시입니다.",
        "RTT는 요청을 보내고 응답이 돌아오기까지의 왕복 시간입니다. 25ms씩 나눈 것은 이 예를 위한 단순화입니다.", 2),
    "l26-daily-note-without-body": ("용건 없는 첫 마디",
        "쪽지 한 장에 받는 곳·보내는 곳, 말머리, 용건 칸이 있습니다. 말머리에서 연결을 시작한다는 표시와 내 시작 번호 1000이 켜지고 용건 칸은 비어 있어 연결 준비만 한다고 표시됩니다.",
        "첫 “여보세요?”에는 용건이 들어 있지 않고 연결 준비만 합니다. 1000은 예시 번호입니다."),
    "l26-syn-segment-no-payload": ("연결 요청도 세그먼트예요",
        "TCP 세그먼트가 IP 헤더, TCP 헤더, Payload로 나뉘어 있습니다. TCP 헤더의 SYN 표시가 켜지고 초기 순서번호 1000이 담기며 Payload는 비어 있습니다.",
        "SYN 세그먼트는 연결 준비만 하며 Payload가 없습니다. 초기 순서번호 1000은 예시입니다.", 1),
    "l26-daily-bookmark-next-page": ("다음에 펼칠 쪽을 알려 줘요",
        "쪽번호 999부터 1003이 한 줄로 있습니다. 내 시작은 1000쪽이고 그 신호도 한 쪽을 차지하며, 상대는 방금 읽은 쪽이 아니라 다음에 펼칠 1001쪽을 알려 줍니다.",
        "책갈피는 방금 읽은 쪽이 아니라 다음에 펼칠 쪽에 꽂습니다. 번호는 예시입니다."),
    "l26-ack-next-number": ("ACK 번호는 다음 순서번호",
        "순서번호 999부터 1003이 한 줄로 있습니다. 클라이언트가 SYN 1000을 보내면 SYN이 한 자리를 차지하고, 서버는 다음에 받고 싶은 1001을 ACK로 알려 줍니다.",
        "ACK 번호는 방금 받은 번호가 아니라 다음에 받고 싶은 순서번호입니다. 번호는 예시입니다.", 1),
    "l26-daily-numbers-call": ("여보세요, 번호를 서로 알려 줘요",
        "나와 가게가 번호를 주고받습니다. 내가 번호 1000을 말하고, 가게가 1001을 기다리며 자기 번호 4000을 알리고, 내가 4000을 잘 들었다며 다음 4001을 말하면 양쪽이 서로의 번호를 알게 됩니다.",
        "세 마디가 오가면 양쪽이 서로의 시작 번호를 알고 확인합니다. 1000과 4000은 예시입니다."),
    "l26-daily-text-length-limit": ("한 통에 보낼 수 있는 길이",
        "나와 친구가 각자 “나한테는 한 통에 70자 이하로”, “나한테는 60자 이하로” 하고 알립니다. 긴 내용은 상대가 정한 길이에 맞춰 나눠 보내며 방향마다 길이가 달라도 됩니다.",
        "문자는 상대가 알린 길이에 맞춰 나눠 보냅니다. 70자와 60자는 예시입니다."),
    "l26-mss-exchange": ("MSS는 한 세그먼트의 데이터 크기",
        "클라이언트가 SYN에 MSS 1460을, 서버가 SYN+ACK에 MSS 1400을 담아 알립니다. 각자 상대가 알린 MSS 이하로 데이터를 나눠 보내며 방향마다 값이 달라도 됩니다.",
        "MSS는 한 TCP 세그먼트에 실을 수 있는 TCP 데이터의 최대 크기입니다. 1460과 1400은 예시입니다.", 1),
    "l26-daily-call-states": ("전화 상태가 바뀌어요",
        "가게는 벨 기다림 상태이고, 내가 걸면 나는 거는 중, 가게는 벨 울림이 됩니다. “들려요”를 받은 내가 먼저 통화 중이 되고 마지막 대답이 닿으면 가게도 통화 중이 됩니다.",
        "받는 쪽은 마지막 대답이 닿은 뒤에 통화 중이 됩니다."),
    "l26-daily-no-new-wire": ("통화 중은 새 전선이 아니에요",
        "나와 친구 사이에 여러 기지국이 있습니다. 양쪽이 통화 중이라고 기록하지만 새 전용선은 깔리지 않고 목소리는 이미 있는 통신망을 지나가며, 통화 중이라는 것이 용건 처리를 뜻하지는 않는다고 표시됩니다.",
        "통화 중은 새 전선이 아니라 양쪽이 기록해 둔 상태입니다."),
    "l26-virtual-circuit": ("TCP 연결은 논리적인 관계예요",
        "클라이언트와 서버 사이에 여러 라우터가 있습니다. 양 끝은 ESTABLISHED 상태와 상대 주소·포트, 순서번호, MSS를 기록하지만 새 케이블이나 전용선은 생기지 않고, 데이터는 기존 네트워크로 갑니다. 연결 수립이 앱의 처리 성공을 뜻하지는 않습니다.",
        "TCP 연결은 양 끝이 상태를 기록해 둔 논리적 관계입니다. 연결이 수립되었다고 앱이 데이터를 처리했다는 뜻은 아닙니다.", 1),
}

OLD = {
    "l26-three-way-handshake": ("SYN, SYN+ACK, ACK로 시작하는 TCP 연결",
        "클라이언트가 SYN과 순서번호 1000을 보내고, 서버가 SYN+ACK로 순서번호 4000과 확인 번호 1001을 돌려주며, 클라이언트가 확인 번호 4001의 ACK를 보내 양쪽이 서로의 시작 번호를 확인하는 과정입니다.",
        "첫 메시지는 연결을 요청하고, 두 번째는 요청을 확인하면서 서버의 시작 번호를 알리며, 세 번째는 그 번호를 확인합니다."),
    "l26-tcp-states": ("연결 상태가 바뀌는 순서",
        "서버는 LISTEN에서 시작하고, 클라이언트가 SYN을 보내면 SYN_SENT, 서버는 SYN_RECEIVED가 됩니다. 클라이언트는 SYN+ACK를 받고 먼저 ESTABLISHED가 되며 서버는 마지막 ACK가 닿은 뒤 ESTABLISHED가 됩니다.",
        "클라이언트는 SYN_SENT에서 ESTABLISHED로, 서버는 LISTEN과 SYN_RECEIVED를 거쳐 ESTABLISHED로 바뀝니다."),
}


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        daily_fn = fn if fn.__code__.co_argcount == 0 else (lambda f=fn: f(True))
        write(OUT, dn, daily_fn())
        items = [(dn, *COPY[dn], -1)]
        if nn in OLD:
            items.append((nn, *OLD[nn], after))
        else:
            write(OUT, nn, fn(False))
            c = COPY[nn]
            items.append((nn, c[0], c[1], c[2], after))
        pages.append(items)
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
