import os
import shutil
import re
import nltk

# Λήψη stopwords για ελληνική γλώσσα
nltk.download("stopwords")
from nltk.corpus import stopwords

# Ρυθμίσεις διαδρομών
desktop_path = os.path.expanduser("~/Desktop/ΑΡΧΕΙΟΘΕΤΗΣΗ")  # Αλλάξτε το αν ο φάκελος είναι αλλού
sorted_folder = os.path.join(desktop_path, "Ταξινομημένα_Αρχεία")

# Ορισμός αρμοδιοτήτων και σχετικών λέξεων-κλειδιών
categories = {
    "Χορήγηση αδειών διενέργειας εράνων": ["έρανος", "λαχείο", "φιλανθρωπία", "δωρεά"],
    "Διαχείριση και κατανομή οικονομικών ενισχύσεων": ["επιδότηση", "επιχορήγηση", "ενίσχυση", "χρηματοδότηση"],
    "Έκδοση αδειών λειτουργίας περίθαλψης ηλικιωμένων": ["γηροκομείο", "περίθαλψη", "φροντίδα", "αναπηρία"],
    "Αδειοδότηση και εποπτεία ΚΔΑΠ και ΚΔΑΠ-ΜΕΑ": ["ΚΔΑΠ", "ΜΕΑ", "παιδιά", "ανάπτυξη"],
    "Αδειοδότηση και εποπτεία ΣΥΔ ΑμεΑ": ["αναπηρία", "υποστήριξη", "ΣΥΔ", "νοητική υστέρηση"],
    "Μητρώο Φορέων Κοινωνικής Πρόνοιας": ["μητρώο", "φορείς", "ιδρύματα", "εγγραφή"],
    "Διενέργεια κοινωνικών ερευνών": ["έρευνα", "κοινωνικές μελέτες", "στατιστικά"],
    "Υλοποίηση προγραμμάτων κοινωνικής πολιτικής": ["προγράμματα", "δράσεις", "ευρωπαϊκά κονδύλια"],
    "Υποστήριξη για προγράμματα αναδοχής και υιοθεσίας": ["υιοθεσία", "ανάδοχη", "παιδιά"],
    "Έλεγχος ιδρυμάτων κοινωνικής φροντίδας": ["έλεγχος", "ιδρύματα", "λειτουργία"],
    "Διασύνδεση κοινωνικών υπηρεσιών": ["διασύνδεση", "συντονισμός", "κοινωνικές υπηρεσίες"],
    "Διαχείριση κρίσεων και εκτάκτων αναγκών": ["κρίση", "επείγον", "ανθρωπιστική βοήθεια"],
    "Ανάπτυξη πολιτικών κοινωνικής συνοχής": ["πολιτική", "στρατηγική", "μελέτες"]
}

# Δημιουργία φακέλων αν δεν υπάρχουν
for category in categories.keys():
    category_path = os.path.join(sorted_folder, category)
    os.makedirs(category_path, exist_ok=True)

# Δημιουργία φακέλου "Άλλα" αν δεν υπάρχει
other_folder = os.path.join(sorted_folder, "Άλλα")
os.makedirs(other_folder, exist_ok=True)

# Συνάρτηση για την κατηγοριοποίηση αρχείων και φακέλων
def categorize_item(item_name):
    """ Κατηγοριοποιεί ένα αρχείο ή φάκελο με βάση το όνομά του """
    item_name_cleaned = re.sub(r"[^a-zA-Zα-ωΑ-Ω0-9 ]", " ", item_name.lower())
    item_words = set(item_name_cleaned.split())

    for category, keywords in categories.items():
        if any(word in item_words for word in keywords):
            return category
    return "Άλλα"

# Διαβάζουμε όλα τα αρχεία και τους φακέλους στον βασικό φάκελο
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)

    # Αν είναι φάκελος ή αρχείο, βρίσκουμε την κατηγορία του
    if os.path.isfile(item_path) or os.path.isdir(item_path):
        category = categorize_item(item)
        dest_folder = os.path.join(sorted_folder, category)

        try:
            shutil.move(item_path, os.path.join(dest_folder, item))
            print(f"✔ Μετακίνηση: {item} → {category}")
        except Exception as e:
            print(f"❌ Σφάλμα κατά τη μετακίνηση του {item}: {e}")

print("✅ Η ταξινόμηση ολοκληρώθηκε χωρίς χρήση API!")
