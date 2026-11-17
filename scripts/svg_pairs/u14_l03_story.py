#!/usr/bin/env python3
"""Unit 14 Lesson 3 situation SVGs (4 steps each, one per Page), admin-tutorial story: 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u14_l03_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("10-*/lessons/restructured/03-*")) / "assets" / "animations"
HY = 225


def ppl(a, x, who, moods, facing="right"):
    """moods = [(mood, t0, t1), ...]. Role line in step 1 only."""
    out = ""
    for mood, t0, t1 in moods:
        if t0 == 1:
            out += a.vis(person(x, HY, who, mood, facing=facing, role=True), 1, 1)
            if t1 > 1:
                out += a.vis(person(x, HY, who, mood, facing=facing), 2, t1)
        else:
            out += a.vis(person(x, HY, who, mood, facing=facing), t0, t1)
    return out


def mk_bubble(a, x, y, s, t):
    lines = wrap(s)
    w = max(tw(ln, 18) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def p1():
    a = new()
    scr = (box(400, 205, 320, 130, BLUE, PANEL, 10, sw=4)
           + f'<rect x="552" y="335" width="16" height="14" fill="{LINE}"/><rect x="524" y="349" width="72" height="7" rx="3" fill="{LINE}"/>')
    chips = "".join(pill(x, 300, s, BLUE, 17) for x, s in ((448, "IKE"), (518, "SA"), (586, "ESP"), (664, "NAT-T")))
    b = [ppl(a, 170, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         scr, a.vis(text(560, 245, "도쿄 지사 SG 교체", 18, TXT, 700), 1, 1),
         a.vis(text(560, 245, "새 장비 설정 화면", 18, TXT, 700), 2, 4),
         a.vis(chips, 2, 4), mark(a, 405, 275, 310, 52, 2),
         a.vis(thought(330, 150, "낯선 단어가 가득해요", tail_to=(180, 200), color=BLUE), 3, 3),
         question(a, "IPsec은 어떤 조각으로 이뤄졌을까?")]
    caps = ["도쿄 지사 SG를 교체하는 날이에요", "새 장비 설정 화면에 IKE, SA, ESP, NAT-T가 보여요",
            "지우에게는 아직 낯선 단어예요", "이 Page에서 IPsec을 네 조각으로 나눠 봐요"]
    return scene(a, "새 장비 설정 화면을 열었어요", "낯선 단어가 가득해요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         router(430, 285, "서울 본사 SG") + router(700, 285, "도쿄 지사 SG"),
         a.vis(line(470, 285, 660, 285, LINE, 4, "10 8"), 1, 4),
         a.vis(alert_card(565, 205, "협상 실패"), 2, 4), mark(a, 485, 177, 160, 56, 2),
         a.vis(thought(290, 150, "연결 자체는\n확인했는데…", tail_to=(160, 200), color=BLUE), 3, 3),
         question(a, "처음 만난 두 장비는 뭘 정할까?")]
    caps = ["두 SG 사이에 터널을 열려고 해요", "터널이 '협상 실패'에서 멈춰요",
            "연결 자체는 확인했어요", "이 Page에서 두 장비가 먼저 정할 것을 알아봐요"]
    return scene(a, "터널이 협상 실패에서 멈췄어요", "도쿄 지사 SG를 새 장비로 바꾼 뒤예요", caps, "".join(b), bg="office")


def p3():
    a = new()
    s = "누가 본사 SG인 척하면 어쩌죠?"
    b = [a.vis(meeting_table(480, 410), 1, 3),
         ppl(a, 340, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 620, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], facing="left"),
         a.vis(bubble(730, 150, s, tail_to=(625, 203), color=VIOLET), 2, 2), mk_bubble(a, 730, 150, s, 2),
         a.vis(thought(330, 150, "끝에 있는 상대가\n가짜라면 소용없어", tail_to=(340, 200), color=BLUE), 3, 3),
         question(a, "상대가 진짜인지 어떻게 확인할까?")]
    caps = ["서 이사가 지우에게 말을 걸어요", "서 이사가 가짜 SG를 걱정해요",
            "암호화해도 끝의 상대가 가짜라면 소용이 없어요", "이 Page에서 상대 확인 방법을 알아봐요"]
    return scene(a, "누가 본사 SG인 척하면?", "서 이사의 날카로운 질문이에요", caps, "".join(b), bg="office")


def p4():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         a.vis(monitor(560, 275, "loading", "SG 설정 화면"), 1, 4),
         a.vis(pill(480, 385, "ESP", BLUE, 20) + pill(640, 385, "AH", BLUE, 20), 2, 2), mark(a, 395, 363, 310, 44, 2),
         a.vis(thought(310, 150, "기밀성·무결성·인증,\n어디에 해당할까?", tail_to=(165, 200), color=BLUE), 3, 3),
         question(a, "ESP와 AH는 뭘 지켜 줄까?")]
    caps = ["지우가 SG 설정 화면을 보고 있어요", "보호 방식으로 ESP와 AH 두 가지를 고르라고 해요",
            "지우는 세 가지 보호 중 어디에 해당하는지 따져 봐요", "이 Page에서 둘이 지키는 것을 알아봐요"]
    return scene(a, "보호 방식을 고르라고 해요", "선택지는 ESP와 AH예요", caps, "".join(b), bg="office")


def p5():
    a = new()
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)]),
         a.vis(pill(150, 360, "집", MUTED, 17), 1, 1),
         monitor(430, 285, "loading", "VPN 연결 중"),
         a.vis(router(660, 285, "집 공유기"), 3, 4), mark(a, 610, 245, 100, 100, 3),
         a.vis(alert_card(550, 195, "시간 초과"), 2, 4), mark(a, 475, 167, 150, 56, 2),
         question(a, "공유기가 끼면 무슨 일이 생길까?")]
    caps = ["박 팀장이 집에서 VPN을 켰어요", "연결이 한참 멈췄다가 시간 초과가 나요",
            "두 장비 사이에 집 공유기가 끼어 있어요", "이 Page에서 공유기(NAT)의 영향을 알아봐요"]
    return scene(a, "집에서 켠 VPN이 멈췄어요", "박 팀장의 노트북 화면이에요", caps, "".join(b), bg="office")


def p6():
    a = new()
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)]),
         a.vis(pill(150, 360, "출장지 호텔 와이파이", MUTED, 17), 1, 1),
         a.vis(monitor(400, 285, "error", "IPsec VPN 안 됨"), 2, 4), mark(a, 295, 229, 210, 112, 2),
         a.vis(monitor(640, 285, "ok", "웹사이트는 열려요"), 3, 3), mark(a, 535, 229, 210, 112, 3),
         question(a, "웹만 열린 곳에서 붙는 VPN은?")]
    caps = ["서 이사가 출장지 호텔에 있어요", "호텔 와이파이에서 IPsec VPN을 쓰지 못해요",
            "그런데 웹사이트는 잘 열려요", "이 Page에서 브라우저로 붙는 SSL VPN을 알아봐요"]
    return scene(a, "호텔에서 VPN이 안 붙어요", "웹사이트는 잘 열리는데요", caps, "".join(b), bg="office")


NAMES = ["tool-screen", "negotiation-fail", "fake-sg", "esp-ah-choice", "home-router", "hotel-wifi"]

if __name__ == "__main__":
    for i, fn in enumerate((p1, p2, p3, p4, p5, p6), 1):
        write(OUT, f"u14-l03-p{i}-story-{NAMES[i-1]}", fn())
        print(f"u14-l03-p{i}-story-{NAMES[i-1]}.svg")
