---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Neuroscience and Anthropology, University of Michigan, 2011
* Postgraduate Studies - Economics, Harvard Business School, 2015
* MSc. Statistics and Applied Mathematics, North Carolina State University, expected (2021)

Work and Research experience
======
* <em>May 2019 - Present: Data Scientist<em>
  * Cisco Systems Incorporated - Security and Trust Organization
  * ***Achievements***:
    1. Zero-Trust: Developing signal processing algorithms for detecting privileged insider threats 
    2. Spearheaded new statistical learning approach for identifying counterfeit in telemetry data
    3. Submitted new patent for anomaly detection in defect-tracking systems for development artifacts
    4. Implemented POC novel deep learning bi-LSTM archiecture for search and classification of forensic evidence
    5. Created ARIMA, SARIMA and AR models for extreme-event forecasting of revenue affects after public disclosures
    6. Applied survival analysis estimation for user engagement studies for compliance training
    7. Presented work to executive leadership and liased with stakeholders for continual feedback
  <!-- * Supervisor: Mr. Joe Gipson and Mr. Jeff Schutt -->

* <em>August 2019 - March 2020: Research Assistant<em>
  * North Carolina State University
  * ***Achievements***:
    1. Developed online-training and batch experimentation architecture for transfer learning
    2. Worked on theoretical derivation of function approximation derivation for off-policy exploration
  * Supervisor: Dr. Eric Laber, Department of Statistics

* <em>January 2019 - May 2019: Research Assistant<em>
  * North Carolina State University
  * ***Achievements***:
    1. Implemented Asynchronous Actor Critic Models (A3C) for NFL football and NBA basketball
    2. Formulated and published research report comparing approaches - including Dueling DQN Prioritized Replay - within the context of first-player shooter games
    3. Researched, replicated and extended MDP and Finite Horizon Reinforcement Learning models for spatial decision making
  * Supervisor: Dr. Eric Laber, Department of Statistics

* <em>May 2018 - August 2018, Automation Engineering Intern<em>
  * Compozed Labs, Allstate
  * ***Achievements***:
    1. Created novel RNN speech generation language model to be integrated into RoadSide Service
    2. Architect and implement a proof-of-concept event-driven microservice, written in Golang, that leverages RabbitMQ as a broker and Redis as a persistent backend. Built additional configuration for client to also accommodate Amazon SQS and Memcache as a job queue. 
    3. Developed custom API schema validator package in order to prevent invalid response and requests to be received from third-party vendor applications. The impetus for this features was to adapt to the lack of a consumer-driven contract implementation.
    4. Created and presented a workshop on advanced functional Java concepts for machine learning
  <!-- * Supervisor: Ms. Julie Clayton     -->

* <em>December 2017 - October 2018: Research Assistant<em>
  * North Carolina State University
  * ***Achievements***:
    1. Architected, built, tested and deployed application that visualized predictions from an online deep neural network classifier trained on random Voronoi partitions of a spatial domain. This deep neural network yields remarkably accurate geolocation predictions. When applied to the microbiomes of over 1,300 dust samples collected across the U.S., more than half of predictions produced by this model fall within 90 kilometers of their origin, a 60% reduction in error from competing geolocation methods.
  * Supervisor: Dr. Eric Laber, Department of Statistics    


* <em>August 2017 - December 2017: Research Assistant<em>
  * North Carolina State University
  * ***Achievements***:
    1. Researched and implemented ad Gated Feedback Recurrent Neural Network that predicts the likelihood that a escort post is from a trafficking victim from the raw text.
  * Supervisor: Dr. Eric Laber, Department of Statistics


* <em>December 2016 - July 2017: Software Engineer<em>
  * Social Tables
  * ***Achievements***:
    1. Cofounding member of the Infrastructure Team building service architecture, data engineering tools and data securitization middleware. This included rewriting roles and permissions management for all applications and building a core data platform to provision all applications with proprietary customer data.
    2. Rearchitected entire front-end of legacy product into mobile-first application – delivered $40,000 in revenue within first two weeks of re-release: Event Sales Solution
  <!-- * Supervisor: Mr. Hunter Powers -->

* <em>April 2016 - November 2016: Software Engineer<em>
  * DivvyCloud
  * ***Achievements***:
  1. Spearheaded the development of an automated testing, orchestration and deployment framework using Docker, Python and AWS S3
  2. Prototyped and deployed memory and request monitoring data pipeline for production deployments using Elasticsearch, Akka, and Scala. Result: Reduced false positive rate for customer-reported memory leaks and excessive resource utilization by 72% in one quarter
  <!-- * Supervisor: Mr. Chris Deramus -->

* <em>June 2015 - March 2016: Associate Technologist<em>
  * Wynyard Group
  * ***Achievements***:
  1. Developed and optimized ETL pipelines using Cassandra, PySpark,
  Python, Pandas and Spark in order to deploy logistic regression
  model for classifying anomalous financial transactions.
  2. Applied and tested n-gram models, tf-idf, Hidden Markov Model,
  Bayesian Bag of Words, in order to describe and to classify audio transcripts and forensic evidence sourced from law-enforcement and national security agencies.
  3. Developed visualizations using d3.js, AngularJS and crossfilter.js, in order to present exploratory data analysis and data mining efforts for geospatial classification of entities for law enforcement agencies.  

Skills
======
* Fluency in statistical learning theory and application using (among others):
  * Pytorch, Tensorflow and Keras
  * SciPy, scikit-learn, statsmodels, and lifelines
  * PyMC3 an ArviZ
  * Numba
* Natural Language Processing with Deep Learning
  * Named Entity Recognition and constituency parsing
  * Word window classification 
  * Dependency parsing
  * Contextual Word Representations
  * Seq2Seq and attention networks  
* Distributed Computing and Data Engineering leveraging:
  * Scala
  * Airflow
  * Kafka
  * Spark and Spark ML
  * Snowflake
  * Google Compute Engine
  * BigQuery
  * Apache Arrow
* Bayesian Estimation and Hierarchical Models:
  * Latent-Dirichelet Allocation
  * Non-parametric hypothesis testing (two sample, etc.)
  * Clustering with Gaussian Mixtures  
* Causal Inference Theory and Application including:
  * Propensity Scoring
  * Matching
  * Difference-in-Difference estimation
  * Mixed Effects Models for hierarchical models


Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Service and leadership
======
*  -->
