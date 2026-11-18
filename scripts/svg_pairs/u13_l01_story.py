#!/usr/bin/env python3
"""Unit 13 Lesson 1 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u13_l01_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("09-*/lessons/restructured/01-*")) / "assets" / "animations"
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


def mk_pill(a, x, y, s, t, fs=17):
    w = tw(s, fs) + 28
    return mark(a, x - w / 2, y - (fs + 16) / 2, w, fs + 16, t)


def mk_alert(a, x, y, s, t):
    w = tw(s, 17) + 76
    return mark(a, x - w / 2, y - 26, w, 52, t)


def srv(x, y, label, c=LINE):
    """Server box centred at (x, y), 130x60."""
    return box(x - 65, y - 30, 130, 60, c, PANEL, 10, sw=3) + text(x, y + 6, label, 18, TXT, 700)


def chips(x, y, n, c=BLUE):
    """n request chips stacked upward from y (bottom chip centre)."""
    return "".join(box(x - 20, y - 10 - i * 24, 40, 18, c, BG, 4, sw=2) for i in range(n))


def p1():
    a = new()
    qb, qs = "인터넷 회선을 더 빠른 걸로\n바꿔 주실 수 있어요?", "서버 사양을 높였는데\n왜 그대로예요?"
    b = [ppl(a, 120, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 480, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 880, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(monitor(700, 285, "ok", "예약·문의 사이트"), 1, 1),
         a.vis(monitor(700, 285, "loading", "답이 30초 넘게"), 2, 4), mark(a, 605, 229, 190, 112, 2),
         a.vis(clock(330, 290, "점심시간"), 2, 4),
         a.vis(bubble(255, 150, qb, tail_to=(126, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 255, 150, qb, 3),
         a.vis(bubble(730, 150, qs, tail_to=(872, 203), color=VIOLET), 3, 3), mk_bubble(a, 730, 150, qs, 3),
         question(a, "느린 곳은 회선일까, 서버일까?")]
    caps = ["고객용 예약·문의 사이트 티켓이 새로 왔어요", "점심시간마다 답이 30초 넘게 걸려요",
            "박 팀장은 회선을, 서 이사는 서버 사양을 말해요", "이 Page에서 어디가 막혔는지 나눠 봐요"]
    return scene(a, "점심시간마다 느려지는 예약 사이트", "지우에게 새 티켓이 왔어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    r1, r2 = "외부 443 → .11", "외부 443 → .12"
    b = [ppl(a, 130, "지우", [("normal", 1, 2), ("worried", 3, 4)]),
         "".join(srv(x, 330, f"서버 .{n}") for x, n in ((560, 11), (700, 12), (840, 13))),
         a.vis(pill(280, 260, r1, GREEN, 17), 2, 4),
         a.vis(pill(280, 310, r2, TXT, 17), 2, 4), mk_pill(a, 280, 310, r2, 2),
         a.vis(alert_card(400, 190, "외부 443이 이미 쓰이고 있다"), 3, 4), mk_alert(a, 400, 190, "외부 443이 이미 쓰이고 있다", 3),
         question(a, "포트 포워딩을 서버 여러 대로 늘리면?")]
    caps = ["서비스 구역에 서버 세 대를 새로 세워요", "서버마다 포워딩 규칙을 쓰려 해요",
            "두 번째 규칙은 거부돼요", "이 Page에서 이유와 다른 방법을 알아봐요"]
    return scene(a, "서버를 세 대로 늘리려는데", "규칙을 쓰던 지우가 막혔어요", caps, "".join(b), bg="server_room")


def p3():
    a = new()
    s = "서버별 주소를 알려 주고\n아무 데나 쓰게 하면…"
    b = [ppl(a, 130, "서 이사", [("normal", 1, 2), ("worried", 3, 4)]),
         ppl(a, 830, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         doc(380, 285, "고객 안내문"),
         "".join(a.vis(pill(560, y, f"서버 .{n}", TXT, 17), 2, 4) for y, n in ((245, 11), (290, 12), (335, 13))), mark(a, 495, 222, 130, 135, 2),
         a.vis(bubble(300, 150, s, tail_to=(140, 203), color=VIOLET), 3, 3), mk_bubble(a, 300, 150, s, 3),
         question(a, "손님이 알아야 할 주소는 몇 개일까?")]
    caps = ["서버가 세 대인데 고객 안내문은 하나예요", "안내문에 주소를 세 개 적어야 할지 고민이에요",
            "서 이사는 서버별 주소를 알려 주자고 해요", "이 Page에서 주소가 몇 개여야 하는지 알아봐요"]
    return scene(a, "안내문에 주소를 세 개 적을까", "서 이사의 제안을 받은 지우예요", caps, "".join(b), bg="office")


def p4():
    a = new()
    t = "서버 세 대가 같은 서비스인데\n왜 결과가 다르지?"
    b = [ppl(a, 150, "고객", [("normal", 1, 1), ("surprised", 2, 4)]),
         a.vis(monitor(420, 285, "ok", "날짜를 20일로 선택"), 1, 1),
         a.vis(monitor(420, 285, "error", "선택한 날짜가 없습니다"), 2, 4), mark(a, 307, 229, 226, 112, 2),
         ppl(a, 830, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(thought(640, 150, t, tail_to=(808, 200), color=BLUE), 3, 3), mk_bubble(a, 640, 150, t, 3),
         question(a, "고른 날짜는 어디에 남을까?")]
    caps = ["한 고객이 예약 화면에서 날짜를 골랐어요", "다음 화면에서 선택한 날짜가 없다고 나와요",
            "지우는 서버 세 대의 결과가 왜 다른지 궁금해요", "이 Page에서 진행 정보를 어디에 둘지 알아봐요"]
    return scene(a, "고른 날짜가 사라졌어요", "예약 사이트의 고객 한 명과 지우예요", caps, "".join(b), bg="office")


def p5():
    a = new()
    t = "같은 개수로 나눴는데\n왜 불공평하지?"
    xs = (420, 580, 740)
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         "".join(srv(x, 330, f"{i + 1}번 서버") for i, x in enumerate(xs)),
         a.vis("".join(chips(x, 290, 2) for x in xs), 1, 1),
         a.vis(chips(xs[0], 290, 1) + chips(xs[1], 290, 6) , 2, 4), mark(a, 555, 130, 50, 160, 2),
         a.vis(thought(300, 150, t, tail_to=(160, 200), color=BLUE), 3, 3), mk_bubble(a, 300, 150, t, 3),
         question(a, "차례대로 나눠 주면 공평할까?")]
    caps = ["서버 1→2→3→1 순서로 보내도록 설정했어요", "오후가 되자 2번 서버만 줄이 길어요",
            "3번 서버는 놀고 있어요", "이 Page에서 나누는 기준을 비교해 봐요"]
    return scene(a, "같은 개수로 나눴는데", "오후의 예약 사이트 서버 상황이에요", caps, "".join(b), bg="server_room")


def p6():
    a = new()
    s = "견적서 요청은 큰 서버로,\n일반 문의는 작은 서버로"
    t = "왜 이 요청을\n가르지 못할까?"
    msg = "설정에 그런 항목이 없어요"
    b = [ppl(a, 140, "박 팀장", [("normal", 1, 4)]),
         ppl(a, 830, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         monitor(480, 285, "ok", "로드 밸런서 설정"),
         a.vis(bubble(300, 150, s, tail_to=(150, 203), color=TERRACOTTA), 2, 2), mk_bubble(a, 300, 150, s, 2),
         a.vis(alert_card(440, 170, msg), 3, 4), mk_alert(a, 440, 170, msg, 3),
         a.vis(thought(700, 150, t, tail_to=(808, 200), color=BLUE), 3, 3),
         question(a, "지금 장비는 요청을 왜 가르지 못할까?")]
    caps = ["박 팀장이 로드 밸런서 설정을 부탁해요", "견적서 요청과 일반 문의를 나눠 보내 달라고 해요",
            "설정 화면에는 그런 항목이 없어요", "이 Page에서 L4와 L7의 차이를 알아봐요"]
    return scene(a, "견적 요청만 큰 서버로", "박 팀장의 요청을 받은 지우예요", caps, "".join(b), bg="office")


def p7():
    a = new()
    t = "순서도 정책도 맞는데\n왜 아픈 서버로 보냈지?"
    xs = (420, 580, 740)
    b = [ppl(a, 140, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         "".join(srv(x, 330, f"{i + 1}번 서버") for i, x in enumerate(xs)),
         a.vis(pill(580, 262, "캐시 채우는 중", BLUE, 17), 2, 4), mk_pill(a, 580, 262, "캐시 채우는 중", 2),
         a.vis(alert_card(600, 195, "오류가 났어요"), 3, 4), mk_alert(a, 600, 195, "오류가 났어요", 3),
         a.vis(thought(300, 152, t, tail_to=(150, 200), color=BLUE), 3, 3),
         question(a, "서버가 일할 수 있는지 어떻게 알까?")]
    caps = ["야간 업데이트로 2번 서버를 재시작했어요", "서버는 켜졌지만 캐시를 채우는 중이에요",
            "그 사이 요청이 가서 오류가 났어요", "이 Page에서 서버 상태를 확인하는 법을 알아봐요"]
    return scene(a, "켜졌는데 왜 오류가 났을까", "재시작한 2번 서버 이야기예요", caps, "".join(b), bg="server_room")


def p8():
    a = new()
    s = "그 5일 동안\n손님은 어떻게 되나요?"
    xs = (360, 520, 680)
    b = [ppl(a, 130, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 870, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left"),
         "".join(srv(x, 330, f"{i + 1}번 서버") for i, x in enumerate(xs)),
         a.vis(pill(360, 258, "CPU 80% 넘고 오류 잦음", RED, 17), 2, 4),
         a.vis(alert_card(360, 195, "수리에 5일 걸려요"), 2, 4), mark(a, 230, 169, 262, 106, 2),
         a.vis(bubble(700, 150, s, tail_to=(862, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, s, 3),
         question(a, "손님이 모르게 한 대를 빼려면?")]
    caps = ["예약 사이트 서버는 세 대예요", "1번 서버는 부하가 높고 수리에 5일이 걸려요",
            "서 이사가 그동안 손님은 어떻게 되는지 물어요", "이 Page에서 서버를 빼는 방법을 알아봐요"]
    return scene(a, "수리에 5일이 걸린다면", "1번 서버가 말썽이에요", caps, "".join(b), bg="server_room")


NAMES = ["slow-lunch", "port-one-server", "three-addresses", "lost-date", "uneven-queue", "estimate-split", "not-ready", "repair-five-days"]

if __name__ == "__main__":
    for i, (nm, fn) in enumerate(zip(NAMES, (p1, p2, p3, p4, p5, p6, p7, p8)), 1):
        write(OUT, f"u13-l01-p{i}-story-{nm}", fn())
        print(f"u13-l01-p{i}-story-{nm}.svg")
