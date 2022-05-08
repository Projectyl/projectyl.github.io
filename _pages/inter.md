---
permalink: /inter/
title: <big>International Internships</big>
excerpt: For those who want additional exposure
tags:
 - international
 - internships
 - content

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Following are some international sources of internships. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. It is available for download as a [pdf](/_pages/summer.pdf).

<table>
<tr>
<th align="right">No.</th>
{% for pair in site.data.international[0] limit:2 %}
<th>{{ pair[0] }}</th>
{% endfor %}
{% for pair in site.data.international[0] offset:2 %}
{% unless forloop.last %}
<th align="center">{{ pair[0] }}</th>
{% endunless %}
{% assign last_key = pair[0] %}
{% endfor %}
</tr>
{% for row in site.data.international offset:1 %}
<tr>
<td align="right">{{ forloop.index }}</td>
{% for pair in row %}
{% if forloop.first %}
{% assign text = pair[1] %}
{% endif %}
{% if forloop.last %}
{% assign url = pair[1] %}
{% endif %}
{% endfor %}
<td><a href="{{ url }}">{{ text }}</a></td>
{% for pair in row offset:1 limit:1 %}
<td>{{ pair[1] }}</td>
{% endfor %}
{% for pair in row offset:2 limit:1 %}
<td align="center">{{ pair[1] }}</td>
{% endfor %}
</tr>
{% endfor %}
</table>
