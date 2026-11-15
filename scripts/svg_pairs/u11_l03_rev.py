#!/usr/bin/env python3
"""Unit 11 Lesson 3 (경로 밖 관찰과 DPI) SVG review: new example SVGs for Pages 2-7 (Page 1 is kept).
Run from repo root: python3 scripts/svg_pairs/u11_l03_rev.py   (--svg-only skips the lesson.md edit).
One running example: 지우 PC 192.168.10.41 / 박 팀장 PC 192.168.10.42 → 코어 스위치 → 게이트웨이 192.168.10.1 → 인터넷,
옆에 센서 192.168.10.250. 4 steps: ① 상황 → ② 동작 → ③ 결과(✓/✗) → ④ 기억할 점; 방금 바뀐 요소만 주황 테두리."""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u11_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"
BLUEF = BLUE


def pcx(x, y, name, ip):
    return laptop(x, y, name) + lbl(x, y + 72, ip, MUTED, 16)


def gwx(x, y):
    return router(x, y, "게이트웨이") + lbl(x, y + 72, "192.168.10.1", MUTED, 16)


def sensor_icon(x, y, label="센서 192.168.10.250"):
    return eye(x, y) + lbl(x, y + 50, label, TXT, 16, 700)


def arrow(x0, y0, x1, y1, c=LINE, w=4, dash=None):
    """Line with a small arrowhead at (x1, y1)."""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    bx, by = x1 - ux * 14, y1 - uy * 14
    head = f'<polygon points="{x1:.0f},{y1:.0f} {bx - uy * 8:.0f},{by + ux * 8:.0f} {bx + uy * 8:.0f},{by - ux * 8:.0f}" fill="{c}"/>'
    return f'<line x1="{x0}" y1="{y0}" x2="{bx + ux * 2:.0f}" y2="{by + uy * 2:.0f}" stroke="{c}" stroke-width="{w}"{d}/>' + head


def tag(x, y, s, c=VIOLET):
    """Small packet with a 3-letter tag inside (e.g. RST)."""
    return (f'<rect x="{x - 30}" y="{y - 15}" width="60" height="30" rx="6" fill="{c}"/>' + text(x, y + 6, s, 17, BG, 700))


def tap_dot(x, y):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{VIOLET}"/>'


# ---------------------------------------------------------------------------------
# Page 2 · 포트 미러링과 TAP
def p2():
    a = new()
    Y2 = 230
    base = [line(155, Y2, 236, Y2, LINE, 4, "10 8"), line(344, Y2, 630, Y2, LINE, 4, "10 8"), line(690, Y2, 780, Y2, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, Y2), (610, Y2)], 1, 1, 1, 0.1, 0.9),
            mv(a, packet(0, 0), [(290, Y2), (610, Y2)], 3, 3, 3, 0.1, 0.9),
            mv(a, packet(0, 0, VIOLET), [(290, 296), (290, 400), (348, 400)], 3, 3, 3, 0.1, 0.9),
            pcx(100, Y2, "지우 PC", "192.168.10.41"), switch(290, Y2, "코어 스위치"), gwx(660, Y2), cloud(850, Y2),
            sensor_icon(400, 400)]
    mirror = line(290, 282, 290, 400, VIOLET, 3, "6 6") + line(290, 400, 372, 400, VIOLET, 3, "6 6")
    tapfig = (line(475, 250, 475, 322, VIOLET, 3, "6 6") + line(400, 322, 570, 322, VIOLET, 3, "6 6")
              + line(400, 322, 400, 372, VIOLET, 3, "6 6") + line(570, 322, 570, 374, VIOLET, 3, "6 6")
              + box(437, 210, 76, 40, GREEN, PANEL, 8, sw=3) + text(475, 236, "TAP", 18, GREEN, 700)
              + box(495, 376, 150, 48, MUTED, PANEL, 10, sw=2) + text(570, 406, "다른 장비", 16, TXT, 700))
    body = base + [
        a.vis(mirror, 2, 3), a.vis(pill(290, 165, "게이트웨이 쪽 포트를 복사 대상으로", VIOLET, 17, False, 330), 2, 2),
        mark(a, 238, 214, 104, 32, 2),
        a.vis(check(470, 400) + pill(480, 165, "원본도 복사본도 도착해요", GREEN, 17, False, 280), 3, 3), mark(a, 372, 378, 56, 44, 3),
        a.vis(tapfig + pill(480, 165, "복사 전용 장비 TAP", GREEN, 17, False, 220), 4, 4), mark(a, 437, 210, 76, 40, 4)]
    caps = ["지우 PC의 통신이 코어 스위치로 들어와요", "스위치에서 게이트웨이 쪽 포트를 복사 대상으로 정해요",
            "원본은 게이트웨이로, 복사본은 센서로 가요", "TAP은 회선에 끼워 복사본을 여러 곳에 나눠 줘요"]
    return frame(a, "복사본 만드는 두 방법", "포트 미러링은 스위치가, TAP은 전용 장비가 해요", caps, "".join(body))


