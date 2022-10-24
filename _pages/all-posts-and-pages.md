---
title: All Posts and Pages
excerpt: Single access point for all content on this website
permalink: /all/
sidebar:
  nav: categories
tags:
    - housekeeping
header:
  overlay_image: /assets/images/general/stacked-steps-haikei.svg

---

Jump to [all pages](/all/#all-pages)

# All Posts
<ol>
{% for post in site.posts %}
<li><a href="{{ post.permalink }}">{{ post.title }}</a></li>
<i>{{ post.excerpt }}</i>
<br>
<b>{{ post.date | date: "%B %d, %Y" }}</b>,&nbsp; {{ post.categories }}

<hr>

{% endfor %}
</ol>

# All Pages

<ol>
{% for page in site.pages %}
{% if page.tags contains "content" %}

<li><a href="{{ page.permalink }}">{{ page.title }}</a></li>
<i>{{ page.excerpt }}</i>
<br>
<b>tags</b>:
{% for tag in page.tags %}
{% unless tag == "content" %}
{{ tag }},
{% endunless %}
{% endfor %}

<hr>

{% endif %}
{% endfor %}
</ol>
