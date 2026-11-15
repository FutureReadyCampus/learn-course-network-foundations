#!/usr/bin/env python3
"""Unit 12 Lesson 3 SVG review: rewrites Pages 1,3,4,5, adds second SVGs for Pages 1 (변환≠허용), 2 (DHCP 예약), 6 (CGNAT/이중 NAT).
Pages 2, 6, 7 keep the earlier SVGs (u12_new_l03_forwarding.py). Run from repo root; --svg-only skips the lesson.md edit."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403
from u12_new_l03_forwarding import ITEMS as OLD, RULE

LESSON = lesson_dir(3)
OUT = LESSON / "assets" / "animations"
ADDR, PUB, CUST = f"{AI}:{AI_PORT}", f"{WAN}:{AI_PORT}", "192.0.2.77"
RULE_SHORT = f"외부 {AI_PORT} → {ADDR}"


def tagcard(x, y, w, s, c, fs=17):
    return cell(x, y, w, 44, s, c, fs)


def p1():
    p = Pg("변환표에 줄을 미리 적어 두면?", "자동으로 생기는 줄과 사람이 적는 줄",
           ["변환표에는 나갈 때 자동으로 생긴 줄만 있어요", "지우가 바깥 8080을 GPU PC로 보내는 줄을 적어요",
            "바깥 8080 요청이 오면 이 줄을 보고 보내요", "직접 적은 줄이 정적 매핑, 포트 포워딩이에요"])
    p.base(box(60, 120, 840, 250, LINE, PANEL, 16, sw=2), ledger(110, 160), lbl(250, 168, "공유기 변환표", MUTED, 20),
           cell(90, 195, 450, 56, "192.168.10.41:3000 → 53001", MUTED, 18), pill(740, 223, "동적 매핑 (자동)", MUTED, 17, False, 250),
           box(90, 280, 450, 56, LINE, PANEL, 6, dash=True, sw=2))
    p.at(lbl(315, 315, "아직 적은 줄이 없어요", MUTED, 17), 1, 1)
    p.at(pill(480, 420, "바깥 8080 요청을 보낼 줄이 아직 없어요", MUTED, 17, False, 400), 1, 1)
    p.at(cell(90, 280, 450, 56, RULE_SHORT, BLUE, 18) + pill(740, 308, "정적 매핑 (직접 적음)", BLUE, 17, False, 250), 2, 3, mark=(90, 280, 450, 56))
    p.at(check(575, 308) + pill(480, 420, "바깥 8080 요청이 오면 이 줄을 보고 GPU PC로 보내요", BLUE, 17, False, 560), 3, 3, mark=(90, 280, 450, 56))
    p.at(cell(90, 280, 450, 56, RULE_SHORT, BLUE, 18) + pill(740, 308, "정적 매핑 = 포트 포워딩", ORANGE, 17, True, 250), 4, 4, mark=(615, 288, 250, 40))
    return p.render()


def p1b():
    p = Pg("규칙을 적으면 바로 들어올 수 있을까?", "주소를 바꿔 주는 것과 들여보내는 것은 달라요",
           ["공유기에 8080 변환 규칙을 적어 두었어요", "공유기는 목적지만 GPU PC 주소로 바꿔 줘요",
            "방화벽이 8080을 막으면 요청은 닿지 못해요", "방화벽에서 허용을 따로 열어야 들어가요"])
    wall = lambda c, gap=False: (box(600, 215, 26, 60, c, c, 4) + box(600, 325, 26, 60, c, c, 4) if gap else box(600, 215, 26, 170, c, c, 4))
    p.base(laptop(100, 300, "박 팀장"), rt(380, 300), dsrv(820, 300, "GPU PC"), lbl(613, 200, "방화벽", MUTED, 17),
           line(150, 300, 350, 300, LINE, 4, "8 6"), line(410, 300, 596, 300, LINE, 4, "8 6"), line(630, 300, 780, 300, LINE, 4, "8 6"))
    p.at(wall(MUTED), 1, 2)
    p.at(cell(205, 155, 350, 46, "외부 8080 → " + ADDR, BLUE, 17), 1, 4)
    p.fly(packet(0, 0, BLUE), [(160, 300), (325, 300)], 1, 0.1, 0.9)
    p.mark((205, 155, 350, 46), 1)
    p.at(pill(480, 445, "목적지가 " + ADDR + "로 바뀌어요", BLUE, 17, False, 440), 2, 2, mark=(260, 427, 440, 36))
    p.fly(packet(0, 0, GREEN), [(430, 300), (575, 300)], 2, 0.1, 0.9)
    p.at(wall(RED) + cross(613, 300) + pill(480, 445, "방화벽이 막으면 닿지 못해요", RED, 17, False, 330), 3, 3, mark=(600, 215, 26, 170))
    p.at(wall(GREEN, True) + check(613, 300) + pill(480, 445, "변환 규칙 ≠ 허용, 방화벽은 따로 열어요", ORANGE, 17, True, 440), 4, 4, mark=(600, 275, 26, 50))
    p.fly(packet(0, 0, GREEN), [(650, 300), (755, 300)], 4, 0.1, 0.9)
    return p.render()


def p2b():
    p = Pg("GPU PC 주소가 바뀌면 규칙은?", "규칙의 내부 IP가 옛 주소를 가리키면 안 닿아요",
           ["규칙이 GPU PC 주소 192.168.10.50을 가리켜요", "재부팅하자 GPU PC 주소가 .57로 바뀌었어요",
            "규칙은 옛 주소 .50을 그대로 가리켜요", "DHCP 예약으로 .50을 계속 받게 묶어요"])
    p.base(rt(250, 300), dsrv(730, 300, "GPU PC"), cell(60, 200, 380, 44, RULE_SHORT, BLUE, 17), line(290, 300, 690, 300, LINE, 4, "8 6"))
    p.at(line(290, 300, 690, 300, GREEN, 5) + pill(730, 395, AI, GREEN, 17, False, 200), 1, 1)
    p.at(pill(730, 395, "192.168.10.57", ORANGE, 17, True, 200), 2, 3, mark=(630, 377, 200, 36))
    p.at(line(290, 300, 690, 300, RED, 5, "10 6") + cross(490, 300) + pill(250, 395, "규칙은 옛 주소 .50을 가리켜요", RED, 16, False, 330), 3, 3, mark=(60, 200, 380, 44))
    p.at(cell(460, 150, 460, 46, "DHCP 예약: MAC 주소 → " + AI, GREEN, 17), 4, 4, mark=(460, 150, 460, 46))
    p.at(line(290, 300, 690, 300, GREEN, 5) + check(490, 300) + pill(730, 395, AI, GREEN, 17, False, 200), 4, 4)
    return p.render()


def mcard(x, y, src, dst, c, w=300):
    return (box(x, y, w, 76, c, PANEL, 8, sw=3) + text(x + 14, y + 31, "출발 " + src, 17, TXT, anchor="start")
            + text(x + 14, y + 61, "도착 " + dst, 17, TXT, anchor="start"))


def p3():
    p = Pg("박 팀장은 어떤 주소로 접속할까?", "바깥 주소로 오면 공유기가 목적지를 바꿔 줘요",
           ["박 팀장은 사설 주소가 아니라 바깥 주소로 가요", "공유기가 8080 줄을 찾아 목적지를 바꿔요",
            "목적지가 192.168.10.50:8080으로 바뀌어요", "응답은 198.51.100.25:8080이 한 것처럼 보여요"])
    p.base(dsrv(110, 340), rt(480, 340), laptop(850, 340, "박 팀장"), line(150, 340, 450, 340, LINE, 4, "8 6"), line(510, 340, 800, 340, LINE, 4, "8 6"))
    p.at(lbl(770, 142, "공유기 바깥쪽", MUTED, 17) + mcard(620, 155, CUST + ":49152", PUB, BLUE), 1, 3)
    p.fly(packet(0, 0, BLUE), [(800, 340), (540, 340)], 1, 0.1, 0.9)
    p.at(cell(320, 250, 320, 44, f"{AI_PORT} → {ADDR}", ORANGE, 17), 2, 3, mark=(320, 250, 320, 44))
    p.at(lbl(190, 142, "공유기 안쪽", MUTED, 17) + mcard(40, 155, CUST + ":49152", ADDR, GREEN), 3, 3, mark=cl(40, 155, 1))
    p.fly(packet(0, 0, GREEN), [(440, 340), (170, 340)], 3, 0.1, 0.9)
    p.at(check(110, 275), 3, 4)
    p.at(lbl(770, 142, "박 팀장이 받은 응답", MUTED, 17) + mcard(620, 155, PUB, CUST + ":49152", ORANGE), 4, 4, mark=cl(620, 155, 0))
    p.fly(packet(0, 0, ORANGE), [(540, 340), (765, 340)], 4, 0.1, 0.9)
    p.at(pill(480, 440, f"박 팀장은 {PUB}가 답한 것으로 봐요", ORANGE, 17, True, 460), 4, 4)
    return p.render()


def p4():
    p = Pg("서비스가 둘이면 규칙도 둘일까?", "외부 포트 하나는 안쪽 한 곳으로만 가요",
           ["AI 서버 외에 도면 NAS도 밖에서 열어 달라고 해요", "NAS 규칙도 같은 외부 8080으로 적어 봐요",
            "같은 외부 8080이 두 줄이면 충돌해요", "NAS는 외부 5001처럼 포트를 따로 나눠요"])
    ai = cell(430, 165, 440, 70, "AI 서버 " + ADDR, GREEN, 19)
    nas = cell(430, 275, 440, 70, "도면 NAS 192.168.10.30:5001", BLUE, 19)
    p.base(lbl(210, 145, "바깥: 외부 포트", MUTED, 17), lbl(650, 145, "안쪽: 보낼 곳", MUTED, 17),
           cell(90, 165, 240, 70, "외부 TCP 8080", BLUE, 20), text(380, 212, "→", 32, MUTED, 700), ai,
           box(90, 275, 240, 70, LINE, PANEL, 6, dash=True, sw=2), text(380, 322, "→", 32, MUTED, 700), nas)
    p.at(lbl(210, 320, "아직 없음", MUTED, 18), 1, 1)
    p.at(pill(480, 425, "NAS도 열어 달라는 요청이 왔어요", MUTED, 17, False, 380), 1, 1)
    p.at(cell(90, 275, 240, 70, "외부 TCP 8080", BLUE, 20), 2, 2, mark=(90, 275, 240, 70))
    p.at(cell(90, 165, 240, 70, "외부 TCP 8080", RED, 20) + cell(90, 275, 240, 70, "외부 TCP 8080", RED, 20) + cross(380, 255)
         + pill(480, 425, "같은 외부 포트는 한 곳으로만 보내요", RED, 17, False, 380), 3, 3, mark=(90, 165, 240, 180))
    p.at(cell(90, 165, 240, 70, "외부 TCP 8080", GREEN, 20) + cell(90, 275, 240, 70, "외부 TCP 5001", GREEN, 20) + check(380, 255)
         + pill(480, 425, "서비스마다 외부 포트를 나눠요", ORANGE, 17, True, 380), 4, 4, mark=(90, 275, 240, 70))
    return p.render()


def p5():
    p = Pg("사무실에서 공인 주소로 시험하면?", "안쪽에서 바깥 주소로 가면 되돌아와야 해요",
           ["지우가 사무실 PC에서 198.51.100.25:8080을 입력해요", "공유기가 안쪽으로 되돌려 보내야 해요(헤어핀)",
            "장비와 설정에 따라 지원하지 않을 수 있어요", "시험은 휴대폰 데이터 같은 바깥 회선에서 해요"])
    arc = lambda c, dash: (f'<path d="M455 305 Q 390 390 300 372" fill="none" stroke="{c}" stroke-width="5" stroke-dasharray="{dash}"/>'
                           f'<polygon points="292,370 312,358 312,382" fill="{c}"/>')
    p.base(net(40, 125, 300, 335, "사무실 LAN", GREEN), pc(110, 210, "지우 PC"), dsrv(260, 350), rt(480, 280), phone(850, 280, "휴대폰 데이터"),
           line(510, 280, 800, 280, LINE, 4, "8 6"))
    p.fly(packet(0, 0, BLUE), [(150, 210), (445, 275)], 1, 0.05, 0.9)
    p.at(pill(560, 165, "목적지 " + PUB, BLUE, 17, False, 320), 1, 1, mark=(400, 145, 320, 40))
    p.at(arc(ORANGE, "10 6") + pill(600, 440, "헤어핀 NAT: 안쪽으로 다시 돌려요", ORANGE, 17, True, 360), 2, 2)
    p.at(arc(RED, "4 8") + cross(384, 364) + pill(600, 440, "장비에 따라 안 될 수 있어요", RED, 17, False, 320), 3, 3, mark=(362, 342, 44, 44))
    p.fly(packet(0, 0, BLUE), [(810, 280), (520, 280), (300, 345)], 4, 0.05, 0.95)
    p.at(check(260, 280) + pill(600, 440, "시험은 사무실 밖 회선에서 해요", GREEN, 17, True, 360), 4, 4)
    return p.render()


def p6b():
    Y6 = 240
    p = Pg("WAN 주소로 앞단을 알아낼 수 있을까?", "WAN 주소가 규칙이 인터넷에 닿는지 알려 줘요",
           ["공유기 WAN 주소를 보면 앞단에 무엇이 있는지 알아요", "100.64.0.0/10 안이면 통신사 NAT(CGNAT)가 있어요",
            "192.168.x.x 사설 주소면 앞단 공유기(이중 NAT)예요", "공인 주소면 NAT가 더 없어서 규칙이 닿아요"])
    p.base(cloud(95, Y6), rt(570, Y6, "우리 공유기"), dsrv(840, Y6, "AI 서버"), line(165, Y6, 235, Y6, LINE, 4, "8 6"),
           line(385, Y6, 540, Y6, LINE, 4, "8 6"), line(600, Y6, 800, Y6, LINE, 4, "8 6"))
    mid = lambda s, c: box(235, Y6 - 45, 150, 90, c, PANEL, 10, sw=3) + text(310, Y6 + 7, s, 18, c, 700)
    wan = lambda s, c: lbl(570, Y6 + 95, "WAN 주소", MUTED, 17) + cell(470, Y6 + 105, 200, 42, s, c, 18)
    p.at(box(235, Y6 - 45, 150, 90, LINE, PANEL, 10, dash=True, sw=2) + text(310, Y6 + 8, "앞단은?", 18, MUTED, 700) + wan("WAN ?", MUTED), 1, 1)
    p.at(mid("통신사 NAT", RED) + wan("100.66.7.9", RED) + cross(460, Y6) + pill(480, 432, "통신사 NAT에는 우리 규칙이 없어요", RED, 16, False, 380), 2, 2, mark=(235, Y6 - 45, 150, 90))
    p.at(mid("앞단 공유기", RED) + wan("192.168.x.x", RED) + cross(460, Y6) + pill(480, 432, "앞단 공유기에는 우리 규칙이 없어요", RED, 16, False, 380), 3, 3, mark=(235, Y6 - 45, 150, 90))
    p.at(line(165, Y6, 540, Y6, GREEN, 5) + wan("198.51.100.25", GREEN) + check(340, Y6) + pill(480, 432, "공인 주소: NAT가 더 없어요", GREEN, 16, False, 340), 4, 4, mark=(470, Y6 + 105, 200, 42))
    return p.render()


NEW = {
    "u12-l03-p01-table-lines": (p1, "변환표에 줄을 미리 적어 두면?",
        "공유기 변환표에 나갈 때 자동으로 생긴 동적 매핑 줄만 있다가, 지우가 외부 8080을 192.168.10.50:8080으로 보내는 줄을 직접 적으면 바깥 8080 요청이 그 줄로 가고, 직접 적은 줄이 정적 매핑인 포트 포워딩임을 보여 줍니다.",
        "포트 포워딩은 직접 적어 넣는 정적 매핑입니다."),
    "u12-l03-p01b-translate-not-allow": (p1b, "규칙을 적으면 바로 들어올 수 있을까?",
        "공유기의 8080 변환 규칙은 목적지만 GPU PC 주소로 바꿔 줄 뿐이라 방화벽이 8080을 막으면 요청이 닿지 못하고, 방화벽에서 허용을 따로 열어야 들어갑니다.",
        "주소를 바꾸는 변환 규칙과 들여보내는 허용은 따로입니다."),
    "u12-l03-p02b-dhcp-reservation": (p2b, "GPU PC 주소가 바뀌면 규칙은?",
        "규칙이 GPU PC의 192.168.10.50을 가리키다가 재부팅으로 주소가 192.168.10.57로 바뀌면 규칙은 옛 주소를 가리켜 닿지 못하고, DHCP 예약으로 MAC 주소에 192.168.10.50을 묶어 두면 해결됩니다.",
        "내부 IP가 바뀌지 않게 DHCP 예약으로 묶어 둡니다."),
    "u12-l03-p03-dest-rewrite": (p3, "박 팀장은 어떤 주소로 접속할까?",
        "박 팀장의 요청이 198.51.100.25:8080으로 도착하면 공유기가 8080 규칙으로 목적지를 192.168.10.50:8080으로 바꿔 GPU PC에 전달하고, 응답은 198.51.100.25:8080이 답한 것처럼 돌아옵니다.",
        "바깥에서는 공유기의 바깥 주소로 접속하고 공유기가 목적지를 바꿔 줍니다."),
    "u12-l03-p04-one-port-one-target": (p4, "서비스가 둘이면 규칙도 둘일까?",
        "AI 서버는 외부 8080으로 이미 연결돼 있고, 도면 NAS도 같은 외부 8080으로 적으면 충돌하므로 NAS는 외부 5001처럼 외부 포트를 나누어 규칙을 추가합니다.",
        "서비스마다 외부 포트를 나누어 규칙을 추가합니다."),
    "u12-l03-p05-hairpin-loop": (p5, "사무실에서 공인 주소로 시험하면?",
        "사무실 PC가 공유기의 바깥 주소 198.51.100.25:8080으로 접속하면 공유기가 안쪽으로 되돌려 보내는 헤어핀 NAT가 필요하지만 장비에 따라 안 될 수 있어서, 휴대폰 데이터 같은 바깥 회선에서 시험합니다.",
        "포트 포워딩 시험은 사무실 밖 회선에서 합니다."),
    "u12-l03-p06b-wan-cgnat": (p6b, "WAN 주소로 앞단을 알아낼 수 있을까?",
        "공유기 WAN 주소가 100.64.0.0/10 안이면 통신사 NAT(CGNAT), 192.168.x.x 사설 주소면 앞단 공유기(이중 NAT)라서 규칙이 인터넷에 닿지 않고, 공인 주소 198.51.100.25면 NAT가 더 없어 규칙이 닿습니다.",
        "WAN 주소를 보면 CGNAT, 이중 NAT, 공인 주소를 구별할 수 있습니다."),
}


def old(i):
    f, _, t, al, c = OLD[i - 1]
    return (f, t, al, c)


def pages():
    n = lambda k, ap: (k, NEW[k][1], NEW[k][2], NEW[k][3], ap)
    o = lambda i, ap: (*old(i), ap)
    return [
        [n("u12-l03-p01-table-lines", 2), n("u12-l03-p01b-translate-not-allow", 3)],
        [o(2, 2), n("u12-l03-p02b-dhcp-reservation", 3)],
        [n("u12-l03-p03-dest-rewrite", 2)],
        [n("u12-l03-p04-one-port-one-target", 1)],
        [n("u12-l03-p05-hairpin-loop", 1)],
        [o(6, 2), n("u12-l03-p06b-wan-cgnat", 3)],
        [o(7, 0)],
    ]


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, (fn, *_) in NEW.items():
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages())
    print("ok", len(NEW), "svgs")
