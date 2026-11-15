#!/usr/bin/env python3
"""Unit 11 Lesson 1 (장치가 트래픽을 다루는 세 가지 구조) SVG review: replaces the old u11-structures-* set.
Run from repo root: python3 scripts/svg_pairs/u11_l01_rev.py   (--svg-only skips the lesson.md edit).

Colour language of this Lesson: Inline = BLUE, Out of path = VIOLET, Proxy = GREEN; ORANGE only marks what just changed.
Running example: 박 팀장 PC 192.168.10.42 / 지우 PC .41 -> 본사 게이트웨이 192.168.10.1 -> 외부 AI 서비스 203.0.113.80:443.
Moving packets are drawn before the device icons so they pass *behind* them."""
import sys
from u11_new_common import *  # noqa: F401,F403
from kit import wire_items
from u6_l03 import arrow

IN, OUT, PX = BLUE, VIOLET, GREEN
FS = 16  # smallest label size


def L(x, y, s, c=MUTED, fs=FS, weight=None):
    return text(x, y, s, fs, c, weight)


def dev2(label, x, y, sub, fn):
    return fn(x, y, label) + L(x, y + 72, sub)


def P(x, y, s, c, filled=False, fs=18, w=None):
    return pill(x, y, s, c, fs, filled, w)


def server(x, y, label="외부 AI 서비스", sub="203.0.113.80:443", c=GREEN):  # shadows the common helper: 16px address line
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, label, 18, TXT, 700) + L(x, y + 84, sub))


def node(x, y, label, sub=None, w=150, h=70, c=BLUE, fs=18):
    s = box(x - w / 2, y - h / 2, w, h, c, PANEL, 12, sw=3) + text(x, y + fs * 0.36, label, fs, c, 700)
    return s + (L(x, y + h / 2 + 24, sub) if sub else "")


def toll(x, y, c=IN):
    return (box(x - 46, y - 50, 92, 100, c, PANEL, 8, sw=3) + f'<rect x="{x - 46}" y="{y - 50}" width="92" height="14" rx="6" fill="{c}"/>'
            + text(x, y + 14, "톨게이트", 17, c, 700))


def camera(x, y, c=OUT):
    return (box(x - 32, y - 20, 64, 40, c, PANEL, 6, sw=3) + f'<circle cx="{x + 8}" cy="{y}" r="11" fill="none" stroke="{c}" stroke-width="3"/>'
            + f'<circle cx="{x + 8}" cy="{y}" r="4" fill="{c}"/><rect x="{x - 25}" y="{y - 12}" width="14" height="8" rx="2" fill="{c}"/>')


def courier(x, y, c=PX):
    return box(x - 55, y - 40, 110, 80, c, PANEL, 12, sw=3) + text(x, y + 7, "심부름꾼", 19, c, 700)


def road(x0=170, x1=800, y=Y, c=LINE):
    return line(x0, y, x1, y, c, 4, "10 8")


# ---------------------------------------------------------------- Page 1 (a): three structures on the road
def p1():
    a = new()
    pkt = lambda s: mv(a, packet(0, 0), [(190, Y), (790, Y)], s, s, s, 0.1, 0.9)
    body = [road(),
            pkt(1), pkt(2), pkt(3),
            mv(a, packet(0, 0), [(190, Y), (640, Y)], 4, 4, 4.5, 0.05, 0.5),
            mv(a, packet(0, 0, GREEN), [(700, Y), (800, Y)], 4, 4.5, 4, 0.55, 0.95),
            dev2("박 팀장 PC", 100, Y, "192.168.10.42", laptop), server(860, Y, "외부 AI 서비스", "203.0.113.80:443"),
            a.vis(P(215, 215, "시안 설명문, 다듬어 줘", BLUE), 1, 1), mark(a, 48, 264, 104, 62, 1),
            a.vis(toll(290, Y) + P(290, 205, "Inline · 경로 위", IN, True), 2, 4), mark(a, 244, 250, 92, 100, 2),
            a.vis(line(480, 224, 480, 288, OUT, 3, "6 6") + f'<circle cx="480" cy="{Y}" r="12" fill="{OUT}"/>' + camera(480, 200), 3, 4),
            a.vis(P(480, 150, "Out of path · 경로 옆", OUT, True), 3, 4), mark(a, 448, 180, 64, 40, 3),
            a.vis(courier(670, Y) + P(670, 205, "Proxy · 대신 연결", PX, True), 4, 4), mark(a, 615, 260, 110, 80, 4)]
    caps = ["박 팀장의 AI 요청은 길을 따라 서비스로 가요", "길 위에서 모두 세워 확인하면 Inline이에요", "길 옆에서 복사본만 보면 Out of path예요", "대신 연결해 다녀오면 Proxy예요"]
    return frame(a, "장치가 길에서 일하는 세 가지 방식", "박 팀장의 AI 요청이 지나가는 길이에요", caps, "".join(body))


