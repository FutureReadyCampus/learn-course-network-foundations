#!/usr/bin/env python3
"""Unit 9 Lesson 4 (HTTP basics) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u9_l04.py   (add --svg-only to skip the lesson.md edit).

Every page gets a daily-life SVG at the top (after_paragraph -1) and a network SVG with the same layout after the
explanatory paragraph. Network scenes use the lesson's one example (GET /example-page, Host: www.example.com);
daily scenes use one matching snack-shop order. The existing wiki `animations:` entries (pages 1, 3) are left as
they are; the new items go into a separate `illustrations:` key on each page."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, person, dur
from u7_l01 import mv
from u10_l01 import role, msg, add_illustrations
from u9_l02 import doc

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/04-*"))
OUT = LESSON / "assets" / "animations"


def ends(daily, ly=290):
    """Client on the left, server on the right."""
    return ((person(110, ly - 10, "손님") if daily else laptop(110, ly, "브라우저"))
            + (house(850, ly - 20, "한빛분식") if daily else pc(850, ly, "서버")))


def card(x, y, w, rows, c, title=None, rh=34):
    """Message card: rows = [(text, colour)], an empty text draws the blank line. Returns (svg, row_top_ys)."""
    top = y + (34 if title else 10)
    h = top - y + rh * len(rows) + 10
    s = box(x, y, w, h, c, PANEL, 10, sw=3) + (text(x + 16, y + 24, title, 15, c, 700, "start") if title else "")
    ys = []
    for i, (t, tc) in enumerate(rows):
        ry = top + i * rh
        ys.append(ry)
        s += (text(x + 16, ry + 23, t, 16, tc, 700, "start") if t
              else line(x + 16, ry + rh / 2, x + w - 16, ry + rh / 2, LINE, 2, "4 6"))
    return s, ys


def rowhl(x, w, ry, c, rh=34):
    return hl(x + 6, ry + 2, w - 12, rh - 4, c, 6)


# ---------- Page 1: HTTP is the request/response promise; TCP carries a stream ----------
def page1(daily):
    a = Anim(4, dur(daily))
    chunks = "".join(box(200 + i * 70, 400, 56, 30, LINE, BG, 4, sw=2) for i in range(8))
    body = [ends(daily),
            box(180, 390, 600, 50, GREEN, PANEL, 10, sw=3) + chunks,
            text(480, 465, "배달 길: 쉬지 않고 이어지는 짐 흐름" if daily else "TCP/IP: 데이터를 이어진 흐름(stream)으로 옮겨요", 15, GREEN, 700),
            a.vis(hl(60, 230, 110, 140, BLUE, 12) + hl(800, 230, 100, 140, BLUE, 12), 1, 1),
            a.vis(msg(170, 790, 200, "주문서 양식대로 주문" if daily else "HTTP 요청", BLUE), 2, 4),
            a.vis(msg(790, 170, 255, "약속대로 음식" if daily else "HTTP 응답", ORANGE), 2, 4),
            a.vis(hl(180, 390, 600, 50, GREEN, 10), 3, 3),
            mv(a, box(-28, -15, 56, 30, ORANGE, ORANGE, 4), [(228, 415), (718, 415)], 3, 3, 3, 0.1, 0.8),
            a.vis("".join(line(x, 385, x, 445, ORANGE, 5) for x in (195, 475, 765))
                  + pill(335, 360, "주문 1" if daily else "요청 1", ORANGE, 14, True) + pill(620, 360, "주문 2" if daily else "요청 2", ORANGE, 14, True), 4, 4)]
    if daily:
        t, sub = "주문서 약속과 배달 길", "주문하는 약속과 나르는 길은 서로 달라요"
        caps = ["손님과 분식집이 주문을 주고받아요", "손님은 약속된 주문서로 주문하고 가게가 답해요", "나르는 일은 배달 길이 이어진 흐름으로 맡아요", "주문서 양식 덕분에 주문 하나하나를 나눠 읽어요"]
    else:
        t, sub = "HTTP와 TCP/IP의 역할", "HTTP는 메시지 약속, TCP/IP는 데이터 전달이에요"
        caps = ["브라우저는 클라이언트, 요청을 받는 쪽은 서버예요", "HTTP 규칙에 따라 요청하고 응답해요", "TCP/IP는 데이터를 이어진 흐름으로 옮겨요", "HTTP 규칙에 맞춰 흐름 속 메시지 경계를 나눠요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: start-line, header, blank line, body ----------
def page2(daily):
    a = Anim(4, dur(daily))
    if daily:
        req = [("포장 주문: 떡볶이 1인분", BLUE), ("가게: 한빛분식", GREEN)]
        res = [("주문 완료 (성공)", BLUE), ("내용물: 떡볶이", GREEN), ("", MUTED), ("떡볶이 1인분이 담긴 상자", ORANGE)]
    else:
        req = [("GET /example-page HTTP/1.1", BLUE), ("Host: www.example.com", GREEN)]
        res = [("HTTP/1.1 200 OK", BLUE), ("Content-Type: text/html; charset=utf-8", GREEN), ("", MUTED), ("<h1>안녕, 웹!</h1>", ORANGE)]
    L, LW, R, RW = 40, 380, 450, 470
    qs, qy = card(L, 140, LW, req, BLUE, "주문서" if daily else "요청 (Request)")
    rs, ry = card(R, 140, RW, res, ORANGE, "답과 음식" if daily else "응답 (Response)")
    tag = lambda y, s, c: pill(L + LW / 2, y, s, c, 15, True)
    body = [qs, rs,
            a.vis(rowhl(L, LW, qy[0], BLUE) + rowhl(R, RW, ry[0], BLUE) + tag(330, "첫 줄: 무엇을 / 결과 요약" if daily else "첫 줄(start-line): 요청·결과 요약", BLUE), 1, 1),
            a.vis(rowhl(L, LW, qy[1], GREEN) + rowhl(R, RW, ry[1], GREEN) + tag(330, "헤더: 덧붙이는 정보", GREEN), 2, 2),
            a.vis(rowhl(R, RW, ry[2], MUTED) + tag(330, "빈 줄: 여기서부터 본문이에요", MUTED), 3, 3),
            a.vis(rowhl(R, RW, ry[3], ORANGE) + tag(330, "본문(body): 실제로 주는 내용", ORANGE), 4, 4),
            a.vis(text(480, 420, "첫 줄 → 헤더 → 빈 줄 → 본문 순서로 읽어요", 17, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "주문서와 답을 줄마다 읽어요", "첫 줄, 덧붙인 정보, 빈 줄, 내용 순서예요"
        caps = ["첫 줄은 무엇을 주문했는지, 결과는 어땠는지 요약해요", "다음 줄들은 가게 이름 같은 덧붙인 정보예요", "빈 줄 하나가 여기부터 내용이라고 알려 줘요", "마지막이 실제로 받는 음식이에요"]
    else:
        t, sub = "HTTP 메시지의 모양", "첫 줄, 헤더, 빈 줄, 본문 순서로 읽어요"
        caps = ["첫 줄은 GET 요청, 200 OK 결과를 요약해요", "Host, Content-Type 같은 헤더가 정보를 더해요", "빈 줄이 헤더가 끝나고 본문이 시작된다고 알려요", "본문에는 실제 HTML 내용이 들어 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: one page, many requests ----------
def page3(daily):
    a = Anim(4, dur(daily))
    extra = ["단무지 주세요", "음료 주세요", "수저 주세요"] if daily else ["GET /logo.png", "GET /style.css", "GET /app.js"]
    body = [ends(daily),
            a.vis(msg(170, 790, 170, "떡볶이 주세요" if daily else "Request: GET /example-page HTTP/1.1", BLUE, 15), 1, 4),
            a.vis(msg(790, 170, 220, "주문 완료 + 떡볶이" if daily else "Response: HTTP/1.1 200 OK + HTML", ORANGE, 15), 2, 4),
            a.vis(text(480, 260, "요청은 손님 → 가게, 응답은 가게 → 손님" if daily else "Request는 클라이언트 → 서버, Response는 서버 → 클라이언트", 15, MUTED, 700), 2, 2)]
    for i, s in enumerate(extra):
        y = 300 + i * 45
        body.append(a.vis(arrow(180, 400, y, VIOLET, 3) + text(290, y - 8, s, 14, VIOLET, 700)
                          + arrow(780, 560, y, GREEN, 3) + text(670, y - 8, "응답", 14, GREEN, 700), 3, 4))
    body.append(a.vis(pill(480, 455, "가게에 한 번 가도 주문은 여러 번이에요" if daily else "페이지 하나에도 요청이 여러 번 생겨요", ORANGE, 17, True), 4, 4))
    if daily:
        t, sub = "주문하면 가게가 답해요", "한 번 방문에도 주문은 여러 번일 수 있어요"
        caps = ["손님이 가게에 떡볶이를 주문해요", "가게가 주문을 처리해 떡볶이를 내줘요", "단무지, 음료, 수저도 따로따로 부탁해요", "한 번 방문에도 주문과 답이 여러 번 오가요"]
    else:
        t, sub = "Request와 Response", "페이지 하나에도 요청이 여러 번 생길 수 있어요"
        caps = ["브라우저가 GET /example-page 요청을 보내요", "서버가 200 OK와 HTML 문서로 응답해요", "이미지, CSS, JavaScript도 각각 요청해요", "페이지 하나에도 메시지가 여러 번 오가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: DevTools Network tab ----------
def page4(daily):
    a = Anim(4, dur(daily))
    rows = ([("떡볶이", "완료"), ("단무지", "완료"), ("음료", "완료"), ("수저", "완료")] if daily else
            [("example-page", "200"), ("logo.png", "200"), ("style.css", "200"), ("app.js", "200")])
    panel = box(40, 130, 420, 330, LINE, PANEL, 12, sw=3) + text(60, 158, "내 주문 내역" if daily else "개발자 도구 · Network", 16, MUTED, 700, "start")
    for i, (n, st) in enumerate(rows):
        y = 175 + i * 50
        panel += box(60, y, 380, 40, LINE, BG, 6, sw=2) + text(76, y + 26, n, 16, TXT, 700, "start") + text(420, y + 26, st, 16, GREEN, 700, "end")
    det = ([("주문 종류: 포장 주문", BLUE), ("결과: 주문 완료", GREEN), ("메모: 덜 맵게", VIOLET), ("받은 것: 떡볶이 1인분", ORANGE)] if daily else
           [("Method: GET", BLUE), ("Status: 200 OK", GREEN), ("Request Headers: Host …", VIOLET), ("Response: HTML 본문", ORANGE)])
    ds, _ = card(500, 175, 420, det, BLUE, "자세히 보기" if daily else "선택한 요청의 자세한 정보")
    body = [panel,
            a.vis(hl(40, 130, 420, 330, BLUE, 12), 1, 1),
            a.vis(hl(60, 175, 380, 40, ORANGE, 6), 2, 4),
            a.vis(ds + arrow(445, 495, 195, ORANGE, 3), 3, 4),
            a.vis(pill(710, 420, "내 주문 내역만 봐요" if daily else "내가 연 페이지의 요청만 봐요", GREEN, 16, True)
                  + text(710, 455, "남의 주문을 몰래 엿보지 않아요" if daily else "다른 사람의 통신은 가로채지 않아요", 15, RED, 700), 4, 4)]
    if daily:
        t, sub = "내 주문 내역 살펴보기", "주문 하나를 누르면 자세한 내용을 볼 수 있어요"
        caps = ["앱의 주문 내역에 내가 한 주문이 모여 있어요", "그중 떡볶이 주문 하나를 골라요", "주문 종류, 결과, 메모, 받은 것을 확인해요", "내 주문만 보고, 남의 주문은 엿보지 않아요"]
    else:
        t, sub = "개발자 도구의 Network 탭", "요청 하나를 고르면 주고받은 내용이 보여요"
        caps = ["Network 탭에 페이지가 불러온 요청이 모여 있어요", "example-page 요청 하나를 골라요", "Method, 상태 코드, 헤더, 본문을 확인해요", "내가 직접 연 페이지의 요청만 살펴봐요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: request headers ----------
def page5(daily):
    a = Anim(4, dur(daily))
    rows = ([("포장 주문: 떡볶이 1인분", MUTED), ("받을 형태: 포장 용기", BLUE), ("원하는 말: 한국어", BLUE),
             ("눌러 담기: 괜찮아요", BLUE), ("주문 기기: 키오스크", VIOLET), ("회원 카드: ●●●●●●", RED)] if daily else
            [("GET /example-page HTTP/1.1", MUTED), ("Accept: text/html", BLUE), ("Accept-Language: ko", BLUE),
             ("Accept-Encoding: gzip", BLUE), ("User-Agent: (브라우저 정보)", VIOLET), ("Cookie: ●●●●●●", RED)])
    X, W = 60, 470
    cs, ys = card(X, 130, W, rows, BLUE, "주문서" if daily else "요청 (Request)", 40)
    notes = (["어떤 형태로 받을지", "어떤 말을 원하는지", "눌러 담아도 되는지"] if daily else
             ["HTML을 받을 수 있어요", "한국어 응답을 원해요", "gzip 압축을 풀 수 있어요"])
    body = [cs, person(820, 290, "손님") if daily else laptop(820, 300, "브라우저")]
    for k, (ry, n) in enumerate(zip(ys[1:4], notes), 1):
        body.append(a.vis(rowhl(X, W, ry, BLUE, 40) + text(560, ry + 26, n, 15, BLUE, 700, "start"), k, k))
    body += [a.vis(rowhl(X, W, ys[4], VIOLET, 40) + rowhl(X, W, ys[5], RED, 40)
                   + text(560, ys[4] + 26, "보낸 프로그램 정보", 15, VIOLET, 700, "start")
                   + text(560, ys[5] + 26, "민감한 값은 가려요", 15, RED, 700, "start"), 4, 4),
             a.vis(text(700, 440, "헤더는 덧붙인 설명, 경로·본문과 달라요" if not daily else "메모는 주문에 덧붙인 설명이에요", 15, MUTED, 700), 3, 4)]
    if daily:
        t, sub = "주문서에 붙이는 메모", "원하는 형태와 필요한 정보를 덧붙여요"
        caps = ["포장 용기에 담아 달라고 적어요", "한국어로 안내해 달라고 적어요", "눌러 담아도 괜찮다고 적어요", "주문 기기와 회원 카드도 적지만 번호는 가려요"]
    else:
        t, sub = "요청 Header", "원하는 형식과 환경을 이름: 값으로 알려요"
        caps = ["Accept: text/html은 HTML을 받을 수 있다고 알려요", "Accept-Language: ko는 한국어를 원한다고 알려요", "Accept-Encoding: gzip은 압축을 풀 수 있다고 알려요", "User-Agent와 Cookie도 담기니 민감한 값은 가려요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: response headers ----------
def page6(daily):
    a = Anim(4, dur(daily))
    rows = ([("주문 완료 (성공)", MUTED), ("내용물: 떡볶이 (매운 음식)", BLUE), ("무게: 500g", GREEN), ("적립: 도장 하나 찍어 두세요", VIOLET),
             ("", MUTED), ("떡볶이 1인분", ORANGE)] if daily else
            [("HTTP/1.1 200 OK", MUTED), ("Content-Type: text/html; charset=utf-8", BLUE), ("Content-Length: 본문 바이트 수", GREEN),
             ("Set-Cookie: ●●●●●●", VIOLET), ("", MUTED), ("<h1>안녕, 웹!</h1>", ORANGE)])
    X, W = 40, 500
    cs, ys = card(X, 130, W, rows, ORANGE, "답과 음식" if daily else "응답 (Response)", 40)
    body = [cs, person(820, 280, "손님") if daily else laptop(820, 290, "브라우저"),
            a.vis(rowhl(X, W, ys[1], BLUE, 40) + rowhl(X, W, ys[5], ORANGE, 40)
                  + text(580, ys[1] + 26, "뒤에 올 내용의 종류", 15, BLUE, 700, "start"), 1, 1),
            a.vis(rowhl(X, W, ys[2], GREEN, 40) + rowhl(X, W, ys[5], ORANGE, 40)
                  + text(580, ys[2] + 26, "내용의 크기" if daily else "본문 크기 (바이트)", 15, GREEN, 700, "start"), 2, 2),
            a.vis(rowhl(X, W, ys[3], VIOLET, 40) + arrow(550, 770, ys[3] + 20, VIOLET, 3)
                  + pill(680, ys[3] - 6, "도장 카드에 저장" if daily else "쿠키 저장", VIOLET, 14, True), 3, 3),
            a.vis(text(700, 430, "설명을 보고 알맞게 먹어요" if daily else "헤더를 참고해 HTML로 처리해요", 16, GREEN, 700)
                  + check(820, 200), 4, 4)]
    if daily:
        t, sub = "음식 상자에 붙은 라벨", "라벨은 내용물과 다루는 법을 알려 줘요"
        caps = ["라벨이 이 상자 안은 떡볶이라고 알려요", "라벨에 내용물의 무게도 적혀 있어요", "가게가 적립 도장을 찍어 두라고 알려요", "손님은 라벨을 보고 음식을 알맞게 다뤄요"]
    else:
        t, sub = "응답 Header", "본문의 형식과 처리 방법을 알려 줘요"
        caps = ["Content-Type이 본문은 HTML이라고 알려요", "Content-Length가 본문 크기를 바이트로 알려요", "Set-Cookie로 브라우저에 쿠키 저장을 알려요", "브라우저는 헤더를 참고해 응답을 처리해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: status codes ----------
def page7(daily):
    a = Anim(4, dur(daily))
    cases = ([("떡볶이 주세요", "주문 완료", GREEN, "성공"), ("떡볶기 주세요", "그런 메뉴는 없어요", ORANGE, "메뉴 이름 오타"),
              ("떡볶이 주세요", "주방 고장으로 못 만들어요", RED, "가게 안 문제")] if daily else
             [("GET /example-page", "200 OK", GREEN, "성공"), ("GET /exmaple-page", "404 Not Found", ORANGE, "주소 오타 · 자원 없음"),
              ("GET /example-page", "500 Internal Server Error", RED, "서버 처리 문제")])
    body = [person(90, 290, "손님") if daily else laptop(90, 300, "브라우저"), house(870, 270, "한빛분식") if daily else pc(870, 300, "서버")]
    for k, (q, r, c, note) in enumerate(cases, 1):
        y = 150 + (k - 1) * 95
        body.append(a.vis(text(480, y + 10, q, 15, BLUE, 700) + arrow(160, 800, y + 20, BLUE, 3)
                          + arrow(800, 160, y + 52, c, 3) + pill(480, y + 52, r, c, 15, True)
                          + text(720, y + 80, note, 14, c, 700), k, 4))
    body.append(a.vis(pill(480, 455, "4xx는 요청 쪽, 5xx는 가게 쪽 단서일 뿐이에요" if daily else "4xx는 요청 쪽, 5xx는 서버 쪽 단서 · 진단서는 아니에요", MUTED, 15, True), 4, 4))
    if daily:
        t, sub = "주문 결과 한마디", "가게의 첫마디가 주문이 어떻게 됐는지 알려 줘요"
        caps = ["떡볶이를 주문하면 주문 완료라고 답해요", "메뉴 이름이 틀리면 그런 메뉴는 없다고 해요", "주방이 고장 나면 만들 수 없다고 해요", "답은 단서일 뿐, 원인을 모두 말하지는 않아요"]
    else:
        t, sub = "상태 코드", "응답 첫 줄의 세 자리 숫자가 처리 결과를 요약해요"
        caps = ["200 OK는 요청을 성공적으로 처리했다는 뜻이에요", "주소 오타로 자원이 없으면 404 Not Found가 와요", "5xx는 서버가 처리 중 문제를 만났다는 단서예요", "상태 코드는 단서이지 원인을 다 말하진 않아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: methods ----------
def page8(daily):
    a = Anim(4, dur(daily))
    rows = ([("보기", "메뉴판 보여 주세요", BLUE), ("제출", "회원 가입서를 내요", GREEN), ("정보만", "가격만 알려 주세요", MUTED), ("바꾸기·취소", "주문을 바꾸거나 취소해요", ORANGE)] if daily else
            [("GET", "자원 조회", BLUE), ("POST", "정보 제출 (로그인 양식)", GREEN), ("HEAD", "본문 없이 헤더만", MUTED), ("PUT · DELETE", "만들기·바꾸기 · 삭제", ORANGE)])
    body = [person(90, 290, "손님") if daily else laptop(90, 300, "브라우저"), house(870, 270, "한빛분식") if daily else pc(870, 300, "서버")]
    for k, (m, s, c) in enumerate(rows):
        y = 155 + k * 70
        st = 1 if k == 0 else 2 if k == 1 else 3
        body.append(a.vis(cell(170, y, 170, 44, m, c, 17) + arrow(345, 790, y + 22, c, 3) + text(565, y + 12, s, 15, c, 700), st, 4))
    body += [a.vis(hl(170, 155, 170, 44, BLUE, 8), 1, 1), a.vis(hl(170, 225, 170, 44, GREEN, 8), 2, 2),
             a.vis(pill(480, 455, "남의 가게 주문을 함부로 바꾸지 않아요" if daily else "다른 사람의 서버에 바꾸는 요청을 함부로 보내지 않아요", RED, 15, True), 4, 4)]
    if daily:
        t, sub = "부탁의 종류", "보기, 제출, 바꾸기처럼 원하는 일이 달라요"
        caps = ["메뉴판을 보여 달라는 건 보기 부탁이에요", "회원 가입서를 내는 건 제출 부탁이에요", "가격만 묻기, 주문 바꾸기·취소 부탁도 있어요", "부탁할 수 있는 일은 가게가 정해 두어요"]
    else:
        t, sub = "HTTP Method", "요청이 원하는 일을 표준 이름으로 나타내요"
        caps = ["GET은 자원을 조회할 때 주로 써요", "POST는 로그인처럼 정보를 제출할 때 흔히 써요", "HEAD, PUT, DELETE도 각자 원하는 일을 나타내요", "실제 동작은 서버와 표준 규칙이 정해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: URL -> DNS -> TCP -> HTTP -> display ----------
def page9(daily):
    a = Anim(4, dur(daily))
    st = ([("가게 이름", "한빛분식", MUTED), ("위치 찾기", "지도 앱에서", ORANGE), ("길 잇기", "가게까지 가요", GREEN), ("주문·받기", "떡볶이 주세요", BLUE), ("먹기", "음식을 받아요", VIOLET)] if daily else
          [("URL", "어느 자원?", MUTED), ("DNS", "IP 주소는?", ORANGE), ("TCP", "연결을 만들어요", GREEN), ("HTTP", "요청·응답 형식", BLUE), ("화면", "브라우저 표시", VIOLET)])
    step_of = [1, 1, 2, 3, 4]
    body = []
    for k, ((n, s, c), sk) in enumerate(zip(st, step_of)):
        x = 30 + k * 184
        body.append(a.vis(role(x, 190, 160, 100, n, s, c, 19) + (arrow(x - 22, x - 2, 240, MUTED, 3) if k else ""), sk, 4))
        body.append(a.vis(hl(x, 190, 160, 100, c, 12), sk, sk))
    body += [a.vis(pill(480, 340, "www.example.com → 203.0.113.10 (예시)" if not daily else "한빛분식 → 한빛로 12 (예시)", ORANGE, 15, True), 1, 1),
             a.vis(pill(480, 340, "GET /example-page → 200 OK + HTML" if not daily else "떡볶이 주세요 → 주문 완료 + 떡볶이", BLUE, 15, True), 3, 3),
             a.vis(text(480, 420, "단계마다 묻는 질문이 달라요", 18, TXT, 700), 4, 4)]
    if daily:
        t, sub = "가게 이름에서 음식까지", "찾기, 가기, 주문, 받기가 차례로 이어져요"
        caps = ["가게 이름으로 지도 앱에서 위치를 찾아요", "찾은 위치로 가게까지 길을 이어요", "주문서로 주문하고 음식을 받아요", "받은 음식을 먹으며 단계마다 할 일이 달랐어요"]
    else:
        t, sub = "URL에서 응답까지", "DNS → TCP → HTTP → 화면 표시로 이어져요"
        caps = ["DNS가 도메인 이름에 맞는 IP 주소를 찾아요", "브라우저가 그 서버와 TCP 연결을 만들어요", "HTTP로 GET 요청을 보내고 200 OK와 HTML을 받아요", "브라우저가 문서를 화면에 표시해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l34-daily-order-promise-road", "l34-http-and-tcp-roles", page1, 0),
    ("l34-daily-order-slip-lines", "l34-message-parts", page2, 5),
    ("l34-daily-many-orders", "l34-many-requests-one-page", page3, 0),
    ("l34-daily-order-history", "l34-devtools-network", page4, 0),
    ("l34-daily-order-memo", "l34-request-headers", page5, 0),
    ("l34-daily-box-label", "l34-response-headers", page6, 0),
    ("l34-daily-order-result", "l34-status-codes", page7, 0),
    ("l34-daily-kinds-of-asks", "l34-http-methods", page8, 0),
    ("l34-daily-name-to-meal", "l34-url-to-response-flow", page9, 0),
]

COPY = {
    "l34-daily-order-promise-road": ("주문서 약속과 배달 길",
        "손님은 약속된 주문서로 분식집에 주문하고 가게는 음식으로 답합니다. 아래 배달 길은 짐을 이어진 흐름으로 나르고, 주문서 양식 덕분에 주문 1과 주문 2를 나누어 읽습니다.",
        "주문하는 약속과 나르는 길은 서로 다른 일입니다."),
    "l34-http-and-tcp-roles": ("HTTP와 TCP/IP의 역할",
        "브라우저가 HTTP 요청을 보내고 서버가 HTTP 응답을 돌려줍니다. 아래 TCP/IP는 데이터를 이어진 흐름으로 옮기고, HTTP 규칙에 맞춰 흐름 속 요청 1과 요청 2의 경계를 나눕니다.",
        "HTTP는 웹 자원을 주고받는 약속이고, TCP/IP는 데이터를 옮기는 데 쓰입니다."),
    "l34-daily-order-slip-lines": ("주문서와 답을 줄마다 읽어요",
        "왼쪽 주문서와 오른쪽 답에서 첫 줄, 가게 이름 같은 덧붙인 정보, 빈 줄, 떡볶이가 담긴 상자가 차례로 강조됩니다.",
        "첫 줄은 요약, 다음 줄들은 덧붙인 정보, 빈 줄 뒤가 실제 내용입니다."),
    "l34-message-parts": ("HTTP 메시지의 모양",
        "요청의 GET /example-page HTTP/1.1과 Host: www.example.com, 응답의 HTTP/1.1 200 OK와 Content-Type 헤더, 빈 줄, <h1>안녕, 웹!</h1> 본문이 차례로 강조됩니다.",
        "첫 줄은 요청이나 결과의 요약, 헤더는 부가 정보, 본문은 실제로 주고받는 내용입니다."),
    "l34-daily-many-orders": ("주문하면 가게가 답해요",
        "손님이 떡볶이를 주문하고 가게가 주문 완료와 함께 떡볶이를 내줍니다. 이어서 단무지, 음료, 수저도 따로 부탁하고 각각 답을 받습니다.",
        "한 번 방문에도 주문과 답이 여러 번 오갈 수 있습니다."),
    "l34-many-requests-one-page": ("Request와 Response",
        "브라우저가 GET /example-page 요청을 보내고 서버가 200 OK와 HTML로 응답합니다. 이어서 logo.png, style.css, app.js도 각각 요청하고 응답을 받습니다.",
        "Request는 클라이언트에서 서버로, Response는 서버에서 클라이언트로 오가며 페이지 하나에도 여러 번 생깁니다."),
    "l34-daily-order-history": ("내 주문 내역 살펴보기",
        "앱의 내 주문 내역에서 떡볶이 주문 하나를 골라 주문 종류, 결과, 메모, 받은 것을 확인합니다. 마지막에 내 주문만 보고 남의 주문은 엿보지 않는다고 표시됩니다.",
        "내 주문 하나를 골라 무엇을 부탁했고 무엇을 받았는지 봅니다."),
    "l34-devtools-network": ("개발자 도구의 Network 탭",
        "Network 탭의 요청 목록에서 example-page를 골라 Method GET, 상태 200 OK, 요청 헤더, HTML 응답 본문을 확인합니다. 마지막에 내가 연 페이지의 요청만 본다고 표시됩니다.",
        "Network 탭에서 요청 하나를 고르면 브라우저가 보낸 것과 서버가 답한 것을 볼 수 있습니다."),
    "l34-daily-order-memo": ("주문서에 붙이는 메모",
        "주문서의 받을 형태, 원하는 말, 눌러 담기 메모가 차례로 강조되고, 마지막에 주문 기기와 가려진 회원 카드 번호가 표시됩니다.",
        "메모는 주문에 덧붙인 설명이고, 민감한 번호는 가립니다."),
    "l34-request-headers": ("요청 Header",
        "요청 헤더 Accept: text/html, Accept-Language: ko, Accept-Encoding: gzip이 차례로 강조되고, 마지막에 User-Agent와 값이 가려진 Cookie가 표시됩니다.",
        "요청 헤더는 원하는 응답 형식과 요청에 필요한 부가 정보를 전달합니다. 민감한 값은 가립니다."),
    "l34-daily-box-label": ("음식 상자에 붙은 라벨",
        "음식 상자 라벨의 내용물, 무게, 적립 도장 안내가 차례로 강조되고, 손님이 라벨을 보고 음식을 알맞게 다룹니다.",
        "라벨은 내용물이 무엇인지와 어떻게 다룰지 알려 줍니다."),
    "l34-response-headers": ("응답 Header",
        "응답 헤더 Content-Type이 본문은 HTML이라고, Content-Length가 본문 크기를 알려 주고, Set-Cookie가 브라우저에 쿠키 저장을 알립니다. 마지막에 브라우저가 헤더를 참고해 응답을 처리합니다.",
        "응답 헤더는 본문이 어떤 내용인지와 브라우저가 어떻게 다룰지 설명합니다."),
    "l34-daily-order-result": ("주문 결과 한마디",
        "떡볶이 주문에는 주문 완료, 메뉴 이름 오타에는 그런 메뉴는 없다는 답, 주방 고장에는 만들 수 없다는 답이 차례로 나타납니다.",
        "가게의 첫마디는 결과의 단서일 뿐 원인을 모두 말하지는 않습니다."),
    "l34-status-codes": ("상태 코드",
        "GET /example-page에는 200 OK, 오타가 난 GET /exmaple-page에는 404 Not Found, 서버 처리 문제에는 500 Internal Server Error가 차례로 돌아옵니다.",
        "200은 성공, 404는 자원을 찾지 못함, 5xx는 서버 처리 문제의 단서입니다."),
    "l34-daily-kinds-of-asks": ("부탁의 종류",
        "메뉴판 보기, 회원 가입서 제출, 가격만 묻기, 주문 바꾸기·취소 부탁이 차례로 나타나고, 마지막에 남의 가게 주문을 함부로 바꾸지 않는다고 표시됩니다.",
        "부탁마다 원하는 일이 다르고, 가능한 일은 가게가 정해 둡니다."),
    "l34-http-methods": ("HTTP Method",
        "GET은 자원 조회, POST는 로그인 양식 같은 정보 제출, HEAD는 본문 없이 헤더만, PUT과 DELETE는 만들기·바꾸기와 삭제를 나타내며 차례로 나타납니다.",
        "GET은 주로 조회, POST는 주로 제출에 쓰이며, Method는 요청의 의도를 나타내는 표준 이름입니다."),
    "l34-daily-name-to-meal": ("가게 이름에서 음식까지",
        "가게 이름으로 지도 앱에서 위치를 찾고, 가게까지 길을 잇고, 떡볶이를 주문해 받은 뒤 먹는 단계가 차례로 나타납니다.",
        "찾기, 가기, 주문, 받기는 단계마다 하는 일이 다릅니다."),
    "l34-url-to-response-flow": ("URL에서 응답까지",
        "URL과 DNS가 www.example.com의 예시 IP 주소를 찾고, TCP 연결을 만든 뒤, HTTP로 GET /example-page를 보내 200 OK와 HTML을 받고, 브라우저가 화면에 표시합니다.",
        "URL 선택 → DNS가 IP 찾기 → TCP 연결 → HTTP 요청·응답 → 브라우저 표시. IP 주소는 예시입니다."),
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
