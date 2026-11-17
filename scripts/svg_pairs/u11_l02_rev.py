#!/usr/bin/env python3
"""Unit 11 Lesson 2 (인라인 구조와 트래픽 처리) SVG review pass: Pages 2-6 (Page 1 kept as is).
Run from repo root: python3 scripts/svg_pairs/u11_l02_rev.py   (--svg-only skips the lesson.md edit).
Running example: 박 팀장 노트북 192.168.10.42 -> 본사 게이트웨이(192.168.10.1 / 198.51.100.25) -> 외부 클라우드 저장소 203.0.113.80."""
import sys
from u11_new_common import *  # noqa: F401,F403

Yc = 300
PH = 34  # pill height at fs 18


def tag(a, x, y, s, c, t, t2=None, w=None, fs=18, filled=False):
    """Step label pill; the orange outline marks it in its first step only."""
    w = w or int(tw(s, fs) + 36)
    h = fs + 16
    return a.vis(pill(x, y, s, c, fs, filled, w), t, t2 or t) + mark(a, x - w / 2, y - h / 2, w, h, t)


def spinner(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="14 14">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 {x} {y}" to="360 {x} {y}" dur="1.5s" repeatCount="indefinite"/></circle>')


# ---- Page 2: 통과시킬까, 버릴까? ----
def p2():
    a = new()
    body = [dev("노트북", 110, Yc, "192.168.10.42", laptop), router(480, Yc, "출구 장치"), server(850, Yc, "클라우드 저장소", "203.0.113.80"),
            line(165, Yc, 445, Yc, LINE, 4, "10 8"), line(515, Yc, 805, Yc, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(190, Yc), (410, Yc)], 1, 1, 2, 0.15, 0.85),
            mark(a, 58, Yc - 38, 104, 66, 1),
            tag(a, 330, 195, "허용한 패킷은 통과", GREEN, 1, w=230), a.vis(pill(630, 195, "차단 대상은 Drop", RED, 18, False, 210), 1, 1),
            a.vis(cross(480, Yc - 52), 2, 4), mark(a, 454, Yc - 26, 52, 52, 2),
            tag(a, 480, 195, "규칙에 걸려 Drop돼요", RED, 2, w=250),
            a.vis(box(35, Yc - 135, 150, 48, ORANGE, PANEL, 24, sw=3) + text(110, Yc - 104, "연결 중…", 18, ORANGE, 700) + spinner(60, Yc - 111), 3, 4),
            mark(a, 35, Yc - 135, 150, 48, 3),
            tag(a, 480, 195, "응답이 없어 한참 기다려요", ORANGE, 3, w=300),
            a.vis(pill(250, 440, "조용히 Drop하면 한참 기다려요", ORANGE, 18, False, 320) + pill(700, 440, "거부 응답을 주면 바로 실패해요", BLUE, 18, False, 330), 4, 4),
            mark(a, 90, 423, 320, 34, 4), mark(a, 535, 423, 330, 34, 4)]
    caps = ["요청이 출구 장치의 규칙을 만나요", "차단 대상이라 이 자리에서 Drop돼요", "노트북은 응답을 못 받고 기다려요", "Drop은 조용히, 거부 응답은 바로 실패해요"]
    return frame(a, "통과시킬까, 버릴까?", "Drop하면 보낸 쪽은 아무 소식도 못 받아요", caps, "".join(body))


