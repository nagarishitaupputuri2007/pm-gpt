
# PM-GPT  
### An AI Co-Pilot for Product Managers

PM-GPT is an AI-assisted decision-support system designed to help Product Managers analyze user feedback, identify key product problems, prioritize features using industry-standard frameworks, and generate data-driven product roadmaps.

Unlike traditional ML projects that focus on prediction, PM-GPT focuses on **decision-making**, combining NLP techniques with Product Management methodologies.

---

## 🚀 Problem Statement

Modern product teams receive large volumes of user feedback in the form of reviews, complaints, and feature requests.  
Manually analyzing this feedback to identify real product problems and decide what to build next is time-consuming, subjective, and error-prone.

There is a lack of tools that bridge:
- AI-based feedback analysis  
- Structured product decision-making frameworks  

PM-GPT aims to close this gap.

---

## 🎯 Objectives

- Analyze raw user feedback using NLP
- Detect recurring product problems
- Convert problems into actionable feature ideas
- Prioritize features using the RICE framework
- Generate a product roadmap to support PM decision-making

---

## 🧠 System Overview

User Feedback  
↓  
Text Cleaning & NLP Processing  
↓  
Problem Detection (Clustering)  
↓  
Feature Generation  
↓  
Feature Prioritization (RICE)  
↓  
Roadmap Generation  
↓  
Web Interface (Streamlit)

Each module follows a **single-responsibility design** to ensure clarity, maintainability, and extensibility.

---

## 🗂️ Project Structure

```text
pm-gpt/
├── data/          # User feedback datasets
├── nlp/           # NLP processing modules
├── product/       # Product logic & prioritization
├── roadmap/       # Roadmap generation logic
├── ui/            # Streamlit web application
├── main.py        # System orchestrator
└── README.md
