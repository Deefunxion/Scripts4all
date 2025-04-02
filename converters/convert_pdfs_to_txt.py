import os
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

# **Ρυθμίζουμε τον φάκελο όπου βρίσκονται τα PDF**
PDF_FOLDER = r"C:\Users\dee\Desktop\ET_GR_REQUESTS"
TXT_FOLDER = os.path.join(PDF_FOLDER, "TXT_Αρχεία")

# **Ορισμός διαδρομής Tesseract OCR (Αν δεν είναι ήδη στο PATH)**
PYTESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH

# **Δημιουργούμε τον φάκελο αποθήκευσης των TXT αν δεν υπάρχει**
os.makedirs(TXT_FOLDER, exist_ok=True)

# **Συνάρτηση για OCR μετατροπή αν το PDF περιέχει εικόνες**
def convert_pdf_with_ocr(pdf_path):
    """Χρησιμοποιεί OCR αν το PDF δεν έχει κανονικό κείμενο"""
    text = ""
    images = convert_from_path(pdf_path)

    for img in images:
        text += pytesseract.image_to_string(img, lang="ell") + "\n"

    return text

# **Συνάρτηση για μετατροπή PDF σε TXT με σωστή αποκωδικοποίηση ελληνικών χαρακτήρων**
def convert_pdf_to_txt(pdf_path, txt_path):
    """Μετατρέπει ένα PDF σε TXT. Αν δεν υπάρχει αναγνώσιμο κείμενο, χρησιμοποιεί OCR"""
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"

        # **Αν δεν βρέθηκε καθόλου κείμενο, χρησιμοποιούμε OCR**
        if not text.strip():
            print(f"⚠ Το PDF {pdf_path} δεν έχει κανονικό κείμενο, χρησιμοποιούμε OCR...")
            text = convert_pdf_with_ocr(pdf_path)

        # **Αποθηκεύουμε το κείμενο σε TXT**
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ PDF σε TXT: {pdf_path} → {txt_path}")
    except Exception as e:
        print(f"❌ Σφάλμα στο {pdf_path}: {e}")

# **Συνάρτηση για επεξεργασία όλων των PDF στον φάκελο**
def process_pdfs(pdf_folder):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdf_files:
        print("❌ Δεν βρέθηκαν αρχεία PDF στον φάκελο.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        txt_filename = os.path.splitext(pdf_file)[0] + ".txt"
        txt_path = os.path.join(TXT_FOLDER, txt_filename)

        convert_pdf_to_txt(pdf_path, txt_path)

# **Εκτέλεση του script**
process_pdfs(PDF_FOLDER)
