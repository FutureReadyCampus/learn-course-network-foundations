#!/usr/bin/env python3
"""Unit 14 Lesson 5 (IP로 판단하는 한계) revision. Run from repo root: python3 scripts/svg_pairs/u14_l05_rev.py
(--svg-only skips the lesson.md edit.) Old generator u14_l05_ip_limits.py is left untouched.

Fixes: 16px+ labels, packets drawn BEFORE icons (pass behind them), result steps use check/cross marks,
server labelled with its role (not just '서버'), no label before the Page body explains it.
Adds a 2nd SVG to Page 7 (tracing chain) and Page 8 (what to add to IP: signals + Unit 15 hand-off).
Running example: 박 팀장(출장지 192.0.2.150) -> 외부 AI 203.0.113.80:443, 회사 출구 198.51.100.25."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u14_l04_remote_vpn import mk, pmk, new, lap  # noqa: F401
from u6_l03 import cell, person, hl
from u7_l01 import mv
from u12_l01_router import net, cloud, rt

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("10-vpn-and-security/lessons/restructured/05-*"))
OUT = LESSON / "assets" / "animations"
Y = 300


def ai(x, y, label, c=GREEN):
    return (f'<rect x="{x - 34}" y="{y - 40}" width="68" height="80" rx="8" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
            + "".join(f'<rect x="{x - 24}" y="{y - 30 + i * 24}" width="48" height="16" rx="3" fill="{c}" fill-opacity="0.45"/>' for i in range(3))
            + text(x, y + 62, label, 18, TXT, 700))


def relay(x, y, label, c=ORANGE, fs=19):
    return (f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" fill="{PANEL}" stroke="{c}" stroke-width="3"/>' + text(x, y + 7, label, fs, c, 700))


def verdict(x, y, s, ok, fs=16):
    """check/cross circle centred at x, then a pill to its right. Returns (svg, right_edge)."""
    w = tw(s, fs) + 28
    return (check if ok else cross)(x, y) + pill(x + 26 + w / 2, y, s, GREEN if ok else RED, fs, False, w), x + 26 + w


def rowc(x, y, w, h, s, c, ok=None, fs=17):
    out = cell(x, y, w, h, s, c, fs)
    if ok is not None:
        out += (check if ok else cross)(x + w - 26, y + h / 2)
    return out


def hold(a, svg, t0, t1):
    return a.vis(svg, t0, t1)


# ---------------------------------------------------------------- Page 1
def p1():
    a = new()
    ip, addr = "192.0.2.150", "203.0.113.80:443"
    guess, fin = "'현지 접속'이라고 짐작", "IP는 출구일 뿐 위치의 사실은 아니에요"
    v1, r1 = verdict(640, 400, "출발지 " + ip, True)
    v2, r2 = verdict(640, 442, "실제 위치는 몰라요", False)
    body = [net(40, 130, 200, 270, "출장지", GREEN), line(200, Y, 380, Y, LINE, 4, "8 6"), line(520, Y, 796, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, BLUE), [(200, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            lap(140, Y, "박 팀장"), cloud(450, Y), ai(830, Y, "외부 AI"),
            pill(140, 215, ip, BLUE, 16, False), pmk(a, 140, 215, ip, 1),
            a.vis(pill(830, 205, addr, GREEN, 16, False), 1, 2),
            a.vis(v1 + v2, 2, 3), mk(a, 618, 382, r1 - 618 + 4, 78, 2),
            a.vis(cell(690, 128, 250, 44, "위치 데이터베이스와 대조", VIOLET, 16), 3, 4),
            a.vis(pill(830, 215, guess, ORANGE, 16, False), 3, 4), pmk(a, 830, 215, guess, 3),
            a.vis(pill(480, 448, fin, GREEN, 17, True), 4, 4), pmk(a, 480, 448, fin, 4, 17)]
    caps = ["박 팀장이 출장지에서 외부 AI에 접속해요", "서버에는 출발지 IP만 확실히 보여요", "IP 위치 데이터베이스와 맞춰 짐작해요", "서비스가 말하는 위치는 추정치예요"]
    return frame(a, "AI 서비스는 내가 어디 있다고 볼까?", "서버가 기본으로 보는 것은 출발지 IP예요", caps, "".join(body))


# ---------------------------------------------------------------- Page 2
def p2():
    a = new()
    ip, pl, pr = "192.0.2.150", "출발지 192.0.2.150", "출발지 198.51.100.25"
    fin = "서비스가 보는 것은 마지막 출구 하나예요"
    body = [box(40, 120, 420, 300, MUTED, PANEL, 16, sw=2) + text(250, 152, "VPN 끔", 20, MUTED, 700),
            box(500, 120, 420, 300, GREEN, PANEL, 16, sw=2) + text(710, 152, "전체 터널 켬", 20, GREEN, 700),
            line(150, Y, 366, Y, LINE, 4, "8 6"), line(610, Y, 676, Y, LINE, 4, "8 6"), line(744, Y, 826, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, BLUE), [(165, Y), (355, Y)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(625, Y), (710, Y), (815, Y)], 2, 2, 2, 0.1, 0.9),
            lap(100, Y, "노트북"), ai(400, Y, "외부 AI"), lap(560, Y, "노트북"), booth(710, Y, "SG"), ai(860, Y, "외부 AI"),
            a.vis(pill(130, 230, ip, BLUE, 16, False) + pill(595, 230, ip, BLUE, 16, False), 1, 2),
            pmk(a, 130, 230, ip, 1) + pmk(a, 595, 230, ip, 1), mk(a, 654, 264, 112, 88, 2),
            a.vis(pill(280, 215, pl, BLUE, 16, False), 3, 4), a.vis(pill(745, 215, pr, ORANGE, 16, True), 3, 4), pmk(a, 745, 215, pr, 3),
            a.vis(pill(480, 448, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 448, fin, 4, 18)]
    caps = ["같은 노트북, 같은 출장지에서 두 경우를 비교해요", "전체 터널은 모든 트래픽을 SG로 보내요", "서비스에 보이는 출발지 IP가 서로 달라요", "IP는 마지막 출구를 말해 줄 뿐이에요"]
    return frame(a, "VPN을 켜면 왜 출구가 바뀔까?", "같은 사람, 같은 노트북인데 출발지가 달라져요", caps, "".join(body))


# ---------------------------------------------------------------- Page 3
def p3():
    a = new()
    fin = "공식 지원 지역과 기업 계약을 먼저 확인해요"
    note = "출구만 바뀌고 약관·계약은 그대로"
    body = [line(165, Y, 810, Y, LINE, 4, "8 6"),
            mv(a, parcel(0, 0), [(185, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            lap(110, Y, "직원"), ai(850, Y, "지역 제한 서비스"), a.vis(relay(480, Y, "개인 VPN"), 2, 4),
            pill(110, 205, "고객 도면 업무", BLUE, 16, False), pmk(a, 110, 205, "고객 도면 업무", 1),
            mk(a, 406, 254, 148, 92, 2), a.vis(pill(480, 400, note, BLUE, 16, False), 2, 3),
            a.vis(pill(480, 185, "도면 유출 위험", RED, 16, False) + cross(480, 232), 3, 3), mk(a, 456, 216, 48, 48, 3),
            a.vis(pill(850, 185, "계정 정지 위험", RED, 16, False) + cross(850, 232), 3, 3), mk(a, 826, 216, 48, 48, 3),
            a.vis(pill(480, 448, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 448, fin, 4, 18)]
    caps = ["직원이 업무 자료로 지역 제한 서비스를 열어요", "누가 운영하는지 모르는 개인 VPN을 거쳐요", "약관·계약은 그대로고 위험만 늘어요", "막는 일과 열어 주는 일을 함께 준비해요"]
    return frame(a, "지역 제한을 VPN으로 넘으면", "출구를 바꿔도 약관과 계약은 그대로예요", caps, "".join(body))


# ---------------------------------------------------------------- Page 4
def p4():
    a = new()
    ipp, fin = "198.51.100.25", "출구 뒤 장비 점검과 차단 해제 요청"
    body = [net(30, 125, 370, 300, "한결디자인 본사", BLUE),
            line(150, 235, 262, 285, LINE, 4, "8 6"), line(150, 340, 262, 318, LINE, 4, "8 6"), line(360, Y, 760, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, RED), [(165, 338), (262, 318), (310, Y), (740, Y)], 2, 2, 2, 0.1, 0.9),
            pc(100, 225, "PC"), pc(100, 345, "감염 PC"), rt(300, Y, "NAT 출구"), ai(800, Y, "메일 받는 쪽"),
            pill(300, 230, ipp, BLUE, 16, False), pmk(a, 300, 230, ipp, 1),
            a.vis(box(58, 303, 84, 66, RED, "none", 8, sw=3) + pill(260, 395, "스팸 발송", RED, 16, False), 2, 2), mk(a, 58, 303, 84, 66, 2),
            a.vis(pill(800, 195, "평판 하락", RED, 16, False) + cross(800, 238), 3, 3), pmk(a, 800, 195, "평판 하락", 3),
            a.vis(pill(620, 430, "정상 메일도 스팸함으로", RED, 16, False), 3, 3),
            a.vis(pill(480, 456, fin, GREEN, 17, True), 4, 4), pmk(a, 480, 456, fin, 4, 17)]
    caps = ["모든 PC가 같은 공인 주소 하나로 나가요", "감염된 PC가 스팸을 같은 출구로 내보내요", "출구 주소의 평판이 깎여 정상 메일도 의심받아요", "평판은 힌트예요. 내부 장비를 점검해요"]
    return frame(a, "IP 주소에도 평판이 있다?", "한 대의 문제를 출구 전체가 떠안아요", caps, "".join(body))


# ---------------------------------------------------------------- Page 5
def p5():
    a = new()
    weak, fin = "기본 비밀번호 · 오래된 펌웨어", "비밀번호 변경 → 기능 끄기 → 펌웨어 업데이트"
    body = [net(400, 125, 520, 285, "박 팀장 집", GREEN), line(240, Y, 450, Y, LINE, 4, "8 6"), line(555, Y, 775, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, RED), [(250, Y), (440, Y)], 2, 2, 2, 0.1, 0.9),
            cloud(170, Y), rt(500, Y, "공유기"), pc(820, Y, "집 기기"),
            a.vis(pill(500, 205, "VPN 서버 켜짐", ORANGE, 16, False), 1, 2), pmk(a, 500, 205, "VPN 서버 켜짐", 1),
            a.vis(pill(560, 385, weak, RED, 16, False), 2, 2), pmk(a, 560, 385, weak, 2),
            a.vis(pill(500, 190, "낯선 계정 생성", RED, 16, False) + cross(500, 240), 3, 3), mk(a, 476, 216, 48, 48, 3),
            a.vis(pill(820, 215, "뒤 기기도 위험", ORANGE, 16, False), 3, 3),
            a.vis(pill(480, 448, fin, GREEN, 17, True), 4, 4), pmk(a, 480, 448, fin, 4, 17)]
    caps = ["켠 기억이 없는 VPN 서버 기능이 켜져 있어요", "기본 비밀번호와 옛 펌웨어는 약점이 돼요", "관리 권한을 잃으면 낯선 계정이 생겨요", "쓰지 않는 기능은 끄고 관리를 먼저 챙겨요"]
    return frame(a, "공유기 VPN 기능의 위험", "쓰지 않는 기능이 열려 있으면 공격 면적이에요", caps, "".join(body))


# ---------------------------------------------------------------- Page 6
def p6():
    a = new()
    lg, fin = "로그 출발지 198.51.100.25", "단정하지 말고 내부 로그부터 확인해요"
    v1, _ = verdict(640, 395, "이 IP에서 왔다", True)
    v2, r2 = verdict(640, 440, "이 사람이 했다", False)
    body = [net(300, 125, 280, 285, "한결디자인", BLUE), a.vis(line(150, Y, 395, Y, LINE, 4, "8 6"), 2, 4), line(490, Y, 810, Y, LINE, 4, "8 6"),
            a.vis(mv(a, packet(0, 0, RED), [(180, Y), (380, Y)], 2, 2, 2, 0.1, 0.9), 2, 2),
            mv(a, packet(0, 0, RED), [(510, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(person(110, 270, "공격자"), 2, 4), rt(440, Y, "공유기"), ai(850, Y, "API 업체"),
            cell(700, 170, 240, 44, lg, BLUE, 16), mk(a, 700, 170, 240, 44, 1),
            a.vis(pill(440, 195, "장악된 공유기", ORANGE, 16, False), 2, 3), mk(a, 412, 272, 56, 56, 2),
            a.vis(v1 + v2, 3, 3), mk(a, 618, 376, r2 - 618 + 4, 80, 3),
            a.vis(pill(480, 448, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 448, fin, 4, 18)]
    caps = ["API 업체 기록에 우리 공인 주소가 찍혀 있어요", "장악된 공유기가 공격자의 요청을 중계해요", "주소의 명의자는 사실 피해자일 수 있어요", "누가 했는지는 따로 확인하는 질문이에요"]
    return frame(a, "내 공유기가 남의 중계소라면?", "이 IP에서 왔다는 말은 누가 했다는 말이 아니에요", caps, "".join(body))


# ---------------------------------------------------------------- Page 7 (a: filter)
def p7():
    a = new()
    fin = "터널 안을 보는 대신 허용할 터널을 정해요"
    body = [line(165, Y, 290, Y, LINE, 4, "8 6"), line(375, Y, 520, Y, LINE, 4, "8 6"), line(660, Y, 790, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, VIOLET), [(190, Y), (330, Y), (590, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            pc(110, Y, "직원 PC"), booth(330, Y, "회사 필터"), relay(590, Y, "개인 VPN"), ai(850, Y, "파일 공유 사이트"),
            a.vis(pill(850, 205, "필터가 막아 둔 곳", ORANGE, 16, False), 1, 2), pmk(a, 850, 205, "필터가 막아 둔 곳", 1),
            a.vis(pill(330, 205, "암호화 통신으로만 보여요", ORANGE, 16, False), 2, 2), mk(a, 286, 266, 88, 84, 2),
            a.vis(pill(330, 185, "필터가 못 막아요", RED, 16, False) + cross(330, 232), 3, 3), mk(a, 306, 216, 48, 48, 3),
            a.vis(pill(480, 448, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 448, fin, 4, 18)]
    caps = ["회사 필터가 막은 사이트를 개인 VPN으로 열어요", "필터에는 암호화된 통신만 보여요", "필터가 안을 볼 수 없어 막지 못해요", "통제는 어떤 터널을 쓰게 할지 정하는 일이에요"]
    return frame(a, "개인 VPN 안은 필터가 볼 수 없어요", "막아 둔 사이트가 터널을 타고 열려요", caps, "".join(body))


# ---------------------------------------------------------------- Page 7 (b: trace chain)
def p7b():
    a = new()
    fin = "한 구간의 기록이 없으면 역추적이 거기서 멈춰요"
    xs = (300, 540, 790)
    names = ("해외 업체 기록", "가정집 기록", "우리 회사 기록")
    arrow = (line(770, 235, 340, 235, ORANGE, 5) + f'<polygon points="324,235 344,224 344,246" fill="{ORANGE}"/>')
    body = [line(150, Y, 230, Y, LINE, 4, "8 6"), line(370, Y, 512, Y, LINE, 4, "8 6"), line(568, Y, 756, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, ORANGE), [(175, Y), (775, Y)], 1, 1, 1, 0.1, 0.9),
            person(90, 270, "공격자"), relay(300, Y, "해외 VPN 업체", ORANGE, 17), rt(540, Y, "감염된 가정 공유기"), ai(790, Y, "한결디자인"),
            a.vis("".join(cell(x - 100, 375, 200, 44, n, VIOLET, 16) for x, n in zip(xs, names)), 2, 4),
            mk(a, 200, 375, 690, 44, 2),
            a.vis(arrow + check(xs[2] + 76, 397) + check(xs[1] + 76, 397), 3, 4),
            a.vis(cell(xs[0] - 100, 375, 200, 44, "기록 없음", RED, 16, PANEL) + cross(xs[0] + 76, 397), 3, 4), mk(a, 200, 375, 200, 44, 3),
            a.vis(pill(480, 456, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 456, fin, 4, 18)]
    caps = ["공격은 중계 지점 세 곳을 거쳐 들어와요", "구간마다 기록이 다른 조직에 있어요", "거슬러 올라가다 기록 없는 곳에서 멈춰요", "그래서 각 구간의 기록 보존이 중요해요"]
    return frame(a, "여러 번 거친 접속은 왜 추적이 어려울까?", "기록이 흩어져 있어 한 곳만 끊겨도 멈춰요", caps, "".join(body))


# ---------------------------------------------------------------- Page 8 (a: IP-only rule)
def p8():
    a = new()
    fin = "IP는 관찰 지점일 뿐 신원이 아니에요"
    body = [line(160, Y, 360, Y, LINE, 4, "8 6"), line(440, Y, 800, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, ORANGE), [(190, Y), (380, Y), (420, Y), (780, Y)], 2, 2, 2, 0.1, 0.9),
            person(110, 270, "공격자"), booth(400, Y, "SG"), ai(840, Y, "사내 AI"),
            cell(700, 140, 240, 44, "허용  10.10.99.0/24", BLUE, 16), mk(a, 700, 140, 240, 44, 1),
            pill(125, 215, "박 팀장 비밀번호 유출", RED, 16, False),
            a.vis(pill(400, 215, "VPN 주소 10.10.99.31", ORANGE, 16, True), 2, 3), pmk(a, 400, 215, "VPN 주소 10.10.99.31", 2),
            a.vis(pill(850, 225, "주소만 보고 통과", RED, 17, False) + cross(745, 225), 3, 3), mk(a, 721, 201, 48, 48, 3),
            a.vis(pill(480, 448, fin, GREEN, 18, True), 4, 4), pmk(a, 480, 448, fin, 4, 18)]
    caps = ["사내 AI는 VPN 주소 풀에서 온 요청을 허용해요", "유출된 계정으로 붙어도 풀 주소를 받아요", "주소만 보는 규칙은 사람을 가려내지 못해요", "IP는 신원이 아니라 관찰 지점이에요"]
    return frame(a, "IP만 보고 믿어도 될까?", "주소만 보는 규칙은 공격자를 알아보지 못해요", caps, "".join(body))


# ---------------------------------------------------------------- Page 8 (b: add signals, hand-off)
def p8b():
    a = new()
    fin = "신호를 더할수록 안전하지만 불편·오탐도 늘어요"
    X, W, H = 300, 340, 52
    ys = (128, 200, 272, 344)
    base = [line(150, 262, 820, 262, LINE, 4, "8 6")]
    body = base + [person(100, 232, "공격자"), ai(860, 262, "사내 AI"),
                   rowc(X, ys[0], W, H, "IP 주소 10.10.99.31 → 규칙 통과", BLUE, True, 16), mk(a, X, ys[0], W, H, 1),
                   a.vis("".join(rowc(X, y, W, H, s, BLUE, None, 17) for y, s in zip(ys[1:], ("계정 · 추가 인증", "기기 상태 확인", "평소와 다른 행동")))
                         + "", 2, 2),
                   mk(a, X, ys[1], W, ys[3] + H - ys[1], 2),
                   a.vis("".join(rowc(X, y, W, H, s, RED, False, 16) for y, s in zip(ys[1:], ("추가 인증을 못 해요", "관리 안 되는 기기", "낯선 시간대 · 낯선 양"))), 3, 4),
                   mk(a, X, ys[1], W, ys[3] + H - ys[1], 3),
                   a.vis(rowc(X, ys[2], W, H, "기기 통제 → Unit 15 NAC", VIOLET, None, 17), 4, 4), mk(a, X, ys[2], W, H, 4),
                   a.vis(pill(480, 452, fin, GREEN, 17, True), 4, 4), pmk(a, 480, 452, fin, 4, 17)]
    caps = ["같은 공격자가 같은 VPN 주소로 다시 시도해요", "IP 말고 계정·기기·행동 신호를 더 확인해요", "신호마다 확인하면 공격자가 걸러져요", "확인이 늘면 불편도 늘고, 기기는 NAC로 이어져요"]
    return frame(a, "IP에 무엇을 더 확인할까?", "계정·기기·행동 신호를 함께 봐요", caps, "".join(body))


ITEMS = [  # (file, title, alt, caption, after_paragraph, fn) ; one list per Page
    [("u14-l05-p1-service-view-rev", "AI 서비스는 내가 어디 있다고 볼까?", "출장지의 박 팀장 요청이 외부 AI 서버에 닿으면 서버는 출발지 IP 192.0.2.150만 확실히 알고 실제 위치는 모른 채, IP 위치 데이터베이스와 맞춰 현지 접속이라고 짐작하므로 위치는 추정치라는 흐름입니다.", "서비스가 보는 위치는 출발지 IP로 짐작한 추정치입니다.", 1, p1)],
    [("u14-l05-p2-exit-changes-rev", "VPN을 켜면 왜 출구가 바뀔까?", "같은 노트북 192.0.2.150에서 왼쪽은 VPN을 끈 채 바로, 오른쪽은 전체 터널로 SG를 거쳐 외부 AI에 보내면 서비스에 보이는 출발지가 192.0.2.150과 198.51.100.25로 달라지는 비교입니다.", "전체 터널을 켜면 서비스는 출장지가 아니라 회사 출구 주소를 봅니다.", 1, p2)],
    [("u14-l05-p3-region-risk-rev", "지역 제한을 VPN으로 넘으면", "직원이 고객 도면 업무로 지역 제한 서비스를 열려고 개인 VPN을 거치면 출구만 바뀌고 약관·계약은 그대로여서 계정 정지와 도면 유출 위험이 생기고, 회사는 공식 지원 지역과 기업 계약부터 확인한다는 흐름입니다.", "지역 제한을 출구로 넘는 일은 계정·데이터·책임의 위험을 낳습니다.", 2, p3)],
    [("u14-l05-p4-ip-reputation-rev", "IP 주소에도 평판이 있다?", "본사 PC들이 NAT 출구 198.51.100.25 하나로 나가므로 감염된 PC의 스팸 때문에 출구 평판이 깎이고 정상 메일도 의심받아서, 출구 뒤 장비를 점검하고 차단 해제를 요청하는 모습입니다.", "출구를 함께 쓰면 남의 행동의 평판도 함께 떠안습니다.", 1, p4)],
    [("u14-l05-p5-router-vpn-rev", "공유기 VPN 기능의 위험", "박 팀장 집 공유기에 켜져 있던 VPN 서버 기능이 기본 비밀번호와 오래된 펌웨어 때문에 낯선 계정을 허용하게 되고, 비밀번호 변경·기능 끄기·펌웨어 업데이트 순서로 막는 모습입니다.", "쓰지 않는 공유기 기능은 끄고 관리자 비밀번호와 펌웨어부터 챙깁니다.", 2, p5)],
    [("u14-l05-p6-relay-rev", "내 공유기가 남의 중계소라면?", "공격자가 장악된 한결디자인 공유기를 거쳐 API 업체에 요청을 보내면 로그에 198.51.100.25가 남아 이 IP에서 왔다는 사실만 확인되고 이 사람이 했다는 것은 이어지지 않는 모습입니다.", "이 IP에서 왔다는 말과 이 사람이 했다는 말은 다릅니다.", 1, p6)],
    [("u14-l05-p7-filter-blind-rev", "개인 VPN 안은 필터가 볼 수 없어요", "직원 PC가 개인 VPN으로 필터가 막아 둔 파일 공유 사이트에 접속하면 회사 필터에는 암호화된 통신만 보여 막지 못하고, 통제는 허용할 터널을 정하는 일로 한다는 흐름입니다.", "회사 필터는 암호화된 터널 안을 볼 수 없습니다.", 1, p7),
     ("u14-l05-p7b-trace-chain", "여러 번 거친 접속은 왜 추적이 어려울까?", "공격이 해외 VPN 업체, 감염된 가정 공유기, 한결디자인 순으로 들어오고 구간마다 기록이 다른 조직에 있어, 거슬러 올라가다 기록이 없는 구간에서 역추적이 멈추는 모습입니다.", "중계 지점이 늘수록 기록이 흩어져 한 곳만 끊겨도 추적이 멈춥니다.", 2, p7b)],
    [("u14-l05-p8-ip-only-rev", "IP만 보고 믿어도 될까?", "사내 AI가 VPN 풀 10.10.99.0/24 주소를 모두 허용하면 비밀번호가 유출된 계정으로 붙은 공격자도 풀 주소를 받아 통과하므로 IP는 신원이 아니라 관찰 지점이라는 흐름입니다.", "주소만 보는 규칙은 유출된 계정의 사용자를 가려내지 못합니다.", 0, p8),
     ("u14-l05-p8b-add-signals", "IP에 무엇을 더 확인할까?", "같은 공격자가 같은 VPN 주소로 다시 시도해도 IP 규칙 외에 추가 인증, 기기 상태, 평소와 다른 행동을 확인하면 걸러지고, 확인이 늘수록 불편과 오탐도 늘며 기기 통제는 Unit 15의 NAC로 이어집니다.", "IP에 계정·기기·행동 신호를 더하고, 기기 통제는 Unit 15에서 이어집니다.", 2, p8b)],
]
assert len(ITEMS) == 8


def wire_lesson():
    wire_items(LESSON / "lesson.md", [[(f, t, al, c, ap) for f, t, al, c, ap, _fn in page] for page in ITEMS])


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for page in ITEMS:
        for f, _t, _al, _c, _ap, fn in page:
            write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire_lesson()
    print("ok", sum(len(p) for p in ITEMS), "svgs")
