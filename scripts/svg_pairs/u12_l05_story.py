#!/usr/bin/env python3
"""Unit 12 Lesson 5 situation SVGs (4 steps, one per Page, 7 Pages): 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u12_l05_story.py"""
from pathlib import Path

from u11_l01_story import *  # noqa: F401,F403  (cast, ROLES override, ppl, mk_bubble, HY)

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("08-*/lessons/restructured/05-*")) / "assets" / "animations"


def bub(a, x, y, s, who_x, t, color, w=None, fs=18):
    return a.vis(bubble(x, y, s, tail_to=(who_x, 203), color=color, w=w, fs=fs), t, t) + mk_bubble(a, x, y, s, t, w)


def p1():
    a = new()
    s = "회의가 끊기면 어떡해요?\n확인해 주실 수 있어요?"
    b = [ppl(a, 200, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 760, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 290, "티켓"), 1, 4), mark(a, 440, 250, 80, 80, 1),
         bub(a, 360, 150, s, 210, 2, TERRACOTTA),
         a.vis(thought(620, 150, "아무도 포트를 안 열었는데\n영상과 음성이 오가요", tail_to=(750, 200), color=BLUE), 3, 3),
         question(a, "포트를 안 열었는데 어떻게 연결됐을까?")]
    caps = ["UPnP를 끈 다음 날, 박 팀장이 티켓을 올려요", "박 팀장이 회의가 끊길까 걱정해요",
            "지우가 보니 회의는 멀쩡해요", "이 Page에서 이 연결의 비밀을 알아봐요"]
    return scene(a, "포트를 안 열었는데 회의는?", "박 팀장의 티켓을 받은 지우예요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(doc(480, 290, "확인 메모"), 1, 4),
         a.vis(monitor(700, 290, "ok", "회의 잘 되는 중"), 2, 4), mark(a, 590, 234, 220, 112, 2),
         a.vis(thought(420, 150, "안 될 거라고 썼는데\n회의는 잘 되네", tail_to=(215, 200), color=BLUE), 3, 3),
         question(a, "NAT에게 따로 물어야 할 두 가지는?")]
    caps = ["지우가 티켓의 확인 메모를 써요", "그런데 회의는 잘 되고 있어요",
            "지우는 메모가 틀렸다는 걸 알아채요", "이 Page에서 NAT에게 물을 두 가지를 알아봐요"]
    return scene(a, "메모가 틀린 까닭은", "이름 하나로 안 될 거라고 적었어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    b = [ppl(a, 140, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         a.vis(pc(320, 285, "집 PC"), 1, 4),
         a.vis(router(520, 285, "집 공유기"), 1, 4) + a.vis(line(358, 285, 490, 285, LINE, 4), 1, 4),
         a.vis(pill(520, 385, "192.0.2.123:40001", TXT, 17), 2, 2), mark(a, 380, 367, 280, 36, 2),
         a.vis(person(820, HY, "직원", "normal", facing="left"), 1, 4),
         a.vis(alert_card(700, 160, "패킷이 도착하지 않아요"), 3, 3),
         question(a, "상대가 바뀌면 바깥 포트도 바뀔까?")]
    caps = ["박 팀장이 집 PC에서 화상회의 앱을 켜요", "앱이 바깥 주소를 협력사 담당자에게 알려 줘요",
            "그런데 협력사가 보낸 패킷이 도착하지 않아요", "이 Page에서 왜 안 되는지 알아봐요"]
    return scene(a, "주소는 맞게 전달됐는데", "협력사 담당자의 패킷이 오지 않아요", caps, "".join(b), bg="home")


