#!/usr/bin/env python3
"""Unit 15 Lesson 1 (NAC): 예시 SVG 6개(Page당 1개, 4단계). Run from repo root:
python3 scripts/svg_pairs/u15_l01_nac.py   (--svg-only: lesson.md는 건드리지 않음)

하나의 예: 회의실 랜 포트에 꽂힌 박 팀장의 개인 노트북 → 사내 AI 서버(192.168.10.50)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

LESSON = lesson_dir(1)
OUT = LESSON / "assets" / "animations"


def chip(x, y, w, h, l1, l2, c):
    return (box(x, y, w, h, c, PANEL, 8, sw=3) + text(x + w / 2, y + 34, l1, 17, TXT, 700) + text(x + w / 2, y + 66, l2, 20, c, 700))


# 1 보안 점검, 무엇부터 물어야 할까? -------------------------------------------------
def p1():
    a, Y = new(), 310
    base = (laptop(120, Y, "박 팀장 노트북") + line(180, Y, 345, Y, LINE, 4, "8 6") + switch(400, Y, "회의실 스위치")
            + line(455, Y, 755, Y, LINE, 4, "8 6") + server(800, Y, "AI 서버", sub="192.168.10.50"))
    qs = [("① 누가 들어오나", "NAC", ORANGE), ("② 무엇을 통과시키나", "방화벽", BLUE), ("③ 무엇이 공격인가", "IPS·NIDS", VIOLET), ("④ 무슨 일이 있었나", "로그", GREEN)]
    body = [a.vis(base, 1, 3),
            pk(a, 2, [(150, Y), (285, Y)], BLUE), P(a, 2, 260, 225, "확인 없이 주소를 받아요", BLUE, 16, False, 3),
            pk(a, 3, [(430, Y), (750, Y)], ORANGE), st(a, 3, pill(790, 205, "관리 화면까지 열려요", RED, 16, False, 190) + cross(790, 165), (695, 180, 190, 32), 3)]
    for i, (q, d, c) in enumerate(qs):
        body.append(a.vis(chip(40 + i * 220, 190, 205, 86, q, d, c), 4, 4))
    body.append(a.vis(hl(40, 190, 205, 86), 4, 4))
    body.append(P(a, 4, 480, 345, "이번 Lesson은 첫 질문 NAC", ORANGE, 18, False, 4, False))
    caps = ["회의실 랜 포트에 개인 노트북이 꽂혀 있어요", "확인 없이 주소를 받고 사내망에 붙어요", "AI 서버 관리 화면까지 열리는 구멍이에요", "점검을 네 질문으로 쪼개고 ①부터 봐요"]
    return frame(a, "보안 점검, 무엇부터?", "회의실에서 발견한 첫 번째 구멍", caps, "".join(body))


# 2 회사 기기인지 무엇으로 알아볼까? -------------------------------------------------
def p2():
    a = new()
    head, rows = rtable(50, 150, ["IP", "MAC"], [["192.168.10.41", "지우 PC의 MAC"], ["192.168.10.42", "박 팀장 PC의 MAC"], ["미등록 기기", "장부에 없음"]],
                        [210, 200], [GREEN, GREEN, RED], 14)
    base = (switch(720, 290, "스위치") + line(720, 306, 720, 345, LINE, 3) + line(620, 345, 720, 345, LINE, 3)
            + line(620, 345, 620, 365, LINE, 3) + line(720, 345, 720, 365, LINE, 3)
            + pc(620, 400, "지우 PC") + pc(720, 400, "박 팀장 PC"))
    body = [P(a, 1, 255, 125, "IP·MAC 장부", GREEN, 16, False, 4, False), head, a.vis(rows[0][0] + rows[1][0], 1, 4), a.vis(base, 1, 4),
            st(a, 2, eye(570, 215) + text(570, 252, "Probe", 15, MUTED), bb(570, 232, 92, 62)),
            a.vis(line(600, 225, 700, 272, VIOLET, 2, "6 5"), 2, 4),
            P(a, 2, 760, 175, "192.168.10.250", VIOLET, 15, False, 2, False),
            st(a, 3, rows[2][0], rows[2][1]), st(a, 3, line(720, 345, 840, 345, LINE, 3) + line(840, 345, 840, 365, LINE, 3) + laptop(840, 400, "미등록 기기", RED), None),
            P(a, 4, 255, 425, "MAC은 바꿀 수 있어 보조 도구예요", BLUE, 16)]
    caps = ["회사 기기마다 IP·MAC 쌍을 장부에 적어요", "Probe가 경로 밖에서 어떤 쌍이 보이는지 봐요", "장부에 없는 쌍이 나타나면 미허가로 봐요", "MAC은 바꿀 수 있어 일단 알아보는 도구예요"]
    return frame(a, "회사 기기인지 알아보기", "IP·MAC 쌍을 장부와 맞춰 봐요", caps, "".join(body))


# 3 포트를 내리면 끝일까? ------------------------------------------------------------
def p3():
    a, Y = new(), 290
    base = (laptop(110, Y, "노트북") + line(170, Y, 365, Y, LINE, 4) + switch(420, Y, "2층 스위치") + node(420, 175, "NAC", ORANGE, 90, 50)
            + line(420, 200, 420, 272, ORANGE, 2, "6 5"))
    body = [base,
            P(a, 2, 420, 237, "이 포트를 내려라", BLUE, 15),
            st(a, 3, cross(300, Y), bb(300, Y, 50, 50)), P(a, 3, 160, 190, "케이블 연결 안 됨", RED, 15, False, 3, False),
            a.vis(pc(110, 410, "정상 PC") + line(170, 410, 215, 410, LINE, 4) + line(215, 410, 215, Y, LINE, 4) + cross(215, 350), 4, 4),
            P(a, 4, 630, 410, "같은 포트 뒤 기기도 함께 끊겨요", RED, 16)]
    caps = ["Probe가 장부에 없는 노트북을 찾았어요", "NAC가 스위치에 포트를 내리라고 지시해요", "링크가 끊겨 노트북에는 이유도 안 보여요", "한 포트 뒤 정상 기기까지 함께 끊겨요"]
    return frame(a, "포트를 내리면 끝일까?", "확실하지만 대가가 있는 차단", caps, "".join(body))


# 4 접속하자마자 안내 페이지가 뜨는 이유는? ---------------------------------------------
def p4():
    a, Y = new(), 320
    base = (laptop(100, Y, "박 팀장 노트북") + line(160, Y, 245, Y, LINE, 4) + switch(300, Y, "스위치") + line(355, Y, 745, Y, LINE, 4, "8 6")
            + cloudi(810, Y, "웹 서버") + eye(300, 205) + text(300, 240, "Probe", 15, MUTED) + line(300, 252, 300, 296, VIOLET, 2, "6 5"))
    body = [base,
            pk(a, 1, [(140, Y), (300, Y), (760, Y)], BLUE, 0.05, 0.95), P(a, 1, 560, 255, "웹사이트 열기", BLUE, 16, False, 1, False),
            mvi(a, 2, packet(0, 0, GREEN), [(320, 205), (150, 205), (110, 270)], 0.1, 0.9), P(a, 2, 560, 195, "안내 페이지로 가세요 (3XX)", GREEN, 16, False, 2),
            st(a, 3, box(40, 125, 190, 52, GREEN, PANEL, 8, sw=3) + text(135, 158, "기기 등록 안내", 17, GREEN, 700) + check(250, 151), bb(135, 151, 200, 60)),
            P(a, 4, 640, 420, "HTTPS·앱 통신에는 약해요", RED, 16)]
    caps = ["박 팀장이 웹사이트를 열어요", "Probe가 더 빨리 안내 페이지 응답을 보내요", "막힌 게 아니라 등록 안내를 받아요", "HTTPS와 앱 통신에는 쓰기 어려워요"]
    return frame(a, "접속하자마자 안내 페이지", "웹 요청에 먼저 끼어드는 안내", caps, "".join(body))


# 5 들어오기 전에 신분을 확인하려면? -------------------------------------------------
def p5():
    a, Y = new(), 310
    base = (laptop(110, Y, "노트북") + line(170, Y, 305, Y, LINE, 4) + switch(360, Y, "스위치") + server(640, 150, "RADIUS 서버")
            + line(380, 290, 600, 180, LINE, 3, "6 5") + zone(700, 220, 220, 180, "사내망", GREEN) + server(810, 330, "AI 서버") + line(412, Y, 700, Y, LINE, 4))
    body = [base, a.vis(lock(560, Y - 14, RED) + text(560, Y + 50, "포트 닫힘", 15, RED, 700), 1, 3),
            pk(a, 2, [(150, Y), (285, Y)], BLUE), P(a, 2, 235, 235, "계정·인증서 제출", BLUE, 15),
            pk(a, 3, [(390, 285), (555, 200)], ORANGE), st(a, 3, check(725, 150), bb(725, 150, 50, 50)),
            st(a, 4, line(412, Y, 700, Y, GREEN, 6) + pill(556, Y - 30, "포트 열림", GREEN, 16, True, 110), (501, Y - 54, 110, 32)),
            P(a, 4, 480, 440, "이 사람·이 기기로 확인해요", GREEN, 17, False, 4, False)]
    caps = ["인증을 마칠 때까지 포트가 닫혀 있어요", "스위치가 신원을 요구하고 노트북이 보내요", "RADIUS 서버가 신원이 맞는지 확인해요", "확인된 기기만 포트가 열려요"]
    return frame(a, "들어오기 전에 신분 확인", "802.1X와 RADIUS", caps, "".join(body))


# 6 몰래 켠 와이파이는 누가 찾을까? ---------------------------------------------------
def p6():
    a = new()
    base = (zone(40, 150, 330, 270, "사내망", GREEN) + pc(205, 310, "사내 PC") + cloudi(830, 230, "인터넷") + phone(600, 340, "핫스팟 폰")
            + line(655, 310, 770, 250, LINE, 3, "6 5"))
    body = [base,
            st(a, 2, line(245, 300, 580, 335, RED, 4, "8 6") + pill(410, 300, "샛길", RED, 16, True, 70), (375, 283, 70, 32)),
            st(a, 3, eye(480, 175) + text(480, 212, "WIPS 센서", 15, MUTED), bb(480, 190, 110, 66)),
            P(a, 3, 740, 175, "허가 목록에 없는 연결", ORANGE, 16, False, 3, False),
            P(a, 4, 480, 455, "경보는 사람이 확인할 후보예요", GREEN, 17)]
    caps = ["사내 PC가 랜에 꽂힌 채 핫스팟도 써요", "사내망과 바깥을 잇는 샛길이 생겨요", "천장 WIPS 센서가 전파로 허가 밖 연결을 찾아요", "경보를 보고 사람이 확인해 막아요"]
    return frame(a, "몰래 켠 와이파이", "NAC가 못 보는 무선 샛길", caps, "".join(body))


ITEMS = [
    ("u15-l01-p1-four-questions", "보안 점검, 무엇부터?", "회의실 랜 포트의 박 팀장 노트북이 확인 없이 주소를 받아 AI 서버 관리 화면까지 닿고, 점검을 네 질문으로 쪼개 첫 질문 NAC부터 보는 모습입니다.", "점검을 네 질문으로 쪼개면 첫 질문은 누가 들어오나, 곧 NAC입니다.", 1, p1),
    ("u15-l01-p2-ledger-probe", "회사 기기인지 알아보기", "IP·MAC 장부에 적은 회사 PC와 달리, Probe가 경로 밖에서 본 장부에 없는 쌍을 미허가 기기로 보는 모습입니다.", "장부와 Probe로 미등록 기기를 알아보지만 MAC은 바꿀 수 있어 보조 도구입니다.", 2, p2),
    ("u15-l01-p3-port-down", "포트를 내리면 끝일까?", "NAC가 스위치에 포트를 내리라고 지시하면 링크가 끊기고, 같은 포트 뒤의 정상 기기까지 함께 끊기는 대가를 보여 줍니다.", "포트 차단은 확실하지만 포트 뒤 기기가 모두 끊기고 이유를 알리지 못합니다.", 2, p3),
    ("u15-l01-p4-redirect-page", "접속하자마자 안내 페이지", "Probe가 웹 요청에 먼저 안내 페이지 응답을 보내 박 팀장 노트북에 기기 등록 안내가 뜨는 모습입니다.", "안내 페이지 방식은 사용자 안내에는 강하지만 HTTPS와 앱 통신에는 약합니다.", 1, p4),
    ("u15-l01-p5-8021x", "들어오기 전에 신분 확인", "노트북이 신원을 내면 스위치가 RADIUS 서버에 확인하고, 통과하면 포트가 열려 사내망에 들어갑니다.", "802.1X는 인증을 마친 기기만 사내망에 들입니다.", 3, p5),
    ("u15-l01-p6-wips", "몰래 켠 와이파이", "사내 PC가 랜과 핫스팟에 동시에 붙어 생긴 샛길을 WIPS 센서가 전파로 찾아 경보하는 모습입니다.", "허가 없는 무선 사용은 WIPS가 찾고, 경보는 사람이 확인할 후보입니다.", 3, p6),
]
assert len(ITEMS) == 6

if __name__ == "__main__":
    build(OUT, ITEMS)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", ITEMS)
    print("ok", len(ITEMS), "svgs")
