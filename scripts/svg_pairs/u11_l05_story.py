#!/usr/bin/env python3
"""Unit 11 Lesson 5 situation SVGs (one 4-step story figure per Page, see hangyeol_cast.py).
Run from the repo root: python3 scripts/svg_pairs/u11_l05_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "units/07-network-devices/lessons/restructured/05-회사-프록시의-검사와-기록/assets/animations"


def ppl(a, x, y, who, spans, facing="right", scale=1.0):
    """spans = [(mood, first_step, last_step), ...]"""
    return "".join(a.vis(person(x, y, who, m, scale, facing), s, e) for m, s, e in spans)


def pm(a, x, y, t, w=88, h=160):
    """Orange mark around a person drawn with head centre (x, y)."""
    return mark(a, x - w / 2, y - 32, w, h, t)


def bub(a, x, y, s, tail, who, t0, t1, **kw):
    return a.vis(bubble(x, y, s, tail_to=tail, color=CAST[who], **kw), t0, t1)


def bub_box(x, y, s, fs=18):
    ls = wrap(s, fs)
    w = max(tw(ln, fs) for ln in ls) + 36
    return x - w / 2 - 5, y - (26 * len(ls) + 22) / 2 - 5, w + 10, 26 * len(ls) + 32


def p1():
    a = new()
    sj = "앞으로 이런 일을\n막을 수 있어요?"
    body = [
        a.vis(pill(480, 395, "월요일 회의", MUTED, 17), 1, 3),
        ppl(a, 700, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
        ppl(a, 850, 235, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], "left"),
        pm(a, 700, 235, 1),
        # 들은 이야기: 박 팀장이 도면 PDF를 외부 AI에 올림
        a.vis(box(30, 128, 470, 240, MUTED, BG, 12, True) + pill(265, 152, "들은 이야기", MUTED, 17)
              + person(95, 218, "박 팀장", "normal", 0.8)
              + chat_window(270, 265, ["견적서 초안 써 줘"]) + text(270, 362, "외부 AI 서비스", 17, TXT, 700)
              + doc(455, 262, "고객 도면", RED), 2, 4),
        mark(a, 30, 128, 470, 240, 2),
        bub(a, 800, 165, sj, (850, 208), "서 이사", 3, 3), mark(a, *bub_box(800, 165, sj), 3),
        a.vis(thought(598, 165, "프록시를 통해서만\n나가게 바꾸자", tail_to=(692, 211), color=BLUE), 3, 4),
        question(a, "프록시를 건너뛰는 길은 어떻게 막을까?"),
    ]
    caps = ["월요일 회의에서 서 이사와 지우가 이야기해요", "박 팀장이 고객 도면 PDF를 외부 AI에 올렸대요",
            "서 이사는 막을 방법을, 지우는 길 하나를 떠올려요", "이 Page에서 건너뛰는 길을 막는 법을 살펴봐요"]
    return scene(a, "박 팀장의 도면이 AI로 나갔대요", "서 이사의 얼굴이 굳은 월요일 회의", caps, "".join(body), "office")


def p2():
    a = new()
    sy = "박 팀장이 어제 뭘 올렸는지\n찾아 줄 수 있어요?"
    r1 = "14:05:12  192.168.10.42  ai-chat.example:443"
    r2 = "14:20:40  192.168.10.41  docs.example:443"
    assert tw(r1, 16) < 430, tw(r1, 16)
    px, py, pw, ph = 250, 214, 460, 146
    log = (box(px, py, pw, ph, BLUE, PANEL, 10, sw=3) + text(px + 24, py + 30, "프록시 기록", 17, BLUE, 700, "start")
           + text(px + 24, py + 80, r1, 16, TXT, 700, "start") + text(px + 24, py + 120, r2, 16, MUTED, 700, "start"))
    body = [
        a.vis(pill(480, 395, "프록시 경로가 자리 잡은 다음 날", MUTED, 17), 1, 3),
        ppl(a, 120, 235, "서 이사", [("normal", 1, 2), ("worried", 3, 4)]),
        ppl(a, 840, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)], "left"),
        pm(a, 120, 235, 1),
        a.vis(log, 2, 4), mark(a, px, py, pw, ph, 2),
        bub(a, 262, 165, sy, (130, 208), "서 이사", 3, 3), mark(a, *bub_box(262, 165, sy), 3),
        a.vis(thought(712, 165, "'무엇을 올렸는지'가\n이 기록에 있을까?", tail_to=(830, 211), color=BLUE), 3, 4),
        question(a, "프록시 기록에는 무엇이 남을까?"),
    ]
    caps = ["프록시를 쓰기 시작한 다음 날, 서 이사가 지우를 불러요", "지우가 연 기록에 박 팀장 PC의 접속이 남아 있어요",
            "서 이사는 올린 내용을, 지우는 기록에 있을지 궁금해요", "이 Page에서 기록에 남는 것을 알아봐요"]
    return scene(a, "박 팀장이 뭘 올렸는지 찾아 줘요", "서 이사의 부탁을 받은 지우", caps, "".join(body), "office")


def p3():
    a = new()
    sy = "고객 연락처 파일이 올라가는\n순간 막을 수는 없어요?"
    body = [
        ppl(a, 110, 235, "서 이사", [("normal", 1, 2), ("worried", 3, 4)]),
        ppl(a, 850, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)], "left"),
        pm(a, 110, 235, 1),
        a.vis(pc(300, 285, "박 팀장 PC") + line(350, 275, 590, 275, BLUE, 6)
              + f'<rect x="446" y="248" width="56" height="54" rx="8" fill="{BG}"/>' + lock(474, 258, BLUE)
              + text(474, 325, "암호", 17, BLUE, 700)
              + cell(590, 240, 150, 70, "AI 서비스", BLUE, 17), 2, 4),
        mark(a, 250, 235, 500, 105, 2),
        bub(a, 262, 165, sy, (118, 208), "서 이사", 3, 3), mark(a, *bub_box(262, 165, sy), 3),
        a.vis(thought(700, 165, "이 암호를 열려면\n무엇이 필요할까?", tail_to=(842, 211), color=BLUE), 3, 4),
        question(a, "암호화된 AI 대화를 열어 보려면?"),
    ]
    caps = ["기록만으로는 부족하다고 서 이사가 말해요", "내용은 박 팀장 PC와 AI 서비스만 푸는 암호 속에 있어요",
            "서 이사는 올리는 순간 막기를, 지우는 암호 열기를 떠올려요", "이 Page에서 암호를 열 조건을 알아봐요"]
    return scene(a, "올라가는 순간 막을 수 없어요?", "기록 다음에 서 이사가 던진 질문", caps, "".join(body), "office")


def p4():
    a = new()
    se = "이거 괜찮은\n파일이에요?"
    sy = "묻지 않아도 들어오는 파일을\n회사가 먼저 걸러 줄 수 없어요?"
    body = [
        ppl(a, 100, 235, "직원", [("normal", 1, 4)]),
        ppl(a, 480, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)]),
        ppl(a, 850, 235, "서 이사", [("normal", 1, 2), ("worried", 3, 4)], "left"),
        pm(a, 100, 235, 1),
        a.vis(pill(275, 225, "처음 보는 외부 사이트", MUTED, 17) + doc(275, 300, "AI 자동 배치", RED), 2, 4),
        mark(a, 150, 200, 250, 195, 2),
        bub(a, 185, 165, se, (108, 208), "직원", 3, 3), mark(a, *bub_box(185, 165, se), 3),
        bub(a, 700, 165, sy, (850, 208), "서 이사", 3, 3, fs=16),
        question(a, "받은 파일에 악성코드가 있다면?"),
    ]
    caps = ["디자인팀 직원이 지우를 찾아와요", "처음 보는 사이트에서 'AI 자동 배치' 설치 파일을 받았어요",
            "직원은 괜찮은지 묻고, 서 이사는 먼저 걸러 주길 바라요", "이 Page에서 파일을 걸러 주는 법을 알아봐요"]
    return scene(a, "받은 파일, 괜찮은 걸까요?", "설치하기 전에 지우에게 물어 온 직원", caps, "".join(body), "office")


def p5():
    a = new()
    box_ = cell(320, 232, 240, 106, "방화벽 · IPS · 프록시", BLUE, 17)
    body = [
        ppl(a, 90, 235, "서 이사", [("normal", 1, 4)]),
        ppl(a, 890, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)], "left"),
        a.vis(doc(200, 290, "장비 견적", BLUE), 1, 1),
        box_ + line(400, 232, 400, 338, BLUE, 2) + line(480, 232, 480, 338, BLUE, 2),
        pm(a, 90, 235, 1),
        a.vis(monitor(700, 285, "loading", "웹·AI만 느려요"), 2, 4),
        a.vis(pill(700, 395, "메일·화상 회의는 멀쩡", GREEN, 17), 2, 3), mark(a, 595, 226, 210, 216, 2),
        a.vis(thought(700, 165, "장비는 한 대인데\n왜 어떤 것만 느릴까?", tail_to=(880, 211), color=BLUE), 3, 4),
        mark(a, 590, 124, 234, 82, 3),
        question(a, "한 상자에 IPS와 프록시가 같이 있다면?"),
    ]
    caps = ["서 이사가 방화벽·IPS·프록시가 든 장비 견적을 받아 와요", "시험에서 웹과 AI만 느리고 메일·화상 회의는 멀쩡해요",
            "장비는 한 대인데 왜 어떤 것만 느린지 지우가 궁금해해요", "이 Page에서 한 상자 안을 들여다봐요"]
    return scene(a, "장비는 한 대인데 웹만 느려요", "통합 보안 장비 시험 중에 생긴 일", caps, "".join(body), "server_room")


def p6():
    a = new()
    sj = "AI 대화 전문을\n1년 동안 보관해 두죠"
    body = [
        a.vis(pill(480, 395, "회의", MUTED, 17), 1, 3),
        ppl(a, 110, 235, "직원", [("normal", 1, 4)]),
        ppl(a, 480, 235, "서 이사", [("normal", 1, 1), ("happy", 2, 4)]),
        ppl(a, 850, 235, "지우", [("normal", 1, 2), ("thinking", 3, 4)], "left"),
        pm(a, 480, 235, 1),
        bub(a, 270, 165, sj, (112, 208), "직원", 2, 2), mark(a, *bub_box(270, 165, sj), 2),
        a.vis(thought(700, 165, "업무 질문, 점심 메뉴 추천,\n건강 상담, 개인 메일 초안", tail_to=(842, 211), color=BLUE), 3, 4),
        mark(a, *bub_box(700, 165, "업무 질문, 점심 메뉴 추천,\n건강 상담, 개인 메일 초안", 18), 3),
        question(a, "직원의 AI 대화, 어디까지 봐도 될까?"),
    ]
    caps = ["회의에서 서 이사와 지우가 의견을 들어요", "한 사람이 AI 대화 전문을 1년 보관하자고 해요",
            "서 이사는 솔깃하고, 지우는 시험 화면의 내용이 마음에 걸려요", "이 Page에서 어디까지 봐도 되는지 따져 봐요"]
    return scene(a, "대화 전문을 1년 보관하자고요?", "시험 적용한 날 회의에서 나온 의견", caps, "".join(body), "office")


PAGES = {
    "u11-l05-p1-story-block-bypass": p1,
    "u11-l05-p2-story-log-question": p2,
    "u11-l05-p3-story-open-chat": p3,
    "u11-l05-p4-story-plugin-download": p4,
    "u11-l05-p5-story-one-box": p5,
    "u11-l05-p6-story-monitoring-limit": p6,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        write(OUT, name, fn())
        print(OUT / f"{name}.svg")