# ---- Page 3: 방화벽은 어느 쪽이 안인지 어떻게 알까? ----
def p3():
    a = new()
    gx0, gx1 = 380, 580
    body = [dev("노트북", 100, Yc, "192.168.10.42", laptop), server(860, Yc, "클라우드 저장소", "203.0.113.80"),
            line(160, Yc, gx0, Yc, LINE, 4, "10 8"), line(gx1, Yc, 815, Yc, LINE, 4, "10 8"),
            mv(a, packet(0, 0, BLUE), [(190, Yc), (770, Yc)], 2, 2, 2, 0.08, 0.92),
            mv(a, packet(0, 0, GREEN), [(770, Yc), (190, Yc)], 3, 3, 3, 0.08, 0.92),
            box(gx0, Yc - 55, gx1 - gx0, 110, BLUE, PANEL, 14, sw=3) + text(480, Yc + 6, "본사 게이트웨이", 18, BLUE, 700),
            a.vis(box(gx0, Yc - 55, gx1 - gx0, 110, BLUE, "none", 14, sw=3), 1, 4),
            f'<circle cx="{gx0}" cy="{Yc}" r="22" fill="{BLUE}"/>' + text(gx0, Yc + 7, "A", 20, BG, 700),
            f'<circle cx="{gx1}" cy="{Yc}" r="22" fill="{ORANGE}"/>' + text(gx1, Yc + 7, "B", 20, BG, 700),
            lbl(gx0, Yc + 86, "A · 사내 쪽", BLUE, 17, 700), lbl(gx1, Yc + 86, "B · 인터넷 쪽", ORANGE, 17, 700),
            mark(a, gx0 - 22, Yc - 22, 44, 44, 1), mark(a, gx1 - 22, Yc - 22, 44, 44, 1),
            tag(a, 480, 195, "문마다 인터페이스 이름이 있어요", BLUE, 1, w=330),
            tag(a, 480, 195, "Outbound · A로 들어와 B로 나가요", BLUE, 2, w=390),
            tag(a, 480, 195, "Inbound · B로 들어와 A로 나가요", GREEN, 3, w=380),
            tag(a, 480, 195, "A→B처럼 풀어 적어 읽어요", ORANGE, 4, w=300)]
    caps = ["게이트웨이의 두 문은 인터페이스 A와 B예요", "요청은 A로 들어와 B로 나가요", "응답은 B로 들어와 A로 나가요", "방향은 장치 기준이라 A→B로 풀어 읽어요"]
    return frame(a, "인터페이스로 방향을 읽기", "같은 대화도 요청과 응답의 방향이 달라요", caps, "".join(body))


# ---- Page 4: 회선을 늘렸는데 왜 그대로 느릴까? ----
def p4():
    a = new()
    wall = lambda c: (f'<rect x="300" y="{Yc - 90}" width="40" height="72" fill="{c}"/><rect x="300" y="{Yc + 18}" width="40" height="72" fill="{c}"/>')
    pipe = lambda h, c: f'<rect x="350" y="{Yc - h / 2}" width="430" height="{h}" rx="8" fill="{c}" fill-opacity="0.3" stroke="{c}" stroke-width="3"/>'
    body = [dev("사내 PC", 90, Yc, None, pc), server(870, Yc, "클라우드 저장소"), line(150, Yc, 300, Yc, LINE, 4, "10 8"),
            a.vis(pipe(72, BLUE), 1, 1), a.vis(pipe(130, BLUE), 2, 4), wall(ORANGE),
            lbl(320, Yc + 118, "방화벽", ORANGE, 18, 700), lbl(320, Yc + 142, "처리량 150Mbps", ORANGE, 17),
            a.vis(lbl(565, Yc - 56, "회선 300Mbps", BLUE, 18, 700), 1, 1), a.vis(lbl(565, Yc - 84, "회선 1Gbps", BLUE, 18, 700), 2, 4),
            mark(a, 52, Yc - 42, 76, 70, 1),
            tag(a, 480, 165, "오후마다 업로드가 느려요", ORANGE, 1, w=290),
            mark(a, 350, Yc - 65, 430, 130, 2), tag(a, 480, 165, "회선을 1Gbps로 올렸어요", BLUE, 2, w=290),
            a.vis("".join(packet(150 + i * 45, Yc) for i in range(3)) + packet(520, Yc) + cross(320, Yc), 3, 4),
            mark(a, 300, Yc - 90, 40, 180, 3), tag(a, 480, 165, "업로드 속도는 그대로예요", RED, 3, w=290),
            tag(a, 480, 165, "가장 좁은 구간이 전체 상한이에요", GREEN, 4, w=370)]
    caps = ["회선은 300Mbps, 방화벽 처리량은 150Mbps예요", "회선만 1Gbps로 넓혔어요", "방화벽 앞에 패킷이 몰려 그대로 느려요", "가장 좁은 구간이 속도를 정해요"]
    return frame(a, "회선을 늘려도 느린 이유", "수치는 설명을 위한 가정이에요", caps, "".join(body))


