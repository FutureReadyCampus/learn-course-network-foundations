#!/usr/bin/env python3
"""Unit 12 Lesson 2 (답장이 제자리로 돌아오는 NAT 변환표): one 4-step example SVG per Page (7).
Run from repo root: python3 scripts/svg_pairs/u12_new_l02_nat_table.py  (--svg-only skips the lesson.md edit).
Example: 지우 PC 192.168.10.41:3000 -> 외부 AI API 203.0.113.80:443, 바깥에서는 198.51.100.25:53001."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(2)
OUT = LESSON / "assets" / "animations"
PC1, PC3, API = "192.168.10.41", "192.168.10.43", "203.0.113.80:443"
L1, E1, L3, E3 = f"{PC1}:3000", f"{WAN}:53001", f"{PC3}:4000", f"{WAN}:53002"


def line3(y):
    return line(170, y, 450, y, LINE, 4, "8 6") + line(510, y, 800, y, LINE, 4, "8 6")


def p1():
    p = Pg("AI API의 답장은 어디로?", "사설 주소는 인터넷에 나갈 수 없는데 답은 어떻게 올까",
           ["지우 PC가 외부 AI API를 불러요", "요청은 기본 게이트웨이인 공유기를 지나가요",
            "답은 198.51.100.25로 오는데 사설 주소는 못 써요", "공유기 안의 변환표가 짝을 기억해요"])
    p.base(laptop(110, 290, "지우 PC"), rt(480, 290), dsrv(850, 290, "외부 AI API"), line3(290))
    p.at(pill(110, 385, PC1, GREEN, 15, False, 170) + pill(850, 385, API, BLUE, 15, False, 170), 1)
    p.fly(packet(0, 0, BLUE), [(190, 290), (790, 290)], 2, 0.05, 0.95)
    p.at(pill(480, 200, "게이트웨이 192.168.10.1", ORANGE, 15, True, 220), 2, 2, mark=(370, 182, 220, 36))
    p.at(ask(330, 235) + pill(640, 235, "답은 " + WAN + "로 와요", BLUE, 15, False, 250), 3, 3, mark=(308, 213, 44, 44))
    p.at(ledger(480, 215) + pill(480, 440, "NAT 변환표가 짝을 기억해요", ORANGE, 17, True, 300), 4, 4, mark=(455, 188, 50, 56))
    return p.render()


def p2():
    p = Pg("공유기를 나설 때 바뀌는 것", "출발지만 바뀌고 목적지는 그대로예요",
           ["안쪽에서 본 패킷의 출발지는 사설 주소예요", "공유기를 지나며 출발지를 바꿔 써요",
            "바깥에서는 198.51.100.25:53001로 보여요", "목적지 서버 주소와 포트는 그대로예요"])
    p.base(laptop(110, 340, "지우 PC"), rt(480, 340), dsrv(850, 340, "외부 AI API"), line3(340))
    p.at(lbl(190, 142, "공유기 안쪽") + card(40, 155, L1, API, GREEN), 1)
    p.fly(packet(0, 0, BLUE), [(190, 340), (790, 340)], 2, 0.05, 0.95)
    p.at(pill(480, 255, "출발지만 바꿔요", ORANGE, 16, True, 170), 2, 2, mark=(395, 237, 170, 36))
    p.at(lbl(770, 142, "공유기 바깥쪽") + card(620, 155, E1, API, ORANGE), 3, mark=cl(620, 155, 0))
    p.at(pill(480, 440, "목적지 " + API + "는 그대로", GREEN, 17, True, 380), 4, 4, mark=cl(620, 155, 1))
    return p.render()


def p3():
    p = Pg("AI 서비스는 누가 접속했다고 볼까?", "서비스가 보는 출발지는 회사 주소 하나예요",
           ["직원 PC 여러 대가 같은 AI API를 써요", "요청이 공유기를 지나 서비스로 가요",
            "접속 기록의 출발지는 모두 198.51.100.25예요", "누가 썼는지는 계정이나 키로 구별해요"])
    ys = (170, 285, 400)
    p.base(net(40, 125, 200, 345, "사무실", GREEN), rt(480, 285), line(240, 285, 450, 285, LINE, 4, "8 6"),
           *[pc(140, y, f"192.168.10.{41 + i}") for i, y in enumerate(ys)],
           box(660, 140, 260, 300, BLUE, PANEL, 12, sw=3) + lbl(790, 172, "AI API 접속 기록", BLUE, 18),
           line(510, 285, 660, 285, LINE, 4, "8 6"))
    for y in ys:
        p.fly(packet(0, 0, BLUE), [(200, y), (445, 283)], 2, 0.05, 0.6)
    for y in ys:
        p.fly(packet(0, 0, ORANGE), [(520, 285), (650, 285)], 2, 0.5, 0.95)
    p.at("".join(cell(680, 190 + i * 56, 220, 44, "출발지 " + WAN, GREEN, 15) for i in range(3)), 3, mark=(680, 190, 220, 156))
    p.at(pill(480, 448, "사람 구별은 계정·API 키로", ORANGE, 17, True, 300), 4, 4)
    return p.render()


def p4():
    p = Pg("변환표 한 줄에는 무엇이 적힐까?", "Local · Remote · External 세 칸이에요",
           ["공유기의 NAT 세션 목록에 한 줄이 있어요", "Local은 통신을 시작한 안쪽 기기예요",
            "External은 바깥에서 보이는 주소·포트예요", "Remote는 상대이고 자동 행은 사라져요"])
    head, rows = table(55, 200, ["프로토콜", "Local", "Remote", "External"], [["TCP", L1, API, E1]], [110, 250, 230, 260], GREEN, 15)
    p.base(head)
    p.at(rows[0] + pill(480, 150, "공유기 NAT 세션 목록", BLUE, 17, True, 220), 1, mark=(55, 244, 844, 42))
    p.at(pill(287, 335, "통신을 시작한 기기", GREEN, 16, False, 190), 2, 2, mark=(165, 244, 244, 42))
    p.at(line(287, 295, 772, 295, ORANGE, 4) + line(287, 288, 287, 302, ORANGE, 4) + line(772, 288, 772, 302, ORANGE, 4)
         + pill(772, 335, "바깥에서 보이는 값", BLUE, 16, False, 190), 3, 3, mark=(645, 244, 254, 42))
    p.at(pill(527, 335, "Remote = 통신 상대", MUTED, 16, False, 190) + pill(480, 410, "자동 행은 시간이 지나면 사라져요", ORANGE, 17, True, 340), 4, 4,
         mark=(415, 244, 224, 42))
    return p.render()


def p5():
    p = Pg("돌아온 답장은 어느 PC로 갈까?", "나갈 때 적은 줄을 거꾸로 읽어요",
           ["AI API의 답은 바깥 주소·포트로 도착해요", "공유기가 53001번 줄을 변환표에서 찾아요",
            "목적지를 지우 PC의 Local 값으로 되돌려요", "기록이 없으면 보낼 곳도 몰라요"])
    p.base(pc(110, 340, "지우 PC"), rt(480, 340), dsrv(850, 340, "외부 AI API"), line3(340))
    p.at(lbl(770, 142, "공유기 바깥쪽") + card(620, 155, API, E1, BLUE), 1)
    p.fly(packet(0, 0, GREEN), [(790, 340), (520, 340)], 1, 0.1, 0.9)
    p.at(cell(355, 235, 250, 40, "53001 → " + L1, ORANGE, 14), 2, 3, mark=(355, 235, 250, 40))
    p.at(lbl(190, 142, "공유기 안쪽") + card(40, 155, API, L1, GREEN), 3, mark=cl(40, 155, 1))
    p.fly(packet(0, 0, GREEN), [(440, 340), (190, 340)], 3, 0.1, 0.9)
    p.at(check(110, 265), 3, 4)
    p.at(pill(480, 440, "기록이 없으면 돌려보낼 곳도 없어요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p6():
    p = Pg("동시에 물어도 답이 안 섞이는 이유", "바깥 주소는 같고 포트가 달라요",
           ["지우 PC와 디자인팀 PC가 동시에 요청해요", "첫 줄: 지우 PC가 53001번이에요",
            "둘째 줄: 디자인팀 PC가 53002번이에요", "응답은 포트로 찾아 각자 PC로 가요"])
    ty = 350
    p.base(pc(110, 160, PC1), pc(110, 280, PC3), rt(480, 225), dsrv(850, 225, "외부 AI API"),
           line(170, 160, 450, 222, LINE, 4, "8 6"), line(170, 280, 450, 228, LINE, 4, "8 6"), line(510, 225, 800, 225, LINE, 4, "8 6"),
           cell(215, ty, 240, 30, "Local", MUTED, 15, BG) + cell(465, ty, 240, 30, "External", MUTED, 15, BG))
    p.fly(packet(0, 0, BLUE), [(190, 160), (445, 220)], 1, 0.05, 0.9)
    p.fly(packet(0, 0, GREEN), [(190, 280), (445, 230)], 1, 0.05, 0.9)
    p.at(cell(215, ty + 36, 240, 34, L1, BLUE, 15) + cell(465, ty + 36, 240, 34, E1, BLUE, 15), 2, mark=(215, ty + 36, 490, 34))
    p.at(cell(215, ty + 76, 240, 34, L3, GREEN, 15) + cell(465, ty + 76, 240, 34, E3, GREEN, 15), 3, mark=(215, ty + 76, 490, 34))
    p.fly(packet(0, 0, BLUE), [(445, 220), (190, 160)], 4, 0.05, 0.9)
    p.fly(packet(0, 0, GREEN), [(445, 230), (190, 280)], 4, 0.05, 0.9)
    p.at(pill(815, 410, "포트로 구분 = NAPT", ORANGE, 16, True, 200), 4, 4)
    return p.render()


def p7():
    p = Pg("박 팀장의 요청은 왜 사라질까?", "바깥에서 먼저 온 요청에는 맞는 줄이 없어요",
           ["박 팀장이 198.51.100.25:8080으로 접속해요", "요청이 공유기 바깥쪽에 도착해요",
            "맞는 줄이 없어 어느 기기로 갈지 몰라요", "줄을 미리 적어 두면 길이 열려요"])
    p.base(net(40, 125, 300, 250, "사무실 LAN", GREEN), dsrv(115, 235, "GPU PC"), pc(255, 235, "지우 PC"), rt(480, 235),
           laptop(850, 235, "박 팀장"), line(340, 235, 450, 235, LINE, 4, "8 6"), line(510, 235, 800, 235, LINE, 4, "8 6"))
    p.at(pill(820, 330, f"{WAN}:{AI_PORT}", BLUE, 15, False, 230), 1, mark=(705, 312, 230, 36))
    p.fly(packet(0, 0, BLUE), [(800, 235), (540, 235)], 2, 0.1, 0.9)
    p.at(ledger(480, 170) + cross(545, 170) + pill(480, 420, "맞는 줄이 없어 버려져요", RED, 17, False, 280), 3, 3, mark=(523, 148, 44, 44))
    p.at(cell(260, 400, 440, 42, f"바깥 {AI_PORT} → {AI}:{AI_PORT}", GREEN, 17) + check(115, 170), 4, 4, mark=(260, 400, 440, 42))
    return p.render()


ITEMS = [
    ("u12-l02-p01-reply-finds-pc", p1, "AI API의 답장은 어디로?",
     "지우 PC 192.168.10.41이 외부 AI API 203.0.113.80:443을 부르면 요청은 공유기를 지나고, 답은 198.51.100.25로 오는데 공유기의 변환표가 짝을 기억해 둔다는 그림입니다.",
     "응답이 원래 PC를 찾는 열쇠는 공유기의 NAT 변환표입니다."),
    ("u12-l02-p02-outbound", p2, "공유기를 나설 때 바뀌는 것",
     "공유기 안쪽에서는 출발지가 192.168.10.41:3000이고 바깥쪽에서는 198.51.100.25:53001로 바뀌며, 목적지 203.0.113.80:443은 그대로임을 두 개의 패킷 카드로 보여 줍니다.",
     "Outbound에서는 출발지 주소와 포트만 바뀝니다."),
    ("u12-l02-p03-who-connected", p3, "AI 서비스는 누가 접속했다고 볼까?",
     "직원 PC 세 대의 요청이 공유기를 지나 AI API 접속 기록에는 모두 출발지 198.51.100.25로 남고, 사람 구별은 계정이나 API 키로 한다는 설명입니다.",
     "서비스가 보는 IP는 직원이 아니라 회사 회선의 흔적입니다."),
    ("u12-l02-p04-table-row", p4, "변환표 한 줄에는 무엇이 적힐까?",
     "NAT 세션 목록 한 줄에서 Local 192.168.10.41:3000, Remote 203.0.113.80:443, External 198.51.100.25:53001이 각각 무엇을 뜻하는지 차례로 짚습니다.",
     "매핑은 Local과 External을 잇고, 자동 행은 시간이 지나면 사라집니다."),
    ("u12-l02-p05-inbound", p5, "돌아온 답장은 어느 PC로 갈까?",
     "AI API의 응답 목적지 198.51.100.25:53001을 변환표에서 찾아 192.168.10.41:3000으로 되돌려 지우 PC에 전달하는 Inbound 과정입니다.",
     "Inbound에서는 목적지가 바뀌고, 나갈 때 적은 기록이 있어야 가능합니다."),
    ("u12-l02-p06-two-pcs", p6, "동시에 물어도 답이 안 섞이는 이유",
     "지우 PC와 디자인팀 PC의 요청이 같은 바깥 주소 198.51.100.25에 포트 53001과 53002로 따로 기록되어 응답이 각자 PC로 돌아가는 NAPT 방식입니다.",
     "주소와 포트를 함께 바꿔 바깥 주소 하나를 여러 PC가 나눠 씁니다."),
    ("u12-l02-p07-no-row-dropped", p7, "박 팀장의 요청은 왜 사라질까?",
     "박 팀장이 198.51.100.25:8080으로 보낸 요청이 도착해도 변환표에 맞는 줄이 없어 GPU PC로 갈지 지우 PC로 갈지 몰라 버려지고, 줄을 미리 적어 두면 길이 열립니다.",
     "바깥에서 먼저 온 요청은 미리 적은 줄이 있어야 안쪽으로 전달됩니다."),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, fn, *_ in ITEMS:
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        wire_pages(LESSON / "lesson.md", [(f, t, al, c) for f, _, t, al, c in ITEMS])
    print("ok", len(ITEMS), "svgs")
