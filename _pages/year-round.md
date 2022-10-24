---
permalink: /year-wide/
title: Year-Round Programs for UG/PG Students in Indian Institutes
excerpt: Apply to these programs at any time of the year - no deadlines to worry about!
header:
  overlay_image: /assets/images/year-wide/year-wide.svg
  overlay_filter: rgba(10, 10, 10, 0.4)
categories:
  - Program Notification
tags:
  - Year-round programs

---

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
