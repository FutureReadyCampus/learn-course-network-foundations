import importlib.util
import tempfile
import unittest
import warnings
from pathlib import Path

import yaml

SPEC = importlib.util.spec_from_file_location("build_course", Path(__file__).with_name("build_course.py"))
bc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bc)

LESSONS = [("l1", ["host-def", None], ["Host", "More"], "Host 호스트"),
           ("l2", ["router-def"], ["Router"], "Router 라우터 서버")]
HERO = {"id": "host", "tier": "hero", "category": "등장인물", "emoji": "🏠", "ko": "호스트",
        "aliases": ["호스트"], "anchor": {"lesson": "l1", "page": "host-def"}}


def run(*entries, lessons=LESSONS, quiet=True):
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "glossary").mkdir()
        (Path(tmp) / "glossary" / "terms.yaml").write_text(yaml.safe_dump(list(entries), allow_unicode=True), encoding="utf-8")
        if quiet:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                return bc.build_glossary(Path(tmp), lessons)
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

    def test_warns_for_recent_emoji_and_missing_anchor_alias(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            run(dict(HERO, emoji="🫨", aliases=["absent"]), quiet=False)
        messages = [str(item.message) for item in caught]
        self.assertTrue(any("Unicode 13" in message for message in messages))
        self.assertTrue(any("no alias" in message for message in messages))

    def test_rejects_combined_aliases(self):
        for alias in ("게이트웨이·기본 게이트웨이", "GET, POST"):
            with self.subTest(alias=alias):
                self.bad("combines multiple terms", dict(HERO, aliases=[alias]))

    def test_rejects_bad_parent(self):
        for parent in ("missing", "plain"):
            with self.subTest(parent=parent):
                plain = {"id": "plain", "tier": "none", "ko": "x"}
                self.bad("not a hero", HERO, plain, {"id": "f", "tier": "family", "parent": parent,
                                                     "anchor_hint": {"lesson": "l1"}})

    def test_rejects_unknown_page_id_and_lesson(self):
        self.bad("does not match", dict(HERO, anchor={"lesson": "l1", "page": "nope"}))
        self.bad("does not match", dict(HERO, anchor={"lesson": ["l1"], "page": "host-def"}))
        self.bad("unknown Lesson", dict(HERO, not_in=["nope"]))

    def test_anchor_hint_page_title_sets_order_and_warns(self):
        term = dict(HERO, anchor=None, anchor_hint={"lesson": "l1", "page_title": "More"})
        with self.assertWarnsRegex(UserWarning, "anchor_hint"):
            glossary, _ = run(term, quiet=False)
        self.assertEqual(glossary[0]["order"], 2)

    def test_anchor_switch_requires_page_id(self):
        previous = bc.GLOSSARY_ANCHORS_REQUIRED
        bc.GLOSSARY_ANCHORS_REQUIRED = True
        try:
            with self.assertRaisesRegex(ValueError, "replace it with a Page ID anchor"):
                run(dict(HERO, anchor=None, anchor_hint={"lesson": "l1", "page_title": "Host"}))
        finally:
            bc.GLOSSARY_ANCHORS_REQUIRED = previous

    def test_rejects_anchor_hint_for_unknown_page_title(self):
        term = dict(HERO, anchor=None, anchor_hint={"lesson": "l1", "page_title": "Missing"})
        with self.assertRaisesRegex(ValueError, "unknown Page title"):
            run(term)

    def test_alias_collision_depends_on_scope(self):
        other = {"id": "sw", "tier": "none", "ko": "x", "aliases": ["호스트"]}
        self.bad("collides", HERO, other)
        run(dict(HERO, only_in=["l1"]), dict(other, only_in=["l2"]))
        run(HERO, dict(other, not_in=["l1", "l2"]))

    def test_term_exclude_passes_through_page_metadata(self):
        self.assertEqual(bc.page_term_exclude({"term_exclude": ["switch"]}), {"term_exclude": ["switch"]})
        self.assertEqual(bc.page_term_exclude({}), {})

    def test_page_id_lookup_uses_grouped_page_order(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lesson.md"
            path.write_text(
                "---\ntitle: Grouped\npage_groups:\n  - title: Combined\n    sections: [1, 2]\n"
                "  - title: Last\n    sections: [3]\n---\n"
                "## First\n<!-- learn-page-id: first -->\n\nOne.\n"
                "## Second\n\nTwo.\n## Third\n<!-- learn-page-id: third -->\n\nThree.",
                encoding="utf-8",
            )
            ids, titles, _ = bc.lesson_page_ids(path)
        self.assertEqual(ids, ["first", "third"])
        self.assertEqual(titles, ["Combined", "Last"])

    def test_grouped_anchor_index_matches_reader_page_order(self):
        term = dict(HERO, anchor={"lesson": "l1", "page": "third"})
        lessons = [("l1", ["first", "third"], ["Combined", "Last"], "호스트")]
        glossary, _ = run(term, lessons=lessons)
        self.assertEqual(glossary[0]["anchor"]["page_index"], 2)

    def test_term_exclude_is_included_on_the_output_page(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lesson.md"
            path.write_text(
                "---\ntitle: Lesson\npage_metadata:\n  - page_id: host-def\n    term_exclude: [host]\n---\n"
                "## Host\n<!-- learn-page-id: host-def -->\n\nHost.",
                encoding="utf-8",
            )
            metadata, _ = bc.read_front_matter(path)
            page = bc.reading_pages(path, metadata, {})[0]
        self.assertEqual(page["term_exclude"], ["host"])

    def test_rejects_term_exclude_unknown_id(self):
        with self.assertRaisesRegex(ValueError, "unknown term"):
            bc.validate_term_excludes([("l1", ["missing"])], {"host"})


if __name__ == "__main__":
    unittest.main()
