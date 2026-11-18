#!/usr/bin/env python3
"""Unit 15 Lesson 3 situation SVGs (4 steps each, one per Page). Run from the repo root: python3 scripts/svg_pairs/u15_l03_story.py"""
from pathlib import Path

from u11_l01_story import HY, mk_bubble, mk_person, ppl  # noqa: F401  (also sets the admin-tutorial ROLES)
from hangyeol_cast import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("15-*/lessons/restructured/03-*")) / "assets" / "animations"


def p1():
    a = new()
    s = "문은 잠갔다면서 왜 이래요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 800, "지우", [("worried", 1, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "방화벽 로그: 허용"), 1, 1),
         a.vis(monitor(480, 285, "error", "수상한 경로 요청"), 2, 4),
         a.vis(text(480, 392, "그룹웨어 서버 웹 화면의 로그", 17, TXT, 700), 2, 4), mark(a, 380, 229, 200, 112, 2),
         a.vis(bubble(320, 150, s, tail_to=(168, 203), color=VIOLET), 3, 3), mk_bubble(a, 320, 150, s, 3),
         question(a, "허용된 문으로 온 공격은 누가 볼까?")]
    caps = ["방화벽 규칙을 정리한 뒤에도 지우는 마음이 편치 않아요", "그룹웨어 서버 로그에 수상한 경로 요청이 계속 찍혀요",
            "서 이사가 문은 잠갔다면서 왜 이러냐고 물어요", "이 Page에서 그 공격을 볼 장비를 찾아봐요"]
    return scene(a, "방화벽을 통과한 요청", "방화벽 로그에는 허용만 남았어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    s = "막아 주는 게 당연히\n좋은 거 아니에요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 1), ("thinking", 2, 4)], facing="left", role_step1=True),
         a.vis(pill(480, 255, "그룹웨어 서버 앞 경로 한가운데", BLUE, 17), 2, 4),
         a.vis(pill(480, 315, "스위치 미러링으로 복사본만", BLUE, 17), 2, 4), mark(a, 270, 225, 420, 120, 2),
         a.vis(text(480, 215, "탐지 장비를 둘 자리", 17, TXT, 700), 2, 4),
         a.vis(bubble(320, 150, s, tail_to=(168, 203), color=VIOLET), 3, 3), mk_bubble(a, 320, 150, s, 3),
         question(a, "막을까, 알리기만 할까?")]
    caps = ["탐지 장비를 들이기로 했어요", "지우는 장비를 둘 자리를 정해야 해요",
            "서 이사는 막아 주는 게 당연히 좋다고 해요", "이 Page에서 막을지 알릴지 정해 봐요"]
    return scene(a, "막을까, 알리기만 할까", "장비를 어디에 둘지 고민해요", caps, "".join(b), bg="office")


def p3():
    a = new()
    t = "사건 현장에서 지문을\n대조하는 수사관"
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(doc(480, 285, "알려진 공격 요청", RED), 1, 4),
         a.vis(doc(620, 285, None, RED) + doc(760, 285, None, RED) + text(690, 347, "비슷한 문자열이 반복", 17, TXT, 700), 2, 4),
         mark(a, 580, 235, 220, 100, 2),
         a.vis(thought(520, 150, t, tail_to=(215, 203), color=BLUE), 3, 3), mk_bubble(a, 520, 150, t, 3),
         question(a, "공격의 지문은 어떻게 찾을까?")]
    caps = ["지우는 알려진 공격 요청을 떠올려요", "알려진 공격 요청에는 비슷한 문자열이 반복돼요",
            "장비가 어떻게 알아볼지 지우는 수사관을 떠올려요", "이 Page에서 공격의 지문을 찾아봐요"]
    return scene(a, "장비는 공격을 어떻게 알아볼까", "지우가 지문 대조를 떠올려요", caps, "".join(b), bg="office")


def p4():
    a = new()
    s = "교육 자료인데 공격이라니요!"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         a.vis(doc(480, 285, "보안 교육 자료"), 1, 4),
         a.vis(alert_card(700, 285, "IPS가 업로드를 막음"), 2, 4), mark(a, 570, 255, 260, 60, 2),
         a.vis(bubble(320, 150, s, tail_to=(168, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 320, 150, s, 3),
         question(a, "정상 요청이 공격으로 찍혔다면?")]
    caps = ["박 팀장이 보안 교육 자료를 그룹웨어에 올려요", "서버 구역 입구의 IPS가 업로드를 막았어요",
            "자료에 공격 예시 문자열이 들어 있었어요", "이 Page에서 오탐을 어떻게 다룰지 알아봐요"]
    return scene(a, "교육 자료가 공격으로 찍혔어요", "박 팀장이 억울해해요", caps, "".join(b), bg="office")


def p5():
    a = new()
    t = "걸리지 않는다고\n안전한 걸까?"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(330, 285, "동기화 설치 파일"), 1, 4),
         a.vis(monitor(560, 285, "ok", "걸린 것 없음"), 2, 4), mark(a, 460, 229, 200, 112, 2),
         a.vis(thought(600, 150, t, tail_to=(800, 203), color=BLUE), 3, 3), mk_bubble(a, 600, 150, t, 3),
         question(a, "처음 보는 악성 파일은 어떻게 잡을까?")]
    caps = ["박 팀장에게 설치 파일이 첨부된 메일이 왔어요", "지우가 시그니처에 대조해 봤지만 걸리는 게 없어요",
            "걸리지 않는다고 안전한 걸까 지우는 생각해요", "이 Page에서 처음 보는 파일을 잡는 방법을 봐요"]
    return scene(a, "시그니처에 걸리지 않는 파일", "지우가 첨부 파일을 확인해요", caps, "".join(b), bg="office")


def p6():
    a = new()
    t1 = "우리 회사 장비 하나가\n혼자 알 수는 없다"
    t2 = "후기를 찾아보듯\n겪은 사람들의 경험을?"
    b = [ppl(a, 200, "지우", [("normal", 1, 1), ("thinking", 2, 4)], role_step1=True),
         a.vis(doc(480, 285, "애매한 파일"), 1, 4), a.vis(pill(700, 285, "접속 주소", TXT, 17), 1, 4),
         a.vis(thought(520, 150, t1, tail_to=(215, 203), color=BLUE), 2, 2), mk_bubble(a, 520, 150, t1, 2),
         a.vis(thought(520, 150, t2, tail_to=(215, 203), color=BLUE), 3, 3), mk_bubble(a, 520, 150, t2, 3),
         question(a, "남들이 이미 아는 악성일까?")]
    caps = ["샌드박스를 거쳐도 애매한 파일과 접속 주소가 남아요", "장비 하나가 모든 악성을 혼자 알 수는 없어요",
            "지우는 동네 식당 후기처럼 남의 경험을 떠올려요", "이 Page에서 평판으로 알아봐요"]
    return scene(a, "판단이 애매한 파일과 주소", "지우가 방법을 생각해요", caps, "".join(b), bg="office")


NAMES = {"p1": "passed-firewall", "p2": "block-or-alert", "p3": "fingerprint", "p4": "false-alarm", "p5": "unknown-file", "p6": "ask-others"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u15-l03-p{k[1]}-story-{NAMES[k]}", fn())
        print(f"u15-l03-p{k[1]}-story-{NAMES[k]}.svg")
