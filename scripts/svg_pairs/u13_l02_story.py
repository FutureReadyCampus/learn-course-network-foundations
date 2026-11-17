#!/usr/bin/env python3
"""Unit 13 Lesson 2 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u13_l02_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("09-*/lessons/restructured/02-*")) / "assets" / "animations"
HY = 225


def ppl(a, x, who, moods, facing="right", role_step1=False):
    out = ""
    for mood, t0, t1 in moods:
        if role_step1 and t0 == 1:
            out += a.vis(person(x, HY, who, mood, facing=facing, role=True), 1, 1)
            if t1 > 1:
                out += a.vis(person(x, HY, who, mood, facing=facing), 2, t1)
        else:
            out += a.vis(person(x, HY, who, mood, facing=facing), t0, t1)
    return out


def mk_bubble(a, x, y, s, t, w=None):
    lines = wrap(s)
    w = w or max(tw(ln, 18) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def dev(x, y, label, state="ok", sub=None):
    """Small equipment box (100x60) with a status icon and a 17px name under it."""
    c = {"ok": GREEN, "error": RED, "idle": MUTED}[state]
    ic = {"ok": check(x, y - 2), "error": cross(x, y - 2), "idle": ""}[state]
    return box(x - 50, y - 30, 100, 60, c, PANEL, 8, sw=3) + ic + text(x, y + 60, label, 17, TXT, 700)


def p1():
    a = new()
    s = "장비를 두 대씩 사면 되나요?\n얼마나 들어요?"
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 820, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(clock(330, 300, "금요일 저녁"), 1, 1),
         a.vis(monitor(480, 285, "ok", "서버 세 대 정상"), 1, 1),
         a.vis(monitor(480, 285, "error", "사이트가 안 열려요"), 2, 4), mark(a, 376, 229, 208, 112, 2),
         a.vis(bubble(650, 160, s, tail_to=(812, 203), color=VIOLET), 3, 3), mk_bubble(a, 650, 160, s, 3),
         a.vis(thought(330, 160, "무엇을 얼마나\n겹쳐 둘지부터 따져야 해", tail_to=(160, 200), color=BLUE), 3, 3),
         question(a, "어디를 얼마나 겹쳐 둘까?")]
    caps = ["금요일 저녁, 지우와 서 이사가 예약·문의 사이트를 살펴봐요", "서버는 정상인데 사이트가 통째로 열리지 않아요",
            "서 이사가 장비를 두 대씩 사면 되는지, 얼마나 드는지 물어요", "이 Page에서 겹쳐 둘 곳을 따져 봐요"]
    return scene(a, "서버는 멀쩡한데 사이트가 멈췄어요", "고객 예약이 멈추는 건 신뢰 문제라고 해요", caps, "".join(b), bg="office")


def p2():
    a = new()
    s = "로드 밸런서를 두 대 사면\n처리 속도도 두 배가 되나요?"
    b = [ppl(a, 820, "서 이사", [("normal", 1, 4)], facing="left", role_step1=True),
         ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(doc(480, 285, "이중화 견적서"), 1, 4), mark(a, 442, 243, 76, 84, 1),
         a.vis(bubble(650, 160, s, tail_to=(812, 203), color=VIOLET), 2, 2), mk_bubble(a, 650, 160, s, 2),
         a.vis(thought(330, 160, "구성 방식에 따라\n답이 달라져요", tail_to=(160, 200), color=BLUE), 3, 3),
         question(a, "쉬게 둘까, 같이 일하게 할까?")]
    caps = ["서 이사가 이중화 견적서를 보고 있어요", "처리 속도도 두 배가 되는지 물어요",
            "지우는 구성 방식에 따라 답이 달라진다고 생각해요", "이 Page에서 두 방식을 견줘 봐요"]
    return scene(a, "두 대 사면 두 배 빨라질까", "서 이사가 견적서를 보고 물어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    b = [ppl(a, 140, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(dev(420, 255, "옛 장비", "idle") + dev(640, 255, "예비 장비", "ok"), 1, 4), mark(a, 582, 221, 116, 68, 1),
         a.vis(alert_card(540, 350, "이웃 장비가 옛 주소로 보내요"), 2, 4), mark(a, 372, 324, 336, 52, 2),
         a.vis(thought(330, 150, "넘겨받는 것과 같은 주소로\n오는 건 별개의 문제", tail_to=(150, 200), color=BLUE), 3, 3),
         question(a, "장비가 바뀌어도 같은 주소로?")]
    caps = ["예비 로드 밸런서가 일을 넘겨받았어요", "그런데 이웃 장비가 옛 장비의 주소로 계속 보내요",
            "지우는 넘겨받는 것과 주소는 별개라는 걸 알아채요", "이 Page에서 주소가 이어지는 방법을 알아봐요"]
    return scene(a, "넘겨받았는데 문제가 남았어요", "지우가 이웃 장비의 주소록을 살펴봐요", caps, "".join(b), bg="office")


def p4():
    s = "이중화에 들인 돈이\n아깝네요"
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 820, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(dev(400, 285, "로드 밸런서", "ok") + dev(560, 285, "로드 밸런서", "ok"), 1, 1),
         a.vis(dev(400, 285, "로드 밸런서", "error") + dev(560, 285, "로드 밸런서", "error"), 2, 4), mark(a, 342, 249, 276, 72, 2),
         a.vis(text(480, 215, "스위치 펌웨어를 올리던 날", 17, TXT, 700), 2, 2),
         a.vis(bubble(660, 160, s, tail_to=(812, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 660, 160, s, 3),
         question(a, "두 대는 왜 같이 멈췄을까?")]
    caps = ["로드 밸런서를 두 대로 이중화해 뒀어요", "스위치 펌웨어를 올리던 날 두 대가 동시에 끊겼어요",
            "박 팀장은 이중화에 들인 돈이 아깝다고 해요", "이 Page에서 원인을 찾아봐요"]
    return scene(a, "두 대를 뒀는데 같이 멈췄어요", "지우는 원인을 찾아야 해요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(monitor(430, 285, "error", "1번 서버 고장"), 1, 4), mark(a, 322, 229, 216, 112, 1),
         a.vis(clock(690, 285, "부품 대기 5일"), 2, 4), mark(a, 652, 247, 76, 76, 2),
         a.vis(thought(330, 150, "처음부터 설치하면\n시간이 걸려요", tail_to=(150, 200), color=BLUE), 3, 3),
         question(a, "5일을 기다려야만 할까?")]
    caps = ["서버 한 대가 고장 났어요", "부품을 기다리는 5일 동안 손님 대기가 길어져요",
            "같은 서버를 새로 만들려면 처음부터 설치해야 해요", "이 Page에서 더 빠른 길을 찾아봐요"]
    return scene(a, "고장 난 서버를 5일 기다려야 할까", "지우가 고장 난 서버를 보고 있어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    s = "필요할 때만 늘릴 수는\n없나요?"
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 820, "서 이사", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(monitor(380, 285, "ok", "예약·문의 사이트"), 1, 1),
         a.vis(monitor(380, 285, "loading", "예약·문의 사이트"), 2, 4), mark(a, 270, 229, 220, 112, 2),
         a.vis(clock(620, 285, "점심시간·월말"), 2, 4),
         a.vis(bubble(650, 160, s, tail_to=(812, 203), color=VIOLET), 3, 3), mk_bubble(a, 650, 160, s, 3),
         question(a, "필요할 때만 서버를 늘릴 수 있을까?")]
    caps = ["예약·문의 사이트는 평소엔 잘 돌아가요", "점심시간과 월말 마감 때만 손님이 몰려요",
            "서 이사가 필요할 때만 늘릴 수 없는지 물어요", "이 Page에서 늘리는 방법을 알아봐요"]
    return scene(a, "몰리는 시간에만 늘릴 수 있을까", "서 이사의 질문을 받은 지우예요", caps, "".join(b), bg="office")


NAMES = {"p1": "friday-outage", "p2": "double-speed", "p3": "old-address", "p4": "both-down", "p5": "five-days", "p6": "peak-hours"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u13-l02-p{k[1]}-story-{NAMES[k]}", fn())
        print(f"u13-l02-p{k[1]}-story-{NAMES[k]}.svg")
