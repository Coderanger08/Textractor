# Screenshot & OCR Extractor

A Python-based OCR tool that extracts text from images and saves it to **Google Docs** automatically.  
Supports **Google Drive sharing, text formatting, and document organization**.

---

## Features

- **Extracts text from screenshots & images** using Tesseract OCR  
- **Automatically saves text** to Google Docs  
- **Append text** to existing docs or **create new ones**  
- **Share documents via email** (Google Drive API)  
- **Formatted text output** with bold headings & structured layout  
- **Handles API authentication** & permissions efficiently  

---

## How This Project Was Built

### **Idea & Concept**
I wanted to automate text extraction from screenshots and make the process seamless.  
After exploring **Notion, PDFs, and Google Docs**, I chose **Google Docs** for better API support.

### **Development Process**

#### ** Setting Up the Environment**
- Installed **Tesseract OCR**, configured paths, and handled dependencies.  
- Set up **Google Cloud API credentials** for authentication.  

#### ** OCR & Image Processing  **
- Used `pytesseract` to extract text from images.  
- Cleaned & formatted the extracted text.  

#### ** Google Docs Integration  **
- Automated **document creation & updating** via the **Google Docs API**.  
- Implemented **document sharing** via **Google Drive API** (Users can add their email).  

#### **Debugging & Fixes ** 
- Solved **Windows permission errors** for accessing `credentials.json`.  
- Fixed **Google Drive API permission issues** when sharing docs.  

---

## **AI-Assisted Development**
I leveraged AI for guidance, but I actively:  
-  Debugged errors manually  
-  Decided which features to implement  
-  Researched & understood **Google API workflows**  
-  Customized the **formatting & user interaction flow**  

---

## **What I Learned**
-  How OCR works in Python  
-  How to authenticate & interact with **Google Docs API**  
-  How to handle **API-based document sharing**  
-  How to troubleshoot **API permission issues**  
-  How **AI can assist in development** while still requiring critical thinking  

---

## **Getting Started**

### ** Install Dependencies  **
```sh
pip install pytesseract pillow google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

### Install Tesseract OCR 

#### **Windows:**  
1. Download & install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).  
2. Add Tesseract to your system PATH.  
3. Find the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).  

#### **Linux/macOS:**  
```sh
sudo apt install tesseract-ocr  # Ubuntu/Debian
brew install tesseract          # macOS

### 3️⃣ Run the Script  
```sh
python screenshot_ocr.py

### 4️⃣ Select an Image  
- Choose an image file containing text.  
- OCR will extract the text and save it to **Google Docs**.  

---

### 5️⃣ Enter Your Email (Optional)  
- If you want **document access**, enter your Google email.  
- Otherwise, the document will **remain private**.  

## 🛠️ Future Enhancements
- 🔹 **AI-powered text correction** (fix OCR errors using GPT)  
- 🔹 **Export to multiple platforms** (Notion, Trello, PDFs)  
- 🔹 **Auto-detect text language & translate it**  
- 🔹 **Hotkey-based screenshot capture & auto-processing**  

---

## 🤝 Credits & Acknowledgment  
💡 **AI-Assisted Development:**  
I used ChatGPT as an assistant for debugging, research, and structuring API calls,  
but every decision, problem-solving step, and customization was done **manually**.  

---

## 🔗 Links  
✅ **GitHub Repository:** [Insert your GitHub link here]  
✅ **Demo Video (if available):** [Insert link]  
✅ **Google Docs API Guide:** [Google Docs API Docs](https://developers.google.com/docs/api)  
