#!/usr/bin/env python3
"""Unit 15 Lesson 1 (NAC) SVG 점검 후 고친 그림: Page 1·2·3·6 (Page 4·5는 기존 u15_l01_nac.py 그림 유지).
Run from repo root: python3 scripts/svg_pairs/u15_l01_rev.py   (--svg-only: lesson.md는 건드리지 않음)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403
import u15_l01_nac as old

LESSON = lesson_dir(1)
OUT = LESSON / "assets" / "animations"


# 1 보안 점검, 무엇부터 물어야 할까? : 4단계에서 장면을 남기고 ①만 크게, ②~④는 작게 ------------------
def p1():
    a, Y = new(), 330
    base = (laptop(120, Y, "박 팀장 노트북") + line(180, Y, 345, Y, LINE, 4, "8 6") + switch(400, Y, "회의실 스위치")
            + line(455, Y, 755, Y, LINE, 4, "8 6") + server(800, Y, "그룹웨어 서버", sub="192.168.10.50"))
    q1 = (box(40, 135, 230, 76, ORANGE, PANEL, 8, sw=3) + text(155, 168, "① 누가 들어오나", 18, TXT, 700) + text(155, 197, "NAC", 22, ORANGE, 700))
    small = "".join(box(300 + i * 200, 149, 185, 48, LINE, PANEL, 8) + text(392 + i * 200, 180, s, 17, MUTED, 700)
                     for i, s in enumerate(["② 방화벽", "③ IPS·NIDS", "④ 로그"]))
    body = [base,
            pk(a, 2, [(150, Y), (285, Y)], BLUE), P(a, 2, 260, 255, "확인 없이 주소를 받아요", BLUE, 16, False, 3),
            pk(a, 3, [(430, Y), (750, Y)], ORANGE),
            st(a, 3, pill(800, 245, "관리 화면까지 열려요", RED, 16, False, 190) + cross(800, 205), None, 3),
            a.vis(q1 + small + line(140, 211, 122, 286, ORANGE, 3, "6 5"), 4, 4), a.vis(hl(40, 135, 230, 76), 4, 4)]
    caps = ["회의실 랜 포트에 개인 노트북이 꽂혀 있어요", "확인 없이 주소를 받고 사내망에 붙어요", "그룹웨어 서버 관리 화면까지 열리는 구멍이에요", "점검을 네 질문으로 쪼개고 ①부터 봐요"]
    return frame(a, "보안 점검, 무엇부터?", "회의실에서 발견한 첫 번째 구멍", caps, "".join(body))


# 2 회사 기기인지 무엇으로 알아볼까? : 스위치 라벨 겹침 수정, 복사본 표시, 글자 16px ----------------------
def p2():
    a = new()
    head, rows = rtable(50, 150, ["IP", "MAC"], [["192.168.10.41", "지우 PC의 MAC"], ["192.168.10.42", "박 팀장 PC의 MAC"], ["미등록 기기", "장부에 없음"]],
                        [210, 200], [GREEN, GREEN, RED], 16)
    base = (switch(720, 290, "") + text(786, 296, "스위치", 16, MUTED, anchor="start") + line(720, 306, 720, 345, LINE, 3) + line(620, 345, 720, 345, LINE, 3)
            + line(620, 345, 620, 365, LINE, 3) + line(720, 345, 720, 365, LINE, 3)
            + pc(620, 400, "지우 PC") + pc(720, 400, "박 팀장 PC"))
    body = [P(a, 1, 255, 125, "IP·MAC 장부", GREEN, 16, False, 4, False), head, a.vis(rows[0][0] + rows[1][0], 1, 4), a.vis(base, 1, 4),
            st(a, 2, eye(570, 215) + text(570, 252, "Probe", 16, MUTED) + line(596, 225, 700, 272, VIOLET, 2, "6 5")
               + pill(662, 254, "복사본", VIOLET, 16, True, 74), bb(565, 232, 100, 76)),
            P(a, 2, 790, 190, "192.168.10.250", VIOLET, 16, False, 2, False),
            st(a, 3, rows[2][0], rows[2][1]), st(a, 3, line(720, 345, 840, 345, LINE, 3) + line(840, 345, 840, 365, LINE, 3) + laptop(840, 400, "미등록 기기", RED), None),
            P(a, 4, 255, 425, "MAC은 바꿀 수 있어 보조 도구예요", BLUE, 16)]
    caps = ["회사 기기마다 IP·MAC 쌍을 장부에 적어요", "Probe가 경로 밖에서 어떤 쌍이 보이는지 봐요", "장부에 없는 쌍이 나타나면 미허가로 봐요", "MAC은 바꿀 수 있어 일단 알아보는 도구예요"]
    return frame(a, "회사 기기인지 알아보기", "IP·MAC 쌍을 장부와 맞춰 봐요", caps, "".join(body))


# 3 포트를 내리면 끝일까? : 정상 PC를 처음부터 같은 포트 뒤(소형 스위치)에 둔다 -------------------------
def p3():
    a = new()
    SX, SY = 620, 300
    base = (laptop(110, 215, "노트북") + pc(110, 385, "정상 PC")
            + line(170, 215, 230, 215, LINE, 4) + line(170, 385, 230, 385, LINE, 4) + line(230, 215, 230, 385, LINE, 4) + line(230, 300, 248, 300, LINE, 4)
            + switch(300, 300, "") + text(300, 345, "소형 스위치", 16, MUTED)
            + line(352, 300, SX - 52, 300, LINE, 4) + switch(SX, SY, "2층 스위치")
            + node(SX, 160, "NAC", ORANGE, 90, 50) + line(SX, 185, SX, SY - 18, ORANGE, 2, "6 5")
            + eye(820, 160) + text(820, 200, "Probe", 16, MUTED) + line(794, 160, SX + 45, 160, VIOLET, 2, "6 5"))
    body = [base,
            P(a, 1, 110, 145, "장부에 없는 기기", RED, 16, False, 1),
            P(a, 2, SX, 237, "이 포트를 내려라", BLUE, 16),
            st(a, 3, cross(460, 300), bb(460, 300, 50, 50)), P(a, 3, 110, 145, "케이블 연결 안 됨", RED, 16, False, 4, False),
            P(a, 4, 110, 318, "함께 끊겨요", RED, 16)]
    caps = ["Probe가 장부에 없는 노트북을 찾았어요", "NAC가 스위치에 포트를 내리라고 지시해요", "링크가 끊겨 노트북에는 이유도 안 보여요", "한 포트 뒤 정상 기기까지 함께 끊겨요"]
    return frame(a, "포트를 내리면 끝일까?", "확실하지만 대가가 있는 차단", caps, "".join(body))


# 6 몰래 켠 와이파이는 누가 찾을까? : 1단계에 랜선 연결 표시, 센서가 샛길을 직접 본다, 4단계는 확인 후보 -----
def p6():
    a = new()
    base = (zone(40, 150, 310, 270, "사내망", GREEN) + switch(195, 222, "") + line(195, 238, 195, 274, GREEN, 3) + text(212, 262, "랜선", 16, MUTED, anchor="start")
            + pc(195, 310, "사내 PC") + cloudi(850, 220, "인터넷") + phone(640, 340, "핫스팟 폰") + line(672, 305, 795, 245, LINE, 3, "6 5"))
    body = [base,
            st(a, 2, line(235, 305, 618, 335, RED, 4, "8 6") + pill(400, 315, "샛길", RED, 16, True, 70), (365, 298, 70, 32)),
            st(a, 3, eye(480, 185) + text(480, 227, "WIPS 센서", 16, MUTED) + line(480, 245, 480, 318, VIOLET, 2, "6 5"), bb(480, 205, 120, 80), 4),
            P(a, 3, 470, 395, "허가 목록에 없는 연결", ORANGE, 16, False, 3, False),
            st(a, 4, ask(520, 285), None),
            P(a, 4, 480, 452, "경보는 사람이 확인할 후보예요", GREEN, 17)]
    caps = ["사내 PC가 랜에 꽂힌 채 핫스팟도 써요", "사내망과 바깥을 잇는 샛길이 생겨요", "천장 WIPS 센서가 전파로 허가 밖 연결을 찾아요", "경보를 보고 사람이 확인해 막아요"]
    return frame(a, "몰래 켠 와이파이", "NAC가 못 보는 무선 샛길", caps, "".join(body))


REV = {
    1: ("u15-l01-p1-four-questions-rev", "보안 점검, 무엇부터?",
        "회의실 랜 포트의 박 팀장 노트북이 확인 없이 주소를 받아 그룹웨어 서버 관리 화면까지 닿고, 그 장면에서 점검의 첫 질문 누가 들어오나, 곧 NAC를 짚는 모습입니다.",
        "점검을 네 질문으로 쪼개면 첫 질문은 누가 들어오나, 곧 NAC입니다.", 1, p1),
    2: ("u15-l01-p2-ledger-probe-rev", "회사 기기인지 알아보기",
        "IP·MAC 장부에 적은 회사 PC와 달리, Probe가 경로 밖에서 받은 복사본에서 장부에 없는 쌍을 미허가 기기로 보는 모습입니다.",
        "장부와 Probe로 미등록 기기를 알아보지만 MAC은 바꿀 수 있어 보조 도구입니다.", 2, p2),
    3: ("u15-l01-p3-port-down-rev", "포트를 내리면 끝일까?",
        "Probe가 찾은 미등록 노트북의 포트를 NAC가 내리면 링크가 끊기고, 같은 포트 뒤 소형 스위치에 물린 정상 PC까지 함께 끊깁니다.",
        "포트 차단은 확실하지만 포트 뒤 기기가 모두 끊기고 이유를 알리지 못합니다.", 2, p3),
    6: ("u15-l01-p6-wips-rev", "몰래 켠 와이파이",
        "랜에 꽂힌 사내 PC가 핫스팟에도 붙어 샛길이 생기면, 천장 WIPS 센서가 전파로 허가 밖 연결을 찾아 경보하고 사람이 확인할 후보로 올리는 모습입니다.",
        "허가 없는 무선 사용은 WIPS가 찾고, 경보는 사람이 확인할 후보입니다.", 3, p6),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, _t, _al, _c, _ap, fn in REV.values():
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        # 기존 6쪽 항목을 기본으로, 고친 Page만 새 파일로 바꾼다
        items = [(f, t, al, c, ap) for f, t, al, c, ap, _ in old.ITEMS]
        for p, (f, t, al, c, ap, _) in REV.items():
            items[p - 1] = (f, t, al, c, ap)
        wire_items(LESSON / "lesson.md", [[it] for it in items])
    print("ok", len(REV), "svgs")
