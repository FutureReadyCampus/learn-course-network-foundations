#!/usr/bin/env python3
"""Unit 14 Lesson 1 situation SVGs (4 steps each, one per Page): 왜 VPN인가.
Run from the repo root: python3 scripts/svg_pairs/u14_l01_story.py"""
from pathlib import Path

from u11_l01_story import *  # noqa: F401,F403  (hangyeol_cast + ROLES override + ppl/mk_bubble helpers)
from u11_l01_story import ppl, HY

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("10-*/lessons/restructured/01-*")) / "assets" / "animations"


def mk_bubble(a, x, y, s, t, fs=18):
    lines = wrap(s, fs)
    w = max(tw(ln, fs) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def p1():
    a = new()
    t = "지사도, 저도 사내 그룹웨어에서\n전자결재 올릴 수 있죠?"
    b = [ppl(a, 300, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 700, "박 팀장", [("normal", 1, 2), ("normal", 3, 4)], facing="left", role_step1=True),
         a.vis(pill(480, 150, "월요일 아침", MUTED, 17), 1, 1),
         a.vis(doc(480, 300, "도쿄 지사 6명 요청"), 2, 3), mark(a, 402, 258, 156, 118, 2),
         a.vis(bubble(700, 150, t, tail_to=(700, 195), color=TERRACOTTA, fs=17), 3, 3), mk_bubble(a, 700, 150, t, 3, 17),
         question(a, "집에서는 왜 그룹웨어가 안 보일까?")]
    caps = ["월요일 아침, 지우의 티켓함이에요", "도쿄 지사 직원 여섯 명의 새 요청이 올라왔어요",
            "박 팀장도 주 2일 재택을 시작하며 거들어요", "이 Page에서 그룹웨어가 안 열리는 이유를 알아봐요"]
    return scene(a, "지사도 재택도 그룹웨어를 쓰고 싶어요", "새 요청이 올라온 월요일이에요", caps, "".join(b), bg="office")


def p2():
    a = new()
    t = "'그냥 쓰게 해 주세요'는\n세 가지가 뭉쳐 있었어"
    b = [a.vis(line(205, 290, 755, 290, LINE, 4, "10 8"), 2, 2),
         ppl(a, 480, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         house(150, 290, "도쿄 지사", GREY) + text(150, 395, "직원 6명", 17, TXT, 700), house(810, 290, "본사", BLUE),
         a.vis(pill(480, 395, "사이에는 공용 인터넷뿐", MUTED, 17), 2, 2), mark(a, 372, 372, 216, 46, 2),
         a.vis(thought(480, 150, t, tail_to=(480, 200), color=BLUE, w=300), 3, 3),
         question(a, "지우는 이 요구를 어떻게 쪼갤까?")]
    caps = ["도쿄 지사 직원 여섯 명과 본사를 이어야 해요", "우리가 깐 선은 없고 공용 인터넷뿐이에요",
            "지우는 요구가 한 덩어리가 아니라는 걸 알아채요", "이 Page에서 요구를 세 가지로 쪼개 봐요"]
    return scene(a, "지사 직원은 본사 그룹웨어를 어떻게 쓰지", "그냥 쓰게 해 달라는 요청이에요", caps, "".join(b), bg="office")


def p3():
    a = new()
    q = "서울과 도쿄 사이에 우리\n전용 선을 깔면 안전하지 않나요?"
    w = "안전한 건 알겠는데\n지점이 늘면 감당이 안 되겠네요"
    b = [a.vis(meeting_table(480, 385), 1, 3),
         ppl(a, 340, "지우", [("normal", 1, 3), ("thinking", 4, 4)], role_step1=True),
         ppl(a, 620, "서 이사", [("normal", 1, 1), ("normal", 2, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(bubble(720, 150, q, tail_to=(625, 200), color=VIOLET, fs=16), 2, 2), mk_bubble(a, 720, 150, q, 2, 16),
         a.vis(bubble(720, 150, w, tail_to=(625, 200), color=VIOLET, fs=16), 3, 3), mk_bubble(a, 720, 150, w, 3, 16),
         question(a, "전용 회선의 대가는 무엇일까?")]
    caps = ["회의에서 서 이사가 지우에게 물어요", "서 이사가 전용 선을 깔면 어떠냐고 해요",
            "서 이사가 고개를 갸웃해요", "이 Page에서 전용 회선의 대가를 따져 봐요"]
    return scene(a, "아예 우리만의 회선을 깔면", "서 이사가 회의에서 물었어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    q = "그럼 도쿄로 보내는 견적서가\n인터넷 길에서 어떻게 보일까요?"
    b = [ppl(a, 300, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 700, "서 이사", [("normal", 1, 1), ("happy", 2, 4)], facing="left", role_step1=True),
         a.vis(pill(480, 150, "전용 회선이 비싸다면", MUTED, 17), 1, 1),
         a.vis(pill(700, 150, "인터넷은 싸고 속도도 충분", VIOLET, 17), 2, 2), mark(a, 570, 132, 260, 36, 2),
         a.vis(bubble(300, 150, q, tail_to=(300, 195), color=BLUE, fs=16), 3, 3), mk_bubble(a, 300, 150, q, 3, 16),
         question(a, "인터넷으로 보내면 무엇이 걱정일까?")]
    caps = ["전용 회선이 비싸다면 어떻게 할까요?", "인터넷은 싸고 속도도 충분해서 서 이사가 솔깃해요",
            "지우가 티켓에 적어 둔 질문을 던져요", "이 Page에서 인터넷의 걱정거리를 알아봐요"]
    return scene(a, "인터넷을 그냥 쓰면 뭐가 걱정일까", "지우가 서 이사에게 질문을 던져요", caps, "".join(b), bg="office")


def p5():
    a = new()
    q1 = "VPN을 켜면 회선이\n하나 더 생기는 거예요?"
    q2 = "통신사에 따로\n신청해야 하나요?"
    b = [ppl(a, 280, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 680, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(bubble(300, 150, q1, tail_to=(285, 195), color=TERRACOTTA), 2, 2), mk_bubble(a, 300, 150, q1, 2),
         a.vis(bubble(300, 150, q2, tail_to=(285, 195), color=TERRACOTTA), 3, 3), mk_bubble(a, 300, 150, q2, 3),
         question(a, "VPN은 새 선일까, 인터넷 위의 통로일까?")]
    caps = ["박 팀장이 지우에게 VPN을 물어요", "VPN을 켜면 회선이 하나 더 생기는지 궁금해해요",
            "통신사에 따로 신청해야 하는지도 물어요", "이 Page에서 VPN이 어떤 연결인지 알아봐요"]
    return scene(a, "VPN은 인터넷 위에 무엇을 씌울까", "박 팀장이 많은 사람이 하는 오해를 물어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    t = "둘을 구분하는 말부터\n정해야 해"
    b = [ppl(a, 480, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         house(150, 285, "도쿄 지사", GREY) + text(150, 385, "PC 여섯 대와 프린터", 17, TXT, 700),
         laptop(810, 285, "박 팀장 노트북 한 대", TERRACOTTA),
         a.vis(pill(150, 175, "VPN", ORANGE, 20), 2, 4) + a.vis(pill(810, 175, "VPN", ORANGE, 20), 2, 4), mark(a, 100, 155, 100, 40, 2) + mark(a, 760, 155, 100, 40, 2),
         a.vis(thought(480, 150, t, tail_to=(480, 200), color=BLUE), 3, 3),
         question(a, "지사용과 재택용 VPN은 뭐가 다를까?")]
    caps = ["연결할 대상은 도쿄 지사와 박 팀장의 노트북이에요", "둘 다 VPN이라고 부르지만 규모가 달라요",
            "지우는 둘을 구분하는 말부터 정하려 해요", "이 Page에서 두 VPN을 구분해 봐요"]
    return scene(a, "지사용 VPN과 재택용 VPN", "연결할 대상의 규모가 달라요", caps, "".join(b), bg="office")


def p7():
    a = new()
    q = "결국 싸면서 전용 회선만큼\n안전하다는 거죠?"
    t = "반은 맞고 반은 틀린 말이야"
    b = [ppl(a, 300, "지우", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 700, "서 이사", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(bubble(700, 150, q, tail_to=(700, 195), color=VIOLET), 2, 2), mk_bubble(a, 700, 150, q, 2),
         a.vis(thought(300, 150, t, tail_to=(300, 200), color=BLUE, w=300), 3, 3),
         question(a, "VPN이면 전용 회선만큼 안전할까?")]
    caps = ["VPN 이야기를 들은 서 이사가 정리해요", "서 이사가 싸면서 안전하다는 거냐고 물어요",
            "지우는 잠깐 망설여요", "이 Page에서 두 방식의 안전을 견줘 봐요"]
    return scene(a, "VPN이면 전용 회선만큼 안전할까", "서 이사의 정리에 지우가 망설여요", caps, "".join(b), bg="office")


NAMES = ["groupware-ticket", "three-needs", "leased-line-ask", "internet-worry", "vpn-question", "two-vpns", "safe-as-leased"]

if __name__ == "__main__":
    for i, (nm, fn) in enumerate(zip(NAMES, (p1, p2, p3, p4, p5, p6, p7)), 1):
        write(OUT, f"u14-l01-p{i}-story-{nm}", fn())
        print(f"u14-l01-p{i}-story-{nm}.svg")
