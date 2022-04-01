---
permalink: /summer/
title: "Summer Programs 2022"

---

{:link: target="_blank" style="text-decoration: none"}

Following are the currently active summer programs. (Note that the institute names in the left columns are hyperlinks to the respective webpages.) It is available for download as a [pdf](https://drive.google.com/file/d/1ACoZx-BdsIJ91rLAThYLnuRHnIXvwOBr/view?usp=sharing){: link}.

<table>
{% for row in site.data.summer.active %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
	{% if forloop.first %}
	<th align="left">{{ pair[0] }}</th>
	{% else %}
	{% unless forloop.last %}
	<th align="center">{{ pair[0] }}</th>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	{% assign link = pair[1] %}
	{% endif %}
	{% endfor %}
	{% for pair in row %}
	{% if forloop.first %}
	<td align="left"><a target="_blank" style="text-decoration: none" href="{{ link }}">{{ pair[1] }}</a></td>
	{% else %}
	{% unless forloop.last %}
	<td align="center">{{ pair[1] }}</td>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>

# Yet To Be Declared

Several other institutes will soon declare summer programs of their own. We will provide updates as soon as they become available.

<table>
{% for row in site.data.summer.yet %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
	{% if forloop.first %}
	<th align="left">{{ pair[0] }}</th>
	{% else %}
	{% unless forloop.last %}
	<th align="center">{{ pair[0] }}</th>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	{% assign link = pair[1] %}
	{% endif %}
	{% endfor %}
	{% for pair in row %}
	{% if forloop.first %}
	<td align="left"><a target="_blank" style="text-decoration: none" href="{{ link }}">{{ pair[1] }}</a></td>
	{% else %}
	{% unless forloop.last %}
	<td align="center">{{ pair[1] }}</td>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>

# Closed or Inactive

These programs have either stopped accepting applications due to closing of deadlines, or have not declared any program this session.

<table>
{% for row in site.data.summer.inactive %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
	{% if forloop.first %}
	<th align="left">{{ pair[0] }}</th>
	{% else %}
	{% unless forloop.last %}
	<th align="center">{{ pair[0] }}</th>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	{% assign link = pair[1] %}
	{% endif %}
	{% endfor %}
	{% for pair in row %}
	{% if forloop.first %}
	<td align="left"><a target="_blank" style="text-decoration: none" href="{{ link }}">{{ pair[1] }}</a></td>
	{% else %}
	{% unless forloop.last %}
	<td align="center">{{ pair[1] }}</td>
	{% endunless %}
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>