def p4b():
    a = new()
    rows = [(215, "전용 하드웨어·가속기", ORANGE, "반복 작업을 전용 하드웨어가 처리"), (335, "범용 컴퓨터 + 소프트웨어", BLUE, "프로그램으로 처리")]
    body = [text(490, 140, "처리 속도", 18, TXT, 700), text(760, 140, "바꾸기 쉬움", 18, TXT, 700)]
    for y, n, c, sub in rows:
        body += [cell(40, y - 35, 310, 70, n, c, 19), lbl(195, y + 58, sub, MUTED, 16)]
        body += [box(380, y - 16, 220, 32, LINE, PANEL, 6), box(650, y - 16, 220, 32, LINE, PANEL, 6)]

    def bar(x, y, w, c, s, inside):
        r = box(x, y - 16, w, 32, c, c, 6)
        t = text(x + w / 2, y + 6, s, 16, BG, 700) if inside else text(x + w + 8, y + 6, s, 16, c, 700, "start")
        return r.replace('fill="%s"' % c, 'fill="%s" fill-opacity="0.85"' % c, 1) + t

    body += [a.vis(bar(380, 215, 210, GREEN, "빠름", True) + bar(380, 335, 90, ORANGE, "느릴 수 있음", False), 2, 4),
             a.vis(bar(650, 215, 80, ORANGE, "바꾸기 어려움", False) + bar(650, 335, 210, GREEN, "바꾸기 쉬움", True), 3, 4),
             mark(a, 380, 120, 220, 250, 2), mark(a, 650, 120, 220, 250, 3),
             tag(a, 480, 440, "같은 일을 하는 두 가지 구현이에요", BLUE, 1, w=370),
             tag(a, 480, 440, "전용 하드웨어는 빠르게 처리해요", GREEN, 2, w=350),
             tag(a, 480, 440, "소프트웨어는 바꾸기 쉬워요", GREEN, 3, w=310),
             tag(a, 480, 440, "하나를 얻으면 하나를 내주는 절충이에요", ORANGE, 4, w=430)]
    caps = ["같은 일을 하는 두 가지 구현이 있어요", "전용 하드웨어는 정해진 작업이 빨라요", "소프트웨어는 기능을 바꾸기 쉬워요", "어느 쪽이든 대가가 있는 절충이에요"]
    return frame(a, "하드웨어와 소프트웨어 구현", "두 방식은 장점과 대가가 달라요", caps, "".join(body))


# ---- Page 5: 주소만 볼까, 내용까지 볼까? ----
def p5():
    a = new()
    px, py, pw, ph = 140, 190, 340, 180
    body = [box(px, py, pw, ph, BLUE, PANEL, 12, sw=3),
            f'<rect x="{px + 1.5}" y="{py + 1.5}" width="{pw - 3}" height="58" rx="11" fill="{BLUE}" fill-opacity="0.25"/>',
            text(px + pw / 2, py + 37, "헤더 · 주소와 포트", 18, BLUE, 700), text(px + pw / 2, py + 128, "내용", 20, MUTED, 700),
            line(px + 40, py + 88, px + pw - 40, py + 88, LINE, 4), line(px + 40, py + 108, px + pw - 90, py + 108, LINE, 4),
            text(700, 232, "처리 속도", 18, TXT, 700), box(560, 250, 280, 30, LINE, PANEL, 6),
            a.vis(eye(80, py + 29) + box(560, 250, 260, 30, GREEN, GREEN, 6)
                  + text(690, 271, "빠름", 17, BG, 700), 2, 2),
            a.vis(eye(80, py + 120) + box(560, 250, 90, 30, ORANGE, ORANGE, 6)
                  + text(660, 271, "느림", 17, ORANGE, 700, "start"), 3, 3),
            mark(a, px, py, pw, 62, 2), mark(a, px, py + 62, pw, ph - 62, 3),
            tag(a, 480, 430, "패킷에는 헤더와 내용이 있어요", BLUE, 1, w=340),
            tag(a, 480, 430, "주소와 포트만 보면 빨라요", GREEN, 2, w=300),
            tag(a, 480, 430, "내용까지 보면 정확하지만 느려요", ORANGE, 3, w=360),
            tag(a, 480, 430, "막을 기준에 필요한 깊이만 봐요", GREEN, 4, w=350)]
    caps = ["패킷은 헤더와 내용으로 이뤄져 있어요", "헤더의 주소와 포트만 읽으면 빨라요", "내용까지 읽으면 더 오래 걸려요", "기준에 필요한 만큼만 깊이 봐요"]
    return frame(a, "주소만 볼까, 내용까지 볼까?", "무엇을 읽느냐가 정확도와 속도를 정해요", caps, "".join(body))


