---
title: "FIT Lab - Publications"
layout: publications
permalink: /publications/
---

{% assign publications_count = site.collections.publications.size %}
<p>Number of publications: {{ publications_count }}</p>


{% assign number_printed = 0 %}

{% if site.collections.publications.size > 0 %}
  {% for publi in site.collections.publications %}
    {% assign even_odd = number_printed | modulo: 2 %}
    {% if publi.weight == 0 %}  <!-- Using 'weight' instead of 'highlight' -->
    
      {% if even_odd == 0 %}
      <div class="row">
      {% endif %}
      
      <div class="col-sm-6 clearfix">
        <div class="well">
          <h3>{{ publi.title }}</h3>
          <p><strong>Authors:</strong> 
            {% for author in publi.authors %}
              {{ author }}{% if forloop.last == false %}, {% endif %}
            {% endfor %}
          </p>
          <p><strong>Venue:</strong> {{ publi.venue }}</p>
          <p><strong>Year:</strong> {{ publi.year }}</p>
          <p><strong>Abstract:</strong> {{ publi.abstract | truncatewords: 50 }}</p>

          <p><a href="{{ publi.links.arxiv }}">Read on Arxiv</a></p>
          <p><a href="{{ publi.links.citations }}">Citations</a></p>
        </div>
      </div>
      
      {% assign number_printed = number_printed | plus: 1 %}
      
      {% if even_odd == 1 %}
      </div>
      {% endif %}
    
    {% endif %}
  {% endfor %}

  {% assign even_odd = number_printed | modulo: 2 %}
  {% if even_odd == 1 %}
  </div>
  {% endif %}

{% else %}
  <p>No publications found.</p>
{% endif %}
