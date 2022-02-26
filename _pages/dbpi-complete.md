---
permalink: /dbpi-complete/
title: "Database for Physicists in India - Complete List"

---
The second column (Institute) has hyperlinks that redirect to the personal homepage of the corresponding professor.

<table>
<tr><th>Name</th>
<th>Institute</th>
<th>Designation</th>
<th>Research Area</th>
<th>Email Id</th></tr>
{% for insti in site.data.dbpi.institute_data %}
{% assign people= insti[1] %}
{% for person in people %}
	<tr>
	<td>{{ person.Name }}</td>
	<td><a target="_blank" style="text-decoration: none" href="{{ person.Homepage }}">{{ person.Institute }}</a></td>
	<td>{{ person.Designation }}</td>
	<td>{{ person.Interests | join: ", " }}</td>
	<td>{{ person.Email }}</td>
	</tr>
{% endfor %}
{% endfor %}
</table>
