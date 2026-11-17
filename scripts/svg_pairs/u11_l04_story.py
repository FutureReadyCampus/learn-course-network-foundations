#!/usr/bin/env python3
"""Unit 11 Lesson 4 (조직의 포워드 프록시와 접속 정책): 상황(이야기) SVG, Page마다 하나. 개념 SVG는 건드리지 않는다.
Run from repo root: python3 scripts/svg_pairs/u11_l04_story.py   (SVG만 쓴다; lesson.md front matter는 별도로 연결한다)
Page 번호 P는 lesson.md 본문 순서: 1=요청을 누군가 대신, 2=브라우저 프록시 주소, 3=연결 몇 개, 4=보이는 주소, 5=무료 프록시, 6=한 번 더 돌아가면.
admin-tutorial 이야기: 신입 네트워크 관리자 지우 + 티켓 (직원 약 40명 회사)."""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from hangyeol_cast import ROLES

ROLES.update({"지우": "신입 네트워크 관리자", "박 팀장": "팀장", "서 이사": "경영진"})  # 이 프로세스에서만 역할 줄을 덮어쓴다

OUT = Path(__file__).resolve().parents[2] / "units/07-network-devices/lessons/restructured/04-조직의-포워드-프록시와-접속-정책/assets/animations"


def pm(a, x, y, t):  # 사람 둘레 주황 표시
    return mark(a, x - 44, y - 32, 88, 160, t)


def bm(a, x, y, s, t, fs=18):  # 말풍선 둘레 주황 표시 (bubble과 같은 크기 계산)
    ls = wrap(s, fs)
    w, h = max(tw(ln, fs) for ln in ls) + 36, 26 * len(ls) + 22
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def srv(x, y, title, sub=None, c=LINE):
    """서버 상자 (160x100) 중심 (x, y), 아래에 17px 이름과 16px 보조 글."""
    out = box(x - 80, y - 50, 160, 100, c, PANEL, 10, sw=3)
    out += "".join(box(x - 62, y - 36 + i * 28, 124, 20, LINE, BG, 4, sw=2) + f'<circle cx="{x + 48}" cy="{y - 26 + i * 28}" r="4" fill="{c}"/>' for i in range(3))
    out += text(x, y + 76, title, 17, TXT, 700)
    return out + (text(x, y + 98, sub, 16, MUTED) if sub else "")


def panel(x, y, title, field, w=230, c=BLUE):
    """브라우저 설정 창 중심 (x, y), 높이 110: 제목줄 + 입력칸 한 줄."""
    l, t = x - w / 2, y - 55
    return (box(l, t, w, 110, c, PANEL, 10, sw=3) + f'<rect x="{l}" y="{t}" width="{w}" height="30" rx="10" fill="{c}" fill-opacity="0.35"/>'
            + text(l + 14, t + 21, title, 17, TXT, 700, "start")
            + box(l + 14, t + 46, w - 28, 44, MUTED, BG, 6, sw=2) + text(x, t + 74, field, 17, TXT, 700))


def p1():
    a = new()
    q = "누가 어떤 파일을 어디에\n올리려 했는지는 모르는 거죠?"
    t = "프록시 칸에 처음 보는\n서버 주소가 있어"
    body = [a.vis(person(110, 215, "서 이사", "normal"), 1, 2), a.vis(person(110, 215, "서 이사", "worried"), 3, 4),
            a.vis(person(440, 215, "지우", "normal", facing="left"), 1, 2), a.vis(person(440, 215, "지우", "thinking", facing="left"), 3, 4),
            doc(275, 260, "센서 보고서"),
            a.vis(monitor(815, 255, "ok") + pill(815, 360, "박 팀장 PC", MUTED, 17), 1, 1),
            a.vis(pill(815, 360, "박 팀장 PC", MUTED, 17) + panel(815, 255, "프록시", "처음 보는 서버 주소", 250, TERRACOTTA), 2, 4), mark(a, 690, 200, 250, 110, 2),
            a.vis(bubble(235, 142, q, tail_to=(118, 188), color=VIOLET), 3, 3), bm(a, 235, 142, q, 3),
            a.vis(thought(580, 160, t, tail_to=(430, 190), color=BLUE), 3, 4),
            question(a, "요청을 누군가 대신 보내 준다면?")]
    caps = ["서 이사가 지우의 센서 보고서를 받아 들었어요", "지우가 박 팀장 브라우저의 낯선 설정을 찾았어요",
            "서 이사가 새 티켓을 올려요", "요청을 대신 보내 주면 어떻게 될까요?"]
    return scene(a, "요청을 누가 대신 보내요?", "서 이사의 질문과 박 팀장 브라우저의 낯선 설정", caps, "".join(body), bg="office")


