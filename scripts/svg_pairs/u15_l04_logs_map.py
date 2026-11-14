#!/usr/bin/env python3
"""Unit 15 Lesson 4 (로그·장치 지도·점검 마무리): 예시 SVG 6개(Page당 1개, 4단계). Run from repo root:
python3 scripts/svg_pairs/u15_l04_logs_map.py   (--svg-only: lesson.md는 건드리지 않음)

하나의 예: 새벽의 세 장비 로그를 SIEM이 이어 한 사건으로 읽고, 해외 고객 요청 하나를 장치 지도 위에 올린다.
마지막 Page는 Unit 11~15 장치(경로 안·경로 밖·대신 연결)를 한 장의 장치 지도로 되짚는다.
옛 learn-flow 그림(assets/diagrams/source-23.svg)은 Page에 붙이지 않고 그대로 둔다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

LESSON = lesson_dir(4)
OUT = LESSON / "assets" / "animations"


def logcard(x, y, who, t, what, c):
    return (box(x, y, 260, 84, c, PANEL, 8, sw=3) + text(x + 130, y + 30, f"{who} · {t}", 18, c, 700) + text(x + 130, y + 62, what, 15, TXT))


# 1 흩어진 로그를 이으면 무엇이 보일까? ---------------------------------------------------
def p1():
    a = new()
    cards = [logcard(60, 130, "NAC", "02:41", "미등록 기기 접속", ORANGE), logcard(350, 130, "방화벽", "02:45", "서버 22번 접속 거부 반복", BLUE),
             logcard(640, 130, "IPS", "02:49", "관리 화면 공격 패턴 경보", VIOLET)]
    siem = node(480, 335, "SIEM", GREEN, 130, 56, 20)
    lines = "".join(line(x, 214, 480, 307, GREEN, 2, "6 5") for x in (190, 480, 770))
    body = [a.vis("".join(cards), 1, 4), st(a, 2, lines + siem, bb(480, 335, 140, 66)), P(a, 2, 200, 335, "시각을 맞춰 시간순으로", BLUE, 15, False, 2),
            st(a, 3, cell(260, 395, 440, 46, "8분 안에 같은 출발지 3건 → 한 사건", GREEN, 17), (260, 395, 440, 46)),
            P(a, 3, 800, 335, "회의실 포트까지 역추적", GREEN, 15, False, 3, False),
            P(a, 4, 800, 335, "시계가 틀리면 순서가 뒤집혀요", RED, 15)]
    caps = ["세 장비에 로그가 따로 남아 있어요", "SIEM이 로그를 모아 시간순으로 엮어요", "같은 출발지의 세 기록이 한 사건이 돼요", "장비 시각이 맞아야 순서가 맞아요"]
    return frame(a, "흩어진 로그를 이으면", "NAC·방화벽·IPS 기록을 한 줄로", caps, "".join(body))


# 2 이 경보는 어떤 규칙이 울렸을까? -------------------------------------------------------
def p2():
    a = new()
    cells = [(60, 104, "alert", ORANGE), (170, 334, "tcp any any -> any 80", BLUE), (510, 404, '(content:"테스트"; sid:1000001;)', GREEN)]
    row = "".join(cell(x, 215, w, 60, t, c, 20 if i < 2 else 17) for i, (x, w, t, c) in enumerate(cells))
    body = [P(a, 1, 480, 160, "NIDS 규칙 한 줄", VIOLET, 18, False, 4, False), row, st(a, 1, "", (170, 215, 334, 60)),
            P(a, 1, 340, 320, "① 누가 어디로: TCP 80번", BLUE, 16, False, 1, False),
            st(a, 2, "", (510, 215, 404, 60), 2), P(a, 2, 715, 320, "② 찾는 것: '테스트'", GREEN, 16, False, 2, False),
            st(a, 3, "", (60, 215, 104, 60), 3), P(a, 3, 115, 320, "③ 동작: 경보만", ORANGE, 16, False, 3, False),
            P(a, 4, 480, 385, "정상 요청에도 울려서 오탐이 많아요", RED, 17), P(a, 4, 480, 435, "443 통신은 이 규칙의 범위 밖이에요", MUTED, 16, False, 4, False)]
    caps = ["규칙 한 줄을 세 덩어리로 나눠 읽어요", "괄호 안에서 무엇을 찾는지 읽어요", "맨 앞 동작으로 찾으면 무엇을 하는지 봐요", "단순한 규칙은 읽기 쉽지만 오탐이 많아요"]
    return frame(a, "이 경보는 어떤 규칙이 울렸을까", "누가 어디로 → 무엇을 → 무엇을 하나", caps, "".join(body))


# 3 규칙 하나 바꿨는데 왜 장애가 났을까? ---------------------------------------------------
def p3():
    a, Y = new(), 310
    base = (laptop(80, Y, "박 팀장") + line(135, Y, 210, Y, LINE, 3, "6 5") + wall(250, Y, "방화벽") + line(295, Y, 385, Y, LINE, 3, "6 5") + node(430, Y, "IPS", GREEN, 90, 56)
            + line(475, Y, 590, Y, LINE, 3, "6 5") + server(640, Y, "한결봇", sub="192.168.20.11–.13") + eye(430, 175) + text(430, 210, "NIDS", 15, MUTED) + line(430, 218, 430, 280, VIOLET, 2, "6 5"))
    logc = box(710, 130, 220, 86, ORANGE, PANEL, 8, sw=3) + text(820, 158, "변경 기록 한 줄", 16, ORANGE, 700) + text(820, 183, "누가·언제·IPS 규칙 갱신", 14, TXT) + text(820, 203, "→ 최근 바뀐 것부터 확인", 14, MUTED)
    body = [base, pk(a, 1, [(130, Y), (520, Y)], ORANGE, 0.05, 0.95), st(a, 1, cross(540, Y), None, 3), P(a, 1, 330, 420, "도면 업로드 실패", RED, 17, False, 1, False),
            st(a, 2, logc, (710, 130, 220, 86)),
            P(a, 3, 250, 175, "복사본만 봐서 후순위", VIOLET, 15),
            st(a, 4, check(540, Y), None), st(a, 4, "", bb(430, Y, 110, 76)), P(a, 4, 480, 420, "규칙을 되돌리니 업로드 성공", GREEN, 17)]
    caps = ["규칙 갱신 뒤 큰 도면 업로드가 실패해요", "변경 기록에서 최근 바뀐 것을 짚어요", "경로 밖 NIDS는 끊기 어려워 후순위예요", "IPS 규칙을 되돌리면 업로드가 돼요"]
    return frame(a, "규칙 하나 바꿨는데 장애가", "장치 위치로 의심 대상을 줄여요", caps, "".join(body))


# 4 한 장의 지도에 요청 하나를 올리면? ---------------------------------------------------
def p4():
    a, Y = new(), 285
    xs = [70, 215, 360, 505, 650, 830]
    road_ = line(110, Y, 790, Y, LINE, 4, "8 6")
    tag = lambda x, s: text(x, Y + 50, s, 14, MUTED)
    body = [road_,
            laptop(xs[0], Y, "192.0.2.77"), P(a, 1, 150, 200, "203.0.113.10:443", BLUE, 15, False, 1, False),
            st(a, 1, node(xs[1], Y, "UTM", GREEN, 96, 56) + tag(xs[1], "경로 안"), bb(xs[1], Y + 10, 110, 100), 4),
            pk(a, 1, [(110, Y), (190, Y)], BLUE),
            st(a, 2, node(xs[2], Y, "TLS 종료", BLUE, 96, 56, 16) + tag(xs[2], "대신 연결") + node(xs[3], Y, "WAF", BLUE, 96, 56) + tag(xs[3], "대신 연결"), (xs[2] - 52, Y - 32, xs[3] - xs[2] + 104, 100), 4),
            pk(a, 2, [(240, Y), (480, Y)], BLUE),
            st(a, 3, node(xs[4], Y, "IPS", GREEN, 96, 56) + tag(xs[4], "경로 안") + server(xs[5], Y, "서버 풀", sub="192.168.20.11–.13"), (xs[4] - 52, Y - 44, xs[5] - xs[4] + 104, 130), 4),
            pk(a, 3, [(530, Y), (790, Y)], BLUE), st(a, 3, check(xs[5], 195), None, 3),
            st(a, 4, eye(430, 410) + text(430, 442, "NIDS", 15, MUTED) + line(430, 395, 430, Y + 12, VIOLET, 2, "6 5"), bb(430, 420, 80, 70)),
            P(a, 4, 690, 420, "경로 밖: 복사본을 보고 경보만", VIOLET, 15, False, 4, False)]
    caps = ["해외 고객이 공개 주소로 요청을 보내요", "TLS를 끝내고 WAF가 풀린 요청을 봐요", "서버 구역 입구에서 IPS가 보고 서버 풀에 도착해요", "NIDS는 옆에서 복사본만 보고 경보를 내요"]
    return frame(a, "한 장의 지도에 요청 하나를", "경로 안·대신 연결·경로 밖으로 읽어요", caps, "".join(body))


# 5 장치마다 보는 층은 어떻게 다를까? ------------------------------------------------------
def p5():
    a = new()
    head, rows = rtable(40, 140, ["층", "보는 식별자", "대표 장치"],
                        [["L2", "MAC 주소", "NAC·스위치"], ["L3", "IP 주소", "라우터·패킷 필터"], ["L4", "포트·TCP 상태", "NAT·상태 추적 방화벽"], ["소켓 위", "URL·헤더·내용", "WAF·Proxy형 방화벽"]],
                        [110, 200, 330], [GREEN, BLUE, BLUE, VIOLET], 16)
    body = [head] + [a.vis(r[0], 1, 4) for r in rows] + [
        st(a, 2, "", rows[0][1], 2), P(a, 2, 805, 200, "MAC을 막아 주세요", ORANGE, 16, False, 2, False),
        st(a, 3, "", rows[3][1], 3), P(a, 3, 805, 330, "URL을 막아 주세요", ORANGE, 16, False, 3, False),
        P(a, 4, 480, 420, "위층일수록 깊게 보지만 느려요", ORANGE, 17)]
    caps = ["장치마다 보는 식별자가 층별로 달라요", "MAC을 막아 달라는 요청은 L2 장치 몫이에요", "URL을 막아 달라는 요청은 소켓 위 장치 몫이에요", "위층일수록 깊게 보지만 느려요"]
    return frame(a, "장치마다 보는 층", "요청의 정보가 어느 층에 있나", caps, "".join(body))


# 6 이제 안전하다고 답할 수 있을까? -- Unit 11~15 장치 지도 -------------------------------
def p6():
    a, Y = new(), 305
    base = (cloudi(70, Y, "인터넷") + line(138, Y, 207, Y, LINE, 3, "6 5"))
    step1 = (zone(110, 130, 240, 90, "사내 LAN · NAC ①", GREEN, 16) + text(230, 200, "192.168.10.0/24", 14, MUTED) + line(230, 220, 230, 268, LINE, 3, "6 5")
             + wall(250, Y, "방화벽 ②"))
    step2 = (zone(440, 150, 470, 270, "서버 구역 192.168.40.0/24", BLUE, 16) + line(292, Y, 500, Y, LINE, 3, "6 5") + node(540, Y, "IPS ③", VIOLET, 96, 56)
             + line(588, Y, 750, Y, LINE, 3, "6 5") + server(800, Y, "AI 서버", sub="192.168.40.50:8080") + eye(390, 190) + text(390, 224, "NIDS ③", 15, MUTED) + line(390, 236, 390, 298, VIOLET, 2, "6 5"))
    siem = node(150, 440, "SIEM ④", GREEN, 110, 44, 17)
    sl = (line(150, 418, 150, 232, GREEN, 2, "6 5") + line(190, 418, 235, Y + 36, GREEN, 2, "6 5") + line(205, 440, 540, 440, GREEN, 2, "6 5") + line(540, 440, 540, Y + 30, GREEN, 2, "6 5"))
    body = [base, a.vis(step1, 1, 4),
            st(a, 2, step2, (440, 150, 470, 270)),
            st(a, 3, siem + sl, bb(150, 440, 130, 60)),
            P(a, 4, 690, 125, "'다 막았다'가 아니라 '네 가지 점검'으로", ORANGE, 15)]
    caps = ["① NAC와 ② 방화벽이 바깥과 사내 사이를 지켜요", "③ IPS·NIDS가 서버 구역의 내용을 봐요", "④ SIEM이 모든 장치의 로그를 이어요", "안전하다는 말 대신 네 가지 점검으로 답해요"]
    return frame(a, "장치 지도로 점검을 되짚기", "이름이 아니라 위치와 역할로 읽어요", caps, "".join(body))


ITEMS = [
    ("u15-l04-p1-siem-timeline", "흩어진 로그를 이으면", "NAC 02:41, 방화벽 02:45, IPS 02:49 세 장비의 로그를 SIEM이 시간순으로 엮어 한 사건으로 읽고 회의실 포트까지 역추적하며, 장비 시각이 맞아야 한다는 전제를 보여 줍니다.", "SIEM은 여러 장비의 로그를 모아 시간순으로 엮어 사건을 추적하며 장비 시각 동기화가 전제입니다.", 4, p1),
    ("u15-l04-p2-rule-reading", "이 경보는 어떤 규칙이 울렸을까", "alert tcp any any -> any 80 규칙 한 줄을 누가 어디로, 무엇을 찾나, 찾으면 무엇을 하나의 순서로 나눠 읽는 모습입니다.", "규칙은 괄호 앞의 통신 조건, 괄호 안의 검사 내용, 맨 앞 동작 순으로 읽고, 단순한 규칙은 오탐이 많습니다.", 3, p2),
    ("u15-l04-p3-rule-change", "규칙 하나 바꿨는데 장애가", "IPS 규칙 갱신 뒤 도면 업로드가 실패하자 변경 기록으로 최근 바뀐 것을 확인하고, 경로 안 IPS를 의심해 규칙을 되돌려 해결하는 모습입니다.", "변경 기록과 장치 위치로 의심 대상을 줄이고 한 번에 하나씩 되돌려 확인합니다.", 2, p3),
    ("u15-l04-p4-device-map", "한 장의 지도에 요청 하나를", "해외 고객 192.0.2.77의 요청이 공개 주소 203.0.113.10:443에서 UTM, TLS 종료, WAF, IPS, 서버 풀 192.168.20.11–.13까지 지나고 NIDS가 옆에서 복사본만 보는 지도입니다.", "장치 이름이 아니라 경로 안·대신 연결·경로 밖의 위치로 읽으면 보이는 것과 할 수 있는 일이 정해집니다.", 2, p4),
    ("u15-l04-p5-layers", "장치마다 보는 층", "L2 MAC, L3 IP, L4 포트, 소켓 위 URL로 층마다 보는 식별자와 대표 장치를 표로 놓고, MAC 차단과 URL 차단 요청을 맡을 장치를 가르는 모습입니다.", "요청의 정보가 어느 층에 있는지 보고 그 층을 볼 수 있는 장치에 맡깁니다.", 1, p5),
    ("u15-l04-p6-unit-map", "장치 지도로 점검을 되짚기", "NAC, 방화벽, 서버 구역의 IPS·NIDS, 모든 장치의 로그를 모으는 SIEM을 한 장의 장치 지도에 놓고, 안전하다는 말 대신 네 가지 점검으로 답하는 모습입니다.", "점검은 네 질문으로 쪼개고, 장치는 이름이 아니라 위치와 역할로 읽습니다.", 2, p6),
]
assert len(ITEMS) == 6

if __name__ == "__main__":
    build(OUT, ITEMS)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", ITEMS)
    print("ok", len(ITEMS), "svgs")
