{% extends "section.md" %}

{% block body %}
{% for topic in items %}
<strong> {{ topic.year }} </strong>
 + {{ topic. presenter1 }}. <i>{{ topic.topic }}</i>. {{ topic.conference }}, {{ topic.place }}

{% endfor %}
{% endblock body %}

