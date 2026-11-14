#!/usr/bin/env python3
"""Unit 12 Lesson 5 (포트를 안 열어도 되는 NAT 통과): one 4-step example SVG per Page (7).
Run from repo root: python3 scripts/svg_pairs/u12_new_l05_nat_traversal.py  (--svg-only skips the lesson.md edit).
Example: 박 팀장 집 192.168.0.20 / 192.0.2.123, 지우 PC 192.168.10.41 / 198.51.100.25, STUN·TURN 203.0.113.60, 협력사 203.0.113.99 / .15."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(5)
OUT = LESSON / "assets" / "animations"
HOME, HOMEWAN, STUN = "192.168.0.20", "192.0.2.123", "203.0.113.60"


def p1():
    p = Pg("포트를 안 열었는데 화상회의는?", "둘 다 바깥으로 먼저 연결하면 막히지 않아요",
           ["양쪽 모두 공유기 뒤에 있고 포트는 안 열었어요", "둘 다 서비스 서버로 먼저 연결해요",
            "영상과 음성이 서버를 거쳐 오가요", "일부 앱은 서버 없이 직접(P2P)도 시도해요"])
    p.base(laptop(90, 290, "박 팀장"), rt(250, 290), dsrv(480, 290, "화상회의 서버"), rt(710, 290), laptop(870, 290, "협력사"),
           line(140, 290, 222, 290, LINE, 4, "8 6"), line(278, 290, 435, 290, LINE, 4, "8 6"),
           line(525, 290, 682, 290, LINE, 4, "8 6"), line(738, 290, 820, 290, LINE, 4, "8 6"))
    p.at(pill(480, 175, "양쪽 모두 공유기 뒤 · 열린 포트 없음", MUTED, 17, False, 400), 1, 1)
    p.fly(packet(0, 0, BLUE), [(140, 290), (440, 290)], 2, 0.05, 0.95)
    p.fly(packet(0, 0, BLUE), [(820, 290), (520, 290)], 2, 0.05, 0.95)
    p.mark((436, 245, 88, 90), 2)
    p.at(check(480, 215) + pill(480, 400, "서버를 거치니 포트를 열 일이 없어요", GREEN, 17, True, 380), 3, 3, mark=(458, 193, 44, 44))
    p.at(line(130, 395, 830, 395, ORANGE, 4, "10 8") + pill(480, 445, "일부 앱은 서버 없이 직접(P2P)도 시도해요", ORANGE, 17, True, 440), 4, 4)
    return p.render()


def p2():
    p = Pg("NAT에게 꼭 따로 물어야 할 두 가지", "이름 하나로 연결 가능성을 판단하지 않아요",
           ["지우의 메모는 이름만 보고 안 될 거라 판단했어요", "첫째 질문은 매핑: 바깥에 어떻게 보이나요",
            "둘째 질문은 필터링: 누가 보낸 패킷을 받나요", "그래서 두 질문을 따로 확인한다고 고쳐요"])
    L, R, Y0 = 60, 510, 245
    p.at(cell(220, 135, 520, 44, "지우 메모: Port Restricted라서 안 될 거야", RED, 17) + pill(480, 205, "그런데 회의는 잘 되고 있어요", GREEN, 16, False, 280), 1, 3)
    p.at(cell(220, 135, 520, 44, "새 메모: 매핑과 필터링을 따로 확인한다", GREEN, 17) + check(780, 157), 4, 4, mark=(220, 135, 520, 44))
    p.at(box(L, Y0, 390, 200, BLUE, PANEL, 14, sw=2) + lbl(L + 195, Y0 + 32, "① 매핑", BLUE, 20)
         + cell(L + 25, Y0 + 55, 340, 48, "바깥에 어떤 주소·포트로 보이나?", BLUE, 17) + pill(L + 195, Y0 + 140, "변환표의 External 칸", BLUE, 16, False, 230), 2, mark=(L, Y0, 390, 200))
    p.at(box(R, Y0, 390, 200, GREEN, PANEL, 14, sw=2) + lbl(R + 195, Y0 + 32, "② 필터링", GREEN, 20)
         + cell(R + 25, Y0 + 55, 340, 48, "누가 보낸 패킷까지 받나?", GREEN, 17) + pill(R + 195, Y0 + 140, "들여보내기 전의 조건", GREEN, 16, False, 230), 3, mark=(R, Y0, 390, 200))
    return p.render()


def p3():
    p = Pg("상대가 바뀌면 바깥 포트도 바뀔까?", "소개한 주소가 협력사에도 맞는지 물어요",
           ["STUN 서버가 본 바깥 주소를 협력사에 알려 줘요", "서버와 통신할 때는 두 방식 모두 :40001이에요",
            "협력사와 통신하면 오른쪽만 :40017로 달라져요", "소개한 주소가 협력사에는 안 맞아요"])
    L, R, Y0 = 60, 510, 215
    strip = (cell(40, 135, 270, 44, "박 팀장 PC " + HOME + ":3000", GREEN, 15) + line(310, 157, 340, 157, MUTED, 3)
             + cell(340, 135, 250, 44, "STUN " + STUN + ":3478", BLUE, 15) + line(590, 157, 620, 157, MUTED, 3)
             + cell(620, 135, 300, 44, "서버가 본 주소 " + HOMEWAN + ":40001", ORANGE, 15))
    p.at(strip, 1, mark=(40, 135, 880, 44))
    box_ = lambda x, t, c: box(x, Y0, 390, 190, c, PANEL, 14, sw=2) + lbl(x + 195, Y0 + 32, t, c, 18)
    p.at(box_(L, "상대와 무관한 매핑", GREEN) + box_(R, "상대마다 달라지는 매핑", BLUE)
         + cell(L + 25, Y0 + 50, 340, 44, "서버 → " + HOMEWAN + ":40001", GREEN, 15) + cell(R + 25, Y0 + 50, 340, 44, "서버 → " + HOMEWAN + ":40001", BLUE, 15), 2,
         mark=(L + 25, Y0 + 50, 340, 44))
    p.mark((R + 25, Y0 + 50, 340, 44), 2)
    p.at(cell(L + 25, Y0 + 110, 340, 44, "협력사 → " + HOMEWAN + ":40001", GREEN, 15) + cell(R + 25, Y0 + 110, 340, 44, "협력사 → " + HOMEWAN + ":40017", RED, 15), 3,
         mark=(R + 25, Y0 + 110, 340, 44))
    p.at(cross(R + 360, Y0 + 32) + pill(480, 450, "소개한 주소가 협력사에는 안 맞아요", RED, 17, False, 360), 4, 4)
    return p.render()


def p4():
    p = Pg("누가 보낸 패킷까지 받아 줄까?", "필터링은 받는 상대의 범위를 정해요",
           ["지우 PC가 협력사 서버로 먼저 UDP를 보냈어요", "누구든 받는 방식은 두 패킷을 모두 받아요",
            "같은 IP만 받는 방식은 포트가 달라도 받아요", "같은 IP·포트만 받는 방식은 둘 다 막아요"])
    X, W = 140, [240, 220, 220]
    cols = [X, X + W[0], X + W[0] + W[1]]
    rows = [("누구든 받음(EIF)", "받음", "받음"), ("같은 IP만(ADF)", "받음", "받지 않음"), ("같은 IP·포트만(APDF)", "받지 않음", "받지 않음")]
    p.base(cell(cols[0], 215, W[0] - 6, 36, "필터링 방식", MUTED, 15, BG) + cell(cols[1], 215, W[1] - 6, 36, "203.0.113.15:7777", MUTED, 15, BG)
           + cell(cols[2], 215, W[2] - 6, 36, "203.0.113.99:40000", MUTED, 15, BG))
    p.at(cell(40, 135, 430, 44, "지우 PC가 203.0.113.15:5555로 먼저 보냈어요", GREEN, 15) + cell(490, 135, 430, 44, "바깥 매핑 " + WAN + ":42000", ORANGE, 15), 1,
         mark=(490, 135, 430, 44))
    for i, (a_, b_, c_) in enumerate(rows):
        y = 259 + i * 50
        cc = lambda v: GREEN if v == "받음" else RED
        p.at(cell(cols[0], y, W[0] - 6, 42, a_, BLUE, 16) + cell(cols[1], y, W[1] - 6, 42, b_, cc(b_), 16) + cell(cols[2], y, W[2] - 6, 42, c_, cc(c_), 16),
             i + 2, 4, mark=(cols[0], y, sum(W) - 6, 42))
    p.at(pill(480, 450, "포트까지 보면 받는 범위가 좁아져요", ORANGE, 17, True, 360), 4, 4)
    return p.render()


def p5():
    p = Pg("Full Cone, Symmetric은 어떻게 읽을까?", "옛 이름을 매핑과 필터링으로 풀어요",
           ["제품 설명서에 Full Cone 문구가 보여요", "Cone 세 가지는 매핑이 같고 필터링이 달라요",
            "Symmetric은 매핑이 상대에 따라 달라져요", "이름 대신 매핑·필터링을 나눠 읽어요"])
    X, W = 85, [230, 260, 300]
    cols = [X, X + W[0], X + W[0] + W[1]]
    rows = [("Full Cone", "상대와 무관", "누구든 받음", GREEN), ("Restricted Cone", "상대와 무관", "같은 IP만 받음", GREEN),
            ("Port Restricted Cone", "상대와 무관", "같은 IP·포트만 받음", GREEN), ("Symmetric", "상대에 따라 달라짐", "상대와 연관된 조건", RED)]
    ys = [249 + i * 46 for i in range(4)]
    p.at(cell(60, 135, 840, 44, "제품 설명서: “Full Cone 지원, P2P에 최적”", ORANGE, 17), 1, 1, mark=(60, 135, 840, 44))
    p.at(cell(cols[0], 205, W[0] - 6, 36, "옛 이름", MUTED, 15, BG) + cell(cols[1], 205, W[1] - 6, 36, "매핑", MUTED, 15, BG) + cell(cols[2], 205, W[2] - 6, 36, "필터링", MUTED, 15, BG), 2)
    for i, (a_, b_, c_, col) in enumerate(rows):
        y = ys[i]
        p.at(cell(cols[0], y, W[0] - 6, 40, a_, col, 16) + cell(cols[1], y, W[1] - 6, 40, b_, col, 16) + cell(cols[2], y, W[2] - 6, 40, c_, col, 16),
             2 if i < 3 else 3, 4)
    p.mark((cols[0], ys[0], sum(W) - 6, 40 + 46 * 2), 2)
    p.mark((cols[0], ys[3], sum(W) - 6, 40), 3)
    p.at(pill(480, 455, "이름 말고 매핑과 필터링을 따로 읽어요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p6():
    p = Pg("양쪽에서 먼저 보내면 길이 열릴까?", "UDP 홀 펀칭은 동시에 인사하는 방법이에요",
           ["양쪽이 STUN 서버에 자기 바깥 주소를 물어요", "소개 서버가 서로의 바깥 주소를 알려 줘요",
            "양쪽이 동시에 먼저 보내 임시 줄을 만들어요", "조건이 맞으면 직접 연결이 이어져요"])
    p.base(dsrv(480, 185, "") + text(545, 192, "소개·STUN 서버", 17, TXT, 700, anchor="start"), laptop(100, 370, "박 팀장 PC"), rt(290, 370, "집 공유기"), rt(670, 370, "회사 공유기"), pc(860, 370, "지우 PC"),
           line(145, 370, 262, 370, LINE, 4, "8 6"), line(698, 370, 815, 370, LINE, 4, "8 6"),
           line(290, 342, 445, 225, LINE, 3, "8 6"), line(670, 342, 515, 225, LINE, 3, "8 6"), line(320, 370, 640, 370, LINE, 3, "8 6"))
    p.fly(packet(0, 0, BLUE), [(290, 342), (450, 225)], 1, 0.05, 0.95)
    p.fly(packet(0, 0, BLUE), [(670, 342), (510, 225)], 1, 0.05, 0.95)
    p.at(pill(215, 300, "상대 " + WAN + ":42000", ORANGE, 14, False, 250) + pill(745, 300, "상대 " + HOMEWAN + ":40001", ORANGE, 14, False, 250), 2, 2,
         mark=(90, 282, 250, 36))
    p.mark((620, 282, 250, 36), 2)
    p.fly(packet(0, 0, ORANGE), [(320, 370), (470, 370)], 3, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(640, 370), (490, 370)], 3, 0.05, 0.95)
    p.at(pill(290, 315, "임시 줄 생김", ORANGE, 14, True, 120) + pill(670, 315, "임시 줄 생김", ORANGE, 14, True, 120), 3, 3, mark=(230, 297, 120, 36))
    p.mark((610, 297, 120, 36), 3)
    p.at(line(320, 370, 640, 370, GREEN, 6) + check(480, 320) + pill(480, 462, "조건이 맞으면 직접 연결 성공", GREEN, 17, True, 340), 4, 4)
    return p.render()


def p7():
    p = Pg("직접 못 만나면 누가 대신 전해 줄까?", "TURN 서버가 교환원처럼 데이터를 중계해요",
           ["먼저 두 PC가 직접 연결을 시도해요", "UDP 차단이나 상대별 매핑이면 직접이 막혀요",
            "양쪽이 TURN 서버로 연결해 대신 전달받아요", "중계는 확실하지만 서버 비용과 지연이 들어요"])
    p.base(dsrv(480, 205, "TURN 서버"), pill(480, 300, STUN, BLUE, 15, False, 150), laptop(110, 370, "박 팀장"), pc(850, 370, "지우 PC"),
           line(170, 370, 790, 370, LINE, 4, "8 6"))
    p.fly(packet(0, 0, ORANGE), [(170, 370), (440, 370)], 1, 0.05, 0.95)
    p.fly(packet(0, 0, ORANGE), [(790, 370), (520, 370)], 1, 0.05, 0.95)
    p.at(cross(480, 370) + pill(480, 445, "UDP 차단 · 상대별 매핑 · 통신사 NAT", RED, 16, False, 400), 2, 2, mark=(458, 348, 44, 44))
    p.at(cross(480, 370), 3, 4)
    p.at(line(170, 350, 446, 215, GREEN, 5) + line(790, 350, 514, 215, GREEN, 5) + check(570, 205), 3, 4, mark=(548, 183, 44, 44))
    p.fly(packet(0, 0, GREEN), [(170, 350), (446, 215)], 3, 0.1, 0.9)
    p.fly(packet(0, 0, GREEN), [(514, 215), (790, 350)], 3, 0.1, 0.9)
    p.at(pill(480, 445, "중계는 확실하지만 서버 비용과 지연이 들어요", ORANGE, 17, True, 460), 4, 4)
    return p.render()


ITEMS = [
    ("u12-l05-p01-video-call-no-port", p1, "포트를 안 열었는데 화상회의는?",
     "박 팀장과 협력사가 모두 공유기 뒤에 있어도 둘 다 화상회의 서버로 먼저 연결하면 포트를 열지 않아도 영상과 음성이 오가고, 일부 앱은 서버 없이 직접 연결도 시도한다는 그림입니다.",
     "안쪽에서 바깥으로 먼저 나가는 연결에는 포트 개방이 필요 없습니다."),
    ("u12-l05-p02-two-questions", p2, "NAT에게 꼭 따로 물어야 할 두 가지",
     "지우의 메모를 이름만 보고 판단한 것에서 매핑과 필터링을 따로 확인하는 것으로 고치고, 매핑은 External 칸, 필터링은 응답을 들여보내기 전의 조건이라는 두 질문을 보여 줍니다.",
     "NAT는 매핑과 필터링을 따로 확인합니다."),
    ("u12-l05-p03-mapping-by-peer", p3, "상대가 바뀌면 바깥 포트도 바뀔까?",
     "박 팀장 PC 192.168.0.20이 STUN 서버 203.0.113.60에는 192.0.2.123:40001로 보였지만 협력사에는 상대마다 다른 매핑이면 :40017로 보여 소개한 주소가 맞지 않는다는 비교입니다.",
     "소개 서버가 알려 준 주소가 맞으려면 매핑이 상대와 무관해야 합니다."),
    ("u12-l05-p04-filtering", p4, "누가 보낸 패킷까지 받아 줄까?",
     "지우 PC가 203.0.113.15:5555로 먼저 보낸 뒤 바깥 매핑 198.51.100.25:42000으로 203.0.113.15:7777과 203.0.113.99:40000의 패킷이 도착할 때 누구든, 같은 IP만, 같은 IP·포트만 받는 방식이 어떻게 다른지 보여 줍니다.",
     "필터링이 꼼꼼할수록 받는 상대의 범위가 좁아집니다."),
    ("u12-l05-p05-cone-names", p5, "Full Cone, Symmetric은 어떻게 읽을까?",
     "Full Cone, Restricted Cone, Port Restricted Cone은 매핑이 상대와 무관하고 필터링만 다르며, Symmetric은 매핑이 상대에 따라 달라진다는 옛 이름 풀이표입니다.",
     "옛 Cone 이름은 매핑과 필터링으로 풀어 읽습니다."),
    ("u12-l05-p06-hole-punching", p6, "양쪽에서 먼저 보내면 길이 열릴까?",
     "박 팀장과 지우 PC가 STUN 서버 203.0.113.60으로 바깥 주소를 알아내고 소개 서버가 서로 알려 준 뒤 동시에 먼저 보내 임시 줄을 만들어 직접 연결하는 UDP 홀 펀칭 과정입니다.",
     "UDP 홀 펀칭은 조건이 맞을 때 직접 연결을 만듭니다."),
    ("u12-l05-p07-relay", p7, "직접 못 만나면 누가 대신 전해 줄까?",
     "직접 연결이 UDP 차단, 상대별 매핑, 통신사 NAT 때문에 막히면 양쪽이 TURN 서버 203.0.113.60으로 연결해 데이터를 중계받고, 확실한 대신 서버 비용과 지연이 든다는 그림입니다.",
     "중계는 직접 연결이 안 될 때의 확실한 대안이며 비용과 지연이 따릅니다."),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, fn, *_ in ITEMS:
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        wire_pages(LESSON / "lesson.md", [(f, t, al, c) for f, _, t, al, c in ITEMS])
    print("ok", len(ITEMS), "svgs")
