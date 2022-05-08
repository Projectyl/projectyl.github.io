---
permalink: /summer/
title: <big>Summer Internships in India</big>
excerpt: Comprehensive list of summer programs in India
tags:
 - summer
 - internships
 - content

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Following are the currently active summer programs. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. It is available for download as a [pdf](/_pages/summer.pdf).

{% assign files = "active,inactive" | split: ',' %}
{% assign heads = "Active,Inactive" | split: ',' %}
{% for file in files %}
{% assign head_index = forloop.index | minus: 1 %}

# {{ heads[head_index] }}

{% assign path = site.data.summer[file] %}
<table class="sortable">
<tr>
{% for pair in path[0] %}
{% unless forloop.last %}
<th align="center">{{ pair[0] }}</th>
{% endunless %}
{% assign last_key = pair[0] %}
{% endfor %}
</tr>
{% for row in path offset: 1%}
<tr>
{% for pair in row %}
{% if forloop.first %}
{% assign text = pair[1] %}
{% endif %}
{% if forloop.last %}
{% assign url = pair[1] %}
{% endif %}
{% endfor %}
<td><a href="{{ url }}">{{ text }}</a></td>
{% for pair in row offset: 1%}
{% unless forloop.last %}
<td align="center">{{ pair[1] }}</td>
{% endunless %}
{% endfor %}
</tr>
{% endfor %}
</table>
{% endfor %}
