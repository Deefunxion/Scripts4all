import os
import fitz  # PyMuPDF για PDF
import docx  # python-docx για Word
import subprocess  # Για μετατροπή .doc σε .txt με Neat Office

# Ρυθμίσεις φακέλων
input_folder = "C:\\Users\\dee\\Desktop\\LLM_txt"
output_folder = "C:\\Users\\dee\\Desktop\\LLM_txt_output"  # Όλα τα TXT αποθηκεύονται εδώ

# Δημιουργία του output folder αν δεν υπάρχει
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_pdf_to_txt(pdf_path, txt_path):
    """Μετατρέπει ένα PDF σε TXT"""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ PDF σε TXT: {pdf_path} → {txt_path}")
    except Exception as e:
        print(f"❌ Σφάλμα στο {pdf_path}: {e}")

def convert_word_to_txt(docx_path, txt_path):
    """Μετατρέπει ένα Word .docx σε TXT"""
    try:
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ DOCX σε TXT: {docx_path} → {txt_path}")
    except Exception as e:
        print(f"❌ Σφάλμα στο {docx_path}: {e}")

def convert_doc_to_txt(doc_path, txt_path):
    """Μετατρέπει ένα .doc σε .txt με απευθείας ανάγνωση"""
    try:
        with open(doc_path, "rb") as f:
            content = f.read()
        text = content.decode("utf-8", "ignore")  # Διαβάζουμε το περιεχόμενο και αγνοούμε λάθη
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ DOC σε TXT: {doc_path} → {txt_path}")
    except Exception as e:
        print(f"❌ Αποτυχία μετατροπής {doc_path}: {e}")

# Σάρωση όλων των φακέλων και αρχείων μέσα στο LLM_txt
for root, dirs, files in os.walk(input_folder):
    for file in files:
        file_path = os.path.join(root, file)

        # Δημιουργούμε το σωστό path για το TXT
        relative_path = os.path.relpath(file_path, input_folder)
        txt_path = os.path.join(output_folder, relative_path).replace(".pdf", ".txt").replace(".docx", ".txt").replace(".doc", ".txt")

        # Αν το TXT υπάρχει ήδη, παράλειψε τη μετατροπή
        if os.path.exists(txt_path):
            print(f"⚠️ Το TXT υπάρχει ήδη, παράλειψη: {txt_path}")
            continue

        # Βεβαιωνόμαστε ότι ο φάκελος προορισμού υπάρχει
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)

        if file.lower().endswith(".pdf"):
            convert_pdf_to_txt(file_path, txt_path)

        elif file.lower().endswith(".docx"):
            convert_word_to_txt(file_path, txt_path)

        elif file.lower().endswith(".doc"):
            convert_doc_to_txt(file_path, txt_path)

print("\n🎉 Όλα τα αρχεία μετατράπηκαν σε TXT!")
