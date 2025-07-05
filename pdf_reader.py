import fitz  # PyMuPDF

def extract_text_sections(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Naive section extraction (can be improved)
    sections = {
        "Abstract": extract_between(text, "Abstract", "Introduction"),
        "Introduction": extract_between(text, "Introduction", "Methodology"),
        "Methodology": extract_between(text, "Methodology", "Results"),
        "Results": extract_between(text, "Results", "Conclusion"),
        "Conclusion": extract_between(text, "Conclusion", None),
    }
    return sections

def extract_between(text, start, end):
    try:
        start_idx = text.index(start)
        end_idx = text.index(end) if end else len(text)
        return text[start_idx + len(start):end_idx].strip()
    except ValueError:
        return ""