# Page 2 · 복사 지점의 위치
def card(x, y, w, h, title, rows, c):
    s = box(x, y, w, h, c, PANEL, 10, sw=3) + text(x + w / 2, y + 26, title, 16, c, 700)
    for i, r in enumerate(rows):
        s += text(x + w / 2, y + 52 + i * 25, r, 16, TXT)
    return s


def p2b():
    a = new()
    Y2 = 225
    body = [line(152, 160, 224, 214, LINE, 4, "10 8"), line(152, 300, 224, 240, LINE, 4, "10 8"),
            line(322, Y2, 492, Y2, LINE, 4, "10 8"), line(548, Y2, 730, Y2, LINE, 4, "10 8"),
            pcx(100, 150, "지우 PC", "192.168.10.41"), pcx(100, 300, "박 팀장 PC", "192.168.10.42"),
            switch(270, Y2, "코어 스위치"), gwx(520, Y2), cloud(800, Y2), pill(520, 160, "주소 변환(NAT)", BLUE, 16, False, 170),
            a.vis(tap_dot(400, Y2) + line(400, 237, 400, 334, VIOLET, 3, "6 6") + card(285, 334, 230, 84, "게이트웨이 안쪽 복사", ["출발지 192.168.10.41", "출발지 192.168.10.42"], VIOLET), 2, 4),
            mark(a, 285, 334, 230, 84, 2), a.vis(check(515, 334), 2, 4),
            a.vis(tap_dot(650, Y2) + line(650, 237, 650, 334, VIOLET, 3, "6 6") + card(535, 334, 230, 84, "게이트웨이 바깥 복사", ["출발지 198.51.100.25", "출발지 198.51.100.25"], VIOLET), 3, 4),
            mark(a, 535, 334, 230, 84, 3), a.vis(cross(765, 334), 3, 4),
            a.vis(pill(480, 452, "알고 싶은 것에 맞춰 복사 지점을 정해요", GREEN, 18, True, 400), 4, 4)]
    caps = ["두 PC의 통신이 코어 스위치와 게이트웨이를 지나가요", "안쪽에서 복사하면 PC마다 주소가 달라요",
            "바깥에서 복사하면 모두 본사 공인 주소로 보여요", "무엇을 알고 싶은지에 맞춰 복사 지점을 정해요"]
    return frame(a, "복사 지점에 따라 보이는 주소", "같은 통신도 어디서 복사하느냐에 따라 달라요", caps, "".join(body))


