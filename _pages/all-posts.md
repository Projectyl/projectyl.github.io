---
title: "All Posts"
permalink: /all/
sidebar:
  nav: categories
tags:
    - housekeeping

---


<ol>
{% for post in site.posts %}
<li><a href="{{ post.permalink }}">{{ post.title }}</a></li>
<i>{{ post.excerpt }}</i>
<br>
{{ post.date | date: "%B %d, %Y" }}, <b>{{ post.categories }}</b>

<hr>

{% endfor %}
</ol>
