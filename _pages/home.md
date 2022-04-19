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
    - label: "All Posts"
      url: /all/
excerpt: _<large>Starting research straight out of college can be daunting - we are here to make it easier.</large>_
author_profile: false

---

# Recent Posts

{:link: target="_blank" style="text-decoration: none"}

{% assign post0 = site.posts[0] %}
{% assign post1 = site.posts[1] %}
{% assign post2 = site.posts[2] %}
{% assign post3 = site.posts[3] %}

|<img src="{{ post0.header.image }}" width="900"/>|<img src="{{ post1.header.image }}" width="900" />|
|[<big>{{ post0.title }}</big>]({{ post0.permalink }})|[<big>{{ post1.title }}</big>]({{ post1.permalink }})|
|[<big>{{ post0.excerpt }}</big>]({{ post0.permalink }})|[<big>{{ post1.excerpt }}</big>]({{ post1.permalink }})|

|<img src="{{ post2.header.image }}" width="900"/>|<img src="{{ post3.header.image }}" width="900" />|
|[<big>{{ post2.title }}</big>]({{ post2.permalink }})|[<big>{{ post3.title }}</big>]({{ post3.permalink }})|
|[<big>{{ post2.excerpt }}</big>]({{ post2.permalink }})|[<big>{{ post3.excerpt }}</big>]({{ post3.permalink }})|
