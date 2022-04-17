---
permalink: /dbpi/
title: "Database for Physicists in India"

---

This is a database of physicists working in faculty positions at various Indian institutes. This service is still in beta, and data for institutes are still being added. If you want to look for the people working in a specific field like high energy physics, take a look at the "Filter by Category" section and click on the "High Energy Physics" item.

## Filter by Category

{% for category_hash in site.data.dbpi.info_files.category_file %}
<details>
<summary> 
&nbsp;
{% assign name = category_hash[0] | replace: ' ','_' | replace: ',','' | replace: '&','' %}
<b>{{ category_hash[0] }}</b>
</summary>
<br>
{% for file_hash in site.data.dbpi.category_data %}
{% if file_hash[0] == name %}
{% assign people = file_hash[1] %}
<table>
<tr><th align="center">Name</th>
<th align="center">Institute</th>
<th align="center">Designation</th>
<th align="center">Research Area</th>
<th align="center">Email Id</th></tr>
{% for person in people %}
	<tr>
	<td>{{ person.Name }}</td>
	<td><a target="_blank" style="text-decoration: none" href="{{ person.Homepage }}">{{ person.Institute }}</a></td>
	<td>{{ person.Designation }}</td>
	<td>{{ person.Interests | join: ", " }}</td>
	<td>{{ person.Email }}</td>
	</tr>
{% endfor %}
</table>
{% endif %}
{% endfor %}
</details>
{% endfor %}


## Complete List

The complete list of physicists is given [here](/dbpi-complete/).

