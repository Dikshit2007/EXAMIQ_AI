# 🎯 ExamIQ AI

Predict. Practice. Perform.

ExamIQ AI is an AI-powered exam preparation tool that helps students analyze notes, identify important topics from previous year question papers (PYQs), and generate mock tests based on exam patterns.

---

## 📌 Problem Statement

Students spend a significant amount of time manually studying notes and analyzing previous year question papers to identify important topics and exam trends.

This process is repetitive, time-consuming, and often inefficient.

ExamIQ AI automates this workflow using Artificial Intelligence, helping students prepare smarter and faster.

---

## 🚀 Features

### 📚 Notes Analyzer
Upload study notes and get:

- Summary
- Important Topics
- Key Concepts
- Predicted Questions
- Quick Revision Points

---

### 📄 PYQ Analyzer
Upload multiple previous year question papers and get:

- Frequently Asked Topics
- Exam Trends
- Important Questions
- Topic Frequency Analysis
- Pattern Insights

---

### 📝 Mock Test Generator
Upload PYQs and generate:

- New Mock Test Papers
- Similar Question Patterns
- Similar Difficulty Level
- Similar Marks Distribution

---

### 🔍 OCR Support
Supports scanned PDFs using Tesseract OCR.

This enables analysis of image-based question papers and notes.

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Gemini 2.5 Flash

### OCR
- Tesseract OCR

### PDF Processing
- PyPDF2

### Environment Management
- Python Dotenv

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ExamIQ-AI.git
cd ExamIQ-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GEMINI_API_KEY=<YOUR_KEY_HERE>
```

Run the application:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
ExamIQ-AI/
│
├── app.py
├── requirements.txt
├── .env.example
│
├── utils/
│   ├── pdf_reader.py
│   └── prompts.py
│
├── screenshots/
│
├── README.md
├── development_log.md
└── .gitignore
```

---

## 📸 Screenshots

### Home Page

Add screenshot here.

### Notes Analyzer

Add screenshot here.

### PYQ Analyzer

Add screenshot here.

### Mock Test Generator

Add screenshot here.

---

## 🔄 Workflow

PDF Upload

↓

Text Extraction

↓

OCR (if required)

↓

Gemini AI Analysis

↓

Results Generated

↓

Student Preparation

---

## 🔮 Future Improvements

- User Authentication
- Subject-wise Analysis
- Download Mock Tests as PDF
- Difficulty Level Analysis
- Personalized Study Plans
- Cloud Deployment

---

## 👨‍💻 Developed For

AI Vibe Coding Challenge 2026

Built using AI-assisted development, prompt engineering, and modern AI tools.