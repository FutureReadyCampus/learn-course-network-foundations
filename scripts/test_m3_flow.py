import html
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

    def test_blog_record_pages_are_single_flow(self):
        for unit, core in (("01", "15"), ("02", "13")):
            with self.subTest(unit=unit):
                pages = markdown_pages(ROOT / unit / "lesson" / core / "lesson.md")
                self.assertEqual(len(pages), 5)
                rendered = html.unescape("\n".join(page["html"] for page in pages))
                self.assertNotIn("응용", rendered)
                self.assertNotIn("report_u", rendered)
                self.assertIn("_posts", rendered)
                for heading in ("문제", "선택과 이유", "검증 결과"):
                    self.assertIn(f"## {heading}\n", rendered)
                self.assertIn("python check_publish.py", rendered)
                self.assertIn("git push", rendered)
                self.assertNotIn("이번 Unit 마무리", rendered)
                self.assertTrue(any(page.get("checklist") for page in pages))



if __name__ == "__main__":
    unittest.main()
