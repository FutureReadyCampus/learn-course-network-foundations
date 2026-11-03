#!/usr/bin/env python3
"""Unit 7 Lesson 3 (TCP close / TIME_WAIT) paired SVGs. Run from the repo root:
python3 scripts/svg_pairs/u7_l03.py   (add --svg-only to skip the lesson.md edit).

Daily side: the phone call from the lesson text (and the hotel room for page 5). Pages 2 and 5 already had
good network SVGs (l27-*), so only a daily partner is made for them. The old time-wait slot SVG moves from
page 4 to page 5, which is where the text talks about it."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, dur  # reuse local helpers
from u7_l01 import mv
from u7_l02 import end, dim

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("05-tcp-and-udp/lessons/03-*"))
OUT = LESSON / "assets" / "animations"


def hourglass(x, y, c=ORANGE):
    return (f'<polygon points="{x - 14},{y - 20} {x + 14},{y - 20} {x},{y}" fill="{c}"/>'
            f'<polygon points="{x - 14},{y + 20} {x + 14},{y + 20} {x},{y}" fill="{c}" fill-opacity="0.45"/>')


def state(x, y, s, c=GREEN, w=220, filled=False):
    return pill(x, y, s, c, 16, filled, w)


# ---------- Page 1: FIN closes one direction only ----------
def page1(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 110, 250, "나" if daily else "클라이언트"), end(daily, 850, 250, "상대" if daily else "서버")
    pk = lambda c: packet(0, 0, c)
    body = [cli, srv, line(190, 215, 770, 215, LINE, 3), line(190, 300, 770, 300, LINE, 3),
            a.vis(arrow(200, 760, 215, BLUE, 5) + text(480, 190, "내 이야기" if daily else "클라이언트 → 서버 데이터", 17, BLUE, 700), 1, 1),
            a.vis(arrow(760, 200, 300, GREEN, 5) + text(480, 335, "상대 이야기" if daily else "서버 → 클라이언트 데이터", 17, GREEN, 700), 1, 4),
            mv(a, pk(BLUE), [(210, 215), (750, 215)], 1, 1, 1, 0.1, 0.8),
            mv(a, pk(GREEN), [(750, 300), (210, 300)], 1, 1, 1, 0.1, 0.8),
            a.vis(pill(480, 190, "“저는 할 말 다 했어요”" if daily else "FIN: 내가 보낼 데이터는 여기까지", ORANGE, 17, True)
                  + box(762, 195, 14, 40, ORANGE, ORANGE, 3), 2, 4),
            mv(a, pk(GREEN), [(750, 300), (210, 300)], 3, 3, 3, 0.1, 0.8),
            a.vis(pill(480, 335, "“저는 아직 할 말이 남았어요”" if daily else "서버는 아직 보낼 수 있어요", GREEN, 17, True), 3, 3),
            a.vis(pill(480, 430, "한쪽 방향만 먼저 닫을 수 있어요 (half-close)", ORANGE, 19, True), 4, 4)]
    if daily:
        t, sub = "말을 마쳐도 상대는 남았을 수 있어요", "한 사람이 끝냈다고 통화가 곧바로 끝나지는 않아요"
        caps = ["두 사람이 서로 이야기를 주고받고 있어요", "내가 “저는 할 말 다 했어요” 하고 알려요", "상대는 아직 할 말이 남아 계속 말해요", "한쪽만 먼저 말을 마칠 수 있어요"]
    else:
        t, sub = "FIN은 한 방향의 송신 끝", "반대 방향은 계속 보낼 수 있어요"
        caps = ["양방향으로 데이터를 주고받고 있어요", "클라이언트가 FIN으로 자기 방향의 송신이 끝났다고 알려요", "서버는 아직 보낼 데이터가 있으면 계속 보내요", "한쪽 방향만 먼저 닫는 것을 half-close라고 해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2 daily partner of l27-tcp-four-way-close ----------
def page2_daily():
    a = Anim(4, dur(True))
    L, R = 300, 660
    ys = [190, 250, 310, 370]
    rows = [(True, "“저는 다 했어요”", ORANGE), (False, "“알겠어요”", BLUE), (False, "“저도 이제 끝났어요”", ORANGE), (True, "“알겠어요”", BLUE)]
    lst = ["끝났다고 알림 · 확인 기다림", "상대가 끝나길 기다림", "상대가 끝나길 기다림", "잠깐 더 들고 있음"]
    rst = ["통화 중", "알겠다고 했어요 · 정리 중", "알겠다고 했어요 · 정리 중", "끝!"]
    body = [pill(L - 60, 128, "나", BLUE, 17, True, 130), pill(R + 60, 128, "상대", GREEN, 17, True, 130),
            line(L, 150, L, 450, LINE, 3), line(R, 150, R, 450, LINE, 3),
            ]
    for k, ((right, lab, c), y) in enumerate(zip(rows, ys), 1):
        arr = arrow(L + 8, R - 8, y, c, 5) if right else arrow(R - 8, L + 8, y, c, 5)
        body.append(a.vis(arr + text(480, y - 14, lab, 17, c, 700), k, 4))
        body.append(a.vis(state(145, 420, lst[k - 1], ORANGE if k < 4 else GREEN, 270)
                          + state(815, 420, rst[k - 1], BLUE if k < 4 else GREEN, 270), k, k))
    caps = ["내가 먼저 “저는 할 말 다 했어요” 하고 알려요", "상대가 “알겠어요” 하고 답해요", "상대도 마저 말한 뒤 “저도 끝났어요” 해요", "내가 “알겠어요” 하면 두 쌍이 끝나요"]
    return frame(a, "끊을 때도 두 쌍의 인사", "각자 끝났다고 말하고 상대가 알겠다고 답해요", caps, "".join(body))


# ---------- Page 3: CLOSE_WAIT ----------
def page3(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 110, 230, "상대" if daily else "클라이언트"), end(daily, 850, 230, "나" if daily else "서버")
    body = [cli, srv, line(190, 215, 770, 215, LINE, 3), line(190, 290, 770, 290, LINE, 3),
            a.vis(arrow(200, 760, 215, ORANGE, 5) + text(480, 190, "“저는 끝났어요”" if daily else "FIN", 17, ORANGE, 700), 1, 4),
            a.vis(arrow(760, 200, 290, BLUE, 5) + text(480, 325, "“알겠어요”" if daily else "ACK", 17, BLUE, 700), 1, 4),
            a.vis(state(800, 360, "상대는 끝냈고 나는 정리 중" if daily else "CLOSE_WAIT", ORANGE, 250), 1, 2),
            a.vis(pill(480, 425, "남은 이야기와 정리를 마칠 수 있어요" if daily else "남은 응답과 정리 작업을 마칠 수 있어요", ORANGE, 18, True), 2, 2),
            a.vis(state(800, 360, "내 끝도 알리고 확인 기다림" if daily else "LAST_ACK", GREEN, 250)
                  + arrow(760, 200, 252, GREEN, 4) + text(480, 243, "“저도 끝났어요”" if daily else "FIN", 15, GREEN, 700)
                  + pill(480, 425, "“저도 끝났어요” 하고 알려요" if daily else "소켓을 닫으면 서버도 FIN을 보내요", GREEN, 18, True), 3, 3),
            a.vis(state(800, 360, "통화 끝" if daily else "CLOSED", GREEN, 250, True)
                  + arrow(200, 760, 252, BLUE, 4) + text(480, 243, "“알겠어요”" if daily else "ACK", 15, BLUE, 700)
                  + pill(480, 425, "마지막 확인이 오면 끝나요" if daily else "마지막 ACK가 오면 종료 절차가 끝나요", GREEN, 18, True), 4, 4)]
    if daily:
        t, sub = "끝났다는 말을 듣고도 정리가 남아요", "상대의 말을 들은 뒤 내 쪽 정리를 마쳐야 해요"
        caps = ["상대가 “저는 끝났어요” 해서 “알겠어요” 하고 답해요", "나는 아직 남은 이야기와 정리가 있어요", "정리가 끝나면 나도 “끝났어요” 하고 알려요", "상대가 확인해 주면 통화가 끝나요"]
    else:
        t, sub = "CLOSE_WAIT는 정리 중인 상태", "상대의 FIN을 확인하고 내 정리를 기다려요"
        caps = ["서버가 FIN을 ACK로 확인하고 CLOSE_WAIT가 돼요", "서버 프로그램이 남은 응답과 정리를 마칠 수 있어요", "소켓을 닫으면 서버도 FIN을 보내고 LAST_ACK가 돼요", "마지막 ACK가 오면 서버의 종료 절차가 끝나요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: TIME_WAIT ----------
def page4(daily):
    a = Anim(4, dur(daily))
    cli, srv = end(daily, 110, 240, "나" if daily else "클라이언트"), end(daily, 850, 240, "상대" if daily else "서버")
    pk = lambda c: packet(0, 0, c)
    body = [cli, srv, line(190, 250, 770, 250, LINE, 3),
            state(110, 330, "잠깐 더 들고 있음" if daily else "TIME_WAIT", ORANGE, 190) + a.vis(hourglass(110, 185), 1, 4),
            mv(a, pk(BLUE), [(210, 250), (480, 250)], 1, 1, 1, 0.1, 0.6),
            a.vis(cross(480, 250), 1.7, 1),
            a.vis(pill(480, 200, "마지막 “네”가 사라졌어요" if daily else "마지막 ACK가 사라졌어요", RED, 17, True), 1, 1),
            mv(a, pk(GREEN), [(750, 250), (210, 250)], 2, 2, 2, 0.1, 0.7),
            a.vis(pill(480, 200, "상대가 “끝났어요”를 다시 말해요" if daily else "서버가 FIN을 다시 보내요", GREEN, 17, True), 2, 2),
            mv(a, pk(BLUE), [(210, 250), (750, 250)], 3, 3, 3, 0.1, 0.7),
            a.vis(pill(480, 200, "아직 들고 있어서 다시 “네” 해요" if daily else "TIME_WAIT라서 ACK를 다시 보내요", BLUE, 17, True), 3, 3),
            a.vis(check(850, 180), 3.7, 3),
            a.vis(line(190, 385, 770, 385, LINE, 2, "8 6") + mv(a, pk(MUTED), [(750, 385), (330, 385)], 4, 4, 4, 0.1, 0.65)
                  + cross(300, 385) + pill(480, 420, "이전 통화의 늦은 말" if daily else "이전 연결의 늦은 세그먼트", MUTED, 16)
                  + pill(480, 456, "같은 번호의 새 통화에 섞이지 않게 해요" if daily else "같은 IP·포트의 새 연결과 섞이지 않게 해요", ORANGE, 18, True), 4, 4)]
    if daily:
        t, sub = "끊은 뒤에도 잠깐 수화기를 들고 있어요", "마지막 확인이 사라질 수도 있어서예요"
        caps = ["마지막 “네”가 도중에 사라졌어요", "상대가 “끝났어요”를 다시 말해요", "아직 들고 있어서 다시 “네” 하고 답해요", "늦게 온 이전 통화의 말이 새 통화에 섞이지 않게 해요"]
    else:
        t, sub = "TIME_WAIT가 남는 두 가지 이유", "예에서는 먼저 FIN을 보낸 클라이언트가 기다려요"
        caps = ["클라이언트가 보낸 마지막 ACK가 사라질 수 있어요", "그러면 서버가 FIN을 다시 보내요", "TIME_WAIT라서 ACK를 한 번 더 보낼 수 있어요", "이전 연결의 늦은 세그먼트가 새 연결에 섞이지 않게 해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5 daily partner of l27-time-wait-socket-slot ----------
def page5_daily():
    a = Anim(4, dur(True))
    cells = "".join(box(40 + (i % 10) * 28, 130 + (i // 10) * 28, 22, 22, BLUE, BLUE, 4, sw=1) for i in range(100))
    cnt = lambda n, c: (box(720, 20, 200, 62, LINE, PANEL, 12, sw=2) + text(740, 60, "사용 중", 18, MUTED, anchor="start")
                        + text(900, 64, str(n), 34, c, 700, "end"))
    room = lambda fill, lab, c: (text(365, 168, "내 객실 한 칸", 18, MUTED, 700, "start") + box(375, 185, 130, 120, fill, fill, 12, sw=0)
                                 + pill(440, 330, lab, c, 19, True, 170))
    body = [text(40, 118, "객실 100개 (설명용)", 17, MUTED, anchor="start"), cells,
            box(350, 135, 570, 290, LINE, PANEL, 14, sw=2),
            box(730, 190, 170, 90, LINE, PANEL, 12, sw=2) + text(815, 228, "다음", 22, TXT, 700) + text(815, 260, "손님", 22, TXT, 700),
            a.vis(cnt(100, TXT) + room(BLUE, "손님이 묵는 중", BLUE) + text(635, 400, "체크아웃해도 바로 빈 방은 아니에요", 20, GREEN, 700), 1, 1),
            a.vis(cnt(100, TXT) + room(ORANGE, "청소 · 점검 중", ORANGE) + hourglass(610, 245) + text(610, 295, "기다리는 중", 17, ORANGE, 700), 2, 2),
            a.vis(cnt(100, TXT) + room(ORANGE, "점검 끝", GREEN) + text(635, 400, "점검이 끝나면 정리해요", 20, GREEN, 700), 3, 3),
            a.vis(cnt(99, GREEN) + room(BLUE, "다음 손님이 입실", BLUE) + text(635, 400, "정리된 방에 다음 손님을 받아요", 20, GREEN, 700), 4, 4)]
    caps = ["객실 100개가 모두 차 있어요", "체크아웃 뒤에도 청소와 점검이 끝날 때까지 기다려요", "점검이 끝나면 객실을 정리해요", "정리된 방에 다음 손님을 받을 수 있어요"]
    return frame(a, "객실은 바로 비지 않아요", "청소와 점검이 끝나야 다음 손님을 받아요", caps, "".join(body))


# ---------- Page 6: who closes first ----------
def page6(daily):
    a = Anim(4, dur(daily))
    panel = lambda x, lab: box(x, 125, 440, 300, LINE, PANEL, 14, sw=3) + text(x + 220, 160, lab, 20, TXT, 700)
    A = end(daily, 100, 270, "나" if daily else "클라이언트")
    B = end(daily, 390, 270, "상대" if daily else "서버")
    A2 = end(daily, 560, 270, "나" if daily else "클라이언트")
    B2 = end(daily, 850, 270, "상대" if daily else "서버")
    body = [panel(30, "내가 먼저 끊으면" if daily else "클라이언트가 먼저 FIN"), panel(490, "상대가 먼저 끊으면" if daily else "서버가 먼저 FIN"),
            A, B, A2, B2,
            a.vis(arrow(150, 330, 215, ORANGE, 5) + text(240, 200, "FIN", 17, ORANGE, 700), 2, 4),
            a.vis(hourglass(100, 205) + pill(140, 380, "잠깐 더 들고 있음" if daily else "TIME_WAIT", ORANGE, 15, True, 150), 2, 4),
            a.vis(arrow(800, 620, 215, ORANGE, 5) + text(710, 200, "FIN", 17, ORANGE, 700), 3, 4),
            a.vis(hourglass(850, 205) + pill(840, 380, "잠깐 더 들고 있음" if daily else "TIME_WAIT", ORANGE, 15, True, 150), 3, 4),
            a.vis(pill(480, 456, "먼저 FIN을 보낸 쪽이 TIME_WAIT를 거쳐요" if not daily else "먼저 끊은 쪽이 잠깐 더 들고 있어요", ORANGE, 19, True), 4, 4)]
    if daily:
        t, sub = "누가 먼저 끊어도 괜찮아요", "먼저 끊은 쪽이 마지막에 잠깐 기다려요"
        caps = ["내가 먼저 끊을 수도, 상대가 먼저 끊을 수도 있어요", "내가 먼저 끊으면 내가 잠깐 더 들고 있어요", "상대가 먼저 끊으면 상대가 잠깐 더 들고 있어요", "먼저 끊은 쪽이 마지막에 기다려요"]
    else:
        t, sub = "먼저 닫는 쪽은 정해져 있지 않아요", "클라이언트와 서버의 고정된 역할이 아니에요"
        caps = ["클라이언트가 먼저 닫을 수도 서버가 먼저 닫을 수도 있어요", "클라이언트가 먼저 FIN을 보내면 클라이언트가 TIME_WAIT예요", "서버가 먼저 FIN을 보내면 서버가 TIME_WAIT예요", "먼저 FIN을 보낸 쪽이 TIME_WAIT를 거쳐요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: three groups of states ----------
def page7(daily):
    a = Anim(4, dur(daily))
    cols = [("연결 전 · 기다림" if daily else "연결 전 · 기다림", MUTED, ["전화 내려놓음", "벨 기다림"] if daily else ["CLOSED", "LISTEN"]),
            ("시작 · 통화" if daily else "시작 · 통신", BLUE, ["거는 중", "벨 울림", "통화 중"] if daily else ["SYN_SENT", "SYN_RECEIVED", "ESTABLISHED"]),
            ("끊는 중" if daily else "정리 중", ORANGE, ["끝났다고 알림", "상대 기다림", "정리 중", "마지막 확인", "잠깐 더 들고 있음", "동시에 끊음"] if daily
             else ["FIN_WAIT_1", "FIN_WAIT_2", "CLOSE_WAIT", "LAST_ACK", "TIME_WAIT", "CLOSING"])]
    xs = [40, 340, 640]
    body = []
    for k, ((lab, c, chips), x) in enumerate(zip(cols, xs), 1):
        inner = box(x, 140, 280, 270, c, PANEL, 14, sw=3) + text(x + 140, 180, lab, 21, c, 700)
        for i, ch in enumerate(chips):
            cx, cy = x + 75 + (i % 2) * 130, 232 + (i // 2) * 48
            inner += pill(cx, cy, ch, c, 14, False, 124)
        body.append(box(x, 140, 280, 270, LINE, PANEL, 14, sw=2) + text(x + 140, 180, lab, 21, MUTED, 700))
        body.append(a.vis(inner, k, 4))
        body.append(a.vis(hl(x, 140, 280, 270, c, 14), k, k))
    body.append(a.vis(pill(480, 448, "이름 전체보다 역할을 기억해요", GREEN, 19, True), 4, 4))
    if daily:
        t, sub = "전화 상태는 세 무리로 읽어요", "이름이 많아도 큰 흐름으로 묶어요"
        caps = ["아직 통화가 없거나 벨을 기다리는 무리예요", "거는 중, 벨 울림, 통화 중이 이어지는 무리예요", "끊으면서 정리하는 무리예요", "하나하나 외우기보다 어느 무리인지 읽어요"]
    else:
        t, sub = "TCP 상태는 세 무리로 읽어요", "상태 이름은 필요할 때 표에서 찾아봐요"
        caps = ["연결이 없거나 서버가 기다리는 무리예요", "연결을 시작하고 통신하는 무리예요", "FIN과 ACK로 연결을 정리하는 무리예요", "이름 전체보다 어느 무리의 역할인지 기억해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: close sequence with states ----------
def page8(daily):
    a = Anim(4, dur(daily))
    L, R = 300, 660
    ys = [190, 255, 320, 385]
    rows = [(True, "“저는 다 했어요”" if daily else "① FIN", ORANGE), (False, "“알겠어요”" if daily else "② ACK", BLUE),
            (False, "“저도 끝났어요”" if daily else "③ FIN", ORANGE), (True, "“알겠어요”" if daily else "④ ACK", BLUE)]
    lst = (["끝났다고 알림", "상대 기다리는 중", "잠깐 더 들고 있음", "잠깐 더 들고 있음"] if daily else ["FIN_WAIT_1", "FIN_WAIT_2", "TIME_WAIT", "TIME_WAIT"])
    rst = (["통화 중", "정리 중", "확인 기다림", "통화 끝"] if daily else ["ESTABLISHED", "CLOSE_WAIT", "LAST_ACK", "CLOSED"])
    body = [pill(L, 128, "나" if daily else "클라이언트", BLUE, 17, True, 150), pill(R, 128, "상대" if daily else "서버", GREEN, 17, True, 150),
            line(L, 150, L, 440, LINE, 3), line(R, 150, R, 440, LINE, 3)]
    for k, ((right, lab, c), y) in enumerate(zip(rows, ys), 1):
        arr = arrow(L + 8, R - 8, y, c, 5) if right else arrow(R - 8, L + 8, y, c, 5)
        body.append(a.vis(arr + text(480, y - 14, lab, 18, c, 700), k, 4))
        body.append(a.vis(state(130, y + 5, lst[k - 1], ORANGE, 200) + state(830, y + 5, rst[k - 1], GREEN if k == 4 else BLUE, 200), k, k))
    body.append(a.vis(text(480, 455, "마지막에는 먼저 끊은 쪽이 기다린 뒤 정리돼요" if daily else "클라이언트는 TIME_WAIT 대기 후 CLOSED로 정리돼요", 17, MUTED, 700), 4, 4))
    if daily:
        t, sub = "끊는 순서를 처음부터 끝까지", "내가 먼저 끊는 흔한 예예요"
        caps = ["내가 먼저 “저는 다 했어요” 하고 알려요", "상대가 “알겠어요” 하고 정리를 시작해요", "상대도 “저도 끝났어요” 하고 알려요", "내가 “알겠어요” 하면 상대는 통화가 끝나요"]
    else:
        t, sub = "FIN과 ACK 네 단계", "클라이언트가 먼저 끝내는 흔한 예예요"
        caps = ["클라이언트가 FIN을 보내고 FIN_WAIT_1이 돼요", "서버가 ACK를 보내고 CLOSE_WAIT가 돼요", "서버도 FIN을 보내고 LAST_ACK가 돼요", "마지막 ACK를 받은 서버는 CLOSED가 돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 9: three things to remember ----------
def page9(daily):
    a = Anim(4, dur(daily))
    cards = [("1", "한쪽이 먼저 끝내요" if daily else "한쪽이 FIN으로 끝내요", "“저는 다 했어요”" if daily else "자기 방향의 송신 끝", BLUE),
             ("2", "상대도 마치고 끝내요" if daily else "상대도 남은 송신 뒤 FIN", "남은 말을 마치고 알려요" if daily else "남은 데이터를 보낸 뒤", GREEN),
             ("3", "먼저 끝낸 쪽이 기다려요" if daily else "먼저 FIN 쪽이 TIME_WAIT", "잠깐 더 들고 있어요" if daily else "마지막 확인에 대비해요", ORANGE)]
    xs = [40, 340, 640]
    body = []
    for k, ((n, h, sub, c), x) in enumerate(zip(cards, xs), 1):
        body.append(box(x, 150, 280, 220, LINE, PANEL, 14, sw=2))
        body.append(a.vis(box(x, 150, 280, 220, c, PANEL, 14, sw=3) + text(x + 140, 215, n, 46, c, 700)
                          + text(x + 140, 275, h, 20, TXT, 700) + text(x + 140, 320, sub, 17, MUTED), k, 4))
    body.append(a.vis(pill(480, 430, "먼저 FIN을 보낸 쪽이 TIME_WAIT를 거쳐요" if not daily else "먼저 끊은 쪽이 마지막에 잠깐 기다려요", ORANGE, 19, True), 4, 4))
    if daily:
        t, sub = "끊는 일에서 기억할 세 가지", "누가 먼저인지는 정해져 있지 않아요"
        caps = ["한쪽이 먼저 자기 이야기를 마쳐요", "상대도 남은 이야기를 마치고 끝내요", "먼저 끝낸 쪽은 마지막에 잠깐 기다려요", "“누가 먼저 끊었나”가 기다리는 쪽을 정해요"]
    else:
        t, sub = "연결 종료에서 기억할 세 가지", "클라이언트·서버가 아니라 누가 먼저인지가 중요해요"
        caps = ["한쪽이 FIN으로 자기 송신을 끝내요", "상대가 남은 송신을 마치고 자기 FIN을 보내요", "먼저 FIN을 보낸 쪽이 TIME_WAIT에서 기다려요", "서버가 먼저 FIN을 보냈다면 서버가 TIME_WAIT예요"]
    return frame(a, t, sub, caps, "".join(body))


# (daily file, network file, daily fn, network fn, network after_paragraph)
PAGES = [
    ("l27-daily-one-side-done", "l27-fin-half-close", page1, 3),
    ("l27-daily-hangup-two-pairs", "l27-tcp-four-way-close", page2_daily, 3),
    ("l27-daily-still-tidying", "l27-close-wait-tidy", page3, 1),
    ("l27-daily-hold-the-phone", "l27-time-wait-reasons", page4, 1),
    ("l27-daily-hotel-room-cleaning", "l27-time-wait-socket-slot", page5_daily, 1),
    ("l27-daily-who-hangs-up-first", "l27-who-closes-first", page6, 0),
    ("l27-daily-three-groups-call", "l27-state-three-groups", page7, 1),
    ("l27-daily-hangup-step-by-step", "l27-fin-ack-steps", page8, 4),
    ("l27-daily-three-to-remember", "l27-close-three-points", page9, 2),
]

COPY = {
    "l27-daily-one-side-done": ("말을 마쳐도 상대는 남았을 수 있어요",
        "두 사람이 이야기를 주고받습니다. 내가 “저는 할 말 다 했어요” 하고 알려 한 방향이 막히지만, 상대는 “아직 할 말이 남았어요” 하며 계속 말합니다. 한쪽 방향만 먼저 닫을 수 있다고 표시됩니다.",
        "한 사람이 말을 마쳐도 상대는 계속 말할 수 있습니다. FIN으로 한쪽 방향만 닫는 것과 같습니다."),
    "l27-fin-half-close": ("FIN은 한 방향의 송신 끝",
        "클라이언트와 서버가 양방향으로 데이터를 주고받습니다. 클라이언트가 FIN을 보내 자기 방향의 송신이 끝났다고 알려도 서버는 아직 보낼 데이터가 있으면 계속 보낼 수 있으며, 이렇게 한쪽 방향만 먼저 닫는 것을 half-close라고 합니다.",
        "FIN은 한 방향의 송신이 끝났음을 알립니다. 반대 방향은 계속 보낼 수 있습니다.", 3),
    "l27-daily-hangup-two-pairs": ("끊을 때도 두 쌍의 인사",
        "나와 상대가 네 번 인사를 주고받습니다. 내가 “저는 다 했어요”, 상대가 “알겠어요”, 상대가 “저도 이제 끝났어요”, 내가 “알겠어요” 하고 말하며 각자 끝났다고 말하고 상대가 알겠다고 답하는 두 쌍이 됩니다.",
        "각자 끝났다고 말하고 상대가 알겠다고 답하는 두 쌍, 모두 네 번의 인사입니다."),
    "l27-close-wait-tidy": ("CLOSE_WAIT는 정리 중인 상태",
        "서버가 클라이언트의 FIN을 ACK로 확인하고 CLOSE_WAIT가 됩니다. 서버 프로그램이 남은 응답과 정리를 마치고 소켓을 닫으면 서버도 FIN을 보내 LAST_ACK가 되고, 마지막 ACK가 오면 종료 절차가 끝납니다.",
        "CLOSE_WAIT는 상대 FIN을 확인했지만 내 쪽 정리는 끝나지 않은 상태입니다. 오래 남을 때는 소켓을 닫았는지 로그와 함께 확인합니다.", 1),
    "l27-daily-still-tidying": ("끝났다는 말을 듣고도 정리가 남아요",
        "상대가 “저는 끝났어요” 하고 알리면 나는 “알겠어요” 하고 답하지만 아직 남은 이야기와 정리가 있습니다. 정리를 마치면 “저도 끝났어요” 하고 알리고, 상대가 확인해 주면 통화가 끝납니다.",
        "상대의 말을 들은 뒤에도 내 쪽 정리가 남아 있을 수 있습니다."),
    "l27-daily-hold-the-phone": ("끊은 뒤에도 잠깐 수화기를 들고 있어요",
        "내가 마지막으로 보낸 “네”가 도중에 사라지자 상대가 “끝났어요”를 다시 말하고, 아직 수화기를 들고 있던 내가 다시 “네” 하고 답합니다. 마지막에는 이전 통화의 늦은 말이 같은 번호의 새 통화에 섞이지 않게 막는다고 표시됩니다.",
        "먼저 끊은 쪽이 잠깐 더 기다리면 마지막 확인이 사라져도 다시 답할 수 있고, 이전 통화의 늦은 말이 섞이지 않습니다."),
    "l27-time-wait-reasons": ("TIME_WAIT가 남는 두 가지 이유",
        "클라이언트가 보낸 마지막 ACK가 사라지면 서버가 FIN을 다시 보내고, TIME_WAIT 상태의 클라이언트가 ACK를 한 번 더 보냅니다. 또한 이전 연결의 늦은 세그먼트가 같은 IP와 포트를 쓰는 새 연결에 섞이지 않게 막습니다.",
        "TIME_WAIT는 마지막 ACK가 사라졌을 때 다시 응답하고 이전 연결의 늦은 세그먼트가 새 연결에 섞이지 않게 합니다. 대기 시간은 운영체제 구현에 따라 다릅니다.", 1),
    "l27-daily-hotel-room-cleaning": ("객실은 바로 비지 않아요",
        "객실 100개가 모두 찬 호텔에서 손님이 체크아웃해도 청소와 점검이 끝날 때까지 기다리고, 점검이 끝나 정리되면 다음 손님을 받아 사용 중인 객실이 99에서 다시 찹니다.",
        "체크아웃 뒤에도 청소와 점검이 끝나야 다음 손님을 받습니다. 객실 100개는 설명용입니다."),
    "l27-daily-who-hangs-up-first": ("누가 먼저 끊어도 괜찮아요",
        "왼쪽 칸에서는 내가 먼저 끊고 내가 잠깐 더 수화기를 들고 있고, 오른쪽 칸에서는 상대가 먼저 끊고 상대가 잠깐 더 들고 있습니다. 먼저 끊은 쪽이 마지막에 기다린다고 표시됩니다.",
        "먼저 끊은 쪽이 마지막에 잠깐 기다립니다. 누가 먼저 끊을지는 정해져 있지 않습니다."),
    "l27-who-closes-first": ("먼저 닫는 쪽은 정해져 있지 않아요",
        "왼쪽 칸에서는 클라이언트가 먼저 FIN을 보내 클라이언트가 TIME_WAIT를 거치고, 오른쪽 칸에서는 서버가 먼저 FIN을 보내 서버가 TIME_WAIT를 거칩니다. 먼저 FIN을 보낸 쪽이 TIME_WAIT를 거친다고 표시됩니다.",
        "능동 종료와 수동 종료는 클라이언트·서버의 고정된 역할이 아니라 누가 먼저 FIN을 보냈는지로 정해집니다.", 0),
    "l27-daily-three-groups-call": ("전화 상태는 세 무리로 읽어요",
        "전화 상태를 세 무리로 묶습니다. 전화를 내려놓거나 벨을 기다리는 무리, 거는 중·벨 울림·통화 중인 무리, 끝났다고 알리고 기다리며 정리하는 끊는 중 무리입니다.",
        "하나하나 외우기보다 어느 무리인지 읽습니다."),
    "l27-state-three-groups": ("TCP 상태는 세 무리로 읽어요",
        "TCP 상태를 세 무리로 묶습니다. CLOSED와 LISTEN의 연결 전·기다림 무리, SYN_SENT·SYN_RECEIVED·ESTABLISHED의 시작·통신 무리, FIN_WAIT_1·FIN_WAIT_2·CLOSE_WAIT·LAST_ACK·TIME_WAIT·CLOSING의 정리 중 무리입니다.",
        "이름 전체보다 어느 단계의 역할인지 기억합니다. 자세한 전이는 상태도에서 찾아봅니다.", 1),
    "l27-daily-hangup-step-by-step": ("끊는 순서를 처음부터 끝까지",
        "내가 먼저 “저는 다 했어요”, 상대가 “알겠어요”, 상대가 “저도 끝났어요”, 내가 “알겠어요” 하고 말하는 네 마디가 오가며 양쪽 상태가 바뀌고, 마지막에는 내가 잠깐 더 들고 있다가 정리됩니다.",
        "내가 먼저 끊는 흔한 예에서 네 마디가 오가며 상태가 바뀝니다."),
    "l27-fin-ack-steps": ("FIN과 ACK 네 단계",
        "클라이언트가 FIN을 보내 FIN_WAIT_1, 서버가 ACK를 보내 CLOSE_WAIT, 서버가 FIN을 보내 LAST_ACK, 클라이언트가 ACK를 보내 서버가 CLOSED가 되는 순서입니다. 클라이언트는 TIME_WAIT 대기 뒤 CLOSED가 됩니다.",
        "흔한 종료 순서입니다. 실제로는 ACK와 FIN이 한 세그먼트에 함께 실릴 수도 있습니다.", 4),
    "l27-daily-three-to-remember": ("끊는 일에서 기억할 세 가지",
        "카드 세 장이 차례로 나타납니다. 한쪽이 먼저 끝내고, 상대도 남은 말을 마치고 끝내며, 먼저 끝낸 쪽이 마지막에 잠깐 기다린다는 내용입니다.",
        "먼저 끊은 쪽이 마지막에 잠깐 기다립니다."),
    "l27-close-three-points": ("연결 종료에서 기억할 세 가지",
        "카드 세 장이 차례로 나타납니다. 한쪽이 FIN으로 자기 송신을 끝내고, 상대가 남은 송신을 마친 뒤 자기 FIN을 보내며, 먼저 FIN을 보낸 쪽이 TIME_WAIT에서 기다린다는 내용입니다.",
        "TIME_WAIT는 먼저 FIN을 보낸 쪽에 남습니다. 서버가 먼저 FIN을 보냈다면 서버 쪽입니다.", 2),
}

OLD = {
    "l27-tcp-four-way-close": ("연결을 끝내는 네 번의 메시지",
        "클라이언트가 FIN 1000을 보내고 서버가 ACK 1001로 답하는 첫 쌍, 서버가 FIN 5000을 보내고 클라이언트가 ACK 5001로 답하는 둘째 쌍이 차례로 오가며 두 쌍, 네 번의 메시지가 됩니다. 두 컴퓨터의 상태 이름도 단계마다 바뀝니다.",
        "FIN과 ACK가 이쪽에서 한 쌍, 저쪽에서 한 쌍 오가 네 번의 메시지가 됩니다."),
    "l27-time-wait-socket-slot": ("끊었다고 바로 빈칸이 되지는 않습니다",
        "연결 상태 칸 100개가 모두 차 있고, 내 연결의 칸은 끊은 뒤에도 TIME_WAIT 동안 남아 있다가 CLOSED가 되면 정리되어 99가 되며 새 연결이 그 자리에 기록될 수 있습니다.",
        "TIME_WAIT 동안에는 연결 상태 기록이 남아 있고, 정리된 뒤에 새 연결이 그 자리를 쓸 수 있습니다. 칸 100개는 설명용 비유입니다."),
}


def build_pages():
    pages = []
    for dn, nn, fn, after in PAGES:
        daily_fn = fn if fn.__code__.co_argcount == 0 else (lambda f=fn: f(True))
        write(OUT, dn, daily_fn())
        items = [(dn, *COPY[dn], -1)]
        if nn in OLD:
            items.append((nn, *OLD[nn], after))
        else:
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