# ---------------------------------------------------------------------------------
# Page 3 · 발견했는데 왜 못 막았을까
def p3():
    a = new()
    Y3 = 225
    base = [line(152, Y3, 238, Y3, LINE, 4, "10 8"), line(342, Y3, 492, Y3, LINE, 4, "10 8"), line(548, Y3, 816, Y3, LINE, 4, "10 8"),
            line(290, 282, 290, 374, VIOLET, 3, "6 6"),
            mv(a, packet(0, 0), [(170, Y3), (455, Y3)], 1, 1, 1, 0.1, 0.9),
            mv(a, packet(0, 0), [(290, Y3), (750, Y3)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, VIOLET), [(290, 300), (290, 350)], 2, 2, 2, 0.1, 0.9),
            pcx(100, Y3, "박 팀장 PC", "192.168.10.42"), switch(290, Y3, "코어 스위치"), gwx(520, Y3),
            server(850, Y3, "피싱 사이트", None, RED), sensor_icon(290, 400)]
    body = base + [
        mark(a, 264, 376, 52, 48, 2),
        a.vis(packet(750, Y3), 3, 3),
        a.vis(pill(470, 400, "위험 주소 경보!", ORANGE, 17, True, 190) + pill(770, 160, "원본은 이미 도착", RED, 17, False, 190) + cross(890, 160), 3, 3),
        mark(a, 366, 380, 208, 40, 3),
        a.vis(line(335, 400, 520, 400, BLUE, 3, "6 6") + line(520, 400, 520, 316, BLUE, 3, "6 6")
              + pill(520, 160, "차단 규칙에 위험 주소 추가", BLUE, 17, False, 300) + packet(440, Y3, RED) + cross(440, 266), 4, 4),
        mark(a, 492, 197, 56, 56, 4)]
    caps = ["박 팀장 PC가 피싱 사이트에 접속해요", "원본은 사이트로 곧장 가고, 복사본은 센서로 가요",
            "센서가 경보를 울릴 때는 원본이 이미 도착했어요", "다음부터 막으려면 경로 안 차단 규칙에 넣어요"]
    return frame(a, "봤는데 왜 못 막았을까", "센서는 읽기만 하고 막는 일은 경로 안이 해요", caps, "".join(body))


# Page 3 · RST 끼어들기
def p3b():
    a = new()
    Y3 = 225
    ok = line(152, Y3, 816, Y3, GREEN, 5)
    body = [a.vis(ok, 1, 2), a.vis(ok, 4, 4), a.vis(line(152, Y3, 816, Y3, RED, 5, "10 10"), 3, 3),
            line(480, 237, 480, 366, VIOLET, 3, "6 6"),
            mv(a, tag(0, 0, "RST"), [(470, 335), (230, 270)], 2, 2, 3, 0.1, 0.45),
            mv(a, packet(0, 0), [(780, Y3), (215, Y3)], 2, 2, 2, 0.1, 0.95),
            pcx(100, Y3, "박 팀장 PC", "192.168.10.42"), server(850, Y3, "피싱 사이트", None, RED), tap_dot(480, Y3),
            sensor_icon(480, 395, "센서"),
            a.vis(pill(480, 150, "RST = 연결을 끊으라는 신호", ORANGE, 18, False, 330), 1, 1),
            a.vis(pill(480, 150, "서버인 척 보낸 가짜 RST", VIOLET, 18, False, 300), 2, 2), mark(a, 198, 254, 64, 32, 2),
            a.vis(check(560, 395) + pill(480, 150, "가짜가 먼저 오면 연결이 끊겨요", GREEN, 18, False, 340), 3, 3), mark(a, 454, 380, 52, 30, 3),
            a.vis(packet(215, Y3), 4, 4),
            a.vis(cross(560, 395) + pill(480, 150, "진짜 응답이 먼저면 실패해요", RED, 18, False, 320), 4, 4), mark(a, 190, 200, 52, 52, 4)]
    caps = ["센서가 가짜 RST로 연결을 끊어 보려 해요", "센서가 서버인 척 RST를 보내고, 진짜 응답도 달려와요",
            "가짜 RST가 먼저 오면 연결이 끊겨요", "진짜 응답이 먼저 오면 실패해요. 이길 보장이 없어요"]
    return frame(a, "경로 밖에서 끊어 보기", "복사본만 받는 센서가 끼어드는 방법이에요", caps, "".join(body))


