#!/usr/bin/env python3
"""Unit 4 Lesson 6 paired SVGs (a file download, end to end). Run from the repo root:
python3 scripts/svg_pairs/u4_l06.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/06-*"))
OUT = LESSON / "assets" / "animations"
CYAN = "#4dd0e1"


def dur(daily, n=4):
    return round(n * (3.75 if daily else 4))


def cell(x, y, w, h, label, c, fs=16, fill=PANEL):
    return box(x, y, w, h, c, fill, 6, sw=3) + text(x + w / 2, y + h / 2 + fs * 0.36, label, fs, c, 700)


def hl(x, y, w, h, c=ORANGE, rx=10):
    return box(x - 4, y - 4, w + 8, h + 8, c, "none", rx, sw=5)


def arrow(x0, x1, y, c, w=8):
    d = 1 if x1 > x0 else -1
    return (line(x0, y, x1 - d * 18, y, c, w) + f'<polygon points="{x1},{y} {x1 - d * 26},{y - w - 7} {x1 - d * 26},{y + w + 7}" fill="{c}"/>')


def varrow(x, y0, y1, c, w=5):
    d = 1 if y1 > y0 else -1
    return (line(x, y0, x, y1 - d * 12, c, w) + f'<polygon points="{x},{y1} {x - 9},{y1 - d * 16} {x + 9},{y1 - d * 16}" fill="{c}"/>')


# ---------- Page 1: the whole map, walked step by step ----------
def page1(daily):
    a = Anim(4, dur(daily))
    item = parcel if daily else packet
    left = (["발송 담당자", "접수 창구", "포장 (나눠 담기)", "송장 붙이기", "트럭에 싣기"] if daily else
            ["서버 프로그램", "소켓 · 송신 버퍼", "TCP · 세그먼트", "IP · 패킷", "링크 · 프레임"])
    right = (["집주인 (꺼내 읽기)", "도착지 보관함", "포장 풀기", "송장 확인", "도착한 트럭"] if daily else
             ["브라우저 프로그램", "소켓 · 수신 버퍼", "TCP · 바이트 흐름", "IP · 패킷 처리", "링크 · 프레임 처리"])
    LX, RX, W, H = 60, 570, 330, 44
    ry = lambda i: 120 + 54 * i
    row = lambda x, i, lab, c=LINE, tc=MUTED: box(x, ry(i), W, H, c, PANEL, 10, sw=2) + text(x + W / 2, ry(i) + 29, lab, 19, tc, 700)
    net = box(390, 394, 180, 50, LINE, PANEL, 10, sw=2) + text(480, 426, "물류센터와 도로" if daily else "스위치 · 라우터 · 링크", 17 if not daily else 19, MUTED, 700)
    cx_l, cx_r = LX + 26, RX + W - 26
    body = ["".join(row(LX, i, left[i]) + row(RX, i, right[i]) for i in range(5)), net,
            line(cx_l, ry(4) + H, cx_l, 419, LINE, 3), line(cx_l, 419, 390, 419, LINE, 3),
            line(570, 419, cx_r, 419, LINE, 3), line(cx_r, 419, cx_r, ry(4) + H, LINE, 3),
            line(cx_l, ry(0) + H, cx_l, ry(1), LINE, 3)]
    on = lambda x, i, lab, c: box(x, ry(i), W, H, c, PANEL, 10, sw=4) + text(x + W / 2, ry(i) + 29, lab, 19, c, 700)
    body += [a.vis(on(LX, 0, left[0], GREEN) + on(LX, 1, left[1], GREEN), 1, 1),
             a.vis("".join(on(LX, i, left[i], BLUE) for i in (2, 3, 4)), 2, 2),
             a.vis(box(390, 394, 180, 50, VIOLET, PANEL, 10, sw=4) + text(480, 426, "물류센터와 도로" if daily else "스위치 · 라우터 · 링크", 17 if not daily else 19, VIOLET, 700), 3, 3),
             a.vis("".join(on(RX, i, right[i], GREEN) for i in range(5)) + text(480, 240, "도착" if not daily else "보관함에 도착", 20, TXT, 700)
                   + text(480, 272, "≠", 30, ORANGE, 700) + text(480, 304, "읽음" if not daily else "꺼내 읽음", 20, TXT, 700), 4, 4),
             a.vis(a.move(item(), [(cx_l, ry(0) + 22), (cx_l, ry(1) + 22)], 1, 0.15, 0.8), 1, 1),
             a.vis(a.move(item(), [(cx_l, ry(1) + 22), (cx_l, ry(4) + 22)], 2, 0.1, 0.85), 2, 2),
             a.vis(a.move(item(), [(cx_l, ry(4) + 22), (cx_l, 419), (480, 419), (cx_r, 419), (cx_r, ry(4) + 22)], 3, 0.05, 0.9), 3, 3),
             a.vis(a.move(item(), [(cx_r, ry(4) + 22), (cx_r, ry(0) + 22)], 4, 0.1, 0.85), 4, 4)]
    if daily:
        t, sub = "책 한 권이 오가는 전체 길", "발송 담당자에서 집주인까지"
        caps = ["발송 담당자가 책을 꺼내 접수 창구에 맡겨요", "포장하고 송장을 붙여 트럭에 실어요",
                "물류센터와 도로가 도착지까지 날라요", "보관함에 도착해도, 집주인이 꺼내 읽어야 끝나요"]
    else:
        t, sub = "서버 프로그램에서 브라우저까지", "파일 하나가 오가는 전체 지도를 따라가요"
        caps = ["서버 프로그램이 읽은 바이트를 소켓에 맡겨요", "TCP가 나누고, IP와 링크가 포장해요",
                "스위치와 라우터가 구간마다 다음으로 넘겨요", "수신 버퍼에 도착한 뒤 브라우저가 읽어요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2A: sender / receiver is a direction ----------
def page2a(daily):
    a = Anim(4, dur(daily))
    me = house(110, 290, "내 집") if daily else laptop(110, 290, "내 PC")
    sv = house(850, 290, "서점") if daily else pc(850, 290, "서버")
    pillS = lambda x, lab, c: pill(x, 190, lab, c, 18, True)
    send, recv = "송신 측", "수신 측"
    big = ("책", "주문서") if daily else ("사진 데이터", "요청")
    mid = ("접수소", "물류센터", "물류센터", "접수소") if daily else ("스위치", "라우터", "라우터", "스위치")
    nodes = ""
    for k, x in enumerate((290, 410, 550, 670)):
        nodes += (switch if (k in (0, 3) and not daily) else (booth if k in (0, 3) else (router if not daily else warehouse)))(x, 320, mid[k])
    body = [me, sv,
            a.vis(arrow(770, 190, 290, BLUE, 9) + pillS(850, send, ORANGE) + pillS(110, recv, GREEN)
                  + text(480, 250, "서점 → 내 집: " + big[0] if daily else "서버 → 내 PC: " + big[0], 21, BLUE, 700), 1, 1),
            a.vis(arrow(190, 770, 290, BLUE, 9) + pillS(110, send, ORANGE) + pillS(850, recv, GREEN)
                  + text(480, 250, "내 집 → 서점: 보내는 책" if daily else "내 PC → 서버: 업로드", 21, BLUE, 700), 2, 2),
            a.vis(arrow(190, 770, 255, GREEN, 4) + text(480, 232, f"짧은 {big[1]}", 19, GREEN, 700)
                  + arrow(770, 190, 330, BLUE, 10) + text(480, 372, big[0], 21, BLUE, 700)
                  + pill(110, 190, "보내기도 받기도", MUTED, 17) + pill(850, 190, "보내기도 받기도", MUTED, 17), 3, 3),
            a.vis(line(190, 340, 770, 340, LINE, 3) + nodes + text(480, 420, "접수소는 같은 구간 안, 물류센터는 구간 사이" if daily else "스위치는 링크 안, 라우터는 네트워크 사이", 20, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "보내는 쪽과 받는 쪽은 방향이에요", "고정된 직업이 아니라 지금 따라가는 짐의 방향"
        caps = ["서점이 책을 보내면 서점이 보내는 쪽이에요", "내가 책을 보내면 내가 보내는 쪽이에요",
                "주문서는 내 집이, 책은 서점이 보내요", "중간에는 여러 접수소와 물류센터가 있어요"]
    else:
        t, sub = "송신 측과 수신 측은 방향이에요", "장비에 붙은 직업이 아니라, 지금 따라가는 데이터의 방향"
        caps = ["사진을 내려받을 때 서버가 송신 측이에요", "사진을 올릴 때는 PC가 송신 측이에요",
                "요청은 PC가, 사진은 서버가 보내요", "중간의 스위치와 라우터가 구간마다 전달해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2B: why a big file is split (3,000B example) ----------
def page2b(daily):
    a = Anim(4, dur(daily))
    big = "전집 30kg" if daily else "3,000B"
    pcs = ("14.6", "14.6", "0.8") if daily else ("1,460", "1,460", "80")
    unit = "kg" if daily else "B"
    gate = (box(410, 205, 150, 130, ORANGE, "none", 10, dash=True, sw=3) + line(410, 205, 410, 335, ORANGE, 6) + line(560, 205, 560, 335, ORANGE, 6))
    bigb = cell(70, 245, 230, 60, big, GREEN, 24)
    mini = "".join(box(130 + i * 34, 250, 28, 50, [GREEN, BLUE][i % 2], PANEL, 4, sw=2) for i in range(20))
    pieces = "".join(cell(x, 245, w, 60, p + unit, GREEN, 18) for (x, w), p in zip(((590, 120), (722, 120), (854, 56)), pcs))
    body = [a.vis(gate + text(485, 190, "상자 한 개: 14.6kg까지" if daily else "한 번에 TCP 데이터 1,460B까지", 20, ORANGE, 700), 1, 3),
            a.vis(bigb + cross(485, 270) + text(485, 372, "한 번에는 안 들어가요", 21, RED, 700), 1, 1),
            a.vis(bigb + text(485, 372, "14.6 = 15 − 0.2 − 0.2" if daily else "1,460 = 1,500 − 20 − 20", 22, ORANGE, 700), 2, 2),
            a.vis(cell(70, 245, 230, 60, "전집 30kg" if daily else "3,000B", MUTED, 24, BG) + pieces + arrow(300, 410, 275, BLUE, 5)
                  + text(750, 372, "마지막 조각은 짧아요", 21, BLUE, 700), 3, 3),
            a.vis(mini + text(480, 345, "…", 34, TXT, 700) + text(480, 400, "큰 파일은 수많은 작은 조각이 돼요" if not daily else "큰 짐은 수많은 상자가 돼요", 22, BLUE, 700), 4, 4)]
    if daily:
        t, sub = "큰 짐은 상자 한도에 맞춰 나눈다", "한도 14.6kg짜리 상자 여러 개에 나눠 담아요"
        caps = ["전집 30kg은 상자 한 개에 안 들어가요", "상자 한 개에는 물건을 14.6kg까지 담을 수 있어요",
                "14.6kg, 14.6kg, 0.8kg 세 상자로 나눠요", "큰 짐일수록 상자가 아주 많아져요"]
    else:
        t, sub = "큰 데이터를 나누는 이유", "기본 IPv4·TCP 헤더 20B씩, 옵션이 없는 예"
        caps = ["3,000B는 한 번에 보내기에 커요", "MTU 1,500B에서 헤더 40B를 빼면 1,460B예요",
                "1,460B, 1,460B, 80B 세 세그먼트로 나눠요", "큰 사진은 수많은 세그먼트가 돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: process / socket / kernel on both hosts ----------
def page3(daily):
    a = Anim(4, dur(daily))
    item = parcel if daily else packet
    pcn = ("직원 가", "직원 나", "직원 다") if daily else ("브라우저", "메신저", "게임")
    svn = "발송 담당자" if daily else "웹 서버 프로세스"
    sk = "창구" if daily else "소켓"
    kn = "우체국 작업장" if daily else "커널 · TCP/IP"
    host = lambda x, w, ttl: box(x, 150, w, 235, MUTED, PANEL, 14, sw=3) + text(x + w / 2, 176, ttl, 18, MUTED, 700)
    pcx = (95, 205, 315)
    procs_pc = "".join(box(x - 45, 190, 90, 40, BLUE, BG, 8, sw=2) + text(x, 216, pcn[i], 16 if not daily else 17, TXT, 700) for i, x in enumerate(pcx))
    socks_pc = "".join(box(x - 28, 252, 56, 34, GREEN, BG, 6, sw=2) + text(x, 275, sk, 14, GREEN, 700) for x in pcx)
    kern = lambda x, w: box(x, 318, w, 50, VIOLET, BG, 8, sw=2) + text(x + w / 2, 349, kn, 17, VIOLET, 700)
    procs_sv = box(645, 190, 210, 40, BLUE, BG, 8, sw=2) + text(750, 216, svn, 17, TXT, 700)
    socks_sv = box(722, 252, 56, 34, GREEN, BG, 6, sw=2) + text(750, 275, sk, 14, GREEN, 700)
    body = [host(40, 350, "내 PC" if not daily else "집주인의 집"), host(570, 350, "서버" if not daily else "서점"),
            procs_pc + socks_pc + kern(60, 310), procs_sv + socks_sv + kern(590, 310),
            line(370, 343, 590, 343, LINE, 4) + text(480, 322, "네트워크" if not daily else "도로", 17, MUTED, 700),
            a.vis("".join(hl(x - 45, 190, 90, 40, ORANGE, 8) for x in pcx) + hl(645, 190, 210, 40, ORANGE, 8)
                  + pill(480, 130, "프로세스 = 실행 중인 프로그램" if not daily else "직원 = 일하는 사람", ORANGE, 17, True), 1, 1),
            a.vis("".join(hl(x - 28, 252, 56, 34, GREEN, 6) for x in pcx) + hl(722, 252, 56, 34, GREEN, 6)
                  + pill(480, 130, "소켓 = 맡기고 받는 접점" if not daily else "창구 = 맡기고 받는 곳", GREEN, 17, True), 2, 2),
            a.vis(hl(60, 318, 310, 50, VIOLET, 10) + hl(590, 318, 310, 50, VIOLET, 10)
                  + pill(480, 130, "커널 = TCP/IP 처리와 장치 사용" if not daily else "작업장 = 포장과 운송", VIOLET, 17, True), 3, 3),
            a.vis(a.move(item(), [(750, 210), (750, 269), (750, 343), (480, 343), (205, 343), (205, 301)], 4, 0.05, 0.9)
                  + pill(750, 410, "send: 보내 달라고 요청" if not daily else "맡기기", BLUE, 16)
                  + pill(205, 410, "recv: 읽어야 받아요" if not daily else "꺼내 읽기", GREEN, 16), 4, 4)]
    if daily:
        t, sub = "직원은 창구에 맡기고, 작업장이 나른다", "건물에 도착해도 누구에게 줄지는 따로 정해요"
        caps = ["건물 안에서는 직원이 일해요", "직원은 창구에 짐을 맡기고 받아요",
                "포장과 운송은 우체국 작업장이 맡아요", "맡겼다고 상대가 읽은 건 아니에요"]
    else:
        t, sub = "프로세스는 소켓에 맡기고, 커널이 나른다", "서버와 PC 모두 같은 구조예요"
        caps = ["통신하는 쪽은 실행 중인 프로세스예요", "프로세스는 소켓으로 데이터를 맡기고 받아요",
                "TCP/IP 처리는 커널이 맡아요", "소켓에 맡겼다고 상대가 읽은 건 아니에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: program buffer vs send buffer ----------
def page4(daily):
    a = Anim(4, dur(daily))
    names = (("창고", "작업대", "접수 창구", "발송 선반", "포장 담당") if daily else
             ("저장장치", "프로그램 버퍼", "소켓", "송신 버퍼", "TCP"))
    st = box(40, 190, 140, 120, MUTED, PANEL, 10, sw=3) + text(110, 238, names[0], 19, TXT, 700) + text(110, 266, "전집 원본" if daily else "photo.bmp", 17, MUTED, 700)
    pb = box(235, 190, 150, 120, ORANGE, PANEL, 10, sw=3) + text(310, 178, names[1], 17, ORANGE, 700)
    sock = box(430, 215, 70, 70, GREEN, PANEL, 10, sw=3) + text(465, 256, names[2], 15, GREEN, 700)
    sb = box(545, 190, 180, 120, BLUE, PANEL, 10, sw=3) + text(635, 178, names[3], 17, BLUE, 700)
    tcp = box(775, 190, 125, 120, VIOLET, PANEL, 10, sw=3) + text(837, 256, names[4], 19, VIOLET, 700)
    links = line(180, 250, 235, 250, LINE, 3) + line(385, 250, 430, 250, LINE, 3) + line(500, 250, 545, 250, LINE, 3) + line(725, 250, 775, 250, LINE, 3)
    blk = lambda x, y, w, c, lab: box(x, y, w, 36, c, c, 6, sw=1) + text(x + w / 2, y + 25, lab, 16, BG, 700)
    one = "한 더미" if daily else "4,096B"
    body = [st + pb + sock + sb + tcp + links,
            a.vis(blk(250, 232, 120, ORANGE, one) + text(110, 340, "원본은 그대로 남아요", 19, MUTED, 700), 1, 1),
            a.vis(blk(560, 232, 150, BLUE, one) + text(310, 340, "작업대는 다시 비워져요" if daily else "프로그램은 다음 바이트를 읽어요", 19, MUTED, 700)
                  + varrow(465, 300, 300, BG), 2, 2),
            a.vis(blk(250, 232, 120, ORANGE, "다음 " + one) + blk(560, 232, 150, BLUE, one), 3, 3),
            a.vis(blk(250, 232, 120, ORANGE, "다음 " + one) + blk(560, 232, 150, BLUE, one)
                  + "".join(cell(745 + 0 * i, 0, 0, 0, "", BG) for i in range(0)), 4, 4)]
    pcs = ("14.6", "14.6", "0.8") if daily else ("1,460", "1,460", "1,176")
    unit = "kg" if daily else "B"
    s4 = "".join(cell(560 + i * 0, 0, 0, 0, "", BG) for i in range(0))
    seg = "".join(cell(x, 345, w, 34, p + unit, VIOLET, 15) for (x, w), p in zip(((545, 115), (670, 115), (795, 92)), pcs))
    body.append(a.vis(seg + text(480, 410, "읽은 양 ≠ 상자 한 개 한도" if daily else "읽는 양 4,096B ≠ MSS 1,460B", 22, ORANGE, 700)
                      + varrow(640, 312, 340, VIOLET), 4, 4))
    if daily:
        t, sub = "작업대와 발송 선반은 다른 공간", "한 번에 가져오는 양과 상자 한도는 별개예요"
        caps = ["창고에서 한 더미를 작업대로 가져와요", "접수 창구에 맡기면 발송 선반에 놓여요",
                "작업대는 다음 한 더미를 가져와 반복해요", "포장 담당은 상자 한도에 맞춰 더 작게 나눠요"]
    else:
        t, sub = "프로그램 버퍼와 송신 버퍼는 다르다", "버퍼는 속도가 다른 단계를 이어 주는 메모리 공간"
        caps = ["파일에서 읽은 바이트가 프로그램 버퍼에 놓여요", "소켓으로 맡기면 커널의 송신 버퍼에 쌓여요",
                "프로그램은 다음 바이트를 읽어 같은 일을 반복해요", "프로그램이 읽는 양과 MSS는 서로 별개예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: send boundaries vs. segment boundaries ----------
def page5(daily):
    a = Anim(4, dur(daily))
    u = "권" if daily else "B"
    S = 720 / 4096
    X0 = 120
    xs = lambda n: X0 + n * S
    sends = (cell(X0, 170, 2048 * S, 54, ("작업대 ①  2,048권" if daily else "send ①  2,048B"), ORANGE, 19)
             + cell(xs(2048), 170, 2048 * S, 54, ("작업대 ②  2,048권" if daily else "send ②  2,048B"), BLUE, 19))
    one = cell(X0, 170, 4096 * S, 54, "발송 선반에 이어진 책 더미 4,096권" if daily else "송신 버퍼의 이어진 바이트 흐름 4,096B", GREEN, 19)
    cuts = "".join(line(xs(n), 150, xs(n), 330, ORANGE, 3, "6 5") for n in (1460, 2920))
    px = [X0 - 10, X0 + 1460 * S + 2, X0 + 2920 * S + 14]
    pw = [1460 * S, 1460 * S, 1176 * S]
    lab = [("A", "1,460"), ("B", "1,460"), ("C", "1,176")]
    pcs = "".join(box(px[i], 270, pw[i], 54, GREEN, PANEL, 6, sw=3) + text(px[i] + 12, 304, f"{lab[i][0]}  {lab[i][1]}{u}", 18, GREEN, 700, "start") for i in range(3))
    hdr = "".join(pill(px[i] + 38, 250, "송장" if daily else "TCP 헤더", ORANGE, 14, True) for i in range(3))
    body = [a.vis(sends, 1, 1), a.vis(one, 2, 2), a.vis(box(X0, 170, 4096 * S, 54, MUTED, PANEL, 6, sw=3) + text(X0 + 12, 204, "4,096권" if daily else "4,096B", 19, MUTED, 700, "start") + cuts, 3, 3),
            a.vis(pcs + text(480, 355, "A·B·C는 조각 이름표예요 (실제 순서 번호 아님)", 18, MUTED, 700), 3, 3),
            a.vis(line(xs(2048), 150, xs(2048), 345, BLUE, 3, "3 4") + pcs + hdr + pill(xs(2048), 135, "맡긴 경계" if daily else "send 경계", BLUE, 15, True)
                  + text(480, 400, "맡긴 횟수 ≠ 상자 수" if daily else "send 횟수 ≠ 세그먼트 수", 24, ORANGE, 700), 4, 4)]
    if daily:
        t, sub = "작업대에서 가져온 횟수와 상자 수는 다르다", "상자는 한도에 맞춰 다시 나눠 담아요"
        caps = ["작업대에서 책을 두 번 가져왔어요", "발송 선반에서는 하나로 이어진 책 더미예요",
                "상자 한도 1,460권씩으로 다시 나눠요", "상자마다 송장이 붙고, 경계는 서로 달라요"]
    else:
        t, sub = "send 횟수와 세그먼트 수는 다르다", "TCP는 송신 버퍼의 바이트를 MSS에 맞춰 나눠요"
        caps = ["프로그램이 send를 두 번 호출했어요", "송신 버퍼에서는 이어진 바이트 흐름이에요",
                "MSS 1,460B씩으로 나누면 1,460·1,460·1,176B예요", "조각마다 TCP 헤더가 붙어 세그먼트가 돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 6: segment -> packet -> frame; a new frame per link ----------
def page6(daily):
    a = Anim(4, dur(daily))
    L = dict(fh=("트럭", 70), ip=("송장", 100), sg=("책 조각 A", 110), fc=("봉인", 60)) if daily else \
        dict(fh=("프레임", 70), ip=("IP 헤더", 100), sg=("세그먼트 A", 110), fc=("FCS", 60))
    nodes = ([house(90, 370, "서점"), warehouse(480, 370, "물류 허브"), house(870, 370, "내 집")] if daily else
             [pc(90, 370, "서버"), router(480, 370, "라우터"), laptop(870, 370, "내 PC")])
    path = line(150, 395, 440, 395, LINE, 3) + line(520, 395, 810, 395, LINE, 3) + text(295, 425, "링크 1" if not daily else "구간 1", 17, MUTED, 700) + text(665, 425, "링크 2" if not daily else "구간 2", 17, MUTED, 700)

    def unit(x0, fcol, parts):
        s = ""
        x = x0
        if "fh" in parts:
            s += cell(x, 200, 70, 64, L["fh"][0], fcol, 15)
        x += 70
        if "ip" in parts:
            s += cell(x, 200, 100, 64, L["ip"][0], BLUE, 15)
        x += 100
        s += cell(x, 200, 110, 64, L["sg"][0], GREEN, 15)
        x += 110
        if "fc" in parts:
            s += cell(x, 200, 60, 64, L["fc"][0], fcol, 15)
        return s

    u1 = 125
    u2 = 505
    names = ("IP 패킷", "프레임") if not daily else ("송장 붙은 상자", "트럭")
    body = list(nodes) + [path,
            a.vis(unit(u1, VIOLET, ()) + pill(u1 + 195, 170, "내용물: TCP 세그먼트" if not daily else "내용물: 책 조각", GREEN, 16, True), 1, 1),
            a.vis(unit(u1, VIOLET, ("ip",)) + pill(u1 + 195, 170, names[0], BLUE, 17, True)
                  + text(u1 + 165, 305, "203.0.113.5 → 198.51.100.10" if not daily else "서점 → 내 집", 17, BLUE, 700), 2, 2),
            a.vis(unit(u1, VIOLET, ("fh", "ip", "fc")) + pill(u1 + 165, 170, names[1] + " (링크 1)", VIOLET, 17, True)
                  + text(u1 + 165, 305, "203.0.113.5 → 198.51.100.10" if not daily else "서점 → 내 집", 17, BLUE, 700), 3, 3),
            a.vis(unit(u2, CYAN, ("fh", "ip", "fc")) + pill(u2 + 165, 170, names[1] + " (링크 2)", CYAN, 17, True)
                  + text(u2 + 165, 305, "203.0.113.5 → 198.51.100.10" if not daily else "서점 → 내 집", 17, BLUE, 700)
                  + text(480, 330, "상자(주소)는 그대로, 트럭(구간)만 새로" if daily else "IP 패킷(주소)은 그대로, 프레임만 새로", 20, TXT, 700), 4, 4)]
    if daily:
        t, sub = "상자는 그대로, 트럭은 구간마다 바뀐다", "허브에서 상자를 내려 다음 구간 트럭에 실어요"
        caps = ["책 조각 하나가 내용물이에요", "송장을 붙이면 상자가 돼요",
                "상자를 구간 1 트럭에 실어요", "허브가 상자를 구간 2 트럭에 옮겨 실어요"]
    else:
        t, sub = "세그먼트는 패킷에, 패킷은 프레임에", "라우터는 링크마다 새 프레임에 패킷을 담아요"
        caps = ["TCP 세그먼트 A가 내용물이에요", "IP 헤더를 붙이면 IP 패킷이에요",
                "링크 1용 프레임에 패킷을 실어요", "라우터가 링크 2용 새 프레임에 다시 담아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 7: peel from the outside, floor by floor ----------
def page7(daily):
    a = Anim(4, dur(daily))
    c = dict(fh=("트럭", 110), ip=("송장", 110), tcp=("조각 라벨", 110), data=("책 조각", 120), fc=("봉인", 70)) if daily else \
        dict(fh=("프레임 헤더", 110), ip=("IP 헤더", 110), tcp=("TCP 헤더", 110), data=("사진 일부 바이트", 120), fc=("FCS", 70))
    floors = (["보관함", "포장 풀기", "송장 확인", "트럭 도착"] if daily else ["소켓", "TCP 계층", "IP 계층", "링크 계층"])
    ys = [135, 215, 295, 375]
    X = dict(fh=370, ip=480, tcp=590, data=700, fc=820)
    keys = [["data"], ["tcp", "data"], ["ip", "tcp", "data"], ["fh", "ip", "tcp", "data", "fc"]]  # floor 0..3 from top
    col = dict(fh=VIOLET, ip=BLUE, tcp=ORANGE, data=GREEN, fc=VIOLET)

    def bar(fl, hi=None):
        y = ys[fl]
        s = box(40, y, 250, 50, LINE, PANEL, 10, sw=2) + text(165, y + 32, floors[fl], 20, TXT, 700)
        for k in keys[fl]:
            s += cell(X[k], y, c[k][1], 50, c[k][0], col[k], 15)
        if hi:
            lo = min(X[k] for k in hi)
            hi_r = max(X[k] + c[k][1] for k in hi)
            s += box(lo - 4, y - 4, hi_r - lo + 8, 58, ORANGE, "none", 10, sw=5)
        return s

    ghost = "".join(f'<g opacity="0.3">{box(40, ys[f], 250, 50, LINE, PANEL, 10, sw=2)}{text(165, ys[f] + 32, floors[f], 20, TXT, 700)}</g>' for f in range(4))
    body = [ghost, a.vis(bar(3, ["fh", "fc"]), 1, 1), a.vis(bar(3), 2, 4),
            a.vis(bar(2, ["ip"]) + varrow(165, ys[3] - 4, ys[2] + 54, GREEN), 2, 2), a.vis(bar(2), 3, 4),
            a.vis(bar(1, ["tcp"]) + varrow(165, ys[2] - 4, ys[1] + 54, GREEN), 3, 3), a.vis(bar(1), 4, 4),
            a.vis(bar(0, ["data"]) + varrow(165, ys[1] - 4, ys[0] + 54, GREEN), 4, 4)]
    notes = (["마지막 구간 트럭의 라벨과 봉인을 확인해요", "송장의 목적지를 확인해요", "조각 라벨로 어느 창구 짐인지 가려요", "책 조각이 보관함에 준비돼요 — 읽는 건 집주인 몫"] if daily else
             ["마지막 링크의 프레임 헤더와 FCS를 처리해요", "IP 헤더의 목적지를 확인해요", "TCP 헤더로 어느 소켓의 데이터인지 가려요", "바이트가 소켓에 준비돼요 — 사진으로 해석하는 건 브라우저 몫"])
    for i, n in enumerate(notes, 1):
        body.append(a.vis(text(480, 452, n, 20, ORANGE if i < 4 else GREEN, 700), i, i))
    if daily:
        t, sub = "집 앞에 온 상자를 바깥부터 푼다", "트럭 → 송장 → 조각 라벨 → 책 조각 순서예요"
        caps = ["트럭이 도착하면 라벨과 봉인부터 확인해요", "상자를 내리고 송장을 확인해요",
                "조각 라벨을 보고 맞는 창구로 보내요", "책 조각이 보관함에 준비돼요"]
    else:
        t, sub = "바깥 헤더부터 처리해 바이트를 꺼낸다", "프레임 → IP 패킷 → TCP 세그먼트 → 소켓의 바이트"
        caps = ["링크 계층이 프레임을 처리해 패킷을 올려요", "IP 계층이 목적지를 확인해 세그먼트를 올려요",
                "TCP가 연결 정보로 소켓을 가리고 바이트를 줘요", "소켓에 읽을 바이트가 준비돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 8: receive buffer fills and drains ----------
def page8(daily):
    a = Anim(4, dur(daily))
    TX, TW = 330, 360
    tank = box(TX, 210, TW, 80, BLUE, PANEL, 10, sw=4)
    fill = lambda w, c=BLUE: f'<rect x="{TX + 4}" y="214" width="{w}" height="72" rx="6" fill="{c}" fill-opacity=".75"/>' if w else ""
    src = box(60, 215, 150, 70, VIOLET, PANEL, 10, sw=3) + text(135, 258, "도착한 트럭" if daily else "TCP", 20, VIOLET, 700)
    rd = box(790, 215, 130, 70, GREEN, PANEL, 10, sw=3) + text(855, 258, "집주인" if daily else "브라우저", 20, GREEN, 700)
    ttl = text(TX + TW / 2, 196, "택배 보관함" if daily else "수신 버퍼", 20, BLUE, 700)
    own = box(790, 320, 130, 54, MUTED, PANEL, 8, dash=True, sw=2) + text(855, 345, "집 안에서" if daily else "브라우저 메모리", 15, MUTED, 700) + text(855, 365, "열어 보기" if daily else "해석 · 저장", 15, MUTED, 700)
    body = [tank, src, rd, ttl,
            a.vis(text(TX + TW / 2, 330, "비어 있어요", 22, MUTED, 700), 1, 1),
            a.vis(fill(8) + arrow(210, 326, 250, VIOLET, 5) + text(TX + TW / 2, 330, "도착하면 빈 칸이 줄어요" if daily else "도착하면 남은 공간이 줄어요", 22, TXT, 700), 2, 2),
            a.vis(fill(250) + arrow(210, 326, 250, VIOLET, 7) + line(690, 250, 786, 250, LINE, 2) + text(TX + TW / 2, 330, "꺼내는 속도가 느리면 쌓여요" if daily else "읽는 속도가 느리면 쌓여요", 22, ORANGE, 700), 3, 3),
            a.vis(fill(120) + arrow(690, 786, 250, GREEN, 7) + own + varrow(855, 290, 318, MUTED)
                  + text(TX + TW / 2, 330, "꺼내 가면 여유가 생겨요" if daily else "읽어 가면 여유가 생겨요", 22, GREEN, 700), 4, 4),
            text(480, 420, "칸 너비는 단순화한 비율이에요", 17, MUTED, 700)]
    if daily:
        t, sub = "도착한 짐과 꺼내 간 짐은 다르다", "보관함이 도착과 꺼내기 사이를 이어 줘요"
        caps = ["아직 비어 있는 보관함이에요", "트럭이 짐을 넣으면 빈 칸이 줄어요",
                "집주인이 바쁘면 보관함이 차올라요", "꺼내 가면 다시 자리가 생겨요"]
    else:
        t, sub = "수신 버퍼에 도착한 일과 읽는 일", "도착한 바이트는 프로그램이 읽을 때까지 기다려요"
        caps = ["아직 비어 있는 수신 버퍼가 있어요", "데이터가 도착하면 남은 공간이 줄어요",
                "브라우저가 느리게 읽으면 쌓여요", "읽어 가면 자리가 생기고, 처리는 따로 남아요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    [("l16-daily-parcel-journey", "l16-whole-map-walk", page1)],
    [("l16-daily-direction-of-parcel", "l16-sender-receiver-direction", page2a), ("l16-daily-split-heavy-load", "l16-why-split-data", page2b)],
    [("l16-daily-staff-window-workshop", "l16-process-socket-kernel", page3)],
    [("l16-daily-workbench-shelf", "l16-program-vs-send-buffer", page4)],
    [("l16-daily-pile-into-boxes", "l16-send-vs-segment-boundary", page5)],
    [("l16-daily-truck-per-leg", "l16-packet-frame-per-link", page6)],
    [("l16-daily-unload-outside-in", "l16-decapsulation-floors", page7)],
    [("l16-daily-parcel-locker", "l16-receive-buffer-fill", page8)],
]

OVERVIEW = ("assets/diagrams/l16-send-receive-overview.svg", "서버 프로그램에서 브라우저까지",
            "왼쪽 서버 프로그램에서 소켓과 송신 버퍼를 거쳐 TCP, IP, 링크 순으로 내려가고, 가운데 네트워크를 지나 오른쪽에서 링크, IP, TCP, 수신 버퍼, 브라우저 순으로 올라가는 지도.",
            "송신 쪽은 아래로 내려가며 나누고 포장한다. 수신 쪽은 위로 올라가며 포장을 처리한다. 수신 버퍼에 도착한 바이트는 브라우저가 읽어 간다.", 3)

# (daily title, alt, caption), (network title, alt, caption), after_paragraph for the network SVG.
COPY = {
    "l16-daily-parcel-journey": (
        "책 한 권이 오가는 전체 길",
        "왼쪽에 발송 담당자, 접수 창구, 포장, 송장 붙이기, 트럭에 싣기가 위에서 아래로 있고, 아래 가운데 물류센터와 도로를 지나 오른쪽의 도착한 트럭, 송장 확인, 포장 풀기, 도착지 보관함, 집주인이 아래에서 위로 이어집니다. 책이 이 길을 차례로 지나가고, 마지막에 보관함에 도착한 것과 집주인이 꺼내 읽은 것이 다르다고 표시됩니다.",
        "택배는 접수에서 도착까지 여러 단계를 지나고, 보관함에 도착해도 집주인이 꺼내 읽어야 끝납니다."),
    "l16-whole-map-walk": (
        "서버 프로그램에서 브라우저까지",
        "왼쪽에 서버 프로그램, 소켓과 송신 버퍼, TCP 세그먼트, IP 패킷, 링크 프레임이 위에서 아래로 있고, 아래 가운데 스위치·라우터·링크를 지나 오른쪽의 링크 프레임 처리, IP 패킷 처리, TCP 바이트 흐름, 소켓과 수신 버퍼, 브라우저 프로그램이 아래에서 위로 이어집니다. 데이터가 이 길을 단계별로 지나가며, 마지막에 수신 버퍼에 도착한 것과 브라우저가 읽은 것이 다르다고 표시됩니다.",
        "앞의 지도를 따라 데이터가 지나가는 순서입니다. 수신 버퍼에 도착한 바이트는 브라우저가 읽어야 쓰입니다.", 3),
    "l16-daily-direction-of-parcel": (
        "보내는 쪽과 받는 쪽은 방향이에요",
        "왼쪽 내 집과 오른쪽 서점 사이에 화살표가 나타납니다. 서점이 책을 보내면 서점이 송신 측, 내 집이 수신 측이고, 내가 책을 보내면 방향과 역할이 바뀝니다. 한 번의 주문에서는 짧은 주문서가 내 집에서, 책이 서점에서 오가고, 마지막으로 중간의 접수소와 물류센터가 구간마다 전달합니다.",
        "보내는 쪽과 받는 쪽은 고정된 직업이 아니라 지금 따라가는 짐의 방향입니다."),
    "l16-sender-receiver-direction": (
        "송신 측과 수신 측은 방향이에요",
        "왼쪽 내 PC와 오른쪽 서버 사이에 화살표가 나타납니다. 사진을 내려받을 때는 서버가 송신 측, PC가 수신 측이고, 올릴 때는 반대가 됩니다. 한 번의 다운로드에서도 짧은 요청은 PC가, 사진 데이터는 서버가 보내며, 마지막으로 중간의 스위치와 라우터가 구간마다 전달합니다.",
        "송신 측과 수신 측은 장비에 붙은 고정 직업이 아니라 데이터가 이동하는 방향입니다. 스위치는 링크 안, 라우터는 네트워크 사이의 전달을 맡습니다.", 2),
    "l16-daily-split-heavy-load": (
        "큰 짐은 상자 한도에 맞춰 나눈다",
        "전집 30kg이 한도 14.6kg짜리 상자 칸 앞에서 한 번에는 안 들어간다고 표시됩니다. 한도는 15kg에서 포장 0.2kg과 송장 0.2kg을 뺀 값이고, 전집은 14.6kg, 14.6kg, 0.8kg 세 상자로 나뉩니다. 마지막에 큰 짐은 수많은 상자가 된다는 표시가 나타납니다.",
        "큰 짐은 한 상자에 담을 수 없어 한도에 맞춰 여러 상자로 나눕니다.", 3),
    "l16-why-split-data": (
        "큰 데이터를 나누는 이유",
        "3,000B 데이터가 TCP 데이터 한도 1,460B 앞에서 한 번에는 안 들어간다고 표시됩니다. 한도는 MTU 1,500B에서 IP 헤더 20B와 TCP 헤더 20B를 뺀 값이고, 데이터는 1,460B, 1,460B, 80B 세 세그먼트로 나뉩니다. 마지막에 큰 사진은 수많은 세그먼트가 된다는 표시가 나타납니다.",
        "기본 IPv4와 TCP 헤더가 각각 20B이고 옵션이 없는 예입니다. 마지막 조각은 한도를 채우지 않아도 돼요.", 6),
    "l16-daily-staff-window-workshop": (
        "직원은 창구에 맡기고, 작업장이 나른다",
        "왼쪽 집주인의 집에는 직원 세 명과 각자의 창구, 우체국 작업장이 있고 오른쪽 서점에는 발송 담당자와 창구, 작업장이 있습니다. 직원, 창구, 작업장이 차례로 강조되고, 서점 창구에서 맡긴 짐이 작업장과 도로를 지나 집주인 쪽 창구에 도착합니다. 맡긴 것과 상대가 꺼내 읽는 것은 다르다고 표시됩니다.",
        "건물에 짐이 도착해도 누구에게 줄지는 창구가 정합니다. 맡겼다고 상대가 읽은 것은 아니에요."),
    "l16-process-socket-kernel": (
        "프로세스는 소켓에 맡기고, 커널이 나른다",
        "왼쪽 내 PC에는 브라우저, 메신저, 게임 프로세스와 각각의 소켓, 커널이 있고 오른쪽 서버에는 웹 서버 프로세스와 소켓, 커널이 있습니다. 프로세스, 소켓, 커널이 차례로 강조되고, 서버의 send 요청이 소켓과 커널, 네트워크를 지나 PC의 소켓에 도착해 브라우저가 recv로 읽어야 한다고 표시됩니다.",
        "프로세스는 소켓으로 데이터를 맡기고 받고, TCP/IP 처리는 커널이 맡습니다. send와 recv는 보내기와 받기 요청 이름이에요.", 5),
    "l16-daily-workbench-shelf": (
        "작업대와 발송 선반은 다른 공간",
        "창고, 작업대, 접수 창구, 발송 선반, 포장 담당이 한 줄로 이어져 있습니다. 창고에서 한 더미가 작업대로 오고 창구를 거쳐 발송 선반에 놓이며, 작업대는 다시 다음 한 더미를 가져옵니다. 포장 담당은 그 더미를 상자 한도에 맞춰 더 작게 나눕니다.",
        "한 번에 가져오는 양과 상자 한 개의 한도는 별개입니다."),
    "l16-program-vs-send-buffer": (
        "프로그램 버퍼와 송신 버퍼는 다르다",
        "저장장치, 프로그램 버퍼, 소켓, 송신 버퍼, TCP가 한 줄로 이어져 있습니다. photo.bmp에서 4,096B를 읽어 프로그램 버퍼에 놓고, 소켓으로 맡기면 커널의 송신 버퍼에 쌓이며, 프로그램은 다음 4,096B를 읽어 같은 일을 반복합니다. TCP는 송신 버퍼의 바이트를 1,460B, 1,460B, 1,176B로 나눕니다.",
        "4,096B는 프로그램이 이번에 읽는 양이지 MTU나 MSS가 아닙니다. 그림의 조각 크기는 예시예요.", 5),
    "l16-daily-pile-into-boxes": (
        "작업대에서 가져온 횟수와 상자 수는 다르다",
        "작업대에서 책을 2,048권씩 두 번 가져온 모습이 나타납니다. 발송 선반에서는 4,096권이 하나로 이어진 더미가 되고, 상자 한도 1,460권씩으로 나뉘어 A, B, C 세 상자가 됩니다. 상자마다 송장이 붙고, 가져온 경계와 상자의 경계가 서로 다르다고 표시됩니다.",
        "책을 가져온 횟수와 상자 수는 같지 않습니다. A·B·C는 이름표예요."),
    "l16-send-vs-segment-boundary": (
        "send 횟수와 세그먼트 수는 다르다",
        "프로그램이 send를 2,048B씩 두 번 호출한 모습이 나타납니다. 송신 버퍼에서는 4,096B가 하나로 이어진 바이트 흐름이 되고, MSS 1,460B씩으로 나뉘어 A 1,460B, B 1,460B, C 1,176B 세 조각이 됩니다. 조각마다 TCP 헤더가 붙고, send의 경계와 세그먼트의 경계가 서로 다르다고 표시됩니다.",
        "한 번의 send와 세그먼트 하나는 같은 단위가 아닙니다. A·B·C는 조각을 구별하는 이름표이고 실제 TCP 순서 번호가 아니에요.", 3),
    "l16-daily-truck-per-leg": (
        "상자는 그대로, 트럭은 구간마다 바뀐다",
        "서점에서 물류 허브를 거쳐 내 집으로 가는 길에 구간 1과 구간 2가 있습니다. 책 조각이 송장을 붙여 상자가 되고, 구간 1 트럭에 실립니다. 허브에서 상자를 내려 구간 2의 새 트럭에 옮겨 싣는데, 상자의 주소는 그대로이고 트럭만 바뀝니다.",
        "상자는 목적지로 가는 단위이고, 트럭은 구간마다 상자를 나르는 단위입니다."),
    "l16-packet-frame-per-link": (
        "세그먼트는 패킷에, 패킷은 프레임에",
        "서버에서 라우터를 거쳐 내 PC로 가는 길에 링크 1과 링크 2가 있습니다. 세그먼트 A에 IP 헤더가 붙어 IP 패킷이 되고 링크 1용 프레임에 실립니다. 라우터가 패킷을 꺼내 링크 2용 새 프레임에 다시 담는데, IP 주소는 그대로이고 프레임만 새로 만들어집니다.",
        "NAT 같은 주소 변환이 없는 예입니다. IP 패킷의 주소는 유지되고, 프레임은 링크마다 달라집니다. 그림의 IP 주소는 설명용 예시예요.", 5),
    "l16-daily-unload-outside-in": (
        "집 앞에 온 상자를 바깥부터 푼다",
        "아래에서 위로 트럭 도착, 송장 확인, 포장 풀기, 보관함 층이 차례로 나타납니다. 트럭의 라벨과 봉인을 확인하면 송장 붙은 상자가 올라오고, 송장을 확인하면 조각 라벨이 붙은 상자가, 조각 라벨을 확인하면 책 조각이 보관함에 준비됩니다. 책을 읽는 일은 집주인 몫이라고 표시됩니다.",
        "바깥 라벨부터 처리하며 안쪽으로 들어가고, 마지막에 책 조각이 보관함에 준비됩니다."),
    "l16-decapsulation-floors": (
        "바깥 헤더부터 처리해 바이트를 꺼낸다",
        "아래에서 위로 링크 계층, IP 계층, TCP 계층, 소켓 층이 차례로 나타납니다. 링크 계층이 프레임 헤더와 FCS를 처리하면 IP 패킷이, IP 헤더를 확인하면 TCP 세그먼트가, TCP 헤더를 확인하면 사진의 일부 바이트가 소켓에 준비됩니다. 사진으로 해석하는 일은 브라우저 몫이라고 표시됩니다.",
        "각 계층은 자기 계층의 헤더를 처리하고 안쪽 단위를 올립니다. 헤더를 처리하는 일은 사진을 해석하는 일이 아니에요.", 3),
    "l16-daily-parcel-locker": (
        "도착한 짐과 꺼내 간 짐은 다르다",
        "도착한 트럭과 택배 보관함, 집주인이 한 줄로 있습니다. 비어 있던 보관함에 트럭이 짐을 넣으면 빈 칸이 줄고, 집주인이 바쁘면 보관함이 차오르며, 집주인이 꺼내 가면 다시 자리가 생깁니다. 꺼낸 뒤에도 집 안에서 열어 보는 일이 남아 있다고 표시됩니다.",
        "보관함에 도착한 시각과 집주인이 꺼내 쓰는 시각은 다릅니다. 칸 너비는 단순화한 비율이에요."),
    "l16-receive-buffer-fill": (
        "수신 버퍼에 도착한 일과 읽는 일",
        "TCP, 수신 버퍼, 브라우저가 한 줄로 있습니다. 비어 있던 수신 버퍼에 데이터가 도착하면 남은 공간이 줄고, 브라우저가 느리게 읽으면 버퍼가 쌓이며, 읽어 가면 다시 여유가 생깁니다. 읽은 뒤에도 브라우저 메모리에서 해석과 저장이 남아 있다고 표시됩니다.",
        "수신 버퍼에 바이트가 도착한 일, 브라우저가 읽은 일, 읽은 내용을 처리하는 일은 서로 다른 순간입니다. 칸 너비는 단순화한 비율이에요.", 3),
}


def build_pages():
    pages = []
    for group in PAGES:
        items = []
        for dn, nn, fn in group:
            write(OUT, dn, fn(True))
            write(OUT, nn, fn(False))
            d = COPY[dn]
            n = COPY[nn]
            items.append((dn, *d, -1))
            if dn == "l16-daily-parcel-journey":
                items.append(OVERVIEW)
            items.append((nn, n[0], n[1], n[2], n[3]))
        pages.append(items)
    return pages


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = build_pages()
    if "--svg-only" not in sys.argv:
        # page 2 pair B: its daily SVG sits right after the "### 파일 하나를 한 번에 보내면 안 될까?" heading
        pages[1][2] = pages[1][2][:4] + (3,)
        wire_items(LESSON / "lesson.md", pages)
    print("ok", sum(len(p) for p in pages), "items")
