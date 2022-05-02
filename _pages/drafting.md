---
title: "Application Drafting"
permalink: /drafting/
sidebar:
  nav: categories
tags:
    - housekeeping

---

{:link: target="_blank" style="text-decoration: none"}

{% for post in site.posts %}
{% if post.categories[0] contains "Drafting" %}
  [**{{ post.title }}**]({{ post.permalink }}){:link}
<br>
  _{{ post.excerpt }}_
<br>
  {{ post.date | date: "%B %d, %Y" }}

  ---
{% endif %}
{% endfor %}
