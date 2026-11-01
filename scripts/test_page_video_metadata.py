import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("build_course.py")
SPEC = importlib.util.spec_from_file_location("build_course", MODULE_PATH)
build_course = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_course)


class PageVideoMetadataTests(unittest.TestCase):
    def test_video_follows_page_id_in_authored_pages_when_heading_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lesson.md"
            path.write_text(
                "---\ntitle: Lesson\nconcepts: []\npages:\n  - concepts: []\n  - concepts: []\n"
                "page_metadata:\n  - page_id: stable-video-page\n    video:\n"
                "      video_id: vBrQ3yzerMg\n      title: Video\n---\n"
                "## First page\n\nFirst text.\n\n"
                "## Renamed second page\n<!-- learn-page-id: stable-video-page -->\n\nSecond text.",
                encoding="utf-8",
            )

            pages = build_course.reading_pages(path, build_course.read_front_matter(path)[0], {})

        self.assertNotIn("video", pages[0])
        self.assertEqual(pages[1]["video"]["video_id"], "vBrQ3yzerMg")
        self.assertEqual(pages[1]["title"], "Renamed second page")
        self.assertEqual(pages[1]["paragraphs"], ["Second text."])

    def test_video_follows_page_id_when_title_and_order_change(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lesson.md"
            path.write_text(
                "## Another page\n\nOther text.\n\n"
                "## Renamed Wireshark page\n<!-- learn-page-id: wireshark-packet-inspection -->\n\nPacket practice.",
                encoding="utf-8",
            )
            metadata = [{"page_id": "wireshark-packet-inspection", "video": {
                "video_id": "vBrQ3yzerMg", "title": "Wireshark intro", "creator": "따라하면서 배우는 IT",
                "duration_seconds": 512,
            }}]

            pages = build_course.reading_pages(path, {"title": "Lesson", "page_metadata": metadata}, {})

        self.assertNotIn("video", pages[0])
        self.assertEqual(pages[1]["video"]["video_id"], "vBrQ3yzerMg")
        self.assertEqual(pages[1]["title"], "Renamed Wireshark page")
        self.assertEqual(pages[1]["paragraphs"], ["Packet practice."])

    def test_rejects_invalid_youtube_id_and_unknown_page_id(self):
        for video_id, expected in [("bad", "11-character"), ("vBrQ3yzerMg", "unknown page_id")]:
            with self.subTest(video_id=video_id), tempfile.TemporaryDirectory() as temporary:
                path = Path(temporary) / "lesson.md"
                path.write_text("## One\n<!-- learn-page-id: known-page -->\n\nText.", encoding="utf-8")
                page_id = "missing-page" if expected == "unknown page_id" else "known-page"
                metadata = [{"page_id": page_id, "video": {"video_id": video_id, "title": "Intro"}}]
                with self.assertRaisesRegex(ValueError, expected):
                    build_course.reading_pages(path, {"title": "Lesson", "page_metadata": metadata}, {})

    def test_rejects_duplicate_markers(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lesson.md"
            path.write_text(
                "## One\n<!-- learn-page-id: duplicate-page -->\n\nText.\n\n"
                "## Two\n<!-- learn-page-id: duplicate-page -->\n\nMore.",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Duplicate learn-page-id"):
                build_course.reading_pages(path, {"title": "Lesson", "page_metadata": []}, {})


if __name__ == "__main__":
    unittest.main()
