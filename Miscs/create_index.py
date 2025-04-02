import json
import os

# 🔹 Φάκελος με τα καθαρισμένα JSON αρχεία
cleaned_folder = r"C:\Users\dee\Desktop\cleaned_json"
index_file = os.path.join(cleaned_folder, "index.json")

# 🔹 Δημιουργία index
index_data = []
for file in os.listdir(cleaned_folder):
    if file.startswith("cleaned_converted_part") and file.endswith(".json"):
        file_path = os.path.join(cleaned_folder, file)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        index_data.append({
            "filename": file,
            "total_records": len(data),
            "sample": data[:3]  # Προβολή των πρώτων 3 εγγραφών ως δείγμα
        })

# 🔹 Αποθήκευση index.json
with open(index_file, "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=4)

print(f"🎉 Το index δημιουργήθηκε: {index_file}")
