---
layout: page
title: Teaching
permalink: /teaching/
---

# Teaching Activities

<p>I am passionate about teaching and mentoring the next generation of machine learning researchers. Below are the courses and guest lectures I have been involved with.</p>

<h2>Courses Taught</h2>
{% for course in site.data.teaching.courses %}
<div class="teaching-entry">
  <h3>{{ course.title }} ({{ course.code }})</h3>
  <p>
    <strong>Role:</strong> {{ course.role }}<br>
    <strong>Institution:</strong> {{ course.institution }}<br>
    <strong>Semester:</strong> {{ course.semester }} ({{ course.level }} Course)<br>
    <strong>Description:</strong> {{ course.description }}
    {% if course.materials_link %}<br><a href="{{ course.materials_link }}" target="_blank" rel="noopener noreferrer" class="btn-link">Course Materials</a>{% endif %}
  </p>
</div>
{% endfor %}

<h2>Guest Lectures</h2>
{% for lecture in site.data.teaching.guest_lectures %}
<div class="teaching-entry">
  <h3>{{ lecture.title }}</h3>
  <p>
    <strong>Course:</strong> {{ lecture.course }}<br>
    <strong>Institution:</strong> {{ lecture.institution }}<br>
    <strong>Date:</strong> {{ lecture.date }}<br>
    <strong>Description:</strong> {{ lecture.description }}
    {% if lecture.slides_link %}<br><a href="{{ lecture.slides_link }}" target="_blank" rel="noopener noreferrer" class="btn-link">Slides</a>{% endif %}
  </p>
</div>
{% endfor %}
