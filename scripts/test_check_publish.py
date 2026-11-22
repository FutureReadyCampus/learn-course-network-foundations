import contextlib
import importlib.util
import io
import os
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "check_publish", os.path.join(ROOT, "portfolio-starter", "check_publish.py"))
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

# 가짜 키는 조각을 이어 붙여 만든다(소스 스캐너 회피).
AWS = "AKI" + "A" + "A" * 16
EMAIL = "me" + "@" + "example.com"


def run(files):
    with tempfile.TemporaryDirectory() as d:
        for name, body in files.items():
            path = os.path.join(d, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(body)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = cp.main([d])
        return code, buf.getvalue()


class CheckPublishTest(unittest.TestCase):
    def test_key_is_error_and_masked(self):
        code, out = run({"a.py": 'key = "%s"\n' % AWS})
        self.assertEqual(code, 1)
        self.assertIn("[오류]", out)
        self.assertIn("a.py:1", out)
        self.assertIn("AKIA***", out)
        self.assertNotIn(AWS, out)

    def test_assignment_and_env_file(self):
        secret = "x" * 30
        code, out = run({"b.txt": "MY_" + "TOKEN = " + secret + "\n", ".env": "A=1\n"})
        self.assertEqual(code, 1)
        self.assertNotIn(secret, out)
        self.assertIn("오류 2건", out)

    def test_clean_and_env_example(self):
        code, out = run({"a.md": "안녕하세요\n", ".env.example": "API_" + "KEY=\n"})
        self.assertEqual(code, 0)
        self.assertIn("오류 0건, 주의 0건", out)

    def test_ignore_comment(self):
        code, _ = run({"a.py": 'k = "%s"  # check_publish: ignore\n' % AWS})
        self.assertEqual(code, 0)

    def test_email_is_warning_only(self):
        code, out = run({"a.md": "문의: %s\n" % EMAIL})
        self.assertEqual(code, 0)
        self.assertIn("[주의]", out)
        self.assertNotIn(EMAIL, out)

    def test_module_folder_is_scanned_and_pycache_skipped(self):
        # 실습 폴더(access_control/)가 포트폴리오와 같은 저장소에 있으므로 함께 점검된다.
        code, out = run({"access_control/config/users.json": '{"k": "%s"}\n' % AWS,
                         "access_control/__pycache__/x.py": 'k = "%s"\n' % AWS})
        self.assertEqual(code, 1)
        self.assertIn(os.path.join("access_control", "config", "users.json") + ":1", out)
        self.assertIn("오류 1건", out)

    def test_config_placeholder_warns(self):
        code, out = run({"_config.yml": "author: 내 이름\n"})
        self.assertEqual(code, 0)
        self.assertIn("주의 1건", out)


if __name__ == "__main__":
    unittest.main()
