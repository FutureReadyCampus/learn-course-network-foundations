#!/usr/bin/env python3
"""Unit 12 Lesson 4 situation SVGs (4 steps each, one per Page): 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u12_l04_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("08-*/lessons/restructured/04-*")) / "assets" / "animations"
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


def panel(x, y, w, h, title):
    return box(x - w / 2, y - h / 2, w, h, BLUE, PANEL, 10, sw=4) + text(x, y - h / 2 + 28, title, 17, TXT, 700)


def p1():
    a = new()
    q = "사람이 안 열었는데\n포트가 열렸다고요?"
    rows = "".join(pill(480, 275 + i * 40, s, TXT, 17) for i, s in enumerate(("TCP 6881", "UDP 27015", "UDP 50001")))
    b = [ppl(a, 140, "지우", [("normal", 1, 1), ("surprised", 2, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 840, "서 이사", [("normal", 1, 2), ("surprised", 3, 4)], facing="left", role_step1=True),
         a.vis(panel(480, 290, 230, 130, "포트 포워딩 목록") + text(480, 300, "비어 있음", 18, MUTED), 1, 1),
         a.vis(panel(480, 290, 250, 170, "UPnP 목록") + rows, 2, 4),
         mark(a, 350, 200, 260, 180, 2),
         a.vis(bubble(700, 150, q, tail_to=(832, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, q, 3),
         question(a, "지우가 만든 적 없는 줄은 누가 만들었을까?")]
    caps = ["지우가 공유기 화면의 모든 목록을 훑어봐요", "'UPnP' 메뉴에 만든 적 없는 줄이 세 개 있어요",
            "곁에서 본 서 이사가 놀라요", "이 Page에서 줄의 정체를 알아봐요"]
    return scene(a, "내가 연 적 없는 포트", "포트 포워딩 목록은 비었는데 다른 메뉴에 줄이 있어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    s1 = "협력사랑 대용량 견적 자료를\n주고받으려고 깔았어요"
    b = [ppl(a, 140, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 840, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "P2P 전송 프로그램"), 2, 4), mark(a, 370, 229, 220, 112, 2),
         a.vis(bubble(300, 150, s1, tail_to=(150, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 300, 150, s1, 3),
         question(a, "프로그램은 왜 포트를 열고 싶어 할까?")]
    caps = ["지우가 줄의 주인을 찾아갔어요", "직원 PC에 P2P 파일 전송 프로그램이 있어요",
            "박 팀장이 변명하듯 까닭을 말해요", "이 Page에서 프로그램의 속사정을 알아봐요"]
    return scene(a, "줄의 주인을 찾아갔더니", "박 팀장의 PC에 파일 전송 프로그램이 있었어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    q = "UPnP라는 게 대체 뭐죠?\n이름만 들어서는 모르겠어요"
    b = [ppl(a, 140, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 840, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 290, "티켓 메모"), 1, 4),
         a.vis(bubble(690, 150, q, tail_to=(832, 203), color=VIOLET, fs=17), 2, 2), mk_bubble(a, 690, 150, q, 2),
         a.vis(thought(300, 150, "Plug and Play,\n꽂으면 바로 쓰는 방식", tail_to=(150, 203), color=BLUE), 3, 3),
         question(a, "편해진 설정을 누가 지켜볼까?")]
    caps = ["서 이사가 지우의 티켓 메모를 봐요", "이름만 들어서는 UPnP가 뭔지 모르겠다고 해요",
            "이름을 풀면 꽂으면 바로 쓰는 방식이에요", "이 Page에서 편리함의 대가를 알아봐요"]
    return scene(a, "UPnP가 대체 뭐죠?", "서 이사가 티켓 메모를 보고 물었어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    b = [ppl(a, 140, "지우", [("normal", 1, 1), ("thinking", 2, 4)], role_step1=True),
         a.vis(pc(480, 295, "프로그램"), 1, 4),
         a.vis(line(520, 295, 740, 295, LINE, 4, "10 8") + router(780, 295, "공유기"), 1, 4),
         a.vis(thought(300, 150, "프로그램은 공유기 주소도\n모르는데 어떻게 부탁하지?", tail_to=(150, 203), color=BLUE), 2, 2),
         a.vis(booth(640, 215, "경비실"), 3, 3),
         a.vis(bubble(470, 190, "경비실이 어디죠?", tail_to=(480, 250), color=BLUE), 3, 3), mk_bubble(a, 470, 190, "경비실이 어디죠?", 3),
         question(a, "프로그램은 어떤 순서로 부탁할까?")]
    caps = ["PC의 프로그램이 공유기에 부탁을 해요", "공유기 주소도 모르는데 어떻게 부탁할까요?",
            "건물에서 경비실을 찾는 일과 비슷해요", "이 Page에서 부탁의 순서를 알아봐요"]
    return scene(a, "프로그램은 어떻게 부탁할까", "공유기 주소를 모르는 프로그램의 부탁이에요", caps, "".join(b), bg="office")


def p5():
    a = new()
    q = "누가 허락한 거예요?\n마음대로 부탁해도 돼요?"
    b = [ppl(a, 140, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 840, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 285, "UPnP 줄"), 1, 4),
         a.vis(bubble(640, 150, q, tail_to=(832, 203), color=VIOLET), 2, 2), mk_bubble(a, 640, 150, q, 2),
         a.vis(thought(300, 150, "관리자 로그인 기록이\n남았는지 찾아보자", tail_to=(150, 203), color=BLUE), 3, 3),
         a.vis(pill(480, 390, "로그인 기록: 없음", RED, 18), 3, 3), mark(a, 380, 370, 200, 40, 3),
         question(a, "비밀번호도 없이 어떻게 열렸을까?")]
    caps = ["서 이사가 UPnP 줄을 함께 보고 있어요", "서 이사가 누가 허락했는지 물어요",
            "관리자 로그인 기록을 찾아봤지만 없어요", "이 Page에서 허락 없이 열린 까닭을 알아봐요"]
    return scene(a, "누가 허락한 거예요?", "서 이사가 다시 물었어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    q = "끄면 불편해진다면서요.\n그럼 어떻게 하죠?"
    b = [ppl(a, 140, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 840, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], facing="left", role_step1=True),
         a.vis(router(480, 290, "공유기 UPnP"), 1, 4),
         a.vis(bubble(640, 150, q, tail_to=(832, 203), color=VIOLET), 2, 2), mk_bubble(a, 640, 150, q, 2),
         a.vis(thought(300, 150, "켜면 편하지만 통제 불가,\n끄면 통제되지만 불편", tail_to=(150, 203), color=BLUE), 3, 3),
         question(a, "UPnP, 켜 둘까 꺼 둘까?")]
    caps = ["지우가 공유기의 UPnP 설정을 두고 고민해요", "서 이사는 직원들의 민원이 걱정이에요",
            "켜도 꺼도 대가가 있어요", "이 Page에서 대가를 비교해 정해 봐요"]
    return scene(a, "UPnP, 끄면 안전할까", "서 이사는 직원들의 민원이 걱정이에요", caps, "".join(b), bg="office")


NAMES = ["unknown-lines", "owner-found", "what-is-upnp", "how-to-ask", "who-allowed", "on-or-off"]

if __name__ == "__main__":
    for i, (fn, n) in enumerate(zip((p1, p2, p3, p4, p5, p6), NAMES), 1):
        write(OUT, f"u12-l04-p0{i}-story-{n}", fn())
        print(f"u12-l04-p0{i}-story-{n}.svg")
