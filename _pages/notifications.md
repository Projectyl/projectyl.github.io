---
title: "Application Drafting"
permalink: /notifications/

---

{% include group-by-array.html collection=site.posts field='categories' %}

{% for tag in group_names %}
{% if tag == 'Program Notification' %}
{% assign posts = group_items[forloop.index0] %}
{% for post in posts %}
<h2 class="archive__item-title"><a href='{{ site.baseurl }}{{ post.url }}' style="text-decoration:none">{{ post.title }}</a></h2>
{{ post.excerpt  | markdownify | remove: "<p>" | remove: "</p>" }}
{% endfor %}
{% endif %}
{% endfor %}