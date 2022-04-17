---
permalink: /dbpi-complete/
title: "Database for Physicists in India - Complete List"

---
The first column (Name) has hyperlinks that redirect to the personal homepage of the corresponding professor.

{% for insti in site.data.dbpi.info_files.institutes %}
## {{ insti }}
<table>
<tr><th align="center">Name</th>
<th align="center">Research Area</th>
<th align="center" width="10%">Email Id</th></tr>
{% for institute in site.data.dbpi.institute_data %}
{% assign people= institute[1] %}
{% for person in people %}
{% if person.Institute == insti %}
	<tr>
	<td><a target="_blank" style="text-decoration: none" href="{{ person.Homepage }}">{{ person.Name }}</a></td>
	<td>{{ person.Interests | join: ", " }}</td>
	<td><a href="mailto:{{person.Email}}">email</a></td>
	</tr>
{% endif %}
{% endfor %}
{% endfor %}
</table>
{% endfor %}
