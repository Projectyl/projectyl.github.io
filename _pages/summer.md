---
permalink: /summer/
title: Summer Internship Programs for Physics Students in India
excerpt: A comprehensive list of summer programs at IITs, IISERs and other institutes
tags:
 - summer
 - internships
 - content
header:
  overlay_image: /assets/images/general/summer-internships.svg
  overlay_filter: rgba(10, 10, 10, 0.6)
  caption: "[Source](https://www.valpo.edu/physics-astronomy/apply/scholarships/)"

---

Following is a list of physics summer internship programs in India. *Note that the institute names in the left columns are hyperlinks to the respective webpages*. It is available for download as a [pdf](/_pages/summer.pdf).

{% assign path = site.data.summer.all | sort: "Institute" %}

<table class="sortable">
<tr>
<th style="text-align:left;">Institute</th>
<th>Deadline</th>
<th>Time-frame</th>
<th style="text-align:right;">Stipend / month</th>
</tr>
{% for row in path offset: 1 %}
<tr>
<td style="text-align:left;"><a href="{{ row["Website"] }}">{{ row["Institute"] }}</a></td>
<td>{{ row["Deadline"] }}</td>
<td>{{ row["Time-frame"] }}</td>
<td style="text-align:right;">{{ row["Stipend"] }}</td>
</tr>
{% endfor %}
</table>


