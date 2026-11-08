#!/usr/bin/env python3
"""Unit 11 Lesson 4 (포워드 프록시와 클라이언트 측 중계). Run from the repo root:
python3 scripts/svg_pairs/u11_l04_forward.py   (add --svg-only to skip the lesson.md edit).

One light 4-stage example SVG per Page (20 Pages: source-06 x7, source-07 x7, source-09 x6), placed after the
first paragraph. Deletes the stale wiki flow diagrams (assets/diagrams/source-06/07/09.svg) and their references."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, dur
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/restructured/04-*"))
OUT = LESSON / "assets" / "animations"
Y = 300


def srv(x, y, label="서버", c=GREEN):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, label, 18, TXT, 700))


def agent(x, y, label="Proxy", c=BLUE):
    return box(x - 55, y - 40, 110, 80, c, PANEL, 12, sw=3) + text(x, y + 8, label, 20, c, 700)


def doc(x, y, c=ORANGE, label="PDF"):
    return (f'<rect x="{x - 20}" y="{y - 26}" width="40" height="52" rx="4" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + text(x, y + 6, label, 14, c, 700))


def P(x, y, s, c=GREEN, filled=False, w=None, fs=18):
    return pill(x, y, s, c, fs, filled, w)


def L(x1, x2, c=BLUE, y=Y, dash=None):
    return line(x1, y, x2, y, c, 5, dash)


def trio(cl="내 컴퓨터", px="Proxy", sv="서버"):
    return laptop(110, Y, cl) + agent(480, Y, px) + srv(850, Y, sv)


def cs(cl="내 컴퓨터", sv="서버"):
    return laptop(110, Y, cl) + srv(850, Y, sv)


# ---------------- source-06 ----------------
def f01(a):
    b = [cs(), a.vis(L(170, 800, MUTED, dash="10 8") + P(480, 255, "직접 연결", MUTED, w=130), 1, 1),
         a.vis(agent(480, Y) + L(170, 425) + L(535, 800, GREEN), 2, 4),
         a.vis(P(480, 215, "한 중계 서버를 거쳐요", BLUE, w=240), 2, 2),
         a.vis(P(480, 215, "요청을 대신 전달", BLUE, True, 200), 3, 3),
         a.vis("".join(P(x, 410, t, VIOLET, w=110) for x, t in ((260, "캐시"), (390, "접근 정책"), (520, "기록"), (650, "내용 검사"))), 4, 4)]
    return ("Proxy를 사용하는 관점", "직접 나갈까, 한 곳을 거칠까?", ["처음엔 컴퓨터마다 직접 인터넷으로 나갈 수 있어요", "한 중계 서버를 거치게 할 수도 있어요", "클라이언트가 고른 중계자가 대신 전달해요", "캐시·정책·기록은 그 위에 얹는 기능이에요"], "".join(b))


def f02(a):
    b = [cs(),
         a.vis(L(170, 800, MUTED, dash="10 8") + P(480, 255, "직접 연결", MUTED, w=130), 1, 1),
         a.vis(agent(480, Y) + L(170, 425) + L(535, 800, GREEN), 2, 4),
         a.vis(P(850, 215, "상대: 내 주소", ORANGE, w=170), 1, 1),
         a.vis(P(850, 215, "상대: Proxy 주소", ORANGE, w=190), 3, 3),
         a.vis(P(850, 215, "상대: Proxy 주소", ORANGE, w=190) + P(480, 410, "신원이 숨는다는 보장은 아니에요", RED, w=400), 4, 4),
         a.vis(P(300, 255, "Proxy에 먼저 연결", BLUE, w=190), 2, 2)]
    return ("직접 가는 길과 돌아가는 길", "서버에 보이는 주소가 달라질 수 있어요", ["직접 접속하면 서버는 내 쪽 주소를 봐요", "Proxy를 지정하면 먼저 Proxy에 연결해요", "서버에는 Proxy 쪽 주소가 보일 수 있어요", "헤더로 원래 정보가 전달될 수도 있어요"], "".join(b))


def f03(a):
    b = [trio(),
         a.vis(box(60, 150, 210, 70, MUTED, PANEL, 10) + text(165, 178, "Proxy 설정", 16, MUTED, 700) + text(165, 205, "주소 + 포트", 18, TXT, 700), 1, 1),
         a.vis(L(170, 425) + P(300, 255, "example.net 요청", BLUE, w=190), 2, 4),
         a.vis(L(535, 800, GREEN) + P(670, 255, "별도 연결", GREEN, w=110), 3, 4),
         a.vis(cross(480, 215) + P(480, 410, "모든 앱이 자동으로 거치진 않아요", ORANGE, w=360), 4, 4)]
    return ("접속 주체를 대신하기", "브라우저가 먼저 Proxy에 말을 걸어요", ["브라우저에 Proxy 주소와 포트를 입력해요", "브라우저는 먼저 Proxy에 요청을 맡겨요", "Proxy가 목적지와 별도 연결을 맺어요", "프로그램별 설정은 따로 확인해요"], "".join(b))


def f04(a):
    b = [box(40, 150, 240, 230, GREEN, PANEL, 16, dash=True) + text(160, 180, "한국", 18, GREEN, 700),
         box(360, 150, 240, 230, BLUE, PANEL, 16, dash=True) + text(480, 180, "해외", 18, BLUE, 700),
         laptop(110, Y, "내 컴퓨터"), agent(480, Y, "해외 Proxy"), srv(850, Y, "자료 사이트"),
         a.vis(L(170, 425) + P(300, 255, "요청", BLUE, w=70), 2, 4),
         a.vis(L(535, 800, GREEN), 2, 4),
         a.vis(P(780, 215, "상대: 해외 출구 주소", ORANGE, w=230), 3, 4),
         a.vis(P(480, 440, "차단 회피·익명 보장은 아니에요", RED, w=360), 4, 4)]
    return ("Proxy를 통한 우회", "다른 나라의 출구로 나가 봐요", ["한국에서 해외 Proxy를 거쳐 접속해요", "요청이 Proxy를 지나 사이트로 가요", "사이트에는 Proxy의 출구 주소가 보여요", "운영자는 기록을 볼 수 있어요"], "".join(b))


def f05(a):
    b = [cs(),
         a.vis(L(170, 800, MUTED, dash="10 8") + P(480, 255, "한 번에 도착", MUTED, w=150), 1, 1),
         a.vis(agent(480, Y) + L(170, 425) + L(535, 800, GREEN) + P(300, 255, "① 이동", BLUE, w=100) + P(670, 255, "② 이동", GREEN, w=100), 2, 4),
         a.vis(P(480, 410, "경로가 늘어 느려질 수 있어요", ORANGE, w=330), 2, 2),
         a.vis(cross(480, 225) + P(480, 410, "Proxy 장애 → 접속에 영향", RED, w=300), 3, 3),
         a.vis(check(480, 225) + P(480, 410, "가깝고 캐시하면 도움이 돼요", GREEN, w=320), 4, 4)]
    return ("우회에 따른 속도와 비용", "편리하지만 거치는 길이 늘어요", ["직접 가면 한 번에 도착해요", "Proxy를 거치면 단계가 늘어요", "Proxy가 멈추면 모두 영향을 받아요", "잘 두면 오히려 도움이 될 수도 있어요"], "".join(b))


def f06(a):
    b = [laptop(110, Y, "브라우저"), srv(850, Y, "서버"), agent(480, Y, "Proxy"),
         a.vis(L(170, 425) + P(300, 255, "소켓 A", BLUE, True, 100), 1, 4),
         a.vis(L(535, 800, GREEN) + P(670, 255, "소켓 B", GREEN, True, 100), 2, 4),
         mv(a, packet(0, 0), [(200, Y), (440, Y)], 3, 3, 3, 0.1, 0.9),
         mv(a, packet(0, 0, GREEN), [(520, Y), (770, Y)], 3, 3, 3, 0.1, 0.9),
         a.vis(P(480, 410, "받은 데이터를 다른 소켓에 이어 줘요", VIOLET, w=380), 3, 3),
         a.vis(P(480, 410, "두 연결은 서로 독립이에요", ORANGE, w=280) + cross(480, 225), 4, 4)]
    return ("두 Socket 사이의 중계", "Proxy에는 연결이 두 개 생겨요", ["클라이언트와 이야기하는 연결 하나", "서버와 이야기하는 연결 하나", "한쪽에서 받은 흐름을 다른 쪽에 이어 줘요", "한쪽이 끊기면 Proxy가 처리해요"], "".join(b))


def f07(a):
    b = [trio(),
         a.vis(P(480, 215, "무엇을 전달하고 기록할까?", ORANGE, w=300), 2, 2),
         a.vis(cross(480, 215) + P(480, 410, "익명성이 자동으로 보장되진 않아요", RED, w=380), 3, 3),
         a.vis("".join(P(x, 410, t, VIOLET, w=w) for x, t, w in ((190, "캐시", 90), (330, "접근 통제", 130), (510, "악성 파일 검사", 170), (730, "개발 중 트래픽 분석", 210))), 4, 4)]
    return ("우회 목적의 Proxy 정리", "핵심은 요청을 대신 전달한다는 점이에요", ["Proxy는 요청을 받아 다른 서버에 접속해요", "무엇을 전달·기록하는지에 따라 달라져요", "그래서 대리 접속이 익명성을 보장하진 않아요", "같은 구조를 여러 목적에 응용해요"], "".join(b))


# ---------------- source-07 ----------------
def g01(a):
    b = [pc(110, Y, "공용 PC"), agent(480, Y, "내부 Proxy"), srv(850, Y, "외부 사이트"),
         a.vis(L(170, 800, MUTED, y=180, dash="10 8") + cross(480, 180) + P(480, 140, "직접 연결은 방화벽이 막아요", RED, w=300), 1, 4),
         a.vis(L(170, 425) + P(300, 255, "요청", BLUE, w=70), 2, 4),
         a.vis(L(535, 800, GREEN) + P(670, 255, "Proxy만 외부로", GREEN, w=170), 3, 4),
         a.vis(P(480, 410, "정책 적용·기록을 한곳에서", VIOLET, w=300), 4, 4)]
    return ("회사에서 직접 접속 제한", "내부 Proxy를 거쳐서만 나가요", ["공용 PC가 바로 인터넷으로 나가지 못하게 해요", "PC는 먼저 내부 Proxy로 요청해요", "Proxy가 외부 서버에 접속해요", "관리자는 한 지점에서 정책을 적용해요"], "".join(b))


def g02(a):
    hdr = text(250, 150, "누가 시작한 연결?", 17, MUTED, 700) + text(560, 150, "방화벽 정책", 17, MUTED, 700)
    row = lambda y, t, r, c: cell(100, y, 300, 60, t, TXT, 20) + cell(420, y, 280, 60, r, c, 22)
    b = [hdr, a.vis(row(170, "공용 PC → 외부 사이트", "차단", RED), 1, 4), a.vis(row(250, "Proxy → 외부 사이트", "허용 (필요한 곳만)", GREEN), 2, 4),
         a.vis(P(480, 370, "접속이 한곳으로 모여 정책이 쉬워요", BLUE, w=380), 3, 3),
         a.vis(P(480, 370, "Proxy 서버가 병목·위험 지점이 될 수도 있어요", ORANGE, w=500), 4, 4)]
    return ("Proxy를 통한 외부 접속", "직접 연결은 막고 Proxy만 열어요", ["공용 PC의 직접 외부 연결은 차단해요", "Proxy가 시작한 연결만 허용해요", "접속이 한곳으로 모여 관리하기 쉬워요", "Proxy 자체의 보안·용량도 챙겨요"], "".join(b))


def g03(a):
    b = [trio("공용 PC", "내부 Proxy", "외부 사이트").replace(laptop(110, Y, "공용 PC"), pc(110, Y, "공용 PC")),
         a.vis(L(170, 425) + L(535, 800, GREEN), 1, 4),
         a.vis(box(390, 120, 180, 80, MUTED, PANEL, 10) + "".join(cell(398 + i * 56, 162, 52, 30, t, BLUE, 14) for i, t in enumerate(("누가", "언제", "어디로"))) + text(480, 150, "접속 기록", 16, MUTED, 700), 2, 4),
         a.vis(lock(480, 385, RED) + P(670, 400, "HTTPS 내용은 그대로 못 읽어요", ORANGE, w=300), 3, 3),
         a.vis(P(480, 410, "목적·권한·보관 기간부터 정해요", GREEN, w=320), 4, 4)]
    return ("중간에서 알 수 있는 것", "Proxy는 접속 기록을 남길 수 있어요", ["PC의 요청이 Proxy를 거쳐 가요", "누가 언제 어디로 갔는지 알 수 있어요", "암호화된 내용은 설정 없이는 읽지 못해요", "기록하기 전에 목적과 범위를 정해요"], "".join(b))


def g04(a):
    b = [pc(110, Y, "공용 PC"), agent(480, Y, "내부 Proxy"), srv(850, Y, "자료 사이트"),
         a.vis(doc(850, Y - 75), 1, 4),
         mv(a, doc(0, 0), [(800, 225), (480, 225), (480, 225)], 2, 2, 2, 0.1, 0.9),
         a.vis(eye(480, 165) + P(480, 128, "알려진 패턴과 비교", ORANGE, w=220), 3, 4),
         a.vis(doc(480, 225, GREEN) + check(520, 190) + P(250, 410, "안전하면 전달", GREEN, True, 170), 3, 3),
         a.vis(doc(480, 225, RED) + cross(520, 190) + P(480, 410, "문제 발견 → 차단·알림", RED, True, 240), 4, 4)]
    return ("악성 파일 검사", "내려받는 파일을 Proxy에서 살펴봐요", ["자료 사이트에서 PDF를 내려받아요", "파일이 Proxy를 지나가요", "구성에 따라 검사 시스템이 확인해요", "문제가 있으면 전달하지 않아요"], "".join(b))


def g05(a):
    b = [srv(110, Y, "외부 서버"), pc(850, Y, "내부 PC"),
         box(450, 160, 60, 280, ORANGE, PANEL, 8, sw=3) + text(480, 300, "Virus Wall", 18, ORANGE, 700).replace('<text', '<text transform="rotate(-90 480 300)"'),
         a.vis(doc(210, 250, GREEN) + doc(210, 350, RED), 1, 4),
         mv(a, doc(0, 0, GREEN), [(210, 250), (780, 250)], 2, 2, 2, 0.1, 0.9),
         a.vis(cross(430, 350) + doc(380, 350, RED), 3, 4),
         a.vis(P(480, 130, "위험한 파일은 안에 못 들어가요", RED, w=320), 3, 3),
         a.vis(P(480, 130, "IPS는 패킷, Proxy는 Stream — 기능은 겹칠 수 있어요", BLUE, w=560, fs=17), 4, 4)]
    return ("Virus Wall과 내부 보호", "웹 통신을 중계하며 파일을 걸러요", ["밖에서 파일 두 개가 들어와요", "안전한 파일은 안으로 전달돼요", "위험한 파일은 벽에서 멈춰요", "IPS와 Proxy는 역할이 겹칠 수 있어요"], "".join(b))


def g06(a):
    b = [box(280, 140, 400, 230, GREEN, PANEL, 18, sw=3) + text(480, 178, "보안 장비 한 대", 22, TXT, 700),
         a.vis(cell(310, 210, 160, 56, "IPS", ORANGE, 22) + text(390, 296, "경로에서 패킷 검사", 15, MUTED), 2, 4),
         a.vis(cell(490, 210, 160, 56, "Proxy", BLUE, 22) + text(570, 296, "연결을 받아 중계", 15, MUTED), 3, 4),
         a.vis(P(480, 430, "한 상자여도 처리 경로는 따로 봐요", GREEN, w=360), 4, 4), a.vis(P(480, 336, "데이터가 어디로 들어와 나가나?", MUTED, w=320, fs=16), 4, 4)]
    return ("보호 기능을 함께 두기", "한 장비 안에 여러 기능이 들어가요", ["물리적으로는 한 장비예요", "어떤 기능은 패킷을 경로에서 검사하고", "어떤 기능은 연결을 받아 중계해요", "경로를 도식으로 그려 보면 정확해요"], "".join(b))


def g07(a):
    b = [pc(110, Y, "공용 PC"), agent(480, Y, "내부 Proxy"), srv(850, Y, "외부 사이트"), L(170, 425), L(535, 800, GREEN),
         a.vis(eye(480, 190) + P(480, 145, "정책 위반 점검", ORANGE, w=170), 2, 4),
         a.vis(ask(250, 215) + P(250, 175, "개인 검색까지?", ORANGE, w=170), 3, 4),
         a.vis("".join(P(x, 410, t, GREEN, w=110) for x, t in ((330, "목적"), (480, "범위"), (630, "알리는 방식"))), 4, 4)]
    return ("내부 사용자의 통신 감시", "점검과 감시는 한 끗 차이예요", ["모든 요청이 내부 Proxy로 모여요", "운영자는 접속 흐름을 점검할 수 있어요", "하지만 개인 검색까지 남으면 사생활 문제예요", "목적·범위·안내를 함께 정해요"], "".join(b))


# ---------------- source-09 ----------------
def h01(a):
    strip = (cell(250, 250, 130, 56, "IP", GREEN, 20) + cell(390, 250, 130, 56, "TCP", GREEN, 20) + cell(530, 250, 180, 56, "내용(HTTPS)", VIOLET, 18))
    b = [text(480, 215, "패킷 하나", 18, MUTED, 700), a.vis(strip, 1, 4), a.vis(eye(480, 160) + P(480, 130, "Wireshark로 캡처", ORANGE, w=200).replace("", ""), 1, 4),
         a.vis(check(315, 340) + check(455, 340) + text(385, 375, "헤더는 보여요", 17, GREEN, 700), 2, 4),
         a.vis(lock(620, 330, RED) + text(620, 385, "암호화되어 못 읽어요", 17, RED, 700), 3, 4),
         a.vis(P(480, 440, "웹 내용을 보려면 로컬 Proxy 도구가 필요해요", BLUE, w=450), 4, 4)]
    return ("암호화된 패킷의 한계", "잡았다고 읽을 수 있는 건 아니에요", ["PC의 패킷을 캡처해 봐요", "IP·TCP 정보는 볼 수 있어요", "HTTPS 내용은 암호화되어 있어요", "그래서 별도의 중계 지점을 만들어요"], "".join(b))


def h02(a):
    b = [box(60, 150, 620, 230, BLUE, PANEL, 16, dash=True) + text(370, 182, "내 PC", 18, BLUE, 700),
         cell(100, 250, 170, 70, "브라우저", BLUE, 20), srv(850, Y, "서버"),
         a.vis(cell(420, 250, 220, 70, "Fiddler·Burp", VIOLET, 20), 2, 4),
         a.vis(L(270, 420, BLUE), 3, 4), a.vis(L(640, 815, GREEN), 4, 4),
         a.vis(P(370, 420, "URL·헤더·상태 코드·본문을 살펴봐요", VIOLET, w=420), 4, 4)]
    return ("PC에 설치하는 Proxy", "내 PC 안에 중계 도구를 둬요", ["브라우저는 내 PC 안에 있어요", "분석 도구가 PC 안에서 Proxy로 동작해요", "브라우저의 요청이 도구로 먼저 가요", "도구가 서버로 전달하고 내용을 보여 줘요"], "".join(b))


def h03(a):
    b = [box(100, 170, 560, 200, BLUE, PANEL, 16, dash=True) + text(380, 202, "내 PC (127.0.0.1)", 18, BLUE, 700),
         cell(140, 250, 170, 70, "브라우저", BLUE, 20), cell(450, 250, 170, 70, "분석 도구 :8080", VIOLET, 18),
         a.vis(box(690, 215, 220, 80, MUTED, PANEL, 10) + text(800, 245, "Proxy 설정", 16, MUTED, 700) + text(800, 276, "127.0.0.1:8080", 18, TXT, 700), 1, 4),
         a.vis(L(310, 450, BLUE) + P(380, 345, "밖으로 안 나가요", BLUE, w=170, fs=16), 2, 2),
         a.vis(hl8080(), 3, 3),
         a.vis(cross(380, 285) + P(480, 430, "도구가 꺼져 있거나 포트가 다르면 실패", RED, w=420), 4, 4)]
    return ("Loopback에 Proxy 설정", "127.0.0.1은 내 컴퓨터를 가리켜요", ["브라우저에 127.0.0.1:8080을 적어요", "연결은 같은 PC 안에서만 오가요", "포트 8080이 어느 프로그램인지 가려 줘요", "도구가 꺼져 있으면 연결할 수 없어요"], "".join(b))


def hl8080():
    return box(444, 244, 182, 82, ORANGE, "none", 10, sw=4) + P(535, 400, "8080 = 이 프로그램", ORANGE, w=200, fs=16)


def h04(a):
    b = [trio("브라우저", "로컬 Proxy", "서버"),
         a.vis(L(170, 425) + P(300, 255, "연결 ①", BLUE, True, 100), 1, 4),
         a.vis(L(535, 800, GREEN) + P(670, 255, "연결 ②", GREEN, True, 100), 2, 4),
         a.vis(lock(300, 200, BLUE) + lock(670, 200, GREEN) + P(480, 410, "암호화 구간도 따로 생길 수 있어요", VIOLET, w=360), 3, 3),
         a.vis(lock(300, 200, BLUE) + lock(670, 200, GREEN) + P(480, 410, "신뢰 설정이 없으면 암호문 그대로예요", RED, w=400), 4, 4)]
    return ("로컬 Proxy를 통과하는 경로", "두 개의 구간을 차례로 따라가요", ["브라우저와 Proxy 사이의 연결이 있어요", "Proxy와 서버 사이의 연결이 따로 있어요", "HTTPS는 구간별로 따로 암호화될 수 있어요", "허가 없이 복호화해서는 안 돼요"], "".join(b))


def h05(a):
    pk = lambda x, n: packet(x, 250) + text(x, 295, n, 17, MUTED, 700)
    b = [a.vis(pk(260, "① GE") + pk(480, "② T /lo") + pk(700, "③ gin"), 1, 2),
         a.vis(P(480, 200, "TCP는 데이터를 여러 조각으로 나눠 보낼 수 있어요", ORANGE, w=480), 2, 2),
         a.vis(pk(260, "①") + pk(480, "②") + pk(700, "③") + line(480, 315, 480, 350, BLUE, 4) + cell(330, 350, 300, 50, "GET /login", BLUE, 20) + P(480, 440, "Proxy는 요청 단위로 읽어요", GREEN, w=280), 3, 4),
         a.vis(P(480, 200, "Stream 처리 ≠ 암호 해제", RED, w=290), 4, 4)]
    return ("Stream 수준의 해석", "조각난 패킷을 하나의 요청으로 봐요", ["패킷은 조각으로 도착해요", "조각을 이어야 요청 전체가 보여요", "소켓에서는 이어진 흐름으로 읽어요", "TLS 내용은 별도 설정이 있어야 보여요"], "".join(b))


def h06(a):
    cards = [("우회", "외부 Proxy", BLUE), ("정책·검사", "내부 Proxy", GREEN), ("분석", "로컬 Proxy", VIOLET)]
    b = ["".join(a.vis(cell(60 + i * 290, 170, 260, 80, t, c, 22) + text(190 + i * 290, 285, s, 17, MUTED, 700), i + 1, 4) for i, (t, s, c) in enumerate(cards)),
         a.vis(P(480, 350, "요청을 받고 → 다른 연결로 전달 → 응답을 되돌려요", ORANGE, w=560), 4, 4),
         a.vis(P(480, 420, "다음: 서버 앞의 Reverse Proxy", MUTED, w=320), 4, 4)]
    return ("Fiddler와 Proxy 활용 정리", "목적은 달라도 중계 원리는 같아요", ["외부 출구로 연결하는 우회 사례", "조직이 관리하는 정책·검사 지점", "내 PC 안의 로컬 분석 도구", "공통 원리는 대신 전달하는 중계예요"], "".join(b))


SCENES = [("06", 1, "forward-view", f01), ("06", 2, "direct-vs-proxy", f02), ("06", 3, "proxy-settings", f03), ("06", 4, "bypass", f04),
          ("06", 5, "speed-cost", f05), ("06", 6, "two-sockets", f06), ("06", 7, "bypass-summary", f07),
          ("07", 1, "limit-direct", g01), ("07", 2, "firewall-rule", g02), ("07", 3, "proxy-log", g03), ("07", 4, "file-scan", g04),
          ("07", 5, "virus-wall", g05), ("07", 6, "combined-box", g06), ("07", 7, "monitoring", g07),
          ("09", 1, "encrypted-packet", h01), ("09", 2, "local-proxy", h02), ("09", 3, "loopback", h03), ("09", 4, "local-path", h04),
          ("09", 5, "stream", h05), ("09", 6, "wrap-up", h06)]


def build(src, n, slug, fn):
    a = Anim(4, dur(False))
    title, sub, caps, body = fn(a)
    return f"u11-fwd-{src}-{n:02d}-{slug}", f"advanced-source-{src}-page-{n:02d}", title, sub, caps, frame(a, title, sub, caps, body)


def wire(lesson_md, items):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-0[679]\.svg\n(?:    .*\n)+", "", s)
    for f, pid, title, sub, caps, _ in items:
        if f"assets/animations/{f}.svg" in s:
            continue
        alt = f"{title}: " + " → ".join(caps)
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(title)}\n    alt: {q(alt)}\n"
               f"    caption: {q(sub)}\n    after_paragraph: 0\n")
        assert f"- page_id: {pid}\n" in s, pid
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    items = [build(*sc) for sc in SCENES]
    for f, *_r, svg in items:
        write(OUT, f, svg)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", items)
        for n in ("06", "07", "09"):
            (LESSON / "assets" / "diagrams" / f"source-{n}.svg").unlink(missing_ok=True)
    print("ok", len(items), "svgs")
