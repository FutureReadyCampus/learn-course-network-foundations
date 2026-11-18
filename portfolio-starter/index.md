---
layout: page
title: 홈
---

이 사이트는 내가 네트워크 과정을 공부하며 남기는 실습 기록입니다. (이 문단을 내 소개로 바꾸세요. 예: 무엇을 배우려고 만들었는지, 누가 읽으면 좋은지)

Module 3~5 실습에서 직접 쓴 파이썬 코드와, 코드를 쓰며 한 고민(무엇을 골랐고 왜 골랐는지)을 글로 정리해 둡니다. 코드는 `code/` 폴더에, 글은 아래 목록에 쌓입니다.

## 나의 진행

글을 쓴 Unit은 칸이 채워집니다. 칸을 누르면 그 글로 이동합니다.

<style>
.prog { margin: 1rem 0 2rem; }
.prog-row { display: flex; align-items: center; gap: 6px; margin: 6px 0; flex-wrap: wrap; }
.prog-row strong { width: 90px; font-size: .9rem; }
.prog .cell { width: 34px; height: 34px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid #ccc; border-radius: 6px; color: #999; font-size: .85rem; text-decoration: none; background: #fafafa; }
.prog .cell.done { background: #e0442e; border-color: #e0442e; color: #fff; font-weight: 700; }
.prog-sum { color: #666; font-size: .9rem; }
</style>

{% assign mods = "3,4,5" | split: "," %}
{% assign real_posts = site.posts | where_exp: "p", "p.sample != true" %}
{% assign total = 0 %}
<div class="prog">
{% for m in mods %}
  <div class="prog-row"><strong>Module {{ m }}</strong>
  {% for u in (1..10) %}
    {% assign hits = real_posts | where: "module", m | where: "unit", u %}
    {% if hits.size > 0 %}{% assign total = total | plus: 1 %}
    <a class="cell done" href="{{ hits.last.url | relative_url }}" title="Unit {{ u }}: {{ hits.last.title }}">{{ u }}</a>
    {% else %}<span class="cell" title="Unit {{ u }}">{{ u }}</span>{% endif %}
  {% endfor %}
  </div>
{% endfor %}
</div>
<p class="prog-sum">30개 Unit 중 {{ total }}개에 글을 남겼습니다.</p>

## 최신 글

<ul>
{% for post in site.posts %}
  <li>
    <span>{{ post.date | date: "%Y-%m-%d" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
