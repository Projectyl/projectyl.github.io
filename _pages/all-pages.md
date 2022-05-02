---
title: <big>All Pages</big>
permalink: /all-pages/
sidebar:
  nav: categories
tags:
    - housekeeping

---


<ol>
{% for post in site.pages %}
{% if post.tags contains "content" %}

<li><a href="{{ post.permalink }}">{{ post.title }}</a></li>

<hr>

{% endif %}
{% endfor %}
</ol>