# ---------------------------------------------------------------------------------
# Page 4 · 송장과 내용물, DPI
def p4():
    a = new()
    hx, hw, px, pw, py, ph = 300, 220, 530, 260, 190, 120
    head = box(hx, py, hw, ph, BLUE, PANEL, 10, sw=3) + text(hx + hw / 2, py + 52, "송장", 24, BLUE, 700) + text(hx + hw / 2, py + 84, "IP·TCP 헤더", 17, MUTED)
    pay_box = box(px, py, pw, ph, ORANGE, PANEL, 10, sw=3)
    pay_txt = text(px + pw / 2, py + 52, "내용물", 24, ORANGE, 700) + text(px + pw / 2, py + 84, "Payload (HTTP 요청 등)", 17, MUTED)
    body = [head, pay_box, a.vis(pay_txt, 1, 3),
            sensor_icon(150, 250, "센서") + line(190, 250, 296, 250, VIOLET, 3, "6 6"),
            a.vis(pill(545, 160, "패킷 하나 = 송장 + 내용물", TXT, 18, False, 300), 1, 1),
            a.vis(box(hx - 4, py - 4, hw + 8, ph + 8, GREEN, "none", 12, sw=5) + pill(410, 350, "얕은 검사: 송장까지만", GREEN, 17, False, 230) + check(520, py - 4), 2, 2),
            a.vis(box(hx - 8, py - 8, hw + pw + 26, ph + 16, VIOLET, "none", 14, sw=5) + pill(545, 350, "DPI: Payload 안까지 분석", VIOLET, 17, True, 290), 3, 3),
            a.vis(lock(px + pw / 2, py + 40, ORANGE) + text(px + pw / 2, py + 100, "암호화된 Payload", 17, ORANGE, 700)
                  + cross(px + pw - 6, py + 6) + pill(545, 350, "TLS 암호는 열쇠 없이 못 읽어요", ORANGE, 17, False, 330), 4, 4),
            mark(a, px, py, pw, ph, 4)]
    caps = ["패킷은 송장(헤더)과 내용물(Payload)로 이뤄져 있어요", "주소·포트만 보는 얕은 검사는 송장까지 읽어요",
            "DPI는 송장을 넘어 Payload 안까지 분석해요", "TLS로 암호화된 Payload는 센서가 읽지 못해요"]
    return frame(a, "송장과 내용물, DPI", "센서는 복사본의 어디까지 읽을까요", caps, "".join(body))


# Page 4 · HTTPS에서 센서가 보는 것
def p4b():
    a = new()
    rows = [("주소·포트·시각·전송량", "누가 언제 어디로 얼마나", "보인다", GREEN),
            ("SNI (서버 이름)", "어느 서비스 쪽인지 단서", "평문일 때만 보여요", ORANGE),
            ("질문 내용 (Payload)", "알 수 없다", "TLS면 안 보여요", RED)]
    ry = [284, 342, 400]
    body = [line(150, 165, 800, 165, LINE, 4, "10 8"), line(480, 177, 480, 205, VIOLET, 3, "6 6"),
            pcx(90, 165, "지우 PC", "192.168.10.41"), server(850, 165, "외부 AI 서비스", "203.0.113.80:443"),
            tap_dot(480, 165), eye(480, 222) + lbl(540, 228, "센서", TXT, 16, 700)]
    for i, (name, mid, chip, c) in enumerate(rows):
        y = ry[i]
        body.append(box(50, y, 860, 50, LINE, PANEL, 10, sw=2) + text(70, y + 32, name, 18, TXT, 700, "start"))
        body.append(a.vis(ask(850, y + 25), 1, 1))
        body.append(a.vis(text(350, y + 31, mid, 17, MUTED, None, "start") + pill(770, y + 25, chip, c, 17, False, 230), i + 2, 4))
        body.append(mark(a, 50, y, 860, 50, i + 2))
    caps = ["지우 PC의 HTTPS 통신 복사본을 센서가 받아요", "주소·포트·시각·전송량은 헤더에서 그대로 보여요",
            "서버 이름(SNI)은 평문으로 보낼 때만 단서가 돼요", "TLS로 암호화된 질문 내용은 읽을 수 없어요"]
    return frame(a, "HTTPS에서 센서가 보는 것", "보이는 것과 안 보이는 것을 나눠 봐요", caps, "".join(body))


