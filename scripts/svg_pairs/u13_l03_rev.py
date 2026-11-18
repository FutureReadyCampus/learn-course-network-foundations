#!/usr/bin/env python3
"""Unit 13 Lesson 3 SVG review pass (generators for the Pages that needed a new or second picture).
Run from repo root: python3 scripts/svg_pairs/u13_l03_rev.py   (--svg-only skips the lesson.md edit).

Kept as is: p1 (latency), p2 (dns-rr), p7 (cdn). New: p2b TTL, p3 cname steps, p4 resolver-ip (+ p4b fix),
p5 geoip steps (+ p5b guide vs block), p6 sync steps, p7b stale copy, p8 two layers (rev).
Same running example as the Lesson: book.company.example, 서울 203.0.113.10 / 도쿄 203.0.113.20, 지사 10.20.0.0/24, 손님 192.0.2.77."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u13_l01_lb import *  # noqa: F401,F403
from u13_l01_lb import lesson_dir

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"
NAME = "book.company.example"
SEOUL, TOKYO = "203.0.113.10", "203.0.113.20"


def site(x, y, w, h, title, c, dash=True):
    return box(x, y, w, h, c, PANEL, 14, dash=dash, sw=3) + text(x + w / 2, y + 30, title, 18, c, 700)


def varrow(x, y0, y1, c=MUTED, w=4):
    d = 1 if y1 > y0 else -1
    return (line(x, y0, x, y1 - d * 14, c, w)
            + f'<polygon points="{x},{y1} {x - w - 6},{y1 - d * 20} {x + w + 6},{y1 - d * 20}" fill="{c}"/>')


def photo(x, y, c):
    return (f'<rect x="{x}" y="{y}" width="44" height="32" rx="4" fill="{c}"/>'
            f'<path d="M{x + 4} {y + 28} l13 -15 l9 10 l7 -8 l7 13 z" fill="{BG}" fill-opacity="0.35"/>')


# 2b TTL: 레코드를 빼도 캐시가 예전 주소를 알려 준다 ---------------------------------------------
def p2b():
    a = new()
    rec_ok = cell(260, 125, 440, 52, f"DNS 레코드 · 도쿄 {TOKYO}", BLUE, 17)
    rec_gone = cell(260, 125, 440, 52, "DNS 레코드 · 도쿄 주소를 뺐어요", MUTED, 17) + cross(730, 151)
    cache = (box(310, 245, 340, 116, BLUE, PANEL, 10, sw=3) + text(480, 275, "리졸버 캐시", 16, MUTED, 700)
             + text(480, 310, f"도쿄 {TOKYO}", 19, BLUE, 700))
    tokyo_ok = site(740, 240, 180, 130, "도쿄 사이트", BLUE)
    tokyo_down = site(740, 240, 180, 130, "도쿄 사이트", RED) + text(830, 322, "점검 중", 18, RED, 700)
    body = [person(90, 300, "손님"), cache, varrow(480, 181, 243),
            a.vis(rec_ok, 1, 1), a.vis(rec_gone, 2, 4), mk(a, 260, 125, 440, 52, 2, 8),
            a.vis(text(480, 340, "TTL 3600초(1시간)", 17, ORANGE, 700), 1, 3),
            a.vis(text(480, 340, "TTL 미리 짧게", 17, GREEN, 700), 4, 4), mk(a, 310, 245, 340, 116, 4),
            arrow(130, 305, 305, MUTED, 5),
            a.vis(arrow(655, 735, 305, MUTED, 5), 1, 2), a.vis(arrow(655, 735, 305, MUTED, 5), 4, 4),
            a.vis(tokyo_ok, 1, 2), a.vis(tokyo_ok, 4, 4), a.vis(tokyo_down, 3, 3),
            a.vis(arrow(655, 735, 305, RED, 5) + cross(695, 305), 3, 3), mk(a, 740, 240, 180, 130, 3, 16),
            fl(a, [(135, 305), (295, 305)], 3),
            a.vis(pill(480, 435, "TTL을 미리 낮춘 뒤, 퍼진 다음 주소를 빼요", GREEN, 18, True, 460), 4, 4)]
    caps = ["리졸버 캐시가 도쿄 주소를 TTL 동안 보관해요", "지우가 DNS 레코드에서 도쿄 주소를 뺐어요",
            "캐시가 예전 주소를 알려 줘서 점검 중인 곳으로 가요", "점검 전에 TTL을 미리 낮춰 두면 금방 바뀌어요"]
    return frame(a, "TTL 때문에 예전 주소가 남아요", "캐시는 TTL이 끝날 때까지 답을 보관해요", caps, "".join(body))


# 3 이름 -> CNAME -> 주소 ---------------------------------------------------------------------
def p3():
    a = new()
    W, H, Y = 260, 120, 250
    X = (30, 350, 670)

    def real(x, sub, val, c):
        return box(x, Y, W, H, c, PANEL, 10, sw=3) + text(x + W / 2, Y + 36, sub, 16, MUTED, 700) + text(x + W / 2, Y + 82, val, 19, c, 700)

    def ghost(x, sub):
        return (box(x, Y, W, H, LINE, PANEL, 10, dash=True, sw=3) + text(x + W / 2, Y + 36, sub, 16, MUTED, 700)
                + text(x + W / 2, Y + 86, "?", 32, MUTED, 700))

    final = (box(X[2], Y, W, H, GREEN, PANEL, 10, sw=3) + text(X[2] + W / 2, Y + 30, "GSLB가 지역별로 골라요", 16, MUTED, 700)
             + text(X[2] + W / 2, Y + 70, f"일본 → 도쿄 {TOKYO}", 17, GREEN, 700)
             + text(X[2] + W / 2, Y + 100, f"한국 → 서울 {SEOUL}", 17, BLUE, 700))
    body = [person(155, 160), pill(400, 158, "일본 쪽 손님이 물어요", BLUE, 17, False, 240), varrow(155, 212, 244, MUTED, 4),
            real(X[0], "손님이 쓰는 이름", NAME, BLUE), mk(a, X[0], Y, W, H, 1),
            a.vis(ghost(X[1], "다른 이름?"), 1, 1), a.vis(ghost(X[2], "주소?"), 1, 2),
            a.vis(arrow(292, 346, Y + 60, MUTED, 5) + real(X[1], "CNAME (별칭)", "jp.book.gslb.example", VIOLET), 2, 4), mk(a, X[1], Y, W, H, 2),
            a.vis(arrow(612, 666, Y + 60, MUTED, 5) + real(X[2], "도쿄 주소", TOKYO, GREEN) + check(X[2] + W / 2, Y + H + 28), 3, 3), mk(a, X[2], Y, W, H, 3),
            a.vis(final, 4, 4), mk(a, X[2], Y, W, H, 4),
            a.vis(arrow(612, 666, Y + 60, MUTED, 5), 4, 4),
            a.vis(pill(480, 440, "지역은 이름을 푸는 단계에서 정해져요", GREEN, 18, True, 400), 4, 4)]
    caps = ["손님은 이름 하나만 물어요", "이름이 GSLB의 다른 이름(CNAME)을 가리켜요",
            "그 이름을 풀 때 도쿄 주소가 나와요", "같은 이름도 지역마다 다른 주소가 돌아가요"]
    return frame(a, "이름 하나로 지역마다 다른 주소를", "이름 → CNAME → 주소 순서로 따라가요", caps, "".join(body))


# 4 권한 DNS는 리졸버의 위치를 본다 --------------------------------------------------------------
def p4():
    a = new()
    res = box(290, 262, 200, 76, VIOLET, PANEL, 10, sw=3) + text(390, 292, "리졸버", 18, VIOLET, 700) + text(390, 322, "서울 쪽에 있어요", 16, MUTED, 700)
    auth = box(700, 262, 220, 76, BLUE, PANEL, 10, sw=3) + text(810, 292, "권한 DNS", 18, BLUE, 700) + text(810, 322, "위치별로 답해요", 16, MUTED, 700)
    body = [pc(90, 300, "손님 PC"), res, auth, arrow(140, 285, 300, MUTED, 5),
            a.vis(pill(212, 235, "주소가 뭐예요?", BLUE, 17, False, 170), 1, 1), mk(a, 140, 278, 148, 44, 1, 8),
            fl(a, [(150, 300), (270, 300)], 1),
            a.vis(arrow(495, 695, 300, MUTED, 5), 2, 4), fl(a, [(505, 300), (685, 300)], 2),
            a.vis(eye(810, 215) + pill(810, 170, "리졸버 주소를 봐요", ORANGE, 16, False, 190), 2, 4), mk(a, 700, 262, 220, 76, 2),
            a.vis(varrow(810, 342, 370, RED) + cell(700, 372, 220, 48, f"서울 {SEOUL}", RED, 17) + cross(675, 396), 3, 3), mk(a, 700, 372, 220, 48, 3, 8),
            a.vis(pill(595, 235, "손님 주소 앞부분(ECS)도 보내요", VIOLET, 16, False, 290), 4, 4),
            a.vis(varrow(810, 342, 370, GREEN) + cell(700, 372, 220, 48, f"도쿄 {TOKYO}", GREEN, 17) + check(675, 396), 4, 4), mk(a, 700, 372, 220, 48, 4, 8),
            a.vis(text(480, 450, "모든 리졸버가 보내는 건 아니에요", 16, MUTED, 700), 4, 4)]
    caps = ["손님 PC가 설정된 리졸버에게 먼저 물어요", "리졸버가 대신 권한 DNS에 물어요",
            "리졸버가 서울 쪽이라 서울 주소가 돌아와요", "ECS를 보내는 리졸버면 손님 쪽 위치도 알아요"]
    return frame(a, "권한 DNS는 누구의 위치를 볼까?", "손님 PC가 아니라 물어 온 리졸버를 봐요", caps, "".join(body))


def p4b():
    a = new()
    lap_cell = cell(120, 316, 260, 50, "공개 DNS (서울 쪽, 수동)", RED, 17)
    lap_auto = cell(120, 316, 260, 50, "자동(DHCP) · 도쿄 쪽", GREEN, 17)
    body = [pill(480, 140, "도쿄 지사 10.20.0.0/24", VIOLET, 17, False, 270),
            laptop(250, 215, "노트북") + pc(710, 215, "다른 PC"),
            varrow(250, 272, 312, MUTED), varrow(710, 272, 312, MUTED),
            a.vis(lap_cell, 1, 3), a.vis(lap_auto, 4, 4), mk(a, 120, 316, 260, 50, 4, 8),
            cell(580, 316, 260, 50, "도쿄 쪽 리졸버 (DHCP)", GREEN, 17),
            a.vis(ask(290, 292) + ask(750, 292), 2, 2), mk(a, 120, 316, 260, 50, 2, 8), mk(a, 580, 316, 260, 50, 2, 8),
            a.vis(pill(250, 425, "서울 사이트로 안내", RED, 17, False, 230) + cross(392, 425), 3, 3), mk(a, 135, 404, 232, 42, 3, 20),
            a.vis(pill(250, 425, "도쿄 사이트로 안내", GREEN, 17, False, 230) + check(392, 425), 4, 4),
            a.vis(pill(710, 425, "도쿄 사이트로 안내", GREEN, 17, False, 230) + check(852, 425), 3, 4)]
    caps = ["노트북은 수동 설정, 다른 PC는 자동 설정이에요", "각자 설정된 리졸버에게 물어요",
            "노트북만 서울 쪽 리졸버라 서울로 가요", "자동(DHCP)으로 되돌리면 도쿄로 가요"]
    return frame(a, "노트북 한 대만 서울로 가는 이유", "수동으로 적어 둔 리졸버 때문이에요", caps, "".join(body))


# 5 IP 위치는 추정값 ---------------------------------------------------------------------------------
def p5():
    a = new()
    X, W, H = (30, 355, 680), 250, 70
    r1, r2 = 200, 320
    ghost = box(X[2], r1, W, H, LINE, PANEL, 6, dash=True, sw=3) + text(X[2] + W / 2, r1 + 43, "어느 나라?", 18, MUTED, 700)
    body = [a.vis(pill(480, 150, "어느 나라에서 왔을까?", BLUE, 17, False, 250), 1, 4),
            cell(X[0], r1, W, H, "손님 192.0.2.77", BLUE, 18), arrow(282, 352, r1 + 35, MUTED, 5), cell(X[1], r1, W, H, "IP 위치 DB", VIOLET, 18),
            mk(a, X[0], r1, W, H, 1, 8),
            a.vis(ghost, 1, 1),
            a.vis(arrow(609, 677, r1 + 35, MUTED, 5) + cell(X[2], r1, W, H, "추정: 일본 → 도쿄", GREEN, 18), 2, 4), mk(a, X[2], r1, W, H, 2, 8),
            a.vis(cell(X[0], r2, W, H, "VPN 쓰는 손님", BLUE, 18) + arrow(282, 352, r2 + 35, MUTED, 5) + cell(X[1], r2, W, H, "VPN 출구", ORANGE, 18)
                  + arrow(609, 677, r2 + 35, MUTED, 5) + cell(X[2], r2, W, H, "추정: 출구 위치", RED, 18) + cross(918, r2 + 4), 3, 4), mk(a, X[1], r2, W, H, 3, 8),
            a.vis(pill(480, 440, "안내용 추정값이에요. 정확해야 하면 다른 근거를 더해요", GREEN, 17, True, 520), 4, 4)]
    caps = ["손님의 IP로 어느 나라인지 알아내려 해요", "IP 위치 DB가 국가·도시를 추정해요",
            "VPN을 쓰면 출구 위치로 보여요", "가까운 곳 안내에만 쓰고 단정하지 않아요"]
    return frame(a, "IP 주소만 보고 나라를 알 수 있을까?", "IP 위치 정보는 추정값이에요", caps, "".join(body))


def p5b():
    a = new()
    L, R = 40, 500
    body = [panel(L, "첫 화면을 어디서 줄까?", BLUE, 125, 420, 300), panel(R, "약관을 보여 줄까?", VIOLET, 125, 420, 300),
            cell(L + 30, 175, 360, 46, "IP 위치 추정: 일본", BLUE, 17), cell(R + 30, 175, 360, 46, "IP 위치 추정: 일본", BLUE, 17),
            mk(a, L + 30, 175, 360, 46, 1, 8), mk(a, R + 30, 175, 360, 46, 1, 8),
            a.vis(pill(L + 210, 258, "실제로는 다른 나라", ORANGE, 16, False, 230) + pill(R + 210, 258, "실제로는 다른 나라", ORANGE, 16, False, 230), 2, 4),
            mk(a, L + 95, 241, 230, 34, 2, 17), mk(a, R + 95, 241, 230, 34, 2, 17),
            a.vis(cell(L + 30, 296, 360, 46, "조금 느릴 뿐이에요", GREEN, 17) + check(L + 365, 319)
                  + cell(R + 30, 296, 360, 46, "엉뚱한 약관을 봐요", RED, 17) + cross(R + 365, 319), 3, 4), mk(a, R + 30, 296, 360, 46, 3, 8),
            a.vis(cell(R + 30, 356, 360, 46, "손님이 직접 고른 국가 설정", GREEN, 17) + check(R + 365, 379), 4, 4), mk(a, R + 30, 356, 360, 46, 4, 8),
            a.vis(pill(480, 452, "틀리면 곤란한 판단엔 다른 근거를 더해요", GREEN, 17, True, 400), 4, 4)]
    caps = ["같은 IP 위치 추정값이 두 곳에 쓰여요", "추정이 틀렸다고 해 봐요",
            "첫 화면은 조금 느릴 뿐, 약관은 곤란해요", "곤란한 판단에는 다른 근거를 더해요"]
    return frame(a, "같은 위치 정보, 쓰임은 다르게", "틀렸을 때의 손해에 따라 달라져요", caps, "".join(body))


# 6 서울·도쿄 안내 문서 동기화 ------------------------------------------------------------------------
def p6():
    a = new()
    L, R, W = 40, 580, 340
    v_old = "안내 문서 doc-2026-11-11"
    v_new = "안내 문서 doc-2026-11-12"
    body = [panel(L, "서울 사이트", GREEN, 125, W, 165), panel(R, "도쿄 사이트", BLUE, 125, W, 165),
            cell(L + 20, 175, 300, 46, v_new, GREEN, 17),
            a.vis(cell(R + 20, 175, 300, 46, v_old, RED, 17), 1, 2), mk(a, R + 20, 175, 300, 46, 1, 8),
            a.vis(cell(R + 20, 175, 300, 46, v_new, GREEN, 17), 3, 4), mk(a, R + 20, 175, 300, 46, 3, 8),
            person(210, 372, "한국 손님") + person(750, 372, "일본 손님"), varrow(210, 330, 294, MUTED), varrow(750, 330, 294, MUTED),
            a.vis(cell(L + 20, 236, 300, 40, "새 요금로 답해요", GREEN, 16), 2, 3),
            a.vis(cell(R + 20, 236, 300, 40, "예전 요금로 답해요", RED, 16) + cross(R + 295, 256), 2, 2), mk(a, R + 20, 236, 300, 40, 2, 8),
            a.vis(arrow(384, 576, 198, ORANGE, 6) + pill(480, 160, "원본 복사", ORANGE, 16, False, 130), 3, 3),
            a.vis(cell(R + 20, 236, 300, 40, "새 요금로 답해요", GREEN, 16), 3, 3),
            a.vis(cell(L + 20, 236, 300, 40, "새 요금 · doc-2026-11-12", GREEN, 16) + cell(R + 20, 236, 300, 40, "새 요금 · doc-2026-11-12", GREEN, 16), 4, 4),
            mk(a, L + 20, 236, 300, 40, 4, 8), mk(a, R + 20, 236, 300, 40, 4, 8),
            a.vis(pill(480, 456, "응답에 버전 번호를 남기면 어긋난 곳이 보여요", GREEN, 17, True, 420), 4, 4)]
    caps = ["서울은 최신, 도쿄는 하루 전 버전이에요(가정)", "일본 손님은 예전 요금로 답을 받아요",
            "서울 원본을 도쿄로 복사해 맞춰요", "응답에 버전 번호를 남겨 두면 확인해요"]
    return frame(a, "서울과 도쿄가 다른 답을 한다면?", "사이트마다 안내 문서 버전이 다르면 생기는 일이에요", caps, "".join(body))


# 7b 고친 사진이 예전 그대로 보인다 ---------------------------------------------------------------------
def p7b():
    a = new()
    edge = (box(330, 200, 270, 170, VIOLET, PANEL, 10, sw=3) + text(465, 228, "도쿄 에지", 18, VIOLET, 700) + text(465, 250, "사본(캐시)", 16, MUTED, 700)
            + photo(350, 268, BLUE) + text(405, 291, "hero.jpg", 17, TXT, 700, "start"))
    origin = (box(710, 200, 210, 170, GREEN, PANEL, 10, sw=3) + text(815, 228, "서울 원본", 18, GREEN, 700) + text(815, 250, "원본 파일", 16, MUTED, 700))
    body = [person(80, 290, "도쿄 손님"), edge, origin,
            line(130, 285, 325, 285, LINE, 3), line(605, 285, 705, 285, LINE, 3, "10 8"),
            a.vis(photo(730, 268, BLUE) + text(785, 291, "hero.jpg", 17, TXT, 700, "start"), 1, 1),
            a.vis(photo(730, 268, GREEN) + text(785, 291, "hero.jpg 새 사진", 16, TXT, 700, "start"), 2, 3), mk(a, 722, 258, 190, 50, 2, 8),
            fl(a, [(320, 285), (150, 285)], 3, BLUE),
            a.vis(pill(190, 215, "예전 사진이 보여요", RED, 16, False, 190) + cross(310, 215), 3, 3), mk(a, 330, 200, 270, 170, 3, 14),
            a.vis(photo(730, 268, GREEN) + text(785, 291, "hero-v2.jpg", 17, TXT, 700, "start"), 4, 4),
            a.vis(photo(350, 322, GREEN) + text(405, 345, "hero-v2.jpg", 17, TXT, 700, "start"), 4, 4), mk(a, 342, 314, 200, 48, 4, 8),
            fl(a, [(690, 285), (625, 285)], 4, GREEN), a.vis(check(80, 235), 4, 4),
            a.vis(pill(480, 430, "파일 이름에 버전을 붙이면 새로 받아요", GREEN, 18, True, 390), 4, 4)]
    caps = ["도쿄 에지가 hero.jpg 사본을 갖고 있어요", "서울 원본에서 사진을 새것으로 고쳤어요",
            "에지는 같은 이름이라 예전 사본을 줘요", "새 이름 hero-v2.jpg는 에지가 새로 받아 와요"]
    return frame(a, "고친 사진이 왜 예전 그대로일까?", "같은 이름이면 에지의 사본이 그대로 남아요", caps, "".join(body))


# 8 지역은 GSLB, 서버는 L4 ----------------------------------------------------------------------------------
def p8():
    a = new()
    ys = (310, 350, 390)
    gs = lbx(250, 270, "GSLB", "지역 고르기", VIOLET, 140, 64)
    body = [person(70, 140, "한국 손님") + person(70, 330, "일본 손님"), gs,
            line(120, 165, 180, 258, LINE, 3), line(120, 355, 180, 284, LINE, 3),
            site(500, 125, 420, 95, f"서울 {SEOUL}", GREEN), site(500, 245, 420, 210, f"도쿄 {TOKYO}", BLUE),
            lbx(570, 350, "L4", "서버 고르기", BLUE, 110, 56) + "".join(line(625, 350, 750, y, LINE, 3) for y in ys)
            + "".join(sv(800, y, f"서버 {i + 1}", GREEN, 100, 34) for i, y in enumerate(ys)),
            mk(a, 180, 238, 140, 64, 1),
            a.vis(line(320, 258, 500, 172, GREEN, 3) + line(320, 284, 500, 350, BLUE, 3), 1, 3),
            fl(a, [(330, 258), (490, 180)], 1, GREEN), fl(a, [(330, 284), (490, 345)], 1, BLUE),
            fl(a, [(635, 350), (725, 350)], 2), mk(a, 515, 322, 110, 56, 2),
            a.vis(sv(800, 390, "서버 3", RED, 100, 34, dash=True) + cross(878, 390) + pill(700, 428, "L4가 알아서 빼요", BLUE, 16, False, 190), 3, 4), mk(a, 746, 371, 108, 42, 3),
            a.vis(site(500, 125, 420, 95, f"서울 {SEOUL} · 전체 장애", RED) + cross(880, 172), 4, 4), mk(a, 496, 121, 428, 103, 4, 16),
            a.vis(line(320, 258, 500, 300, ORANGE, 4), 4, 4),
            a.vis(pill(250, 440, "큰 장애는 GSLB가, 작은 장애는 L4가 맡아요", GREEN, 17, True, 440), 4, 4)]
    caps = ["GSLB가 손님 위치에 맞는 지역을 골라요", "지역 안에서는 L4가 서버를 골라요",
            "서버 한 대 고장은 L4가 빼면 끝나요", "사이트 전체 장애는 GSLB가 도쿄로 돌려요"]
    return frame(a, "지역을 고른 뒤엔 누가 서버를 고를까?", "공항 안내와 게이트 배정처럼 두 층이 나눠 맡아요", caps, "".join(body))


# (file, title, alt, caption, fn)
ITEMS = {
    "p2b": ("u13-l03-p2b-ttl", "TTL 때문에 예전 주소가 남아요",
            "리졸버 캐시가 도쿄 주소를 TTL 3600초 동안 보관하는 중에 DNS 레코드에서 도쿄 주소를 빼도 캐시가 예전 주소를 알려 점검 중인 곳으로 가고, 점검 전에 TTL을 미리 낮추면 금방 바뀐다는 모습입니다.",
            "DNS 레코드를 바꿔도 캐시는 TTL이 끝날 때까지 예전 주소를 알려 주므로 TTL을 미리 낮춰 둡니다.", p2b),
    "p3": ("u13-l03-p3-cname-steps", "이름 하나로 지역마다 다른 주소를",
           "손님이 book.company.example을 물으면 GSLB의 이름 jp.book.gslb.example(CNAME)을 거쳐 도쿄 주소 203.0.113.20이 나오고, 같은 이름도 한국 쪽 손님에게는 서울 주소가 돌아간다는 흐름입니다.",
           "지역 선택은 GSLB가 이름을 풀어 주는 단계에서 일어납니다.", p3),
    "p4": ("u13-l03-p4-resolver-ip", "권한 DNS는 누구의 위치를 볼까?",
           "손님 PC가 서울 쪽 리졸버에게 묻고 리졸버가 권한 DNS에 대신 물으면 권한 DNS는 리졸버의 위치를 보고 서울 주소를 돌려주며, ECS를 보내는 리졸버라면 손님 주소 앞부분으로 도쿄 주소를 고르는 모습입니다.",
           "권한 DNS는 손님 PC가 아니라 질문을 대신 보낸 리졸버의 주소를 기본으로 봅니다.", p4),
    "p4b": ("u13-l03-p4b-resolver-fix", "노트북 한 대만 서울로 가는 이유",
            "도쿄 지사의 노트북은 수동으로 적은 서울 쪽 공개 DNS를 써서 서울로, 다른 PC는 DHCP로 받은 도쿄 쪽 리졸버를 써서 도쿄로 안내되고, 노트북을 자동으로 되돌리면 도쿄로 안내되는 모습입니다.",
            "리졸버를 같은 지역의 것으로 맞추면 도쿄 지사 손님이 도쿄 사이트로 갑니다.", p4b),
    "p5": ("u13-l03-p5-geoip-steps", "IP 주소만 보고 나라를 알 수 있을까?",
           "IP 위치 DB가 손님 IP 192.0.2.77을 일본·도쿄로 추정하지만 VPN을 쓰는 손님은 출구 위치로 추정돼 틀릴 수 있다는 흐름입니다.",
           "IP 위치 정보는 가까운 지역 안내에 쓰는 추정값입니다.", p5),
    "p5b": ("u13-l03-p5b-guide-vs-block", "같은 위치 정보, 쓰임은 다르게",
            "같은 IP 위치 추정값이 틀렸을 때 첫 화면 안내는 조금 느릴 뿐이지만 약관 표시는 엉뚱한 약관을 보게 되므로, 손님이 직접 고른 국가 설정 같은 다른 근거를 더한다는 비교입니다.",
            "틀렸을 때의 손해가 크면 IP 위치 말고 다른 근거를 함께 씁니다.", p5b),
    "p6": ("u13-l03-p6-sync-steps", "서울과 도쿄가 다른 답을 한다면?",
           "서울은 최신 안내 문서 버전이고 도쿄는 하루 전 버전이라 일본 손님이 예전 요금를 받다가, 서울 원본을 도쿄로 복사해 맞추고 응답에 버전 번호를 남겨 어긋남을 확인하는 모습입니다.",
           "한 곳을 원본으로 배포하고 응답에 버전 번호를 남겨 어긋난 곳을 찾습니다.", p6),
    "p7b": ("u13-l03-p7b-stale-copy", "고친 사진이 왜 예전 그대로일까?",
            "도쿄 에지가 hero.jpg 사본을 갖고 있는 상태에서 서울 원본의 사진을 고쳐도 같은 이름이면 에지가 예전 사본을 주고, 파일 이름에 버전을 붙여 hero-v2.jpg로 바꾸면 에지가 새로 받아 오는 모습입니다.",
            "CDN 사본이 오래 남아 고친 파일이 늦게 보이면 캐시 시간과 파일 이름의 버전, 삭제 요청으로 관리합니다.", p7b),
    "p8": ("u13-l03-p8-two-layers-rev", "지역을 고른 뒤엔 누가 서버를 고를까?",
           "GSLB가 한국 손님은 서울, 일본 손님은 도쿄로 고르고 도쿄 안의 L4가 서버를 고르며, 서버 한 대 고장은 L4가 빼고 서울 전체 장애는 GSLB가 한국 손님을 도쿄로 돌리는 모습입니다.",
           "서버 한 대 고장은 지역 안 L4가, 사이트 전체 장애는 GSLB가 처리합니다.", p8),
}

# Page order for lesson.md: per Page a list of (item key or existing (file,title,alt,caption), after_paragraph); None = untouched
EXISTING = {
    "p2": ("u13-l03-p2-dns-rr", "DNS가 주소를 둘 알려 주면?", "이름 하나에 서울과 도쿄 주소를 둘 다 등록했지만 도쿄 사이트가 점검 중이어도 DNS는 몰라서 손님을 도쿄로 안내하다 막히는 모습입니다.", "DNS 라운드 로빈은 살아 있는지 확인하지 않으므로 상태를 보는 GSLB가 필요합니다."),
    "p7": ("u13-l03-p7-cdn", "사진과 화면은 더 가까이 둘 수 없을까?", "도쿄 손님이 서울 원본에서 3MB 사진을 받다가 도쿄 에지에 사본을 저장해 두고 이후 가까운 에지에서 바로 받으며, 개인 응답은 캐시하지 않는 모습입니다.", "CDN은 누구에게나 같은 정적 파일만 가까이 캐시하고 개인 응답은 캐시하지 않습니다."),
}


def entry(key, after):
    if key in ITEMS:
        f, t, al, c, _ = ITEMS[key]
        return (f, t, al, c, after)
    f, t, al, c = EXISTING[key]
    return (f, t, al, c, after)


PAGES = [
    None,
    [entry("p2", 1), entry("p2b", 2)],
    [entry("p3", 1)],
    [entry("p4", 2), entry("p4b", 3)],
    [entry("p5", 2), entry("p5b", 4)],
    [entry("p6", 3)],
    [entry("p7", 2), entry("p7b", 4)],
    [entry("p8", 3)],
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, _, _, _, fn in ITEMS.values():
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", PAGES)
    print("ok", len(ITEMS), "svgs")
