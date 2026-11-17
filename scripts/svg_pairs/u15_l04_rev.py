#!/usr/bin/env python3
"""Unit 15 Lesson 4 SVG 점검 개정판(Page 1·3·4·5·6). Run from repo root:
python3 scripts/svg_pairs/u15_l04_rev.py   (--svg-only: lesson.md는 건드리지 않음)

Page 2(규칙 읽기)는 기존 u15-l04-p2-rule-reading.svg를 그대로 쓴다. 옛 파일은 지우지 않고 Page에서만 뺀다.
Page 4는 요청 경로 + TLS 앞뒤 센서(두 번째 그림), Page 6은 네 가지 점검 + 다섯 Unit 되짚기(두 번째 그림)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u15_l00_common import *  # noqa: F401,F403

LESSON = lesson_dir(4)
OUT = LESSON / "assets" / "animations"
IP = "192.168.10.77"


def spk(x, y, c=BLUE):
    """작은 패킷(32x22). 아이콘 사이 빈 칸에 가만히 놓아 라벨을 가리지 않는다."""
    return (f'<rect x="{x - 16}" y="{y - 11}" width="32" height="22" rx="4" fill="{c}"/>'
            f'<path d="M{x - 16} {y - 10} l16 10 l16 -10" fill="none" stroke="{BG}" stroke-width="2"/>')


def ghost(x, y, w=84, h=56):
    return box(x - w / 2, y - h / 2, w, h, LINE, "none", 8, dash=True, sw=2) + text(x, y + 8, "?", 22, LINE, 700)


def darrow(x, y0, y1, c):
    return line(x, y0, x, y1 - 12, c, 4) + f'<polygon points="{x},{y1} {x - 9},{y1 - 14} {x + 9},{y1 - 14}" fill="{c}"/>'


# 1 흩어진 로그를 이으면 -------------------------------------------------------------------
def logcard(x, y, who, t, l1, l2, c):
    return (box(x, y, 280, 112, c, PANEL, 8, sw=3) + text(x + 140, y + 32, f"{who} · {t}", 20, c, 700)
            + text(x + 140, y + 64, l1, 16, TXT) + text(x + 140, y + 90, l2, 16, TXT))


def p1():
    a = new()
    cards = (logcard(40, 124, "NAC", "02:41", "회의실 포트에 미등록 기기 접속", f"DHCP가 {IP} 부여", ORANGE)
             + logcard(340, 124, "방화벽", "02:45", f"{IP} → 그룹웨어 서버 22번", "접속 거부 반복", BLUE)
             + logcard(640, 124, "IPS", "02:49", f"{IP}에서 온", "관리 화면 공격 패턴 경보", VIOLET))
    siem = node(480, 335, "SIEM", GREEN, 150, 56, 22)
    lines = "".join(line(x, 236, 480, 307, GREEN, 2, "6 5") for x in (180, 480, 780))
    body = [a.vis(cards, 1, 4),
            st(a, 2, lines + siem, bb(480, 335, 160, 66)), P(a, 2, 190, 335, "시각을 맞춰 시간순으로", BLUE, 16, False, 2),
            st(a, 3, cell(190, 392, 580, 50, f"같은 출발지 {IP} · 8분 안에 3건 → 한 사건", GREEN, 18), (190, 392, 580, 50)),
            P(a, 3, 800, 335, "회의실 포트까지 역추적", GREEN, 16, False, 3, False),
            P(a, 4, 790, 335, "시계가 틀리면 순서가 뒤집혀요", RED, 16)]
    caps = ["세 장비에 로그가 따로 남아 있어요", "SIEM이 로그를 모아 시간순으로 엮어요", "같은 출발지의 세 기록이 한 사건이 돼요", "장비 시각이 맞아야 순서가 맞아요"]
    return frame(a, "흩어진 로그를 이으면", "NAC·방화벽·IPS 기록을 한 줄로", caps, "".join(body))


# 3 규칙 하나 바꿨는데 왜 장애가 났을까 ---------------------------------------------------
def p3():
    a, Y = new(), 320
    path = (laptop(70, Y, "박 팀장") + line(125, Y, 175, Y, LINE, 3, "6 5") + wall(220, Y, "방화벽")
            + line(262, Y, 330, Y, LINE, 3, "6 5") + node(380, Y, "IPS", GREEN, 96, 56, 20)
            + line(428, Y, 520, Y, LINE, 3, "6 5") + server(555, Y, "예약·문의 사이트", sub="192.168.20.11–.13"))
    nids = eye(380, 190) + text(380, 232, "NIDS", 16, MUTED) + line(380, 244, 380, 290, VIOLET, 2, "6 5")
    logc = (box(640, 140, 290, 104, ORANGE, PANEL, 8, sw=3) + text(785, 170, "변경 기록 한 줄", 18, ORANGE, 700)
            + text(785, 197, "누가·언제·IPS 규칙 갱신", 16, TXT) + text(785, 222, "→ 최근 바뀐 것부터 확인", 16, MUTED))
    body = [path, nids,
            st(a, 1, cross(474, Y), None, 3), P(a, 1, 330, 430, "첨부 업로드 실패", RED, 18, False, 1, False),
            st(a, 2, logc + line(640, 236, 428, 296, ORANGE, 3, "6 5"), (640, 140, 290, 104)),
            P(a, 3, 170, 190, "경로 밖: 복사본만 봐서 후순위", VIOLET, 16, False, 3),
            st(a, 4, check(474, Y), None), st(a, 4, "", bb(380, Y, 110, 76)), P(a, 4, 380, 430, "규칙을 되돌리니 업로드 성공", GREEN, 18)]
    caps = ["규칙 갱신 뒤 큰 첨부 파일 업로드가 실패해요", "변경 기록에서 최근 바뀐 것을 짚어요", "경로 밖 NIDS는 끊기 어려워 후순위예요", "IPS 규칙을 되돌리면 업로드가 돼요"]
    return frame(a, "규칙 하나 바꿨는데 장애가", "장치 위치로 의심 대상을 줄여요", caps, "".join(body))


# 4 한 장의 지도에 요청 하나를 올리면 ----------------------------------------------------
def p4():
    a, Y = new(), 290
    X = dict(me=55, utm=200, tls=330, waf=460, ips=590, pool=800)
    tag = lambda x, s, c: text(x, Y + 52, s, 16, c, 700)
    ghosts = "".join(ghost(X[k], Y) for k in ("tls", "waf", "ips")) + box(X["pool"] - 34, Y - 40, 68, 80, LINE, "none", 8, dash=True, sw=2)
    body = [line(107, Y, 766, Y, LINE, 4, "8 6"), ghosts, laptop(X["me"], Y, "192.0.2.77"),
            P(a, 1, 150, 190, "공개 주소 203.0.113.10:443", BLUE, 16, False, 1, False),
            st(a, 1, node(X["utm"], Y, "UTM", GREEN, 84, 56, 18) + tag(X["utm"], "경로 안", GREEN), bb(X["utm"], Y + 10, 110, 100), 4),
            a.vis(spk(132, Y), 1, 1),
            st(a, 2, node(X["tls"], Y, "TLS 종료", BLUE, 84, 56, 16) + tag(X["tls"], "대신 연결", BLUE)
               + node(X["waf"], Y, "WAF", BLUE, 84, 56, 18) + tag(X["waf"], "대신 연결", BLUE), (282, Y - 32, 226, 100), 4),
            a.vis(spk(525, Y), 2, 2),
            st(a, 3, node(X["ips"], Y, "IPS", GREEN, 84, 56, 18) + tag(X["ips"], "경로 안", GREEN) + server(X["pool"], Y, "서버 풀", sub="192.168.20.11–.13"),
               (542, Y - 48, 332, 142), 4),
            a.vis(spk(690, Y), 3, 3), st(a, 3, check(X["pool"], 215), None, 3),
            st(a, 4, eye(525, 405) + text(525, 440, "NIDS", 16, MUTED) + line(525, 390, 525, Y + 12, VIOLET, 2, "6 5"), bb(525, 415, 80, 80)),
            P(a, 4, 760, 410, "경로 밖: 복사본만 보고 경보를 내요", VIOLET, 16, False, 4, False)]
    caps = ["해외 고객이 공개 주소로 요청을 보내요", "TLS를 끝내고 WAF가 풀린 요청을 봐요", "서버 구역 입구에서 IPS가 보고 서버 풀에 도착해요", "NIDS는 옆에서 복사본만 보고 경보를 내요"]
    return frame(a, "한 장의 지도에 요청 하나를", "경로 안·대신 연결·경로 밖으로 읽어요", caps, "".join(body))


# 4b 같은 공격 문자열, 센서 두 곳 ---------------------------------------------------------
def p4b():
    a, Y = new(), 330
    sealed = lambda x: spk(x, Y) + lock(x, Y + 40)
    sensor = lambda x, name: eye(x, 218) + text(x, 254, name, 16, MUTED) + line(x, 266, x, Y - 6, VIOLET, 2, "6 5")
    bubble = lambda x, l1, l2, c: (box(x - 105, 118, 210, 64, c, PANEL, 10, sw=3) + text(x, 144, l1, 18, c, 700) + text(x, 168, l2, 16, TXT))
    body = [line(107, Y, 766, Y, LINE, 4, "8 6"), laptop(55, Y, "192.0.2.77"),
            node(330, Y, "TLS 종료", BLUE, 84, 56, 16) + text(330, Y + 52, "대신 연결", 16, BLUE, 700),
            node(460, Y, "WAF", BLUE, 84, 56, 18) + text(460, Y + 52, "대신 연결", 16, BLUE, 700),
            server(800, Y, "서버 풀"),
            sensor(200, "인터넷 쪽 센서"), sensor(590, "WAF 뒤 센서"),
            a.vis(sealed(140), 1, 1), a.vis(sealed(244), 2, 2), a.vis(spk(545, Y, RED), 3, 3),
            P(a, 1, 480, 440, "같은 공격 문자열, 센서 두 곳", BLUE, 18, False, 1, False),
            st(a, 2, bubble(200, "암호문만 보여요", "경보 없음", MUTED), (95, 118, 210, 64)),
            st(a, 3, bubble(590, "공격 문자열이 보여요", "경보!", RED), (485, 118, 210, 64)),
            P(a, 4, 480, 440, "TLS를 끝낸 뒤에야 내용이 보여요", GREEN, 18)]
    caps = ["같은 공격 문자열을 담아 센서 두 곳을 지나게 해요", "TLS 종료 앞 센서는 암호문만 봐요", "WAF 뒤 센서는 풀린 요청을 보고 경보를 내요", "TLS를 끝낸 뒤에야 내용을 볼 수 있어요"]
    return frame(a, "같은 공격 문자열, 센서 두 곳", "센서가 놓인 자리가 보이는 것을 정해요", caps, "".join(body))


# 5 장치마다 보는 층 ------------------------------------------------------------------------
def p5():
    a = new()
    cols = [("L2", "MAC 주소", ["NAC·스위치"], GREEN), ("L3", "IP 주소", ["라우터·패킷 필터"], BLUE),
            ("L4", "포트·TCP 상태", ["NAT·상태 추적", "방화벽"], BLUE), ("소켓 위", "URL·헤더·내용", ["WAF·Proxy형", "방화벽"], VIOLET)]
    X = [40 + i * 224 for i in range(4)]
    base = ""
    for x, (layer, ident, devs, c) in zip(X, cols):
        base += (text(x + 104, 152, layer, 22, c, 700) + cell(x, 168, 208, 62, ident, c, 18)
                 + line(x + 104, 230, x + 104, 292, c, 3, "6 5")
                 + box(x, 296, 208, 66, c, PANEL, 8, sw=3)
                 + "".join(text(x + 104, 296 + (33 + 6 if len(devs) == 1 else 27 + i * 22), d, 16, c, 700) for i, d in enumerate(devs)))
    col = lambda i: (X[i] - 4, 134, 216, 232)
    body = [base,
            st(a, 2, "", col(0), 2), P(a, 2, X[0] + 104, 410, "MAC을 막아 주세요", ORANGE, 18, False, 2, False),
            st(a, 3, "", col(3), 3), P(a, 3, X[3] + 104, 410, "URL을 막아 주세요", ORANGE, 18, False, 3, False),
            st(a, 4, line(70, 404, 880, 404, LINE, 4) + f'<polygon points="900,404 876,392 876,416" fill="{LINE}"/>'
               + text(70, 440, "빠르지만 내용을 몰라요", 18, GREEN, 700, "start") + text(890, 440, "깊게 보지만 느려요", 18, VIOLET, 700, "end"), (60, 392, 840, 62))]
    caps = ["장치마다 보는 식별자가 층별로 달라요", "MAC을 막아 달라는 요청은 L2 장치 몫이에요", "URL을 막아 달라는 요청은 소켓 위 장치 몫이에요", "위층일수록 깊게 보지만 느려요"]
    return frame(a, "장치마다 보는 층", "요청의 정보가 어느 층에 있나", caps, "".join(body))


# 6 이제 안전하다고 답할 수 있을까 -- 네 가지 점검 ------------------------------------------
def p6():
    a = new()
    Q = [("① 누가 들어오나", "NAC", ["미등록 기기를", "찾아내요"], ["인증 못 하는 기기의", "예외 목록 관리"]),
         ("② 무엇을 통과시키나", "방화벽", ["서버 구역으로 나누고", "기본은 차단"], ["규칙이 늘면 생기는", "충돌 점검"]),
         ("③ 무엇이 공격인가", "IPS·NIDS", ["알려진 공격은", "IPS·NIDS가 봐요"], ["처음 보는 공격,", "오탐·미탐 균형"]),
         ("④ 무슨 일이 있었나", "SIEM", ["시각 맞춘 로그를", "이어 거슬러 가요"], ["로그 보관 기간,", "계정 기록 연결"])]
    X = [40 + i * 224 for i in range(4)]
    head = "".join(box(x, 176, 208, 60, BLUE, PANEL, 8, sw=3) + text(x + 104, 202, q, 18, BLUE, 700) + text(x + 104, 225, d, 16, MUTED)
                   for x, (q, d, _, _) in zip(X, Q))
    ghosts = "".join(box(x, y, 208, 76, LINE, "none", 8, dash=True, sw=2) + text(x + 104, y + 48, "?", 24, LINE, 700) for x in X for y in (246, 332))

    def row(y, label, c, k, dash):
        return "".join(box(x, y, 208, 76, c, PANEL, 8, dash=dash, sw=3) + text(x + 104, y + 21, label, 15, c, 700)
                       + text(x + 104, y + 44, q[k][0], 16, TXT) + text(x + 104, y + 65, q[k][1], 16, TXT) for x, q in zip(X, Q))
    body = [box(40, 112, 880, 40, MUTED, PANEL, 20, sw=2) + text(480, 139, "서 이사 · 우리 회사, 이제 안전하다고 답할 수 있어요?", 20, TXT, 700),
            a.vis(head, 1, 4), ghosts,
            st(a, 2, row(246, "✓ 답할 수 있는 것", GREEN, 2, False), (40, 246, 880, 76)),
            st(a, 3, row(332, "△ 아직 비어 있는 것", VIOLET, 3, True), (40, 332, 880, 76)),
            P(a, 4, 480, 448, "안전하다는 말 대신, 네 가지를 이렇게 점검한다고 답해요", ORANGE, 20)]
    caps = ["서 이사의 질문을 네 가지 점검으로 쪼개요", "각 점검에서 지금 답할 수 있는 것을 짚어요", "아직 비어 있는 것도 함께 말해요", "'안전하다' 대신 네 가지 점검으로 답해요"]
    return frame(a, "이제 안전하다고 답할 수 있을까", "네 가지 질문에 답할 수 있는 칸과 빈 칸", caps, "".join(body))


# 6b 다섯 Unit 되짚기 + Module 3·4·5 ------------------------------------------------------
def p6b():
    a = new()
    U = [("Unit 11", "쪼개기", ["집과 회사 경로를", "나눠 규칙 찾기"], BLUE), ("Unit 12", "같은 모양 찾기", ["UPnP 매핑은", "포트 포워딩 한 줄"], BLUE),
         ("Unit 13", "대가 따지기", ["이중화의 비용과", "여유 견주기"], BLUE), ("Unit 14", "순서대로 확인하기", ["VPN 구간을 가까운", "곳부터 확인"], BLUE),
         ("Unit 15", "필요한 것만 남기기", ["장비 열 개를", "한 장의 지도로"], GREEN)]
    X = [24 + i * 186 for i in range(5)]
    cards = line(60, 184, 900, 184, GREEN, 3, "6 5")
    for x, (u, m, d, c) in zip(X, U):
        cards += (box(x, 124, 168, 120, c, PANEL, 10, sw=3) + text(x + 84, 150, u, 16, MUTED, 700) + text(x + 84, 180, m, 18, c, 700)
                  + text(x + 84, 208, d[0], 16, TXT) + text(x + 84, 230, d[1], 16, TXT))
    H = [("장부와 규칙표를", "직접 고치기"), ("아침마다 로그를", "이어 보기"), ("의심 기기 포트를", "직접 내리기")]
    M = [("Module 3", "접근통제 자동화"), ("Module 4", "이상탐지 자동화"), ("Module 5", "자동대응")]
    CX = [140, 370, 600]
    hand = "".join(box(cx - 105, 306, 210, 60, MUTED, PANEL, 8, sw=3) + text(cx, 330, h[0], 16, TXT) + text(cx, 352, h[1], 16, TXT) for cx, h in zip(CX, H))
    mods = "".join(darrow(cx, 368, 398, GREEN) + box(cx - 105, 400, 210, 56, GREEN, PANEL, 8, sw=3) + text(cx, 424, m[0], 16, GREEN, 700) + text(cx, 446, m[1], 16, TXT)
                   for cx, m in zip(CX, M))
    human = (box(735, 306, 190, 150, ORANGE, PANEL, 10, sw=3) + person(830, 340) + text(830, 418, "정책과 승인 범위는", 16, TXT, 700) + text(830, 442, "계속 사람이 정해요", 16, TXT, 700))
    body = [a.vis(cards, 1, 4),
            st(a, 2, pill(480, 280, "아직 손으로 하는 일", MUTED, 17) + hand, (30, 262, 680, 106)),
            st(a, 3, mods, (30, 372, 680, 88)),
            st(a, 4, human, (735, 306, 190, 150))]
    caps = ["다섯 Unit에서 쓴 생각법을 되짚어요", "아직 손으로 하는 일이 남아 있어요", "Module 3·4·5가 이 일들을 자동화로 이어요", "정책과 승인 범위는 계속 사람이 정해요"]
    return frame(a, "다섯 Unit을 한 줄로 되짚기", "생각법 다섯 가지와 다음 Module", caps, "".join(body))


ITEMS = [
    ("u15-l04-p1-siem-correlation", "흩어진 로그를 이으면", f"NAC 02:41, 방화벽 02:45, IPS 02:49 세 기록에 같은 주소 {IP}가 남고, SIEM이 시간순으로 엮어 8분 안의 한 사건으로 읽고 회의실 포트까지 역추적하며, 장비 시각이 틀리면 순서가 뒤집힌다는 전제를 보여 줍니다.", "SIEM은 같은 출발지의 기록을 시간순으로 엮어 한 사건으로 읽고, 장비 시각이 맞아야 합니다.", 4, p1),
    ("u15-l04-p3-rule-rollback", "규칙 하나 바꿨는데 장애가", "IPS 규칙 갱신 뒤 첨부 파일 업로드가 실패하자 변경 기록에서 최근 바뀐 IPS를 짚고, 경로 밖 NIDS는 후순위로 두고, IPS 규칙을 되돌려 업로드가 되는 모습입니다.", "변경 기록과 장치 위치로 의심 대상을 줄이고 한 번에 하나씩 되돌려 확인합니다.", 2, p3),
    ("u15-l04-p4-request-path", "한 장의 지도에 요청 하나를", "해외 고객 192.0.2.77의 요청이 공개 주소 203.0.113.10:443에서 UTM, TLS 종료와 WAF, IPS를 지나 서버 풀에 도착하고 NIDS가 옆에서 복사본만 보는 지도입니다.", "장치 이름이 아니라 경로 안·대신 연결·경로 밖의 위치로 읽으면 보이는 것과 할 수 있는 일이 정해집니다.", 2, p4),
    ("u15-l04-p4b-tls-sensors", "같은 공격 문자열, 센서 두 곳", "같은 공격 문자열이 TLS 종료 앞의 센서에는 암호문으로만 보여 경보가 없고, TLS 종료와 WAF 뒤의 센서에는 풀린 요청으로 보여 경보가 나는 모습입니다.", "TLS를 끝낸 뒤에야 내용을 볼 수 있어, 센서의 자리가 보이는 것을 정합니다.", 4, p4b),
    ("u15-l04-p5-layer-bar", "장치마다 보는 층", "요청의 L2 MAC, L3 IP, L4 포트, 소켓 위 URL을 층별로 놓고 각 층을 보는 장치를 이어, MAC 차단은 L2 장치에, URL 차단은 소켓 위 장치에 맡기며 위층일수록 깊게 보지만 느린 모습입니다.", "요청의 정보가 어느 층에 있는지 보고 그 층을 볼 수 있는 장치에 맡깁니다.", 1, p5),
    ("u15-l04-p6-four-checks", "이제 안전하다고 답할 수 있을까", "서 이사의 질문을 누가 들어오나, 무엇을 통과시키나, 무엇이 공격인가, 무슨 일이 있었나 네 가지 점검으로 쪼개 각각 답할 수 있는 것과 아직 비어 있는 것을 말하는 모습입니다.", "안전하다는 말 대신 네 가지 점검으로 답할 수 있는 칸과 빈 칸을 말합니다.", 2, p6),
    ("u15-l04-p6b-unit-recap", "다섯 Unit을 한 줄로 되짚기", "Unit 11부터 15까지 쪼개기, 같은 모양 찾기, 대가 따지기, 순서대로 확인하기, 필요한 것만 남기기를 되짚고, 손으로 하던 일이 Module 3·4·5의 자동화로 이어지며 정책과 승인 범위는 사람이 정한다는 모습입니다.", "다섯 Unit의 생각법을 되짚고, 손으로 하는 일은 Module 3·4·5로 이어집니다.", 14, p6b),
]
assert len(ITEMS) == 7

if __name__ == "__main__":
    for f, _t, _al, _c, _ap, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        by = {f: (f, t, al, c, ap) for f, t, al, c, ap, _ in ITEMS}
        order = [["u15-l04-p1-siem-correlation"], None, ["u15-l04-p3-rule-rollback"],
                 ["u15-l04-p4-request-path", "u15-l04-p4b-tls-sensors"], ["u15-l04-p5-layer-bar"],
                 ["u15-l04-p6-four-checks", "u15-l04-p6b-unit-recap"]]
        wire_items(LESSON / "lesson.md", [None if o is None else [by[f] for f in o] for o in order])
    print("ok", len(ITEMS), "svgs")