# ---------------------------------------------------------------------------------
# Page 5 · 다 저장하면 생기는 일
def p5():
    a = new()
    body = [line(155, 190, 790, 190, LINE, 4, "10 8"), laptop(100, 190, "직원 PC"), cloud(860, 190),
            pill(300, 190, "업무 통신", BLUE, 17, True, 130), pill(500, 190, "사적 통신", VIOLET, 17, True, 130),
            lbl(500, 232, "병원 예약 · 은행 알림", MUTED, 15),
            tap_dot(400, 190) + line(400, 202, 400, 300, VIOLET, 3, "6 6") + sensor_icon(400, 325, "센서"),
            mark(a, 560, 268, 330, 150, 2), mark(a, 560, 268, 330, 150, 4),
            box(560, 268, 330, 150, LINE, PANEL, 12, sw=3) + text(725, 300, "센서 저장소", 18, TXT, 700),
            a.vis(line(430, 325, 556, 325, ORANGE, 3, "6 6") + pill(725, 345, "업무 통신", BLUE, 16, False, 190) + pill(725, 390, "사적 통신", VIOLET, 16, False, 190), 2, 3),
            a.vis(cross(900, 268) + pill(480, 456, "사생활·통신 비밀을 건드려요", RED, 18, False, 320), 3, 3),
            a.vis(line(430, 325, 556, 325, GREEN, 3, "6 6") + pill(725, 360, "주소·SNI·시각·전송량", GREEN, 16, False, 250) + check(900, 268)
                  + pill(480, 456, "무엇을 위해, 어디까지 볼지 먼저 정해요", GREEN, 18, True, 400), 4, 4),
            ]
    caps = ["회선에는 업무 통신과 사적인 통신이 함께 지나가요", "복사본이 오니 통째로 저장하면 어떨까요",
            "사적인 내용까지 모이면 사생활을 건드려요", "필요한 것만 남기도록 범위를 좁혀요"]
    return frame(a, "다 저장하면 생기는 일", "볼 수 있다고 모두 저장해도 되는 건 아니에요", caps, "".join(body))


# Page 5 · 회사 센서와 망중립성
def p5b():
    a = new()
    L, R = 40, 490
    body = [box(L, 125, 430, 290, MUTED, PANEL, 16, sw=2) + text(L + 215, 158, "회사 업무망", 20, TXT, 700),
            box(R, 125, 430, 290, MUTED, PANEL, 16, sw=2) + text(R + 215, 158, "통신사업자 회선", 20, TXT, 700),
            laptop(L + 85, 260, "직원 PC"), line(L + 140, 255, L + 270, 255, VIOLET, 3, "6 6"), eye(L + 320, 255) + lbl(L + 320, 305, "회사 센서", TXT, 16, 700),
            house(R + 90, 260, "통신사업자"), line(R + 150, 255, R + 300, 255, LINE, 4, "10 8"), server(R + 360, 255, "AI 서비스"),
            a.vis(pill(480, 450, "DPI 같은 내용 검사 기술은 두 논의에 모두 나와요", BLUE, 17, False, 500), 1, 1),
            a.vis(pill(L + 215, 380, "사내 규정과 동의의 문제", GREEN, 17, False, 260), 2, 4), mark(a, L, 125, 430, 290, 2),
            a.vis(pill(R + 215, 380, "특정 서비스 차별 = 망중립성", ORANGE, 17, False, 300) + cross(R + 300, 215), 3, 4), mark(a, R, 125, 430, 290, 3),
            a.vis(pill(480, 450, "서로 다른 논의라서 구별해서 따져요", GREEN, 18, True, 360), 4, 4)]
    caps = ["내용을 깊이 보는 기술은 두 논의에 모두 등장해요", "회사 업무망에서 직원 통신을 보는 일은 사내 규정과 동의의 문제예요",
            "사업자가 특정 서비스만 차별하는 일은 망중립성이에요", "헷갈리기 쉬우니 두 논의를 구별해요"]
    return frame(a, "회사 센서와 망중립성", "두 이야기는 서로 다른 논의예요", caps, "".join(body))


