---
id: m3-u05-l08
title: 문제 해결 과정 블로그 기록
render: markdown
---

# 문제 해결 과정 블로그 기록

## 질문 하나 고르기

`_posts`에서 실습 전에 만든 M3 Unit 5 초안을 엽니다. 아직 글이 없으면 [블로그 초안 준비](__SITE__/exercises/module/3/unit/5/lesson/7/page/1)에서 시작합니다.

1. 퇴사자 계정 점검에서 어떤 값 때문에 점검에 실패했나요?
2. 점검에 걸린 계정을 조사할 때 어떤 파일부터 확인할까요?

직접 확인한 근거가 있는 질문 하나를 제목에 씁니다. 처음 읽는 사람도 상황을 알 수 있게 어떤 요청이나 기록을 왜 살펴봤는지 설명하세요.

## 같은 글에서 판단과 근거 연결하기

초안에서 다음 세 항목을 찾습니다.

<pre class="copyable"><code>&#35;# 문제
&#35;# 선택과 이유
&#35;# 검증 결과
</code></pre>

교재가 정한 조건은 ‘실습에서는 …로 정했다’고 밝힙니다. 내가 선택한 입력이나 비교 방법이 있다면 왜 그렇게 확인했는지 씁니다. 마지막으로 모아 둔 출력에서 한두 줄을 골라 그 값이 무엇을 보여 주는지 설명하세요. 예상과 달랐다면 마지막으로 확인한 값과 다음에 볼 곳까지 쓰면 됩니다.

<h2>근거를 찾는 힌트</h2>

퇴사자 계정과 만료된 예외가 각각 어느 점검에 걸렸는지 이름과 출력 한 줄을 함께 찾아보세요.

## 코드에서 근거 찾기

`checklist.py`를 읽고 판단했다면 아래 링크를 본문에 붙일 수 있습니다. 다른 파일을 읽었다면 경로와 링크 설명을 함께 고치세요. 실행 결과만으로 설명할 수 있으면 그 출력을 인용합니다.

<pre class="copyable"><code>[checklist.py에서 확인한 처리 과정]({{ "/access_control/checklist.py" | relative_url }})</code></pre>

## 공개 전 확인하고 올리기

글과 코드에서 비밀키, 개인정보, 실제 서비스 로그를 확인합니다. 초안의 `published: false` 줄을 지우고 저장하세요. 이미 공개한 글의 파일명과 날짜는 유지합니다.

**Module 3 대표 글 고르기.** 다섯 편 가운데 질문과 근거가 가장 잘 연결된 글 하나를 엽니다. 머리말의 두 `---` 사이에 아래 두 줄을 넣고 요약을 내 결과로 바꿉니다. 이 모듈에서 이미 다른 대표 글을 골랐다면 그 글의 `featured: true`를 지웁니다.

<pre class="copyable"><code>featured: true
summary: "어떤 문제를 살펴봤고 무엇을 확인했는지 한 문장으로 씁니다."</code></pre>

저장소 루트(`network-study-notes`)에서 다음 명령을 차례로 실행합니다. `pwd`가 `access_control`로 끝나면 먼저 `cd ..`로 올라갑니다. 점검 오류가 나오면 고친 뒤 다시 실행하세요. 커밋하기 전에 목록에서 글과 공개할 실습 코드만 포함됐는지 확인합니다.

```bash
python check_publish.py
git status --short
git add _posts/ access_control/
git diff --cached --stat
git commit -m "Publish M3 Unit 5 practice post"
git push
```

GitHub Pages의 **전체 글**에서 제목을 누르고 본문과 코드 링크를 열어 봅니다. 글이 보이지 않으면 [첫 화면 점검 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/9)를 확인하세요.

<!-- checklist -->
- [ ] 독자가 제목에서 질문을, 본문에서 직접 확인한 근거를 찾을 수 있다
- [ ] 공개한 글을 열어 본문과 근거를 확인했다
- [ ] 블로그 홈의 대표 글에서 이번 모듈의 한 편과 요약을 확인했다
<!-- /checklist -->