def p5b():
    a = new()
    def card(y, addr, tagtxt, c, t0, t1):
        s = box(600, y - 45, 260, 90, LINE, PANEL, 10, sw=3) + text(730, y - 14, addr, 18, TXT, 700)
        return a.vis(s, t0, t1)
    body = [dev("사내 PC", 90, Yc, None, laptop), line(150, Yc, 280, Yc, LINE, 4, "10 8"),
            line(340, Yc, 600, 210, LINE, 3, "10 8"), a.vis(line(340, Yc, 600, 390, LINE, 3, "10 8"), 2, 4),
            mv(a, packet(0, 0), [(180, Yc), (250, Yc)], 1, 1, 1, 0.1, 0.8),
            mv(a, packet(0, 0), [(180, Yc), (310, Yc), (585, 388)], 2, 2, 2, 0.08, 0.9),
            mv(a, packet(0, 0), [(180, Yc), (250, Yc)], 3, 3, 3, 0.1, 0.8),
            router(310, Yc, "출구 장치"),
            pill(310, 200, "차단 규칙: 203.0.113.80", RED, 17, False, 270),
            card(210, "203.0.113.80", "", GREEN, 1, 4), card(390, "새 주소", "", GREEN, 2, 4),
            a.vis(pill(730, 224, "파일 공유", GREEN, 16, False, 130), 1, 1),
            a.vis(pill(730, 404, "파일 공유", GREEN, 16, False, 130), 2, 4),
            a.vis(pill(730, 224, "다른 서비스", ORANGE, 16, False, 140), 3, 4),
            a.vis(cross(310, Yc - 52), 1, 1), a.vis(check(860, 345), 2, 2), a.vis(cross(310, Yc - 52), 3, 3),
            mark(a, 175, 183, 270, 34, 1), mark(a, 600, 345, 260, 90, 2), mark(a, 660, 208, 140, 32, 3),
            tag(a, 330, 435, "주소로 막으면 오늘은 막혀요", RED, 1, w=330),
            tag(a, 330, 435, "새 주소로 옮기면 통과돼요", ORANGE, 2, w=320),
            tag(a, 330, 435, "그 주소의 다른 서비스가 막혀요", RED, 3, w=350),
            tag(a, 330, 435, "주소는 서비스 이름표가 아니에요", GREEN, 4, w=360)]
    caps = ["파일 공유 서비스 주소를 규칙으로 막았어요", "서비스가 새 주소로 옮기면 규칙이 소용없어요", "그 주소를 쓰는 다른 서비스가 대신 막혀요", "목적지 주소는 서비스 이름표가 아니에요"]
    return frame(a, "주소 목록 차단의 한계", "주소로 서비스를 막으면 빗나갈 수 있어요", caps, "".join(body))


# ---- Page 6: 길목 장치가 멈추면 인터넷도 멈출까? ----
def gw(a_, x, y, label, c=BLUE, w=190, h=80):
    return box(x - w / 2, y - h / 2, w, h, c, PANEL, 12, sw=3) + text(x, y + 6, label, 18, c, 700)


