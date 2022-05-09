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

Following are some international sources of internships. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. Most of these travel allowances, check their websites to make sure. The table can be sorted by clicking on the column headings; use that to find internships from a specific country.

{% assign count = 1 %}
{% for group in site.data.countries %}
# {{ group[0] }}

<details>

<table class="sortable">
<tr>
<th align="center"></th>
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
{% if group[1] contains row["Country"] %}
<tr>
<td align="center">{{ count }}.</td>
{% assign count = count | plus:1 %}
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
{% endif %}
{% endfor %}
</table>
</details>
<br>

{% endfor %}