# ---------------------------------------------------------------- Page 1 (b): five memos -> three structures
MEMOS = ["회사에서만 AI 사이트가 안 열려요", "고객 도면을 AI에 붙여넣으면요?", "누가 어떤 AI를 쓰는지 알 수 있어요?",
         "이 AI 플러그인이 뭘 보내는지 알아요?", "AI 서버를 밖에 열어 두면 안전해요?"]


def p1b():
    a = new()

    def chip(i, c=None):
        y = 128 + i * 68
        col = c or MUTED
        return (box(40, y, 480, 52, col, PANEL, 10, sw=3)
                + f'<circle cx="68" cy="{y + 26}" r="14" fill="{col}"/>' + text(68, y + 32, str(i + 1), 17, BG, 700)
                + text(92, y + 33, MEMOS[i], 18, TXT, None, "start"))

    def legend(k, name, sub, c):
        y = 140 + k * 104
        return box(560, y, 360, 84, c, PANEL, 12, sw=3) + text(740, y + 36, name, 24, c, 700) + text(740, y + 64, sub, 17, MUTED)

    for m in MEMOS:
        assert tw(m, 18) <= 410, m
    grp = {0: IN, 2: OUT, 1: PX, 3: PX, 4: PX}
    body = [a.vis("".join(chip(i) for i in range(5)), 1, 1),
            a.vis(chip(0, IN) + "".join(chip(i) for i in (1, 2, 3, 4)), 2, 2),
            a.vis(chip(0, IN) + chip(2, OUT) + "".join(chip(i) for i in (1, 3, 4)), 3, 3),
            a.vis("".join(chip(i, grp[i]) for i in range(5)), 4, 4),
            a.vis(box(560, 150, 360, 250, LINE, PANEL, 14, dash=True) + text(740, 250, "경로의 어디에 붙나?", 26, TXT, 700)
                  + text(740, 292, "이 기준 하나로 나눠 봐요", 18, MUTED) + text(740, 334, "(장비 이름은 잠시 잊어요)", 17, MUTED), 1, 1),
            a.vis(legend(0, "Inline", "경로 위 · Lesson 11-2", IN), 2, 4), mark(a, 560, 140, 360, 84, 2), mark(a, 40, 128, 480, 52, 2),
            a.vis(legend(1, "Out of path", "경로 옆 복사본 · Lesson 11-3", OUT), 3, 4), mark(a, 560, 244, 360, 84, 3), mark(a, 40, 264, 480, 52, 3),
            a.vis(legend(2, "Proxy", "대신 연결 · Lesson 11-4 이후", PX), 4, 4), mark(a, 560, 348, 360, 84, 4),
            mark(a, 40, 196, 480, 52, 4), mark(a, 40, 332, 480, 52, 4), mark(a, 40, 400, 480, 52, 4)]
    caps = ["지우의 모니터에 고민 메모 다섯 장이 붙었어요", "길 위에서 막는 문제는 Inline이에요", "복사본으로 지켜보는 문제는 Out of path예요", "나머지는 Proxy예요. 서버 앞에는 Inline도 써요"]
    return frame(a, "고민 메모 다섯 장을 세 갈래로", "장비 이름 대신 붙는 자리로 나눠요", caps, "".join(body))


