#!/usr/bin/env python3
"""Unit 13 Lesson 2 (이중화로 장애에 대비하기) SVG review pass. Run from repo root:
python3 scripts/svg_pairs/u13_l02_rev.py   (--svg-only skips the lesson.md edit).

Fixes: 한 단계에 두 가지가 바뀌던 곳(Page 2 두 장비, Page 4 두 패널, Page 6 부하 막대+클라우드)을 나누고,
Page마다 본문이 묻는 두 번째 내용(가용성 계산, 액티브/액티브, 두 주인, 대가 세 가지)을 두 번째 그림으로 뺐다.
공유 헬퍼는 import만 한다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u13_l01_lb import *  # noqa: F401,F403
from u13_l01_lb import lesson_dir

LESSON = lesson_dir(2)
OUT = LESSON / "assets" / "animations"


def vtext(x, y, s, fs=17, c=TXT, anchor="middle"):
    return text(x, y, s, fs, c, 700, anchor)


def lbx(x, y, label, sub=None, c=BLUE, w=150, h=64, dash=False):
    """공유 lbx와 같지만 보조 글자를 16px로."""
    s = box(x - w / 2, y - h / 2, w, h, c, PANEL, 10, dash=dash, sw=3)
    if sub:
        return s + text(x, y - 3, label, 18, c, 700) + text(x, y + 19, sub, 16, MUTED, 700)
    return s + text(x, y + 6, label, 18, c, 700)


# 1 서버는 멀쩡한데 왜 통째로 멈췄을까? ----------------------------------------------------------
def p1():
    a = new()
    ys = (190, 300, 410)
    body = [person(80, 285, "손님"), line(130, 300, 330, 300, LINE, 3),
            lbx(410, 300, "로드 밸런서", None, BLUE, 160, 64),
            "".join(line(490, 300, 735, y, LINE, 3) for y in ys), pools(800, ys),
            pill(800, 140, "서버 3대 모두 정상", GREEN, 17, False, 220),
            a.vis(lbx(410, 300, "로드 밸런서", None, RED, 160, 64, dash=True) + vtext(410, 358, "멈춤", 17, RED), 2, 4), mk(a, 325, 263, 170, 74, 2),
            fl(a, [(140, 300), (290, 300)], 3, RED), a.vis(cross(320, 262), 3, 4), mk(a, 304, 246, 32, 32, 3, 16),
            a.vis(pill(410, 215, "단일 장애점 (SPOF)", ORANGE, 17, True, 230), 4, 4)]
    caps = ["손님은 로드 밸런서를 지나 서버로 가요", "로드 밸런서 한 대가 멈췄어요", "서버가 멀쩡해도 손님은 못 들어가요", "한 곳이 멈추면 전체가 멈추는 곳이에요"]
    return frame(a, "서버는 멀쩡한데 왜 멈췄을까?", "손님이 지나는 길에서 한 곳이 막힌 거예요", caps, "".join(body))


# 1b 가용성 99.9% = 1년 중 얼마나 멈출 수 있나 ---------------------------------------------------
def p1b():
    a = new()
    X, W, H = 80, 800, 30

    def row(y, label, pill_txt=None):
        s = vtext(X, y - 10, label, 18, TXT, "start") + box(X, y, W, H, LINE, GREEN, 5, sw=2)
        if pill_txt:
            s += (f'<rect x="{X + W - 5}" y="{y}" width="5" height="{H}" rx="2" fill="{RED}"/>'
                  + line(X + W - 2, y + H, X + W - 2, y + H + 22, RED, 3) + pill(X + W - 150, y + H + 40, pill_txt, RED, 17, False, 300))
        return s
    body = [row(142, "1년 = 365일 (전체 시간) · 가용성 = 정상 시간 ÷ 전체 시간"),
            a.vis(row(222, "가용성 99.9% → 전체의 0.1%가 멈춰도 돼요", "멈춰도 되는 시간: 약 8.8시간"), 2, 4), mk(a, X + W - 12, 218, 24, 38, 2, 6),
            a.vis(row(345, "가용성 99.99% → 전체의 0.01%가 멈춰도 돼요", "멈춰도 되는 시간: 약 53분"), 3, 4), mk(a, X + W - 12, 341, 24, 38, 3, 6),
            a.vis(pill(480, 458, "숫자가 높을수록 멈춰도 되는 시간이 짧아져요", GREEN, 18, True, 480), 4, 4)]
    caps = ["가용성은 정상으로 쓴 시간의 비율이에요", "99.9%는 1년에 약 8.8시간까지 멈춰도 돼요", "99.99%는 약 53분까지만 멈춰도 돼요", "숫자가 높을수록 멈춤이 짧아져요"]
    return frame(a, "99.9%는 얼마나 멈춰도 된다는 뜻일까?", "빨간 칸이 1년 중 멈춰도 되는 시간이에요 (실제보다 크게 그렸어요)", caps, "".join(body))


# 2 액티브/스탠바이: 쉬는 예비 장비 -----------------------------------------------------------------
POOL = box(710, 232, 170, 100, GREEN, PANEL, 10, sw=3) + vtext(795, 276, "서버 풀", 18, GREEN) + vtext(795, 304, ".11~.13", 16, MUTED)


def two_lb_base(a, ya, yb, flow_a_step, flow_b_step):
    """공통 배경: 손님, 장비 두 대, 서버 풀, 평소 연결선."""
    return [person(70, 262, "손님"), POOL,
            line(130, 285, 345, ya, LINE, 3) + line(130, 285, 345, yb, LINE, 3),
            line(515, ya, 710, 270, LINE, 3) + line(515, yb, 710, 295, LINE, 3)]


def p2():
    a = new()
    ya, yb = 190, 370
    body = two_lb_base(a, ya, yb, 1, 3)
    body += [lbx(430, ya, "장비 A", "일하는 중", GREEN, 170, 70) + lbx(430, yb, "장비 B", "대기", MUTED, 170, 70),
             a.vis(line(130, 285, 345, ya, BLUE, 4) + line(515, ya, 710, 270, BLUE, 4), 1, 1),
             fl(a, [(150, 285), (345, ya), (515, ya), (700, 270)], 1, BLUE),
             a.vis(lbx(430, ya, "장비 A", "고장", RED, 170, 70, dash=True) + cross(520, ya - 34)
                   + line(130, 285, 345, ya, RED, 3, "6 6") + line(515, ya, 710, 270, RED, 3, "6 6"), 2, 2), mk(a, 345, ya - 39, 170, 78, 2),
             a.vis(lbx(430, ya, "장비 A", "고장", RED, 170, 70, dash=True), 3, 4),
             a.vis(lbx(430, yb, "장비 B", "일하는 중", GREEN, 170, 70) + line(130, 285, 345, yb, BLUE, 4) + line(515, yb, 710, 295, BLUE, 4)
                   + check(540, yb - 36) + pill(640, 438, "B가 넘겨받아요 (페일오버)", GREEN, 17, False, 280), 3, 3), mk(a, 345, yb - 39, 170, 78, 3),
             a.vis(lbx(430, yb, "장비 B", "일하는 중", GREEN, 170, 70) + line(130, 285, 345, yb, BLUE, 4) + line(515, yb, 710, 295, BLUE, 4) + check(540, yb - 36)
                   + pill(480, 456, "안전하지만 성능은 한 대와 같아요", ORANGE, 18, True, 400), 4, 4)]
    caps = ["평소엔 장비 A만 일하고 B는 쉬어요", "일하던 장비 A가 고장 났어요", "쉬던 장비 B가 일을 넘겨받아요", "안전하지만 처리 성능은 한 대와 같아요"]
    return frame(a, "예비 장비는 평소에 쉬게 둘까?", "액티브/스탠바이는 한 대만 일하고 한 대는 대기해요", caps, "".join(body))


# 2b 액티브/액티브: 둘이 같이 일하면 ------------------------------------------------------------------
def p2b():
    a = new()
    ya, yb = 168, 342
    body = [person(70, 262, "손님"), POOL.replace('y="232"', 'y="205"').replace('y="276"', 'y="249"').replace('y="304"', 'y="277"'),
            line(130, 285, 345, ya, LINE, 3) + line(130, 285, 345, yb, LINE, 3),
            line(515, ya, 710, 245, LINE, 3) + line(515, yb, 710, 270, LINE, 3)]
    for y, n in ((ya, "A"), (yb, "B")):
        body.append(lbx(430, y, f"장비 {n}", None, GREEN, 170, 60) + box(345, y + 40, 170, 18, LINE, BG, 5, sw=2))
    ba = lambda y, pct, c: f'<rect x="345" y="{y + 40}" width="{170 * pct / 100:.0f}" height="18" rx="5" fill="{c}"/>'
    body += [a.vis(ba(ya, 60, GREEN) + vtext(430, ya + 84, "60%(가정)", 16, GREEN), 1, 1),
             a.vis(ba(yb, 60, GREEN) + vtext(430, yb + 84, "60%(가정)", 16, GREEN), 1, 2),
             a.vis(lbx(430, ya, "장비 A", "고장", RED, 170, 60, dash=True) + cross(520, ya - 28), 2, 4), mk(a, 345, ya - 34, 170, 68, 2),
             a.vis(ba(yb, 100, RED) + vtext(430, yb + 84, "120%(가정) 넘쳐요", 16, RED) + cross(520, yb - 28), 3, 4), mk(a, 345, yb + 36, 170, 26, 3, 8),
             a.vis(pill(742, 400, "평소 50% 이하로 써요(가정)", GREEN, 17, True, 300), 4, 4)]
    caps = ["평소엔 두 장비가 60%씩 나눠 일해요", "장비 A가 고장 났어요", "남은 장비 B가 두 대 몫을 맡아 넘쳐요", "평소 50% 이하여야 한 대가 빠져도 버텨요"]
    return frame(a, "둘이 같이 일하면 한 대가 빠질 때는?", "액티브/액티브는 평소엔 빠르지만 여유가 필요해요", caps, "".join(body))


# 3 장비가 바뀌어도 손님은 왜 같은 주소로 올까? ---------------------------------------------------------
def p3():
    a = new()
    ya, yb = 190, 370
    pool = box(720, 250, 160, 80, GREEN, PANEL, 10, sw=3) + vtext(800, 285, "서버 풀", 18, GREEN) + vtext(800, 312, ".11~.13", 16, MUTED)
    body = [person(70, 262, "손님"), pool,
            lbx(440, ya, "장비 A", None, GREEN, 150, 60) + lbx(440, yb, "장비 B", None, MUTED, 150, 60),
            line(515, ya, 720, 280, LINE, 3) + line(515, yb, 720, 300, LINE, 3),
            line(440, ya + 30, 440, yb - 30, LINE, 3, "6 6"),
            a.vis(line(130, 285, 365, ya, BLUE, 3) + pill(440, 135, VIP, ORANGE, 17, True, 210), 1, 2),
            fl(a, [(440, 235), (440, 320)], 1, GREEN), a.vis(vtext(412, 285, "하트비트", 17, GREEN, "end"), 1, 1),
            a.vis(lbx(440, ya, "장비 A", None, RED, 150, 60, dash=True) + cross(440, 280) + vtext(412, 285, "하트비트 끊김", 17, RED, "end"), 2, 3), mk(a, 365, ya - 34, 150, 68, 2),
            a.vis(lbx(440, ya, "장비 A", None, RED, 150, 60, dash=True), 4, 4),
            a.vis(lbx(440, yb, "장비 B", None, GREEN, 150, 60) + line(130, 285, 365, yb, BLUE, 3) + pill(440, 432, VIP, ORANGE, 17, True, 210)
                  + check(545, yb), 3, 4), mk(a, 365, yb - 34, 150, 68, 3),
            a.vis(pill(150, 450, "손님이 쓰는 주소는 그대로", GREEN, 17, False, 280), 4, 4)]
    caps = ["일하는 장비 A가 VIP를 맡고 신호를 보내요", "장비 A가 멈춰 신호가 끊겨요", "장비 B가 VIP를 넘겨받아요", "손님은 같은 주소 하나만 써요"]
    return frame(a, "장비가 바뀌어도 같은 주소로", "일하는 장비가 보내는 하트비트가 끊기면 넘겨받아요", caps, "".join(body))


# 3b 신호선만 끊기면: 두 주인 ---------------------------------------------------------------------------
def p3b():
    a = new()
    ya, yb = 190, 370
    pool = box(720, 250, 160, 80, GREEN, PANEL, 10, sw=3) + vtext(800, 285, "서버 풀", 18, GREEN) + vtext(800, 312, ".11~.13", 16, MUTED)
    body = [person(70, 262, "손님"), pool,
            lbx(440, ya, "장비 A", None, GREEN, 150, 60) + lbx(440, yb, "장비 B", None, MUTED, 150, 60),
            line(130, 285, 365, ya, BLUE, 3) + pill(440, 135, VIP, ORANGE, 17, True, 210),
            line(515, ya, 720, 280, LINE, 3) + line(515, yb, 720, 300, LINE, 3),
            line(440, ya + 30, 440, yb - 30, LINE, 3, "6 6"), a.vis(vtext(412, 285, "하트비트", 17, GREEN, "end"), 1, 1),
            a.vis(cross(440, 280) + vtext(412, 285, "하트비트 끊김", 17, RED, "end"), 2, 4),
            a.vis(lbx(440, yb, "장비 B", None, GREEN, 150, 60) + line(130, 285, 365, yb, BLUE, 3) + pill(440, 432, VIP, ORANGE, 17, True, 210)
                  + pill(165, 450, "접속이 들쭉날쭉해요", RED, 17, False, 240), 3, 3), mk(a, 365, yb - 34, 150, 68, 3),
            a.vis(lbx(440, yb, "장비 B", None, MUTED, 150, 60), 4, 4),
            a.vis(line(490, ya + 30, 490, yb - 30, GREEN, 3, "6 6") + check(490, 280) + pill(700, 445, "신호 경로를 이중으로 둬요", GREEN, 17, True, 300), 4, 4)]
    caps = ["장비 A가 VIP를 맡고 신호를 보내요", "두 장비 사이 신호선만 끊겼어요", "B도 A가 죽었다 여겨 VIP를 가져가요", "신호 경로를 이중으로 두면 막을 수 있어요"]
    return frame(a, "신호선만 끊기면 주인이 둘이 돼요", "둘 다 멀쩡한데 서로 신호를 못 받는 경우예요", caps, "".join(body))


# 4 두 대를 뒀는데 왜 같이 멈췄을까? -------------------------------------------------------------------
def p4():
    a = new()
    L, R = 40, 500
    body = [panel(L, "같은 스위치에 연결", MUTED), panel(R, "스위치를 나눔", GREEN)]
    for x in (L, R):
        body.append(lbx(x + 110, 200, "장비 A", None, GREEN, 140, 52) + lbx(x + 310, 200, "장비 B", None, GREEN, 140, 52))
    sw = lambda x, y, c, t: box(x - 70, y - 20, 140, 40, c, PANEL, 8, sw=3) + vtext(x, y + 6, t, 17, c)
    body += [line(L + 110, 226, L + 180, 280, LINE, 3) + line(L + 310, 226, L + 240, 280, LINE, 3) + sw(L + 210, 300, GREEN, "스위치 1대"),
             line(R + 110, 226, R + 110, 280, LINE, 3) + line(R + 310, 226, R + 310, 280, LINE, 3) + sw(R + 110, 300, GREEN, "스위치 1") + sw(R + 310, 300, GREEN, "스위치 2"),
             a.vis(sw(L + 210, 300, RED, "멈춤") + pill(L + 210, 352, "스위치 펌웨어를 올리는 날", ORANGE, 16, False, 260), 2, 2), mk(a, L + 140, 276, 140, 48, 2),
             a.vis(sw(L + 210, 300, RED, "멈춤") + cross(L + 210, 365) + pill(L + 210, 402, "두 대가 함께 끊겨요", RED, 17, False, 220), 3, 4),
             mk(a, L + 90, 344, 240, 80, 3, 14),
             a.vis(sw(R + 110, 300, RED, "스위치 1 멈춤") + check(R + 210, 365) + pill(R + 210, 402, "장비 B는 이어 가요", GREEN, 17, False, 220), 4, 4),
             mk(a, R + 40, 276, 140, 48, 4), mk(a, R + 90, 344, 240, 80, 4, 14)]
    caps = ["장비 두 대를 같은 스위치에 꽂았어요", "스위치 펌웨어를 올리다 스위치가 멈췄어요", "왼쪽은 장비 두 대가 함께 끊겨요", "오른쪽은 한 대만 멈춰 B가 이어 가요"]
    return frame(a, "두 대를 뒀는데 왜 같이 멈췄을까?", "공통으로 기대는 스위치 하나가 새 단일 장애점이 돼요", caps, "".join(body))


# 5 고장 난 서버, 수리를 5일이나 기다려야 할까? -----------------------------------------------------------
def p5():
    a = new()
    img = (box(70, 255, 160, 80, VIOLET, PANEL, 10, sw=3) + vtext(150, 292, "VM 이미지", 18, VIOLET) + text(150, 318, "(미리 만든 틀)", 14, MUTED, 700))
    s11, s12, s13, s14 = (635, 215), (805, 215), (805, 315), (635, 315)
    body = [img, panel(520, "서버 풀", GREEN, 125, 400, 300),
            sv(*s11, "서버 .11", GREEN, 150) + sv(*s12, "서버 .12", GREEN, 150) + sv(*s13, "서버 .13", GREEN, 150),
            a.vis(sv(*s11, "서버 .11", RED, 150) + cross(725, 195) + pill(635, 262, "수리 5일", RED, 16, False, 120), 1, 4), mk(a, 559, 188, 154, 54, 1),
            a.vis(sv(*s14, "서버 .14", ORANGE, 150, dash=True), 2, 2),
            a.vis(pill(150, 385, "이미지에서 몇 분(가정)", ORANGE, 16, False, 230), 2, 3),
            fl(a, [(240, 295), (480, 315), (545, 315)], 2, VIOLET),
            a.vis(sv(*s14, "서버 .14", GREEN, 150) + check(704, 296) + pill(635, 362, "헬스 체크 통과", GREEN, 16, False, 150), 3, 4), mk(a, 559, 288, 154, 54, 3),
            a.vis(pill(480, 456, "틀로 찍어 내면 기다리는 시간이 줄어요", GREEN, 18, True, 400), 4, 4)]
    caps = ["서버 .11이 고장 나 수리에 5일이 걸려요", "이미지로 새 서버를 만들어요", "헬스 체크를 통과하면 풀에 들어가요", "VM은 틀로 찍어 내듯 복제해요"]
    return frame(a, "수리를 5일이나 기다려야 할까?", "서버를 VM으로 돌리면 이미지에서 바로 만들 수 있어요", caps, "".join(body))


# 6 몰리는 시간에만 서버를 늘릴 수 있을까? -----------------------------------------------------------------
def p6():
    a = new()
    ys = (225, 297, 369)
    sbar = lambda x, y, pct, c: bar(x, y, 110, pct, c, 18)
    body = [person(60, 290) + line(100, 300, 160, 300, LINE, 3) + lbx(230, 300, "로드 밸런서", None, BLUE, 130, 56)
            + panel(380, "우리 서버", GREEN, 150, 260, 280) + panel(680, "클라우드", VIOLET, 150, 240, 280),
            "".join(line(295, 300, 400, y, LINE, 3) for y in ys),
            "".join(sv(450, y, f"서버 {l}", GREEN, 100) for y, l in zip(ys, (".11", ".12", ".13"))),
            a.vis("".join(sbar(510, y - 9, 40, GREEN) for y in ys) + vtext(510, 418, "평소 40%(가정)", 16, GREEN), 1, 1),
            a.vis("".join(sbar(510, y - 9, 100, RED) for y in ys) + vtext(510, 418, "점심 100%(가정)", 16, RED), 2, 3),
            mk(a, 396, 200, 232, 190, 2),
            a.vis(f'<path d="M230 268 V132 H800 V150" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="8 6"/>'
                  + sv(800, 240, "컨테이너", VIOLET, 130) + sv(800, 320, "컨테이너", VIOLET, 130) + check(890, 282)
                  + vtext(800, 418, "헬스 체크 통과 후 붙음", 16, VIOLET), 3, 4), mk(a, 695, 212, 210, 132, 3),
            a.vis("".join(sbar(510, y - 9, 60, GREEN) for y in ys) + vtext(510, 418, "나눠 맡아 60%(가정)", 16, GREEN)
                  + bar(745, 267, 110, 60, GREEN, 14) + bar(745, 347, 110, 60, GREEN, 14), 4, 4), mk(a, 396, 200, 232, 190, 4)]
    caps = ["평소엔 우리 서버만으로 충분해요", "점심에는 우리 서버가 꽉 차요", "클라우드에서 컨테이너를 늘려 붙여요", "넘치던 몫을 나눠 맡아 여유가 생겨요"]
    return frame(a, "몰리는 시간에만 서버를 늘릴 수 있을까?", "넘치는 몫만 클라우드에서 빌려 쓰는 안이에요", caps, "".join(body))


# 6b 클라우드로 늘리면 치르는 대가 세 가지 ----------------------------------------------------------------
def p6b():
    a = new()
    X, W = 80, 800
    top = (box(X, 130, 560, 44, GREEN, PANEL, 8, sw=3) + vtext(X + 280, 159, "평소 몫: 우리 서버", 18, GREEN)
           + box(X + 560, 130, 240, 44, VIOLET, PANEL, 8, sw=3) + vtext(X + 680, 159, "넘치는 몫: 클라우드", 18, VIOLET))
    cx = (60, 350, 640)
    cw, cy, ch = 260, 215, 235
    cards = [(ORANGE, "비용", "쓰는 만큼 계속 내요"), (BLUE, "시차", "서버가 늘기까지 몇 분(가정)"), (RED, "데이터 위치", "고객 예약 정보를 외부 인프라가 처리")]

    def icon(i, x, y):
        if i == 0:
            return f'<circle cx="{x}" cy="{y}" r="32" fill="{BG}" stroke="{ORANGE}" stroke-width="4"/>' + vtext(x, y + 11, "₩", 32, ORANGE)
        if i == 1:
            return (f'<circle cx="{x}" cy="{y}" r="32" fill="{BG}" stroke="{BLUE}" stroke-width="4"/>'
                    + line(x, y, x, y - 20, BLUE, 4) + line(x, y, x + 15, y + 8, BLUE, 4))
        return lock(x, y - 16, RED)
    body = [top]
    for i, (c, t, s) in enumerate(cards):
        x = cx[i]
        body.append(box(x, cy, cw, ch, MUTED, PANEL, 14, dash=True, sw=2) + vtext(x + cw / 2, cy + 130, "?", 52, MUTED))
        body.append(a.vis(box(x, cy, cw, ch, c, PANEL, 14, sw=3) + vtext(x + cw / 2, cy + 40, t, 24, c)
                          + icon(i, x + cw / 2, cy + 100) + vtext(x + cw / 2, cy + 190, s, 17, TXT), i + 2, 4))
        body.append(mk(a, x, cy, cw, ch, i + 2, 16))
    caps = ["평소 몫은 우리 서버, 넘치는 몫은 클라우드예요", "첫째, 쓰는 만큼 계속 내는 비용이에요", "둘째, 서버가 늘기까지 몇 분이 걸려요", "셋째, 고객 예약 정보가 외부 인프라에서 처리돼요"]
    return frame(a, "클라우드로 늘리면 무엇을 치를까?", "넘치는 몫을 빌리는 대신 세 가지 대가를 따져요", caps, "".join(body))


ITEMS = [
    # (file, title, alt, caption, after_paragraph, fn) grouped per Page
    [("u13-l02-p1-spof", "서버는 멀쩡한데 왜 멈췄을까?", "서버 세 대는 정상인데 앞의 로드 밸런서 한 대가 멈추면 손님이 서버에 닿지 못해, 한 곳이 멈추면 전체가 멈추는 단일 장애점이 됩니다.", "한 곳이 멈추면 전체가 멈추는 지점이 단일 장애점(SPOF)입니다.", 1, p1),
     ("u13-l02-p1b-availability", "99.9%는 얼마나 멈춰도 된다는 뜻일까?", "1년 365일 중 가용성 99.9%는 약 8.8시간, 99.99%는 약 53분까지 멈춰도 된다는 뜻으로, 숫자가 높을수록 멈춰도 되는 시간이 짧아집니다.", "가용성은 1년 중 정상으로 쓴 시간의 비율이라 99.9%는 약 8.8시간까지 멈출 수 있습니다.", 2, p1b)],
    [("u13-l02-p2-standby", "예비 장비는 평소에 쉬게 둘까?", "액티브/스탠바이에서 일하던 장비 A가 고장 나면 쉬던 장비 B가 일을 넘겨받지만(페일오버), 처리 성능은 한 대와 같습니다.", "액티브/스탠바이는 안전하지만 처리 성능이 한 대와 같습니다.", 1, p2),
     ("u13-l02-p2b-active", "둘이 같이 일하면 한 대가 빠질 때는?", "액티브/액티브에서 두 장비가 평소 60%씩 일하다 한 대가 고장 나면 남은 장비가 120%를 맡아 넘치므로, 평소 50% 이하로 써야 합니다.", "액티브/액티브는 한 대가 빠져도 버틸 여유까지 포함해 용량을 잡아야 합니다.", 3, p2b)],
    [("u13-l02-p3-vip", "장비가 바뀌어도 같은 주소로", "일하는 장비 A가 VIP를 맡고 하트비트를 보내다 멈추면 신호가 끊기고, 장비 B가 VIP 203.0.113.10:443을 넘겨받아 손님은 같은 주소를 계속 쓰는 모습입니다.", "VIP와 하트비트 덕분에 장비가 바뀌어도 바깥에서는 같은 주소로 이어집니다.", 2, p3),
     ("u13-l02-p3b-split", "신호선만 끊기면 주인이 둘이 돼요", "두 장비 사이 신호선만 끊기면 예비 장비 B도 A가 죽었다고 여겨 VIP를 가져가 두 주인이 생기고, 신호 경로를 이중으로 두어 막습니다.", "신호선만 끊겨도 둘 다 VIP를 주장하므로 신호 경로를 이중으로 둡니다.", 4, p3b)],
    [("u13-l02-p4-common", "두 대를 뒀는데 왜 같이 멈췄을까?", "장비 두 대가 같은 스위치에 연결돼 스위치가 멈추면 둘 다 끊기고, 스위치를 나눈 구성에서는 스위치 하나가 멈춰도 장비 B가 이어 가는 모습입니다.", "이중화의 핵심은 장비 개수가 아니라 공통 지점 없이 따로 고장 나는가입니다.", 2, p4)],
    [("u13-l02-p5-vm", "수리를 5일이나 기다려야 할까?", "서버 .11이 고장 나 수리에 5일이 걸리는 동안, VM 이미지로 새 서버 .14를 만들어 헬스 체크를 통과시킨 뒤 서버 풀에 넣는 모습입니다.", "VM 이미지로 서버를 복제하면 수리를 기다리는 시간을 줄일 수 있습니다.", 3, p5)],
    [("u13-l02-p6-cloud", "몰리는 시간에만 서버를 늘릴 수 있을까?", "점심에 우리 서버가 100%로 차면 클라우드의 컨테이너를 헬스 체크를 거쳐 서버 풀에 붙여 넘치던 몫을 나눠 맡고, 사용률이 60%로 내려갑니다(가정).", "넘치는 몫만 클라우드로 늘리되 헬스 체크를 통과한 서버만 붙입니다.", 2, p6),
     ("u13-l02-p6b-cost", "클라우드로 늘리면 무엇을 치를까?", "평소 몫은 우리 서버가 맡고 넘치는 몫을 클라우드로 늘리면 쓰는 만큼 내는 비용, 서버가 늘기까지의 몇 분 시차, 고객 예약 정보가 외부 인프라에서 처리되는 데이터 위치라는 세 가지 대가가 따릅니다.", "클라우드로 늘릴 때의 대가는 비용, 시차, 데이터 위치입니다.", 3, p6b)],
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for page in ITEMS:
        for f, *_, fn in page:
            write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", [[(f, t, al, c, ap) for f, t, al, c, ap, _ in page] for page in ITEMS])
    print("ok", sum(len(p) for p in ITEMS), "svgs")
