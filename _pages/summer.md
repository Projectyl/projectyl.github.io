---
permalink: /summer/
title: "Summer Internships"
tags:
 - Summer Programs 2022

---

Following are the currently active summer programs. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. It is available for download as a [pdf](/_pages/summer.pdf).

{% assign files = "active,inactive" | split: ',' %}
{% assign heads = "Active,Inactive" | split: ',' %}
{% for file in files %}
{% assign head_index = forloop.index | minus: 1 %}

# {{ heads[head_index] }}

{% assign path = site.data.summer[file] %}
<table>
<tr>
{% for pair in site.data.summer.active[0] %}
{% unless forloop.last %}
<th align="center">{{ pair[0] }}</th>
{% endunless %}
{% assign last_key = pair[0] %}
{% endfor %}
</tr>
{% for row in site.data.summer.active offset: 1%}
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
<td>{{ pair[1] }}</td>
{% endunless %}
{% endfor %}
</tr>
{% endfor %}
</table>
{% endfor %}
