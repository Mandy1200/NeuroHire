# 📁 File: resume_upload.py

import streamlit as st
import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def handle_resume_upload():
    uploaded_file = st.sidebar.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.sidebar.success("✅ Resume uploaded and processed.")
        return resume_text
    return None
