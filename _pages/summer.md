---
permalink: /summer/
title: "Summer Programs 2022"

---

{:link: target="_blank" style="text-decoration: none"}

Following are the currently active summer programs. It is available for download as a [pdf](https://bit.ly/34oEdNg){: link}.

<table>
{% for row in site.data.active %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
		<th>{{ pair[0] }}</th>
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	<td><a target="_blank" style="text-decoration: none" href="{{ pair[1] }}">{{ pair[1] }}</a></td>
	{% else %}
	<td>{{ pair[1] }}</td>
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>

# Yet To Be Declared

Several other institutes will soon declare summer programs of their own. We will provide updates as soon as they become available.

<table>
{% for row in site.data.yet %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
		<th>{{ pair[0] }}</th>
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	<td><a target="_blank" style="text-decoration: none" href="{{ pair[1] }}">{{ pair[1] }}</a></td>
	{% else %}
	<td>{{ pair[1] }}</td>
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>

# Closed or Inactive

These programs have either stopped accepting applications due to closing of deadlines, or have not declared any program this session.
<table>
{% for row in site.data.inactive %}
	{% if forloop.first %}
	<tr>
	{% for pair in row %}
		<th>{{ pair[0] }}</th>
	{% endfor %}
	</tr>
	{% else %}
	<tr>
	{% for pair in row %}
	{% if forloop.last %}
	<td><a target="_blank" style="text-decoration: none" href="{{ pair[1] }}">{{ pair[1] }}</a></td>
	{% else %}
	<td>{{ pair[1] }}</td>
	{% endif %}
	{% endfor %}
	</tr>
	{% endif %}
{% endfor %}
</table>
