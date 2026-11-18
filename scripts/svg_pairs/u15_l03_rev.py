#!/usr/bin/env python3
"""Unit 15 Lesson 3 점검본: p2 p2b p3 p3b p4b p5 p6 (p1·p4는 기존 그림 유지). Run from repo root:
python3 scripts/svg_pairs/u15_l03_rev.py   (--svg-only: lesson.md는 건드리지 않음)

한 가지 예: 서버 구역 입구의 IPS·NIDS가 그룹웨어 서버(192.168.40.50:8080)로 가는 요청을 본다. 방어 장면만."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403
from u15_l00_common import mvi, bb

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"
GW = "192.168.40.50:8080"


def req(x, y, label, c=RED):
    """헤더+내용 패킷(글자 14px). 내용 칸에 label."""
    return (f'<rect x="{x - 50}" y="{y - 22}" width="38" height="44" rx="4" fill="{BLUE}"/>'
            f'<rect x="{x - 12}" y="{y - 22}" width="62" height="44" rx="4" fill="{c}"/>'
            + text(x - 31, y + 5, "헤더", 14, BG, 700) + text(x + 19, y + 5, label, 14, BG, 700))


def enc(x, y):
    return (f'<rect x="{x - 50}" y="{y - 22}" width="100" height="44" rx="4" fill="#2a2440" stroke="{VIOLET}" stroke-width="3"/>'
            + text(x, y + 5, "암호문", 15, VIOLET, 700))


def tag(x, y, s, c=MUTED, fs=17):
    return text(x, y, s, fs, c, 700, "start")


# 2 막을까, 알리기만 할까? (탐지했을 때) ---------------------------------------------------
def lanes(a, fail=False):
    """위: IPS(경로 안) 줄, 아래: NIDS(경로 밖, 스위치 미러링) 줄. 패킷은 장비 뒤에 그려 장비 아래로 지나가게 한다."""
    y1, y2 = 195, 375
    lines = (line(158, y1, 360, y1, LINE, 3, "6 5") + line(440, y1, 766, y1, LINE, 3, "6 5")
             + line(158, y2, 328, y2, LINE, 3, "6 5") + line(452, y2, 766, y2, LINE, 3, "6 5")
             + line(400, 320, 400, y2 - 20, VIOLET, 3, "6 5"))
    devs = (cloudi(90, y1, "인터넷") + node(400, y1, "IPS", GREEN, 90, 56) + server(800, y1, "그룹웨어 서버")
            + cloudi(90, y2, "인터넷") + switch(400, y2, "스위치") + node(400, 298, "NIDS", VIOLET, 100, 44) + server(800, y2, "그룹웨어 서버")
            + text(40, 128, "IPS: 경로 안(Inline)", 17, GREEN, 700, "start") + text(40, 295, "NIDS: 경로 밖(Out of path)", 17, VIOLET, 700, "start")
            + pill(495, 345, "복사본", VIOLET, 16, False, 80))
    return y1, y2, lines, devs


def p2():
    a = new()
    y1, y2, lines, devs = lanes(a)
    body = [lines,
            a.vis(a.move(req(0, 0, "공격"), [(230, y1), (300, y1)], 2, 0.1, 0.9), 1, 2),
            a.vis(a.move(req(0, 0, "공격"), [(230, y2), (300, y2)], 2, 0.1, 0.9), 1, 2),
            a.vis(mvi(a, 3, req(0, 0, "공격"), [(300, y2), (700, y2)], 0.05, 0.85), 3, 4),
            devs,
            st(a, 2, "", bb(400, y1, 100, 66)), a.vis(hl(*bb(400, 298, 110, 54)), 2, 2),
            st(a, 3, cross(400, 135), bb(400, 135, 50, 50), 4), P(a, 3, 530, 140, "바로 차단", GREEN, 16, False, 4),
            P(a, 3, 560, 298, "경보만 내요", ORANGE, 16, False, 4),
            P(a, 4, 555, 452, "복사본만으론 확실히 못 막아요", RED, 16)]
    caps = ["IPS는 길 한가운데, NIDS는 길 옆에 있어요", "같은 공격 요청이 두 장비에 보여요", "IPS는 막고, NIDS 쪽 원본은 그대로 가요", "복사본을 보는 NIDS는 확실히 막지 못해요"]
    return frame(a, "막을까, 알리기만 할까", "탐지했을 때 두 장비가 하는 일", caps, "".join(body))


def p2b():
    a = new()
    y1, y2, lines, devs = lanes(a)
    body = [lines,
            a.vis(mvi(a, 1, pk_(), [(230, y1), (700, y1)], 0.1, 0.9), 1, 1),
            a.vis(mvi(a, 1, pk_(), [(230, y2), (700, y2)], 0.1, 0.9), 1, 1),
            a.vis(req(300, y1, "정상", GREEN), 3, 3),
            a.vis(mvi(a, 3, req(0, 0, "정상", GREEN), [(230, y2), (700, y2)], 0.1, 0.9), 3, 3),
            devs,
            st(a, 2, cross(400, 135) + cross(485, 298), bb(400, 135, 50, 50), 4), a.vis(hl(*bb(485, 298, 50, 50)), 2, 2),
            P(a, 3, 580, 140, "통신이 끊길 수 있어요", RED, 16, False, 4),
            P(a, 3, 700, 298, "서비스는 계속, 탐지만 멈춰요", GREEN, 16, False, 4),
            P(a, 4, 480, 452, "고장 났을 때 통과·차단 설정을 확인해요", ORANGE, 16)]
    caps = ["평소에는 두 줄 모두 요청이 서버까지 가요", "두 장비가 모두 고장 났어요", "IPS 줄은 막히고, NIDS 줄은 계속 가요", "설명서에서 고장 났을 때 동작을 확인해요"]
    return frame(a, "장비가 고장 나면", "IPS와 NIDS의 영향이 서로 달라요", caps, "".join(body))


def pk_():
    return req(0, 0, "정상", GREEN)


# 3 공격의 '지문'은 어떻게 찾을까? --------------------------------------------------------
def p3():
    a, Y = new(), 345
    lines = line(158, Y, 435, Y, LINE, 3, "6 5") + line(525, Y, 766, Y, LINE, 3, "6 5") + line(480, 212, 480, Y - 30, VIOLET, 2, "6 5")
    card = (box(330, 128, 300, 84, VIOLET, PANEL, 8, sw=3) + text(480, 154, "규칙: 대상 " + GW, 15, TXT, 700)
            + a.vis(text(480, 190, "찾을 패턴: 패턴 A", 16, VIOLET, 700), 1, 3)
            + a.vis(text(480, 190, "패턴 A · 패턴 B", 16, VIOLET, 700), 4, 4))
    devs = cloudi(90, Y, "인터넷") + node(480, Y, "IPS", GREEN, 90, 56) + server(830, Y, "그룹웨어 서버", sub=GW)
    body = [lines, a.vis(mvi(a, 2, req(0, 0, "패턴 A"), [(230, Y), (385, Y)], 0.1, 0.8), 2, 2),
            a.vis(mvi(a, 3, req(0, 0, "패턴 B"), [(230, Y), (720, Y)], 0.1, 0.9), 3, 3),
            devs, st(a, 1, card, bb(480, 170, 300, 84)),
            st(a, 2, check(480, 290), bb(480, 290, 50, 50), 2), P(a, 2, 480, 420, "패턴 일치 → 탐지", GREEN, 17, False, 2),
            st(a, 3, cross(480, 290), bb(480, 290, 50, 50), 3), P(a, 3, 600, 420, "새 공격은 놓쳐요", RED, 17, False, 3),
            a.vis(hl(*bb(480, 170, 300, 84)), 4, 4), P(a, 4, 480, 425, "새 공격이 알려지면 규칙을 갱신해요", ORANGE, 17)]
    caps = ["규칙은 볼 대상과 찾을 패턴을 함께 적어요", "알려진 패턴 A는 규칙과 일치해 탐지해요", "규칙에 없는 패턴 B는 그냥 지나가요", "새 공격은 규칙을 갱신해야 잡혀요"]
    return frame(a, "공격의 지문 찾기", "시그니처는 알려진 패턴만 찾아요", caps, "".join(body))


# 3b TLS가 풀리는 위치 -----------------------------------------------------------------------
def p3b():
    a = new()
    ya, yb = 205, 385

    def row(Y, order):
        mid = {"ips": node(0, 0, "IPS", GREEN, 90, 56), "tls": node(0, 0, "TLS 종료", BLUE, 96, 56, 16)}
        xs = (380, 600)
        s = cloudi(90, Y, "인터넷") + server(840, Y, "그룹웨어 서버")
        for x, k in zip(xs, order):
            s += f'<g transform="translate({x},{Y})">{mid[k]}</g>'
        return s

    lines = "".join(line(158, Y, 806, Y, LINE, 3, "6 5") for Y in (ya, yb))
    devs = (row(ya, ("ips", "tls")) + row(yb, ("tls", "ips"))
            + text(40, 140, "A. TLS 종료 앞에 둔 IPS", 17, ORANGE, 700, "start") + text(40, 316, "B. TLS 종료 뒤, 서버 구역 입구의 IPS", 17, GREEN, 700, "start"))
    body = [lines,
            a.vis(a.move(enc(0, 0), [(220, ya), (300, ya)], 2, 0.1, 0.8), 1, 4),
            a.vis(a.move(enc(0, 0), [(220, yb), (380, yb)], 3, 0.05, 0.45), 1, 3),
            a.vis(a.move(req(0, 0, "패턴 A"), [(380, yb), (500, yb)], 3, 0.5, 0.9), 3, 4),
            devs,
            st(a, 2, cross(380, 140) + "", bb(380, 140, 50, 50), 4), P(a, 2, 380, 262, "암호문이라 내용 패턴은 못 읽어요", RED, 16, False, 4),
            P(a, 3, 380, 448, "여기서 TLS가 끝나요", BLUE, 16, False, 3),
            st(a, 4, check(600, 325), bb(600, 325, 50, 50)), P(a, 4, 600, 448, "풀린 요청이라 패턴을 읽어요", GREEN, 16)]
    caps = ["같은 암호문 요청이 두 줄에 도착해요", "TLS 종료 앞의 IPS에는 암호문만 보여요", "B줄은 TLS가 먼저 풀려 평문이 돼요", "IPS는 TLS가 풀린 구간에 둬야 읽어요"]
    return frame(a, "TLS가 풀리는 위치", "센서가 어디 있느냐가 보이는 것을 정해요", caps, "".join(body))


# 4b 오탐·미탐·정탐 -------------------------------------------------------------------------
def p4b():
    a, Y = new(), 290
    lines = line(158, Y, 435, Y, LINE, 3, "6 5") + line(525, Y, 766, Y, LINE, 3, "6 5")
    devs = node(90, Y, "요청", BLUE, 100, 56) + node(480, Y, "IPS", GREEN, 90, 56) + server(830, Y, "그룹웨어 서버")
    body = [lines,
            a.vis(mvi(a, 1, req(0, 0, "공격"), [(220, Y), (385, Y)], 0.1, 0.8), 1, 1),
            a.vis(mvi(a, 2, req(0, 0, "정상", GREEN), [(220, Y), (385, Y)], 0.1, 0.8), 2, 2),
            a.vis(mvi(a, 3, req(0, 0, "공격"), [(220, Y), (720, Y)], 0.1, 0.9), 3, 3),
            devs,
            P(a, 1, 480, 205, "울림", ORANGE, 17, False, 1), P(a, 1, 480, 375, "정탐 (공격을 맞게 잡음)", GREEN, 17, False, 1),
            P(a, 2, 480, 205, "울림", ORANGE, 17, False, 2), P(a, 2, 480, 375, "오탐 (정상을 공격으로 봄)", RED, 17, False, 2),
            P(a, 3, 480, 205, "안 울림", MUTED, 17, False, 3), P(a, 3, 480, 375, "미탐 (공격을 놓침)", RED, 17, False, 3),
            P(a, 4, 250, 400, "느슨한 규칙: 오탐↓ 미탐↑", BLUE, 17), P(a, 4, 710, 400, "엄격한 규칙: 미탐↓ 오탐↑", VIOLET, 17)]
    caps = ["공격 요청에 IPS가 울리면 정탐이에요", "정상 요청에 울리면 오탐이에요", "공격 요청에 안 울리면 미탐이에요", "규칙은 느슨하게도 엄격하게도 대가가 있어요"]
    return frame(a, "울렸나, 안 울렸나", "요청과 경보의 네 가지 조합", caps, "".join(body))


# 5 처음 보는 악성 파일은 어떻게 잡을까? ----------------------------------------------------
def p5():
    a, Y = new(), 330
    lines = line(135, Y, 240, Y, LINE, 3, "6 5") + line(360, Y, 800, Y, LINE, 3, "6 5")
    devs = doc(90, Y, MUTED, "첨부 파일") + node(300, Y, "보안 장비", BLUE, 120, 60, 17) + person(850, Y - 10, "박 팀장")
    zn = zone(410, 130, 230, 135, "샌드박스(유리 방)", VIOLET, 17)
    body = [lines, devs,
            a.vis(mvi(a, 1, packet(0, 0, MUTED), [(140, Y), (200, Y)], 0.1, 0.8), 1, 1),
            P(a, 1, 300, 410, "시그니처에 안 걸려요", BLUE, 16, False, 1),
            st(a, 2, zn + doc(525, 222, BLUE).replace('<rect', '<rect', 1), bb(525, 197, 230, 135)),
            a.vis(mvi(a, 2, packet(0, 0, BLUE), [(300, Y - 36), (300, 215), (440, 215)], 0.1, 0.85), 2, 2),
            P(a, 2, 580, 375, "원본 전달은 보류", ORANGE, 16, False, 2),
            st(a, 3, line(640, 215, 750, 195, RED, 3, "7 5") + cloudi(820, 190, "낯선 주소", RED).replace('rx="68"', 'rx="60"'), bb(820, 190, 130, 90), 4),
            P(a, 3, 770, 262, "접속 시도", RED, 16, False, 3, False),
            st(a, 3, cross(580, Y), bb(580, Y, 50, 50), 4), P(a, 3, 580, 375, "막고 경보를 내요", RED, 16, False, 3),
            P(a, 4, 480, 440, "시간이 걸리고, 얌전한 파일은 놓칠 수 있어요", ORANGE, 16)]
    caps = ["처음 나온 첨부 파일은 대조할 지문이 없어요", "복사본을 샌드박스에서 실행하고 원본은 보류해요", "복사본이 낯선 주소로 접속하려 해요", "분석이 느리고 얌전한 파일은 놓칠 수 있어요"]
    return frame(a, "처음 보는 악성 파일", "격리된 곳에서 먼저 실행해 봐요", caps, "".join(body))


# 6 남들이 이미 아는 악성일까? ---------------------------------------------------------------
def p6():
    a = new()
    cy = 285
    base = (doc(90, 190, BLUE, "파일 요약값") + cloudi(400, cy, "평판 정보", BLUE) + line(140, 215, 335, 262, LINE, 3, "6 5"))
    cellw = 270
    c1, c2, c3 = 150, 258, 375
    body = [base, a.vis(mvi(a, 1, packet(0, 0, BLUE), [(150, 212), (330, 258)], 0.1, 0.9), 1, 1),
            P(a, 1, 250, 150, "알려졌는지 조회", BLUE, 17, False, 1),
            st(a, 2, line(465, 265, 625, c1 + 28, RED, 3, "7 5") + cell(630, c1, cellw, 56, "알려진 악성 → 차단", RED, 17), (630, c1, cellw, 56), 4),
            st(a, 3, line(468, cy, 625, c2 + 28, VIOLET, 3, "7 5") + cell(630, c2, cellw, 56, "모르는 파일 → 샌드박스", VIOLET, 17), (630, c2, cellw, 56), 4),
            st(a, 4, cloudi(90, 390, "접속 주소", GREEN) + line(150, 375, 340, 315, GREEN, 3, "7 5") + line(465, 310, 625, c3 + 28, GREEN, 3, "7 5")
               + cell(630, c3, cellw, 56, "이상 행위·로그와 함께", GREEN, 17), (630, c3, cellw, 56)),
            P(a, 4, 400, 450, "샌드박스는 파일에만 써요", ORANGE, 16)]
    caps = ["파일 요약값이 이미 알려졌는지 조회해요", "알려진 악성이면 바로 막아요", "모르는 파일은 샌드박스로 넘겨요", "접속 주소는 평판을 보고, 모르면 다른 신호도 봐요"]
    return frame(a, "남들이 이미 아는 악성일까", "평판은 외부 정보를 빌려요", caps, "".join(body))


ITEMS = {
    "p2": ("u15-l03-p2-ips-vs-nids", "막을까, 알리기만 할까", "경로 안의 IPS는 공격 요청을 바로 차단하고, 경로 밖 NIDS는 복사본으로 탐지해 경보만 내며 원본은 서버로 그대로 가는 모습을 위아래 두 줄로 비교합니다.", "IPS는 막을 수 있고, 복사본을 보는 NIDS는 경보가 기본이라 확실히 막지 못합니다.", 1, p2),
    "p2b": ("u15-l03-p2b-failure", "장비가 고장 나면", "평소에는 두 줄 모두 요청이 서버까지 가다가 장비가 고장 나면, 경로 안 IPS 줄은 통신이 끊길 수 있고 경로 밖 NIDS 줄은 서비스가 계속되며 탐지만 멈추는 모습입니다.", "IPS는 고장 나면 통신이 끊길 수 있고, NIDS는 서비스는 계속되지만 탐지가 멈춥니다.", 2, p2b),
    "p3": ("u15-l03-p3-signature", "공격의 지문 찾기", "규칙에 적힌 패턴 A가 든 공격은 IPS가 탐지하고, 규칙에 없는 패턴 B의 새 공격은 놓치며, 새 공격이 알려지면 규칙을 갱신해야 하는 모습입니다.", "시그니처 검사는 규칙에 적힌 알려진 패턴만 찾습니다.", 2, p3),
    "p3b": ("u15-l03-p3b-tls-position", "TLS가 풀리는 위치", "TLS 종료 앞에 둔 IPS는 암호문만 보아 내용 패턴을 못 읽고, TLS 종료 뒤 서버 구역 입구의 IPS는 풀린 평문 요청에서 패턴을 읽는 모습을 위아래 두 줄로 비교합니다.", "센서가 TLS 종료 앞에 있는지 뒤에 있는지가 시그니처 검사 범위를 정합니다.", 5, p3b),
    "p4b": ("u15-l03-p4b-outcomes", "울렸나, 안 울렸나", "같은 IPS에 공격 요청이 울리면 정탐, 정상 요청이 울리면 오탐, 공격 요청이 안 울리면 미탐이고, 규칙이 느슨하면 오탐이 줄고 미탐이 늘며 엄격하면 반대인 모습입니다.", "요청과 경보의 조합에 따라 정탐·오탐·미탐이 갈립니다.", 2, p4b),
    "p5": ("u15-l03-p5-sandbox", "처음 보는 악성 파일", "시그니처에 걸리지 않은 첨부 파일의 복사본을 보안 장비가 샌드박스로 보내 실행하고 원본 전달은 보류하며, 복사본이 낯선 주소로 접속하려 하면 막고 경보를 내지만 느리고 얌전한 파일은 놓칠 수 있습니다.", "샌드박스는 모르는 파일을 격리된 곳에서 먼저 실행해 보지만 느리고 얌전한 파일은 놓칠 수 있습니다.", 2, p5),
    "p6": ("u15-l03-p6-reputation", "남들이 이미 아는 악성일까", "파일 요약값을 평판 정보로 조회해 알려진 악성은 막고, 모르는 파일은 샌드박스로 넘기며, 접속 주소는 주소 평판을 보되 모르면 이상 행위·로그 같은 다른 신호와 함께 보는 모습입니다.", "평판은 외부 정보를 빌려 알려진 악성을 거르고, 샌드박스는 파일에만 씁니다.", 4, p6),
}

if __name__ == "__main__":
    for key, (f, _t, _al, _c, _ap, fn) in ITEMS.items():
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        pages = [None] * 6
        pages[1] = [ITEMS["p2"][:5], ITEMS["p2b"][:5]]
        pages[2] = [ITEMS["p3"][:5], ITEMS["p3b"][:5]]
        import u15_l03_detect as old  # p4 그림은 기존 파일 그대로, Page에서 위치만 옮김
        pages[3] = [ITEMS["p4b"][:5], old.ITEMS[3][:4] + (5,)]
        pages[4] = [ITEMS["p5"][:5]]
        pages[5] = [ITEMS["p6"][:5]]
        wire_items(LESSON / "lesson.md", pages)
    print("ok", len(ITEMS), "svgs")
