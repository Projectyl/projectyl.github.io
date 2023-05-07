---
layout: splash
permalink: /schools/
title: Summer & Winter Schools and Conferences in Physics
excerpt: List of annual summer & winter schools and conferences held in India and abroad
classes: wide
toc_sticky: true
tags:
  - summer-schools
  - content
header:
  overlay_image: /assets/images/schools/summer.svg
  overlay_filter: 0.7
  caption: "[Source](https://www.aalto.fi/en/aaltosummer)"
  actions:
    - label: "Internships"
      url: /summer/
    - label: "International"
      url: /inter/
    - label: "Physicists database"
      url: /dbpi/

---

{% assign data = site.data.summer_schools %}
{% assign length = data | size %}
{% assign half_length = length | divided_by:2 %}
{% for i in  (0..half_length)  %}
{% assign index = i | times:2 %}
<div markdown=1 class="horizontal__block">
 {% for in in (1..2) %}
 <div markdown=1 class="vertical__block">
  {% if index >= length %}{% continue %}{% endif %}
  {% assign row = data[index] %}
  <h3>{{ row["Name"] | upcase }} </h3>
  {{ row["Venue"] }}<br>
  **Timeframe**: {{ row["Time"] }}<br>
  [Webpage]({{ row["Link"] }}){: .btn .btn--info}&nbsp;&nbsp;&nbsp;<span class="btn btn--danger details__hider" onclick="hide__details()">Show details</span>
  <div markdown=1 class="schools__details">
  **Topics:**
  {%- for t in row["Topics"] %}
  - {{ t }}
  <br>
  {%- endfor %}
  **Target Audience:**
  <br>
  {%- for t in row["Target Audience"] %}
  - {{ t }}
  {%- endfor %}
  </div>
 </div>
 {% assign index = index | plus:1 %}
 {% endfor %}
</div>
{% if index < length %}<hr class="thick__line">{% endif %}
{% endfor %}

<script>
function hide__details() {
    event.target.textContent = event.target.textContent == "Show details" ? "Hide details" : "Show details";
    event.target.nextSibling.nextSibling.style.display = event.target.textContent == "Show details" ? "none": "block";
}
</script>