# ---------------------------------------------------------------- Page 2: Inline passes or drops
def p2():
    a = new()
    gw = lambda c=IN, label="본사 게이트웨이": node(480, Y, label, "192.168.10.1", 200, 80, c)
    body = [line(150, 215, 380, 280, LINE, 4, "10 8"), line(150, 385, 380, 320, LINE, 4, "10 8"), line(580, Y, 800, Y, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(190, 222), (430, 284)], 1, 1, 1.5, 0.05, 0.45), mv(a, packet(0, 0), [(190, 378), (430, 316)], 1, 1, 1.5, 0.05, 0.45),
            mv(a, packet(0, 0), [(530, Y), (790, Y)], 1, 1.5, 1, 0.55, 0.95),
            mv(a, packet(0, 0), [(190, 378), (340, 322)], 3, 3, 3, 0.1, 0.6),
            dev2("지우 PC", 100, 215, "192.168.10.41", pc), dev2("박 팀장 PC", 100, 385, "192.168.10.42", pc), server(850, Y, "외부 AI 서비스", "203.0.113.80:443"),
            a.vis(gw(), 1, 3), a.vis(gw(MUTED, "게이트웨이 꺼짐"), 4, 4),
            a.vis(P(480, 190, "모든 요청이 게이트웨이를 지나요", IN), 1, 1), mark(a, 380, 260, 200, 80, 1),
            a.vis(P(480, 205, "목적지 203.0.113.80 → Drop", RED, True), 2, 3), mark(a, 380, 260, 200, 80, 2),
            a.vis(cross(398, 262), 3, 3),
            a.vis(cross(690, Y) + P(480, 205, "꺼지면 통신도 끊겨요", IN, True), 4, 4), mark(a, 380, 260, 200, 80, 4)]
    caps = ["지우 PC도 박 팀장 PC도 게이트웨이를 지나요", "지나가는 길에 차단 규칙을 걸어요", "규칙에 맞는 패킷은 그 자리에서 버려져요", "꺼지면 통신도 끊기는 장치가 Inline이에요"]
    return frame(a, "길 한가운데서 막는 장치", "Inline은 지나가는 패킷을 직접 처리해요", caps, "".join(body))


# ---------------------------------------------------------------- Page 3: Out of path copies
def p3():
    a = new()
    pkt = lambda s: mv(a, packet(0, 0), [(190, Y), (790, Y)], s, s, s, 0.1, 0.9)
    dot = f'<circle cx="290" cy="{Y}" r="12" fill="{OUT}"/>'
    body = [road(),
            mv(a, packet(0, 0, OUT), [(290, 296), (290, 252)], 2, 2, 2, 0.3, 0.8),
            pkt(1), pkt(2), pkt(3), pkt(4),
            dev2("박 팀장 PC", 100, Y, "192.168.10.42", laptop), node(530, Y, "출구 장치", "192.168.10.1", 150, 70, IN), server(860, Y, "외부 AI 서비스", "203.0.113.80:443"),
            a.vis(P(480, 170, "서 이사: 업무는 멈추지 않게 보고만 싶어요", BLUE), 1, 1), mark(a, 48, 264, 104, 62, 1),
            a.vis(dot + line(290, 224, 290, 288, OUT, 3, "6 6") + camera(290, 195), 2, 3),
            a.vis(L(290, 345, "Tapping Point", OUT, 16, 700) + P(380, 255, "복사본", OUT, True, 16), 2, 2), mark(a, 258, 280, 64, 40, 2),
            a.vis(L(290, 162, "센서", OUT, 17, 700), 2, 3),
            a.vis(box(400, 160, 360, 72, OUT, PANEL, 10, sw=3) + L(580, 190, "192.168.10.42 → 203.0.113.80", TXT, 17, 700) + L(580, 216, "센서가 복사본으로 만든 기록", MUTED, 16), 3, 3),
            mark(a, 400, 160, 360, 72, 3),
            a.vis(dot + line(290, 224, 290, 288, MUTED, 3, "6 6") + camera(290, 195, MUTED) + L(290, 162, "센서 꺼짐", MUTED, 17, 700), 4, 4), mark(a, 258, 175, 64, 40, 4),
            a.vis(check(860, 235) + P(540, 430, "원래 통신은 그대로 도착해요", GREEN, False), 4, 4)]
    caps = ["박 팀장의 요청은 평소처럼 서비스로 가요", "길 옆 Tapping Point가 복사본을 센서로 보내요", "센서는 복사본으로 누가 어디 갔는지 알아내요", "센서가 꺼져도 통신은 그대로, 막지는 못해요"]
    return frame(a, "길 옆에서 복사본만 보는 장치", "Out of path는 통신에 손대지 않고 지켜봐요", caps, "".join(body))


