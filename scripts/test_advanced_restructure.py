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
        cls.catalog = build_course.build(sha, "synthetic preflight")
        cls.version = cls.catalog["version"]
        cls.plan = cls.create_plan()
        cls.by_key = {l["target_key"]: l for l in cls.plan["lessons"]}

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
        self.assertEqual(self.plan["counts"]["source_assets"], 22)
        self.assertEqual(self.plan["counts"]["source_catalog_pages"], 462)
        self.assertEqual(self.plan["counts"]["aliases_by_namespace"], {
            "content-stage-14": 462, "learn-v2": 462, "learn-unversioned": 456})
        self.assertFalse(self.plan["runtime_ready"])

    def test_resources_are_separate_and_not_required(self):
        resources = self.plan["resources"]
        self.assertEqual([8, 1], [len(r["pages"]) for r in resources])
        self.assertFalse(any(r["required"] for r in resources))
        self.assertFalse({r["id"] for r in resources} & {l["id"] for l in self.plan["lessons"]})
        self.assertEqual(len(resources[1]["links"]), 2)
        self.assertEqual(resources[1]["links"], self.snapshot["resources"][1]["links"])

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

    def test_guide_and_material_bookmarks_reach_resources(self):
        for lesson, page, resource in [(1, 8, "advanced-guide"), (4, 1, "advanced-materials")]:
            mapped = resolve_saved_location(self.plan, "learn-v2",
                f"/m2-network/v2/unit/11/lesson/{lesson}/page/{page}")
            self.assertEqual((mapped["kind"], mapped["id"], mapped["page"]), ("resource", resource, page))

    def test_stage_and_learn_unversioned_are_different_namespaces(self):
        path = "/m2-network/unit/7/lesson/1/page/1"
        stage = resolve_saved_location(self.plan, "content-stage-14", path)
        learn = resolve_saved_location(self.plan, "learn-unversioned", path)
        self.assertNotEqual(stage["id"], learn["id"])
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
