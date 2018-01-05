{% extends "section.md" %}

{% block body %}

2017
{% for year in items %}
{% if year.year == 2017 %}
 + <i>{{ year.conference }}</i>, {{ year.place }}
{% endif %}
{% endfor %}

2016
{% for year in items %}
{% if year.year == 2016 %}
 + <i>{{ year.conference }}</i>, {{ year.place }}
{% endif %}
{% endfor %}


{% endblock body %}



