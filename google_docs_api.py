"""Creates and updates Google Docs"""

from config import docs_service, drive_service

doc_store = {}

def get_or_create_doc(doc_name, user_email):
    """
    Checks if a document exists or creates a new one.
    """
    if doc_name in doc_store:
        return doc_store[doc_name]

    document = docs_service.documents().create(body={"title": doc_name}).execute()
    doc_id = document["documentId"]
    doc_store[doc_name] = doc_id

    print(f"✅ Document created: {doc_name} → https://docs.google.com/document/d/{doc_id}")

    if user_email:
        share_document_with_user(doc_id, user_email)

    return doc_id

def save_text_to_doc(doc_id, text):
    """
    Appends extracted text to a Google Doc.
    """
    requests = [{"insertText": {"location": {"index": 1}, "text": f"\n\n📸 Screenshot OCR:\n{text}"}}]
    docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

    print(f"✅ Extracted text saved to Google Doc: https://docs.google.com/document/d/{doc_id}")

def share_document_with_user(doc_id, user_email):
    """
    Grants access to the created Google Doc for a specific user.
    """
    permission = {
        "type": "user",
        "role": "writer",
        "emailAddress": user_email
    }

    drive_service.permissions().create(
        fileId=doc_id,
        body=permission,
        fields="id"
    ).execute()

    print(f"📧 Document shared with {user_email}")
