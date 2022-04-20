---
permalink: /year-round/
title: <big>Year-Round Programs</big>
excerpt: BARC, HRI and ARIES
header:
  image: /assets/images/year-wide/aries.svg
categories:
  - Program Notification
tags:
  - "Year-round programs"

---

<span class="excerpt">{{ page.excerpt }}</span>

<br>

Many institutes offer year-round internships for interested students that are open throughout the year. UG/PG students are asked to send in their applications at any point of the year and participate in summer programs/research work for a certain amount of time. Below we have listed 10 institutes that offer such year-wide programs. _Note that the headings are hyperlinks to the respective webpages_. The list is available for download as [pdf](/_pages/summer.pdf/).

{% for row in site.data.year-round %}
{% assign name = row["Institute"] %}
{% assign link = row["Link"] %}
{% assign dur = row["Duration"] %}
{% assign stip = row["Stipend"] %}
{% assign elig = row["Eligibility"] %}

### [{{ name }}]({{ link }})

**Duration**: {{ dur }}

**Stipend**: {{ stip }}

**Eligibility**:<br>
{% for item in elig %} 
- {{ item }}
{% endfor %}

{% endfor %}
