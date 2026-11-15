#!/usr/bin/env python3
"""Unit 11 Lesson 4 (포워드 프록시와 접속 정책): reviewed 4-step SVGs, one running example.
Run from repo root: python3 scripts/svg_pairs/u11_l04_rev.py   (--svg-only skips lesson.md edit).
Page 2 (u11-l04-p02-browser-proxy.svg, from u11_l04_new_scenes.py) is kept as is.
주소: 지우 PC 192.168.10.41, 박 팀장 PC 192.168.10.42, 게이트웨이 192.168.10.1, 프록시 192.168.10.5:8080,
AI 서비스 203.0.113.80:443, 본사 공인 주소 198.51.100.25."""
import sys
from u11_new_common import *  # noqa: F401,F403

PX, PIP = "프록시", "192.168.10.5"
SUBC = MUTED


def sub(x, y, s, c=SUBC, fs=16):
    return text(x, y, s, fs, c)


def nd(x, y, label, s=None, w=150, h=70, c=BLUE, fs=18):
    out = box(x - w / 2, y - h / 2, w, h, c, PANEL, 12, sw=3) + text(x, y + fs * 0.36, label, fs, c, 700)
    return out + (sub(x, y + h / 2 + 22, s) if s else "")


def sv(x, y, label="AI 서비스", s=None, c=GREEN):
    return server(x, y, label, None, c) + (sub(x, y + 84, s) if s else "")


def lap(x, y, c=BLUE):
    return laptop(x, y, None, c)


def tgl(x, y, on):
    c = GREEN if on else LINE
    kx = x + 12 if on else x - 12
    return (f'<rect x="{x - 24}" y="{y - 12}" width="48" height="24" rx="12" fill="{c}" fill-opacity="{0.9 if on else 0.6}"/>'
            f'<circle cx="{kx}" cy="{y}" r="9" fill="{TXT}"/>')


def panel(x, y, w, h, title, rows, c=BLUE, rc=TXT, fs=17):
    s = box(x, y, w, h, c, PANEL, 10, sw=2) + text(x + 14, y + 26, title, 17, c, 700, "start")
    for i, r in enumerate(rows):
        s += text(x + 14, y + 56 + i * 26, r, fs, rc, None, "start")
    return s


