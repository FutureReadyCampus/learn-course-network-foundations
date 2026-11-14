#!/usr/bin/env python3
"""Unit 12 Lesson 3 (밖에서 사내 AI 서버로 들어오는 포트 포워딩): one 4-step example SVG per Page (7).
Run from repo root: python3 scripts/svg_pairs/u12_new_l03_forwarding.py  (--svg-only skips the lesson.md edit).
Example: 바깥 198.51.100.25:8080 -> AI 서버 192.168.10.50:8080, 고객 시연 출발지 192.0.2.77."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"
ADDR, PUB, CUST = f"{AI}:{AI_PORT}", f"{WAN}:{AI_PORT}", "192.0.2.77"
RULE = f"외부 TCP {AI_PORT} → {ADDR}"


def p1():
    p = Pg("변환표에 줄을 미리 적어 두면?", "자동으로 생기는 줄과 사람이 적는 줄",
           ["바깥 8080 요청을 GPU PC로 보내는 줄을 적어요", "동적 매핑은 안쪽에서 나갈 때 공유기가 만들어요",
            "정적 매핑은 관리자가 미리 적어 둬요", "포트 포워딩은 직접 적는 정적 매핑이에요"])
    L, R = 50, 510
    p.base(box(L, 125, 400, 285, MUTED, PANEL, 16, sw=2) + lbl(L + 200, 158, "동적 매핑 (자동 행)", MUTED, 19) + ledger(L + 200, 215),
           box(R, 125, 400, 285, BLUE, PANEL, 16, sw=2) + lbl(R + 200, 158, "정적 매핑 (포트 포워딩)", BLUE, 19) + ledger(R + 200, 215))
    p.at(pill(480, 452, "바깥 8080 → GPU PC로 보내라는 한 줄", BLUE, 17, False, 380), 1, 1)
    p.at(cell(L + 25, 265, 350, 42, "192.168.10.41:3000 → 53001", MUTED, 15) + pill(L + 200, 345, "공유기가 나갈 때 자동으로", MUTED, 16, False, 250), 2, mark=(L + 25, 265, 350, 42))
    p.at(cell(R + 25, 265, 350, 42, RULE, BLUE, 14) + pill(R + 200, 345, "관리자가 미리 적어 둬요", BLUE, 16, False, 230), 3, mark=(R + 25, 265, 350, 42))
    p.at(pill(480, 452, "포트 포워딩 = 직접 적는 정적 매핑", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p2():
    p = Pg("포트 포워딩 설정 화면", "칸마다 바깥 값인지 안쪽 값인지 물어요",
           ["공유기 설정 화면에는 다섯 칸이 있어요", "바깥 칸: 외부 포트 8080, 프로토콜 TCP",
            "안쪽 칸: 내부 IP와 내부 포트를 채워요", "원격지를 비우면 누구나 들어와요"])
    rows = [("외부 포트 · 바깥", BLUE, "8080"), ("프로토콜 · 공통", MUTED, "TCP"), ("내부 IP · 안쪽", GREEN, AI),
            ("내부 포트 · 안쪽", GREEN, AI_PORT), ("원격지 · 바깥", BLUE, "비워 둠 = 누구나 들어와요")]
    ys = [135 + i * 58 for i in range(5)]
    p.base(*[cell(170, y, 220, 46, t, c, 17) + box(400, y, 390, 46, LINE, PANEL, 6, dash=True, sw=2) for (t, c, _), y in zip(rows, ys)])
    for i, ((t, c, v), y) in enumerate(zip(rows, ys)):
        st = 2 if i < 2 else 3 if i < 4 else 4
        p.at(cell(400, y, 390, 46, v, ORANGE if i == 4 else c, 18), st, 4)
    p.mark((400, ys[0], 390, 104), 2)
    p.mark((400, ys[2], 390, 104), 3)
    p.mark((400, ys[4], 390, 46), 4)
    p.at(pill(480, 452, "저장해도 방화벽 허용은 따로 확인해요", GREEN, 17, False, 380), 4, 4)
    return p.render()


def p3():
    p = Pg("박 팀장은 어떤 주소로 접속할까?", "바깥 주소로 오면 공유기가 목적지를 바꿔 줘요",
           ["박 팀장은 사설 주소가 아니라 바깥 주소로 가요", "공유기가 8080 줄을 찾아 목적지를 바꿔요",
            "목적지가 192.168.10.50:8080으로 바뀌어요", "응답은 198.51.100.25:8080이 한 것처럼 보여요"])
    p.base(dsrv(110, 340), rt(480, 340), laptop(850, 340, "박 팀장"), line(150, 340, 450, 340, LINE, 4, "8 6"), line(510, 340, 800, 340, LINE, 4, "8 6"))
    p.at(lbl(770, 142, "공유기 바깥쪽") + card(620, 155, CUST + ":49152", PUB, BLUE), 1)
    p.fly(packet(0, 0, BLUE), [(800, 340), (540, 340)], 1, 0.1, 0.9)
    p.at(cell(355, 235, 250, 40, f"{AI_PORT} → {ADDR}", ORANGE, 14), 2, 3, mark=(355, 235, 250, 40))
    p.at(lbl(190, 142, "공유기 안쪽") + card(40, 155, CUST + ":49152", ADDR, GREEN), 3, mark=cl(40, 155, 1))
    p.fly(packet(0, 0, GREEN), [(440, 340), (170, 340)], 3, 0.1, 0.9)
    p.at(check(110, 265), 3, 4)
    p.at(pill(480, 440, f"박 팀장은 {PUB}가 답한 것으로 봐요", ORANGE, 17, True, 440), 4, 4)
    return p.render()


def p4():
    p = Pg("서비스가 둘이면 규칙도 둘일까?", "외부 포트 하나는 안쪽 한 곳으로만 가요",
           ["AI 서버 외에 도면 NAS도 밖에서 열어 달라고 해요", "AI 서버는 외부 8080으로 연결해 둬요",
            "NAS도 같은 8080으로 넣으면 충돌해요", "NAS는 외부 5001처럼 포트를 따로 나눠요"])
    p.base(net(40, 125, 260, 340, "사무실 LAN", GREEN), dsrv(165, 205), dsrv(165, 355, "도면 NAS", BLUE), rt(480, 300), cloud(850, 300, "인터넷"),
           line(510, 300, 780, 300, LINE, 4, "8 6"), line(300, 215, 452, 285, LINE, 4, "8 6"), line(300, 365, 452, 315, LINE, 4, "8 6"))
    p.at(pill(165, 295, ADDR, GREEN, 15, False, 190) + pill(165, 445, "192.168.10.30:5001", BLUE, 15, False, 190), 1)
    p.at(line(300, 215, 452, 285, ORANGE, 6) + pill(376, 245, "외부 8080", ORANGE, 15, True, 110), 2, mark=(321, 227, 110, 36))
    p.at(line(300, 365, 452, 315, RED, 6, "10 6") + pill(376, 345, "외부 8080", RED, 15, False, 110) + cross(480, 405), 3, 3, mark=(458, 383, 44, 44))
    p.at(line(300, 365, 452, 315, GREEN, 6) + pill(376, 345, "외부 5001", GREEN, 15, True, 110) + pill(700, 430, "서비스마다 외부 포트를 나눠요", ORANGE, 17, True, 300), 4, 4, mark=(321, 327, 110, 36))
    return p.render()


def p5():
    p = Pg("사무실에서 공인 주소로 시험하면?", "안쪽에서 바깥 주소로 가면 되돌아와야 해요",
           ["지우가 사무실 PC에서 198.51.100.25:8080을 입력해요", "공유기가 안쪽으로 되돌려 보내야 해요(헤어핀)",
            "장비와 설정에 따라 지원하지 않을 수 있어요", "시험은 휴대폰 데이터 같은 바깥 회선에서 해요"])
    p.base(net(40, 125, 300, 335, "사무실 LAN", GREEN), pc(110, 210, "지우 PC"), dsrv(260, 350), rt(480, 280), phone(850, 280, "휴대폰 데이터"),
           line(510, 280, 800, 280, LINE, 4, "8 6"))
    p.fly(packet(0, 0, BLUE), [(150, 210), (445, 275)], 1, 0.05, 0.9)
    p.at(pill(520, 165, "목적지 " + PUB, BLUE, 15, False, 270), 1, 1, mark=(385, 147, 270, 36))
    p.at(f'<path d="M455 305 Q 390 390 300 372" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-dasharray="10 6"/>'
         f'<polygon points="292,370 312,358 312,382" fill="{ORANGE}"/>' + pill(580, 440, "헤어핀 NAT: 안쪽으로 다시 돌려요", ORANGE, 17, True, 340), 2, 2)
    p.at(cross(480, 215) + pill(580, 440, "장비에 따라 안 될 수 있어요", RED, 17, False, 300), 3, 3, mark=(458, 193, 44, 44))
    p.fly(packet(0, 0, ORANGE), [(810, 280), (520, 280), (300, 345)], 4, 0.05, 0.95)
    p.at(check(260, 280) + pill(580, 440, "시험은 사무실 밖 회선에서 해요", GREEN, 17, True, 340), 4, 4)
    return p.render()


def p6():
    p = Pg("포워딩했는데 왜 밖에서 안 열릴까?", "가까운 곳부터 하나씩 지워 가요",
           ["규칙을 넣었는데 휴대폰 데이터로도 안 열려요", "서버 주소는 맞고 GPU PC 방화벽이 8080을 막고 있어요",
            "지우가 8080을 허용하자 막힌 곳이 풀려요", "규칙 값과 WAN 주소도 맞아서 CGNAT는 아니에요"])
    rows = ["① AI 서버가 기다리는 주소", "② GPU PC 방화벽 8080/TCP", "③ 규칙의 내부 IP·포트·TCP", "④ 공유기 WAN " + WAN]
    ys = [135 + i * 70 for i in range(4)]
    cellr = lambda i, c: cell(90, ys[i], 500, 54, rows[i], c, 19)
    p.base(*[cellr(i, MUTED) for i in range(4)])
    p.at(pill(480, 440, "규칙은 넣었는데 휴대폰으로도 안 열려요", RED, 17, False, 380), 1, 1)
    p.at(cellr(0, GREEN) + check(620, ys[0] + 27) + cellr(1, RED) + cross(620, ys[1] + 27) + pill(790, ys[1] + 27, "8080 연결이 막혀요", RED, 16, False, 190), 2, 2, mark=(90, ys[1], 580, 54))
    p.at(cellr(0, GREEN) + check(620, ys[0] + 27), 3, 4)
    p.at(cellr(1, GREEN) + check(620, ys[1] + 27) + pill(790, ys[1] + 27, "지우가 8080 허용", GREEN, 16, False, 190), 3, 3, mark=(90, ys[1], 580, 54))
    p.at(cellr(1, GREEN) + check(620, ys[1] + 27), 4, 4)
    p.at(cellr(2, GREEN) + check(620, ys[2] + 27) + cellr(3, GREEN) + check(620, ys[3] + 27) + pill(790, ys[3] + 27, "공인 주소라 CGNAT 아님", GREEN, 15, False, 210),
         4, 4, mark=(90, ys[2], 580, 124))
    return p.render()


def p7():
    p = Pg("포트를 열어도 정말 괜찮을까?", "원격지를 제한하면 들어올 수 있는 곳이 줄어요",
           ["원격지를 비운 8080은 인터넷 누구에게나 열려요", "원격지를 고객사 주소 192.0.2.77로 제한해요",
            "낯선 출발지는 막히고 고객만 들어와요", "시연 기간만 열고 로그인과 기록을 남겨요"])
    p.base(dsrv(115, 275), rt(480, 275), person(850, 120, "낯선 출발지"), laptop(850, 265, "고객 " + CUST), person(850, 375, "낯선 출발지"),
           line(150, 275, 450, 275, LINE, 4, "8 6"), line(510, 275, 790, 275, LINE, 4, "8 6"),
           line(505, 255, 810, 140, LINE, 4, "8 6"), line(505, 295, 810, 395, LINE, 4, "8 6"))
    p.at(cell(260, 385, 440, 40, "원격지 비어 있음 = 누구나", RED, 17), 1, 1)
    for pts in ([(810, 140), (520, 255)], [(800, 275), (540, 275)], [(810, 395), (520, 295)]):
        p.fly(packet(0, 0, RED), pts, 1, 0.1, 0.9)
    p.at(cell(260, 385, 440, 40, "원격지 " + CUST + "만 허용", GREEN, 17), 2, 4, mark=(260, 385, 440, 40))
    p.at(cross(650, 197) + cross(650, 343) + check(650, 275), 3, 4, mark=(628, 253, 44, 44))
    p.at(pill(480, 456, "시연 기간만 열고 · 로그인 · 기록", ORANGE, 16, True, 340), 4, 4)
    return p.render()


ITEMS = [
    ("u12-l03-p01-static-mapping", p1, "변환표에 줄을 미리 적어 두면?",
     "자동으로 생기는 동적 매핑과 관리자가 미리 적는 정적 매핑을 비교하고, 외부 TCP 8080을 192.168.10.50:8080으로 보내는 포트 포워딩 한 줄을 보여 줍니다.",
     "포트 포워딩은 직접 적어 넣는 정적 매핑입니다."),
    ("u12-l03-p02-settings-form", p2, "포트 포워딩 설정 화면",
     "공유기 포트 포워딩 화면의 외부 포트 8080, 프로토콜 TCP, 내부 IP 192.168.10.50, 내부 포트 8080, 원격지 비움 칸을 바깥 값과 안쪽 값으로 나누어 채웁니다.",
     "칸마다 바깥 값인지 안쪽 값인지 구별해 채웁니다."),
    ("u12-l03-p03-public-address", p3, "박 팀장은 어떤 주소로 접속할까?",
     "박 팀장의 요청이 198.51.100.25:8080으로 도착하면 공유기가 8080 규칙으로 목적지를 192.168.10.50:8080으로 바꿔 AI 서버에 전달하고 응답은 바깥 주소가 답한 것처럼 보입니다.",
     "바깥에서는 공유기의 바깥 주소로 접속하고 공유기가 목적지를 바꿔 줍니다."),
    ("u12-l03-p04-two-services", p4, "서비스가 둘이면 규칙도 둘일까?",
     "AI 서버는 외부 8080, 도면 NAS 192.168.10.30은 외부 5001로 나누어야 하고 같은 외부 8080을 두 곳에 쓰면 충돌합니다.",
     "서비스마다 외부 포트를 나누어 규칙을 추가합니다."),
    ("u12-l03-p05-hairpin", p5, "사무실에서 공인 주소로 시험하면?",
     "사무실 PC가 공유기의 바깥 주소 198.51.100.25:8080으로 접속하면 공유기가 안쪽으로 되돌려 보내야 하는 헤어핀 NAT가 필요하며 장비에 따라 안 될 수 있고, 휴대폰 데이터 같은 바깥 회선에서 시험하면 확인됩니다.",
     "포트 포워딩 시험은 사무실 밖 회선에서 합니다."),
    ("u12-l03-p06-not-open-checklist", p6, "포워딩했는데 왜 밖에서 안 열릴까?",
     "서버 수신 주소, GPU PC 방화벽, 규칙의 내부 IP·포트·프로토콜, 공유기 WAN 주소를 가까운 곳부터 확인하고 방화벽의 8080을 허용해 해결하는 점검표입니다.",
     "확인 순서를 정해 하나씩 지워 갑니다."),
    ("u12-l03-p07-open-port-risk", p7, "포트를 열어도 정말 괜찮을까?",
     "원격지를 비운 8080은 누구에게나 열리지만 원격지를 고객사 주소 192.0.2.77로 제한하면 낯선 출발지는 막히고, 시연 기간만 열고 로그인과 기록을 남긴다는 정책입니다.",
     "열린 포트는 원격지 제한, 기간 한정, 기록으로 노출을 줄입니다."),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, fn, *_ in ITEMS:
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        wire_pages(LESSON / "lesson.md", [(f, t, al, c) for f, _, t, al, c in ITEMS])
    print("ok", len(ITEMS), "svgs")
