from transformers import pipeline
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def explain_sections(sections):
    explanations = {}
    for section, text in sections.items():
        if not text:
            explanations[section] = "No content found."
            continue
        # Limit to 1024 tokens for BART
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        simplified = ""
        for chunk in chunks:
            summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
            simplified += summary + " "
        explanations[section] = simplified.strip()
    return explanations
