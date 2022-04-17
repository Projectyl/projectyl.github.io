---
permalink: /schools/
title: "Summer Schools"

---

Various institutes organise summer schools and workshops to help students get exposed to specific topics at the front line of research. They may also address more general topics that are too advanced for college curricula. Here is a list of summer schools being organised in India. _Note that the headings are hyperlinks to the respective webpages_.

{% for row in site.data.summer.schools %}
{% assign name = row["Name"] %}
{% assign link = row["Link"] %}

### [{{ name }}]({{ link }})

{% for pair in row offset:2 %}
{% if pair[1].first %}
**{{ pair[0] }}**:
<ul>
{% for item in pair[1] %}
<li>{{ item }}</li>
{% endfor %}
</ul>
{% else %}
**{{ pair[0] }}**: {{ pair[1] }}
{% endif %}
{% endfor %}
{% endfor %}
