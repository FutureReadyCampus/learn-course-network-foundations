#!/usr/bin/env python3
"""Unit 11 Lesson 6 (내 PC의 로컬 프록시): one 4-step "situation" SVG per Page (6 files).
Run from repo root: python3 scripts/svg_pairs/u11_l06_story.py
Writes assets/animations/u11-l06-p{P}-story-<slug>.svg only; lesson.md illustrations are added by hand."""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})  # admin-tutorial roles (shared dict, this process only)

OUT = Path(__file__).resolve().parents[2] / "units/07-network-devices/lessons/restructured/06-PC의-로컬-프록시로-통신-살펴보기/assets/animations"


def who(a, x, y, name, moods, facing="right"):
    """moods = [(mood, t0, t1), ...]"""
    return "".join(a.vis(person(x, y, name, m, facing=facing), t0, t1) for m, t0, t1 in moods)


def pm(a, x, y, t):
    return mark(a, x - 44, y - 32, 88, 160, t)


def p1():
    a = new()
    q = "그 프로그램이 뭘 밖으로\n보내는지 확인해 주실래요?"
    body = [who(a, 130, 235, "박 팀장", [("happy", 1, 4)]),
            a.vis(monitor(310, 290, "ok", "파일 동기화"), 1, 4),
            who(a, 610, 235, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], "left"),
            who(a, 840, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)], "left"),
            pm(a, 130, 235, 1),
            a.vis(bubble(560, 168, q, tail_to=(606, 208), color=VIOLET), 2, 2),
            mark(a, 560 - 163, 131, 326, 78, 2),
            a.vis(thought(745, 168, "이 요청에 이것이\n들어 있었다고 답하자", tail_to=(832, 208), color=BLUE), 3, 3),
            mark(a, 745 - 160, 130, 320, 78, 3),
            question(a, "패킷을 잡으면 내용도 읽힐까?")]
    caps = ["박 팀장 PC에 파일 동기화 프로그램이 깔렸어요", "서 이사가 밖으로 뭘 보내는지 확인을 요청해요",
            "지우는 확실하게 답할 방법을 찾고 싶어요", "이 Page에서 패킷 캡처로 확인해 봐요"]
    return scene(a, "동기화 프로그램은 뭘 보낼까요?", "네 번째 티켓이 지우에게 왔어요", caps, "".join(body), bg="office")


