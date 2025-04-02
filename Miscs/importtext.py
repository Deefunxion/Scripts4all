import PyPDF2
import pytesseract
from pdf2image import convert_from_path

# Ορισμός του Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ορισμός του poppler_path (βεβαιώσου ότι το path είναι σωστό)
poppler_path = r"C:\Users\dee\Release-24.08.0-0\poppler-24.08.0\Library\bin"

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
        images = convert_from_path(pdf_path, first_page=1, last_page=1, poppler_path=poppler_path)
        for img in images:
            text += pytesseract.image_to_string(img, lang='ell')
    return text

# Ορισμός διαδρομής για το αρχείο Ν.4837_2021.pdf
pdf_path = r"C:\Users\dee\Desktop\ΝΟΜΟΘΕΣΙΕΣ ΑΔΑ ΧΩΡΙΣ ΘΕΜΑ - Copy\1992-ΦΕΚ 125  Ν 2072 αρθ 10 ΚΑΑ.pdf"

extracted_text = extract_text_from_pdf(pdf_path)
print("=== Εξαγόμενο κείμενο από την πρώτη σελίδα ===")
print(extracted_text)
