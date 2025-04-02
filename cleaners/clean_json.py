import json
import os
import re

# 🔹 Ρύθμιση αρχείων
input_folder = r"C:\Users\dee\Desktop"  # Εκεί που αποθηκεύτηκαν τα JSON
output_folder = r"C:\Users\dee\Desktop\cleaned_json"  # Νέος φάκελος για καθαρά JSON
os.makedirs(output_folder, exist_ok=True)

# 🔹 Καθαρισμός κειμένου: Αφαίρεση περιττών κενών, άσχετων συμβόλων
def clean_text(text):
    if not text or not isinstance(text, str):
        return ""  # Αν το κείμενο είναι άδειο ή None, επιστρέφουμε κενό

    text = re.sub(r"\n{2,}", "\n", text)  # Αφαίρεση πολλών κενών γραμμών
    text = re.sub(r"[^\w\s,.!?-]", "", text)  # Αφαίρεση ασυνήθιστων συμβόλων (OCR noise)
    text = text.strip()  # Αφαίρεση κενών από την αρχή και το τέλος
    return text

# 🔹 Διαβάζουμε και καθαρίζουμε τα JSON αρχεία
for file in os.listdir(input_folder):
    if file.startswith("converted_part") and file.endswith(".json"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, f"cleaned_{file}")

        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        cleaned_data = []
        for entry in data:
            cleaned_text = clean_text(entry.get("content", ""))
            if cleaned_text:  # Προσθέτουμε την εγγραφή μόνο αν δεν είναι κενή
                entry["content"] = cleaned_text
                cleaned_data.append(entry)

        # 🔹 Αποθήκευση καθαρισμένου JSON
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

        print(f"✅ Καθαρίστηκε και αποθηκεύτηκε: {output_path}")

print("🎉 Ο καθαρισμός ολοκληρώθηκε! Τα καθαρά JSON αρχεία είναι στον φάκελο 'cleaned_json'.")
