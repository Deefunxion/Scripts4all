import os
import re
import pandas as pd
import subprocess
from docx import Document

illegal_characters_re = re.compile(r'[\x00-\x08\x0B\x0C\x0E-\x1F]')

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_doc(doc_path):
    # Χρειάζεται το Antiword εγκατεστημένο και στο PATH
    try:
        result = subprocess.run(["antiword", doc_path], capture_output=True, text=True)
        text = result.stdout
        return text
    except Exception as e:
        print(f"Σφάλμα ανάγνωσης για {doc_path}: {e}")
        return ""

def extract_first_half(text):
    lines = text.splitlines()
    if not lines:
        return ""
    end_index = max(1, len(lines) // 2)
    return "\n".join(lines[:end_index])

def process_folder(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            ext = file.lower().split(".")[-1]
            
            # Αν είναι docx
            if ext == "docx":
                try:
                    text = extract_text_from_docx(filepath)
                    extracted_text = extract_first_half(text)
                    
                    if illegal_characters_re.search(extracted_text):
                        print(f"Παράλειψη αρχείου λόγω παράνομων χαρακτήρων: {filepath}")
                        continue

                    relpath = os.path.relpath(filepath, folder_path)
                    data.append([relpath, extracted_text])
                    print(f"Επεξεργάστηκε (docx): {relpath}")
                except Exception as e:
                    print(f"Παράλειψη αρχείου {filepath} λόγω σφάλματος: {e}")
            
            # Αν είναι doc
            elif ext == "doc":
                try:
                    text = extract_text_from_doc(filepath)
                    extracted_text = extract_first_half(text)
                    
                    if illegal_characters_re.search(extracted_text):
                        print(f"Παράλειψη αρχείου λόγω παράνομων χαρακτήρων: {filepath}")
                        continue

                    relpath = os.path.relpath(filepath, folder_path)
                    data.append([relpath, extracted_text])
                    print(f"Επεξεργάστηκε (doc): {relpath}")
                except Exception as e:
                    print(f"Παράλειψη αρχείου {filepath} λόγω σφάλματος: {e}")
            
            else:
                # Παράβλεψη άλλων τύπων αρχείων
                continue

    df = pd.DataFrame(data, columns=["Αρχική Διαδρομή", "Εξαγόμενο Κείμενο"])
    excel_path = os.path.join(folder_path, "results_doc_docx.xlsx")
    df.to_excel(excel_path, index=False)
    print(f"Αποθηκεύτηκε το Excel: {excel_path}")

if __name__ == "__main__":
    folder_path = r"C:\Users\dee\Desktop\ΑΡΧΕΙΟΘΕΤΗΣΗ\WORDS"
    process_folder(folder_path)
