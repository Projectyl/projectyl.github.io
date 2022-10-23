---
permalink: /schools/
title: Annual Summer Schools and Workshops - Domestic and International
excerpt: The perfect opportunity to boost your skills and gather some experience
tags:
  - summer-schools
  - content
header:
  overlay_image: /assets/images/schools/summer.svg
  overlay_filter: rgba(10, 10, 10, 0.6)
  caption: "[Source](https://www.aalto.fi/en/aaltosummer)"

---

Various institutes organise summer schools and workshops to help students get exposed to specific topics at the front line of research. They may also address more general topics that are too advanced for college curricula. Here is a list of summer schools being organised annually, both within and outside India. _Note that the headings are hyperlinks to the respective webpages_. The list is available for download as [pdf](/_pages/summer.pdf/).

{% for row in site.data.summer.schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

<h3><a href="{{ link }}">{{ forloop.index }}.  {{ name }}</a></h3>

<div style="float:left;"><b>Institute</b>: {{ row["Institute"] }}</div>
<div style="float:right"><b>Time</b>: {{ row["Time"] }}</div>

<br>

<b>Topics:</b>
<ul>
{% for t in row["Topics"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>
<b>Target Audience:</b>
<ul>
{% for t in row["Target Audience"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>

{% endfor %}
