"""This file stores Google API authentication and Tesseract OCR path"""

import pytesseract
from google.oauth2 import service_account
import googleapiclient.discovery

# ✅ Set up Tesseract OCR path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ✅ Google API Authentication
SERVICE_ACCOUNT_FILE = r"C:\Users\User\Desktop\VS-Code projects\credentials.json"

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive"
]

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
docs_service = googleapiclient.discovery.build("docs", "v1", credentials=credentials)
drive_service = googleapiclient.discovery.build("drive", "v3", credentials=credentials)
