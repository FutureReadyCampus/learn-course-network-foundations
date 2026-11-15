#!/usr/bin/env python3
"""Unit 14 Lesson 2 (터널을 지나는 패킷) SVG review: replaces the old u14-l02-p*-*.svg set.
Run from repo root: python3 scripts/svg_pairs/u14_l02_rev.py   (--svg-only skips the lesson.md edit).

Look of this Lesson (differs from Lesson 1's two dashed site boxes): a thin one-row route strip on top
(쇼룸 PC - 도쿄 SG - 인터넷 - 서울 SG - 서버, zones only as colour bars) and a big "packet X-ray" below it.
Colours: 안쪽(원본) = BLUE, 바깥(새 헤더·터널) = VIOLET, ORANGE only marks what just changed.
Running example: 쇼룸 PC 10.20.0.15 -> AI 서버 192.168.10.50, 도쿄 SG 198.51.100.20 <-> 서울 SG 198.51.100.25.
Moving packets only travel in the gaps between icons, so they never cover a label."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from kit import wire_items, router
from u14_l01_vpn import new, mark, build, ROOT, UNIT
from u7_l01 import mv
from u6_l03 import cell

SRC, DST = "10.20.0.15", "192.168.10.50"
TOK, SEO = "198.51.100.20", "198.51.100.25"
YS = 200
PC, TSG, NET, SSG, SRV = 90, 290, 480, 670, 870


def srvi(x, y, c=GREEN):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3)))


def wp(x=0, y=0):
    """감싼 패킷: 보라색 바깥 포장 안에 파란 원본."""
    return (f'<rect x="{x - 28}" y="{y - 18}" width="56" height="36" rx="6" fill="{VIOLET}"/>'
            f'<rect x="{x - 17}" y="{y - 9}" width="34" height="18" rx="3" fill="{BLUE}"/>'
            f'<path d="M{x - 17} {y - 8} l17 9 l17 -9" fill="none" stroke="{BG}" stroke-width="2"/>')


def lbl(x, name, sub=None, y=YS):
    return text(x, y + 58, name, 17, TXT, 700) + (text(x, y + 80, sub, 16, MUTED) if sub else "")


def zone(x0, x1, c, s):
    return line(x0, 131, x1, 131, c, 4) + text((x0 + x1) / 2, 121, s, 16, c, 700)


def tube(x0=332, x1=628, y=YS, c=VIOLET):
    return box(x0, y - 34, x1 - x0, 68, c, "none", 34, sw=4)


def route(sub_sg=None):
    """한 줄 경로 띠. 인터넷 타원에는 글자를 넣지 않아 패킷이 지나가도 가리지 않는다."""
    return (zone(30, 345, BLUE, f"도쿄 쇼룸 · 10.20.0.0/24") + zone(615, 930, GREEN, "서울 본사 · 192.168.10.0/24")
            + line(124, YS, 250, YS, LINE, 4) + line(330, YS, 410, YS, LINE, 4, "8 6") + line(550, YS, 630, YS, LINE, 4, "8 6")
            + line(710, YS, 836, YS, LINE, 4)
            + pc(PC, YS, None) + booth(TSG, YS, "") + f'<ellipse cx="{NET}" cy="{YS}" rx="70" ry="24" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
            + booth(SSG, YS, "") + srvi(SRV, YS)
            + lbl(PC, "쇼룸 PC", SRC) + lbl(TSG, "도쿄 SG", sub_sg) + lbl(NET, "인터넷") + lbl(SSG, "서울 SG") + lbl(SRV, "서버", DST))


def lc(x, y, s, c, fs=17, w=700):
    """왼쪽 정렬 글자."""
    return text(x, y, s, fs, c, w, anchor="start")


# 1 지사 PC의 질문 -----------------------------------------------------------------
def p1():
    a = new()
    rule = (box(410, 295, 510, 118, VIOLET, PANEL, 10, sw=3) + text(665, 322, "도쿄 SG 규칙", 17, VIOLET, 700)
            + text(665, 355, "192.168.10.0/24 → 터널로", 17, TXT, 700) + text(665, 387, "나머지 → 일반 경로로", 17, MUTED, 700))
    body = [route("기본 게이트웨이"),
            mv(a, packet(0, 0, BLUE), [(150, YS), (226, YS)], 1, 1, 2, 0.1, 0.9),
            pill(215, 335, f"목적지 {DST} (본사 AI)", BLUE, 16, False), mark(52, 318, 326, 40, 1),
            a.vis(rule, 2, 4), mark(406, 291, 518, 126, 2),
            a.vis(tube(), 3, 3), mv(a, wp(), [(360, YS), (600, YS)], 3, 3, 3, 0.1, 0.9), a.vis(check(732, YS - 36), 3, 3), mark(332, YS - 34, 296, 68, 3),
            mv(a, packet(0, 0, MUTED), [(354, YS), (480, YS)], 4, 4, 4, 0.1, 0.9),
            a.vis(pill(215, 395, "목적지 203.0.113.80 (외부 AI 서비스)", MUTED, 16, False), 4, 4), mark(416, 366, 498, 34, 4)]
    caps = ["쇼룸 PC가 패킷을 기본 게이트웨이로 보내요", "도쿄 SG가 목적지를 규칙에 대 봐요", "본사 목적지는 터널로 포장해 서울 SG로 가요", "규칙에 없는 목적지는 일반 경로로 나가요"]
    return frame(a, "지사 PC의 질문은 어디로", "PC는 평소처럼 출구에 맡기기만 해요", caps, "".join(body))


# 2 사설 주소 패킷은 왜 인터넷을 못 건너나 -------------------------------------------
def p2():
    a = new()
    inner = box(275, 365, 410, 56, BLUE, PANEL, 8, sw=3) + text(480, 400, f"원본 패킷 {SRC} → {DST}", 17, BLUE, 700)
    outer = box(250, 298, 460, 136, VIOLET, "none", 12, sw=3) + text(480, 326, f"새 IP 헤더 {TOK} → {SEO}", 17, VIOLET, 700)
    body = [route(), inner, mark(271, 361, 418, 64, 1),
            mv(a, packet(0, 0, BLUE), [(354, YS), (392, YS)], 2, 1, 2, 0.1, 0.9),
            a.vis(cross(430, YS - 40), 2, 2), a.vis(pill(480, 330, "사설 주소로 가는 길을 몰라 버려져요", RED, 17, False), 2, 2),
            a.vis(outer, 3, 4), mark(246, 294, 468, 144, 3),
            a.vis(tube(), 3, 4), mv(a, wp(), [(360, YS), (600, YS)], 4, 3, 4, 0.1, 0.9), a.vis(check(732, YS - 36), 4, 4)]
    caps = ["쇼룸 PC가 만든 원본 패킷이에요", "그대로 내보내면 인터넷 라우터가 버려요", "도쿄 SG가 새 IP 헤더를 한 겹 더 씌워요", "인터넷에서는 바깥 헤더 주소만 쓰여요"]
    return frame(a, "사설 주소 패킷은 왜 못 건널까", "원본 패킷을 통째로 감싸야 해요", caps, "".join(body))


# 3 안쪽 IP와 바깥 IP (이 Lesson의 핵심 그림: 패킷 엑스레이) ----------------------------
def p3():
    a = new()
    outer = (box(40, 150, 600, 64, VIOLET, PANEL, 6, sw=3) + lc(60, 177, "바깥 IP 헤더", VIOLET) + lc(60, 202, f"{TOK} → {SEO}", TXT, 16, None)
             + box(40, 220, 600, 38, MUTED, PANEL, 6, sw=3) + text(340, 245, "암호화 헤더", 16, MUTED, 700))
    inner = (box(40, 266, 600, 150, BLUE, PANEL, 10, sw=3)
             + box(56, 282, 390, 118, BLUE, BG, 6, sw=3) + lc(76, 323, "안쪽 IP 헤더", BLUE) + lc(76, 354, f"{SRC} → {DST}", TXT, 16, None)
             + box(458, 282, 166, 118, MUTED, BG, 6, sw=3) + text(541, 347, "데이터", 17, MUTED, 700))
    rt = router(805, 262, "인터넷 라우터")
    read = (line(776, 248, 662, 196, GREEN, 4) + check(650, 190) + pill(805, 182, "라우터가 읽어요", GREEN, 16, False))
    blind = (line(776, 280, 662, 334, RED, 4, "8 6") + cross(650, 340) + pill(805, 372, "라우터는 못 읽어요", RED, 16, False))
    roles = pill(805, 182, "어느 터널로", VIOLET, 16, True) + pill(805, 372, "누가 누구에게", BLUE, 16, True)
    body = [inner, rt, a.vis(text(340, 205, "쇼룸 PC가 만든 원본 패킷", 17, MUTED, 700), 1, 1), mark(52, 278, 580, 130, 1),
            a.vis(outer, 2, 4), mark(36, 146, 608, 116, 2),
            a.vis(read + blind, 3, 3), mark(660, 160, 290, 44, 3), mark(660, 350, 290, 44, 3),
            a.vis(roles, 4, 4), mark(690, 160, 230, 44, 4), mark(690, 350, 230, 44, 4)]
    caps = ["원본 패킷에는 안쪽 IP 한 쌍이 들어 있어요", "도쿄 SG가 바깥 IP 헤더를 한 겹 씌워요", "인터넷 라우터는 바깥 IP 헤더만 읽어요", "바깥은 터널 양 끝, 안쪽은 실제 통신이에요"]
    return frame(a, "안쪽 IP와 바깥 IP", "주소 네 개를 두 쌍으로 나눠 봐요", caps, "".join(body))


# 4 본사 SG의 포장 풀기 -------------------------------------------------------------
def p4():
    a = new()
    outer = (box(250, 305, 460, 40, VIOLET, PANEL, 8, sw=3) + text(480, 331, f"새 IP 헤더 {TOK} → {SEO}", 16, VIOLET, 700)
             + box(250, 349, 460, 34, MUTED, PANEL, 8, sw=3) + text(480, 372, "암호화 헤더", 16, MUTED, 700))
    inner = box(250, 391, 460, 56, BLUE, PANEL, 8, sw=3) + text(480, 425, f"안쪽 패킷 {SRC} → {DST}", 17, BLUE, 700)
    inner_rev = box(250, 391, 460, 56, BLUE, PANEL, 8, sw=3) + text(480, 425, f"응답 {DST} → {SRC}", 17, BLUE, 700)
    outer_rev = (box(250, 305, 460, 40, VIOLET, PANEL, 8, sw=3) + text(480, 331, f"새 IP 헤더 {SEO} → {TOK}", 16, VIOLET, 700)
                 + box(250, 349, 460, 34, MUTED, PANEL, 8, sw=3) + text(480, 372, "암호화 헤더", 16, MUTED, 700))
    body = [route(), tube(),
            mv(a, wp(), [(360, YS), (600, YS)], 1, 1, 1, 0.1, 0.9),
            a.vis(inner, 1, 3), a.vis(outer, 1, 1), mark(246, 301, 468, 86, 1),
            a.vis(pill(480, 330, "서울 SG가 바깥 헤더를 벗기고 복호화", VIOLET, 16, False, 420), 2, 2), mark(250, 307, 460, 46, 2),
            mv(a, packet(0, 0, BLUE), [(734, YS), (812, YS)], 3, 3, 3, 0.1, 0.9), a.vis(check(773, YS - 34), 3, 3), mark(246, 387, 468, 64, 3),
            a.vis(outer_rev + inner_rev, 4, 4), mv(a, wp(), [(600, YS), (360, YS)], 4, 4, 4, 0.1, 0.9), mark(246, 301, 468, 150, 4)]
    caps = ["터널을 지나 서울 SG에 포장된 패킷이 도착해요", "서울 SG가 바깥 헤더를 벗기고 복호화해요", "서버에는 쇼룸 PC 주소가 그대로 보여요", "응답은 거꾸로, 같은 터널로 돌아가요"]
    return frame(a, "본사 SG는 포장을 어떻게 풀까", "풀린 뒤의 안쪽 패킷이 서버로 가요", caps, "".join(body))


# 4b 터널이 붙어도 서버가 답하지 않을 때 ------------------------------------------------
def p4b():
    a = new()
    Y = 190
    gate = (box(604, Y - 40, 32, 80, MUTED, PANEL, 4, sw=3) + line(604, Y - 14, 636, Y - 14, MUTED, 2) + line(604, Y + 14, 636, Y + 14, MUTED, 2))
    card = (box(120, 296, 720, 148, LINE, PANEL, 12, dash=True, sw=2) + text(480, 320, "본사 방화벽 규칙", 16, MUTED, 700)
            + box(140, 332, 680, 46, RED, BG, 8, sw=3) + text(480, 362, "인터넷에서 직접 오는 접속 → 차단", 17, RED, 700))
    allow = box(140, 388, 680, 46, GREEN, BG, 8, sw=3) + text(480, 418, "터널에서 나온 10.20.0.0/24 → 허용", 17, GREEN, 700)
    body = [line(140, Y, 400, Y, LINE, 4, "8 6"), line(480, Y, 560, Y, LINE, 4), line(640, Y, 816, Y, LINE, 4),
            tube(146, 394, Y), mv(a, wp(), [(172, Y), (368, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(270, 128, "터널 연결됨", GREEN, 17, True), 1, 4), mark(172, 108, 196, 40, 1),
            mv(a, packet(0, 0, BLUE), [(512, Y), (572, Y)], 2, 2, 3, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(572, Y), (790, Y)], 4, 4, 4, 0.1, 0.9),
            booth(100, Y, "") + booth(440, Y, "") + gate + srvi(850, Y) + lbl(100, "도쿄 SG", y=Y) + lbl(440, "서울 SG", y=Y) + lbl(620, "방화벽", y=Y + 4) + lbl(850, "서버", DST, y=Y),
            card, mark(136, 328, 688, 54, 2),
            a.vis(cross(665, Y) + pill(850, 128, "응답 없음", RED, 17, False), 3, 3), mark(600, Y - 40, 40, 80, 3),
            a.vis(allow + pill(850, 128, "응답해요", GREEN, 17, True), 4, 4), a.vis(box(604, Y - 40, 32, 80, GREEN, PANEL, 4, sw=3) + line(604, Y - 14, 636, Y - 14, GREEN, 2) + line(604, Y + 14, 636, Y + 14, GREEN, 2), 4, 4), mark(136, 384, 688, 54, 4)]
    caps = ["터널은 연결됨, 풀린 패킷이 본사에 나와요", "본사 규칙은 직접 오는 접속을 막아 둬요", "허용 규칙이 없으면 서버는 응답하지 못해요", "터널에서 나온 주소를 허용하면 응답해요"]
    return frame(a, "터널이 붙었는데 AI가 답하지 않으면", "연결됨과 응답함은 따로 확인해요", caps, "".join(body))


# 5 터널 밖에서 보이는 것 ------------------------------------------------------------
def p5():
    a = new()
    Y = 190
    eyei = (f'<ellipse cx="440" cy="133" rx="26" ry="15" fill="{BG}" stroke="{TXT}" stroke-width="3"/><circle cx="440" cy="133" r="7" fill="{TXT}"/>'
            + lc(480, 140, "통신사(ISP)", TXT))
    left = (box(40, 258, 430, 160, GREEN, PANEL, 14, sw=3) + text(255, 286, "통신사에게 보이는 것", 18, GREEN, 700)
            + cell(60, 300, 390, 46, f"두 SG 주소 {TOK} → {SEO}", GREEN, 16) + cell(60, 356, 390, 46, "패킷 크기 · 오간 시간", GREEN, 16) + check(448, 262))
    right = (box(490, 258, 430, 160, RED, PANEL, 14, sw=3) + text(705, 286, "통신사에게 가려진 것", 18, RED, 700)
             + cell(510, 300, 390, 46, f"안쪽 주소 {SRC} · {DST}", RED, 16) + cell(510, 356, 390, 46, "AI에 묻는 질문 내용", RED, 16) + cross(898, 262))
    body = [tube(140, 820, Y), line(130, Y, 140, Y, LINE, 4), eyei,
            mv(a, wp(), [(190, Y), (770, Y)], 1, 1, 4, 0.1, 0.9),
            booth(90, Y, "도쿄 SG") + booth(870, Y, "서울 SG"),
            a.vis(left, 2, 4), mark(36, 254, 438, 168, 2),
            a.vis(right, 3, 4), mark(486, 254, 438, 168, 3),
            a.vis(pill(480, 450, "내용은 가려져도 통신 사실은 보여요", GREEN, 17, True), 4, 4)]
    caps = ["통신사는 터널 구간의 패킷을 볼 수 있어요", "바깥 헤더에 적힌 정보는 보여요", "암호화된 안쪽은 보이지 않아요", "통신이 있다는 사실까지 숨겨지진 않아요"]
    return frame(a, "터널 밖에서는 무엇이 보일까", "L3 터널링은 바깥 헤더만 읽혀요", caps, "".join(body))


# 6 포장 한 겹의 대가 (MTU) -------------------------------------------------------------
def p6():
    a = new()
    X0, XM, Y = 60, 700, 250  # 막대 시작, MTU 선, 막대 중심 높이
    hdr = lambda c, x: box(x, Y - 36, 140, 72, c, PANEL, 6, sw=3) + text(x + 70, Y - 4, "바깥 IP", 16, c, 700) + text(x + 70, Y + 20, "IPsec 헤더", 16, c, 700)
    body = [line(XM, 170, XM, 380, RED, 3, "8 6"), text(XM, 160, "회선 한계 MTU 1,500바이트", 17, RED, 700),
            a.vis(cell(X0, Y - 36, XM - X0, 72, "원본 패킷 (한계까지 꽉 참)", BLUE, 17), 1, 3), mark(X0 - 4, Y - 40, XM - X0 + 8, 80, 1),
            a.vis(check(790, Y), 1, 1),
            a.vis(hdr(ORANGE, XM), 2, 2), mark(XM - 4, Y - 40, 148, 80, 2),
            a.vis(hdr(RED, XM) + cross(890, Y) + pill(480, 340, "한계를 넘어 쪼개지거나 버려져요", RED, 17, False), 3, 3),
            a.vis(cell(X0, Y - 36, XM - X0 - 140, 72, "SG가 미리 줄인 원본", BLUE, 17) + hdr(VIOLET, XM - 140) + check(790, Y)
                  + pill(480, 340, "크기 기준을 헤더만큼 줄여요", GREEN, 17, True), 4, 4), mark(X0 - 4, Y - 40, XM - X0 + 8, 80, 4)]
    caps = ["큰 파일 조각은 한계까지 꽉 차 있어요", "터널이 바깥 IP·IPsec 헤더를 더 붙여요", "한계를 넘으면 쪼개지거나 버려져요", "SG에서 미리 줄이면 한계 안에 들어가요"]
    return frame(a, "포장 한 겹의 대가", "짧은 질문은 되는데 큰 파일만 멈춰요", caps, "".join(body))


ITEMS = [
    ("u14-l02-p1-first-hop", "지사 PC의 질문은 어디로", "쇼룸 PC 10.20.0.15가 목적지 192.168.10.50 패킷을 기본 게이트웨이인 도쿄 SG에 맡기면, SG가 규칙에 대 보고 본사 목적지는 터널로 보내고 203.0.113.80 같은 다른 목적지는 일반 경로로 보냅니다.", "SG 규칙이 어떤 목적지를 터널로 보낼지 정합니다.", 4, p1),
    ("u14-l02-p2-private-wrap", "사설 주소 패킷은 왜 못 건널까", "원본 패킷을 그대로 내보내면 인터넷에서 버려지고, 도쿄 SG가 198.51.100.20에서 198.51.100.25로 가는 새 IP 헤더를 한 겹 씌우면 터널로 인터넷을 건너 서울 SG에 닿습니다.", "사설 주소 패킷은 새 바깥 IP 헤더로 감싸야 인터넷을 건넙니다.", 3, p2),
    ("u14-l02-p3-inner-outer", "안쪽 IP와 바깥 IP", "원본 패킷의 안쪽 IP 한 쌍 위에 바깥 IP 헤더와 암호화 헤더가 씌워지고, 인터넷 라우터는 바깥 IP 헤더만 읽으며 바깥은 어느 터널로, 안쪽은 누가 누구에게를 뜻합니다.", "누가 누구에게는 안쪽 IP, 어느 터널로는 바깥 IP를 봅니다.", 2, p3),
    ("u14-l02-p4-unwrap", "본사 SG는 포장을 어떻게 풀까", "서울 SG가 도착한 패킷의 바깥 헤더를 벗기고 복호화하면 서버에는 쇼룸 PC 주소가 그대로 보이고, 응답은 다시 포장되어 같은 터널로 돌아갑니다.", "서울 SG가 포장을 풀면 서버에는 쇼룸 PC의 주소가 그대로 보입니다.", 2, p4),
    ("u14-l02-p4b-allow-rule", "터널이 붙었는데 AI가 답하지 않으면", "터널이 연결됨이어도 본사 방화벽이 직접 오는 접속을 막고 허용 규칙이 없으면 서버가 응답하지 않고, 터널에서 나온 10.20.0.0/24를 허용하면 응답합니다.", "터널 연결과 서버 응답은 별개라서 본사의 허용 규칙이 따로 필요합니다.", 3, p4b),
    ("u14-l02-p5-visible", "터널 밖에서는 무엇이 보일까", "통신사에게는 두 SG 주소와 패킷 크기·시간이 보이고, 안쪽 주소와 AI 질문 내용은 가려지지만 통신 사실은 숨겨지지 않습니다.", "내용은 가려지지만 서울과 도쿄 사이에 통신이 있다는 사실은 보입니다.", 3, p5),
    ("u14-l02-p6-mtu", "포장 한 겹의 대가", "한계까지 꽉 찬 패킷에 바깥 IP·IPsec 헤더가 붙으면 MTU 1,500바이트를 넘고, SG가 원본 크기를 헤더만큼 미리 줄이면 한계 안에 들어갑니다.", "터널 헤더만큼 패킷 크기 여유와 장비 연산을 내어 줍니다.", 3, p6),
]
LESSON = next((ROOT / "units").glob(f"{UNIT}/02-*"))

if __name__ == "__main__":
    out = LESSON / "assets" / "animations"
    for f, *_r, fn in ITEMS:
        write(out, f, fn())
    if "--svg-only" not in sys.argv:
        groups = [[0], [1], [2], [3, 4], [5], [6]]
        wire_items(LESSON / "lesson.md", [[ITEMS[i][:5] for i in g] for g in groups])
    print("ok", len(ITEMS), "svgs")
