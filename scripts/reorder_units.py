#!/usr/bin/env python3
"""Exercises M3~M5 Unit 순서 재배치.

새 순서: 시작하기(+보고서 파일 만들기 쪽) → 핵심 실습·제공 파일 → 보고서 쓰기 → 오늘의 글 쓰기
        → 이번 Unit 마무리(새 레슨, 마지막 실습 레슨 끝의 마무리 쪽들) → 응용 → 정답

쪽(`## `)과 쪽별 SVG(`assets/pNN.svg`)를 함께 옮기고, `unit.md` 순서와 `__SITE__/…/lesson/L/page/P` 링크를 새 번호로 고친다.
사용: python3 scripts/reorder_units.py [--check] [M:U ...]
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLOSING_TITLE = re.compile(r"^(이번 Unit|Unit \d) 마무리")
MARKER_TAIL = re.compile(r"\n---\s*\n+<!--\s*learn:answers\s*-->\s*$")
LINK = re.compile(r"(__SITE__/exercises/module/(\d)/unit/(\d)/lesson/)(\d+)(?:/page/(\d+))?")


def split_pages(text: str):
    """(preamble, [page_text...]) — `## ` 제목(코드 울타리 밖)으로 나눈다."""
    lines = text.split("\n")
    starts, fence = [], False
    for i, line in enumerate(lines):
        if line.startswith("```") or line.startswith("~~~"):
            fence = not fence
        if not fence and line.startswith("## "):
            starts.append(i)
    pre = "\n".join(lines[: starts[0]])
    pages = ["\n".join(lines[a:b]) for a, b in zip(starts, starts[1:] + [len(lines)])]
    return pre, pages


def page_title(page: str) -> str:
    return page.split("\n", 1)[0][3:].strip()


class Lesson:
    def __init__(self, directory: Path):
        self.dir = directory
        self.path = directory / "lesson.md"
        text = self.path.read_text(encoding="utf-8")
        self.title = re.search(r"^title: (.*)$", text, re.M).group(1).strip()
        tail = MARKER_TAIL.search(text)
        self.tail = tail.group(0) if tail else ""
        body = text[: tail.start()] if tail else text
        self.pre, self.pages = split_pages(body)
        if self.tail:
            self.pages[-1] = self.pages[-1].rstrip("\n")
        self.svgs = []
        for n in range(1, len(self.pages) + 1):
            svg = directory / "assets" / f"p{n:02d}.svg"
            self.svgs.append(svg if svg.exists() else None)

    @property
    def kind(self):
        t = self.title
        if "정답" in t:
            return "answers"
        if "보고서 쓰기" in t:
            return "report"
        if "오늘의 글" in t:
            return "post"
        if "응용" in t:
            return "apply"
        if "시작하기" in t or t.startswith("준비"):
            return "start"
        return "core"


def plan_unit(m: int, u: int):
    udir = ROOT / f"exercises/module/{m}/unit/{u:02d}"
    unit_md = (udir / "unit.md").read_text(encoding="utf-8")
    paths = re.findall(r"^- path: (lesson/\d+/lesson\.md)$", unit_md, re.M)
    lessons = [Lesson(udir / Path(p).parent) for p in paths]
    return udir, unit_md, lessons


def reorder(m: int, u: int, check: bool):
    udir, unit_md, lessons = plan_unit(m, u)
    old_pos = {id(l): i + 1 for i, l in enumerate(lessons)}
    by_kind = lambda k: [l for l in lessons if l.kind == k]
    start = [l for l in lessons if l.kind == "start"][-1]  # 준비·시작하기 중 마지막이 시작하기
    report, post, answers = by_kind("report")[0], by_kind("post")[0], by_kind("answers")[0]
    core = by_kind("core")
    applies = by_kind("apply")
    # 1. 마무리 쪽: 마지막 실습 레슨에서 `이번 Unit 마무리` 제목부터 끝까지
    donor = None
    for l in reversed(core):
        if any(CLOSING_TITLE.match(page_title(p)) for p in l.pages):
            donor = l
            break
    assert donor, f"M{m}U{u}: 마무리 쪽을 찾지 못함"
    cut = next(i for i, p in enumerate(donor.pages) if CLOSING_TITLE.match(page_title(p)))
    moved_closing = donor.pages[cut:]
    moved_closing_svgs = donor.svgs[cut:]
    # 2. 보고서 파일 만들기 쪽
    assert page_title(report.pages[0]).startswith("보고서 파일 만들기"), f"M{m}U{u}: 보고서 첫 쪽이 다름"
    report_first, report_first_svg = report.pages[0], report.svgs[0]
    # 3. 새 위치 계산
    insert_at = len(start.pages)
    if page_title(start.pages[-1]).startswith("오류가 나면") and not (m == 3 and u == 1):
        insert_at -= 1
    new_order = [l for l in lessons if l.kind == "start"] + core + [report, post]
    closing_dir = udir / f"lesson/{max(int(l.dir.name) for l in lessons) + 1:02d}"
    new_order_final = new_order + ["CLOSING"] + applies + [answers]
    new_pos = {}
    closing_pos = None
    for i, item in enumerate(new_order_final, 1):
        if item == "CLOSING":
            closing_pos = i
        else:
            new_pos[id(item)] = i
    # 링크 매핑 (옛 레슨 위치, 쪽) -> (새 레슨 위치, 쪽)
    def mapping(L, P):
        lesson = lessons[L - 1]
        if lesson is report:
            if P == 1:
                return new_pos[id(start)], insert_at + 1
            return new_pos[id(report)], (P - 1) if P else P
        if lesson is donor and P and P > cut:
            return closing_pos, P - cut
        if lesson is start and P and P > insert_at:
            return new_pos[id(start)], P + 1
        return new_pos[id(lesson)], P

    print(f"M{m}U{u}: 시작하기 {len(start.pages)}쪽에 보고서 파일 쪽을 {insert_at + 1}번째로, "
          f"{donor.dir.name}레슨의 마무리 {len(moved_closing)}쪽 → 새 레슨 {closing_dir.name}(위치 {closing_pos})")
    if check:
        return mapping, udir
    # 4. 파일 쓰기
    def write_lesson(l: Lesson, pages, svgs, tail=None):
        body = l.pre.rstrip("\n") + "\n\n" + "\n\n".join(p.rstrip("\n") for p in pages) + "\n"
        t = l.tail if tail is None else tail
        if t:
            body = body.rstrip("\n") + t if t.startswith("\n") else body + t
            if not body.endswith("\n"):
                body += "\n"
        l.path.write_text(body, encoding="utf-8")
        assets = l.dir / "assets"
        tmp = l.dir / "_assets_new"
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir()
        for old in assets.glob("*") if assets.exists() else []:
            if not re.fullmatch(r"p\d\d\.svg", old.name):
                shutil.copy2(old, tmp / old.name)
        for n, svg in enumerate(svgs, 1):
            if svg is not None:
                shutil.copy2(svg, tmp / f"p{n:02d}.svg")
        if assets.exists():
            shutil.rmtree(assets)
        tmp.rename(assets)

    # 새 마무리 레슨
    nid = f"m{m}-u{u:02d}-l{int(closing_dir.name):02d}"
    closing_dir.mkdir(parents=True)
    pre = f"---\nid: {nid}\ntitle: 이번 Unit 마무리\nrender: markdown\n---\n\n# 이번 Unit 마무리\n"
    cl = Lesson.__new__(Lesson)
    cl.dir, cl.path, cl.pre, cl.tail = closing_dir, closing_dir / "lesson.md", pre, ""
    (closing_dir / "assets").mkdir()
    # 출처 이미지(figure)도 함께: 옮기는 쪽이 `assets/xxx` 를 참조하면 복사
    for page in moved_closing:
        for ref in set(re.findall(r"assets/([\w.\-]+)", page)):
            src = donor.dir / "assets" / ref
            if src.exists() and not re.fullmatch(r"p\d\d\.svg", ref):
                shutil.copy2(src, closing_dir / "assets" / ref)
    # SVG 는 원본이 지워지기 전에 읽어 둔다
    write_lesson(cl, moved_closing, moved_closing_svgs)
    # 시작하기에 보고서 쪽 삽입
    sp = start.pages[:insert_at] + [report_first] + start.pages[insert_at:]
    ss = start.svgs[:insert_at] + [report_first_svg] + start.svgs[insert_at:]
    write_lesson(start, sp, ss)
    # 보고서 레슨: 첫 쪽 제거
    write_lesson(report, report.pages[1:], report.svgs[1:])
    # 도너: 마무리 쪽 제거. 끝 구분선 정리
    kept = donor.pages[:cut]
    kept[-1] = re.sub(r"\n+---\s*$", "", kept[-1].rstrip("\n"))
    write_lesson(donor, kept, donor.svgs[:cut])
    # unit.md
    all_paths = {id(l): f"lesson/{l.dir.name}/lesson.md" for l in lessons}
    ordered = [all_paths[id(i)] if i != "CLOSING" else f"lesson/{closing_dir.name}/lesson.md" for i in new_order_final]
    head, rest = unit_md.split("lessons:\n", 1)
    tail_md = rest[rest.index("\n---"):] if "\n---" in rest else ""
    (udir / "unit.md").write_text(head + "lessons:\n" + "\n".join(f"- path: {p}" for p in ordered) + tail_md, encoding="utf-8")
    return mapping, udir


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    targets = [tuple(map(int, a.split(":"))) for a in args] or [(m, u) for m in (3, 4, 5) for u in range(1, 6)]
    maps = {}
    for m, u in targets:
        mp, _ = reorder(m, u, check)
        maps[(m, u)] = mp
    if check:
        return
    # 링크 재작성: 모든 lesson.md, 같은 Unit 링크만 매핑
    changed = 0
    for path in list((ROOT / "exercises").rglob("*.md")) + [ROOT / "portfolio-starter/README.md"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")

        def fix(match):
            m, u = int(match.group(2)), int(match.group(3))
            if (m, u) not in maps:
                return match.group(0)
            L, P = int(match.group(4)), match.group(5)
            nl, np_ = maps[(m, u)](L, int(P) if P else None)
            return f"{match.group(1)}{nl}" + (f"/page/{np_}" if P else "")

        new = LINK.sub(fix, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print("링크를 고친 파일:", changed)


if __name__ == "__main__":
    main()
