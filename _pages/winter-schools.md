---
permalink: /winter-schools/
title: <big>Winter Schools in India</big>
excerpt: List of winter schools on various topics in physics held in India
tags:
 - winter
 - schools
 - content

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Following are the currently active summer programs. Note that the institute names in the left columns are **hyperlinks** to the respective webpages. It is available for download as a [pdf](/_pages/summer.pdf).

{% for row in site.data.winter.schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

<h3><a href="{{ link }}">{{ forloop.index }}. {{ name }}</a></h3>

<div style="float: left;"><b>Institute</b>: {{ row["Institute"] }}</div><div style="float: right;"><b>Time</b>: {{ row["Time"] }}</div>
<br>
{% if row["Topics"].size == 1 %}
<b>Topics:</b>
{{ row["Topics"] }}
{% else %}
<b>Topics:</b>
<ul>
{% for t in row["Topics"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>
{% endif %}
{% if row["Target Audience"].size == 1 %}
<b>Target Audience:</b>
{{ row["Target Audience"] }}
{% else %}
<b>Target Audience:</b>
<ul>
{% for t in row["Target Audience"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>
{% endif %}

{% endfor %}
