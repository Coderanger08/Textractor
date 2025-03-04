import pytesseract  # Optical Character Recognition (OCR) library
from PIL import Image  # Image handling
import tkinter as tk  # GUI module for file selection
from tkinter import filedialog  # To open file selection dialog
import googleapiclient.discovery  # Google API client for Docs & Drive
from google.oauth2 import service_account  # Google service account authentication

# ============================
# ✅ CONFIGURATION & AUTHENTICATION
# ============================

# Set the path to Tesseract OCR (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the Google API credentials JSON file (rename your downloaded JSON to credentials.json)
SERVICE_ACCOUNT_FILE = r"C:\Users\User\Desktop\VS-Code projects\credentials.json"

# Required Google API Scopes for Google Docs & Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/documents",  # Access Google Docs
    "https://www.googleapis.com/auth/drive"  # Access Google Drive (for document sharing)
]

# Authenticate using the service account
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize Google Docs and Google Drive API clients
docs_service = googleapiclient.discovery.build("docs", "v1", credentials=credentials)
drive_service = googleapiclient.discovery.build("drive", "v3", credentials=credentials)

# Store document IDs to prevent duplicate creation
doc_store = {}

# ============================
# ✅ FUNCTION: FILE SELECTION FIX (Ensures the file dialog appears every time)
# ============================

def select_image():
    """
    Opens file dialog for user to select an image.
    Ensures the dialog appears on top of VS Code.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    root.attributes('-topmost', True)  # Force it to appear on top
    root.update()  # Update the window to bring it to the foreground

    file_path = filedialog.askopenfilename(
        title="Select a Screenshot",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    root.destroy()  # Close Tkinter after selection
    return file_path

# ============================
# ✅ FUNCTION: SHARE DOCUMENT WITH USER
# ============================

def share_document_with_user(doc_id, user_email):
    """
    Grants access to the created Google Doc for a specific user.
    
    Parameters:
    - doc_id (str): The ID of the Google Document.
    - user_email (str): The email address of the user to share with.
    """
    permission = {
        "type": "user",  # Sharing with a specific user
        "role": "writer",  # User will have editing access; change to "reader" for view-only
        "emailAddress": user_email
    }

    drive_service.permissions().create(
        fileId=doc_id,
        body=permission,
        fields="id"
    ).execute()

    print(f"📧 Document shared with {user_email}")

# ============================
# ✅ FUNCTION: CREATE OR GET EXISTING DOCUMENT
# ============================

def get_or_create_doc(doc_name, user_email):
    """
    Checks if a document with the given name exists, or creates a new one.

    Parameters:
    - doc_name (str): The name of the Google Document.
    - user_email (str): The email address to share the document with (if provided).

    Returns:
    - doc_id (str): The ID of the Google Document.
    """
    if doc_name in doc_store:
        return doc_store[doc_name]  # Return existing document ID

    # Create a new Google Doc with the specified title
    document = docs_service.documents().create(body={"title": doc_name}).execute()
    doc_id = document["documentId"]
    doc_store[doc_name] = doc_id  # Store the document ID to avoid recreating it

    print(f"✅ New document created: {doc_name} → https://docs.google.com/document/d/{doc_id}")

    # If an email is provided, share the document with the user
    if user_email:
        share_document_with_user(doc_id, user_email)

    return doc_id

# ============================
# ✅ MAIN PROCESS: OCR & DOCUMENT UPDATING
# ============================

# 📌 Ask user for the document name only once
doc_name = None
doc_id = None

# 📌 Ask user for email once (optional)
user_email = input("\n📧 Enter your Google email to receive document access (leave blank to skip): ").strip()

while True:
    # ============================
    # 📌 STEP 1: SELECT AN IMAGE FILE
    # ============================

    image_path = select_image()

    if not image_path:
        print("❌ No image selected. Exiting...")
        break

    print(f"📂 Selected file: {image_path}")

    # ============================
    # 📌 STEP 2: PERFORM OCR TO EXTRACT TEXT
    # ============================

    # Open the selected image
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    raw_text = pytesseract.image_to_string(image)

    # Clean up extracted text: Remove empty lines and extra spaces
    cleaned_text = raw_text.strip()
    cleaned_text = "\n".join([line.strip() for line in cleaned_text.splitlines() if line.strip()])

    # ============================
    # 📌 STEP 3: CHOOSE DOCUMENT (NEW OR EXISTING) ONLY ONCE
    # ============================

    if doc_id is None:  # Only ask the first time
        while True:
            choice = input("\n📜 Save text to an existing document or create a new one? (1 = Same Doc, 2 = New Doc): ").strip()

            #1(same doc): Saves all extracted text in the same document
            #2(New doc): Creates a new Google Doc every time you select an image
            if choice == "1":
                doc_name = input("Enter the document name to append to: ").strip()
                break  # Exit the loop when valid input is given
            elif choice == "2":
                doc_name = input("Enter a name for the new document: ").strip()
                break  # Exit the loop when valid input is given
            else:
                print("❌ Invalid input! Please enter '1' or '2' to proceed.")

        # Get or create the document
        doc_id = get_or_create_doc(doc_name, user_email)

    # ============================
    # 📌 STEP 4: SAVE TEXT TO GOOGLE DOCS
    # ============================

    # Append extracted text to the Google Document
    requests = [{"insertText": {"location": {"index": 1}, "text": f"\n\n📸 Screenshot OCR:\n{cleaned_text}"}}]
    docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

    print(f"✅ Extracted text saved to Google Doc: https://docs.google.com/document/d/{doc_id}")

    # ============================
    # 📌 STEP 5: ASK IF USER WANTS TO PROCESS ANOTHER IMAGE
    # ============================

    while True:
        continue_choice = input("\n📌 Do you want to process another screenshot? (y/n): ").strip().lower()
        if continue_choice == "y":
            break  # Restart the loop to allow another image selection
        elif continue_choice == "n":
            print("👋 Exiting the program. Goodbye!")
            exit()  # Completely exit the program
        else:
            print("❌ Invalid input! Please enter 'y' to continue or 'n' to exit.")
