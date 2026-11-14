#!/usr/bin/env python3
"""Read-only #163/#223 preflight. Never connects to a DB or changes a catalog."""

import argparse
import copy
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def make_plan(snapshot, contract, catalog, legacy_units, source_root=ROOT):
    require(contract["schema"] == "advanced-restructure-contract-v1", "Unknown contract")
    require(snapshot["format"] == "advanced-restructure-audit-v1", "Unknown snapshot")
    require(contract["future_route_version"] == "v3", "Reordered positions need a new route edition")
    require(re.fullmatch(r"network-[0-9a-f]{40}", catalog["version"]), "Use a full source SHA")
    require(len(catalog["units"]) == 14, "Preflight expects the unchanged 14 Unit source edition")
    require(legacy_units == contract["learn_legacy_units"], "Reviewed legacy route table changed")
    targets = {item["target_key"]: item for item in snapshot["targets"]}
    for override in contract.get("target_overrides", []):
        targets[override["target_key"]] = override
    ids = {item["target_key"]: item["lesson_id"] for item in contract["lesson_ids"]}
    targets = {item["target_key"]: targets[item["target_key"]]
               for item in contract["lesson_ids"]}
    require(len(ids) == len(contract["lesson_ids"]) == 24 and set(ids) == set(targets),
            "Exactly 24 distinct targets required")
    require(len(set(ids.values())) == 24, "Duplicate target Lesson ID")
    require(all(isinstance(value, str) and 0 < len(value) <= 100 for value in ids.values()),
            "Lesson IDs must fit the current API")
    excluded_sources = set(contract.get("excluded_source_keys", []))
    require(excluded_sources == {item["source"] for item in snapshot["resources"]},
            "Excluded source list differs")
    source_lessons = {item["id"]: item for item in catalog["lessons"]}
    source_pages, sources = {}, {}
    assigned = []
    for target in targets.values():
        assigned.extend(target["source_pages"])
    for ordinal, source in enumerate(snapshot["sources"], 1):
        source_id = source["lesson_id"]
        require(source_id not in sources, "Duplicate source Lesson")
        require(hashlib.sha256((source_root / source["path"]).read_bytes()).hexdigest()
                == source["file_sha256"], f"Source changed: {source['path']}")
        current = source_lessons[source_id]
        require(len(current["pages"]) == len(source["pages"]), f"Page count changed: {source_id}")
        sources[source_id] = source
        for old in source["pages"]:
            page = current["pages"][old["source_page"] - 1]
            require(digest(page) == old["content_sha256"], f"Page changed: {old['audit_page_key']}")
            require([q["id"] for q in page["questions"]] == old["question_ids"], "Question set changed")
            page_id = old["existing_page_id"] or contract["page_id_rule"].format(
                source_ordinal=ordinal, source_page=old["source_page"])
            require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", page_id), "Invalid Page ID")
            require(old["audit_page_key"] not in source_pages, "Duplicate source Page")
            source_pages[old["audit_page_key"]] = {
                "source_lesson_id": source_id, "source_page": old["source_page"],
                "page_id": page_id, "content_sha256": old["content_sha256"],
                "source_wiki": source["source_wiki"], "payload": copy.deepcopy(page),
                "role": old["destination"]["role"],
            }
    baseline_targets = {page: target["target_key"] for target in snapshot["targets"]
                        for page in target["source_pages"]}
    current_targets = {page: target["target_key"] for target in targets.values()
                       for page in target["source_pages"]}
    remapped_pages = {page: target for page, target in current_targets.items()
                      if baseline_targets.get(page) != target}
    require(remapped_pages == contract.get("source_page_remapping", {}),
            "Target changes must be recorded in source_page_remapping")
    excluded_pages = {page["audit_page_key"] for source in snapshot["sources"]
                      if source["source_key"] in excluded_sources for page in source["pages"]}
    assigned.extend(excluded_pages)
    require(len(assigned) == len(set(assigned)) == len(source_pages) == 203,
            "Every source Page must be assigned once or explicitly excluded")
    require(set(assigned) == set(source_pages), "Unknown or missing source Page")
    technical_pages = set(source_pages) - excluded_pages
    require(len(technical_pages) == 194, "Technical Page total changed")
    require(len({source_pages[key]["page_id"] for key in technical_pages}) == 194,
            "Duplicate technical Page ID")
    for path, expected in snapshot["source_asset_sha256"].items():
        require(hashlib.sha256((source_root / path).read_bytes()).hexdigest() == expected,
                f"Asset changed: {path}")

    lessons, destinations = [], {}
    source_uses = {}
    for key, target in targets.items():
        for audit_key in target["source_pages"]:
            source_id = source_pages[audit_key]["source_lesson_id"]
            source_uses.setdefault(source_id, set()).add(key)
    for key, target in targets.items():
        contributors = list(dict.fromkeys(source_pages[p]["source_lesson_id"]
                                          for p in target["source_pages"]))
        # "identity": "new" drops a whole-source ID; "preserved" records a reviewed decision
        # to keep a contributing source's ID although Pages moved in or out.
        preserve = target.get("identity") == "preserved" or (
            len(contributors) == 1 and len(source_uses[contributors[0]]) == 1
            and len(target["source_pages"]) == len(sources[contributors[0]]["pages"])
            and target.get("identity") != "new")
        require((ids[key] in contributors) if preserve else ids[key] not in source_lessons,
                f"Unchanged Lessons keep IDs; merged/split Lessons use new IDs: {key}")
        lesson_number = int(key.rsplit("l", 1)[1])
        kept_order = 0
        lesson = {"id": ids[key], "target_key": key, "title": target["title"],
                  "unit_number": target["unit_number"], "lesson_number": lesson_number,
                  "identity": "preserved" if preserve else "new",
                  "source_lesson_ids": contributors, "pages": []}
        for number, audit_key in enumerate(target["source_pages"], 1):
            page = source_pages[audit_key]
            original = next(p for p in sources[page["source_lesson_id"]]["pages"]
                            if p["audit_page_key"] == audit_key)
            if audit_key in contract.get("source_page_remapping", {}):
                require(contract["source_page_remapping"][audit_key] == key,
                        "Remapped source Page has the wrong target")
            else:
                # Remapped Pages may shift numbers, but staying Pages keep their relative order.
                require(original["destination"]["target_key"] == key
                        and original["destination"]["source_order"] > kept_order,
                        "Page destination/order changed")
                kept_order = original["destination"]["source_order"]
            lesson["pages"].append({k: v for k, v in page.items() if k != "payload"})
            destinations[(page["source_lesson_id"], page["source_page"])] = {
                "kind": "lesson", "id": ids[key], "page_id": page["page_id"], "page": number,
                "path": f"/m2-network/v3/unit/{target['unit_number']}/lesson/{lesson_number}/page/{number}",
            }
        lessons.append(lesson)

    # Freeze all old positions, including basic Units; never feed old numbers into v3.
    aliases = []
    excluded_lesson_ids = {source["lesson_id"] for source in snapshot["sources"]
                           if source["source_key"] in excluded_sources}
    learn_v2_unmapped = set(contract.get("learn_v2_unmapped_lesson_ids", []))
    require(learn_v2_unmapped.issubset(source_lessons),
            "Learn v2 Unit 10 exclusions must name current source Lessons")
    for unit_number, unit in enumerate(catalog["units"], 1):
        siblings = [l for l in catalog["lessons"] if l["unit"] == unit["id"]]
        for lesson_number, lesson in enumerate(siblings, 1):
            if lesson["id"] in excluded_lesson_ids:
                continue
            for number in range(1, len(lesson["pages"]) + 1):
                destination = destinations.get((lesson["id"], number)) or {
                    "kind": "lesson", "id": lesson["id"], "page": number,
                    "path": f"/m2-network/v3/unit/{unit_number}/lesson/{lesson_number}/page/{number}",
                }
                for namespace, prefix in [("content-stage-14", "/m2-network"),
                                          ("learn-v2", "/m2-network/v2")]:
                    if namespace == "learn-v2" and lesson["id"] in learn_v2_unmapped:
                        continue
                    aliases.append({"namespace": namespace,
                                    "path": f"{prefix}/unit/{unit_number}/lesson/{lesson_number}/page/{number}",
                                    "source_lesson_id": lesson["id"], "source_page": number,
                                    "destination": destination})
    intentionally_unmapped = set(contract.get("legacy_unmapped_lesson_ids", []))
    require(intentionally_unmapped.isdisjoint(source_lessons),
            "Intentionally unmapped legacy Lessons must not be treated as current source Lessons")
    for unit_number, group in enumerate(legacy_units, 1):
        for lesson_number, lesson_id in enumerate(group, 1):
            if lesson_id in intentionally_unmapped:
                continue
            require(lesson_id in source_lessons, f"Unknown legacy Lesson: {lesson_id}")
            for number in range(1, len(source_lessons[lesson_id]["pages"]) + 1):
                canonical = next((a for a in aliases if a["namespace"] == "learn-v2"
                                  and a["source_lesson_id"] == lesson_id and a["source_page"] == number), None)
                if canonical is None:
                    continue
                aliases.append({**canonical, "namespace": "learn-unversioned",
                                "path": f"/m2-network/unit/{unit_number}/lesson/{lesson_number}/page/{number}"})
    require(len({(a['namespace'], a['path']) for a in aliases}) == len(aliases), "Ambiguous alias")
    current_v2 = {a["path"]: (a["source_lesson_id"], a["source_page"])
                  for a in aliases if a["namespace"] == "learn-v2"}
    for source in snapshot["sources"]:
        if source["source_key"] in excluded_sources:
            continue
        for page in source["pages"]:
            require(current_v2.get(page["learn_v2_path"]) == (source["lesson_id"], page["source_page"]),
                    "Source positions changed before preflight")
    require(sum(len(l["pages"]) for l in lessons) == 194, "Technical Page total changed")
    require(not any(alias["source_lesson_id"] in {s["lesson_id"] for s in snapshot["sources"]
                                                  if s["source_key"] in excluded_sources}
                    for alias in aliases), "Excluded source received a route alias")
    return {"schema": "advanced-restructure-preflight-v1", "mode": "read-only",
            "runtime_ready": False, "source_catalog_version": catalog["version"],
            "snapshot_sha256": digest(snapshot), "contract_sha256": digest(contract),
            "lessons": lessons, "excluded_source_lessons": [s["lesson_id"] for s in snapshot["sources"]
                if s["source_key"] in excluded_sources], "aliases": aliases,
            "unmapped_legacy_lessons": sorted(intentionally_unmapped),
            "unmapped_learn_v2_lessons": sorted(learn_v2_unmapped),
            "counts": {"target_lessons": len(lessons), "technical_pages": 194,
                       "excluded_pages": len(excluded_pages),
                       "source_assets": len(snapshot["source_asset_sha256"]),
                       "source_catalog_pages": sum(len(l["pages"]) for l in catalog["lessons"]),
                       "aliases_by_namespace": {namespace: sum(a["namespace"] == namespace for a in aliases)
                                                for namespace in ("content-stage-14", "learn-v2", "learn-unversioned")},
            "aliases": len(aliases)}}


