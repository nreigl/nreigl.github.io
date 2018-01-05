{% extends "section.md" %}

{% block body %}
{% for award in items %}
 + {% if award.descr %} {{ award.descr }}. {% endif %} <i>{{ award.title }}</i>, {{ award.year }}
{% endfor %}
{% endblock body %}
