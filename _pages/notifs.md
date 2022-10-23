---
title: Notification Posts
excerpt: All updates regarding upcoming or past programs, within or outside India
permalink: /notifs/
tags:
    - housekeeping
header:
  overlay_image: /assets/images/general/layered-steps-haikei.svg

---

{:link: target="_blank" style="text-decoration: none"}

{% for post in site.posts %}
{% if post.categories[0] contains "Notification" %}
  [**{{ post.title }}**]({{ post.permalink }}){:link}
<br>
  _{{ post.excerpt }}_
<br>
  {{ post.date | date: "%B %d, %Y" }}

  ---
{% endif %}
{% endfor %}