def p4():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         router(400, 285, "지우의 공유기"),
         a.vis(packet(640, 250, BLUE) + text(640, 285, "통과", 17, GREEN, 700) + packet(640, 340, BLUE) + text(640, 375, "막힘", 17, RED, 700), 2, 4),
         mark(a, 600, 220, 80, 176, 2),
         a.vis(thought(330, 150, "같은 IP에서 왔는데\n왜 결과가 다를까?", tail_to=(160, 200), color=BLUE), 3, 3),
         question(a, "누가 보낸 패킷까지 받아 줄까?")]
    caps = ["지우의 공유기로 바깥에서 패킷이 들어와요", "같은 IP에서 왔는데 어떤 패킷은 통과하고 어떤 패킷은 막혀요",
            "지우는 까닭이 궁금해요", "이 Page에서 필터링을 알아봐요"]
    return scene(a, "같은 IP인데 결과가 달라요", "협력사 서버에서 온 패킷이에요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 800, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(480, 290, "제품 설명서"), 1, 4),
         a.vis(pill(480, 355, "Full Cone 지원, P2P에 최적", TXT, 17), 2, 4), mark(a, 330, 337, 300, 36, 2),
         bub(a, 700, 150, "Full Cone이 뭐예요?\n좋은 건가요?", 790, 3, VIOLET),
         question(a, "Full Cone, Symmetric은 어떻게 읽을까?")]
    caps = ["공유기를 바꿀지 지우가 제품 설명서를 봐요", "설명서에 옛 이름이 적혀 있어요",
            "서 이사가 뜻과 좋은 점을 물어요", "이 Page에서 옛 이름을 읽는 법을 알아봐요"]
    return scene(a, "설명서의 옛 이름", "서 이사가 Full Cone을 물어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    b = [ppl(a, 110, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 850, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         pc(250, 285), router(370, 285, "박 팀장 쪽"), router(590, 285, "지우 쪽"), pc(710, 285),
         line(280, 285, 342, 285, LINE, 4) + line(398, 285, 562, 285, LINE, 4, "10 8") + line(618, 285, 680, 285, LINE, 4),
         a.vis(packet(465, 285, BLUE), 2, 4) + a.vis(cross(530, 285), 2, 4), mark(a, 430, 250, 120, 70, 2),
         a.vis(thought(700, 150, "지우 쪽에서 먼저 나간\n기록이 없어요", tail_to=(840, 200), color=BLUE), 3, 3),
         question(a, "양쪽에서 먼저 보내면 길이 열릴까?")]
    caps = ["두 PC가 서로의 바깥 주소를 알게 되었어요", "박 팀장 쪽이 먼저 보낸 패킷이 막힐 수 있어요",
            "지우 쪽에서 먼저 나간 기록이 없기 때문이에요", "이 Page에서 길을 여는 방법을 알아봐요"]
    return scene(a, "먼저 보낸 패킷이 막히면", "박 팀장 PC와 지우 PC 사이예요", caps, "".join(b), bg="office")


def p7():
    a = new()
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(line(260, 285, 700, 285, LINE, 4, "10 8"), 1, 4),
         a.vis(cross(480, 285), 2, 4) + "".join(a.vis(pill(480, y, s, TXT, 17), 2, 2) for y, s in
                ((215, "상대에 따라 달라지는 매핑"), (345, "회사 방화벽의 UDP 차단"), (385, "통신사 NAT가 여러 겹"))), mark(a, 440, 245, 80, 80, 2),
         a.vis(thought(640, 150, "이번 회의가 어느 방식이었는지\n확인해서 알려 드리자", tail_to=(800, 200), color=BLUE), 3, 3),
         question(a, "직접 못 만나면 누가 대신 전해 줄까?")]
    caps = ["지우가 박 팀장의 회의 연결을 살펴봐요", "직접 연결이 되지 않는 환경이 겹칠 수 있어요",
            "지우는 이번 회의의 방식을 확인하기로 해요", "이 Page에서 대신 전해 주는 방법을 알아봐요"]
    return scene(a, "직접 연결이 안 되면", "홀 펀칭이 항상 되지는 않아요", caps, "".join(b), bg="office")


NAMES = ["outbound-ticket", "wrong-memo", "address-not-arrive", "same-ip-different", "old-name-question", "blocked-first-packet", "direct-fails"]

if __name__ == "__main__":
    for i, (fn, n) in enumerate(zip((p1, p2, p3, p4, p5, p6, p7), NAMES), 1):
        write(OUT, f"u12-l05-p0{i}-story-{n}", fn())
        print(f"u12-l05-p0{i}-story-{n}.svg")
