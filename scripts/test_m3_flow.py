import unittest
from pathlib import Path

from build_course import markdown_pages

ROOT = Path(__file__).resolve().parents[1] / "exercises/module/3/unit"


class M3FlowTest(unittest.TestCase):
    def test_answers_render_in_exercise_pages(self):
        lessons = {"01": ("02", "03", "05", "06", "07", "08", "09", "10"),
                   "02": ("03", "04", "06", "07", "08")}
        for unit, ids in lessons.items():
            for lesson in ids:
                with self.subTest(unit=unit, lesson=lesson):
                    pages = markdown_pages(ROOT / unit / "lesson" / lesson / "lesson.md")
                    answers = [p["html"] for p in pages if 'class="exercise-answer"' in p["html"]]
                    self.assertEqual(len(answers), 1)
                    self.assertIn("<summary>정답과 해설 보기</summary>", answers[0])
                    self.assertIn("<code", answers[0])

    def test_core_records_preserve_checklist_and_hide_optional_pages(self):
        for unit, original, core in (("01", "12", "15"), ("02", "10", "13")):
            with self.subTest(unit=unit):
                source = markdown_pages(ROOT / unit / "lesson" / original / "lesson.md")
                copy = markdown_pages(ROOT / unit / "lesson" / core / "lesson.md")
                self.assertEqual(copy[0].get("checklist"), source[0].get("checklist"))
                self.assertTrue(all(not p["title"].startswith("응용") for p in copy))
                self.assertTrue(any(p["title"].startswith("응용") for p in source))


if __name__ == "__main__":
    unittest.main()
