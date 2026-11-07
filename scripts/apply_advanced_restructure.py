#!/usr/bin/env python3
"""Apply the reviewed 20-Lesson structure while keeping source manuscripts intact."""

import argparse
import json
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "u11-l01": ("units/07-network-devices", "01-장치가-트래픽을-다루는-세-가지-구조"),
    "u11-l02": ("units/07-network-devices", "02-인라인-구조와-트래픽-처리"),
    "u11-l03": ("units/07-network-devices", "03-경로-밖-관찰과-dpi"),
    "u11-l04": ("units/07-network-devices", "04-포워드-프록시와-클라이언트-측-중계"),
    "u11-l05": ("units/07-network-devices", "05-리버스-프록시와-서버-앞단"),
    "u12-l01": ("units/08-router-and-nat", "01-사설-주소-공인-주소와-공유기"),
    "u12-l02": ("units/08-router-and-nat", "02-nat-변환표로-통신-따라가기"),
    "u12-l03": ("units/08-router-and-nat", "03-nat의-매핑과-수신-허용-방식"),
    "u12-l04": ("units/08-router-and-nat", "04-포트-포워딩으로-내부-서비스-연결하기"),
    "u12-l05": ("units/08-router-and-nat", "05-upnp와-자동-포트-설정"),
    "u13-l01": ("units/09-load-balancing", "01-l4-부하-분산과-서버-상태-확인"),
    "u13-l02": ("units/09-load-balancing", "02-이중화로-장애에-대비하기"),
    "u13-l03": ("units/09-load-balancing", "03-dns-기반-부하-분산과-gslb"),
    "u14-l01": ("units/10-vpn-and-security", "01-사설망을-인터넷으로-연결하는-vpn"),
    "u14-l02": ("units/10-vpn-and-security", "02-ipsec과-터널링"),
    "u14-l03": ("units/10-vpn-and-security", "03-원격-접속-vpn과-사용-시-주의"),
    "u15-l01": ("units/15-network-security-solutions", "01-보안-장치의-배치와-역할"),
    "u15-l02": ("units/15-network-security-solutions", "02-nac와-네트워크-접근-통제"),
    "u15-l03": ("units/15-network-security-solutions", "03-방화벽과-연결-상태-추적"),
    "u15-l04": ("units/15-network-security-solutions", "04-침입-탐지-차단과-보안-로그-분석"),
}
UNIT_META = {
    11: ("network-devices", "네트워크 장치의 배치와 프록시", "units/07-network-devices"),
    12: ("router-and-nat", "공유기와 NAT의 동작", "units/08-router-and-nat"),
    13: ("load-balancing", "부하 분산과 서비스 가용성", "units/09-load-balancing"),
    14: ("vpn-and-security", "VPN과 원격 네트워크 연결", "units/10-vpn-and-security"),
    15: ("network-security-solutions", "네트워크 보안 솔루션", "units/15-network-security-solutions"),
}
LESSON_SECTIONS = re.compile(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", re.M | re.S)


def frontmatter(data):
    return "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000).strip() + "\n---\n\n"


def page_title(heading):
    return re.sub(r"\s*·\s*\d+:\d+.*$", "", heading).strip()


def apply(plan_path: Path, write: bool):
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    if plan.get("runtime_ready") is not False or len(plan.get("lessons", [])) != 20:
        raise ValueError("Expected the reviewed, read-only 20-Lesson plan")
    if sum(len(item["pages"]) for item in plan["lessons"]) != 194:
        raise ValueError("Expected 194 technical Pages")
    if set(TARGETS) != {item["target_key"] for item in plan["lessons"]}:
        raise ValueError("Target paths do not match the reviewed structure")
    snapshot = json.loads((ROOT / "docs/advanced-restructure-snapshot.json").read_text(encoding="utf-8"))
    source_by_id = {item["lesson_id"]: item for item in snapshot["sources"]}
    source_ordinal = {item["lesson_id"]: index for index, item in enumerate(snapshot["sources"], 1)}
    used_source_ids = {source_id for lesson in plan["lessons"] for source_id in lesson["source_lesson_ids"]}
    source_meta, source_sections = {}, {}
    for source in snapshot["sources"]:
        if source["lesson_id"] not in used_source_ids:
            continue
        path = ROOT / source["path"]
        raw = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", raw, re.S)
        if not match:
            raise ValueError(f"Source lacks front matter: {source['path']}")
        metadata = yaml.safe_load(match.group(1)) or {}
        sections = [(page_title(h), body.strip()) for h, body in LESSON_SECTIONS.findall(match.group(2))]
        if len(sections) != len(source["pages"]):
            raise ValueError(f"Source Page count changed: {source['lesson_id']}")
        for (title, _), page in zip(sections, source["pages"]):
            if title != page["title"]:
                raise ValueError(f"Source heading changed: {source['lesson_id']} Page {page['source_page']}")
        source_meta[source["lesson_id"]] = metadata
        source_sections[source["lesson_id"]] = sections

    writes, copies = {}, {}
    unit_lessons = {number: [] for number in UNIT_META}
    for lesson in plan["lessons"]:
        unit_dir, directory_name = TARGETS[lesson["target_key"]]
        lesson_dir = ROOT / unit_dir / "lessons/restructured" / directory_name
        lesson_path = lesson_dir / "lesson.md"
        if lesson_path.exists():
            raise FileExistsError(f"Refusing to overwrite existing target: {lesson_path}")
        source_ids = lesson["source_lesson_ids"]
        source_wikis = [source_meta[source_id].get("source_wiki", "") for source_id in source_ids]
        metadata = {
            "id": lesson["id"], "title": lesson["title"],
            "source_lesson_ids": source_ids, "source_wikis": source_wikis,
            "source_wiki": source_wikis[0] if source_wikis else "",
        }
        page_metadata = []
        output = [frontmatter(metadata)]
        for page in lesson["pages"]:
            source_id, source_page = page["source_lesson_id"], page["source_page"]
            heading, body = source_sections[source_id][source_page - 1]
            expected_title = source_by_id[source_id]["pages"][source_page - 1]["title"]
            if heading != expected_title:
                raise ValueError(f"Planned title differs for {source_id} Page {source_page}")
            output.extend([f"## {heading}\n\n<!-- learn-page-id: {page['page_id']} -->\n\n{body}\n\n"])
            source_diagram = source_meta[source_id].get("wiki_diagram")
            if source_diagram and source_page == 1:
                original = (ROOT / source_diagram).resolve()
                if not original.is_relative_to(ROOT.resolve()) or not original.is_file():
                    raise ValueError(f"Missing or unsafe source diagram: {source_diagram}")
                filename = f"source-{source_ordinal[source_id]:02d}.svg"
                relative = f"assets/diagrams/{filename}"
                destination = lesson_dir / relative
                copies[destination] = original
                page_metadata.append({
                    "page_id": page["page_id"],
                    "illustrations": [{
                        "file": relative,
                        "title": f"{heading} · 원고 그림",
                        "alt": f"{heading}에서 원고가 함께 제공한 개념 그림",
                        "caption": "기존 원고의 그림을 참고해 구조와 용어를 확인한다.",
                        "after_paragraph": -1,
                    }],
                })
        if page_metadata:
            metadata["page_metadata"] = page_metadata
            output[0] = frontmatter(metadata)
        writes[lesson_path] = "".join(output).rstrip() + "\n"
        unit_number = lesson["unit_number"]
        unit_lessons[unit_number].append({"path": f"lessons/restructured/{directory_name}/lesson.md"})

    units_path = ROOT / "course.yaml"
    course = yaml.safe_load(units_path.read_text(encoding="utf-8"))
    ordinary = [item for item in course["units"] if item["id"] not in {v[0] for v in UNIT_META.values()}]
    advanced_units = []
    for number, (unit_id, title, unit_dir) in UNIT_META.items():
        advanced_units.append({"id": unit_id, "title": title, "path": f"{unit_dir}/unit.md"})
        unit_path = ROOT / unit_dir / "unit.md"
        old = unit_path.read_text(encoding="utf-8") if unit_path.exists() else ""
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", old, re.S)
        unit_meta = yaml.safe_load(match.group(1)) if match else {}
        unit_meta = unit_meta or {}
        unit_meta.update({"id": unit_id, "title": title, "lessons": unit_lessons[number]})
        if not unit_meta.get("source"):
            unit_meta["source"] = {"repository": "physical-spark/course-network",
                                    "commit": "d1b650e39cb0fd01f4b67adb76926172dbd517c9",
                                    "path": "studio/wiki/oeweo-network/advanced/book.json"}
        writes[unit_path] = frontmatter(unit_meta).rstrip() + "\n"
    course["units"] = ordinary + advanced_units
    course["route_aliases_file"] = "docs/advanced-route-aliases.json"
    writes[units_path] = yaml.safe_dump(course, allow_unicode=True, sort_keys=False, width=1000)
    writes[ROOT / "docs/advanced-route-aliases.json"] = json.dumps(
        plan["aliases"], ensure_ascii=False, indent=2) + "\n"

    if not write:
        return {"mode": "dry-run", "new_lessons": len(plan["lessons"]),
                "new_pages": 194, "illustration_files": len(copies), "files_to_write": len(writes)}
    for path, content in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for destination, original in copies.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, destination)
    return {"mode": "written", "new_lessons": len(plan["lessons"]),
            "new_pages": 194, "illustration_files": len(copies), "files_written": len(writes)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--write", action="store_true", help="Write target Lessons and curriculum files")
    args = parser.parse_args()
    print(json.dumps(apply(args.plan, args.write), ensure_ascii=False))


if __name__ == "__main__":
    main()
