---
layout: page
title: 홈
---

{{ site.description | escape }}

{% assign posts = site.posts | where_exp: "post", "post.sample != true" %}
{% assign featured_posts = posts | where: "featured", true %}
{% if featured_posts.size > 0 %}
<h2>대표 글</h2>
<ul>
{% for post in featured_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>{% if post.summary %} — {{ post.summary | escape }}{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

{% if posts.size > 0 %}
<h2>전체 글</h2>
<ul>
{% for post in posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a> · {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
{% endif %}
