---
title: Welcome to Projectyl!
layout: splash
permalink: /
header:
  overlay_image: /assets/images/general/banner.svg
  actions:
    - label: "Learn More"
      url: /about/
    - label: "Contact Us"
      url: /contact/
excerpt: _<large>Starting research straight out of college can be daunting - we are here to make it easier.</large>_
author_profile: false
tags:
    - housekeeping

---

# [Recent Posts](/all/)
---

{% assign styles = "float:right;,float:left;" | split: ',' %}

{% for post in site.posts limit: 4 %}

{% assign value = forloop.index | modulo:2 %}
{% assign style = styles[value] %}

<div style="{{ style }}">
<a href="{{ post.permalink }}"><img src="{{ post.header.image }}" width="750"/>
<p style="text-align:center;margin:0"><big>{{ post.title }}</big></p>
<p style="text-align:center;color:black;margin-bottom:2em">{{ post.excerpt }}</p></a>
</div>

{% endfor %}
