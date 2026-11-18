#!/usr/bin/env python3
"""Unit 11 Lesson 3 (경로 밖 관찰과 DPI): one 4-step admin-tutorial "situation" SVG per Page (7), plus lesson.md wiring.
Run from repo root: python3 scripts/svg_pairs/u11_l03_story.py   (--svg-only skips the lesson.md edit)."""
import json
import re
import sys
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES
from u11_new_common import cloud  # only cloud: that module's doc() differs from hangyeol_cast.doc

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})  # admin-tutorial roles (shared dict, this process only)

LESSON = Path(__file__).resolve().parents[2] / "units/07-network-devices/lessons/restructured/03-경로-밖-관찰과-dpi"
HY = 235  # head centre y of every person


def pm(a, x, t, role=False):
    """Orange outline around one person (head+torso+name tag, +role line)."""
    return mark(a, x - 42, 203, 84, 182 if role else 160, t)


def bm(a, x, y, s, t, kind="bubble"):
    """Orange outline around a bubble/thought centred at (x, y)."""
    lines = wrap(s)
    if kind == "bubble":
        w, h = max(tw(ln, 18) for ln in lines) + 36, 26 * len(lines) + 22
    else:
        w, h = max(tw(ln, 18) for ln in lines) + 40, 26 * len(lines) + 26
    return mark(a, x - w / 2, y - h / 2, w, h, t)


def tag(a, x, y, s, s0, s1, c=MUTED):
    return a.vis(pill(x, y, s, c, 17), s0, s1)


