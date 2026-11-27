---
id: m4-u01-l05
title: 문제 해결 과정을 블로그에 기록하기
render: markdown
---

# 문제 해결 과정을 블로그에 기록하기

## 기록할 문제 고르기

두 실습을 마쳤으면 실제로 판단이 어려웠던 문제를 한 가지 고릅니다. 로그가 깨져 읽히지 않은 이유, 오류와 의심을 구분한 조건, 작은 회사에서 SIEM 방식을 선택한 근거 중 하나를 다뤄도 됩니다.

읽는 사람이 당시 상황과 선택을 다시 따라 볼 수 있도록 증상, 확인한 결과, 비교한 방법, 선택 이유와 다음 확인 항목을 남깁니다.

## 실행 결과에서 근거 찾기

출력 전체 대신 판단에 직접 쓰인 두세 줄을 고릅니다. 예를 들어 같은 주소가 드물게 쓰는 경로를 연달아 요청했다면, 경로와 시각을 같이 보고 단일 404 요청과 어떻게 달랐는지 적습니다. 샘플에서 확인한 사실과 가능한 해석을 구분합니다.

아직 해결하지 못했다면 어디까지 확인했고 다음에는 무엇을 볼지 적습니다. AI에게 물었다면 질문과 답변을 통째로 붙이기보다 직접 확인한 내용을 요약합니다.

## 선택과 확인을 글로 쓰기

M3 Unit 1에서 만든 `network-study-notes`의 `_posts/`에 날짜를 넣은 `YYYY-MM-DD-m4-u1-log-analysis.md` 파일을 만듭니다. 블로그 설정이 아직 없다면 [M3 Unit 1의 Jekyll/GitHub Pages 설정 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)를 먼저 따라갑니다.

아래 틀을 복사해 내 경험으로 채웁니다.

<pre class="copyable"><code>---
layout: post
title: "연속된 접속 요청을 함께 살펴본 이유"
date: YYYY-MM-DD
module: 4
unit: 1
---

&#35;# 문제 상황
무엇을 확인해야 했나요?

&#35;# 확인한 근거
어떤 로그 줄이나 실행 결과를 봤나요?

&#35;# 가능한 원인
어떤 설명을 고려했나요?

&#35;# 선택과 이유
어떤 규칙이나 확인 절차를 선택했고, 왜인가요?

&#35;# 다시 확인한 결과
샘플에서 무엇을 확인했나요?

&#35;# 남은 질문
다음에는 무엇을 확인하고 싶나요?

&#35;# AI와 나눈 대화 (사용했다면)
어떤 질문을 했고, 답변 중 무엇을 직접 확인했나요?
</code></pre>

## GitHub에 글과 실습 코드 올리기

1. 글과 `anomaly_detection/`을 살펴보고 API 키, 비밀번호, 개인 연락처와 실제 사용자 로그가 있는지 확인합니다.
2. VS Code에서 `network-study-notes`를 열어 터미널을 엽니다. `git status --short`로 이번에 올리는 변경을 확인하고 `python check_publish.py`를 실행합니다(macOS에서는 `python3`). `.env`나 가상환경이 목록에 나타나면 `.gitignore`를 확인합니다.
3. 올릴 폴더를 지정해 기록합니다. GitHub Pages에서 새 글을 열고, GitHub 저장소에서 실습 코드가 보이는지 확인합니다.

```bash
git add anomaly_detection _posts
git diff --cached --stat
git commit -m "Record M4 Unit 1 problem solving"
git push
```
