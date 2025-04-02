import os
import json
import io
import pytesseract
import chardet
import subprocess
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from docx import Document

# 🔹 Ρύθμιση διαδρομών
input_folder = r"C:\Users\dee\Desktop\FINE-TUNING LLM TEXT FILES"
output_file = r"C:\Users\dee\Desktop\converted_data.json"

# OCR για PDF με εικόνες
def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)  # Πρώτη προσπάθεια με PDFMiner
    if not text.strip():  # Αν δεν βρήκε κείμενο, τρέχουμε OCR
        images = convert_from_path(pdf_path)
        text = "\n".join([pytesseract.image_to_string(img, lang="eng") for img in images])
    return text

# DOCX Extraction (Pandoc αν υπάρχει, αλλιώς python-docx)
def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        if not text.strip():
            text = subprocess.run(["pandoc", docx_path, "-t", "plain"], capture_output=True, text=True).stdout
    except:
        text = "⚠ Error reading DOCX file"
    return text

# TXT Encoding Detection
def extract_text_from_txt(txt_path):
    with open(txt_path, "rb") as f:
        raw_data = f.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
        if detected_encoding is None:
            detected_encoding = 'utf-8'
        return raw_data.decode(detected_encoding, errors="ignore")

# 🔹 Διαβάζουμε όλα τα αρχεία και τους υποφακέλους
json_data = []
for root, _, files in os.walk(input_folder):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_extension = os.path.splitext(filename)[1].lower()
        relative_path = os.path.relpath(file_path, input_folder)  # Αποθήκευση σχετικής διαδρομής

        try:
            if file_extension == ".pdf":
                text = extract_text_from_pdf(file_path)
            elif file_extension == ".docx":
                text = extract_text_from_docx(file_path)
            elif file_extension == ".txt":
                text = extract_text_from_txt(file_path)
            else:
                continue  # Αγνοούμε άγνωστα formats

            json_data.append({"path": relative_path, "filename": filename, "content": text})

        except Exception as e:
            json_data.append({"path": relative_path, "filename": filename, "content": f"⚠ Error processing file: {str(e)}"})

# 🔹 Αποθήκευση JSON στο Desktop
with open(output_file, "w", encoding="utf-8") as json_out:
    json.dump(json_data, json_out, ensure_ascii=False, indent=4)

print(f"✅ Μετατροπή ολοκληρώθηκε! Το JSON αρχείο αποθηκεύτηκε στο: {output_file}")
