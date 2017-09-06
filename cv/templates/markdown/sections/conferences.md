{% extends "section.md" %}

{% block body %}
{% for conference in items %}
<strong> {{ conference.year }} </strong>
 + <i>{{ conference.conference }}</i>, {{ conference.place }}

{% endfor %}
{% endblock body %}

