---
id: m4-u03-l09
title: 오늘의 글 쓰기
render: markdown
---

# 오늘의 글 쓰기

## 질문 하나 고르기

`_posts`에서 실습 전에 만든 M4 Unit 3 초안을 엽니다. 아직 글이 없으면 [블로그 초안 준비](__SITE__/exercises/module/4/unit/3/lesson/8/page/1)에서 시작합니다.

1. 요청이 몰린 분과 평소의 분은 요청 수에서 얼마나 차이가 났나요?
2. 반복 거절을 조사할 때 횟수와 거절 이유를 함께 보는 이유는 무엇인가요?

직접 확인한 근거가 있는 질문 하나를 제목에 씁니다. 처음 읽는 사람도 상황을 알 수 있게 어떤 요청이나 기록을 왜 살펴봤는지 설명하세요.

## 같은 글에서 판단과 근거 연결하기

초안에서 다음 세 항목을 찾습니다.

<pre class="copyable"><code>&#35;# 문제
&#35;# 선택과 이유
&#35;# 검증 결과
</code></pre>

교재가 정한 조건은 ‘실습에서는 …로 정했다’고 밝힙니다. 내가 선택한 입력이나 비교 방법이 있다면 왜 그렇게 확인했는지 씁니다. 마지막으로 모아 둔 출력에서 한두 줄을 골라 그 값이 무엇을 보여 주는지 설명하세요. 예상과 달랐다면 마지막으로 확인한 값과 다음에 볼 곳까지 쓰면 됩니다.

**근거를 찾는 힌트**

요청 수가 급증한 시각과 기준값을 같은 단위로 적어 보세요. 횟수만 보고 요청의 원인까지 설명할 수 있나요?

## 코드에서 근거 찾기

`traffic_detection.py`를 읽고 판단했다면 아래 링크를 본문에 붙일 수 있습니다. 다른 파일을 읽었다면 경로와 링크 설명을 함께 고치세요. 실행 결과만으로 설명할 수 있으면 그 출력을 인용합니다.

<pre class="copyable"><code>[traffic_detection.py에서 확인한 처리 과정]({{ "/anomaly_detection/traffic_detection.py" | relative_url }})</code></pre>

<details><summary>교재 예시 · 분당 요청 급증 규칙이 놓친 요청</summary>

샘플 웹 로그에서 요청이 평소보다 몰린 시점을 찾았습니다. 요청을 분 단위로 묶고 평소 평균인 2건의 세 배인 6건을 탐지 기준으로 삼았습니다. 09:12의 9건이 탐지됐고, 09:20에 확인할 만한 요청 3건은 기준에 못 미쳐 탐지되지 않았습니다.

</details>

## 공개 전 확인하고 올리기

글과 코드에서 비밀키, 개인정보, 실제 서비스 로그를 확인합니다. 초안의 `published: false` 줄을 지우고 저장하세요. 이미 공개한 글의 파일명과 날짜는 유지합니다.

저장소 루트(`network-study-notes`)에서 다음 명령을 차례로 실행합니다. `pwd`가 `anomaly_detection`로 끝나면 먼저 `cd ..`로 올라갑니다. 점검 오류가 나오면 고친 뒤 다시 실행하세요. 커밋하기 전에 목록에서 글과 공개할 실습 코드만 포함됐는지 확인합니다.

```bash
python check_publish.py
git status --short
git add _posts/ anomaly_detection/
git diff --cached --stat
git commit -m "Publish M4 Unit 3 practice post"
git push
```

GitHub Pages의 **전체 글**에서 제목을 누르고 본문과 코드 링크를 열어 봅니다. 글이 보이지 않으면 [첫 화면 점검 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/9)를 확인하세요.

<!-- checklist -->
- [ ] 독자가 제목에서 질문을, 본문에서 직접 확인한 근거를 찾을 수 있다
- [ ] 공개한 글을 열어 본문과 근거를 확인했다
<!-- /checklist -->
