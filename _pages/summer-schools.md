---
layout: splash
permalink: /schools/
title: Summer & winter physics schools and conferences
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
{% assign half_length = length | divided_by:2 | minus:1 %}
{% for i in  (0..half_length)  %}
{% assign index = i | times:2 | minus:1 %}
<div markdown=1 class="horizontal__block">
 {% for in in (1..2) %}
 {% assign index = index | plus:1 %}
 <div markdown=1 class="vertical__block">
  {% if index >= length %}{% continue %}{% endif %}
  {% assign row = data[index] %}
  <h3>{{ index | plus:1 }}. {{ row["Name"] }}</h3>
  {{ row["Institute"] }}&nbsp;&nbsp;&nbsp;[Webpage]({{ row["Link"] }}){: .btn .btn--info}<br>
  **Timeframe**: {{ row["Time"] }}
  <div class="btn btn--danger details__hider" onclick="hide__details()">Show details</div>
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
  <hr class="thick__line only_when_small">
 </div>
 {% endfor %}
</div>
<hr class="thick__line only_when_large">
{% endfor %}

<script>
function hide__details() {
    if (event.target.textContent == "Show details") {
        event.target.textContent = "Hide details";
        event.target.nextSibling.nextSibling.style.display = "block";
    } 
    else {
        event.target.textContent = "Show details";
        event.target.nextSibling.nextSibling.style.display = "none";
    }
}
</script>