# ---------------------------------------------------------------------------------
# Page 6 · 관찰용 포트가 넘칠 때
def p6():
    a = new()
    Y6 = 250
    pipe = box(470, 238, 280, 24, VIOLET, PANEL, 12, sw=2)
    rec = "".join(box(770 + i * 22, 330, 16, 26, GREEN if i not in (2, 4) else RED, PANEL if i in (2, 4) else GREEN, 3, sw=2) for i in range(6))
    body = [pipe, a.vis(f'<rect x="472" y="240" width="276" height="20" rx="10" fill="{VIOLET}" fill-opacity="0.55"/>', 3, 3),
            arrow(340, 222, 180, 222, MUTED, 4), arrow(180, 278, 340, 278, MUTED, 4),
            mv(a, packet(0, 0), [(300, 222), (215, 222)], 1, 1, 1, 0.1, 0.9),
            mv(a, packet(0, 0, VIOLET), [(400, Y6), (540, Y6)], 2, 2, 2, 0.05, 0.5),
            mv(a, packet(0, 0, VIOLET), [(400, Y6), (600, Y6)], 2, 2, 2, 0.4, 0.9),
            mv(a, packet(0, 0, RED), [(600, 262), (600, 345)], 3, 3, 3, 0.1, 0.8),
            mv(a, packet(0, 0, RED), [(680, 262), (680, 345)], 3, 3, 3, 0.3, 0.95),
            router(100, Y6, "게이트웨이") + lbl(100, 322, "192.168.10.1", MUTED, 16),
            switch(400, Y6, "코어 스위치"), eye(830, Y6),
            lbl(255, 192, "보내기 1Gbps", TXT, 16, 700), lbl(255, 316, "받기 1Gbps", TXT, 16, 700),
            lbl(610, 228, "관찰용 포트 1Gbps", TXT, 16, 700), lbl(830, 292, "센서", TXT, 16, 700),
            a.vis(pill(610, 170, "양방향을 합쳐 최대 2Gbps", ORANGE, 17, False, 280), 2, 2), mark(a, 470, 238, 280, 24, 2),
            a.vis(cross(640, 380) + pill(610, 430, "넘친 만큼 스위치에서 버려져요", RED, 17, False, 300), 3, 3), mark(a, 470, 238, 280, 24, 3),
            a.vis(rec + lbl(830, 380, "센서 기록에 빈틈", RED, 16, 700) + check(150, 222) + pill(430, 440, "원본은 그대로, 비는 건 센서 기록뿐", GREEN, 17, False, 380), 4, 4),
            mark(a, 770, 330, 126, 26, 4)]
    caps = ["회선의 보내기·받기 통신이 스위치를 지나가요", "양방향 복사를 합치면 최대 2Gbps가 한 포트로 몰려요",
            "1Gbps 포트가 넘치면 스위치가 그만큼 버려요", "원본 통신은 그대로이고 센서 기록만 비어요"]
    return frame(a, "관찰용 포트가 넘칠 때", "복사본이 몰리면 센서까지 오지 못해요", caps, "".join(body))


# Page 6 · 센서 안의 병목
def p6b():
    a = new()
    bx = [56, 282, 508, 734]
    names = [("NIC", "받기"), ("메모리 버퍼", "잠시 담기"), ("캡처·CPU", "분석"), ("디스크", "기록")]
    body = [mv(a, packet(0, 0, VIOLET), [(40, 275), (930, 275)], 1, 1, 1, 0.1, 0.9)]
    for x, (n, sub) in zip(bx, names):
        body.append(box(x, 230, 170, 90, BLUE, PANEL, 12, sw=3) + text(x + 85, 281, n, 19, BLUE, 700) + lbl(x + 85, 346, sub, MUTED, 16))
    body += [arrow(bx[i] + 172, 275, bx[i] + 224, 275, MUTED, 4) for i in range(3)]
    body.append(lbl(480, 165, "센서(192.168.10.250) 안에서 패킷이 지나가는 길", MUTED, 18))
    msgs = ["", "순간적으로 몰리면 버퍼가 넘쳐요", "분석이 밀리면 패킷을 버려요", "쓰기가 못 따라오면 기록이 끊겨요"]
    for s in (2, 3, 4):
        x = bx[s - 1]
        inner = cross(x + 160, 230) + pill(x + 85 if s < 4 else 770, 385, msgs[s - 1], RED, 16, False, 270)
        if s == 4:
            inner += pill(480, 440, "1Gbps ≈ 초당 약 125MB가 쌓여요", ORANGE, 18, False, 340)
        body.append(mark(a, x, 230, 170, 90, s))
        body.append(a.vis(inner, s, s))
    caps = ["센서 안에서 패킷은 네 단계를 차례로 지나가요", "버퍼 단계가 넘치면 패킷이 버려져요",
            "분석이 밀리는 단계에서도 패킷이 버려져요", "디스크 쓰기가 느려도 기록이 끊겨요"]
    return frame(a, "센서 안에서 기록이 비는 곳", "어느 단계든 느리면 빈틈이 생겨요", caps, "".join(body))


