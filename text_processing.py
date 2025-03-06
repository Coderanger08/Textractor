"""Cleans the raw OCR text output"""

def clean_text(raw_text):
    """
    Cleans extracted text by removing empty lines and extra spaces.
    """
    cleaned_text = raw_text.strip()
    return "\n".join([line.strip() for line in cleaned_text.splitlines() if line.strip()])
