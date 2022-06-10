---
permalink: /winter-schools/
title: <big>Winter Schools in India</big>
excerpt: List of winter schools on various topics in physics held in India
tags:
 - winter
 - schools
 - content
header:
  image: /assets/images/winter-schools/winter.svg
  caption: "[Source](https://www.ready.gov/winter-weather-safety-social-media-toolkit)"

---

<span class="excerpt">{{ page.excerpt }}</span>
<br>

This is a list of winter schools held in India. They are mostly targeted at graduate students, although some also admit undergraduates. Most of them are held regularly.

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