# ---------------------------------------------------------------- Page 1
def p1():
    a = new()
    q1, q2, q3 = "누가 어떤 사이트를 많이\n쓰는지 알고 싶어요", "업무 속도는 1초도 느려지면 안 돼요", "통신은 그대로 두고\n옆에서 지켜볼 방법을 찾자"
    body = [tag(a, 480, 395, "본사 사무실", 1, 1),
            person(130, HY, "서 이사", "normal", role=True), person(330, HY, "지우", "normal", role=True),
            a.vis(person(850, HY, "직원", "normal", facing="left"), 1, 1),
            pm(a, 130, 1, True),
            a.vis(person(850, HY, "직원", "normal", facing="left"), 2, 4),
            a.vis(monitor(620, 290, "loading", "클라우드 저장소"), 2, 4), mark(a, 515, 225, 210, 142, 2),
            a.vis(text(620, 404, "클라우드 저장소를 쓰는 직원이 늘었어요", 17, TXT, 700), 2, 2),
            a.vis(bubble(215, 150, q1, tail_to=(135, 208), color=VIOLET), 2, 2),
            a.vis(bubble(215, 150, q2, tail_to=(135, 208), color=VIOLET), 3, 3), bm(a, 215, 150, q2, 3),
            a.vis(thought(560, 150, q3, tail_to=(335, 208), color=BLUE), 3, 3),
            question(a, "통신은 그대로 두고 옆에서 지켜볼 수 있을까?")]
    # persons whose mood changes: redraw 서 이사 worried / 지우 thinking from step 2 / 3
    body.insert(3, a.vis(person(130, HY, "서 이사", "worried"), 2, 4))
    body.insert(4, a.vis(person(330, HY, "지우", "thinking"), 3, 4))
    caps = ["본사 사무실의 서 이사와 지우예요", "클라우드 저장소를 쓰는 직원이 늘었어요",
            "속도는 그대로, 지우는 지켜볼 방법을 찾아요", "이 Page에서 그 방법을 알아봐요"]
    return scene(a, "서 이사는 누가 어떤 사이트를 쓰는지 알고 싶어요", "업무는 멈추지 않고 지켜볼 수 있을까요?", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 2
def p2():
    a = new()
    t3 = "외부 사이트로 나가는\n통신이 알고 싶어"
    body = [person(110, HY, "지우", "normal", role=True),
            a.vis(person(110, HY, "지우", "thinking"), 2, 4), pm(a, 110, 1, True),
            switch(330, 300, "코어 스위치"), router(560, 300, "게이트웨이"), cloud(820, 300, "외부 사이트"),
            line(382, 300, 532, 300, LINE, 4, "10 8"), line(588, 300, 750, 300, LINE, 4, "10 8"),
            a.vis(eye(320, 230) + text(356, 237, "센서", 17, TXT, 700, "start") + ask(262, 230), 2, 2), mark(a, 238, 208, 170, 44, 2),
            a.vis(thought(330, 150, t3, tail_to=(118, 208), color=BLUE), 3, 3),
            a.vis(eye(320, 230) + text(356, 237, "센서", 17, TXT, 700, "start"), 3, 4), mark(a, 372, 282, 156, 36, 3),
            question(a, "복사는 누가, 어떻게 해 줄까?")]
    caps = ["지우는 코어 스위치 옆에 센서를 들였어요", "이제 무엇을 복사해 줄지 정해야 해요",
            "알고 싶은 건 외부 사이트로 나가는 통신이에요", "이 Page에서 복사 방법을 알아봐요"]
    return scene(a, "센서는 들였는데 무엇을 복사하지?", "인터넷 통신은 스위치와 게이트웨이 사이를 지나요", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 3
def p3():
    a = new()
    q, t = "센서가 봤다면서요.\n그런데 왜 못 막았어요?", "벌써 회사 계정을\n입력했어"
    al = "경보: 피싱 사이트 접속"
    aw = tw(al, 17) + 76
    body = [tag(a, 480, 395, "센서를 켠 지 사흘째", 1, 1),
            person(110, HY, "박 팀장", "normal"), person(540, HY, "지우", "normal"), person(840, HY, "서 이사", "normal", facing="left"),
            a.vis(person(110, HY, "박 팀장", "worried"), 2, 4), a.vis(person(540, HY, "지우", "worried"), 3, 4),
            a.vis(person(840, HY, "서 이사", "worried", facing="left"), 3, 4),
            mark(a, 68, 203, 84, 160, 1),
            a.vis(monitor(290, 300, "error", "로그인 화면"), 2, 4), a.vis(alert_card(540, 160, al), 2, 2), mark(a, 540 - aw / 2, 134, aw, 52, 2),
            a.vis(thought(380, 150, t, tail_to=(530, 208), color=BLUE), 3, 3),
            a.vis(bubble(700, 150, q, tail_to=(838, 208), color=VIOLET), 3, 3), bm(a, 700, 150, q, 3),
            question(a, "봤는데 왜 막지 못했을까?")]
    caps = ["센서를 켠 지 사흘째, 사무실이에요", "박 팀장 PC가 피싱 사이트에 접속했다는 경보예요",
            "계정은 이미 입력했고, 서 이사가 물어요", "이 Page에서 그 이유를 알아봐요"]
    return scene(a, "경보가 떴는데 막지 못했어요", "박 팀장은 이미 로그인 화면에 계정을 입력했어요", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 4
def p4():
    a = new()
    b2, b3, t3 = "저장소에 올린 파일도\n센서로 알 수 있나요?", "거래처 견적 자료를\n올렸는지 알고 싶어서요", "센서가 볼 수 있는 부분과\n없는 부분을 나눠야 해"
    body = [person(120, HY, "지우", "normal", role=True), person(850, HY, "서 이사", "normal", facing="left", role=True),
            a.vis(person(850, HY, "서 이사", "thinking", facing="left"), 2, 4), a.vis(person(120, HY, "지우", "thinking"), 3, 4),
            doc(330, 300, "센서 보고서"), mark(a, 278, 262, 104, 108, 1),
            a.vis(monitor(590, 290, "loading", "견적 자료 올리기"), 2, 4), mark(a, 485, 225, 210, 142, 2),
            a.vis(bubble(700, 150, b2, tail_to=(846, 208), color=VIOLET), 2, 2),
            a.vis(bubble(700, 150, b3, tail_to=(846, 208), color=VIOLET), 3, 3), bm(a, 700, 150, b3, 3),
            a.vis(thought(290, 150, t3, tail_to=(124, 208), color=BLUE), 3, 3),
            question(a, "센서는 패킷에서 무엇까지 볼 수 있을까?")]
    # step 1 highlights the report only (above); step 2 highlights the chat window
    caps = ["서 이사가 센서 보고서를 받아 봐요", "직원이 저장소에 무엇을 올렸는지도 궁금해해요",
            "거래처 견적 자료를 올렸는지 알고 싶어 해요", "이 Page에서 센서가 볼 수 있는 부분을 알아봐요"]
    return scene(a, "올린 파일 내용까지 볼 수 있나요?", "센서 보고서를 받은 서 이사의 또 다른 부탁", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 5
def p5():
    a = new()
    b2, b3 = "직원 통신을 통째로 저장해\n두면 나중에 찾아볼 수 있죠?", "병원 예약, 은행 알림 같은\n사적인 통신도 지나가요"
    body = [meeting_table(480, 320), tag(a, 480, 404, "회의", 1, 1),
            person(250, HY, "직원", "normal"), person(480, HY, "지우", "normal"), person(700, HY, "박 팀장", "normal", facing="left"),
            a.vis(person(480, HY, "지우", "thinking"), 3, 4), a.vis(person(700, HY, "박 팀장", "worried", facing="left"), 3, 4),
            mark(a, 208, 203, 84, 160, 1),
            a.vis(bubble(300, 150, b2, tail_to=(255, 208), color=GREY), 2, 2), bm(a, 300, 150, b2, 2),
            a.vis(bubble(700, 150, b3, tail_to=(700, 208), color=TERRACOTTA), 3, 3), bm(a, 700, 150, b3, 3),
            question(a, "다 볼 수 있다면 다 봐도 될까?")]
    caps = ["회의에서 센서 보고서가 쓸모 있다는 이야기가 돌아요", "한 사람이 통신을 통째로 저장하자고 해요",
            "박 팀장은 고개를 저어요, 사적인 통신도 지나가거든요", "이 Page에서 어디까지 볼지 따져 봐요"]
    return scene(a, "통신을 통째로 저장하면 될까요?", "회의에서 나온 의견에 박 팀장이 고개를 저었어요", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 6
def _panel():
    x0, y0, w, h = 400, 235, 380, 135
    o = box(x0, y0, w, h, BLUE, PANEL, 10, sw=3)
    o += text(x0 + 20, y0 + 28, "시작만 있고 끝이 없어요", 17, TXT, 700, "start")
    o += f'<rect x="{x0 + 20}" y="{y0 + 40}" width="60" height="14" rx="4" fill="{BLUE}"/>' + line(x0 + 84, y0 + 47, x0 + w - 20, y0 + 47, MUTED, 3, "4 8")
    o += text(x0 + 20, y0 + 88, "중간이 군데군데 비어요", 17, TXT, 700, "start")
    for sx, ex in ((20, 100), (122, 182), (214, 244), (280, 360)):
        o += f'<rect x="{x0 + sx}" y="{y0 + 100}" width="{ex - sx}" height="14" rx="4" fill="{BLUE}"/>'
    return o


def p6():
    a = new()
    t3 = "미러링은 분명히 켰는데\n무엇이 빠진 걸까?"
    body = [person(110, HY, "박 팀장", "normal"), person(850, HY, "지우", "normal", facing="left"),
            a.vis(person(850, HY, "지우", "worried", facing="left"), 3, 4),
            clock(480, 165, "금요일 오후"), doc(270, 300, "마감 자료"),
            mark(a, 66, 203, 84, 160, 1), a.vis(line(150, 290, 225, 290, MUTED, 4, "8 6"), 1, 1),
            a.vis(person(850, HY, "지우", "surprised", facing="left"), 2, 2), a.vis(_panel(), 2, 4), mark(a, 400, 235, 380, 135, 2),
            a.vis(thought(660, 150, t3, tail_to=(846, 208), color=BLUE), 3, 3),
            question(a, "기록이 비는 곳은 어디일까?")]
    caps = ["금요일 오후, 영업팀이 마감 자료를 한꺼번에 올려요", "지우가 센서 기록에서 이상한 점을 찾았어요",
            "미러링은 켜져 있는데 무엇이 빠졌을까요", "이 Page에서 빠진 곳을 찾아봐요"]
    return scene(a, "미러링을 켰는데 기록이 비어요", "금요일 오후 센서 기록에서 이상한 점을 봤어요", caps, "".join(body), bg="office")


# ---------------------------------------------------------------- Page 7
def p7():
    a = new()
    t3 = "세 요청, 경로 안과 경로 밖\n어디서 처리하지?"
    body = [tag(a, 480, 395, "센서를 한 달 운영한 뒤", 1, 1),
            person(130, HY, "지우", "normal", role=True), person(830, HY, "서 이사", "normal", facing="left", role=True),
            a.vis(person(830, HY, "서 이사", "normal", facing="left"), 2, 4), a.vis(person(130, HY, "지우", "thinking"), 3, 4),
            pm(a, 830, 1, True),
            a.vis(doc(330, 290, "즉시 막기", RED) + doc(480, 290, "사이트 사용 통계") + doc(630, 290, "사고 증거", GREEN), 2, 4), mark(a, 270, 240, 420, 130, 2),
            a.vis(thought(330, 150, t3, tail_to=(138, 208), color=BLUE), 3, 3), bm(a, 330, 150, t3, 3, "thought"),
            question(a, "요청마다 경로 안일까, 경로 밖일까?")]
    caps = ["센서를 한 달 운영한 뒤, 서 이사가 찾아왔어요", "서 이사가 요청 세 가지를 들고 왔어요",
            "지우는 요청마다 처리할 자리를 정해야 해요", "이 Page에서 요청마다 자리를 골라 봐요"]
    return scene(a, "서 이사의 요청 세 가지", "막기, 통계, 사고 증거를 어디서 처리할까요?", caps, "".join(body), bg="office")


SCENES = [
    ("advanced-source-05-page-01", "u11-l03-p01-story-ai-usage", p1, "서 이사가 사이트 사용 현황을 묻는 장면",
     "본사 사무실에서 서 이사가 직원이 어떤 외부 사이트를 많이 쓰는지 알고 싶지만 업무 속도는 늦추면 안 된다고 하고, 지우가 통신은 그대로 두고 옆에서 지켜볼 방법을 찾기로 합니다.",
     "서 이사는 업무는 그대로 두고 누가 어떤 사이트를 많이 쓰는지 알고 싶어 합니다."),
    ("advanced-source-05-page-02", "u11-l03-p02-story-what-to-copy", p2, "무엇을 복사해 달라고 할지 고민하는 장면",
     "센서를 코어 스위치 옆에 들인 지우가 직원 PC에서 외부 사이트로 나가는 통신이 알고 싶다며, 그 통신을 누가 어떻게 복사해 줄지 고민합니다.",
     "센서는 들였는데 무엇을, 누가 복사해 줄지 정해야 합니다."),
    ("advanced-source-05-page-03", "u11-l03-p03-story-phishing-alert", p3, "피싱 접속 경보가 떴는데 못 막은 장면",
     "센서를 켠 지 사흘째 박 팀장 PC가 피싱 사이트에 접속했다는 경보가 뜨고, 이미 계정을 입력한 뒤라는 걸 안 서 이사가 센서가 봤는데 왜 못 막았느냐고 묻습니다.",
     "경보는 떴지만 이미 계정을 입력한 뒤였고, 서 이사가 왜 못 막았느냐고 묻습니다."),
    ("advanced-source-05-page-06", "u11-l03-p04-story-ask-content", p4, "올린 파일 내용까지 볼 수 있느냐는 부탁 장면",
     "센서 보고서를 받은 서 이사가 직원이 클라우드 저장소에 무엇을 올렸는지, 거래처 견적 자료를 올렸는지도 센서로 보여 줄 수 있느냐고 묻고, 지우는 센서가 볼 수 있는 부분과 없는 부분을 나눠야 한다고 생각합니다.",
     "서 이사는 직원이 클라우드 저장소에 무엇을 올렸는지까지 센서로 알고 싶어 합니다."),
    ("advanced-source-05-page-07", "u11-l03-p05-story-save-all", p5, "통신을 통째로 저장하자는 의견 장면",
     "회의에서 직원 통신을 통째로 저장해 두자는 의견이 나오자 박 팀장이 병원 예약이나 은행 알림 같은 사적인 통신도 지나간다며 고개를 젓습니다.",
     "통신을 통째로 저장하자는 의견에 박 팀장이 사적인 통신을 걱정합니다."),
    ("advanced-source-05-page-08", "u11-l03-p06-story-missing-records", p6, "금요일 오후 센서 기록이 빈 장면",
     "금요일 오후 영업팀이 마감 자료를 한꺼번에 올리는 시간에 지우가 센서 기록에서 끝이 없거나 중간이 빈 연결을 발견하고, 미러링은 켜져 있는데 무엇이 빠졌는지 의아해합니다.",
     "미러링은 켜져 있는데 금요일 오후 기록에는 빈 곳이 있습니다."),
    ("advanced-source-05-page-10", "u11-l03-p07-story-three-requests", p7, "서 이사가 요청 세 가지를 들고 온 장면",
     "센서를 한 달 운영한 뒤 서 이사가 즉시 막기, 사이트 사용 통계, 사고 증거 찾기 요청 세 가지를 들고 오고, 지우는 요청마다 경로 안과 경로 밖 중 어디서 처리할지 정해야 합니다.",
     "서 이사의 요청 세 가지를 지우가 어디서 처리할지 정해야 합니다."),
]
AFTER = 0  # last paragraph of the story scene = first paragraph of every Page


def main():
    out = LESSON / "assets/animations"
    for _pid, stem, fn, *_ in SCENES:
        write(out, stem, fn())
        print(out / f"{stem}.svg")
    if "--svg-only" in sys.argv:
        return
    md = LESSON / "lesson.md"
    s = md.read_text(encoding="utf-8")
    q = lambda v: json.dumps(v, ensure_ascii=False)
    for pid, stem, _fn, title, alt, cap in SCENES:
        if f"assets/animations/{stem}.svg" in s:
            continue
        item = (f"  - file: assets/animations/{stem}.svg\n    title: {q(title)}\n    alt: {q(alt)}\n"
                f"    caption: {q(cap)}\n    after_paragraph: {AFTER}\n")
        pat = re.compile(rf"(- page_id: {re.escape(pid)}\n  illustrations:\n)")
        assert pat.search(s), pid
        s = pat.sub(lambda m: m.group(1) + item, s, count=1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    main()
