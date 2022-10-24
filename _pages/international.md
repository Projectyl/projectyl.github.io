---
permalink: /inter/
title: International Physics Internships in Foreign Universities
excerpt: Perfect for achieving more exposure to cutting-edge research and meeting new people
header:
  overlay_image: /assets/images/inter/inter.svg
  overlay_filter: rgba(10, 10, 10, 0.4)
tags:
 - international
 - internships
 - content

---

Following are some international sources of internships. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. Most of these travel allowances, check their websites to make sure. The table can be sorted by clicking on the column headings; use that to find internships from a specific country.

{% assign count = 1 %}
{% for group in site.data.countries %}
# {{ group[0] }}

<details>

<table class="sortable">
<tr>
<th style="text-align:left;">Institute</th>
<th>Country</th>
<th>Stipend</th>
</tr>
{% assign data = site.data.international | sort: "Country" %}
{% for row in data offset:1 %}
{% if group[1] contains row["Country"] %}
<tr>
<td style="text-align:left;"><a href="{{ row["Website"] }}">{{ row["Institute"] }}</a></td>
<td>{{ row["Country"] }}</td>
<td>{{ row["Stipend"] }}</td>
</tr>
{% endif %}
{% endfor %}
</table>
</details>
<br>

{% endfor %}
