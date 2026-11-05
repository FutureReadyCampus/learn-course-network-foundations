#!/usr/bin/env python3
"""Unit 10 Lesson 2 (WAS, RESTful API, JVM) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u10_l02.py   (add --svg-only to skip the lesson.md edit).

- 7 Pages x (daily-life SVG at the top + network SVG after a matching paragraph) = 14 new SVGs.
- assets/diagrams/lesson-36.svg is rewritten as the current login request path + seven-page concept map.
- l36-three-tier-path.svg and l36-https-segments.svg (animation-source and animations copies, kept byte-identical)
  get small text fixes (login-case wording; "SSL 장비" -> "TLS 처리 장비").
- lesson.md: only `illustrations:` is added to each Page; `animations:`, `terms`, quizzes and prose are untouched."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv
from u10_l01 import at, role, lanes, msg, add_illustrations

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/06-*"))
OUT = LESSON / "assets" / "animations"
SRC = LESSON / "assets" / "animation-source"
DIAGRAM = LESSON / "assets" / "diagrams" / "lesson-36.svg"


# ---------- Page 1: where did the time go? ----------
def page1(daily):
    a = Anim(4, dur(daily))
    names = ["손님", "홀", "주방", "창고"] if daily else ["브라우저", "웹 서버", "WAS", "DB"]
    cols = [BLUE, GREEN, ORANGE, VIOLET]
    xs = [40, 270, 500, 730]
    chain = "".join(role(x, 130, 170, 64, n, "", c, 19) for x, n, c in zip(xs, names, cols))
    chain += arrow(210, 270, 162, MUTED, 3) + arrow(440, 500, 162, MUTED, 3) + arrow(670, 730, 162, MUTED, 3)
    # time bar: 0.1 / 0.4 / 2.5 of 3.0 over 800px (explanatory assumption)
    x0, w = 80, 800
    seg = [(0.1, BLUE), (0.4, ORANGE), (2.5, VIOLET)]
    bar, x = [], x0
    for v, c in seg:
        ww = w * v / 3.0
        bar.append((x, ww, c))
        x += ww
    lab = (["전달 0.1", "조리 0.4", "재료 기다림 2.5"] if daily else ["네트워크 왕복 0.1초", "WAS 처리 0.4초", "DB 응답 대기 2.5초"])
    body = [chain, a.vis(text(480, 235, "요청은 이 순서로 들어가고 결과는 되돌아와요", 18, MUTED, 700), 1, 1)]
    for k, ((bx, bw, c), lb) in enumerate(zip(bar, lab)):
        body.append(a.vis(box(bx, 285, bw, 46, c, c, 4, sw=1), 2, 4))
    legend = "".join(box(lx, 406, 16, 16, c, c, 3, sw=1) + text(lx + 24, 420, lb, 16, TXT, 600, "start") for lx, lb, c in ((70, lab[0], BLUE), (330, lab[1], ORANGE), (590, lab[2], VIOLET)))
    body += [a.vis(legend, 2, 4),
             a.vis(brace(x0, x0 + w, 345, TXT, "화면이 뜨기까지 3초 (설명용 가정)" if not daily else "음식이 나오기까지 (설명용 가정)", False, 17), 2, 4),
             a.vis(hl(bar[2][0], 285, bar[2][1], 46, ORANGE, 6) + pill(bar[2][0] + bar[2][1] / 2, 255, "이 예에서 가장 길어요", ORANGE, 17, True), 3, 4),
             a.vis(pill(480, 456, "APM 같은 관측 도구는 단서를 줘요 · 원인은 로그와 함께 확인해요" if not daily else "시간 기록표는 단서를 줘요 · 원인은 함께 확인해요", GREEN, 16, True), 4, 4)]
    if daily:
        t, sub = "주문이 늦으면 어디서 늦었는지 봐요", "일을 나누면 늦어진 곳을 따로 볼 수 있어요"
        caps = ["손님 주문은 홀, 주방, 창고를 차례로 거쳐요", "구간마다 걸린 시간을 나눠 적어 봐요", "이 예에서는 창고에서 재료를 기다린 시간이 가장 길어요", "기록표는 단서일 뿐 원인은 함께 확인해요"]
    else:
        t, sub = "3초를 구간별로 나눠 보기", "숫자는 설명을 위한 가정이에요"
        caps = ["요청은 웹 서버, WAS, DB를 차례로 거쳐요", "구간별로 걸린 시간을 나눠서 봐요", "이 예에서는 DB 응답 대기가 가장 길어요", "APM은 조사할 단서를 주고 원인은 로그와 함께 확인해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: WAS / JVM / Servlet container ----------
def page2(daily):
    a = Anim(4, dur(daily))
    c1, c2, c3 = BLUE, GREEN, ORANGE
    outer = box(40, 120, 880, 300, LINE, PANEL, 14, sw=3) + text(60, 150, "공연장 전체" if daily else "WAS: 요청을 처리하는 서버 쪽 환경", 18, MUTED, 700, "start")
    left = (box(70, 170, 300, 235, c1, PANEL, 12, sw=3) + text(220, 200, "악보와 연주자" if daily else "Java 실행 기반", 18, c1, 700)
            + cell(100, 220, 240, 44, "악보(바이트코드)" if daily else "Java 코드 → 바이트코드", c1, 16)
            + line(220, 264, 220, 305, MUTED, 3) + polygon_down(220, 312)
            + cell(100, 318, 240, 60, "연주자(JVM)" if daily else "JVM", c1, 20))
    life = ("무대에 올림", "장면마다 연기", "내려옴") if daily else ("시작", "요청마다 실행", "종료")
    right = (box(400, 170, 490, 235, c2, PANEL, 12, sw=3) + text(645, 200, "무대 뒤 운영자" if daily else "Servlet 컨테이너 (예: Tomcat)", 18, c2, 700)
             + cell(430, 220, 200, 50, "배우" if daily else "Servlet", c3, 18)
             + text(760, 252, "맡은 장면을 연기해요" if daily else "요청에 맞는 응답을 만들어요", 15, MUTED)
             + "".join(cell(x, 320, w, 44, lab, c2, 15) for x, w, lab in ((425, 130, life[0]), (570, 150, life[1]), (735, 125, life[2])))
             + text(645, 395, "언제 올라오고 내려가는지를 관리해요" if daily else "Servlet의 시작부터 끝까지(생명주기)를 관리해요", 15, MUTED))
    pills = [pill(250, 450, "WAS = 요청 처리 환경" if not daily else "공연장 = 전체 환경", GREEN, 16, True, 270),
             pill(530, 450, "JVM = Java 실행 기반" if not daily else "연주자 = 악보를 읽는 쪽", BLUE, 16, True, 250),
             pill(790, 450, "컨테이너 = 연결·관리" if not daily else "운영자 = 관리하는 쪽", ORANGE, 16, True, 250)]
    body = [outer, left, right,
            a.vis(hl(40, 120, 880, 300, GREEN, 14), 1, 1),
            a.vis(hl(70, 170, 300, 235, BLUE, 12), 2, 2),
            a.vis(hl(400, 170, 490, 235, GREEN, 12), 3, 3),
            a.vis("".join(pills), 4, 4)]
    if daily:
        t, sub = "극장의 배우와 무대 뒤 운영자", "공연장, 연주자, 운영자는 같은 말이 아니에요"
        caps = ["공연장 전체가 공연을 올리는 환경이에요", "악보는 연주자를 거쳐 소리가 돼요", "운영자는 배우가 언제 올라올지 관리해요", "공연장, 연주자, 운영자는 각자 다른 역할이에요"]
    else:
        t, sub = "WAS, JVM, Servlet 컨테이너", "같은 말이 아니라 역할이 달라요"
        caps = ["WAS는 요청을 실행하는 서버 쪽 환경이에요", "JVM은 Java 바이트코드를 실행하는 기반이에요", "컨테이너는 Servlet의 시작부터 끝까지를 관리해요", "세 이름은 서로 다른 역할을 가리켜요"]
    return frame(a, t, sub, caps, "".join(body))


def polygon_down(x, y):
    return f'<polygon points="{x},{y} {x - 9},{y - 14} {x + 9},{y - 14}" fill="{MUTED}"/>'


# ---------- Page 3: server HTML vs JSON then browser builds ----------
def page3(daily):
    a = Anim(4, dur(daily))
    lane = lambda y, tag, c, src, mid, scr: (
        pill(110, y + 40, tag, c, 17, True, 170)
        + role(230, y, 140, 80, ("재료 업체" if daily else "서버"), "", c, 18)
        + arrow(375, 495, y + 40, c, 5) + text(435, y + 28, mid, 15, c, 700)
        + role(500, y, 150, 80, "내 주방" if daily else "브라우저", "", c, 18)
        + arrow(655, 710, y + 40, c, 5) + role(715, y, 205, 80, ("식탁" if daily else scr[0]), scr[1], c, 17))
    body = [
        a.vis(lane(150, "방식 A" if not daily else "완성품 배달", BLUE, "", "완성된 HTML" if not daily else "완성된 요리", ("화면", "받은 문서를 그려요" if not daily else "그대로 차려요")), 1, 4),
        a.vis(lane(280, "방식 B" if not daily else "밀키트 배달", GREEN, "", "JSON 자료" if not daily else "재료와 조리법", ("화면", "JavaScript가 조립해요" if not daily else "내 식탁에서 조립해요")), 2, 4),
        a.vis(pill(480, 400, "두 방식 모두 널리 쓰여요", ORANGE, 17, True), 3, 4),
        a.vis(text(480, 450, "화면의 가격을 바꿔도 서버의 실제 가격은 그대로예요" if not daily else "내 식탁에서 조리법을 바꿔도 업체의 재료 가격은 그대로예요", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "완성품 배달과 밀키트 배달", "누가 마지막 조립을 하는지가 달라요"
        caps = ["완성된 요리를 받아 그대로 차릴 수 있어요", "재료와 조리법을 받아 내 식탁에서 조립할 수도 있어요", "두 방법 모두 가게마다 널리 쓰여요", "내 식탁에서 바꿔도 업체의 실제 가격은 그대로예요"]
    else:
        t, sub = "HTML을 받거나 JSON을 받거나", "누가 화면을 조립하는지가 달라요"
        caps = ["서버가 완성한 HTML 문서를 보내면 브라우저가 그려요", "서버가 JSON 자료를 보내면 JavaScript가 화면을 조립해요", "두 방식 모두 널리 쓰여요", "화면의 가격을 바꿔도 서버의 실제 가격은 그대로예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: API, URI, method ----------
def page4(daily):
    a = Anim(4, dur(daily))
    row = lambda y, m, uri, act, c: (pill(120, y, m, c, 17, True, 110) + text(200, y + 7, uri, 19, TXT, 700, "start")
                                     + arrow(450, 600, y, c, 4) + pill(745, y, act, c, 16, False, 270))
    body = [pill(110, 128, "손님" if daily else "브라우저", BLUE, 17, True, 150), pill(745, 128, "도서관 창구" if daily else "서버의 API", GREEN, 17, True, 190),
            a.vis(row(195, "조회" if daily else "GET", "7번 서가의 책" if daily else "/products/7", "읽기(Read): 정보를 보여 줘요", BLUE), 1, 4),
            a.vis(row(270, "신청" if daily else "POST", "새 신청서" if daily else "/orders", "만들기(Create): 새 처리를 요청해요", ORANGE), 2, 4),
            a.vis(box(60, 330, 410, 90, GREEN, PANEL, 10, sw=2) + text(265, 362, "서가 번호는 대상, 동작은 따로" if daily else "GET /products", 17, GREEN, 700)
                  + text(265, 395, "대상은 주소로, 동작은 메서드로" if not daily else "대상은 번호로, 동작은 신청서 종류로", 15, MUTED)
                  + box(490, 330, 410, 90, MUTED, PANEL, 10, dash=True, sw=2) + text(695, 362, "서가 번호에 동작 이름을 쓰는 방식" if daily else "/getProducts", 17, MUTED, 700)
                  + text(695, 395, "이런 설계도 볼 수 있어요", 15, MUTED), 3, 4),
            a.vis(pill(480, 452, "CRUD는 작업의 분류예요 · 실제 동작은 서비스의 API 명세가 정해요" if not daily else "신청 종류는 도서관 안내문이 정해요", ORANGE, 16, True), 4, 4)]
    if daily:
        t, sub = "도서관 창구에서 요청하기", "무엇을 대상으로 어떤 일을 할지 말해요"
        caps = ["7번 서가의 책 정보를 보여 달라고 조회해요", "새 신청서를 내서 새 처리를 요청해요", "대상은 번호로, 동작은 신청 종류로 나타내요", "실제로 어떻게 처리할지는 안내문이 정해요"]
    else:
        t, sub = "URI는 대상, 메서드는 동작", "API는 기능을 요청하는 약속된 접점이에요"
        caps = ["GET /products/7은 7번 상품 정보를 읽어 달라는 요청이에요", "POST /orders는 주문 자료를 보내 새 처리를 요청해요", "REST에서는 대상을 주소로, 동작을 메서드로 나타내요", "CRUD는 분류이고 실제 동작은 API 명세가 정해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: where TLS ends ----------
def page5(daily):
    a = Anim(4, dur(daily))
    nodes = [(100, "브라우저" if not daily else "손님", BLUE), (300, "IPS · WAF" if not daily else "가방 검사대", ORANGE),
             (520, "TLS 처리 장비" if not daily else "로비 데스크", GREEN), (800, "WAS" if not daily else "사무실", VIOLET)]
    top = "".join(role(x - 80, 150, 160, 66, n, "", c, 17) for x, n, c in nodes)
    green, orange = GREEN, ORANGE
    seg = lambda y, x0, x1, c: line(x0, y, x1, y, c, 10)
    rowA = (text(60, 292, "구성 A" if not daily else "방법 A", 18, TXT, 700, "start") + seg(300, 100, 520, green) + seg(300, 520, 800, orange)
            + text(310, 330, "잠김(TLS)" if not daily else "잠금 가방", 16, green, 700) + text(660, 330, "평문일 수 있음" if not daily else "열린 채로 이동", 16, orange, 700))
    rowB = (text(60, 372, "구성 B" if not daily else "방법 B", 18, TXT, 700, "start") + seg(380, 100, 520, green) + seg(380, 520, 800, green)
            + text(310, 410, "잠김(TLS)" if not daily else "잠금 가방", 16, green, 700) + text(660, 410, "다시 TLS로 암호화" if not daily else "새 가방에 다시 잠금", 16, green, 700))
    body = [top,
            a.vis(text(480, 248, "검사 장비의 종류와 위치는 제품과 구성에 따라 달라요", 16, MUTED, 700), 1, 4),
            a.vis(hl(430, 150, 180, 66, GREEN, 12), 1, 1),
            a.vis(rowA, 2, 4), a.vis(rowB, 3, 4),
            a.vis(pill(480, 452, "HTTPS 표시만으로 모든 내부 구간을 단정하지 않아요" if not daily else "잠금 표시만으로 모든 구간을 단정하지 않아요", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "잠금 가방은 어디까지 갈까", "가방이 열리는 곳에서 보호 구간이 갈려요"
        caps = ["짐은 검사대와 로비 데스크를 지나 사무실로 가요", "로비 데스크에서 가방을 열면 그 뒤는 열린 채일 수 있어요", "열고 나서 새 가방에 다시 잠그는 구성도 있어요", "잠금 표시만 보고 모든 구간을 단정하면 안 돼요"]
    else:
        t, sub = "TLS가 어디서 끝나는지 보기", "구성에 따라 보호 구간이 달라요"
        caps = ["요청은 보안 장비와 TLS 처리 장비를 지날 수 있어요", "장비에서 복호화하면 그 뒤 구간은 평문일 수 있어요", "장비에서 서버까지 다시 TLS로 암호화하는 구성도 있어요", "HTTPS 표시만으로 모든 내부 구간을 단정할 수 없어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: checks in the browser and on the server ----------
def page6(daily):
    a = Anim(4, dur(daily))
    panelL = box(40, 125, 300, 190, BLUE, PANEL, 12, sw=3) + text(190, 155, "접수 안내 창구" if daily else "브라우저 검사", 18, BLUE, 700)
    panelR = box(620, 125, 300, 190, GREEN, PANEL, 12, sw=3) + text(770, 155, "심사실" if daily else "서버 검증", 18, GREEN, 700)
    ok = lambda lab, c: (pill(480, 400, lab, c, 16, False, 420))
    body = [panelL, panelR, arrow(345, 615, 220, MUTED, 4) + text(480, 205, "요청" if not daily else "제출", 16, MUTED, 700),
            a.vis(text(190, 205, "이름 길이·나이 범위" if not daily else "빈 칸·글자 수", 16, TXT, 600) + text(190, 245, "틀리면 바로 알려 줘요", 16, BLUE, 700) + text(190, 285, "사용을 편하게 해요", 15, MUTED), 1, 4),
            a.vis(line(190, 315, 190, 362, ORANGE, 3, "6 5") + line(190, 362, 770, 362, ORANGE, 3, "6 5") + line(770, 362, 770, 330, ORANGE, 3) + f'<polygon points="770,316 761,332 779,332" fill="{ORANGE}"/>'
                  + text(480, 350, "화면을 거치지 않고 직접 만든 요청도 올 수 있어요" if not daily else "창구를 거치지 않고 직접 낸 서류도 올 수 있어요", 16, ORANGE, 700), 2, 4),
            a.vis(text(770, 205, "길이·범위·필수 항목을", 16, TXT, 600) + text(770, 235, "직접 검사해요", 16, GREEN, 700) + text(770, 285, "처리를 지키는 경계예요", 15, MUTED), 2, 4),
            a.vis(box(60, 385, 400, 55, GREEN, PANEL, 8, sw=2) + text(260, 420, "명령 + 입력 자료를 분리해요" if not daily else "양식 칸과 쓴 내용을 분리해요", 17, GREEN, 700)
                  + box(500, 385, 400, 55, RED, PANEL, 8, dash=True, sw=2) + text(700, 420, "입력을 명령에 이어 붙이지 않아요" if not daily else "받아 적은 말을 지시서에 끼우지 않아요", 17, RED, 700), 3, 3),
            a.vis(pill(480, 415, "쿠키 값도 입력이라 서버가 세션 정보와 대조해요" if not daily else "보관증 번호도 심사실이 장부와 대조해요", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "접수 안내와 심사실", "안내 창구는 편의를, 심사실은 최종 확인을 맡아요"
        caps = ["안내 창구는 빈 칸을 바로 알려 줘서 편해요", "창구를 거치지 않은 서류도 있어서 심사실이 확인해요", "양식 칸과 쓴 내용을 섞지 않고 따로 다뤄요", "보관증 번호도 심사실이 장부와 대조해요"]
    else:
        t, sub = "브라우저 검사와 서버 검증", "서버는 받은 값을 직접 확인해요"
        caps = ["브라우저 검사는 틀린 입력을 바로 알려 줘서 편해요", "직접 만든 요청도 올 수 있어서 서버가 다시 검사해요", "SQL은 명령과 입력 자료를 분리해 다뤄요", "쿠키 값도 입력이라 서버가 세션 정보와 대조해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: one login request end to end ----------
def page7(daily):
    a = Anim(4, dur(daily))
    names = ["손님", "전화번호부", "홀", "주방", "창고"] if daily else ["브라우저", "DNS", "웹 서버", "WAS", "DB"]
    cols = [BLUE, ORANGE, GREEN, ORANGE, VIOLET]
    xs = [40, 220, 420, 620, 790]
    ws = [150, 150, 150, 140, 130]
    ch = "".join(role(x, 135, w, 64, n, "", c, 17) for x, w, n, c in zip(xs, ws, names, cols))
    body = [ch,
            a.vis(msg(115, 295, 245, "주소 찾기" if daily else "URL → IP 주소", ORANGE, 15), 1, 4),
            a.vis(msg(115, 495, 285, "전화 연결 + 주문" if daily else "TCP/IP 연결 + HTTP 요청", BLUE, 15), 2, 4),
            a.vis(msg(495, 690, 325, "입력을 확인해요" if not daily else "주문을 확인해요", GREEN, 15) + msg(690, 855, 365, "자료 조회" if not daily else "재료 확인", VIOLET, 15), 3, 4),
            a.vis(arrow(840, 115, 420, ORANGE, 5) + text(480, 408, "응답: HTML 또는 JSON → 브라우저가 화면으로" if not daily else "완성된 요리 → 손님 식탁에", 17, ORANGE, 700), 4, 4),
            a.vis(pill(480, 456, "HTTPS여도 TLS 처리 지점에 따라 보호 구간이 달라요" if not daily else "잠금 가방이 어디서 열리는지에 따라 보호 구간이 달라요", MUTED, 15), 4, 4)]
    if daily:
        t, sub = "식당 예약 전화로 이어 보기", "로그인 한 번에 지금까지의 흐름이 모두 쓰여요"
        caps = ["전화번호부에서 식당 번호를 찾아요", "전화를 연결해 주문을 전해요", "홀이 받고 주방이 만들며 창고에서 재료를 꺼내요", "완성된 요리가 손님 식탁으로 돌아와요"]
    else:
        t, sub = "로그인 요청 하나로 전체 흐름 잇기", "DNS부터 화면까지 한 줄로 이어요"
        caps = ["DNS로 서버의 IP 주소를 찾아요", "TCP/IP로 연결해 HTTP 요청을 보내요", "웹 서버가 받고 WAS가 검증해 DB에서 자료를 조회해요", "응답을 받은 브라우저가 화면을 만들어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- lesson-36.svg: current login path + seven-page concept map ----------
def diagram_svg():
    W, H = 1120, 660
    f = "-apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Segoe UI',sans-serif"
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" class="learning-flow" viewBox="0 0 {W} {H}" role="group" aria-labelledby="lesson-36-flow-title lesson-36-flow-desc" lang="ko" font-family="{f}">',
         '<title id="lesson-36-flow-title">로그인 요청 한 건으로 보는 WAS와 API 구조</title>',
         '<desc id="lesson-36-flow-desc">브라우저의 로그인 요청이 보안 장비, 웹 서버, WAS, DB를 지나 응답으로 돌아오는 길과, 이 Lesson의 일곱 페이지가 그 길의 어느 부분을 다루는지 보여 줍니다.</desc>',
         f'<rect width="{W}" height="{H}" fill="#0f1115"/>',
         '<defs><marker id="l36-arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 1 L7 4.5 L0 8" fill="none" stroke="#7ee7c7" stroke-width="1.8"/></marker>'
         '<marker id="l36-arr-o" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 1 L7 4.5 L0 8" fill="none" stroke="#ffb454" stroke-width="1.8"/></marker></defs>',
         text(560, 48, "로그인 요청 한 건이 지나가는 길", 30, TXT, 700)]
    nodes = [(40, "브라우저", "화면과 입력", BLUE), (250, "보안 장비 · TLS 처리", "IPS·WAF, HTTPS 종료 지점", ORANGE),
             (500, "웹 서버", "요청을 접수해요", GREEN), (730, "WAS", "로그인 규칙을 실행해요", ORANGE), (930, "DB", "계정 자료", VIOLET)]
    widths = [170, 200, 190, 170, 150]
    for (x, n, s, c), w in zip(nodes, widths):
        o.append(box(x, 100, w, 86, c, PANEL, 12, sw=3) + text(x + w / 2, 138, n, 20, c, 700) + text(x + w / 2, 168, s, 15, MUTED))
    ends = [(x + w) for (x, *_), w in zip(nodes, widths)]
    for i in range(4):
        x0, x1 = ends[i] + 4, nodes[i + 1][0] - 4
        o.append(f'<path d="M{x0} 132 H{x1}" stroke="#7ee7c7" stroke-width="3" fill="none" marker-end="url(#l36-arr)"/>')
    o.append('<path d="M1005 192 V222 H125 V196" stroke="#ffb454" stroke-width="3" fill="none" marker-end="url(#l36-arr-o)"/>')
    o.append(text(560, 246, "응답: HTML 문서 또는 JSON 자료 → 브라우저가 화면으로", 16, "#ffb454", 700))
    o.append(text(560, 288, "이 Lesson의 일곱 페이지가 길의 어느 곳을 다루는지", 20, TXT, 700))
    items = [("1", "세 단으로 나눠 느린 곳 찾기", "웹 서버 · WAS · DB", GREEN),
             ("2", "WAS 안의 JVM과 Servlet 컨테이너", "WAS", ORANGE),
             ("3", "서버는 자료, 브라우저는 화면", "응답 → 브라우저", BLUE),
             ("4", "API: URI와 메서드로 요청", "브라우저 → 서버", BLUE),
             ("5", "보안 장비와 HTTPS 보호 구간", "보안 장비 · TLS 처리", ORANGE),
             ("6", "입력은 브라우저와 서버에서 각각 확인", "브라우저 + WAS", VIOLET),
             ("7", "로그인 요청으로 흐름 연결", "처음부터 끝까지", MUTED)]
    for i, (n, ttl, where, c) in enumerate(items):
        col, row = i % 2, i // 2
        x, y = 40 + col * 540, 308 + row * 76
        if i == 6:
            x, y = 40 + 270, 308 + 3 * 76
        o.append(box(x, y, 500, 64, c, PANEL, 10, sw=2) + f'<circle cx="{x + 34}" cy="{y + 32}" r="20" fill="{c}"/>' + text(x + 34, y + 40, n, 22, BG, 700)
                 + text(x + 70, y + 29, ttl, 18, TXT, 700, "start") + text(x + 70, y + 51, "다루는 곳: " + where, 15, MUTED, anchor="start"))
    o.append(text(560, 645, "식당에 빗대면 웹 서버는 홀, WAS는 주방, DB는 창고예요", 17, MUTED))
    o.append("</svg>\n")
    return "\n".join(o)


# ---------- text fixes on the two existing animation SVGs (source + output kept byte-identical) ----------
def fix_existing():
    pairs = {
        "l36-https-segments.svg": [("SSL 장비", "TLS 처리 장비")],
        "l36-three-tier-path.svg": [
            ("주문 한 건이 지나가는 세 단", "로그인 요청이 지나가는 세 단"),
            (">주문</text>", ">로그인</text>"),
            (">자료</text>", ">계정</text>"),
            ("주문은 웹 서버 → WAS → DB 순서로 들어갑니다", "로그인 요청은 웹 서버 → WAS → DB 순서로 들어갑니다"),
            ("DB의 자료가 WAS에서 결과가 되어 되돌아옵니다", "DB의 계정 정보가 WAS에서 로그인 결과가 되어 돌아옵니다"),
        ],
    }
    for name, reps in pairs.items():
        for d in (SRC, OUT):
            p = d / name
            s = p.read_text(encoding="utf-8")
            for a_, b_ in reps:
                if a_ in s:
                    s = s.replace(a_, b_)
            p.write_text(s, encoding="utf-8")
        assert (SRC / name).read_bytes() == (OUT / name).read_bytes(), f"{name}: source/output differ"


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l36-daily-where-time-went", "l36-three-tier-time-split", page1, 2),
    ("l36-daily-theater-backstage", "l36-was-jvm-container", page2, 3),
    ("l36-daily-meal-kit-delivery", "l36-html-vs-json-screen", page3, 2),
    ("l36-daily-library-counter", "l36-api-uri-method", page4, 1),
    ("l36-daily-locked-bag-route", "l36-tls-ends-where", page5, 2),
    ("l36-daily-reception-and-review", "l36-browser-and-server-checks", page6, 2),
    ("l36-daily-reservation-call", "l36-login-end-to-end", page7, 1),
]

COPY = {
    "l36-daily-where-time-went": ("주문이 늦으면 어디서 늦었는지 봐요",
        "손님 주문이 홀, 주방, 창고를 차례로 거치고, 구간마다 걸린 시간을 막대로 나눠 보면 이 예에서는 창고에서 재료를 기다린 시간이 가장 깁니다. 시간 기록표는 단서일 뿐 원인은 함께 확인해야 한다고 표시됩니다.",
        "일을 나누면 늦어진 곳을 따로 볼 수 있습니다. 구간별 시간은 설명을 위한 가정입니다."),
    "l36-three-tier-time-split": ("3초를 구간별로 나눠 보기",
        "브라우저의 요청이 웹 서버, WAS, DB를 차례로 거치고, 화면이 뜨기까지 3초 중 네트워크 왕복 0.1초, WAS 처리 0.4초, DB 응답 대기 2.5초로 나뉩니다. 이 예에서는 DB 대기가 가장 길고, APM은 조사할 단서를 주며 원인은 로그와 함께 확인합니다.",
        "3초와 0.1초, 0.4초, 2.5초는 설명을 위한 가정입니다. 전체 시간이 길다는 사실만으로 어느 구성요소가 느린지 단정할 수는 없습니다.", 2),
    "l36-daily-theater-backstage": ("극장의 배우와 무대 뒤 운영자",
        "공연장 안에서 악보는 연주자를 거쳐 소리가 되고, 무대 뒤 운영자는 배우가 언제 무대에 올라오고 장면마다 연기하고 내려오는지를 관리합니다. 공연장, 연주자, 운영자는 같은 말이 아니라고 표시됩니다.",
        "배우는 맡은 장면을 연기하고, 운영자는 그 시작부터 끝까지를 관리합니다. 실제 무대는 프로그램 실행 환경을 뜻합니다."),
    "l36-was-jvm-container": ("WAS, JVM, Servlet 컨테이너",
        "WAS는 요청을 처리하는 서버 쪽 환경이고, 그 안에서 Java 코드가 바이트코드가 되어 JVM에서 실행되며, Servlet 컨테이너는 Servlet의 시작, 요청마다 실행, 종료를 관리합니다. WAS, JVM, 컨테이너는 서로 다른 역할이라고 표시됩니다.",
        "WAS는 요청 처리 환경, JVM은 Java 실행 기반, Servlet 컨테이너는 Java 웹 요청과 Servlet을 이어 주는 관리자입니다. 제품에 따라 한 프로그램에 함께 들어갈 수 있습니다.", 3),
    "l36-daily-meal-kit-delivery": ("완성품 배달과 밀키트 배달",
        "재료 업체가 완성된 요리를 보내면 내 주방에서 그대로 차리고, 재료와 조리법을 보내면 내 식탁에서 조립합니다. 두 방법 모두 널리 쓰이며, 내 식탁에서 바꿔도 업체의 실제 가격은 그대로입니다.",
        "누가 마지막 조립을 하는지가 다른 두 방식입니다. 둘 다 널리 쓰입니다."),
    "l36-html-vs-json-screen": ("HTML을 받거나 JSON을 받거나",
        "서버가 완성한 HTML 문서를 보내면 브라우저가 그대로 그리고, 서버가 JSON 자료를 보내면 브라우저의 JavaScript가 화면을 조립합니다. 두 방식 모두 널리 쓰이며 화면의 가격을 바꿔도 서버의 실제 가격은 그대로입니다.",
        "JSON을 받는다고 해서 특정 프레임워크가 반드시 필요한 것은 아닙니다. 서버가 HTML을 완성해 보내는 사이트도 널리 쓰입니다.", 2),
    "l36-daily-library-counter": ("도서관 창구에서 요청하기",
        "손님이 도서관 창구에서 7번 서가의 책 정보를 조회하고 새 신청서를 내 새 처리를 요청합니다. 대상은 서가 번호로, 동작은 신청 종류로 나타내며 실제 처리는 도서관 안내문이 정한다고 표시됩니다.",
        "무엇을 대상으로 어떤 일을 할지 말하는 창구와 같이, API는 요청의 대상과 종류를 나타냅니다."),
    "l36-api-uri-method": ("URI는 대상, 메서드는 동작",
        "브라우저가 GET /products/7로 7번 상품 정보를 읽어 달라고 하고 POST /orders로 주문 자료를 보내 새 처리를 요청합니다. REST에서는 대상을 주소로, 동작을 메서드로 나타내는 방식을 흔히 쓰고 /getProducts처럼 동작 이름을 주소에 넣는 설계도 볼 수 있으며, 실제 동작은 API 명세가 정합니다.",
        "API는 URI와 HTTP 메서드, 요청 자료로 무엇을 요청하는지 나타냅니다. CRUD는 작업 분류이며 HTTP 메서드와 고정된 일대일 규칙은 아닙니다.", 1),
    "l36-daily-locked-bag-route": ("잠금 가방은 어디까지 갈까",
        "짐이 가방 검사대와 로비 데스크를 지나 사무실로 가고, 로비 데스크에서 가방을 열면 그 뒤는 열린 채일 수 있으며, 열고 나서 새 가방에 다시 잠그는 방법도 있습니다. 잠금 표시만으로 모든 구간을 단정하면 안 된다고 표시됩니다.",
        "가방이 열리는 곳에 따라 보호되는 구간이 달라집니다."),
    "l36-tls-ends-where": ("TLS가 어디서 끝나는지 보기",
        "브라우저의 요청이 IPS·WAF 같은 보안 장비와 TLS 처리 장비를 지나 WAS로 갑니다. 구성 A는 장비까지만 TLS로 잠그고 그 뒤는 평문일 수 있으며, 구성 B는 장비에서 WAS까지 다시 TLS로 암호화합니다. HTTPS 표시만으로 모든 내부 구간을 단정할 수 없습니다.",
        "TLS를 처리하는 지점에 따라 보호되는 구간이 달라집니다. 장비의 종류와 배치는 제품과 네트워크 구성에 따라 다릅니다.", 2),
    "l36-daily-reception-and-review": ("접수 안내와 심사실",
        "접수 안내 창구는 빈 칸이나 글자 수를 바로 알려 주고, 창구를 거치지 않고 직접 낸 서류도 올 수 있어 심사실이 직접 확인합니다. 양식 칸과 쓴 내용을 섞지 않고 따로 다루며, 보관증 번호도 심사실이 장부와 대조합니다.",
        "안내 창구는 편의를, 심사실은 처리를 지키는 최종 확인을 맡습니다."),
    "l36-browser-and-server-checks": ("브라우저 검사와 서버 검증",
        "브라우저는 이름 길이와 나이 범위를 확인해 틀린 입력을 바로 알려 주지만, 직접 만든 요청도 서버에 올 수 있어 서버가 길이와 범위와 필수 항목을 다시 검사합니다. SQL은 명령과 입력 자료를 분리해 다루고 이어 붙이지 않으며, 쿠키 값도 입력이라 서버가 세션 정보와 대조합니다.",
        "브라우저 검사는 사용을 편하게 하고 서버 검증은 실제 처리를 지킵니다.", 2),
    "l36-daily-reservation-call": ("식당 예약 전화로 이어 보기",
        "손님이 전화번호부에서 식당 번호를 찾아 전화를 연결해 주문을 전하고, 홀이 받아 주방이 만들며 창고에서 재료를 꺼내 확인하고, 완성된 요리가 손님 식탁으로 돌아옵니다. 잠금 가방이 어디서 열리는지에 따라 보호 구간이 달라질 수 있다고 표시됩니다.",
        "로그인 한 번이 식당 예약 전화와 같은 길을 지납니다. 홀은 웹 서버, 주방은 WAS, 창고는 DB에 빗댈 수 있습니다."),
    "l36-login-end-to-end": ("로그인 요청 하나로 전체 흐름 잇기",
        "브라우저가 DNS로 서버의 IP 주소를 찾고, TCP/IP로 연결해 HTTP 요청을 보내면, 웹 서버가 받고 WAS가 입력을 확인해 DB에서 자료를 조회한 뒤, 응답으로 HTML 또는 JSON이 돌아와 브라우저가 화면을 만듭니다. HTTPS여도 TLS를 처리하는 지점에 따라 보호 구간이 달라집니다.",
        "로그인 요청 하나에 DNS, TCP/IP, HTTP, 웹 서버, WAS, DB, 응답과 화면까지의 흐름이 이어집니다.", 1),
}


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
    DIAGRAM.write_text(diagram_svg(), encoding="utf-8")
    fix_existing()
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        add_illustrations(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
