# Development Log

# Project Name

ExamIQ AI

Predict. Practice. Perform.

---

# Challenge

AI Vibe Coding Challenge 2026

---

# Problem Statement

Students spend significant time manually reading notes and previous year question papers to identify important topics, repeated questions, and exam trends.

The goal of ExamIQ AI is to automate this process using Artificial Intelligence and help students prepare more efficiently.

---

# AI Coding Assistants Used

- ChatGPT
- Gemini
- VS Code AI Assistance

---

# AI Models Used

- Gemini 2.5 Flash

Purpose:

- Notes Analysis
- PYQ Analysis
- Mock Test Generation
- Topic Extraction
- Pattern Recognition

---

# Technologies Used

## Frontend

- Streamlit

## Backend

- Python

## AI

- Gemini 2.5 Flash

## OCR

- Tesseract OCR

## PDF Processing

- PyPDF2

## Environment Variables

- Python Dotenv

---

# Features Implemented

## Notes Analyzer

Users can upload study notes in PDF format.

The AI generates:

- Summary
- Important Topics
- Revision Notes
- Predicted Questions
- Key Concepts

---

## PYQ Analyzer

Users can upload multiple previous year question papers.

The AI identifies:

- Frequently Asked Topics
- Exam Trends
- Repeated Questions
- Important Units
- Pattern Insights

---

## Mock Test Generator

Users can upload previous year papers.

The AI generates:

- New Mock Tests
- Similar Question Styles
- Similar Marks Distribution
- Similar Difficulty Levels

based on historical question patterns.

---

## OCR Support

Integrated Tesseract OCR to support scanned PDFs and image-based documents.

This enables extraction of text even when PDFs contain images instead of selectable text.

---

# Important Prompts Used

## Notes Analysis Prompt

Analyze the uploaded notes and provide:

- Summary
- Important Topics
- Key Concepts
- Predicted Questions
- Revision Notes

Format the response clearly using headings.

---

## PYQ Analysis Prompt

Analyze the uploaded previous year question papers and identify:

- Frequently Asked Topics
- Repeated Questions
- Important Units
- Exam Trends
- Question Patterns

Provide a structured report.

---

## Mock Test Generation Prompt

Based on the uploaded previous year question papers:

Generate a new mock test paper.

Requirements:

- Follow similar marks distribution
- Follow similar question styles
- Maintain comparable difficulty level
- Cover important topics identified in analysis

---

# AI Generated Code

AI assisted in generating:

- Streamlit Interface
- Gemini API Integration
- PDF Reading Functions
- OCR Logic
- Prompt Structures
- Mock Test Generator Logic
- Error Handling

---

# Manual Modifications

The following changes were performed manually:

- UI Simplification
- Layout Improvements
- Tab Organization
- Prompt Adjustments
- OCR Configuration
- API Key Management
- Debugging Streamlit Errors
- Testing Multiple PDFs
- Improving Output Formatting

---

# Challenges Faced

## 1. Gemini API Configuration

Initially encountered:

- Invalid model errors
- API key loading issues
- Environment variable configuration problems

Solution:

- Verified available Gemini models
- Updated model configuration
- Fixed .env loading

---

## 2. Scanned PDF Processing

Many question papers contained images instead of text.

Problem:

PyPDF2 could not extract text.

Solution:

Integrated Tesseract OCR to support image-based PDFs.

---

## 3. Streamlit UI Errors

Faced:

- Indentation issues
- Tab configuration errors
- Layout problems

Solution:

Refactored UI structure and simplified layout.

---

## 4. Prompt Optimization

Early outputs were inconsistent.

Solution:

Improved prompts to enforce structured responses and exam-focused analysis.

---

# Lessons Learned

During this project I learned:

- AI-assisted software development
- Prompt engineering
- Gemini API integration
- OCR fundamentals
- Streamlit application development
- Debugging AI-powered systems
- Managing environment variables
- Building MVPs rapidly using AI tools

---

# Future Improvements

- User Authentication
- Cloud Deployment
- Download Reports as PDF
- Performance Tracking
- Subject-wise Analytics
- Question Difficulty Analysis
- Personalized Study Plans
- Database Integration

---

# Conclusion

ExamIQ AI successfully demonstrates how AI can be used to simplify exam preparation by automating note analysis, PYQ analysis, and mock test generation.

The project combines AI, OCR, and PDF processing into a practical productivity tool that helps students study smarter and save time.