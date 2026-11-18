#!/usr/bin/env python3
"""Unit 15 Lesson 2 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u15_l02_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("15-*/lessons/restructured/02-*")) / "assets" / "animations"
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


def mk_bubble(a, x, y, s, t, w=None, fs=18):
    lines = wrap(s, fs)
    w = w or max(tw(ln, fs) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def say(a, x, y, s, tail, color, t, fs=18):
    return a.vis(bubble(x, y, s, tail_to=tail, color=color, fs=fs), t, t) + mk_bubble(a, x, y, s, t, fs=fs)


def p1():
    a = new()
    s = "필요한 문만 열고\n나머지는 닫으세요"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "error", "22번·8080 응답"), 2, 4), mark(a, 380, 229, 200, 112, 2),
         say(a, 300, 150, s, (160, 203), VIOLET, 3),
         a.vis(thought(660, 150, "무엇이 필요한 문일까?", tail_to=(800, 200), color=BLUE), 3, 3),
         question(a, "필요한 문은 누가 정할까?")]
    caps = ["바깥쪽 문을 점검하는 지우와 서 이사예요", "닫히지 않은 포트 포워딩으로 SSH와 웹이 응답해요",
            "서 이사가 필요한 문만 열라고 해요", "이 Page에서 문을 정하는 기준을 알아봐요"]
    return scene(a, "열려 있는 문", "시험하며 연 포트 포워딩이 남아 있어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    s = "우리 방화벽이 그룹웨어 서버를\n지켜 주고 있는 게 맞아요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "방화벽 로그 비어 있음"), 2, 4), mark(a, 370, 229, 220, 112, 2),
         say(a, 330, 150, s, (160, 203), VIOLET, 3, fs=17),
         question(a, "방화벽은 어느 통신까지 볼까?")]
    caps = ["방화벽 규칙을 점검하는 지우와 서 이사예요", "박 팀장 PC가 서버에 접속했는데 로그에 기록이 없어요",
            "서 이사가 방화벽이 서버를 지켜 주는지 물어요", "이 Page에서 로그에 안 남은 까닭을 찾아봐요"]
    return scene(a, "로그에 없는 접속", "접속은 되는데 기록만 없어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    b = [ppl(a, 180, "직원", [("normal", 1, 4)]),
         ppl(a, 800, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "error", "저장소 응답 막힘"), 2, 4), mark(a, 380, 229, 200, 112, 2),
         a.vis(thought(640, 150, "높은 번호 포트를\n통째로 열까?", tail_to=(790, 200), color=BLUE), 3, 3),
         question(a, "문을 열지 않고 응답만 들이려면?")]
    caps = ["직원들은 외부 클라우드 저장소를 써요", "지우가 넣은 규칙 때문에 저장소 응답이 막혀요",
            "급한 마음에 포트를 통째로 열고 싶어져요", "이 Page에서 응답만 들이는 방법을 알아봐요"]
    return scene(a, "막혀 버린 응답", "들어오는 통신은 허용한 것만이라는 규칙을 넣었어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    b = [ppl(a, 180, "고객", [("normal", 1, 2), ("worried", 3, 4)]),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "방화벽 CPU 한가"), 2, 4), mark(a, 380, 229, 200, 112, 2),
         a.vis(pill(180, 368, "새 접속 실패", RED, 17), 2, 4),
         say(a, 640, 150, "장비가 한가한데\n왜 안 되지?", (800, 200), BLUE, 3),
         question(a, "한가한데 왜 새 접속만 실패할까?")]
    caps = ["예약 오픈 이벤트 날 아침이에요", "이미 연결된 사람은 괜찮은데 새 고객만 접속에 실패해요",
            "방화벽 CPU는 한가해서 지우가 갸웃해요", "이 Page에서 막히는 까닭을 찾아봐요"]
    return scene(a, "한가한데 안 되는 날", "고객용 예약·문의 사이트 이벤트 날이에요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         "".join(a.vis(x, 1, 4) for x in (monitor(300, 285, "ok", "점검 중인 PC"),)),
         "".join(a.vis(pill(560, y, s, TXT, 17), 2, 4) for y, s in ((235, "허용"), (285, "처음 보는 해외 주소"), (335, "포트 443"))),
         mark(a, 450, 205, 220, 160, 2),
         a.vis(thought(620, 150, "포트가 맞는데 왜\n안심할 수 없을까?", tail_to=(790, 200), color=BLUE), 3, 3),
         question(a, "443이면 모두 웹 요청일까?")]
    caps = ["지우가 PC의 프로그램이 보내는 통신을 점검해요", "웹이 아닌 통신이 443 포트로 계속 나가요",
            "로그에는 허용, 목적지, 포트만 남아 있어요", "이 Page에서 포트만으로 알 수 있는 것을 알아봐요"]
    return scene(a, "443으로 나가는 통신", "처음 보는 해외 주소로 가고 있어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    s = "한 대로 되면 그게\n제일 좋은 거 아니에요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("happy", 3, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 285, "견적서"), 1, 4), a.vis(pill(540, 200, "올인원 장비 한 대", TXT, 17), 2, 4), mark(a, 440, 177, 200, 46, 2),
         say(a, 300, 150, s, (160, 203), VIOLET, 3),
         question(a, "한 대에 다 넣으면 무엇을 잃을까?")]
    caps = ["직원 40명 회사의 보안 장비를 고르고 있어요", "견적서에 올인원 장비 한 대가 올라와 있어요",
            "서 이사의 눈이 반짝여요", "이 Page에서 한 대에 모을 때의 대가를 알아봐요"]
    return scene(a, "올인원 한 대", "따로 사기엔 부담이 큰 방화벽·VPN·IPS·웹 필터예요", caps, "".join(b), bg="office")


def p7():
    a = new()
    s = "그룹웨어 화면 하나 쓰는데\n건물 전체 열쇠를 줘야 해요?"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 810, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(pill(150, 360, "재택", MUTED, 17), 1, 1),
         a.vis(pill(480, 285, "VPN 접속", TXT, 18), 2, 4), mark(a, 405, 262, 150, 46, 2),
         say(a, 640, 150, s, (800, 200), VIOLET, 3, fs=17),
         question(a, "화면 하나에 어디까지 열어야 할까?")]
    caps = ["박 팀장이 재택에서 일해요", "VPN으로 사내에 접속해요",
            "서 이사가 건물 전체 열쇠가 필요한지 물어요", "이 Page에서 VPN으로 열어 줄 범위를 알아봐요"]
    return scene(a, "재택 직원의 VPN", "화면 하나를 쓰는데 어디까지 닿아야 할까요", caps, "".join(b), bg="home")


NAMES = {"p1": "open-doors", "p2": "log-missing", "p3": "reply-blocked", "p4": "full-table-day",
         "p5": "port-443-worry", "p6": "all-in-one", "p7": "remote-vpn"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6, p7)):
        write(OUT, f"u15-l02-p{k[1]}-story-{NAMES[k]}", fn())
        print(f"u15-l02-p{k[1]}-story-{NAMES[k]}.svg")
