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
{% assign half_length = length | divided_by:2 | plus:1 %}
{% for i in  (0..half_length)  %}
{% assign index1 = i | times:2 %}
{% assign index2 = index1 | plus:1 %}
<div markdown=1 class="horizontal__block">
<div markdown=1 class="vertical__block">
{% if index1 >= length %}
{% continue %}
{% endif %}
{% assign row = data[index1] %}
{% assign name = row["Name"] %}
{% if name == blank %}
{% continue %}
{% endif %}
{% assign link = row["Link"] %}

### {{ name }}

**Institute**: {{ row["Institute"] }}
<br>
**Webpage**: [**Link**]({{ link }})
<br>
**Time-frame**: {{ row["Time"] }}

<div class="btn btn--danger details__hider"  onclick="hide__details()">Show details</div>

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
<div markdown=1 class="vertical__block">
{% if index2 >= length %}
{% continue %}
{% endif %}
{% assign row = data[index2] %}

{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

### {{ name }}

**Institute**: {{ row["Institute"] }}
<br>
**Webpage**: [**Link**]({{ link }})
<br>
**Time-frame**: {{ row["Time"] }}

<div class="btn btn--danger details__hider"  onclick="hide__details()">Show details</div>

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
</div>

<hr class="thick__line">

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
