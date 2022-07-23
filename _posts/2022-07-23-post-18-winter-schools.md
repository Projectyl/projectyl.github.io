---
title: <big>Upcoming International Winter Schools</big>
excerpt: Particle Physics and Statistical Physics
permalink: /post18/
categories:
  - Program Notification
tags:
  - "Winter Schools"
  - international
header:
  image: /assets/images/post-18/kias.jpg

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Here are some upcoming winter schools on various topics in physics. For the full list and more details, check [here](/winter-schools/). 

{% for row in site.data.winter.schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

{% if name == "CHIPP Winter School of Particle Physics" or name == "ITAMP/B2 Winter School" or name == "KIAS-APCTP Winter School on Statistical Physics" %}

<h3><a href="{{ link }}">{{ name }}</a></h3>

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

{% endif %}

{% endfor %}
