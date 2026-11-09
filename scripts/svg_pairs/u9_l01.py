#!/usr/bin/env python3
"""Unit 9 Lesson 1 (DNS) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u9_l01.py   (add --svg-only to skip the lesson.md edit).

Every page gets a daily-life SVG at the top (after_paragraph -1) and a network SVG with the same layout after the
first concept paragraph. The existing wiki `animations:` entries (pages 1, 2, 6) are left as they are; the new
items go into a separate `illustrations:` key on each page."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, person, dur
from u7_l01 import mv
from u10_l01 import role, msg, add_illustrations

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("06-web-fundamentals/lessons/01-*"))
OUT = LESSON / "assets" / "animations"


# ---------- Page 1: a name is not a location ----------
def page1(daily):
    a = Anim(4, dur(daily))
    L, M, R = 130, 480, 830
    body = [person(L, 290, "나") if daily else laptop(L, 300, "내 컴퓨터"),
            role(M - 120, 150, 240, 80, "안내 데스크" if daily else "DNS", "위치를 알려 줘요" if daily else "이름 → IP 주소", ORANGE),
            house(R, 290, "3층 2반 교실") if daily else pc(R, 300, "example.com 서버"),
            a.vis(pill(L, 200, "친구 이름: 민수" if daily else "example.com", BLUE, 16, True)
                  + text(480, 430, "이름만 알아서는 찾아갈 수 없어요" if daily else "이름만으로는 데이터를 보낼 수 없어요", 18, ORANGE, 700), 1, 1),
            a.vis(msg(L + 45, M - 125, 175, "민수 교실은?" if daily else "IP 주소는?", BLUE), 2, 3),
            a.vis(msg(M - 125, L + 45, 215, "3층 2반" if daily else "203.0.113.10 (예시)", GREEN), 3, 4),
            a.vis(line(L + 60, 300, R - 60, 300, LINE, 3, "8 6"), 4, 4),
            mv(a, pill(0, 0, "나", BLUE, 15, True) if daily else packet(0, 0), [(L + 60, 300), (R - 60, 300)], 4, 4, 4),
            a.vis(text(480, 430, "위치를 알아야 찾아갈 수 있어요" if daily else "한 이름이 여러 주소를 쓰거나 주소를 바꿀 수도 있어요", 18, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "친구 이름과 교실 위치", "이름만 알아서는 찾아갈 수 없어요"
        caps = ["나는 친구 이름만 알고 교실 위치는 몰라요", "안내 데스크에 친구 교실이 어디인지 물어요", "안내 데스크가 3층 2반이라는 위치를 알려 줘요", "위치를 알았으니 그 교실로 찾아가요"]
    else:
        t, sub = "DNS는 이름을 IP 주소로 바꿔요", "데이터를 보내려면 IP 주소가 필요해요"
        caps = ["브라우저에 example.com이라는 이름을 입력해요", "컴퓨터가 DNS에 이 이름의 IP 주소를 물어요", "DNS가 IP 주소 203.0.113.10(예시)을 알려 줘요", "컴퓨터가 그 IP 주소로 데이터를 보내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: nested name scopes ----------
def page2(daily):
    a = Anim(4, dur(daily))
    # (cell x, cell w, label, colour) from big to small scope
    if daily:
        segs = [(230, 150, "대한민국", BLUE), (410, 130, "서울시", GREEN), (570, 150, "한빛학교", ORANGE)]
        hint = "큰 범위부터 적어요 →"
        names = ["대한민국", "서울시", "한빛학교"]
        owners = ["나라가 관리", "서울시가 관리"]
    else:
        segs = [(580, 100, "com", BLUE), (420, 130, "example", GREEN), (300, 90, "www", ORANGE)]
        hint = "← 오른쪽이 큰 범위"
        names = ["com", "example.com", "www.example.com"]
        owners = ["com 담당 서버", "example.com 담당 서버"]
    row = "".join(cell(x, 118, w, 34, s, c, 18) for x, w, s, c in segs)
    if not daily:
        row += text(405, 142, ".", 24, TXT, 700) + text(565, 142, ".", 24, TXT, 700)
    rects = [(80, 180, 800, 230), (200, 225, 560, 160), (320, 270, 320, 90)]
    body = [row, text(800 if daily else 790, 141, hint, 16, MUTED, 700)]
    for k, ((x, y, w, h), (_, _, _, c)) in enumerate(zip(rects, segs), 1):
        lab = (text(x + 20, y + 29, names[k - 1], 18, c, 700, "start") if k < 3
               else text(480, y + 52, names[2], 20, c, 700))
        body.append(a.vis(box(x, y, w, h, c, PANEL if k == 1 else "none", 12, sw=3) + lab, k, 4))
        sx, sw_, _, _ = segs[k - 1]
        body.append(a.vis(hl(sx, 118, sw_, 34, c, 8), k, k))
    body += [a.vis(pill(760, 203, owners[0], BLUE, 14, True) + pill(660, 248, owners[1], GREEN, 14, True)
                   + text(480, 445, "한 곳에 몰지 않고 범위마다 나누어 맡아요 (분산)", 18, TXT, 700), 4, 4)]
    if daily:
        t, sub = "큰 범위에서 작은 범위로", "주소는 나라, 도시, 학교 순으로 좁혀요"
        caps = ["주소는 대한민국처럼 큰 범위에서 시작해요", "그 안에서 서울시로 범위를 좁혀요", "마지막으로 한빛학교를 찾아요", "범위마다 맡아서 관리하는 곳이 따로 있어요"]
    else:
        t, sub = "도메인 이름은 오른쪽이 큰 범위", "범위마다 다른 DNS 서버가 나누어 맡아요"
        caps = ["가장 오른쪽 com이 가장 큰 범위예요", "그 안에 example이라는 도메인이 있어요", "www는 example.com 안에서 쓰는 이름이에요", "범위마다 다른 DNS 서버가 나누어 맡아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: hosts file and cache before asking ----------
def page3(daily):
    a = Anim(4, dur(daily))
    hosts = ("내 수첩", "직접 적어 둔 위치") if daily else ("hosts 파일", "직접 적은 이름과 주소")
    cache = ("최근 메모", "전에 들은 답") if daily else ("DNS 캐시", "최근 조회한 답")
    body = [box(40, 140, 560, 290, LINE, PANEL, 14, sw=3) + text(120, 170, "나" if daily else "내 컴퓨터", 18, MUTED, 700),
            person(120, 290) if daily else laptop(120, 300),
            role(220, 185, 340, 90, *hosts, BLUE), role(220, 305, 340, 90, *cache, VIOLET),
            role(700, 240, 220, 90, "동네 안내소" if daily else "지정된 DNS 서버", "", ORANGE, 18),
            a.vis(hl(220, 185, 340, 90, BLUE, 12) + cross(530, 215), 1, 1),
            a.vis(cross(530, 215), 2, 4),
            a.vis(hl(220, 305, 340, 90, VIOLET, 12) + cross(530, 335), 2, 2),
            a.vis(cross(530, 335), 3, 3),
            a.vis(msg(600, 700, 268, "질문", ORANGE, 15) + hl(700, 240, 220, 90, ORANGE, 12), 3, 3),
            a.vis(msg(700, 600, 308, "답", GREEN, 15) + check(530, 335)
                  + pill(480, 456, "수첩은 직접 적은 것, 메모는 전에 들은 답" if daily else "hosts는 직접 적은 값, 캐시는 조회 결과", GREEN, 16, True), 4, 4)]
    if daily:
        t, sub = "먼저 내 수첩부터 봐요", "직접 적은 것과 전에 들은 답을 확인해요"
        caps = ["먼저 내 수첩에 직접 적어 둔 위치가 있는지 봐요", "최근에 들은 답을 적은 메모가 있는지도 봐요", "둘 다 없으면 동네 안내소에 물어봐요", "들은 답은 메모에 잠시 남겨 두어요"]
    else:
        t, sub = "hosts 파일과 DNS 캐시 먼저", "컴퓨터 안에 답이 없을 때 DNS 서버에 물어요"
        caps = ["먼저 hosts 파일에 직접 적은 주소가 있는지 봐요", "DNS 캐시에 최근 조회한 답이 있는지도 봐요", "둘 다 없으면 지정된 DNS 서버에 물어봐요", "받은 답은 DNS 캐시에 잠시 기억해 두어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: computer -> (router) -> configured DNS server -> others ----------
def page4(daily):
    a = Anim(4, dur(daily))
    body = [person(110, 280, "나") if daily else laptop(110, 290, "내 컴퓨터"),
            booth(340, 290, "경비실") if daily else router(340, 290, "공유기"),
            role(470, 245, 180, 90, "동네 안내소" if daily else "지정된 DNS 서버", "", ORANGE, 17),
            role(780, 245, 150, 90, "다른 안내소" if daily else "다른 DNS 서버", "", VIOLET, 17),
            a.vis(msg(110, 340, 200, "한빛학교는 어디?" if daily else "IP 주소는?", BLUE), 1, 4),
            a.vis(msg(340, 470, 200, "전달", MUTED) + text(340, 372, "전해 주기만 하기도 해요" if daily else "전달만 하기도 해요", 15, MUTED, 700), 2, 4),
            a.vis(msg(650, 780, 270, "물어요", VIOLET, 15) + msg(780, 650, 315, "답", VIOLET, 15)
                  + text(560, 372, "알면 바로, 모르면 찾아와요", 15, ORANGE, 700), 3, 4),
            a.vis(msg(560, 110, 420, "본관 3층이에요" if daily else "IP 주소 203.0.113.10 (예시)", GREEN), 4, 4)]
    if daily:
        t, sub = "동네 안내소에 물어봐요", "경비실은 질문을 전해 주기만 할 수도 있어요"
        caps = ["나는 한빛학교가 어디인지 물어보기 시작해요", "경비실이 질문을 안내소에 전해 주기도 해요", "동네 안내소가 모르면 다른 안내소에 물어봐요", "안내소가 찾은 답을 나에게 알려 줘요"]
    else:
        t, sub = "지정된 DNS 서버에 질의해요", "공유기는 질의를 전달만 할 수도 있어요"
        caps = ["컴퓨터가 이 이름의 IP 주소를 묻는 질의를 시작해요", "집에서는 공유기가 질의를 전달하기도 해요", "지정된 DNS 서버가 모르면 다른 DNS 서버에 물어요", "찾은 답을 지정된 DNS 서버가 컴퓨터에 돌려줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: root -> TLD -> authoritative ----------
def page5(daily):
    a = Anim(4, dur(daily))
    if daily:
        rows = [("전국 안내소", "서울시 안내소로 가세요"), ("서울시 안내소", "한빛학교 교무실로 가세요"), ("한빛학교 교무실", "2반은 본관 3층이에요")]
    else:
        rows = [("루트 DNS 서버", ".com 서버에 물어보세요"), (".com 서버", "example.com 담당에 물어보세요"),
                ("example.com 담당", "www.example.com = 203.0.113.10 (예시)")]
    cols = [BLUE, GREEN, ORANGE]
    body = [role(40, 200, 200, 100, "동네 안내소" if daily else "지정된 DNS 서버", "답을 모르면 따라가요", MUTED, 17)]
    for k, ((name, reply), c) in enumerate(zip(rows, cols), 1):
        y = 130 + (k - 1) * 110
        cy = y + 40
        body.append(role(640, y, 280, 80, name, "", c, 18))
        body.append(a.vis(arrow(250, 630, cy - 16, BLUE, 4) + arrow(630, 250, cy + 16, c, 4)
                          + pill(440, cy + 16, reply, c, 14, True), k, 4))
        body.append(a.vis(hl(640, y, 280, 80, c, 12), k, k))
    body.append(a.vis(hl(640, 350, 280, 80, ORANGE, 12) + check(140, 335)
                      + text(140, 380, "담당이 최종 답을 줘요", 16, ORANGE, 700)
                      + text(140, 405, "앞 단계는 방향만 알려 줘요", 15, MUTED, 700), 4, 4))
    if daily:
        t, sub = "안내소를 따라 좁혀 가요", "마지막 담당 교무실이 정확한 답을 줘요"
        caps = ["전국 안내소는 서울시 안내소로 가라고 알려 줘요", "서울시 안내소는 한빛학교 교무실을 알려 줘요", "한빛학교 교무실이 2반 위치를 정확히 알려 줘요", "앞 단계는 방향을, 담당 교무실은 답을 알려 줘요"]
    else:
        t, sub = "루트부터 담당 DNS 서버까지", "앞 단계는 다음에 물을 서버를 알려 줘요"
        caps = ["루트 DNS 서버는 .com을 맡은 서버를 알려 줘요", ".com 서버는 example.com 담당 서버를 알려 줘요", "example.com 담당 DNS 서버가 최종 답을 줘요", "앞 단계는 방향을, 담당 서버는 답을 알려 줘요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: cache with TTL ----------
def page6(daily):
    a = Anim(4, dur(daily))
    entry = "한빛학교 2반 → 본관 3층" if daily else "example.com → 203.0.113.10"
    left = ["남은 시간 5분", "남은 시간 2분", "0분: 시간 지남", "새로 적음: 5분"] if daily else \
           ["TTL 남은 시간 300초", "TTL 남은 시간 120초", "TTL 0초: 만료", "새 답: TTL 300초"]
    state = [GREEN, GREEN, RED, GREEN]

    def card(k):
        c = state[k - 1]
        return (box(330, 240, 270, 120, c, BG, 10, sw=3) + text(465, 268, "메모" if daily else "DNS 캐시", 15, MUTED, 700)
                + text(465, 300, entry, 16, TXT if c == GREEN else MUTED, 700) + text(465, 336, left[k - 1], 18, c, 700))

    body = [person(110, 280, "나") if daily else laptop(110, 290, "내 컴퓨터"),
            box(310, 160, 310, 250, ORANGE, PANEL, 14, sw=3) + text(465, 192, "동네 안내소" if daily else "지정된 DNS 서버", 18, ORANGE, 700),
            role(740, 245, 190, 90, "한빛학교 교무실" if daily else "담당 DNS 서버", "", VIOLET, 17)]
    body += [a.vis(card(k), k, k) for k in range(1, 5)]
    body += [a.vis(msg(740, 620, 250, "답 · 5분 유효" if daily else "답 · TTL 300초", VIOLET, 14), 1, 1),
             a.vis(msg(165, 310, 210, "같은 질문", BLUE, 14) + msg(310, 165, 250, "메모 보고 바로" if daily else "캐시에서 바로", GREEN, 14), 2, 2),
             a.vis(text(465, 440, "오래된 답을 계속 쓰지 않아요", 18, RED, 700), 3, 3),
             a.vis(msg(620, 740, 210, "다시 물어요", ORANGE, 14) + msg(740, 620, 250, "새 답", VIOLET, 14), 4, 4)]
    if daily:
        t, sub = "메모에 유효 시간을 적어요", "시간이 지나면 다시 물어봐요"
        caps = ["교무실의 답을 5분 동안 쓸 수 있다고 메모해요", "같은 질문이 오면 메모를 보고 바로 답해요", "5분이 지나면 그 메모는 더 쓰지 않아요", "다시 물어서 새 답을 받고 시간을 새로 세요"]
    else:
        t, sub = "DNS 캐시와 TTL", "TTL 동안만 답을 기억해요"
        caps = ["담당 서버의 답을 TTL 300초와 함께 캐시에 넣어요", "같은 이름을 다시 물으면 캐시에서 바로 답해요", "TTL이 다 지나면 그 답은 더 쓰지 않아요", "다시 조회해 새 답을 받고 TTL을 새로 세요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: DNS failure vs connection failure ----------
def page7(daily):
    a = Anim(4, dur(daily))
    body = [person(110, 280, "나") if daily else laptop(110, 290, "내 컴퓨터"),
            role(330, 140, 240, 80, "주 안내소" if daily else "주 DNS 서버", "", ORANGE, 18),
            role(330, 330, 240, 80, "보조 안내소" if daily else "보조 DNS 서버", "", GREEN, 18),
            house(820, 170, "한빛학교") if daily else pc(820, 180, "진짜 서버"),
            house(820, 315, "엉뚱한 건물", RED) if daily else pc(820, 310, "엉뚱한 서버"),
            a.vis(msg(170, 330, 180, "질문" if daily else "이름 질의", BLUE, 14) + cross(600, 180)
                  + text(450, 255, "응답 없음", 17, ORANGE, 700), 1, 1),
            a.vis(msg(170, 330, 355, "다시 질문" if daily else "다시 질의", BLUE, 14) + msg(330, 170, 392, "위치" if daily else "주소", GREEN, 14)
                  + check(600, 370), 2, 2),
            a.vis(msg(170, 770, 300, "가짜 답을 믿고 엉뚱한 곳으로" if daily else "변조된 답을 믿고 엉뚱한 주소로", RED, 15) + hl(768, 262, 104, 72, RED, 10), 3, 3),
            a.vis(box(300, 125, 300, 300, ORANGE, "none", 14, dash=True, sw=3) + box(680, 125, 260, 300, BLUE, "none", 14, dash=True, sw=3)
                  + pill(450, 448, "① 위치 알아내기" if daily else "① 이름 → 주소", ORANGE, 15, True)
                  + pill(810, 448, "② 찾아가기" if daily else "② 주소로 연결", BLUE, 15, True), 4, 4)]
    if daily:
        t, sub = "안내가 막히거나 틀리면", "위치 알아내기와 찾아가기를 나누어 봐요"
        caps = ["주 안내소가 대답하지 않으면 위치를 알 수 없어요", "보조 안내소가 대신 알려 줄 수 있어요", "가짜 안내는 그럴듯한 엉뚱한 위치를 알려 줘요", "위치 알아내기와 찾아가기를 나누어 살펴봐요"]
    else:
        t, sub = "DNS 문제와 연결 문제 구분", "이름 조회가 막히면 이름으로 접속하기 어려워요"
        caps = ["주 DNS 서버가 응답하지 않으면 이름 조회가 막혀요", "보조 DNS 서버가 대신 응답을 도울 수 있어요", "DNS 변조는 정상처럼 보이는 가짜 답을 보내요", "이름 조회와 그 뒤의 연결을 나누어 살펴봐요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l31-daily-friend-classroom", "l31-dns-name-to-ip", page1, 0),
    ("l31-daily-address-scope", "l31-domain-name-scope", page2, 0),
    ("l31-daily-notebook-first", "l31-hosts-cache-first", page3, 0),
    ("l31-daily-ask-local-desk", "l31-local-dns-server-query", page4, 0),
    ("l31-daily-follow-desks", "l31-root-tld-authoritative", page5, 0),
    ("l31-daily-memo-expiry", "l31-cache-ttl-expiry", page6, 0),
    ("l31-daily-desk-down-or-wrong", "l31-dns-failure-split", page7, 0),
]

COPY = {
    "l31-daily-friend-classroom": ("친구 이름과 교실 위치",
        "나는 친구 민수의 이름만 알고 교실 위치는 모릅니다. 안내 데스크에 민수 교실이 어디인지 묻고 3층 2반이라는 위치를 들은 뒤, 그 위치를 따라 교실로 찾아갑니다.",
        "이름만 알아서는 찾아갈 수 없고, 위치를 알아야 찾아갈 수 있습니다."),
    "l31-dns-name-to-ip": ("DNS는 이름을 IP 주소로 바꿔요",
        "브라우저에 example.com을 입력하면 컴퓨터가 DNS에 이 이름의 IP 주소를 묻고, 예시 주소 203.0.113.10을 받아 그 주소의 서버로 데이터를 보냅니다. 한 이름이 여러 주소를 쓰거나 주소를 바꿀 수도 있다고 표시됩니다.",
        "데이터를 보내려면 IP 주소가 필요하고, DNS는 이름에 맞는 주소를 찾아 줍니다. 주소는 예시입니다."),
    "l31-daily-address-scope": ("큰 범위에서 작은 범위로",
        "대한민국, 서울시, 한빛학교가 차례로 강조되며 큰 상자 안에 더 작은 상자가 하나씩 들어갑니다. 마지막에는 나라와 서울시가 각 범위를 맡아 관리한다고 표시됩니다.",
        "주소는 큰 범위에서 작은 범위로 좁혀 가며, 범위마다 맡아 관리하는 곳이 따로 있습니다."),
    "l31-domain-name-scope": ("도메인 이름은 오른쪽이 큰 범위",
        "www.example.com에서 오른쪽의 com, 그 안의 example, 마지막으로 www가 차례로 강조되며 큰 상자 안에 작은 상자가 들어갑니다. 마지막에는 com과 example.com을 각각 다른 담당 서버가 나누어 맡는다고 표시됩니다.",
        "도메인 이름은 오른쪽이 큰 범위이고, DNS 정보는 여러 서버가 범위를 나누어 관리합니다.", 0),
    "l31-daily-notebook-first": ("먼저 내 수첩부터 봐요",
        "나는 먼저 직접 적어 둔 수첩을 보고, 다음으로 전에 들은 답을 적은 최근 메모를 봅니다. 둘 다 없어서 동네 안내소에 묻고, 들은 답을 메모에 잠시 남깁니다.",
        "직접 적어 둔 수첩과 전에 들은 답을 적은 메모를 먼저 보고, 없으면 밖에 묻습니다."),
    "l31-hosts-cache-first": ("hosts 파일과 DNS 캐시 먼저",
        "컴퓨터가 먼저 직접 적은 이름과 주소의 목록인 hosts 파일을 보고, 다음으로 최근 조회한 답이 있는 DNS 캐시를 봅니다. 둘 다 없어서 지정된 DNS 서버에 묻고, 받은 답을 DNS 캐시에 잠시 기억합니다.",
        "hosts는 직접 적은 값이고 캐시는 조회 결과입니다. 확인 순서는 운영체제와 설정에 따라 다를 수 있습니다.", 0),
    "l31-daily-ask-local-desk": ("동네 안내소에 물어봐요",
        "나는 한빛학교가 어디인지 묻고, 경비실이 그 질문을 동네 안내소에 전해 줍니다. 동네 안내소는 알면 바로, 모르면 다른 안내소에 물어 답을 찾아오고, 본관 3층이라는 답을 나에게 알려 줍니다.",
        "질문은 내가 시작하고, 경비실은 전해 주기만 할 수 있으며, 답은 안내소가 찾아 줍니다."),
    "l31-local-dns-server-query": ("지정된 DNS 서버에 질의해요",
        "컴퓨터가 이름의 IP 주소를 묻는 질의를 시작하고, 공유기가 이 질의를 지정된 DNS 서버에 전달합니다. 지정된 DNS 서버는 알면 바로 답하고 모르면 다른 DNS 서버에 물어 답을 찾은 뒤, 예시 주소 203.0.113.10을 컴퓨터에 돌려줍니다.",
        "컴퓨터는 질의를 시작하고, 지정된 DNS 서버가 답을 돌려줍니다. 공유기는 질의를 전달만 할 수도 있습니다.", 0),
    "l31-daily-follow-desks": ("안내소를 따라 좁혀 가요",
        "답을 모르는 동네 안내소가 전국 안내소에 물으면 서울시 안내소를 알려 주고, 서울시 안내소는 한빛학교 교무실을 알려 주며, 한빛학교 교무실이 2반은 본관 3층이라고 정확히 알려 줍니다.",
        "앞 단계의 안내소는 방향만 알려 주고, 마지막 담당 교무실이 정확한 답을 줍니다."),
    "l31-root-tld-authoritative": ("루트부터 담당 DNS 서버까지",
        "지정된 DNS 서버가 루트 DNS 서버에 물으면 .com 서버를 안내받고, .com 서버는 example.com 담당 서버를 안내하며, example.com 담당 DNS 서버가 www.example.com의 예시 주소 203.0.113.10을 알려 줍니다.",
        "앞 단계의 서버는 다음에 물을 서버를 알려 주고, 담당 DNS 서버가 최종 답을 줍니다. 주소는 예시입니다.", 0),
    "l31-daily-memo-expiry": ("메모에 유효 시간을 적어요",
        "동네 안내소가 교무실의 답을 5분 동안 쓸 수 있다고 메모하고, 같은 질문이 오면 메모를 보고 바로 답합니다. 5분이 지나면 그 메모를 더 쓰지 않고, 다시 물어 새 답을 받고 시간을 새로 셉니다.",
        "메모에 유효 시간을 적어 두면 빨리 답할 수 있고, 시간이 지나면 다시 물어봅니다."),
    "l31-cache-ttl-expiry": ("DNS 캐시와 TTL",
        "지정된 DNS 서버가 담당 서버의 답을 TTL 300초와 함께 캐시에 넣고, 같은 이름을 다시 물으면 캐시에서 바로 답합니다. TTL이 0초가 되면 그 답은 만료되어 더 쓰지 않고, 다시 조회해 새 답을 받으면 TTL을 새로 셉니다.",
        "DNS 캐시는 조회를 빠르게 하고, TTL은 답을 기억할 시간을 정합니다. 300초는 예시입니다.", 0),
    "l31-daily-desk-down-or-wrong": ("안내가 막히거나 틀리면",
        "주 안내소가 대답하지 않으면 위치를 알 수 없고, 보조 안내소가 대신 알려 줄 수 있습니다. 가짜 안내를 믿으면 한빛학교가 아닌 엉뚱한 건물로 가게 됩니다. 마지막에는 위치 알아내기와 찾아가기가 두 단계로 나뉘어 표시됩니다.",
        "위치를 알아내는 단계와 찾아가는 단계를 나누어 보면 어디서 막혔는지 알 수 있습니다."),
    "l31-dns-failure-split": ("DNS 문제와 연결 문제 구분",
        "주 DNS 서버가 응답하지 않으면 이름 조회가 막히고, 보조 DNS 서버가 대신 응답을 도울 수 있습니다. DNS 변조가 일어나면 정상처럼 보이는 답을 믿고 진짜 서버가 아닌 엉뚱한 서버로 연결됩니다. 마지막에는 이름을 주소로 바꾸는 단계와 주소로 연결하는 단계가 나뉘어 표시됩니다.",
        "사이트 이름이 열리지 않으면 DNS 조회와 그 뒤의 연결을 나누어 살펴봅니다.", 0),
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
