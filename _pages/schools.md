---
permalink: /schools/
title: <big>Annual Summer Schools and Workshops</big>
excerpt: Learn physics while the sun shines
tags:
  - summer-schools
  - content
header:
  image: /assets/images/schools/grasses.svg
  caption: "[Photo by Quang Nguyen Vinh](https://www.pexels.com/photo/two-fish-nets-in-body-of-water-2163334/)"

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Various institutes organise summer schools and workshops to help students get exposed to specific topics at the front line of research. They may also address more general topics that are too advanced for college curricula. Here is a list of summer schools being organised annually, both within and outside India. _Note that the headings are hyperlinks to the respective webpages_. The list is available for download as [pdf](/_pages/summer.pdf/).

<ol>
{% for row in site.data.summer.schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

<h3><li><a href="{{ link }}">{{ name }}</a></li></h3>

<b>Institute</b>: {{ row["Institute"] }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>Time</b>: {{ row["Time"] }}

<details>

<br>
<b>Topics:</b>
<br>
<ul>
{% for t in row["Topics"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>
<br>
<b>Target Audience:</b>
<br>
<ul>
{% for t in row["Target Audience"] %}
<li>{{ t }}</li>
{% endfor %}
</ul>

</details>
{% endfor %}
</ol>
