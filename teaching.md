---
layout: page
title: Teaching
permalink: /teaching/
---

<div class="constrained-content">
  <h1>Teaching Activities</h1>

  {% comment %}
    Display Courses
  {% endcomment %}
  {% if site.data.teaching.courses %}
    <section class="teaching-section">
      <h2 class="teaching-section-title"><i class="fa-solid fa-chalkboard-user"></i> Courses Taught</h2>
      <div class="teaching-items-container">
        {% for course in site.data.teaching.courses %}
          <div class="teaching-item">
            <h3 class="teaching-item-title">{{ course.title }} {% if course.code %}<span class="course-code">({{ course.code }})</span>{% endif %}</h3>
            <p class="teaching-item-meta">
              {{ course.role }} | {{ course.institution }}
              {% if course.semester %} | <span class="teaching-year-highlight">{{ course.semester }}</span>{% endif %}
              {% if course.level %}&nbsp;{{ course.level }}{% endif %}
            </p>
            {% if course.description %}
              <p class="teaching-item-description">{{ course.description }}</p>
            {% endif %}
            {% if course.materials_link %}
              <p class="teaching-item-link"><a href="{{ course.materials_link }}" target="_blank" rel="noopener noreferrer" class="btn-link">Course Materials <i class="fa-solid fa-arrow-up-right-from-square"></i></a></p>
            {% endif %}
          </div>
        {% endfor %}
      </div>
    </section>
  {% endif %}

  {% comment %}
    Display Guest Lectures
  {% endcomment %}
  {% if site.data.teaching.guest_lectures %}
    <section class="teaching-section">
      <h2 class="teaching-section-title"><i class="fa-solid fa-microphone-alt"></i> Guest Lectures</h2>
      <div class="teaching-items-container">
        {% for lecture in site.data.teaching.guest_lectures %}
          <div class="teaching-item">
            <h3 class="teaching-item-title">{{ lecture.title }}</h3>
            <p class="teaching-item-meta">
              {{ lecture.course }} | {{ lecture.institution }}
              {% if lecture.date %} | <span class="teaching-year-highlight">{{ lecture.date | date: "%B %d, %Y" }}</span>{% endif %}
            </p>
            {% if lecture.description %}
              <p class="teaching-item-description">{{ lecture.description }}</p>
            {% endif %}
            {% if lecture.slides_link %}
              <p class="teaching-item-link"><a href="{{ lecture.slides_link }}" target="_blank" rel="noopener noreferrer" class="btn-link">Slides <i class="fa-solid fa-arrow-up-right-from-square"></i></a></p>
            {% endif %}
          </div>
        {% endfor %}
      </div>
    </section>
  {% endif %}

</div>
