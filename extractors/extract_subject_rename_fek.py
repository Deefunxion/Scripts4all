import os
import re
import PyPDF2
import csv
import shutil
import pytesseract
from pdf2image import convert_from_path

# Ορισμός του Tesseract – βεβαιώσου ότι το path είναι σωστό
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ορισμός του poppler_path
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

def is_fek(text):
    """
    Ελέγχει αν το εξαγόμενο κείμενο περιέχει τις υποαλυσίδες "ΕΦΗΜ" και "ΚΥΒ".
    Αυτό βοηθά να καλυφθούν και περιπτώσεις όπου το OCR έχει σφάλματα.
    """
    text_up = text.upper()
    return "ΕΦΗΜ" in text_up and "ΚΥΒ" in text_up

def get_from_teyxos(lines, start_index):
    """
    Από το παράθυρο που ξεκινάει στη γραμμή start_index και τις 2 επόμενες γραμμές,
    προσπαθεί να εξάγει:
      - Τον τύπο του Τεύχους (π.χ. "ΠΡΩΤΟ" ή "ΔΕΥΤΕΡΟ") μέσω του μοτίβου "ΤΕΥΧΟΣ <τύπος>".
      - Τον αριθμό του Φύλλου βάσει του μοτίβου "Αρ. Φύλλου <αριθμός>".
        Εξάγεται ο πλήρης αριθμός και κρατάμε μόνο τα πρώτα 1 έως 4 ψηφία.
      - Το 4ψήφιο έτος (με τιμή μεταξύ 1900 και 2025) που εμφανίζεται μέσα στο παράθυρο.
    Επιστρέφει (teyxos, fek_number, year) ή (None, None, None) αν δεν βρεθούν όλα.
    """
    teyxos = None
    fek_number = None
    year = None
    window = lines[start_index:min(start_index+3, len(lines))]
    for line in window:
        # Αναζήτηση τύπου Τεύχους, π.χ. "ΤΕΥΧΟΣ ΠΡΩΤΟ" ή "ΤΕΥΧΟΣ ΔΕΥΤΕΡΟ"
        match_teyxos = re.search(r'ΤΕΥΧΟΣ\s+(\S+)', line, re.IGNORECASE)
        if match_teyxos:
            teyxos = match_teyxos.group(1).upper()
        # Εξαγωγή του αριθμού μετά το "Αρ. Φύλλου"
        match_fek = re.search(r'Αρ\.?\s*Φύλλου\s*(\d+)', line, re.IGNORECASE)
        if match_fek:
            full_number = match_fek.group(1)
            fek_number = full_number[:4]  # κρατάμε μόνο τα πρώτα 1-4 ψηφία
        # Αναζήτηση για 4ψήφιο έτος
        match_year = re.search(r'\b(19\d{2}|20\d{2})\b', line)
        if match_year:
            candidate_year = int(match_year.group(1))
            if 1900 <= candidate_year <= 2025:
                year = str(candidate_year)
        if teyxos and fek_number and year:
            return teyxos, fek_number, year
    return teyxos, fek_number, year

def get_fek_number_and_year(text, filename):
    """
    Αναζητά σε όλες τις γραμμές το "ΤΕΥΧΟΣ" και, όταν το βρει, 
    καλεί τη get_from_teyxos για το αντίστοιχο παράθυρο.
    Αν δεν βρεθεί έτος στο κείμενο, ψάχνει στον τίτλο του αρχείου για έναν
    τετραψήφιο αριθμό (1900-2025) που να μην προηγείται από "Ν " ή "Ν. ".
    Επιστρέφει (teyxos, fek_number, year) ή (None, None, None) αν δεν βρεθούν όλα τα στοιχεία.
    """
    lines = text.splitlines()
    teyxos, fek_number, year = None, None, None
    for idx, line in enumerate(lines):
        if "ΤΕΥΧΟΣ" in line.upper():
            teyxos, fek_number, year = get_from_teyxos(lines, idx)
            if fek_number and year:
                return teyxos, fek_number, year
    # Αν δεν βρέθηκε έτος στο κείμενο, ψάξε στον τίτλο του αρχείου
    if not year:
        # Χρησιμοποιούμε δύο negative lookbehind για "Ν " (2 χαρακτήρες) και "Ν. " (3 χαρακτήρες)
        pattern = r'(?<!Ν\s)(?<!Ν\.\s)(\b(19\d{2}|20\d{2})\b)'
        matches = re.findall(pattern, filename, re.IGNORECASE)
        if matches:
            for match in matches:
                candidate_year = int(match[0])
                if 1900 <= candidate_year <= 2025:
                    year = str(candidate_year)
                    break
    return teyxos, fek_number, year

def rename_pdf_files(folder_path):
    """
    Διατρέχει όλα τα PDF στον καθορισμένο φάκελο:
      - Εξάγει το κείμενο της πρώτης σελίδας.
      - Ελέγχει αν το κείμενο περιέχει τις υποαλυσίδες "ΕΦΗΜ" και "ΚΥΒ".
      - Αναζητά σε όλο το κείμενο τη λέξη "ΤΕΥΧΟΣ" και από το αντίστοιχο παράθυρο εξάγει:
            τον τύπο του Τεύχους, τον αριθμό του ΦΕΚ (τα πρώτα 1-4 ψηφία)
            και το 4ψήφιο έτος (μέσα στο διάστημα 1900-2025).
      - Αν δεν βρεθεί έτος στο κείμενο, ψάχνει στον τίτλο του αρχείου για ένα έτος.
      - Αν βρεθούν όλα τα δεδομένα, μετονομάζει το αρχείο στον ίδιο φάκελο με το πρότυπο:
            "ΦΕΚ Α' [αριθμός]-[έτος]_[παλιό όνομα]" για τύπο "ΠΡΩΤΟ",
         ή "ΦΕΚ Β' [αριθμός]-[έτος]_[παλιό όνομα]" για τύπο "ΔΕΥΤΕΡΟ".
      - Αν δεν βρεθούν όλα τα στοιχεία, το αρχείο παραμένει αμετάβλητο.
      - Δημιουργεί ένα CSV αρχείο με τα αποτελέσματα.
    """
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            if not is_fek(text):
                print(f"Παραλείφθηκε (Δεν είναι ΦΕΚ): {filename}")
                continue
            teyxos, fek_number, year = get_fek_number_and_year(text, filename)
            if not fek_number or not year:
                print(f"Παραλείφθηκε (Δεν βρέθηκε αριθμός ΦΕΚ ή έτος): {filename}")
                continue
            prefix = "ΦΕΚ Α'"
            if teyxos and "ΔΕΥΤΕΡ" in teyxos.upper():
                prefix = "ΦΕΚ Β'"
            new_filename = f"{prefix} {fek_number}-{year}_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            try:
                shutil.move(pdf_path, new_path)
                results.append([filename, new_filename])
                print(f"Μετονομάστηκε: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Σφάλμα μετονομασίας {filename}: {e}")
    csv_path = os.path.join(folder_path, "results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Αρχικό Όνομα", "Νέο Όνομα"])
        writer.writerows(results)
    print("Ολοκληρώθηκε η επεξεργασία! Δες το", csv_path, "για λεπτομέρειες.")

# Ορισμός του φακέλου
folder_path = r"C:\Users\dee\Desktop\PDFs"
rename_pdf_files(folder_path)
