#!/usr/bin/env python3
"""Unit 10 Lesson 1 (web service structure, basics) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u10_l01.py   (add --svg-only to skip the lesson.md edit).

Every page gets a daily-life SVG at the top (after_paragraph -1) and a network SVG with the same layout after a
matching paragraph. The existing wiki diagram (lesson-35.svg) and the page 2 / page 9 `animations:` entries are
left exactly as they are; the new items are added as a separate `illustrations:` key on each page."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/05-*"))
OUT = LESSON / "assets" / "animations"


def at(x, y, inner):
    return f'<g transform="translate({x},{y})">{inner}</g>'


def role(x, y, w, h, title, sub, c, fs=19):
    return (box(x, y, w, h, c, PANEL, 12, sw=3) + text(x + w / 2, y + 30, title, fs, c, 700)
            + (text(x + w / 2, y + h - 16, sub, 14, MUTED) if sub else ""))


def lanes(L, R, hl_, hr, y0=150, y1=450, cl=BLUE, cr=GREEN, w=170):
    return (pill(L, 128, hl_, cl, 17, True, w) + pill(R, 128, hr, cr, 17, True, w)
            + line(L, y0, L, y1, LINE, 3, "8 6") + line(R, y0, R, y1, LINE, 3, "8 6"))


def msg(x0, x1, y, label, c, fs=16):
    return arrow(x0 + 8, x1 - 8, y, c, 5) + text((x0 + x1) / 2, y - 12, label, fs, c, 700)


# ---------- Page 1: content vs envelope, then server structure ----------
def page1(daily):
    a = Anim(4, dur(daily))
    L, R, y = 130, 830, 300
    cli = person(L, y - 10, "나") if daily else laptop(L, y, "브라우저")
    srv = house(R, y - 20, "가게") if daily else pc(R, y, "서버")
    letter = cell(-80, -24, 160, 48, "로그인 화면 주세요" if daily else "GET /login", ORANGE, 15)
    env = box(-98, -40, 196, 80, BLUE, "none", 8, sw=3)
    mid = box(330, 215, 300, 170, LINE, PANEL, 14, dash=True, sw=2) + text(480, 240, "우체국" if daily else "네트워크 (TCP/IP)", 17, MUTED, 700)
    body = [cli, srv, mid,
            a.vis(at(250, y, letter) + pill(250, 360, "내용: 무엇을 원하는지" if daily else "HTTP: 요청의 의미", ORANGE, 16, True), 1, 1),
            a.vis(at(250, y, letter + env) + pill(250, 360, "봉투: 어디로 나를지" if daily else "TCP/IP: 데이터 전달", BLUE, 16, True), 2, 2),
            mv(a, letter + env, [(250, y), (480, y), (700, y)], 3, 3, 3, 0.1, 0.8),
            a.vis(text(480, 430, "내용과 봉투는 서로 다른 일이에요" if daily else "의미(HTTP)와 전달(TCP/IP)은 서로 다른 층이에요", 18, MUTED, 700), 3, 3),
            a.vis(at(700, y, letter) + pill(700, 360, "받는 쪽이 내용을 읽어요" if daily else "서버가 요청으로 읽어요", GREEN, 16, True)
                  + arrow(740, 200, 425, GREEN, 5) + text(480, 412, "답장" if daily else "응답", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "편지의 내용과 봉투", "내용을 쓰는 일과 나르는 일은 달라요"
        caps = ["먼저 원하는 내용을 편지에 써요", "그 편지를 봉투에 담아 주소를 적어요", "우체국이 봉투를 가게까지 날라요", "가게는 내용을 읽고 답장을 보내요"]
    else:
        t, sub = "HTTP 요청과 TCP/IP 전달", "요청의 의미와 전달은 서로 다른 층이에요"
        caps = ["브라우저가 GET /login 요청을 만들어요", "TCP/IP가 그 요청을 데이터로 감싸 전달해요", "네트워크가 요청을 서버까지 날라요", "서버가 요청을 읽고 응답을 돌려보내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: four steps ----------
def page2(daily):
    a = Anim(4, dur(daily))
    if daily:
        cli, srv = phone(110, 300, "나"), phone(850, 300, "친구")
        card = (box(320, 135, 320, 100, LINE, PANEL, 12, sw=3) + text(480, 165, "연락처", 17, MUTED, 700)
                + pill(385, 205, "친구 이름", BLUE, 16, False, 120) + arrow(450, 515, 205, MUTED, 3) + pill(575, 205, "전화번호", GREEN, 16, True, 110))
        body = [cli, srv, card, line(190, 300, 780, 300, LINE, 3, "8 6"),
                a.vis(hl(320, 135, 320, 100, BLUE, 12), 1, 1),
                a.vis(line(190, 300, 780, 300, GREEN, 6) + pill(480, 345, "대표번호 + 내선 번호", GREEN, 17, True), 2, 4),
                a.vis(msg(200, 760, 275, "“로그인 화면 보여 주세요”", BLUE, 17), 3, 3),
                a.vis(msg(760, 200, 275, "“네, 여기 있어요”", ORANGE, 17), 4, 4)]
        t, sub = "친구에게 전화하는 네 걸음", "번호 찾기, 연결, 말 건네기, 대답 듣기예요"
        caps = ["먼저 연락처에서 이름에 맞는 번호를 찾아요", "전화를 걸어 말할 통로를 이어요", "통로가 이어지면 필요한 말을 건네요", "친구가 말에 대답해 줘요"]
        return frame(a, t, sub, caps, "".join(body))
    B, D, S = 170, 480, 790
    body = [pill(B, 128, "브라우저", BLUE, 17, True, 150), pill(D, 128, "DNS", ORANGE, 17, True, 150), pill(S, 128, "웹 서버", GREEN, 17, True, 150),
            line(B, 150, B, 450, LINE, 3, "8 6"), line(D, 150, D, 450, LINE, 3, "8 6"), line(S, 150, S, 450, LINE, 3, "8 6"),
            a.vis(msg(B, D, 190, "shop.example의 IP는?", ORANGE) + msg(D, B, 235, "IP 주소 203.0.113.10 (예시)", ORANGE), 1, 4),
            a.vis(msg(B, S, 295, "TCP 연결 준비: IP + 포트 443 (예시)", BLUE), 2, 4),
            a.vis(msg(B, S, 350, "GET /login", GREEN), 3, 4),
            a.vis(msg(S, B, 405, "응답: 상태 코드 · 헤더 · 본문(HTML)", GREEN), 4, 4)]
    t, sub = "이름 찾기, 연결, 요청, 응답", "네 걸음은 서로 다른 일이에요"
    caps = ["DNS가 사이트 이름에 맞는 IP 주소를 알려 줘요", "서버와 요청을 주고받을 TCP 통로를 마련해요", "브라우저가 GET /login 요청을 보내요", "서버가 HTTP 응답으로 HTML을 돌려줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: HTML content vs CSS style ----------
def page3(daily):
    a = Anim(4, dur(daily))
    left = (box(40, 140, 250, 250, BLUE, PANEL, 12, sw=3) + text(165, 172, "메뉴판 내용" if daily else "HTML (구조·내용)", 18, BLUE, 700)
            + (text(60, 230, "불고기 8,000원", 18, TXT, 600, "start") + text(60, 275, "비빔밥 7,000원", 18, TXT, 600, "start")
               if daily else text(60, 230, "<h1>상품 목록</h1>", 16, TXT, 600, "start") + text(60, 275, '<a href="/items/7">', 15, TXT, 600, "start")
               + text(60, 300, "상품 보기</a>", 15, TXT, 600, "start")))
    css = lambda lab, c: box(330, 190, 260, 150, c, PANEL, 12, sw=3) + text(460, 222, lab, 18, c, 700)
    res = lambda big, c, fs: (box(640, 140, 280, 250, LINE, PANEL, 12, sw=3) + text(780, 172, "화면" if not daily else "완성된 메뉴판", 18, MUTED, 700)
                              + text(780, 235, "불고기 8,000원" if daily else "상품 목록", fs, c, 700)
                              + text(780, 300, "비빔밥 7,000원" if daily else "상품 보기", 20 if not daily else 18, TXT, 500))
    rA, rB = ("모양 규칙 A" if daily else "CSS A"), ("모양 규칙 B" if daily else "CSS B")
    dA, dB = ("제목: 크게 · 빨강" if daily else "제목: 크게 · 파랑"), ("제목: 작게 · 검정" if daily else "제목: 작게 · 검정")
    body = [left,
            a.vis(css(rA, ORANGE) + text(460, 280, dA, 17, TXT) + arrow(295, 335, 265, MUTED, 3) + arrow(595, 635, 265, MUTED, 3)
                  + res("A", RED if daily else BLUE, 34), 2, 2),
            a.vis(css(rB, GREEN) + text(460, 280, dB, 17, TXT) + arrow(295, 335, 265, MUTED, 3) + arrow(595, 635, 265, MUTED, 3)
                  + res("B", TXT, 20), 3, 4),
            a.vis(hl(40, 140, 250, 250, BLUE, 12), 1, 1),
            a.vis(text(165, 420, "내용은 그대로예요", 18, BLUE, 700), 3, 3),
            a.vis(pill(480, 440, "모양만으로 없던 내용이 생기지는 않아요", ORANGE, 18, True), 4, 4)]
    if daily:
        t, sub = "메뉴판의 내용과 모양", "같은 내용도 모양 규칙에 따라 달라 보여요"
        caps = ["메뉴판에는 음식 이름과 가격이 적혀 있어요", "모양 규칙 A를 입히면 제목이 크고 빨갛게 보여요", "모양 규칙 B로 바꿔도 내용은 그대로예요", "모양만으로 없던 메뉴가 생기지는 않아요"]
    else:
        t, sub = "HTML은 구조, CSS는 모양", "같은 HTML에 다른 CSS를 입힐 수 있어요"
        caps = ["HTML은 제목과 링크 같은 구조와 내용을 표시해요", "CSS A를 적용하면 제목이 크고 파랗게 보여요", "CSS B로 바꿔도 HTML의 내용과 링크는 그대로예요", "CSS만으로 없던 상품 정보가 생기지는 않아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: browser renders, JS runs in the browser ----------
def page4(daily):
    a = Anim(4, dur(daily))
    files = ["레시피 카드", "플레이팅 규칙", "반응 지침"] if daily else ["HTML", "CSS", "JavaScript"]
    cols = [BLUE, ORANGE, VIOLET]
    stages = ["레시피 읽기", "플레이팅 입히기", "접시 완성"] if daily else ["HTML 읽기", "CSS 적용", "화면 그리기"]
    body = [box(40, 140, 220, 260, LINE, PANEL, 12, sw=3) + text(150, 170, "재료 업체" if daily else "서버", 18, MUTED, 700),
            box(330, 140, 590, 260, LINE, PANEL, 12, sw=3) + text(625, 170, "내 주방" if daily else "브라우저", 18, MUTED, 700)]
    for i, (f, c) in enumerate(zip(files, cols)):
        body.append(cell(65, 195 + i * 62, 170, 46, f, c, 16))
    for i, s in enumerate(stages):
        body.append(box(350 + i * 190, 185, 175, 50, cols[i], BG, 8, sw=2) + text(437 + i * 190, 217, s, 15, cols[i], 700))
    body += [a.vis(arrow(245, 335, 295, MUTED, 4) + pill(290, 262, "보내요", MUTED, 15, False, 72), 1, 4),
             a.vis(hl(350, 185, 175, 50, BLUE) + hl(540, 185, 175, 50, ORANGE) + hl(730, 185, 175, 50, VIOLET), 2, 2),
             a.vis(box(350, 270, 290, 110, TXT, PANEL, 10, sw=2) + (text(495, 310, "접시: 불고기", 20, TXT, 700) if daily else text(495, 310, "상품 목록", 22, TXT, 700))
                   + cell(430, 330, 130, 36, "호출벨" if daily else "로그인 버튼", VIOLET, 15), 2, 4),
             a.vis(hl(430, 330, 130, 36, VIOLET) + text(780, 300, "“곧 갑니다” 안내", 16, VIOLET, 700) if daily else
                   hl(430, 330, 130, 36, VIOLET) + text(780, 300, "안내 문구 표시", 16, VIOLET, 700), 3, 3),
             a.vis(box(660, 320, 245, 60, VIOLET, BG, 10, sw=2) + text(782, 345, "내려받은 곳이 아니라", 15, VIOLET, 700) + text(782, 366, "내 주방에서 실행돼요" if daily else "브라우저에서 실행돼요", 15, VIOLET, 700), 3, 3),
             a.vis(arrow(335, 245, 380, GREEN, 4) + pill(290, 415, "그림 같은 자원도 요청해요" if not daily else "사진도 따로 주문해요", GREEN, 15), 4, 4)]
    if daily:
        t, sub = "배달된 재료를 내 주방에서", "읽고, 입히고, 완성하고, 움직여요"
        caps = ["업체가 레시피, 플레이팅 규칙, 반응 지침을 보내요", "내 주방에서 레시피를 읽고 규칙대로 접시를 완성해요", "반응 지침도 받은 곳이 아니라 내 주방에서 실행돼요", "사진 같은 자원은 따로 주문할 수 있어요"]
    else:
        t, sub = "브라우저가 읽고 그리고 실행해요", "다운로드한 곳과 실행되는 곳은 달라요"
        caps = ["서버가 HTML, CSS, JavaScript 자원을 보내요", "브라우저가 HTML을 읽고 CSS를 적용해 화면을 그려요", "JavaScript는 서버가 아니라 브라우저에서 실행돼요", "이미지 같은 외부 자원도 브라우저가 요청해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: GET vs POST ----------
def page5(daily):
    a = Anim(4, dur(daily))
    L, R = 170, 790
    body = [lanes(L, R, "나" if daily else "브라우저", "우체국" if daily else "서버"),
            a.vis(msg(L, R, 195, "조회 창구: 목록을 보여 주세요" if daily else "GET /items", BLUE) + msg(R, L, 240, "서류를 받아요" if daily else "응답: 문서", BLUE), 1, 4),
            a.vis(msg(L, R, 305, "접수 창구: 내가 쓴 서류를 낼게요" if daily else "POST /login + 입력 내용", ORANGE), 2, 4),
            a.vis(box(560, 330, 380, 56, GREEN, PANEL, 10, sw=2) + text(750, 365, "서류를 확인해 처리해요" if daily else "서버가 입력을 확인해 처리해요", 16, GREEN, 700), 3, 4),
            a.vis(msg(R, L, 415, "결과: 승인 또는 반려" if daily else "결과: 성공 화면 또는 오류 안내", GREEN), 4, 4)]
    if daily:
        t, sub = "조회 창구와 접수 창구", "보기만 하는 일과 내가 낸 서류를 처리하는 일이에요"
        caps = ["조회 창구에서는 목록을 보여 달라고 해요", "접수 창구에서는 내가 쓴 서류를 내요", "우체국이 서류를 확인해 처리해요", "결과를 승인이나 반려로 알려 줘요"]
    else:
        t, sub = "GET은 가져오기, POST는 제출", "정확한 처리는 서버가 정해요"
        caps = ["GET 요청은 문서를 가져올 때 흔히 써요", "POST 요청은 입력한 자료를 제출할 때 흔히 써요", "서버가 입력을 확인해 처리해요", "결과로 성공 화면이나 오류 안내가 돌아와요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: stateless, then cookie ----------
def page6(daily):
    a = Anim(4, dur(daily))
    if daily:
        cli, srv = person(110, 290, "손님"), person(850, 290, "가게 직원")
        card = lambda lab, c: box(330, 215, 300, 90, c, PANEL, 12, sw=3) + text(480, 268, lab, 18, c, 700)
        body = [cli, srv,
                a.vis(msg(170, 790, 215, "“로그인했어요”", BLUE) + text(480, 340, "직원은 손님을 확인하고 기록 없이 보내요", 17, MUTED, 700), 1, 1),
                a.vis(msg(170, 790, 215, "“지난번에 왔어요”", BLUE) + ask(850, 215) + text(480, 340, "기록이 없어서 알아보지 못해요", 18, ORANGE, 700), 2, 2),
                a.vis(msg(790, 170, 215, "보관증을 건네요", GREEN) + card("보관증(번호표)", GREEN) + text(480, 340, "손님이 지갑에 보관해요", 17, GREEN, 700), 3, 3),
                a.vis(msg(170, 790, 215, "“보관증 여기 있어요”", BLUE) + card("보관증(번호표)", GREEN) + text(480, 340, "보관증으로 손님을 구별해요", 18, GREEN, 700), 4, 4)]
        t, sub = "기록하지 않는 가게", "보관증이 있으면 손님을 구별할 수 있어요"
        caps = ["손님이 처음 방문해 이름을 대요", "다음 방문에서는 직원이 손님을 알아보지 못해요", "가게가 보관증을 건네 손님이 보관해요", "보관증을 보여 주면 손님을 구별할 수 있어요"]
        return frame(a, t, sub, caps, "".join(body))
    B, S = 170, 790
    body = [lanes(B, S, "브라우저", "서버"),
            a.vis(msg(B, S, 195, "POST /login", BLUE) + msg(S, B, 245, "로그인 확인", GREEN), 1, 1),
            a.vis(msg(B, S, 195, "GET /next", BLUE) + ask(S, 250) + text(480, 275, "이전 요청의 내용이 자동으로 붙지 않아요", 17, ORANGE, 700)
                  + box(170, 360, 620, 50, MUTED, PANEL, 8, sw=2) + text(480, 392, "TCP 연결이 이어져 있어도 HTTP가 기억하는 것은 아니에요", 16, MUTED, 700), 2, 2),
            a.vis(msg(S, B, 195, "Set-Cookie: (식별 표식)", GREEN) + box(60, 250, 220, 50, GREEN, PANEL, 8, sw=2) + text(170, 282, "브라우저가 보관", 16, GREEN, 700), 3, 3),
            a.vis(msg(B, S, 195, "Cookie: (식별 표식)", BLUE) + box(500, 250, 290, 56, GREEN, PANEL, 8, sw=2) + text(645, 284, "표식으로 요청을 구별해요", 16, GREEN, 700), 4, 4)]
    t, sub = "HTTP는 요청을 자동으로 기억하지 않아요", "쿠키는 브라우저가 보내는 표식이에요"
    caps = ["로그인 요청을 보내고 서버가 확인해요", "다음 요청에는 앞의 내용이 자동으로 붙지 않아요", "서버가 Set-Cookie로 표식을 저장하라고 해요", "브라우저가 다음 요청에 Cookie를 실어 보내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: session ID ----------
def page7(daily):
    a = Anim(4, dur(daily))
    B, S = 150, 560
    table = lambda hi: (box(650, 200, 280, 140, GREEN, PANEL, 10, sw=3) + text(790, 228, "회원 장부" if daily else "세션 저장소", 16, GREEN, 700)
                        + text(670, 268, "번호표 a1b2c3" if daily else "세션 ID a1b2c3", 15, MUTED, anchor="start")
                        + text(670, 296, "→ 로그인 확인함", 15, TXT, 600, "start")
                        + (hl(655, 250, 270, 56, ORANGE, 8) if hi else ""))
    jar = box(40, 270, 215, 56, BLUE, PANEL, 8, sw=2) + text(147, 296, "쿠키(보관)" if not daily else "번호표(보관)", 15, BLUE, 700) + text(147, 316, "a1b2c3", 15, TXT, 600)
    body = [lanes(B, S, "손님" if daily else "브라우저", "가게" if daily else "서버"),
            a.vis(msg(B, S, 195, "로그인 요청" if not daily else "“로그인할게요”", BLUE) + text(S - 5, 250, "자격을 확인해요", 16, GREEN, 700), 1, 1),
            a.vis(msg(S, B, 195, "번호표를 건네요" if daily else "Set-Cookie: 세션 ID", GREEN) + table(False) + jar
                  + pill(790, 365, "장부에 기록: 세션 생성" if daily else "서버가 세션 생성", GREEN, 15, True, 240), 2, 2),
            a.vis(msg(B, S, 195, "번호표를 보여 줘요" if daily else "Cookie: 세션 ID", BLUE) + table(False) + jar, 3, 3),
            a.vis(msg(S, B, 195, "확인됐어요" if daily else "응답", GREEN) + table(True) + jar + pill(790, 365, "번호로 장부를 찾아요" if daily else "ID로 세션을 찾아요", ORANGE, 15, True, 240)
                  + text(480, 468, "쿠키는 브라우저가 보내는 표식, 세션은 서버가 보관하는 상태" if not daily else "번호표는 손님이 가진 표식, 장부는 가게가 보관하는 기록", 15, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "번호표와 회원 장부", "번호표로 가게의 장부를 찾아요"
        caps = ["손님이 로그인하면 가게가 자격을 확인해요", "가게가 장부에 기록하고 번호표를 건네요", "다음에 손님이 번호표를 보여 줘요", "가게가 번호표로 장부를 찾아 확인해요"]
    else:
        t, sub = "세션 ID로 로그인 상태 잇기", "쿠키는 표식, 세션은 서버가 보관하는 상태예요"
        caps = ["로그인 요청이 오면 서버가 자격을 확인해요", "서버가 세션을 만들고 ID를 쿠키로 전달해요", "브라우저가 다음 요청에 세션 ID를 보내요", "서버가 ID로 자신이 보관한 세션을 찾아 확인해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: WAS asks the DB ----------
def page8(daily):
    a = Anim(4, dur(daily))
    names = ["손님", "접수 창구", "담당 직원", "회원 장부실"] if daily else ["브라우저", "웹 서버", "WAS", "DB"]
    cols = [BLUE, GREEN, ORANGE, VIOLET]
    xs = [40, 270, 500, 730]
    body = [role(x, 175, 150, 70, n, "", c, 18) for x, n, c in zip(xs, names, cols)]
    tbl = (box(580, 335, 350, 100, VIOLET, PANEL, 10, sw=2)
           + "".join(text(x, 365, h, 14, MUTED, 600, "start") for x, h in zip((598, 700, 830), (("이름", "확인 정보", "상태") if daily else ("사용자 ID", "비밀번호 확인값", "계정 상태"))))
           + "".join(text(x, 400, v, 14, TXT, 600, "start") for x, v in zip((598, 700, 830), (("tester", "(원본이 아닌 표시)", "사용 중") if daily else ("tester", "(원문이 아닌 값)", "사용 중")))))
    body += [tbl,
             a.vis(msg(190, 270, 195, "신청서" if daily else "요청", BLUE, 13) + msg(420, 500, 195, "전달" if daily else "넘김", GREEN, 13), 1, 4),
             a.vis(msg(650, 730, 195, "있나요?" if daily else "계정 조회", ORANGE, 13) + hl(580, 335, 350, 100, VIOLET, 10), 2, 2),
             a.vis(msg(730, 650, 230, "결과" if daily else "결과", VIOLET, 13), 3, 3),
             a.vis(arrow(570, 120, 300, ORANGE, 5) + text(345, 288, "성공 또는 실패 응답" if not daily else "승인 또는 안내", 15, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "담당 직원이 장부에 물어봐요", "접수한 신청서는 장부 확인을 거쳐요"
        caps = ["손님의 신청서가 접수 창구를 거쳐 담당 직원에게 가요", "담당 직원이 장부실에 이름이 있는지 물어봐요", "장부실이 있는지 없는지를 알려 줘요", "담당 직원이 결과를 정리해 손님에게 돌려줘요"]
    else:
        t, sub = "WAS가 DB에 묻고 응답을 만들어요", "DB는 계정 같은 자료를 저장하고 조회해요"
        caps = ["로그인 요청이 웹 서버를 거쳐 WAS에 넘어가요", "WAS가 DB에 계정 정보를 조회해요", "DB가 계정 정보나 없음을 돌려줘요", "WAS가 성공 또는 실패 응답을 만들어 돌려보내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: roles vs machines ----------
def page9(daily):
    a = Anim(4, dur(daily))
    names = ["손님", "홀", "주방", "창고"] if daily else ["브라우저", "웹 서버", "WAS", "DB"]
    subs = ["", "주문을 받아요", "요리를 만들어요", "재료를 보관해요"] if daily else ["", "요청 접수·정적 파일", "처리·응답 만들기", "자료 저장·조회"]
    cols = [BLUE, GREEN, ORANGE, VIOLET]
    xs = [40, 270, 500, 730]
    top = "".join(role(x, 140, 170, 80, n, s, c, 18) for x, n, s, c in zip(xs, names, subs, cols))
    one = (box(250, 285, 470, 110, GREEN, PANEL, 14, dash=True, sw=3) + text(485, 313, "서버 한 대" if not daily else "한 사람이 겸임", 17, GREEN, 700)
           + "".join(cell(270 + i * 150, 335, 135, 40, n, c, 15) for i, (n, c) in enumerate(zip(names[1:], cols[1:]))))
    many = "".join(box(150 + i * 250, 285, 200, 110, c, PANEL, 14, dash=True, sw=3) + text(250 + i * 250, 320, ["서버 A", "서버 B", "서버 C"][i] if not daily else ["홀 담당", "주방 담당", "창고 담당"][i], 17, c, 700)
                   + text(250 + i * 250, 360, n, 16, TXT, 600) for i, (n, c) in enumerate(zip(names[1:], cols[1:])))
    body = [top,
            a.vis(arrow(210, 270, 180, MUTED, 3) + arrow(440, 500, 180, MUTED, 3) + arrow(670, 730, 180, MUTED, 3), 1, 4),
            a.vis(pill(355, 255, "정적 파일은 바로 보내요" if not daily else "메뉴판은 바로 줘요", ORANGE, 15, True)
                  + pill(700, 255, "처리가 필요하면 WAS → DB로" if not daily else "요리는 주방 → 창고로", GREEN, 15, True), 2, 2),
            a.vis(one + pill(485, 440, "작은 서비스는 한 곳에서 여러 역할을 맡기도 해요", GREEN, 16, True), 3, 3),
            a.vis(many + pill(485, 440, "서비스가 커지면 역할별로 나눌 수 있어요", ORANGE, 16, True), 4, 4)]
    if daily:
        t, sub = "홀, 주방, 창고의 역할", "한 사람이 겸임할 수도 있고 나눌 수도 있어요"
        caps = ["손님 주문은 홀이 받고 주방과 창고가 도와요", "메뉴판은 홀이 바로 주고 요리는 주방이 만들어요", "작은 가게는 한 사람이 여러 일을 맡아요", "큰 가게는 역할마다 담당을 나눠요"]
    else:
        t, sub = "역할 구분과 장비 수는 달라요", "웹 서버·WAS·DB는 논리적인 역할이에요"
        caps = ["웹 서버는 접수, WAS는 처리, DB는 저장을 맡아요", "정적 파일은 웹 서버가, 처리는 WAS와 DB가 맡아요", "작은 서비스는 한 서버에서 여러 역할을 맡을 수 있어요", "서비스가 커지면 여러 장비나 가상 서버로 나눌 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l35-daily-letter-and-envelope", "l35-http-over-tcpip", page1, 3),
    ("l35-daily-call-a-friend", "l35-dns-tcp-get-response", page2, 3),
    ("l35-daily-menu-content-style", "l35-html-content-css-style", page3, 2),
    ("l35-daily-kitchen-delivery", "l35-browser-render-js-runs-here", page4, 1),
    ("l35-daily-two-counters", "l35-get-vs-post", page5, 2),
    ("l35-daily-shop-keeps-no-record", "l35-stateless-then-cookie", page6, 4),
    ("l35-daily-ticket-and-ledger", "l35-session-id-cookie", page7, 1),
    ("l35-daily-clerk-asks-ledger", "l35-was-asks-db", page8, 2),
    ("l35-daily-hall-kitchen-storage", "l35-roles-vs-machines", page9, 2),
]

COPY = {
    "l35-daily-letter-and-envelope": ("편지의 내용과 봉투",
        "나와 가게 사이에서 로그인 화면을 달라는 편지의 내용이 먼저 쓰이고, 봉투에 담겨 우체국을 지나 가게에 도착하며, 가게가 내용을 읽고 답장을 보냅니다. 내용을 쓰는 일과 나르는 일은 다르다고 표시됩니다.",
        "편지의 내용과 봉투가 다르듯, HTTP 요청의 의미와 그것을 전달하는 네트워크의 역할은 서로 다른 층에 있습니다."),
    "l35-http-over-tcpip": ("HTTP 요청과 TCP/IP 전달",
        "브라우저가 GET /login 요청을 만들고, TCP/IP가 그 요청을 데이터로 감싸 네트워크를 지나 서버에 전달하며, 서버가 요청을 읽고 응답을 돌려보냅니다. 요청의 의미(HTTP)와 전달(TCP/IP)은 서로 다른 층이라고 표시됩니다.",
        "HTTP는 요청과 응답의 규칙이고 TCP/IP는 데이터를 전달합니다. 서버에 도착한 뒤의 웹 서버, WAS, DB 구조는 이어지는 페이지에서 살펴봅니다.", 3),
    "l35-daily-call-a-friend": ("친구에게 전화하는 네 걸음",
        "나와 친구 사이에서 먼저 연락처에서 친구 이름에 맞는 전화번호를 찾고, 전화를 걸어 대표번호와 내선 번호로 통로를 잇고, 필요한 말을 건네고, 친구의 대답을 듣습니다.",
        "연락처에서 번호를 찾고, 연결하고, 말을 건네고, 대답을 듣는 것은 웹 접속의 네 걸음과 닮았습니다."),
    "l35-dns-tcp-get-response": ("이름 찾기, 연결, 요청, 응답",
        "브라우저가 DNS에 shop.example의 IP 주소를 묻고 예시 주소 203.0.113.10을 받은 뒤, 웹 서버와 IP 주소와 포트로 TCP 연결을 준비하고, GET /login 요청을 보내면 서버가 상태 코드와 헤더와 HTML 본문이 담긴 응답을 돌려줍니다.",
        "DNS가 돌려주는 것은 서버를 찾을 주소이고, 이어서 연결 준비, 요청, 응답이 서로 다른 일로 이어집니다. 주소와 포트 번호는 예시입니다.", 3),
    "l35-daily-menu-content-style": ("메뉴판의 내용과 모양",
        "메뉴판에 음식 이름과 가격이 적혀 있고, 모양 규칙 A를 입히면 제목이 크고 빨갛게 보이며, 모양 규칙 B로 바꿔도 내용은 그대로이고, 모양만으로 없던 메뉴가 생기지는 않는다고 표시됩니다.",
        "같은 메뉴판 내용도 모양 규칙에 따라 다르게 보일 수 있지만, 모양만으로 없던 내용이 생기지는 않습니다."),
    "l35-html-content-css-style": ("HTML은 구조, CSS는 모양",
        "같은 HTML의 제목과 링크에 CSS A를 적용하면 제목이 크고 파랗게, CSS B를 적용하면 작고 검게 보입니다. 내용과 링크는 그대로이며 CSS만으로 없던 상품 정보가 생기지는 않는다고 표시됩니다.",
        "HTML은 문서의 구조와 내용을, CSS는 그 구조를 표현하는 모양을 맡습니다. 그림의 색과 크기는 예시입니다.", 2),
    "l35-daily-kitchen-delivery": ("배달된 재료를 내 주방에서",
        "재료 업체가 레시피 카드, 플레이팅 규칙, 반응 지침을 내 주방으로 보내고, 내 주방에서 레시피를 읽고 규칙대로 접시를 완성하며, 호출벨을 누르면 안내하는 반응 지침도 받은 곳이 아니라 내 주방에서 실행됩니다. 사진 같은 자원은 따로 주문할 수 있습니다.",
        "받은 자원을 읽고 모양을 입히고 실행하는 일은 모두 내 주방에서 일어납니다. 다운로드한 곳과 실행되는 곳은 다릅니다."),
    "l35-browser-render-js-runs-here": ("브라우저가 읽고 그리고 실행해요",
        "서버가 HTML, CSS, JavaScript를 보내면 브라우저가 HTML을 읽고 CSS를 적용해 화면을 그리고(렌더링), 버튼을 누르면 JavaScript가 서버가 아닌 브라우저에서 실행되어 안내 문구를 보여 줍니다. 이미지 같은 외부 자원도 브라우저가 요청합니다.",
        "JavaScript를 서버에서 내려받았다는 사실만으로 그 코드가 서버에서 실행되는 것은 아닙니다. 다운로드한 곳과 실행되는 곳은 구별해야 합니다.", 1),
    "l35-daily-two-counters": ("조회 창구와 접수 창구",
        "나는 조회 창구에서 목록을 보여 달라고 하여 서류를 받고, 접수 창구에서는 내가 쓴 서류를 내면 우체국이 확인해 처리한 뒤 승인 또는 반려를 알려 줍니다.",
        "목록을 보는 일과 내가 쓴 서류를 내서 처리하는 일은 다르며, 어떻게 처리할지는 받는 쪽이 정합니다."),
    "l35-get-vs-post": ("GET은 가져오기, POST는 제출",
        "브라우저가 GET /items로 문서를 가져오고, POST /login으로 입력 내용을 제출하면 서버가 입력을 확인해 처리한 뒤 성공 화면이나 오류 안내를 응답합니다.",
        "GET은 자료를 가져올 때, POST는 자료를 제출하거나 처리를 요청할 때 흔히 쓰이며 정확한 동작은 서버가 정합니다.", 2),
    "l35-daily-shop-keeps-no-record": ("기록하지 않는 가게",
        "손님이 처음 방문해 로그인했다고 말해도 가게는 기록을 남기지 않아 다음 방문에서는 알아보지 못합니다. 가게가 보관증을 건네고 손님이 보관해 두었다가 보여 주면 손님을 구별할 수 있습니다.",
        "기록을 남기지 않는 가게는 손님을 알아보지 못하지만, 보관증이 있으면 구별할 수 있습니다."),
    "l35-stateless-then-cookie": ("HTTP는 요청을 자동으로 기억하지 않아요",
        "브라우저가 POST /login으로 로그인하고 서버가 확인하지만, 다음 GET /next 요청에는 앞의 내용이 자동으로 붙지 않아 서버가 요청을 구별하지 못합니다. TCP 연결이 이어져 있어도 HTTP가 기억하는 것은 아닙니다. 서버가 Set-Cookie로 식별 표식을 저장하라고 하면 브라우저가 보관했다가 이후 요청의 Cookie 헤더에 실어 보냅니다.",
        "HTTP는 요청 사이의 기억을 자동으로 보존하지 않으며, 쿠키는 브라우저가 저장해 요청에 실어 보내는 표식입니다.", 4),
    "l35-daily-ticket-and-ledger": ("번호표와 회원 장부",
        "손님이 로그인하면 가게가 자격을 확인하고 장부에 기록한 뒤 번호표를 건네며, 다음에 손님이 번호표를 보여 주면 가게가 번호표로 회원 장부를 찾아 확인합니다. 번호표는 손님이 가진 표식이고 장부는 가게가 보관하는 기록입니다.",
        "번호표는 손님이 가진 표식이고 장부는 가게가 보관하는 기록이라는 점에서 쿠키와 세션에 대응합니다."),
    "l35-session-id-cookie": ("세션 ID로 로그인 상태 잇기",
        "로그인 요청이 오면 서버가 자격을 확인해 세션을 만들고 세션 ID를 Set-Cookie로 전달하며, 브라우저가 이후 요청의 Cookie에 세션 ID를 실어 보내면 서버가 ID로 자신이 보관한 세션을 찾아 응답합니다. 쿠키는 브라우저가 보내는 표식이고 세션은 서버가 보관하는 상태입니다. 세션 ID a1b2c3은 예시입니다.",
        "쿠키는 브라우저가 보내는 표식이고, 세션은 서버가 보관하는 로그인 상태입니다. 세션 ID 값은 예시입니다.", 1),
    "l35-daily-clerk-asks-ledger": ("담당 직원이 장부에 물어봐요",
        "손님의 신청서가 접수 창구를 거쳐 담당 직원에게 가고, 담당 직원이 회원 장부실에 이름이 있는지 물어 있음 또는 없음을 듣고, 결과를 손님에게 돌려줍니다.",
        "신청서는 접수 창구와 담당 직원을 거쳐 장부 확인을 마친 뒤 결과로 돌아옵니다."),
    "l35-was-asks-db": ("WAS가 DB에 묻고 응답을 만들어요",
        "브라우저의 로그인 요청이 웹 서버를 거쳐 WAS에 넘어가고, WAS가 DB의 users 표에서 계정 정보를 조회하면 DB가 계정 정보나 없음을 돌려주며, WAS가 성공 또는 실패 응답을 만들어 웹 서버와 네트워크를 거쳐 돌려보냅니다. DB에는 비밀번호 원문이 아닌 확인값이 보관됩니다.",
        "웹 서버가 요청을 접수해 WAS에 넘기면 WAS가 DB에서 필요한 계정 정보를 조회하고 응답을 만듭니다. 표의 값은 예시입니다.", 2),
    "l35-daily-hall-kitchen-storage": ("홀, 주방, 창고의 역할",
        "손님의 주문을 홀이 받고, 메뉴판은 홀이 바로 주지만 요리는 주방이 창고의 재료로 만들며, 작은 가게는 한 사람이 여러 일을 맡고 큰 가게는 역할마다 담당을 나눈다고 표시됩니다.",
        "역할을 나누는 것과 사람 수는 별개입니다. 작은 가게는 한 사람이 여러 일을 맡을 수 있습니다."),
    "l35-roles-vs-machines": ("역할 구분과 장비 수는 달라요",
        "웹 서버는 접수와 정적 파일, WAS는 처리와 응답 만들기, DB는 자료 저장과 조회를 맡습니다. 정적 파일은 웹 서버가 바로 보내고 처리가 필요하면 WAS와 DB가 맡으며, 작은 서비스는 한 서버에서 여러 역할을 맡고 서비스가 커지면 여러 장비나 가상 서버로 나눌 수 있습니다.",
        "논리적인 역할 구분과 물리적인 장비 개수는 같은 말이 아닙니다. 모든 웹 서비스가 서로 다른 컴퓨터 세 대를 쓰는 것은 아닙니다.", 2),
}


def add_illustrations(lesson_md, pages):
    """Add (or refresh) an `illustrations:` key on each Page without touching `animations:` or anything else."""
    import json
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(("- terms:", "- page_id:"))]
    assert len(starts) == len(pages), f"page count {len(starts)} != {len(pages)}"
    end_fm = next((i for i, l in enumerate(lines) if i > starts[-1] and l and not l.startswith(" ") and not l.startswith("- ")), len(lines))
    bounds = starts + [end_fm]
    out = lines[:starts[0]]
    for p, items in enumerate(pages):
        seg = lines[bounds[p]:bounds[p + 1]]
        # drop any previous generated illustrations block
        clean, i = [], 0
        while i < len(seg):
            if seg[i] == "  illustrations:":
                i += 1
                while i < len(seg) and seg[i].startswith(("  - file:", "    ")):
                    i += 1
                continue
            clean.append(seg[i]); i += 1
        while clean and clean[-1] == "":
            clean.pop()
        block = ["  illustrations:"]
        for f, t, al, c, ap in items:
            block += [f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
        out += clean + block
    out += lines[end_fm:]
    text_ = "\n".join(out)
    if not text_.endswith("\n"):
        text_ += "\n"
    Path(lesson_md).write_text(head + "---\n" + text_ + "---\n" + body, encoding="utf-8")


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        d, n = COPY[dn], COPY[nn]
        pages.append([(dn, d[0], d[1], d[2], -1), (nn, n[0], n[1], n[2], n[3])])
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        add_illustrations(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
