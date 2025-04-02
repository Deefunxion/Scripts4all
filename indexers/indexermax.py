import os
import re
import PyPDF2
import pytesseract
from pdf2image import convert_from_path
import pandas as pd

# Ορισμός του Tesseract – βεβαιώσου ότι το path είναι σωστό
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ορισμός του poppler_path (βεβαιώσου ότι το path είναι σωστό)
poppler_path = r"C:\Users\dee\Release-24.08.0-0\poppler-24.08.0\Library\bin"

# Ορισμός δικού μας regex για παράνομους χαρακτήρες (ASCII 0-8, 11-12, 14-31)
illegal_characters_re = re.compile(r'[\x00-\x08\x0B\x0C\x0E-\x1F]')

def extract_text_from_pdf(pdf_path):
    """
    Εξάγει το κείμενο από την πρώτη σελίδα ενός PDF.
    Αν δεν υπάρχει αναγνώσιμο κείμενο, χρησιμοποιεί OCR.
    """
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            first_page = reader.pages[0]
            text = first_page.extract_text() if first_page.extract_text() else ""
    except Exception as e:
        print(f"Σφάλμα ανάγνωσης με PyPDF2 στο {pdf_path}: {e}")
    
    if not text.strip():
        print(f"OCR για: {pdf_path}")
        try:
            images = convert_from_path(pdf_path, first_page=1, last_page=1, poppler_path=poppler_path)
            for img in images:
                text += pytesseract.image_to_string(img, lang='ell')
        except Exception as e:
            print(f"Σφάλμα OCR στο {pdf_path}: {e}")
    
    return text

def extract_first_half(text):
    """
    Διαιρεί το κείμενο σε γραμμές και παίρνει το πρώτο μισό.
    Επιστρέφει το υποσύνολο των γραμμών ως ενιαίο κείμενο.
    """
    lines = text.splitlines()
    if not lines:
        return ""
    end_index = max(1, len(lines) // 2)
    return "\n".join(lines[:end_index])

def process_folder(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                try:
                    text = extract_text_from_pdf(pdf_path)
                    extracted_text = extract_first_half(text)
                    
                    # Έλεγχος για παράνομους χαρακτήρες
                    if illegal_characters_re.search(extracted_text):
                        print(f"Παράλειψη αρχείου λόγω παράνομων χαρακτήρων: {pdf_path}")
                        continue

                    relative_path = os.path.relpath(pdf_path, folder_path)
                    data.append([relative_path, extracted_text])
                    print(f"Επεξεργάστηκε: {relative_path}")
                
                except Exception as e:
                    print(f"Παράλειψη αρχείου {pdf_path} λόγω σφάλματος: {e}")
                    continue
    
    df = pd.DataFrame(data, columns=["Αρχική Διαδρομή", "Εξαγόμενο Κείμενο"])
    excel_path = os.path.join(folder_path, "results.xlsx")
    df.to_excel(excel_path, index=False)
    print(f"Αποθηκεύτηκε το Excel: {excel_path}")

# Ορισμός του φακέλου (τροποποίησε το path αν χρειάζεται)
folder_path = r"C:\Users\dee\Desktop\ΑΡΧΕΙΟΘΕΤΗΣΗ"
process_folder(folder_path)
