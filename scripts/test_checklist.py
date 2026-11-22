import tempfile, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_course import markdown_pages

LESSON = """---
id: t-l01
title: 테스트
render: markdown
---

# 테스트

## 첫 쪽

본문입니다.

<!-- checklist -->
- [ ] `users.json` 파일을 만들고 붙여 넣었다
- [ ] **실행**했더니 `6` 이 나왔다
<!-- /checklist -->

## 둘째 쪽

<!-- checklist optional -->
- [ ] 여유가 되면 해 본다
<!-- /checklist -->

## 셋째 쪽

체크리스트가 없는 쪽입니다.

## 넷째 쪽

순서 1.

<!-- checklist -->
- [ ] 하나
<!-- /checklist -->

순서 2.

<!-- checklist -->
- [ ] 둘
- [ ] 셋
<!-- /checklist -->
"""


class ChecklistTest(unittest.TestCase):
    def test_extract(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "lesson.md"
            p.write_text(LESSON, encoding="utf-8")
            pages = markdown_pages(p, {})
        first, second, third, fourth = pages
        self.assertEqual(len(first["checklist"]["items"]), 2)
        self.assertFalse(first["checklist"]["optional"])
        self.assertIn("<code>users.json</code>", first["checklist"]["items"][0])
        self.assertIn("<strong>실행</strong>", first["checklist"]["items"][1])
        self.assertNotIn("checklist", first["html"])
        self.assertIn('data-start="0" data-count="2"', first["html"])  # 자리표시는 블록 위치에 남는다
        self.assertNotIn("users.json", first["html"])  # 본문 HTML 에는 중복해서 나오지 않는다
        self.assertTrue(second["checklist"]["optional"])
        self.assertNotIn("checklist", third)
        self.assertEqual(len(fourth["checklist"]["items"]), 3)
        self.assertIn('data-start="0" data-count="1"', fourth["html"])
        self.assertIn('data-start="1" data-count="2"', fourth["html"])
        self.assertLess(fourth["html"].index("순서 1"), fourth["html"].index('data-start="0"'))
        self.assertLess(fourth["html"].index('data-start="0"'), fourth["html"].index("순서 2"))


if __name__ == "__main__":
    unittest.main()
