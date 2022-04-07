---
title: "Application Drafting"
permalink: /drafting/

---

{% include group-by-array.html collection=site.posts field='categories' %}

{% for tag in group_names %}
{% if tag == 'Application Drafting' %}
{% assign posts = group_items[forloop.index0] %}
{% for post in posts %}
<h3 class="archive__item-title"><a href='{{ site.baseurl }}{{ post.url }}' style="text-decoration:none">{{ post.title }}</a></h3>
{{ post.excerpt  | markdownify | remove: "<p>" | remove: "</p>" }}
{% endfor %}
{% endif %}
{% endfor %}
