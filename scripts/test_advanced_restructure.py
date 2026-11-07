#!/usr/bin/env python3
"""Synthetic preflight checks only; no learner database or runtime catalog writes."""

import copy
import json
import subprocess
import unittest

import build_course
from plan_advanced_restructure import (
    ROOT,
    completion_preflight,
    make_plan,
    resolve_saved_location,
)


class AdvancedRestructureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads((ROOT / "docs/advanced-restructure-contract.json").read_text())
        cls.snapshot = json.loads((ROOT / "docs/advanced-restructure-snapshot.json").read_text())
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        current = build_course.build(sha, "synthetic preflight")
        cls.applied_catalog = current
        cls.catalog = cls.source_catalog(current)
        cls.version = cls.catalog["version"]
        cls.plan = cls.create_plan()
        cls.by_key = {l["target_key"]: l for l in cls.plan["lessons"]}

    @classmethod
    def source_catalog(cls, current):
        """Rebuild the audited 14-Unit source edition from preserved originals."""
        if len(current["units"]) == 14:
            return current
        basics = [unit for unit in current["units"] if unit["id"] not in {
            "network-devices", "router-and-nat", "load-balancing", "vpn-and-security",
            "network-security-solutions",
        }]
        basic_ids = {unit["id"] for unit in basics}
        lessons = [lesson for lesson in current["lessons"] if lesson["unit"] in basic_ids]
        course_meta = __import__("yaml").safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))
        advanced_unit_ids = {11: "network-devices", 12: "router-and-nat",
                             13: "load-balancing", 14: "vpn-and-security"}
        for source in cls.snapshot["sources"]:
            match = __import__("re").fullmatch(r"U(\d+)L(\d+)", source["source_key"])
            if not match:
                raise AssertionError(f"Unexpected source key: {source['source_key']}")
            unit_number = int(match.group(1))
            if unit_number not in advanced_unit_ids:
                continue
            path = ROOT / source["path"]
            metadata, _ = build_course.read_front_matter(path)
            lessons.append({"id": metadata["id"], "unit": advanced_unit_ids[unit_number],
                            "title": metadata["title"], "pages": build_course.reading_pages(
                                path, metadata, course_meta.get("animation_assets", {}))})
        lessons.sort(key=lambda lesson: (
            next((i for i, unit in enumerate(basics + [
                {"id": advanced_unit_ids[n]} for n in range(11, 15)
            ]) if unit["id"] == lesson["unit"]), 99),
            int(next((s["source_key"].split("L")[1] for s in cls.snapshot["sources"]
                      if s["lesson_id"] == lesson["id"]), "0"))
            if lesson["unit"] in advanced_unit_ids.values() else 0,
        ))
        units = basics + [{"id": "network-devices", "title": "심화 네트워크 장치의 구조"},
                          {"id": "router-and-nat", "title": "심화 인터넷 공유기 작동원리"},
                          {"id": "load-balancing", "title": "심화 부하분산 시스템 작동원리"},
                          {"id": "vpn-and-security", "title": "심화 VPN과 네트워크 보안 솔루션"}]
        return {"version": f"network-{cls.snapshot['content_source_sha']}",
                "units": units, "lessons": lessons}

    @classmethod
    def create_plan(cls, contract=None, catalog=None):
        return make_plan(cls.snapshot, contract or cls.contract, catalog or cls.catalog,
                         cls.contract["learn_legacy_units"])

    def evaluate(self, rows=None, published=None):
        return {r["lesson_id"]: r for r in completion_preflight(
            self.plan, rows or {}, published or [], {self.version})}

    def completed_row(self):
        return {"version": self.version, "revision": 7,
                "state": json.dumps({"check": {"complete": True}})}

    def test_all_source_pages_and_assets_are_preserved(self):
        self.assertEqual([6, 9, 10, 20, 5, 9, 11, 24, 8, 8, 7, 4, 11, 9, 13, 20, 5, 4, 4, 7],
                         [len(l["pages"]) for l in self.plan["lessons"]])
        self.assertEqual(self.plan["counts"]["technical_pages"], 194)
        self.assertEqual(self.plan["counts"]["excluded_pages"], 9)
        self.assertEqual(self.plan["counts"]["source_assets"], 22)
        self.assertEqual(self.plan["counts"]["source_catalog_pages"], 462)
        self.assertEqual(self.plan["counts"]["aliases_by_namespace"], {
            "content-stage-14": 453, "learn-v2": 453, "learn-unversioned": 447})
        self.assertFalse(self.plan["runtime_ready"])

    def test_applied_course_has_fifteen_units_and_twenty_advanced_lessons(self):
        unit_ids = [unit["id"] for unit in self.applied_catalog["units"]]
        self.assertEqual(len(unit_ids), 15)
        self.assertEqual(unit_ids[10:], ["network-devices", "router-and-nat", "load-balancing",
                                         "vpn-and-security", "network-security-solutions"])
        advanced_ids = [lesson["id"] for lesson in self.applied_catalog["lessons"]
                        if lesson["unit"] in set(unit_ids[10:])]
        self.assertEqual(advanced_ids, [item["id"] for item in self.plan["lessons"]])
        self.assertEqual(sum(len(lesson["pages"]) for lesson in self.applied_catalog["lessons"]
                             if lesson["unit"] in set(unit_ids[10:])), 194)
        self.assertEqual(len(self.applied_catalog["route_aliases"]), 1353)
        self.assertEqual(self.applied_catalog["advanced_completion_migration"], {
            "schema": "network-advanced-completion-v1",
            "from_version": "network-b01c8869a5d35f0cf79d827a49d32d4ce51d99ed",
            "target_unit_ids": ["network-devices", "router-and-nat", "load-balancing",
                                "vpn-and-security", "network-security-solutions"],
            "aliases_sha256": "c6eb0ea44764cc45335415cb1e240d0667f4cf387ec496d5e703b77d412c9927",
        })

    def test_guide_and_print_material_are_excluded_from_the_new_course(self):
        excluded = set(self.plan["excluded_source_lessons"])
        self.assertEqual(excluded, {
            "u7-advanced-01-강의소개-및-교육목표",
            "u7-advanced-04-강의자료-인쇄용",
        })
        self.assertFalse(any(alias["source_lesson_id"] in excluded for alias in self.plan["aliases"]))
        self.assertTrue(all(lesson["id"] not in excluded for lesson in self.plan["lessons"]))

    def test_unchanged_ids_survive_and_composite_ids_are_new(self):
        old_ids = {s["lesson_id"] for s in self.snapshot["sources"]}
        self.assertEqual(sum(l["identity"] == "preserved" for l in self.plan["lessons"]), 11)
        for lesson in self.plan["lessons"]:
            self.assertEqual(lesson["id"] in old_ids, lesson["identity"] == "preserved")

    def test_merged_page_offsets_do_not_open_wrong_source(self):
        for old_page, new_page in [(1, 8), (2, 9), (7, 14)]:
            mapped = resolve_saved_location(self.plan, "learn-v2",
                f"/m2-network/v2/unit/11/lesson/7/page/{old_page}")
            self.assertEqual(mapped["id"], "advanced-forward-proxy")
            self.assertEqual(mapped["page"], new_page)

    def test_split_boundaries_and_reference_pages(self):
        for old_page, target, new_page in [(5, "advanced-security-placement", 5),
                (6, "advanced-network-access-control", 1), (9, "advanced-network-access-control", 4),
                (10, "advanced-stateful-firewall", 1), (13, "advanced-stateful-firewall", 4),
                (14, "advanced-intrusion-and-logs", 1), (20, "advanced-intrusion-and-logs", 7)]:
            mapped = resolve_saved_location(self.plan, "learn-v2",
                f"/m2-network/v2/unit/14/lesson/5/page/{old_page}")
            self.assertEqual((mapped["id"], mapped["page"]), (target, new_page))
        for page in [10, 11]:
            mapped = resolve_saved_location(self.plan, "learn-v2",
                f"/m2-network/v2/unit/13/lesson/1/page/{page}")
            self.assertEqual(mapped["id"], "advanced-service-redundancy")

    def test_guide_and_print_material_bookmarks_are_not_redirected_into_learning_pages(self):
        for lesson, page in [(1, 8), (4, 1)]:
            mapped = resolve_saved_location(self.plan, "learn-v2",
                f"/m2-network/v2/unit/11/lesson/{lesson}/page/{page}")
            self.assertIsNone(mapped)

    def test_stage_and_learn_unversioned_are_different_namespaces(self):
        path = "/m2-network/unit/7/lesson/1/page/1"
        stage = resolve_saved_location(self.plan, "content-stage-14", path)
        learn = resolve_saved_location(self.plan, "learn-unversioned", path)
        # This legacy slot belonged to the removed introduction; don't silently
        # point it at the unrelated Lesson occupying the same numeric slot now.
        self.assertIsNotNone(stage)
        self.assertIsNone(learn)
        self.assertIsNone(resolve_saved_location(self.plan, "unknown", path))
        self.assertIsNone(resolve_saved_location(self.plan, "learn-v2",
                            "/m2-network/v2/unit/11/lesson/7/page/999"))

    def test_no_row_empty_quizzes_and_cursor_never_prove_completion(self):
        self.assertFalse(any(x["completion_eligible"] for x in self.evaluate().values()))
        lesson = self.by_key["u11-l04"]
        rows = {s: {"version": self.version, "revision": 0, "state": {
            "page_mastery": {"required": [], "passed": []}, "step": 20}}
            for s in lesson["source_lesson_ids"]}
        self.assertFalse(self.evaluate(rows)[lesson["id"]]["completion_eligible"])

    def test_partial_merge_and_partial_publication_do_not_expand(self):
        lesson = self.by_key["u11-l04"]
        sources = lesson["source_lesson_ids"]
        rows = {sources[0]: self.completed_row()}
        before = copy.deepcopy(rows)
        result = self.evaluate(rows, sources[:1])[lesson["id"]]
        self.assertFalse(result["completion_eligible"])
        self.assertFalse(result["publication_eligible"])
        self.assertEqual(len(result["missing_completion_evidence"]), 2)
        self.assertEqual(rows, before)
        rows.update({s: self.completed_row() for s in sources[1:]})
        result = self.evaluate(rows, sources)[lesson["id"]]
        self.assertTrue(result["completion_eligible"])
        self.assertTrue(result["publication_eligible"])
        self.assertEqual(len(result["source_evidence"]), 3)

    def test_explicit_whole_completion_can_cover_unchanged_split_ranges(self):
        source = self.by_key["u15-l01"]["source_lesson_ids"][0]
        rows = {source: self.completed_row()}
        result = self.evaluate(rows, [source])
        for key in ["u15-l01", "u15-l02", "u15-l03", "u15-l04"]:
            self.assertTrue(result[self.by_key[key]["id"]]["completion_eligible"])
        rows[source]["version"] = "network-" + "0" * 40
        result = self.evaluate(rows)
        self.assertFalse(result[self.by_key["u15-l01"]["id"]]["completion_eligible"])

    def test_changed_content_and_duplicate_targets_fail_closed(self):
        changed = copy.deepcopy(self.catalog)
        source_id = self.snapshot["sources"][0]["lesson_id"]
        source = next(l for l in changed["lessons"] if l["id"] == source_id)
        source["pages"][0]["paragraphs"].append("unreviewed change")
        with self.assertRaisesRegex(ValueError, "Page changed"):
            self.create_plan(catalog=changed)
        changed = copy.deepcopy(self.contract)
        changed["lesson_ids"][1]["lesson_id"] = changed["lesson_ids"][0]["lesson_id"]
        with self.assertRaisesRegex(ValueError, "Duplicate target"):
            self.create_plan(contract=changed)

    def test_basic_bookmarks_keep_lesson_and_page(self):
        basic_ids = {l["id"] for l in self.catalog["lessons"] if l["unit"] in
                     {u["id"] for u in self.catalog["units"][:10]}}
        for alias in self.plan["aliases"]:
            if alias["namespace"] == "learn-v2" and alias["source_lesson_id"] in basic_ids:
                self.assertEqual(alias["destination"]["id"], alias["source_lesson_id"])
                self.assertEqual(alias["destination"]["page"], alias["source_page"])

    def test_unreviewed_source_reordering_is_rejected(self):
        changed = copy.deepcopy(self.catalog)
        changed["lessons"][-1], changed["lessons"][-2] = changed["lessons"][-2], changed["lessons"][-1]
        with self.assertRaisesRegex(ValueError, "Source positions changed"):
            self.create_plan(catalog=changed)

    def test_legacy_completion_requires_reviewed_origin_and_archive_evidence(self):
        lesson = self.by_key["u15-l01"]
        source = lesson["source_lesson_ids"][0]
        state = {"check": {"complete": True}, "legacy_completion": {
            "complete": True, "source_version": "network-" + "0" * 40,
            "archive_fingerprint": "a" * 64}}
        row = {"version": self.version, "revision": 2, "state": state}
        self.assertFalse(self.evaluate({source: row})[lesson["id"]]["completion_eligible"])
        state["legacy_completion"]["source_version"] = self.version
        self.assertTrue(self.evaluate({source: row})[lesson["id"]]["completion_eligible"])
        state["legacy_completion"].pop("archive_fingerprint")
        self.assertFalse(self.evaluate({source: row})[lesson["id"]]["completion_eligible"])


if __name__ == "__main__":
    unittest.main()
