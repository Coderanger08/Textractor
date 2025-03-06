"""Extracts text from images using Tesseract OCR"""

from PIL import Image
import pytesseract

def extract_text(image_path):
    """
    Extracts text from the given image using OCR.
    """
    image = Image.open(image_path)
    raw_text = pytesseract.image_to_string(image)
    return raw_text
