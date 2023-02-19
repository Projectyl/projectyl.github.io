---
permalink: /schools/
title: Annual Summer Schools and Workshops - Domestic and International
excerpt: The perfect opportunity to boost your skills and gather some experience
classes: ""
toc: true
toc_sticky: true
tags:
  - summer-schools
  - content
header:
  overlay_image: /assets/images/schools/summer.svg
  overlay_filter: rgba(10, 10, 10, 0.6)
  caption: "[Source](https://www.aalto.fi/en/aaltosummer)"

---

Various institutes organise summer schools and workshops to help students get exposed to specific topics at the front line of research. They may also address more general topics that are too advanced for college curricula. Here is a list of summer schools being organised annually, both within and outside India. _Note that the headings are hyperlinks to the respective webpages_. The list is available for download as [pdf](/_pages/summer.pdf/).

{% for row in site.data.summer_schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

## {{ name }}
<a href="{{ link }}">[Link to website]</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Institute**: {{ row["Institute"] }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Time**: {{ row["Time"] }}

**Topics:**
<br>
{%- for t in row["Topics"] -%}
&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-angle-right"></i>&nbsp;&nbsp;{{ t }}<br>
{% endfor %}

**Target Audience:**
<br>
{%- for t in row["Target Audience"] -%}
&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-angle-right"></i>&nbsp;&nbsp;{{ t }}<br>
{% endfor %}

{% endfor %}