def p6():
    a = new()
    body = [pc(110, 230), pc(110, 340), lbl(110, 410, "사무실 PC", TXT, 17, 700), cloud(850, 265),
            line(150, 230, 385, 255, LINE, 4, "10 8"), line(150, 340, 385, 285, LINE, 4, "10 8"), line(575, 265, 780, 265, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, 235), (350, 252)], 1, 1, 1, 0.05, 0.5), mv(a, packet(0, 0), [(610, 265), (770, 265)], 1, 1, 1, 0.5, 0.95),
            a.vis(cross(700, 265) + packet(300, 250), 3, 4),
            a.vis(line(150, 350, 380, 395, GREEN, 3, "6 6") + line(580, 395, 790, 295, GREEN, 3, "6 6"), 4, 4),
            mv(a, packet(0, 0, GREEN), [(180, 355), (480, 405), (700, 340), (775, 300)], 4, 4, 4, 0.1, 0.92),
            gw(a, 480, 265, "본사 게이트웨이"), lbl(480, 330, "192.168.10.1", MUTED, 16),
            a.vis(gw(a, 480, 265, "재부팅 중", ORANGE), 2, 4),
            a.vis(gw(a, 480, 405, "두 번째 장치", GREEN, 210, 56), 4, 4),
            mark(a, 385, 225, 190, 80, 1), tag(a, 480, 175, "평소엔 모든 통신이 여기를 지나요", BLUE, 1, w=390),
            mark(a, 385, 225, 190, 80, 2), tag(a, 480, 175, "토요일 보안 업데이트 → 재부팅", ORANGE, 2, w=380),
            mark(a, 676, 241, 48, 48, 3), tag(a, 480, 175, "사무실 전체 인터넷이 끊겨요", RED, 3, w=340),
            mark(a, 375, 377, 210, 56, 4), tag(a, 480, 175, "한 대가 멈추면 다른 한 대가 이어받아요", GREEN, 4, w=450)]
    caps = ["게이트웨이 하나가 모든 통신을 맡아요", "업데이트하려고 재부팅을 걸었어요", "재부팅하는 몇 분 동안 인터넷이 끊겨요", "같은 역할의 장치를 한 대 더 두어요"]
    return frame(a, "길목 장치가 멈추면?", "단일 장애점이 만드는 일이에요", caps, "".join(body))


def p6b():
    a = new()
    Y2 = 270
    cx = (250, 710)
    body = [line(480, 130, 480, 460, LINE, 2, "6 8")]
    for x, t, c in ((cx[0], "이중화 (장치 두 대)", BLUE), (cx[1], "장애 시 우회 (Bypass)", ORANGE)):
        body += [pill(x, 150, t, c, 18, False, 270), pc(x - 160, Y2 - 5), lbl(x - 160, Y2 + 50, "사무실 PC", MUTED, 16),
                 box(x + 110, Y2 - 22, 84, 44, BLUE, PANEL, 22, sw=3) + text(x + 152, Y2 + 6, "인터넷", 16, BLUE, 700),
                 line(x - 118, Y2, x - 55, Y2, LINE, 4, "10 8"), line(x + 55, Y2, x + 110, Y2, LINE, 4, "10 8")]
    L, R = cx
    byp = lambda c: (f'<polyline points="{R - 105},{Y2} {R - 105},195 {R + 150},195 {R + 150},{Y2 - 22}" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="10 8"/>')
    body += [a.vis(line(L - 118, Y2 + 8, L - 70, 375, GREEN, 3, "6 6") + line(L + 70, 375, L + 120, Y2 + 22, GREEN, 3, "6 6"), 3, 4),
             a.vis(byp(ORANGE), 3, 4),
             mv(a, packet(0, 0, GREEN), [(L - 100, 322), (L, 375), (L + 95, 328)], 3, 3, 3, 0.12, 0.9),
             mv(a, packet(0, 0), [(L - 100, Y2), (L + 85, Y2)], 1, 1, 1, 0.1, 0.9), mv(a, packet(0, 0), [(R - 100, Y2), (R + 85, Y2)], 1, 1, 1, 0.1, 0.9),
             mv(a, packet(0, 0, ORANGE), [(R - 105, 235), (R - 105, 195), (R + 150, 195), (R + 150, 228)], 3, 3, 3, 0.12, 0.9),
             gw(a, L, Y2, "본사 게이트웨이", BLUE, 130, 56), gw(a, R, Y2, "본사 게이트웨이", BLUE, 130, 56),
             a.vis(gw(a, L, Y2, "멈춤", RED, 130, 56) + gw(a, R, Y2, "멈춤", RED, 130, 56), 2, 4),
             a.vis(gw(a, L, 375, "두 번째 장치", GREEN, 150, 44), 3, 4),
             mark(a, L - 65, Y2 - 28, 130, 56, 2), mark(a, R - 65, Y2 - 28, 130, 56, 2),
             tag(a, L, 440, "다른 장치가 이어받아요", GREEN, 3, w=250), tag(a, R, 440, "검사 없이 지나가요", ORANGE, 3, w=230),
             a.vis(pill(L, 440, "장비·관리 비용이 늘어요", BLUE, 18, False, 260) + pill(R, 440, "차단·기록이 빠져요", RED, 18, False, 230), 4, 4),
             mark(a, L - 130, 423, 260, 34, 4), mark(a, R - 115, 423, 230, 34, 4)]
    caps = ["평소엔 게이트웨이를 거쳐 인터넷으로 가요", "게이트웨이가 멈춰요", "이중화는 이어받고, 우회는 검사를 건너뛰어요", "두 방법은 치르는 대가가 달라요"]
    return frame(a, "멈춤에 대비하는 두 방법", "이중화와 우회는 대가가 달라요", caps, "".join(body))