def p2():
    a = new()
    t = "동기화 프로그램 요청은\n기록에 하나도 없어"
    row = lambda y, ok, n=None: (box(612, y, 216, 34, GREEN if ok else RED, BG, 6, sw=2) + (check(632, y + 17) if ok else cross(632, y + 17))
                         + text(652, y + 23, n if ok else "동기화 프로그램", 16, TXT, 700, "start"))
    body = [a.vis(person(110, 215, "지우", "normal"), 1, 2), a.vis(person(110, 215, "지우", "thinking"), 3, 4),
            panel(335, 285, "프록시 설정", "192.168.10.5 : 8080", 240, BLUE), pill(335, 365, "지우 PC 브라우저", MUTED, 17),
            box(600, 130, 240, 245, BLUE, PANEL, 10, sw=3) + text(720, 160, "프록시 192.168.10.5", 17, TXT, 700) + line(612, 176, 828, 176, LINE, 2),
            a.vis(row(188, True, "저장소 웹 페이지"), 2, 4), a.vis(row(232, True, "저장소 파일 목록"), 2, 4), mark(a, 612, 188, 216, 78, 2),
            a.vis(row(284, False), 3, 4), mark(a, 612, 284, 216, 34, 3),
            a.vis(thought(335, 165, t, tail_to=(128, 195), color=BLUE), 3, 4),
            question(a, "같은 PC인데 왜 어떤 요청만 프록시를 거칠까?")]
    caps = ["지우가 PC 브라우저에 프록시 주소를 넣어요", "클라우드 저장소를 열자 기록이 쌓여요",
            "같은 PC의 동기화 프로그램은 기록이 없어요", "프록시를 거치는 요청은 따로 있을까요?"]
    return scene(a, "브라우저의 프록시 칸", "같은 PC인데 어떤 요청만 기록에 남아요", caps, "".join(body), bg="office")


def p3():
    a = new()
    b = "프록시가 고장 났나 봐요"
    t = "내 PC도 그 저장소만\n안 열려"
    body = [a.vis(person(110, 215, "박 팀장", "normal"), 1, 1), a.vis(person(110, 215, "박 팀장", "worried"), 2, 4),
            a.vis(person(840, 215, "지우", "normal", facing="left"), 1, 2), a.vis(person(840, 215, "지우", "thinking", facing="left"), 3, 4),
            a.vis(monitor(380, 275, "ok", "다른 사이트는 열려요"), 1, 1),
            a.vis(monitor(380, 275, "error", "프록시 터널 연결 실패"), 2, 4), mark(a, 270, 212, 220, 126, 2),
            a.vis(bubble(250, 150, b, tail_to=(118, 188), color=TERRACOTTA), 3, 3), bm(a, 250, 150, b, 3),
            a.vis(thought(660, 160, t, tail_to=(830, 190), color=BLUE), 3, 4),
            question(a, "정말 프록시가 고장 난 걸까?")]
    caps = ["박 팀장과 지우가 아침 사무실에 있어요", "박 팀장 화면에 터널 연결 실패만 떠요",
            "박 팀장은 프록시가 고장 났다고 말해요", "지우는 프록시 안을 들여다봐야 해요"]
    return scene(a, "프록시가 고장 났나 봐요", "박 팀장 화면에는 터널 연결 실패만 떠요", caps, "".join(body), bg="office")


