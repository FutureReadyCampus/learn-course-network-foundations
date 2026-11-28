# 네트워크 실습 노트

접근 권한, 로그 분석, 자동 대응을 공부하며 내린 판단과 확인한 결과를 기록하는 포트폴리오입니다. 실습 폴더와 포트폴리오(Jekyll) 파일이 이 저장소 하나에 함께 있고, GitHub Pages(Jekyll, 기본 빌드)로 공개합니다. 별도 Action이나 설치 없이 동작합니다.

안내: 코스의 Module 3 Unit 1 「시작하기」 → 「저장소를 만들고 내려받아 작업 폴더 열기」 페이지 (<https://futurereadycampus.github.io/learn-course-network-foundations/exercises/module/3/unit/1/lesson/1/page/3>)

## 파일 구성

| 이름 | 설명 |
|---|---|
| `_config.yml` | 사이트 이름·주소 설정 |
| `index.md` | 첫 화면(소개, 대표 글, 전체 글) |
| `about.md` | 소개 페이지 |
| `_posts/` | 글 |
| `_templates/` | 글 틀 |
| `access_control/` · `anomaly_detection/` · `soar_response/` | Module 3 · 4 · 5 실습 폴더(코드) |
| `assets/images/` | 글에 넣는 이미지 |
| `check_publish.py` | 공개 전 점검 스크립트 |

## 소개와 글 게시하기

1. `_config.yml`: `title`, `description`, `author`, `baseurl`을 내 것으로 바꿉니다(`url`은 비워 둡니다). (`← 내 것으로 바꾸기` 표시)
2. `description`에 관심 분야와 글을 쓰는 이유를 두 문장으로 적습니다. 이 문장은 홈과 소개 페이지에 표시됩니다.
3. 첫 글을 쓸 때 `_posts/` 폴더에 날짜와 주제가 담긴 Markdown 파일을 만듭니다. 대표로 고를 때는 머리말에 `featured: true`와 선택 이유·확인 결과를 담은 `summary` 한 줄을 적으세요.

## Pages 켜기

1. 이 파일들을 내 공개(Public) 저장소의 `main` 브랜치에 올립니다.
2. 저장소의 **Settings > Pages**로 갑니다.
3. **Source**는 **Deploy from a branch**, **Branch**는 `main`과 `/ (root)`를 고르고 **Save**를 누릅니다.
4. 1~2분 뒤 `https://<내 아이디>.github.io/<저장소 이름>/` 주소를 엽니다.

실습 폴더의 `.py` · `.json` 도 사이트에 파일 그대로 함께 공개됩니다. `.env` 와 키는 올리지 않습니다. `.gitignore` 가 `.env` · `.venv/` · `__pycache__/` 를 막아 주고, 올리기 전에 `python check_publish.py` 로 한 번 더 점검합니다.
