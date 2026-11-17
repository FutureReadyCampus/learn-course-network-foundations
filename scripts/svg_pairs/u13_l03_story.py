#!/usr/bin/env python3
"""Unit 13 Lesson 3 situation SVGs (4 steps each, one per Page), admin-tutorial story.
Run from the repo root: python3 scripts/svg_pairs/u13_l03_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from u11_l01_story import HY, mk_bubble, ppl  # also applies the admin-tutorial ROLES override

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("09-*/lessons/restructured/03-*")) / "assets" / "animations"


def sp(a, x, who, moods, facing="right"):
    return ppl(a, x, who, moods, facing=facing, role_step1=True)


def p1():
    a = new()
    s = "도쿄 지사 직원만 첫 화면이\n1~2초씩 더 늦게 떠요"
    b = [a.vis(pill(480, 150, "고객용 예약·문의 사이트", MUTED, 17), 1, 1),
         sp(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)]),
         sp(a, 810, "지우", [("normal", 1, 3), ("thinking", 4, 4)], facing="left"),
         a.vis(clock(400, 285, "서울 응답 시간") + clock(560, 285, "도쿄 응답 시간"), 2, 4), mark(a, 340, 245, 280, 110, 2),
         a.vis(bubble(330, 160, s, tail_to=(160, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 330, 160, s, 3),
         a.vis(thought(640, 160, "서버 대수는 충분한데\n왜 느린가", tail_to=(800, 200), color=BLUE), 4, 4),
         question(a, "서버가 충분한데 왜 느릴까?")]
    caps = ["회사가 일본 거래처에도 예약·문의 사이트를 열었어요", "지우가 서울과 도쿄의 첫 화면 응답 시간을 재 봐요",
            "박 팀장이 티켓을 올려요", "서 이사에게 설명할 이유를 찾아봐요"]
    return scene(a, "일본에서만 느린 예약 사이트", "박 팀장이 티켓을 올렸어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [sp(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(pill(270, 150, "서울 203.0.113.10", GREEN, 17) + pill(690, 150, "도쿄 203.0.113.20", GREEN, 17), 1, 4),
         a.vis(alert_card(600, 320, "도쿄 점검 중에도 일부 손님이 도쿄로"), 2, 4), mark(a, 420, 288, 360, 64, 2),
         a.vis(thought(340, 235, "알아서 살아 있는 곳으로\n갈 줄 알았는데", tail_to=(175, 215), color=BLUE), 3, 3),
         question(a, "DNS는 살아 있는 곳을 알까?")]
    caps = ["지우가 이름 하나에 서울과 도쿄 주소 둘을 등록했어요", "도쿄를 점검하는데도 일부 손님이 도쿄로 가요",
            "지우는 알아서 살아 있는 곳으로 갈 줄 알았어요", "이 Page에서 DNS가 아는 것을 알아봐요"]
    return scene(a, "주소를 둘 등록했는데도", "점검 중인 도쿄로 손님이 갔어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    b = [sp(a, 200, "지우", [("normal", 1, 3), ("thinking", 4, 4)]),
         a.vis(doc(700, 285, "고객 안내문"), 1, 4) + a.vis(pill(700, 195, "book.company.example", MUTED, 17), 1, 4),
         a.vis(pill(480, 385, "인쇄한 뒤에도 지역 구성은 바꾸고 싶다", MUTED, 17), 2, 2), mark(a, 290, 361, 380, 48, 2),
         a.vis(thought(390, 150, "이름은 하나만 쓰고, 지역은\nGSLB 쪽에서 바꾸고 싶다", tail_to=(215, 200), color=BLUE), 3, 3),
         question(a, "이름 하나로 지역마다 다른 주소를?")]
    caps = ["고객 안내문에는 이름 하나만 적어요", "안내문을 인쇄한 뒤에도 지역 구성은 바꿀 수 있어야 해요",
            "지역은 GSLB를 맡은 쪽에서 바꾸고 싶어요", "이 Page에서 이름 하나로 지역을 나눠 봐요"]
    return scene(a, "안내문엔 이름 하나만", "지역 구성은 나중에 바꿀 수 있어야 해요", caps, "".join(b), bg="office")


def p4():
    a = new()
    s = "다른 PC는 도쿄로 잘 가는데\n이 노트북만 느려요"
    b = [sp(a, 130, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)]),
         sp(a, 830, "지우", [("normal", 1, 3), ("thinking", 4, 4)], facing="left"),
         a.vis("".join(pc(x, 285) for x in (330, 430, 530)) + laptop(640, 290), 1, 4) + a.vis(text(480, 372, "도쿄 지사", 17, TXT, 700), 1, 4),
         a.vis(pill(640, 220, "서울 사이트로 안내", ORANGE, 17), 2, 4), mark(a, 540, 193, 200, 140, 2),
         a.vis(bubble(330, 160, s, tail_to=(150, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 330, 160, s, 3),
         a.vis(thought(680, 150, "이 노트북만\n왜 다를까?", tail_to=(815, 200), color=BLUE), 4, 4),
         question(a, "DNS는 손님이 어디 있는지 어떻게 알까?")]
    caps = ["도쿄 지사에는 PC 여러 대와 노트북 한 대가 있어요", "노트북 한 대만 서울 사이트로 안내돼요",
            "박 팀장이 이 노트북만 느리다고 티켓을 올려요", "지우는 이 노트북만 왜 다른지 궁금해요"]
    return scene(a, "노트북 한 대만 서울로", "같은 지사의 다른 PC는 도쿄로 잘 가요", caps, "".join(b), bg="office")


def p5():
    a = new()
    s = "한국 손님은 서울로,\n일본 손님은 도쿄로"
    b = [sp(a, 150, "서 이사", [("normal", 1, 1), ("worried", 2, 4)]),
         sp(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         pill(400, 285, "서울 사이트", GREEN, 18) + pill(560, 285, "도쿄 사이트", GREEN, 18),
         a.vis(bubble(330, 165, s, tail_to=(165, 203), color=VIOLET), 2, 2), mk_bubble(a, 330, 165, s, 2),
         a.vis(thought(660, 150, "IP 주소만으로 나라를\n확실히 알 수 있을까?", tail_to=(795, 200), color=BLUE), 3, 3),
         question(a, "IP 주소만 보고 나라를 알 수 있을까?")]
    caps = ["서울과 도쿄 두 사이트가 있어요", "서 이사가 손님을 나라별로 나눠 달라고 해요",
            "지우는 IP 주소만으로 나라를 알 수 있을지 생각해요", "이 Page에서 IP 주소로 알 수 있는 것을 알아봐요"]
    return scene(a, "나라별로 확실히 나눠 주세요", "서 이사가 요청했어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    b = [sp(a, 480, "지우", [("normal", 1, 3), ("thinking", 4, 4)]),
         a.vis(doc(240, 285, "서울 사이트") + doc(720, 285, "도쿄 사이트"), 1, 1),
         a.vis(doc(240, 285, "새 요금표", GREEN) + doc(720, 285, "예전 요금표", ORANGE), 2, 4), mark(a, 660, 245, 120, 140, 2),
         a.vis(alert_card(480, 150, "일본 고객만 예전 요금으로 견적"), 3, 4), mark(a, 300, 118, 360, 64, 3),
         question(a, "서울과 도쿄가 다른 답을 한다면?")]
    caps = ["같은 예약 사이트가 서울과 도쿄에 있어요", "요금표를 바꿨는데 도쿄만 예전 그대로예요",
            "다음 날 일본 고객이 예전 요금으로 견적을 받았다는 티켓이 와요", "이 Page에서 어긋난 이유를 찾아봐요"]
    return scene(a, "일본 고객만 예전 요금으로", "요금표를 바꾼 다음 날 티켓이 왔어요", caps, "".join(b), bg="office")


def p7():
    a = new()
    b = [sp(a, 160, "고객", [("normal", 1, 1), ("worried", 2, 4)]),
         a.vis(pill(160, 150, "도쿄 고객", TEAL, 17), 1, 4),
         sp(a, 810, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(monitor(330, 285, "loading", "첫 화면 로딩 중"), 2, 4), mark(a, 220, 225, 220, 112, 2),
         a.vis(doc(560, 285, "고화질 사진"), 2, 4),
         a.vis(thought(660, 150, "모든 손님이 같은 사진을\n매번 서울에서 내려받는다", tail_to=(790, 200), color=BLUE), 3, 3),
         question(a, "사진은 더 가까이 둘 수 없을까?")]
    caps = ["일본 고객이 예약 사이트를 열어요", "상품 소개 고화질 사진 때문에 첫 화면이 느려요",
            "지우는 사진을 매번 서울에서 내려받고 있었다는 걸 알아채요", "이 Page에서 파일을 가까이 두는 법을 알아봐요"]
    return scene(a, "사진 때문에 첫 화면이 느려요", "도쿄 고객의 화면이 늦게 떠요", caps, "".join(b), bg="office")


def p8():
    a = new()
    b = [sp(a, 480, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(pill(260, 170, "도쿄 웹 서버 3대", GREEN, 17), 1, 4),
         a.vis(alert_card(260, 250, "서버 한 대 고장"), 2, 4), mark(a, 140, 218, 240, 64, 2),
         a.vis(thought(700, 200, "도쿄 전체를 빼야 할까?\n모두 서울로 몰리면?", tail_to=(500, 215), color=BLUE, fs=17), 3, 3),
         question(a, "지역은 누가, 서버는 누가 고를까?")]
    caps = ["도쿄 사이트에는 웹 서버가 세 대 있어요", "그중 한 대가 고장 났어요",
            "GSLB가 도쿄 전체를 빼야 할지 지우가 따져 봐요", "이 Page에서 일을 나눠 맡을 곳을 알아봐요"]
    return scene(a, "서버 한 대가 고장 나면", "도쿄 사이트에 문제가 생겼어요", caps, "".join(b), bg="office")


NAMES = ["latency-ticket", "two-addresses", "one-name", "one-laptop", "country-request", "old-price", "slow-photo", "one-server-down"]

if __name__ == "__main__":
    for i, (fn, n) in enumerate(zip((p1, p2, p3, p4, p5, p6, p7, p8), NAMES), 1):
        write(OUT, f"u13-l03-p0{i}-story-{n}", fn())
        print(f"u13-l03-p0{i}-story-{n}.svg")