def p4():
    a = new()
    b = "회사에서 쓴 건지 아무도 모르는 거죠?"
    t = "직접 접속, 회사 프록시,\n해외 프록시일 때는?"
    body = [a.vis(person(110, 215, "박 팀장", "normal"), 1, 1), a.vis(person(110, 215, "박 팀장", "worried"), 2, 4),
            a.vis(person(400, 215, "지우", "normal", facing="left"), 1, 2), a.vis(person(400, 215, "지우", "thinking", facing="left"), 3, 4),
            clock(600, 250, "점심시간"), srv(850, 260, "클라우드 저장소", "203.0.113.80"),
            a.vis(bubble(250, 150, b, tail_to=(118, 188), color=TERRACOTTA), 2, 2), bm(a, 250, 150, b, 2),
            a.vis(thought(610, 150, t, tail_to=(392, 190), color=BLUE), 3, 4), mark(a, 520, 112, 195, 76, 99) if False else "",
            question(a, "저장소에는 누구 주소가 보일까?")]
    caps = ["점심시간, 박 팀장이 지우와 이야기해요", "박 팀장이 회사에서 쓴 게 드러날지 물어요",
            "지우는 바로 답하지 못하고 생각해요", "저장소에 보이는 주소를 따져 봐요"]
    return scene(a, "저장소에 보이는 주소", "점심시간, 박 팀장이 지우에게 물어요", caps, "".join(body), bg="office")


def p5():
    a = new()
    b = "그 무료 서버는 대체 누가 운영하는 거예요?"
    body = [a.vis(person(170, 215, "서 이사", "normal"), 1, 2), a.vis(person(170, 215, "서 이사", "worried"), 3, 4),
            person(790, 215, "지우", "normal", facing="left"),
            doc(480, 225, "박 팀장 사례"),
            a.vis(alert_card(480, 345, "막아 둔 개인 클라우드를 써 왔어요"), 2, 4), mark(a, 312, 319, 336, 52, 2),
            a.vis(bubble(330, 150, b, tail_to=(178, 188), color=VIOLET), 3, 3), bm(a, 330, 150, b, 3),
            question(a, "그 대가로 무엇을 넘겨주게 될까?")]
    caps = ["지우가 서 이사에게 박 팀장 사례를 보고해요", "박 팀장이 막아 둔 개인 클라우드를 써 왔어요",
            "서 이사는 무료 서버 운영자를 걱정해요", "낯선 중계 서버가 무엇을 아는지 따져 봐요"]
    return scene(a, "무료 프록시 사례 보고", "서 이사가 낯선 운영자를 걱정해요", caps, "".join(body), bg="office")


def p6():
    a = new()
    b = "사이트가 예전보다 살짝 늦게 열리는 것 같아요"
    link = line(450, 265, 555, 265, LINE, 4, "10 8")
    body = [a.vis(person(110, 215, "박 팀장", "normal"), 1, 1), a.vis(person(110, 215, "박 팀장", "worried"), 2, 4),
            pill(480, 140, "프록시를 정식으로 쓴 지 2주", MUTED, 17, False, 300) if False else "",
            a.vis(monitor(340, 275, "ok"), 1, 1), a.vis(monitor(340, 275, "loading"), 2, 2), a.vis(monitor(340, 275, "error", "웹과 저장소가 끊겼어요"), 3, 4),
            link, srv(660, 262, "프록시", "192.168.10.5"),
            a.vis(bubble(300, 150, b, tail_to=(118, 188), color=TERRACOTTA), 2, 2), bm(a, 300, 150, b, 2),
            a.vis(alert_card(740, 150, "업데이트 뒤 안 켜져요"), 3, 4), mark(a, 580, 212, 160, 100, 3),
            a.vis(cross(660, 262), 3, 4),
            question(a, "프록시 하나로 얻은 편리함에 붙은 값은?")]
    caps = ["프록시를 정식으로 쓴 지 2주가 지났어요", "박 팀장은 사이트가 조금 늦다고 말해요",
            "금요일 오후 프록시가 다시 켜지지 않아요", "편리함에 어떤 값이 붙어 있었을까요?"]
    return scene(a, "프록시를 쓴 지 2주 뒤", "느려진 사이트, 그리고 금요일 오후", caps, "".join(body), bg="office")


PAGES = {"u11-l04-p1-story-ai-request": p1, "u11-l04-p2-story-proxy-field": p2, "u11-l04-p3-story-tunnel-fail": p3,
         "u11-l04-p4-story-seen-address": p4, "u11-l04-p5-story-free-proxy": p5, "u11-l04-p6-story-extra-hop": p6}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        write(OUT, name, fn())
        print(OUT / f"{name}.svg")
