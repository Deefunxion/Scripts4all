import os
import re

# Ρύθμιση του φακέλου όπου βρίσκονται τα ήδη κατεβασμένα ΦΕΚ.
# Αντικατέστησε τις παρακάτω διαδρομές με τις δικές σου.
BASE_FOLDER = r"path/to/your/requests"

# Το TXT αρχείο που περιέχει τις δομές και τα ΦΕΚ.
TXT_FILE = r"path/to/your/requests/legislation.txt"

def read_legislation_file(file_path):
    """
    Διαβάζει το αρχείο κειμένου και εξάγει τα ΦΕΚ ανά δομή.
    Οι γραμμές που δεν περιέχουν το μοτίβο "ΦΕΚ" θεωρούνται ως ονομασίες δομών.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    fek_data = {}
    current_structure = None

    for line in lines:
        line = line.strip()
        # Εάν η γραμμή δεν περιέχει "ΦΕΚ" θεωρείται ονομασία δομής.
        if line and not re.search(r"ΦΕΚ\s*\d+", line, re.IGNORECASE):
            current_structure = line
            fek_data[current_structure] = []
        # Αναζήτηση του μοτίβου Φ.Ε.Κ. <αριθμός>/Τ.<Τεύχος>/<Έτος>
        elif re.search(r"Φ\.Ε\.Κ\.\s*(\d+)/Τ\.(Α|Β|Γ)΄?/(\d{4})", line, re.IGNORECASE):
            match = re.search(r"Φ\.Ε\.Κ\.\s*(\d+)/Τ\.(Α|Β|Γ)΄?/(\d{4})", line, re.IGNORECASE)
            fek_number, fek_issue, fek_year = match.groups()
            if current_structure:
                fek_data[current_structure].append({
                    "number": fek_number,
                    "issue": fek_issue,
                    "year": fek_year
                })

    return fek_data

def rename_fek_files(base_folder, fek_data):
    """
    Για κάθε δομή, ψάχνει στον αντίστοιχο φάκελο τα PDF αρχεία (με αρχικό "FEK_") 
    και μετονομάζει το πρώτο που βρίσκει σύμφωνα με τα στοιχεία του ΦΕΚ.
    """
    for structure, fek_list in fek_data.items():
        folder_path = os.path.join(base_folder, structure)

        if not os.path.exists(folder_path):
            print(f"⚠ Δεν βρέθηκε φάκελος για τη Δομή: {structure}")
            continue

        print(f"\n📂 Επεξεργασία φακέλου: {structure}")
        files = os.listdir(folder_path)

        for fek in fek_list:
            fek_number = fek["number"]
            fek_issue = fek["issue"]
            fek_year = fek["year"]

            # Εύρεση του PDF αρχείου που αντιστοιχεί σε αυτό το ΦΕΚ
            matching_files = [f for f in files if f.startswith("FEK_") and f.endswith(".pdf")]

            if not matching_files:
                print(f"❌ Δεν βρέθηκε αρχείο για ΦΕΚ {fek_number}/Τ.{fek_issue}΄/{fek_year} στη δομή {structure}")
                continue

            # Παίρνουμε το πρώτο διαθέσιμο αρχείο και το μετονομάζουμε
            old_filename = os.path.join(folder_path, matching_files[0])
            new_filename = os.path.join(folder_path, f"ΦΕΚ_{fek_number}_Τ.{fek_issue}_{fek_year}.pdf")

            try:
                os.rename(old_filename, new_filename)
                print(f"✅ Μετονομασία: {old_filename} → {new_filename}")
            except Exception as e:
                print(f"❌ Σφάλμα κατά τη μετονομασία του {old_filename}: {e}")

if __name__ == "__main__":
    fek_data = read_legislation_file(TXT_FILE)
    rename_fek_files(BASE_FOLDER, fek_data)

