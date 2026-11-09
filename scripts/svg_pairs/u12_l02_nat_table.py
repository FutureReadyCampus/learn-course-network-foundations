#!/usr/bin/env python3
"""Unit 12 Lesson 2 (NAT 변환표로 통신 따라가기): light example SVG per Page (11). Run from repo root:
python3 scripts/svg_pairs/u12_l02_nat_table.py   (--svg-only skips lesson.md edit / stale diagram removal).

Daily-life thread: 아파트 경비실(공유기)이 택배 대장(변환표)에 '누가 어디로 보냈는지' 적어 두고 답장을 제 호수로 돌려준다."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur
from u7_l01 import mv
from u11_structures import srv
from u12_l01_router import net, rt, cloud

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-router-and-nat/lessons/restructured/02-*"))
OUT = LESSON / "assets" / "animations"
Y = 300
PC, PC2 = "192.168.0.10:3000", "192.168.0.11:4000"
WEB, WEB2 = "203.0.113.80:443", "203.0.113.81:443"
EXT, EXT2, EXT3 = "198.51.100.25:53001", "198.51.100.25:53002", "198.51.100.25:53003"


def env(x, y, src, dst, c=BLUE, hi=None):
    """Packet card (top-left x,y; 270x74): 출발지/목적지 rows; hi = 'src'|'dst' highlights a row."""
    rows = [("출발지", src, "src"), ("목적지", dst, "dst")]
    s = box(x, y, 270, 74, c, PANEL, 10, sw=3)
    for i, (k, v, key) in enumerate(rows):
        yy = y + 27 + i * 30
        col = ORANGE if hi == key else TXT
        s += text(x + 14, yy, k, 14, MUTED, 700, "start") + text(x + 80, yy, v, 15, col, 700, "start")
    return s


def table(x, y, heads, rows, widths, c=GREEN, fs=15):
    """Header + rows; returns (header_svg, [row_svg...]) so rows can be revealed per stage."""
    hx = [x + sum(widths[:i]) for i in range(len(widths))]
    head = "".join(cell(hx[i], y, widths[i] - 6, 36, h, MUTED, 15, BG) for i, h in enumerate(heads))
    out = []
    for r, row in enumerate(rows):
        yy = y + 44 + r * 50
        out.append("".join(cell(hx[i], yy, widths[i] - 6, 42, v, c, fs) for i, v in enumerate(row)))
    return head, out


def ledger(x, y):
    """작은 대장(노트) 아이콘."""
    return (f'<rect x="{x - 18}" y="{y - 22}" width="36" height="44" rx="4" fill="{PANEL}" stroke="{ORANGE}" stroke-width="3"/>'
            + "".join(f'<line x1="{x - 10}" y1="{y - 10 + i * 10}" x2="{x + 10}" y2="{y - 10 + i * 10}" stroke="{ORANGE}" stroke-width="2"/>' for i in range(3)))


def scene(pc_label="192.168.0.10", srv_x=850):
    return (laptop(110, Y, pc_label) + rt(480, Y) + srv(srv_x, Y)
            + line(170, Y, 450, Y, LINE, 4, "10 8") + line(510, Y, srv_x - 50, Y, LINE, 4, "10 8"))


# 1 ---
def p1():
    a = Anim(4, dur(False))
    body = [scene(),
            a.vis(pill(480, 160, "IP 주소 = 건물, 포트 = 호수", BLUE, 18, False, 320), 1, 1),
            a.vis(pill(200, 220, PC, BLUE, 16, True, 210) + pill(780, 220, WEB, GREEN, 16, True, 210), 2, 4),
            a.vis(ledger(480, 220) + pill(480, 160, "공유기의 변환표(대장)", ORANGE, 18, True, 250), 3, 4),
            a.vis(pill(480, 420, "나갈 때 적고, 돌아올 때 찾아요", GREEN, 19, False, 340), 4, 4)]
    caps = ["주소 뒤 콜론 숫자는 포트 번호예요", "집 PC가 웹 서버에 접속하는 예를 따라가요", "공유기는 변환표에 통신을 적어 둬요", "나갈 때 기록하고 돌아올 때 찾아요"]
    return frame(a, "주소와 포트를 함께 바꾸기", "경비실이 택배 대장을 적는 것과 비슷해요", caps, "".join(body))


# 2 ---
def p2():
    a = Anim(4, dur(False))
    body = [a.vis(net(40, 160, 300, 230, "내부 사설망", GREEN) + laptop(190, 290, "192.168.0.10"), 1, 4), rt(480, 280),
            a.vis(pill(480, 205, "안쪽 192.168.0.1", GREEN, 15, True, 170), 2, 4),
            a.vis(pill(480, 370, "바깥 198.51.100.25", BLUE, 15, True, 190) + net(640, 160, 280, 230, "외부 공인망", BLUE) + srv(780, 290), 3, 4),
            a.vis(pill(480, 430, "Local = 노트북의 주소·포트 (공유기 주소 X)", ORANGE, 17, False, 440), 4, 4)]
    caps = ["노트북은 집 안 사설 주소를 써요", "공유기의 안쪽 주소는 기본 게이트웨이예요", "바깥 주소는 ISP가 배정해요", "Local은 통신을 시작한 기기의 값이에요"]
    return frame(a, "내부 사설망과 외부 공인망", "경계는 공유기 하나예요", caps, "".join(body))


# 3 ---
def p3():
    a = Anim(4, dur(False))
    body = [scene(),
            a.vis(pill(780, 220, "HTTPS 서버 :443", GREEN, 16, True, 190), 1, 4),
            a.vis(pill(200, 220, "OS가 고른 포트 :3000", BLUE, 16, True, 220), 2, 4),
            a.vis(env(80, 380, PC, WEB), 3, 4),
            mv(a, packet(0, 0), [(190, Y), (430, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(700, 417, "3000 ≠ 443 · 역할이 달라요", ORANGE, 17, False, 280), 4, 4)]
    caps = ["웹 서버는 443번 포트에서 기다려요", "PC의 운영체제가 출발 포트 3000을 골라요", "첫 패킷에 출발지와 목적지가 적혀요", "출발 포트와 서비스 포트는 서로 달라도 돼요"]
    return frame(a, "내부 PC가 연결을 시작", "편지 봉투에 보내는 곳과 받는 곳을 적어요", caps, "".join(body))


# 4 ---
def p4():
    a = Anim(4, dur(False))
    body = [scene(),
            a.vis(env(60, 150, PC, WEB), 1, 4),
            mv(a, packet(0, 0), [(190, Y), (430, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(ledger(480, 220), 2, 4),
            a.vis(env(630, 150, EXT, WEB, ORANGE, "src"), 2, 4),
            mv(a, packet(0, 0, ORANGE), [(530, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 400, "바뀐 건 출발지 주소·포트", ORANGE, 18, True, 280), 3, 3),
            a.vis(pill(480, 400, "목적지 203.0.113.80:443은 그대로", GREEN, 18, True, 330), 4, 4)]
    caps = ["안쪽에서 출발한 패킷이 공유기에 와요", "공유기가 출발지를 바깥 주소·포트로 바꿔요", "바뀌는 쪽은 출발지예요", "목적지인 서버 주소와 포트는 그대로예요"]
    return frame(a, "Outbound · 출발지 변환", "봉투의 보내는 곳을 경비실 주소로 바꿔 써요", caps, "".join(body))


# 5 ---
def p5():
    a = Anim(4, dur(False))
    body = [house(140, 290, "집 안"), rt(480, Y), srv(820, Y), line(510, Y, 770, Y, LINE, 4, "10 8"),
            a.vis(pill(780, 190, f"{EXT}에서 왔네", GREEN, 16, False, 260), 1, 4),
            a.vis(pill(140, 400, "192.168.0.10은 몰라요", MUTED, 16, False, 220), 2, 4),
            a.vis(pill(780, 410, "사용자 구별은 로그인·쿠키로", BLUE, 16, False, 270), 3, 4),
            a.vis(pill(480, 450, "바뀐 건 출발 포트 · 서버 포트 443은 그대로", ORANGE, 16, True, 400), 4, 4)]
    caps = ["서버는 바깥에서 보이는 주소·포트를 봐요", "집 안 노트북의 사설 주소는 알지 못해요", "사용자는 로그인이나 쿠키로 구별해요", "공유기가 바꾼 것은 서버 포트가 아니에요"]
    return frame(a, "웹 서버가 보는 접속 주체", "편지를 받은 쪽은 경비실 주소만 봐요", caps, "".join(body))


# 6 ---
def p6():
    a = Anim(4, dur(False))
    head, rows = table(60, 160, ["프로토콜", "내부(Local)", "상대(Remote)", "바깥(External)"], [["TCP", PC, WEB, EXT]], [120, 260, 240, 220])
    body = [head, a.vis(rows[0], 1, 4),
            a.vis(hl(180, 204, 254, 42, BLUE) + pill(307, 290, "이 내부 통신이", BLUE, 16, True, 160), 2, 2),
            a.vis(hl(680, 204, 214, 42, ORANGE) + pill(787, 290, "바깥에선 이렇게 보여요", ORANGE, 16, True, 230), 3, 3),
            a.vis(pill(480, 330, "자동으로 생긴 행은 시간이 지나면 사라질 수 있어요", MUTED, 17, False, 480)
                  + pill(480, 390, "포트 포워딩 같은 고정 규칙과는 달라요", GREEN, 17, False, 380), 4, 4)]
    caps = ["변환표 한 줄에 통신 한 개가 적혀요", "왼쪽은 집 안에서 시작한 통신이에요", "오른쪽은 바깥에서 보이는 주소·포트예요", "자동 기록은 유휴 시간이 지나면 지워질 수 있어요"]
    return frame(a, "NAT Table에 남기는 기록", "택배 대장 한 줄을 읽어 봐요", caps, "".join(body))


# 7 ---
def p7():
    a = Anim(4, dur(False))
    body = [scene(),
            a.vis(env(630, 150, WEB, EXT, GREEN, "dst"), 1, 4),
            mv(a, packet(0, 0, GREEN), [(780, Y), (530, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(ledger(480, 220) + pill(480, 400, "목적지 53001 → 변환표에서 찾기", ORANGE, 17, True, 330), 2, 2),
            a.vis(pill(480, 400, "필터링 규칙에도 맞아야 들어가요", VIOLET, 17, True, 330), 3, 3),
            a.vis(cross(480, 225) + pill(480, 400, "맞는 행이 없으면 전달 못 해요", RED, 17, True, 320), 4, 4)]
    caps = ["서버의 응답은 바깥 주소·포트로 돌아와요", "공유기는 변환표에서 짝을 찾아요", "상대를 확인하는 필터링 규칙도 적용돼요", "기록이 없으면 어느 PC인지 알 수 없어요"]
    return frame(a, "서버에서 응답이 돌아오기", "답장은 경비실 주소로 먼저 도착해요", caps, "".join(body))


# 8 ---
def p8():
    a = Anim(4, dur(False))
    body = [scene(),
            a.vis(env(630, 150, WEB, EXT, GREEN, "dst"), 1, 4),
            a.vis(ledger(480, 220), 1, 4),
            a.vis(env(60, 150, WEB, PC, GREEN, "dst"), 2, 4),
            mv(a, packet(0, 0, GREEN), [(440, Y), (190, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 400, "갈 때는 출발지, 올 때는 목적지를 바꿔요", ORANGE, 17, True, 400), 3, 3),
            a.vis(check(200, 250) + pill(480, 400, "같은 기록 한 줄로 왕복이 이어져요", GREEN, 17, True, 360), 4, 4)]
    caps = ["응답의 목적지는 바깥 주소·포트예요", "공유기가 목적지를 원래 PC로 되돌려요", "요청 땐 출발지, 응답 땐 목적지가 바뀌어요", "같은 기록으로 응답이 제자리를 찾아요"]
    return frame(a, "Inbound · 원래 PC로 되돌리기", "경비실이 대장을 보고 답장을 호수로 전해요", caps, "".join(body))


# 9 ---
def p9():
    a = Anim(4, dur(False))
    head, rows = table(110, 250, ["내부(Local)", "상대(Remote)", "바깥(External)"], [[PC, WEB, EXT], [PC2, WEB, EXT2]], [260, 240, 240])
    body = [laptop(180, 160, "PC ①") + laptop(420, 160, "PC ②") + srv(760, 160), head,
            a.vis(rows[0], 1, 4), a.vis(rows[1], 2, 4),
            a.vis(hl(610, 294, 234, 42, ORANGE) + hl(610, 344, 234, 42, ORANGE), 3, 3),
            a.vis(pill(480, 420, "바깥 IP 하나 + 포트로 나눠 쓰기 = NAPT", GREEN, 18, True, 420), 4, 4)]
    caps = ["PC ①의 통신은 53001로 기록돼요", "PC ②의 통신은 53002로 따로 기록돼요", "바깥 IP는 같고 포트가 달라요", "그래서 응답을 올바른 PC에 돌려줘요"]
    return frame(a, "다른 PC의 연결도 구분하기", "같은 경비실 주소, 다른 대장 번호예요", caps, "".join(body))


# 10 ---
def p10():
    a = Anim(4, dur(False))
    head, rows = table(110, 250, ["내부(Local)", "상대(Remote)", "바깥(External)"], [[PC, WEB, EXT], [PC, WEB2, EXT3]], [260, 240, 240])
    body = [laptop(180, 160, "PC ①") + srv(600, 160) + srv(800, 160), head,
            a.vis(rows[0], 1, 4), a.vis(rows[1], 2, 4),
            a.vis(hl(370, 344, 234, 42, BLUE) + hl(610, 344, 234, 42, ORANGE), 3, 3),
            a.vis(pill(480, 420, "옛 Symmetric 예시일 뿐, 모든 NAT가 이렇진 않아요", MUTED, 17, False, 460), 4, 4)]
    caps = ["PC ①이 첫 번째 서버와 통신해요", "같은 PC가 다른 서버에도 접속해요", "이 예시에서는 상대가 바뀌면 바깥 포트도 달라요", "실제 장비마다 동작은 달라요"]
    return frame(a, "서버가 구별하는 연결", "상대가 바뀌면 대장 줄이 따로 생길 수 있어요", caps, "".join(body))


# 11 ---
def p11():
    a = Anim(4, dur(False))
    items = [("Local", PC, "누가 시작했나?", BLUE), ("Remote", WEB, "누구와 통신하나?", GREEN), ("External", EXT, "바깥에선 어떻게 보이나?", ORANGE)]
    body = []
    for i, (n, v, q, c) in enumerate(items):
        x = 60 + i * 290
        body.append(a.vis(cell(x, 170, 260, 50, n, c, 22) + cell(x, 230, 260, 46, v, c, 15) + text(x + 130, 305, q, 16, MUTED, 700), i + 1, 4))
    body.append(a.vis(f'<path d="M190 330 C190 400 770 400 770 330" fill="none" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="8 6"/>'
                      + pill(480, 425, "매핑은 Local ↔ External을 잇는 일", ORANGE, 18, True, 360), 4, 4))
    caps = ["Local은 집 안에서 시작한 통신이에요", "Remote는 통신 상대 서버예요", "External은 바깥에서 보이는 통신이에요", "NAT 매핑은 Local과 External을 이어요"]
    return frame(a, "Local · Remote · External", "변환표 세 칸을 정리해요", caps, "".join(body))


ITEMS = [
    ("u12-nat-table-intro", "advanced-source-11-page-01", "주소와 포트를 함께 바꾸기", "집 PC 192.168.0.10:3000이 웹 서버 203.0.113.80:443에 접속하고, 공유기가 변환표에 기록해 두는 모습입니다.", "공유기는 나갈 때 기록하고 돌아올 때 그 기록을 찾습니다.", p1),
    ("u12-nat-table-inside-outside", "advanced-source-11-page-02", "내부 사설망과 외부 공인망", "내부 사설망의 노트북, 안쪽 192.168.0.1과 바깥 198.51.100.25를 가진 공유기, 외부 공인망의 서버를 보여 주고 Local이 노트북의 값임을 강조합니다.", "Local은 공유기 주소가 아니라 통신을 시작한 기기의 값입니다.", p2),
    ("u12-nat-table-start", "advanced-source-11-page-03", "내부 PC가 연결을 시작", "운영체제가 고른 출발 포트 3000과 HTTPS 서버 포트 443이 적힌 첫 패킷이 공유기로 가는 모습입니다.", "패킷에는 출발지와 목적지 주소·포트가 함께 적힙니다.", p3),
    ("u12-nat-table-outbound", "advanced-source-11-page-04", "Outbound · 출발지 변환", "공유기를 지나며 출발지 192.168.0.10:3000이 198.51.100.25:53001로 바뀌고 목적지는 그대로인 두 패킷 카드를 비교합니다.", "Outbound에서는 출발지 주소·포트만 바뀝니다.", p4),
    ("u12-nat-table-server-view", "advanced-source-11-page-05", "웹 서버가 보는 접속 주체", "웹 서버는 198.51.100.25:53001에서 온 요청으로 보고, 집 안 사설 주소는 모르며 사용자 구별은 로그인·쿠키로 한다는 그림입니다.", "서버는 NAT가 바깥에 보여 준 주소·포트를 봅니다.", p5),
    ("u12-nat-table-row", "advanced-source-11-page-06", "NAT Table에 남기는 기록", "프로토콜, 내부, 상대, 바깥 네 칸으로 된 변환표 한 줄을 읽고, 자동 행은 시간이 지나면 사라질 수 있음을 보여 줍니다.", "변환표 한 줄은 내부 통신과 바깥 통신을 잇습니다.", p6),
    ("u12-nat-table-reply", "advanced-source-11-page-07", "서버에서 응답이 돌아오기", "응답이 바깥 주소·포트로 공유기에 도착해 변환표와 필터링 규칙을 거치고, 맞는 행이 없으면 전달되지 않는 모습입니다.", "응답은 변환표에서 짝을 찾아야 안으로 들어갑니다.", p7),
    ("u12-nat-table-inbound", "advanced-source-11-page-08", "Inbound · 원래 PC로 되돌리기", "공유기가 응답의 목적지 198.51.100.25:53001을 192.168.0.10:3000으로 되돌려 노트북에 전달하는 모습입니다.", "Inbound에서는 목적지를 기록된 내부 주소·포트로 복원합니다.", p8),
    ("u12-nat-table-two-pcs", "advanced-source-11-page-09", "다른 PC의 연결도 구분하기", "두 PC의 통신이 같은 바깥 IP를 쓰지만 53001과 53002로 다른 변환표 행에 기록되는 모습입니다.", "포트와 변환표 기록으로 여러 기기의 통신을 나눕니다.", p9),
    ("u12-nat-table-two-servers", "advanced-source-11-page-10", "서버가 구별하는 연결", "같은 PC가 서로 다른 두 서버에 접속할 때 이 예시에서는 바깥 포트가 53001과 53003으로 달라지는 모습입니다.", "외부 상대에 따라 매핑이 달라질 수 있지만 모든 NAT가 그렇지는 않습니다.", p10),
    ("u12-nat-table-terms", "advanced-source-11-page-11", "Local · Remote · External", "Local, Remote, External 세 칸과 이 예의 값, 확인할 질문을 차례로 보여 주고 매핑이 Local과 External을 잇는다고 정리합니다.", "Local, Remote, External을 구분해 변환표를 읽습니다.", p11),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-11\.svg\n(?:    .*\n)+", "", s, count=1)
    for f, pid, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in s:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        (LESSON / "assets" / "diagrams" / "source-11.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
