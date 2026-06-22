# ExamIQ AI - Development Log

## Project Title

ExamIQ AI – AI-Powered Exam Preparation Assistant

## Objective

To help students analyze study notes and previous year question papers (PYQs) using AI and generate predicted questions and mock tests based on exam patterns.

---

## Day 1 – Project Planning

### Tasks Completed

* Finalized project idea.
* Defined core features:

  * Notes Analyzer
  * PYQ Analyzer
  * Mock Test Generator
* Selected technology stack.

### Decisions Taken

* Frontend: Streamlit
* AI Model: Google Gemini 2.5 Flash
* Language: Python

---

## Day 2 – Notes Analyzer Development

### Tasks Completed

* Implemented PDF upload feature.
* Added text extraction from PDF files.
* Integrated Gemini AI.
* Generated:

  * Important topics
  * Summaries
  * Expected questions

### Challenges

* Handling large PDF files.
* Managing Gemini response length.

### Solutions

* Limited extracted text size before sending to AI.

---

## Day 3 – PYQ Analyzer Development

### Tasks Completed

* Added multiple PYQ upload support.
* Extracted content from question papers.
* Implemented pattern analysis using Gemini.

### Outputs Generated

* Frequently asked topics
* Important units
* Repeated questions
* Exam trends

### Challenges

* Some PDFs contained scanned images.

### Solutions

* Added OCR support using Tesseract OCR.

---

## Day 4 – OCR Integration

### Tasks Completed

* Installed Tesseract OCR.
* Connected OCR with PDF processing.
* Enabled analysis of scanned question papers.

### Result

* Both text-based and scanned PDFs became supported.

---

## Day 5 – Mock Test Generator

### Tasks Completed

* Created Mock Test Generator module.
* Generated mock tests based on:

  * PYQ patterns
  * Question frequency
  * Mark distribution
  * Difficulty level

### Features Added

* 20 Marks Mock Test
* 50 Marks Mock Test
* 100 Marks Mock Test

---

## Day 6 – UI Improvement

### Tasks Completed

* Redesigned interface.
* Simplified navigation.
* Added tab-based workflow.

### Final UI Sections

1. Notes Analyzer
2. PYQ Analyzer
3. Mock Test Generator

---

## Testing

### Test Cases Performed

* Notes PDF Upload
* PYQ Upload
* OCR Extraction
* Gemini Response Generation
* Mock Test Generation

### Result

All major features functioning successfully.

---

## Final Outcome

ExamIQ AI successfully:

* Analyzes notes
* Analyzes previous year question papers
* Detects important topics
* Predicts exam-oriented questions
* Generates AI-based mock tests
* Supports scanned and text PDFs

## Status

MVP Completed and Ready for Submission.
