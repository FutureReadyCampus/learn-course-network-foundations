#!/usr/bin/env python3
"""Unit 11 Lesson 7 situation SVGs (한결디자인 story, one per Page, 4 steps each).
Run from repo root: python3 scripts/svg_pairs/u11_l07_story.py   (writes SVGs into the lesson's assets/animations/)."""
from hangyeol_cast import *  # noqa: F401,F403
import u11_new_common as C

OUT = C.lesson_dir(7) / "assets" / "animations"
HY = 240  # head centre y for standing people


def cast(a, x, who, moods, facing="right", y=HY):
    """person whose mood may change per step; moods = 4 strings (consecutive equal ones are merged)."""
    out, s = "", 1
    for t in range(2, 6):
        if t == 5 or moods[t - 1] != moods[s - 1]:
            out += a.vis(person(x, y, who, moods[s - 1], facing=facing), s, t - 1)
            s = t
    return out


def pmark(a, x, t, y=HY):
    return mark(a, x - 44, y - 32, 88, 160, t)


def bmark(a, x, y, s, t, thought=False):
    lines = wrap(s)
    w = max(tw(ln, 18) for ln in lines) + (40 if thought else 36)
    h = 26 * len(lines) + (26 if thought else 22)
    return mark(a, x - w / 2 - 5, y - h / 2 - 5, w + 10, h + 10, t)


def say(a, x, y, s, tail, who, t0, t1=None, hx=None):
    """bubble + its orange mark during t0 (only)."""
    return a.vis(bubble(x, y, s, tail_to=tail, color=CAST[who]), t0, t1 or t0) + bmark(a, x, y, s, t0)


def think(a, x, y, s, tail, t0, t1=None):
    return a.vis(thought(x, y, s, tail_to=tail, color=BLUE), t0, t1 or t0) + bmark(a, x, y, s, t0, True)


def srv(x, y, label, sub=None, c=GREEN, dash=False):
    d = ' stroke-dasharray="7 5"' if dash else ""
    s = (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"{d}/>'
         + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
         + text(x, y + 66, label, 17, TXT, 700))
    return s + (text(x, y + 86, sub, 16, MUTED) if sub else "")


def srv_mark(a, x, y, t, sub=True):
    return mark(a, x - 80, y - 44, 160, 142 if sub else 124, t)


def finish(a, name, title, sub, caps, body, bg):
    svg = scene(a, title, sub, caps, "".join(body), bg=bg)
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT, name, svg)


# ------------------------------------------------------------------ Page 1
def p1():
    a = new()
    t1 = "아직 띄우기 전이니\n설계도부터 그리자"
    body = [cast(a, 330, "지우", ["normal", "normal", "thinking", "thinking"]),
            cast(a, 780, "서 이사", ["normal", "normal", "worried", "worried"], facing="left"),
            a.vis(pill(555, 395, "한결디자인 사무실", MUTED, 17), 1, 3), pmark(a, 330, 1),
            a.vis(srv(555, 262, "AI 서버", "192.168.10.50:8080", GREEN, True), 2, 4), srv_mark(a, 555, 262, 2),
            say(a, 745, 168, "시연 때 밖에서도 보여 주려면\n열어야 하잖아요?", (780, 212), "서 이사", 3),
            think(a, 330, 168, t1, (330, 212), 3),
            question(a, "서버 앞에 무엇을 어떤 순서로 세울까?")]
    caps = ["지우와 서 이사가 사내 AI 서버 계획을 봐요", "GPU PC에 AI 서버를 띄우자는 의견이 나왔어요",
            "서 이사는 공격이 걱정, 지우는 설계도부터 그려요", "이 Page에서 서버 앞 경비를 알아봐요"]
    finish(a, "u11-l07-p01-story-open-server", "밖에 열면 공격받지 않아요?", "사내 AI 서버를 고객사 시연에 보여 줘야 해요", caps, body, "office")


# ------------------------------------------------------------------ Page 2
def p2():
    a = new()
    body = [cast(a, 150, "지우", ["thinking", "thinking", "worried", "worried"]), pmark(a, 150, 1),
            srv(560, 290, "AI 서버", "192.168.10.50:8080", GREEN, True),
            a.vis(C.cloud(860, 290, "해외 대역") + "".join(line(780, 250 + 30 * i, 625, 250 + 30 * i, RED, 3, "8 6") + packet(700 + 30 * (i % 2), 250 + 30 * i, RED)
                                                         for i in range(4)), 2, 4),
            a.vis(pill(715, 200, "443번 포트를 수없이 두드려요", ORANGE, 17), 2, 2), mark(a, 780, 245, 140, 90, 2),
            think(a, 300, 168, "전부 들여보내면\n앞단도 AI 서버도 지쳐", (150, 212), 3),
            question(a, "문 앞에서 먼저 걸러 낼 수는 없을까?")]
    caps = ["지우는 서버를 열었을 때 생길 일을 그려 봐요", "처음 보는 해외 대역에서 연결 시도가 쏟아져요",
            "전부 안쪽까지 들이면 금방 지치겠어요", "이 Page에서 문 앞 첫 관문을 알아봐요"]
    finish(a, "u11-l07-p02-story-gate-flood", "문을 열면 연결이 쏟아져요", "인터넷에 공개된 서버를 두드리는 요청들", caps, body, "server_room")


