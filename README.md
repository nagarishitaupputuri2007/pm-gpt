# 🚀 PM-GPT  
### An AI Co-Pilot for Product Managers

PM-GPT is a **decision-support system for Product Managers** that combines NLP techniques with established Product Management frameworks to help teams move from  
**raw user feedback → structured decisions → actionable product roadmaps**.

Unlike traditional ML projects that focus on prediction accuracy, PM-GPT focuses on  
**how product decisions are made, explained, and communicated**.

---

## 🚩 Problem Statement

Modern product teams receive large volumes of unstructured user feedback in the form of reviews, complaints, and feature requests.

Manually analyzing this feedback to identify real product problems and decide what to build next is:

- Time-consuming  
- Highly subjective  
- Difficult to justify to stakeholders  

While AI tools exist for text analysis and PM frameworks exist for prioritization, there are very few systems that **connect both into a single, end-to-end decision workflow**.

PM-GPT is designed to bridge this gap.

---

## 🎯 Objectives

- Analyze raw user feedback using NLP techniques  
- Identify recurring product problems  
- Convert problems into actionable feature ideas  
- Prioritize features using standard PM frameworks (RICE, ICE, Kano, MoSCoW)  
- Generate a realistic 6-month product roadmap  
- Export a complete product analysis as a PDF  

---

## 🧠 System Overview

```
User Feedback
   ↓
Text Cleaning & NLP Processing
   ↓
Problem Identification
   ↓
Feature Ideation
   ↓
Feature Prioritization (RICE)
   ↓
Roadmap Generation
   ↓
Streamlit Web Interface
   ↓
Full Analysis PDF Export
```

---

## 🗂️ Project Structure

```
pm-gpt/
├── assets/
│   └── screenshots/
├── data/
├── nlp/
├── product/
├── roadmap/
├── ui/
├── exports/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧩 Core Features

### 🔍 Problem Insight
Converts unstructured feedback into clear, human-readable product problems.

### 🛠 Feature Generation
Translates identified problems into concrete, actionable feature ideas.

### 📐 Framework-Based Prioritization
Supports auto and manual framework selection with transparent scoring and explanation.

### 🗺 6-Month Product Roadmap
Quarter-based roadmap (Q1–Q3) reflecting realistic PM planning.

### 📤 Full Analysis PDF Export
Generates a complete PM-style document suitable for stakeholders and interviews.

---

## 🧪 Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- ReportLab  

---

## 🧠 Design Philosophy

PM-GPT is intentionally **deterministic and explainable**.
The goal is to support — not replace — PM judgment.

---

## 👤 Author

**Upputuri Naga Rishita**  
B.Tech Computer Science Engineering  
Specialization: AI & Future Technology
