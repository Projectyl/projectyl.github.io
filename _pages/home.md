---
title: "Welcome to Projectyl!"
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

---

# Recent Posts

---

{:link: target="_blank" style="text-decoration: none"}

{% assign post0 = site.posts[0] %}
{% assign post1 = site.posts[1] %}
{% assign post2 = site.posts[2] %}

|<img src="{{ post0.header.image }}" width="50%"/>|
|<a href="{{ post0.permalink }}" style="font-size: 140%; text-decoration: none"><b>{{ post0.title }}</b></a>|

|<img src="{{ post1.header.image }}" width="50%" />|
|<a href="{{ post1.permalink }}" style="font-size: 140%; text-decoration: none"><b>{{ post1.title }}</b></a>|

|<img src="{{ post2.header.image }}" width="50%" />|
|<a href="{{ post2.permalink }}" style="font-size: 140%; text-decoration: none"><b>{{ post2.title }}</b></a>|
