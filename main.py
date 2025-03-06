from file_manager import select_image
from ocr_extractor import extract_text
from text_processing import clean_text
from google_docs_api import get_or_create_doc, save_text_to_doc

# ✅ Ask for user email (optional)
user_email = input("\n📧 Enter your Google email to receive document access (leave blank to skip): ").strip()
doc_id = None
doc_name = None

while True:
    # 📌 Select Image
    image_path = select_image()

    if not image_path:
        print("❌ No image selected. Exiting...")
        break

    print(f"📂 Selected file: {image_path}")

    # 📌 Perform OCR
    raw_text = extract_text(image_path)
    cleaned_text = clean_text(raw_text)

    # 📌 Choose Document (First Time Only)
    if doc_id is None:
        while True:
            choice = input("\n📜 Save text to an existing document or create a new one? (1 = Same Doc, 2 = New Doc): ").strip()

            if choice == "1":
                doc_name = input("Enter the document name to append to: ").strip()
                break
            elif choice == "2":
                doc_name = input("Enter a name for the new document: ").strip()
                break
            else:
                print("❌ Invalid input! Please enter '1' or '2'.")

        doc_id = get_or_create_doc(doc_name, user_email)

    # 📌 Save to Google Docs
    save_text_to_doc(doc_id, cleaned_text)

    # 📌 Ask to Process Another Image
    while True:
        continue_choice = input("\n📌 Process another screenshot? (y/n): ").strip().lower()
        if continue_choice == "y":
            break
        elif continue_choice == "n":
            print("👋 Exiting. Goodbye!")
            exit()
        else:
            print("❌ Invalid input! Enter 'y' or 'n'.")
