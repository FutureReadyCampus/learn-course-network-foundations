#!/usr/bin/env python3
"""Unit 11 Lesson 2 situation SVGs (4-step admin-tutorial story, one per Page). Writes straight into the Lesson's assets/animations.
Run from repo root: python3 scripts/svg_pairs/u11_l02_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})  # admin-tutorial roles (this process only)

OUT = Path("units/07-network-devices/lessons/restructured/02-인라인-구조와-트래픽-처리/assets/animations")
HEAD_Y = 235  # head centre of the standing cast


def bm(a, x, y, s, t, fs=18):
    """Orange outline around bubble(x, y, s) in step t."""
    ls = wrap(s, fs)
    w, h = max(tw(ln, fs) for ln in ls) + 36, 26 * len(ls) + 22
    return mark(a, x - w / 2 - 5, y - h / 2 - 5, w + 10, h + 10, t)


def tm(a, x, y, s, t, fs=18):
    """Orange outline around thought(x, y, s) in step t."""
    ls = wrap(s, fs)
    w, h = max(tw(ln, fs) for ln in ls) + 40, 26 * len(ls) + 26
    return mark(a, x - w / 2, y - h / 2, w, h, t)


def mm(a, x, y, t, msg):
    """Orange outline around monitor(x, y, msg)."""
    w = max(190, tw(msg, 16) + 32)
    return mark(a, x - w / 2 - 4, y - 60, w + 8, 120, t)


def p1():
    a = new()
    bs, ts = "집 와이파이에선 잘 됐어요", "바뀐 건 장소뿐"
    body = [a.vis(pill(480, 395, "첫 번째 티켓 · 월요일 아침", MUTED, 17), 1, 3),
            a.vis(person(170, HEAD_Y, "박 팀장"), 1, 1), a.vis(person(170, HEAD_Y, "박 팀장", "worried"), 2, 4),
            a.vis(person(760, HEAD_Y, "지우", facing="left"), 1, 2), a.vis(person(760, HEAD_Y, "지우", "thinking", facing="left"), 3, 4),
            mark(a, 126, 203, 88, 160, 1),
            a.vis(monitor(440, 290, "error", "연결할 수 없음"), 2, 4), mm(a, 440, 290, 2, "연결할 수 없음"),
            a.vis(bubble(230, 160, bs, tail_to=(178, 208), color=TERRACOTTA), 3, 3), bm(a, 230, 160, bs, 3),
            a.vis(thought(690, 160, ts, tail_to=(752, 208), color=BLUE), 3, 4),
            question(a, "사이트 요청은 어떤 장치를 거쳐 나갈까?")]
    caps = ["월요일 아침, 박 팀장이 지우 자리로 왔어요", "사무실 유선에 꽂으니 연결할 수 없음만 떠요",
            "집에서는 잘 됐는데, 바뀐 것은 장소뿐이에요", "이 Page에서 요청이 지나는 길을 따라가요"]
    return scene(a, "회사에서만 사이트가 안 열려요", "박 팀장 노트북, 같은 서비스인데 왜 막힐까요?", caps, "".join(body), bg="office")


def p2():
    a = new()
    ts = "왜 이렇게 오래 기다렸을까?"
    body = [a.vis(pill(480, 395, "사무실", MUTED, 17), 1, 3),
            a.vis(person(160, HEAD_Y, "지우"), 1, 2), a.vis(person(160, HEAD_Y, "지우", "thinking"), 3, 4),
            a.vis(person(800, HEAD_Y, "박 팀장", facing="left"), 1, 1), a.vis(person(800, HEAD_Y, "박 팀장", "worried", facing="left"), 2, 4),
            mark(a, 756, 203, 88, 160, 1),
            a.vis(monitor(560, 290, "loading", "빙글빙글 도는 중"), 1, 1),
            a.vis(monitor(560, 290, "error", "연결할 수 없음"), 2, 4), mm(a, 560, 290, 2, "연결할 수 없음"),
            a.vis(thought(250, 160, ts, tail_to=(168, 208), color=BLUE), 3, 4), tm(a, 250, 160, ts, 3),
            question(a, "통과시킬까, 버릴까?")]
    caps = ["박 팀장 화면이 한참 빙글빙글 돌아요", "한참 뒤에야 연결할 수 없음이 떠요",
            "거절당했다면 바로 실패했을 텐데 이상해요", "이 Page에서 장치의 처리 방식을 알아봐요"]
    return scene(a, "오류가 곧바로 뜨지 않아요", "화면은 한참 돌다가 실패했어요", caps, "".join(body), bg="office")


def p4():
    a = new()
    ts = "요청은 나가는데\n답은 들어와요"
    rule = (box(405, 218, 330, 124, BLUE, PANEL, 10, sw=3) + line(405, 280, 735, 280, LINE, 2)
            + text(570, 256, "Inbound · Outbound", 20, TXT, 700) + text(570, 318, "인터페이스 A · B", 20, TXT, 700))
    body = [a.vis(pill(480, 395, "사무실", MUTED, 17), 1, 3),
            a.vis(person(200, HEAD_Y, "지우"), 1, 1), a.vis(person(200, HEAD_Y, "지우", "worried"), 2, 3),
            a.vis(person(200, HEAD_Y, "지우", "thinking"), 4, 4),
            mark(a, 156, 203, 88, 160, 1),
            a.vis(doc(570, 280, "규칙표"), 1, 1),
            a.vis(rule, 2, 4), mark(a, 405, 218, 330, 124, 2),
            a.vis(thought(300, 150, ts, tail_to=(204, 208), color=BLUE), 3, 3), tm(a, 300, 150, ts, 3),
            question(a, "방화벽은 어느 쪽이 안인지 어떻게 알까?")]
    caps = ["지우가 방화벽 규칙표를 열어요", "첫 줄부터 Inbound, Outbound, 인터페이스가 섞여 있어요",
            "나가는 요청과 들어오는 답, 어느 쪽일까요", "이 Page에서 방향을 읽는 법을 알아봐요"]
    return scene(a, "규칙표 첫 줄에서 멈칫했어요", "Inbound일까, Outbound일까?", caps, "".join(body), bg="office")


def p7():
    a = new()
    ts = "돈을 들였는데\n왜 안 빨라지지?"
    body = [a.vis(pill(480, 395, "오후 · 큰 파일 업로드", MUTED, 17), 1, 3),
            a.vis(person(130, HEAD_Y, "직원"), 1, 2), a.vis(person(130, HEAD_Y, "직원", "worried"), 3, 4),
            a.vis(person(830, HEAD_Y, "서 이사", facing="left"), 1, 2), a.vis(person(830, HEAD_Y, "서 이사", "worried", facing="left"), 3, 4),
            mark(a, 86, 203, 88, 160, 1),
            monitor(330, 290, "loading", "업로드 중"),
            a.vis(pill(610, 255, "회선 300Mbps → 1Gbps", BLUE, 20, False, 270), 2, 4), mark(a, 475, 233, 270, 44, 2),
            a.vis(thought(720, 150, ts, tail_to=(826, 208), color=VIOLET), 3, 4), tm(a, 720, 150, ts, 3),
            question(a, "회선을 늘렸는데 왜 그대로 느릴까?")]
    caps = ["오후마다 직원들의 업로드가 느려져요", "서 이사가 회선 계약을 올렸어요",
            "그래도 체감 속도는 그대로예요", "이 Page에서 느린 이유를 따져 봐요"]
    return scene(a, "회선을 올렸는데 그대로예요", "큰 파일 업로드는 여전히 하염없이 느려요", caps, "".join(body), bg="office")


def p8():
    a = new()
    s1, s2, ts = "개인용 파일 공유 사이트는\n아예 전부 막아 주세요", "업무용으로 허락된\n서비스는 열어 둬야죠", "무엇을 기준으로\n막을 수 있나?"
    body = [a.vis(meeting_table(480, 368), 1, 3), a.vis(pill(480, 428, "회의실", MUTED, 17), 1, 3),
            a.vis(person(210, 245, "서 이사"), 1, 1), a.vis(person(210, 245, "서 이사", "worried"), 2, 4),
            a.vis(person(480, 245, "지우"), 1, 3), a.vis(person(480, 245, "지우", "thinking"), 4, 4),
            a.vis(person(750, 245, "박 팀장", facing="left"), 1, 2), a.vis(person(750, 245, "박 팀장", "worried", facing="left"), 3, 4),
            mark(a, 166, 213, 88, 160, 1),
            a.vis(bubble(240, 170, s1, tail_to=(212, 218), color=VIOLET), 2, 2), bm(a, 240, 170, s1, 2),
            a.vis(bubble(720, 170, s2, tail_to=(750, 218), color=TERRACOTTA), 3, 3), bm(a, 720, 170, s2, 3),
            a.vis(thought(480, 160, ts, tail_to=(480, 216), color=BLUE), 4, 4),
            question(a, "주소만 볼까, 내용까지 볼까?")]
    caps = ["차단 규칙을 두고 회의가 열렸어요", "서 이사는 개인용 공유 사이트를 전부 막자고 해요",
            "박 팀장은 허락된 서비스는 열어 두자고 맞서요", "이 Page에서 무엇을 기준으로 막는지 봐요"]
    return scene(a, "외부 사이트를 어디까지 막을까요", "결정은 경영진의 몫, 지우는 기준을 정리해요", caps, "".join(body))


def p11():
    a = new()
    ts = "평일 오후였다면…"
    body = [pill(480, 135, "토요일 오전", MUTED, 17),
            a.vis(person(170, HEAD_Y, "지우"), 1, 2), a.vis(person(170, HEAD_Y, "지우", "thinking"), 3, 4),
            a.vis(person(800, HEAD_Y, "박 팀장", facing="left"), 1, 1), a.vis(person(800, HEAD_Y, "박 팀장", "worried", facing="left"), 2, 4),
            mark(a, 126, 203, 88, 160, 1),
            doc(330, 290, "보안 업데이트"),
            a.vis(monitor(620, 290, "loading", "업로드 중"), 1, 1),
            a.vis(monitor(620, 290, "error", "인터넷 끊김"), 2, 4), mm(a, 620, 290, 2, "인터넷 끊김"),
            a.vis(thought(250, 160, ts, tail_to=(176, 208), color=BLUE), 3, 4), tm(a, 250, 160, ts, 3),
            question(a, "길목 장치가 멈추면 인터넷도 멈출까?")]
    caps = ["토요일 오전, 지우가 방화벽을 재부팅해요", "몇 분 동안 사무실 인터넷이 끊겨요",
            "평일 오후였다면 회사 업무가 멈췄을 거예요", "이 Page에서 장치 하나의 장애를 따져 봐요"]
    return scene(a, "재부팅 몇 분에 인터넷이 끊겼어요", "주말에 출근한 박 팀장의 업로드도 멈췄어요", caps, "".join(body), bg="server_room")


if __name__ == "__main__":
    for name, fn in (("p1-story-office-path", p1), ("p2-story-silent-drop", p2), ("p3-story-rule-direction", p4),
                     ("p4-story-bottleneck", p7), ("p5-story-block-criteria", p8), ("p6-story-reboot-outage", p11)):
        write(OUT, f"u11-l02-{name}", fn())
        print(OUT / f"u11-l02-{name}.svg")