# ---------------------------------------------------------------- Page 4 (a): Proxy = two connections + Stream
def p4():
    a = new()
    px = lambda: node(480, Y, "프록시", "192.168.10.5:8080", 150, 80, PX)
    cells = "".join(f'<rect x="{230 + i * 36}" y="396" width="30" height="26" rx="4" fill="none" stroke="{OUT}" stroke-width="3"/>' for i in range(6))
    body = [dev2("박 팀장 PC", 100, Y, "192.168.10.42", pc), px(), server(860, Y, "외부 AI 서비스", "203.0.113.80:443"),
            a.vis(doc(100, 215) + text(128, 221, "고객 도면", 16, TXT, 700, "start"), 1, 1),
            a.vis(P(480, 160, "서 이사: 도면을 AI에 올리면 어떡하죠?", BLUE), 1, 1), mark(a, 84, 195, 32, 40, 1),
            a.vis(line(170, Y, 405, Y, PX, 5) + P(290, 262, "연결 ①", PX, True, 17), 2, 4), mark(a, 247, 246, 86, 33, 2),
            a.vis(line(555, Y, 810, Y, PX, 5) + P(680, 262, "연결 ②", PX, True, 17), 3, 4), mark(a, 637, 246, 86, 33, 3),
            a.vis(cells + f'<rect x="496" y="396" width="200" height="26" rx="4" fill="{OUT}"/>' + arrow(448, 486, 409, MUTED, 3)
                  + L(463, 456, "조각난 패킷을 이어 붙인 Stream을 읽어요", TXT, 17, 700), 4, 4), mark(a, 230, 396, 466, 26, 4)]
    body += [mv(a, packet(0, 0), [(200, Y), (380, Y)], 2, 2, 2, 0.1, 0.7), mv(a, packet(0, 0, GREEN), [(590, Y), (770, Y)], 3, 3, 3, 0.1, 0.7)]
    caps = ["고객 도면 파일을 AI에 올리려는 상황이에요", "먼저 PC와 프록시 사이에 연결 ①을 맺어요", "프록시가 서비스와 연결 ②를 따로 맺어요", "프록시는 이어진 Stream으로 내용을 읽어요"]
    return frame(a, "대신 접속해 주는 프록시", "양쪽과 따로 연결을 맺는 대리인이에요", caps, "".join(body))


# ---------------------------------------------------------------- Page 4 (b): HTTPS needs CA + TLS inspection
def p4b():
    a = new()
    cipher = lambda: "".join(cell(315 + i * 56, 385, 50, 34, s, MUTED, 17) for i, s in enumerate(["7#", "q9", "$k", "Zx", "@2", "m!"]))
    plain = lambda: "".join(cell(315 + i * 56, 385, 50, 34, s, OUT, 17) for i, s in enumerate(["P", "O", "S", "T", "", "/"]))
    body = [line(170, Y, 405, Y, PX, 5), line(555, Y, 810, Y, PX, 5), lock(290, 250, MUTED),
            dev2("박 팀장 PC", 100, Y, "192.168.10.42", laptop), node(480, Y, "프록시", "192.168.10.5:8080", 150, 80, PX), server(860, Y, "외부 AI 서비스", "203.0.113.80:443"),
            a.vis(P(480, 165, "AI 서비스는 HTTPS를 써요", BLUE), 1, 1), mark(a, 270, 236, 40, 46, 1),
            a.vis(cipher() + cross(700, 402) + L(480, 450, "프록시가 읽은 바이트는 암호문이에요", TXT, 17, 700), 1, 2),
            a.vis(P(100, 215, "회사 CA 설치", BLUE, True), 2, 4), mark(a, 30, 198, 140, 34, 2),
            a.vis(P(480, 215, "TLS 검사 설정", PX, True), 3, 4), mark(a, 390, 198, 180, 34, 3),
            a.vis(plain() + check(700, 402) + L(480, 450, "프록시가 내용을 읽을 수 있어요", TXT, 17, 700), 3, 4), mark(a, 315, 385, 330, 34, 3),
            a.vis(P(480, 165, "두 설정이 모두 있어야 읽혀요", GREEN, True), 4, 4)]
    caps = ["HTTPS라 프록시를 지나는 바이트는 암호문이에요", "PC에 회사 CA를 깔아도 아직 읽을 수 없어요", "프록시에 TLS 검사 설정을 켜면 읽혀요", "중계하는 연결에서 두 설정이 있을 때만 읽어요"]
    return frame(a, "HTTPS는 설정이 있어야 읽혀요", "프록시가 암호문을 읽는 조건이에요", caps, "".join(body))


