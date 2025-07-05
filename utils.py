# For future text processing functions (cleaning, tokenizing, etc.)

def clean_text(text):
    return text.replace("\n", " ").replace("\xa0", " ").strip()
