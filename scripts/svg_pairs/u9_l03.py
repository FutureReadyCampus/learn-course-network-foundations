#!/usr/bin/env python3
"""Unit 9 Lesson 3 (URL and URI) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u9_l03.py   (add --svg-only to skip the lesson.md edit).

Every page gets a daily-life SVG at the top (after_paragraph -1) and a network SVG with the same layout after the
explanatory paragraph. All network scenes use the lesson's one example URL; the daily scenes use one matching
library request. The existing wiki `animations:` entries (pages 4, 7) are left as they are; the new items go into a
separate `illustrations:` key on each page."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur
from u7_l01 import mv
from u10_l01 import role, msg, add_illustrations
from u9_l02 import doc

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/03-*"))
OUT = LESSON / "assets" / "animations"

# index: 0 scheme, 1 separator, 2 host, 3 port, 4 path, 5 query, 6 fragment
PARTS_N = ["https", "://", "www.test.co.kr", ":8080", "/data/index.html", "?search_keyword=Test", "#result"]
PARTS_D = ["빌리기", "→", "한빛도서관", "8번 창구", "과학 서가/공룡책", "?검색어=공룡", "#3장"]
COLS = [BLUE, MUTED, GREEN, ORANGE, VIOLET, RED, TXT]
NAMES_N = ["scheme", "", "host", "port", "path", "query", "fragment"]
NAMES_D = ["방법", "", "건물", "창구", "서가와 책", "조건", "책 속 위치"]


def strip(daily, y=140, fs=16, h=40):
    """The example address as coloured cells; returns (svg, [(x, w), ...])."""
    parts = PARTS_D if daily else PARTS_N
    ws = [tw(s, fs) + (12 if k == 1 else 22) for k, s in enumerate(parts)]
    x = 480 - (sum(ws) + 4 * (len(ws) - 1)) / 2
    svg, pos = "", []
    for s, w, c in zip(parts, ws, COLS):
        svg += cell(round(x), y, round(w), h, s, c, fs)
        pos.append((round(x), round(w)))
        x += w + 4
    return svg, pos


def darrow(x0, y0, x1, y1, c, w=4):
    a = math.atan2(y1 - y0, x1 - x0)
    p = [(x1 - 16 * math.cos(a + s), y1 - 16 * math.sin(a + s)) for s in (-0.45, 0.45)]
    return line(x0, y0, x1, y1, c, w) + f'<polygon points="{x1},{y1} {p[0][0]:.0f},{p[0][1]:.0f} {p[1][0]:.0f},{p[1][1]:.0f}" fill="{c}"/>'


def mark(pos, k, y=140, h=40, c=ORANGE):
    x, w = pos[k]
    return hl(x, y, w, h, c, 8)


# ---------- Page 1: URI is the big category, URL is inside ----------
def page1(daily):
    a = Anim(4, dur(daily))
    full = " ".join(PARTS_D) if daily else "".join(PARTS_N)
    body = [box(80, 130, 800, 320, VIOLET, PANEL, 18, sw=3)
            + text(110, 165, "책을 가리키는 모든 이름표" if daily else "URI: 자원을 식별하는 큰 범주", 19, VIOLET, 700, "start"),
            a.vis(hl(80, 130, 800, 320, VIOLET, 18), 1, 1),
            a.vis(box(160, 200, 640, 180, GREEN, BG, 14, sw=3)
                  + text(190, 234, "찾아갈 위치와 방법까지 적은 것" if daily else "URL: 위치와 접근 방법을 나타내는 URI", 18, GREEN, 700, "start"), 2, 4),
            a.vis(hl(160, 200, 640, 180, GREEN, 14), 2, 2),
            a.vis(pill(480, 300, full, GREEN, 15 if daily else 14), 3, 4),
            a.vis(text(480, 420, "URL은 URI 안에 들어가요. 같은 범위의 말이 아니에요" if not daily else "위치 쪽지는 이름표 중 한 종류예요", 18, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "이름표와 위치 쪽지", "위치 쪽지는 이름표 중 한 종류예요"
        caps = ["책을 가리키는 이름표에는 여러 종류가 있어요", "그중 찾아갈 위치와 방법을 적은 쪽지가 있어요", "도서관, 창구, 서가, 책까지 적힌 쪽지예요", "이름표가 더 큰 범위, 위치 쪽지는 그 일부예요"]
    else:
        t, sub = "URI와 URL의 범위", "URI는 큰 범주, URL은 위치를 알려 주는 URI예요"
        caps = ["URI는 웹 자원을 식별하는 큰 범주예요", "URL은 위치와 접근 방법을 나타내는 URI예요", "주소창에 적는 웹 주소가 URL의 예예요", "URI가 더 넓고, URL은 그 안에 들어가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: many kinds of resources ----------
def page2(daily):
    a = Anim(4, dur(daily))
    items = ([("책", "읽을 글"), ("사진집", "사진"), ("지도", "길 그림"), ("DVD", "영상"), ("대출 목록", "그때 뽑아 줘요")] if daily else
             [("HTML", "문서"), ("CSS", "디자인 파일"), ("JavaScript", "동작 코드"), ("JPG", "사진"), ("JSON", "API 데이터")])
    xs = [55, 235, 415, 595, 775]
    cs = [BLUE, VIOLET, ORANGE, GREEN, RED]
    body = []
    for k, ((n, s), x, c) in enumerate(zip(items, xs, cs)):
        st = 1 if k == 0 else 2 if k < 4 else 3
        body.append(a.vis(role(x, 160, 150, 90, n, s, c, 18), st, 4))
    body += [a.vis(hl(55, 160, 150, 90, BLUE, 12), 1, 1),
             a.vis("".join(hl(x, 160, 150, 90, c, 12) for x, c in zip(xs[1:4], cs[1:4])), 2, 2),
             a.vis(hl(775, 160, 150, 90, RED, 12) + text(850, 285, "저장 파일이 아니라" if daily else "저장된 파일이 아니라", 15, RED, 700)
                   + text(850, 305, "그때 만들어요", 15, RED, 700), 3, 3),
             a.vis("".join(darrow(x + 75, 255, 480 + (x - 415) / 6, 330, c, 3) for x, c in zip(xs, cs))
                   + (person(480, 365, "필요한 것을 모아 숙제해요") if daily else laptop(480, 375, "브라우저가 모아 화면을 만들어요")), 4, 4)]
    if daily:
        t, sub = "도서관에서 받을 수 있는 것", "책뿐 아니라 사진, 지도, 목록도 받아요"
        caps = ["도서관에서 책을 빌려 볼 수 있어요", "사진집, 지도, DVD도 따로따로 받을 수 있어요", "대출 목록은 사서가 그때 뽑아 만들어 줘요", "필요한 것을 각각 받아 모아서 써요"]
    else:
        t, sub = "웹 자원의 여러 모습", "문서, 디자인, 코드, 사진, 데이터가 모두 자원이에요"
        caps = ["웹페이지의 HTML 문서는 자원이에요", "CSS, JavaScript, JPG 사진도 각각 자원이에요", "API가 그때 만들어 주는 JSON 데이터도 자원이에요", "브라우저는 자원을 각각 요청해 화면을 만들어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: identify vs locate ----------
def page3(daily):
    a = Anim(4, dur(daily))
    centre = person(480, 290, "민수") if daily else doc(480, 220, "자원", BLUE, 130, 130)
    body = [centre,
            a.vis(role(40, 210, 290, 110, "이름: 누구인가?" if daily else "식별: 어떤 자원인가?", "민수, 신분 번호" if daily else "URI라는 넓은 개념", VIOLET, 19)
                  + arrow(335, 405, 265, VIOLET, 4), 2, 4),
            a.vis(role(630, 210, 290, 110, "주소: 어디서 만나나?" if daily else "위치: 어디서 어떻게?", "한빛동 12번지" if daily else "접근 위치와 방법 = URL", GREEN, 19)
                  + arrow(625, 555, 265, GREEN, 4), 3, 4),
            a.vis(hl(410, 200, 140, 180, BLUE, 12), 1, 1), a.vis(hl(40, 210, 290, 110, VIOLET, 12), 2, 2),
            a.vis(hl(630, 210, 290, 110, GREEN, 12), 3, 3),
            a.vis(pill(480, 420, "이름과 주소는 서로 다른 질문에 답해요" if daily else "자원은 대상 · URI는 식별 · URL은 위치", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "누구인지와 어디 있는지", "이름과 주소는 서로 다른 질문에 답해요"
        caps = ["여기 민수라는 친구가 있어요", "이름이나 신분 번호는 누구인지 알려 줘요", "집 주소는 어디로 가면 만날지 알려 줘요", "누구인지와 어디 있는지는 다른 질문이에요"]
    else:
        t, sub = "식별과 위치 지정", "어떤 자원인지와 어디서 가져올지는 다른 질문이에요"
        caps = ["웹에서 다루는 자원 하나가 있어요", "URI는 어떤 자원인지 식별하는 넓은 개념이에요", "URL은 어디서 어떻게 가져올지 알려 줘요", "사람 비유는 이해를 돕는 그림일 뿐이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: read the address part by part ----------
def page4(daily):
    a = Anim(4, dur(daily))
    s, pos = strip(daily, 200, 17, 44)
    names = NAMES_D if daily else NAMES_N
    seps = [1, 3, 4, 5, 6]
    labels = "".join(text(x + w / 2, 280 + (k % 2) * 30, names[k], 16, COLS[k], 700) for k, (x, w) in enumerate(pos) if names[k])
    body = [s, a.vis(text(480, 320, "한 덩어리로 보면 읽기 어려워요", 18, MUTED, 700), 1, 1),
            a.vis("".join(f'<polygon points="{pos[k][0] - 2},{256} {pos[k][0] - 10},{270} {pos[k][0] + 6},{270}" fill="{ORANGE}"/>' for k in seps)
                  + text(480, 320, "칸을 나누는 표시를 찾아요" if daily else "구분 기호  : / ? #  를 찾아요", 18, ORANGE, 700), 2, 2),
            a.vis(labels, 3, 4),
            a.vis(brace(pos[2][0], pos[3][0] + pos[3][1], 190, GREEN, "어느 곳" if daily else "authority", True, 15), 3, 4),
            a.vis(mark(pos, 3, 200, 44, ORANGE) + mark(pos, 6, 200, 44, ORANGE)
                  + pill(480, 395, "창구 번호와 책 속 위치는 빠질 수 있어요" if daily else "port와 fragment는 생략될 수 있어요", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "도서관 쪽지를 칸으로 나눠요", "방법, 건물, 창구, 서가, 조건, 위치로 읽어요"
        caps = ["쪽지 한 줄을 통째로 보면 읽기 어려워요", "칸을 나누는 표시를 먼저 찾아요", "칸마다 방법, 건물, 창구, 서가가 적혀 있어요", "창구 번호나 책 속 위치는 빠질 수 있어요"]
    else:
        t, sub = "주소를 부분으로 나누어 읽기", "구분 기호를 따라 다섯 부분으로 나눠요"
        caps = ["예시 주소 한 줄을 통째로 보면 어려워요", "콜론, 슬래시, 물음표, 샵 기호를 찾아요", "scheme, authority, path, query, fragment로 나눠요", "port와 fragment는 생략될 수도 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: scheme, host, port ----------
def page5(daily):
    a = Anim(4, dur(daily))
    s, pos = strip(daily)
    rows = ([("방법: 빌리기", "어떻게 요청할지"), ("건물: 한빛도서관", "어느 곳에 갈지"), ("창구: 8번", "어느 창구에서 볼지")] if daily else
            [("scheme: https", "요청 방식 (프로토콜)"), ("host: www.test.co.kr", "요청을 보낼 서버 이름"), ("port: 8080", "서비스 연결점 번호")])
    body = [s]
    for k, (idx, (n, sb), x, c) in enumerate(zip([0, 2, 3], rows, [40, 345, 650], [BLUE, GREEN, ORANGE]), 1):
        cx = pos[idx][0] + pos[idx][1] / 2
        body.append(a.vis(role(x, 250, 270, 100, n, sb, c, 18) + darrow(cx, 186, x + 135, 244, c, 3), k, 4))
        body.append(a.vis(mark(pos, idx, 140, 40, c), k, k))
    body.append(a.vis(pill(480, 410, "늘 쓰는 기본 창구면 번호를 안 적어요" if daily else "HTTPS 기본 포트 443이면 생략:  https://www.test.co.kr/", ORANGE, 16, True), 4, 4))
    if daily:
        t, sub = "방법, 건물, 창구", "어떻게, 어느 곳, 어느 창구를 나눠 봐요"
        caps = ["맨 앞 칸은 빌리기라는 요청 방법이에요", "한빛도서관은 찾아갈 건물 이름이에요", "8번 창구는 그 건물에서 볼 창구 번호예요", "기본 창구라면 번호를 빼고 적기도 해요"]
    else:
        t, sub = "Scheme, Host, Port", "요청 방식, 서버 이름, 서비스 번호를 구분해요"
        caps = ["https는 어떤 방식으로 요청할지 알려 주는 scheme이에요", "www.test.co.kr은 요청을 보낼 서버의 host예요", "8080은 그 서버에서 연결할 서비스의 port예요", "기본 포트(HTTP 80, HTTPS 443)는 흔히 생략해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: relative vs absolute path ----------
def page6(daily):
    a = Anim(4, dur(daily))
    R, D, I, X, G = (("도서관 입구", "과학 서가", "사진 서가", "공룡책", "지도책") if daily else
                     ("/ (사이트 기준점)", "data/", "images/", "index.html", "logo.png"))
    body = [line(480, 190, 250, 250, LINE, 3) + line(480, 190, 710, 250, LINE, 3) + line(250, 300, 250, 350, LINE, 3) + line(710, 300, 710, 350, LINE, 3),
            cell(370, 140, 220, 50, R, MUTED, 17), cell(160, 250, 180, 50, D, VIOLET, 17), cell(620, 250, 180, 50, I, VIOLET, 17),
            cell(160, 350, 180, 50, X, BLUE, 17), cell(620, 350, 180, 50, G, GREEN, 17),
            a.vis(hl(160, 350, 180, 50, BLUE, 8) + pill(250, 430, "지금 위치", BLUE, 15, True), 1, 3),
            a.vis(darrow(300, 250, 405, 196, ORANGE, 4) + pill(300, 205, "../ 한 단계 위로", ORANGE, 15, True), 2, 3),
            a.vis(darrow(560, 196, 690, 246, ORANGE, 4) + darrow(710, 300, 710, 346, ORANGE, 4) + check(820, 375)
                  + pill(480, 455, "../사진 서가/지도책 : 지금 위치에서 출발" if daily else "../images/logo.png : 현재 위치에서 출발", ORANGE, 15, True), 3, 3),
            a.vis(hl(370, 140, 220, 50, GREEN, 8) + darrow(560, 196, 690, 246, GREEN, 5) + darrow(710, 300, 710, 346, GREEN, 5) + check(820, 375)
                  + pill(480, 455, "/사진 서가/지도책 : 입구에서 출발" if daily else "/images/logo.png : 기준점에서 출발", GREEN, 15, True), 4, 4)]
    if daily:
        t, sub = "지금 자리에서, 또는 입구에서", "길은 지금 위치나 입구를 기준으로 적어요"
        caps = ["나는 지금 과학 서가의 공룡책 앞에 있어요", "../는 한 단계 위로 나간다는 약속이에요", "거기서 사진 서가의 지도책으로 찾아가요", "입구에서부터 적으면 어디서든 같은 길이에요"]
    else:
        t, sub = "상대 경로와 절대 경로", "현재 위치 기준인지, 사이트 기준점 기준인지 봐요"
        caps = ["지금 문서는 /data/index.html에 있어요", "..은 현재 위치보다 한 단계 위 폴더예요", "../images/logo.png로 logo.png를 찾아가요", "/로 시작하면 사이트 기준점에서 출발해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: document root and default document ----------
def page7(daily):
    a = Anim(4, dur(daily))
    body = [box(40, 130, 600, 330, LINE, PANEL, 16, sw=3) + text(70, 160, "도서관 건물 전체" if daily else "서버 컴퓨터의 디스크 전체", 17, MUTED, 700, "start"),
            box(60, 190, 190, 110, RED, BG, 10, sw=3) + text(155, 230, "직원실" if daily else "설정·비공개 파일", 16, RED, 700)
            + text(155, 260, "공개 안 해요" if daily else "웹에 공개 안 해요", 14, MUTED),
            box(280, 180, 340, 260, GREEN, BG, 12, sw=3) + text(450, 210, "열람실 (공개 구역)" if daily else "문서 루트 (공개 시작 폴더)", 17, GREEN, 700),
            cell(310, 240, 280, 50, "과학 서가/공룡책" if daily else "data/index.html", VIOLET, 16),
            cell(310, 320, 280, 50, "안내 책자 (기본)" if daily else "index.html (기본 문서)", BLUE, 16),
            person(830, 280, "나") if daily else laptop(830, 290, "브라우저"),
            a.vis(hl(40, 130, 600, 330, MUTED, 16), 1, 1),
            a.vis(hl(280, 180, 340, 260, GREEN, 12) + cross(250, 195), 2, 2),
            a.vis(msg(770, 620, 240, "과학 서가/공룡책" if daily else "/data/index.html", VIOLET, 15) + hl(310, 240, 280, 50, VIOLET, 8), 3, 3),
            a.vis(msg(770, 620, 330, "그냥 왔어요" if daily else "/", BLUE, 15) + hl(310, 320, 280, 50, BLUE, 8)
                  + text(800, 420, "무엇을 줄지는 도서관이 정해요" if daily else "기본 문서는 서버 설정이 정해요", 15, BLUE, 700), 4, 4)]
    if daily:
        t, sub = "공개된 열람실 안에서 찾아요", "건물 전체가 아니라 공개 구역 안에서 찾아요"
        caps = ["도서관 건물에는 여러 공간이 있어요", "손님에게는 열람실만 공개하고 직원실은 닫혀 있어요", "쪽지의 위치는 열람실 안에서 찾아요", "그냥 오면 도서관이 정한 안내 책자를 줘요"]
    else:
        t, sub = "웹 서버의 문서 루트", "주소의 경로는 공개한 루트 안에서 찾아요"
        caps = ["서버 컴퓨터의 디스크에는 여러 폴더가 있어요", "웹에 공개할 시작 폴더가 문서 루트예요", "/data/index.html은 루트 아래 data 폴더에서 찾아요", "/만 요청하면 서버 설정에 따라 기본 문서를 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: path is a request, not always a file ----------
def page8(daily):
    a = Anim(4, dur(daily))
    body = [person(110, 280, "나") if daily else laptop(110, 290, "클라이언트"),
            box(500, 130, 420, 330, LINE, PANEL, 16, sw=3) + text(710, 160, "도서관 창구" if daily else "서버", 18, MUTED, 700),
            role(530, 185, 360, 100, "서가에 꽂힌 책" if daily else "저장된 파일", "사진집" if daily else "images/logo.png", BLUE, 18),
            role(530, 320, 360, 110, "사서가 그때 만들기" if daily else "요청 처리 프로그램", "목록을 뽑아 줘요" if daily else "HTML 또는 JSON을 만들어요", ORANGE, 18),
            a.vis(msg(170, 525, 220, "사진집 주세요" if daily else "/images/logo.png", BLUE, 15) + hl(530, 185, 360, 100, BLUE, 12), 1, 1),
            mv(a, parcel(), [(520, 255), (180, 255)], 2, 2, 2),
            a.vis(text(340, 300, "있는 것을 그대로" if daily else "파일을 그대로 보내요", 15, BLUE, 700), 2, 2),
            a.vis(msg(170, 525, 220, "17번 회원 목록 주세요" if daily else "/products/17", ORANGE, 15)
                  + hl(530, 320, 360, 110, ORANGE, 12) + text(710, 300, "꽂힌 책은 없어요" if daily else "products/17 파일은 없어요", 14, RED, 700), 3, 3),
            mv(a, doc(0, -40, "목록" if daily else "JSON", ORANGE, 70, 80), [(520, 360), (270, 360)], 4, 4, 4, 0.1, 0.6),
            a.vis(text(300, 455, "모양만 보고 파일이라고 단정하지 않아요" if daily else "경로만 보고 파일이 있다고 단정하지 않아요", 16, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "꺼내 주기와 만들어 주기", "부탁하는 말이 늘 꽂힌 책 이름은 아니에요"
        caps = ["사진집을 부탁하면 서가에서 찾아요", "꽂혀 있던 사진집을 그대로 건네줘요", "17번 회원 목록은 서가에 꽂혀 있지 않아요", "사서가 그때 목록을 만들어 건네줘요"]
    else:
        t, sub = "URL 경로와 실제 파일", "경로는 요청 주소이고, 결과는 서버가 정해요"
        caps = ["클라이언트가 /images/logo.png를 요청해요", "서버가 저장된 이미지 파일을 그대로 보내요", "/products/17은 같은 이름의 파일이 없을 수 있어요", "프로그램이 처리해 HTML이나 JSON 응답을 만들어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: query = name=value pairs ----------
def page9(daily):
    a = Anim(4, dur(daily))
    s, pos = strip(daily)
    q = ["?", "검색어", "=", "공룡"] if daily else ["?", "search_keyword", "=", "Test"]
    ws = [40, tw(q[1], 18) + 30, 40, tw(q[3], 18) + 30]
    x0 = 480 - (sum(ws) + 12 + 130) / 2
    xs = [x0]
    for w in ws[:-1]:
        xs.append(xs[-1] + w + 4)
    big = "".join(cell(round(x), 230, round(w), 50, t_, c, 18) for x, w, t_, c in zip(xs, ws, q, [RED, VIOLET, MUTED, GREEN]))
    ex = xs[-1] + ws[-1] + 8
    body = [s,
            a.vis(mark(pos, 5, 140, 40, RED) + text(480, 210, "? 뒤가 조건이에요" if daily else "? 뒤가 query예요", 17, RED, 700), 1, 1),
            a.vis(big, 2, 4),
            a.vis(text(xs[1] + ws[1] / 2, 310, "이름 (매개변수)", 15, VIOLET, 700) + text(xs[3] + ws[3] / 2, 310, "값", 15, GREEN, 700), 2, 4),
            a.vis(cell(round(ex), 230, 130, 50, "&쪽=2" if daily else "&page=2", ORANGE, 18)
                  + text(ex + 65, 310, "& 로 이어 붙여요", 15, ORANGE, 700), 3, 4),
            a.vis(role(300, 350, 360, 90, "사서가 받은 조건" if daily else "서버가 받은 조건", "검색어 = 공룡, 쪽 = 2" if daily else "search_keyword = Test, page = 2", ORANGE, 17)
                  + text(820, 380, "서가 위치와는", 15, MUTED, 700) + text(820, 400, "다른 부분이에요", 15, MUTED, 700) if daily else
                  role(300, 350, 360, 90, "서버가 받은 조건", "search_keyword = Test, page = 2", ORANGE, 17)
                  + text(820, 380, "path와는", 15, MUTED, 700) + text(820, 400, "다른 부분이에요", 15, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "물음표 뒤에 조건을 적어요", "이름=값 모양으로 원하는 조건을 알려요"
        caps = ["쪽지의 ? 뒤에는 찾을 조건을 적어요", "검색어는 이름, 공룡은 그 값이에요", "조건을 더 붙이려면 &로 이어요", "사서는 서가 위치와 따로 조건을 받아요"]
    else:
        t, sub = "Query: 물음표 뒤의 조건", "이름=값 쌍으로 서버에 조건을 전달해요"
        caps = ["? 뒤의 search_keyword=Test가 query예요", "search_keyword는 매개변수, Test는 값이에요", "&로 이어 page=2 같은 조건을 더 붙여요", "서버는 path와 따로 이 조건들을 받아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 10: fragment = position inside the document ----------
def page10(daily):
    a = Anim(4, dur(daily))
    s, pos = strip(daily)
    sec = ["1장", "2장", "3장"] if daily else ["intro", "list", "result"]
    page = box(60, 210, 300, 250, LINE, PANEL, 12, sw=3) + text(210, 240, "공룡책" if daily else "받은 문서 (index.html)", 16, MUTED, 700)
    page += "".join(cell(90, 260 + i * 62, 240, 48, s_, MUTED, 16) for i, s_ in enumerate(sec))
    body = [s, person(860, 280, "사서") if daily else pc(860, 290, "서버"),
            a.vis(mark(pos, 6, 140, 40, TXT) + text(480, 210, "# 뒤는 책 안의 위치예요" if daily else "# 뒤는 문서 안의 위치예요", 17, TXT, 700), 1, 1),
            a.vis(msg(400, 800, 260, "공룡책 빌려 주세요" if daily else "/data/index.html?search_keyword=Test", BLUE, 14)
                  + text(600, 300, "3장은 말하지 않아요" if daily else "#result는 보통 보내지 않아요", 14, MUTED, 700), 2, 2),
            a.vis(page, 3, 4), mv(a, doc(0, -30, "", BLUE, 50, 60), [(800, 360), (400, 360)], 3, 3, 3, 0.1, 0.6),
            a.vis(hl(90, 384, 240, 48, GREEN, 8) + darrow(380, 330, 336, 400, GREEN, 4)
                  + text(560, 410, "내가 3장을 펼쳐요" if daily else "브라우저가 result 위치로 이동", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "빌린 책에서 3장을 펼쳐요", "책 속 위치는 책을 받은 뒤 내가 찾아요"
        caps = ["쪽지의 #3장은 책 안에서 펼칠 위치예요", "사서에게는 공룡책만 빌려 달라고 해요", "사서가 공룡책을 건네줘요", "책을 받은 뒤 내가 3장을 펼쳐요"]
    else:
        t, sub = "Fragment: 문서 안의 위치", "# 뒤는 문서 안에서 보여 줄 위치를 가리켜요"
        caps = ["#result는 문서 안에서 보여 줄 위치예요", "서버에는 path와 query로 문서를 요청해요", "서버가 index.html 문서를 돌려줘요", "브라우저가 문서 안의 result 위치로 이동해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l33-daily-name-tag-scope", "l33-uri-url-scope", page1, 0),
    ("l33-daily-library-items", "l33-web-resources", page2, 0),
    ("l33-daily-name-vs-address", "l33-identify-vs-locate", page3, 0),
    ("l33-daily-note-cells", "l33-url-part-split", page4, 0),
    ("l33-daily-method-building-desk", "l33-scheme-host-port", page5, 0),
    ("l33-daily-shelf-route", "l33-relative-absolute-path", page6, 1),
    ("l33-daily-open-reading-room", "l33-document-root-default", page7, 0),
    ("l33-daily-fetch-or-make", "l33-path-not-file", page8, 0),
    ("l33-daily-search-condition", "l33-query-name-value", page9, 0),
    ("l33-daily-open-chapter", "l33-fragment-in-page", page10, 0),
]

U = "https://www.test.co.kr:8080/data/index.html?search_keyword=Test#result"
COPY = {
    "l33-daily-name-tag-scope": ("이름표와 위치 쪽지",
        "책을 가리키는 이름표라는 큰 상자 안에, 찾아갈 위치와 방법까지 적은 쪽지라는 작은 상자가 나타나고 그 안에 도서관 쪽지 예시가 보입니다.",
        "위치 쪽지는 이름표의 한 종류이고, 이름표가 더 큰 범위입니다."),
    "l33-uri-url-scope": ("URI와 URL의 범위",
        f"URI라는 큰 범주 상자 안에 URL 상자가 나타나고, 그 안에 예시 주소 {U}가 보입니다. 마지막에는 URL이 URI 안에 들어간다고 표시됩니다.",
        "URI는 자원을 식별하는 큰 범주이고, URL은 위치와 접근 방법을 나타내는 URI입니다."),
    "l33-daily-library-items": ("도서관에서 받을 수 있는 것",
        "책, 사진집, 지도, DVD가 차례로 나타나고, 사서가 그때 뽑아 만드는 대출 목록이 이어서 나타납니다. 마지막에는 필요한 것을 각각 받아 모읍니다.",
        "도서관에서는 책뿐 아니라 여러 가지를 따로 받아 볼 수 있습니다."),
    "l33-web-resources": ("웹 자원의 여러 모습",
        "HTML 문서, CSS 디자인 파일, JavaScript 코드, JPG 사진, API가 그때 만드는 JSON 데이터가 차례로 나타나고, 마지막에 브라우저가 이 자원들을 모아 화면을 만듭니다.",
        "문서, 파일, 이미지, API 데이터처럼 웹에서 식별해 다룰 수 있는 것이 자원입니다."),
    "l33-daily-name-vs-address": ("누구인지와 어디 있는지",
        "민수라는 친구를 가운데 두고, 왼쪽에는 누구인지 알려 주는 이름과 신분 번호, 오른쪽에는 어디서 만날지 알려 주는 집 주소가 차례로 나타납니다.",
        "이름은 누구인지, 주소는 어디 있는지에 답합니다."),
    "l33-identify-vs-locate": ("식별과 위치 지정",
        "자원 하나를 가운데 두고, 왼쪽에는 어떤 자원인지 식별하는 URI, 오른쪽에는 어디서 어떻게 가져올지 알려 주는 URL이 차례로 나타납니다.",
        "자원은 대상이고, URI는 대상을 식별하며, URL은 접근할 위치를 알려 줍니다. 사람 비유는 이해를 돕기 위한 것입니다."),
    "l33-daily-note-cells": ("도서관 쪽지를 칸으로 나눠요",
        "도서관 쪽지 한 줄을 방법, 건물, 창구, 서가와 책, 조건, 책 속 위치 칸으로 나누고, 마지막에 창구 번호와 책 속 위치가 빠질 수 있다고 표시합니다.",
        "한 줄을 통째로 외우지 않고 칸마다 나누어 읽습니다."),
    "l33-url-part-split": ("주소를 부분으로 나누어 읽기",
        f"예시 주소 {U}에서 구분 기호를 찾고, scheme, host와 port를 묶은 authority, path, query, fragment로 나눕니다. 마지막에 port와 fragment가 생략될 수 있다고 표시됩니다.",
        "구분 기호를 따라 scheme·authority·path·query·fragment로 나누어 읽습니다."),
    "l33-daily-method-building-desk": ("방법, 건물, 창구",
        "도서관 쪽지에서 빌리기라는 방법, 한빛도서관이라는 건물, 8번 창구가 차례로 강조되고, 기본 창구라면 번호를 빼고 적는다고 표시됩니다.",
        "어떻게 요청할지, 어느 곳에 갈지, 어느 창구에서 볼지를 나누어 봅니다."),
    "l33-scheme-host-port": ("Scheme, Host, Port",
        "예시 주소에서 scheme https, host www.test.co.kr, port 8080이 차례로 강조되며 각각 요청 방식, 서버 이름, 서비스 번호로 설명됩니다. 마지막에 HTTPS 기본 포트 443이면 생략한다고 표시됩니다.",
        "Host는 서버 이름, Port는 서비스 번호, Path는 요청할 자원을 가리킵니다."),
    "l33-daily-shelf-route": ("지금 자리에서, 또는 입구에서",
        "과학 서가의 공룡책 앞에서 한 단계 위로 나간 뒤 사진 서가의 지도책으로 찾아가고, 마지막에는 도서관 입구부터 같은 지도책까지 가는 길이 표시됩니다.",
        "지금 위치에서 출발하는 길과 입구에서 출발하는 길을 구분합니다."),
    "l33-relative-absolute-path": ("상대 경로와 절대 경로",
        "/data/index.html에서 ../로 한 단계 위 폴더로 간 뒤 images/logo.png를 찾아가고, 마지막에는 /images/logo.png처럼 사이트 기준점에서 바로 출발하는 경로가 표시됩니다.",
        "상대 경로는 현재 위치를 기준으로, /로 시작하는 웹 경로는 사이트 기준점에서 시작합니다."),
    "l33-daily-open-reading-room": ("공개된 열람실 안에서 찾아요",
        "도서관 건물 안에서 직원실은 닫혀 있고 열람실만 공개됩니다. 과학 서가/공룡책 요청은 열람실 안에서 찾고, 그냥 온 손님에게는 도서관이 정한 안내 책자를 줍니다.",
        "손님의 요청은 공개된 열람실 안에서 찾습니다."),
    "l33-document-root-default": ("웹 서버의 문서 루트",
        "서버 디스크 전체 가운데 비공개 파일은 닫혀 있고 문서 루트만 공개됩니다. /data/index.html 요청은 루트 아래 data 폴더에서 찾고, / 요청에는 서버 설정이 정한 기본 문서 index.html을 줍니다.",
        "브라우저 경로는 서버가 공개한 웹 루트에서 시작하고, / 요청의 기본 문서는 서버가 정합니다."),
    "l33-daily-fetch-or-make": ("꺼내 주기와 만들어 주기",
        "사진집을 부탁하면 서가에 꽂힌 것을 그대로 건네주고, 17번 회원 목록을 부탁하면 꽂힌 책이 없어서 사서가 그때 목록을 만들어 건네줍니다.",
        "부탁하는 말이 늘 꽂혀 있는 책 이름과 같지는 않습니다."),
    "l33-path-not-file": ("URL 경로와 실제 파일",
        "클라이언트가 /images/logo.png를 요청하면 서버가 저장된 파일을 그대로 보내고, /products/17을 요청하면 같은 이름의 파일 없이 프로그램이 HTML이나 JSON 응답을 만들어 보냅니다.",
        "URL의 경로는 요청 주소이고, 서버가 파일을 보내거나 프로그램으로 결과를 만들 수 있습니다."),
    "l33-daily-search-condition": ("물음표 뒤에 조건을 적어요",
        "쪽지의 ?검색어=공룡에서 검색어는 이름, 공룡은 값으로 나뉘고, &쪽=2가 이어 붙습니다. 마지막에 사서가 서가 위치와 따로 두 조건을 받습니다.",
        "? 뒤에는 이름=값 모양으로 원하는 조건을 적습니다."),
    "l33-query-name-value": ("Query: 물음표 뒤의 조건",
        "예시 주소의 ?search_keyword=Test에서 search_keyword는 매개변수, Test는 값으로 나뉘고, &page=2가 이어 붙습니다. 마지막에 서버가 path와 따로 두 조건을 받습니다.",
        "? 뒤는 Query이고, 이름=값 쌍으로 서버에 조건을 전달합니다."),
    "l33-daily-open-chapter": ("빌린 책에서 3장을 펼쳐요",
        "쪽지의 #3장이 강조되고, 사서에게는 공룡책만 빌려 달라고 합니다. 책을 받은 뒤 내가 책 안의 3장을 펼칩니다.",
        "책 속 위치는 책을 받은 뒤 내가 찾습니다."),
    "l33-fragment-in-page": ("Fragment: 문서 안의 위치",
        "예시 주소의 #result가 강조되고, 서버에는 /data/index.html?search_keyword=Test로 문서를 요청합니다. 문서를 받은 뒤 브라우저가 문서 안의 result 위치로 이동합니다.",
        "# 뒤의 fragment는 문서 안의 위치를 가리킬 수 있습니다."),
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