def completion_preflight(plan, rows, published_source_ids, reviewed_versions):
    """Return eligibility only. No new states, answers, events, or publication writes.

    Whole-Lesson explicit evidence can cover unchanged source ranges. Empty quiz
    sets, visit cursors, and partial passes never manufacture completion.
    """
    result = []
    for lesson in plan["lessons"]:
        evidence, missing = [], []
        for source_id in lesson["source_lesson_ids"]:
            row = rows.get(source_id)
            state = row.get("state", {}) if row else {}
            if isinstance(state, str):
                state = json.loads(state)
            require(isinstance(state, dict), "Malformed source state")
            legacy = state.get("legacy_completion") or {}
            complete = (state.get("check") or {}).get("complete") is True
            if legacy:
                # A promoted row's current version alone does not review its older completion.
                complete = (legacy.get("complete") is True and legacy.get("source_version") in reviewed_versions
                            and bool(re.fullmatch(r"[0-9a-f]{64}", legacy.get("archive_fingerprint", ""))))
            if row and row["version"] in reviewed_versions and complete:
                evidence.append({"lesson_id": source_id, "version": row["version"],
                                 "revision": row["revision"], "row_sha256": digest(row)})
            else:
                missing.append(source_id)
        result.append({"lesson_id": lesson["id"], "completion_eligible": not missing,
                       "missing_completion_evidence": missing, "source_evidence": evidence,
                       "publication_eligible": all(s in published_source_ids for s in lesson["source_lesson_ids"])})
    return result


