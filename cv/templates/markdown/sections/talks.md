{% extends "section.md" %}

{% block body %}

2017
{% for year in items %}
{% if year.year == 2017 %}
+ {{  year.presenter1 }}. <i>{{ year.topic }}</i>. {{ year.conference }}, {{ year.place }}
{% endif %}
{% endfor %}


2016
{% for year in items %}
{% if year.year == 2016 %}
+ {{ year.presenter1 }}. <i>{{ year.topic }}</i>. {{ year.conference }}, {{ year.place }}
{% endif %}
{% endfor %}


{% endblock body %}

