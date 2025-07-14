# 🧠 AI Resume Recruiter

[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-green?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![Made with 💙](https://img.shields.io/badge/Built%20with-💙%20NLP%20+%20BERT-brightgreen)](#)

AI-powered Resume Screening and Job Matching Tool built with Streamlit, BERT embeddings, and NLP tools. Upload a resume and job description — get back insights, recommendations, and match scores.

---

## 📌 Features

- 📄 Upload PDF resumes and .txt job descriptions  
- 🧠 Analyze resumes for skills, education, red flags, and career progression  
- 🔍 Semantic matching using BERT (Sentence Transformers)  
- 📊 Screening with qualification, experience & culture-fit indicators  
- 🧭 Final recommendations with job match suggestions  
- 📈 Visualizations with matplotlib, seaborn, altair, wordcloud  
- 💬 Fully modular and expandable architecture  

---

## 🗂️ File Structure

📦 AI-Resume-Recruiter
├── main.py
├── resume_upload.py
├── jd_input.py
├── analysis.py
├── job_matches.py
├── screening.py
├── recommendation.py
├── requirements.txt
└── README.md


---

## 🚀 Deployment (Streamlit Cloud)

> ✅ No payment required — 100% free hosting for small apps

### 1. Push to GitHub  
Make sure your repo includes:
- `main.py`
- `requirements.txt`
- All your Python files

### 2. Add requirements.txt  
```txt
streamlit
pymupdf
nltk
spacy
sentence-transformers
scikit-learn
torch
matplotlib
seaborn
wordcloud
altair
faiss-cpu
numpy
pandas
regex
```

### 3. Go to streamlit.io/cloud
Click "Deploy an app"

Choose your repo

Set main.py as the entry point

Done! 🎉

---

### 🔧 Post Install Instructions

python -m spacy download en_core_web_sm

### In your code (top of main.py):

import nltk
nltk.download('punkt')
nltk.download('stopwords')

---

### 📊 Resume Analysis Sections

| Section                | Description                          |
| ---------------------- | ------------------------------------ |
| **Key Skills**         | Extracted from resume using NLP      |
| **Education**          | Degree and institution detection     |
| **Experience**         | Estimated from text and job titles   |
| **Red Flags**          | Gaps, short stints, etc.             |
| **Career Progression** | Hierarchical growth analysis         |
| **Recommendations**    | Missing skills and improvement areas |
| **Confidence Score**   | Matching accuracy estimate           |

---

### 📁 Modules Overview

| File                | Responsibility                       |
| ------------------- | ------------------------------------ |
| `main.py`           | UI and routing for all tabs          |
| `resume_upload.py`  | Resume PDF upload and parsing        |
| `jd_input.py`       | Job description input (write/upload) |
| `analysis.py`       | NLP-driven resume breakdown          |
| `job_matches.py`    | Semantic similarity using BERT       |
| `screening.py`      | Screening score breakdown            |
| `recommendation.py` | Final decision logic                 |

---

### 📌 Technologies Used

Frontend: Streamlit

Resume Parsing: PyMuPDF (fitz)

Text Preprocessing: NLTK, spaCy

Semantic Matching: Sentence Transformers (BERT)

Machine Learning: Scikit-learn, torch

Similarity Search: Faiss (optional)

Visualization: matplotlib, seaborn, altair, wordcloud

---

### 🛠 Sample Inputs (to test locally)

📄 resume.pdf

📑 job_description.txt (write or upload)

---

### 📬 Contact
Made with 💙 by Mandy

---

### 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.



