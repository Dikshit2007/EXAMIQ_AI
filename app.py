import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils.prompts import (
    NOTES_PROMPT,
    PYQ_PROMPT,
    MOCK_TEST_PROMPT
)
from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import NOTES_PROMPT, PYQ_PROMPT

# ----------------------------
# Load Environment Variables
# ----------------------------

load_dotenv(".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found. Add it to .env file")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Streamlit Config
# ----------------------------

st.set_page_config(
    page_title="ExamIQ AI",
    page_icon="🎯",
    layout="wide"
)

# ============================
# CUSTOM CSS
# ============================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    max-width:1000px;
}

.stTabs [data-baseweb="tab-list"]{
    gap:20px;
}

.stTabs [data-baseweb="tab"]{
    height:60px;
    font-size:18px;
    font-weight:600;
    border-radius:12px;
    background:#1f1f1f;
    padding:10px 25px;
}

.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

.result-box{
    background:#1a1a1a;
    padding:20px;
    border-radius:12px;
    border:1px solid #333;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR
# ============================

with st.sidebar:
    st.title("🎯 ExamIQ AI")

    st.markdown("---")

    st.markdown("""
### Features

✅ Notes Analyzer

✅ PYQ Analyzer

✅ OCR Support

✅ AI Predictions

✅ Model Answers
""")

    st.markdown("---")

    st.success("Powered by Gemini 2.5 Flash")

# ============================
# HERO SECTION
# ============================

st.markdown("""
<div style='text-align:center;padding:20px'>
<h1>🎯 ExamIQ AI</h1>
<p style='font-size:20px;color:gray'>
Predict. Practice. Perform.
</p>
</div>
""", unsafe_allow_html=True)

# ============================
# FEATURE CARDS
# ============================


tab1, tab2, tab3 = st.tabs([
    "📚 Notes Analysis",
    "📄 PYQ Analysis",
    "📝 Mock Test Generator"
])

# ============================
# NOTES ANALYZER
# ============================

with tab1:

    st.markdown("## 📚 Notes Analyzer")
    st.caption(
        "Upload study notes and generate summaries, important topics, questions and answers."
    )

    notes_pdf = st.file_uploader(
        "Upload Notes PDF",
        type=["pdf"],
        key="notes"
    )

    if st.button("Analyze Notes"):

        if notes_pdf is None:
            st.warning("Please upload a Notes PDF.")

        else:

            try:

                with st.spinner("Reading PDF..."):
                    notes_text = extract_text_from_pdf(notes_pdf)

                with st.spinner("Analyzing with Gemini AI..."):
                    prompt = NOTES_PROMPT + "\n\n" + notes_text
                    response = model.generate_content(prompt)

                st.success("Analysis Complete!")

                with st.container():
                    st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# ============================
# PYQ ANALYZER
# ============================

with tab2:

    st.markdown("## 📄 PYQ Analyzer")
    st.caption(
        "Upload previous year question papers and predict likely exam questions."
    )

    pyq_files = st.file_uploader(
        "Upload Previous Year Question Papers",
        type=["pdf"],
        accept_multiple_files=True,
        key="pyq"
    )

    if st.button("Analyze PYQs"):

        if not pyq_files:
            st.warning("Please upload at least one PYQ PDF.")

        else:

            try:

                combined_text = ""

                with st.spinner("Reading Question Papers..."):
                    for pdf in pyq_files:
                        combined_text += extract_text_from_pdf(pdf)
                        combined_text += "\n\n"

                combined_text = combined_text[:15000]
                st.session_state["pyq_text"] = combined_text

                with st.spinner("Analyzing PYQs with Gemini AI..."):
                    prompt = PYQ_PROMPT + combined_text
                    response = model.generate_content(prompt)

                st.success("Analysis Complete!")

                with st.container():
                    st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# ============================
# MOCK TEST GENERATOR
# ============================

# ============================
# MOCK TEST GENERATOR
# ============================

with tab3:

    st.markdown("## 📝 Mock Test Generator")

    st.caption(
        "Upload PYQs and generate a pattern-based mock test."
    )

    mock_files = st.file_uploader(
        "Upload Previous Year Question Papers",
        type=["pdf"],
        accept_multiple_files=True,
        key="mock_test"
    )

    exam_type = st.selectbox(
        "Select Mock Test Size",
        [
            "20 Marks",
            "50 Marks",
            "100 Marks"
        ]
    )

    if st.button("Generate Mock Test"):

        if not mock_files:
            st.warning("Please upload at least one PYQ PDF.")

        else:

            try:

                combined_text = ""

                with st.spinner("Reading PYQs..."):

                    for pdf in mock_files:
                        combined_text += extract_text_from_pdf(pdf)
                        combined_text += "\n\n"

                combined_text = combined_text[:15000]

                with st.spinner("Generating Mock Test..."):

                    prompt = f"""
Generate a {exam_type} mock test.

{MOCK_TEST_PROMPT}

Previous Year Question Papers:

{combined_text}
"""

                    response = model.generate_content(prompt)

                st.success("Mock Test Generated!")

                st.markdown(response.text)

            except Exception as e:
                st.error(str(e))