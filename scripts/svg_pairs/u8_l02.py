#!/usr/bin/env python3
"""Unit 8 Lesson 2 (TCP/UDP headers, game servers) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u8_l02.py   (add --svg-only to skip the lesson.md edit).

The Lesson folder is 05-tcp-and-udp/lessons/04-*. 8 Pages x (daily-life SVG at the top + network SVG after a
matching paragraph). Existing media is kept as is: the static header overview on Page 1 (`illustrations:`) and the
l28-* animations on Pages 2, 4 and 7 (`animations:`). New items are appended; re-running replaces only ours."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv
from u7_l02 import end
from u10_l01 import at, role, lanes, msg

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("05-tcp-and-udp/lessons/04-*"))
OUT = LESSON / "assets" / "animations"


# ---------- Page 1: read the header like a map ----------
def page1(daily):
    a = Anim(4, dur(daily))
    rows = ([("받는 곳", "누구에게 가나?", BLUE), ("접수 번호 · 수령 확인", "어디까지 받았나?", GREEN), ("보관함 여유", "얼마나 더 받을 수 있나?", ORANGE), ("파손 점검 스티커", "가다가 상했나?", VIOLET)] if daily
            else [("포트 번호", "어느 프로그램으로?", BLUE), ("순서 번호 · ACK", "바이트 흐름이 어디까지?", GREEN), ("Window", "얼마나 더 받을 수 있나?", ORANGE), ("Checksum", "전송 중 손상됐나?", VIOLET)])
    head = box(50, 135, 360, 250, LINE, PANEL, 12, sw=3) + text(230, 165, "송장 (안내 정보)" if daily else "헤더 (안내 정보)", 18, MUTED, 700)
    for i, (f, q, c) in enumerate(rows):
        y = 185 + i * 50
        head += cell(70, y, 320, 40, f, c, 16)
    content = box(50, 400, 360, 58, MUTED, PANEL, 10, dash=True, sw=2) + text(230, 436, "상자 속 물건 (내용 자체)" if daily else "내용: 사진이나 웹 문서", 17, MUTED, 700)
    body = [head, content]
    for i, (f, q, c) in enumerate(rows):
        y = 185 + i * 50
        step = 2 if i == 0 else (3 if i in (1, 2) else 4)
        body.append(a.vis(arrow(395, 490, y + 20, c, 4) + text(500, y + 27, q, 18, c, 700, "start") + hl(70, y, 320, 40, c, 8), step, step if step != 3 else 3))
    body.insert(2, a.vis(hl(50, 135, 360, 250, MUTED, 12) + text(690, 280, "내용 앞에 붙는 안내예요", 20, TXT, 700), 1, 1))
    body.append(a.vis(pill(690, 400, "외울 표가 아니라 찾아 읽는 지도예요", ORANGE, 17, True, 400), 4, 4))
    if daily:
        t, sub = "송장은 상자 겉에 붙는 안내예요", "칸마다 하나의 질문에 답해요"
        caps = ["송장은 상자 속 물건이 아니라 겉에 붙는 안내예요", "받는 곳 칸은 누구에게 가는지 알려 줘요", "접수·수령 번호와 보관함 여유 칸도 각자 역할이 있어요", "파손 점검 스티커는 가다가 상했는지 확인하는 칸이에요"]
    else:
        t, sub = "헤더 칸은 질문에 답해요", "칸마다 어떤 질문에 답하는지만 알면 돼요"
        caps = ["헤더는 내용 앞에 붙는 안내 정보예요", "포트 번호는 받을 프로그램을 알려 줘요", "순서 번호·ACK와 Window는 흐름과 수신 여유를 알려 줘요", "Checksum은 전송 중 손상을 확인해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: source and destination ports swap on the reply ----------
def page2(daily):
    a = Anim(4, dur(daily))
    L, R = 40, 620
    me = ("우리 집 3동", "1203호") if daily else ("클라이언트", "포트 51514")
    you = ("가게 7동", "502호") if daily else ("웹 서버", "포트 443")
    n1, n2 = me[1].replace("포트 ", ""), you[1].replace("포트 ", "")
    left = box(L, 150, 300, 210, BLUE, PANEL, 12, sw=3) + text(L + 150, 182, me[0], 19, BLUE, 700) + cell(L + 70, 220, 160, 44, me[1], BLUE, 17)
    right = box(R, 150, 300, 210, GREEN, PANEL, 12, sw=3) + text(R + 150, 182, you[0], 19, GREEN, 700) + cell(R + 70, 220, 160, 44, you[1], GREEN, 17)
    body = [left, right,
            a.vis(text(L + 150, 310, "건물 = 컴퓨터" if daily else "IP 주소 = 컴퓨터", 16, MUTED) + text(L + 150, 335, "호수 = 프로그램" if daily else "포트 = 프로그램", 16, MUTED)
                  + text(R + 150, 310, "건물 = 컴퓨터" if daily else "IP 주소 = 컴퓨터", 16, MUTED) + text(R + 150, 335, "호수 = 프로그램" if daily else "포트 = 프로그램", 16, MUTED), 1, 1),
            a.vis(arrow(L + 305, R - 5, 220, BLUE, 5) + pill(480, 185, f"출발 {n1} → 도착 {n2}", BLUE, 15, True, 270) + hl(L + 70, 220, 160, 44, BLUE, 8), 2, 2),
            a.vis(arrow(R - 5, L + 305, 290, GREEN, 5) + pill(480, 325, f"출발 {n2} → 도착 {n1}", GREEN, 15, True, 270) + hl(R + 70, 220, 160, 44, GREEN, 8), 3, 3),
            a.vis(pill(480, 430, "80은 HTTP, 443은 HTTPS의 흔한 기본 포트 · 다른 번호도 설정할 수 있어요" if not daily else "대표 번호가 정해져 있어도 다른 호수를 쓰는 가게도 있어요", ORANGE, 16, True), 4, 4)]
    if daily:
        t, sub = "답장에서는 보낸 호수와 받는 호수가 바뀌어요", "건물은 컴퓨터를, 호수는 프로그램을 찾아요"
        caps = ["건물이 컴퓨터를, 호수가 안의 프로그램을 가리켜요", "요청은 우리 집 1203호에서 가게 502호로 가요", "답장에서는 가게 502호가 보낸 곳이 돼요", "대표 호수는 약속이라 다른 번호를 쓸 수도 있어요"]
    else:
        t, sub = "응답에서는 출발지와 목적지 포트가 바뀌어요", "예시 포트 51514와 443이에요"
        caps = ["IP는 컴퓨터를, 포트는 그 안의 프로그램을 찾아요", "요청은 출발지 51514에서 목적지 443으로 가요", "응답에서는 443이 출발지, 51514가 목적지가 돼요", "80과 443은 흔한 기본 포트이고 다른 번호도 설정할 수 있어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: sequence number, ACK, flags, data offset, checksum ----------
def page3(daily):
    a = Anim(4, dur(daily))
    strip = lambda: (box(120, 175, 600, 56, BLUE, PANEL, 8, sw=3) + text(120, 165, "1000" if not daily else "1000쪽", 17, BLUE, 700, "start") + text(720, 165, "1099" if not daily else "1099쪽", 17, BLUE, 700, "end")
                     + text(420, 210, "100바이트 데이터" if not daily else "원고 100쪽", 18, TXT, 700))
    flags = [("SYN", "연결 시작" if not daily else "통화 시작"), ("FIN", "정상 마침" if not daily else "정상 마침"), ("ACK", "확인 번호 유효" if not daily else "확인 번호 유효"), ("RST", "연결 초기화" if not daily else "처음부터 다시")]
    fl = "".join(cell(80 + i * 190, 300, 170, 40, f, GREEN, 17) + text(165 + i * 190, 365, d, 15, MUTED) for i, (f, d) in enumerate(flags))
    body = [a.vis(strip() + text(420, 255, "순서 번호 = 시작 위치 1000" if not daily else "쪽번호 = 시작 쪽 1000", 18, BLUE, 700), 1, 2),
            a.vis(box(735, 175, 105, 56, ORANGE, PANEL, 8, dash=True, sw=3) + text(787, 210, "1100", 18, ORANGE, 700) + line(787, 236, 787, 292, ORANGE, 3) + '<polygon points="787,236 778,252 796,252" fill="#ffb454"/>' + pill(500, 320, "ACK 1100 = 다음에 기대하는 위치" if not daily else "다음에 받을 쪽은 1100쪽", ORANGE, 18, True, 440), 2, 2),
            a.vis(text(480, 270, "제어 플래그" if not daily else "신호 카드", 18, MUTED, 700) + fl, 3, 3),
            a.vis(box(120, 175, 720, 56, MUTED, PANEL, 8, sw=2) + box(120, 175, 220, 56, VIOLET, PANEL, 8, sw=3) + text(230, 210, "헤더" if not daily else "안내문", 18, VIOLET, 700) + text(590, 210, "데이터" if not daily else "내용", 18, TXT, 700)
                  + line(340, 160, 340, 245, ORANGE, 4) + text(340, 150, "Data Offset: 헤더가 끝나는 곳" if not daily else "안내문이 끝나는 곳", 16, ORANGE, 700)
                  + pill(480, 310, "Checksum: 손상 점검 · 도착이나 의미를 보장하지는 않아요" if not daily else "파손 스티커: 점검일 뿐 도착을 보장하지는 않아요", VIOLET, 16, True, 700), 4, 4)]
    if daily:
        t, sub = "쪽번호와 신호 카드", "1000쪽부터 100쪽을 보내면 다음은 1100쪽이에요"
        caps = ["원고 1000쪽부터 100쪽을 보내요", "다 받았으면 다음에 받을 1100쪽을 알려요", "신호 카드로 시작, 마침, 확인, 다시 시작을 알려요", "안내문이 끝나는 곳과 파손 점검 스티커도 있어요"]
    else:
        t, sub = "순서 번호, ACK, 제어 플래그", "숫자는 설명을 위한 예시예요"
        caps = ["1000번부터 100바이트는 1000~1099를 차지해요", "모두 받았다는 ACK는 다음 위치 1100을 가리켜요", "SYN, FIN, ACK, RST는 통신 상태를 알려요", "Data Offset은 헤더의 끝을, Checksum은 손상 점검을 맡아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: receive window shrinks to zero ----------
def page4(daily):
    a = Anim(4, dur(daily))
    c = ORANGE if daily else BLUE
    sx, sy, sw_, sh = 400, 165, 160, 265
    slot_h = sh / 8
    shelf = box(sx, sy, sw_, sh, LINE, PANEL, 10, sw=3)
    for i in range(1, 8):
        shelf += line(sx, sy + i * slot_h, sx + sw_, sy + i * slot_h, LINE, 2)
    fill = lambda n, col=c: "".join(box(sx + 6, sy + sh - (i + 1) * slot_h + 4, sw_ - 12, slot_h - 8, col, col, 4, sw=0) for i in range(n))
    snd = person(110, 280, "접시를 내는 주방") if daily else end(False, 110, 290, "송신 측")
    rdr = person(850, 280, "서빙하는 직원") if daily else end(False, 850, 290, "프로그램")
    lbl = lambda s, col: pill(480, 132, s, col, 17, True, 300)
    body = [shelf, snd, rdr, text(sx + sw_ / 2, sy + sh + 28, "서빙대" if daily else "수신 버퍼", 17, MUTED, 700),
            a.vis(fill(3) + lbl("여유가 많아요 · 윈도 큼" if not daily else "빈자리가 많아요", GREEN) + arrow(190, 390, 300, BLUE, 5), 1, 1),
            a.vis(fill(7) + lbl("여유가 줄어요 · 윈도 작아짐" if not daily else "빈자리가 줄어요", ORANGE) + arrow(190, 390, 300, BLUE, 3), 2, 2),
            a.vis(fill(8, RED) + lbl("Zero Window · 공간 없음" if not daily else "빈자리 없음", RED) + cross(300, 300) + text(290, 340, "새 데이터를 멈춰요" if not daily else "새 접시를 멈춰요", 17, RED, 700), 3, 3),
            a.vis(fill(4) + lbl("공간이 생기면 알려요" if not daily else "자리가 나면 알려요", GREEN) + arrow(570, 770, 300, GREEN, 5) + arrow(190, 390, 300, BLUE, 5)
                  + text(670, 275, "읽어 가요" if not daily else "서빙해요", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "서빙대에 접시를 둘 자리가 있을까", "받는 쪽의 여유에 맞춰 접시를 내요"
        caps = ["서빙대에 빈자리가 많으면 접시를 계속 내요", "빈자리가 줄면 알리는 여유도 작아져요", "자리가 없으면 새 접시 내기를 멈춰요", "자리가 나면 알리고 다시 내기 시작해요"]
    else:
        t, sub = "수신 윈도가 줄어 0이 되는 과정", "흐름 제어는 받는 쪽의 여유를 살펴요"
        caps = ["수신 버퍼에 여유가 많으면 윈도도 커요", "버퍼가 차면 알리는 윈도 값이 작아져요", "가득 차면 Zero Window로 새 데이터를 멈춰요", "공간이 생기면 알리고 전송을 이어가요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: flow control vs congestion control ----------
def page5(daily):
    a = Anim(4, dur(daily))
    L = end(daily, 100, 280, "주방" if daily else "송신 측")
    R = box(740, 190, 180, 190, GREEN, PANEL, 12, sw=3) + text(830, 222, "서빙대" if daily else "수신 버퍼", 18, GREEN, 700) + "".join(box(760 + (i % 4) * 36, 245 + (i // 4) * 50, 30, 40, MUTED, PANEL, 4, sw=2) for i in range(8))
    road = box(200, 255, 520, 50, LINE, PANEL, 8, sw=2) + text(460, 340, "좁은 도로" if daily else "네트워크 경로", 17, MUTED, 700)
    cars = "".join(box(230 + i * 64, 265, 44, 30, ORANGE, ORANGE, 5, sw=0) for i in range(7))
    body = [L, R, road, a.vis(cars, 3, 4),
            a.vis(hl(740, 190, 180, 190, GREEN, 12) + pill(830, 150, "흐름 제어: 받는 쪽 여유" if not daily else "받는 쪽 자리", GREEN, 16, True, 220), 1, 1),
            a.vis(hl(200, 255, 520, 50, ORANGE, 8) + pill(460, 215, "혼잡 제어: 경로의 붐빔" if not daily else "도로의 붐빔", ORANGE, 16, True, 240), 2, 2),
            a.vis(pill(830, 150, "받는 프로그램과 컴퓨터를 보호" if not daily else "받는 쪽을 보호", GREEN, 15, False, 220) + pill(460, 215, "공유하는 경로를 보호" if not daily else "함께 쓰는 길을 보호", ORANGE, 15, False, 240), 3, 3),
            a.vis(pill(480, 445, "패킷 하나가 늦었다고 곧 혼잡이라고 단정하지는 않아요" if not daily else "접시 하나가 늦었다고 곧 길이 막혔다고 단정하지는 않아요", RED, 16, True), 4, 4)]
    if daily:
        t, sub = "받는 쪽 자리와 도로의 붐빔은 달라요", "둘 다 보내는 양을 조절하지만 살피는 곳이 달라요"
        caps = ["서빙대의 빈자리는 받는 쪽의 여유예요", "도로가 붐비는지는 길의 상태예요", "하나는 받는 쪽을, 하나는 함께 쓰는 길을 보호해요", "접시 하나가 늦었다고 길이 막혔다고 단정하지 않아요"]
    else:
        t, sub = "흐름 제어와 혼잡 제어", "둘 다 보내는 양을 조절하지만 살피는 곳이 달라요"
        caps = ["흐름 제어는 받는 쪽의 수신 버퍼 여유를 살펴요", "혼잡 제어는 데이터가 지나는 경로의 혼잡을 살펴요", "각각 받는 쪽과 공유하는 경로를 보호해요", "패킷 하나가 늦었다고 혼잡이라고 단정할 수는 없어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: header sizes ----------
def page6(daily):
    a = Anim(4, dur(daily))
    u = lambda n: n * 20
    xrow = 130
    udp_h, tcp_h, pw = u(8), u(20), 400
    rows = text(80, 205, "UDP", 20, ORANGE, 700, "start") + text(80, 295, "TCP", 20, BLUE, 700, "start")
    body = [rows,
            a.vis(box(xrow + udp_h, 180, pw, 46, MUTED, PANEL, 6, sw=2) + text(xrow + udp_h + pw / 2, 210, "같은 크기의 데이터" if not daily else "같은 물건", 17, MUTED, 700)
                  + box(xrow + tcp_h, 270, pw, 46, MUTED, PANEL, 6, sw=2) + text(xrow + tcp_h + pw / 2, 300, "같은 크기의 데이터" if not daily else "같은 물건", 17, MUTED, 700), 1, 4),
            a.vis(box(xrow, 180, udp_h, 46, ORANGE, ORANGE, 6, sw=0) + text(xrow + udp_h / 2, 170, "8바이트" if not daily else "짧은 송장", 17, ORANGE, 700)
                  + text(480, 260, "출발지 포트 · 목적지 포트 · 길이 · Checksum" if not daily else "보낸 호수 · 받는 호수 · 크기 · 파손 점검", 16, MUTED), 2, 4),
            a.vis(box(xrow, 270, tcp_h, 46, BLUE, BLUE, 6, sw=0) + text(xrow + tcp_h / 2, 336, "최소 20바이트 (옵션이 붙으면 더 길어요)" if not daily else "상세 송장 (추가 칸이 붙으면 더 길어요)", 17, BLUE, 700), 3, 4),
            a.vis(pill(480, 425, "헤더 길이만 보고 빠르기를 판단하지 않아요 · 필요한 전달 기능을 함께 봐요" if not daily else "송장 길이만으로 좋고 나쁨을 정하지 않아요 · 필요한 서비스를 함께 봐요", ORANGE, 16, True), 4, 4)]
    if daily:
        t, sub = "같은 물건에 붙는 송장 길이", "짧은 송장과 상세 송장은 해 주는 일이 달라요"
        caps = ["같은 크기의 물건을 보낸다고 해 봐요", "짧은 송장은 꼭 필요한 칸만 있어요", "상세 송장은 확인과 순서 칸이 더해져 더 길어요", "송장이 길고 짧음만으로 좋고 나쁨을 정하지 않아요"]
    else:
        t, sub = "UDP 헤더 8바이트, TCP 헤더 20바이트 이상", "헤더가 짧다고 항상 더 빠르거나 좋은 것은 아니에요"
        caps = ["같은 크기의 데이터를 보낸다고 가정해요", "UDP 헤더는 네 칸, 8바이트예요", "TCP 헤더는 옵션이 없어도 최소 20바이트예요", "헤더 길이만이 아니라 필요한 전달 기능을 봐요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: latest state vs waiting for the lost update ----------
def page7(daily):
    a = Anim(4, dur(daily))
    pk = lambda n, c: cell(-22, -20, 44, 40, str(n), c, 18)
    laneL = lambda y, tag, c: pill(108, y, tag, c, 15, True, 190)
    screen = lambda y, lab, c: box(700, y - 45, 220, 90, c, PANEL, 10, sw=3) + text(810, y - 12, lab[0], 16, MUTED, 700) + text(810, y + 22, lab[1], 20, c, 700)
    yT, yU = 190, 340
    names = ("기다림 방식 (TCP처럼)", "최신 우선 (앱이 선택)") if not daily else ("순서대로 모두 보여 줘요", "최신 위치를 먼저 보여 줘요")
    body = [laneL(yT - 50, names[0], BLUE), laneL(yU - 50, names[1], GREEN), line(200, yT, 680, yT, LINE, 3), line(200, yU, 680, yU, LINE, 3),
            a.vis(at(260, yT, pk(3, ORANGE)) + at(340, yT, pk(4, ORANGE)) + at(420, yT, pk(5, ORANGE)) + at(260, yU, pk(3, ORANGE)) + at(340, yU, pk(4, ORANGE)) + at(420, yU, pk(5, ORANGE)), 1, 1),
            a.vis(at(380, yT, pk(4, ORANGE)) + at(460, yT, pk(5, ORANGE)) + at(380, yU, pk(4, ORANGE)) + at(460, yU, pk(5, ORANGE))
                  + cross(560, yT) + cross(560, yU) + text(560, yT + 40, "3번이 늦거나 사라졌어요" if not daily else "3번 알림이 사라졌어요", 16, RED, 700), 2, 2),
            a.vis(screen(yT, ("앱 화면", "3번 기다리는 중" if not daily else "3번 기다리는 중"), ORANGE) + text(430, yT + 48, "4, 5번도 앱에 전달되기 전에 기다릴 수 있어요", 15, ORANGE, 700)
                  + screen(yU, ("앱 화면", "5번을 바로 반영"), GREEN) + text(430, yU + 48, "앱이 번호를 보고 낡은 값은 버려요", 15, GREEN, 700), 3, 3),
            a.vis(pill(480, 440, "UDP가 스스로 고르는 것은 아니에요 · 중요한 행동은 확인받게 규칙을 따로 둘 수도 있어요" if not daily else "앱이 규칙을 정해요 · 중요한 일은 따로 확인받을 수도 있어요", ORANGE, 15, True), 4, 4)]
    if daily:
        t, sub = "늦은 옛 위치보다 제때 온 새 위치", "어느 쪽이 중요한지는 앱이 정해요"
        caps = ["배달 기사 위치 알림 3, 4, 5번이 차례로 가요", "3번 알림이 늦거나 사라졌어요", "한쪽은 3번을 기다리고 한쪽은 5번을 바로 보여 줘요", "어느 방식이 맞는지는 앱이 정하는 규칙이에요"]
    else:
        t, sub = "위치 갱신 3번이 사라졌을 때", "순서를 지키는 방식과 최신을 택하는 방식을 비교해요"
        caps = ["위치 갱신 3, 4, 5번을 차례로 보내요", "3번이 늦거나 사라졌어요", "순서 있는 흐름은 3번을 기다릴 수 있고 앱이 최신 5번을 고를 수도 있어요", "UDP가 스스로 고르는 것이 아니라 앱이 규칙을 정해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: how to choose TCP / UDP, and HTTP/3 ----------
def page8(daily):
    a = Anim(4, dur(daily))
    card = lambda x, title, lines_, c: (box(x, 135, 400, 160, c, PANEL, 12, sw=3) + text(x + 200, 168, title, 20, c, 700)
                                        + "".join(text(x + 200, 205 + i * 30, s, 16, TXT) for i, s in enumerate(lines_)))
    tcp = card(40, "등기 우편" if daily else "TCP", ["받았다고 확인받아요", "빠진 것은 다시 보내요"] if daily else ["순서 있는 바이트 흐름", "확인과 재전송"], BLUE)
    udp = card(520, "엽서" if daily else "UDP", ["그냥 보내요", "확인은 보낸 사람이 정해요"] if daily else ["데이터그램을 보내요", "도착·순서 보장은 앱이 정해요"], ORANGE)
    stack = [("HTTP/3", GREEN), ("QUIC (연결·암호화·흐름·혼잡 제어)", VIOLET), ("UDP", ORANGE), ("IP", MUTED)]
    if daily:
        stack = [("서비스", GREEN), ("엽서 위에 더한 확인 규칙", VIOLET), ("엽서", ORANGE), ("우편 배달", MUTED)]
    st = "".join(cell(250, 150 + i * 70, 460, 56, n, c, 17) for i, (n, c) in enumerate(stack))
    body = [a.vis(tcp, 1, 3), a.vis(udp, 2, 3),
            a.vis(pill(240, 350, "빠짐없이 전달이 중요하면" if not daily else "빠짐없이 가야 하면", BLUE, 16, True, 330) + pill(720, 350, "최신 상태를 제때 처리가 중요하면" if not daily else "제때 보는 것이 중요하면", ORANGE, 16, True, 380), 3, 3),
            a.vis(st + text(480, 450, "UDP를 쓴다고 신뢰성이나 혼잡 제어가 전혀 없다는 뜻은 아니에요" if not daily else "엽서를 쓴다고 확인 규칙이 전혀 없다는 뜻은 아니에요", 16, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "등기 우편과 엽서, 상황에 맞춰 골라요", "어느 쪽이 더 좋은지는 내용에 따라 달라요"
        caps = ["등기 우편은 받았다고 확인하고 빠진 것은 다시 보내요", "엽서는 그냥 보내며 확인은 보낸 사람이 정해요", "빠짐없이 가야 하는지, 제때 보는지가 기준이에요", "엽서 위에 확인 규칙을 더한 서비스도 있어요"]
    else:
        t, sub = "TCP와 UDP는 상황에 맞춰 골라요", "HTTP/3는 UDP 위에서 QUIC을 사용해요"
        caps = ["TCP는 순서 있는 바이트 흐름과 확인·재전송을 제공해요", "UDP는 데이터그램을 보내는 기본 기능에 집중해요", "빠짐없는 전달과 최신 상태 처리 중 무엇이 중요한지가 기준이에요", "HTTP/3는 UDP 위의 QUIC에서 필요한 기능을 제공해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, fn, network after_paragraph)
PAGES = [
    ("l28-daily-waybill-fields", "l28-header-fields-questions", page1, 1),
    ("l28-daily-apartment-reply", "l28-ports-swap-on-reply", page2, 2),
    ("l28-daily-page-numbers-signals", "l28-seq-ack-flags-checksum", page3, 0),
    ("l28-daily-serving-counter-space", "l28-window-shrinks-to-zero", page4, 1),
    ("l28-daily-counter-vs-road", "l28-flow-vs-congestion", page5, 0),
    ("l28-daily-short-vs-detailed-waybill", "l28-udp-8-tcp-20-header-size", page6, 1),
    ("l28-daily-latest-position-alert", "l28-lost-update-wait-or-latest", page7, 1),
    ("l28-daily-registered-vs-postcard", "l28-choose-tcp-udp-quic", page8, 1),
]

COPY = {
    "l28-daily-waybill-fields": ("송장은 상자 겉에 붙는 안내예요",
        "상자 속 물건과 겉에 붙는 송장이 구분되고, 송장의 받는 곳, 접수·수령 번호, 보관함 여유, 파손 점검 스티커 칸이 각각 누구에게 가는지, 어디까지 받았는지, 얼마나 더 받을 수 있는지, 가다가 상했는지에 답한다고 표시됩니다.",
        "송장은 상자 속 내용이 아니라 겉에 붙는 안내입니다. 칸마다 하나의 질문에 답하며 모든 칸을 외우는 표가 아닙니다."),
    "l28-header-fields-questions": ("헤더 칸은 질문에 답해요",
        "내용 앞에 붙는 헤더의 칸을 포트 번호, 순서 번호·ACK, Window, Checksum 순서로 보며 각각 어느 프로그램으로 가는지, 바이트 흐름이 어디까지인지, 얼마나 더 받을 수 있는지, 전송 중 손상됐는지에 답하는 칸으로 연결합니다.",
        "헤더는 외울 표가 아니라 전송에 필요한 안내 정보를 찾아 읽는 지도입니다. 어떤 질문에 답하는 칸인지 알면 됩니다.", 1),
    "l28-daily-apartment-reply": ("답장에서는 보낸 호수와 받는 호수가 바뀌어요",
        "건물은 컴퓨터를, 호수는 그 안의 프로그램을 가리킵니다. 요청은 우리 집 1203호에서 가게 502호로 가고, 답장에서는 가게 502호가 보낸 곳, 1203호가 받는 곳이 됩니다. 대표 호수는 약속이라 다른 번호를 쓸 수도 있습니다.",
        "IP 주소는 컴퓨터를, 포트 번호는 그 안의 프로그램을 찾습니다. 호수 번호는 예시입니다."),
    "l28-ports-swap-on-reply": ("응답에서는 출발지와 목적지 포트가 바뀌어요",
        "클라이언트의 포트 51514에서 웹 서버의 포트 443으로 요청이 가고, 응답에서는 443이 출발지, 51514가 목적지가 됩니다. 80과 443은 HTTP와 HTTPS의 흔한 기본 포트이고 다른 번호도 설정할 수 있다고 표시됩니다.",
        "응답에서는 요청의 출발지 포트가 목적지 포트가 됩니다. 포트 51514와 443은 예시입니다.", 2),
    "l28-daily-page-numbers-signals": ("쪽번호와 신호 카드",
        "원고 1000쪽부터 100쪽을 보내면 다음에 받을 쪽은 1100쪽이고, 신호 카드로 시작, 마침, 확인, 처음부터 다시를 알립니다. 안내문이 끝나는 곳을 표시하는 표지와 파손 점검 스티커가 있지만 스티커는 도착을 보장하지 않습니다.",
        "1000쪽부터 100쪽을 보내면 모두 받았다는 확인은 다음 쪽인 1100을 가리킵니다. 숫자는 예시입니다."),
    "l28-seq-ack-flags-checksum": ("순서 번호, ACK, 제어 플래그",
        "1000번 바이트부터 100바이트를 보내면 1000~1099를 차지하고 모두 받았다는 ACK는 다음 위치인 1100을 가리킵니다. 이어 SYN, FIN, ACK, RST 제어 플래그와, 헤더가 끝나는 곳을 알리는 Data Offset, 손상을 점검하지만 도착이나 의미를 보장하지 않는 Checksum이 나옵니다.",
        "순서 번호는 바이트의 위치, ACK는 다음에 기대하는 위치를 나타냅니다. 숫자는 설명을 위한 예시입니다.", 0),
    "l28-daily-serving-counter-space": ("서빙대에 접시를 둘 자리가 있을까",
        "서빙대에 빈자리가 많으면 접시를 계속 내고, 빈자리가 줄면 알리는 여유도 작아지며, 자리가 없으면 새 접시 내기를 멈췄다가 자리가 나면 알리고 다시 냅니다.",
        "받는 쪽의 여유에 맞춰 접시를 냅니다. 칸 수는 설명용입니다."),
    "l28-window-shrinks-to-zero": ("수신 윈도가 줄어 0이 되는 과정",
        "수신 버퍼에 여유가 많으면 윈도가 크고, 버퍼가 차면 알리는 윈도 값이 작아지며, 가득 차면 Zero Window로 새 데이터를 멈추게 합니다. 프로그램이 읽어 공간이 생기면 알리고 전송을 이어 갑니다.",
        "흐름 제어는 받는 쪽이 데이터를 받아 둘 여유를 살핍니다. 칸 수는 설명용입니다.", 1),
    "l28-daily-counter-vs-road": ("받는 쪽 자리와 도로의 붐빔은 달라요",
        "주방에서 서빙대로 가는 길에서 서빙대의 빈자리는 받는 쪽의 여유이고 좁은 도로의 붐빔은 길의 상태입니다. 둘 다 내는 양을 조절하지만 하나는 받는 쪽을, 하나는 함께 쓰는 길을 보호하며 접시 하나가 늦었다고 길이 막혔다고 단정하지는 않습니다.",
        "받는 쪽의 자리와 길의 붐빔은 서로 다른 문제입니다."),
    "l28-flow-vs-congestion": ("흐름 제어와 혼잡 제어",
        "송신 측에서 수신 측으로 가는 길에서 흐름 제어는 받는 쪽 수신 버퍼의 여유를, 혼잡 제어는 데이터가 지나는 네트워크 경로의 혼잡을 살핍니다. 각각 받는 프로그램과 컴퓨터, 공유하는 경로를 보호하며 패킷 하나가 늦었다고 혼잡이라고 단정할 수는 없습니다.",
        "흐름 제어는 받는 쪽, 혼잡 제어는 네트워크 경로를 살핍니다. 혼잡 제어의 구체적 알고리즘은 이 Lesson의 범위가 아닙니다.", 0),
    "l28-daily-short-vs-detailed-waybill": ("같은 물건에 붙는 송장 길이",
        "같은 크기의 물건에 짧은 송장은 보낸 호수, 받는 호수, 크기, 파손 점검의 네 칸만 있고, 상세 송장은 확인과 순서 칸이 더해져 더 깁니다. 송장 길이만으로 좋고 나쁨을 정하지 않는다고 표시됩니다.",
        "짧은 송장과 상세 송장은 해 주는 일이 다릅니다. 길이만으로 판단하지 않습니다."),
    "l28-udp-8-tcp-20-header-size": ("UDP 헤더 8바이트, TCP 헤더 20바이트 이상",
        "같은 크기의 데이터 앞에 UDP 헤더는 출발지 포트, 목적지 포트, 길이, Checksum 네 칸의 8바이트이고 TCP 헤더는 옵션이 없어도 최소 20바이트이며 옵션이 붙으면 더 깁니다. 헤더 길이만이 아니라 필요한 전달 기능을 함께 봐야 합니다.",
        "헤더가 짧다고 모든 상황에서 UDP가 더 빠르거나 좋은 것은 아닙니다. 필요한 전달 기능을 함께 봅니다.", 1),
    "l28-daily-latest-position-alert": ("늦은 옛 위치보다 제때 온 새 위치",
        "배달 기사 위치 알림 3, 4, 5번이 가다가 3번이 늦거나 사라집니다. 한쪽은 3번을 기다리며 보여 주고 다른 쪽은 5번을 바로 보여 주며, 어느 방식이 맞는지는 앱이 정하는 규칙이라고 표시됩니다.",
        "늦은 옛 정보보다 제때 온 새 정보를 택할 수 있지만 그 선택은 앱이 합니다."),
    "l28-lost-update-wait-or-latest": ("위치 갱신 3번이 사라졌을 때",
        "위치 갱신 3, 4, 5번을 보내다 3번이 늦거나 사라지면, 순서를 지키는 흐름은 4, 5번도 앱에 전달되기 전에 3번을 기다릴 수 있고, 앱이 번호를 보고 낡은 값을 버리면 최신 5번을 바로 반영할 수 있습니다. UDP가 스스로 고르는 것이 아니라 앱이 규칙을 정합니다.",
        "UDP는 도착과 순서를 보장하지 않으며, 최신 값을 고르거나 중요한 행동을 확인받는 규칙은 앱이 정합니다. 모든 게임이 UDP만 쓰는 것은 아닙니다.", 1),
    "l28-daily-registered-vs-postcard": ("등기 우편과 엽서, 상황에 맞춰 골라요",
        "등기 우편은 받았다고 확인하고 빠진 것은 다시 보내며 엽서는 그냥 보내고 확인은 보낸 사람이 정합니다. 빠짐없이 가야 하는지 제때 보는지가 기준이고, 엽서 위에 확인 규칙을 더한 서비스도 있습니다.",
        "어느 쪽이 더 좋은지는 내용에 따라 달라집니다."),
    "l28-choose-tcp-udp-quic": ("TCP와 UDP는 상황에 맞춰 골라요",
        "TCP는 순서 있는 바이트 흐름과 확인·재전송을, UDP는 데이터그램을 보내는 기본 기능을 제공합니다. 빠짐없는 전달과 최신 상태 처리 중 무엇이 중요한지가 기준이며, HTTP/3는 UDP 위의 QUIC이 연결·암호화·흐름 제어·혼잡 제어를 제공하므로 UDP를 쓴다고 신뢰성이나 혼잡 제어가 전혀 없다는 뜻은 아닙니다.",
        "TCP와 UDP는 앱에 제공하는 전달 방식이 다르며, 어느 쪽이 더 좋은지는 상황에 따라 달라집니다.", 1),
}


def add_pairs(lesson_md, pages):
    """Append our items to each Page's `illustrations:` (creating it if absent). Existing media stays untouched."""
    q = lambda v: json.dumps(v, ensure_ascii=False)
    ours = {f"assets/animations/{n}.svg" for items in pages for (n, *_rest) in items}
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(("- terms:", "- page_id:"))]
    assert len(starts) == len(pages), f"page count {len(starts)} != {len(pages)}"
    end_fm = next((i for i, l in enumerate(lines) if i > starts[-1] and l and not l.startswith((" ", "- "))), len(lines))
    bounds = starts + [end_fm]
    out = lines[:starts[0]]
    for p, items in enumerate(pages):
        seg = lines[bounds[p]:bounds[p + 1]]
        new = []
        for f, t, al, c, ap in items:
            new += [f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
        # drop previously generated items, keep everything else
        kept, i, in_ill = [], 0, False
        while i < len(seg):
            l = seg[i]
            if l == "  illustrations:":
                in_ill = True
            elif in_ill and l.startswith("  - file:"):
                j = i + 1
                while j < len(seg) and seg[j].startswith("    "):
                    j += 1
                if l.split("file: ", 1)[1] in ours:
                    i = j
                    continue
            elif in_ill and not l.startswith("    ") and not l.startswith("  - file:"):
                in_ill = False
            kept.append(l)
            i += 1
        if "  illustrations:" in kept:
            k = kept.index("  illustrations:") + 1
            while k < len(kept) and (kept[k].startswith("  - file:") or kept[k].startswith("    ")):
                k += 1
            kept[k:k] = new
        else:
            while kept and kept[-1] == "":
                kept.pop()
            kept += ["  illustrations:"] + new
        out += kept
    out += lines[end_fm:]
    text_ = "\n".join(out)
    if not text_.endswith("\n"):
        text_ += "\n"
    Path(lesson_md).write_text(head + "---\n" + text_ + "---\n" + body, encoding="utf-8")


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        d, n = COPY[dn], COPY[nn]
        pages.append([(dn, d[0], d[1], d[2], -1), (nn, n[0], n[1], n[2], n[3])])
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        add_pairs(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