# ---------------------------------------------------------------- Page 1
def p1():
    a = new()
    ys = (190, 290, 390)
    pcs = "".join(lap(100, y) for y in ys) + text(100, 440, "직원 PC 40대", 18, TXT, 700)
    gw, pr, ai = (480, 400), (480, 190), (840, 290)
    direct = "".join(line(160, y, 405, gw[1], LINE, 3, "8 6") for y in ys) + line(555, 400, 795, 312, LINE, 3, "8 6")
    solid = "".join(line(160, y, 405, gw[1], BLUE, 4) for y in ys) + line(555, 400, 795, 312, BLUE, 4)
    toproxy = "".join(line(160, y, 405, pr[1], BLUE, 4) for y in ys)
    body = [pcs, sv(*ai, s="203.0.113.80"), nd(*gw, "게이트웨이", "192.168.10.1", c=MUTED),
            a.vis(solid, 1, 1), a.vis(direct, 2, 4),
            a.vis(nd(*pr, PX, PIP + ":8080") + toproxy, 2, 4), mark(a, 405, 155, 150, 70, 2),
            mv(a, packet(0, 0), [(175, 290), (395, 195)], 2, 2, 2, 0.1, 0.9),
            a.vis(line(555, 190, 795, 268, ORANGE, 12) + line(555, 190, 795, 268, GREEN, 4), 3, 3), a.vis(line(555, 190, 795, 268, GREEN, 4), 4, 4),
            mv(a, packet(0, 0, GREEN), [(575, 197), (775, 262)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(825, 212, "요청한 상대: 프록시", ORANGE, 18, True, 200), 4, 4), mark(a, 725, 195, 200, 34, 4)]
    caps = ["지금은 PC마다 게이트웨이를 지나 바로 나가요", "PC가 요청을 프록시에 맡겨요", "프록시가 AI 서비스에 새로 연결해요", "AI 서비스가 보는 상대는 PC가 아니라 프록시예요"]
    return frame(a, "PC가 요청을 프록시에 맡겨요", "한결디자인 PC 40대가 AI 서비스를 쓰는 모습이에요", caps, "".join(body))


def p1b():
    a = new()
    rows = [("캐시", 238), ("접근 정책", 276), ("접속 기록", 314), ("내용 검사", 352)]
    inner = box(330, 165, 300, 225, BLUE, PANEL, 12, sw=3) + text(480, 198, f"{PX} {PIP}:8080", 18, BLUE, 700)
    inner += "".join(text(365, y + 6, n, 17, TXT, 700, "start") for n, y in rows)
    off = "".join(tgl(580, y, False) for n, y in rows if n not in ("접근 정책", "접속 기록"))
    body = [inner, lap(110, 290) + text(110, 340, "PC", 18, TXT, 700), sv(850, 290, s="203.0.113.80"),
            line(165, 290, 330, 290, BLUE, 4), line(630, 290, 815, 290, LINE, 4), off,
            a.vis(tgl(580, 276, False), 1, 3), a.vis(tgl(580, 276, True), 4, 4),
            a.vis(tgl(580, 314, False), 1, 2), a.vis(tgl(580, 314, True), 3, 4),
            mv(a, packet(0, 0), [(175, 290), (320, 290)], 2, 2, 2, 0.05, 0.4),
            mv(a, packet(0, 0, GREEN), [(640, 290), (790, 290)], 2, 2, 2, 0.55, 0.95),
            a.vis(line(630, 290, 815, 290, GREEN, 4), 2, 3), a.vis(check(850, 225), 2, 3),
            a.vis(pill(480, 438, "기록도 차단도 없이 전달만 해요", GREEN, 18, False, 340), 2, 2),
            a.vis(pill(480, 438, "접속 기록이 한 줄 남아요", GREEN, 18, True, 280), 3, 3), mark(a, 350, 295, 270, 38, 3),
            a.vis(cross(722, 290) + pill(480, 438, "접근 정책을 켜면 요청을 막을 수 있어요", ORANGE, 18, False, 440), 4, 4), mark(a, 350, 257, 270, 38, 4)]
    caps = ["프록시를 막 설치하면 기능은 모두 꺼져 있어요", "요청은 기록 없이 그대로 전달돼요", "접속 기록을 켜면 한 줄씩 남아요", "접근 정책을 켜면 요청을 막을 수 있어요"]
    return frame(a, "기능은 설정한 만큼만 생겨요", "기본은 대신 연결, 나머지는 켜야 생겨요", caps, "".join(body))


# ---------------------------------------------------------------- Page 3
def p3():
    a = new()
    pc_, pr, ai = (110, 300), (480, 300), (860, 300)
    body = [lap(*pc_) + text(110, 350, "박 팀장 PC", 18, TXT, 700) + sub(110, 372, "192.168.10.42"),
            nd(*pr, PX, PIP, w=130), sv(*ai, s="203.0.113.80"),
            line(165, 300, 415, 300, BLUE, 4),
            a.vis(line(545, 300, 815, 300, LINE, 3, "10 8"), 1, 1), a.vis(line(545, 300, 815, 300, GREEN, 4), 2, 4),
            a.vis(pill(290, 245, "① PC ↔ 프록시", BLUE, 17, False, 190), 1, 4), mark(a, 165, 285, 250, 30, 1),
            a.vis(pill(680, 245, "② 프록시 ↔ AI 서비스", GREEN, 17, False, 230), 2, 4), mark(a, 545, 285, 270, 30, 2),
            a.vis(sub(290, 340, "프록시의 서버 측 소켓"), 1, 3), a.vis(sub(680, 340, "프록시의 클라이언트 측 소켓"), 2, 3),
            a.vis(sub(290, 340, "도착지 192.168.10.5:8080") + sub(680, 340, "도착지 203.0.113.80:443"), 4, 4),
            mv(a, packet(0, 0), [(180, 300), (385, 300)], 3, 3, 3, 0.05, 0.4), mv(a, packet(0, 0), [(575, 300), (790, 300)], 3, 3, 3, 0.55, 0.95),
            mark(a, 415, 262, 130, 76, 3),
            a.vis(pill(480, 430, "두 연결은 서로 독립이에요", ORANGE, 20, True, 320), 4, 4)]
    caps = ["PC가 프록시와 연결을 하나 맺어요", "프록시가 AI 서비스와 따로 연결을 맺어요", "한쪽에서 받은 흐름을 다른 쪽에 이어 써요", "출발지와 도착지가 다른 독립된 연결 둘이에요"]
    return frame(a, "프록시에는 연결이 두 개예요", "박 팀장 PC가 프록시를 거쳐 AI 서비스에 접속해요", caps, "".join(body))


def chain(a, ox, tag):
    """Mini chain PC -①- 프록시 -②- 서버 at x offset ox (y=260)."""
    return (lap(ox + 60, 270, MUTED) + nd(ox + 220, 260, PX, None, 100, 56)
            + server(ox + 380, 260, "AI 서비스", None) + line(ox + 112, 260, ox + 170, 260, BLUE, 4)
            + line(ox + 270, 260, ox + 345, 260, GREEN, 4))


def p3b():
    a = new()
    L, R = 40, 500
    heads = [text(L + 220, 150, "① 구간이 끊기면", 21, BLUE, 700), text(R + 220, 150, "② 구간이 끊기면", 21, GREEN, 700)]
    body = heads + [chain(a, L, 0), chain(a, R, 1),
                    text(L + 141, 222, "①", 20, BLUE, 700), text(R + 141, 222, "①", 20, BLUE, 700),
                    text(L + 307, 222, "②", 20, GREEN, 700), text(R + 307, 222, "②", 20, GREEN, 700),
                    a.vis(cross(L + 141, 260), 2, 4), mark(a, L + 112, 236, 58, 48, 2),
                    a.vis(box(L + 20, 380, 400, 60, RED, PANEL, 10, sw=2) + text(L + 220, 408, "브라우저가 프록시에 닿지 못해요", 18, RED, 700)
                          + text(L + 220, 430, "\"프록시 서버에 연결할 수 없다\"", 16, MUTED), 2, 3),
                    a.vis(cross(R + 307, 260), 3, 4), mark(a, R + 270, 236, 75, 48, 3),
                    a.vis(box(R + 20, 380, 400, 60, ORANGE, PANEL, 10, sw=2) + text(R + 220, 408, "프록시가 504 오류를 만들어 돌려줘요", 18, ORANGE, 700)
                          + text(R + 220, 430, "\"다음 서버 응답을 기다리다 시간 초과\"", 16, MUTED), 3, 3),
                    a.vis(pill(480, 400, "프록시 기록에 요청이 있으면 ①은 정상이에요", GREEN, 19, True, 520) + pill(480, 445, "그다음 ② 구간을 확인해요", BLUE, 18, False, 300), 4, 4)]
    caps = ["프록시 앞뒤로 연결 두 개가 있어요", "① 구간이 끊기면 프록시에 닿지 못해요", "② 구간이 끊기면 프록시가 504를 돌려줘요", "프록시 기록에 요청이 있으면 ②를 의심해요"]
    return frame(a, "어느 구간이 문제일까?", "끊긴 구간에 따라 오류의 모양이 달라요", caps, "".join(body))


# ---------------------------------------------------------------- Page 4
def p4():
    a = new()
    ys = 330

    def bubble(s, c, fs):
        return (box(700, 150, 240, 70, c, PANEL, 10, sw=3) + text(820, 176, "AI 서비스에 보이는 주소", 16, MUTED)
                + text(820, 206, s, fs, c, 700) + line(870, 220, 870, 288, c, 3))
    body = [lap(90, ys) + text(90, ys + 50, "박 팀장 PC", 18, TXT, 700) + sub(90, ys + 72, "192.168.10.42"),
            nd(470, ys, "경계 장비", "공인 주소 198.51.100.25", w=130, c=MUTED, fs=17), sv(870, ys, s=None),
            line(145, ys, 405, ys, BLUE, 4), line(535, ys, 835, ys, BLUE, 4),
            a.vis(nd(260, ys, PX, PIP, w=120), 2, 2), mark(a, 200, ys - 35, 120, 70, 2),
            a.vis(nd(680, ys, "해외 프록시", None, w=140, c=ORANGE, fs=17), 3, 4),
            a.vis(bubble("198.51.100.25", GREEN, 24), 1, 2), mark(a, 700, 150, 240, 70, 1),
            a.vis(bubble("해외 프록시 서버의 주소", ORANGE, 19), 3, 4),
            a.vis(pill(480, 450, "주소가 바뀌어도 로그인하면 누구인지 알아요", BLUE, 18, True, 450), 4, 4), mark(a, 255, 431, 450, 38, 4)]
    caps = ["직접 접속하면 본사 공인 주소가 보여요", "회사 프록시를 거쳐도 같은 주소가 보여요", "해외 프록시를 거치면 그 서버 주소가 보여요", "주소가 바뀐다고 신원이 숨는 건 아니에요"]
    return frame(a, "AI 서비스에 보이는 주소는?", "접속 방법마다 AI 서비스가 보는 주소를 비교해요", caps, "".join(body))


def p4b():
    a = new()
    ys, y0 = (200, 305, 410), 315
    names = [("지우 PC", "192.168.10.41"), ("박 팀장 PC", "192.168.10.42"), ("다른 직원 PC", None)]
    left = ""
    for y, (n, ip) in zip(ys, names):
        left += lap(75, y) + text(130, y - 2 if ip else y + 6, n, 17, TXT, 700, "start") + (text(130, y + 20, ip, 16, MUTED, None, "start") if ip else "")
        left += line(265, y, 375, y0, BLUE, 3)
    body = [left, nd(440, y0, PX, None, w=130), nd(620, y0, "경계 장비", None, w=120, c=MUTED, fs=17), sv(860, y0, s=None),
            line(505, y0, 560, y0, BLUE, 4), line(680, y0, 825, y0, BLUE, 4),
            a.vis(panel(680, 120, 250, 118, "AI 서비스 기록", ["198.51.100.25"] * 3, ORANGE, ORANGE) + line(860, 238, 860, 272, ORANGE, 3), 2, 4),
            mark(a, 680, 120, 250, 118, 2),
            a.vis(panel(330, 120, 250, 118, "회사 프록시 기록", ["192.168.10.41", "192.168.10.42", "다른 직원 PC"], GREEN) + line(440, 238, 440, 278, GREEN, 3), 3, 4),
            mark(a, 330, 120, 250, 118, 3),
            a.vis(pill(600, 450, "어느 PC인지는 회사 프록시 기록에서 찾아요", GREEN, 18, True, 450), 4, 4)]
    caps = ["직원 PC 여러 대가 회사 프록시를 거쳐 AI 서비스를 써요", "AI 서비스 기록에는 모두 같은 주소로 남아요", "회사 프록시 기록에는 PC별로 구분돼요", "그래서 어느 PC인지는 회사 기록에서 찾아요"]
    return frame(a, "어느 PC가 보냈는지는?", "직원 모두가 같은 회사 프록시를 거쳐 나가요", caps, "".join(body))


# ---------------------------------------------------------------- Page 5
def p5():
    a = new()
    y0 = 340
    body = [lap(100, y0) + text(100, y0 + 50, "박 팀장 PC", 18, TXT, 700), nd(480, y0, "무료 우회 프록시", "운영자를 알 수 없어요", w=190, c=ORANGE, fs=17), sv(860, y0, s=None),
            line(155, y0, 385, y0, BLUE, 4), line(575, y0, 825, y0, BLUE, 4),
            a.vis(panel(300, 118, 360, 150, "운영자가 보는 것", ["출발지 주소 198.51.100.25", "접속 시각", "목적지", "데이터 양"], ORANGE) + line(480, 268, 480, 303, ORANGE, 3), 2, 2),
            mark(a, 300, 118, 360, 150, 2),
            a.vis(lock(480, 185, GREEN) + pill(480, 245, "경고 없는 HTTPS 내용은 못 읽어요", GREEN, 18, False, 380) + line(480, 268, 480, 303, GREEN, 3), 3, 3),
            mark(a, 290, 150, 380, 125, 3),
            a.vis(box(30, 125, 240, 82, RED, PANEL, 10, sw=3) + text(150, 156, "회사 프록시 기록", 17, MUTED) + text(150, 186, "이 접속은 없어요", 20, RED, 700) + cross(235, 150), 4, 4),
            mark(a, 30, 125, 240, 82, 4),
            a.vis(pill(480, 440, "업무 자료가 회사 기록 밖으로 나가요", RED, 18, True, 400), 4, 4)]
    caps = ["박 팀장이 무료 우회 프록시를 거쳐 AI 사이트를 써요", "운영자는 연결 정보를 거의 언제나 알아요", "경고 없이 연결된 HTTPS의 내용은 읽지 못해요", "하지만 회사 기록에는 남지 않아요"]
    return frame(a, "낯선 운영자는 무엇을 볼까?", "무료 우회 프록시를 거치는 접속을 따라가 봐요", caps, "".join(body))


# ---------------------------------------------------------------- Page 6
def p6():
    a = new()
    t, b = 185, 360
    body = [lap(110, t) + text(110, t + 50, "PC", 18, TXT, 700), sv(850, t, s=None), a.vis(lap(110, b) + text(110, b + 50, "PC", 18, TXT, 700) + sv(850, b, s=None), 2, 4),
            line(165, t, 810, t, BLUE, 4), a.vis(pill(480, 150, "한 구간", BLUE, 17, False, 110), 1, 4), mark(a, 165, t - 15, 645, 30, 1),
            mv(a, packet(0, 0), [(175, t), (790, t)], 1, 1, 1, 0.1, 0.9),
            a.vis(line(165, b, 810, b, BLUE, 4) + nd(480, b, PX, None, w=150) + pill(295, 310, "구간 ①", BLUE, 17, False, 120) + pill(665, 310, "구간 ②", GREEN, 17, False, 120), 2, 4),
            mark(a, 405, b - 35, 150, 70, 2),
            a.vis(pill(480, 266, "읽고 · 확인하고 · 기록해요", ORANGE, 17, False, 270), 3, 4), mark(a, 345, 249, 270, 34, 3),
            a.vis("".join(packet(250 + 55 * i, b, VIOLET) for i in range(3)) + pill(480, 448, "사람이 몰리면 대기 시간이 더해져요", RED, 18, True, 400), 4, 4),
            mark(a, 220, b - 20, 175, 40, 4)]
    caps = ["직접 가면 한 구간만 지나요", "프록시를 거치면 구간이 둘로 늘어요", "프록시가 요청을 읽고 확인하고 기록해요", "사람이 몰리면 모든 요청이 더 기다려요"]
    return frame(a, "프록시를 거치면 길이 늘어요", "직접 갈 때와 프록시를 거칠 때를 비교해요", caps, "".join(body))


def p6b():
    a = new()
    ys = (200, 300, 400)
    A, B, ai = (480, 230), (480, 385), (860, 300)
    pcs = "".join(lap(100, y) for y in ys) + text(100, 450, "직원 PC 40대", 18, TXT, 700)
    toA = "".join(line(160, y, 405, A[1], BLUE, 4) for y in ys) + line(555, 230, 815, 285, BLUE, 4)
    toB = "".join(line(160, y, 405, B[1], GREEN, 4) for y in ys) + line(555, 385, 815, 320, GREEN, 4)
    crosses = "".join(cross(205, round(y + (A[1] - y) * 45 / 245)) for y in ys)
    body = [pcs, sv(*ai, s=None), a.vis(toA, 1, 3), a.vis(nd(*A, PX, PIP + ":8080", c=BLUE), 1, 1),
            a.vis(nd(*A, PX, PIP + ":8080", c=RED) + cross(480, 168), 2, 4), mark(a, 405, 195, 150, 70, 2),
            a.vis(crosses, 3, 3), a.vis(pill(480, 450, "사무실 전체의 웹과 AI가 끊겨요", RED, 18, True, 360), 3, 3),
            a.vis(toB + nd(*B, "두 번째 프록시", None, w=170, c=GREEN, fs=17) + check(480, 330), 4, 4), mark(a, 395, 350, 170, 70, 4),
            a.vis(pill(480, 450, "한 대가 멈춰도 다른 한 대가 받아요", GREEN, 18, True, 380), 4, 4)]
    caps = ["모든 요청이 프록시 한 대를 지나가요", "그 프록시가 멈췄어요", "직원들의 웹 요청이 갈 곳을 잃어요", "프록시를 두 대로 두면 한 대가 멈춰도 계속돼요"]
    return frame(a, "프록시가 멈추면 모두 멈춰요", "프록시 한 대에 모두가 기대고 있어요", caps, "".join(body))


SCENES = [
    ("advanced-source-06-page-01", "u11-l04-p1-client-chooses", "PC가 요청을 프록시에 맡겨요",
     "PC 40대가 게이트웨이를 지나 바로 나가던 것을 → PC가 요청을 프록시에 맡기고 → 프록시가 AI 서비스에 새로 연결하며 → AI 서비스가 보는 상대는 프록시라는 것을 보여 줍니다.",
     "클라이언트가 고른 대리자가 대신 연결합니다.", 3, p1),
    ("advanced-source-06-page-01", "u11-l04-p1b-features-on-demand", "기능은 설정한 만큼만 생겨요",
     "막 설치한 프록시는 기능이 모두 꺼져 있어 요청을 그대로 전달하고 → 접속 기록을 켜면 한 줄이 남고 → 접근 정책을 켜면 요청을 막을 수 있습니다.",
     "기본은 대신 연결이고, 기록·차단은 켜야 생깁니다.", 5, p1b),
    ("advanced-source-06-page-06", "u11-l04-p3-two-connections", "프록시에는 연결이 두 개예요",
     "박 팀장 PC와 프록시 사이의 연결 ①, 프록시와 AI 서비스 사이의 연결 ②가 따로 맺어지고 → 프록시가 흐름을 이어 쓰며 → 도착지가 다른 독립된 연결임을 보여 줍니다.",
     "프록시 앞뒤로 서로 독립된 연결이 둘 있습니다.", 3, p3),
    ("advanced-source-06-page-06", "u11-l04-p3b-which-leg", "어느 구간이 문제일까?",
     "① 구간이 끊기면 브라우저가 프록시에 닿지 못하고, ② 구간이 끊기면 프록시가 504 오류를 돌려주며, 프록시 기록에 요청이 있으면 ①은 정상입니다.",
     "프록시 기록에 요청이 있으면 ② 구간을 확인합니다.", 5, p3b),
    ("advanced-source-06-page-02", "u11-l04-p4-seen-address", "AI 서비스에 보이는 주소는?",
     "직접 접속과 회사 프록시 경유는 본사 공인 주소 198.51.100.25로 보이고, 해외 프록시 경유는 그 서버 주소로 보이며, 주소가 바뀌어도 로그인하면 누구인지 압니다.",
     "보이는 주소가 바뀌는 것과 신원이 감춰지는 것은 다릅니다.", 4, p4),
    ("advanced-source-06-page-02", "u11-l04-p4b-who-sent", "어느 PC가 보냈는지는?",
     "직원 PC 여러 대가 회사 프록시를 거치면 AI 서비스 기록에는 모두 같은 주소로 남지만, 회사 프록시 기록에는 PC별로 구분됩니다.",
     "어느 PC가 보냈는지는 회사 프록시 기록에서 찾습니다.", 5, p4b),
    ("advanced-source-06-page-07", "u11-l04-p5-stranger-operator", "낯선 운영자는 무엇을 볼까?",
     "박 팀장이 무료 우회 프록시를 거치면 운영자는 연결 정보를 알고, 경고 없는 HTTPS 내용은 읽지 못하지만, 업무 자료가 회사 기록 밖으로 나가 회사 프록시 기록에는 남지 않습니다.",
     "무료 우회 프록시의 운영자는 낯선 사람입니다.", 4, p5),
    ("advanced-source-06-page-05", "u11-l04-p6-extra-steps", "프록시를 거치면 길이 늘어요",
     "직접 가면 한 구간이지만 프록시를 거치면 두 구간이 되고, 프록시가 읽고 확인하고 기록하는 처리가 더해져 사람이 몰리면 모든 요청이 더 기다립니다.",
     "프록시를 거치면 구간과 처리 단계가 늘어납니다.", 2, p6),
    ("advanced-source-06-page-05", "u11-l04-p6b-spof", "프록시가 멈추면 모두 멈춰요",
     "모든 PC가 프록시 한 대를 지나다가 그 프록시가 멈추면 사무실 전체가 끊기고, 프록시를 두 대로 두면 한 대가 멈춰도 다른 한 대가 요청을 받습니다.",
     "프록시도 단일 장애점이라 두 대로 대비합니다.", 6, p6b),
]


def main(argv):
    d = lesson_dir(4)
    out = d / "assets" / "animations"
    for _p, stem, *_r, fn in SCENES:
        write(out, stem, fn())
    if "--svg-only" in argv:
        return
    by = {}
    for pid, stem, t, al, cap, ap, _ in SCENES:
        by.setdefault(pid, []).append((stem, t, al, cap, ap))
    order = ["advanced-source-06-page-01", "advanced-source-06-page-03", "advanced-source-06-page-06",
             "advanced-source-06-page-02", "advanced-source-06-page-07", "advanced-source-06-page-05"]
    wire_items(d / "lesson.md", [by.get(p) for p in order])
    print("ok", len(SCENES), "svgs", d.name)


if __name__ == "__main__":
    main(sys.argv)
