#!/usr/bin/env python3
"""Unit 8 Lesson 1 (TCP ACK, retransmission, window) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u8_l01.py   (add --svg-only to skip the lesson.md edit).

Page 1 already had a good network SVG (l16-tcp-ack, 'ACK 3' with simplified pieces, as the text says),
so only a daily partner with the same layout is made for it and the old file is reused."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv
from u7_l02 import end
from u7_l03 import hourglass

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-tcp-udp-details/lessons/01-*"))
OUT = LESSON / "assets" / "animations"


# ---------- Page 1 daily partner of l16-tcp-ack ----------
def page1_daily():
    a = Anim(4, dur(True))
    box_ = lambda n: cell(-32, -22, 64, 44, f"{n}번", ORANGE, 18)
    slots = "".join(box(768, 170 + i * 66, 100, 52, ORANGE, BG, 8, dash=True, sw=2) for i in range(3))
    at = lambda x, y, n: f'<g transform="translate({x},{y})">' + box_(n) + "</g>"
    body = [box(40, 125, 190, 290, LINE, PANEL, 14, sw=3) + text(135, 158, "보내는 사람", 20, TXT, 700),
            box(730, 125, 190, 290, LINE, PANEL, 14, sw=3) + text(825, 158, "받는 사람", 20, TXT, 700),
            text(480, 150, "상자 →", 17, MUTED), line(235, 380, 725, 380, LINE, 2, "8 6"), text(480, 410, "← 수령 문자", 17, MUTED),
            slots, text(818, 330, "?", 26, ORANGE, 700),
            a.vis(at(135, 330, 3), 1, 3),
            mv(a, box_(1), [(135, 196), (818, 196)], 1, 1, 1, 0.1, 0.7), mv(a, box_(2), [(135, 262), (818, 262)], 1, 1, 1, 0.1, 0.8),
            a.vis(at(818, 196, 1) + at(818, 262, 2) + check(895, 196) + check(895, 262), 2, 4),
            mv(a, pill(0, 0, "3번 주세요", GREEN, 19, True), [(780, 380), (200, 380)], 3, 3, 3, 0.1, 0.8),
            a.vis(pill(135, 380, "3번 주세요", GREEN, 19, True), 4, 4),
            mv(a, box_(3), [(135, 330), (780, 330)], 4, 4, 4, 0.1, 0.8)]
    caps = ["보내는 사람이 1번, 2번 상자를 보내요", "받는 사람 칸에 1번, 2번이 도착했어요", "받는 사람이 “3번 주세요”라고 수령 문자를 보내요", "앞은 받았으니 3번 상자가 출발해요"]
    return frame(a, "다음에 받을 번호를 알려 줘요", "1·2번까지 연속해서 받았다는 뜻이에요", caps, "".join(body))


# ---------- Page 2: receive window ----------
def page2(daily):
    a = Anim(4, dur(daily))
    x0, step, y = 300, 52, 290
    c = ORANGE if daily else BLUE
    slots = "".join(box(x0 + i * step, y, 46, 60, LINE, PANEL, 6, sw=3) for i in range(8))
    fill = lambda lo, hi: "".join(box(x0 + i * step, y, 46, 60, c, c, 6, sw=3) for i in range(lo, hi))
    srv = person(110, 275, "보내는 사람") if daily else end(False, 110, 290, "송신 측")
    rdr = person(850, 275, "결재하는 사람") if daily else end(False, 850, 290, "프로그램")
    body = [slots, text(x0 + 4 * step - 3, 388, "서류 트레이" if daily else "수신 버퍼", 18, MUTED, 700), srv, rdr,
            a.vis(fill(0, 3) + brace(x0 + 3 * step, x0 + 8 * step - 6, 282, GREEN, "윈도 5칸" if not daily else "남은 자리 5칸"), 1, 1),
            a.vis(fill(0, 6) + brace(x0 + 6 * step, x0 + 8 * step - 6, 282, GREEN, "윈도 2칸" if not daily else "남은 자리 2칸")
                  + pill(850, 200, "늦게 읽어요" if not daily else "늦게 처리해요", ORANGE, 16, True), 2, 2),
            a.vis(fill(0, 3) + brace(x0 + 3 * step, x0 + 8 * step - 6, 282, GREEN, "윈도 5칸" if not daily else "남은 자리 5칸")
                  + arrow(800, 740, 320, GREEN, 5) + text(770, 360, "읽어 가요" if not daily else "처리해요", 17, GREEN, 700), 3, 3),
            a.vis(fill(0, 3) + pill(250, 440, "흐름 제어: 받는 쪽 공간은?", GREEN, 18, True) + pill(690, 440, "혼잡 제어: 경로가 감당할까?", BLUE, 18, True), 4, 4)]
    if daily:
        t, sub = "트레이에 남은 자리를 알려 줘요", "자리가 있는 만큼만 더 받을 수 있어요"
        caps = ["서류 트레이에 3칸이 차 있고 5칸이 비어 있어요", "처리가 늦으면 쌓여서 남은 자리가 2칸이에요", "처리해 가면 남은 자리가 다시 늘어요", "받는 쪽 자리와 길이 감당하는 양은 다른 문제예요"]
    else:
        t, sub = "수신 윈도는 남은 버퍼 공간", "한 칸은 설명용 단위예요"
        caps = ["수신 버퍼에 3칸이 차 있고 윈도는 5칸이에요", "프로그램이 늦게 읽으면 윈도가 2칸으로 줄어요", "읽어 가면 윈도가 다시 늘어요", "흐름 제어는 받는 쪽 공간, 혼잡 제어는 경로를 살펴요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: RTO and retransmission ----------
def page3(daily):
    a = Anim(4, dur(daily))
    cli = person(110, 215, "보내는 사람") if daily else end(False, 110, 230, "송신 측")
    srv = house(850, 245, "받는 집") if daily else end(False, 850, 230, "수신 측")
    lab = "1번 상자" if daily else "1001~1500"
    pk = lambda: cell(-52, -20, 104, 40, lab, ORANGE, 15)
    body = [cli, srv, line(190, 245, 770, 245, LINE, 3), line(200, 372, 760, 372, LINE, 2),
            mv(a, pk(), [(250, 245), (480, 245)], 1, 1, 1, 0.1, 0.6),
            a.vis(cross(480, 245), 1.7, 1),
            a.vis(pill(480, 190, "도중에 사라졌어요", RED, 17, True), 1, 1),
            a.vis(ask(110, 150) + pill(480, 190, "수령 소식이 없어요" if daily else "ACK가 오지 않아요", ORANGE, 17, True), 2, 2)]
    for i in range(4):
        body.append(a.vis(box(200 + i * 140, 372, 134, 22, ORANGE, ORANGE, 3, sw=1), 2 + i * 0.25, 3))
    body += [a.vis(text(480, 358, "기다리는 시간이 흘러요", 17, ORANGE, 700), 2, 2) if daily else a.vis(text(480, 358, "RTO 동안 기다려요", 17, ORANGE, 700), 2, 2),
             a.vis(pill(480, 190, "기다릴 시간이 지났어요" if daily else "RTO가 만료됐어요", ORANGE, 17, True), 3, 3),
             mv(a, pk(), [(250, 245), (740, 245)], 3, 3, 3, 0.15, 0.85),
             a.vis(text(480, 300, "같은 번호를 다시 보내요" if daily else "같은 순서 번호 범위를 다시 보내요", 18, BLUE, 700), 3, 3),
             a.vis(check(850, 180) + text(480, 300, "대기 시간은 상황에 따라 조정돼요" if daily else "RTO는 RTT 표본 등으로 조정돼요", 18, MUTED, 700)
                   + text(480, 335, "(ping 결과와 같은 값은 아니에요)" if not daily else "", 16, MUTED), 4, 4)]
    if daily:
        t, sub = "소식이 없으면 기다렸다 다시 보내요", "정해진 시간이 지나도 소식이 없을 때예요"
        caps = ["상자가 도중에 사라졌어요", "받았다는 소식이 오지 않아요", "기다릴 시간이 지났어요", "같은 번호의 상자를 다시 보내요"]
    else:
        t, sub = "RTO가 지나면 다시 전송해요", "타임아웃은 손실 확정이 아니라 기다릴 시간이 지났다는 뜻이에요"
        caps = ["세그먼트가 도중에 사라졌어요", "확인 응답(ACK)이 오지 않아요", "재전송 타임아웃(RTO)이 만료돼요", "같은 순서 번호 범위를 다시 보내요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: out of order + duplicate ACK ----------
def page4(daily):
    a = Anim(4, dur(daily))
    la, lb = ("1번 상자", "2번 상자") if daily else ("1001~1500", "1501~2000")
    A = lambda: cell(-46, -20, 92, 40, la, ORANGE, 14)
    B = lambda: cell(-46, -20, 92, 40, lb, BLUE, 14)
    snd = person(110, 250, "보내는 사람") if daily else end(False, 110, 265, "송신 측")
    body = [snd, box(610, 130, 310, 300, LINE, PANEL, 14, sw=3) + text(765, 160, "받는 사람" if daily else "수신 측", 20, TXT, 700),
            box(650, 185, 110, 50, ORANGE, BG, 8, dash=True, sw=2), box(650, 255, 110, 50, BLUE, BG, 8, dash=True, sw=2),
            box(650, 335, 230, 50, LINE, BG, 8, sw=2) + text(765, 367, "담당 직원" if daily else "프로그램", 17, MUTED, 700),
            mv(a, A(), [(230, 210), (400, 210)], 1, 1, 1, 0.1, 0.6), a.vis(cross(400, 210), 1.65, 1),
            mv(a, B(), [(230, 280), (705, 280)], 1, 1, 1, 0.1, 0.85),
            a.vis(box(650, 255, 110, 50, BLUE, BLUE, 8, sw=2) + text(705, 286, lb, 14, BG, 700) + text(820, 288, "보관", 16, BLUE, 700), 2, 3),
            a.vis(box(650, 185, 110, 50, ORANGE, BG, 8, dash=True, sw=2) + text(705, 216, "?", 24, ORANGE, 700)
                  + pill(765, 410, "건너뛰어 전달 못 해요", RED, 15, True, 230), 2, 2),
            mv(a, pill(0, 0, "다음은 1번이에요" if daily else "ACK 1001", GREEN, 16, True), [(610, 330), (230, 330)], 3, 3, 3, 0.05, 0.5),
            mv(a, pill(0, 0, "다음은 1번이에요" if daily else "ACK 1001", GREEN, 16, True), [(610, 330), (230, 330)], 3, 3, 3, 0.4, 0.85),
            a.vis(text(400, 375, "같은 소식이 반복돼요" if daily else "중복 ACK: 빠진 구간이 있을 수 있어요", 17, GREEN, 700), 3, 3),
            mv(a, A(), [(230, 210), (705, 210)], 4, 4, 4, 0.1, 0.7),
            a.vis(box(650, 185, 110, 50, ORANGE, ORANGE, 8, sw=2) + text(705, 216, la, 14, BG, 700) + box(650, 255, 110, 50, BLUE, BLUE, 8, sw=2) + text(705, 286, lb, 14, BG, 700)
                  + check(900, 360) + text(400, 375, "이어지면 한꺼번에 전달해요 (ACK 2001)" if not daily else "이어지면 한꺼번에 전달해요 (3번을 주세요)", 17, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "뒤쪽 상자가 먼저 와도 건너뛰지 않아요", "빈 구간이 채워져야 순서대로 전달해요"
        caps = ["1번이 사라지고 2번이 먼저 도착해요", "2번은 보관하지만 1번을 건너뛰어 전달하지 못해요", "받는 사람은 “다음은 1번”이라고 같은 소식을 반복해요", "1번이 도착해 이어지면 한꺼번에 전달해요"]
    else:
        t, sub = "뒤쪽 데이터가 먼저 와도 기다려요", "Out of order와 중복 ACK 읽기"
        caps = ["1001~1500이 사라지고 1501~2000이 먼저 도착해요", "뒤쪽은 보관하지만 앞 구간을 건너뛰어 전달하지 못해요", "수신 측이 ACK 1001을 반복해요 (중복 ACK)", "빠진 구간이 도착해 이어지면 연속 데이터로 전달해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: zero window ----------
def page5(daily):
    a = Anim(4, dur(daily))
    snd = person(110, 255, "물 따르는 사람") if daily else end(False, 110, 270, "송신 측")
    rdr = person(850, 255, "마시는 사람") if daily else end(False, 850, 270, "프로그램")
    c = BLUE
    gx, gy, gw, gh = 420, 140, 120, 260
    level = lambda frac, col=c: box(gx + 3, gy + gh - 3 - (gh - 6) * frac, gw - 6, (gh - 6) * frac, col, col, 4, sw=0)
    body = [snd, rdr, box(gx, gy, gw, gh, LINE, PANEL, 10, sw=3), text(gx + gw / 2, gy - 12, "컵" if daily else "수신 버퍼", 18, MUTED, 700),
            a.vis(level(0.7) + arrow(190, 410, 270, BLUE, 5) + pill(gx + gw / 2, gy + gh + 30, "윈도 30%" if not daily else "남은 자리 조금", GREEN, 16), 1, 1),
            a.vis(level(1.0, RED) + cross(300, 270) + pill(gx + gw / 2, gy + gh + 30, "윈도 0" if not daily else "남은 자리 없음", RED, 17, True)
                  + text(300, 235, "잠시 멈춰요", 18, ORANGE, 700), 2, 2),
            a.vis(level(0.45) + arrow(550, 790, 270, GREEN, 5) + text(670, 245, "마셔요" if daily else "읽어 가요", 17, GREEN, 700)
                  + pill(gx + gw / 2, gy + gh + 30, "윈도 55%" if not daily else "남은 자리 생김", GREEN, 16), 3, 3),
            a.vis(level(0.45) + arrow(190, 410, 270, BLUE, 5) + pill(gx + gw / 2, gy + gh + 30, "윈도가 다시 열렸어요" if not daily else "다시 따라도 돼요", GREEN, 16, True)
                  + pill(690, 200, "연결을 닫은 것이 아니에요", ORANGE, 17, True), 4, 4)]
    if daily:
        t, sub = "컵이 가득 차면 잠시 멈춰요", "다 마시면 다시 따를 수 있어요"
        caps = ["컵에 물이 많이 차 있어요", "컵이 가득 차서 잠시 따르기를 멈춰요", "마시면 자리가 다시 생겨요", "자리가 생기면 다시 따라요"]
    else:
        t, sub = "제로 윈도는 잠시 멈추라는 뜻", "연결 종료(FIN)와는 달라요"
        caps = ["수신 버퍼가 많이 차 있어요", "버퍼가 가득 차면 윈도 0을 알려 새 데이터를 멈춰요", "프로그램이 읽으면 공간이 다시 생겨요", "윈도가 열리면 전송이 이어져요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: capture marks -> first question ----------
def page6(daily):
    a = Anim(5, dur(daily, 5))
    tags = (["분실이 의심돼요", "다시 배송됐어요", "순서가 뒤바뀌어 도착해요", "같은 소식이 반복돼요", "받을 자리가 가득해요"] if daily
            else ["손실 세그먼트", "재전송", "순서가 어긋난 데이터", "중복 ACK", "제로 윈도"])
    qs = (["어느 상자가 아직 확인되지 않았나?", "같은 상자 번호를 다시 보냈나?", "도착 순서와 번호 순서가 어디서 달라졌나?",
           "받는 사람은 다음에 어떤 상자를 기다리나?", "받는 사람이 더 받을 자리가 없다고 알렸나?"] if daily
          else ["어떤 바이트 범위가 아직 확인되지 않았나?", "같은 순서 번호 범위가 다시 전송됐나?", "도착 순서와 바이트 순서가 어디서 달라졌나?",
                "수신 측은 다음에 어떤 바이트를 기다리나?", "수신 측이 더 받을 공간이 없다고 알렸나?"])
    cols = [RED, ORANGE, BLUE, VIOLET, GREEN]
    body = [text(210, 135, "표식" if not daily else "배송 조회", 18, MUTED, 700), text(560, 135, "먼저 확인할 질문", 18, MUTED, 700)]
    for k, (tg, q, c) in enumerate(zip(tags, qs, cols), 1):
        y = 175 + (k - 1) * 55
        body.append(a.vis(pill(210, y, tg, c, 17, True, 330) + arrow(390, 440, y, MUTED, 3) + text(460, y + 6, q, 18, TXT, 600, "start"), k, 5))
    body.append(a.vis(pill(480, 455, "표식 하나만으로 원인을 단정하지는 않아요", ORANGE, 18, True), 5, 5))
    if daily:
        t, sub = "배송 조회 표식, 무엇을 물을까", "표식마다 먼저 확인할 질문이 달라요"
        caps = ["분실이 의심되면 확인되지 않은 상자를 찾아요", "다시 배송됐으면 같은 번호인지 확인해요", "순서가 뒤바뀌었으면 어디서 달라졌는지 봐요", "같은 소식이 반복되면 기다리는 상자를 봐요", "자리가 가득하다는 소식인지 확인해요"]
    else:
        t, sub = "캡처 표식마다 질문을 골라요", "표식 하나로 원인을 단정하지 않아요"
        caps = ["손실 세그먼트는 확인되지 않은 범위를 찾아요", "재전송은 같은 번호 범위인지 확인해요", "Out of order는 어디서 순서가 달라졌는지 봐요", "중복 ACK는 수신 측이 기다리는 바이트를 봐요", "제로 윈도는 공간이 없다고 알렸는지 확인해요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, daily fn, network after_paragraph)
PAGES = [
    ("l16-daily-next-box-number", "l16-tcp-ack", page1_daily, 2),
    ("l16-daily-tray-free-slots", "l16-receive-window-free-space", page2, 1),
    ("l16-daily-no-news-resend", "l16-rto-resend", page3, 0),
    ("l16-daily-later-box-first", "l16-out-of-order-dup-ack", page4, 0),
    ("l16-daily-cup-full-pause", "l16-zero-window-pause", page5, 0),
    ("l16-daily-tracking-marks", "l16-capture-marks-questions", page6, 1),
]

COPY = {
    "l16-daily-next-box-number": ("다음에 받을 번호를 알려 줘요",
        "보내는 사람이 1번, 2번 상자를 보내면 받는 사람 칸에 도착하고, 받는 사람이 “3번 주세요”라는 수령 문자를 돌려보냅니다. 앞은 받았으니 3번 상자가 출발합니다.",
        "수령 문자의 ‘3번 주세요’는 1·2번까지 연속해서 받았다는 뜻입니다. 확인을 기다리지 않고 여러 상자를 보내도 됩니다."),
    "l16-tcp-ack": ("ACK는 다음에 받을 바이트 위치를 가리켜요",
        "왼쪽 송신 측에서 1번과 2번 상자가 오른쪽 수신 측으로 가고, ACK 3이라고 적힌 말풍선이 돌아옵니다. 이어 3번 상자가 출발하는 단순화된 누적 확인 예시입니다.",
        "그림에서 ACK 3은 앞의 두 조각을 연속해서 받았다는 뜻입니다. 실제 번호는 바이트 기준이고, 송신 측은 여러 조각을 동시에 보낼 수 있습니다."),
    "l16-daily-tray-free-slots": ("트레이에 남은 자리를 알려 줘요",
        "서류 트레이 8칸 중 3칸이 차 있고 남은 자리는 5칸입니다. 처리가 늦으면 6칸이 차서 남은 자리가 2칸이 되고, 처리해 가면 다시 늘어납니다. 마지막에 받는 쪽 자리와 길이 감당하는 양은 다른 문제라고 표시됩니다.",
        "남은 자리가 있는 만큼만 더 받을 수 있습니다. 한 칸은 설명용 단위입니다."),
    "l16-receive-window-free-space": ("수신 윈도는 남은 버퍼 공간",
        "수신 버퍼 8칸 중 3칸이 차 있고 윈도는 5칸입니다. 프로그램이 늦게 읽으면 윈도가 2칸으로 줄고, 읽으면 다시 늘어납니다. 흐름 제어는 받는 쪽 공간을, 혼잡 제어는 경로가 감당할 수 있는지를 살핍니다.",
        "수신 윈도는 더 받아 둘 수 있는 바이트 범위입니다. 한 칸은 설명용 단위이며 속도나 세그먼트 크기가 아닙니다.", 1),
    "l16-daily-no-news-resend": ("소식이 없으면 기다렸다 다시 보내요",
        "1번 상자가 도중에 사라지고 받았다는 소식이 오지 않아 시간이 흐릅니다. 기다릴 시간이 지나면 같은 번호의 상자를 다시 보내 받는 집에 도착합니다.",
        "정해진 시간이 지나도 소식이 없으면 같은 상자를 다시 보냅니다."),
    "l16-rto-resend": ("RTO가 지나면 다시 전송해요",
        "순서 번호 1001~1500의 세그먼트가 도중에 사라지고 ACK가 오지 않아 RTO를 기다립니다. RTO가 만료되면 같은 순서 번호 범위를 다시 보내고, RTO는 RTT 표본 등으로 조정되며 ping 결과와 같은 값은 아닙니다.",
        "타임아웃은 손실 확정이 아니라 확인을 기다릴 시간이 지났다는 뜻입니다. 번호는 예시입니다.", 0),
    "l16-daily-later-box-first": ("뒤쪽 상자가 먼저 와도 건너뛰지 않아요",
        "1번 상자가 사라지고 2번 상자가 먼저 도착해 보관되지만 1번을 건너뛰어 전달하지는 못합니다. 받는 사람은 “다음은 1번이에요”를 반복해 보내고, 1번이 도착해 이어지면 한꺼번에 전달합니다.",
        "빈 구간이 채워져야 순서대로 전달합니다."),
    "l16-out-of-order-dup-ack": ("뒤쪽 데이터가 먼저 와도 기다려요",
        "1001~1500이 사라지고 1501~2000이 먼저 도착해 보관되지만 앞 구간을 건너뛰어 프로그램에 전달하지 못합니다. 수신 측은 ACK 1001을 반복하고(중복 ACK), 빠진 구간이 도착해 이어지면 ACK 2001과 함께 연속 데이터로 전달합니다.",
        "중복 ACK는 빠진 구간이 있을 수 있다는 단서입니다. 번호는 예시입니다.", 0),
    "l16-daily-cup-full-pause": ("컵이 가득 차면 잠시 멈춰요",
        "컵에 물이 많이 차 있다가 가득 차면 물 따르기를 잠시 멈추고, 마시면 자리가 생겨 다시 따릅니다. 마지막에 연결을 닫은 것이 아니라고 표시됩니다.",
        "컵이 가득 차면 잠시 멈추고 자리가 생기면 다시 따릅니다."),
    "l16-zero-window-pause": ("제로 윈도는 잠시 멈추라는 뜻",
        "수신 버퍼가 가득 차 윈도 0을 알리면 송신 측이 새 데이터를 잠시 멈추고, 프로그램이 읽어 공간이 생기면 윈도가 다시 열려 전송이 이어집니다. 연결을 닫은 것이 아닙니다.",
        "제로 윈도는 이 수신 측에 지금 새 데이터를 받을 공간이 없다는 알림이며 연결 종료와 다릅니다.", 0),
    "l16-daily-tracking-marks": ("배송 조회 표식, 무엇을 물을까",
        "분실이 의심돼요, 다시 배송됐어요, 순서가 뒤바뀌어 도착해요, 같은 소식이 반복돼요, 받을 자리가 가득해요의 다섯 표식이 차례로 나타나고 각각 먼저 확인할 질문이 옆에 붙습니다. 표식 하나만으로 원인을 단정하지는 않는다고 표시됩니다.",
        "표식마다 먼저 확인할 질문이 다릅니다."),
    "l16-capture-marks-questions": ("캡처 표식마다 질문을 골라요",
        "손실 세그먼트, 재전송, 순서가 어긋난 데이터, 중복 ACK, 제로 윈도의 다섯 캡처 표식이 차례로 나타나고 각각 먼저 확인할 질문이 옆에 붙습니다. 표식 하나만으로 원인을 단정하지는 않는다고 표시됩니다.",
        "표식 하나만으로 문제가 네트워크 경로인지 애플리케이션인지 단정할 수는 없습니다.", 1),
}

OLD = {"l16-tcp-ack"}


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        daily_fn = fn if fn.__code__.co_argcount == 0 else (lambda f=fn: f(True))
        write(OUT, dn, daily_fn())
        items = [(dn, *COPY[dn][:3], -1)]
        if nn not in OLD:
            write(OUT, nn, fn(False))
        c = COPY[nn]
        items.append((nn, c[0], c[1], c[2], after))
        pages.append(items)
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
