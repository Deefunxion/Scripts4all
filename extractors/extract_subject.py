import os
import re
import csv
import PyPDF2

# Βήμα 1: Ορίστε το μονοπάτι του φακέλου που περιέχει τα PDF αρχεία
folder_path = r"C:\Users\dee\Desktop\ΑΡΧΕΙΟΘΕΤΗΣΗ\PDFs"

# Βήμα 2: Ορισμός του μοτίβου (pattern) για να βρούμε το "ΘΕΜΑ:" και ό,τι έρχεται μετά
pattern = re.compile(r"ΘΕΜΑ:\s*(.+)")

results = []  # Εδώ θα αποθηκεύσουμε τα αποτελέσματα

# Βήμα 3: Διάσχιση όλων των PDF αρχείων στον φάκελο
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(folder_path, filename)
        text = ""
        # Άνοιγμα του PDF σε δυαδική λειτουργία
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            # Συγκέντρωση κειμένου από όλες τις σελίδες
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Έλεγχος αν η σελίδα επέστρεψε κείμενο
                    text += page_text + "\n"
        # Αναζήτηση για το "ΘΕΜΑ:" μέσα στο κείμενο
        match = pattern.search(text)
        if match:
            subject = match.group(1).strip()  # Παίρνει το κείμενο μετά το "ΘΕΜΑ:"
        else:
            subject = "Δεν βρέθηκε"
        results.append((filename, subject))

# Βήμα 4: Αποθήκευση των αποτελεσμάτων σε ένα αρχείο CSV (π.χ. "subjects.csv")
with open("subjects.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Όνομα Αρχείου", "ΘΕΜΑ"])
    writer.writerows(results)

print("Τα αποτελέσματα αποθηκεύτηκαν στο subjects.csv")
