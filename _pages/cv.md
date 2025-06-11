---
layout: page
title: CV
permalink: /cv/
---

# Curriculum Vitae

<p>{{ site.data.cv.short_bio | markdownify }}</p> {# markdownify filter allows Markdown in YAML #}

## Current Position

<p>
  **{{ site.data.cv.current_position.title }}**<br>
  {{ site.data.cv.current_position.institution }}<br>
  {{ site.data.cv.current_position.start_date }} - {{ site.data.cv.current_position.end_date }}
</p>

## Past Positions

{% for position in site.data.cv.past_positions %}

<p>
  **{{ position.title }}**<br>
  {{ position.institution }}<br>
  {{ position.start_date }} - {{ position.end_date }}
</p>
{% endfor %}

<h2>Education</h2>
{% for edu in site.data.cv.education %}
<p>
  **{{ edu.degree }}**, {{ edu.institution }} ({{ edu.year }})<br>
  {{ edu.details }}
</p>
{% endfor %}

<h2>Skills</h2>
<p>
  **Programming Languages:** {{ site.data.cv.skills.programming }}<br>
  **Frameworks:** {{ site.data.cv.skills.frameworks }}<br>
  **Tools:** {{ site.data.cv.skills.tools }}
</p>

<h2>Download Full CV</h2>
<p>
  For a detailed overview of my experience and qualifications, please download my full CV:<br>
  <a href="{{ '/assets/John_Doe_CV.pdf' | relative_url }}" target="_blank" class="btn btn-primary">Download CV (PDF)</a>
</p>
