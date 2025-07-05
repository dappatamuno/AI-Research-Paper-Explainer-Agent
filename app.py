import streamlit as st
from pdf_reader import extract_text_sections
from explain import explain_sections

st.set_page_config(page_title="AI Research Paper Explainer", layout="wide")

st.title("🤖 AI Research Paper Explainer Agent")
st.write("Upload an AI/ML research paper in PDF format to get simplified explanations of the abstract, methodology, results, and more.")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting and simplifying content..."):
        text_sections = extract_text_sections(uploaded_file)
        explanations = explain_sections(text_sections)

    for section, content in text_sections.items():
        st.subheader(section)
        st.text_area("Original", content, height=150)
        st.text_area("Simplified", explanations.get(section, ""), height=150)
