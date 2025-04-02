import os
import shutil
import re
import docx
import PyPDF2
import pandas as pd
import openpyxl
import pdfplumber

# Ρυθμίσεις διαδρομών
desktop_path = os.path.expanduser("~/Desktop/ΑΡΧΕΙΟΘΕΤΗΣΗ")  # Αρχικός φάκελος
sorted_folder = os.path.join(desktop_path, "Ταξινομημένα_Αρχεία")

# Ορισμός αρμοδιοτήτων και σχετικών λέξεων-κλειδιών
categories = {
    "Χορήγηση αδειών διενέργειας εράνων": ["έρανος", "λαχείο", "φιλανθρωπία", "δωρεά"],
    "Διαχείριση και κατανομή οικονομικών ενισχύσεων": ["επιδότηση", "επιχορήγηση", "ενίσχυση", "χρηματοδότηση"],
    "Έκδοση αδειών λειτουργίας περίθαλψης ηλικιωμένων": ["γηροκομείο", "περίθαλψη", "φροντίδα", "αναπηρία", "ΜΦΗ"],
    "Αδειοδότηση και εποπτεία ΚΔΑΠ και ΚΔΑΠ-ΜΕΑ": ["ΚΔΑΠ", "ΜΕΑ", "παιδιά", "ανάπτυξη"],
    "Αδειοδότηση και εποπτεία ΣΥΔ ΑμεΑ": ["αναπηρία", "υποστήριξη", "ΣΥΔ", "νοητική υστέρηση"],
    "Μητρώο Φορέων Κοινωνικής Πρόνοιας": ["μητρώο", "φορείς", "ιδρύματα", "εγγραφή"],
    "Διενέργεια κοινωνικών ερευνών": ["έρευνα", "κοινωνικές μελέτες", "στατιστικά"],
    "Υλοποίηση προγραμμάτων κοινωνικής πολιτικής": ["προγράμματα", "δράσεις", "ευρωπαϊκά κονδύλια"],
    "Υποστήριξη για προγράμματα αναδοχής και υιοθεσίας": ["υιοθεσία", "ανάδοχη", "παιδιά"],
    "Έλεγχος ιδρυμάτων κοινωνικής φροντίδας": ["έλεγχος", "ιδρύματα", "λειτουργία"],
    "Διασύνδεση κοινωνικών υπηρεσιών": ["διασύνδεση", "συντονισμός", "κοινωνικές υπηρεσίες"],
    "Διαχείριση κρίσεων και εκτάκτων αναγκών": ["κρίση", "επείγον", "ανθρωπιστική βοήθεια"],
    "Ανάπτυξη πολιτικών κοινωνικής συνοχής": ["πολιτική", "στρατηγική", "μελέτες"],
    "Νομοθεσίες και ΦΕΚ": ["νόμος", "νομοθεσία", "ΦΕΚ", "κανονισμός"]
}

# **Δημιουργία φακέλων αν δεν υπάρχουν**
if not os.path.exists(sorted_folder):
    os.makedirs(sorted_folder)

for category in categories.keys():
    category_path = os.path.join(sorted_folder, category)
    os.makedirs(category_path, exist_ok=True)

# **Δημιουργία φακέλου "Άλλα"**
other_folder = os.path.join(sorted_folder, "Άλλα")
os.makedirs(other_folder, exist_ok=True)

# **Συνάρτηση για την ανάγνωση αρχείων**
def extract_text_from_file(file_path):
    """Ανάγνωση κειμένου από PDF, DOCX, TXT και XLSX αρχεία"""
    text = ""
    try:
        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = pdfplumber.open(f)
                for page in reader.pages:
                    text += page.extract_text() + " "
        elif file_path.endswith(".docx"):
            doc = docx.Document(file_path)
            text = " ".join([p.text for p in doc.paragraphs])
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine="openpyxl")
            text = " ".join(df.astype(str).values.flatten())
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
    except Exception as e:
        print(f"❌ Δεν μπόρεσε να διαβαστεί το αρχείο {file_path}: {e}")
    return text.lower()

# **Συνάρτηση για την κατηγοριοποίηση αρχείων**
def categorize_content(text_content):
    """Κατηγοριοποιεί ένα αρχείο με βάση το κείμενό του"""
    for category, keywords in categories.items():
        if any(word in text_content for word in keywords):
            return category
    return "Άλλα"

# **Έλεγχος και μετακίνηση αρχείων**
for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)

    if os.path.isfile(file_path):
        text_content = extract_text_from_file(file_path)
        category = categorize_content(text_content)
        dest_folder = os.path.join(sorted_folder, category)

        try:
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"✔ Μετακίνηση: {file} → {category}")
        except Exception as e:
            print(f"❌ Σφάλμα κατά τη μετακίνηση του {file}: {e}")

print("✅ Η ταξινόμηση ολοκληρώθηκε! Όλα τα αρχεία διαβάστηκαν και ταξινομήθηκαν σωστά.")
