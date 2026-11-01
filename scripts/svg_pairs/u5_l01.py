#!/usr/bin/env python3
"""Unit 5 Lesson 1 paired SVGs (IP header). Run from the repo root:
python3 scripts/svg_pairs/u5_l01.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/07-*"))
OUT = LESSON / "assets" / "animations"


def dur(daily, n=4):
    return round(n * (3.75 if daily else 4))


def cell(x, y, w, h, label, c, fs=16, fill=PANEL):
    return box(x, y, w, h, c, fill, 6, sw=3) + text(x + w / 2, y + h / 2 + fs * 0.36, label, fs, c, 700)


def brace(x0, x1, y, c, label, fs=18):
    return (line(x0, y, x1, y, c, 4) + line(x0, y, x0, y + 12, c, 4) + line(x1, y, x1, y + 12, c, 4)
            + pill((x0 + x1) / 2, y - 26, label, c, fs, True))


# ---------- Page 1: header (front part) + payload ----------
def page1(daily):
    a = Anim(4, dur(daily))
    X0, XM, X1, Y, H = 110, 390, 850, 190, 100
    hdr, pay = ("송장 (앞부분)", "내용물 (뒤에 실린 것)") if daily else ("IP 헤더 (앞부분)", "페이로드 (뒤에 실린 데이터)")
    chips = (["받는 곳", "내용물 종류", "더 거칠 수 있는 횟수", "나눠 보낼 때 참고"] if daily else
             ["목적지 주소", "다음에 올 프로토콜", "전달 범위 제한 (TTL)", "나눠 보낼 때 참고"])
    cx = [174, 378, 582, 786]
    base = box(X0, Y, X1 - X0, H, MUTED, PANEL, 8, sw=3)
    one = text(480, Y + 60, "택배 상자 하나" if daily else "IP 패킷 하나", 26, TXT, 700)
    parts = (box(X0, Y, XM - X0, H, ORANGE, PANEL, 8, sw=3) + text((X0 + XM) / 2, Y + 60, hdr, 22, ORANGE, 700)
             + box(XM, Y, X1 - XM, H, GREEN, PANEL, 8, sw=3) + text((XM + X1) / 2, Y + 60, pay, 22, GREEN, 700))
    drops = line(250, Y + H, 250, 322, ORANGE, 3) + line(cx[0], 322, cx[3], 322, ORANGE, 3) \
        + "".join(line(c, 322, c, 345, ORANGE, 3) for c in cx)
    chip = "".join(cell(c - 95, 345, 190, 54, t, ORANGE, 16) for c, t in zip(cx, chips))
    body = [base, a.vis(one, 1, 1), a.vis(parts, 2, 4), a.vis(drops + chip, 3, 4),
            a.vis(brace(X0, X1, 160, BLUE, "상자 하나 = 송장 + 내용물" if daily else "IP 패킷 하나 = 헤더 + 페이로드"), 4, 4)]
    if daily:
        t, sub = "송장에는 받는 곳 말고도 적힌다", "상자는 송장과 내용물로 이뤄져요"
        caps = ["택배 상자 하나를 떠올려 봐요", "앞쪽엔 송장, 뒤쪽엔 내용물이 있어요",
                "송장엔 받는 곳 말고도 적혀 있어요", "송장과 내용물이 모여 상자 하나예요"]
    else:
        t, sub = "IP 헤더에는 전달 정보가 담긴다", "패킷은 헤더와 페이로드로 이뤄져요"
        caps = ["IP 패킷 하나를 떠올려 봐요", "앞부분은 IP 헤더, 뒤는 페이로드예요",
                "헤더엔 목적지 주소 말고도 담겨요", "헤더와 페이로드가 모여 패킷 하나예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: read 0x45 -> Version, IHL -> 20 bytes ----------
def page2(daily):
    a = Anim(4, dur(daily))
    c4, c5 = 400, 560
    tiles = cell(c4 - 55, 118, 110, 62, "4", BLUE, 40) + cell(c5 - 55, 118, 110, 62, "5", ORANGE, 40) \
        + text(250, 160, "첫 바이트 (16진수)" if not daily else "상자에 적힌 두 자리", 17, MUTED, 700, "end") \
        + text(690, 160, "= 45", 28, TXT, 700, "start")
    row_b = (cell(c4 - 75, 200, 150, 40, "0100" if not daily else "앞 숫자", BLUE, 22)
             + cell(c5 - 75, 200, 150, 40, "0101" if not daily else "뒤 숫자", ORANGE, 22)
             + line(c4, 180, c4, 200, BLUE, 3) + line(c5, 180, c5, 200, ORANGE, 3)
             + text(c4, 272, "Version = 4" if not daily else "양식 번호 = 4", 24, BLUE, 700)
             + text(c5, 272, "IHL = 5" if not daily else "줄 수 = 5", 24, ORANGE, 700))
    grid = "".join(box(130 + k * 70, 300 + 22 * i, 68, 20, ORANGE, PANEL, 3, sw=2) for i in range(5) for k in range(4))
    s3 = (grid + text(430, 316, "← 한 줄 = 4바이트" if not daily else "← 한 줄 = 4칸", 19, TXT, 700, "start")
          + text(560, 372, "IHL 5 = 4바이트 단위 5개" if not daily else "줄 수 5 = 4칸짜리 줄 5개", 22, ORANGE, 700, "start"))
    s4 = (text(560, 412, "5 × 4 = 20바이트" if not daily else "5 × 4 = 20칸", 32, ORANGE, 700, "start")
          + pill(760, 444, "옵션 없는 기본 헤더" if not daily else "추가 칸 없는 기본 송장", GREEN, 17, True))
    body = [a.vis(tiles, 1, 4), a.vis(row_b, 2, 4), a.vis(s3, 3, 4), a.vis(s4, 4, 4)]
    if daily:
        t, sub = "두 자리 번호로 송장 길이를 읽는다", "앞 숫자는 양식 번호, 뒤 숫자는 줄 수예요"
        caps = ["상자에 두 자리 번호 45가 적혀 있어요", "앞 숫자 4는 양식, 뒤 숫자 5는 줄 수예요",
                "송장은 4칸짜리 줄이 다섯 개예요", "그래서 송장 길이는 20칸이에요"]
    else:
        t, sub = "첫 바이트 0x45로 헤더 길이 읽기", "16진수 한 자리는 4비트, 앞은 Version, 뒤는 IHL"
        caps = ["헤더의 첫 바이트는 16진수 45예요", "4비트씩 나누면 Version 4, IHL 5예요",
                "IHL은 4바이트 단위가 몇 개인지예요", "그래서 헤더 길이는 20바이트예요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 3: Protocol (which next) + TTL (how far) ----------
def page3(daily):
    a = Anim(4, dur(daily))
    stamp = "내용물 종류: 식품" if daily else "Protocol = 6"
    doors = ["식품 창구", "서류 창구", "의류 창구"] if daily else ["TCP · 6", "UDP · 17", "ICMP · 1"]

    def panel_a(lit):
        s = box(70, 130, 270, 100, ORANGE, PANEL, 8, sw=3) + text(205, 160, "송장" if daily else "IP 헤더", 18, ORANGE, 700) \
            + pill(205, 200, stamp, ORANGE, 19, lit)
        s += line(340, 180, 590, 180, LINE, 3) + f'<polygon points="600,180 580,170 580,190" fill="{LINE}"/>'
        for i, d in enumerate(doors):
            on = lit and i == 0
            s += box(600, 124 + 48 * i, 280, 42, GREEN if on else LINE, PANEL, 8, sw=4 if on else 2) \
                + text(740, 152 + 48 * i, d, 20, GREEN if on else MUTED, 700)
        return s

    xs = [120, 330, 540, 750]
    icons = [(house(xs[0], 345) if daily else pc(xs[0], 345)),
             "".join((warehouse(x, 345, "환승센터 %d" % i) if daily else router(x, 345, "R%d" % i)) for i, x in enumerate(xs[1:], 1))]
    lane = line(xs[0], 345, xs[3], 345, LINE, 3)
    nodes = lane + icons[0] + icons[1] + text(xs[0], 345 + 66 if daily else 345 + 50, "출발" if daily else "PC", 17, MUTED)
    mids = [225, 435, 645]
    ttl = "".join(a.vis(pill(m, 296, ("한도 %d" if daily else "TTL %d") % v, GREEN, 18, True) + packet(m, 345, BLUE), s, 4)
                  for m, v, s in zip(mids, (3, 2, 1), (3.05, 3.4, 3.75)))
    dead = (pill(xs[3], 296, "한도 0" if daily else "TTL 0", RED, 18, True) + cross(xs[3] + 64, 345)
            + text(xs[3], 440, "버려져요" if daily else "폐기돼요", 19, RED, 700))
    body = [a.vis(panel_a(False), 1, 1), a.vis(panel_a(True), 2, 2), a.vis(f'<g opacity="0.3">{panel_a(True)}</g>', 3, 4),
            f'<g opacity="0.35">{nodes}</g>', a.vis(nodes, 3, 4), a.vis(ttl, 3, 4), a.vis(dead, 4, 4)]
    if daily:
        t, sub = "송장의 종류 표시와 이동 한도", "종류는 맞는 창구를, 한도는 환승 횟수를 정해요"
        caps = ["도착한 상자는 송장의 종류 표시를 봐요", "종류에 맞는 창구로 넘겨요",
                "환승센터를 지날 때마다 한도가 줄어요", "한도가 0이 되면 상자를 버려요 (예시)"]
    else:
        t, sub = "Protocol과 TTL의 역할", "Protocol은 다음에 풀 프로토콜, TTL은 전달 범위를 제한해요"
        caps = ["도착한 패킷은 Protocol 값을 먼저 봐요", "6이면 TCP로 해석해요 (17 UDP, 1 ICMP)",
                "라우터를 지날 때마다 TTL이 줄어요", "TTL이 0이 되면 폐기돼요 (예시 값)"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: Wireshark -- fields on top, raw bytes below ----------
def page4(daily):
    a = Anim(4, dur(daily))
    hexs = ["45", "00", "01", "4b", "··", "··", "··", "··", "40", "06", "··", "··",
            "c0", "00", "02", "0a", "c6", "33", "64", "07"]
    rows = [("Version", "4", "송장 양식" if daily else "IPv4", ORANGE),
            ("Header Length", "20 bytes", "송장 길이 (줄 수 × 4칸)" if daily else "IHL 5 × 4바이트", ORANGE),
            ("Total Length", "331", "송장 + 내용물" if daily else "헤더 + 페이로드", GREEN),
            ("Protocol", "6", "내용물 종류" if daily else "다음에 해석할 프로토콜 (6 = TCP)", ORANGE),
            ("TTL", "64", "더 거칠 수 있는 횟수" if daily else "전달 범위 제한", ORANGE),
            ("Source", "192.0.2.10", "보낸 곳" if daily else "출발지 IP 주소", BLUE),
            ("Destination", "198.51.100.7", "받는 곳" if daily else "목적지 IP 주소", BLUE)]
    if daily:
        rows = [(n.replace("Version", "양식").replace("Header Length", "송장 길이").replace("Total Length", "전체 크기")
                  .replace("Protocol", "종류").replace("TTL", "이동 한도").replace("Source", "보낸 곳").replace("Destination", "받는 곳"),
                 {"192.0.2.10": "A 지점", "198.51.100.7": "B 지점"}.get(v, v.replace("bytes", "칸")), nt, c) for n, v, nt, c in rows]

    def row(i, lit):
        n, v, nt, c = rows[i]
        y = 116 + 29 * i
        col = c if lit else LINE
        return (box(80, y, 800, 25, col, PANEL if not lit else BG, 5, sw=3 if lit else 1)
                + text(96, y + 19, n, 17, c if lit else MUTED, 700, "start") + text(300, y + 19, v, 17, TXT if lit else MUTED, 700, "start")
                + text(470, y + 19, nt, 17, c if lit else MUTED, 400, "start"))

    CW, X0, Y = 40, 80, 360

    def raw(lit):
        s = text(80, 350, "송장 바코드 번호 20칸 (예시)" if daily else "원시 바이트 20개 (예시)", 17, MUTED, 700, "start")
        for i, h in enumerate(hexs):
            c = LINE
            for rng, col in lit:
                if i in rng:
                    c = col
            s += cell(X0 + i * CW, Y, CW, 38, h, c, 17) if c != LINE else box(X0 + i * CW, Y, CW, 38, LINE, PANEL, 4, sw=2) + text(X0 + i * CW + CW / 2, Y + 25, h, 17, MUTED, 700)
        return s

    def tag(idx0, idx1, label, c):
        x0, x1 = X0 + idx0 * CW, X0 + (idx1 + 1) * CW
        return line(x0 + 2, 408, x1 - 2, 408, c, 3) + text((x0 + x1) / 2, 428, label, 15, c, 700)

    allrows = "".join(row(i, False) for i in range(7))
    s2 = (row(0, True) + row(1, True) + raw([(range(0, 1), ORANGE)]) + tag(0, 0, "양식 · 줄 수" if daily else "Version · IHL", ORANGE))
    s3 = (row(3, True) + row(4, True) + row(5, True) + row(6, True)
          + raw([(range(8, 9), ORANGE), (range(9, 10), ORANGE), (range(12, 16), BLUE), (range(16, 20), BLUE)])
          + tag(8, 9, "한도 · 종류" if daily else "TTL · Protocol", ORANGE) + tag(12, 15, "보낸 곳" if daily else "Source", BLUE)
          + tag(16, 19, "받는 곳" if daily else "Destination", BLUE))
    s4 = (row(2, True) + raw([(range(2, 4), GREEN)]) + tag(2, 3, "전체 크기" if daily else "Total Length", GREEN)
          + text(560, 448, "331 − 20 = 311 → " + ("내용물" if daily else "페이로드") + " (예시)", 24, GREEN, 700))
    body = [allrows, a.vis(raw([]), 1, 1), a.vis(s2, 2, 2), a.vis(s3, 3, 3), a.vis(s4, 4, 4)]
    if daily:
        t, sub = "송장 조회 화면에서 칸 찾기", "위는 풀어 쓴 칸, 아래는 원래 번호예요"
        caps = ["조회 화면은 풀이와 원래 번호를 같이 보여요", "첫 칸 45에서 양식과 줄 수를 읽어요",
                "종류, 이동 한도, 보낸 곳과 받는 곳을 찾아요", "전체 크기에서 송장 20칸을 빼면 내용물이에요"]
    else:
        t, sub = "Wireshark에서 핵심 필드 찾기", "위는 해석된 필드, 아래는 원시 바이트예요"
        caps = ["해석된 필드와 원시 바이트가 함께 보여요", "첫 바이트 45에서 Version과 IHL을 읽어요",
                "Protocol, TTL, 출발지·목적지를 찾아요", "Total Length에서 헤더 20바이트를 빼요"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    ("l17-daily-label-contents", "l17-header-payload-parts", page1),
    ("l17-daily-form-code-45", "l17-version-ihl-length", page2),
    ("l17-daily-kind-and-limit", "l17-protocol-ttl", page3),
    ("l17-daily-lookup-screen", "l17-wireshark-ip-fields", page4),
]

STATIC = ("assets/diagrams/ipv4-header-map.svg", "IPv4 패킷의 헤더와 페이로드",
          "32비트 폭의 IPv4 헤더 구조를 보여 준다. 첫 세 행에는 Version, IHL, DS 필드, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum이 있다. 다음 두 행에는 출발지와 목적지 IP 주소가 있다. Options와 Padding은 선택 항목이고, 헤더 뒤에는 페이로드가 놓인다.",
          "이 그림은 RFC 791의 IPv4 헤더 배치를 입문용으로 다시 그린 것이다. 필드 전체를 외우기보다 지금 배울 Version·IHL·Protocol·TTL이 어디 있는지 찾아보자.", 1)

# (daily copy), (network copy), after_paragraph of the network SVG
COPY = [
    (("송장에는 받는 곳 말고도 적힌다",
      "긴 상자 하나가 나타납니다. 상자의 앞쪽은 송장, 뒤쪽은 내용물로 나뉘고, 송장에서 받는 곳, 내용물 종류, 더 거칠 수 있는 횟수, 나눠 보낼 때 참고하는 정보 네 칸이 아래로 갈라져 나옵니다. 마지막에 송장과 내용물이 모여 상자 하나가 된다고 표시됩니다.",
      "택배 상자의 송장에는 받는 곳만 적힌 게 아니라 여러 안내가 함께 적힙니다."),
     ("IP 헤더에는 전달 정보가 담긴다",
      "긴 IP 패킷 하나가 나타납니다. 앞부분은 IP 헤더, 뒤쪽은 페이로드로 나뉘고, 헤더에서 목적지 주소, 다음에 올 프로토콜, 전달 범위를 제한하는 TTL, 나눠 보낼 때 참고하는 정보 네 칸이 아래로 갈라져 나옵니다. 마지막에 헤더와 페이로드가 모여 IP 패킷 하나가 된다고 표시됩니다.",
      "IP 헤더에는 목적지 주소 외에도 다음 프로토콜, 전달 범위 제한, 나눠 보낼 때 참고할 정보가 담깁니다."), 0),
    (("두 자리 번호로 송장 길이를 읽는다",
      "상자에 두 자리 번호 45가 적혀 있습니다. 앞 숫자 4는 양식 번호, 뒤 숫자 5는 줄 수로 나뉩니다. 송장은 4칸짜리 줄이 다섯 개이고, 5 곱하기 4로 송장 길이는 20칸입니다.",
      "두 자리 번호의 앞 숫자는 양식, 뒤 숫자는 줄 수입니다. 송장 길이는 줄 수에 한 줄의 칸 수를 곱해 구해요."),
     ("첫 바이트 0x45로 헤더 길이 읽기",
      "첫 바이트 16진수 45가 4와 5로 나뉘고, 각각 2진수 0100과 0101로 펼쳐집니다. 앞의 네 비트는 Version 4, 뒤의 네 비트는 IHL 5입니다. IHL 5는 4바이트 단위 다섯 줄이므로 5 곱하기 4로 헤더 길이는 20바이트이고, 옵션이 없는 기본 헤더입니다.",
      "0x45를 4비트씩 나누면 Version 4와 IHL 5를 읽을 수 있습니다. IHL은 4바이트(32비트) 단위의 개수이고, 5이면 헤더는 20바이트입니다."), 2),
    (("송장의 종류 표시와 이동 한도",
      "위쪽에서는 상자의 송장에 내용물 종류 표시가 있고, 식품 창구, 서류 창구, 의류 창구 중 맞는 식품 창구가 켜집니다. 아래쪽에서는 출발 집에서 환승센터 세 곳을 지나며 이동 한도가 3, 2, 1로 줄고, 세 번째 환승센터에서 0이 되어 상자가 버려집니다.",
      "송장의 종류 표시는 맞는 창구를 고르고, 이동 한도는 환승할 때마다 줄어 0이 되면 상자가 버려집니다. 한도 값은 예시예요."),
     ("Protocol과 TTL의 역할",
      "위쪽에서는 IP 헤더의 Protocol 값 6이 TCP 칸과 이어져 켜지고, UDP는 17, ICMP는 1입니다. 아래쪽에서는 PC에서 라우터 세 대를 지나며 TTL이 3, 2, 1로 줄고, 세 번째 라우터에서 0이 되어 패킷이 폐기됩니다.",
      "Protocol은 다음에 해석할 프로토콜을 가리키고, 포트 번호와는 다릅니다. TTL은 라우터를 지날 때마다 줄고 0이 되면 폐기돼요. 그림의 TTL 값은 예시입니다."), 1),
    (("송장 조회 화면에서 칸 찾기",
      "위쪽에는 송장 조회 화면의 풀이 줄 일곱 개(양식, 송장 길이, 전체 크기, 종류, 이동 한도, 보낸 곳, 받는 곳)가, 아래쪽에는 원래 번호 20칸이 있습니다. 첫 칸 45에서 양식과 줄 수를, 이어서 종류, 이동 한도, 보낸 곳, 받는 곳 칸을 찾고, 마지막으로 전체 크기 331에서 송장 20칸을 빼면 내용물 311이 남습니다.",
      "조회 화면은 풀어 쓴 칸과 원래 번호를 함께 보여 줍니다. 번호와 크기 값은 설명용 예시예요."),
     ("Wireshark에서 핵심 필드 찾기",
      "위쪽에는 Version, Header Length, Total Length, Protocol, TTL, Source, Destination 필드 일곱 줄이, 아래쪽에는 원시 바이트 20개가 있습니다. 첫 바이트 45에서 Version과 IHL을, 이어서 TTL, Protocol, 출발지와 목적지 주소 바이트를 찾고, 마지막으로 Total Length 331에서 헤더 20바이트를 빼면 페이로드 311바이트가 남습니다.",
      "Wireshark는 원시 바이트와 해석된 필드를 함께 보여 줍니다. 그림의 바이트, 주소, TTL 값은 설명용 예시예요."), 2),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = []
    for (dn, nn, fn), (d, n, after) in zip(PAGES, COPY):
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        items = [(dn, *d, -1), (nn, *n, after)]
        pages.append(items)
        print(dn, nn)
    pages[0].append(STATIC)
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", pages)
