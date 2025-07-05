# 🤖 AI Research Paper Explainer Agent

This app lets you upload AI/ML research papers (PDFs) and get simplified explanations of the paper's core ideas using free and open-source NLP models. Ideal for students, developers, and non-experts.

## 💡 Features
- Upload and read PDF research papers
- Extracts and simplifies Abstract, Methodology, and Results
- Summarizes sections using Hugging Face models
- Simple but clean UI with Streamlit
- Deployable on Streamlit Cloud or Hugging Face Spaces

## 🛠 Tech Stack
- Streamlit
- HuggingFace Transformers (T5, BART, etc.)
- PyMuPDF
- Python, spaCy/NLTK

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Deployment
Deploy on [Streamlit Cloud](https://streamlit.io/cloud) or [Hugging Face Spaces](https://huggingface.co/spaces)

## ✨ Add-ons
- Glossary for AI terms like "backpropagation", "transformer", etc.
- Q&A chatbot interface (optional)
- Semantic search using SentenceTransformers + FAISS
