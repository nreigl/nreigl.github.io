{% extends "section.md" %}

{% block body %}
{% for course in items %}
+ {{ course.school}}. <i>{{ course.name }}</i>,
 {{ course.instructor}}, {{ course.semester }}
{% endfor %}
{% endblock body %}
