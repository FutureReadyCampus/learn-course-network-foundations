#!/usr/bin/env python3
"""Unit 15 Lesson 4 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u15_l04_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})  # admin-tutorial roles (shared dict, this process only)

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("15-*/lessons/restructured/04-*")) / "assets" / "animations"
HY = 225  # head y of every avatar


def ppl(a, x, who, moods, facing="right", role_step1=False):
    """moods = [(mood, t0, t1), ...]. role line only in step 1 when role_step1."""
    out = ""
    for mood, t0, t1 in moods:
        if role_step1 and t0 == 1:
            out += a.vis(person(x, HY, who, mood, facing=facing, role=True), 1, 1)
            if t1 > 1:
                out += a.vis(person(x, HY, who, mood, facing=facing), 2, t1)
        else:
            out += a.vis(person(x, HY, who, mood, facing=facing), t0, t1)
    return out


def mk_person(a, x, t):
    return mark(a, x - 44, HY - 32, 88, 160, t)


def mk_bubble(a, x, y, s, t, w=None):
    lines = wrap(s)
    w = w or max(tw(ln, 18) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def p1():
    a = new()
    s = "점검 결과를\n\"한 장으로\" 주세요"
    b = [ppl(a, 110, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 850, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         "".join(a.vis(monitor(x, 285, "ok", m), 1, 4) for x, m in ((290, "NAC"), (490, "방화벽"), (690, "IPS"))),
         a.vis(alert_card(490, 190, "경보 하루 수천 건"), 2, 2), mark(a, 380, 162, 220, 56, 2),
         a.vis(bubble(700, 150, s, tail_to=(845, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, s, 3),
         question(a, "흩어진 기록을 어떻게 이어 읽을까?")]
    caps = ["지우는 장비마다 따로인 화면을 돌며 로그를 봐요", "경보가 하루 수천 건 쌓여요",
            "서 이사는 점검 결과를 한 장으로 달라고 해요", "이 Page에서 기록을 이어 읽는 법을 알아봐요"]
    return scene(a, "화면은 따로, 경보는 수천 건", "지우의 아침이 달라졌어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         monitor(560, 285, "ok", "테스트어택"), mark(a, 460, 229, 200, 112, 1),
         a.vis(alert_card(560, 190, "같은 경보 수십 건"), 2, 2), mark(a, 440, 162, 240, 56, 2),
         a.vis(thought(480, 150, "공격일까, 오탐일까?", tail_to=(205, 200), color=BLUE), 3, 3),
         question(a, "이 경보는 어떤 규칙이 울렸을까?")]
    caps = ["\"테스트어택\" 경보가 화면에 떠 있어요", "같은 경보가 수십 건 찍혔어요",
            "지우는 공격인지 오탐인지 가리고 싶어요", "이 Page에서 규칙 한 줄을 읽어 봐요"]
    return scene(a, "수십 건의 테스트어택", "지우가 경보 앞에 앉았어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    pk, sv = "서버가 이상한\n것 같아요", "네트워크 탓\n아닌가요?"
    b = [ppl(a, 110, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 520, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 850, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(300, 285, "error", "업로드 실패"), 2, 4), mark(a, 200, 229, 200, 112, 2),
         a.vis(bubble(250, 150, pk, tail_to=(118, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 250, 150, pk, 3),
         a.vis(bubble(720, 150, sv, tail_to=(845, 203), color=VIOLET), 3, 3), mk_bubble(a, 720, 150, sv, 3),
         question(a, "의심할 대상을 어떻게 줄일까?")]
    caps = ["IPS 규칙을 갱신한 다음 날이에요", "예약·문의 사이트에 큰 파일 업로드가 실패해요",
            "박 팀장은 서버를, 서 이사는 네트워크를 의심해요", "이 Page에서 원인을 좁히는 법을 알아봐요"]
    return scene(a, "업로드가 안 돼요", "서로 상대를 의심하고 있어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    s = "무엇이 어디서 무엇을 하는지\n한 장으로 보여 줘요"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 4)]),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(doc(480, 285, "장비 이름 열 개"), 2, 4), mark(a, 420, 242, 120, 130, 2),
         a.vis(bubble(430, 150, s, tail_to=(160, 203), color=VIOLET, fs=17), 3, 3), mk_bubble(a, 430, 150, s, 3),
         a.vis(thought(660, 150, "요청 하나를 올려\n따라가 보자", tail_to=(800, 200), color=BLUE), 4, 4),
         question(a, "장치를 한 장의 지도에 놓으면?")]
    caps = ["서 이사와 지우가 점검 결과를 마주하고 있어요", "서 이사가 장비 이름 열 개짜리 보고서를 덮어요",
            "서 이사는 이름이 아니라 위치로 그리라고 해요", "이 Page에서 지도 위에 요청을 올려 봐요"]
    return scene(a, "이름 말고 한 장으로", "서 이사가 보고서를 덮었어요", caps, "".join(b), bg="office")


def p5():
    a = new()
    pk = "도쿄 지사 노트북을\nMAC 주소로 막아 주세요"
    sv = "특정 URL을 막아 달라"
    b = [ppl(a, 110, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 480, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 850, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(bubble(310, 150, pk, tail_to=(118, 203), color=TERRACOTTA, fs=17), 2, 2), mk_bubble(a, 310, 150, pk, 2),
         a.vis(bubble(700, 150, sv, tail_to=(845, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, sv, 3),
         question(a, "요청한 정보는 어느 층에 있을까?")]
    caps = ["박 팀장과 서 이사가 지우에게 차례로 요청해요", "박 팀장은 노트북을 MAC 주소로 막아 달라고 해요",
            "다음 날 서 이사는 특정 URL을 막아 달라고 해요", "이 Page에서 두 요청의 차이를 알아봐요"]
    return scene(a, "비슷해 보이는 두 요청", "장비마다 보는 정보가 달라요", caps, "".join(b), bg="office")


def p6():
    a = new()
    sv = "우리 회사, 이제 안전하다고\n답할 수 있어요?"
    jw = "안전하다는 말은 못 드려요.\n어디가 비었는지는 말씀드려요"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 4)]),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(bubble(320, 150, sv, tail_to=(160, 203), color=VIOLET), 2, 2), mk_bubble(a, 320, 150, sv, 2),
         a.vis(doc(480, 285, "네 질문 표"), 3, 4),
         a.vis(bubble(630, 150, jw, tail_to=(800, 203), color=BLUE, fs=17), 3, 3), mk_bubble(a, 630, 150, jw, 3),
         question(a, "무엇을 근거로 답할까?")]
    caps = ["점검 보고를 마친 지우 앞에 서 이사가 서 있어요", "서 이사가 첫날의 질문을 다시 꺼내요",
            "지우는 \"네\"도 \"아니요\"도 하지 않아요", "이 Page에서 답할 수 있는 칸을 알아봐요"]
    return scene(a, "이제 안전하다고 답할 수 있을까", "서 이사가 첫날의 질문을 다시 물어요", caps, "".join(b), bg="office")


NAMES = {"p1": "siem-morning", "p2": "test-attack", "p3": "upload-fail", "p4": "one-map", "p5": "two-requests", "p6": "safe-answer"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u15-l04-p{k[1]}-story-{NAMES[k]}", fn())
        print(f"u15-l04-p{k[1]}-story-{NAMES[k]}.svg")
