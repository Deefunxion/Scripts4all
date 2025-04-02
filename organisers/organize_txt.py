import os
import re
from collections import defaultdict

def categorize_text(text):
    """Αναγνωρίζει τη θεματική κατηγορία ενός κειμένου με βάση λέξεις-κλειδιά."""
    categories = {
        "Δημόσια Διοίκηση": ["Ν. 2690/1999", "διοικητική διαδικασία", "διοίκηση"],
        "Προμήθειες & Συμβάσεις": ["Ν. 4412/2016", "σύμβαση", "ανάθεση"],
        "Δημοσιονομικά & Λογιστικά": ["κρατικός προϋπολογισμός", "λογιστική", "έλεγχος δαπανών"],
        "Κοινωνική Πολιτική": ["επίδομα", "πρόνοια", "ΑμεΑ"],
        "Προσωπικό & Υπαλληλικός Κώδικας": ["Ν. 3528/2007", "υπάλληλος", "πειθαρχικό"],
        "Τροποποιήσεις Νομοθεσίας": ["τροποποίηση", "ΦΕΚ", "νόμος"],
    }
    
    for category, keywords in categories.items():
        if any(re.search(keyword, text, re.IGNORECASE) for keyword in keywords):
            return category
    
    return "Άλλο"

def split_large_files(folder_path, max_files=15):
    """Σπάει μεγάλα αρχεία σε μικρότερα, ώστε να μην ξεπερνούν το όριο των 15 αρχείων."""
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            chunks = [content[i:i + len(content) // max_files] for i in range(0, len(content), len(content) // max_files)]
            
            for idx, chunk in enumerate(chunks):
                new_filename = f"{filename.replace('.txt', '')}_{idx+1}.txt"
                with open(os.path.join(folder_path, new_filename), "w", encoding="utf-8") as new_file:
                    new_file.write(chunk)
        os.remove(file_path)  # Διαγραφή του αρχικού μεγάλου αρχείου

def organize_files(folder_path):
    """Διαβάζει όλα τα TXT αρχεία του φακέλου, οργανώνει τις πληροφορίες και αποθηκεύει νέα αρχεία."""
    categorized_data = defaultdict(str)
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                text = file.read()
                category = categorize_text(text)
                categorized_data[category] += f"\n=== {filename} ===\n{text}\n"
    
    output_folder = os.path.join(folder_path, "organized")
    os.makedirs(output_folder, exist_ok=True)
    
    for category, content in categorized_data.items():
        with open(os.path.join(output_folder, f"{category}.txt"), "w", encoding="utf-8") as out_file:
            out_file.write(content)
    
    print("Ολοκληρώθηκε η οργάνωση των αρχείων!")
    split_large_files(output_folder, max_files=15)

# Παράδειγμα χρήσης
folder_path = r"C:\Users\dee\Desktop\organize_txt\organized"
organize_files(folder_path)
