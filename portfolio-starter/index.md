---
layout: page
title: 홈
---

이 사이트는 내가 네트워크 과정을 공부하며 남기는 실습 기록입니다. (이 문단을 내 소개로 바꾸세요. 예: 무엇을 배우려고 만들었는지, 누가 읽으면 좋은지)

Module 3~5 실습에서 직접 쓴 파이썬 코드와, 코드를 쓰며 한 고민(무엇을 골랐고 왜 골랐는지)을 글로 정리해 둡니다. 코드는 `code/` 폴더에, 글은 아래 목록에 쌓입니다.

## 최신 글

<ul>
{% for post in site.posts %}
  <li>
    <span>{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
