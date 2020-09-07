---
layout: page
title: To-do
permalink: /todo/
---

<ul>
  {%- for post in site.posts %}
    {%- assign is_target = false %}
    {%- for category in post.categories %}
      {%- if category == "To-do" %}
        {%- assign is_target = true %}
        {%- break %}
      {%- endif %}
    {%- endfor %}
    {%- if is_target %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {%- endif %}
  {%- endfor %}
</ul>
