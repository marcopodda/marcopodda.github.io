---
layout: page
title: CV
permalink: /cv/
---

# Curriculum Vitae

<p>{{ site.data.cv.short_bio | markdownify }}</p>

<h2>Current Position</h2>
<div class="cv-entry">
    <h3>{{ site.data.cv.current_position.title }}</h3>
    <p>{{ site.data.cv.current_position.institution }}<br>
    <em>{{ site.data.cv.current_position.duration }}</em></p>
</div>

<h2>Past Positions</h2>
{% for position in site.data.cv.past_positions %}
<div class="cv-entry">
    <h3>{{ position.title }}</h3>
    <p>{{ position.institution }}<br>
    <em>{{ position.duration }}</em></p>
</div>
{% endfor %}

<h2>Education</h2>
{% for edu in site.data.cv.education %}
<div class="cv-entry">
    <h3>{{ edu.degree }}</h3>
    <p>{{ edu.institution }} ({{ edu.year }})<br>
    <em>{{ edu.details }}</em></p>
</div>
{% endfor %}

<h2>Skills</h2>
<div class="cv-skills">
{% for skill_set in site.data.cv.skills %}
    <p><strong>{{ skill_set.category }}:</strong> {{ skill_set.list }}</p>
{% endfor %}
</div>

{% if site.data.cv.awards_honors %}

<h2>Awards & Honors</h2>
<ul>
{% for award in site.data.cv.awards_honors %}
    <li>{{ award }}</li>
{% endfor %}
</ul>
{% endif %}

<h2 style="margin-top: 3em;">Download Full CV</h2>
<p>
  For a detailed overview of my experience and qualifications, please download my complete Curriculum Vitae in PDF format: <br>
  <a href="{{ '/assets/John_Doe_CV.pdf' | relative_url }}" target="_blank" class="btn">Download CV (PDF)</a>
</p>
