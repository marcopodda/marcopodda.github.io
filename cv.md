---
layout: page
title: Curriculum Vitae
permalink: /cv/
---

{% comment %}
  Loops through sections defined in _data/cv.yaml and renders each.
{% endcomment %}
{% for section in site.data.cv %}
  <section class="cv-section">
    <h2 class="cv-section-title">
      {%- if section.icon -%}<i class="{{ section.icon }}"></i> {%- endif -%}
      {{ section.title }}
    </h2>
    <div class="cv-section-content">
      {% for item in section.items %}
        <div class="cv-item">
          {% if section.title == "Education" %}
            <h3 class="cv-item-title">{{ item.degree }}</h3>
            <p class="cv-item-meta">
              {%- if item.years -%}<span class="cv-year-highlight">{{ item.years }}</span>{%- endif -%}
              {%- if item.university -%}, {{ item.university }}{%- endif -%}
            </p>
            {% if item.details %}
              <p class="cv-item-details">{{ item.details | markdownify }}</p>
            {% endif %}
          {% elsif section.title == "Academic Positions" %}
            <h3 class="cv-item-title">{{ item.position }}</h3>
            <p class="cv-item-meta">
              {%- if item.years -%}<span class="cv-year-highlight">{{ item.years }}</span>{%- endif -%}
              {%- if item.institution -%}&nbsp;{{ item.institution }}{%- endif -%}
            </p>
            {% if item.details %}
              <p class="cv-item-details">{{ item.details | markdownify }}</p>
            {% endif %}
          {% elsif section.title == "Awards & Honors" %}
            <h3 class="cv-item-title">{{ item.name }}</h3>
            <p class="cv-item-meta">
              {%- if item.year -%}<span class="cv-year-highlight">{{ item.year }}</span>{%- endif -%}
              {%- if item.awarder -%}, {{ item.awarder }}{%- endif -%}
            </p>
            {% if item.details %}
              <p class="cv-item-details">{{ item.details | markdownify }}</p>
            {% endif %}
          {% elsif section.title == "Skills" %}
            <h3 class="cv-item-title">{{ item.category }}</h3>
            <p class="cv-item-list">{{ item.list }}</p>
          {% elsif section.title == "Languages" %}
            {% if item.details %}
              <p class="cv-item-details">{{ item.details | markdownify }}</p>
            {% endif %}
            {% if item.language %}
              <p class="cv-item-title">{{ item.language }}</p>
              <p class="cv-item-meta">{{ item.level }}</p>
            {% endif %}
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </section>
{% endfor %}
