#!/usr/bin/env python3
"""Unit 11 Lesson 7 (사내 AI 서버 앞에 경비를 세우자) SVG review: Page 2, 3, 4(+b), 5b, 6(+b) rebuilt.
Page 1 (u11_l07_new_scenes.p1) and Page 5 (p5) are kept as is.
Run from repo root: python3 scripts/svg_pairs/u11_l07_rev.py   (--svg-only skips lesson.md edit).
Running example: 외부 192.0.2.77 → 앞단 198.51.100.25:443 → AI 서버 192.168.10.50:8080."""
import json
import sys
from u11_new_common import *  # noqa: F401,F403
from u11_new_common import lesson_dir

STAGES = 4


def olock(x, y, c=GREEN):
    """Open padlock (TLS ended)."""
    return (f'<rect x="{x - 20}" y="{y - 4}" width="40" height="32" rx="5" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            f'<path d="M{x - 11} {y - 4} v-10 a11 11 0 0 1 22 0" fill="none" stroke="{c}" stroke-width="3"/>')


# ---- Page 2: IPS --------------------------------------------------------------
def p2():
    a = new()
    ips = box(425, 245, 110, 110, VIOLET, PANEL, 12, sw=3) + lbl(480, 232, "IPS", VIOLET, 22, 700)
    body = [line(165, 215, 425, 285, LINE, 4, "10 8"), line(165, 385, 425, 315, LINE, 4, "10 8"), line(535, 300, 816, 300, LINE, 4, "10 8"),
            dev("외부 출발지", 100, 215, "192.0.2.77", laptop), dev("해외 대역", 100, 385, "연결 시도가 쏟아져요", laptop), server(850, 300, "서버"), ips,
            a.vis(pill(480, 165, "서버 앞 첫 관문", VIOLET, 18, False, 200), 1, 1), mark(a, 425, 245, 110, 110, 1),
            # 2: 대역·포트로 판단
            mv(a, packet(0, 0, GREEN), [(180, 219), (405, 281), (480, 300), (560, 300), (790, 300)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, RED), [(180, 381), (400, 322)], 2, 2, 2, 0.1, 0.6),
            a.vis(check(850, 225) + cross(480, 385) + pill(620, 430, "대역·포트를 보고 통과·차단", ORANGE, 18, False, 320), 2, 2), mark(a, 425, 245, 110, 110, 2),
            # 3: HTTPS 속은 못 읽음
            mv(a, packet(0, 0, BLUE) + lock(0, -32, BLUE), [(180, 219), (405, 281), (480, 300), (560, 300), (790, 300)], 3, 3, 3, 0.1, 0.9),
            a.vis(eye(480, 165) + cross(520, 155) + pill(620, 430, "HTTPS 속 내용은 암호문이라 못 읽어요", BLUE, 18, False, 400), 3, 3), mark(a, 454, 142, 78, 42, 3),
            # 4: 내용 검사는 TLS 푼 뒤
            a.vis(node(690, 300, "내용 검사", "TLS를 푼 뒤", 150, 56, GREEN, 18) + pill(480, 165, "내용 검사는 TLS를 푼 뒤 단계로", GREEN, 18, True, 340), 4, 4), mark(a, 615, 272, 150, 56, 4)]
    caps = ["서버 앞 첫 관문에 IPS를 둬요", "대역·포트를 보고 통과시키거나 막아요", "HTTPS 요청 속 내용은 암호문이라 못 읽어요", "내용 검사는 TLS를 푼 뒤의 단계로 넘겨요"]
    return frame(a, "IPS는 대역·포트로 걸러요", "서버 앞 첫 관문은 요청 내용까지는 못 봐요", caps, "".join(body))


# ---- Page 3: TLS 종단 ---------------------------------------------------------
def p3():
    a = new()
    front = node(480, Y, "앞단", "198.51.100.25:443", 190, 80, BLUE, 20)
    body = [dev("고객 브라우저", 110, Y, "192.0.2.77", laptop), front, server(850, Y, "AI 서버", "192.168.10.50:8080"),
            line(575, Y, 810, Y, LINE, 4, "10 8"),
            a.vis(line(165, Y, 385, Y, BLUE, 5) + lock(277, 250, BLUE) + lbl(277, 345, "TLS 연결 (HTTPS)", BLUE, 16, 700), 1, 4), mark(a, 175, 226, 200, 80, 1),
            a.vis(olock(480, 205) + pill(480, 160, "앞단에서 TLS가 끝나요", GREEN, 18, True, 250), 2, 2), mark(a, 385, 260, 190, 80, 2),
            mv(a, packet(0, 0, GREEN), [(590, Y), (790, Y)], 3, 3, 4, 0.1, 0.9), a.vis(line(575, Y, 810, Y, GREEN, 5) + lbl(690, 345, "풀린 요청", GREEN, 16, 700) + check(850, 225), 3, 4),
            a.vis(eye(690, 240) + lbl(690, 205, "검사 장치", ORANGE, 16, 700) + pill(480, 430, "풀린 요청은 내용을 볼 수 있어요", GREEN, 18, False, 340), 4, 4), mark(a, 655, 222, 70, 36, 4)]
    caps = ["고객 브라우저는 앞단과 TLS 연결을 맺어요", "앞단이 그 TLS 연결을 끝내요", "풀린 요청이 안쪽 AI 서버로 가요", "그래서 뒤의 검사 장치가 내용을 볼 수 있어요"]
    return frame(a, "TLS는 앞단에서 끝나요", "서버 대신 앞단이 암호를 풀어요", caps, "".join(body))


# ---- Page 4: WAF ------------------------------------------------------------------
def p4():
    a = new()
    tls = node(290, Y, "TLS 종료", None, 130, 70, BLUE, 17)
    waf = node(520, Y, "WAF", None, 130, 80, VIOLET, 22)
    ok, bad = "/history?customer=1042", "customer=1042' OR '1'='1"
    body = [line(150, Y, 225, Y, LINE, 4, "10 8"), line(355, Y, 455, Y, LINE, 4, "10 8"), line(585, Y, 816, Y, LINE, 4, "10 8"),
            dev("외부 요청", 100, Y, "192.0.2.77", laptop), tls, waf, server(850, Y, "AI 서버", "192.168.10.50:8080"),
            a.vis(pill(480, 175, "TLS가 풀린 뒤에 WAF가 요청을 읽어요", VIOLET, 18, False, 400), 1, 1), mark(a, 455, 260, 130, 80, 1),
            mv(a, packet(0, 0, GREEN), [(150, Y), (790, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 175, ok, GREEN, 18, False, 300) + check(850, 225), 2, 2), mark(a, 455, 260, 130, 80, 2),
            mv(a, packet(0, 0, RED), [(150, Y), (420, Y)], 3, 3, 3, 0.1, 0.6),
            a.vis(pill(480, 175, bad, RED, 18, False, 340) + cross(520, 365), 3, 3), mark(a, 455, 260, 130, 80, 3),
            a.vis(pill(480, 175, "정상은 막는 오탐 · 공격은 놓치는 미탐", ORANGE, 18, False, 420) + pill(480, 430, "규칙은 계속 손봐야 해요", ORANGE, 18, True, 260), 4, 4), mark(a, 270, 156, 420, 38, 4)]
    caps = ["TLS가 풀린 뒤에 WAF가 놓여요", "정상 요청은 읽어 보고 AI 서버로 넘겨요", "SQL 삽입 같은 공격 요청은 막아요", "규칙이 안 맞으면 오탐과 미탐이 생겨요"]
    return frame(a, "WAF는 풀린 요청의 내용을 봐요", "무엇을 해 달라는 요청인지 읽어요", caps, "".join(body))


def p4b():
    a = new()
    xs = [235, 405, 575]
    names = [("IPS", VIOLET), ("TLS 종단", BLUE), ("WAF", VIOLET)]
    seen = [("출발지 대역 · 포트 · 연결 빈도", "TLS 안의 요청 내용"), ("TLS 연결 · 인증서로 서비스 신분 증명", "공격인지는 따지지 않아요"),
            ("풀린 요청의 경로 · 매개변수 · 본문", "규칙에 없는 새로운 공격"), ("실제 질문 처리", "앞단이 알려 주지 않은 고객 정보")]
    stops = [(x, n, c) for x, (n, c) in zip(xs, names)] + [(800, "AI 서버", GREEN)]
    body = [line(122, Y, 170, Y, LINE, 4), line(300, Y, 340, Y, LINE, 4), line(470, Y, 510, Y, LINE, 4), line(640, Y, 765, Y, LINE, 4),
            dev("고객", 70, Y, None, laptop)]
    for i, (x, n, c) in enumerate(stops, 1):
        w = 130
        if n == "AI 서버":
            dim, lit = server(x, Y, n, None, "#5b677a"), server(x, Y, n, None, c)
            rect = (x - 34, Y - 40, 68, 80)
        else:
            dim, lit = node(x, Y, n, None, w, 70, "#5b677a", 18), node(x, Y, n, None, w, 70, c, 18)
            rect = (x - w / 2, Y - 35, w, 70)
        body += [a.vis(dim, 1, i - 1) if i > 1 else "", a.vis(lit, i, 4), a.vis(lbl(x, 245, "①②③④"[i - 1], MUTED, 20, 700), 1, 4), mark(a, *rect, i),
                 a.vis(pill(480, 400, "보는 것: " + seen[i - 1][0], GREEN, 17, False, None) + pill(480, 448, "못 보는 것: " + seen[i - 1][1], ORANGE, 17, False, None), i, i)]
    caps = ["맨 앞 IPS는 대역·포트·연결 빈도를 봐요", "TLS 종단 프록시가 연결을 받아 암호를 풀어요", "풀린 뒤에야 WAF가 요청 내용을 읽어요", "AI 서버는 걸러진 요청의 질문을 처리해요"]
    return frame(a, "앞단 장치는 순서가 중요해요", "장치마다 볼 수 있는 것이 달라요", caps, "".join(body))


# ---- Page 5b: 서버 기록의 고객 주소 ---------------------------------------------
def p5b():
    a = new()
    Y0 = 250
    rec = box(670, 360, 260, 92, LINE, PANEL, 10, sw=2) + lbl(800, 384, "AI 서버 기록", MUTED, 16, 700)
    body = [dev("고객", 110, Y0, "192.0.2.77", laptop), node(480, Y0, "앞단", "198.51.100.25:443", 190, 80, BLUE, 20), server(850, Y0, "AI 서버", "192.168.10.50:8080"),
            line(165, Y0, 385, Y0, LINE, 4, "10 8"), line(575, Y0, 810, Y0, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(170, Y0), (380, Y0)], 1, 1, 1, 0.05, 0.45), mv(a, packet(0, 0), [(580, Y0), (790, Y0)], 1, 1, 1, 0.55, 0.95),
            a.vis(pill(480, 165, "AI 서버와 연결하는 상대는 앞단이에요", BLUE, 18, False, 380), 1, 1), mark(a, 385, 210, 190, 80, 1),
            a.vis(rec + lbl(800, 414, "보낸 곳: 앞단", TXT, 18, 700), 2, 4), mark(a, 670, 360, 260, 92, 2),
            a.vis(cross(930, 360) + pill(400, 400, "고객 주소가 기록에 안 남아요", RED, 18, False, 320), 2, 2),
            mv(a, packet(0, 0, ORANGE), [(580, Y0), (790, Y0)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(700, 175, "X-Forwarded-For: 192.0.2.77", ORANGE, 17, False, 300), 3, 4), mark(a, 550, 156, 300, 38, 3),
            a.vis(lbl(800, 440, "고객: 192.0.2.77", GREEN, 18, 700) + check(930, 360) + pill(400, 400, "기록에 고객 주소가 남아요", GREEN, 18, True, 300), 4, 4), mark(a, 670, 360, 260, 92, 4)]
    caps = ["AI 서버가 연결을 받는 상대는 앞단이에요", "서버 기록에는 앞단만 남고 고객은 안 보여요", "앞단이 고객 주소를 헤더에 덧붙여 넘겨요", "그러면 서버 기록에도 고객 주소가 남아요"]
    return frame(a, "서버 기록에는 누구 주소가 남을까?", "앞단이 헤더로 고객 주소를 알려 줘야 해요", caps, "".join(body))


# ---- Page 6: 포워드 vs 리버스 -----------------------------------------------------
def p6():
    a = new()
    r1, r2 = 205, 380
    body = [dev("직원 PC", 100, r1, "192.168.10.41", laptop), node(480, r1, "회사 프록시", "192.168.10.5:8080", 200, 70, BLUE, 19), server(850, r1, "외부 AI 서비스", "203.0.113.80:443", GREEN),
            dev("고객", 100, r2, "192.0.2.77", laptop), node(480, r2, "앞단 리버스 프록시", "198.51.100.25:443", 240, 70, GREEN, 18), server(850, r2, "사내 AI 서버", "192.168.10.50:8080", GREEN),
            line(155, r1, 380, r1, BLUE, 4), line(580, r1, 810, r1, BLUE, 4), line(155, r2, 360, r2, GREEN, 4), line(600, r2, 810, r2, GREEN, 4),
            a.vis(pill(480, 318, "둘 다 연결이 두 개예요", MUTED, 18, False, 260), 1, 1),
            "".join(lbl(x, y - 14, n, c, 22, 700) for y, c in ((r1, BLUE), (r2, GREEN)) for x, n in ((268 if y == r1 else 258, "①"), (695 if y == r1 else 705, "②"))),
            a.vis(pill(480, 150, "직원 편 · 안쪽 연결을 받아 바깥으로", BLUE, 18, False, 360), 2, 3), mark(a, 380, 170, 200, 70, 2),
            a.vis(pill(480, 318, "서버 편 · 바깥 연결을 받아 안쪽으로", GREEN, 18, False, 360), 3, 3), mark(a, 360, 345, 240, 70, 3),
            a.vis(pill(480, 318, "누구 편에서 어느 쪽 연결을 받나?", ORANGE, 18, True, 340), 4, 4), mark(a, 310, 299, 340, 38, 4)]
    caps = ["두 프록시 모두 연결을 두 개 맺어요", "포워드는 직원 편에서 안쪽 연결을 받아요", "리버스는 서버 편에서 바깥 연결을 받아요", "이름보다 누구 편인지 확인하면 돼요"]
    return frame(a, "누구 편에 서 있느냐가 달라요", "포워드와 리버스는 같은 모양이에요", caps, "".join(body))


def p6b():
    a = new()
    dash = box(495, 278, 130, 64, BLUE, PANEL, 12, dash=True, sw=3) + lbl(560, 316, "앞단", BLUE, 20, 700) + lbl(560, 366, "설계도", MUTED, 16)
    body = [dev("고객사", 100, Y, "192.0.2.77", laptop),
            box(400, 175, 530, 280, LINE, "none", 14, dash=True, sw=3), lbl(665, 202, "본사 사무실", MUTED, 16, 700),
            line(165, Y, 400, Y, LINE, 4, "10 8"), line(400, Y, 495, Y, LINE, 4, "10 8"), line(625, Y, 806, Y, LINE, 4, "10 8"),
            dash, server(840, Y, "AI 서버", "192.168.10.50:8080"),
            a.vis(pill(480, 140, "설계도는 완성, 앞단은 아직 종이 위예요", BLUE, 18, False, 420), 1, 1), mark(a, 495, 278, 130, 64, 1),
            a.vis(lbl(282, 268, "→ 192.168.10.50:8080", MUTED, 16, 700), 2, 2),
            mv(a, packet(0, 0), [(180, Y), (345, Y)], 2, 2, 2, 0.1, 0.8), a.vis(cross(400, Y) + pill(480, 140, "고객사에서는 사내 서버에 닿지 않아요", RED, 18, False, 400), 2, 2), mark(a, 380, 275, 40, 50, 2),
            a.vis(lbl(282, 268, "공인 주소 198.51.100.25", ORANGE, 16, 700), 3, 4),
            mv(a, packet(0, 0), [(180, Y), (370, Y)], 3, 3, 3, 0.1, 0.8), a.vis(ask(447, Y) + pill(480, 140, "공인 주소로 온 연결은 안으로 어떻게 닿을까?", ORANGE, 18, False, 480), 3, 3), mark(a, 430, 275, 36, 50, 3),
            a.vis(pill(480, 140, "Unit 12에서 따져요", GREEN, 18, True, 220) + pill(680, 420, "시연 기간에는 고객사 주소에만 임시로 열어요", BLUE, 17, False, 420), 4, 4), mark(a, 470, 403, 420, 34, 4)]
    caps = ["앞단은 아직 설계도 위에만 있어요", "고객사에서는 사설 주소 서버에 닿지 않아요", "공인 주소로 온 연결이 안으로 닿는 길이 남았어요", "그 길은 Unit 12에서 따져요"]
    return frame(a, "다음 이야기: 앞단은 아직 종이 위", "공인 주소로 온 연결이 사무실 안까지 닿으려면", caps, "".join(body))


# stem, title, alt, caption, after_paragraph, fn
Q = {
    "advanced-source-08-page-02": [("u11-l07-p02-ips-pass-block", "IPS는 대역·포트로 걸러요",
        "외부 출발지의 요청은 IPS를 통과하고 처음 보는 해외 대역은 막히지만, HTTPS로 암호화된 요청 속 내용은 IPS가 읽지 못해 내용 검사는 TLS를 푼 뒤로 넘기는 모습입니다.",
        "IPS는 대역·포트로 거르고, 요청 내용 검사는 TLS를 푼 뒤로 넘깁니다.", 3, p2)],
    "advanced-source-08-page-03": [("u11-l07-p03-tls-ends-at-front", "TLS는 앞단에서 끝나요",
        "고객 브라우저가 앞단 198.51.100.25:443과 TLS 연결을 맺으면 앞단이 그 연결을 끝내고, 풀린 요청을 AI 서버 192.168.10.50:8080으로 넘겨 뒤의 검사 장치가 내용을 볼 수 있게 되는 모습입니다.",
        "앞단이 TLS를 끝내야 그 뒤에서 요청 내용을 볼 수 있습니다.", 1, p3)],
    "advanced-source-08-page-04": [("u11-l07-p04-waf-reads-request", "WAF는 풀린 요청의 내용을 봐요",
        "TLS가 풀린 뒤에 놓인 WAF가 정상 요청 /history?customer=1042는 AI 서버로 넘기고 customer=1042' OR '1'='1 같은 공격 요청은 막지만, 규칙이 맞지 않으면 오탐과 미탐이 생기는 모습입니다.",
        "WAF는 풀린 요청의 내용을 읽고 허용하거나 차단합니다.", 1, p4),
        ("u11-l07-p04b-front-order", "앞단 장치는 순서가 중요해요",
        "고객 요청이 IPS, TLS 종단 프록시, WAF, AI 서버 순서로 지나며 각 장치가 대역·포트, TLS 연결, 풀린 요청 내용, 질문 처리처럼 서로 다른 것을 보는 모습입니다.",
        "장치마다 볼 수 있는 것이 달라서 설계도에 순서를 적습니다.", 3, p4b)],
    "advanced-source-08-page-05": [("u11-l07-p05-single-front", "앞단 한 대에 기대면?",
        "모든 시연 요청이 지나는 앞단 한 대가 멈추면 AI 서버가 멀쩡해도 서비스 전체가 멈추고, 앞단을 이중화해 대비하는 모습입니다.",
        "앞단은 단일 장애점이므로 이중화가 필요하고 그만큼 비용과 설정이 늘어납니다.", 2, None),
        ("u11-l07-p05b-client-address", "서버 기록에는 누구 주소가 남을까?",
        "AI 서버가 연결을 받는 상대는 앞단이라 서버 기록에 고객 주소가 보이지 않지만, 앞단이 X-Forwarded-For 헤더로 고객 192.0.2.77을 덧붙여 넘기면 기록에 남는 모습입니다.",
        "앞단이 원래 고객 주소를 헤더에 덧붙여야 서버 기록에 남습니다.", 3, p5b)],
    "u11-l07-page-06": [("u11-l07-p06-forward-vs-reverse", "누구 편에 서 있느냐가 달라요",
        "포워드 프록시는 직원 PC 편에서 안쪽 연결을 받아 바깥 AI 서비스로 내보내고, 리버스 프록시는 서버 편에서 고객의 바깥 연결을 받아 사내 AI 서버로 넘기는 같은 모양의 두 구조입니다.",
        "포워드와 리버스는 연결을 두 개 맺는 같은 모양이고, 누구 편인지만 다릅니다.", 1, p6),
        ("u11-l07-p06b-next-unit12", "다음 이야기: 앞단은 아직 종이 위",
        "설계한 앞단은 아직 종이 위에 있고, 고객사에서는 사설 주소 192.168.10.50:8080에 닿지 않아서 공인 주소 198.51.100.25로 온 연결이 사무실 안까지 닿는 방법을 Unit 12에서 따지는 모습입니다.",
        "공인 주소로 온 연결이 사무실 안 서버까지 닿는 길은 Unit 12에서 따집니다.", 14, p6b)],
}


def wire(md, spec):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    lines, out, i, left = fm.split("\n"), [], 0, set(spec)
    while i < len(lines):
        l = lines[i]
        out.append(l)
        i += 1
        if l.startswith("- page_id: ") and l[len("- page_id: "):] in left:
            pid = l[len("- page_id: "):]
            left.discard(pid)
            out.append("  illustrations:")
            for stem, t, al, c, ap, _fn in spec[pid]:
                out += [f"  - file: assets/animations/{stem}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            if i < len(lines) and lines[i] == "  illustrations:":
                i += 1
                while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                    i += 1
    assert not left, left
    md.write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    d = lesson_dir(7)
    out = d / "assets" / "animations"
    for items in Q.values():
        for stem, *_r, fn in items:
            if fn:
                write(out, stem, fn())
    if "--svg-only" not in sys.argv:
        wire(d / "lesson.md", Q)
    print("ok", d.name)
