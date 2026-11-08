#!/usr/bin/env python3
"""Unit 11 Lesson 3 (경로 밖 관찰과 DPI), 10 Pages. Run from repo root:
python3 scripts/svg_pairs/u11_l03_oop.py   (--svg-only skips lesson.md edit / stale diagram delete)."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur
from u7_l01 import mv
from u11_structures import Y, srv, ends, road, gate, sensor, circle_tap

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("07-network-devices/lessons/restructured/03-*"))
OUT = LESSON / "assets" / "animations"
V = VIOLET


def tap(extra=""):
    return line(480, 235, 480, Y - 14, V, 3, "6 6") + circle_tap(480, Y) + extra


def p1():
    a = Anim(4, dur(False))
    body = [ends(), road(), mv(a, packet(0, 0), [(190, Y), (770, Y)], 1, 1, 4, 0.1, 0.9),
            a.vis(sensor(480, 215) + tap(), 2, 4), a.vis(pill(480, 165, "센서", V, 18, False, 90), 2, 4),
            a.vis(pill(480, 430, "복사본으로 양과 패턴을 살펴요", V, 18, True, 340), 3, 3),
            a.vis(pill(480, 430, "원래 통신은 경로에서 그대로 이어져요", GREEN, 18, False, 380), 4, 4)]
    caps = ["신청 요청은 서버로 계속 가요", "길 옆에 센서를 두고 복사본을 받아요", "센서는 트래픽의 양과 이상 징후를 살펴요", "경로를 바꾸지 않아서 서비스에 영향이 적어요"]
    return frame(a, "Sensor · 경로 밖에서 관찰", "서비스는 그대로 두고 옆에서 지켜봐요", caps, "".join(body))


def p2():
    a = Anim(4, dur(False))
    body = [laptop(110, 260, "사용자"), srv(850, 260), switch(480, 260), line(170, 260, 440, 260, LINE, 4, "10 8"), line(520, 260, 800, 260, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(190, 260), (770, 260)], 1, 1, 4, 0.1, 0.9),
            a.vis(line(480, 300, 480, 370, V, 3, "6 6") + laptop(480, 395, "분석 장치", V), 2, 4),
            a.vis(pill(480, 160, "미러 포트로 복사", V, 18, True, 200), 3, 3),
            a.vis(pill(480, 160, "많이 복사할수록 포트 용량이 필요해요", ORANGE, 18, False, 400), 4, 4)]
    caps = ["스위치가 사용자와 서버 사이 패킷을 전달해요", "관찰용 포트에 분석 장치를 연결해요", "원본은 목적지로, 같은 내용은 복사본으로 가요", "복사도 공짜가 아니에요"]
    return frame(a, "Mirroring · 패킷을 복사하기", "스위치 포트 미러링의 모습이에요", caps, "".join(body))


def p3():
    a = Anim(4, dur(False))
    body = [ends(), road(), sensor(480, 215) + tap(), pill(480, 165, "읽기 전용", V, 18, False, 120),
            mv(a, packet(0, 0, RED), [(190, Y), (770, Y)], 2, 2, 3, 0.1, 0.9),
            a.vis(ask(560, 235) + pill(640, 235, "이상한 패킷!", ORANGE, 17, True, 140), 2, 3),
            a.vis(pill(480, 430, "발견해도 원본은 그대로 가요", ORANGE, 18, True, 320), 3, 3),
            a.vis(gate(640, Y) + cross(640, Y - 70) + pill(480, 430, "막으려면 경로 안 Inline이 필요해요", BLUE, 18, False, 420), 4, 4)]
    caps = ["센서는 청진기처럼 읽기만 해요", "이상한 패킷을 발견했어요", "복사본을 본다고 원본이 막히진 않아요", "차단은 Inline 규칙이 따로 해야 해요"]
    return frame(a, "Read only와 차단의 차이", "발견하는 일과 막는 일은 달라요", caps, "".join(body))


def p4():
    a = Anim(4, dur(False))
    body = [ends(), road(), sensor(480, 215) + tap(),
            mv(a, packet(0, 0), [(190, Y), (770, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(480, 165, "경고 대상 주소 감지", V, 17, False, 220), 2, 4),
            mv(a, packet(0, 0, ORANGE), [(480, 235), (130, Y - 50)], 3, 3, 4, 0.1, 0.9),
            a.vis(pill(300, 215, "별도 경고 응답", ORANGE, 17, True, 160), 3, 3),
            a.vis(pill(480, 430, "관찰 + 별도 응답 = 능동 개입 (늘 되는 건 아니에요)", ORANGE, 17, False, 560), 4, 4)]
    caps = ["이용자가 특정 주소에 접속해요", "센서가 그 연결을 복사본으로 알아채요", "센서가 이용자에게 따로 응답을 보내요", "관찰만 하는 것과는 다른 능동 개입이에요"]
    return frame(a, "경로 밖에서 접속에 개입하기", "원래 패킷을 버리는 게 아니에요", caps, "".join(body))


def p5():
    a = Anim(4, dur(False))
    body = [ends(), line(170, Y, 800, Y, BLUE, 4), a.vis(pill(480, 330, "TCP 연결 (번호 확인)", BLUE, 16, False, 200), 1, 4),
            a.vis(sensor(480, 215) + tap(), 2, 4),
            mv(a, packet(0, 0, ORANGE), [(480, 235), (130, Y - 50)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(480, 165, "서버인 척 보낸 패킷", ORANGE, 17, True, 210), 3, 3),
            a.vis(ask(110, 220) + pill(480, 430, "번호가 안 맞으면 무시돼요 · HTTPS는 더 어려워요", ORANGE, 17, False, 520), 4, 4)]
    caps = ["웹 서버로 가는 TCP 연결이 있어요", "센서가 연결을 관찰해요", "연결의 한쪽인 척 별도 패킷을 보낼 수 있어요", "받아들일지는 단말이 정해서 항상 통하진 않아요"]
    return frame(a, "TCP 응답을 이용한 개입", "되는 경우도, 안 되는 경우도 있어요", caps, "".join(body))


def p6():
    a = Anim(4, dur(False))
    bx = 250
    body = [cell(bx, 200, 200, 110, "송장 (IP·포트)", BLUE, 18), cell(bx + 220, 200, 240, 110, "내용물 (Payload)", ORANGE, 18),
            a.vis(hl(bx, 200, 200, 110, GREEN) + pill(bx + 100, 345, "헤더만 보면 SPI", GREEN, 17, True, 170), 2, 2),
            a.vis(hl(bx, 200, 460, 110, V) + pill(bx + 230, 345, "안쪽까지 보면 DPI", V, 17, True, 190), 3, 3),
            a.vis(lock(bx + 340, 150, MUTED) + pill(480, 400, "HTTPS 내용은 복호화 권한 없이 못 읽어요", ORANGE, 17, False, 430), 4, 4)]
    caps = ["패킷은 송장과 내용물로 이뤄져 있어요", "주소·포트만 보는 얕은 검사예요", "Payload까지 보는 깊은 검사가 DPI예요", "암호화된 내용은 그대로 읽을 수 없어요"]
    return frame(a, "DPI · Payload까지 살펴보기", "택배 송장과 내용물에 비유해요", caps, "".join(body))


def p7():
    a = Anim(4, dur(False))
    body = [cell(370, 220, 220, 90, "이용자의 통신", BLUE, 20),
            a.vis(eye(480, 165), 1, 3), a.vis(pill(480, 360, "열어 보면 악성 단서를 찾을 수 있지만", GREEN, 18, False, 400), 2, 2),
            a.vis(lock(570, 150, ORANGE) + pill(480, 360, "사적인 내용까지 보일 수 있어요", ORANGE, 18, True, 330), 3, 3),
            a.vis("".join(pill(x, 400, t, GREEN, 17, False, w) for x, t, w in ((190, "수집 목적", 120), (370, "데이터 범위", 130), (570, "보관 기간", 120), (750, "접근 권한", 120))), 4, 4)]
    caps = ["운영자는 접속을 자세히 보고 싶어요", "내용을 검사하면 도움이 될 수 있어요", "하지만 이용자의 사생활이 담겨 있어요", "목적·범위·기간·권한을 함께 정해요"]
    return frame(a, "망중립과 사생활의 문제", "할 수 있다고 모두 해도 되는 건 아니에요", caps, "".join(body))


def p8():
    a = Anim(4, dur(False))
    pk = "".join(packet(150 + i * 55, Y, BLUE) for i in range(6))
    body = [a.vis(pk + pill(300, 235, "신청이 한꺼번에 몰려요", BLUE, 17, False, 220), 1, 4),
            a.vis(box(620, 250, 170, 100, V, PANEL, 12, sw=3) + text(705, 308, "센서", 22, V, 700) + arrow2(530, 610, Y), 2, 4),
            a.vis("".join(cross(150 + i * 55, 360) for i in (1, 3, 5)) + pill(300, 410, "못 받은 패킷은 기록에 없어요", RED, 17, True, 280), 3, 3),
            a.vis(pill(480, 430, "미러링 설정뿐 아니라 포트 속도·드롭 카운터도 점검해요", GREEN, 17, False, 560), 4, 4)]
    caps = ["짧은 시간에 패킷이 몰려요", "센서가 그 속도로 받아야 해요", "못 따라가면 일부가 누락돼요", "켰는지만 말고 드롭 여부도 확인해요"]
    return frame(a, "놓치지 않고 수집하는 문제", "복사본이 전부라고 보장되지는 않아요", caps, "".join(body))


def arrow2(x0, x1, y, c=MUTED):
    return line(x0, y, x1 - 14, y, c, 4) + f'<polygon points="{x1},{y} {x1 - 16},{y - 9} {x1 - 16},{y + 9}" fill="{c}"/>'


def p9():
    a = Anim(4, dur(False))
    steps = [("받기", "네트워크 카드", 70, BLUE), ("분석", "CPU·메모리", 380, V), ("저장", "디스크 쓰기", 690, ORANGE)]
    body = []
    for i, (t, s, x, c) in enumerate(steps):
        body.append(a.vis(cell(x, 210, 200, 100, t, c, 24) + text(x + 100, 340, s, 17, MUTED, 700), i + 1, 4))
    body += [a.vis(arrow2(275, 375, 260), 2, 4), a.vis(arrow2(585, 685, 260), 3, 4),
             a.vis(hl(690, 210, 200, 100, RED) + pill(480, 430, "1Gbps ≈ 초당 약 125MB씩 쌓여요", RED, 18, True, 380), 4, 4)]
    caps = ["센서는 먼저 복사본을 받아요", "CPU가 읽어서 분석해요", "기록하면 디스크 쓰기 성능이 필요해요", "어느 단계든 느리면 누락이 생겨요"]
    return frame(a, "저장과 분석의 부하", "빠른 포트 하나로 끝나지 않아요", caps, "".join(body))


def p10():
    a = Anim(4, dur(False))
    left = box(60, 130, 400, 270, ORANGE, PANEL, 16, sw=3) + text(260, 168, "Inline", 24, ORANGE, 700) + gate(260, 260)
    right = box(500, 130, 400, 270, V, PANEL, 16, sw=3) + text(700, 168, "Out of path", 24, V, 700) + eye(700, 255)
    body = [a.vis(left, 1, 4), a.vis(right, 2, 4),
            a.vis(pill(260, 360, "실시간 차단에 알맞아요", ORANGE, 17, True, 230) + pill(700, 360, "영향 없이 사후 분석해요", V, 17, True, 240), 3, 4),
            a.vis(pill(480, 438, "정답은 없고 목적·누락·개인정보를 함께 따져요", GREEN, 18, False, 500), 4, 4)]
    caps = ["Inline은 경로 안에서 바로 처리해요", "Out of path는 복사본을 받아 분석해요", "목표에 따라 알맞은 쪽이 달라요", "하나가 늘 더 좋다고 단정하지 않아요"]
    return frame(a, "Inline과 Out of path 비교", "같은 상황에서 무엇이 다를까요", caps, "".join(body))


ITEMS = [
    ("u11-oop-sensor", "advanced-source-05-page-01", "Sensor · 경로 밖에서 관찰", "길 옆 센서가 복사본으로 트래픽을 살피고 원래 통신은 그대로 서버에 도착하는 모습입니다.", "센서는 복사본만 보고 원래 경로는 바꾸지 않습니다.", p1),
    ("u11-oop-mirroring", "advanced-source-05-page-02", "Mirroring · 패킷을 복사하기", "스위치가 원본 패킷은 서버로 보내고 같은 내용을 관찰용 포트의 분석 장치로 복사하는 모습입니다.", "포트 미러링은 복사본을 분석 장치로 보냅니다.", p2),
    ("u11-oop-read-only", "advanced-source-05-page-03", "Read only와 차단의 차이", "센서가 이상한 패킷을 발견해도 원본은 서버로 가고, 차단은 경로 안 Inline 장치가 맡는 모습입니다.", "발견하는 일과 차단하는 일은 다릅니다.", p3),
    ("u11-oop-intervene", "advanced-source-05-page-04", "경로 밖에서 접속에 개입하기", "센서가 연결을 감지해 이용자에게 별도 경고 응답을 보내는 능동 개입을 보여 줍니다.", "관찰 외에 별도 응답을 보내는 것은 능동 개입입니다.", p4),
    ("u11-oop-tcp-reply", "advanced-source-05-page-05", "TCP 응답을 이용한 개입", "센서가 TCP 연결의 한쪽인 척 패킷을 보내도 번호가 맞지 않으면 단말이 무시할 수 있음을 보여 줍니다.", "TCP 응답 개입은 연결 상태가 맞아야 통합니다.", p5),
    ("u11-oop-dpi", "advanced-source-05-page-06", "DPI · Payload까지 살펴보기", "패킷을 송장(헤더)과 내용물(Payload)로 나누어 헤더만 보는 SPI와 안쪽까지 보는 DPI를 비교합니다.", "DPI는 헤더를 넘어 Payload까지 검사합니다.", p6),
    ("u11-oop-privacy", "advanced-source-05-page-07", "망중립과 사생활의 문제", "통신 내용을 열어 보면 악성 단서와 사적 정보가 함께 보이므로 목적·범위·기간·권한을 정해야 한다는 그림입니다.", "검사 범위는 목적과 권한에 맞춰 정해야 합니다.", p7),
    ("u11-oop-dropped", "advanced-source-05-page-08", "놓치지 않고 수집하는 문제", "몰리는 패킷을 센서가 못 따라가면 일부가 누락될 수 있음을 보여 줍니다.", "복사본이 전부 수집된다고 보장되지는 않습니다.", p8),
    ("u11-oop-storage", "advanced-source-05-page-09", "저장과 분석의 부하", "받기, 분석, 저장 세 단계 중 어느 단계든 느리면 누락이 생기고 1Gbps는 초당 약 125MB라는 점을 보여 줍니다.", "수집·분석·저장 전체 처리 용량을 봐야 합니다.", p9),
    ("u11-oop-compare", "advanced-source-05-page-10", "Inline과 Out of path 비교", "Inline은 실시간 차단에, Out of path는 영향 없는 사후 분석에 알맞다는 비교입니다.", "목적에 따라 알맞은 구조가 다릅니다.", p10),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    s = md.read_text(encoding="utf-8")
    s = re.sub(r"  illustrations:\n  - file: assets/diagrams/source-05\.svg\n(?:    .*\n)+", "", s, count=1)
    for f, pid, t, al, c, _ in ITEMS:
        if f"assets/animations/{f}.svg" in s:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: 0\n")
        s = s.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_r, fn in ITEMS:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
        (LESSON / "assets" / "diagrams" / "source-05.svg").unlink(missing_ok=True)
    print("ok", len(ITEMS), "svgs")