# ---------------------------------------------------------------------------------
# Page 7 · 막을까, 지켜볼까
def p7():
    a = new()
    px, pw, ph = 50, 380, 52
    reqs = [(190, "① 랜섬웨어 주소 즉시 차단"), (290, "② AI 서비스 사용 통계"), (390, "③ 사고 증거 찾기")]
    top = box(590, 140, 320, 120, BLUE, PANEL, 12, sw=3) + text(750, 176, "Inline · 경로 안", 20, BLUE, 700) \
        + lbl(750, 206, "게이트웨이 192.168.10.1", TXT, 16) + lbl(750, 232, "차단 규칙으로 바로 막아요", MUTED, 16)
    bot = box(590, 300, 320, 120, VIOLET, PANEL, 12, sw=3) + text(750, 336, "Out of path · 경로 밖", 20, VIOLET, 700) \
        + lbl(750, 366, "센서 192.168.10.250", TXT, 16) + lbl(750, 392, "복사본을 모아 분석해요", MUTED, 16)
    body = [top, bot]
    for i, (y, t) in enumerate(reqs):
        body.append(box(px, y - ph / 2, pw, ph, MUTED, PANEL, 26, sw=2) + text(px + pw / 2, y + 7, t, 18, TXT, 700))
    body += [a.vis(arrow(435, 190, 585, 200, BLUE, 4) + check(910, 140), 2, 4), mark(a, px, 190 - 26, pw, ph, 2),
             a.vis(arrow(435, 290, 585, 345, VIOLET, 4) + check(910, 300), 3, 4), mark(a, px, 290 - 26, pw, ph, 3),
             a.vis(arrow(435, 390, 585, 385, VIOLET, 4) + pill(750, 450, "누락이 없게 여유를 둬요", VIOLET, 17, False, 260), 4, 4), mark(a, px, 390 - 26, pw, ph, 4)]
    caps = ["서 이사의 요청 세 가지를 어디서 처리할까요?", "원본을 즉시 막아야 하니 경로 안에서 처리해요",
            "통계는 원본에 손댈 필요가 없어 센서가 맡아요", "증거도 센서로 하되 누락이 없게 여유를 둬요"]
    return frame(a, "요청마다 알맞은 자리", "막을지 지켜볼지는 요청이 정해요", caps, "".join(body))


