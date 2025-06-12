---
layout: default
title: Publications
permalink: /publications/
---

<div class="constrained-content">
    <h1>My Publications</h1>
    {% assign sorted_publications = site.data.publications | sort: 'year' | reverse %}
    {% assign current_year = null %}
    {% for publication in sorted_publications %}
      {% if publication.year != current_year %}
        {% assign current_year = publication.year %}
        <div class="bibliography-year">
          <h2>{{ current_year }}</h2>
        </div>
      {% endif %}
      <div class="publication-item">
        <p class="publication-authors">{{ publication.authors }}</p>
        <h3 class="publication-title">{{ publication.title }}</h3>
        <p class="publication-details">
            {% comment %} Authors are already above, so start with (Year). Title. {% endcomment %}
            {%- if publication.type == "Journal" -%}
                {%- if publication.journal -%}
                    <em>{{- publication.journal -}}</em>
                    {%- if publication.volume -%},&nbsp;{{- publication.volume -}}{%- endif -%}
                    {%- if publication.number -%}({{- publication.number -}}){%- endif -%}
                    {%- if publication.pages -%}, pp. {{- publication.pages -}}{%- endif -%}
                    .
                {%- endif -%}
            {%- elsif publication.type == "Conference" -%}
                {%- if publication.booktitle-%}
                  In <em>{{ publication.booktitle }}</em>
                {%- endif -%}
                {%- if publication.pages -%}
                  &nbsp;(pp. {{ publication.pages }}).
                {%- else -%}
                  .
                {%- endif -%}
                {%- if publication.publisher -%}
                    &nbsp;{{- publication.publisher -}}.
                {%- endif -%}
            {%- elsif publication.type == "Book Chapter" -%}
                {%- if publication.booktitle-%}
                  In <em>{{ publication.booktitle }}</em>
                {%- endif -%}
                {%- if publication.pages -%}
                  &nbsp;(pp. {{ publication.pages }}).
                {%- else -%}
                .
                {%- endif -%}
                {%- if publication.publisher -%}
                    &nbsp;{{- publication.publisher -}}.
                {%- endif -%}
            {%- elsif publication.type == "Abstract" -%}
                {%- if publication.journal -%}
                    <em>{{- publication.journal -}}</em>
                    {%- if publication.volume -%},&nbsp;{{- publication.volume -}}{%- endif -%}
                    {%- if publication.number -%}({{- publication.number -}}){%- endif -%}
                    {%- if publication.pages -%}, pp. {{- publication.pages -}}{%- endif -%}
                    .
                {%- else -%}
                  {%- if publication.booktitle-%}
                    In <em>{{ publication.booktitle }}</em>
                  {%- endif -%}
                  {%- if publication.pages -%}
                    &nbsp;(pp. {{ publication.pages }}).
                  {%- else -%}
                    .
                  {%- endif -%}
                  {%- if publication.publisher -%}
                      &nbsp;{{- publication.publisher -}}.
                  {%- endif -%}
                {%- endif -%}
            {%- endif -%}
        </p>
        {% if publication.tags %}
          <div class="publication-tags">
          {% for tag in publication.tags %}
            <span class="tag">{{ tag | capitalize }}</span>
          {% endfor %}
          </div>
        {% endif %}
        <div class="pub-links">
          {% if publication.url %}
            <a href="{{ publication.url }}" target="_blank" rel="noopener noreferrer" class="btn-link">URL</a>
          {% endif %}
          {% if publication.DOI %}
            <a href="https://doi.org/{{ publication.DOI }}" target="_blank" rel="noopener noreferrer" class="btn-link">DOI</a>
          {% endif %}
          {% if publication.pdf %}
            <a href="{{ publication.pdf | relative_url }}" target="_blank" rel="noopener noreferrer" class="btn-link">PDF</a>
          {% endif %}
          {% if publication.code %}
            <a href="{{ publication.code }}" target="_blank" rel="noopener noreferrer" class="btn-link">Code</a>
          {% endif %}
        </div>
      </div>
    {% endfor %}
</div>