# ---------------------------------------------------------------- Page 5: 송장(header) vs 편지(content)
def p5():
    a = new()
    card = (box(300, 128, 360, 228, LINE, PANEL, 12, sw=3))

    def part(y, h, c, name, l1, l2):
        return (box(312, y, 336, h, c, BG, 8, sw=3) + L(480, y + 30, name, c, 17, 700) + L(480, y + 58, l1, TXT, 17) + L(480, y + 84, l2, TXT, 17))

    top = lambda c: part(140, 100, c, "송장 · 패킷 헤더", "보내는 곳 192.168.10.42", "받는 곳 203.0.113.80:443")
    bot = lambda c: part(248, 100, c, "편지 · HTTP 내용", "요청한 URL", "올린 본문")
    dev_l = box(40, 150, 200, 76, IN, PANEL, 12, sw=3) + text(140, 182, "패킷을 보는 장치", 18, IN, 700) + text(140, 208, "Inline · Out of path", 16, MUTED)
    dev_r = box(720, 252, 200, 76, PX, PANEL, 12, sw=3) + text(820, 284, "Proxy", 20, PX, 700) + text(820, 310, "소켓 Stream", 16, MUTED)
    body = [card, top(MUTED), bot(MUTED),
            a.vis(P(480, 410, "서 이사: 이 플러그인이 어디로, 뭘 보내요?", BLUE), 1, 1), mark(a, 300, 128, 360, 228, 1),
            a.vis(top(IN) + dev_l + arrow(240, 300, 188, IN, 4) + check(270, 150) + L(140, 258, "어느 주소·포트로 가나", TXT, 17, 700), 2, 4), mark(a, 312, 140, 336, 100, 2),
            a.vis(bot(PX) + dev_r + arrow(720, 660, 290, PX, 4) + check(690, 252) + L(820, 360, "어떤 URL·본문을 보냈나", TXT, 17, 700), 3, 4), mark(a, 312, 248, 336, 100, 3),
            a.vis(P(480, 410, "알고 싶은 층에 맞는 장치를 골라요", GREEN, True), 4, 4)]
    caps = ["플러그인의 요청은 송장과 편지로 이뤄져요", "주소와 포트는 송장만 봐도 알 수 있어요", "URL과 본문은 편지를 열어야 알 수 있어요", "알고 싶은 층에 맞춰 장치를 골라요"]
    return frame(a, "패킷을 볼까, 대화를 볼까?", "송장만 읽을지, 편지까지 읽을지 정해요", caps, "".join(body))


# ---------------------------------------------------------------- Page 6: one box, three structures
def p6():
    a = new()
    rows = [("외부 사이트 차단", "Inline", "패킷 헤더", IN), ("접속 기록", "관찰 (Out of path 식)", "패킷", OUT), ("웹 필터링", "Proxy", "소켓 Stream (HTTP)", PX)]
    ys = [215, 293, 371]
    for r in rows:
        assert tw(r[1], 18) <= 250 and tw(r[2], 18) <= 210, r
    frame_box = box(50, 115, 860, 335, GREEN, PANEL, 16, sw=3)
    body = [frame_box + text(80, 150, "새 보안 장비 한 대", 20, TXT, 700, "start"),
            L(205, 200, "기능", MUTED, 17), L(495, 200, "어떤 구조?", MUTED, 17), L(775, 200, "무엇을 보나?", MUTED, 17)]
    for (f, s, u, c), y in zip(rows, ys):
        body.append(cell(80, y, 250, 56, f, TXT, 19, BG))
        body.append(box(360, y, 270, 56, LINE, BG, 6, dash=True, sw=2) + text(495, y + 36, "?", 22, MUTED, 700))
    body += [a.vis("".join(cell(360, y, 270, 56, s, c, 18) for (f, s, u, c), y in zip(rows, ys)), 2, 4), mark(a, 360, 215, 270, 212, 2),
             a.vis("".join(cell(660, y, 230, 56, u, c, 18) for (f, s, u, c), y in zip(rows, ys)), 3, 4), mark(a, 660, 215, 230, 212, 3),
             a.vis(f'<rect x="50" y="165" width="860" height="285" rx="16" fill="{BG}" fill-opacity="0.6"/>' + box(50, 115, 860, 335, RED, "none", 16, sw=4)
                   + P(480, 150, "상자가 멈추면 세 기능이 한꺼번에 멈춰요", RED, True), 4, 4)]
    caps = ["설명서에 기능 세 가지가 한 줄에 적혀 있어요", "기능마다 붙는 자리가 달라 구조도 달라요", "구조에 따라 보는 단위도 달라요", "다만 한 상자가 멈추면 기능이 모두 멈춰요"]
    return frame(a, "한 상자 안의 세 구조", "구조는 상자가 아니라 기능마다 따져요", caps, "".join(body))


