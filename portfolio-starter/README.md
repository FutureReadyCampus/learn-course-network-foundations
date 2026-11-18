# 네트워크 실습 노트

Module 3~5 실습에서 쓴 파이썬 코드와 고민을 기록하는 포트폴리오 저장소입니다. GitHub Pages(Jekyll, 기본 빌드)로 공개합니다. 별도 Action이나 설치 없이 동작합니다.

안내: 코스의 Module 3 Unit 1 「시작하기」 → 「내 기록 남기기」 페이지 (<https://futurereadycampus.github.io/learn-course-network-foundations/exercises/module/3/unit/1/lesson/1/page/3>)

## 파일 구성

| 이름 | 설명 |
|---|---|
| `_config.yml` | 사이트 이름·주소 설정 |
| `index.md` | 첫 화면(최신 글 목록) |
| `about.md` | 소개 페이지 |
| `_posts/` | 글 |
| `_templates/` | 글 틀 |
| `code/` | 실습 코드 |
| `assets/images/` | 글에 넣는 이미지 |
| `check_publish.py` | 공개 전 점검 스크립트 |

## 꼭 바꿔야 하는 3곳

1. `_config.yml`: `title`, `description`, `author`, `baseurl`을 내 것으로 바꿉니다(`url`은 비워 둡니다). (`← 내 것으로 바꾸기` 표시)
2. `about.md`: 빈칸 안내 문구를 내 소개로 채웁니다.
3. `_posts/`의 샘플 글: 지우고 내 첫 글을 씁니다.

## Pages 켜기

1. 이 파일들을 내 공개(Public) 저장소의 `main` 브랜치에 올립니다.
2. 저장소의 **Settings > Pages**로 갑니다.
3. **Source**는 **Deploy from a branch**, **Branch**는 `main`과 `/ (root)`를 고르고 **Save**를 누릅니다.
4. 1~2분 뒤 `https://<내 아이디>.github.io/<저장소 이름>/` 주소를 엽니다.

올리기 전에 `.env`나 비밀키 같은 파일이 들어 있지 않은지 확인합니다.