def p2():
    a = new()
    body = [who(a, 150, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
            pill(150, 395, "테스트용 PC", MUTED, 17),
            a.vis(monitor(350, 290, "ok", "파일 동기화"), 1, 4),
            a.vis(box(690, 230, 210, 110, MUTED, PANEL, 12, sw=3) + text(795, 292, "클라우드 저장소", 18, TXT, 700), 2, 4),
            a.vis(line(450, 285, 685, 285, LINE, 4, "10 8") + packet(570, 285), 2, 2),
            mark(a, 450, 255, 235, 60, 2),
            a.vis(line(450, 285, 685, 285, LINE, 4, "10 8") + ask(570, 285), 3, 4),
            a.vis(thought(380, 160, "내가 볼 수 있는 누군가를\n먼저 거치게 하자", tail_to=(200, 205), color=BLUE), 3, 3),
            mark(a, 380 - 150, 122, 300, 78, 3),
            question(a, "내 PC 안에 중계소를 세운다면?")]
    caps = ["지우는 테스트용 PC에서 프로그램을 써요", "프로그램 요청이 저장소로 바로 나가요",
            "지우가 들여다볼 누군가를 거치게 하고 싶어요", "이 Page에서 그 중계소를 세워 봐요"]
    return scene(a, "요청을 내가 볼 수 있다면", "한 건 한 건의 주소·헤더·본문이 궁금해요", caps, "".join(body), bg="office")


def p3():
    a = new()
    body = [a.vis(monitor(430, 290, "ok", "프록시 127.0.0.1:8080"), 1, 1),
            a.vis(monitor(430, 290, "error", "사이트가 안 열려요"), 2, 4),
            mark(a, 330, 232, 200, 118, 2),
            a.vis(alert_card(430, 175, "프록시 서버에 연결할 수 없습니다"), 2, 2),
            who(a, 760, 235, "지우", [("normal", 1, 1), ("surprised", 2, 2), ("thinking", 3, 4)], "left"),
            a.vis(thought(560, 165, "도구 하나 꺼졌을 뿐인데\n왜 전부 끊겼지?", tail_to=(752, 208), color=BLUE), 3, 3),
            mark(a, 560 - 150, 127, 300, 78, 3),
            question(a, "127.0.0.1:8080은 어디로 가는 주소?")]
    caps = ["지우가 브라우저 프록시 칸에 주소를 적었어요", "도구를 켜지 않은 채 열었더니 다 막혀요",
            "도구 하나 꺼졌을 뿐인데 왜 다 끊겼을까요", "이 Page에서 이 주소의 정체를 알아봐요"]
    return scene(a, "모든 사이트가 안 열려요", "프록시 칸에 적은 주소가 문제일까요?", caps, "".join(body), bg="office")


def p4():
    a = new()
    body = [who(a, 760, 235, "지우", [("normal", 1, 1), ("worried", 2, 2), ("thinking", 3, 4)], "left"),
            a.vis(monitor(330, 290, "ok", "요청 목록"), 1, 1),
            a.vis(monitor(330, 290, "error", "내용 푸는 옵션 켬"), 2, 4),
            mark(a, 225, 232, 210, 118, 2),
            a.vis(alert_card(330, 175, "연결이 비공개로 설정되어 있지 않습니다"), 2, 2),
            a.vis(thought(560, 165, "도구는 왜 처음엔 못 열고,\n열려고 하면 경고가 날까?", tail_to=(752, 208), color=BLUE), 3, 3),
            mark(a, 560 - 160, 127, 320, 78, 3),
            question(a, "로컬 프록시는 HTTPS를 어떻게 열까?")]
    caps = ["설정을 맞추자 도구 목록에 요청이 찍혀요", "내용을 푸는 옵션을 켜자 인증서 경고가 떠요",
            "처음엔 못 열고, 열려 하면 경고가 나요", "이 Page에서 그 까닭을 알아봐요"]
    return scene(a, "인증서 경고가 떴어요", "HTTPS 내용을 보려는데 막혔어요", caps, "".join(body), bg="client")


def p5():
    a = new()
    body = [who(a, 480, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
            pill(230, 395, "캡처 도구", BLUE, 17), pill(730, 395, "프록시 도구", BLUE, 17),
            a.vis(monitor(230, 290, "ok", "같은 순간"), 1, 1), a.vis(monitor(730, 290, "ok", "같은 순간"), 1, 1),
            a.vis(monitor(230, 290, "ok", "수천 줄의 패킷"), 2, 4), a.vis(monitor(730, 290, "ok", "요청 한 줄"), 2, 4),
            mark(a, 135, 232, 190, 118, 2), mark(a, 635, 232, 190, 118, 2),
            a.vis(thought(480, 155, "견적서를 통째로 보내는지\n답하기 쉬운 쪽은?", tail_to=(480, 207), color=BLUE), 3, 3),
            mark(a, 480 - 150, 116, 300, 78, 3),
            question(a, "패킷 조각 대신 요청 한 건으로 보려면?")]
    caps = ["지우가 두 도구 화면을 나란히 놓아요", "같은 순간이 수천 줄 대 한 줄로 보여요",
            "견적서를 통째로 보내는지 답하기 쉬운 쪽은요", "이 Page에서 요청 한 건으로 봐요"]
    return scene(a, "두 화면을 나란히 놓으면", "가짜 견적서를 올린 같은 순간이에요", caps, "".join(body), bg="office")


def p6():
    a = new()
    items = [(360, "무료 우회 프록시", "회사 밖 인터넷", VIOLET), (570, "회사 프록시", "사내 서버실", GREEN), (780, "로컬 프록시", "분석하는 PC 안", BLUE)]
    body = [who(a, 130, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
            a.vis(doc(260, 290, "분석 결과"), 1, 1)]
    for x, n, w, c in items:
        body.append(a.vis(box(x - 95, 255, 190, 70, c, PANEL, 12, sw=3) + text(x, 296, n, 17, TXT, 700), 2, 4))
    body += [mark(a, 265, 255, 620, 70, 2),
             a.vis(thought(310, 165, "정말 셋은\n다른 물건일까?", tail_to=(150, 208), color=BLUE), 3, 3),
             mark(a, 310 - 100, 127, 200, 78, 3),
             question(a, "우회·통제·분석, 다 같은 모양일까?")]
    caps = ["지우가 분석 결과를 정리하고 있어요", "이번 Unit에서 프록시를 세 번 만났어요",
            "이름도 쓰임도 달라서 다른 장비 같아요", "이 Page에서 셋을 견줘 봐요"]
    return scene(a, "프록시를 세 번 만났어요", "우회, 회사, 내 PC 안의 프록시예요", caps, "".join(body), bg="server_room")


PAGES = {"p01-story-unreadable-capture": p1, "p02-story-local-relay": p2, "p03-story-proxy-down": p3,
         "p04-story-cert-warning": p4, "p05-story-two-screens": p5, "p06-story-three-proxies": p6}

if __name__ == "__main__":
    for slug, fn in PAGES.items():
        write(OUT, f"u11-l06-{slug}", fn())
        print(OUT / f"u11-l06-{slug}.svg")
