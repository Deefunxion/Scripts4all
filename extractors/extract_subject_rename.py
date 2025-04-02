import os
import re
import csv
import PyPDF2
from pdf2image import convert_from_path
import pytesseract

# === 1) Ρύθμιση διαδρομής Tesseract (αν δεν είναι ήδη στο PATH) ===
# Προσαρμόστε τη διαδρομή αν χρειάζεται (π.χ. αν το έχεις σε άλλο φάκελο)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def clean_filename(text):
    """
    Αντικαθιστά τους μη επιτρεπόμενους χαρακτήρες με "_".
    """
    forbidden_chars = r'<>:"/\|?*'
    for ch in forbidden_chars:
        text = text.replace(ch, "_")
    return text

# === 2) Ορισμός φακέλου με τα PDF αρχεία ===
folder_path = r"C:\Users\dee\Desktop\ΝΟΜΟΘΕΣΙΕΣ ΑΔΑ ΧΩΡΙΣ ΘΕΜΑ - Copy"

# === 3) Regex: non-greedy match, σταματάει στο πρώτο newline ή στο τέλος ===
pattern = re.compile(r"[Θθ][Εέ]ΜΑ:\s*(.+?)(?:\n|$)", re.IGNORECASE | re.DOTALL)

results = []

# === 4) Διάσχιση όλων των PDF αρχείων στον φάκελο ===
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(folder_path, filename)
        text = ""
        # --- 4.1 Προσπάθεια εξαγωγής κειμένου με PyPDF2 ---
        try:
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"Σφάλμα PyPDF2 στο {filename}: {e}")
        
        # --- 4.2 Αν δεν βρέθηκε κείμενο, μάλλον σκαναρισμένο PDF -> OCR ---
        if not text.strip():
            print(f"Το αρχείο {filename} φαίνεται να είναι σκαναρισμένο, τρέχουμε OCR.")
            try:
                # Προσαρμόστε τη διαδρομή στο poppler_path εάν το έχεις αλλού
                images = convert_from_path(
                    filepath,
                    poppler_path=r"C:\Users\dee\Release-24.08.0-0\poppler-24.08.0\Library\bin"
                )
                for img in images:
                    text += pytesseract.image_to_string(img, lang='ell') + "\n"
            except Exception as e:
                print(f"Σφάλμα OCR στο {filename}: {e}")

        # --- 4.3 Αναζήτηση για το "ΘΕΜΑ:" στο εξαγόμενο κείμενο ---
        match = pattern.search(text)
        if match:
            subject = match.group(1).strip()
        else:
            subject = "Δεν_βρέθηκε"
        safe_subject = clean_filename(subject)
        results.append((filename, safe_subject))
        print(f"Αρχείο: {filename} | Θέμα: {subject}")
        
        # --- 4.4 Δημιουργία νέου ονόματος & μετονομασία ---
        new_filename = f"{safe_subject}_{filename}"
        new_filepath = os.path.join(folder_path, new_filename)
        try:
            os.rename(filepath, new_filepath)
            print(f"Μετονομάστηκε: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Σφάλμα μετονομασίας για το {filename}: {e}")

# === 5) Αποθήκευση των αποτελεσμάτων σε CSV ===
with open("subjects.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Όνομα Αρχείου", "ΘΕΜΑ"])
    writer.writerows(results)

print("Τα αποτελέσματα αποθηκεύτηκαν στο subjects.csv")
