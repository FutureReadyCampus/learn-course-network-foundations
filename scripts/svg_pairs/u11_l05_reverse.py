#!/usr/bin/env python3
"""Unit 11 Lesson 5 (리버스 프록시와 서버 앞단): light example SVG per Page (5). Run from repo root:
python3 scripts/svg_pairs/u11_l05_reverse.py   (--svg-only skips lesson.md edit / stale diagram removal)."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, dur
from u7_l01 import mv
from u11_structures import srv, agent, gate

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/restructured/05-*"))
OUT = LESSON / "assets" / "animations"
Y = 300


def two_servers():
    return srv(850, 230) + srv(850, 370)


def p1():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "사용자"), agent(480, Y),
            a.vis(pill(110, 215, "event.example", BLUE, 17, False, 170), 1, 4),
            a.vis(line(170, Y, 425, Y, BLUE, 5) + pill(300, 262, "DNS가 알려 준 주소", BLUE, 15, True, 170), 2, 4),
            a.vis(two_servers() + line(535, Y, 816, 230, GREEN, 4) + line(535, Y, 816, 370, GREEN, 4), 3, 4),
            a.vis(pill(480, 215, "서버 앞에서 먼저 받아요", GREEN, 18, True, 250), 4, 4)]
    caps = ["사용자는 서비스 이름으로 접속해요", "도착하는 곳은 실제 서버가 아니라 앞단 Proxy예요", "Proxy가 안쪽 서버로 대신 전달해요", "이것이 Reverse Proxy예요"]
    return frame(a, "Client 보호와 Server 보호", "서버 앞에서 요청을 먼저 받아요", caps, "".join(body))


def p2():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "외부"), srv(850, Y), line(170, Y, 800, Y, LINE, 4, "10 8"), gate(480, Y, VIOLET),
            text(480, 242, "IPS", 20, VIOLET, 700),
            a.vis(pill(480, 190, "서버 앞 IPS", VIOLET, 18, False, 160), 1, 4),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, RED), [(190, Y), (440, Y)], 2, 2, 2, 0.1, 0.6),
            a.vis(pill(480, 430, "정상은 통과, 공격 패턴은 차단", ORANGE, 18, True, 330) + cross(480, 365), 2, 2),
            a.vis(packet(370, Y, BLUE) + lock(370, Y - 46, BLUE) + pill(480, 430, "HTTPS 본문은 그대로 못 읽어요", BLUE, 18, False, 330), 3, 3),
            a.vis(pill(480, 430, "어디서 무엇이 보이는지 먼저 확인", GREEN, 18, True, 350), 4, 4)]
    caps = ["외부 요청이 서버에 닿기 전에 IPS를 놓아요", "규칙에 맞으면 통과, 공격 패턴이면 차단해요", "암호화(HTTPS)된 본문은 그대로 읽기 어려워요", "그래서 보이는 범위부터 확인해요"]
    return frame(a, "IPS · 앞단에서의 방어", "서버 앞 검문소가 규칙으로 걸러요", caps, "".join(body))


def p3():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "브라우저"), agent(480, Y), srv(850, Y),
            a.vis(line(170, Y, 425, Y, BLUE, 5) + lock(300, 262, BLUE) + pill(300, 340, "TLS 연결 ①", BLUE, 16, True, 120), 1, 4),
            a.vis(pill(480, 215, "TLS 종단 Proxy", VIOLET, 18, False, 190), 2, 4),
            a.vis(line(535, Y, 800, Y, GREEN, 5) + pill(668, 262, "내부 전달 ②", GREEN, 16, True, 130), 3, 4),
            a.vis(pill(480, 430, "인증서·키 준비가 필요해요", ORANGE, 18, False, 300), 4, 4)]
    caps = ["브라우저는 먼저 Proxy와 TLS 연결을 맺어요", "Proxy가 서버를 대신해 TLS를 끝내요", "풀린 요청을 내부 서버로 전달해요", "허가 없는 복호화와는 달라요"]
    return frame(a, "SSL Accelerator와 복호화", "TLS 처리를 앞단에 모아요", caps, "".join(body))


def p4():
    a = Anim(4, dur(False))
    body = [laptop(110, Y, "사용자"), agent(480, Y, VIOLET), srv(850, Y), line(170, Y, 425, Y, LINE, 4, "10 8"), line(535, Y, 800, Y, LINE, 4, "10 8"),
            a.vis(pill(480, 215, "WAF · 웹 요청 검사", VIOLET, 18, False, 210), 1, 4),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(pill(480, 430, "정상 요청 → 내부 서버로 전달", GREEN, 18, True, 330), 2, 2),
            mv(a, packet(0, 0, RED), [(190, Y), (420, Y)], 3, 3, 3, 0.1, 0.6),
            a.vis(cross(300, 262) + pill(480, 430, "' OR 1=1 같은 공격 패턴 → 차단", RED, 18, True, 400), 3, 3),
            a.vis(pill(480, 430, "모든 공격을 찾지는 못해요", ORANGE, 18, False, 300), 4, 4)]
    caps = ["WAF는 웹 요청의 내용을 살펴봐요", "정상 요청은 서버까지 전달돼요", "웹 공격 패턴은 정책에 따라 막아요", "규칙이 안 맞으면 놓치거나 오차단도 있어요"]
    return frame(a, "WAF · 웹 요청을 검사", "앞단이 웹 요청의 내용을 봐요", caps, "".join(body))


def p5():
    a = Anim(4, dur(False))
    rows = [("Forward Proxy", "내 컴퓨터 대신 →", "외부 서버", BLUE), ("Reverse Proxy", "서버 대신 ←", "외부 요청 받기", GREEN)]
    body = [cell(330, 120, 250, 36, "누구를 대신하나?", MUTED, 17, BG), cell(600, 120, 250, 36, "어디로 전달하나?", MUTED, 17, BG)]
    for i, (n, who, to, c) in enumerate(rows):
        y = 168 + i * 76
        body.append(a.vis(cell(90, y, 220, 60, n, c, 20) + cell(330, y, 250, 60, who, c, 19) + cell(600, y, 250, 60, to, c, 19), i + 1, 4))
    body.append(a.vis(pill(480, 350, "서버 앞 Reverse Proxy: 외부 → 내부 서버", GREEN, 18, False, 440), 3, 4))
    body.append(a.vis("".join(cell(110 + i * 270, 395, 250, 46, t, c, 18) for i, (t, c) in enumerate((("경로 안에서 처리", ORANGE), ("복사본 관찰", VIOLET), ("연결 대신 중계", BLUE)))), 4, 4))
    caps = ["Forward는 내 요청을 밖으로 대신 보내요", "Reverse는 서버 앞에서 요청을 받아요", "누굴 대신하는지 보면 헷갈리지 않아요", "이 Unit의 세 가지 구조를 구별해요"]
    return frame(a, "Reverse Proxy로 서버 보호", "대신하는 방향이 달라요", caps, "".join(body))


ITEMS = [
    ("u11-reverse-front", "advanced-source-08-page-01", "Client 보호와 Server 보호",
     "사용자가 서비스 이름으로 접속하면 DNS가 알려 준 앞단 Proxy가 요청을 받아 안쪽 서버로 전달하는 모습입니다.",
     "Reverse Proxy는 서버 앞에서 요청을 먼저 받습니다.", p1),
    ("u11-reverse-ips", "advanced-source-08-page-02", "IPS · 앞단에서의 방어",
     "서버 앞 IPS가 정상 패킷은 통과시키고 공격 패턴은 차단하며, 암호화된 HTTPS 본문은 그대로 읽기 어렵다는 그림입니다.",
     "IPS가 볼 수 있는 정보는 위치와 암호화에 따라 달라집니다.", p2),
    ("u11-reverse-tls", "advanced-source-08-page-03", "SSL Accelerator와 복호화",
     "브라우저가 앞단 Proxy와 TLS 연결을 맺고, Proxy가 내부 서버로 요청을 전달하는 모습입니다.",
     "TLS 종단 Proxy는 서버 대신 HTTPS 연결을 받습니다.", p3),
    ("u11-reverse-waf", "advanced-source-08-page-04", "WAF · 웹 요청을 검사",
     "WAF가 정상 요청은 서버로 전달하고 웹 공격 패턴은 차단하지만 모든 공격을 찾지는 못한다는 그림입니다.",
     "WAF는 웹 요청의 내용을 보고 허용하거나 차단합니다.", p4),
    ("u11-reverse-compare", "advanced-source-08-page-05", "Reverse Proxy로 서버 보호",
     "Forward Proxy는 클라이언트를 대신하고 Reverse Proxy는 서버를 대신하며, 이번 Unit의 세 가지 구조를 정리하는 표입니다.",
     "Forward와 Reverse는 대신하는 방향이 다릅니다.", p5),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-08\.svg\n(?:    .*\n)+", "", s, count=1)
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
        (LESSON / "assets" / "diagrams" / "source-08.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
