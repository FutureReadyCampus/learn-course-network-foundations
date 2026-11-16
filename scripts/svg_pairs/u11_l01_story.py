#!/usr/bin/env python3
"""Unit 11 Lesson 1 situation SVGs (4 steps each, one per Page), using hangyeol_cast.
Run from the repo root: python3 scripts/svg_pairs/u11_l01_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("07-*/lessons/restructured/01-*")) / "assets" / "animations"
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


def mk_person(a, x, t):
    return mark(a, x - 44, HY - 32, 88, 160, t)


def mk_bubble(a, x, y, s, t, w=None):
    lines = wrap(s)
    w = w or max(tw(ln, 18) for ln in lines) + 36
    h = 26 * len(lines) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def memo_monitor(x, y):
    """Monitor with five numbered sticky notes (지우's screen)."""
    out = box(x - 95, y - 56, 190, 112, BLUE, PANEL, 10, sw=4)
    for i in range(5):
        nx = x - 76 + i * 32
        out += box(nx - 12, y - 22, 26, 34, MUTED, BG, 4, sw=2) + text(nx + 1, y + 1, str(i + 1), 16, TXT, 700)
    out += (f'<rect x="{x - 8}" y="{y + 56}" width="16" height="14" fill="{LINE}"/>'
            f'<rect x="{x - 36}" y="{y + 70}" width="72" height="7" rx="3" fill="{LINE}"/>')
    return out


def p1():
    a = new()
    sign = pill(480, 150, "한결디자인 · 직원 40명", MUTED, 17)
    chat = chat_window(305, 270, ["시안 설명문", "", ""])
    b = [a.vis(sign, 1, 1),
         ppl(a, 120, "박 팀장", [("happy", 1, 1), ("worried", 2, 4)], role_step1=True),
         a.vis(chat, 1, 1),
         ppl(a, 520, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         ppl(a, 880, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], facing="left", role_step1=True),
         mark(a, 476, HY - 32, 88, 182, 1),
         a.vis(memo_monitor(700, 285), 2, 4) + a.vis(text(700, 392, "메모 다섯 장", 17, TXT, 700), 2, 3), mark(a, 605, 229, 190, 133, 2),
         a.vis(bubble(205, 160, "회사에서만 AI 사이트가\n안 열려요", tail_to=(126, 203), color=TERRACOTTA), 2, 2),
         a.vis(bubble(720, 160, "고객 도면을 AI에 붙여넣으면\n어떡하죠?", tail_to=(872, 203), color=VIOLET), 3, 3),
         mk_bubble(a, 720, 160, "고객 도면을 AI에 붙여넣으면\n어떡하죠?", 3),
         question(a, "다섯 고민을 세 갈래로 나눌 수 있을까?")]
    caps = ["박 팀장은 AI로 시안 설명문을 다듬고, 지우는 신입이에요", "첫 주가 지나자 지우의 모니터에 메모 다섯 장이 붙었어요",
            "서 이사는 고객 도면이 걱정돼요", "이 Page에서 다섯 고민을 나눠 봐요"]
    return scene(a, "AI를 들인 한결디자인의 첫 주", "지우, 박 팀장, 서 이사를 만나 봐요", caps, "".join(b), bg="office")


def p2():
    a = new()
    b = [ppl(a, 150, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 840, "서 이사", [("normal", 1, 4)], facing="left"),
         "".join(a.vis(pc(x, 275), 1, 4) for x in (260, 340, 420)) + a.vis(text(340, 325, "PC 40대", 17, TXT, 700), 1, 1),
         a.vis(line(455, 275, 565, 275, LINE, 4, "10 8") + router(600, 275, "출구 장치"), 2, 4), mark(a, 562, 237, 76, 100, 2),
         a.vis(bubble(700, 160, "특정 AI 사이트를\n막을 수는 있어요?", tail_to=(832, 203), color=VIOLET), 3, 3),
         mk_bubble(a, 700, 160, "특정 AI 사이트를\n막을 수는 있어요?", 3),
         question(a, "길 한가운데서 막는 장치는?")]
    caps = ["사무실 PC 40대의 요청은 모두 한 출구로 나가요", "그 자리에 출구 장치가 있어요",
            "서 이사가 특정 AI 사이트를 막을 수 있는지 물어요", "이 Page에서 막는 장치의 자리를 알아봐요"]
    return scene(a, "특정 AI 사이트를 막을 수 있을까", "서 이사의 질문을 받은 지우의 머릿속이에요", caps, "".join(b), bg="office")


def p3():
    a = new()
    s = "누가 어떤 AI를 얼마나\n쓰는지부터 알고 싶어요"
    b = [a.vis(meeting_table(480, 385), 1, 3),
         ppl(a, 340, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
         ppl(a, 620, "서 이사", [("normal", 1, 1), ("worried", 2, 4)], facing="left"),
         a.vis(bubble(700, 150, "당장 막자는 게 아니에요", tail_to=(615, 203), color=VIOLET), 2, 2), mk_bubble(a, 700, 150, "당장 막자는 게 아니에요", 2),
         a.vis(bubble(700, 150, s, tail_to=(615, 203), color=VIOLET), 3, 3), mk_bubble(a, 700, 150, s, 3),
         a.vis(thought(330, 150, "업무는 멈추면 안 된다는\n서 이사의 조건", tail_to=(340, 200), color=BLUE), 3, 3),
         question(a, "통신에 손대지 않고 지켜보는 장치는?")]
    caps = ["출구 장치에 차단 규칙을 걸 수 있다는 말을 들었어요", "서 이사는 당장 막자는 게 아니라고 해요",
            "알고 싶은 건 누가 어떤 AI를 쓰는지예요", "이 Page에서 지켜보기만 하는 장치를 알아봐요"]
    return scene(a, "막지 말고 먼저 알고 싶어요", "서 이사가 고개를 저었어요", caps, "".join(b), bg="office")


def p4():
    a = new()
    s = "고객 도면을 AI에 붙여넣으면\n어떡하죠?"
    pk = "".join(packet(480 + (i % 4) * 54, 255 + (i // 4) * 40, BLUE) for i in range(8))
    b = [ppl(a, 180, "서 이사", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         a.vis(doc(340, 285, "고객 도면"), 2, 2), mark(a, 306, 245, 68, 118, 2),
         a.vis(bubble(300, 150, s, tail_to=(190, 203), color=VIOLET), 2, 2),
         a.vis(doc(340, 285, "도면 파일 하나"), 3, 3),
         a.vis(pk + text(567, 345, "수천 개의 패킷 조각", 17, TXT, 700), 3, 3), mark(a, 454, 233, 220, 76, 3),
         a.vis(thought(700, 150, "조각을 모아\n조립해야 하나?", tail_to=(812, 200), color=BLUE), 3, 3),
         question(a, "대신 접속해 주는 장치는?")]
    caps = ["서 이사의 두 번째 메모는 고객 도면 걱정이에요", "도면을 AI에 붙여넣으면 어떡하냐고 물어요",
            "파일 하나는 수천 개의 패킷으로 쪼개져 와요", "이 Page에서 더 알맞은 구조를 찾아봐요"]
    return scene(a, "고객 도면이 AI로 나가면", "무엇을 올렸는지를 봐야 하는 걱정이에요", caps, "".join(b), bg="office")


def p5():
    a = new()
    s = "이 플러그인이 어디로 뭘 보내는지 알 수 있어요?"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 1), ("worried", 2, 4)]),
         ppl(a, 800, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left"),
         monitor(480, 285, "ok", "AI 플러그인"), mark(a, 380, 229, 200, 112, 1),
         a.vis(bubble(300, 150, s, tail_to=(168, 203), color=VIOLET, w=340), 2, 2),
         a.vis(thought(620, 150, "어느 주소로 가나?\n어떤 요청을 보냈나?", tail_to=(790, 200), color=BLUE), 3, 3),
         question(a, "패킷을 볼까, 대화를 볼까?")]
    caps = ["이번 주에 새로 깔린 AI 플러그인이 있어요", "서 이사가 어디로 뭘 보내는지 물어요",
            "지우는 이 한 문장에 질문이 두 개 있다는 걸 알아채요", "이 Page에서 어느 쪽을 볼지 정해 봐요"]
    return scene(a, "이 플러그인은 뭘 보낼까", "서 이사가 새 플러그인을 가리켰어요", caps, "".join(b), bg="office")


def p6():
    a = new()
    b = [ppl(a, 160, "서 이사", [("normal", 1, 4)]),
         ppl(a, 810, "지우", [("normal", 1, 2), ("surprised", 3, 4)], facing="left"),
         a.vis(doc(330, 270, "설명서"), 1, 1), mark(a, 276, 226, 108, 118, 1),
         "".join(a.vis(pill(x, y, s, TXT, 17), 2, 4) for x, y, s in
                 ((480, 215, "외부 사이트 차단"), (480, 265, "접속 기록"), (480, 315, "웹 필터링"))), mark(a, 390, 190, 180, 150, 2),
         a.vis(thought(620, 150, "이 상자는 Inline?\nOut of path·Proxy?", tail_to=(800, 200), color=BLUE, fs=16), 3, 3),
         question(a, "한 상자에 세 구조가 다 있다면?")]
    caps = ["한 달 뒤 회사가 새 보안 장비를 검토해요", "설명서에 세 기능이 한 줄에 나란히 적혀 있어요",
            "지우는 잠깐 헷갈려요", "이 Page에서 한 상자를 기능별로 나눠 봐요"]
    return scene(a, "새 보안 장비는 어느 구조일까", "서 이사가 설명서를 건넸어요", caps, "".join(b), bg="office")


NAMES = {"p1": "first-week", "p2": "block-request", "p3": "just-watch", "p4": "drawing-worry", "p5": "plugin-question", "p6": "new-box"}

if __name__ == "__main__":
    for k, fn in zip(NAMES, (p1, p2, p3, p4, p5, p6)):
        write(OUT, f"u11-l01-p0{k[1]}-story-{NAMES[k]}", fn())
        print(f"u11-l01-p0{k[1]}-story-{NAMES[k]}.svg")
