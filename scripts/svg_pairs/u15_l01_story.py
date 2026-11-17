#!/usr/bin/env python3
"""Unit 15 Lesson 1 situation SVGs (4 steps each, one per Page), admin-tutorial story: 신입 IT·보안 담당 지우 + 점검.
Run from the repo root: python3 scripts/svg_pairs/u15_l01_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 IT·보안 담당", "박 팀장": "팀장", "서 이사": "경영진"})  # shared dict, this process only

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("15-*/lessons/restructured/01-*")) / "assets" / "animations"
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


def mk_bubble(a, x, y, s, t, w=None):
    lines = wrap(s)
    w = w or max(tw(ln, 18) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def server(x, y, label=None):
    out = "".join(box(x - 36, y - 40 + i * 30, 72, 26, BLUE, PANEL, 5, sw=3)
                  + f'<circle cx="{x + 22}" cy="{y - 27 + i * 30}" r="3" fill="{BLUE}"/>' for i in range(3))
    return out + (text(x, y + 66, label, 17, TXT, 700) if label else "")


def p1():
    a = new()
    q = "우리 회사, 지금 안전하다고\n답할 수 있어요?"
    b = [ppl(a, 110, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 440, "지우", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(275, 320, "보안 점검표"), 1, 4), mark(a, 220, 275, 110, 118, 1),
         a.vis(bubble(280, 150, q, tail_to=(125, 200), color=VIOLET), 2, 2), mk_bubble(a, 280, 150, q, 2),
         a.vis(line(640, 300, 760, 300, LINE, 4, "10 8") + laptop(580, 300, "박 팀장 노트북", TERRACOTTA)
               + server(830, 300, "그룹웨어 서버"), 3, 4)
         + a.vis(text(700, 240, "관리 화면까지 열려요", 16, RED, 700), 3, 3), mark(a, 520, 215, 360, 190, 3),
         question(a, "점검을 어떤 질문으로 쪼갤까?")]
    caps = ["서 이사가 거래처 점검표를 들고 와요", "서 이사가 안전한지 물어요",
            "점검 첫날, 박 팀장 노트북이 서버 관리 화면까지 닿아요", "이 Page에서 점검의 순서를 세워 봐요"]
    return scene(a, "우리 회사, 안전한가요", "신입 IT·보안 담당 지우에게 점검이 맡겨졌어요", caps, "".join(b), bg="office")


def p2():
    a = new()
    rows = ["지우 PC  192.168.10.41", "박 팀장 PC  192.168.10.42"]
    led = box(330, 160, 300, 170, GREEN, PANEL, 10, sw=3) + text(480, 190, "IP·MAC 장부", 17, TXT, 700)
    led += "".join(text(480, 226 + i * 34, r, 16, TXT) for i, r in enumerate(rows))
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(doc(480, 250, "엑셀 장부"), 1, 1),
         a.vis(led + text(480, 306, "사무실 PC 40여 대", 16, MUTED), 2, 4), mark(a, 322, 152, 316, 186, 2),
         a.vis(laptop(810, 290, "회의실 노트북", TERRACOTTA) + text(810, 226, "장부에 없음", 17, RED, 700), 3, 4), mark(a, 740, 205, 140, 150, 3),
         question(a, "회사 기기인지 무엇으로 알아볼까?")]
    caps = ["지우는 먼저 엑셀 장부를 만들어요", "사무실 PC의 IP·MAC을 한 줄씩 적어요",
            "회의실 노트북은 장부에 없어요", "이 Page에서 알아보는 기준을 찾아봐요"]
    return scene(a, "회사 기기는 장부에 있어요", "지우가 이름표 대신 장부를 만들어요", caps, "".join(b), bg="office")


def p3():
    a = new()
    t = "왜 끊겼지?\n어디에 물어야 하지?"
    b = [ppl(a, 150, "지우", [("normal", 1, 4)], role_step1=True),
         ppl(a, 820, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         switch(390, 300, "2층 스위치"), laptop(620, 300, "회의실 노트북", TERRACOTTA),
         a.vis(line(442, 300, 576, 300, LINE, 4), 1, 1),
         a.vis(line(442, 300, 576, 300, RED, 4, "6 10") + alert_card(620, 225, "케이블이 연결되지 않음"), 2, 4), mark(a, 490, 195, 260, 60, 2),
         a.vis(thought(720, 135, t, tail_to=(800, 195), color=TERRACOTTA), 3, 3), mk_bubble(a, 720, 135, t, 3),
         question(a, "포트를 내리면 끝일까?")]
    caps = ["회의실 벽면 포트에 노트북이 꽂혀 있어요", "NAC가 포트를 내리자 화면에 표시만 떠요",
            "막힌 사람은 이유도, 물어볼 곳도 몰라요", "이 Page에서 포트 차단을 따져 봐요"]
    return scene(a, "포트를 내려 막았더니", "노트북 화면에 표시 하나만 떠요", caps, "".join(b), bg="office")


def p4():
    a = new()
    s = "누가 중간에서\n가로챈 것 같아요"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("surprised", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(monitor(480, 285, "ok", "웹사이트 열기"), 1, 1),
         a.vis(monitor(480, 285, "loading", "기기 등록 안내"), 2, 4), mark(a, 375, 229, 210, 112, 2),
         a.vis(bubble(300, 150, s, tail_to=(165, 200), color=TERRACOTTA), 3, 3), mk_bubble(a, 300, 150, s, 3),
         question(a, "안내 페이지는 왜 뜰까?")]
    caps = ["다른 방식의 NAC를 켜고, 박 팀장이 웹사이트를 열어요", "열 때마다 기기 등록 안내 페이지가 떠요",
            "박 팀장이 놀라 지우에게 말해요", "이 Page에서 안내가 뜨는 이유를 알아봐요"]
    return scene(a, "열 때마다 안내 페이지가 떠요", "막힌 게 아니라 안내를 받았어요", caps, "".join(b), bg="office")


def p5():
    a = new()
    s = "애초에 확인된 기기만\n들어오게 할 수 없어요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(pill(480, 190, "포트 차단", MUTED, 17) + pill(480, 240, "안내 페이지", MUTED, 17), 1, 1),
         a.vis(box(380, 170, 200, 160, MUTED, PANEL, 10, dash=True) + text(480, 198, "사내망", 17, TXT, 700)
               + laptop(480, 262, None, TERRACOTTA) + pill(480, 345, "이미 들어온 기기", RED, 17), 2, 4), mark(a, 372, 162, 216, 216, 2),
         a.vis(bubble(300, 150, s, tail_to=(165, 200), color=VIOLET), 3, 3), mk_bubble(a, 300, 150, s, 3),
         question(a, "들어오기 전에 신분을 확인하려면?")]
    caps = ["지금까지 본 방식들이에요", "모두 이미 들어온 기기를 쫓아내서 한발 늦어요",
            "서 이사가 들어오기 전 확인을 물어요", "이 Page에서 문 앞의 확인을 알아봐요"]
    return scene(a, "늘 한발 늦는 방식", "서 이사가 다른 방법을 물어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    t = "유선 포트만 지키면\n이 샛길은 못 보네"
    b = [ppl(a, 150, "직원", [("normal", 1, 4)]),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         pc(330, 250), a.vis(line(370, 250, 470, 250, LINE, 4) + box(470, 220, 90, 60, MUTED, PANEL, 10) + text(515, 257, "사내망", 17, TXT, 700), 1, 4),
         a.vis(phone(330, 355) + line(330, 280, 330, 312, ORANGE, 4) + line(372, 355, 640, 355, ORANGE, 4, "8 8")
               + text(690, 361, "바깥", 17, TXT, 700) + text(410, 335, "핫스팟", 16, TXT, 700), 2, 4),
         mark(a, 296, 305, 420, 95, 2),
         a.vis(thought(680, 145, t, tail_to=(790, 200), color=BLUE), 3, 3), mk_bubble(a, 680, 145, t, 3),
         question(a, "몰래 켠 와이파이는 누가 찾을까?")]
    caps = ["직원이 사내 PC를 랜에 꽂아 두었어요", "휴대폰 핫스팟에도 동시에 붙으면 바깥으로 샛길이 생겨요",
            "지우는 유선 NAC가 이 샛길을 못 본다고 깨달아요", "이 Page에서 샛길을 찾는 장치를 알아봐요"]
    return scene(a, "랜에 꽂고 핫스팟도 켰어요", "사내망과 바깥을 잇는 샛길이에요", caps, "".join(b), bg="office")


NAMES = {"p1": "four-questions", "p2": "ledger", "p3": "port-down", "p4": "notice-page", "p5": "before-entry", "p6": "side-path"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u15-l01-{k}-story-{NAMES[k]}", fn())
        print(f"u15-l01-{k}-story-{NAMES[k]}.svg")