PAGES = [
    ("u11-l01-p01-three-structures", "장치가 길에서 일하는 세 가지 방식",
     "박 팀장의 AI 요청이 길을 따라 서비스로 가는 중에, 길 위의 톨게이트는 Inline, 길 옆 감시카메라는 Out of path, 대신 다녀오는 심부름꾼은 Proxy라는 그림입니다.",
     "요청이 지나는 길 위, 옆, 대신 연결 세 자리로 구조를 나눕니다.", 3, p1),
    ("u11-l01-p01b-five-memos", "고민 메모 다섯 장을 세 갈래로",
     "지우의 고민 메모 다섯 장이 길 위의 Inline, 경로 옆 복사본의 Out of path, 대신 연결하는 Proxy 세 갈래로 나뉘는 그림입니다.",
     "메모마다 붙는 자리를 정하면 풀 장치가 보입니다.", 5, p1b),
    ("u11-l01-p02-inline-drop", "길 한가운데서 막는 장치",
     "지우 PC와 박 팀장 PC의 요청이 모두 본사 게이트웨이를 지나고, 목적지 203.0.113.80에 Drop 규칙을 걸면 그 자리에서 버려지며, 게이트웨이가 꺼지면 통신도 끊기는 그림입니다.",
     "Inline 장치는 지나가는 패킷을 통과시키거나 버리고, 꺼지면 통신도 끊깁니다.", 2, p2),
    ("u11-l01-p03-out-of-path-copy", "길 옆에서 복사본만 보는 장치",
     "Tapping Point가 복사본을 센서로 보내 센서가 누가 어디로 갔는지 기록하고, 센서가 꺼져도 원래 통신은 서비스에 그대로 도착하는 그림입니다.",
     "Out of path 센서는 복사본만 보므로 꺼져도 통신은 이어지지만 막지는 못합니다.", 3, p3),
    ("u11-l01-p04-proxy-two-connections", "대신 접속해 주는 프록시",
     "박 팀장 PC와 프록시, 프록시와 AI 서비스 사이에 연결을 따로 맺고, 프록시가 조각난 패킷을 이어 붙인 Stream으로 도면 내용을 읽는 그림입니다.",
     "프록시는 연결을 두 번 맺고 이어진 Stream으로 내용을 읽습니다.", 2, p4),
    ("u11-l01-p04b-https-ca", "HTTPS는 설정이 있어야 읽혀요",
     "HTTPS라 프록시가 읽은 바이트는 암호문이고, 회사 CA를 깔아도 아직 읽히지 않으며, 프록시에 TLS 검사 설정을 켜야 내용이 읽히는 그림입니다.",
     "프록시도 회사 CA 설치와 TLS 검사 설정이 있어야 HTTPS 내용을 읽습니다.", 3, p4b),
    ("u11-l01-p05-header-vs-content", "패킷을 볼까, 대화를 볼까?",
     "패킷 장치는 송장에 해당하는 헤더에서 주소와 포트를, Proxy는 편지에 해당하는 내용에서 URL과 본문을 읽으며, 알고 싶은 층에 맞는 장치를 고른다는 그림입니다.",
     "송장(헤더)만 읽을지 편지(내용)까지 읽을지에 따라 장치를 고릅니다.", 2, p5),
    ("u11-l01-p06-one-box-three", "한 상자 안의 세 구조",
     "새 보안 장비 한 대의 외부 사이트 차단은 Inline, 접속 기록은 관찰, 웹 필터링은 Proxy이고, 한 상자가 멈추면 세 기능이 모두 멈추는 그림입니다.",
     "구조는 상자가 아니라 기능마다 따지고, 한 상자에 모으면 멈출 때도 함께 멈춥니다.", 3, p6),
]
# lesson.md wiring: Page index -> [PAGES indices]
WIRING = [[0, 1], [2], [3], [4, 5], [6], [7]]

if __name__ == "__main__":
    d = lesson_dir(1)
    out = d / "assets" / "animations"
    for stem, *_r, fn in PAGES:
        write(out, stem, fn())
    if "--svg-only" not in sys.argv:
        pages = [[(PAGES[i][0], PAGES[i][1], PAGES[i][2], PAGES[i][3], PAGES[i][4]) for i in grp] for grp in WIRING]
        wire_items(d / "lesson.md", pages)
    print("ok", len(PAGES), "svgs", d.name)