# (page_id, stem, title, alt, caption, after_paragraph, fn) in display order per Page; Page 1 is kept as is.
PAGES = {
    "advanced-source-05-page-02": [
        ("u11-l03-p02-mirroring-tap", "복사본 만드는 두 방법",
         "지우 PC의 통신 중 게이트웨이 쪽 포트를 스위치가 복사해 원본은 게이트웨이로, 복사본은 센서로 보내고, TAP은 회선에 끼워 복사본을 여러 장비에 나눠 주는 모습입니다.",
         "포트 미러링은 스위치가, TAP은 복사 전용 장비가 복사본을 만듭니다.", 2, p2),
        ("u11-l03-p02b-copy-point", "복사 지점에 따라 보이는 주소",
         "게이트웨이 안쪽에서 복사하면 PC마다 다른 사설 주소가 보이고, 바깥에서 복사하면 모두 본사 공인 주소 198.51.100.25로 보이는 모습입니다.",
         "복사 지점은 알고 싶은 것에 맞춰 정합니다.", 4, p2b)],
    "advanced-source-05-page-03": [
        ("u11-l03-p03-read-only-gap", "봤는데 왜 못 막았을까",
         "박 팀장 PC의 원본은 피싱 사이트로 곧장 가고 복사본만 센서로 가서, 센서가 경보를 울릴 때는 이미 도착해 있으므로 위험 주소를 경로 안 차단 규칙에 넣어야 막는다는 그림입니다.",
         "센서는 발견하고, 막는 일은 경로 안 차단 규칙이 합니다.", 3, p3),
        ("u11-l03-p03b-rst-race", "경로 밖에서 끊어 보기",
         "센서가 서버인 척 보낸 가짜 RST가 진짜 응답보다 먼저 도착하면 연결이 끊기지만, 진짜 응답이 먼저 오면 실패하는 모습입니다.",
         "RST 끼어들기는 이길 보장이 없는 보조 수단입니다.", 4, p3b)],
    "advanced-source-05-page-06": [
        ("u11-l03-p04-dpi-payload", "송장과 내용물, DPI",
         "패킷을 송장(헤더)과 내용물(Payload)로 나누어, 주소·포트만 보는 얕은 검사와 Payload 안까지 보는 DPI를 견주고, TLS로 암호화된 Payload는 센서가 읽지 못한다는 그림입니다.",
         "DPI는 Payload까지 보지만 TLS 암호는 열쇠 없이 못 읽습니다.", 3, p4),
        ("u11-l03-p04b-https-view", "HTTPS에서 센서가 보는 것",
         "센서는 헤더의 주소·포트·시각·전송량은 보고, SNI 서버 이름은 평문일 때만 보며, TLS로 암호화된 질문 내용은 읽지 못한다는 그림입니다.",
         "센서가 알 수 있는 것은 누가 언제 어디로 얼마나까지입니다.", 4, p4b)],
    "advanced-source-05-page-07": [
        ("u11-l03-p05-save-everything", "다 저장하면 생기는 일",
         "업무 통신과 사적인 통신이 함께 지나가는 회선의 복사본을 통째로 저장하면 사생활을 건드리므로, 주소·SNI·시각·전송량처럼 필요한 것만 남기도록 범위를 좁히는 모습입니다.",
         "볼 수 있다고 모두 저장하지 않고 필요한 것만 남깁니다.", 1, p5),
        ("u11-l03-p05b-net-neutral", "회사 센서와 망중립성",
         "회사 업무망에서 직원 통신을 보는 일은 사내 규정과 동의의 문제이고, 사업자가 특정 서비스를 차별하는 일은 망중립성이라는 별개의 논의라는 그림입니다.",
         "회사 센서의 수집과 사업자의 서비스 차별은 서로 다른 논의입니다.", 2, p5b)],
    "advanced-source-05-page-08": [
        ("u11-l03-p06-port-overflow", "관찰용 포트가 넘칠 때",
         "보내기·받기 양방향을 합친 최대 2Gbps의 복사본이 1Gbps 관찰용 포트로 몰리면 넘친 만큼 스위치에서 버려져 센서 기록에만 빈틈이 생기고 원본 통신은 그대로라는 그림입니다.",
         "복사본이 관찰용 포트를 넘치면 센서 기록만 비고 원본은 영향이 없습니다.", 1, p6),
        ("u11-l03-p06b-sensor-stages", "센서 안에서 기록이 비는 곳",
         "센서 안에서 NIC, 메모리 버퍼, 캡처·CPU, 디스크 어느 단계가 느려도 패킷이 버려지거나 기록이 끊기며, 1Gbps는 초당 약 125MB라는 점을 보여 줍니다.",
         "NIC에서 디스크까지 어느 한 단계만 느려도 기록에 빈틈이 생깁니다.", 3, p6b)],
    "advanced-source-05-page-10": [
        ("u11-l03-p07-request-split", "요청마다 알맞은 자리",
         "랜섬웨어 주소 즉시 차단은 경로 안 게이트웨이 규칙에, AI 서비스 사용 통계와 사고 증거 찾기는 경로 밖 센서에 맡기고 증거는 누락이 없게 여유를 두는 그림입니다.",
         "요청마다 원본에 개입해야 하는지, 누락을 허용하는지로 자리를 나눕니다.", 2, p7)],
}


def wire(items_by_page):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = LESSON / "lesson.md"
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    lines, out, i = fm.split("\n"), [], 0
    done = set()
    while i < len(lines):
        l = lines[i]
        out.append(l)
        i += 1
        if l.startswith("- page_id: ") and l[len("- page_id: "):] in items_by_page:
            pid = l[len("- page_id: "):]
            done.add(pid)
            out.append("  illustrations:")
            for stem, t, al, c, ap, _fn in items_by_page[pid]:
                out += [f"  - file: assets/animations/{stem}.svg", f"    title: {q(t)}", f"    alt: {q(al)}",
                        f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            if i < len(lines) and lines[i] == "  illustrations:":
                i += 1
                while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                    i += 1
    assert done == set(items_by_page), set(items_by_page) - done
    md.write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for items in PAGES.values():
        for stem, *_r, fn in items:
            write(OUT, stem, fn())
            n += 1
    if "--svg-only" not in sys.argv:
        wire(PAGES)
    print("ok", n, "svgs", LESSON.name)