def resolve_saved_location(plan, namespace, fragment):
    """Only exact known aliases; caller must supply the origin/route edition."""
    return next((a["destination"] for a in plan["aliases"]
                 if a["namespace"] == namespace and a["path"] == fragment), None)


def verify_learn_builder(learn_root, source_root, catalog, snapshot):
    """Compare actual source-built advanced pages across both builders, without import."""
    spec = importlib.util.spec_from_file_location(
        "learn_source_builder", learn_root / "scripts/build_network_foundations.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    learned = builder.build(source_root, catalog["version"].removeprefix("network-"), "preflight")
    actual = {l["id"]: l["pages"] for l in learned["lessons"]}
    expected = {l["id"]: l["pages"] for l in catalog["lessons"]}
    for source in snapshot["sources"]:
        require(actual[source["lesson_id"]] == expected[source["lesson_id"]],
                f"Learn/content builder Pages differ: {source['lesson_id']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--learn-root", type=Path, help="Also compare a reviewed Learn checkout; read only")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    contract = json.loads((ROOT / "docs/advanced-restructure-contract.json").read_text())
    snapshot = json.loads((ROOT / "docs" / contract["snapshot"]).read_text())
    catalog = json.loads(args.catalog.read_text())
    legacy = contract["learn_legacy_units"]
    if args.learn_root:
        legacy = json.loads((args.learn_root / "backend/network_legacy_units.json").read_text())
        verify_learn_builder(args.learn_root, ROOT, catalog, snapshot)
    plan = make_plan(snapshot, contract, catalog, legacy)
    plan["learn_builder_verified"] = bool(args.learn_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"mode": plan["mode"], "runtime_ready": False, **plan["counts"]}))


if __name__ == "__main__":
    main()
