#!/usr/bin/env python3
"""Unit 9 Lesson 2 (web and internet history) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u9_l02.py   (add --svg-only to skip the lesson.md edit).

Every page gets a daily-life SVG at the top (after_paragraph -1) and a network SVG with the same layout after a
concept paragraph. The existing wiki `animations:` entries (pages 3, 4, 8) are left as they are; the new items go
into a separate `illustrations:` key on each page."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import hl, arrow, brace, person, dur
from u7_l01 import mv
from u10_l01 import role, msg, add_illustrations

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/02-*"))
OUT = LESSON / "assets" / "animations"


def doc(x, y, label, c=BLUE, w=110, h=120, link=None):
    """Document card centred on x with its top at y; optional underlined link line at the bottom."""
    s = box(x - w / 2, y, w, h, c, PANEL, 8, sw=3) + text(x, y + 26, label, 15, c, 700)
    s += "".join(line(x - w / 2 + 14, y + 46 + i * 16, x + w / 2 - 14, y + 46 + i * 16, LINE, 4) for i in range(2))
    if link:
        s += text(x, y + h - 16, link, 14, BLUE, 700) + line(x - tw(link, 14) / 2, y + h - 12, x + tw(link, 14) / 2, y + h - 12, BLUE, 2)
    return s


# ---------- Page 1: base vs services on it ----------
def page1(daily):
    a = Anim(4, dur(daily))
    svc = ([("도서관 버스", "책을 빌려 읽어요", BLUE), ("우편차", "편지를 날라요", ORANGE), ("놀이 버스", "함께 놀러 가요", VIOLET)] if daily
           else [("웹", "문서와 링크", BLUE), ("이메일", "편지 주고받기", ORANGE), ("온라인 게임", "함께 플레이", VIOLET)])
    xs = [110, 380, 650]
    body = [box(80, 380, 800, 60, GREEN, PANEL, 12, sw=3) + text(480, 418, "도로: 모두가 다니는 기반" if daily else "인터넷: 컴퓨터와 네트워크를 잇는 기반", 18, GREEN, 700),
            a.vis(hl(80, 380, 800, 60, GREEN, 12), 1, 1)]
    for k, (x, (n, s, c)) in enumerate(zip(xs, svc)):
        st = 2 if k == 0 else 3
        body.append(a.vis(role(x, 230, 200, 100, n, s, c) + line(x + 100, 330, x + 100, 380, c, 4, "6 5"), st, 4))
    body += [a.vis(hl(110, 230, 200, 100, BLUE, 12), 2, 2),
             mv(a, parcel() if daily else packet(), [(130, 410), (840, 410)], 2, 2, 2),
             a.vis(brace(110, 850, 205, MUTED, "도로는 기반, 버스는 그 위의 한 가지" if daily else "웹은 인터넷을 이용하는 여러 서비스 중 하나", True, 17), 4, 4)]
    if daily:
        t, sub = "도로와 그 위를 달리는 차", "도로는 기반이고, 차마다 하는 일이 달라요"
        caps = ["도로는 여러 차가 함께 다니는 기반이에요", "도서관 버스는 도로를 달려 책을 빌려줘요", "우편차와 놀이 버스도 같은 도로를 써요", "도로와 도서관 버스는 같은 것이 아니에요"]
    else:
        t, sub = "웹은 인터넷 위의 서비스", "인터넷은 연결 기반, 웹은 문서·링크 서비스예요"
        caps = ["인터넷은 컴퓨터와 네트워크를 잇는 기반이에요", "웹은 인터넷 위에서 문서와 링크를 주고받아요", "이메일과 온라인 게임도 인터넷을 이용해요", "웹은 인터넷을 이용하는 서비스 중 하나예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: find references by hand vs a direct connection ----------
def page2(daily):
    a = Anim(4, dur(daily))
    A, C, D, B = ("보고서", "책 C", "책 D", "책 B") if daily else ("논문 A", "논문 C", "논문 D", "논문 B")
    body = [person(110, 290, "나" if daily else "연구자"),
            doc(300, 180, A, BLUE, 140, 140, "참고: 책 B" if daily else "참고문헌: 논문 B"),
            doc(620, 140, C, MUTED), doc(820, 140, D, MUTED), doc(720, 300, B, GREEN),
            a.vis(hl(230, 180, 140, 140, BLUE, 10), 1, 1),
            a.vis(f'<polyline points="370,250 565,200 765,200 720,300" fill="none" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="8 6"/>'
                  + ask(620, 120) + ask(820, 120) + text(470, 450, "이리저리 찾아다녀요" if daily else "직접 찾아 옮겨 가기 번거로워요", 18, ORANGE, 700), 2, 2),
            a.vis(line(370, 300, 662, 355, GREEN, 5) + check(720, 290)
                  + pill(470, 450, "책 B로 바로 가는 쪽지" if daily else "팀 버너스리의 제안: 문서를 서로 연결", GREEN, 17, True), 3, 4),
            a.vis(pill(300, 395, "누구나 쪽지를 따라 바로 찾아요" if daily else "연결된 자료를 함께 찾고 공유해요", VIOLET, 16, True), 4, 4)]
    if daily:
        t, sub = "참고한 책을 바로 찾고 싶어요", "책과 책을 이어 두면 찾기와 나누기가 쉬워요"
        caps = ["보고서를 읽다가 참고한 책 B가 궁금해요", "책장 여기저기를 다니며 책 B를 찾아요", "보고서에 책 B로 바로 가는 쪽지를 붙여요", "쪽지를 따라가면 누구나 바로 찾을 수 있어요"]
    else:
        t, sub = "CERN에서 시작된 문서 연결", "논문과 참고문헌을 이어 쉽게 찾고 공유해요"
        caps = ["CERN 연구자가 논문 A의 참고문헌을 봐요", "다른 논문을 직접 찾아 옮겨 가기 번거로워요", "팀 버너스리가 문서를 서로 잇는 방법을 제안해요", "연결된 자료를 여러 연구자가 찾고 공유해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: hypertext structure vs a link ----------
def page3(daily):
    a = Anim(4, dur(daily))
    names = ["과학책", "용어 사전", "동물 도감"] if daily else ["문서 A", "문서 B", "문서 C"]
    links = ["→ 사전 보기", "→ 도감 보기", None] if daily else ["링크: 문서 B", "링크: 문서 C", None]
    xs = [200, 480, 760]
    body = [doc(x, 180, n, c, 150, 160, l) for x, n, l, c in zip(xs, names, links, [BLUE, GREEN, VIOLET])]
    body += [a.vis(line(200, 250, 200, 300, ORANGE, 4) + f'<polygon points="200,312 192,298 208,298" fill="{ORANGE}"/>'
                   + text(200, 375, "앞에서 뒤로" if daily else "위에서 아래로", 16, ORANGE, 700), 1, 1),
             a.vis(arrow(255, 400, 324, GREEN, 4), 2, 4), a.vis(hl(130, 308, 140, 26, ORANGE, 8), 2, 2),
             a.vis(arrow(535, 680, 324, VIOLET, 4), 3, 4), a.vis(hl(410, 308, 140, 26, ORANGE, 8), 3, 3),
             a.vis(brace(125, 835, 165, VIOLET, "책들이 표시로 이어진 묶음" if daily else "하이퍼텍스트: 링크로 이어진 문서 구조", True, 16)
                   + hl(130, 308, 140, 26, ORANGE, 8) + hl(410, 308, 140, 26, ORANGE, 8)
                   + text(480, 420, "표시 하나는 건너갈 지점이에요" if daily else "링크: 실제로 누르는 연결 지점", 18, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "표시를 따라 다른 책으로", "책 속 표시를 따라 바로 건너갈 수 있어요"
        caps = ["종이책은 보통 앞에서 뒤로 차례대로 읽어요", "과학책 속 표시를 따라 사전으로 건너가요", "사전 속 표시를 따라 도감으로 또 건너가요", "이어진 책 묶음과 표시 하나를 구분해요"]
    else:
        t, sub = "하이퍼텍스트와 링크", "링크로 이어진 문서 구조가 하이퍼텍스트예요"
        caps = ["문서는 보통 위에서 아래로 차례대로 읽어요", "문서 A의 링크를 누르면 문서 B로 이동해요", "문서 B의 링크를 따라 문서 C로 갈 수 있어요", "링크로 이어진 구조가 하이퍼텍스트예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: content / exchange rule / road ----------
def page4(daily):
    a = Anim(4, dur(daily))
    content = (box(390, 130, 180, 150, ORANGE, PANEL, 8, sw=3) + text(480, 158, "편지 내용" if daily else "HTML 문서", 16, ORANGE, 700)
               + "".join(text(410, 190 + i * 28, s, 15, TXT, 700, "start") for i, s in enumerate(
                   ["제목", "문단", "다른 글 안내"] if daily else ["<h1> 제목", "<p> 문단", "<a> 링크"])))
    body = [person(110, 290, "나") if daily else laptop(110, 300, "브라우저"),
            house(850, 280, "도서관") if daily else pc(850, 300, "서버"),
            box(60, 390, 840, 60, LINE, PANEL, 12, sw=3) + text(480, 440, "편지가 다니는 길" if daily else "인터넷 (TCP/IP)", 15, MUTED, 700),
            a.vis(msg(170, 790, 330, "편지 보내 주세요" if daily else "HTTP 요청: GET /index.html", BLUE), 1, 1),
            a.vis(content, 2, 4), a.vis(hl(390, 130, 180, 150, ORANGE, 10), 2, 2),
            mv(a, parcel(), [(820, 412), (150, 412)], 3, 3, 3, 0.1, 0.8),
            a.vis(text(480, 340, "약속대로 답장" if daily else "HTTP 응답", 17, BLUE, 700), 3, 3),
            a.vis(pill(680, 205, "내용" if daily else "HTML", ORANGE, 17, True) + pill(480, 330, "주고받는 약속" if daily else "HTTP: 요청·응답 규칙", BLUE, 17, True)
                  + hl(60, 390, 840, 60, GREEN, 12) + pill(800, 380, "길" if daily else "전달 기반", GREEN, 15, True), 4, 4)]
    if daily:
        t, sub = "편지 내용, 약속, 그리고 길", "무엇을 쓰는지와 어떻게 주고받는지는 달라요"
        caps = ["나는 도서관에 소개 편지를 보내 달라고 부탁해요", "도서관이 제목과 문단을 갖춘 편지를 써요", "약속대로 답장이 길을 따라 나에게 와요", "내용, 주고받는 약속, 길은 각자 다른 일이에요"]
    else:
        t, sub = "HTML, HTTP, 인터넷의 역할", "문서 구조와 주고받는 규칙, 전달 기반을 나눠요"
        caps = ["브라우저가 HTTP 규칙으로 웹페이지를 요청해요", "서버에는 HTML로 구조를 표시한 문서가 있어요", "HTTP 응답이 인터넷(TCP/IP)을 따라 와요", "HTML은 문서, HTTP는 약속, 인터넷은 길이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: open standard -> interoperability ----------
def page5(daily):
    a = Anim(4, dur(daily))
    names = [f"{k}사 휴대폰" if daily else f"{k}사 브라우저" for k in "ABC"]
    ys = [150, 260, 370]
    body = [role(60, y, 180, 70, n, "", c, 17) for y, n, c in zip(ys, names, [BLUE, ORANGE, VIOLET])]
    body += [role(700, 250, 220, 90, "충전기" if daily else "웹 서버", "", GREEN, 19),
             a.vis(line(240, 185, 700, 280, RED, 4, "8 6") + cross(470, 232)
                   + text(470, 190, "회사 전용 비밀 모양" if daily else "회사 전용 비밀 규칙", 16, RED, 700), 1, 1),
             a.vis(pill(470, 150, "공개 규격 (모두가 볼 수 있어요)" if daily else "공개 표준: HTML · HTTP", GREEN, 17, True), 2, 4),
             a.vis(hl(700, 250, 220, 90, GREEN, 12), 2, 2),
             a.vis("".join(line(240, y + 35, 700, 295, GREEN, 4) for y in ys) + "".join(check(270, y + 35) for y in ys), 3, 4),
             a.vis(text(480, 460, "규칙이 없는 게 아니라 모두 아는 규칙이에요" if daily else "상호운용성: 회사가 달라도 함께 동작해요", 18, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "누구나 맞는 공통 규격", "규격이 공개되면 회사가 달라도 함께 써요"
        caps = ["회사만 아는 모양의 플러그는 다른 충전기에 안 맞아요", "모두가 볼 수 있는 공통 규격을 공개해요", "규격을 따르면 회사가 달라도 모두 충전돼요", "규칙이 없는 게 아니라 모두 아는 규칙이 있어요"]
    else:
        t, sub = "공개 표준과 상호운용성", "브라우저와 서버의 회사가 달라도 웹을 함께 써요"
        caps = ["회사 전용 비밀 규칙은 상대가 알아듣지 못해요", "HTML과 HTTP 같은 공개 표준을 함께 써요", "표준을 따르면 어느 회사 브라우저든 웹을 써요", "서로 다른 프로그램이 함께 동작해요: 상호운용성"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: idea -> build -> grow together -> award ----------
def page6(daily):
    a = Anim(4, dur(daily))
    st = ([("아이디어", "나눔함을 떠올려요"), ("직접 만들기", "상자를 만들어 시험"), ("함께 고치기", "친구들이 쓰며 고쳐요"), ("상 받기", "기여를 인정해요")] if daily
          else [("웹 제안", "문서를 잇는 아이디어"), ("초기 웹 구현", "쓸 수 있게 만들어요"), ("여럿이 발전", "오랫동안 함께 키워요"), ("튜링상", "컴퓨터 과학 공헌 인정")])
    cs = [BLUE, ORANGE, GREEN, VIOLET]
    body = []
    for k, ((n, s), c) in enumerate(zip(st, cs), 1):
        x = 40 + (k - 1) * 225
        body.append(a.vis(role(x, 180, 200, 100, n, s, c, 18) + (arrow(x - 22, x - 2, 230, MUTED, 3) if k > 1 else ""), k, 4))
        body.append(a.vis(hl(x, 180, 200, 100, c, 12), k, k))
    body += [a.vis(person(540, 350) + person(590, 350) + person(640, 350), 3, 4),
             a.vis(f'<circle cx="790" cy="355" r="26" fill="{ORANGE}"/>' + f'<polygon points="775,378 790,410 805,378" fill="{RED}"/>'
                   + text(480, 455, "상은 기여를 인정해요. 혼자 다 만들었다는 뜻은 아니에요", 17, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "아이디어에서 상까지", "생각, 만들기, 고치기가 이어져야 해요"
        caps = ["책 나눔함을 만들자는 아이디어를 떠올려요", "직접 상자를 만들어 시험해 봐요", "친구들이 함께 쓰며 오래 고쳐 나가요", "학교가 이 기여를 인정해 상을 줘요"]
    else:
        t, sub = "웹의 발전과 튜링상", "튜링상은 컴퓨터 과학에 기여한 일을 인정해요"
        caps = ["팀 버너스리가 문서를 잇는 웹을 제안해요", "초기 웹을 직접 만들어 쓰게 해요", "많은 사람이 오랫동안 웹을 발전시켜요", "그 공헌을 인정받아 튜링상을 받아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: two different contributions ----------
def page7(daily):
    a = Anim(4, dur(daily))
    L = (house(150, 300) + house(370, 300) + line(195, 320, 325, 320, GREEN, 6)) if daily else \
        (pc(150, 300, "서울") + pc(370, 300, "구미") + line(190, 290, 330, 290, GREEN, 5))
    R = "".join(doc(x, 230, n, BLUE, 90, 110) for x, n in zip([600, 720, 840], ["책 1", "책 2", "책 3"] if daily else ["문서", "문서", "문서"]))
    R += arrow(645, 675, 290, GREEN, 3) + arrow(765, 795, 290, GREEN, 3)
    body = [box(50, 160, 420, 280, LINE, PANEL, 14, sw=3) + text(260, 192, "길을 놓은 사람" if daily else "전길남 · 국내 연결 기반", 18, GREEN, 700),
            box(490, 160, 420, 280, LINE, PANEL, 14, sw=3) + text(700, 192, "이동 도서관을 만든 사람" if daily else "팀 버너스리 · 웹 문서 서비스", 18, BLUE, 700),
            a.vis(L, 1, 4), a.vis(hl(50, 160, 420, 280, GREEN, 14), 1, 1),
            a.vis(R, 2, 4), a.vis(hl(490, 160, 420, 280, BLUE, 14), 2, 2),
            a.vis(pill(480, 410, "서로 다른 일이에요" if daily else "연결 기반 ≠ 문서 서비스", ORANGE, 17, True), 3, 3),
            a.vis(pill(480, 140, "마을 공로상" if daily else "인터넷 명예의 전당", VIOLET, 17, True)
                  + pill(480, 410, "함께 언급되지만 역할은 달라요", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "길을 놓은 사람, 도서관을 만든 사람", "둘 다 마을에 도움이 됐지만 하는 일이 달라요"
        caps = ["한 사람은 마을과 마을을 잇는 길을 놓았어요", "다른 사람은 길 위를 다니는 이동 도서관을 만들었어요", "길 놓기와 도서관 만들기는 서로 다른 일이에요", "둘 다 상을 받았지만 맡은 역할은 달라요"]
    else:
        t, sub = "전길남과 팀 버너스리", "연결 기반과 웹 서비스, 서로 다른 기여예요"
        caps = ["전길남은 국내 컴퓨터 네트워크 연결에 기여했어요", "팀 버너스리는 문서를 잇는 웹을 만들었어요", "연결 기반과 문서 서비스는 서로 다른 일이에요", "둘 다 인터넷 명예의 전당에 올랐지만 역할은 달라요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: 1982 research link with a software router ----------
def page8(daily):
    a = Anim(4, dur(daily))
    body = [box(50, 180, 250, 190, BLUE, PANEL, 14, sw=3) + text(175, 210, "마을 A" if daily else "서울대학교", 18, BLUE, 700),
            box(660, 180, 250, 190, GREEN, PANEL, 14, sw=3) + text(785, 210, "마을 B" if daily else "구미 전자기술연구소", 17, GREEN, 700),
            house(175, 300) if daily else pc(175, 300), house(785, 300) if daily else pc(785, 300),
            a.vis(ask(480, 275) + text(480, 330, "어떻게 이을까요?", 17, ORANGE, 700), 1, 1),
            a.vis(role(400, 220, 160, 90, "안내판" if daily else "라우터 장비", "구하기 어려워요", RED, 17) + cross(560, 220), 2, 2),
            a.vis(line(300, 275, 660, 275, LINE, 4, "8 6")
                  + role(390, 220, 180, 110, "직접 만든 안내판" if daily else "소프트웨어 라우터", "길을 골라 보내요", GREEN, 16), 3, 4),
            mv(a, parcel() if daily else packet(), [(240, 345), (480, 345), (720, 345)], 3, 3, 3, 0.1, 0.8),
            a.vis(pill(480, 430, "길이 생긴 것 ≠ 모두가 버스를 타는 것" if daily else "초기 연구망 ≠ 누구나 쓰는 대중 인터넷 서비스", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "안내판을 직접 만들어 길을 이어요", "필요한 장비가 없으면 직접 만들기도 해요"
        caps = ["멀리 떨어진 두 마을 사이에 길을 이으려 해요", "갈림길 안내판을 구하기 어려웠어요", "안내판을 직접 만들어 세우고 짐을 보내요", "길이 생긴 것과 모두가 버스를 타는 건 달라요"]
    else:
        t, sub = "1982년 서울대–구미 연구망", "라우터 기능을 소프트웨어로 구현해 연결했어요"
        caps = ["1982년 서울대와 구미 연구소를 이으려 해요", "당시에는 라우터 장비를 구하기 어려웠어요", "라우터 기능을 소프트웨어로 직접 만들어 이어요", "초기 연구망은 대중 인터넷 서비스와 구분해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: request, response, transport, link restarts ----------
def page9(daily):
    a = Anim(4, dur(daily))
    body = [person(110, 290, "나") if daily else laptop(110, 300, "브라우저"),
            house(850, 280, "도서관") if daily else pc(850, 300, "서버"),
            box(60, 390, 840, 60, LINE, PANEL, 12, sw=3) + text(480, 440, "배달 길" if daily else "인터넷 · TCP/IP", 15, MUTED, 700),
            a.vis(msg(170, 790, 180, "신청서로 부탁" if daily else "HTTP 요청", BLUE), 1, 1),
            a.vis(msg(790, 170, 240, "약속대로 답" if daily else "HTTP 응답", ORANGE), 2, 2),
            a.vis(doc(260, 260, "책" if daily else "HTML 문서", ORANGE, 120, 110, "→ 다른 책" if daily else "링크"), 2, 4),
            mv(a, parcel() if daily else packet(), [(820, 412), (150, 412)], 3, 3, 3, 0.1, 0.8),
            a.vis(hl(60, 390, 840, 60, GREEN, 12), 3, 3),
            a.vis(hl(205, 340, 110, 26, ORANGE, 8) + msg(330, 790, 300, "다시 신청" if daily else "다시 요청", GREEN), 4, 4)]
    if daily:
        t, sub = "책 내용, 신청 약속, 배달 길", "책 속 표시를 보면 또 다른 책을 신청해요"
        caps = ["나는 신청서 약속대로 도서관에 책을 부탁해요", "도서관이 약속대로 책을 보내 줘요", "책은 배달 길을 따라 나에게 와요", "책 속 ‘다른 책’ 표시를 보면 다시 신청해요"]
    else:
        t, sub = "문서·규칙·연결로 나누어 보기", "HTML은 문서, HTTP는 규칙, 인터넷은 연결이에요"
        caps = ["브라우저가 HTTP 규칙으로 서버에 요청해요", "서버가 HTML 문서를 HTTP 응답으로 보내요", "데이터는 인터넷과 TCP/IP를 통해 오가요", "링크를 누르면 다른 문서를 다시 요청해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l32-daily-road-and-vehicles", "l32-web-on-internet", page1, 0),
    ("l32-daily-reference-note", "l32-cern-linked-papers", page2, 0),
    ("l32-daily-book-jump", "l32-hypertext-structure", page3, 0),
    ("l32-daily-letter-promise-road", "l32-html-http-roles", page4, 0),
    ("l32-daily-common-plug", "l32-open-standard-interop", page5, 1),
    ("l32-daily-idea-to-award", "l32-turing-award-path", page6, 1),
    ("l32-daily-road-vs-library", "l32-two-contributions", page7, 0),
    ("l32-daily-handmade-sign", "l32-1982-software-router", page8, 0),
    ("l32-daily-book-order-loop", "l32-web-page-flow", page9, 0),
]

COPY = {
    "l32-daily-road-and-vehicles": ("도로와 그 위를 달리는 차",
        "도로가 먼저 강조되고, 그 위에 도서관 버스, 우편차, 놀이 버스가 차례로 나타납니다. 마지막에는 도로는 기반이고 버스는 그 위의 한 가지라고 표시됩니다.",
        "도로는 여러 차가 함께 쓰는 기반이고, 차마다 하는 일이 다릅니다."),
    "l32-web-on-internet": ("웹은 인터넷 위의 서비스",
        "인터넷 연결 기반이 먼저 강조되고, 그 위에 웹, 이메일, 온라인 게임이 차례로 나타납니다. 마지막에는 웹이 인터넷을 이용하는 여러 서비스 중 하나라고 표시됩니다.",
        "인터넷은 연결 기반이고, 웹은 그 위에서 문서와 링크를 주고받는 서비스입니다."),
    "l32-daily-reference-note": ("참고한 책을 바로 찾고 싶어요",
        "보고서의 참고 표시를 보고 책장 여기저기를 다니며 책 B를 찾다가, 보고서에 책 B로 바로 가는 쪽지를 붙입니다. 마지막에는 누구나 쪽지를 따라 바로 찾는다고 표시됩니다.",
        "책과 책을 이어 두면 찾기와 나누기가 쉬워집니다."),
    "l32-cern-linked-papers": ("CERN에서 시작된 문서 연결",
        "CERN 연구자가 논문 A의 참고문헌을 보고 다른 논문을 직접 찾아다니다가, 문서를 서로 연결하자는 제안으로 논문 B까지 바로 이어집니다. 마지막에는 연결된 자료를 함께 찾고 공유한다고 표시됩니다.",
        "연구 자료를 연결하고 공유하려는 필요가 초기 웹의 출발점이 되었습니다.", 0),
    "l32-daily-book-jump": ("표시를 따라 다른 책으로",
        "과학책을 앞에서 뒤로 읽다가, 책 속 표시를 따라 용어 사전으로, 다시 사전 속 표시를 따라 동물 도감으로 건너갑니다. 마지막에는 표시로 이어진 책 묶음과 표시 하나가 구분되어 표시됩니다.",
        "표시로 이어진 묶음 전체와 건너갈 지점 하나를 구분합니다."),
    "l32-hypertext-structure": ("하이퍼텍스트와 링크",
        "문서 A를 위에서 아래로 읽다가 링크를 눌러 문서 B로, 다시 B의 링크를 따라 문서 C로 이동합니다. 마지막에는 전체 연결 구조가 하이퍼텍스트, 누르는 지점이 링크라고 표시됩니다.",
        "하이퍼텍스트는 링크로 이어진 문서 구조이고, 링크는 다른 자료로 이동하는 연결 지점입니다.", 0),
    "l32-daily-letter-promise-road": ("편지 내용, 약속, 그리고 길",
        "나는 도서관에 소개 편지를 부탁하고, 도서관은 제목·문단·다른 글 안내를 갖춘 편지를 씁니다. 답장은 길을 따라 나에게 오고, 마지막에는 내용, 주고받는 약속, 길이 따로 표시됩니다.",
        "편지의 내용과 주고받는 약속, 편지가 다니는 길은 각자 다른 일입니다."),
    "l32-html-http-roles": ("HTML, HTTP, 인터넷의 역할",
        "브라우저가 HTTP 요청 GET /index.html을 보내고, 서버에는 제목·문단·링크 구조를 표시한 HTML 문서가 있습니다. HTTP 응답이 인터넷(TCP/IP)을 따라 브라우저에 오고, 마지막에는 HTML, HTTP, 전달 기반이 따로 표시됩니다.",
        "HTML은 문서 구조, HTTP는 요청·응답 규칙, 인터넷은 데이터가 이동할 기반입니다.", 0),
    "l32-daily-common-plug": ("누구나 맞는 공통 규격",
        "A사 휴대폰의 회사 전용 플러그는 충전기에 맞지 않다가, 모두가 볼 수 있는 공통 규격이 공개됩니다. 규격을 따르자 A, B, C사 휴대폰이 모두 충전기에 연결됩니다.",
        "규칙이 없는 것이 아니라 모두가 아는 공개 규칙이 있어서 함께 쓸 수 있습니다."),
    "l32-open-standard-interop": ("공개 표준과 상호운용성",
        "A사 브라우저의 회사 전용 비밀 규칙은 웹 서버가 알아듣지 못하다가, HTML·HTTP 같은 공개 표준을 함께 쓰자 A, B, C사 브라우저가 모두 웹 서버와 연결됩니다. 마지막에는 상호운용성이 표시됩니다.",
        "공개된 표준을 따르면 회사가 다른 브라우저와 서버도 함께 동작합니다.", 1),
    "l32-daily-idea-to-award": ("아이디어에서 상까지",
        "책 나눔함 아이디어, 직접 만들어 시험하기, 친구들이 함께 쓰며 고치기, 상 받기가 차례로 나타납니다. 마지막에는 상이 기여를 인정할 뿐 혼자 다 만들었다는 뜻은 아니라고 표시됩니다.",
        "아이디어만으로는 완성되지 않고, 만들고 고치는 과정이 이어져야 합니다."),
    "l32-turing-award-path": ("웹의 발전과 튜링상",
        "웹 제안, 초기 웹 구현, 여러 사람의 발전, 튜링상이 차례로 나타납니다. 마지막에는 상이 기여를 인정할 뿐 혼자 다 만들었다는 뜻은 아니라고 표시됩니다.",
        "튜링상은 컴퓨터 과학에 큰 공헌을 한 사람의 기여를 인정합니다.", 1),
    "l32-daily-road-vs-library": ("길을 놓은 사람, 도서관을 만든 사람",
        "왼쪽에는 마을과 마을을 잇는 길, 오른쪽에는 그 길 위를 다니는 이동 도서관의 책들이 차례로 나타납니다. 마지막에는 둘 다 상을 받았지만 역할은 다르다고 표시됩니다.",
        "함께 상을 받아도 길 놓기와 도서관 만들기는 서로 다른 일입니다."),
    "l32-two-contributions": ("전길남과 팀 버너스리",
        "왼쪽에는 전길남의 서울과 구미 사이 연결 기반, 오른쪽에는 팀 버너스리의 링크로 이어진 웹 문서가 차례로 나타납니다. 마지막에는 두 사람이 인터넷 명예의 전당에 함께 언급되지만 역할은 다르다고 표시됩니다.",
        "인터넷 연결 기반의 구축과 웹 문서 서비스의 발전은 서로 다른 기여입니다.", 0),
    "l32-daily-handmade-sign": ("안내판을 직접 만들어 길을 이어요",
        "두 마을 사이를 이으려는데 갈림길 안내판을 구하기 어려워서, 직접 만든 안내판을 세우고 짐을 마을 A에서 마을 B로 보냅니다. 마지막에는 길이 생긴 것과 모두가 버스를 타는 것은 다르다고 표시됩니다.",
        "필요한 장비가 없으면 직접 만들어 길을 잇기도 합니다."),
    "l32-1982-software-router": ("1982년 서울대–구미 연구망",
        "서울대학교와 구미 전자기술연구소를 이으려는데 라우터 장비를 구하기 어려워서, 소프트웨어로 만든 라우터가 길을 골라 데이터를 보냅니다. 마지막에는 초기 연구망과 대중 인터넷 서비스가 다르다고 표시됩니다.",
        "1982년 연구망은 라우터 기능을 소프트웨어로 구현한 국내 초기 네트워크 구축 사례입니다.", 0),
    "l32-daily-book-order-loop": ("책 내용, 신청 약속, 배달 길",
        "나는 신청서로 도서관에 책을 부탁하고, 도서관은 약속대로 책을 보냅니다. 책은 배달 길을 따라 오고, 책 속 다른 책 표시를 보면 다시 신청합니다.",
        "책 내용, 신청 약속, 배달 길은 각자 다른 역할을 맡습니다."),
    "l32-web-page-flow": ("문서·규칙·연결로 나누어 보기",
        "브라우저가 HTTP 요청을 보내고, 서버가 HTML 문서를 HTTP 응답으로 돌려줍니다. 데이터는 인터넷과 TCP/IP를 통해 오가고, 문서 속 링크를 누르면 다시 요청이 시작됩니다.",
        "HTML이 문서를 만들고, HTTP가 주고받으며, 인터넷이 연결을 제공합니다.", 0),
}


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        d, n = COPY[dn], COPY[nn]
        pages.append([(dn, d[0], d[1], d[2], -1), (nn, n[0], n[1], n[2], after)])
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        add_illustrations(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
