{% extends "section.md" %}

{% block body %}

<table class="table table-hover">
{% for school in items %}
  <tr>
    <td class="col-md-3">{{ school.dates }}</td>
    <td>
    {{ school.school }} <br/>

{% if school.degree %}
<strong>{{ school.degree }}</strong> <br/>
{% if school.overallGPA %}
({{ school.overallGPA }})
{% endif %}

{% if school.thesis %}
{{ school.thesis }} <br/>
{% endif %}

{% if school.advisor1 and school.advisor2 and school.advisorlink2 and school.advisor2 %}
<br/> Advisors - <a href="{{school.advisorlink1}}">{{ school.advisor1 }}</a> and <a href="{{school.advisorlink2}}">{{ school.advisor2 }}</a>
{% endif %}
{% endif %}

  </tr>
{% endfor %}
</table>
{% endblock body %}
