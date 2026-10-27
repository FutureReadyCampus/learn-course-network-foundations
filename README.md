# learn-course-network-foundations
Markdown source for the Network Foundations course served by Learn

## Unit 1 local preview

The Markdown files are the source. Generate the Learn catalog with:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/build_course.py
```

This writes `preview/learn-network-course.json`. Treat that file as generated output; edit the Unit and Lesson Markdown instead. The current pilot exports only Lessons that have a `lesson.md` and at least one file in `steps/`.