def lesson_items():
    """Pages 1..6; None keeps Page 1 as is."""
    return [None,
            [("u11-l02-p2-drop-wait", "통과시킬까, 버릴까?",
              "노트북의 요청이 출구 장치의 차단 규칙에 걸려 Drop되고, 응답을 받지 못한 노트북이 한참 기다리는 모습입니다.",
              "조용히 Drop하면 보낸 쪽은 응답 없이 기다리고, 거부 응답을 받으면 바로 실패합니다.", 2)],
            [("u11-l02-p3-interface-direction", "인터페이스로 방향을 읽기",
              "본사 게이트웨이의 요청은 A로 들어와 B로 나가 Outbound, 응답은 B로 들어와 A로 나가 Inbound로 읽는 모습입니다.",
              "방향은 장치의 인터페이스 기준이라 A→B처럼 풀어 읽습니다.", 3)],
            [("u11-l02-p4-bottleneck", "회선을 늘려도 느린 이유",
              "회선을 300Mbps에서 1Gbps로 넓혀도 처리량 150Mbps인 방화벽 앞에서 패킷이 몰려 속도가 그대로인 모습입니다.",
              "가장 좁은 구간인 방화벽 처리량이 전체 속도의 상한입니다.", 2),
             ("u11-l02-p4b-hw-sw-tradeoff", "하드웨어와 소프트웨어 구현",
              "전용 하드웨어·가속기는 처리가 빠르지만 바꾸기 어렵고, 범용 컴퓨터와 소프트웨어는 바꾸기 쉽지만 느릴 수 있는 모습입니다.",
              "어느 구현이든 장점과 대가를 맞바꾸는 절충입니다.", 4)],
            [("u11-l02-p5-inspect-depth", "주소만 볼까, 내용까지 볼까?",
              "헤더의 주소와 포트만 읽으면 빠르고, 내용까지 읽으면 더 정확하지만 느려지는 모습입니다.",
              "막을 기준을 정하고 그 기준에 필요한 깊이만 봅니다.", 3),
             ("u11-l02-p5b-address-limits", "주소 목록 차단의 한계",
              "파일 공유 서비스 주소를 막아도 서비스가 새 주소로 옮기면 통과하고, 그 주소를 쓰는 다른 서비스가 대신 막히는 모습입니다.",
              "목적지 주소는 서비스 이름표가 아닙니다.", 4)],
            [("u11-l02-p6-reboot-spof", "길목 장치가 멈추면?",
              "본사 게이트웨이를 재부팅하자 사무실 PC 전체의 인터넷이 끊기고, 같은 역할의 장치를 한 대 더 두면 이어받는 모습입니다.",
              "Inline 장치는 단일 장애점이 될 수 있어 같은 역할의 장치를 두어 대비합니다.", 2),
             ("u11-l02-p6b-failover-bypass", "멈춤에 대비하는 두 방법",
              "장치가 멈추면 이중화는 다른 장치가 이어받아 검사를 계속하고, 장애 시 우회는 검사 없이 통과시켜 대가가 서로 다른 모습입니다.",
              "이중화는 비용이 늘고, 장애 시 우회는 검사와 기록이 빠집니다.", 4)]]


SVGS = {"u11-l02-p2-drop-wait": p2, "u11-l02-p3-interface-direction": p3, "u11-l02-p4-bottleneck": p4, "u11-l02-p4b-hw-sw-tradeoff": p4b,
        "u11-l02-p5-inspect-depth": p5, "u11-l02-p5b-address-limits": p5b, "u11-l02-p6-reboot-spof": p6, "u11-l02-p6b-failover-bypass": p6b}

if __name__ == "__main__":
    d = lesson_dir(2)
    out = d / "assets" / "animations"
    for stem, fn in SVGS.items():
        write(out, stem, fn())
    if "--svg-only" not in sys.argv:
        wire_items(d / "lesson.md", lesson_items())
    print("ok", len(SVGS), "svgs")
