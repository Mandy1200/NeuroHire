# 🧠 NeuroHire – AI Resume Recruiter

A modular, NLP-powered AI application for **resume screening**, **job matching**, and **visual feedback**. Built using **Streamlit**, **FAISS**, and **BERT embeddings** with advanced resume parsing, scoring intelligence, and personalized recommendations.

NeuroHire transforms the traditional hiring process with deep semantic insights, resume red-flag detection, and a visually guided recruitment dashboard. Recruit smarter, faster, and fairer — powered by real-time machine learning.

---
Project Link : https://airecruiterapp.streamlit.app/

Full Website : https://codezens.vercel.app/

Project Demo : https://drive.google.com/file/d/1fUyFEpyaUV-0_jNrH8iwpqu49uVSiVjE/view?usp=sharing

## 📌 Features

* 📄 Upload PDF resumes and text-based Job Descriptions (JD)
* 🧠 Analyze resumes for:

  * Skills
  * Education
  * Red flags
  * Career progression
* 🔍 Semantic JD-resume matching using **Sentence Transformers** (MiniLM)
* 📊 Screening with qualification, experience & culture-fit indicators
* 🧽 Role-fit scoring and recommendation
* 📈 Visual insights (bar charts, pie charts, skill overlap, ATS match %)
* 🦮 Modular architecture with FAISS, regex, and NLP utilities

---

## 📁 Project Structure

```
📆 AI-Resume-Recruiter
🔼 main.py                  # App entry point and routing
🔼 resume_upload.py        # Resume upload + PDF parsing
🔼 jd_input.py             # JD input (text or PDF)
🔼 analysis.py             # Core resume analysis and NLP insights
🔼 job_matches.py          # FAISS-based similarity analysis
🔼 screening.py            # Screening metrics and scoring
🔼 recommendation.py       # Final recommendation logic
🔼 faiss_engine.py         # Sentence encoding and FAISS engine
🔼 nlp_utils.py            # All helper functions and NLP pipelines
🔼 requirements.txt        # Dependencies
🔼 README.md
```

---

## 🚪 Installation

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 📦 requirements.txt (core)

```
streamlit
sentence-transformers
faiss-cpu
pymupdf
matplotlib
seaborn
numpy
regex
nltk
spacy
altair
wordcloud
```

### 📥 Post Install (for spaCy & NLTK)

```bash
python -m spacy download en_core_web_sm

import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 Functional Requirements

1. Resume Upload & Parsing
2. Job Description Input (Text/PDF)
3. Skill Extraction
4. JD–Resume Matching Engine
5. Screening Analysis
6. Role Fit Recommendation
7. Resume Visual Insights (Graphs & Charts)
8. Multi-JD Matching with FAISS
9. Career Path Inference
10. Certification & Achievement Extraction
11. Experience Estimation
12. Education Detection
13. Summary Metrics and Confidence Score

---

## ⚙️ Non-Functional Requirements

* UI Responsiveness (Streamlit performance)
* Session Persistence (`st.session_state`)
* Data Privacy & Secure File Handling
* Modular Code Structure (pluggable architecture)
* Efficient Inference with lightweight transformers
* Visualization: matplotlib, seaborn, altair

---

## 🔐 Technical Requirements

### 1. Programming Language & Environment

* Python 3.8+
* Streamlit Web App

### 2. Core Libraries

| Library                  | Purpose                      |
| ------------------------ | ---------------------------- |
| sentence-transformers    | Text embeddings (MiniLM)     |
| faiss-cpu                | High-speed similarity search |
| pymupdf                  | PDF parsing                  |
| matplotlib / seaborn     | Graphs and charts            |
| nltk / spacy             | NLP tools                    |
| numpy / regex / tempfile | Data utilities               |

---

## 🚀 Future Enhancements

* JD–Resume Chatbot Q\&A
* AI Feedback for Resume Lines
* PDF Report Export per Tab
* JD Skill Taxonomy Generation
* Role-Based Interview Questions
* Admin Dashboard for Recruiters

---

## 📊 Resume Analysis Modules

| Section            | Description                                   |
| ------------------ | --------------------------------------------- |
| Key Skills         | Extracted from resume using NLP               |
| Education          | Degree and institution detection              |
| Experience         | Estimated from roles and years                |
| Red Flags          | Gaps, short stints, or missing data           |
| Career Progression | Hierarchical growth from intern to leadership |
| Confidence Score   | AI confidence based on input                  |
| Recommendations    | Suggestions for improvements                  |

---

## 📬 Contact

**Made with 💙 by Mandy**

---