# ------------------------------------------------------------------ Page 3
def p3():
    a = new()
    body = [cast(a, 170, "지우", ["normal", "thinking", "thinking", "thinking"]), pmark(a, 170, 1),
            srv(520, 262, "AI 서버", "192.168.10.50:8080", GREEN) + lock(520, 264, GREEN),
            a.vis(C.doc(620, 240, BLUE), 2, 4) + a.vis(pill(520, 395, "서버가 TLS를 직접 풀어요", BLUE, 17), 2, 3), mark(a, 598, 218, 44, 44, 2),
            a.vis(srv(790, 262, "AI 서버 (늘림)", None, GREEN) + lock(790, 264, GREEN) + C.doc(885, 240, BLUE), 3, 4), mark(a, 728, 200, 190, 160, 3),
            think(a, 300, 168, "서버를 늘릴 때마다\n인증서를 설치·갱신?", (170, 212), 3, 4),
            question(a, "암호는 어디서 풀어야 할까?")]
    caps = ["요청 내용을 검사하려면 TLS를 풀어야 해요", "가장 단순한 답은 AI 서버가 직접 푸는 거예요",
            "서버가 늘면 서버마다 인증서가 따라가요", "이 Page에서 더 나은 자리를 찾아봐요"]
    finish(a, "u11-l07-p03-story-who-decrypts", "암호는 AI 서버가 풀까요?", "TLS를 푸는 일을 누가 맡을지 고민해요", caps, body, "office")


# ------------------------------------------------------------------ Page 4
def p4():
    a = new()
    t = "주소도 포트도 TLS도\n평범해요"
    body = [cast(a, 140, "지우", ["thinking", "thinking", "worried", "worried"]), pmark(a, 140, 1),
            monitor(400, 290, "ok", "/history?customer=1042"),
            a.vis(pill(400, 395, "상담 이력 조회 주소", MUTED, 17), 1, 1),
            a.vis(alert_card(700, 290, "customer=1042' OR '1'='1"), 2, 4), mark(a, 548, 262, 304, 56, 2),
            think(a, 340, 168, t, (140, 212), 3),
            question(a, "이상한 요청을 어떻게 거를까?")]
    caps = ["지우가 상담 이력 조회 주소를 보안 점검해요", "이런 주소에는 공격 요청이 흔히 들어와요",
            "출발지도 포트도 TLS도 평범해 검문소는 못 걸러요", "이 Page에서 이 요청을 거르는 법을 알아봐요"]
    finish(a, "u11-l07-p04-story-odd-request", "평범해 보이는 이상한 요청", "남의 상담 이력까지 꺼내려는 요청이 와요", caps, body, "office")


# ------------------------------------------------------------------ Page 5
def p5():
    a = new()
    body = [cast(a, 330, "지우", ["normal", "normal", "worried", "worried"]),
            cast(a, 780, "서 이사", ["normal", "normal", "worried", "worried"], facing="left"),
            doc(555, 285, "설계도"), pmark(a, 780, 1),
            say(a, 745, 168, "시연 요청은 전부\n앞단 하나를 지나요?", (780, 212), "서 이사", 2),
            say(a, 745, 168, "이게 고장 나면요?", (780, 212), "서 이사", 3),
            think(a, 330, 168, "AI 서버가 멀쩡해도\n앞단이 멈추면…", (330, 212), 3),
            question(a, "앞단 한 대로 무엇을 얻고 잃을까?")]
    caps = ["설계도를 들여다보던 서 이사가 물어요", "시연 요청이 앞단 하나를 지나는지 물어요",
            "지우는 바로 답하지 못해요", "이 Page에서 앞단 한 대의 득실을 따져 봐요"]
    finish(a, "u11-l07-p05-story-front-fails", "이게 고장 나면요?", "설계도를 본 서 이사의 질문", caps, body, "office")


# ------------------------------------------------------------------ Page 6
def p6():
    a = new()
    body = [cast(a, 150, "박 팀장", ["normal", "worried", "worried", "worried"]),
            cast(a, 840, "지우", ["normal", "normal", "thinking", "thinking"], facing="left"),
            doc(700, 280, "설계도(종이 위)"), pmark(a, 840, 1),
            a.vis(monitor(330, 290, "error", "서버에 닿지 않아요"), 2, 4), mark(a, 218, 228, 224, 124, 2),
            think(a, 640, 168, "가장 빠른 길을 찾되,\n열면 뭐가 노출될까?", (840, 212), 3),
            a.vis(C.node(545, 290, "198.51.100.25", None, 170, 56, ORANGE, 17) + ask(545, 345), 4, 4),
            a.vis(text(480, 402, "다음 Unit 12에서 알아볼 것", 16, MUTED) + pill(480, 438, "밖에서 온 연결은 서버까지 어떻게 닿을까?", ORANGE, 22, True), 4, 4)]
    caps = ["박 팀장이 고객사에서 시연하기로 했어요", "그런데 고객사에서는 서버에 닿지 않아요",
            "지우는 가장 빠른 길과 노출을 함께 따져요", "공인 주소로 온 연결은 Unit 12에서 따져요"]
    finish(a, "u11-l07-p06-story-handoff", "고객사에서는 서버에 안 닿아요", "설계도는 완성, 앞단은 아직 종이 위", caps, body, "client")


if __name__ == "__main__":
    for f in (p1, p2, p3, p4, p5, p6):
        f()
    print("ok", OUT)
