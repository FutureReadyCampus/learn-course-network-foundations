#!/usr/bin/env python3
"""Unit 13 Lesson 1 SVG review pass: rebuilt Pages 2-8 (+ a second SVG on Page 4). Run from repo root:
python3 scripts/svg_pairs/u13_l01_rev.py   (--svg-only skips the lesson.md edit).  Page 1 is kept as is.
Helpers are imported from u13_l01_lb.py (not modified). Same example throughout: VIP 203.0.113.10:443, pool 192.168.20.11~.13."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u13_l01_lb import *  # noqa: F401,F403

M = 16  # minimum label size


def svr(x, y, label, c=GREEN, w=124, h=46, dash=False, tc=None):
    return sv(x, y, label, c, w, h, dash, tc)


def tag(x, y, s, c, w=None, filled=False):
    return pill(x, y, s, c, 16, filled, w)


def lb_box(x, y, w=170, h=74, sub=None):
    s = box(x - w / 2, y - h / 2, w, h, BLUE, PANEL, 10, sw=3)
    if sub:
        return s + text(x, y - 5, "로드 밸런서", 17, BLUE, 700) + text(x, y + 20, sub, 16, MUTED, 700)
    return s + text(x, y + 6, "로드 밸런서", 18, BLUE, 700)


# 2 포트 포워딩을 서버 여러 대로 늘리면? -------------------------------------------------
def p2():
    a = new()
    L, R = 40, 500
    sx = 345
    body = [panel(L, "포트 포워딩", MUTED), panel(R, "L4 로드 밸런서", BLUE),
            rt_(L + 80, 250), pools(L + sx - 15, (210, 280, 350), c=MUTED),
            line(L + 130, 250, L + 266, 210, MUTED, 3),
            a.vis(text(L + 80, 320, "외부 443", 16, TXT, 700), 1, 4),
            a.vis(line(L + 130, 250, L + 266, 280, ORANGE, 3, "6 5") + tag(L + 210, 396, "443 → .12 규칙은 거부", RED, 240)
                  + cross(L + 408, 280), 2, 4), mk(a, L + 266, 257, 128, 52, 2),
            a.vis(lb_box(R + 105, 280, 170, 78, VIP)
                  + "".join(line(R + 190, 280, R + 268, y, BLUE, 3) for y in (210, 280, 350)) + pools(R + 330, (210, 280, 350)), 3, 4), mk(a, R + 20, 241, 170, 78, 3),
            fl(a, [(R + 210, 280), (R + 245, 280)], 3, ORANGE),
            a.vis(tag(480, 452, "L4는 IP·포트만 보고 서버를 골라요", GREEN, 380, True), 4, 4)]
    caps = ["포워딩은 포트 하나에 서버 한 대예요", "같은 443에 서버를 더 넣으려 해요", "로드 밸런서가 연결마다 서버를 골라요", "L4 장비는 IP·포트만 보고 나눠요"]
    return frame(a, "포트 포워딩을 서버 여러 대로?", "고정 안내판 vs 연결마다 고르는 장비", caps, "".join(body))


# 3 손님은 왜 주소 하나만 알면 될까? -----------------------------------------------------
def p3():
    a = new()
    body = [person(90, 280, "손님"), lbx(430, 300, "로드 밸런서", None, BLUE, 160, 64),
            pools(790, (190, 300, 410)) + line(510, 300, 725, 190, LINE, 3) + line(510, 300, 725, 300, LINE, 3) + line(510, 300, 725, 410, LINE, 3),
            line(150, 300, 350, 300, LINE, 3),
            a.vis(tag(205, 222, "bot.hangyeol.example", BLUE, 236), 1, 4), mk(a, 87, 205, 236, 34, 1),
            a.vis(tag(440, 222, VIP, ORANGE, 210, True), 2, 4), mk(a, 335, 205, 210, 34, 2),
            fl(a, [(160, 300), (360, 300)], 2),
            fl(a, [(500, 300), (640, 300), (715, 300)], 3, GREEN), a.vis(check(870, 300), 3, 4), mk(a, 727, 277, 128, 52, 3),
            a.vis(tag(480, 455, "서버가 늘어도 손님이 아는 주소는 그대로", GREEN, 440, True), 4, 4)]
    caps = ["손님은 이름 하나만 알아요", "이름을 풀면 VIP 주소 하나가 나와요", "로드 밸런서가 서버 풀 중 하나로 넘겨요", "서버 수가 바뀌어도 주소는 그대로예요"]
    return frame(a, "손님은 주소 하나만 알면 돼요", "대표 주소(VIP)는 서버가 아니라 로드 밸런서 것이에요", caps, "".join(body))


# 4 대화 중에 한결봇이 앞말을 잊는다면? --------------------------------------------------
def p4():
    a = new()
    body = [person(80, 290), lbx(260, 300, "로드 밸런서", None, BLUE, 150, 60) + line(140, 300, 185, 300, LINE, 3),
            svr(560, 190, "서버 .11") + svr(560, 300, "서버 .12") + svr(560, 410, "서버 .13", MUTED, tc=MUTED),
            line(335, 300, 498, 190, LINE, 3) + line(335, 300, 498, 300, LINE, 3),
            a.vis(tag(125, 215, "거실은 15평이에요", BLUE, 200), 1, 1),
            fl(a, [(150, 300), (260, 300), (440, 200), (490, 190)], 1),
            a.vis(cell(630, 172, 90, 36, "15평", GREEN, 17), 1, 4), mk(a, 626, 168, 98, 42, 1),
            a.vis(tag(125, 215, "아까 평수로 계산해 줘", BLUE, 220), 2, 2),
            fl(a, [(150, 300), (260, 300), (440, 300), (490, 300)], 2),
            a.vis(tag(715, 300, "처음 듣는 이야기", RED, 170) + cross(825, 300), 3, 3), mk(a, 498, 277, 124, 46, 3),
            a.vis(box(790, 255, 130, 90, GREEN, PANEL, 10, sw=3) + text(855, 292, "공유 저장소", 16, GREEN, 700) + text(855, 322, "15평", 16, TXT, 700)
                  + line(720, 190, 790, 280, GREEN, 3) + line(620, 300, 790, 300, GREEN, 3) + line(620, 410, 790, 330, GREEN, 3) + check(855, 235), 4, 4), mk(a, 786, 251, 138, 98, 4),
            a.vis(tag(480, 458, "대화 기록은 서버 밖 저장소에 두면 안전해요", GREEN, 460, True), 4, 4)]
    caps = ["첫 요청은 서버 .11이 받고 기억해요", "다음 요청은 다른 서버로 가요", "서버 .12는 앞말을 몰라요", "공유 저장소면 어느 서버든 기억해요"]
    return frame(a, "대화 중에 앞말을 잊는다면?", "요청마다 다른 서버가 받을 수 있어요", caps, "".join(body))


# 4b 세션 고정 (같은 손님은 같은 서버로) -----------------------------------------------------
def p4b():
    a = new()
    body = [person(80, 285, "같은 손님"), lbx(260, 300, "로드 밸런서", None, BLUE, 150, 60) + line(140, 300, 185, 300, LINE, 3),
            svr(560, 190, "서버 .11") + svr(560, 300, "서버 .12", MUTED, tc=MUTED) + svr(560, 410, "서버 .13", MUTED, tc=MUTED),
            line(335, 300, 498, 190, LINE, 3) + line(335, 300, 498, 300, LINE, 3) + line(335, 300, 498, 410, LINE, 3),
            a.vis(tag(480, 140, "세션 고정: 같은 손님은 같은 서버로", BLUE, 380), 1, 4),
            a.vis(tag(125, 225, "거실은 15평이에요", BLUE, 200), 1, 1),
            fl(a, [(150, 300), (260, 300), (440, 200), (490, 190)], 1),
            a.vis(cell(630, 172, 90, 36, "15평", GREEN, 17), 1, 2),
            a.vis(tag(125, 225, "아까 평수로 계산해 줘", BLUE, 220), 2, 2),
            a.vis(line(335, 300, 498, 190, ORANGE, 5), 2, 2),
            fl(a, [(150, 300), (260, 300), (440, 200), (490, 190)], 2, ORANGE),
            a.vis(check(760, 190), 2, 2),
            a.vis(svr(560, 190, "서버 .11", RED, tc=RED) + cross(760, 190) + tag(715, 245, "고장 → 기록도 사라져요", RED, 240), 3, 3), mk(a, 498, 167, 124, 46, 3),
            a.vis(tag(480, 458, "세션 고정은 꼭 필요한 곳에만 써요", GREEN, 380, True), 4, 4)]
    caps = ["같은 손님의 첫 요청은 서버 .11로 가요", "다음 요청도 같은 서버 .11로 가요", "그 서버가 고장 나면 대화가 끊겨요", "기본은 공유 저장소, 고정은 꼭 필요할 때만"]
    return frame(a, "같은 손님은 같은 서버로 보내면?", "세션 고정은 간단하지만 대가가 있어요", caps, "".join(body))


# 5 차례대로 나눠 주면 공평할까? -----------------------------------------------------------
def p5():
    a = new()
    ys = (190, 290, 390)
    body = [lbx(130, 290, "로드 밸런서", None, BLUE, 160, 64), pools(380, ys),
            "".join(line(210, 290, 318, y, LINE, 3) for y in ys),
            a.vis("".join(text(268, y - 14 + (290 - y) * 0.25, f"{i + 1}", 17, ORANGE, 700) for i, y in enumerate(ys)) + tag(130, 160, "라운드 로빈 1→2→3", BLUE, 210), 1, 3), mk(a, 25, 143, 210, 34, 1),
            a.vis(bar(470, 181, 150, 15, BLUE) + bar(470, 281, 120, 15, BLUE) + bar(470, 381, 140, 15, BLUE), 1, 1),
            a.vis(bar(470, 181, 150, 15, BLUE) + bar(470, 281, 380, 95, RED) + bar(470, 381, 140, 15, BLUE), 2, 4),
            a.vis(text(660, 264, "긴 견적 계산", 16, RED, 700), 2, 4), mk(a, 462, 273, 396, 34, 2),
            a.vis(cross(880, 290), 3, 4), a.vis(text(700, 396, "놀고 있어요", 16, MUTED, 700), 3, 4), mk(a, 462, 373, 160, 38, 3),
            a.vis(tag(700, 150, "최소 연결: 한가한 서버로", GREEN, 290, True) + check(880, 390) + line(210, 290, 318, 390, GREEN, 5), 4, 4),
            fl(a, [(220, 296), (300, 360)], 4, GREEN)]
    caps = ["라운드 로빈은 순서대로 나눠 줘요", "그런데 요청 하나가 아주 길어요", "서버 .12만 막히고 .13은 놀아요", "최소 연결은 한가한 서버를 골라요"]
    return frame(a, "차례대로 나눠 주면 공평할까?", "개수만 세면 일의 크기를 몰라요", caps, "".join(body))


# 6 도면 질문만 큰 GPU로 보낼 수 있을까? -----------------------------------------------------
def p6():
    a = new()
    L, R = 40, 500
    body = [panel(L, "L4 · IP와 포트만 봐요", MUTED), panel(R, "L7 · 경로까지 읽어요", BLUE)]
    for x in (L, R):
        c = MUTED if x == L else BLUE
        body += [packet(x + 55, 250, ORANGE) + text(x + 55, 288, "도면 요청", 16, ORANGE, 700)
                 + packet(x + 55, 345, BLUE) + text(x + 55, 383, "일반 문의", 16, BLUE, 700),
                 line(x + 80, 250, x + 145, 285, LINE, 3) + line(x + 80, 345, x + 145, 305, LINE, 3),
                 lbx(x + 200, 295, "로드 밸런서", None, c, 112, 56),
                 svr(x + 350, 215, "작은 서버", GREEN, 110, 46) + svr(x + 350, 375, "큰 GPU", VIOLET, 110, 46)]
    body += [a.vis(line(L + 256, 285, L + 295, 222, RED, 4, "6 5") + cross(L + 350, 262) + tag(L + 130, 195, "내용은 안 보여요", RED, 190), 2, 4), mk(a, L + 295, 192, 110, 46, 2),
             a.vis(line(R + 256, 285, R + 295, 222, GREEN, 4) + line(R + 256, 305, R + 295, 368, GREEN, 4) + check(R + 350, 262) + check(R + 350, 328)
                   + tag(R + 150, 195, "/api/drawing 보고 구분", GREEN, 250), 3, 4), mk(a, R + 295, 352, 110, 46, 3),
             a.vis(tag(480, 458, "경로·쿠키로 나누려면 L7이 필요해요", GREEN, 400, True), 4, 4)]
    caps = ["도면 요청과 일반 문의가 섞여 와요", "L4는 겉봉만 봐서 가르지 못해요", "L7은 경로를 읽어 큰 GPU로 보내요", "경로·쿠키 기준이면 L7을 써요"]
    return frame(a, "도면 질문만 큰 GPU로?", "겉봉만 보는 L4 vs 내용을 읽는 L7", caps, "".join(body))


# 7 모델을 싣는 중인 서버로 왜 요청이 갔을까? -------------------------------------------------
def p7():
    a = new()
    ys = (190, 290, 390)
    body = [lbx(150, 290, "로드 밸런서", None, BLUE, 170, 64), pools(560, ys),
            "".join(line(235, 290, 498, y, LINE, 3) for y in ys),
            a.vis(text(730, 296, "모델 싣는 중", 17, ORANGE, 700), 1, 3),
            a.vis(tag(150, 205, "ping 응답 정상", GREEN, 190), 1, 4), mk(a, 55, 188, 190, 34, 1),
            fl(a, [(250, 290), (420, 290), (480, 290)], 2, ORANGE), a.vis(cross(640, 262), 2, 2), mk(a, 498, 267, 124, 46, 2),
            fl(a, [(250, 292), (420, 292), (480, 292)], 3, BLUE),
            a.vis(svr(560, 290, "서버 .12", MUTED, dash=True, tc=MUTED) + tag(780, 290, "/health: 준비 전", RED, 190) + tag(780, 345, "풀에서 제외", MUTED, 150), 3, 3), mk(a, 498, 267, 124, 46, 3),
            a.vis(svr(560, 290, "서버 .12", MUTED, dash=True, tc=MUTED) + tag(780, 290, "풀에서 제외", MUTED, 150), 4, 4),
            a.vis(tag(480, 452, "켜졌는지 말고 준비됐는지를 물어요", GREEN, 380, True), 4, 4)]
    caps = ["ping만 보면 .12가 정상으로 보여요", "요청이 가서 오류가 나요", "/health로 물으면 준비 전이라 빼요", "서비스가 준비됐는지를 확인해요"]
    return frame(a, "모델을 싣는 서버로 왜 갔을까?", "켜졌다고 일할 준비가 된 건 아니에요", caps, "".join(body))


# 8 서버 한 대를 빼도 손님이 모르게 하려면? -----------------------------------------------------
def p8():
    a = new()
    ys = (190, 290, 390)
    X, W = 470, 380
    body = [lbx(130, 290, "로드 밸런서", None, BLUE, 160, 64), pools(380, ys),
            "".join(line(210, 290, 318, y, LINE, 3) for y in ys[1:]),
            a.vis(line(210, 290, 318, 190, LINE, 3), 1, 1),
            a.vis(text(660, 166, "평소 세 대가 60%씩(가정)", 16, GREEN, 700), 1, 1),
            a.vis(bar(X, 181, W, 60, RED) + bar(X, 281, W, 60, GREEN) + bar(X, 381, W, 60, GREEN) + cross(880, 190), 1, 1),
            a.vis(bar(X, 181, W, 60, RED) + bar(X, 281, W, 60, GREEN) + bar(X, 381, W, 60, GREEN), 2, 2),
            a.vis(text(660, 166, "진행 중인 대화는 마무리해요", 16, ORANGE, 700), 2, 2),
            a.vis(line(210, 290, 318, 190, RED, 3, "6 5") + tag(130, 222, "새 연결에서 제외", ORANGE, 170)
                  + svr(380, 190, "서버 .11", MUTED, dash=True, tc=MUTED), 2, 4), mk(a, 318, 167, 124, 46, 2),
            a.vis(bar(X, 281, W, 90, GREEN) + bar(X, 381, W, 90, GREEN) + text(660, 264, "나머지 두 대가 90%(가정)", 16, ORANGE, 700) + check(880, 330), 3, 4), mk(a, 462, 273, 396, 34, 3),
            a.vis(line(X + W, 270, X + W, 445, RED, 3, "6 5") + text(X + W, 466, "한계 100%", 16, RED, 700), 4, 4), mk(a, X + W - 6, 270, 12, 175, 4),
            a.vis(tag(430, 450, "평소 여유가 있어야 한 대를 빼도 버텨요", GREEN, 410, True), 4, 4)]
    caps = ["서버 .11이 계속 느리고 오류가 나요", "새 연결에서 먼저 빼요", "남은 두 대가 90%씩 맡아요(가정)", "빠진 몫을 받을 여유가 필요해요"]
    return frame(a, "서버 한 대를 빼도 손님이 모르게", "먼저 빼고, 남은 서버의 여유를 따져요", caps, "".join(body))


NEW = [  # (file, page_id, title, alt, caption, after_paragraph, fn)  -- after_paragraph kept from the previous SVG
    ("u13-l01-p2-forward-vs-lb", "advanced-source-17-page-01", "포트 포워딩을 서버 여러 대로?",
     "왼쪽은 외부 443이 서버 .11 한 대에만 연결돼 .12 규칙이 거부되고, 오른쪽은 로드 밸런서(203.0.113.10:443)가 연결마다 서버 .11~.13 중 하나를 고르는 모습입니다.",
     "포트 포워딩은 목적지가 한 대뿐이고, L4 로드 밸런서는 IP와 포트만 보고 연결마다 서버를 고릅니다.", 2, p2),
    ("u13-l01-p3-vip-one-address", "advanced-source-17-page-02", "손님은 주소 하나만 알면 돼요",
     "손님이 bot.hangyeol.example을 풀어 VIP 203.0.113.10:443을 받고, 로드 밸런서가 서버 풀 192.168.20.11~.13 중 하나로 넘기는 모습입니다.",
     "VIP는 로드 밸런서의 주소라서 서버가 늘거나 줄어도 손님이 쓰는 주소는 같습니다.", 2, p3),
    ("u13-l01-p4-forgets-first-line", "advanced-source-17-page-03", "대화 중에 앞말을 잊는다면?",
     "첫 요청은 서버 .11이 기억하지만 다음 요청이 서버 .12로 가면 앞말을 모르고, 공유 저장소에 두면 어느 서버든 같은 기록을 읽는 모습입니다.",
     "대화 기록을 서버 밖 공유 저장소에 두면 어느 서버가 받아도 맥락이 이어집니다.", 2, p4),
    ("u13-l01-p4b-sticky-session", "advanced-source-17-page-03", "같은 손님은 같은 서버로 보내면?",
     "세션 고정은 같은 손님의 요청을 계속 서버 .11로 보내 기억을 이어 가지만, 그 서버가 고장 나면 기록도 함께 사라져 대화가 끊기는 모습입니다.",
     "세션 고정은 간단하지만 한 서버에 기대는 대가가 있어 꼭 필요한 곳에만 씁니다.", 3, p4b),
    ("u13-l01-p5-round-robin-vs-least", "advanced-source-17-page-04", "차례대로 나눠 주면 공평할까?",
     "라운드 로빈은 순서대로 나누지만 긴 요청이 걸린 서버 .12만 막히고 .13은 놀며, 최소 연결은 한가한 서버 .13을 고르는 모습입니다.",
     "라운드 로빈은 개수만 세므로 요청 처리 시간이 들쭉날쭉하면 최소 연결이 어울립니다.", 1, p5),
    ("u13-l01-p6-l4-vs-l7-requests", "u13-l01-page-06", "도면 질문만 큰 GPU로?",
     "왼쪽 L4는 IP와 포트만 봐서 도면 요청과 일반 문의를 가르지 못하고, 오른쪽 L7은 /api/drawing 경로를 읽어 도면 요청을 큰 GPU 서버로 보내는 모습입니다.",
     "경로나 쿠키로 나누려면 요청 내용을 읽는 L7 로드 밸런서가 필요합니다.", 2, p6),
    ("u13-l01-p7-health-check-ready", "advanced-source-17-page-05", "모델을 싣는 서버로 왜 갔을까?",
     "ping에는 정상으로 답하지만 모델을 싣는 중인 서버 .12로 요청이 가 오류가 나고, /health로 준비 여부를 물으면 준비 전이라 풀에서 제외되는 모습입니다.",
     "헬스 체크는 서버가 켜졌는지가 아니라 서비스가 준비됐는지를 확인해야 합니다.", 2, p7),
    ("u13-l01-p8-drain-headroom", "advanced-source-17-page-06", "서버 한 대를 빼도 손님이 모르게",
     "평소 서버 세 대가 60%씩 맡다가 오류가 잦은 서버 .11을 새 연결에서 먼저 빼면 남은 두 대가 90%씩 맡고, 한계 100%까지 여유가 있어야 버티는 모습입니다.",
     "서버를 뺄 때는 새 연결에서 먼저 빼고 남은 서버의 여유를 따져야 합니다.", 2, p8),
]


def rewire(lesson_md):
    """Replace each Page's illustrations block with the old p1 (kept) + NEW entries for that page."""
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    by_page = {}
    for f, pid, t, al, c, ap, _ in NEW:
        by_page.setdefault(pid, []).append((f, t, al, c, ap))
    for pid, ills in by_page.items():
        blk = "  illustrations:\n" + "".join(
            f"  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n    caption: {q(c)}\n    after_paragraph: {ap}\n"
            for f, t, al, c, ap in ills)
        pat = re.compile(rf"(- page_id: {re.escape(pid)}\n)  illustrations:\n(?:  (?:-|  ).*\n)+")
        assert pat.search(fm), pid
        fm = pat.sub(lambda m: m.group(1) + blk, fm, count=1)
    md.write_text(head + "---\n" + fm + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for it in NEW:
        write(OUT, it[0], it[-1]())
    if "--svg-only" not in sys.argv:
        rewire(LESSON / "lesson.md")
    print("ok", len(NEW), "svgs")
