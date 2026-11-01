import importlib.util
import tempfile
import unittest
from pathlib import Path

import yaml

SPEC = importlib.util.spec_from_file_location("build_course", Path(__file__).with_name("build_course.py"))
bc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bc)

LESSONS = [("l1", ["host-def", None]), ("l2", ["router-def"])]
HERO = {"id": "host", "tier": "hero", "category": "등장인물", "emoji": "🏠", "ko": "호스트",
        "aliases": ["호스트"], "anchor": {"lesson": "l1", "page": "host-def"}}


def run(*entries, lessons=LESSONS):
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "glossary").mkdir()
        (Path(tmp) / "glossary" / "terms.yaml").write_text(yaml.safe_dump(list(entries), allow_unicode=True), encoding="utf-8")
        return bc.build_glossary(Path(tmp), lessons)


class GlossaryTests(unittest.TestCase):
    def bad(self, expected, *entries):
        with self.assertRaisesRegex(ValueError, expected):
            run(*entries)

    def test_ok_resolves_family_anchor_index_and_order(self):
        family = {"id": "server", "tier": "family", "parent": "host", "ko": "서버", "aliases": ["서버"],
                  "anchor": {"lesson": "l2", "page": "router-def"}}
        glossary, _ = run(HERO, family)
        self.assertEqual((glossary[1]["emoji"], glossary[1]["category"]), ("🏠", "등장인물"))
        self.assertEqual(glossary[1]["anchor"]["page_index"], 1)
        self.assertEqual((glossary[0]["order"], glossary[1]["order"]), (1, 3))

    def test_no_file_means_no_glossary(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(bc.build_glossary(Path(tmp), LESSONS))

    def test_rejects_duplicate_id(self):
        self.bad("duplicate id", HERO, dict(HERO, emoji="🏪", aliases=[]))

    def test_rejects_duplicate_or_zwj_emoji(self):
        self.bad("already used", HERO, dict(HERO, id="b", aliases=[]))
        self.bad("ZWJ", dict(HERO, emoji="👨‍💻"))

    def test_rejects_bad_parent(self):
        for parent in ("missing", "plain"):
            with self.subTest(parent=parent):
                plain = {"id": "plain", "tier": "none", "ko": "x"}
                self.bad("not a hero", HERO, plain, {"id": "f", "tier": "family", "parent": parent,
                                                     "anchor_hint": {"lesson": "l1"}})

    def test_rejects_unknown_page_id_and_lesson(self):
        self.bad("does not match", dict(HERO, anchor={"lesson": "l1", "page": "nope"}))
        self.bad("unknown Lesson", dict(HERO, not_in=["nope"]))

    def test_alias_collision_depends_on_scope(self):
        other = {"id": "sw", "tier": "none", "ko": "x", "aliases": ["호스트"]}
        self.bad("collides", HERO, other)
        run(dict(HERO, only_in=["l1"]), dict(other, only_in=["l2"]))
        run(HERO, dict(other, not_in=["l1", "l2"]))

    def test_term_exclude_passes_through_page_metadata(self):
        self.assertEqual(bc.page_term_exclude({"term_exclude": ["switch"]}), {"term_exclude": ["switch"]})
        self.assertEqual(bc.page_term_exclude({}), {})


if __name__ == "__main__":
    unittest.main()
